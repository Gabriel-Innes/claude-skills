<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MessageDataColumns (Collection)

MessageDataColumns is a collection of MessageDataColumn data stractures. This enables to attache data to a message, such as invoice or quatation, that exits in the company database. The MessageDataColumns collection represents the columns of the Data tab table of a message.

## Properties (1)
- `Public Property Count() As Long` [R] Specifies the number of columns in the data table.

## Methods (5)
- `Public Function Add() As MessageDataColumn` Adds a column to the data table.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As MessageDataColumn` Returns a reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the location of the column in the data table (starts from 0).
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
