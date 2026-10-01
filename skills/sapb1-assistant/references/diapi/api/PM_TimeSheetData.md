<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PM_TimeSheetData (Object)

PM_TimeSheetData Class

## Properties (14)
- `Public Property AbsEntry() As Long` [R/W] property AbsEntry
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property DateFrom() As Date` [R/W] property DateFrom
- `Public Property Dateto() As Date` [R/W] property DateTo
- `Public Property Department() As Long` [R/W] property Department
- `Public Property DocNumber() As Long` [R] property DocNumber
- `Public Property FirstName() As String` [R/W] property FirstName
- `Public Property LastName() As String` [R/W] property LastName
- `Public Property PM_TimeSheetLineDataCollection() As PM_TimeSheetLineDataCollection` [R] property PM_TimeSheetLineDataCollection
- `Public Property SAPPassport() As String` [R] property SAPPassport
- `Public Property TimeSheetType() As TimeSheetTypeEnum` [R/W] property TimeSheetType
- `Public Property UserCode() As String` [R/W] property UserCode
- `Public Property UserFields() As Fields` [R] property User Fields
- `Public Property UserID() As Long` [R/W] property UserID

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
