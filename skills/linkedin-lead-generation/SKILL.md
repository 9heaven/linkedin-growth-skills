---
name: linkedin-lead-generation
description: "Turns LinkedIn attention into booked calls and paying clients for founders, consultants, and creators selling their own services. Finds the broken step in the content-to-client path, fixes the one-line offer, scripts inbound plays and DM replies, and plans capped, personalized warm outreach. Use when someone asks how to get leads, clients, or calls from LinkedIn, how to reply to DMs, or how to do outreach. Refuses mass automation, scraping, and templated DM spam."
license: MIT
metadata:
  author: "9HEAVEN"
  version: "1.2.0"
  audience: "founders, consultants, agency owners, creators selling services"
  not_for: "job seekers, mass automation, scraping at scale"
---

# LinkedIn Lead Generation

Convert LinkedIn attention into conversations, and conversations into clients.

**Hard boundary:** this skill does personalized, human outreach at human volume. It
does not build automated connection blasts, scraped lead lists, or templated DM
spam. Those get accounts restricted and burn reputation permanently. If the user
asks for mass automation, say no once, explain why in a sentence, and offer the
version that works.

## Pick the depth

- **Quick:** the user needs one thing ("how do I reply to this DM", "fix my offer
  line"). Do that step only, using `references/dm-scripts.md` for messages, and name
  the broken step if the numbers they gave point to one.
- **Full** (default for "help me get leads"): the path diagnosis, then Steps 1 to 6.

## The path

Every lead follows the same route. Find the broken step before optimizing anything
else.

```
Content seen -> profile visited -> offer understood -> conversation started -> call booked -> client
```

Diagnose with the user's own numbers:

| Symptom | Broken step | Fix with |
|---|---|---|
| Posts get no views | Content | `linkedin-content-strategy` |
| Views but no profile visits | Hook and identity in the post | `linkedin-content-strategy` |
| Profile visits but no DMs | Profile conversion | `linkedin-profile-audit` |
| DMs but no calls | Offer clarity and DM handling | this skill, Steps 1 and 3 |
| Calls but no clients | Offer, price, or qualification | this skill, Step 5 |

Never optimize step 4 when step 1 is broken. Name the broken step, with the number
that proves it, before giving any tactic.

## Step 1: Make the offer legible

Before any outreach, the user must be able to finish this in one line:

> "I help [specific audience] achieve [specific outcome] in [timeframe], usually
> via [mechanism]."

If it takes a paragraph, prospects will not repeat it to their network and DMs will
stall. Fix this first: it is the most common real blocker.

Then place it where traffic already lands: the headline, the About CTA, Featured
slot 1, and the pinned post.

## Step 2: Inbound plays (run these before outreach)

Inbound converts better and costs no reputation.

**Comment-to-deliver, used sparingly.** End a high-value post with "Comment [WORD]
and I'll send it", reply to each comment, then DM the asset. It creates real
conversations with real consent. But LinkedIn reduces the reach of posts that ask
for engagement mainly to boost reach, so use it rarely, only for an asset worth the
ask, and also put the link in the first comment for anyone who does not want to
comment.

**A lead magnet that proves competence.** A checklist, teardown template, or
calculator that solves one narrow problem end to end. Ten useful pages beat a
50-page ebook nobody opens.

**Profile-to-call path.** Featured slot 1 is the booking link. The About ends with
the same link. Both use the same words as the offer line.

**Free teardown play.** Publicly audit a real example (with permission, or a public
brand), post the findings, and let readers ask for theirs. It converts better than
any cold DM because the work is visible before the ask.

## Step 3: DM handling

Most founders lose leads here by pitching too early. Messages follow
`references/voice-rules.md`, and the templates are in `references/dm-scripts.md`,
written to be edited, never sent as-is.

Sequence for an inbound DM:

1. **Acknowledge and give.** Deliver the promised thing with no strings.
2. **One question.** About their situation, not your service: "What made you grab
   this? What are you trying to fix?"
3. **Diagnose in the thread.** Give one genuinely useful answer for free. This is
   the sale.
4. **Soft bridge, once.** "This is exactly what I do with clients. Want me to walk
   you through how I'd fix it on a call?"
5. **If they say no or go quiet, stay useful.** One follow-up, 3–4 weeks later, with
   something relevant. Then stop.

Never: pitch right after a connection is accepted, send a voice note to a stranger,
or follow up more than once on an unanswered thread.

## Step 4: Warm outreach (capped volume)

Only once inbound is running. Every figure here comes from
`references/platform-reality.md`; check it there before quoting it.

- **Weekly budget first.** LinkedIn's invitation limit is reported at about 100 a
  week. Send 10–15 personalized requests a weekday. 20 a day is the ceiling, not a
  target: it spends the whole weekly budget in five days.
- **Daily action ceiling.** Invitations, DMs, profile views, likes, comments, and
  endorsements all count toward a reported ceiling near 120 a day. Stay well below
  it.
- **Watch the acceptance rate.** Above 30% is healthy. Between 15% and 30%, slow
  down and tighten targeting. Below 15%, stop and fix targeting before sending more.
- **Warm up a dormant account first.** If the user has been inactive for months,
  follow the warm-up protocol in `references/platform-reality.md` before any
  invitations.
- **Target only active people.** People who posted or commented in the last 30 days
  (Sales Navigator can filter for this; otherwise check their activity by hand).
  Requests to dormant profiles burn a capped weekly budget for nothing.
- **Targeting sources:** people who engaged with the user's posts, people who
  viewed the profile, second-degree connections of happy clients, and members of
  the same communities. Never a scraped or bought list.
- **Note or no note:** send a note only with a real, specific reason (they
  commented, you share a client, you read their post). Otherwise send it blank:
  generic notes lower acceptance.
- **Keep messages to 3–4 sentences,** sent during the recipient's business hours.
- **The first message is never a pitch.** Reference the actual reason you connected.

Track acceptance rate, reply rate, and calls booked per 100 requests. If the reply
rate is under 10%, the targeting is wrong, not the script.

## Step 5: Qualify before the call

Ask three questions in DM before booking: what they are trying to fix, what they
have already tried, and their timeline. It protects the calendar and raises the
close rate, because the call starts mid-conversation.

Disqualify openly when it is not a fit, and refer them elsewhere. It costs one lead
and buys a lasting reputation.

## Step 6: Deliver

1. Which step of the path is broken, with the number that proves it
2. The one-line offer, rewritten
3. Two inbound plays to run in the next 14 days, scripted
4. The DM sequence adapted to their offer
5. An outreach plan with daily and weekly caps and targeting sources, only if
   inbound is live
6. Metrics: profile views, DMs started, calls booked, close rate, with today's
   baseline (or "not provided")

## Anti-patterns

- Pitching in the connection request. The fastest way to be ignored and reported.
- Automation tools that send on the user's behalf. Against LinkedIn's terms and a
  restriction risk.
- Buying lead lists or scraping at volume.
- "Quick question" openers and fake personalization.
- Booking calls with unqualified people to feel busy.
- Measuring followers instead of conversations. Report conversations.
