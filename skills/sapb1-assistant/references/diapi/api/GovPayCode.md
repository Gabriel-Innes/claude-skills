<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# GovPayCode (Object)

GovPayCode Class

## Properties (6)
- `Public Property AbsId() As Long` [R] property AbsId
- `Public Property Authorities() As GovPayCodeAuthorities` [R] property Authorities
- `Public Property Code() As String` [R/W] property Code
- `Public Property Description() As String` [R/W] property Description
- `Public Property Periodicity() As GovPayCodePeriodicityEnum` [R/W] property Periodicity
- `Public Property StateTax() As BoYesNoEnum` [R/W] property StateTax

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
