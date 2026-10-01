<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoPickStatus (Enumeration)

Specifies the options of the pick list status.

| Member | Value | Description |
|---|---|---|
| ps_Released | 0 | The pick list is released for picking. |
| ps_Picked | 1 | All the items have been picked. |
| ps_PartiallyPicked | 2 | Only part of the items, specified in the pick list, have been picked. |
| ps_PartiallyDelivered | 3 | Part of the items have been delivered. The lines for the delivered items cannot be updated. |
| ps_Closed | 4 | The pick list is closed. No additional items can be picked or delivered. |
