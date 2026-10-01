<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ExternalCallStatusEnum (Enumeration)

Statuses for a request call.

| Member | Value | Description |
|---|---|---|
| ecsNew | 0 | The request call is newly created and not processed by any applications. |
| ecsInProcess | 1 | The request call is received and is in process by the receiver applications. |
| ecsCompleted | 2 | The request call is completed successfully by the receiver applications. |
| ecsConfirmed | 3 | The request call is completed successfully and confirmed by the sender application (usually SAP Business One). |
| ecsFailed | 4 | The process of the request call failed. |
