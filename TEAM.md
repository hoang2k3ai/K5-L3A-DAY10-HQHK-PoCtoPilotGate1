# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): HQHK
- Lớp: L3A
- Repo của bàn: `K5-L3A-DAY10-HQHK-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

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
