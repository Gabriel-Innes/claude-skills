<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoDefaultBatchStatus (Enumeration)

Specifies the default batch statuses.

| Member | Value | Description |
|---|---|---|
| dbs_Released | 0 | Enables the running of batch processes. |
| dbs_NotAccessible | 1 | Prevents the running of batch processes for sales documents and A/P credit memos. This setting is used for batch processes in production or undergoing a quality check. It allows, however, the running of batch processes in stock-transfer documents. This status is used for reports to distinguish between locked batches and not accessible ones. |
| dbs_Locked | 2 | Enables the running of batch processes in stock documents only, such as stock transfers or goods issues. |
