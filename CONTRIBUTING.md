# Contributing

Thanks for helping. Keep new work consistent with the principles in the
[README](README.md#what-makes-these-different): no fabrication, no automation for
spam, decisive scoring, and concrete deliverables instead of general advice.

## Repository layout

```
skills/<skill>/SKILL.md          the instructions an agent loads
skills/<skill>/references/       files the skill reads on demand
shared/references/               canonical copies of files several skills share
evals/<case>/                    test cases, in the layout `claude plugin eval` reads
scripts/check.py                 validation, shared-file sync, and a voice-rule linter
.claude-plugin/                  Claude Code plugin manifest and marketplace
```

## Shared files

`voice-rules.md` and `platform-reality.md` are edited only in `shared/references/`.
Each skill carries its own copy so it still works when installed alone. After
editing, copy the change into every skill that cites the file:

```bash
python3 scripts/check.py --fix
```

## Checks

CI runs the checks on every push and pull request. Run them locally first:

```bash
python3 scripts/check.py
```

They cover Agent Skills frontmatter, references that resolve inside each skill,
shared-file copies, the profile and company-page weight tables, matching versions,
em dashes, banned phrases in templates, and eval structure.

To lint a draft, or a skill's output, against the voice rules:

```bash
python3 scripts/check.py lint draft.md
```

## Evals

`evals/` holds test cases for every skill, including the refusal paths, in the
layout [`claude plugin eval`](https://code.claude.com/docs/en/plugins/cli-reference)
reads. Each case is tagged with its skill, and every skill needs at least two. Runs
are real, billed model calls (3 runs a case by default). From the repo root:

```bash
claude plugin eval . --tag linkedin-profile-audit --runs 1
```

## Platform figures

Add a source link and a grade (LinkedIn, Study, Reported, or House rule) for any new
number in `shared/references/platform-reality.md`, and update its "Last verified"
date. Never add a figure you cannot trace.

## Releases

Bump the version in `.claude-plugin/plugin.json`, in every `SKILL.md`
(`metadata.version`), in the README version badge, and in `CHANGELOG.md`. The checks
fail if any of them disagree.
