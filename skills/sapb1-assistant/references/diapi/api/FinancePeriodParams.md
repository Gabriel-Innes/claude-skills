<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# FinancePeriodParams (Object)

The FinancePeriodParams specifies the identification key(system number, period indicator ) for which the CompanyService is related.

## Properties (2)
- `Public Property AbsoluteEntry() As Long` [R/W] Sets or returns the System Number, a key to the CompanyService. Field name: AbsEntry.
- `Public Property PeriodIndicator() As String` [R/W] Sets or returns the period indicator. Field name: Indicator. Length: 10 characters. This is a foreign key to the Period Indicators table OPID, which is not exposed through the DI API.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
