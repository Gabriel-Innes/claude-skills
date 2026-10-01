<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BankStatement (Object)

A data structure related with the BankStatementService holding the bank statement header properties. Source table: OBNH.

## Properties (14)
- `Public Property BankAccountKey() As Long` [R/W] Sets or returns the bank account code. Field name: ActKey.
- `Public Property BankStatementFileHash() As String` [R/W] Sets or returns the bank statement file hash. Field name: FileCRC.
- `Public Property BankStatementGUID() As String` [R/W] Sets or returns the bank statement GUID. Field name: StmtGuid.
- `Public Property BankStatementRows() As BankStatementRows` [R] Returns a reference to a data collection holding properties of bank statement lines.
- `Public Property Currency() As String` [R/W] Sets or returns the statement currency. Field name: Currency.
- `Public Property EndingBalanceF() As Double` [R/W] Sets or returns the statement end balance in foreign currency. Field name: EndBlncF.
- `Public Property EndingBalanceL() As Double` [R/W] Sets or returns the statement end balance in local currency. Field name: EndBlncL.
- `Public Property Imported() As BoYesNoEnum` [R] Returns a valid value specifying whether or not the statement created manually or imported from file.
- `Public Property InternalNumber() As Long` [R] Returns the unique ID of the statement in the system. Field name: IdNumber.
- `Public Property StartingBalanceF() As Double` [R/W] Sets or returns the statement start balance in foreign currency. Field name: StrtBlncF.
- `Public Property StartingBalanceL() As Double` [R/W] Sets or returns the statement start balance in local currency. Field name: StrtBlncL.
- `Public Property StatementDate() As Date` [R/W] Sets or returns the statement creation date. Field name: BSDate.
- `Public Property StatementNumber() As String` [R/W] Sets or returns the statement sequential number. Field name: BSFileNum.
- `Public Property Status() As BankStatementStatusEnum` [R] Returns a value specifying the statement status. Field name: Status.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
