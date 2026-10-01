<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ElectronicDocumentEntryStatusEnum (Enumeration)

Status of electronic document. Source table: ECM2.

| Member | Value | Description |
|---|---|---|
| edesNone | 0 | Invalid status |
| edesNew | 1 | New document |
| edesReadyToProcess | 2 | Document is ready for processing |
| edesPending | 3 | Document is being prepared for processing |
| edesError | 4 | Document processing error |
| edesOK | 5 | Document was accepted by authority |
| edesSent | 6 | Document has been sent to external authority |
| edesDocError | 7 | Sent document contains syntactic or semantic errors |
| edesTempError | 8 | Communication-releated error |
| edesWarning | 9 | Document processing warning |
| edesWaiting | 10 | Document is waiting for user action |
| edesAuthorized | 11 | Document has been accepted by authority |
| edesInProcess | 12 | Document is being processed |
| edesRejected | 13 | Document can be re-sent again |
| edesDenied | 14 | Document can't be re-sent again |
| edesCanceled | 15 | Document has been canceled |
| edesAborted | 16 | User changed electronic document type to 'not relevant' |
| edesUnused | 17 | Document number skipping |
| edesQueued | 18 | Document is waiting in queue to become "New" |
| edesImported | 19 | Manually imported electronic document |
| edesApproved | 20 | Document has been approved |
| edesApproving | 21 | Document is waiting for approval |
| edesRejecting | 22 | Document approval has been rejected |
| edesGenerated | 23 | Draft document has been used to generate electronic document |
| edesDetermined | 24 | Imported document has been reconciled with existing documents |
| edesImporting | 25 |  |
