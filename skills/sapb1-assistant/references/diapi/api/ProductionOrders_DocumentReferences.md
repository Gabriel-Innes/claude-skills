<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ProductionOrders_DocumentReferences (Object)

ProductionOrders_DocumentReferences Class

## Properties (9)
- `Public Property Count() As Long` [R] property Count
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExtDocNum
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ReferencedDocEntry() As Long` [R/W] property RefDocEntr
- `Public Property ReferencedDocNumber() As Long` [R] property RefDocNum
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property RefObjType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`:
