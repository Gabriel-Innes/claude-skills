# acumatica-assistant: scrubbed builder inputs

Machine-generated inputs that `skills/acumatica-assistant/scripts/` needs to regenerate a bundled reference. They
are kept here, outside the skill folder, so they are never packaged or loaded at runtime, and so that anyone can
rebuild the generated files and review a builder change by diffing its output.

| File | What it is | How it was scrubbed | Regenerates |
|---|---|---|---|
| `Default-25.200.001.swagger.json` | **Pending.** The OpenAPI 3.0 document of the `Default/25.200.001` system endpoint (Acumatica ERP 2025 R2, build 25.201.0213) that produced the bundled snapshot | `servers` removed by `build_endpoint_reference.py --scrub-to`; the script refuses to write it if any part of the source host name appears in it | `skills/acumatica-assistant/references/endpoints/Default-25.200.001/` |

A system endpoint's contract is fixed by Acumatica, so the document is the same on every instance of that release.
Its only instance-specific member is the `servers` URL, which the builder strips. Custom endpoints, endpoint
extensions and anything carrying a customer's own entities or fields never go here.

To regenerate a snapshot from a file in this folder, run from `skills/acumatica-assistant/`:

```
python scripts/build_endpoint_reference.py --swagger ../../sources/acumatica-assistant/Default-25.200.001.swagger.json --out references/endpoints --release "2025 R2" --build 25.201.0213 --verified YYYY-MM-DD --source-note "a sandbox instance; instance name withheld, raw file not in the repository"
```

The procedure for capturing and scrubbing a new one is "Add or refresh an endpoint snapshot" in
`skills/acumatica-assistant/MAINTENANCE.md`.
