<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReportBusinessPartners (Collection)

TaxReportBusinessPartners is a Data Collection of TaxReportBusinessPartner data structures. Source table: VTR4. Remark: VTR4 is a virtual table and not exposed in the database reference files.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of TaxReportBusinessPartner data structures in the TaxReportBusinessPartners data collection.

## Methods (5)
- `Public Function Add() As TaxReportBusinessPartner` Adds a new TaxReportBusinessPartner to the TaxReportBusinessPartners data collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As TaxReportBusinessPartner` Returns reference to existing TaxReportBusinessPartner in the collection by its index.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
