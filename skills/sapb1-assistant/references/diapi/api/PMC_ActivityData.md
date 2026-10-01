<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PMC_ActivityData (Object)

PMC_ActivityData Class

## Properties (5)
- `Public Property ActivityID() As Long` [R/W] property ActivityID
- `Public Property ActivityType() As String` [R/W] property ActivityType
- `Public Property IsAbsence() As BoYesNoEnum` [R/W] property IsAbsence
- `Public Property IsChargeable() As BoYesNoEnum` [R/W] property IsChargeable
- `Public Property LaborItem() As String` [R/W] property LaborItem

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
