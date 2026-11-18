# Tự kiểm tra sự cố S6 · FAIL

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S6-grade-20261118-171805-66e7a6` · bàn: `NguyenSonTung` · grader `lab10-1.0` · 0.303s
- Ba mốc: base `R-S6-before-20261118-171805-66e7a6` · prepared `R-S6-prepared-20261118-171805-66e7a6` · after `R-S6-after-20261118-171805-66e7a6` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `93fdfbf6`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `66e7a6d7e50a`
- Hash Bản tiêu chí chấp nhận: `c807fd79c5c0` · đã ký: `c807fd79c5c0` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S6` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: (trống) · chưa ghi (ghi đúng số đã bốc vào dòng `Thẻ đã bốc:` ở đầu `templates/form-c-incident.md`)

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ❌ | file khoá bị đổi: ['incidents/S1/card.json', 'incidents/S1/card.md', 'incidents/S1/tickets.jsonl', 'incidents/S1/world_patch.json', 'incidents/S2/card.json', 'incidents/S2/card.md', 'incidents/S2/tickets.jsonl', 'incidents/S2/world_patch.json', 'incidents/S3/card.json', 'incidents/S3/card.md', 'incidents/S3/tickets.jsonl', 'incidents/S3/world_patch.json', 'incidents/S4/card.json', 'incidents/S4/card.md', 'incidents/S4/tickets.jsonl', 'incidents/S4/world_patch.json', 'incidents/S5/card.json', 'incidents/S5/card.md', 'incidents/S5/tickets.jsonl', 'incidents/S5/world_patch.json', 'incidents/S7/card.json', 'incidents/S7/card.md', 'incidents/S7/tickets.jsonl', 'incidents/S7/world_patch.json', 'incidents/S8/card.json', 'incidents/S8/card.md', 'incidents/S8/tickets.jsonl', 'incidents/S8/world_patch.json'] |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ✅ | base có vấn đề: True; after sạch: True; ticket còn hỏng: không; trần còn vượt: không |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['carrier_fault_misattribution_rate']; sáng đèn: [('carrier_fault_misattribution_rate', 'before', 0.017857, 0.416667)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.0 | 0.0 | 0.375 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 3162 · 10000 | 3262 · 10000 | 7372 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 667 · 1500 | 767 · 1500 | 767 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 28061 | 26861 | 21023 |
| ROI | 0.74 | 0.69 | 0.36 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 96000 · 2000000 | 96000 · 2000000 | 38000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 54000 · 2000000 | 54000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 0.6667 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 40 | 25 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 0.5; hoàn sai 0; oan 5; PII 0; chi phí 659đ | pass 0.5; hoàn sai 0; oan 5; PII 0; chi phí 759đ | — |
| kho DN | pass 0.0; hoàn sai 0; oan 10; PII 0; chi phí 663đ | pass 0.0; hoàn sai 0; oan 5; PII 0; chi phí 763đ | — |
| kho HCM | pass 0.25; hoàn sai 270000; oan 15; PII 0; chi phí 661đ | pass 0.25; hoàn sai 270000; oan 10; PII 0; chi phí 761đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 5481đ |
| kho HN | pass 0.5; hoàn sai 0; oan 10; PII 0; chi phí 663đ | pass 0.5; hoàn sai 0; oan 5; PII 0; chi phí 763đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1763đ |
| hãng DNB | pass 0.0; hoàn sai 140000; oan 10; PII 0 | pass 0.0; hoàn sai 140000; oan 5; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng GHSH | pass 0.3333; hoàn sai 130000; oan 30; PII 0 | pass 0.3333; hoàn sai 130000; oan 20; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | — |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.2273 | 0.3077 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 0 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 4275 · 10000 | 5550 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 770 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 121942 | 57853 |
| ROI | 1.34 | 1.3 | 0.8 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 20000 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 1.0 | 0.5909 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 1 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 665đ | — |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4646đ | — |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2651đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3447đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | — |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | — |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- Không vượt trần kinh doanh / vận hành nào.
- Mọi ngưỡng đã ký đều đạt.
- Được phép cân nhắc 'Tiếp tục'.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 0.9909 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 0.9545 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 20000 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 1 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.2273 | 0.2308 | +0.0035 |
| visible | pass_rate | 0.3333 | 0.3333 | 1.0 | +0.6667 |
| visible | pass_k | 0.3333 | 0.3333 | 1.0 | +0.6667 |
| visible | wrongful_refund_vnd | 270000 | 270000 | 0 | -270000 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 40 | 25 | 0 | -40 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 0 | 0 | 0 | +0 |
| visible | escalation_rate | 0.0 | 0.0 | 0.25 | +0.25 |
