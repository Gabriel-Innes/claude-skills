<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# UserDefaultGroups (Object)

The UserDefaultGroups object enables to define default values (such as, default documents, default address in printed documents, windows color, and so on). These default values can be applied to specific user or group of users by setting the Defaults property of the Users object. Source table: OUDG.

**Remarks:** Mandatory field in SAP Business One: Code. If you set this object, the system uses these defaults instead of the company defaults. For example: - The Address setting is used instead of the Address setting of the AdminInfo object. - The BPforInvoicePayment setting is used instead of the InvoicePaymentBP setting of the PeriodCategory object. To display the form in the application: - Select Administration -->Setup -->General -->Users. - From the Defaults field, click the Choose From List button. - In the List of User Defaults, click the New button.

## Properties (36)
- `Public Property AdditionalIdNumber() As String` [R/W] Sets or returns the default additional ID number of the company. Field name: FreeZoneNo. Length: 32 characters.
  - remarks: If you set this property, the system uses its setting as default instead of the AdditionalIdNumber of the AdminInfo object.
- `Public Property Address() As String` [R/W] Sets or returns the default company address. Field name: Address. Length: 254 characters.
  - remarks: If you set this property, the system uses its setting as default instead of Address of the AdminInfo object.
- `Public Property AddressinForeignLanguage() As String` [R/W] Sets or returns the default company address in foreign language. Field name: FrgnAddr. Length: 254 characters.
  - remarks: If you set this property, the system uses its setting as default instead of the AddressinForeignLanguage of the AdminInfo object.
- `Public Property AssetInDoc() As BoYesNoEnum` [R/W] property AssetInDoc
- `Public Property BPforInvoicePayment() As String` [R/W] Sets or returns the default customer for A/R invoices and payments. This is a foreign key to CardCode (BusinessPartners. Field name: ICTCard. Length: 15 characters. This is a foreign key to the BusinessPartners object.
  - remarks: If you set this property, the system uses its setting as default instead of InvoicePaymentBP (PeriodCategory object).
- `Public Property BPLID() As Long` [R/W] property BPLID
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CashAccount() As String` [R/W] Sets or returns the default G/L account for cash receipt. Field name: CashAcct. Length: 15 characters.
  - remarks: If you set this property, the system uses its setting as default instead of AccountforCashReceipt (PeriodCategory object).
- `Public Property CheckingAcct() As String` [R/W] Sets or returns the default G/L account for incoming checks. Field name: CheckAcct. Length: 15 characters.
  - remarks: If you set this property, the system uses its setting as default instead of AccountforOutgoingchecks (PeriodCategory object).
- `Public Property Code() As String` [R/W] Sets or returns the code (primary key) of the user defaults group. Mandatory property. Field name: Code. Length: 8 characters.
- `Public Property Country() As String` [R/W] Sets or returns the default country code. Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
  - remarks: This a foreign key to the Countries table (OCRY - not exposed through the DI API). If you set this property, the system uses its setting as default instead of Country of the AdminInfo object.
- `Public Property DefaultCreditCards() As DefaultCreditCards` [R] Returns the DefaultCreditCards child object.
- `Public Property DefaultDocuments() As DefaultDocuments` [R] Returns the DefaultDocuments child object.
- `Public Property DefaultPTICode() As String` [R/W] property DefaultPTICode
- `Public Property DefaultPTICodes() As DefaultPTICodes` [R] property DefaultPTICodes
- `Public Property DefaultTaxCode() As String` [R/W] Sets or returns the default sales tax code. This is a foreign key to Code of the SalesTaxCodes object. Field name: DflTaxCode. Length: 8 charcters. This is a foreign key to the SalesTaxCodes object.
  - remarks: If you set this property, the system uses its setting as default instead of DefaultTaxCode of the AdminInfo object. Applicable for US and Canada only where the tax is calculated per card. The system displays this tax group code by default in a document row in case the following conditions are met: - The item is not an inventory one. - The item is a purchase item. - The item is taxable.
- `Public Property eMail() As String` [R/W] Sets or returns the default e-mail address. Field name: E_Mail. Length: 100 characters.
  - remarks: If you set this property, the system uses its setting as default instead of eMail of the AdminInfo object.
- `Public Property FaxNumber() As String` [R/W] Sets or returns the default fax number. Field name: Fax. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of FaxNumber of the AdminInfo object.
- `Public Property FaxNumberForeignLang() As String` [R/W] Sets or returns the default fax number in foreign language. Field name: FrgnFax. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of FaxNumberForeignLang of the AdminInfo object.
- `Public Property LanguageCode() As BoSuppLangs` [R/W] property LanguageCode
- `Public Property Name() As String` [R/W] Sets or returns the name of the user defaults group. Field name: Name. Length: 20 characters.
- `Public Property PhoneNumber1() As String` [R/W] Sets or returns the first default phone number. Field name: Phone1. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PhoneNumber1 of the AdminInfo object.
- `Public Property PhoneNumber1ForeignLang() As String` [R/W] Sets or returns the first default phone number in foreign language. Field name: FrgnPhone1. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PhoneNumber1ForeignLang of the AdminInfo object.
- `Public Property PhoneNumber2() As String` [R/W] Sets or returns the second default phone number. Field name: Phone2. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PhoneNumber2 of the AdminInfo object.
- `Public Property PhoneNumber2ForeignLang() As String` [R/W] Sets or returns the second default phone number in foreign language. Field name: FrgnPhone2. Length: 50 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PhoneNumber2ForeignLang of the AdminInfo object.
- `Public Property PrintingHeader() As String` [R/W] Sets or returns the default header to print in all documents (for example, the company name). Field name: PrintHeadr. Length: 100 characters.
  - remarks: If you set this property, the system uses its setting as default instead of PrintingHeader of the AdminInfo object.
- `Public Property PrintingHeaderInForeignLangu() As String` [R/W] Sets or returns the default header in foreign language to print in all documents. Field name: FrnPrntHdr. Length: 100 characters.
  - remarks: If you set this property, the system uses its setting as default instead of LetterHeaderinForeignLangu of the AdminInfo object.
- `Public Property PrintInvoiceandPaymentinS() As BoYesNoEnum` [R/W] Determines the default for whether or not to print invoices and payments in succession. Field name: ShortRcpt.
  - remarks: If you set this property, the system uses its setting as default instead of the ShortRcpt field of the Print Preferences (OADP table, which is not exposed through the DI API).
- `Public Property PrintReceipt() As BoPrintReceiptEnum` [R/W] Sets or returns a valid value of BoPrintReceiptEnum that determines when to print payment with invoice. Field name: PrintRcpt.
  - remarks: If you set this property, the system uses its setting as default instead of the PrintRcpt field of the Print Preferences (OADP table, which is not exposed through the DI API).
- `Public Property SalesEmployee() As Long` [R/W] Sets or returns the default sales employee code that will be applied in documents, sales opportunities, and so on. Field name: SalePerson. This is a foreign key to SalesEmployeeCode.
  - remarks: If you set this property, the system uses its value as default instead of -1 (No sales employee).
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Sets or returns the key of the user who defines the UseDefaultGroups object. Field name: UserSign. This is a foreign key to Users object.
- `Public Property UseTax() As BoYesNoEnum` [R/W] Determines the default whether or not to enable Use Tax calculations. Country-specific for U.S. Field name: UseTax.
  - remarks: If you set this property, the system uses its setting as default instead of UseTax of the AdminInfo object.
- `Public Property UseWarehouseAddressinAPD() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to use the warehouse address in purchase documents. Field name: AdrsFromWh.
  - remarks: If you set this property, the system uses its setting as default instead of AdressFromWH of the AdminInfo object.
- `Public Property Warehouse() As String` [R/W] Sets or returns the default warehouse code that will be applied in documents. Length 8 characters. Field name: Warehouse. This is a foreign key to the Warehouses object.
  - remarks: If you set this property, the system uses its setting as default instead of DefaultWarehouse of the AdminInfo object.
- `Public Property WindowsColor() As Long` [R/W] Sets or returns the the default windows color. Field name: Color.
  - remarks: If you set this property, the system uses its setting as default instead of CompanyColor of the AdminInfo object. The valid values include: 0 - Combined 1 - Classic (default) 2 - Gray 3 - Violet 4 - Blue 5 - Green 6 - Yellow 7 - Orange 8 - Red 9 - Brown

## Methods (7)
- `Public Function Add() As Long` method Add
  - remarks: Adds a users group.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrCode`: Code.
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
