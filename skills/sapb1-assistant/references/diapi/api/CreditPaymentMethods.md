<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# CreditPaymentMethods (Object)

The CreditPaymentMethods object enables to define payment methods by credit cards. Source table: OCRP.

**Remarks:** The methods for credit card payments are used by the Payments_CreditCards object. Mandatory field in SAP Business One: Name. To display the form in the application: - Select Administration --> Setup --> Banking --> Credit Card Payment Methods.

## Properties (10)
- `Public Property AssignedtoCreditCard() As Long` [R/W] Sets or returns the foreign key of the credit card assigned to the payment method. Field name: CreditCard. This is a foreign key to the CreditCards object.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property InstallmentPaymentsPossible() As InstallmentPaymentsPossiblityEnum` [R/W] Sets or returns a valid value that defines the options for installments available for the payment method. Field name: InstalMent.
- `Public Property MaxQtyWithoutApproval() As Double` [R/W] Sets or returns the maximum amount of incoming and outgoing payments without the approval of the credit card company. Field name: MaxValid.
  - remarks: The system issues a warning if the value of credit card transactions does not match the maximum amount with approval.
- `Public Property MinimumCreditAmount() As Double` [R/W] Sets or returns the minimum amount for credit vouchers. Field name: MinCredit.
  - remarks: The system issues a warning if the value of credit card transactions does not match the minimum amount of credit vouchers.
- `Public Property MinimumPaymentAmount() As Double` [R/W] Sets or returns the minimum amount for incoming and outgoing payments. Field name: MinToPay.
  - remarks: The system issues a warning if the value of credit card transactions does not match the minimum amount of payment.
- `Public Property Name() As String` [R/W] Sets or returns the name of the credit payment method. Field name: CrTypeName. Mandatory property. Length: 30 characters.
  - remarks: The Name clearly identifies the payment method in documents (such as Visa Regular).
- `Public Property PaymentCode() As String` [R/W] Sets or returns the foreign key of the credit card payment due dates. Field name: DueTerms. This is a foreign key to the CreditCardPayments object.
- `Public Property PaymentMethodCode() As Long` [R] Returns the payment method code as assigned by the system when adding the payment method definition. Field name: CrTypeCode.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a credit card payment method.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal lCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `lCode`: PaymentMethodCode.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal bstrFileName As String)` Save the object to a file as XML data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef pbstrFileName As String)` Saves the object data to XML formatted data.
  - param `pbstrFileName`: Specifies the path and file name of the XML data.
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
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
