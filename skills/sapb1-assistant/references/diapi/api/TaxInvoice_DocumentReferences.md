<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxInvoice_DocumentReferences (Object)

TaxInvoice_DocumentReferences Class

## Properties (10)
- `Public Property CardCode() As String` [R/W] property CardCode
- `Public Property Count() As Long` [R] property Count
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property ExternalReferencedDocNumber() As String` [R/W] property ExternalReferencedDocNumber
- `Public Property IssueDate() As Date` [R/W] property IssueDate
- `Public Property LineNumber() As Long` [R] property LineNumber
- `Public Property ReferencedDocEntry() As Long` [R/W] property ReferencedDocEntry
- `Public Property ReferencedDocNumber() As Long` [R] property ReferencedDocNumber
- `Public Property ReferencedObjectType() As ReferencedObjectTypeEnum` [R/W] property ReferencedObjectType
- `Public Property Remark() As String` [R/W] property Remark

## Methods (2)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
