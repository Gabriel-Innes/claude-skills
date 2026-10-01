<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ChecksforPaymentDocumentReferences (Object)

The document references of checks for payment. Source table: CHO3.

## Properties (9)
- `Public Property Count() As Long` [R] The count of rows. Field name: LogInstanc.
- `Public Property DocEntry() As Long` [R] The index (Primary Key). Field name: DocEntry.
- `Public Property ExternalReferencedDocNumber() As String` [R/W] External referenced document number. Field name: ExtDocNum. Length: 100 characters.
- `Public Property IssueDate() As Date` [R/W] Issue date. Field name: IssueDate.
- `Public Property LineNumber() As Long` [R] The row number (Primary Key). Field name: LineNum.
- `Public Property ReferencedDocEntry() As Long` [R/W] Referenced document internal number. Field name: RefDocEntr.
- `Public Property ReferencedDocNumber() As Long` [R] Referenced document number. Field name: RefDocNum.
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] Referenced object type. Field name: RefObjType. Length: 20 characters.
- `Public Property Remark() As String` [R/W] Field name: Remark. Length: 254 characters.

## Methods (2)
- `Public Sub Add()` method Add
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`:
