# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NguyenSonTung
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-NguyenSonTung-2A202603658-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyen Son Tung | 2A202603658 | Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý | Có |
|   2 |           |      |     |             |
|   3 |           |      |     |             |
|   4 |           |      |     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenSonTung-2A202603658

### Phần việc phụ trách

Kỹ sư cổng và chuẩn bị hồ sơ A/B/C; `lab10/guards.py`, `lab10/monitors.py`, `config/operating_gates.json`, các phiếu và submission. AI hỗ trợ đọc repo, soạn code và nội dung; người học cần tự rà soát và giải thích ở demo.

### Đóng góp cụ thể

Đặt cổng kiểm tra refund theo policy/tracking; thêm đối chiếu ghi lỗi theo parcel, xử lý đơn nhiều kiện mơ hồ, áp trần lỗi/hãng/ngày, thêm monitor `carrier_fault_misattribution_rate`; giới hạn pilot HN/HCM và 10% kiểm mẫu.

### Bằng chứng

Commit ký tiêu chí `1579f6e`; checkpoint `93fdfbf6`; baseline `R-base-before-20261118-171328-bde05c`; grade S6 `R-S6-grade-20261118-171805-66e7a6`; kiểm hồi quy `R-base-after-20261118-171805-66e7a6`.

### Exit ticket

Học được là lỗi ở đơn nhiều kiện phải được kiểm ở write boundary theo parcel, không thể suy từ số tổng của đơn. Chưa chắc tracking production có độ chính xác/độ trễ đủ để làm nguồn thật; cần đối soát độc lập trước mở rộng.
