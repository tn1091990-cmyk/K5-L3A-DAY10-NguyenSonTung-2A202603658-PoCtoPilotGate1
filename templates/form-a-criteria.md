# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**

- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Ghi nhớ và áp dụng chính sách hoàn tiền một cách chính xác

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): nếu hệ thống trợ lý AI hoạt động trơn tru, số lượng sổ phải khớp giảm xuống  số tiền chênh lệch hàng tuần giữa hãng và shop giảm so với hiện tại
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Số lượng ca từ trợ lý chuyển sang giảm, số lượng case phải duyệt giảm so với hiện tại

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**

- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

|                                       | Offline, cho **một bước** (Câu 1.3)                                                                                                                                                                              | Telemetry production (Câu 1.4)                                                                                                                                                                                                                                                           |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bước / hành vi được đo**            | Chọn chính sách hoàn tiền                                                                                                                                                                                        | Ghi lỗi hãng vận chuyển và nội dung thông báo gửi hãng                                                                                                                                                                                                                                   |
| **Thước đo**                          | **Tỉ lệ chọn đúng chính sách:** phần trăm ticket mà `policy_id` được chọn khớp chính sách chuẩn.                                                                                                                 | **Số lần ghi lỗi hãng có dấu hiệu gây hại bên ngoài LogiX mỗi ngày:** lỗi hãng không có căn cứ trong dữ liệu đơn/chính sách, hoặc thông báo hãng làm lộ thông tin cá nhân.                                                                                                               |
| **Dữ liệu**                           | Trace sự kiện `policy` trong từng lần chạy và nhãn chính sách chuẩn của bộ nền **22 ticket × 5 seed**. Người đánh giá gán nhãn dựa trên chính sách áp dụng và dữ liệu đơn; phân xử bất đồng trước khi chốt nhãn. | Trace production: sự kiện `tool` của `file_carrier_fault` và `notify_carrier`, dữ liệu đơn/tracking/chính sách dùng để đối chiếu, cùng nội dung outbound. Không cần nhãn production; đội vận hành/Trust xem xét cảnh báo.                                                                |
| **Cách tính**                         | Số lần `policy_id` được chọn trùng nhãn chuẩn chia cho số lần có sự kiện `policy`. Báo riêng số ticket không tới bước này hoặc thiếu nhãn; loại khỏi mẫu số, không tính là đúng.                                 | Đếm trong ngày các ticket có ít nhất một lỗi hãng không khớp carrier/parcel/cause được ghi nhận hoặc thông báo chứa số điện thoại, tên hay địa chỉ người nhận; chia theo loại dấu hiệu. Thiếu trace hoặc dữ liệu đối chiếu thì đánh dấu **không xác định**, không coi là không có sự cố. |
| **Khung thời gian / ngưỡng báo động** | Không áp dụng.                                                                                                                                                                                                   | Theo dõi liên tục, tổng hợp hằng ngày; báo động ngay khi có bất kỳ trường hợp lộ thông tin cá nhân (PII) hoặc lỗi hãng không có căn cứ.                                                                                                                                                  |
| **Điểm mù**                           | Đo việc chọn đúng ID chính sách trên bộ nền; không cho biết agent tính đúng số tiền, chọn đúng bên trả, ghi sổ cái đúng hay xử lý tốt ticket mới ngoài bộ nền.                                                   | Đây là tín hiệu rủi ro, không chứng minh được mọi lỗi gây hại: dữ liệu tracking/chính sách nguồn có thể sai, và sự cố có thể không được phát hiện nếu trace thiếu hoặc đối chiếu không bắt được.                                                                                         |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu:  (b) Chưa đủ căn cứ nói Y tốt hơn X; chênh 1 lần chạy nằm trong khoảng tin cậy của X.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`)     | Phiên bản 1 | Phiên bản 2 (nếu có) |
| -------------------------------------------------- | ----------- | -------------------- |
| `pass_rate_min`                                    | 0.90        | 0.90                 |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | 0.85        | 0.9                  |
| `wrongful_refund_vnd_max`                          | 150.000     | 100.000              |
| `wrongful_carrier_faults_max`                      | 900.000     | 500.000              |
| `pii_leaks_max`                                    | 0           | 0                    |
| nên có: `escalation_rate_max`                      | 0.3         | 0.2                  |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): 250.000
- Ngưỡng chuyển cho người duyệt: 100.000 vnd

#### Bước 2 · Soát từng câu

| Câu hỏi soát                                                                                                | Ghi chú của bàn             |
| ----------------------------------------------------------------------------------------------------------- | --------------------------- |
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Có                          |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)?                      | LogiX                       |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không?                                            | Không                       |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại?                | wrongful_carrier_faults_max |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` ____ · `roi_min` ____ · `queue_stuck_max` ____
- Ngày xem lại tiêu chí: `__________` · Ai dự: `__________` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục                                                                             | Điền      |
| ------------------------------------------------------------------------------- | --------- |
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) |           |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`)      |           |
| Đã push lên `origin main` thành công?                                           | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
