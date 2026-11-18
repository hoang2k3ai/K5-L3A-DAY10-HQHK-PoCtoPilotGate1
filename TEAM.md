# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): HQHK
- Lớp: L3A
- Repo của bàn: `K5-L3A-DAY10-HQHK-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): **S2**

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Đào Huy Hoàng          | 2A202603451     | Vận hành và pháp lý    |      x      |
|   2 | Trần Mạnh Hùng         | 2A202603496     | Gate Engineer          |             |
|   3 | Lê Hồng Quân          | 2A202603705     | Sản phẩm và kinh doanh   |             |
|   4 | Nguyễn Khắc Khánh | 2A202603472 | Sản phẩm và kinh doanh |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## DaoHuyHoang-2A202603451

### Phần việc phụ trách

- Trưởng nhóm; vai **Vận hành và pháp lý**.
- `config/operating_gates.json`: mục `operations` (PIC, `approver_id`, số người trực, `review_capacity_per_hour`, `max_queue_wait_minutes`, `stop_conditions`, `alert_channel`, `decision_note`, `review_sampling_pct`) và mục `legal` (`pii_fields_blocked_to_third_party`, `carrier_fault_requires_recorded_cause`).
- `submission/submission.json`: `team`, `members`, `incident`, `decision_v1`, `decision_v2`, `three_lines`.
- Phiếu B mục **B7.5** (cổng con người – vận hành – pháp lý + Runbook 1–3) và phần vận hành/chi phí của **B8**; Phiếu C mục **C12** (quyết định v2 + ba dòng bắt buộc) — chốt cùng cả bàn.
- `TEAM.md`: bảng thành viên, danh tính Git, giữ repo sạch (không commit `runs/`, `.venv`, `__pycache__`).
- Hỗ trợ bạn Quân (Sản phẩm và kinh doanh) phần Phiếu A Khối 1 và bộ ngưỡng trong `config/acceptance_criteria.json`.

### Đóng góp cụ thể

- Chọn eval card Lab 9 và ca chính **C-002** (`seeded_regression C-002@11`, FM-03 `ticket_trust`) ứng với `T-002@55`; ca dự phòng C-101 (prompt injection), C-113 (PII/số điện thoại), C-005 (cross-principal), C-006/C-103 (điều khoản hết hiệu lực).
- Lập `docs/lab9-reference/` (README ánh xạ ngưỡng Lab 9 → Lab 10 + 3 khoảng trống, eval card, PRD v1.1, trace, eval case C-002) kèm nguồn.
- Đề xuất bộ ngưỡng **0,91 / 0,91 / 6.000đ / ROI 0,5** và phần "Căn cứ ngưỡng": 110 trial → 0,91 ⇔ ≤9 lần trượt ⇔ đúng 1 ticket hỏng; pass^k 0,91 ⇔ ≤1 ticket không đạt 5/5; 6.000đ nằm dưới trần `cost_per_ticket_vnd_max` và tại trần ROI ≈ 0,67 > 0,5. Bàn đã chốt và ký bộ ngưỡng này lúc 2026-11-18 16:08:15 (commit `cbfa81c`, `Sign acceptance criteria`), trước lần chạy đánh giá đầu tiên.
- Điền Khối 1 Phiếu A: A1 (câu 1.1 + 1.2 với `NV-OANH`/`NV-HANH`), A2 (hai cột, 5 dòng), A3 (phương án b), A4 (6 tiêu chí + 2 dòng ranh giới + 4 dòng soát + `business_ops` + ngày soát lại 30/11/2026).
- Sửa lỗi toàn vẹn hash: `core.autocrlf=true` làm 19 file khoá lệch sha256; đặt `core.autocrlf false` + `core.eol lf`, `git rm --cached -r .` rồi `git reset --hard HEAD` → `integrity` chỉ còn báo 32 file `incidents/*` chưa pull (đúng phút 125 mới lấy thẻ).
- Đặt danh tính Git `2A202603451 / 2A202603451@example.com`, gộp nhánh của Quân/Hùng/Khánh, giữ `main` = `origin/main`.

### Bằng chứng

- Commit: `f6146b7`, `60466b2` (TEAM.md); `1b39d54` (chọn eval card C-002 + `docs/lab9-reference/`); `fdbc007` (Phiếu A Khối 1 + bộ ngưỡng trình bàn); `7545d76`, `157ffca` (gộp nhánh, giữ TEAM.md 4 thành viên).
- Dòng phiếu: Phiếu A mục A1–A4, gồm bảng "Căn cứ ngưỡng" trong A4.
- File: `docs/lab9-reference/README.md`, `eval-card.md`, `PRD-v1.1.md`, `trace-case.md`, `eval-case-C-002.md`; `config/acceptance_criteria.json`; `TEAM.md`.
- Máy đo: chưa có `runs/` — cố ý chưa chạy `eval`/`grade` trước khi ký (README luật 1).
- AI: dùng trợ lý AI để đọc `lab10/*`, soát câu chữ Phiếu A, kiểm hash/line-ending và rà luật nộp bài; mọi ngưỡng và quyết định là của bàn.

### Exit ticket

- Học được: ngưỡng phải suy ra từ trần vận hành (`ops_limits`, `ops_facts`) và từ câu hỏi "chấp nhận bao nhiêu ticket hỏng", không chọn theo cảm giác; và "ký trước khi đo" là thứ kiểm được bằng lịch sử git, không phải bằng lời.
- Chưa chắc: 0,91 (⇔ 1 ticket hỏng trên 110 trial) đã đủ chặt để bảo vệ quyết định trước hội đồng chưa, và có nên siết pass^k riêng cho nhóm lỗi tiền/thẩm quyền thay vì dùng một ngưỡng chung cho mọi loại lỗi.

## LeHongQuan-2A202603705

### Phần việc phụ trách

- Vai **Sản phẩm và kinh doanh** (cùng bạn Khánh); đổi từ Kỹ sư cổng sang vai này ở CP1.
- Phiếu A: mục **A1** (câu 1.1), **A3** (câu 1.5), **A4** (câu 1.6: câu tiêu chí, hai câu ranh giới đầu ra, bảng soát bốn câu, nhóm `business_ops`, ngày xem lại).
- Phiếu B: **B3** (câu 2.3: bản đồ dữ liệu, ví dụ drift REFUND-v4), dòng **Kinh doanh** của **B6** (câu 2.5), **B7.4** (câu 2.9: cổng kinh doanh), hai dòng ngoài kỹ thuật của **B4** (Ngân sách, Phạm vi pilot), hai ô của **B8**.
- Phiếu C: **C12** (quyết định Gate 1 v2 và ba dòng bắt buộc), **C3.1** (mức kiểm soát của con người, thẻ S2), **C10** (risk register, 4 dòng).
- File: `config/acceptance_criteria.json` (bản điền đầu tiên), `config/operating_gates.json` (mục `business`), `templates/form-a-criteria.md`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md`, `TEAM.md`.

### Đóng góp cụ thể

- Điền bảng thành viên `TEAM.md`, gắn `upstream` cho repo, chạy `python3 -m unittest discover -s tests` (13 test OK) ở CP1.
- Soạn nháp Phiếu A: mục tiêu hệ thống (câu 1.1), phương án (b) của câu 1.5, sáu câu tiêu chí "Nếu … thì chúng tôi sẽ …", ranh giới đầu ra (300.000đ/khách/ngày, 2.000.000đ/ngày, lỗi hãng thứ 3 trở đi phải có người duyệt), bảng soát bốn câu hỏi.
- Điền `config/acceptance_criteria.json` lần đầu và suy ngưỡng `business_ops` từ `ops_facts`, `ops_limits` và công thức trong `lab10/ops.py` (chi phí/ticket, ROI, `escalation_rate_max`, `queue_stuck_max`). Bộ ngưỡng cuối cùng do cả nhóm chốt trước khi ký.

- Điền mục `business` của `config/operating_gates.json` (trần hoàn 2.000.000đ, ngân sách LLM 1.500đ, ROI 0,5) theo `ops_limits`; chạy `lab10.eval` và `lab10.grade --incident S2` để kiểm chứng số của Hùng, phát hiện kho `?` (`T-018`) tốn 10.359đ/ticket, cao hơn làm tay.
- Soạn nháp C12: quyết định v2 Tiếp tục, bằng chứng từ gói S2, ba dòng bắt buộc.
- Điền C3.1 từ trace `S2-01` mốc base (chữ cài trong ticket làm trợ lý chọn `payer = MERCHANT` và hoàn 475.000đ thay vì 25.000đ, không có mã phê duyệt) và C10 gồm bốn rủi ro có PIC và chỉ số lấy từ report/`monitors.py`.

### Bằng chứng

- Commit: `d08395d` (CP1, `TEAM.md`), `24b7931` (đổi vai), `73d79ca` (nháp Phiếu A), `5489e98` (điền JSON), `c654b04` (chỉnh ngưỡng theo `ops_facts`), `0500b77` và `489edb8` (Phiếu B), `8a3a884` (`operating_gates.json` mục business), `9d04ed7` (C12).
- Dòng phiếu: Phiếu A mục A1 (1.1), A3 (1.5), A4 (1.6, "Căn cứ ngưỡng"); Phiếu B mục B3, B4 (hai dòng ngoài kỹ thuật), B6 (dòng Kinh doanh), B7.4; Phiếu C mục C12, C3.1, C10.
- Máy đo: chỉ chạy `eval` và `grade` sau khi ký (commit ký `cbfa81c`); mã lần chạy dùng làm bằng chứng cho S2 ở C12 là `R-S2-{before,prepared,after}-20261118-172549-ae34d0` (từ `R-S2-grade-20261118-172549-ae34d0`).
- AI: dùng trợ lý AI soạn nháp và đối chiếu số trong `data/world.json`, `lab10/ops.py`; ngưỡng cuối do nhóm quyết.

### Exit ticket

- Học được: một con số tổng (pass_rate 0,9909 ở bộ nền) có thể che hoàn toàn một lỗi gây thiệt hại ra ngoài LogiX (một ticket `T-002@55`: hoàn oan 20.000đ và ghi oan lỗi hãng), nên ngưỡng an toàn phải đặt riêng bằng 0 chứ không gộp vào pass_rate; và ngưỡng kinh doanh phải suy từ `ops_facts` (mỗi ca chuyển người tốn 10.000đ, bằng làm tay), không chép từ ví dụ.
- Chưa chắc: các con số vận hành đều là mock (6 ca/giờ, 10 phút/ca, chi phí LLM theo độ dài chữ), nên chưa biết chi phí 5.273đ/ticket và ROI 0,9 trên gói S2 có giữ được khi người duyệt thật chậm hơn, và khi REFUND-v4 (01/12/2026) làm tỉ lệ chuyển người tăng.

## TranManhHung-2A202603496

### Phần việc phụ trách

- Vai **Gate Engineer** (Kỹ sư cổng).
- Code và chỉ số: `lab10/guards.py` (Vòng 1 và Vòng 2), `lab10/monitors.py` (chỉ số theo dõi mới Vòng 2), phối hợp điều chỉnh `config/operating_gates.json` (`pilot_scope`).
- Phiếu B: mục **B0** (dòng 1–3), **B1** (câu 2.1), **B2** (câu 2.2 dò `T-002@55`), **B7.1–B7.3** (câu 2.6–2.8), **B8** (chốt cổng Vòng 1 & cột quyết định v1).
- Phiếu C (thẻ **S2**): mục **C0** (nhật ký lần chạy Vòng 2), **C1** (câu 3.0 mốc `prepared`), **C2** (câu 3.1 dò trace `S2-01`, `S2-04`, `S2-20`, `S2-44`), **C7** (câu 3.5 bảng sửa), **C8** (câu 3.6 chỉ số `directive_override_rate`).

### Đóng góp cụ thể

- Xử lý xung đột Git (`TEAM.md`, `templates/form-b-evaluation-gates.md`) và khắc phục lỗi sai khác xuống dòng `LF`/`CRLF` trên Windows (`core.autocrlf false`) để `criteria verify` và `1 integrity` đạt chuẩn SHA-256.
- Đo mốc nền `base` và dò trace `T-002@55` (xếp loại **lỗi chìm** từ đầu vào `model_override`), hoàn thiện **B0–B2** trong Phiếu B.
- Viết 3 cổng phòng ngừa Vòng 1 trong `lab10/guards.py`: ghim chính sách hiệu lực theo ngày (`pre_guard` + `H.effective_policy`), chặn ghi đúp và đối chiếu quyền lợi chuẩn từ DB ở `issue_refund` (`_gate_issue_refund`), kiểm tra điều kiện/đúng kiện phạt hãng ở `file_carrier_fault`, lọc PII `recipient_contact` ở `notify_carrier`. Chạy kiểm tra 2 ticket hiểm `--adhoc` (**B7.3**) và chốt mốc `prepared` bằng `lab10.checkpoint` (`5249aa04`).
- Vòng 2 (thẻ **S2**): chạy `grade --incident S2` mốc `prepared` (cổng Vòng 1 đã chặn sạch `33.580.000đ` hoàn sai & `32.750.000đ` trừ tiền oan shop, chỉ còn vướng ROI `0.2 < 0.5` do độ phủ hẹp và thiếu monitor). Bổ sung nhánh kiểm tra trần hoàn tự động `300.000đ/khách/ngày` trong `guards.py`, mở `pilot_scope` thành `all` trong `config/operating_gates.json`, và viết mới chỉ số `directive_override_rate` trong `lab10/monitors.py` → đạt **`PASS-VISIBLE`** (`1 integrity ✅`, `2 criteria ✅`, `3 visible ✅`, `5 regression ✅`, `6 monitor ✅`, `13/13` unit tests `OK`).

### Bằng chứng

- Commit: `e75b347`, `6468aad` (xử lý merge conflict); `e553e65` (Vòng 1 `guards.py` + `B7.1–B7.3`); `c707c51` (`LAB 10: chot cong vong 1, quyet dinh v1`, hash `5249aa04`); `0168614` (Vòng 2 `S2`: `guards.py`, `monitors.py`, `operating_gates.json`, Phiếu C `C0–C2, C7–C8`).
- Mã lần chạy: `R-base-before-20261118-162600-b45eeb` (base), `R-base-after-20261118-170236-6b9105` (cổng Vòng 1), `R-base-prepared-20261118-170337-6b9105` (chốt `prepared`), `R-S2-grade-20261118-172549-ae34d0` (S2 `prepared`), `R-S2-after-20261118-172549-ae34d0` & `R-S2-grade-20261118-172549-ae34d0` (S2 `PASS-VISIBLE`).
- File: `lab10/guards.py`, `lab10/monitors.py`, `config/operating_gates.json`, `templates/form-b-evaluation-gates.md`, `templates/form-c-incident.md`.
- AI: dùng trợ lý AI để đọc cấu trúc repo, phân tích trace lỗi, gợi ý thiết kế cổng `guards.py` / `monitors.py` và rà soát đối chiếu số liệu; mọi con số và code đều được tự chạy kiểm chứng trực tiếp.

### Exit ticket

- Học được: cổng bảo vệ cấp hệ thống (nằm ngoài model và prompt, đối chiếu trực tiếp nguồn sự thật DB) ngăn được cả lỗi tin lời khách lẫn prompt injection mà không làm hỏng ca hợp lệ, nhưng vẫn cần đi kèm `pilot_scope` và chỉ số `monitors` phù hợp để đảm bảo bài toán kinh doanh (ROI, chi phí/ticket).
- Chưa chắc: hiệu năng và độ bền của các cổng hiện tại trên bộ test ẩn (với các kiểu diễn đạt ticket hoặc tình huống biên mới ngoài `S2`) và thời gian duyệt thực tế của nhân sự khi áp dụng quy trình kiểm mẫu 10% ngoài thực địa.

## NguyenKhacKhanh-2A202603472

### Phần việc phụ trách

- Vai **Sản phẩm và kinh doanh** (cùng bạn Quân).
- Phiếu B: mục **B3** (câu 2.3, bản đồ dữ liệu và ví dụ drift), **B7.4** (câu 2.9, cổng kinh doanh), dòng 6 "Chi phí" của checklist **B5**.
- Phiếu C (thẻ **S2**): mục **C5** (câu 3.2 specification; nháp câu 3.3 để vai Vận hành soát), soát số liệu **C12** (quyết định v2).
- File: `templates/form-b-evaluation-gates.md` (B3, B5 dòng 6, B7.4), `templates/form-c-incident.md` (C5, C12), `submission/submission.json` (`decision_v1`, `decision_v2`, `three_lines`).

### Đóng góp cụ thể

- Viết lại B3 và B7.4 bằng số đo thật thay cho số ước lượng: đối chiếu dữ liệu `data/world.json` (5/26 kiện thiếu `delay_cause`, 1 đơn nhiều kiện `O-1013`, 2 đơn quà tặng), dùng `T-002` (khách khai trễ 5 ngày, tracking trễ 2 ngày) làm bằng chứng nguồn sự thật và làm ví dụ drift REFUND-v3 → v4.
- Đo đánh đổi phạm vi pilot trên bộ nền với cổng vòng 1 (chỉ đổi `pilot_scope`): HN + HCM chi phí 5.550đ, ROI 0,80, độ phủ 0,59; tất cả kho chi phí 4.456đ, ROI 1,24. Ở vòng 2 thử thêm trên gói S2 và báo cho nhóm: mở `all` khi chưa vá cổng thì S2 còn hoàn sai 1.080.000đ ở kho DN, tức phạm vi hẹp đang che một lỗ hổng của cổng.
- Sửa lỗi `1 integrity ❌` trên máy Windows của mình do ký tự xuống dòng CRLF (không đổi nội dung file khoá).
- Viết specification câu 3.2 cho `issue_refund` (người trả, số tiền theo tracking, hạn mức không phê duyệt, trần mỗi khách/ngày); sửa C12 cho khớp config hiện tại (`pilot_scope: all`, số của gói S2: chi phí 5.273đ, ROI 0,9); điền `submission.json`.

### Bằng chứng

- Commit: `b237eaa` (B3 và B7.4 bằng số đo thật) và commit nháp vòng 2 (C5, C12, B5 dòng 6, `submission.json`, mục này).
- Mã lần chạy (trên máy Khánh): `R-base-before-20261118-162600-b45eeb`, `R-base-after-20261118-165438-2a46a2` (HN + HCM), `R-base-after-20261118-165448-508836` (tất cả kho), `R-S2-after-20261118-170739-504c85` (S2 với `all` trước khi vá cổng), `R-S2-grade-20261118-172549-ae34d0` (S2 `PASS-VISIBLE`).
- Dòng phiếu: Phiếu B mục B3, B5 (dòng 6), B7.4; Phiếu C mục C5, C12.
- AI: dùng trợ lý AI (Claude Code) để soạn nháp, chạy lệnh đo và đối chiếu số với `data/world.json`, `lab10/ops.py`; mọi con số trong phiếu lấy từ lần chạy thật, quyết định cuối do nhóm chốt.

### Exit ticket

- Học được: (bạn tự viết)
- Chưa chắc: (bạn tự viết)
