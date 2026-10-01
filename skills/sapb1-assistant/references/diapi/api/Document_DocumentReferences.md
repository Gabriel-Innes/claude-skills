<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Document_DocumentReferences (Object)

Document_DocumentReferences Class

## Properties (18)
- `Public Property AccessKey() As String` [R/W] property AccessKey
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExtDocNum
- `Public Property FiscalDocumentModel() As String` [R/W] property Model
- `Public Property FiscalDocumentNumber() As Long` [R/W] property Number
- `Public Property FiscalDocumentSeries() As String` [R/W] property Series
- `Public Property FiscalDocumentSubseries() As String` [R/W] property SubSeries
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property IssuerCNPJ() As String` [R/W] property IssuerCNPJ
- `Public Property IssuerCode() As String` [R/W] property IssuerCode
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property LinkReferenceType() As LinkReferenceTypeEnum` [R/W] property LinkRefTyp
- `Public Property ReferencedAccessKey() As String` [R/W] property RefAccKey
- `Public Property ReferencedAmount() As Double` [R/W] property RefAmount
- `Public Property ReferencedDocEntry() As Long` [R/W] property RefDocEntr
- `Public Property ReferencedDocNumber() As Long` [R] property RefDocNum
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property RefObjType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (3)
- `Public Sub Add()` method Add
- `Public Sub Delete()` method Delete
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` method SetCurrentLine
  - param `LineNum`:
