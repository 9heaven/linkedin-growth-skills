# Capturing a Company Page for Audit

Company pages are public by default, which makes the logged-out read reliable and
honest: it is exactly what a prospect sees before deciding to trust the business.

## Rules

- Never log in as the user. No credentials, no session cookies.
- One page at a time. No bulk collection, no competitor-list scraping. Checking two
  or three named competitors as part of one audit is fine; harvesting is not.
- If an auth wall or a challenge appears, stop and ask for a paste.

## Procedure

1. Open `linkedin.com/company/<slug>/` logged out.
2. Capture: name, tagline, About text, industry, size, HQ, founded year, website,
   specialties, follower count, and the custom button label.
3. Open the `/posts/` tab and record the last 5 posts: date, format, topic, and the
   visible reaction and comment counts.
4. Check `/people/` for how many employees list the company. A page with 8
   employees and 3 listed has a free fix sitting there.
5. Check for a Products or Services tab and whether it is filled.
6. Take one screenshot of the top of the page for the banner, logo, and
   above-the-fold layout.

Sections render as they scroll into view, as on personal profiles. If something
comes back empty, scroll and read again, or ask the user, before scoring it. Until
then it is N/A, not 0.

## What is not public

Page analytics (page views, unique visitors, button clicks, follower demographics),
lead-gen form data, and competitor analytics. Ask for these from the page's
Analytics tab (item 10 of the paste); `linkedin-metrics-review` needs them.

## Competitor comparison

When comparing 2–3 named competitors, keep the comparison to what matters: tagline
clarity, post cadence, content mix, and whether their proof is visible. Follower
counts are mostly noise for small businesses, since a page that bought or inherited
followers converts nothing.
