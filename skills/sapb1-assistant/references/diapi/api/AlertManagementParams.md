<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# AlertManagementParams (Object)

This object specifies the identification key combination (Code, Name and Type) for which the AlertManagementService is related. Source table: OALT.

## Properties (3)
- `Public Property Code() As Long` [R/W] Sets or returns the Internal Number of this alert. Field name: Code.
- `Public Property Name() As String` [R] Sets or returns the Name of this Alert. Field name: Name. Length: 50 characters.
- `Public Property Type() As AlertManagementTypeEnum` [R/W] Sets or returns valid value that determines whether this alert is System Alert or a User Alert. Field name: Type.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
