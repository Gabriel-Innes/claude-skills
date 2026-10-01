<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ResourceIssueMethodEnum (Enumeration)

Issue method for the resource consumption.

| Member | Value | Description |
|---|---|---|
| rimBackflush | 0 | Upon receiving finished items on a production order, the resource capacity is automatically consumed, that is, the issue to production is then automatically issued. Default value. |
| rimManual | 1 | Receipt of finished items on a production order does not impact the capacity of the resource. Resource consumption (issue to production) must be issued manually. |
