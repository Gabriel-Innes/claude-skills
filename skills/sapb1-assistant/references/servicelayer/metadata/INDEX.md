<!-- source: Service Layer /b1s/v2/$metadata | version: SAP Business One 10.0 FP 2602 | verified: 2026-10-05 -->

# Service Layer generated metadata reference

Built from an OData v4 `$metadata` snapshot. Namespaces: SAPB1.

| Path | Covers |
|---|---|
| `api/INDEX.md` | EntityType and ComplexType routing: keys, counts, filtered-property count, OpenType, BaseType, entity sets, bundle location |
| `api/members.md` | Flat `Type.Property : ODataType` index |
| `api/types-NN.md` | Full bundled type entries |
| `entity-sets.md` | Entity sets, containers, navigation bindings and scalar annotations |
| `operation-imports.md` | ActionImport/FunctionImport endpoint names mapped to operations |
| `operations/INDEX.md` | Action/Function routing: binding type, parameters, return type, bundle location |
| `operations/members.md` | Flat operation signatures |
| `operations/operations-NN.md` | Full bundled operations |
| `enums/INDEX.md` | Enum routing and bundle location |
| `enums/members.md` | Flat `Enum.Member = Value` index |
| `enums/enums-NN.md` | Full bundled enums |

## Counts

- schemas: 1
- types: 1080
- entity_types: 298
- complex_types: 782
- properties: 11054
- entity_sets: 330
- operation_imports: 603
- operations: 667
- actions: 643
- functions: 24
- enums: 473
- enum_members: 2827
- excluded: 414
- excluded_properties: 475
- kept_key_properties: 0

## Scope

- This is a snapshot of one Service Layer OData v4 metadata document; another feature pack can expose a different surface.
- A company can expose UDF properties explicitly in `$metadata`, including on `OpenType=true` types. Use property exclusion filters for a shared snapshot when the source company contains customer UDFs.
- A type whose properties or navigation properties were removed by a property exclusion filter carries a count-only `Filtered properties: N` line and a Filtered count in `api/INDEX.md`; removed names are never written. Key properties are never removed.
- A company can expose client-specific UDO/entity sets. Prefer a clean demo company or review/exclude custom names before committing a shared reference.
- Core CSDL and compact scalar annotations (inline and out-of-line `Annotations Target=`) are extracted; complex annotation expression trees remain in the source metadata.

## Exclusion filters

- generated name: `(?:^|[/\.])(?:U_|COR_|IAG_|SWA_)`

## Property exclusion filters

Matched against property and navigation-property names; a pattern containing `/` is also matched against the `Namespace.Type/Property` target.

- property/name target: `^U_`
