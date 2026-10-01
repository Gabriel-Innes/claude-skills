<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BOEPortfolio (Object)

A data structure object holding properties for the BOEPortfoliosService. Source table: OPTF.

## Properties (5)
- `Public Property PortfolioCode() As String` [R/W] Sets or returns a string specifying the portfolio code. Field name: PtfCode.
- `Public Property PortfolioDescription() As String` [R/W] Sets or returns a string specifying the portfolio description. Field name: PtfDespt.
- `Public Property PortfolioEntry() As Long` [R] Returns a number specifying the portfolio entry. Field name: AbsEntry.
- `Public Property PortfolioID() As String` [R/W] Sets or returns a string specifying the internal portfolio id. Field name: PtfId.
- `Public Property PortfolioNum() As String` [R/W] Sets or returns a string specifying the portfolio number. Field name: PtfNum.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the string of the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
