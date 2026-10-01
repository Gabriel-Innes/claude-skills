<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# MultiplePayment (Object)

A data structure related to BankStatementService holding properties for a multiple payment on a bank statement line. Source table: BNK1.

## Properties (6)
- `Public Property AmountFC() As Double` [R/W] Sets or returns the payment amount in foriegn currency. Field name: AmntFC.
- `Public Property AmountLC() As Double` [R/W] Sets or returns the payment amount in local currency. Field name: AmntLC.
- `Public Property BankStatmentLineID() As Long` [R] Returns the ID number of the bank statement line connected with the payment. Field name: BSLine.
- `Public Property DocumentIdentifier() As String` [R/W] Sets or returns the ID number of the bank statement document. Field name: DocID.
- `Public Property IsDebit() As BoYesNoEnum` [R/W] Sets or returns a boolean value specifying whether the payment is credit amount or debit amount. Field name: IsDebit.
- `Public Property ListLineID() As Long` [R] Returns the ID number of the payment line. Field name: ListLineID.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
