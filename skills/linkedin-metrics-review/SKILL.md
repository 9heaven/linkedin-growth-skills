---
name: linkedin-metrics-review
description: "Reviews LinkedIn performance for founders, creators, and business pages by ranking metrics from revenue down to impressions, computing engagement rates properly, running weekly and monthly review rituals, and ending with one change for next week. Use when someone shares LinkedIn analytics, asks how their posts or profile are doing, whether LinkedIn is working, or what to track. Ties activity to leads, not vanity metrics. Not for job seekers or follower-count chasing."
license: MIT
metadata:
  author: "9HEAVEN"
  version: "1.2.0"
  audience: "founders, creators, influencers, agency owners"
  not_for: "job seekers, follower-count chasing"
---

# LinkedIn Metrics Review

Turn LinkedIn analytics into one decision a week. Most people track impressions,
feel bad, and change nothing. This skill fixes that by ranking metrics by how close
they sit to revenue.

## Pick the depth

- **Quick:** one post or one number ("how did this post do?"). Compute its
  engagement rate, grade it, name the likely reason (hook, topic, format, or
  timing), and give one change. Then offer the full review.
- **Full** (default): the hierarchy, the weekly or monthly review, and the delivery
  below.

## The metric hierarchy

Read from the bottom up; report from the top down. A win at a lower tier that does
not move an upper tier is not a win.

| Tier | Metric | Why it matters |
|---|---|---|
| 1. Revenue | Clients closed, revenue from LinkedIn | The only number that ends the argument |
| 2. Pipeline | Calls booked, qualified conversations | Predicts tier 1 in 30–60 days |
| 3. Intent | Inbound DMs, comment-to-DM conversions, link clicks, lead-magnet opt-ins | Predicts tier 2 |
| 4. Interest | Profile views, search appearances, follows from the target audience | Predicts tier 3 |
| 5. Attention | Impressions, reactions, comments, reposts, saves | Cheapest to move, easiest to fake |

If impressions doubled and DMs did not move, the content reached the wrong people.
Say that plainly.

## What each number is actually telling you

- **Impressions:** distribution, nothing else. High impressions with few profile
  views means the hook worked and the identity did not.
- **Reactions:** the weakest signal. Cheap to give, easy to farm.
- **Comments:** real interest. Comments that ask questions are near-buying signals.
- **Reposts, saves, and sends:** the strongest content signals. Saves mean useful;
  reposts mean the reader staked their reputation on it.
- **Profile views after a post:** the number that links content to conversion.
  Watch it per post, not per month.
- **Search appearances and the search terms shown:** whether the headline matches
  how buyers describe the problem. A mismatch means rewrite the headline.
- **Social Selling Index (SSI):** free at `linkedin.com/sales/ssi`, four components
  scored out of 25. A directional health check, never a goal. If you report it,
  report the weakest component, not the total.
- **Follower demographics** (job titles, industries, company sizes): the check most
  people skip. If the top titles are not buyers, the content is pointed at the wrong
  crowd and every other metric is noise.

For company pages, add unique visitors vs page views, custom-button clicks, and
follower growth split by organic vs sponsored.

## Where to find the data

- **Post analytics:** "View analytics" on each post: impressions, members reached,
  reactions, comments, reposts, saves, sends, and viewer demographics.
- **Profile analytics:** the Analytics section of the profile: profile viewers, post
  impressions, followers, and search appearances. Note the period LinkedIn shows for
  each.
- **Creator analytics** (audience growth and top posts) are on by default for
  eligible profiles since the creator-mode toggle was retired in March 2024.
- **Company page:** the Analytics tab: visitors, followers, content, competitors,
  leads. Page analytics export to a spreadsheet for time series.
- Personal analytics export is limited, so keep the manual sheet in
  `references/tracking-sheet.md`: 12 columns, no more. If tracking takes more than
  10 minutes a week, it will be abandoned.

## The weekly review, 15 minutes

Same time every week. Five questions, in this order:

1. **How many conversations started this week?** DMs, replies, calls booked. This is
   the headline number, not impressions.
2. **Which post drove the most profile views?** Not the most reactions. Study its
   hook and format.
3. **Which post underperformed, and why?** Hook, topic, format, or timing: pick one.
4. **Did the follower mix improve?** Check the new followers' titles.
5. **What is the single change for next week?** One change, not five. Changing one
   variable is the only way to learn anything.

Log the answers. Four weeks of logs beat any dashboard.

## The monthly review, 45 minutes

- **Pillar performance:** which content pillar produced conversations, not
  impressions. Shift the mix toward it, but keep at least 20% of posts across the
  other pillars so you keep learning.
- **Format performance:** text vs carousel vs video, judged on saves and profile
  views.
- **Time to lead:** how long between a first impression and a DM. It tells you how
  many touches the audience needs before acting.
- **Audience audit:** follower demographics against the target buyer. Drift here
  explains most "engagement is up but nothing converts".
- **Kill list:** what to stop doing. Every monthly review removes something.

## Benchmarks, used carefully

**Always show the calculation, not the raw count:**

```
Engagement rate = (reactions + comments + reposts) / impressions x 100
```

15 reactions and 1 comment on 1,376 impressions is 16 / 1,376 = 1.16%. "16
interactions" sounds fine; 1.16% is below target. Report the rate, the band, and
the verdict in one row. For a period, use the median of the posts, so one outlier
does not decide the verdict.

The engagement bands and the other orientation ranges (profile views per 1,000
impressions, inbound DMs a week, follower growth, connection acceptance) are in
`references/platform-reality.md`, with their grades. They apply to accounts under
about 10K followers and are orientation, never targets.

The user's own numbers over time beat anyone's benchmark. Compare them with
themselves last month.

## Deliver

1. The tier table filled with the user's actual numbers, top down (unknown cells say
   "not provided", never a guess)
2. The one honest verdict: is this working, and which tier is the bottleneck
3. The best and worst post of the period, with the reason
4. The follower-mix check against the target buyer
5. One change for next week, and the number it should move
6. The updated baseline for the next review

## Anti-patterns

- Reporting impressions as the headline result.
- Changing five things at once, then not knowing what worked.
- Judging a post at 2 hours. Give it 48 hours for a fair read and 7 days for saves.
- Comparing with creators in other niches with other audiences.
- Tracking so many metrics that the reviews stop happening.
- Concluding "LinkedIn does not work" from a 3-week sample.
