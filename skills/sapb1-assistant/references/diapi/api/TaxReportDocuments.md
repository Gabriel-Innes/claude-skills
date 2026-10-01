<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReportDocuments (Collection)

TaxReportDocuments is a Data Collection of TaxReportDocument data structures. Source table: VTR2.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportDocument data structures in the TaxReportDocuments data collection.

## Methods (5)
- `Public Function Add() As TaxReportDocument` Adds a new TaxReportDocument to the TaxReportDocuments data collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportDocument` Returns reference to existing TaxReportDocument item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
