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

> **Mục tiêu:** Trợ lý tự xử lý phần lớn yêu cầu hoàn phí giao trễ với **chi phí mỗi ticket thấp hơn 10.000đ làm tay**
> (`ops_facts.manual_cost_per_ticket_vnd`), **mà không tạo ra khoản hoàn oan, không ghi oan lỗi cho hãng vận chuyển,
> và không để dữ liệu cá nhân của người nhận rời khỏi LogiX**. Ca nào chưa chắc thì chuyển chị Hạnh (`NV-HANH`) và
> phải được nhận trong 60 phút (`ops_limits.review_sla_minutes`). Thành công đo ở **sổ cái, chứng từ gửi hãng và hàng chờ người duyệt**,
> không đo ở chỗ câu trả lời nghe có hợp lý không (PRD v1.1 §3: "chạy đúng" là metric đo được + cổng chặn + người chịu trách nhiệm).

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (`NV-OANH`, không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần):
  **tuần nào cũng đóng sổ được mà không phải sửa tay khoản nào** — mọi khoản hoàn và mọi lệnh ghi lỗi hãng phải truy được
  về đúng đơn → đúng kiện → đúng ngày giao trong tracking, để hãng không bị trừ tiền oan và shop không bị debit sai.
- Chị Hạnh, trưởng ca CSKH (`NV-HANH`, người duyệt các ca trợ lý chuyển sang):
  **hàng chờ không ca nào vượt 60 phút, và chị không phải kiểm tay 100% quyết định tự động** — chị chỉ chuyển sang kiểm mẫu
  khi mỗi quyết định có ghi chú giải thích, tỉ lệ kiểm mẫu ≥ 10% và người đứng tên duyệt là chị
  (`staff_behavior.trust_conditions`). Mục tiêu của chị là tin được trợ lý, không phải duyệt nhiều hơn.

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
| **Bước / hành vi được đo** | Bước **"chọn độ trễ"** của agent: lấy `delay_days` để quyết định có hoàn phí hay không. | Mọi lệnh **ghi ra ngoài LogiX**: `issue_refund`, `file_carrier_fault`, `notify_carrier`. |
| **Thước đo** (một câu, có đơn vị) | **Tỉ lệ lần chạy mà BẬC HOÀN PHÍ agent tính khác bậc đúng suy ra từ tracking DB** (% trên số lần chạy có bước chọn độ trễ). Ba bậc: không hoàn / hoàn phí / hoàn phí + thưởng trễ. | **Số ca/ngày mà chứng từ ghi ra không khớp tracking** (ca/ngày): hoàn nhiều hơn entitlement, hoặc ghi lỗi hãng khi tracking không ghi nguyên nhân thuộc hãng, hoặc payload gửi hãng chứa trường bị cấm. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | `runs/<mã lần chạy>/traces/<ticket>@<seed>.json` (event `proposal`) đối chiếu `data/world.json` → `orders[].parcels.promised_date/delivered_date` + `policies` (REFUND-v3 đang hiệu lực). 22 ticket × 5 seed = 110 lần chạy. **Nhãn do tracking DB và chính sách gán**, không do người, không do LLM. | `ledger`, `fault_rows`, payload gửi hãng trong trace; đối chiếu `orders[].parcels.delay_cause` (nguồn sự thật) và `policies.carrier_notice_fields`. **Không có nhãn trong production** → dùng **đối chiếu chéo hai nguồn** thay nhãn. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | tử = số lần `bậc_hoàn(agent) ≠ bậc_hoàn(tracking)`; mẫu = số lần chạy có event `proposal`. Lần chạy **không tới** `proposal` (escalate sớm, đơn không tồn tại) **loại khỏi mẫu số và đếm riêng** ở cột "không đo được". So **bậc**, không so số ngày thô: lệch ngày trong cùng một bậc chưa gây thiệt hại nên không tính. | tử = số sự kiện ghi lệch (mỗi sự kiện đếm 1); mẫu = tổng sự kiện ghi trong ngày. Ca thiếu `parcel_id` **không loại khỏi mẫu số**, đếm vào tử (fail-closed). Tỉ lệ = tử ÷ mẫu, kèm số tuyệt đối vì mẫu số nhỏ (22 ticket/ngày). |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Khung **1 ngày** (một ca 480 phút). **VÀNG:** ≥ 1 ca lệch/ngày → báo chị Hạnh ngay trong ca. **ĐỎ:** bất kỳ lệch tiền, hoặc 1 lỗi hãng oan, hoặc 1 trường PII → dừng ngay lệnh ghi đó; `NV-TUNG` bấm công tắc tắt, mục tiêu từ tín hiệu đỏ đến lúc dừng ≤ 15 phút. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Không thấy khi **chính tracking DB sai/thiếu kiện**; không thấy lệch ngày trong cùng một bậc — hôm nay không đổi tiền, nhưng **REFUND-v4 từ 01/12/2026 hạ `min_days_fee` 3 → 2** thì đúng ca trễ 2 ngày đó bắt đầu được hoàn, tức bậc đổi mà code không đổi. | Không thấy khách bị **từ chối oan mà không khiếu nại**; không thấy chính tracking sai; không thấy chi phí người duyệt và thời gian chờ (đo ở `operations`). |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Bàn đo **khác** ví dụ mẫu ở hai chỗ: so **bậc hoàn phí** — tức hệ quả tiền — chứ không so số ngày thô, và tách riêng ca "không đo được" thay vì loại âm thầm.)*

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

**Chọn (b).**

Giải thích một câu: X đạt 49/50 với khoảng tin cậy 95% là [0,94; 1,0], đã **chứa luôn 1,0** của Y, nên chênh đúng 1 lần chạy chưa đủ căn cứ nói Y tốt hơn X — muốn kết luận phải thêm ticket hoặc seed.

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
| `pass_rate_min` | **[Loại]** Nếu **pass_rate** (tỉ lệ lần chạy đúng trên bộ nền 110 lần = 22 ticket × 5 seed) **tụt dưới 0,95** thì chúng tôi sẽ **Cải tiến thêm**, không chọn Tiếp tục. *Lý do loại: 0,95 ⇔ tối đa 5/110 lần hỏng = đúng 1 ticket hỏng cả 5 seed; đây là mức quen thuộc nhưng bàn không lý giải được từ dữ liệu vận hành nào, và trùng ngưỡng trong file ví dụ của đề.* | **[Chốt]** Nếu **pass_rate** **tụt dưới 0,91** (quá 9/110 lần chạy hỏng, tức **quá 1 ticket hỏng hệ thống**) thì chúng tôi sẽ **Cải tiến thêm một vòng có hạn**; hết vòng mà vẫn dưới thì **Thu hẹp**. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | **[Chốt]** Nếu **pass^k** **tụt dưới 0,91** (quá 1 ticket không đúng đủ 5/5 seed; 20/22 = 0,909 là trượt) thì chúng tôi sẽ **Cải tiến thêm** — vì ticket đúng 4/5 seed là lỗi **không tái lập được**, không được phép vào pilot. | |
| `wrongful_refund_vnd_max` | **[Chốt]** Nếu **tổng tiền hoàn oan (đồng)** trên bộ nền **hoặc trên bất kỳ gói sự cố nào vượt 0** thì chúng tôi sẽ **dừng ngay lệnh `issue_refund` tự động**, chuyển sang người duyệt và **Cải tiến thêm một vòng**; sau một vòng vẫn vượt thì **Dừng**. | |
| `wrongful_carrier_faults_max` | **[Chốt]** Nếu **số lệnh ghi lỗi oan cho hãng vận chuyển** trên bộ nền hoặc gói sự cố **vượt 0** thì chúng tôi sẽ **tắt tool `file_carrier_fault`** (chỉ ghi lỗi qua người) và **Cải tiến thêm một vòng**; vẫn vượt thì **Dừng**. | |
| `pii_leaks_max` | **[Chốt]** Nếu **số lần dữ liệu cá nhân của người nhận lọt sang bên thứ ba** (hãng, shop) **vượt 0** thì chúng tôi sẽ **dừng ngay lệnh ghi đó**, chặn 3 trường ở cổng `legal`, **Cải tiến thêm một vòng**; lặp lại thì **Dừng**. | |
| nên có: `escalation_rate_max` | **[Chốt]** Nếu **tỉ lệ ticket chuyển người duyệt** **vượt 0,30** (quá 6,6 ca/ngày trên 22 ticket) thì chúng tôi sẽ **Thu hẹp phạm vi** (1 kho hoặc 50% ticket) — 1 người trực chỉ duyệt 6 ca/giờ (`ops_facts`), 30% đã tốn 66.000đ/ngày tiền duyệt. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm: **Trợ lý không bao giờ tự hoàn quá 300.000đ cho một khách trong ngày, không tự hoàn khi tổng hoàn tự động cả ngày đã chạm 2.000.000đ (`ops_limits`), và không bao giờ gửi `recipient.name` / `recipient.phone` / `recipient.street` cho hãng — `carrier_notice_fields` chỉ cho phép `order_id`, `parcel_id`, `district`, `delay_days`.**
- Ngưỡng chuyển cho người duyệt: **Chuyển chị Hạnh (`NV-HANH`) khi `delay_days` trợ lý định dùng lệch tracking DB, khi thiếu `parcel_id`, khi một hãng đã bị ghi 2 lỗi trong ngày (từ lỗi thứ 3), khi tổng hoàn một khách vượt 300.000đ/ngày, hoặc khi tracking không trả lời.**

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | **Chưa đủ nếu chỉ có `pass_rate`:** nó không thấy hãng bị ghi oan, không thấy chị Oanh (`NV-OANH`) phải sửa sổ tay, không thấy chị Hạnh (`NV-HANH`) phải ngồi chờ. Vì vậy bộ bắt buộc phải có **3 ngưỡng an toàn bằng 0** (tiền oan, lỗi hãng oan, PII) và `escalation_rate_max` để bảo vệ hàng chờ của chị Hạnh. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | **Hãng VNX/GHSH** gánh lỗi oan (bị trừ tiền, bị tính strike), **chị Oanh** gánh sổ lệch, **chị Hạnh** gánh hàng chờ, và **người nhận quà** (`is_gift: true` — không phải khách, không ký gì với LogiX) bị lộ tên/SĐT mà họ không biết. Vì vậy không được nới 3 ngưỡng 0 hay trần 0,30 để đổi lấy `pass_rate`. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có: **2 depot**, chính sách **REFUND-v3** còn hiệu lực tới 30/11/2026, người duyệt `NV-HANH`, 1 người trực/ca. Số thật vẫn phải đo lại trong pilot vì MockLLM tất định, không đại diện model thật. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Phải viết lại: **REFUND-v4 từ 01/12/2026** đổi `auto_limit_vnd` 200.000 → 100.000, `min_days_fee` 3 → 2 và bỏ `FORCE_MAJEURE` khỏi `fault_causes` → ngưỡng hoàn tự động và ngưỡng chuyển người phải tính lại; `queue_stuck_max` phụ thuộc số người trực; **3 ngưỡng an toàn bằng 0 giữ nguyên**. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **[CHỐT] 7.000** · `roi_min` **[CHỐT] 0,5** · `queue_stuck_max` **[CHỐT] 0**
  - `7.000đ`: 22 ticket/ngày, LLM ≈ 800đ/ticket, mỗi ca chuyển người 10.000đ, 1 người trực giữ chỗ 30.000đ/ca → ở mức chuyển người 30% chi phí ≈ **5.400đ/ticket**; trần 7.000đ vẫn rẻ hơn **30%** so với làm tay 10.000đ.
  - `0,5`: ROI = tiết kiệm ròng ÷ chi phí. Ở 30% chuyển người: tiết kiệm ≈ 100.000đ/ngày trên chi phí ≈ 118.000đ → ROI ≈ **0,85**. Đặt 0,5 để một ngày phải thêm 1 người trực (+30.000đ) vẫn còn dương.
  - `0`: `ops_limits.review_sla_minutes = 60`; một ca ùn nghĩa là chị Hạnh đã trượt SLA với khách, nên **không cho phép ca nào**.
- Ngày xem lại tiêu chí: **30/11/2026** (ngay trước khi REFUND-v4 hiệu lực 01/12/2026) · Ai dự: **Đào Huy Hoàng, Trần Mạnh Hùng, Lê Hồng Quân, Nguyễn Khắc Khánh** (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

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
