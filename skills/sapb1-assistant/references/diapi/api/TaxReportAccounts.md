<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReportAccounts (Collection)

TaxReportAccounts is a Data Collection of TaxReportAccount data structures. Source table: VTR5.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportAccount data structures in the TaxReportAccounts data collection.

## Methods (5)
- `Public Function Add() As TaxReportAccount` Adds a new TaxReportAccount to the TaxReportAccounts data collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportAccount` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
