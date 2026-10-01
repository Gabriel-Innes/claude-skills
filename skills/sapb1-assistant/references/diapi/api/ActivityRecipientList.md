<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ActivityRecipientList (Object)

ActivityRecipientList Class

## Properties (5)
- `Public Property Active() As BoYesNoEnum` [R/W] property Active
- `Public Property ActivityRecipientCollection() As ActivityRecipientCollection` [R] property ActivityRecipientCollection
- `Public Property Code() As Long` [R] property Code
- `Public Property IsMultiple() As BoYesNoEnum` [R] property IsMultiple
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
