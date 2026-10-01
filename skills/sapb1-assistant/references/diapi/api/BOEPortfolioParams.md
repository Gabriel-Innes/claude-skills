<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BOEPortfolioParams (Object)

This object holds identification properties for the BOEPortfoliosService object.

## Properties (3)
- `Public Property PortfolioCode() As String` [R] Returns a number specifying the portfolio code. Field name: PtfCode.
- `Public Property PortfolioEntry() As Long` [R/W] Sets or returns a string specifying the portfolio entry. Field name: AbsEntry.
- `Public Property PortfolioID() As String` [R] Returns a number specifying the internal portfolio id. Field name: PtfId.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
