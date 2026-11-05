---
name: linkedin-company-page-audit
description: "Audits and rebuilds a LinkedIn company page for a small business, agency, or startup so it earns credibility, followers, and inbound leads. Scores 12 page elements, diagnoses where page traffic comes from, rewrites the tagline, About, specialties, button, and Products entries, and builds a founder-to-page content loop. Use when someone asks to review, audit, or fix their LinkedIn company page or business page. Not for job seekers or large-enterprise employer branding."
license: MIT
metadata:
  author: "9HEAVEN"
  version: "1.2.0"
  audience: "founders, agency owners, startups, small businesses, creators with brands"
  not_for: "job seekers, employer branding for large enterprises"
---

# LinkedIn Company Page Audit

Company pages get a small fraction of the organic reach that people get. That is the
whole strategic problem, and an audit that ignores it is decoration.

**The rule this skill enforces:** the page is a credibility and proof asset that
converts traffic sent to it. Reach comes from humans: the founder, the team, and
their reshares. Never sell the user a plan built on the page going viral on its own.

## Pick the depth

- **Quick:** the user names one piece ("rewrite our tagline", "fix our About"). Ask
  who the page is for and what visitors should do, get that text, and deliver that
  rewrite plus one line naming the next fix. No score table.
- **Full** (default for "audit our page"): Steps 1 to 6.

## Step 1: Get the page

Ask: **who should follow this page, and what do you want them to do?** For most
small businesses the honest answer is "prospects who are already mid-evaluation".
That shifts the whole content mix toward proof.

Then ask for a paste:

```
Paste what you have, labeled. Skip anything you don't know and I'll mark it
N/A instead of guessing.

1. Page name, tagline, and the About (Overview) text
2. Industry, company size, HQ location, founded year, website URL
3. Specialties list
4. Custom button: which one, and where does it point?
5. Followers; total employees; how many employees list the company on their profile
6. Last 5 posts: date, format, topic, impressions, reactions, comments
7. Products or Services tab entries, if any
8. Banner and logo: describe each in one line
9. Any Showcase pages
10. From page Analytics, last 30 days: page views, unique visitors, button clicks
```

Optional live read: company pages are public, so a logged-out read shows exactly
what a prospect sees. Follow `references/capture-page.md`. Check what a stranger
sees; never read at volume.

## Step 2: Score the page

Score each element 0–5. Weights reflect what moves leads.

| Element | Weight | Pass condition |
|---|---|---|
| Tagline | 5 | States audience and outcome within 120 characters. Shows in search and on every post. |
| Custom button | 5 | Set, and points to a converting page, not the homepage. |
| Post cadence | 5 | 2–5 posts a week, and posts get comments, not just reactions. |
| About | 4 | First 2–3 lines carry the pitch; search terms appear naturally; ends with a next step. |
| Content mix | 4 | Proof and point of view outweigh announcements. |
| Employee linkage | 4 | The founder and the team list the company on their profiles. |
| Featured customer proof | 4 | Case studies, reviews, or named results visible without much scrolling. |
| Banner | 3 | Offer or proof, readable at phone width. |
| Specialties | 3 | 10–20 filled, phrased the way buyers search, not as internal jargon. |
| Products or Services tab | 3 | Filled, with real descriptions and CTAs. |
| Logo | 2 | Square, high contrast, legible at small sizes. |
| Completeness | 2 | Website, location, size, industry, and custom URL all set. |

**Total weight: 44.**

At two people or fewer, score Employee linkage on the founder's link alone.

```
Weighted score = sum(score x weight) / (5 x sum(weight)) x 100
```

N/A elements drop out of both sums. Round to a whole number. Never score an element
0 because it was not in the paste: unknown is N/A.

Bands:

- **Under 40:** the page fails the credibility check prospects run before they buy.
  Fix the tagline, button, and About first.
- **40–59:** present but not converting. Fix the elements losing the most points
  (`weight x (5 - score)`).
- **60–79:** solid. The bottleneck is traffic, so go to Step 3 and Step 5.
- **80 and over:** stop editing the page. Put the time into founder content and the
  team habit.

## Step 3: Diagnose the traffic problem first

**Set expectations with the numbers before giving a single tactic.** Page posts
reach a small slice of the page's own followers, page organic reach fell sharply
between 2024 and early 2026, and the same content from people reaches several times
further. Quote the ranges and their grades from `references/platform-reality.md`;
never present a single figure as precise.

This is not the user's failure, and better page copy will not fix it. It changes
what the page is for. Say it plainly.

Then answer: **where do page visitors come from today?** Real sources, ranked by
what works for small businesses:

1. The founder's personal profile (its Experience entry links to the page) and
   founder posts that mention or tag it.
2. Employees and collaborators resharing page content.
3. The website footer, email signatures, and proposals.
4. Comments made as the page on relevant posts.
5. Paid promotion, only once organic proof exists.

If none of these are live, the page has no audience and copy fixes change nothing.
Say that first, then fix the copy anyway, because the page is a credibility check
people run before they buy.

## Step 4: Rewrite

Voice rules: `references/voice-rules.md`. No fabrication, no corporate filler, no
em dashes, short lines.

### Tagline (up to 120 characters)

Three options. Formula: `[What you do] for [who] | [proof or differentiator]`.
Avoid "Empowering businesses to...": it says nothing and everyone uses it.

### About (up to 2,000 characters)

1. Two lines: what you do, for whom, and the result.
2. The problem you exist to solve, in the buyer's own words.
3. Services as outcomes, one line each.
4. Proof: clients, volume, years, named results. Real numbers only.
5. Who it is for, and who it is not for.
6. An explicit CTA plus the link.

Use the terms buyers search: LinkedIn indexes this text and search engines index
the public page. Do not stuff.

### Specialties

Write them the way a prospect searches: "Shopify checkout optimization", "GST
invoicing setup", "HIPAA-ready intake forms", not "digital transformation".

### Custom button

Pick the button that matches the next step (for example Visit website, Contact us,
Learn more, Register, or Sign up). Point it at the highest-intent page that exists:
a booking link or a service page with a form, never the generic homepage.

### Products or Services tab

Underused. One entry per core offer: name, a two-line description, who it is for,
and a CTA link.

## Step 5: Build the content engine

Give a concrete 4-week plan, not "post consistently".

- **Cadence:** 3 posts a week is the floor that keeps the page from looking
  abandoned. 5 if a team supports it.
- **Mix per 10 posts:** 4 proof (case study, before and after, client result), 3
  point of view or teaching (opinion, how-to, myth-bust), 2 behind the scenes
  (process, team, build logs), 1 offer (direct pitch, launch, hiring).
- **Never post text-only from a page.** Always attach an image, document, or video:
  text-only is the weakest page format measured.
- **Links go in the first comment** on page posts, where the measured link penalty
  concentrates.
- **Formats that suit a page:** document carousels for frameworks and checklists,
  custom images for proof, and short captioned video for the team and the work.
- **Amplification on every post:** the founder reshares with an added comment within
  the hour, team members comment (not just react), and the page comments on 5
  relevant posts that week.

**People are the page's only real organic lever.** State the mechanism, not the
buzzword: LinkedIn's own figures say employees have about 10x as many connections
as the company has followers, and that the roughly 3% of employees who share drive
a 30% increase in total engagement.

What works at small scale:

- Draft the shareable content and suggested commentary, but have each person
  personalize it. Identical reshares look coordinated and perform worse.
- If the page offers an option to notify employees about a post, use it.
- Founder content usually outperforms the page by several times. If there is one
  person to invest in, it is the founder.
- At two or three people, "advocacy program" is the wrong frame. Say so, and make it
  a standing habit instead: everyone comments within the hour.
- **Repurposing:** each founder post that performs becomes a page post 3–5 days
  later with a light rewrite. The page is the archive of the founder's proof.

Hand off to `linkedin-content-strategy` for pillars and the writing system.

## Step 6: Deliver

1. Score table with the weight column visible, the weighted total and band, and the
   three elements losing the most points
2. Traffic verdict: where visitors come from today, and the single fix
3. Rewrites: 3 taglines, full About, specialties list, button choice, banner brief,
   Products entries
4. 4-week content plan: 12 concrete post ideas with formats
5. Baseline: followers, page views, unique visitors, button clicks, posts a week,
   written down today (or "not provided") so the next review has a comparison

## Anti-patterns

- Promising organic page growth without a personal-profile engine behind it.
- Recommending an "employee advocacy program" to a two-person company. Say what
  applies at their actual size.
- Filling the About with mission statements nobody reads.
- Auto-posting the website's RSS feed to the page. It reads like a bot.
- Buying followers, or running follower ads before there is anything worth following.
