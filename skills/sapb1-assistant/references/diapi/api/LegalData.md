<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# LegalData (Object)

LegalData Class

## Properties (15)
- `Public Property DateOfPrinting() As Date` [R/W] property DateOfPrinting
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property DocumentNumber() As String` [R/W] property DocumentNumber
- `Public Property FiscalNumber() As String` [R/W] property FiscalNumber
- `Public Property FiscalSeries() As String` [R/W] property FiscalSeries
- `Public Property FiscalUserID() As Long` [R/W] property FiscalUserID
- `Public Property LegalDataDetailCollection() As LegalDataDetailCollection` [R] property LegalDataDetailCollection
- `Public Property PrinterBrand() As String` [R/W] property PrinterBrand
- `Public Property PrinterDllVersion() As String` [R/W] property PrinterDllVersion
- `Public Property PrinterFirmwareVersion() As String` [R/W] property PrinterFirmwareVersion
- `Public Property PrinterModel() As String` [R/W] property PrinterModel
- `Public Property PrinterType() As String` [R/W] property PrinterType
- `Public Property SourceObjectEntry() As Long` [R/W] property SourceObjectEntry
- `Public Property SourceObjectType() As BoAPARDocumentTypes` [R/W] property SourceObjectType
- `Public Property TimeOfPrinting() As Date` [R/W] property TimeOfPrinting

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString
