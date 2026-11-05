# Capturing a Profile for Audit

Pasting is the default and it always works. Use a live read only when the user asks
for it and the profile is theirs, or it is public and they have a legitimate reason
to review it (for example, comparing against two or three named competitors).

## Rules

- **Never log in as the user.** Do not ask for credentials, cookies, or a session.
  Read the logged-out public view.
- **One profile at a time.** This is an audit tool, not a scraper. No loops over
  lists of people, no exports, no bulk collection.
- **Respect the platform.** LinkedIn's terms prohibit automated data collection. A
  single human-paced page read for the user's own profile is a different thing from
  harvesting, and this skill only does the former.
- If LinkedIn shows an auth wall or a challenge, stop and ask for a paste. Do not
  try to route around it.

## The logged-out read is the point

What a signed-out visitor sees is what strangers, Google, and AI search engines
see. It often lacks sections the user assumes are visible. Flag two things every
time:

- **Public profile settings:** if Featured, About, or Activity are hidden from the
  public view, inbound traffic from search sees a stub. Tell the user to make
  everything relevant public.
- **Custom URL:** an auto-generated URL with a hash suffix looks unfinished
  everywhere it is pasted.

## Pitfall: lazy loading looks identical to an empty profile

**LinkedIn renders profile sections only as they scroll into view.** A single
`document.body.innerText` read right after load returns the top card and the
activity feed, and nothing else. About, Services, Featured, Skills, and
Recommendations come back missing, which is indistinguishable from a genuinely
empty profile. Scoring them 0 produces a confidently wrong audit.

Two rules:

1. **Scroll incrementally before reading.** Step down the page in about 500px
   increments with a short pause at each stop, then read. One jump to the bottom is
   not enough: sections skipped over never mount.
2. **Never score a section 0 from a single failed read.** If a section is absent,
   confirm it by loading its details URL (`/in/<slug>/details/experience/`,
   `/details/recommendations/`) or by asking the user. Until it is confirmed, it is
   N/A. Absent from your read is not the same as absent from the profile.

Details pages are the reliable source for Experience and Recommendations. The main
profile truncates both.

## Procedure

1. Open the public URL in a fresh tab with the browser tool.
2. Scroll incrementally (see the pitfall above), then capture the text of the
   headline, About, Services, Experience, Featured titles, Skills, the
   recommendation count, and whether an activity feed renders. Verify anything that
   came back empty against its details URL before scoring it.
3. Take one screenshot to judge the banner, photo, and above-the-fold layout. Those
   cannot be judged from text.
4. Note what is missing from the public view versus what the user says exists.
5. Continue the audit from the captured text, using the same rubric as a paste.

## What you cannot get logged out

Follower counts on some profiles, full activity history, post analytics, profile
viewers, and search appearances. Ask for those with items 11–13 of the paste.
Analytics are never public, and `linkedin-metrics-review` needs them.
