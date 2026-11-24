# Changelog

All notable changes to this project. Versions follow [Semantic Versioning](https://semver.org/).
The plugin manifest and every skill share one version number.

## [Unreleased]

Found by running the profile audit on a live founder profile in the owner's own
browser.

### Added

- Profile audit: an owner-session capture mode. When the user opens their own
  profile in their own signed-in browser, the skill may read it there, including
  the Analytics card, and no longer asks for numbers it can already see. A
  logged-out check is still required for what strangers see.
- Profile audit: a cross-section consistency check (banner, headline, About,
  Services, current role) and an audience-signal check from "Who your viewers also
  viewed" titles. Neither carries weight; both steer the rewrites.
- Profile audit: `references/edit-paths.md`, so every do-this-week item says where
  the edit lives.
- Profile audit: one-line guidance for the Premium custom button, the education
  line in the top card, and older Experience entries.
- Eval case `profile-audit-mixed-positioning`.

### Fixed

- Profile audit: a hands-off live audit no longer stalls on the two intake
  questions. The skill infers audience and action, marks them "assumed", and
  confirms at the end.
- Profile audit: the 40–59 band said to fix headline, About, and Featured first,
  while the Activity rule said publishing comes first. The Activity rule now wins,
  in both the skill and the rubric.
- Rubric: the About anchors had no fit for a generic opener with no proof, and the
  Featured anchors had no fit for a single item or a featured recommendation.
- Rubric: reshares no longer reset the date of the last post, and a Completeness
  item that cannot be confirmed drops out of the fraction.
- Engagement rate is N/A when fewer than 3 original posts from the last 90 days
  have numbers.
- Capture guide: details paths added for Featured, Skills, Activity, and Contact
  info. The lazy-loading note now says the mounted sections vary between loads, and
  that the Skills details page lazy-loads too.

## [1.2.0] - 2026-11-05

### Fixed

- Every skill now ships the reference files it cites. Four skills pointed at a
  `platform-reality.md` they did not contain, which broke single-skill installs.
- Profile audit: the SKILL.md table (10 sections, weight 32) and the rubric (9
  sections, weight 30) now match. Services has its own scoring anchors and is no
  longer counted twice.
- Profile audit: engagement-rate example corrected (15 reactions on 1,376
  impressions is 1.09%; the 1.16% example now includes the 1 comment).
- Lead generation: the "well under the weekly limit" claim was wrong (20 a day is
  the full ~100 a week). The pace is now 10–15 a weekday with 20 as a hard ceiling.
- Acceptance-rate threshold unified at 30% healthy and 15% stop (lead generation
  said 40%).
- Follow-ups unified at one, 3–4 weeks later (the skill allowed two, the scripts one).
- Templates no longer contain em dashes, which the voice rules ban.
- Score bands are contiguous (40–59, 60–79) instead of overlapping at 60 and 80.
- Engagement bands have no gap between 2% and 3%.
- Tracking sheet records saves at 7 days, matching the "judge saves at 7 days" rule.
- README: the `git clone` install nested skills too deep for Claude Code to find,
  and the Claude.ai instructions dropped the reference files.

### Changed

- `platform-reality.md` rebuilt with a source link and an evidence grade (LinkedIn,
  Study, Reported, House rule) for every figure. Corrections found while sourcing:
  "561% more reach" is about 6.6x, not 5.6x, and it is a 2015 MSLGroup figure about
  employee shares across all social networks. LinkedIn denies a link penalty and
  studies measure about 26.5% (mostly on company pages), not 60%. The unverified
  14.6% vs 1.7% share rates were replaced with LinkedIn's own figures (10x network,
  3% of employees driving 30% of engagement). Polls and video lost measured reach.
- Comment-to-get lead magnets now carry LinkedIn's engagement-bait caveat and a
  first-comment link alternative.
- Frontmatter follows the Agent Skills spec: `version` moved into `metadata`, all
  metadata values are strings, and the non-spec `platforms` key is gone.
- Descriptions rewritten with the trigger phrases agents use to pick a skill.
- Examples diversified across niches, with a rule never to carry an example's
  niche, numbers, or currency into a draft. Posting-time advice is time-zone neutral.
- Authority growth no longer asks the agent to name 15–25 real accounts; the user
  supplies names and the agent never invents them.
- Shared files live once in `shared/references/` and are copied into each skill.
- README rewritten for users: quick start, a "which skill do I need" table, an
  example audit, collapsible install options with update commands, a Mermaid
  workflow diagram, and an FAQ. Maintainer material moved to `CONTRIBUTING.md`.

### Added

- Quick mode in every skill for single-piece requests ("just my headline").
- Profile audit: profile-type weight adjustments, an explicit weighted-score
  formula with a worked example, N/A handling for missing data, and paste fields
  for every section it scores.
- Company page audit: weighted-score formula and verdict bands.
- `.claude-plugin/marketplace.json` for one-command install in Claude Code.
- `scripts/check.py` and a GitHub Actions workflow: frontmatter, references,
  shared-file sync, weights, versions, em dashes, banned phrases in templates, and
  eval structure. `check.py lint FILE` checks any draft against the voice rules.
- Eval cases for every skill in the `claude plugin eval` layout, including the
  refusal paths (job seeker, mass automation, invented names).
- `CONTRIBUTING.md`: repository layout, shared-file sync, checks, evals, and
  release steps. `check.py` also checks the README version badge.

## [1.1.0] - 2026-09-05

### Added

- Platform-reality reference, engagement-rate math, profile classification,
  account limits and warm-up protocol, employee-advocacy mechanics.
- Lazy-load pitfall for live profile reads.

### Fixed

- Removed references to the retired creator-mode toggle and profile hashtags.

## [1.0.0] - 2026-09-05

### Added

- Six LinkedIn growth skills for founders, creators, and influencers.
