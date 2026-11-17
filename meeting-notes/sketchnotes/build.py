"""Builds the sketchnote-style infographics (HTML) for both meetings.

Run:  python3 build.py   (writes *.html next to this file)
Then: node render.js      (renders the HTML to PNG with Playwright)
"""
from pathlib import Path

HERE = Path(__file__).parent

S = 'fill="none" stroke="#222" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "person": f'<svg viewBox="0 0 64 64"><circle cx="32" cy="18" r="10" {S}/><path d="M14 56c2-14 9-22 18-22s16 8 18 22" {S}/></svg>',
    "people": f'<svg viewBox="0 0 64 64"><circle cx="22" cy="20" r="8" {S}/><circle cx="44" cy="22" r="7" {S}/><path d="M6 54c2-12 8-18 16-18s14 6 16 18M34 38c3-3 6-4 10-4 7 0 12 6 14 18" {S}/></svg>',
    "clock": f'<svg viewBox="0 0 64 64"><circle cx="32" cy="34" r="22" {S}/><path d="M32 20v15l10 6M24 6h16" {S}/></svg>',
    "moon": f'<svg viewBox="0 0 64 64"><path d="M42 8a24 24 0 1 0 14 34A20 20 0 0 1 42 8z" {S}/><path d="M50 12l2 5 5 1-5 2-1 5-2-5-5-1 5-2z" {S}/></svg>',
    "class": f'<svg viewBox="0 0 64 64"><rect x="8" y="8" width="48" height="30" rx="2" {S}/><path d="M16 18h20M16 26h28M20 56c1-7 4-10 8-10s7 3 8 10M28 46a5 5 0 1 0 0-.1" {S}/></svg>',
    "question": f'<svg viewBox="0 0 64 64"><path d="M22 22c0-7 5-12 11-12s11 4 11 10c0 8-11 9-11 18" {S}/><circle cx="33" cy="50" r="2.5" fill="#222"/></svg>',
    "doc": f'<svg viewBox="0 0 64 64"><path d="M14 6h26l12 12v40H14z" {S}/><path d="M40 6v12h12M22 30l4 4 8-8M22 44h20" {S}/></svg>',
    "pen": f'<svg viewBox="0 0 64 64"><path d="M10 54l4-14L44 10l10 10-30 30z" {S}/><path d="M38 16l10 10M10 54l14-4" {S}/></svg>',
    "keyboard": f'<svg viewBox="0 0 64 64"><rect x="6" y="18" width="52" height="30" rx="4" {S}/><path d="M14 28h4M24 28h4M34 28h4M44 28h6M14 38h36" {S}/></svg>',
    "juggle": f'<svg viewBox="0 0 64 64"><circle cx="14" cy="14" r="6" {S}/><circle cx="32" cy="8" r="6" {S}/><circle cx="50" cy="14" r="6" {S}/><path d="M12 56c4-14 10-20 20-20s16 6 20 20M18 30c4 4 8 6 14 6s10-2 14-6" {S}/></svg>',
    "laptop": f'<svg viewBox="0 0 64 64"><rect x="12" y="12" width="40" height="28" rx="2" {S}/><path d="M4 48h56l-4 6H8z" {S}/><path d="M26 22l12 10M38 22L26 32" {S}/></svg>',
    "book": f'<svg viewBox="0 0 64 64"><path d="M32 14C24 8 14 8 6 10v40c8-2 18-2 26 4 8-6 18-6 26-4V10c-8-2-18-2-26 4zM32 14v40" {S}/></svg>',
    "phone": f'<svg viewBox="0 0 64 64"><path d="M18 8l8 12-5 6c3 7 9 13 16 16l6-5 12 8-4 9C33 54 10 31 9 12z" {S}/><path d="M40 10a14 14 0 0 1 14 14M40 18a6 6 0 0 1 6 6" {S}/></svg>',
    "eye": f'<svg viewBox="0 0 64 64"><path d="M4 32C12 20 22 14 32 14s20 6 28 18c-8 12-18 18-28 18S12 44 4 32z" {S}/><circle cx="32" cy="32" r="8" {S}/><path d="M10 54L54 10" {S}/></svg>',
    "chart": f'<svg viewBox="0 0 64 64"><path d="M8 8v48h48" {S}/><path d="M16 44l10-12 8 6 10-16 10 4" {S}/><path d="M46 10l6 6M52 10l-6 6" {S}/></svg>',
    "wrong": f'<svg viewBox="0 0 64 64"><circle cx="18" cy="18" r="8" {S}/><circle cx="46" cy="46" r="8" {S}/><path d="M24 24l16 16M50 18l-6-6M38 12h12v12" {S}/></svg>',
    "folder": f'<svg viewBox="0 0 64 64"><path d="M6 16h18l6 6h28v32H6z" {S}/><path d="M26 34c0-4 3-7 6-7s6 3 6 6c0 4-6 5-6 10M32 48v.1" {S}/></svg>',
    "satellite": f'<svg viewBox="0 0 64 64"><rect x="24" y="24" width="14" height="14" rx="2" transform="rotate(45 31 31)" {S}/><path d="M18 18L8 8M44 44l10 10M14 22l-8 8 8 8M42 14l8-8 8 8M10 52a12 12 0 0 0 10 4M6 46a20 20 0 0 0 16 14" {S}/></svg>',
    "mentor": f'<svg viewBox="0 0 64 64"><circle cx="20" cy="16" r="8" {S}/><path d="M6 56c1-14 6-22 14-22 6 0 10 4 12 10M36 30h22v16H36zM42 50l-4 6M52 50l4 6" {S}/></svg>',
    "check": f'<svg viewBox="0 0 64 64"><rect x="8" y="8" width="48" height="48" rx="6" {S}/><path d="M18 32l10 10 18-20" {S}/></svg>',
    "bell": f'<svg viewBox="0 0 64 64"><path d="M16 44V28a16 16 0 0 1 32 0v16l6 6H10z" {S}/><path d="M26 54a6 6 0 0 0 12 0M54 12l4-4M10 12L6 8" {S}/></svg>',
    "toggle": f'<svg viewBox="0 0 64 64"><rect x="6" y="10" width="40" height="16" rx="8" {S}/><circle cx="38" cy="18" r="5" fill="#222"/><rect x="18" y="38" width="40" height="16" rx="8" {S}/><circle cx="26" cy="46" r="5" {S}/></svg>',
    "ladder": f'<svg viewBox="0 0 64 64"><path d="M18 58V6M46 58V6M18 16h28M18 30h28M18 44h28M40 2l6 4 6-4" {S}/></svg>',
    "chat": f'<svg viewBox="0 0 64 64"><path d="M6 10h34v22H20l-8 8v-8H6z" {S}/><path d="M44 24h14v20h-6v8l-8-8H28v-6" {S}/></svg>',
    "loop": f'<svg viewBox="0 0 64 64"><path d="M50 22A20 20 0 0 0 14 24M14 42a20 20 0 0 0 36-2" {S}/><path d="M50 10v12H38M14 54V42h12" {S}/></svg>',
    "target": f'<svg viewBox="0 0 64 64"><circle cx="30" cy="34" r="22" {S}/><circle cx="30" cy="34" r="12" {S}/><circle cx="30" cy="34" r="3" fill="#222"/><path d="M30 34L56 8M50 6l6 2 2 6" {S}/></svg>',
    "bolt": f'<svg viewBox="0 0 64 64"><path d="M36 4L14 36h16l-4 24 24-34H34z" {S}/></svg>',
}

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Patrick+Hand&family=Permanent+Marker&display=swap');
:root{--ink:#222;--paper:#fbf8f1;--y:#ffe27a;--b:#a9d8f5;--g:#b9e8a3;--p:#f7b6c8;--o:#ffc98b;--v:#d4c2f5;--r:#ff8f8f}
*{box-sizing:border-box;margin:0}
body{background:var(--paper);color:var(--ink);font-family:'Patrick Hand',cursive;width:1600px;padding:56px 60px 70px;
  background-image:radial-gradient(#e6dfcf 1.2px,transparent 1.3px);background-size:26px 26px}
.title{text-align:center;margin-bottom:10px;position:relative}
.title h1{display:inline-block;font-family:'Permanent Marker',cursive;font-size:74px;letter-spacing:2px;padding:6px 40px 2px;position:relative;transform:rotate(-1.2deg)}
.title h1::after{content:"";position:absolute;left:10px;right:10px;bottom:6px;height:26px;background:var(--y);z-index:-1;border-radius:40% 10% 35% 15%;transform:rotate(.8deg)}
.title p{font-family:'Caveat',cursive;font-size:36px;margin-top:2px}
.rough{position:relative}
.rough::before{content:"";position:absolute;inset:0;border:3px solid var(--ink);border-radius:255px 18px 225px 18px/18px 225px 18px 255px;pointer-events:none}
.grid{display:grid;gap:34px}
.card{padding:22px 24px 22px;background:#fff;box-shadow:7px 8px 0 var(--sh,var(--y))}
.card:nth-child(odd){transform:rotate(-.6deg)}.card:nth-child(even){transform:rotate(.7deg)}
.card h2{font-family:'Permanent Marker',cursive;font-size:31px;line-height:1.1;display:flex;align-items:center;gap:12px;margin-bottom:12px}
.card h2 .num{flex:none;width:46px;height:46px;border:3px solid var(--ink);border-radius:50% 45% 52% 48%;display:grid;place-items:center;background:var(--sh,var(--y));font-size:24px}
.item{display:flex;gap:14px;align-items:flex-start;margin:12px 0}
.item svg{flex:none;width:58px;height:58px}
.item div{font-size:26px;line-height:1.18}
.item b{font-family:'Caveat',cursive;font-weight:700;font-size:33px;display:block;line-height:1}
.hl{background:linear-gradient(transparent 55%,var(--hl,var(--y)) 55%);padding:0 3px}
.arrow{font-family:'Caveat',cursive;font-size:28px;font-weight:700}
.quote{font-family:'Caveat',cursive;font-size:36px;font-weight:700;text-align:center;padding:14px 20px;margin:4px 0 0}
.tag{display:inline-block;font-family:'Caveat',cursive;font-weight:700;font-size:26px;padding:0 12px;margin:4px 6px 0 0;border:2.5px solid var(--ink);border-radius:20px 8px 18px 10px/10px 18px 8px 20px;background:#fff}
.colhead{font-family:'Permanent Marker',cursive;font-size:44px;text-align:center;margin:26px 0 22px}
.colhead span{padding:2px 26px;display:inline-block}
.foot{text-align:center;font-family:'Caveat',cursive;font-size:26px;margin-top:40px;color:#555}
.star{position:absolute;font-size:44px;font-family:'Permanent Marker',cursive}
"""


def item(icon, head, body=""):
    return f'<div class="item">{ICONS[icon]}<div><b>{head}</b>{body}</div></div>'


def card(num, title, color, inner, extra_style=""):
    return (f'<section class="card rough" style="--sh:var(--{color});--hl:var(--{color});{extra_style}">'
            f'<h2><span class="num">{num}</span>{title}</h2>{inner}</section>')


def page(title, sub, body, foot):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{CSS}</style></head><body>
<header class="title"><h1>{title}</h1><p>{sub}</p></header>
{body}
<p class="foot">{foot}</p>
</body></html>"""


def assessors():
    cards = [
        card(1, "Learners &amp; Delivery", "b",
             item("person", "Newbies", "New learners need <span class='hl'>extra support</span>")
             + item("moon", "Shift workers", "Need a <span class='hl'>workplace assessor</span> <span class='arrow'>&rarr; takes time!</span>")
             + item("class", "F2F delivery", "Face-to-face sessions in the mix")),
        card(2, "Clarity", "p",
             item("question", "Confusion", "What does the <span class='hl'>assessment task</span> ask for? What <span class='hl'>feedback</span> is required?")
             + item("doc", "Templates + guidelines", "A proper <span class='hl'>MARKING GUIDE</span> please!")),
        card(3, "Workload", "o",
             item("clock", "Time for marking", "Never enough of it")
             + item("keyboard", "Data entry", "<span class='arrow'>&rarr;</span> should it sit with <span class='hl'>ADMIN</span>?")
             + item("juggle", "Competing priorities", "Marking vs. admin vs. teaching")),
        card(4, "LMS", "v",
             item("laptop", "LMS issues", "Problems with <span class='hl'>access</span> + <span class='hl'>usage</span>")),
        card(5, "Training", "g",
             item("book", "aXcelerate training", "<span class='arrow'>&rarr;</span> was \"100 yrs ago\"<br><span class='arrow'>&rarr;</span> <span class='hl'>*duplication*</span><br><span class='arrow'>&rarr;</span> old version?")),
    ]
    body = f"""
<div class="grid" style="grid-template-columns:1fr 1fr 1fr;margin-top:34px">{cards[0]}{cards[1]}{cards[2]}</div>
<div class="grid" style="grid-template-columns:1fr 1.25fr;margin-top:40px;align-items:start">{cards[3]}{cards[4]}</div>
<div class="rough quote" style="margin:44px auto 0;width:1080px;background:var(--y);transform:rotate(-.8deg)">
 Clear templates + less admin + better training = <u>more time to assess well</u>
</div>"""
    return page("ASSESSMENTS", "Meeting with the Assessors", body,
                "Sketchnote &middot; from handwritten notes")


def admin():
    pain = [
        card("!", "Role &amp; visibility", "r",
             '<div class="quote" style="padding:0 0 6px;font-size:34px">"I just answer the phones &amp; emails"</div>'
             + item("phone", "No time awareness", "Admin can't see how long marking takes")),
        card("!", "LMS status unreliable", "r",
             item("eye", "Looks unmarked", "Submissions show, but they <span class='hl'>can look unmarked</span>")
             + '<span class="tag">system inadequacy</span><span class="tag">heavy workload</span>'),
        card("!", "Inconsistent marking data", "r",
             item("chart", "Hard to monitor", "Assessors update the system themselves, so admin <span class='hl'>can't easily track assessments</span>")),
        card("!", "Wrong door", "r",
             item("wrong", "Trainers contacted", "...instead of admin")),
        card("!", "Policies?", "r",
             item("folder", "Unsure", "of the existing <span class='hl'>policies &amp; procedures</span>")),
        card("!", "Remote areas", "r",
             item("satellite", "No LMS", "<span class='hl'>Offline batch mode</span><br><span class='arrow'>&rarr; Skylink?</span>&nbsp;for remote areas or data points?")),
    ]
    help_ = [
        card("+", "More people", "g",
             item("people", "More trainers / assessors", "")
             + item("mentor", "Extra staff member", "Classroom mentor &middot; SSO")),
        card("+", "Records up to date", "g",
             item("check", "Assessors update records IMMEDIATELY", "")),
        card("+", "Student notification", "g",
             item("bell", "Transparency", "Keep students informed about their status")),
        card("+", "LMS status controls", "g",
             item("toggle", "+ TRAINING!!!!!", "Clear statuses everyone actually uses")),
        card("+", "Escalation contact", "g",
             item("ladder", "One clear person", "to escalate issues to")),
        card("+", "Workflow", "g",
             item("bolt", "\"Talk of\" automation", "for assessments...")
             + item("chat", "...prefer MESSAGING", "<span class='hl'>Less siloing</span>")),
        card("+", "Continuous improvement", "g",
             item("loop", "Monthly reports", "Toolbox talks &middot; CI")),
        card("+", "Work with QA team", "g",
             item("target", "\"Single source of truth\"", "")),
    ]
    col = lambda cards: "".join(cards)
    body = f"""
<div style="display:grid;grid-template-columns:1fr 1.25fr;gap:56px;margin-top:10px">
 <div>
  <div class="colhead"><span class="rough" style="background:var(--r)">What's hurting</span></div>
  <div class="grid" style="grid-template-columns:1fr">{col(pain)}</div>
 </div>
 <div>
  <div class="colhead"><span class="rough" style="background:var(--g)">What would help</span></div>
  <div class="grid" style="grid-template-columns:1fr 1fr">{col(help_)}</div>
 </div>
</div>
<div class="rough quote" style="margin:48px auto 0;width:1120px;background:var(--y);transform:rotate(.6deg)">
 Clear LMS status + shared info + one source of truth = <u>less chasing, more visibility</u>
</div>"""
    return page("ADMIN TEAM", "Meeting with the Administrative Team", body,
                "Sketchnote &middot; from handwritten notes")


if __name__ == "__main__":
    (HERE / "assessors-sketchnote.html").write_text(assessors())
    (HERE / "admin-team-sketchnote.html").write_text(admin())
    print("written")
