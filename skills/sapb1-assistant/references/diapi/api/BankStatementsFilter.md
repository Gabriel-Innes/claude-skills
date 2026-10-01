<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BankStatementsFilter (Object)

This object fefines filtering properties for GetBankStatementList

## Properties (3)
- `Public Property Account() As String` [R/W] Sets or returns the account name for which you want to get bank statements.
- `Public Property Bank() As String` [R/W] Sets or returns the bank from which you want to get bank statements.
- `Public Property Country() As String` [R/W] Sets or returns the country for which you want to get bank statements.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
