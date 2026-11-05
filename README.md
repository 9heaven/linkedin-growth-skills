# LinkedIn Growth Skills

Six agent skills that audit and grow a LinkedIn presence for **founders, creators,
influencers, consultants, and agency owners**: people selling something, building
an audience, or building credibility.

**Not for job seekers.** No ATS scoring, no recruiter keyword stuffing, no "open to
work" framing. Every skill treats the profile as a conversion asset, not a resume.

Works with Claude Code, Claude.ai, Codex, Cursor, OpenClaw, Hermes, and any agent that reads
[Agent Skills](https://agentskills.io/specification).

## Install

**Any agent, with the skills CLI:**

```bash
npx skills add 9heaven/linkedin-growth-skills
```

A single skill:

```bash
npx skills add https://github.com/9heaven/linkedin-growth-skills --skill linkedin-profile-audit
```

**Claude Code, as a plugin** (inside a session):

```
/plugin marketplace add 9heaven/linkedin-growth-skills
/plugin install linkedin-growth-skills@9heaven
```

Or from your shell:

```bash
claude plugin marketplace add 9heaven/linkedin-growth-skills
```

```bash
claude plugin install linkedin-growth-skills@9heaven
```

Plugin skills are namespaced, for example `/linkedin-growth-skills:linkedin-profile-audit`.
Claude also picks them up automatically when a request matches.

**Claude Code, by hand:** Claude Code looks for `~/.claude/skills/<skill-name>/SKILL.md`,
so clone the repo somewhere else and link each skill folder in:

```bash
git clone https://github.com/9heaven/linkedin-growth-skills.git ~/linkedin-growth-skills
```

```bash
mkdir -p ~/.claude/skills && ln -s ~/linkedin-growth-skills/skills/* ~/.claude/skills/
```

**Claude.ai:** zip a skill folder (for example `skills/linkedin-profile-audit/`, with
its `references/` inside) and upload it as a custom skill. Code execution must be on.
See Anthropic's [Use skills](https://support.claude.com/en/articles/12512180-use-skills)
help article for where the upload button is on your plan. Upload the whole folder:
pasting only `SKILL.md` into a Project drops the reference files the skill reads.

## The skills

| Skill | Use it when |
|---|---|
| **linkedin-profile-audit** | Score and rewrite a personal profile so visitors convert. Weighted rubric across 10 sections, adjusted by profile type, 3 headline options, full About rewrite. |
| **linkedin-company-page-audit** | Audit a company page: tagline, About, custom button, Products tab, and the founder-to-page traffic loop that actually drives page reach. |
| **linkedin-content-strategy** | Build pillars, a 4-week calendar, hooks, and formats tied to a buyer journey. |
| **linkedin-lead-generation** | Turn attention into booked calls: the 6-step path, inbound plays, DM handling, capped warm outreach. |
| **linkedin-authority-growth** | Narrow the position, build the proof stack, grow the right network, run a 90-day arc. |
| **linkedin-metrics-review** | Read analytics by a 5-tier hierarchy from revenue down to impressions. Weekly and monthly review rituals. |

Every skill has a **quick mode**: ask for one piece ("just rewrite my headline") and
it does that piece instead of the full audit.

## How they fit together

```
profile-audit ──► content-strategy ──► lead-generation
      │                  │                    │
      └──► authority-growth ◄─────────────────┘
                         │
                  metrics-review (weekly loop)

company-page-audit ──► content-strategy (page content engine)
```

Start with `linkedin-profile-audit`. If the profile scores well but nothing happens,
the bottleneck is content, not copy: go to `linkedin-content-strategy`.

## Principles

- **Zero fabrication.** Skills never invent clients, numbers, credentials, or
  people. Missing figures become explicit placeholders, and missing data is marked
  N/A instead of scored 0.
- **Conversations over vanity metrics.** Followers are a leading indicator at best.
  Every skill reports qualified conversations first.
- **No spam, no automation, no scraping.** Outreach is capped at human volume and
  personalized. The skills refuse mass-DM and bulk-scraping requests.
- **Paste-first data capture.** Optional logged-out reads of public pages only, for
  the user's own profile or a small named comparison set. Never a login, never
  credentials.
- **Sourced numbers.** Every platform figure in
  [`platform-reality.md`](shared/references/platform-reality.md) carries a source
  link and an evidence grade, so the skills know which numbers are LinkedIn's,
  which are third-party studies, and which are practitioner lore.
- **Human voice.** A banned-phrase list, no em dashes, and a rule to keep the user's
  own phrasing so drafts actually get published.

## Data and privacy

The skills ask the user to paste their own profile text and analytics. The optional
browser read fetches public, logged-out pages one at a time. Nothing is stored, sent
anywhere, or collected in bulk. No LinkedIn credentials are ever requested.

## Repository layout

```
skills/<skill>/SKILL.md          the instructions an agent loads
skills/<skill>/references/       files the skill reads on demand
shared/references/               canonical copies of files several skills share
evals/<case>/                    test cases, in the layout `claude plugin eval` reads
scripts/check.py                 validation, shared-file sync, and a voice-rule linter
.claude-plugin/                  Claude Code plugin manifest and marketplace
```

## Contributing

Issues and PRs welcome. Keep new work consistent with the principles above: no
fabrication, no automation for spam, decisive scoring, and concrete deliverables
instead of general advice.

- **Shared files** (`voice-rules.md`, `platform-reality.md`) are edited only in
  `shared/references/`. Each skill carries its own copy so it works when installed
  alone. After editing, run:

  ```bash
  python3 scripts/check.py --fix
  ```

- **Checks** run in CI on every push and PR. Run them locally first:

  ```bash
  python3 scripts/check.py
  ```

- **Lint a draft** or a skill's output against the voice rules:

  ```bash
  python3 scripts/check.py lint draft.md
  ```

- **Evals:** `evals/` holds test cases for every skill, including the refusal
  paths, in the layout [`claude plugin eval`](https://code.claude.com/docs/en/plugins/cli-reference)
  reads. Each case is tagged with its skill. These make real, billed model runs
  (3 runs a case by default). From the repo root:

  ```bash
  claude plugin eval . --tag linkedin-profile-audit --runs 1
  ```

- **Platform figures:** add a source link and a grade for any new number, and update
  the "Last verified" date.
- **Releases:** bump the version in `.claude-plugin/plugin.json`, in every
  `SKILL.md` (`metadata.version`), and in `CHANGELOG.md`. The checks fail if they
  disagree.

## Related work

These skills were built after reviewing the LinkedIn skills already published on
skills.sh. Several are good and solve adjacent problems:

| Skill | What it does better | Why ours is separate |
|---|---|---|
| [paramchoudhary/resumeskills: linkedin-profile-optimizer](https://github.com/paramchoudhary/resumeskills/tree/main/skills/linkedin-profile-optimizer) | Job-seeker profile optimization, recruiter search | We deliberately exclude job seekers |
| [social-media-skills/skills: linkedin-company-pages](https://github.com/social-media-skills/skills/tree/main/skills/linkedin-company-pages) | Deep employee-advocacy program design, publishing-tool integration | Ours is small-business sized, no tool dependency |
| [schwepps/skills: linkedin-personal-branding](https://github.com/schwepps/skills/tree/main/linkedin-personal-branding) | Industry benchmark tables, SSI reporting, Chrome extension capture | Ours is conversion-first and paste-first |
| [brianrwagner: linkedin-authority-builder](https://github.com/brianrwagner/ai-marketing-claude-code-skills) | Quick, standard, and deep mode selection | Ours ties authority to a proof stack and a 90-day arc |
| [cold-iq/coldiq-s-gtm-skills: linkedin-limits-warmup](https://github.com/cold-iq/coldiq-s-gtm-skills/tree/main/skills/linkedin-limits-warmup) | Account limits and warm-up detail | We absorbed the limits; we do not sell a data vendor |

## License

MIT. See [LICENSE](LICENSE).
