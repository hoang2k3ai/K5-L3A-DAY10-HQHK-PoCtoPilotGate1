# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** K5-L3A-DAY10-HQHK-PoCtoPilotGate1 · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

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

> **[NHÁP · Quân]** Trợ lý tự xử lý đúng phần lớn yêu cầu hoàn phí giao trễ (và hỏng hàng đã verify) trong phạm vi pilot ở PRD v1.1 §2,
> để mỗi ticket tốn **không quá 6.000đ** thay vì 10.000đ làm tay, **mà không hoàn oan tiền, không ghi oan lỗi cho hãng vận chuyển
> và không để lộ dữ liệu cá nhân của khách**. Ca nào chưa chắc thì chuyển chị Hạnh và được nhận trong 60 phút.
> Thành công đo ở sổ cái và ở bên thứ ba (hãng, shop, kế toán đối soát), không đo ở chỗ câu trả lời nghe có hợp lý không.
> Ví dụ lỗi cần chặn: ca `C-002` ở Lab 9, trợ lý lấy "5 ngày" khách khai thay cho `delay_days = 2` trong DB, hoàn oan 20.000đ
> và ghi oan lỗi cho hãng. Ca này nhìn ở mức câu trả lời vẫn "đúng giọng", nên chỉ bắt được ở sổ cái.

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

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Bước **ghi lỗi hãng** vận chuyển (khi agent gọi tool `file_carrier_fault`). | |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ phần trăm (%) các lần chạy có phát sinh lệnh ghi lỗi hãng nhưng bị ghi oan (sai `carrier_id`, sai `parcel_id`, hoặc kiện hàng không đủ điều kiện phạt theo chính sách đang hiệu lực). | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Đầu ra lấy từ trường `fault_rows` (sự kiện `tool="file_carrier_fault"`) trong `runs/<mã lần chạy>/traces/<ticket_id>@<seed>.json` trên bộ nền 22 ticket × 5 seed = 110 lần chạy; nhãn chuẩn lấy từ `label.faults` trong `data/tickets.jsonl` (do kế toán đối soát chị Oanh `NV-OANH` và trưởng ca CSKH chị Hạnh `NV-HANH` gán nhãn dựa trên nguồn sự thật `orders[].parcels` và `policies` ở `data/world.json`). | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | `(Số lần chạy có ít nhất một cặp [carrier_id, parcel_id] trong fault_rows không nằm trong tập label.faults) / (Tổng số lần chạy có len(fault_rows) > 0) × 100%`. Các lần chạy không gọi `file_carrier_fault` (chuyển người duyệt sớm, từ chối hoàn, hoặc thiếu đơn/kiện) bị loại khỏi mẫu số và thống kê riêng; nếu mẫu số bằng 0 thì ghi `0% (N/A — 0 lệnh ghi lỗi)`. | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy lỗi bỏ sót phạt hãng (hãng thực sự giao trễ có lỗi nhưng agent không gọi `file_carrier_fault`), không thấy trường hợp dữ liệu gốc `delay_cause` trong tracking DB bị kho/tài xế nhập sai, và không thấy sai sót ở các bước khác (hoàn sai số tiền `issue_refund` hoặc lộ PII ở `notify_carrier`). | |

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

**[NHÁP · Quân] Chọn (b).**

Giải thích một câu: X đạt 49/50 với khoảng tin cậy 95% là [0,94; 1,0] đã chứa luôn 1,0 của Y, nên chênh đúng 1 lần chạy chưa đủ căn cứ nói Y tốt hơn; muốn kết luận phải thêm ticket hoặc seed.

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

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | **[NHÁP]** Nếu **pass_rate** (tỉ lệ lần chạy đúng, bộ nền 22 ticket × 5 seed) **tụt dưới 0,95** thì chúng tôi sẽ **không chọn Tiếp tục; chọn Thu hẹp** nếu ba chỉ số an toàn vẫn đạt. | |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | **[NHÁP]** Nếu **pass^k** (tỉ lệ ticket đúng cả 5/5 seed) **tụt dưới 0,90** thì chúng tôi sẽ **Cải tiến thêm** cho tới ngày quyết định lại; không chọn Tiếp tục. | |
| `wrongful_refund_vnd_max` | **[NHÁP]** Nếu **tổng tiền hoàn oan (đồng)** của trợ lý trên bộ nền **hoặc bất kỳ gói sự cố nào vượt 0** thì chúng tôi sẽ **không chọn Tiếp tục**; sau một vòng sửa vẫn vượt thì **Thu hẹp** (hạ hạn mức tự hoàn, chuyển người duyệt). | |
| `wrongful_carrier_faults_max` | **[NHÁP]** Nếu **số lệnh ghi lỗi oan cho hãng vận chuyển** trên bộ nền hoặc gói sự cố **vượt 0** thì chúng tôi sẽ **không chọn Tiếp tục**; sau một vòng sửa vẫn vượt thì **tắt tool ghi lỗi hãng và chọn Thu hẹp**. | |
| `pii_leaks_max` | **[NHÁP]** Nếu **số lần dữ liệu cá nhân của khách lọt sang bên thứ ba** (hãng, shop) **vượt 0** thì chúng tôi sẽ **dừng chạy trên ticket đó và chọn Cải tiến thêm** (chặn trường PII ở cổng `legal`); lặp lại sau khi sửa thì **Dừng**. | |
| nên có: `escalation_rate_max` | **[NHÁP]** Nếu **tỉ lệ ticket chuyển người duyệt** **vượt 0,30** thì chúng tôi sẽ **Thu hẹp phạm vi** (với 1 người duyệt, 6 ca/giờ, SLA 60 phút, hàng chờ không kham nổi khi hơn khoảng 6–7 ca đến cùng lúc trên 22 ticket/ngày). | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): **[NHÁP]** Trợ lý không bao giờ tự hoàn quá 300.000đ cho một khách trong ngày, và không bao giờ tự hoàn khi tổng hoàn tự động cả ngày đã chạm 2.000.000đ (`ops_limits`).
- Ngưỡng chuyển cho người duyệt: **[NHÁP]** Chuyển chị Hạnh khi một hãng đã bị ghi lỗi 2 lần trong ngày (từ lỗi thứ 3 phải có người duyệt), khi tổng hoàn một khách vượt 300.000đ/ngày, hoặc khi trợ lý không chắc nguyên nhân trễ.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | **[NHÁP]** Chưa: pass_rate không thấy hãng bị ghi oan hay kế toán (chị Oanh) phải đối soát lại, nên phải có thêm hai chỉ số 0 cho tiền oan và lỗi hãng oan. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | **[NHÁP]** Ép pass_rate hoặc giảm chuyển người thì hãng vận chuyển gánh lỗi oan, chị Hạnh gánh hàng chờ, khách bị từ chối sai gánh trải nghiệm. Vì vậy mới có trần chuyển người 0,30 và SLA 60 phút. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | **[NHÁP]** Có, ở 2 depot với chính sách REFUND-v3 hiện hành và dữ liệu giả; số thật phải đo lại trong pilot. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | **[NHÁP]** Phải viết lại: `daily_refund_cap`, ngưỡng chuyển người duyệt (theo chính sách mới, REFUND-v3 hết hiệu lực 30/11/2026) và `queue_stuck_max` theo số người trực. Ba ngưỡng an toàn bằng 0 giữ nguyên. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **[NHÁP] 6.000** · `roi_min` **[NHÁP] 0,5** · `queue_stuck_max` **[NHÁP] 0** (căn cứ ở mục "Căn cứ ngưỡng" ngay dưới)
- Ngày xem lại tiêu chí: `30/11/2026` **[NHÁP, nhóm chốt]** (REFUND-v3 hết hiệu lực ngày này, ngưỡng và chính sách phải xem lại cùng lúc) · Ai dự: `Quân, Khánh (kinh doanh), Hoàng (vận hành và pháp lý), Hùng (kỹ sư cổng), chị Hạnh (trưởng ca), chị Oanh (kế toán đối soát)` **[NHÁP, nhóm chốt]** (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

#### Căn cứ ngưỡng (từ `data/world.json` và `lab10/ops.py`) · **[NHÁP · Quân]**

Công thức trong `ops.py`: tổng chi phí ngày = tiền LLM + (số ca chuyển người × 10.000đ) + phí giữ chỗ người duyệt (30.000đ mỗi người mỗi ca);
chi phí mỗi ticket = tổng ÷ 22; tiết kiệm = 22 × 10.000đ − tổng − tiền hoàn oan; ROI = tiết kiệm ÷ tổng.

| Ngưỡng | Căn cứ |
|---|---|
| `cost_per_ticket_vnd_max` = **6.000** | Làm tay 10.000đ/ticket. Tiền LLM khoảng 850đ/ticket (200 + 150 + 200 + 100 + 100 + tiền đọc chữ), dưới trần 1.500đ của `ops_limits`. Phí người duyệt 30.000đ/ngày chia 22 ticket = khoảng 1.364đ/ticket. Chỉ cần **không cao hơn 10.000đ** là bài kinh doanh đã trượt, nên đặt 6.000đ (60% làm tay) để chừa chỗ cho người duyệt thứ hai và cho ca chuyển nhiều hơn dự kiến. |
| `roi_min` = **0,5** | Ở mức chi phí 6.000đ/ticket: tổng 132.000đ, tiết kiệm 220.000 − 132.000 = 88.000đ, ROI khoảng 0,67. Đặt 0,5 chừa khoảng 0,17: một khoản hoàn oan 20.000đ (như ca `C-002`) làm ROI giảm khoảng 0,15 mà vẫn chưa tụt dưới ngưỡng, nhưng vẫn bị chặn bởi ngưỡng an toàn bằng 0. |
| `escalation_rate_max` = **0,30** | Nhãn bộ nền có 5 ticket đúng ra phải chuyển người trên 22 (khoảng 0,23). Một người duyệt xử lý 6 ca/giờ, SLA 60 phút, nên chịu được khoảng 6–7 ca đến cùng lúc (khoảng 0,27–0,32). 0,30 nằm giữa nhãn thật và sức chứa. Chuyển nhiều hơn nữa là đẩy việc cho chị Hạnh, không phải tự động hoá. |
| `queue_stuck_max` = **0** | SLA 60 phút đã thống nhất với Ops (`ops_limits`). Ca chờ quá 60 phút là bên thứ ba và khách phải đợi, không đánh đổi được. |
| `pass_rate_min` = **0,95**, `pass_k_min` = **0,90** | `ops_facts` không quy định hai số này, đây là lựa chọn của nhóm. Bộ nền có 110 lần chạy (22 ticket × 5 seed): 0,95 cho phép tối đa 5 lần chạy sai. `pass^k` 0,90 cho phép tối đa 2 ticket không ổn định (20/22 = 0,909). Lab 9 đặt 0,85 và 0,80 vì tiền hoàn nhỏ và có người xem lại; ở LogiX tiền đi qua hãng và shop nên nhóm đặt cao hơn. Số Lab 9 không dùng làm bằng chứng. |
| Ba ngưỡng an toàn = **0** | Hoàn oan và ghi lỗi oan đi ra ngoài LogiX (hãng, shop, kế toán đối soát), không rút lại bằng sửa trợ lý được. |

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

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
