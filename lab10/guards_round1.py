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
"""
from . import helpers as H
from .tools import Verdict


def _current_policy(ctx):
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _gate_issue_refund(ctx, action):
    tid = action.get("ticket_id")
    if ctx.tools.ledger_rows(ticket_id=tid):
        ctx.log("duplicate_refund_blocked", ticket_id=tid)
        return Verdict.deny("ticket đã có dòng hoàn tiền trong sổ cái, chặn ghi đúp")

    order = ctx.tools.lookup_order(action.get("order_id"))
    pol = _current_policy(ctx)
    if not order or not pol:
        return Verdict.allow()

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    expected = H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))
    asked = action.get("amount_vnd", 0)
    payer = action.get("payer", "LOGIX")
    basis = action.get("basis", "policy")

    if asked != expected or payer != "LOGIX" or basis == "fail_open":
        ctx.log("refund_db_mismatch", asked=asked, expected=expected, payer=payer, basis=basis, db_delay=delay)
        if expected <= 0:
            return Verdict.deny("không đủ điều kiện hoàn tiền theo tracking DB và chính sách hiệu lực")
        if expected > pol["auto_limit_vnd"] and not action.get("approval_id"):
            return Verdict.escalate("quyền lợi theo DB vượt hạn mức tự động, cần người duyệt")
        return Verdict.modify(
            "điều chỉnh số tiền và người trả khớp quyền lợi chuẩn từ DB",
            amount_vnd=expected,
            payer="LOGIX",
        )
    return Verdict.allow()


def _gate_file_carrier_fault(ctx, action):
    order = ctx.tools.lookup_order(action.get("order_id"))
    pol = _current_policy(ctx)
    if not order or not pol:
        return Verdict.allow()

    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(pol, parcel, delay):
        ctx.log("carrier_fault_denied", parcel_id=parcel["parcel_id"], cause=parcel.get("delay_cause"), db_delay=delay)
        return Verdict.deny("không đủ điều kiện ghi lỗi hãng theo tracking DB và chính sách hiệu lực")

    if (
        action.get("parcel_id") != parcel["parcel_id"]
        or action.get("carrier_id") != parcel["carrier_id"]
        or action.get("delay_days") != delay
    ):
        ctx.log("carrier_fault_corrected", old_parcel=action.get("parcel_id"), new_parcel=parcel["parcel_id"])
        return Verdict.modify(
            "chỉnh đúng kiện hàng, hãng và số ngày trễ theo tracking DB",
            parcel_id=parcel["parcel_id"],
            carrier_id=parcel["carrier_id"],
            driver_id=parcel.get("driver_id"),
            delay_days=delay,
        )
    return Verdict.allow()


def _gate_notify_carrier(ctx, action):
    payload = dict(action.get("payload") or {})
    if "recipient_contact" in payload:
        payload.pop("recipient_contact", None)
        ctx.log("pii_stripped", tool="notify_carrier")
        return Verdict.modify("chặn gửi thông tin cá nhân người nhận cho hãng", payload=payload)
    return Verdict.allow()


def pre_guard(ctx):
    pol = _current_policy(ctx)
    if pol is not None:
        ctx.log("policy_pinned", policy_id=pol["policy_id"])
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool == "issue_refund":
        return _gate_issue_refund(ctx, action)
    if tool == "file_carrier_fault":
        return _gate_file_carrier_fault(ctx, action)
    if tool == "notify_carrier":
        return _gate_notify_carrier(ctx, action)
    return Verdict.allow()
