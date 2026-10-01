<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# TaxInvoices (Object)

TaxInvoices is a business object that represents the header data of a Tax Invoice document. Source table: OTSI for sales invoices, OTPI for purchase invoices, or OTXD for journal entry according to the DocType valid value.

**Remarks:** Country-specific for Russia.

## Properties (36)
- `Public Property Address() As String` [R/W] Sets or returns the Bill To address. Field name: Address. Length: 254 characters.
- `Public Property Address2() As String` [R/W] Sets or returns the alternative Ship To address. Field name: Address2. Length: 254 characters.
- `Public Property AlterationRevision() As Long` [R/W] property AlterationRevision
- `Public Property BPLID() As Long` [R] property BPLID
- `Public Property BPLName() As String` [R] property BPLName
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object. Returns the DataBrowser object.
- `Public Property CancelDate() As Date` [R] Returns the Cancel Date of the tax invoice . Field name: CancelDate. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner Customer Code. Field name: CardCode. This is a foreign key to the BusinessPartners object. Mandatory field in SAP Business One. Length: 15 characters.
- `Public Property Comments() As String` [R/W] Sets or returns the Remarks regarding the tax invoice document. Field name: Comments. Length: 254 characters.
- `Public Property ContactPersonCode() As Long` [R/W] Sets or returns the contact person code. Field name: CntctCode. This is a foreign key to the ContactEmployees object.
  - remarks: The contact employee codes are defined through the ContactEmployees object (foreign key linked to OCPR table).
- `Public Property CreationDate() As Date` [R] Returns the creation date of the tax invoice document. Field name: CreateDate.
- `Public Property CurrencySource() As BoCurrencySources` [R/W] Sets or returns a valid value of BoCurrencySources type that specifies the currency source: - L - local - S - system - C - customer (business partner, default) Field name: CurSource.
- `Public Property CustomerOrVendorName() As String` [R/W] Sets or returns a string that specifies the business partner's full name. Field name: CardName. Length: 100 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
  - remarks: The default value is retrieved from CardName property of the BusinessPartners object.
- `Public Property CustomerOrVendorRefNo() As String` [R/W] Sets or returns a string that specifies the business partner's Reference number. Field name: NumAtCard. Length: 16 characters. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property DocCurrency() As String` [R/W] Sets or returns the currency used in this document. Field name: DocCur. Length: 3 characters.
- `Public Property DocDate() As Date` [R/W] Sets or returns the document posting date. Field name: DocDate.
- `Public Property DocDueDate() As Date` [R/W] Sets or returns the document value date. Field name: DocDueDate.
- `Public Property DocEntry() As Long` [R] Returns the document key. Field name: DocEntry.
- `Public Property DocNum() As Long` [R] Returns the document number. Field name: DocNum.
- `Public Property DocType() As BoTaxInvoiceTypes` [R/W] Sets or returns a valid value of BoTaxInvoiceTypes that specifies the document type of the tax invoice. Field name: DocType.
- `Public Property DocumentReferences() As TaxInvoice_DocumentReferences` [R] Returns TaxInvoice_DocumentReferences child object.
- `Public Property DocumentTotal() As Double` [R] Sets or returns the Document Total value in document currency. Field name: DocTotal.
  - remarks: The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property Lines() As TaxInvoice_Lines` [R] Returns TaxInvoice_Lines child object.
- `Public Property LinkedDownPayments() As TaxInvoice_LinkedDownPayments` [R] Returns TaxInvoice_LinkedDownPayments child object.
- `Public Property OperationCodes() As TaxInvoice_OperationCodes` [R] Returns TaxInvoice_OperationCodes child object.
- `Public Property PaymentRefDate() As Date` [R/W] Sets or returns the Payment Ref. Date. Field name: PayRefDate. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property PaymentRefNo() As String` [R/W] Sets or returns a string that specifies the the payment document number. Field name: PayRefNo. The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property Printed() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not this tax invoice document was printed. Field name: Printed.
- `Public Property Segment() As Long` [R] Returns the segment number of the tax invoice document. Field name: Segment.
  - remarks: Default: 0.
- `Public Property Series() As Long` [R/W] Returns the auto-numbering series that generated the document number. Field name: Series.
  - remarks: Default: 0.
- `Public Property ShipToCode() As String` [R/W] Sets or returns the Ship To address name. Field name: ShipToCode. Length: 50 characters.
  - remarks: For sales documents, the value is retrieved from the business partner record. This address name can be updated only for open sales documents. For purchase documents, the value is retrieved from the company record.
- `Public Property TaxDate() As Date` [R/W] Sets or returns the document VAT date. Field name: VatDate.
- `Public Property TaxTotal() As Double` [R] Returns a double integer that specifies the Tax Total amount in document currency. Field name: VatSum.
  - remarks: The object is applicable for SAP Business One 2004C CEE (country-specific for Russia).
- `Public Property UpdateDate() As Date` [R] Returns the document last update date. Field name: UpdateDate.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VATRegNum() As String` [R] property VATRegNum

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database. Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
  - example note: The following sample shows how to add an invoice (with lines) document to the database. Use this sample as a basis for all business objects of document type (not master data type).
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
     Sub AddInvoice_Click()

        Dim RetVal As Long

        Dim ErrCode As Long

        Dim ErrMsg As String

        'Create the Documents object

        Dim vInvoice    As SAPbobsCOM.Documents

        Set vInvoice = vCmp.GetBusinessObject(oInvoices)

        'Set values to the fields

        vInvoice.Series = 0

        vInvoice.CardCode = "BP234"

        vInvoice.HandWritten = tNO

        vInvoice.PaymentGroupCode = "-1"

        vInvoice.DocDate = "21/8/2003"

        vInvoice.DocTotal = 264.6

        'Invoice Lines - Set values to the first line

        vInvoice.Lines.ItemCode = "A00023"

        vInvoice.Lines.ItemDescription = "Banana"

        vInvoice.Lines.PriceAfterVAT = 2.36

        vInvoice.Lines.Quantity = 50

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Invoice Lines - Set values to the second line

        vInvoice.Lines.Add

        vInvoice.Lines.ItemCode = " A00033"

        vInvoice.Lines.ItemDescription = "Orange"

        vInvoice.Lines.PriceAfterVAT = 118

        vInvoice.Lines.Quantity = 1

        vInvoice.Lines.Currency = "Eur"

        vInvoice.Lines.DiscountPercent = 10

        'Add the Invoice

        RetVal = vInvoice.Add

       'Check the result

        If RetVal <> 0 Then

            vCmp.GetLastError ErrCode, ErrMsg

            MsgBox ErrCode & " " & ErrMsg

        End If

     End Sub
    ```
- `Public Function Cancel() As Long` Cancels a record from the object table. Cancels a record from the object table.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal DocEntry As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from SAP Business One database. Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `DocEntry`: Document key (DocEntry).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data. Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
- `Public Sub SaveXML(ByRef FileName As String)` Saves the object data to XML formatted data. Saves the object data to XML formatted data.
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
- `Public Function Update() As Long` Updates the object data in the SAP Business One company database. Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
