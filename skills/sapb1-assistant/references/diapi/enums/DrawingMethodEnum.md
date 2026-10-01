<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DrawingMethodEnum (Enumeration)

Methods of calculating freight per row in a document. The calculation method is relevant when you copy rows from a base document to a target document.

| Member | Value | Description |
|---|---|---|
| dmNone | 0 | No freight is copied. |
| dmQuantity | 1 | The amount is divided by the item quantity and each unit is charged the same amount of freight. |
| dmTotal | 2 | SAP Business One calculates the portion of the document total or row total is copied to the target document, and then adds the relative amount of the document or row freight to the target document. |
| dmAll | 3 | All freight is copied. |
