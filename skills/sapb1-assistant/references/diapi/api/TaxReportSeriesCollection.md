<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReportSeriesCollection (Collection)

TaxReportSeriesCollection is a Data Collection of TaxReportSeries. Source table: VTR3.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportSeries. in the TaxReportSeriesCollection data collection. Field name: .

## Methods (5)
- `Public Function Add() As TaxReportSeries` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportSeries` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates XML file that represents the object data.
