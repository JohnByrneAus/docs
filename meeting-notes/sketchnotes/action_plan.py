"""Builds the action-plan sketchnote (HTML). Reuses styles and icons from build.py.

Run:  python3 action_plan.py   then   node render.js
"""
from build import CSS, ICONS, S, HERE, item, card, page

ICONS.update({
    "toolbox": f'<svg viewBox="0 0 64 64"><rect x="6" y="22" width="52" height="32" rx="3" {S}/><path d="M22 22v-8h20v8M6 34h52M28 30h8v8h-8z" {S}/></svg>',
    "trophy": f'<svg viewBox="0 0 64 64"><path d="M18 8h28v14a14 14 0 0 1-28 0zM18 14H8c0 10 5 14 12 14M46 14h10c0 10-5 14-12 14M32 36v10M22 56h20l-2-10H24z" {S}/></svg>',
    "megaphone": f'<svg viewBox="0 0 64 64"><path d="M8 26v12h8l24 12V14L16 26z" {S}/><path d="M16 38l4 16h8l-4-14M48 24c4 2 4 14 0 16M54 18c8 6 8 22 0 28" {S}/></svg>',
    "ruler": f'<svg viewBox="0 0 64 64"><path d="M6 44L44 6l14 14-38 38z" {S}/><path d="M16 34l5 5M24 26l5 5M32 18l5 5M40 10l5 5" {S}/></svg>',
    "warn": f'<svg viewBox="0 0 64 64"><path d="M32 6L60 56H4z" {S}/><path d="M32 24v16" {S}/><circle cx="32" cy="48" r="2.5" fill="#222"/></svg>',
})

EXTRA_CSS = """
.root{margin:30px auto 0;width:1240px;padding:20px 30px;background:#fff;box-shadow:8px 9px 0 var(--r);transform:rotate(-.5deg);display:flex;align-items:center;gap:22px}
.root svg{width:70px;height:70px;flex:none}
.root b{font-family:'Permanent Marker',cursive;font-size:30px;display:block}
.root div{font-size:30px;line-height:1.2}
.tips{margin-top:14px;padding:12px 16px 10px;border:2.5px dashed #555;border-radius:14px 6px 16px 8px;background:#fffdf6}
.tips h3{font-family:'Caveat',cursive;font-size:30px;font-weight:700;margin-bottom:2px}
.tips li{font-size:23px;line-height:1.22;margin:4px 0 4px 22px}
.road{display:grid;grid-template-columns:repeat(5,1fr);gap:18px;margin-top:8px;position:relative}
.road::before{content:"";position:absolute;left:30px;right:30px;top:42px;border-top:4px dashed var(--ink)}
.step{position:relative;text-align:center}
.step .dot{width:84px;height:84px;margin:0 auto 10px;border:3px solid var(--ink);border-radius:52% 48% 50% 46%;background:var(--y);display:grid;place-items:center;font-family:'Permanent Marker',cursive;font-size:22px;line-height:1}
.step b{font-family:'Caveat',cursive;font-size:30px;display:block}
.step p{font-size:22px;line-height:1.2}
.section{font-family:'Permanent Marker',cursive;font-size:40px;text-align:center;margin:50px 0 22px}
.section span{padding:2px 24px;display:inline-block}
ul.plain{list-style:none;padding:0}
ul.plain li{font-size:24px;line-height:1.2;margin:8px 0;padding-left:30px;position:relative}
ul.plain li::before{content:"\\2713";position:absolute;left:0;font-family:'Permanent Marker',cursive}
ul.warn li::before{content:"!";left:8px}
"""


def tips(items, title="Make it work"):
    return f'<div class="tips"><h3>{title}</h3><ul>' + "".join(f"<li>{t}</li>" for t in items) + "</ul></div>"


def action_plan():
    a1 = card(1, "Admin + Assessor Taskforce", "b",
              item("people", "Work together", "Better <span class='hl'>communication</span> between departments, "
                   "<span class='hl'>continual improvement</span>, and it builds the toolkit")
              + tips([
                  "A co-lead from <b>each</b> team; add a <b>QA</b> rep",
                  "<b>Protected time</b>: meetings count as work, not extra",
                  "Fortnightly to start, then monthly",
                  "Include a voice from <b>remote / shift</b> staff",
                  "First jobs: define LMS statuses &amp; decide <b>who owns data entry</b>",
              ]))
    a2 = card(2, "Assessor Toolkit", "p",
              item("toolbox", "Uniform practice", "<span class='hl'>Feedback template</span> + consistent assessment &amp; feedback procedure")
              + item("ruler", "Put the LMS steps in it", "What each <span class='hl'>status</span> means, who updates it, <span class='hl'>within X days</span>, plus the escalation contact")
              + tips([
                  "<b>One home, one version</b>: owner, version no. &amp; review date (no more duplicates or old copies)",
                  "Pilot with a few assessors, then roll out",
                  "Keep it short: one page per process",
                  "Offline/printable copy for remote sites",
                  "Pair it with refreshed <b>aXcelerate training</b> &amp; onboarding for <b>new trainers</b>",
              ]))
    a3 = card(3, "PD Rewards System (PDRS)", "o",
              item("target", "Team hits target", "<span class='arrow'>&rarr;</span> team <span class='hl'>chooses additional PD</span>")
              + tips([
                  "<b>Baseline first</b>, then set realistic targets",
                  "Measure <b>speed + quality</b>: e.g. % results entered in X days <i>and</i> a QA sample against the toolkit",
                  "Keep required PD (industry currency / VET skills) <b>separate</b>, so rewards are truly extra",
                  "Adjust targets for <b>offline / remote</b> sites",
                  "Publish progress monthly so teams can see it",
              ]))
    a4 = card(4, "Recognition", "v",
              item("megaphone", "Toolbox talk shout-outs", "<span class='hl'>Every toolbox talk</span>: quick, specific thanks")
              + item("trophy", "Awards night: every 6 months", "<span class='hl'>Effort &middot; Improvement &middot; Excellence</span>: staff feel valued and build industry credibility")
              + tips([
                  "Tie categories to the goals (e.g. most improved LMS accuracy, best toolkit contribution)",
                  "<b>Peer nominations</b> as well as manager picks",
                  "Timing that suits <b>shift &amp; remote</b> staff (or stream it)",
                  "Certificates staff can add to their CV / portfolio",
              ]))

    road = [
        ("Month<br>0&ndash;1", "Set up", "Form taskforce &middot; pull LMS baseline &middot; explain the <i>why</i> to all staff"),
        ("Month<br>1&ndash;3", "Build", "Agree LMS statuses &amp; procedure &middot; toolkit v1 pilot &middot; training refresh"),
        ("Month<br>3", "Launch", "Toolkit rolled out &middot; PDRS targets live"),
        ("Every<br>month", "Run", "Monthly report &middot; toolbox talks + shout-outs"),
        ("Month<br>6", "Celebrate &amp; review", "1st awards night &middot; toolkit v2 &middot; reset targets"),
    ]
    road_html = '<div class="road">' + "".join(
        f'<div class="step"><div class="dot">{d}</div><b>{t}</b><p>{p}</p></div>' for d, t, p in road) + "</div>"

    measures = card("&#10003;", "How we'll know it's working", "g",
                    '<ul class="plain">'
                    "<li>% of results entered in the LMS within X days</li>"
                    "<li>Fewer submissions that <i>look unmarked</i></li>"
                    "<li>Fewer calls &amp; emails chasing results</li>"
                    "<li>QA audits: feedback consistent with the toolkit</li>"
                    "<li>Staff pulse survey: clarity, confidence, feeling valued</li>"
                    "</ul>")
    watch = card("!", "Watch-outs", "r",
                 '<ul class="plain warn">'
                 "<li><b>Workload</b>: give time, or uniform practice won't stick</li>"
                 "<li><b>Gaming</b>: speed targets without quality checks backfire</li>"
                 "<li><b>Free-riding</b>: mix team rewards with individual recognition</li>"
                 "<li><b>Change fatigue</b>: show early wins, keep it simple</li>"
                 "<li><b>Fairness</b>: remote, shift &amp; new staff included</li>"
                 "</ul>")

    body = f"""
<div class="rough root">{ICONS['target']}<div><b>Root cause</b>Trainers don't use a <span class="hl" style="--hl:var(--r)">uniform practice</span> to update the LMS with student results</div></div>
<div class="section"><span class="rough" style="background:var(--y)">4 Actions</span></div>
<div class="grid" style="grid-template-columns:1fr 1fr;align-items:start;gap:40px">{a1}{a2}{a3}{a4}</div>
<div class="section"><span class="rough" style="background:var(--b)">Roadmap</span></div>
{road_html}
<div class="grid" style="grid-template-columns:1fr 1fr;align-items:start;gap:40px;margin-top:54px">{measures}{watch}</div>
<div class="rough quote" style="margin:48px auto 0;width:1200px;background:var(--y);transform:rotate(-.6deg)">
 Work together &rarr; one way of doing it &rarr; measure it &rarr; <u>celebrate it</u>
</div>"""
    html = page("ACTION PLAN", "Assessors + Admin Team: uniform LMS results", body,
                "Sketchnote &middot; action plan from the assessor &amp; admin team meetings")
    return html.replace("</style>", EXTRA_CSS + "</style>", 1)


if __name__ == "__main__":
    (HERE / "action-plan-sketchnote.html").write_text(action_plan())
    print("written")
