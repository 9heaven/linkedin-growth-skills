---
name: linkedin-metrics-review
description: "Use when reviewing LinkedIn performance for a founder, creator, or business page: which numbers matter, how to read post and profile analytics, weekly and monthly review rituals, and what to change next. Ties activity to leads, not vanity metrics."
version: 1.1.0
license: MIT
platforms: [linux, macos, windows]
metadata:
  audience: [founders, creators, influencers, agency-owners]
  not_for: [job-seekers, follower-count-chasing]
---

# LinkedIn Metrics Review

Turn LinkedIn analytics into one decision per week. Most people track
impressions, feel bad, and change nothing. This skill fixes that by ranking
metrics by how close they sit to revenue.

## The metric hierarchy

Read bottom-up. A win at a lower tier that does not move an upper tier is not a
win.

| Tier | Metric | Why it matters |
|---|---|---|
| 1. Revenue | Clients closed, revenue from LinkedIn | The only number that ends the argument |
| 2. Pipeline | Calls booked, qualified conversations | Predicts tier 1 in 30–60 days |
| 3. Intent | Inbound DMs, comment-to-DM conversions, link clicks, lead magnet opts | Predicts tier 2 |
| 4. Interest | Profile views, search appearances, follows from target audience | Predicts tier 3 |
| 5. Attention | Impressions, reactions, comments, saves | Cheapest to move, easiest to fake |

Rule: report every review from the top down. If impressions doubled and DMs did
not move, the content reached the wrong people. Say that plainly.

## What each number is actually telling you

- **Impressions** — distribution, nothing else. High impressions with low
  profile views means the hook worked and the identity did not.
- **Reactions** — the weakest signal. Cheap to give, easy to farm.
- **Comments** — real interest, and they extend reach. Comments that ask
  questions are near-buying signals.
- **Reposts and saves** — the strongest content signals. Saves mean useful,
  reposts mean the reader staked their reputation on it.
- **Profile views after a post** — the number that links content to conversion.
  Watch it per post, not per month.
- **Search appearances + the search terms shown** — tells you whether the
  headline matches how buyers describe the problem. Mismatch means rewrite the
  headline.
- **Social Selling Index (SSI)** — at `linkedin.com/sales/ssi`, free, four components
  scored out of 25. A directional health check on whether the profile and activity
  point the right way, never a goal. Nobody was ever paid for an SSI score. If you
  report it, report the weakest component, not the total.
- **Follower demographics** (job titles, industries, company sizes) — the audit
  most people skip. If the top titles are not buyers, the content is pointed at
  the wrong crowd, and every other metric is noise.

For company pages, add: unique visitors vs page views, custom-button clicks,
and follower growth split by organic vs sponsored.

## Where to find the data

- Post analytics: on each post, "View analytics" — impressions, members reached,
  demographics per post.
- Profile analytics: profile page, "Analytics" panel — profile viewers, post
  impressions, search appearances (last 90 days).
- Creator analytics: audience growth and top posts. Available by default on eligible
  profiles since the creator-mode toggle was retired in March 2024.
- Company page: Analytics tab — visitors, followers, content, competitors,
  leads.
- Export: page analytics export to XLSX for time series. Personal profile has no
  bulk export, so keep a manual sheet.

`references/tracking-sheet.md` has a minimal weekly sheet: 12 columns, no more.
If tracking takes more than 10 minutes a week, it will be abandoned.

## The weekly review, 15 minutes

Same time every week. Five questions, in this order:

1. **How many conversations started this week?** (DMs, replies, calls booked.)
   This is the headline number, not impressions.
2. **Which post drove the most profile views?** Not the most reactions. Study
   its hook and format.
3. **Which post underperformed and why?** Hook, topic, or timing — pick one.
4. **Did the follower mix improve?** Check new followers' titles.
5. **What is the single change for next week?** One change, not five. A single
   variable is the only way to learn anything.

Log the answers. Four weeks of logs beats any dashboard.

## The monthly review, 45 minutes

- **Pillar performance:** which content pillar produced conversations, not
  impressions. Reallocate the mix toward it, but keep at least 20% on the
  others.
- **Format performance:** text vs carousel vs video, judged on saves and profile
  views.
- **Time-to-lead:** how long between first impression and DM. Tells you how many
  touches the audience needs before they act.
- **Audience audit:** follower demographics vs the target ICP. Drift here
  explains most "engagement is up but nothing converts".
- **Kill list:** what to stop doing. Every review must remove something.

## Benchmarks, used carefully

**Always show the calculation, not the raw count.**

```
Engagement rate = (reactions + comments + shares) / impressions x 100
```

15 reactions and 1 comment on 1,376 impressions is 1.16%. "16 interactions" sounds
fine; 1.16% against a 3% target does not. Report the percentage, the benchmark, and
the verdict in one row.

Rough ranges for small B2B accounts under ~10K followers. Treat as orientation,
never as targets:

- Engagement rate: 3–5% healthy, 1–2% below target. Personal profiles average
  around 4.7%; company pages sit near 1–2%.
- Profile views per 1,000 impressions: 5–15 when the hook and identity align.
- Inbound DMs: 1–5 per week at 3 posts/week with a clear offer.
- Follower growth: 100–400/month at consistent 3–5 posts/week.
- Connection acceptance rate: above 30% is healthy, below 15% means stop and fix
  targeting.

Fuller figures and their sources: `references/platform-reality.md` in
`linkedin-content-strategy`.

Own numbers over time beat anyone's benchmark. Compare the user to themselves
last month.

## Deliver

1. Tier table filled with the user's actual numbers, top-down
2. The one honest verdict: is this working, and which tier is the bottleneck
3. Best and worst post of the period, with the reason
4. Follower-mix check against the ICP
5. One change for next week, and the number it should move
6. Updated baseline for the next review

## Anti-patterns

- Reporting impressions as the headline result.
- Changing five things at once, then not knowing what worked.
- Judging a post in 2 hours. Give it 48 for a fair read, and 7 days for saves.
- Comparing to creators in other niches with other audiences.
- Tracking so many metrics that reviews stop happening.
- Concluding "LinkedIn does not work" from a 3-week sample.
