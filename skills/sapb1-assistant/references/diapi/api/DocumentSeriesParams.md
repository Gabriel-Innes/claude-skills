<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DocumentSeriesParams (Object)

The DocumentSeriesParams specifies the identification key combination (Document and Series) for which the Documents is related. Source table: NNM1. DocumentSeries

**Remarks:** To display the form in the application: - Select a document type (for example: Sales A/R -- Sales Quotation). - Select Tools -- Print Layout Designer. - Choose a template name for the specified document type. - Click Set as default.

## Properties (3)
- `Public Property Document() As String` [R/W] Sets or returns the key of the document type for which the series relates. Field name: Document. Length: 20 characters.
- `Public Property DocumentSubType() As String` [R/W] Sets or returns the Document Sub-Type. Field name: DocSubType. Length: 2 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the Series a part of a document name. Field name: Series.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
