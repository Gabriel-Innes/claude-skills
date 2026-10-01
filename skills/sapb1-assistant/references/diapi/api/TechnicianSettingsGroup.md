<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TechnicianSettingsGroup (Object)

TechnicianSettingsGroup Class

## Properties (11)
- `Public Property AdvancedDashBoard() As Long` [R/W] property AdvancedDashBoard
- `Public Property Code() As Long` [R] property Code
- `Public Property CustomizedGroup() As BoYesNoEnum` [R/W] property CustomizedGroup
- `Public Property EnableActualDuration() As BoYesNoEnum` [R/W] property EnableActualDuration
- `Public Property EnableEditTime() As BoYesNoEnum` [R/W] property EnableEditTime
- `Public Property EnableFollowup() As BoYesNoEnum` [R/W] property EnableFollowup
- `Public Property EnableReject() As BoYesNoEnum` [R/W] property EnableReject
- `Public Property EnableResign() As BoYesNoEnum` [R/W] property EnableResign
- `Public Property EnableSignature() As BoYesNoEnum` [R/W] property EnableSignature
- `Public Property EnableStarRating() As BoYesNoEnum` [R/W] property EnableStarRating
- `Public Property Name() As String` [R/W] property Name

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
