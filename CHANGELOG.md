# Changelog

All notable changes to this project. Versions follow [Semantic Versioning](https://semver.org/).
The plugin manifest and every skill share one version number.

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
