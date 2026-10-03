<!-- source: Pastel.Evolution.chm + Pastel.Evolution.xml (+ Pastel.Evolution.dll for enum members), SDK 11.0.0.10 | verified: 2026-10-03 -->

# Pastel Evolution SDK reference index

Read this first, then open only what the request needs. The SDK is `Pastel.Evolution.dll` (namespace
`Pastel.Evolution`), the managed object layer Sage 200 Evolution / Pastel Evolution ships for reading and
writing accounting data through its own business logic. Extracted from the shipped `Pastel.Evolution.chm`
(primary) with summaries backfilled from `Pastel.Evolution.xml`, SDK **11.0.0.10**; enumeration members the
CHM omits were read from `Pastel.Evolution.dll` by reflection.

| Path | Covers | Verified |
|---|---|---|
| `sdk-guide.md` | The correct way to drive the SDK: environment/build, connecting via `DatabaseContext` (accounting + `EvolutionCommon` databases), the `RecordBase` load/set/`Save()` pattern, transactional/posting objects, atomic transactions (`BeginTran`/`CommitTran`/`RollBackTran`), generating correct C#, and lookup recipes | 2026-10-02 |
| `common-mistakes.md` | Anti-patterns → the correct alternative: raw SQL writes, missing common connection, guessed members/enums, un-transacted multi-record writes, parallel connections, version mismatch, swallowed errors | 2026-10-02 |
| `api/INDEX.md` | Authoritative class/interface/struct/delegate surface (152 types): per type a summary, C# declaration, and property/method/field/event members with signatures, parameters, returns and remarks. One line per type gives its bundle **file + line range** — read exactly that range, or grep `^# <Type> (`. Bundles: `api/classes-01.md`…`classes-03.md` | 2026-10-02 |
| `enums/INDEX.md` | All 94 public enumerations with **Member / Value / Description** tables and a `Source` column — the CHM documents members for 6; the rest come from `Pastel.Evolution.dll` by reflection (values, no descriptions), 53 of them undocumented in the CHM. Look up the integer value; use the named constant in code. Bundle: `enums/enums-01.md` | 2026-10-03 |

**Workflow:** pin the request (which module/record/document; read vs. create/post) → read `sdk-guide.md` and
`common-mistakes.md` → find the exact types in `api/INDEX.md` and verify every member/enum there → generate
C# using the record/transaction pattern, citing the files. Never emit a class, property, method or enum value
you haven't seen in `api/`/`enums/`.
