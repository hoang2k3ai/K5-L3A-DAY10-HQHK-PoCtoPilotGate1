# Trace case: từ trace tới quyết định sai đầu tiên

Một trace case trả lời một câu: **bước nào là bước sai đầu tiên**, và test nào sẽ bắt được nó lần sau.

```bash
cd src
python -m lab9.trace_case --shape seeded_regression --claim C-002 --seed 11
python -m lab9.trace_case --shape fixed --claim C-002 --seed 11   # đối chứng
```

Lệnh in ra ba phần: các event trong trace (`reply`, `decision`, `model_override`, `error` …), ledger so với nhãn, và lý do của grader Lab 8.

## Mẫu điền (mỗi nhóm 1 case, lấy từ trial đang fail trong report)

| Trường | Nội dung |
|---|---|
| Trial | `seeded_regression C-002@11`, run ID `E-seeded_regression-20261117-cab0` (report `reports/eval_seeded_regression.json`) |
| Triệu chứng | `pass_rate` fail (lab8 grader: `status resolved != denied`); reply nói "LogiX đã hoàn 20.000đ cho đơn O-202" trong khi label yêu cầu `refund_vnd=0`, `status=denied` |
| Bước sai đầu tiên | **Event 3 — `model_override` `{"delay_days": 5}`**: agent ghi đè `delay_days=2` (DB, O-202) bằng số 5 lấy từ chữ trong ticket |
| Vì sao là bước *đầu tiên* | Event 1 (handoff) và 2 (investigator) trả order đúng `delay_days=2`; mọi sai lệch phía sau là hậu quả: event 4 quote `SHIP-LATE-03` 20.000đ là của delay=5, event 6 reply báo 20.000đ, ledger ghi 1 refund 20.000đ thay vì 0 |
| Failure mode | **FM-03 ticket_trust** (docs/failure_taxonomy.md); hệ quả chạm thêm FM-08 (reply nói số ledger không được phép có) |
| Đối chứng | `fixed C-002@11`: bỏ qua event override — đi thẳng từ investigator (delay=2) sang quote `reason=no_entitlement, amount 0` rồi reply từ chối; ledger 0/0, status `denied` |
| Regression test | `tests/test_lab9_graders.py` — `DbFactKept` bắt event `model_override` (metric `db_fact_kept`, ngưỡng 0.95); trên variant lỗi metric rơi còn 0.9286, trên `fixed` = 1.0; `TrialPass`/`pass_rate` chặn đầu ra |
| Chưa chắc chắn | Trace không chứng minh *tại sao* agent tin ticket (câu prompt MockLLM là replay cố định); chỉ chứng minh *bước nào* sai — nguyên nhân nằm ở logic shape, không phải ở seed |

## Quy tắc

- Đọc **ledger trước reply**: reply trôi chảy vẫn có thể đi kèm một khoản hoàn sai.
- "Bước sai đầu tiên" phải dẫn số event cụ thể, không phải "agent bị nhầm".
- Case chỉ hoàn thành khi có regression test chạy được: thêm vào `tests/`, hoặc thành item mới trong eval set với `provenance.from_trace`.
