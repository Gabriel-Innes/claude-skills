# claude-skills

A public collection of [Agent Skills](https://agentskills.io/specification) for Claude, by Francois Taljaard.

## Skills

| Skill | What it does |
|---|---|
| [`sage300-assistant`](skills/sage300-assistant) | Sage 300 (Accpac) ERP assistant for consultants and integrators: verified T-SQL views/queries from bundled AOM data dictionaries, version/upgrade guidance and release notes, and C# against the `ACCPAC.Advantage` .NET library. |

## Installing a skill

Copy the skill folder into your Claude skills directory:

- **Claude Code (all projects):** `~/.claude/skills/<skill-name>/`
- **Claude Code (one project):** `<project>/.claude/skills/<skill-name>/`

For example:

```bash
git clone https://github.com/fdtaljaard/claude-skills.git
cp -r claude-skills/skills/sage300-assistant ~/.claude/skills/
```

Each skill's `SKILL.md` describes when it triggers and how it works; `MAINTENANCE.md` (where present) covers how it is built and kept up to date.

## Layout

```
skills/
  <skill-name>/
    SKILL.md        # entry point loaded on activation
    references/     # bulk reference material, read on demand
    scripts/        # maintenance tooling (not needed at runtime)
```

## Disclaimer

Sage 300 and Accpac are trademarks of their respective owners. This project is independent and not affiliated with or endorsed by Sage. Reference material bundled with `sage300-assistant` is derived from Sage's published documentation and product metadata for use as a lookup aid; always verify against official Sage documentation before acting on it in a production system.
