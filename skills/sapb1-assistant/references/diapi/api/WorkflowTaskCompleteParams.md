<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WorkflowTaskCompleteParams (Object)

This object specifies the identification key of the Complete method.

## Properties (3)
- `Public Property Note() As String` [R/W] The note that needs to be added to the task for processing.
- `Public Property TaskID() As Long` [R/W] The ID of the related workflow task.
- `Public Property TriggerParams() As String` [R/W] The trigger parameter that needs to be added to the task. The TriggerParams is a string in xml format.
  - remarks: The TriggerParams format is as follows: "<Params> <Param> <Key>%key1%</Key> <Value Type=\"type1\">%value1%</Value> </Param> <Param> <Key>%key2%</Key> <Value Type=\"type2\">%value2%</Value> </Param> … </Params>" The supported value types are: “integer”, “double”, “string”, “date” and “time”.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
