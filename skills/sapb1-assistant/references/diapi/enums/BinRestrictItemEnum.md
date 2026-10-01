<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BinRestrictItemEnum (Enumeration)

The item restriction status of the bin location.

| Member | Value | Description |
|---|---|---|
| briNone | 0 | None - the bin location has no item restrictions, that is, the bin location can store any item. |
| briSpecificItem | 1 | Specific Item - the bin location is restricted to a specific item, that is, the bin location can only store a specific item. |
| briSingleItemOnly | 2 | Single Item Only - the bin location is restricted to a single item, that is, the bin location can only store one item. |
| briSpecificItemGroup | 3 | Specific Item Group - the bin location is restricted to a specific item group, that is, the bin location can only store items from a specific item group. |
| briSpecificItemGroupOnly | 4 | Single Item Group Only - the bin location is restricted to a single item group, that is, the bin location can only store items from one item group. |
