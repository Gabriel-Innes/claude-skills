<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReportFilterParams (Object)

The TaxReportFilterParams specifies the identification key combination(Code, Filter-Type and Name) for which the TaxReportsService is related. Source table: OVTR.

## Properties (3)
- `Public Property Code() As Long` [R/W] Sets or returns the unique code of this tax report filter. Field name: AbsEntry.
- `Public Property FilterType() As TaxReportFilterType` [R/W] Sets or returns a valid value that determines selection criteria type for this report. Field name: FilterType.
- `Public Property Name() As String` [R] Returns this report name . Field name: ReportName. Length: 50 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the index of the item that you want to get.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Creates an XML string that represents the object data.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
