# Profile Scoring Rubric

Score each section 0–5. Be decisive: a 2 is a 2. Averaging everything to 3
produces an audit nobody acts on.

Anchors: **0** confirmed absent · **1** present but harmful · **2** generic ·
**3** functional · **4** strong · **5** best in niche. **N/A** means the data was
not provided or the section does not apply to this profile type. N/A is never 0.

Section names and default weights match the table in `SKILL.md`. Apply the
profile-type changes listed there before computing the score.

## Headline (weight 5)

| Score | Condition |
|---|---|
| 0–1 | Empty, "Founder at X" only, or keyword soup |
| 2 | Title, company, and a vague descriptor |
| 3 | Names an audience or an outcome, but not both |
| 4 | Audience and outcome, front-loaded in roughly the first 60 characters |
| 5 | Audience, outcome, and a differentiator or proof point, and it sounds human |

Check: do the first 60 or so characters stand alone? That is what shows next to the
name in comments, notifications, and search.

## About (weight 5)

Score the first two lines separately in your head, because they are all a visitor
sees before "see more".

| Score | Condition |
|---|---|
| 0–1 | Empty, a third-person bio, or a resume summary |
| 2 | Opens with "I have N years of experience" |
| 3 | Explains what they do, but buries it below line 5 |
| 4 | Hook in lines 1–2, clear positioning, some proof |
| 5 | Hook, agitate, positioning, real proof, who it is not for, and one CTA |

## Activity (weight 5)

| Score | Condition |
|---|---|
| 0 | No posts ever |
| 1 | Last post more than 6 months ago |
| 2 | Only reshares and congratulation comments |
| 3 | 1–3 original posts a month |
| 4 | Weekly original posts, some comments |
| 5 | 3 or more posts a week with real comment threads |

Activity at 0–2 caps the value of every other fix. Say so, and hand off to
`linkedin-content-strategy`.

## Featured (weight 4)

| Score | Condition |
|---|---|
| 0 | Section not set up |
| 1 | Items that hurt: dead links, an old job, off-topic content |
| 2 | Random posts, no thumbnails, no order |
| 3 | Relevant items but no direct conversion path |
| 4 | The primary-action item first, custom thumbnails, benefit-led titles |
| 5 | All of that, plus a lead magnet and a case study, all 4 slots working |

The primary-action item is the booking or offer link for founders, consultants, and
operators, and the newsletter or lead magnet for creators.

## Banner (weight 3)

0 = LinkedIn default. 1 = misleading or unreadable. 2 = a stock image or a logo
alone. 3 = readable text. 4 = offer or proof, legible on a phone. 5 = offer, proof,
and a visual that is unmistakably theirs, with the bottom-left kept clear for the
profile photo.

## Experience (current role) (weight 3)

0 = blank. 1 = misleading or out of date. 2 = a duty list. 3 = describes the company.
4 = describes who the company serves and the outcome. 5 = that, plus 3–4 proof
bullets with numbers.

For an operator with a side offer, score accuracy and clarity about the employer
role instead: 5 = accurate, clear, and consistent with the rest of the profile.

## Photo (weight 2)

0 = none or a logo. 1 = unprofessional for the audience. 2 = distant, dim, or a
group crop. 3 = clear but stiff. 4 = face fills the frame, eye contact, good light.
5 = that, plus a background and expression that fit the positioning.

## Skills and recommendations (weight 2)

0 = no recommendations and generic skills. 2 = skills unrelated to the positioning
or 1 recommendation. 3 = top 3 skills match the positioning, 2 or more
recommendations. 4 = 3–4 recommendations that name what was delivered. 5 = 5 or more
recommendations naming specific results, and skills ordered deliberately.

## Services (weight 2)

0 = empty. 2 = listed, but generic categories with no description. 3 = the services
match the positioning. 4 = they match, with a description of who each is for and
the outcome. 5 = that, plus reviews or a request path that matches the profile CTA.

N/A for creators whose primary action is follow or subscribe.

## Completeness (weight 1)

Five binary items: custom URL, location, contact info, website link, and Follow set
as the primary button where inbound outpaces outbound. Score = 5 x the fraction
done, rounded to a whole number. Do not score "creator mode" or profile hashtags:
both were retired in early 2024.

## Computing the score

```
Weighted score = sum(score x weight) / (5 x sum(weight)) x 100
```

Both sums run over scored sections only. N/A sections drop out of both. Round to a
whole number.

**Losing the most points:** for each scored section, `lost = weight x (5 - score)`.
The three highest are the work. Break ties by weight, then by table order.

### Worked example

A founder profile with defaults, Services not provided (N/A):

| Section | Weight | Score | score x weight | Lost |
|---|---|---|---|---|
| Headline | 5 | 2 | 10 | 15 |
| About | 5 | 2 | 10 | 15 |
| Activity | 5 | 1 | 5 | 20 |
| Featured | 4 | 0 | 0 | 20 |
| Banner | 3 | 2 | 6 | 9 |
| Experience (current role) | 3 | 3 | 9 | 6 |
| Photo | 2 | 4 | 8 | 2 |
| Skills and recommendations | 2 | 2 | 4 | 6 |
| Services | 2 | N/A | n/a | n/a |
| Completeness | 1 | 3 | 3 | 2 |

Scored weight = 30. Sum of score x weight = 55. Score = 55 / (5 x 30) x 100 =
36.7, which rounds to **37: under 40, full rewrite**. The three sections losing the
most points: Activity (20), Featured (20), Headline (15). Activity is at 1, so the
verdict leads with publishing, not copy.

## Bands

- **Under 40:** the profile is losing people. Full rewrite.
- **40–59:** a functional resume, not a conversion asset. Fix headline, About, and
  Featured, in that order.
- **60–79:** a good asset. The bottleneck is traffic, not copy.
- **80 and over:** do not touch the profile. Work on content and the offer.

Always report the weighted total, its band, and the three sections losing the most
points, because those are the work.
