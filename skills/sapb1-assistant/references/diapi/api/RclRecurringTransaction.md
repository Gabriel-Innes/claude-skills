<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# RclRecurringTransaction (Object)

RclRecurringTransaction Class

## Properties (7)
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property DocType() As String` [R] property DocType
- `Public Property Instance() As Long` [R] property Instance
- `Public Property PlannedDate() As Date` [R] property PlannedDate
- `Public Property Status() As RclRecurringTransactionStatusEnum` [R] property Status
- `Public Property TemplateID() As Long` [R] property TemplateID
- `Public Property TransactionID() As Long` [R] property TransactionID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
