<img src="assets/logo.svg" alt="claude-skills logo" width="88" align="right" />

# claude-skills

[![License: MIT](https://img.shields.io/github/license/fdtaljaard/claude-skills)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/fdtaljaard/claude-skills)](https://github.com/fdtaljaard/claude-skills/releases)
[![Claude Code plugin marketplace](https://img.shields.io/badge/Claude%20Code-plugin%20marketplace-5A4FE5)](#installing-a-skill)

A public collection of [Agent Skills](https://agentskills.io/specification) for Claude, by Francois Taljaard — reference-backed assistants for ERP consultants and integrators (Sage 300, Sage 200 Evolution, SAP Business One).

> **The point of these skills: no guessing.** Every material claim — a table or field, an enum value, a version requirement, an SDK class or method — comes from a **bundled reference** (data dictionaries, release notes, SDK class/enum references extracted from the vendors' own files) or a fresh fetch of the vendor's official docs, and is **cited**. Field names, enum values and version facts are exactly what a language model otherwise guesses plausibly and wrongly, so each skill is built to look them up and show its source.

## Skills

| Skill | What it does |
|---|---|
| [`sage300-assistant`](skills/sage300-assistant) | Sage 300 (Accpac) ERP assistant for consultants and integrators: verified T-SQL views/queries from bundled AOM data dictionaries, version/upgrade guidance and release notes, and C# against the `ACCPAC.Advantage` .NET library. |
| [`sage200-assistant`](skills/sage200-assistant) | Sage 200 Evolution (Pastel Evolution) ERP assistant for consultants and integrators: C# development against the `Pastel.Evolution` .NET SDK — connecting via `DatabaseContext`, the record load/set/`Save()` pattern, posting transactions, and generating correct code from a bundled class and enum reference (152 types, 41 enums) extracted from the shipped SDK CHM. More capabilities to follow. |
| [`sapb1-assistant`](skills/sapb1-assistant) | SAP Business One ERP assistant for consultants and integrators: object type number, table and primary key lookup from a bundled list of all B1 object types, verified SQL views/queries from bundled B1 10.0 and 9.3 data dictionaries (tables, columns, indexes, valid values, parent-table links), and C# development against the DI API (`SAPbobsCOM`) from a bundled DI API 10.0 class and enum reference. More capabilities to follow. |

## Example

Ask in plain language; the skill routes, looks up the reference, and shows its source:

> **You:** I need a SQL view of open sales orders with the customer name and order total — client's on Sage 300 2026.
>
> **Claude (with `sage300-assistant`):** Uses the bundled 7.3A data dictionary — `OEORDH` joined to `ARCUS`, "open" decoded from the `COMPLETE IN (1,2)` enum on `OEORDH` (not guessed), one row per order. Returns a complete `CREATE OR ALTER VIEW` with a `TOP 20` sanity check, the joins and status filter explained in business terms, and a note on which dictionary files each field came from.

Each skill refuses to guess: if a fact isn't in its references and can't be verified against the vendor's docs, it says so rather than inventing it — and it never writes SQL that modifies vendor-owned tables.

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

## Contributing

Issues and pull requests are welcome — corrections to a reference, a new skill, or a new capability on an existing one. See [CONTRIBUTING.md](CONTRIBUTING.md) for how skills are structured and the bar a change should meet (every claim verifiable and cited). To report a problem with the data a skill returns, or a security concern, see [SECURITY.md](SECURITY.md).

## License

The code and original content in this repository are released under the [MIT License](LICENSE). Reference material derived from Sage's documentation and product metadata remains subject to Sage's own terms (see the disclaimer below).

## Disclaimer

Sage 300 and Accpac are trademarks of their respective owners. This project is independent and not affiliated with or endorsed by Sage. Reference material bundled with `sage300-assistant` is derived from Sage's published documentation and product metadata for use as a lookup aid; always verify against official Sage documentation before acting on it in a production system.

Sage 200 Evolution and Pastel Evolution are trademarks of their respective owners. `sage200-assistant` is independent and not affiliated with or endorsed by Sage. Its SDK reference is extracted from the shipped `Pastel.Evolution.chm` and XML documentation for SDK version **11.0.0.10 only** (other versions are not included), and Sage's own terms apply to that material. It documents the `Pastel.Evolution` object SDK, not the Evolution ODBC/SQL layer or the Connector/API web service. Verify against Sage's own documentation, and on the client's installed SDK, before relying on any of it — the SDK binds to a licensed Evolution install of a matching version.

SAP and SAP Business One are trademarks of SAP SE. `sapb1-assistant` is independent and not affiliated with or endorsed by SAP. Its object type list is compiled from community websites, its B1 10.0 schema dictionary and DI API reference are compiled from SAP's own SDK help (`REFDB.chm`, `REFDI.chm`) and SAP's terms apply to them, and its 9.3 schema dictionary comes from erpref.com (a third party; the schema IP belongs to SAP) (sources and caveats are in `skills/sapb1-assistant/references/objects/INDEX.md`, `skills/sapb1-assistant/references/dictionary/INDEX.md` and `skills/sapb1-assistant/references/diapi/INDEX.md`). The schema dictionaries cover SAP Business One **10.0 and 9.3 only**; other releases (including later feature packs) and client-specific user-defined tables and fields are not included. Confirm against SAP's own documentation, and on the client's database, before relying on any of it.
