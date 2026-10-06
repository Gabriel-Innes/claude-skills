# references/qbfc — index

Correct C# idioms for the QB SDK, QBFC-first (the typed COM wrapper, `Interop.QBFC<ver>`).

| File | Covers | Source | Verified |
|---|---|---|---|
| `csharp.md` | Full QBFC lifecycle (open connection → begin session → build `IMsgSetRequest` → append request → `DoRequests` → walk `IMsgSetResponse`/`IResponseList`, check `StatusCode`, cast `Detail`); OR aggregates in QBFC; query paging; Mod with `EditSequence`; linking invoice↔sales order; error handling | QB SDK / QBFC, author knowledge | 2026-10 |
| `common-mistakes.md` | The wrong patterns and why — session leaks, bitness/threading, version/feature gating, OR misuse, `FullName`-as-key, stale `EditSequence`, stock edited the wrong way, unchecked `StatusCode`, null response fields, COM-vs-status error confusion, formats | QB SDK / QBFC, author knowledge | 2026-10 |

Idioms are version-independent. Confirm exact method signatures and enum members (`ENOpenMode`,
`ENRqOnError`, `ENResponseType`) against the QBFC type library or the SDK's QBFC help (`.chm`), and object/
field names against the OSR (`../qbxml/`).
