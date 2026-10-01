<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# DocumentSeriesUserParams (Object)

The DocumentSeriesUserParams specifies the identification key combination (Document, Series and Users) for which Documents is related. Source table: NNM2.

## Properties (4)
- `Public Property Document() As String` [R/W] Sets or returns the Document code. Field name: ObjectCode. For example: The Document property shall return 13 for A/R Invoice. Length: 20 Characters.
- `Public Property DocumentSubType() As String` [R/W] Sets or returns the Document Sub-Type. Field name: DocSubType. Length: 2 characters.
- `Public Property Series() As Long` [R/W] Sets or returns the Series Object, part of the document name. Field name: Series.
- `Public Property User() As Long` [R/W] Sets or returns the User Id, This is a foreign key to the Users object. Field name: UserSign).

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
