<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CountryParams (Object)

This object holds identification properties for the CountriesService object. Source table: OCRY.

## Properties (2)
- `Public Property Code() As String` [R/W] Sets or returns the country code. Field name: code. Character length: 3.
- `Public Property Name() As String` [R] Returns the name of the country. Field name: Name. Character length: 100.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data. Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path. Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
