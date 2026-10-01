<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DocumentAuthorizationStatusEnum (Enumeration)

Status of the document and authorization.

| Member | Value | Description |
|---|---|---|
| dasWithout | 0 | Without a status. |
| dasPending | 1 | The status of a transaction awaiting approval. |
| dasApproved | 2 | The status of a transaction that has been approved, but not yet converted from a draft to a regular document. |
| dasRejected | 3 | The status of a transaction that was not approved and remains a draft. The authorizer can grant approval for a rejected transaction by changing the status accordingly. |
| dasGenerated | 4 | The status of a transaction that has been approved and converted from a draft to a regular document by the originator. |
| dasGeneratedbyAuthorizer | 5 | The status of a transaction that has been approved and converted from a draft to a regular document by the authorizer. |
| dasCancelled | 6 | An approval procedure can be cancelled and restarted as necessary. If the approval procedure is cancelled, the draft document cannot be converted to a regular document. |
