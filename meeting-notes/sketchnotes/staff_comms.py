"""Builds the 5-page full-colour staff communication sketchnotes (HTML).

Run:  python3 staff_comms.py   then   node render.js
"""
from build import CSS, ICONS, S, HERE, item
import action_plan  # noqa: F401  (registers toolbox, trophy, gift-related icons)

ICONS.update({
    "calendar": f'<svg viewBox="0 0 64 64"><rect x="8" y="12" width="48" height="44" rx="4" {S}/><path d="M8 24h48M20 6v12M44 6v12M18 34h6M30 34h6M42 34h6M18 44h6M30 44h6" {S}/></svg>',
    "idcard": f'<svg viewBox="0 0 64 64"><rect x="6" y="12" width="52" height="40" rx="4" {S}/><circle cx="22" cy="28" r="6" {S}/><path d="M12 44c2-6 6-8 10-8s8 2 10 8M38 26h12M38 34h12M38 42h8" {S}/></svg>',
    "cap": f'<svg viewBox="0 0 64 64"><path d="M4 24L32 12l28 12-28 12z" {S}/><path d="M16 30v12c8 6 24 6 32 0V30M56 26v16" {S}/></svg>',
    "clipboard": f'<svg viewBox="0 0 64 64"><rect x="12" y="10" width="40" height="48" rx="3" {S}/><path d="M24 6h16v8H24zM20 26l3 3 6-6M34 26h12M20 40l3 3 6-6M34 40h12" {S}/></svg>',
    "piggy": f'<svg viewBox="0 0 64 64"><path d="M10 34c0-10 10-18 22-18 8 0 14 3 18 8h6v10h-4c-1 4-3 7-6 9v7h-8v-4h-12v4h-8v-8c-5-2-8-5-8-8z" {S}/><path d="M28 16v-6M24 10h8M44 30v.1" {S}/></svg>',
    "coin": f'<svg viewBox="0 0 64 64"><ellipse cx="32" cy="32" rx="22" ry="22" {S}/><path d="M38 22c-2-2-4-3-7-3-4 0-7 2-7 6 0 8 15 4 15 12 0 4-3 6-8 6-3 0-6-1-8-3M31 14v6M31 44v6" {S}/></svg>',
    "star": f'<svg viewBox="0 0 64 64"><path d="M32 6l7 17 18 1-14 12 5 18-16-10-16 10 5-18L7 24l18-1z" {S}/></svg>',
    "gift": f'<svg viewBox="0 0 64 64"><rect x="8" y="24" width="48" height="12" {S}/><path d="M12 36v22h40V36M32 24v34M32 24c-6-12-18-12-16-4 1 4 10 4 16 4 6 0 15 0 16-4 2-8-10-8-16 4" {S}/></svg>',
    "gears": f'<svg viewBox="0 0 64 64"><circle cx="24" cy="26" r="9" {S}/><path d="M24 8v6M24 38v6M6 26h6M36 26h6M11 13l4 4M33 35l4 4M37 13l-4 4M15 35l-4 4" {S}/><circle cx="46" cy="46" r="6" {S}/><path d="M46 34v4M46 54v4M34 46h4M54 46h4" {S}/></svg>',
    "sheet": f'<svg viewBox="0 0 64 64"><rect x="8" y="8" width="48" height="48" rx="3" {S}/><path d="M8 22h48M8 36h48M24 8v48M40 8v48" {S}/></svg>',
    "mail": f'<svg viewBox="0 0 64 64"><rect x="6" y="14" width="52" height="36" rx="3" {S}/><path d="M6 16l26 20 26-20" {S}/></svg>',
    "peak": f'<svg viewBox="0 0 64 64"><path d="M4 54l16-26 10 12 12-26 18 40z" {S}/><path d="M38 20l4-6 4 6" {S}/></svg>',
    "heart": f'<svg viewBox="0 0 64 64"><path d="M32 56S8 40 8 22c0-8 6-14 13-14 5 0 9 3 11 7 2-4 6-7 11-7 7 0 13 6 13 14 0 18-24 34-24 34z" {S}/></svg>',
})

EXTRA = """
body{position:relative}
.pg{position:absolute;top:30px;right:44px;font-family:'Permanent Marker',cursive;font-size:24px;background:#fff;padding:6px 18px;transform:rotate(3deg)}
.pg::before{border-width:2.5px}
.fill{background:var(--bg)!important}
.why{margin:26px auto 0;width:1300px;padding:18px 28px;background:#fff;box-shadow:8px 9px 0 var(--r);transform:rotate(-.5deg);display:flex;gap:22px;align-items:center}
.why svg{width:66px;height:66px;flex:none}
.why div{font-size:29px;line-height:1.22}
.why b{font-family:'Permanent Marker',cursive;font-size:28px;display:block}
.sec{font-family:'Permanent Marker',cursive;font-size:40px;text-align:center;margin:46px 0 22px}
.sec span{padding:2px 24px;display:inline-block}
.mini{font-size:24px;line-height:1.22}
.mini b{font-family:'Caveat',cursive;font-size:30px}
.when{display:inline-block;font-family:'Caveat',cursive;font-weight:700;font-size:26px;background:#fff;border:2.5px solid var(--ink);border-radius:18px 8px 16px 10px/10px 16px 8px 18px;padding:0 12px;margin:2px 0 6px}
ul.dots{margin:6px 0 0 26px}
ul.dots li{font-size:24px;line-height:1.22;margin:5px 0}
.flow{display:flex;align-items:stretch;justify-content:center;gap:0;margin-top:10px}
.flow .node{flex:1;text-align:center;padding:16px 12px 14px;box-shadow:6px 7px 0 var(--ink)}
.flow .node svg{width:70px;height:70px}
.flow .node b{font-family:'Permanent Marker',cursive;font-size:25px;display:block;margin:4px 0}
.flow .node p{font-size:22px;line-height:1.2}
.flow .arr{flex:none;width:70px;display:grid;place-items:center;font-family:'Permanent Marker',cursive;font-size:48px}
.folders{display:grid;grid-template-columns:repeat(5,1fr);gap:20px}
.folder{position:relative;padding:44px 14px 16px;text-align:center;border:3px solid var(--ink);border-radius:6px 14px 8px 12px;background:var(--bg)}
.folder::before{content:"";position:absolute;top:-20px;left:-3px;width:46%;height:22px;border:3px solid var(--ink);border-bottom:none;border-radius:10px 14px 0 0;background:var(--bg)}
.folder b{font-family:'Permanent Marker',cursive;font-size:24px;display:block;line-height:1.1}
.folder p{font-size:22px;line-height:1.2;margin-top:6px}
.roles{display:grid;grid-template-columns:repeat(4,1fr);gap:26px}
.role{padding:18px 16px;text-align:center;background:var(--bg);box-shadow:6px 7px 0 var(--ink)}
.role:nth-child(odd){transform:rotate(-.8deg)}.role:nth-child(even){transform:rotate(.8deg)}
.role svg{width:66px;height:66px}
.role b{font-family:'Permanent Marker',cursive;font-size:23px;display:block;line-height:1.1;margin:4px 0 6px}
.role p{font-size:22px;line-height:1.2}
.triad{display:flex;justify-content:center;gap:30px;margin-top:20px}
.blob{width:300px;padding:22px 10px;text-align:center;border:3px solid var(--ink);border-radius:50% 46% 52% 48%/48% 52% 46% 50%;background:var(--bg);font-family:'Permanent Marker',cursive;font-size:32px}
.blob small{display:block;font-family:'Patrick Hand';font-size:22px;margin-top:4px}
.path{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.stepc{display:flex;gap:14px;align-items:flex-start;padding:16px 16px;background:var(--bg);box-shadow:6px 7px 0 var(--ink)}
.stepc .n{flex:none;width:52px;height:52px;border:3px solid var(--ink);border-radius:50% 46% 52% 48%;background:#fff;display:grid;place-items:center;font-family:'Permanent Marker',cursive;font-size:26px}
.stepc p{font-size:23px;line-height:1.2}
.stepc b{font-family:'Caveat',cursive;font-size:29px;display:block;line-height:1}
.yesno{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:6px}
.qa{display:grid;grid-template-columns:1fr 1fr;gap:26px}
.qa .q{padding:16px 20px;background:var(--bg);box-shadow:6px 7px 0 var(--ink)}
.qa .q b{font-family:'Caveat',cursive;font-size:30px;display:block}
.qa .q p{font-size:23px;line-height:1.22}
"""

C = {"y": "#ffe27a", "b": "#a9d8f5", "g": "#b9e8a3", "p": "#f7b6c8", "o": "#ffc98b", "v": "#d4c2f5", "r": "#ff8f8f", "t": "#9fe3d6"}
L = {"y": "#fff3c4", "b": "#dcf0fc", "g": "#e2f6d8", "p": "#fde0e8", "o": "#ffe6c9", "v": "#ece3fb", "r": "#ffd9d9", "t": "#d9f5ef"}


def fcard(num, title, col, inner, style=""):
    return (f'<section class="card rough fill" style="--sh:{C[col]};--hl:{C[col]};--bg:{L[col]};{style}">'
            f'<h2><span class="num" style="background:{C[col]}">{num}</span>{title}</h2>{inner}</section>')


def doc(title, sub, n, accent, body):
    css = CSS.replace("background:var(--y);z-index:-1", f"background:{C[accent]};z-index:-1") + EXTRA
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{css}</style></head><body>
<div class="pg rough">Page {n} of 5</div>
<header class="title"><h1>{title}</h1><p>{sub}</p></header>
{body}
<p class="foot">Staff update &middot; Assessment &amp; LMS improvement initiatives &middot; {n}/5</p>
</body></html>"""


def overview():
    cards = [
        fcard(1, "Assessor Toolkit", "b",
              item("toolbox", "One way of working", "Planner, templates &amp; reviews so everyone records results the <span class='hl'>same way</span>")
              + '<p class="mini"><b>For you:</b> clear time for prep, delivery &amp; review, plus ready-made templates</p>'),
        fcard(2, "Joint Taskforce", "t",
              item("people", "Cross-team group", "Assessors, admin, LMS expert, QA, students &amp; more <span class='hl'>build &amp; improve</span> the toolkit")
              + '<p class="mini"><b>For you:</b> less double handling, fairer workload in peak weeks</p>'),
        fcard(3, "Organisational Awards Night", "p",
              item("trophy", "Celebrate together", "Recognise individuals &amp; teams across the <span class='hl'>whole RTO</span>")
              + '<p class="mini"><b>For you:</b> your effort seen, valued &amp; celebrated</p>'),
        fcard(4, "PD Rewards System", "o",
              item("gift", "Hit your KPI = extra PD", "<span class='hl'>Your choice</span> of PD, on top of your normal entitlement")
              + '<p class="mini"><b>For you:</b> a real reward for orderly, current LMS records</p>'),
    ]
    flow = [
        ("t", "people", "Taskforce", "builds &amp; reviews"),
        ("b", "toolbox", "Toolkit", "everyone uses it"),
        ("y", "laptop", "Current LMS", "accurate records"),
        ("o", "gift", "PDRS", "rewards KPIs"),
        ("p", "trophy", "Awards Night", "celebrates success"),
    ]
    fl = '<div class="flow">' + '<div class="arr">&rarr;</div>'.join(
        f'<div class="node rough" style="background:{L[c]}">{ICONS[i]}<b>{t}</b><p>{p}</p></div>' for c, i, t, p in flow) + "</div>"
    body = f"""
<div class="rough why">{ICONS['question']}<div><b>Why are we changing?</b>Trainers don't all follow the <span class="hl" style="--hl:{C['r']}">same practice</span> when updating the LMS with student results. Records look unmarked, data is inconsistent and work gets handled twice.</div></div>
<div class="sec"><span class="rough" style="background:{C['y']}">4 innovations</span></div>
<div class="grid" style="grid-template-columns:1fr 1fr;gap:40px;align-items:start">{''.join(cards)}</div>
<div class="sec"><span class="rough" style="background:{C['t']}">How they fit together</span></div>
{fl}
<div class="rough quote" style="margin:56px auto 0;width:1200px;background:{C['y']};transform:rotate(-.6deg)">
 People + processes + technology = <u>consistent, current records for every student</u>
</div>"""
    return doc("WHAT'S CHANGING", "Four innovations to make assessment &amp; LMS records consistent", 1, "y", body)


def toolkit():
    tools = [
        fcard("A", "4-Term Delivery &amp; Workload Planner", "b",
              '<span class="when">Before each term &middot; with the taskforce</span>'
              + item("calendar", "Plan only what you'll deliver", "Narrow down <span class='hl'>delivery methods</span> and map out each term")
              + '<ul class="dots"><li>Set aside time for <b>preparation, implementation &amp; review</b></li>'
                '<li>Shows your <b>capacity</b>: what you can deliver &amp; cohort size</li></ul>'),
        fcard("B", "Student Communication Template / Profiles", "t",
              '<span class="when">At every catch-up, query or resubmission</span>'
              + item("idcard", "Record it, file it", "Saved in the <span class='hl'>student profile / folder</span>")
              + '<ul class="dots"><li>One accurate record for <b>trainers, assessors &amp; workplace mentors</b></li></ul>'),
        fcard("C", "Assessment Feedback Template", "g",
              '<span class="when">As soon as you&rsquo;re notified of a submission</span>'
              + item("doc", "Clear, consistent feedback", "What's marked <span class='hl'>Competent</span>")
              + '<ul class="dots"><li>For units <b>not yet competent</b>: the required detail of <b>why</b></li></ul>'),
        fcard("D", "Bi-monthly Trainer Review", "v",
              '<span class="when">After each term &middot; reviewed by the taskforce</span>'
              + item("loop", "Where is each cohort at?", "Which cohorts are <span class='hl'>meeting quota</span>?")
              + '<ul class="dots"><li>Spot <b>gaps</b> &amp; where trainers need support</li>'
                '<li>Find <b>who can help</b>, e.g. other assessors marking written work while you do practicals</li></ul>'),
    ]
    folders = [
        ("y", "Templates", "Enrolment &middot; timetables &middot; student communication"),
        ("b", "Training &amp; delivery materials", "Sorted by year &amp; term"),
        ("g", "Feedback records", "Assessment feedback, all in one place"),
        ("t", "Cohorts / students", "Profiles &amp; communication records"),
        ("p", "Term &amp; yearly reviews", "Organisational review outcomes"),
    ]
    fhtml = '<div class="folders">' + "".join(
        f'<div class="folder" style="--bg:{L[c]}"><b>{t}</b><p>{p}</p></div>' for c, t, p in folders) + "</div>"
    body = f"""
<div class="rough why" style="box-shadow:8px 9px 0 {C['b']}">{ICONS['toolbox']}<div><b>What is it?</b>A set of planners, templates and reviews so <span class="hl" style="--hl:{C['b']}">everyone plans, assesses, gives feedback and records results the same way</span>.</div></div>
<div class="sec"><span class="rough" style="background:{C['b']}">What's in the toolkit</span></div>
<div class="grid" style="grid-template-columns:1fr 1fr;gap:40px;align-items:start">{''.join(tools)}</div>
<div class="sec"><span class="rough" style="background:{C['y']}">&darr; Leads to a structured filing system &darr;</span></div>
{fhtml}
<div class="rough quote" style="margin:56px auto 0;width:1200px;background:{C['b']};transform:rotate(.6deg)">
 Plan it &rarr; record it &rarr; give feedback &rarr; review it &rarr; <u>file it</u>
</div>"""
    return doc("THE TOOLKIT", "Innovation 1: one consistent way to plan, assess &amp; record", 2, "b", body)


def taskforce():
    roles = [
        ("v", "check", "Quality Assurance Rep", "Compliance, assessment quality &amp; CQI"),
        ("b", "class", "Trainers &amp; Assessors", "Practical delivery, workload &amp; the assessment process"),
        ("g", "book", "Content / Subject Expert", "Learning resources, assessment content &amp; industry relevance"),
        ("t", "laptop", "LMS / Systems Specialist", "Tracking, reporting, access, submission dates &amp; real-time feedback"),
        ("y", "person", "Student Rep", "Student experience, communication &amp; feedback"),
        ("o", "mentor", "Workplace Mentors", "Workplace relevance &amp; competency support"),
        ("p", "cap", "Alumni Rep", "Graduate experience &amp; improving training"),
        ("r", "clipboard", "Taskforce Coordinator", "Meetings, actions register &amp; monitoring"),
    ]
    rhtml = '<div class="roles">' + "".join(
        f'<div class="role rough" style="--bg:{L[c]}">{ICONS[i]}<b>{t}</b><p>{p}</p></div>' for c, i, t, p in roles) + "</div>"
    fixes = fcard("&#10003;", "What changes", "g",
                  item("sheet", "No more double handling", "Between the <span class='hl'>LMS, email &amp; the shared spreadsheet</span>")
                  + item("peak", "Fair work in peak weeks", "Better <span class='hl'>allocation of work</span> when it's busiest")
                  + item("toolbox", "Builds the toolkit", "&hellip;and keeps improving it"))
    how = fcard("?", "How it works", "t",
                item("people", "Reps from across the RTO", "Work together on <span class='hl'>one shared plan</span>")
                + item("clipboard", "Actions register", "The coordinator tracks every action to completion")
                + item("loop", "Reviews each term", "Cohort progress, gaps &amp; support needs"))
    body = f"""
<div class="rough why" style="box-shadow:8px 9px 0 {C['t']}">{ICONS['people']}<div><b>What is it?</b>A cross-team group of <span class="hl" style="--hl:{C['t']}">assessors, an LMS expert and administration staff</span>, plus other voices, that builds the toolkit and improves the process.</div></div>
<div class="triad"><div class="blob" style="--bg:{L['p']}">People<small>the right voices in the room</small></div><div class="blob" style="--bg:{L['y']}">Processes<small>one agreed way of working</small></div><div class="blob" style="--bg:{L['b']}">Technology<small>an LMS that works for us</small></div></div>
<div class="sec"><span class="rough" style="background:{C['t']}">Who's on the taskforce</span></div>
{rhtml}
<div class="grid" style="grid-template-columns:1fr 1fr;gap:40px;align-items:start;margin-top:52px">{fixes}{how}</div>
<div class="rough quote" style="margin:52px auto 0;width:1200px;background:{C['t']};transform:rotate(-.6deg)">
 Different roles, one team, <u>one source of truth</u>
</div>"""
    return doc("THE TASKFORCE", "Innovation 2: assessors, LMS expert &amp; admin working as one", 3, "t", body)


def awards():
    steps = [
        ("Working group", "Reps from different teams &amp; departments"),
        ("Purpose &amp; format", "Agree objectives &amp; how the night runs"),
        ("Award categories", "Aligned to our values, mission &amp; vision"),
        ("Ask staff", "What recognition matters to you?"),
        ("Budget", "Venue, catering, awards &amp; other costs"),
        ("Logistics", "Venue, invitations, nominations &amp; promotion"),
        ("Fair nominations", "Transparent, inclusive &amp; open to all staff"),
        ("The program", "Presentations celebrating teams &amp; individuals"),
        ("Feedback", "Evaluate the impact &amp; improve next time"),
    ]
    cols = ["p", "o", "y", "g", "t", "b", "v", "p", "o"]
    shtml = '<div class="path">' + "".join(
        f'<div class="stepc rough" style="--bg:{L[cols[k]]}"><span class="n">{k+1}</span><p><b>{t}</b>{p}</p></div>'
        for k, (t, p) in enumerate(steps)) + "</div>"
    why = [
        ("star", "Celebrate", "achievements of individuals &amp; teams"),
        ("heart", "Culture", "a stronger, positive organisational culture"),
        ("people", "Collaborate", "across departments"),
        ("target", "Shared purpose", "&amp; a sense of belonging"),
    ]
    whtml = '<div class="roles">' + "".join(
        f'<div class="role rough" style="--bg:{L[c]}">{ICONS[i]}<b>{t}</b><p>{p}</p></div>'
        for c, (i, t, p) in zip(["p", "y", "t", "o"], why)) + "</div>"
    body = f"""
<div class="rough why" style="box-shadow:8px 9px 0 {C['p']}">{ICONS['trophy']}<div><b>What is it?</b>A night for <span class="hl" style="--hl:{C['p']}">all staff across the RTO</span> to come together, celebrate achievements and recognise contributions towards our mission and vision.</div></div>
<div class="sec"><span class="rough" style="background:{C['p']}">Why we're doing it</span></div>
{whtml}
<div class="sec"><span class="rough" style="background:{C['y']}">How we'll make it happen</span></div>
{shtml}
<div class="grid" style="grid-template-columns:1fr;margin-top:50px">
{fcard("&#9733;", "The long-term goal", "v", item("calendar", "An annual RTO event", "Supporting <span class='hl'>staff engagement</span>, recognising positive contributions &amp; strengthening <span class='hl'>collaboration</span>"))}
</div>
<div class="rough quote" style="margin:52px auto 0;width:1200px;background:{C['p']};transform:rotate(.6deg)">
 Your effort matters. <u>Let's celebrate it together.</u>
</div>"""
    return doc("AWARDS NIGHT", "Innovation 3: Organisational Awards Night (OAN)", 4, "p", body)


def pdrs():
    flow = [
        ("b", "toolbox", "Follow the toolkit", "orderly, current LMS records"),
        ("g", "target", "Hit your KPI", "for the month"),
        ("o", "gift", "Choose extra PD", "your pick, on top of baseline PD"),
    ]
    fl = '<div class="flow">' + '<div class="arr">&rarr;</div>'.join(
        f'<div class="node rough" style="background:{L[c]}">{ICONS[i]}<b>{t}</b><p>{p}</p></div>' for c, i, t, p in flow) + "</div>"
    yes = fcard("&#10003;", "Within the price range?", "g",
                item("star", "Go for it!", "Book your PD activity"))
    no = fcard("$", "Costs more than the allowance?", "y",
               item("piggy", "Bank it", "Save your incentive and combine it later")
               + item("coin", "Or pay the difference", "Top it up yourself"))
    qa = [
        ("Who is it for?", "Assessors who meet their monthly Key Performance Indicators (KPIs)."),
        ("Does it replace my PD?", "No. It's <strong>in addition to</strong> your baseline PD requirements &amp; entitlements."),
        ("Does it have to relate to my job?", "No. It's <strong>your choice</strong>, and it may not be directly related to your position."),
        ("Why are we doing this?", "To reward following the toolkit and keeping <strong>orderly, current LMS records</strong>."),
    ]
    qhtml = '<div class="qa">' + "".join(
        f'<div class="q rough" style="--bg:{L[c]}"><b>{q}</b><p>{a}</p></div>'
        for c, (q, a) in zip(["b", "v", "t", "p"], qa)) + "</div>"
    body = f"""
<div class="rough why" style="box-shadow:8px 9px 0 {C['o']}">{ICONS['gift']}<div><b>What is it?</b>A reward system triggered when assessors meet their KPIs. <span class="hl" style="--hl:{C['o']}">Hit your monthly KPI and choose an extra PD activity.</span></div></div>
<div class="sec"><span class="rough" style="background:{C['o']}">How it works</span></div>
{fl}
<div class="sec"><span class="rough" style="background:{C['y']}">Paying for it</span></div>
<p class="mini" style="text-align:center;font-size:27px;margin-bottom:22px">Each PD activity has a set <b>price range</b>.</p>
<div class="yesno">{yes}{no}</div>
<div class="sec"><span class="rough" style="background:{C['b']}">Quick Q&amp;A</span></div>
{qhtml}
<div class="rough quote" style="margin:52px auto 0;width:1200px;background:{C['o']};transform:rotate(-.6deg)">
 Good records &rarr; KPI met &rarr; <u>PD you choose</u>
</div>"""
    return doc("PD REWARDS", "Innovation 4: Professional Development Rewards System (PDRS)", 5, "o", body)


PAGES = {
    "staff-comms-1-overview": overview,
    "staff-comms-2-toolkit": toolkit,
    "staff-comms-3-taskforce": taskforce,
    "staff-comms-4-awards-night": awards,
    "staff-comms-5-pdrs": pdrs,
}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        (HERE / f"{name}.html").write_text(fn())
    print("written")
