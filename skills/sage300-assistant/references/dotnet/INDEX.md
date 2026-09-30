# .NET / C# (ACCPAC.Advantage View API) index

Read this first, then open only what the request needs. All idioms are version-independent; defaults target
Sage 300 2026 (7.3A). Field names and single-table rotoIDs are verified against `references/dictionary/<version>/`.

| Path | Covers | Sage 300 versions | Verified |
|---|---|---|---|
| `view-api.md` | The correct way to program the Sage 300 .NET View API: environment/build (Framework, x86, workstation + seat), session lifecycle (Init/Open/OpenDBLink), open & compose views, view verbs & field access (`SetValue` verify flag), header/detail create-and-post, reading/querying, optional fields & transactions, a greenfield `IDisposable` scaffold, finding rotoIDs/compose order (macro-record), verifying against the dictionary, and error-stack handling | all (idioms); defaults 2026/7.3A | 2026-09-25 |
| `common-mistakes.md` | Anti-patterns from real integrations → the correct alternative: construction-time SignOn, no dispose/seat leaks, guessed rotoIDs/compose order, lossy catch, swallowed errors, magic numbers, raw SQL into Sage tables, SQL injection | version-independent | 2026-09-25 |
| `compose-graphs.md` | Verified view-composition graphs for 19 core transaction documents (OE/PO/IC/AR/AP/GL): the views to open and the exact `Compose()` slot order per view — so `OpenView`/`Compose` code isn't guessed. Extracted from the 7.3A AOM; stable across 7.0A–7.3A | 7.3A (applies 7.0A–7.3A) | 2026-09-25 |
| `api/INDEX.md` | Authoritative `ACCPAC.Advantage` class/enum surface, extracted from the shipped `Sage Accpac .NET Libraries.chm` (library 5.5.0.1). Start here to look up an **exact** signature, parameter, return value, or enum value: `api/enums.md` (all 38 enumerations + member meanings) and the class bundles `api/classes-session.md`, `api/classes-view.md`, `api/classes-system.md` (31 classes — summary, C# declaration, property/method tables, per-method C# signatures + parameters + returns + remarks; `api/INDEX.md` maps each class to its bundle). This is the *signature/enum* reference; `view-api.md` is the *how-to*. | all (idioms); library 5.5.0.1 | 2026-09-25 |

Sources are cited inline (Stephen Smith's smist08.wordpress.com .NET API series + Sage community R&D); URLs are
listed at the foot of `view-api.md`. External post text is cited, not reproduced.
