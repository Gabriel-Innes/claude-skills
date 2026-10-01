<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# PaymentTermsTypes (Object)

PaymentTermsTypes is a business object that represents the types of payment terms in the Banking module. The payment terms define typical agreements that apply to transactions with customers and vendors. This object enables you to: - Add a payment term type. - Retrieve a payment term type by its key. - Update a payment term type. - Remove a payment term type. - Save the object in XML format. Source table: OCTG.

**Remarks:** Mandatory field in SAP Business One: PaymentTermsGroupName. To display the form in the application: - Select Business Partners --> Business Partner Master Data. - Select Payment Terms tab. - Click the arrow to open the Define Payment Terms window.

## Properties (18)
- `Public Property BaselineDate() As BoBaselineDate` [R/W] Sets or returns a valid value of BoBaselineDate type that specifies the reference date for executing a payment transaction. Field name: BslineDate.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CreditLimit() As Double` [R/W] Sets or returns the maximum credit allowed. Field name: CredLimit.
  - remarks: SAP Business One validates the maximum credit value only if Credit Limit is selected in the Customer Activity Restrictions definitions (in Administrations -> System Initialization -> General Settings -> Sales). The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property DiscountCode() As String` [R/W] Sets or returns the discount code (type) as defined in Cash Discount (based on the payment due date). Field name: DiscCode. Length: 20 characters. This is a foreign key to the Cash Discount table (OCDC), not exposed through the DI API.
- `Public Property DunningCode() As String` [R/W] Sets or returns the dunning code as defined in the Dunning System. The dunning code sets the type of interest calculation for late payments. Field name: DunningCod. Length: 20 characters. This is a foreign key to the Dunning Interest Rate table (ORIT), not exposed through the DI API.
- `Public Property GeneralDiscount() As Double` [R/W] Sets or returns the general discount percentage for the total amount in a document. Field name: VolumDscnt.
  - remarks: The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property GroupNumber() As Long` [R] Returns the internal number, as assigned by the system, for the payment terms type. Field name: GroupNum.
- `Public Property InterestOnArrears() As Double` [R/W] Sets or returns the interest for late payments. The value of this property is for information only. Field name: LatePyChrg.
  - remarks: The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property LoadLimit() As Double` [R/W] Sets or returns the maximum allowed debt (CreditLimit + Postdated Checks). Field name: ObligLimit.
  - remarks: The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property NumberOfAdditionalDays() As Long` [R/W] Sets or returns the number of additional days for calculating the document due date. Field name: ExtraDays.
  - remarks: SAP Business One calculates the payment due date as follows: Payment due date = StartFrom + NumberOfAdditionalMonths + NumberOfAdditionalDays.
- `Public Property NumberOfAdditionalMonths() As Long` [R/W] Sets or returns the number of additional months for calculating the document due date. Field name: ExtraMonth.
  - remarks: SAP Business One calculates the payment due date as follows: Payment due date = StartFrom + NumberOfAdditionalMonths + NumberOfAdditionalDays.
- `Public Property NumberOfInstallments() As Long` [R] Returns the number of installments for the payment terms as defined in Installments in SAP Business One. Field name: InstNum.
  - remarks: Each installment creates as an exclusive record in payments, journal entries, reconciliations, and reports.
- `Public Property NumberOfToleranceDays() As Long` [R/W] Sets or returns the number of days earlier than the calculated due date to start expecting the payment. Field name: TolDays.
  - remarks: For example: If the payment due date is October 1, and the value of the Tolerance Days is 5, the payment is expected to be received starting from September 26.
- `Public Property OpenReceipt() As BoOpenIncPayment` [R/W] Sets or returns a valid value of BoOpenIncPayment type that specifies default means of payment from customers. OpenRcpt Field name: OpenRcpt.
- `Public Property PaymentTermsGroupName() As String` [R/W] Sets or returns the name of the payment terms type. Field name: PymntGroup. Length: 100 characters. Mandatory field in SAP Business One.
- `Public Property PriceListNo() As Long` [R/W] Sets or returns the Price List index to link to the business partner. Field name: ListNum. This is a foreign key to the PriceLists object.
  - remarks: The value of this property is used as a default in the Business Partner master card and its related documents.
- `Public Property StartFrom() As BoPayTermDueTypes` [R/W] Sets or returns a valid value of BoPayTermDueTypes type that specifies start time for calculating the payment due date. Field name: PayDuMonth.
  - remarks: SAP Business One calculates the payment due date as follows: Payment due date = StartFrom + NumberOfAdditionalMonths + NumberOfAdditionalDays.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (9)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal GroupNum As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `GroupNum`: Specifies the group number (see GroupNumber property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
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
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
- `Public Function UpdateWithBPs() As Long` method UpdateWithBPs
