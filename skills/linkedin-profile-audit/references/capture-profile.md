# Capturing a Profile for Audit

Pasting is the default and it always works. Use a live read only when the user
asks for it and the profile is theirs (or public and they have a legitimate
reason to review it, e.g. a competitor comparison).

## Rules

- **Never log in as the user.** Do not ask for credentials, cookies, or a
  session. Read the logged-out public view.
- **One profile at a time.** This is an audit tool, not a scraper. No loops over
  lists of people, no exports, no bulk collection.
- **Respect the platform.** LinkedIn's terms prohibit automated data collection.
  A single human-paced page read for the user's own profile is a different thing
  from harvesting, and this skill only does the former.
- If LinkedIn shows an auth wall or a challenge, stop and ask for a paste. Do not
  try to route around it.

## The logged-out read is the point

What a signed-out visitor sees is what strangers, Google, and AI search engines
see. It is often missing sections the user assumes are visible. Two things worth
flagging every time:

- **Public profile settings** — if Featured, About, or Activity are hidden from
  public view, inbound traffic from search sees a stub. Tell the user to set the
  public profile to show everything relevant.
- **Custom URL** — an auto-generated URL with a hash suffix looks unfinished
  everywhere it is pasted.

## Procedure

1. Open the public URL in a fresh tab with the browser tool.
2. Wait for load, then capture the text of headline, About, Experience, Featured
   titles, and whether an activity feed renders.
3. Take one screenshot to judge banner, photo, and above-the-fold layout — those
   cannot be assessed from text.
4. Note what is missing from the public view versus what the user says exists.
5. Continue the audit from the captured text, using the same rubric as a paste.

## What you cannot get logged out

Follower counts on some profiles, full activity history, analytics, and search
appearances. Ask for those in the paste. Analytics in particular are never
public, and `linkedin-metrics-review` needs them.
