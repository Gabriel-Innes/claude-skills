<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# GLAccount (Object)

GLAccount is a data structure related to the AccountsService. The data is stored temporarily in a virtual table.

**Remarks:** To display the form related to the data structure: - Select Administration --> System Initialization --> Openning Balances --> G/L Accounts Openning Balance.

## Properties (9)
- `Public Property Code() As String` [R/W] Sets or returns the G/L account code for which to create an opening balance. Length: 15 characters.
- `Public Property Credit() As Double` [R/W] Sets or returns the amount to credit the G/L account.
- `Public Property Debit() As Double` [R/W] Sets or returns the amount to debit the G/L account.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date of the transaction.
- `Public Property ForeignCredit() As Double` [R/W] Sets or returns the amount, in foreign currency, to credit the G/L account.
- `Public Property ForeignCurrency() As String` [R/W] Sets or returns the foreign currency code used in the transaction. Length: 3 characters.
- `Public Property ForeignDebit() As Double` [R/W] Sets or returns the amount, in foreign currency, to debit the G/L account.
- `Public Property SystemCredit() As Double` [R/W] Sets or returns the amount, in system currency, to credit the G/L account.
- `Public Property SystemDebit() As Double` [R/W] Sets or returns the amount, in system currency, to debit the G/L account.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
