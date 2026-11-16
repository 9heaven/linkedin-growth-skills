# The LinkedIn Context File

One small file, `linkedin-context.md`, carries what every LinkedIn skill needs to
know about the user, so they answer the intake questions once instead of in every
skill.

## At the start of a skill

1. Look for `linkedin-context.md` in the working folder, and for a pasted
   "LinkedIn context" block in the conversation.
2. **Found:** read it. Say in one line what you are using (audience, action,
   offer) and that they can correct it. Then ask only for what this skill needs and
   the file lacks. Do not re-ask anything the file answers.
3. **Not found:** run the skill's normal intake.
4. If `Updated` is more than 90 days old, ask whether the audience, offer, and
   numbers still hold before relying on them.

## At the end of a skill

If you learned anything the file should hold (an answer to an intake question, a
new score, a new baseline, a chosen position or pillar), update it:

- **You can write files:** save `linkedin-context.md` in the working folder and
  tell the user where it is.
- **You cannot:** print the whole block and tell the user to keep it, then paste it
  at the start of the next conversation or add it to their Project.

If nothing new was learned, leave the file alone and say nothing about it.

## Rules

- **Only what the user said or approved.** Never fill a field by guessing. An
  unknown field stays empty.
- **The user's edits win.** If they changed the file by hand, do not undo it.
- **No secrets.** Never store passwords, cookies, or login details. Store a client
  name only with the user's "may be named" answer next to it.
- **Keep it short.** Replace old values instead of appending. The log keeps the last
  3 entries of each kind.
- A score or baseline always carries its date.

## Template

```
# LinkedIn context
Updated: [YYYY-MM-DD]

## Who and what
- Profile type: [founder / consultant or freelancer / creator or influencer / operator with a side offer]
- Audience, by situation: [who you want to attract]
- Primary action: [book a call / DM a keyword / subscribe / follow]
- Fallback action: [one]
- Offer in one line: [I help ... achieve ... in ..., usually via ...]
- Price band and decision cycle: [range, how long buyers take]
- Primary market and time zone: [market, zone]
- Account size: [followers] followers as of [date]

## Position
- Position in 8 words or fewer: [position]
- Deliberately excludes: [who it is not for]

## Proof inventory
- [result, with its number] | client may be named: [yes / no]
- [result, with its number] | client may be named: [yes / no]

## Voice
- Phrases to keep: [their own words]
- Never say: [words they dislike]
- Sample: [one past post or paragraph, pasted]

## Content system
- Pillars: [3-4, one sentence each]
- Cadence: [posts a week, comment routine]
- Signature format: [name]

## Log (last 3 of each)
- Profile score: [date] [score]/100, biggest leak: [leak]
- Baseline: [date] profile viewers [n], search appearances [n], inbound DMs a week [n], calls booked [n]
- One change: [date] [the single change made, and the number it should move]
```
