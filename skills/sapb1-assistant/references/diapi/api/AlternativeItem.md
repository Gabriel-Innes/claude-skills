<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlternativeItem (Object)

A data structure object related to the AlternativeItemsService service. Source table: OALI.

## Properties (3)
- `Public Property AlternativeItemCode() As String` [R/W] Sets or returns unique ID of the alternative item.
- `Public Property MatchFactor() As Double` [R/W] Returns or sets a value specifying the matching degree of this item with the original item. A higher value represents a higher match.
- `Public Property Remarks() As String` [R/W] Returns or sets a string specifying comments to this alternative item.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
