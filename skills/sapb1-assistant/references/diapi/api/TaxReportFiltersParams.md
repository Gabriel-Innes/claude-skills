<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReportFiltersParams (Collection)

TaxReportFiltersParams is a Data Collection of TaxReportFilterParams Identification key combination. Source table: OVTR.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportFilterParams identification keys in the TaxReportFiltersParams data collection.

## Methods (5)
- `Public Function Add() As TaxReportFilterParams` Adds a new record to the Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportFilterParams` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
