# Sage Intacct Assistant

**Coming soon.** This is a scaffold for a reference-backed Claude skill for **Sage Intacct** consultants and
integrators. No capability is implemented yet and no references are bundled.

When it lands it will work like the other assistants in this collection: ask in plain English, it looks the
answer up in bundled, attributed references, cites where it came from, and tells you what it could not verify.

## What it does

| Ask about | What you get |
|---|---|
| *(nothing yet)* | |

## Install

Not yet published. Once the first capability lands the skill will be installable the same way as the others:

```
/plugin marketplace add fdtaljaard/claude-skills
/plugin install sageintacct-assistant@fdtaljaard-skills
```

or packaged for the Claude desktop app and claude.ai with:

```bash
python skills/sageintacct-assistant/scripts/package_skill.py skills/sageintacct-assistant dist
```

## Keeping it current and contributing

- [`SKILL.md`](SKILL.md) is what Claude loads; it describes routing, ground rules, the workflow and the gotchas.
- [`MAINTENANCE.md`](MAINTENANCE.md) explains the conventions and how to add a capability.
- [`evals/evals.json`](evals/evals.json) holds test prompts per capability.
- Corrections and additions are welcome. See the repository's [CONTRIBUTING.md](../../CONTRIBUTING.md).

## Disclaimer

Sage and Sage Intacct are trademarks of The Sage Group plc or its affiliates. This skill is independent and not
affiliated with or endorsed by Sage. Confirm against Sage Intacct's documentation, and on the client's company,
before relying on any of it.
