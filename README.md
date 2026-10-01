# claude-skills

A public collection of [Agent Skills](https://agentskills.io/specification) for Claude, by Francois Taljaard.

## Skills

| Skill | What it does |
|---|---|
| [`sage300-assistant`](skills/sage300-assistant) | Sage 300 (Accpac) ERP assistant for consultants and integrators: verified T-SQL views/queries from bundled AOM data dictionaries, version/upgrade guidance and release notes, and C# against the `ACCPAC.Advantage` .NET library. |
| [`sapb1-assistant`](skills/sapb1-assistant) | SAP Business One ERP assistant for consultants and integrators: object type number, table and primary key lookup from a bundled list of all B1 object types. More capabilities to follow. |

## Installing a skill

### With the skills CLI

```bash
npx -y skills add fdtaljaard/claude-skills --skill sage300-assistant --agent claude-code
```

### As a Claude Code plugin

```
/plugin marketplace add fdtaljaard/claude-skills
/plugin install sage300-assistant@fdtaljaard-skills
```

### Manually

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

## License

The code and original content in this repository are released under the [MIT License](LICENSE). Reference material derived from Sage's documentation and product metadata remains subject to Sage's own terms (see the disclaimer below).

## Disclaimer

Sage 300 and Accpac are trademarks of their respective owners. This project is independent and not affiliated with or endorsed by Sage. Reference material bundled with `sage300-assistant` is derived from Sage's published documentation and product metadata for use as a lookup aid; always verify against official Sage documentation before acting on it in a production system.

SAP and SAP Business One are trademarks of SAP SE. `sapb1-assistant` is independent and not affiliated with or endorsed by SAP. Its object type list is compiled from community websites, not SAP documentation (sources and caveats are in `skills/sapb1-assistant/references/objects/INDEX.md`); confirm against SAP's own documentation before relying on it.
