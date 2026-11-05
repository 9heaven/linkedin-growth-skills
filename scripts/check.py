#!/usr/bin/env python3
"""Repository checks for linkedin-growth-skills. Python 3.8+, standard library only.

Usage:
  python3 scripts/check.py              run every check (CI runs this)
  python3 scripts/check.py --fix        first copy shared/references/* into each skill
                                        that cites them, then run every check
  python3 scripts/check.py lint FILE..  check a draft or a generated output against
                                        the voice rules (em dashes, banned phrases)
"""

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
SHARED = ROOT / "shared" / "references"
VOICE_RULES = SHARED / "voice-rules.md"

ALLOWED_FRONTMATTER = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
REQUIRED_METADATA = {"author", "version"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
CASE_NAME_RE = re.compile(r"^[a-z][a-z0-9-]*$")
RESERVED_CASE_NAMES = {"results", "mocks", "node_modules", "files", "true", "false", "null"}
PROMPT_SETTINGS = {"tags", "max_turns", "timeout_seconds", "allowed_tools"}
REF_RE = re.compile(r"references/([A-Za-z0-9_.-]+\.md)")
SKILL_NAME_RE = re.compile(r"`(linkedin-[a-z0-9-]+)`")
EM_DASH = "—"
MAX_SKILL_LINES = 500

errors = []


def fail(path, msg):
    try:
        shown = path.relative_to(ROOT)
    except ValueError:
        shown = path
    errors.append(f"{shown}: {msg}")


def skill_dirs():
    return sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())


def split_frontmatter(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    return text[4:end], text[end + 5:]


def parse_frontmatter(block, path):
    """Parse the restricted YAML used here: top-level `key: value` and one level
    of `metadata:` children. Values must be single-line scalars."""
    data, meta, in_meta = {}, {}, False
    for raw in block.splitlines():
        if not raw.strip():
            continue
        if raw.startswith("  "):
            if not in_meta:
                fail(path, f"unexpected indented frontmatter line: {raw.strip()}")
                continue
            key, _, value = raw.strip().partition(":")
            value = value.strip()
            if not (len(value) >= 2 and value[0] == value[-1] == '"'):
                fail(path, f"metadata.{key} must be a quoted string (Agent Skills metadata is string to string)")
            meta[key.strip()] = value.strip('"')
            continue
        key, _, value = raw.partition(":")
        key, value = key.strip(), value.strip()
        in_meta = key == "metadata" and value == ""
        if in_meta:
            data["metadata"] = meta
        else:
            if value.startswith("[") or value.startswith("{"):
                fail(path, f"{key} must be a scalar, not a list or map")
            data[key] = value.strip('"')
    return data


def check_frontmatter(skill, versions):
    path = skill / "SKILL.md"
    text = path.read_text(encoding="utf-8")
    block, body = split_frontmatter(text)
    if block is None:
        fail(path, "missing YAML frontmatter")
        return
    fm = parse_frontmatter(block, path)
    for key in fm:
        if key not in ALLOWED_FRONTMATTER:
            fail(path, f"frontmatter key '{key}' is not in the Agent Skills spec")
    name = fm.get("name", "")
    if not NAME_RE.match(name) or len(name) > 64:
        fail(path, f"invalid name '{name}'")
    if name != skill.name:
        fail(path, f"name '{name}' must match the directory name '{skill.name}'")
    desc = fm.get("description", "")
    if not 1 <= len(desc) <= 1024:
        fail(path, f"description must be 1-1024 characters (is {len(desc)})")
    if "compatibility" in fm and not 1 <= len(fm["compatibility"]) <= 500:
        fail(path, "compatibility must be 1-500 characters")
    meta = fm.get("metadata", {})
    for key in REQUIRED_METADATA - set(meta):
        fail(path, f"metadata.{key} is required")
    if "version" in meta:
        versions[f"{skill.name} metadata.version"] = meta["version"]
    lines = text.count("\n") + 1
    if lines > MAX_SKILL_LINES:
        fail(path, f"{lines} lines; keep SKILL.md under {MAX_SKILL_LINES}")
    if not body.strip():
        fail(path, "empty body")


def cited_references(skill):
    cited = {}
    for md in [skill / "SKILL.md"] + sorted((skill / "references").glob("*.md")):
        for ref in REF_RE.findall(md.read_text(encoding="utf-8")):
            cited.setdefault(ref, md)
    return cited


def sync_shared():
    for skill in skill_dirs():
        for ref in cited_references(skill):
            src = SHARED / ref
            if src.is_file():
                dst = skill / "references" / ref
                dst.parent.mkdir(exist_ok=True)
                if not dst.is_file() or dst.read_bytes() != src.read_bytes():
                    shutil.copyfile(src, dst)
                    print(f"synced {dst.relative_to(ROOT)}")


def check_references(skill):
    cited = cited_references(skill)
    for ref, where in cited.items():
        target = skill / "references" / ref
        if not target.is_file():
            fail(where, f"cites references/{ref}, which does not exist in {skill.name} "
                        "(skills must be self-contained; run scripts/check.py --fix for shared files)")
        elif (SHARED / ref).is_file() and target.read_bytes() != (SHARED / ref).read_bytes():
            fail(target, f"differs from shared/references/{ref}; edit the shared copy and run --fix")
    skill_md = (skill / "SKILL.md").read_text(encoding="utf-8")
    for ref_file in sorted((skill / "references").glob("*.md")):
        if f"references/{ref_file.name}" not in skill_md:
            fail(ref_file, "not cited from SKILL.md, so an agent will never load it")


def check_skill_names(names):
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        for found in SKILL_NAME_RE.findall(md.read_text(encoding="utf-8")):
            if found not in names and found != "linkedin-growth-skills":
                fail(md, f"mentions `{found}`, which is not a skill in this repo")


def check_em_dashes():
    for path in sorted(ROOT.rglob("*")):
        if ".git" in path.parts or not path.is_file() or path.suffix not in {".md", ".json", ".yaml", ".yml"}:
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if EM_DASH in line:
                fail(path, f"line {n}: em dash (the voice rules ban them; skills copy their own style)")


def banned_phrases():
    text = VOICE_RULES.read_text(encoding="utf-8")
    section = text.split("## Banned phrases", 1)[1].split("\n## ", 1)[0]
    phrases = []
    for line in section.splitlines():
        if not line.startswith("- "):
            continue
        for item in re.findall(r'"([^"]+)"|([^,"]+)', line[2:]):
            phrase = (item[0] or item[1]).strip()
            phrase = re.sub(r"\s*\(.*?\)", "", phrase).strip()
            if phrase:
                phrases.append(phrase.lower())
    return phrases


def phrase_pattern(phrase):
    words = [re.escape(w) for w in phrase.replace("’", "'").split()]
    body = r"[\s-]+".join(words)
    suffix = r"(?:s|d|ed|ing)?" if len(words) == 1 else ""
    return re.compile(r"(?<![A-Za-z])" + body + suffix + r"(?![A-Za-z])", re.IGNORECASE)


def lint_text(text, path, phrases, only_fenced=False):
    patterns = [(p, phrase_pattern(p)) for p in phrases]
    in_fence = False
    for n, line in enumerate(text.replace("’", "'").splitlines(), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if only_fenced and not in_fence:
            continue
        if EM_DASH in line and not only_fenced:
            fail(path, f"line {n}: em dash")
        for phrase, pattern in patterns:
            if pattern.search(line):
                fail(path, f"line {n}: banned phrase '{phrase}'")


def check_templates(phrases):
    for md in sorted(SKILLS.rglob("*.md")):
        if md.name == "voice-rules.md" or "evals" in md.parts:
            continue
        lint_text(md.read_text(encoding="utf-8"), md, phrases, only_fenced=True)


def weight_table(text):
    """Return {name: weight} from the first table whose header has a Weight column."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.startswith("|") and "Weight" in cells:
            col = cells.index("Weight")
            table = {}
            for row in lines[i + 2:]:
                if not row.startswith("|"):
                    break
                parts = [c.strip() for c in row.strip().strip("|").split("|")]
                table[parts[0]] = int(parts[col])
            return table
    return {}


def check_weights():
    for skill_name in ("linkedin-profile-audit", "linkedin-company-page-audit"):
        path = SKILLS / skill_name / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        table = weight_table(text)
        stated = re.search(r"Total weight: (\d+)", text)
        if not table:
            fail(path, "no weight table found")
            continue
        if not stated:
            fail(path, "missing 'Total weight: N' line")
        elif int(stated.group(1)) != sum(table.values()):
            fail(path, f"says Total weight: {stated.group(1)}, but the table sums to {sum(table.values())}")
    rubric_path = SKILLS / "linkedin-profile-audit" / "references" / "scoring-rubric.md"
    rubric = dict(
        (name.strip(), int(w))
        for name, w in re.findall(r"^## (.+?) \(weight (\d+)\)$", rubric_path.read_text(encoding="utf-8"), re.M)
    )
    table = weight_table((SKILLS / "linkedin-profile-audit" / "SKILL.md").read_text(encoding="utf-8"))
    if rubric != table:
        fail(rubric_path, f"rubric sections/weights {rubric} do not match the SKILL.md table {table}")


def check_manifests(versions, names):
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    versions["plugin.json version"] = plugin.get("version")
    market_path = ROOT / ".claude-plugin" / "marketplace.json"
    market = json.loads(market_path.read_text(encoding="utf-8"))
    for key in ("name", "owner", "plugins"):
        if key not in market:
            fail(market_path, f"missing required '{key}'")
    entries = market.get("plugins", [])
    if not any(e.get("name") == plugin.get("name") and e.get("source") == "./" for e in entries):
        fail(market_path, f"needs an entry named '{plugin.get('name')}' with source './'")
    for e in entries:
        if "version" in e:
            fail(market_path, "leave version to plugin.json (plugin.json wins and validate warns)")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    top = re.search(r"^## \[(\d+\.\d+\.\d+)\]", changelog, re.M)
    versions["CHANGELOG.md latest"] = top.group(1) if top else None
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    badge = re.search(r"badge/version-(\d+\.\d+\.\d+)-", readme)
    versions["README version badge"] = badge.group(1) if badge else None
    for name in names:
        if f"**{name}**" not in readme:
            fail(ROOT / "README.md", f"skills table is missing {name}")
    if len(set(versions.values())) != 1:
        fail(ROOT, "versions disagree: " + ", ".join(f"{k}={v}" for k, v in sorted(versions.items())))


def check_evals(names):
    """Cases live in the plugin-level evals/ folder, one folder per case, in the
    layout `claude plugin eval` reads. Each case is tagged with its skill name."""
    evals = ROOT / "evals"
    cases = sorted(p for p in evals.iterdir() if p.is_dir() and p.name != "results") if evals.is_dir() else []
    per_skill = {name: 0 for name in names}
    for case in cases:
        if not CASE_NAME_RE.match(case.name) or case.name in RESERVED_CASE_NAMES:
            fail(case, "case name must be lowercase letters, digits, hyphens, starting with a letter")
        prompt = case / "prompt.md"
        if not prompt.is_file():
            fail(case, "missing prompt.md")
        else:
            block, body = split_frontmatter(prompt.read_text(encoding="utf-8"))
            if block is None or not body.strip():
                fail(prompt, "needs a settings block and a prompt")
            else:
                settings = dict(
                    (l.split(":", 1)[0].strip(), l.split(":", 1)[1].strip())
                    for l in block.splitlines() if ":" in l
                )
                for key in set(settings) - PROMPT_SETTINGS:
                    fail(prompt, f"unknown settings key '{key}' (the case would fail to load)")
                tags = re.findall(r"[a-z0-9-]+", settings.get("tags", ""))
                skill_tags = [t for t in tags if t in names]
                if not skill_tags:
                    fail(prompt, "tags must include the skill this case tests")
                for t in skill_tags:
                    per_skill[t] += 1
        case_yaml = case / "case.yaml"
        if case_yaml.is_file():
            text = case_yaml.read_text(encoding="utf-8")
            if 'schema_version: "1.1"' not in text:
                fail(case_yaml, 'needs schema_version: "1.1" (quoted)')
            if f"name: {case.name}\n" not in text:
                fail(case_yaml, f"name must be {case.name}")
            if "expected_outcome: |" not in text:
                fail(case_yaml, "needs expected_outcome: |")
        graders = sorted((case / "graders").glob("*.md")) if (case / "graders").is_dir() else []
        if not graders:
            fail(case, "needs at least one grader in graders/")
        for g in graders:
            block, body = split_frontmatter(g.read_text(encoding="utf-8"))
            if block is None or "type:" not in block or "weight:" not in block or not body.strip():
                fail(g, "grader needs a type and weight block, then one statement")
    for name, count in sorted(per_skill.items()):
        if count < 2:
            fail(evals, f"{name} has {count} eval case(s); add at least 2")


def run_checks():
    skills = skill_dirs()
    names = {s.name for s in skills}
    versions = {}
    for skill in skills:
        check_frontmatter(skill, versions)
        check_references(skill)
    check_evals(names)
    check_skill_names(names)
    check_em_dashes()
    check_templates(banned_phrases())
    check_weights()
    check_manifests(versions, names)
    return len(skills)


def main(argv):
    if argv[:1] == ["lint"]:
        if len(argv) < 2:
            print(__doc__)
            return 2
        phrases = banned_phrases()
        for name in argv[1:]:
            path = Path(name).resolve()
            lint_text(path.read_text(encoding="utf-8"), path, phrases)
    else:
        if "--fix" in argv:
            sync_shared()
        count = run_checks()
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s) found.")
        return 1
    print("lint passed." if argv[:1] == ["lint"] else f"All checks passed ({count} skills).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
