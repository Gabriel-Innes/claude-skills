<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxReportDocument (Object)

TaxReportDocument is a data structure related to the TaxReportsService. Source table: VTR2.

## Properties (3)
- `Public Property DocumentType() As TaxReportFilterDocumentType` [R/W] Sets or returns a valid value that determines Document Type . Field name: ObjectCode.
- `Public Property FromNumber() As Long` [R/W] Sets or returns the from document number. Field name: FromDocNo.
- `Public Property ToNumber() As Long` [R/W] Sets or returns the to document number. Field name: ToDocNo.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
