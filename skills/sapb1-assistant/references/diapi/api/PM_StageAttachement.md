<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PM_StageAttachement (Object)

Source table: PMG1.AtcEntry.

## Properties (6)
- `Public Property AbsEntry() As Long` [R] property AbsEntry
- `Public Property AttachementDate() As Date` [R/W] property AttachementDate
- `Public Property FileExtension() As String` [R/W] property FileExtension
- `Public Property FileName() As String` [R/W] property FileName
- `Public Property LineId() As Long` [R] property LineID
- `Public Property SourcePath() As String` [R/W] property SourcePath

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
