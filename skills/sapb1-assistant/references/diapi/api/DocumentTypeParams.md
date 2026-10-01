<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DocumentTypeParams (Object)

The DocumentTypeParams specifies the identification key combination (Document and DocumentSubType) for which the Documents object is related. Source table: NNM2.

## Properties (2)
- `Public Property Document() As String` [R/W] Sets or returns the Document code. Field name: ObjectCode. For example: The Document property shall return 13 for A/R Invoice. Length: 20 Characters.
- `Public Property DocumentSubType() As String` [R/W] Sets or returns the document sub-type. Field name: DocSubType.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
