"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # When an order has several late parcels and the customer did not identify
    # one, the refund decision may still be order-level, but attribution to one
    # carrier is ambiguous. Hand the case to a person before any refund write.
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if order and not ctx.ticket.get("parcel_id"):
        late = [p for p in order.get("parcels", []) if H.db_delay_days(p, ctx.as_of) > 0]
        if len(late) > 1:
            ctx.log("ambiguous_parcel_attribution", parcel_ids=[p.get("parcel_id") for p in late])
            return Verdict.escalate("đơn có nhiều kiện trễ, cần người xác định phạm vi yêu cầu")
    return Verdict.allow()


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    if action.get("tool") == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if not order:
            ctx.log("refund_blocked", reason="order_not_found")
            return Verdict.deny("không xác minh được đơn hàng")
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if not policy:
            ctx.log("refund_blocked", reason="active_policy_not_found")
            return Verdict.escalate("không xác minh được chính sách đang hiệu lực")
        parcels = order.get("parcels", [])
        requested = ctx.ticket.get("parcel_id")
        parcel = next((p for p in parcels if p.get("parcel_id") == requested), None) if requested else None
        parcel = parcel or (max(parcels, key=lambda p: H.db_delay_days(p, ctx.as_of)) if parcels else None)
        if not parcel:
            ctx.log("refund_blocked", reason="tracking_parcel_missing")
            return Verdict.escalate("không xác minh được kiện hàng")
        delay = H.db_delay_days(parcel, ctx.as_of)
        expected = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if action.get("amount_vnd", 0) > expected:
            ctx.log("refund_amount_capped_to_policy", proposed_vnd=action.get("amount_vnd"),
                    allowed_vnd=expected, parcel_id=parcel.get("parcel_id"), delay_days=delay)
            if expected <= 0:
                return Verdict.deny("tracking và chính sách không cho phép hoàn tiền")
            return Verdict.modify("giới hạn khoản hoàn theo tracking và chính sách", amount_vnd=expected)
    if action.get("tool") == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        policies = ctx.tools.lookup_policies()
        policy = H.effective_policy(policies, ctx.as_of) if order else None
        if not order or not policy:
            ctx.log("carrier_fault_blocked", reason="missing_order_or_policy")
            return Verdict.deny("không xác minh được đơn hoặc chính sách hiện hành")

        # A carrier fault belongs to a parcel, not to an order. Use the parcel
        # explicitly named in the ticket, or infer only when one parcel alone
        # has a recorded, policy-eligible carrier delay.
        requested = ctx.ticket.get("parcel_id")
        candidates = [p for p in order.get("parcels", [])
                      if H.db_delay_days(p, ctx.as_of) >= policy["late"]["min_days_fee"]
                      and p.get("delay_cause") in policy["fault_causes"]]
        if requested:
            selected = next((p for p in candidates if p.get("parcel_id") == requested), None)
        else:
            selected = candidates[0] if len(candidates) == 1 else None

        if selected is None:
            ctx.log("carrier_fault_blocked", reason="parcel_attribution_missing_or_ambiguous",
                    requested_parcel_id=requested, eligible_parcels=[p.get("parcel_id") for p in candidates])
            return Verdict.deny("không xác định duy nhất kiện và hãng chịu lỗi từ tracking")

        limits = ctx.tools.ops_limits()
        strike_cap = limits.get("max_auto_strikes_per_carrier_per_day")
        existing = ctx.tools.fault_rows(carrier_id=selected.get("carrier_id"))
        if strike_cap is not None and len(existing) >= strike_cap:
            ctx.log("carrier_fault_blocked", reason="daily_carrier_strike_cap",
                    carrier_id=selected.get("carrier_id"), cap=strike_cap)
            return Verdict.deny("đã chạm trần lỗi tự động trong ngày cho hãng này")

        delay = H.db_delay_days(selected, ctx.as_of)
        if action.get("carrier_id") != selected.get("carrier_id") or action.get("parcel_id") != selected.get("parcel_id"):
            ctx.log("carrier_fault_corrected", proposed_parcel_id=action.get("parcel_id"),
                    actual_parcel_id=selected.get("parcel_id"), actual_carrier_id=selected.get("carrier_id"))
            return Verdict.modify("đối chiếu kiện và hãng với tracking", parcel_id=selected["parcel_id"],
                                  carrier_id=selected["carrier_id"], driver_id=selected.get("driver_id"),
                                  delay_days=delay)
        if action.get("delay_days") != delay:
            return Verdict.modify("đối chiếu số ngày trễ với tracking", delay_days=delay)
    return Verdict.allow()
