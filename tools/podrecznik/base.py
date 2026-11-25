CSS = """
*{box-sizing:border-box}html,body{min-height:844px}body{display:flex;flex-direction:column;margin:0;font-family:Roboto,'Noto Sans',Arial,sans-serif;background:#F1F3F2;color:#16201C;width:390px}
.st{display:flex;justify-content:space-between;padding:8px 18px 2px;font-size:13px;color:#16201C}
.pad{padding:6px 16px 16px}
.h1{font-size:28px;font-weight:700;margin:6px 0 2px}
.top{display:flex;align-items:center;gap:8px;height:48px;font-size:18px;font-weight:500}
.top .back{font-size:22px;width:28px}
.top .sp{flex:1}
h2{font-size:20px;font-weight:500;margin:20px 0 10px;display:flex;align-items:center;justify-content:space-between}
.card{background:#fff;border:1px solid #E1E6E3;border-radius:16px;padding:12px;margin-bottom:8px}
.mut{color:#56635D;font-size:13px}.sm{font-size:12px}
.b{font-weight:600}.row{display:flex;align-items:center;gap:8px}.grow{flex:1}
.pill{display:inline-block;font-size:12px;font-weight:500;padding:3px 10px;border-radius:999px;white-space:nowrap}
.over{background:#FDE4D6;color:#9A3412}.soon{background:#FEF0C2;color:#7C4A03}.ok{background:#D9EEE8;color:#0B5A4D}.never{background:#E5E9E7;color:#46524D}.plan{background:#DCE8FD;color:#1E3A8A}
.btn{display:inline-block;background:#0F6B5C;color:#fff;border-radius:999px;padding:10px 16px;font-size:14px;font-weight:500;white-space:nowrap}
.btn.o{background:#fff;color:#0F6B5C;border:1px solid #CBD3CF}
.tb{color:#0F6B5C;font-weight:500;font-size:14px}
.chip{display:inline-block;border:1px solid #CBD3CF;border-radius:8px;padding:6px 12px;font-size:14px;background:#fff}
.chip.on{background:#D9EEE8;border-color:#D9EEE8;color:#0B4F44}
.av{width:44px;height:44px;border-radius:50%;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:600;flex:none}
.bar{height:6px;border-radius:3px;background:#E5E9E7;overflow:hidden;margin-top:6px}.bar i{display:block;height:100%}
.nav{margin-top:auto;display:flex;justify-content:space-around;background:#fff;border-top:1px solid #E1E6E3;padding:8px 2px 12px}
.nav div{display:flex;flex-direction:column;align-items:center;font-size:11px;color:#56635D;gap:2px}
.nav span{padding:3px 14px;border-radius:999px;font-size:16px}
.nav .a{color:#16201C;font-weight:600}.nav .a span{background:#D9EEE8}
.in{border:1px solid #B9C4BF;border-radius:8px;padding:12px;font-size:15px;background:#fff;color:#16201C}
.lab{font-size:12px;color:#3F4B46;margin:10px 0 4px}
.dot{width:8px;height:8px;border-radius:50%;flex:none;margin-top:6px}
.hint{background:#E7F1EE;color:#0B4F44;border-radius:12px;padding:10px 12px;font-size:13px}
table{width:100%;border-collapse:collapse;font-size:13px}td{padding:7px 0;border-bottom:1px solid #EDF0EE}
.hi{color:#9A3412;font-weight:600}.lo{color:#1E40AF;font-weight:600}
.fab{position:absolute;right:16px;bottom:84px;background:#D9EEE8;color:#0B4F44;border-radius:16px;padding:16px 18px;font-weight:600;box-shadow:0 4px 10px rgba(0,0,0,.18)}
.dlgbg{background:rgba(0,0,0,.38);flex:1;padding:40px 18px}
.dlg{background:#fff;border-radius:26px;padding:22px 20px}
.dlg .t{font-size:22px;margin-bottom:10px}
"""
TABS = [("⌂", "Pulpit"), ("▦", "Kalendarz"), ("✚", "Leki"), ("⟋", "Wykresy"), ("♥", "Zwierzaki"), ("⇪", "Dane")]
def nav(active):
    return '<div class="nav">' + "".join(f'<div class="{"a" if l == active else ""}" data-tab="{l}"><span>{i}</span>{l}</div>' for i, l in TABS) + "</div>"
def page(body, active=None):
    return f'<!doctype html><html lang="pl"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="st"><span>9:41</span><span>▾ ▴ 86%</span></div>{body}{nav(active) if active else ""}</body></html>'
