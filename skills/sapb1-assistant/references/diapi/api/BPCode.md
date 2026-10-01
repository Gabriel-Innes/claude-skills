<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BPCode (Object)

BPCode is a data structure related to the BusinessPartnersService. Source table: OPB1.

**Remarks:** To display the form related to the data structure: - Select Administration --> System Initialization --> Openning Balances --> Busines Partners Openning Balance.

## Properties (10)
- `Public Property BpCtrlAcct() As String` [R/W] property BpCtrlAcct
- `Public Property Code() As String` [R/W] Sets or returns the business partner code for which to create an opening balance. Field name: CardCode. Length: 15 characters.
- `Public Property Credit() As Double` [R/W] Sets or returns the amount to credit the business partner account.
- `Public Property Debit() As Double` [R/W] Sets or returns the amount to debit the business partner account.
- `Public Property DueDate() As Date` [R/W] Sets or returns the due date of the transaction.
- `Public Property ForeignCredit() As Double` [R/W] Sets or returns the amount, in foreign currency, to credit the business partner account.
- `Public Property ForeignCurrency() As String` [R/W] Sets or returns the foreign currency code used in the transaction. Length: 3 characters.
- `Public Property ForeignDebit() As Double` [R/W] Sets or returns the amount, in foreign currency, to debit the business partner account.
- `Public Property SystemCredit() As Double` [R/W] Sets or returns the amount, in system currency, to credit the business partner account.
- `Public Property SystemDebit() As Double` [R/W] Sets or returns the amount, in system currency, to debit the business partner account.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
