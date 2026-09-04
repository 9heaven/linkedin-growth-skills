---
name: linkedin-company-page-audit
description: "Use when auditing or rebuilding a LinkedIn company page for a small business, agency, or startup so it earns followers, credibility, and inbound leads. Covers setup, copy, content engine, and the founder-to-page traffic loop."
version: 1.0.0
license: MIT
platforms: [linux, macos, windows]
metadata:
  audience: [founders, agency-owners, startups, small-business, creators-with-brands]
  not_for: [job-seekers, employer-branding-for-large-enterprises]
---

# LinkedIn Company Page Audit

Company pages get a fraction of the organic reach personal profiles get. That is
the whole strategic problem, and any audit that ignores it is decoration.

**The rule this skill enforces:** the page is a credibility and proof asset that
converts traffic sent to it. Reach comes from humans — the founder, the team,
and employee reshares. Do not sell the user a plan built on the page going viral
on its own.

## Step 1 — Get the page

Ask for a paste:

```
Paste these, labeled:
1. Page name, tagline (120 chars), and the About/Overview text
2. Industry, company size, HQ location, founded year, website URL
3. Specialties list (up to 20)
4. Custom button: which one, and where does it point?
5. Follower count, and employees listed on the page
6. Last 5 posts: date, format, topic, reactions/comments
7. Featured/Products/Services sections, if any
8. Banner and logo: describe each in one line
9. Any Showcase pages
```

Optional live read: public company pages are viewable logged out. See
`references/capture-page.md`. Use it to check what a stranger sees, not to
scrape at volume.

Then ask: **who should follow this page, and what do you want them to do?**
For most small businesses the honest answer is "prospects who are already
mid-evaluation" — that changes the entire content mix toward proof.

## Step 2 — Score the page

Score 0–5 per row. Weights reflect what actually moves leads.

| Element | Weight | Pass condition |
|---|---|---|
| Tagline (120 chars) | 5 | States audience + outcome. Shows in search and in every post. |
| About / Overview | 4 | First 2–3 lines carry the pitch; keywords appear naturally; ends with a next step. |
| Custom button | 5 | Set, and points to a converting page — not the homepage. |
| Banner | 3 | Offer or proof, readable at mobile width. |
| Logo | 2 | Square, high contrast, legible at 40px. |
| Specialties | 3 | 10–20 filled, phrased as buyers search, not as internal jargon. |
| Post cadence | 5 | 2–5 posts/week, and posts get comments not just reactions. |
| Content mix | 4 | Proof and POV outweigh announcements. |
| Employee linkage | 4 | Team members list the company; founder links to it. |
| Products/Services tab | 3 | Filled, with real descriptions and CTAs. |
| Featured customer proof | 4 | Case studies, reviews, named results visible without scrolling far. |
| Completeness signals | 2 | Website, location, size, industry, custom URL all set. |

## Step 3 — Diagnose the traffic problem first

Before copy fixes, answer: **where do page visitors come from today?**

Real sources, ranked by what works for small businesses:

1. Founder's personal profile (their Experience entry links to the page) and
   founder posts that mention or tag it.
2. Employees and collaborators reposting page content.
3. The website footer, email signature, and proposals.
4. Comments from the page on relevant posts (pages can comment as the page).
5. Paid, only once organic proof exists.

If none of these are live, the page has no audience and copy fixes change
nothing. Say that first, then fix copy anyway because the page is a
credibility check people run before they buy.

## Step 4 — Rewrite

Same voice rules as the profile skill (`references/voice-rules.md`): no
fabrication, no corporate filler, no em dashes, short lines.

### Tagline (120 chars)

Three options. Formula: `[What you do] for [who] | [proof or differentiator]`.
Avoid "Empowering businesses to..." — it says nothing and everyone uses it.

### About / Overview (2,000 chars)

1. Two lines: what you do, for whom, and the result.
2. The problem you exist to solve, in the buyer's own words.
3. Services, as outcomes with a line each.
4. Proof: clients, volume, years, named results. Real numbers only.
5. Who it is for, and who it is not for.
6. Explicit CTA plus the link.

Weave in the terms buyers search — LinkedIn indexes this text and Google
indexes the public page. Do not stuff.

### Specialties

Write them as a prospect would search: "WooCommerce speed optimization",
"GST-compliant invoicing setup", not "digital transformation".

### Custom button

Pick one: Visit website / Contact us / Learn more / Register / Sign up. Point
it at the highest-intent page that exists (booking link or a service page with
a form), never the generic homepage.

### Products / Services tab

Underused and it ranks. One entry per core offer: name, 2-line description,
who it is for, and a CTA link.

## Step 5 — Build the content engine

Give a concrete 4-week plan, not "post consistently".

- **Cadence:** 3 posts/week is the floor that keeps the page from looking
  abandoned. 5 if a team supports it.
- **Mix per 10 posts:** 4 proof (case study, before/after, client result),
  3 POV/teaching (opinion, how-to, myth-bust), 2 behind-the-scenes (process,
  team, build logs), 1 offer (direct pitch, launch, hiring).
- **Amplification, every single post:** founder reshares with an added comment
  within an hour, team members comment (not just react), and the page comments
  on 5 relevant posts that week as the page.
- **Repurposing:** each founder post that performs becomes a page post 3–5 days
  later with a small rewrite. The page is the archive of the founder's proof.

Hand off to `linkedin-content-strategy` for topic pillars and the writing
system.

## Step 6 — Deliver

1. Score table with the weight column visible
2. Traffic verdict: where visitors come from today, and the single fix
3. Rewrites: 3 taglines, full About, specialties list, button choice, banner
   brief, Products entries
4. 4-week content plan: 12 concrete post ideas with formats
5. Baseline metrics: followers, page views, unique visitors, custom-button
   clicks, posts/week — written down today so the next review has a comparison

## Anti-patterns

- Promising organic page growth without a personal-profile engine behind it.
- Recommending "employee advocacy" to a two-person company. Say what applies at
  their actual size.
- Filling the About with mission statements nobody reads.
- Auto-posting website RSS to the page. It reads like a bot and gets no reach.
- Buying followers or running follower ads before there is anything worth
  following.
