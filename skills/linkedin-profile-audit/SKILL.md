---
name: linkedin-profile-audit
description: "Audits and rewrites a personal LinkedIn profile for founders, consultants, creators, and operators so visitors become followers, leads, and clients. Scores 10 sections on a weighted rubric, names the single biggest leak, and rewrites the headline, About, Featured, current role, and banner. Use when someone asks to review, audit, score, fix, or rewrite their LinkedIn profile, headline, or About section. Not for job seekers, resumes, or ATS keywords."
license: MIT
metadata:
  author: "9HEAVEN"
  version: "1.2.0"
  audience: "founders, solopreneurs, consultants, creators, influencers, agency owners"
  not_for: "job seekers, resume writing, ATS optimization"
---

# LinkedIn Profile Audit

Audit a personal profile as a **conversion asset**, not a resume. The reader is a
potential client, partner, or follower who arrived from a post, a search, or a DM.
They decide in seconds whether to follow, book, or leave.

**Not for job seekers.** No ATS scoring, no recruiter keywords, no "seeking
opportunities" framing. If the user wants a job, say so plainly and stop: a resume
skill fits better.

## Pick the depth

- **Quick:** the user names one piece ("just my headline", "fix my About"). Ask the
  two intake questions in Step 1, get that section's text, and deliver that rewrite
  plus one line naming the next most valuable fix. No score table.
- **Full** (default for "audit my profile"): Steps 1 to 6.

## Step 1: Get the profile

Two questions decide every judgement below. Ask them first:

- **Who are you trying to attract?** Specific beats broad: "operations leads at
  20–200 person logistics companies who still run dispatch on spreadsheets" beats
  "businesses".
- **What single action should they take?** Book a call, DM a keyword, subscribe,
  or follow. One primary, one fallback. Not five.

Then ask for a paste. It always works and needs no login:

```
Paste what you have, labeled. Skip anything you don't know and I'll mark it
N/A instead of guessing.

Profile text
1. Headline (exact text)
2. About section (full)
3. Current role, plus your top 2 other Experience entries (title, company, description)
4. Featured items: titles and where each one links
5. Services section: the services listed, or "empty"
6. Your top 3 skills, and how many recommendations you have received

Visuals and setup
7. Banner: describe it in one line (or say "default")
8. Profile photo: describe it in one line
9. Custom URL set (linkedin.com/in/yourname)? Location, website, and contact info filled in?
10. Newsletter: do you run one, and how many subscribers?

Numbers (from your Analytics)
11. Followers and connections
12. Posts in the last 30 days, and for your last 5 posts: impressions, reactions, comments, reposts
13. Profile viewers and search appearances, with the period LinkedIn shows for each
```

**Optional live read:** if the user gives a public profile URL and asks you to fetch
it, read the logged-out public view. That is exactly what a stranger sees, which is
the point. Follow `references/capture-profile.md`. Never log in as the user, never
read at scale, never touch someone else's profile without a legitimate reason.

**Do not ask about "creator mode" or profile hashtags.** Both were retired in early
2024 (`references/platform-reality.md`). Asking for a setting that no longer exists
tells the user you are working from stale knowledge.

## Step 2: Classify

Record these in the report header. Step 3 depends on them.

| Field | Options | What it changes |
|---|---|---|
| Profile type | Founder / consultant or freelancer / creator or influencer / operator with a side offer | The weights (table in Step 3) |
| Target audience | Clients / partners / investors / peers and followers | The CTA and what goes in Featured slot 1 |
| Primary market | Local / national / global | Language, examples, and posting windows |
| Account size | Under or over about 10K followers | The engagement bands apply only under about 10K |

Note the industry too, but there is no reliable public benchmark per industry:
compare the user with their own history first.

If the profile type is "job seeker", stop. This skill is the wrong tool.

## Step 3: Score against the rubric

Score each section 0–5 using `references/scoring-rubric.md`. Weight matters more
than the total: fix the section losing the most points first.

| Section | Weight | The one job it does |
|---|---|---|
| Headline | 5 | Shows everywhere. Says who you help and the outcome. |
| About | 5 | Lines 1–2 are the hook; the rest sits behind "see more". |
| Activity | 5 | An empty feed makes the whole profile a dead end. |
| Featured | 4 | The only place on the profile that converts directly. |
| Banner | 3 | A free billboard: offer, proof, or credibility marker. |
| Experience (current role) | 3 | Positions the business, not the duties. |
| Photo | 2 | Face, eye contact, warm, cropped tight. |
| Skills and recommendations | 2 | Social proof and search surface. |
| Services | 2 | A free lead surface most founders leave empty. |
| Completeness | 1 | Custom URL, location, contact info, website, Follow button. |

**Total weight: 32** (defaults, before the profile-type changes below).

Adjust the weights by profile type before scoring:

| Profile type | Change | Why |
|---|---|---|
| Founder | none | The defaults are built for this case |
| Consultant or freelancer | Services 2 -> 4 | Services is a direct request path for people who sell their own time |
| Creator or influencer | Services -> N/A | The primary action is follow or subscribe; Featured slot 1 becomes the newsletter or lead magnet |
| Operator with a side offer | Experience (current role) 3 -> 1, Featured 4 -> 5 | The current role belongs to the employer and must describe that job honestly. Featured is where the side offer lives. Remind them to check the employer's social media policy |

Compute the weighted score with the formula in the rubric. Sections marked N/A drop
out of both sides of the formula. **Never score a section 0 because the data is
missing.** 0 means confirmed absent from the profile; unknown means N/A.

Report a table: section, weight, score, biggest leak, fix. Under it: the weighted
total, its band, and the three sections losing the most points.

**Compute the engagement rate, do not quote raw counts:**

```
Engagement rate = (reactions + comments + reposts) / impressions x 100
```

15 reactions and 1 comment on 1,376 impressions is 16 / 1,376 = 1.16%. That reads
very differently from "16 interactions". Compute it per post, report the median of
the last 5, and grade it against the bands in `references/platform-reality.md`.

## Step 4: Name the biggest leak

Do not hand over nine parallel fixes. State one sentence:

> "Your biggest leak is X: [what happens to the visitor because of it]."

The four leaks behind most weak founder profiles:

1. **The headline is a job title.** "Founder at Acme" tells a stranger nothing. It
   needs an audience and an outcome.
2. **The About is an autobiography.** It opens with "I have 10 years of
   experience...". The visitor does not care yet. Open with their problem.
3. **No Featured section.** The profile has no exit door, so visitors leave without
   a next step.
4. **No recent posts.** The profile is a landing page for traffic that never
   arrives, so a rewrite changes nothing.

If #4 is true, say it directly: the profile is not the bottleneck, publishing is.
Hand off to `linkedin-content-strategy`.

## Step 5: Rewrite the weak sections

Write in the user's voice, from their own words in the paste. Rules are in
`references/voice-rules.md`. Non-negotiables:

- **Zero fabrication.** Never invent a client, number, result, or credential. If a
  claim needs a number the user did not give, ask for it or leave a
  `[your number]` placeholder.
- No banned phrases ("passionate about", "results-driven", "unlock", "on a mission
  to", and the rest of the list) and no em dashes.
- Short lines. LinkedIn renders on mobile, where a 4-line paragraph is a wall.

### Headline (up to 220 characters)

Give **3 options**, each in a different frame:

- **Outcome frame:** "I help [audience] get [outcome] without [pain]"
- **Proof frame:** "[Result achieved] for [N] [audience] | [what you do now]"
- **Category frame:** "[Category you own] for [audience] | [credibility marker]"

Front-load roughly the first 60 characters: that is what shows next to the name in
comments, notifications, and search.

### About (up to 2,600 characters)

1. **Hook (lines 1–2, about 200 characters):** the visitor's problem or a specific,
   surprising claim. This is the only part shown before "see more".
2. **Agitate (2–3 lines):** what staying stuck costs them.
3. **Positioning (3–5 lines):** how you solve it and what makes the approach
   different. A concrete method beats adjectives.
4. **Proof (2–4 lines):** results, names, numbers, volume. Real ones only.
5. **Who this is for, and who it is not for:** a disqualifier builds more trust than
   a pitch.
6. **CTA (2 lines):** the single action, stated plainly, with the link or the DM
   keyword.

### Featured (pick 4)

Rank by conversion value for the profile type:

- Founder, consultant, operator: booking link or landing page, then lead magnet,
  then best-performing post, then case study, then podcast or press.
- Creator: newsletter or lead magnet, then best-performing post, then a signature
  series, then collaborations or press.

Each item needs a custom thumbnail and a title that reads as a benefit, not a
filename.

### Experience: current role

Two or three lines on who the company serves and the outcome it delivers, then
bullets of proof. Kill responsibility lists. For creators with no company, the
"role" is the body of work: audience size, output, notable collaborations. For an
operator with a side offer, keep the employer role accurate and put the offer in
Featured and the About CTA instead.

### Banner (1584 x 396 px)

Specify what to put in it, never just "improve it": offer, proof, and face or
product, readable at phone width, with the bottom-left corner kept clear because the
profile photo covers it.

## Step 6: Deliver

Output in this order, nothing else:

1. **Header:** profile type, target audience, primary market, account size, and the
   list of N/A sections
2. **Score table** (section / weight / score / leak / fix), the weighted total and
   band, and the three sections losing the most points. Mark the score
   "provisional" if N/A sections carry more than a third of the weight.
3. **The one biggest leak**, in one sentence
4. **Rewrites:** 3 headlines, full About draft, Featured list, current-role rewrite,
   banner brief
5. **Do-this-week list:** at most 5 items, ordered, each under 30 minutes
6. **Baseline to measure:** profile viewers, search appearances, and inbound DMs a
   week, written down from the paste (or "not provided")

Then offer the natural next step: `linkedin-content-strategy` if the feed is empty,
`linkedin-lead-generation` if traffic arrives but nobody converts,
`linkedin-company-page-audit` if they run a business page too.

## Anti-patterns

- Scoring every section 3/5 and calling it an audit. Be decisive: a 2 is a 2.
- Scoring a section 0 because the paste left it out. Unknown is N/A.
- Rewriting into polished corporate copy that erases the user's voice.
- Recommending "post consistently" without a topic system. That belongs to
  `linkedin-content-strategy`, and vague advice is why profiles stay dead.
- Keyword-stuffing the headline. Humans read the headline more than search does.
- Treating follower count as the goal. The goal is qualified conversations.
