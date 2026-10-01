<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Project (Object)

A data structure object holding properties for the ProjectsService (Code and Name). Source table: OPRJ.

## Properties (6)
- `Public Property Active() As BoYesNoEnum` [R/W] Specify whether the project status is active. Field: Active.
- `Public Property Code() As String` [R/W] Sets or returns a string specifying the project unique ID. Length: 20 characters.
- `Public Property Name() As String` [R/W] Sets or returns a string specifying the project name.
- `Public Property UserFields() As Fields` [R] Returns the UserFields object.
- `Public Property ValidFrom() As Date` [R/W] The valid period of the project. Field: ValidFrom.
- `Public Property ValidTo() As Date` [R/W] The valid period of the project. Field: ValidTo.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
