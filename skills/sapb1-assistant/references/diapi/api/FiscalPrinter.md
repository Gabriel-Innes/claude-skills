<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FiscalPrinter (Object)

FiscalPrinter Class

## Properties (6)
- `Public Property EquipmentNo() As String` [R/W] property EquipmentNo
- `Public Property FiscalDocumentModel() As String` [R/W] property FiscalDocumentModel
- `Public Property FiscalPrintersParams() As FiscalPrintersParams` [R] property FiscalPrintersParams
- `Public Property ManufacturerSerialN() As String` [R/W] property ManufacturerSerialN
- `Public Property Model() As String` [R/W] property Model
- `Public Property RegisterNo() As Long` [R/W] property RegisterNo

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
