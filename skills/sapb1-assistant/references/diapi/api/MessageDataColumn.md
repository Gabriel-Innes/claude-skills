<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MessageDataColumn (Object)

MessageDataColumn is a data structure related to the MessagesService. It enables to add one data column to the data columns collection. The MessageDataColumn object contains the title of the column and whether or not it includes a link to a document. Source table: ALR2.

**Remarks:** To display the form in the application: - From the main menu bar, click the Message/Alert Overview icon. - Select the Data tab.

## Properties (3)
- `Public Property ColumnName() As String` [R/W] Sets or returns the column name in the message. Field name: ColName. Length: 30 characters.
- `Public Property Link() As BoYesNoEnum` [R/W] Determines whether or not to display a Link button in the data column. For example, link to a specified invoice. If the Link property is set to tYES, the object type (Object) and document key (ObjectKey) must be specified in the MessageDataLine object. Field name: Link.
- `Public Property MessageDataLines() As MessageDataLines` [R/W] Sets or returns the MessageDataLines collection.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
