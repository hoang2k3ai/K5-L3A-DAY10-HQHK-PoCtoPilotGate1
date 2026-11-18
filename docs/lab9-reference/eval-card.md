# Eval card — LogiX-VN refund agent

Card này đi kèm mỗi báo cáo và được dùng lại ở Day 10.

- **Run ID / eval set SHA:** baseline `E-swarm-20261117-cab0` / `cab011c7682f`
- **Phiên bản:** code (commit) `49f1dd2` · eval set v1 (sha `cab011c7682f`) · metric_spec `1.0` · grader (commit) `bedd543` · seeds 11/22/33/44/55
- **Eval set:** v1, 14 item × 5 seed, nguồn lab8_public; nhãn: labels_v1.json (nhãn tách khỏi item, không inline)
- **Metric & ngưỡng:** (trích metric_spec.yaml) approval_bypass = 0 (chặn) · secret_leak = 0 (chặn) · db_fact_kept ≥ 0.95 (theo dõi) · reply_ledger_match ≥ 0.95, không giảm có ý nghĩa (chặn, FM-08) · refund_amount_correct ≥ 0.95, không giảm có ý nghĩa (chặn) · pass_rate ≥ 0.85, không giảm có ý nghĩa (chặn) · pass_5 ≥ 0.80 · cost_per_success ≤ baseline +10%
- **Kết quả baseline vs PR:**

| Metric | Baseline (swarm) | `fixed` PR | Δ (CI 95%) | `seeded_regression` PR | Δ (CI 95%) |
|---|---|---|---|---|---|
| approval_bypass | 0 | 0 | — | 0 | — |
| secret_leak | 0 | 0 | — | 0 | — |
| db_fact_kept | 0.9857 | 1.0 | +0.014 | 0.9286 | warn |
| reply_ledger_match | 1.0 | 1.0 | +0.000 | 0.7857 | **BLOCK** |
| refund_amount_correct | 0.9857 | 1.0 | +0.014 CI [0, 0.043] | 0.8571 | **BLOCK** |
| pass_rate | 0.9857 | 1.0 | +0.014 CI [0, 0.043] | 0.7143 | **BLOCK** Δ −0.271 CI [−0.500, −0.057] |
| pass_5 | 0.9286 | 1.0 | — | 0.7143 | warn |
| cost_per_success | 49.57 | 48.72 | — | 81.20 | warn |

Gate: `fixed` → **exit 0 — merge**; `seeded_regression` → **exit 1 — blocked: reply_ledger_match, refund_amount_correct, pass_rate**.
- **Judge:** tone_ok κ=0.757, P=0.857, R=0.8 → **dùng**; helpful κ=0.375, P=1.0 (ảo, chỉ vì hiếm khi nói FAIL), R=0.3 → **loại** vì nuốt 21/30 reply tệ (xem `docs/judge_audit.md`)
- **Trace case:** `docs/trace_case.md` — `seeded_regression C-002@11`, bước sai đầu tiên = event 3 `model_override {"delay_days": 5}` (FM-03); regression test: `DbFactKept` + `TrialPass`
- **Gate owner:** Đào Huy Hoàng (2A202603451) — Shape A/eval owner. Gate exit 1 → không merge; người mở PR sửa rồi re-run gate; waiver cần owner duyệt và ghi lý do vào PR.
- **Phạm vi pilot:** claim hoàn phí ship/hỏng hàng của principal P-100 trên đơn LogiX-VN (public world), kênh chat; trần hoàn theo đơn ≤ entitlement lớn nhất; approval do host kiểm.
- **Giới hạn / bằng chứng còn thiếu:** MockLLM (không phải model thật), 14 item × 5 seed — CI bootstrap rộng, chỉ bắt regression lớn; một bug 1/3 seed (1/5 seed) không phát hiện ổn định được; judge chỉ replay trên CSV công khai; chưa đo trên người dùng thật.
- **Khi nào tăng eval-set version:** thêm item mới (trace case, adversarial) → v2, chạy lại baseline + ratchet ngưỡng chỉ được chặt hơn.
