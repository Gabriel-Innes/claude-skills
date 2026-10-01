<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BlanketAgreementStatusEnum (Enumeration)

The status of the blanket agreement.

| Member | Value | Description |
|---|---|---|
| asApproved | 0 | You can sell or buy items and thus create sales or purchasing documents associated with the blanket agreement. |
| asOnHold | 1 | Blanket agreement is set to inactive, and you cannot sell or buy items and thus create sales or purchasing documents associated with the blanket agreement. |
| asDraft | 2 | The blanket agreement is not approved, and you cannot sell or buy items and thus create sales or purchasing documents associated with the blanket agreement. |
| asTerminated | 3 | The blanket agreement is terminated, and you can only sell or buy items and thus create sales or purchasing documents associated with the blanket agreement, if the posting date of the document lies within the date range of the agreement. That is, the document's posting date lies between the start date and the termination date of the agreement. To end the blanket agreement, you specify the termination date in the Termination Date field. SAP Business One sets the status to Terminated. |
