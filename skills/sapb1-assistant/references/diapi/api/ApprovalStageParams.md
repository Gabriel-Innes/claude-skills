<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ApprovalStageParams (Object)

The ApprovalStageParams specifies the identification key combination (Code and Name) for which the ApprovalStagesService is related. Source table: OWST.

## Properties (2)
- `Public Property Code() As Long` [R/W] Sets or returns this approval stage Code. Field name: WstCode. This is a key to the ApprovalStage object.
- `Public Property Name() As String` [R] Returns the the stage approver's name. Field name: Name. Length: 20 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the an XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
