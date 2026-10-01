<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BoApprovalRequestStatusEnum (Enumeration)

Specifies the status of the approval request.

| Member | Value | Description |
|---|---|---|
| arsPending | 0 | The status of a transaction awaiting approval. |
| arsApproved | 1 | The status of a transaction that has been approved, but not yet converted from a draft to a regular document. |
| arsNotApproved | 2 | The status of a transaction that was not approved and remains a draft. The authorizer can grant approval for a rejected transaction by changing the status accordingly. |
| arsGenerated | 3 | The status of a transaction that has been approved and converted from a draft to a regular document by the originator. |
| arsGeneratedByAuthorizer | 4 | The status of a transaction that has been approved and converted from a draft to a regular document by the authorizer. |
| arsCancelled | 5 | An approval procedure can be cancelled and restarted as necessary. If the approval procedure is cancelled, the draft document cannot be converted to a regular document. |
