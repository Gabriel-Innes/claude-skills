<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MessageDataLine (Object)

The MessageDataLine is a child data structure related to the MessageDataColumn. It contains the value of a specified cell in the Data table, which is defined by its column number (vtIndex of Item of MessageDataColumns) and row number (vtIndex of Item of MessageDataLines. Source table: ALR3.

## Properties (3)
- `Public Property Object() As String` [R/W] Sets or returns the object type that is linked to the message. For example, 13 for A/R invoice. Mandatory in case Link (MessageDataColumn) is set to tYES. Field name: ObjType. Length: 20 characters.
- `Public Property ObjectKey() As String` [R/W] Sets or returns the object key that is linked to the message. For example, a document identification key. Mandatory in case Link (MessageDataColumn) is set to tYES. Field name: KeyStr. Length: 254 characters.
- `Public Property Value() As String` [R/W] Sets or returns the value of the cell in the Data table (represented by the column index and line index). Field name: Value. Length: 254 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
