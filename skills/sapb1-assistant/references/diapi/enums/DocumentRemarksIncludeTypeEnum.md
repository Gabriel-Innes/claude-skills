<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DocumentRemarksIncludeTypeEnum (Enumeration)

Determines the Remarks field when you copy a base marketing document to a target document.

| Member | Value | Description |
|---|---|---|
| driBaseDocumentNumber | 0 | Base document number: When you copy a base marketing document to a target document, the base document number is copied as well and is included in the Remarks field. |
| driBPReferenceNumber | 1 | BP reference number: When you copy a base marketing document to a target document, the customer or vendor reference number is copied as well and is included in the Remarks field. If the customer or vendor reference number doesn’t exist, the Remarks field remains unchanged. |
| driManualRemarksOnly | 2 | Manual remarks only: When you copy a base marketing document to a target document, the target Remarks field only includes the manual remarks from the base document. |
