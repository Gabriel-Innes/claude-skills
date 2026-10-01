<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BankStatementsImportFile (Object)

This object defines the properties of the external file you want to import in BankStatementFromFile.

## Properties (4)
- `Public Property Account() As String` [R/W] Sets or returns the account namde for the imported file.
- `Public Property Bank() As String` [R/W] Sets or returns the bank name for the imported file.
- `Public Property Country() As String` [R/W] Sets or returns the country for the imported file.
- `Public Property FileName() As String` [R/W] Sets or returns the imported file name.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
