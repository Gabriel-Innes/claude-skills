<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# EDFEntryListInputParams (Object)

EDFEntryListInputParams Class

## Properties (14)
- `Public Property Ascending() As BoYesNoEnum` [R/W] property Ascending
- `Public Property BranchID() As Long` [R/W] property BranchID
- `Public Property CancellationStatusSet() As String` [R/W] property CancellationStatusSet
- `Public Property Code() As ElectronicDocProtocolCodeStrEnum` [R/W] property Code
- `Public Property FromDate() As Date` [R/W] property FromDate
- `Public Property FromEntryID() As Long` [R/W] property FromEntryID
- `Public Property FromTime() As Long` [R/W] property FromTime
- `Public Property MaxLines() As Long` [R/W] property MaxLines
- `Public Property ProcessingTarget() As ElectronicDocProcessingTargetEnum` [R/W] property ProcessingTarget
- `Public Property ProcessingTargetStr() As String` [R/W] property ProcessingTargetStr
- `Public Property StoreEntryStatusSet() As String` [R/W] property StoreEntryStatusSet
- `Public Property StoreEntryTypeSet() As String` [R/W] property StoreEntryTypeSet
- `Public Property ToDate() As Date` [R/W] property ToDate
- `Public Property ToTime() As Long` [R/W] property ToTime

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
