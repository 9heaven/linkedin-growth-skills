# LinkedIn Growth Skills

Six agent skills that audit and grow a LinkedIn presence for **founders,
creators, influencers, consultants, and agency owners** — people selling
something, building an audience, or building credibility.

**Not for job seekers.** No ATS scoring, no recruiter keyword stuffing, no
"open to work" framing. Every skill treats the profile as a conversion asset,
not a resume.

Works with Claude Code, Claude.ai, Codex, Cursor, OpenClaw, Hermes, and any
agent that reads Agent Skills.

## Install

```bash
npx skills add 9heaven/linkedin-growth-skills
```

Or a single skill:

```bash
npx skills add https://github.com/9heaven/linkedin-growth-skills --skill linkedin-profile-audit
```

Or clone into your agent's skills directory:

```bash
git clone https://github.com/9heaven/linkedin-growth-skills.git ~/.claude/skills/linkedin-growth-skills
```

Claude.ai without Desktop: open each `SKILL.md` and add it to a Project.

## The skills

| Skill | Use it when |
|---|---|
| **linkedin-profile-audit** | Score and rewrite a personal profile so visitors convert. Weighted rubric across 9 sections, 3 headline options, full About rewrite. |
| **linkedin-company-page-audit** | Audit a company page: tagline, About, custom button, Products tab, and the founder-to-page traffic loop that actually drives page reach. |
| **linkedin-content-strategy** | Build pillars, a 4-week calendar, hooks, and formats tied to a buyer journey. |
| **linkedin-lead-generation** | Turn attention into booked calls: the 6-step path, inbound plays, DM handling, capped warm outreach. |
| **linkedin-authority-growth** | Narrow the position, build the proof stack, grow the right network, run a 90-day arc. |
| **linkedin-metrics-review** | Read analytics by a 5-tier hierarchy from revenue down to impressions. Weekly and monthly review rituals. |

## How they fit together

```
profile-audit ──► content-strategy ──► lead-generation
      │                  │                    │
      └──► authority-growth ◄─────────────────┘
                         │
                  metrics-review (weekly loop)

company-page-audit ──► content-strategy (page content engine)
```

Start with `linkedin-profile-audit`. If the profile scores well but nothing
happens, the bottleneck is content, not copy — go to `linkedin-content-strategy`.

## Principles

- **Zero fabrication.** Skills never invent clients, numbers, or credentials.
  Missing figures become explicit placeholders.
- **Conversations over vanity metrics.** Followers are a leading indicator at
  best. Every skill reports qualified conversations first.
- **No spam, no automation, no scraping.** Outreach is capped at human volume
  and personalized. The skills refuse mass-DM and bulk-scraping requests.
- **Paste-first data capture.** Optional logged-out reads of public pages only,
  for the user's own profile or a small named comparison set. Never a login,
  never credentials.
- **Human voice.** A banned-phrase list, no em dashes, and a rule to keep the
  user's own phrasing so drafts actually get published.

## Data and privacy

The skills ask the user to paste their own profile text. The optional browser
read fetches public, logged-out pages one at a time. Nothing is stored, sent
anywhere, or collected in bulk. No LinkedIn credentials are ever requested.

## Contributing

Issues and PRs welcome. Keep new skills consistent with the principles above:
no fabrication, no automation-for-spam, decisive scoring, and concrete
deliverables instead of general advice.

## License

MIT. See [LICENSE](LICENSE).
