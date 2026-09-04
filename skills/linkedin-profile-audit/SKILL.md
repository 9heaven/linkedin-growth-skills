---
name: linkedin-profile-audit
description: "Use when auditing or rewriting a founder, creator, or influencer LinkedIn profile so visitors convert into followers, leads, and clients. Scores every section against a buyer-journey rubric and rewrites the weak ones."
version: 1.1.0
license: MIT
platforms: [linux, macos, windows]
metadata:
  audience: [founders, solopreneurs, creators, influencers, consultants, agency-owners]
  not_for: [job-seekers, resume-writing, ats-optimization]
---

# LinkedIn Profile Audit (Founders, Creators, Operators)

Audit a personal LinkedIn profile as a **conversion asset**, not a resume. The
reader is a potential client, partner, or follower who arrived from a post,
a search, or a DM. They decide in under 15 seconds whether to follow, book, or
leave.

**This skill is not for job seekers.** No ATS scoring, no recruiter keywords,
no "seeking opportunities" framing. If the user wants a job, say so plainly and
stop — a resume skill fits better.

## Step 1 — Get the profile

Ask for a paste first; it always works and needs no login:

```
Paste these, each labeled:
1. Headline (exact text)
2. About section (full)
3. Top 3 Experience entries (title, company, and the description text)
4. Featured section items (titles + what they link to)
5. Banner image: describe it in one line (or say "default blue")
6. Profile photo: describe it in one line
7. Follower count, connection count, and how many posts in the last 30 days
8. Custom URL (linkedin.com/in/...) — yes or no
9. Services section — set up, or empty?
10. Newsletter — do you run one?
```

**Do not ask about "creator mode".** LinkedIn removed the toggle in March 2024 and
profile hashtags/"Talks about" topics in February 2024. Its features (newsletter,
Follow button, creator analytics) are on by default for eligible profiles. Asking
for a setting that no longer exists tells the user you are working from stale
knowledge. See `references/platform-reality.md`.

## Step 1b — Classify before you score

Record these four in the report header. Every judgement below changes based on them,
and an audit that skips them applies the wrong benchmarks.

| Field | Options |
|---|---|
| **Profile type** | Founder / consultant-freelancer / creator-influencer / operator with a side offer |
| **Industry** | Determines which engagement benchmarks apply |
| **Target audience** | Clients / partners / investors / peers-and-followers |
| **Primary market** | Local, national, or global — affects language and posting windows |

If the answer to profile type is "job seeker", stop. This skill is the wrong tool.

Then ask the two questions that decide every judgement below:

- **Who are you trying to attract?** Specific: "D2C brand owners in India doing
  ₹50L–₹5Cr who bleed money on a slow WooCommerce store" beats "businesses".
- **What single action should they take?** Book a call / DM a keyword / join the
  newsletter / follow. One primary, one fallback. Not five.

**Optional live read:** if the user gives a public profile URL and asks you to
fetch it, open it with the browser tool logged out and read the public view —
this is exactly what a stranger sees, which is the point. See
`references/capture-profile.md`. Never log in as the user, never scrape at
scale, never touch profiles that are not the user's own without permission.

## Step 2 — Score against the rubric

Score each section 0–5 using `references/scoring-rubric.md`. Weight matters more
than the total: fix the highest-weight low score first.

| Section | Weight | The one job it does |
|---|---|---|
| Headline | 5 | Appears everywhere. Must say who you help + the outcome. |
| Banner | 3 | Free billboard: proof, offer, or credibility marker. |
| About | 5 | First 2 lines are the hook (rest is behind "see more"). |
| Featured | 4 | The only place on the profile that converts directly. |
| Experience (current) | 3 | Positions the business, not the duties. |
| Photo | 2 | Face, eye contact, warm, cropped tight. |
| Activity/posts | 5 | An empty feed makes the whole profile a dead end. |
| Skills + recommendations | 2 | Social proof and search surface. |
| Custom URL + contact info | 1 | Cheap, one-time fixes. |
| Services section | 2 | Free lead surface most founders leave empty. |

Report as a table: section, score, the biggest single leak, the fix.

**Compute the engagement rate, do not just quote raw numbers.**

```
Engagement rate = (reactions + comments + shares) / impressions x 100
```

A post with 15 reactions on 1,376 impressions is 1.16%, which is below target — and
that reads very differently from "15 reactions". For small B2B accounts, 3–5% is
healthy and 1–2% needs work. Benchmarks in `references/platform-reality.md`.

## Step 3 — Name the biggest leak

Do not hand over nine parallel fixes. State one sentence:

> "Your biggest leak is X: [what happens to the visitor because of it]."

The four leaks that account for most weak founder profiles:

1. **Headline is a job title.** "Founder at Acme" tells a stranger nothing. It
   must carry an audience and an outcome.
2. **About is an autobiography.** Opens with "I have 10 years of experience..."
   The visitor does not care yet. Open with their problem.
3. **No Featured section.** The profile has no exit door — visitors leave
   without a next step.
4. **No recent posts.** Profile is a landing page for traffic that never
   arrives. No content means no visitors means the rewrite changes nothing.

If #4 is true, say it directly: the profile is not the bottleneck, publishing
is. Hand off to `linkedin-content-strategy`.

## Step 4 — Rewrite the weak sections

Write in the user's voice, using their own words from the paste. Rules in
`references/voice-rules.md`. Non-negotiables:

- **Zero fabrication.** Never invent a client, a number, a result, or a
  credential. If a claim needs a number the user did not give, ask for it or
  leave a `[your number]` placeholder.
- No em dashes, no "unlock", "elevate", "passionate about", "results-driven",
  "wearing many hats", "on a mission to".
- Short lines. LinkedIn renders on mobile — a 4-line paragraph is a wall.

### Headline (220 chars)

Give **3 options**, each in a different frame:

- **Outcome frame:** "I help [audience] get [outcome] without [pain]"
- **Proof frame:** "[Result achieved] for [N] [audience] | [what you do now]"
- **Category frame:** "[Category you own] for [audience] | [credibility marker]"

Front-load the first 60 characters. That is all that shows in search results,
comments, and notifications.

### About (2,600 chars)

Structure:

1. **Hook (lines 1–2, ~200 chars):** the visitor's problem or a specific,
   surprising claim. This is the only part shown before "see more".
2. **Agitate (2–3 lines):** what it costs them to stay stuck.
3. **Positioning (3–5 lines):** how you solve it, what makes your approach
   different. Concrete method beats adjectives.
4. **Proof (2–4 lines):** results, names, numbers, volume. Only real ones.
5. **Who this is for / not for:** a disqualifier builds more trust than a
   sales pitch.
6. **CTA (2 lines):** the single action, stated plainly, with the link or the
   DM keyword.

### Featured (pick 4)

Rank by conversion value: booking link or landing page > lead magnet >
best-performing post > case study > podcast/press. Each needs a custom
thumbnail and a title that reads as a benefit, not a filename.

### Experience — current role

Two or three lines about who the company serves and the outcome it delivers,
then bullets of proof. Kill responsibility lists. For creators with no company,
the "role" is the body of work: audience size, output, notable collaborations.

### Banner

Specify what to put in it, do not just say "improve it": offer + proof + face
or product, readable at thumbnail size, with the bottom-left corner kept clear
because the profile photo covers it on desktop.

## Step 5 — Deliver

Output in this order, nothing else:

1. **Score table** (section / score / leak / fix)
2. **The one biggest leak**, one sentence
3. **Rewrites**: 3 headlines, full About draft, Featured list, current-role
   rewrite, banner brief
4. **Do-this-week list**: max 5 items, ordered, each under 30 minutes
5. **What to measure**: profile views, search appearances, and DMs per week,
   with today's baseline written down

Then offer the natural next step: `linkedin-content-strategy` if the feed is
empty, `linkedin-lead-generation` if traffic arrives but nobody converts,
`linkedin-company-page-audit` if they run a business page too.

## Anti-patterns

- Scoring every section 3/5 and calling it an audit. Be decisive; a 2 is a 2.
- Rewriting into polished corporate copy that erases the user's voice.
- Recommending "post consistently" without a topic system — that belongs to
  the content-strategy skill, and vague advice is why profiles stay dead.
- Keyword-stuffing the headline. LinkedIn search rewards relevance, and humans
  read the headline more than the algorithm does.
- Treating follower count as the goal. The goal is qualified conversations.
