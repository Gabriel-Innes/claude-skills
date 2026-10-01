<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# BillOfExchangeTransaction (Object)

BillOfExchangeTransaction is a business object that represents the Bill Of Exchange Transaction table in the Banking module. Bill Of Exchange is a commercial document used as a payment method in Spain, Portugal, Italy, and France. Use this object for Bill Of Exchange documents that their status was changed to Generated. Each status change of a Bill-of-exchange creates a transaction. This object enables you to: - Add a Bill Of Exchange Transaction. - Retrieve a Bill Of Exchange Transaction. - Save the Bill Of Exchange Transaction in XML format. Source table: OBOT.

**Remarks:** Mandatory fields is SAP Business One: StatusFrom and StatusTo. To display the form in the application: - Select Banking --> Bill of Exchange --> Bill of Exchange Transactions.

## Properties (14)
- `Public Property BankPages() As BillOfExchangeTrans_BankPages` [R] Returns the BillOfExchangeTrans_BankPages object.
- `Public Property BOETransactionkey() As Long` [R] Returns the unique ID of the bill-of-exchange transaction (primary key). SAP Business One assigns a sequential number when adding a bill-of-exchange transaction. Field name: AbsEntry.
- `Public Property Browser() As DataBrowser` [R] returns the DataBrowser object.
- `Public Property Deposits() As BillOfExchangeTrans_Deposits` [R] Returns the BillOfExchangeTrans_Deposits object.
- `Public Property IsBoeReconciled() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the Bill Of Exchange is reconciled. Field name: Reconciled.
  - remarks: Applies to a Bill Of Exchange with a status Deposit or Paid only.
- `Public Property Lines() As BillOfExchangeTransaction_Lines` [R] Returns the BillOfExchangeTransaction_Lines object.
- `Public Property PostingDate() As Date` [R/W] Sets or returns the posting date of the Bill Of Exchange transaction. Field name: PostDate.
- `Public Property StatusFrom() As BoBOTFromStatus` [R/W] Sets or returns a valid value of BoBOTFromStatus type that specifies the current status of the Bill Of Exchange. Mandatory field is SAP Business One. Field name: StatusFrom.
  - remarks: For example, you can use this property to change the status of the Bill Of Exchange from (StatusFrom) Generated to (StatusTo) Deposit.
- `Public Property StatusTo() As BoBOTToStatus` [R/W] Sets or returns a valid value of BoBOTToStatus type that specifies the required status of the Bill Of Exchange. Mandatory field is SAP Business One. Field name: StatusTo.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the date for the tax calculation or payment. Field name: TaxDate.
  - remarks: Default: current date retrieved from the system server. This property is relevant also for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property TransactionDate() As Date` [R] Sets or returns the transaction date. Field name: TranDate.
- `Public Property TransactionNumber() As Long` [R] Returns the transaction code that SAP Business One creates for the Bill Of Exchange. Field name: TransId. This is a foreign key to the JournalEntries object.
- `Public Property TransactionTime() As Date` [R] Returns the transaction time. Field name: TranTime.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (5)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal InternalKey As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `InternalKey`: Specifies an internal key identifier (read only) of a bill of exchange transaction that is provided by the system and used as a reference for other documents in the system.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method to save a business object to an XML file. Then, call the GetBusinessObjectFromXML method to load this object into memory again, for example, to copy customers from one database to another. To enable this operation, set the XmlExportType property of the Company object to xet_ValidNodesOnly. To use ReadXML method, set the XmlExportType to xet_ExportImportMode (3). For more information, see Exchanging Data Using the DI API XML Capabilities.
  - example note: The following sample shows how to save data of an object to an XML file. Use this sample as a basis to all business objects (both document and master data types).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim vInvoice As SAPbobsCOM.Documents

    Set vInvoice = vCmp.GetBusinessObject(oInvoices)

    'Retrieve an invoice document from the database

    RetVal = vInvoice.GetByKey("1023")

    If RetVal <> 0 Then

         vCmp.GetLastError ErrCode, ErrMsg

         MsgBox "Failed to Retrieve the record " & ErrCode & " " & ErrMsg

         Exit Sub

    End If

    'Save the object as an xml file

    vInvoice.SaveXML ("C:\Program Files\SAP\XML\Invoice.xml")

    'Retrieve the object back from the XML file

    Set vInvoice = vCmp.GetBusinessObjectFromXML("C:\Program Files\SAP\XML\Invoice.xml", 0)
    ```
