<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# SalesTaxAuthorities (Object)

SalesTaxAuthorities is a business object that represents the sales tax jurisdictions data for US and Canada localizations, or sales tax types for Latin America localization. In US and Canada localizations, the sales tax jurisdictions can be defined, for example, for each state, country, and city. In Latin America localization, the sales tax types are related to specific items, such as fuel and cigarettes, that are liable to tax (Rate) in addition to VAT. This object enables you to: - Add a sales tax authority. - Retrieve a sales tax authority by its key. - Update a sales tax authority data. - Save the object in XML format. Source table: OSTA.

**Remarks:** Mandatory field in SAP Business One: Code. To display the form in the application (US and Canada localizations): - Select Administration --> Setup --> Financials --> Tax --> Sales Tax Jurisdiction. A Selection Criteria dialog box opens. - From the Define Sales Tax Jurisdiction Types - Selection Criteria select a tax jurisdiction type and click OK. To display the form in the application (Latin America localization): - Select Administration --> Setup --> Financials --> Tax --> Tax Types. - From the Define Tax Types - Selection Criteria select a tax category and click OK.

## Properties (30)
- `Public Property AOrPTaxAccount() As String` [R/W] Sets or returns the G/L account for purchase (A/P) tax. Field name: PurchTax. Length: 15 characters.
- `Public Property AOrRTaxAccount() As String` [R/W] Sets or returns the G/L account for sales (A/R) tax. Field name: SalesTax. Length: 15 characters. This is a foreign key to the ChartOfAccounts object, not exposed through the DI API).
- `Public Property APExpAccount() As String` [R/W] property APExpAccount
- `Public Property ARExpAccount() As String` [R/W] property ARExpAccount
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Code() As String` [R/W] Sets or returns the code of the tax authority. Mandatory in SAP Business One. Field name: Code. Length: 8 characters.
- `Public Property DeferredTaxAccount() As String` [R/W] Sets or returns the G/L account for deferred tax. Field name: deferrAcct. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property Exempt() As BoYesNoEnum` [R/W] property Exempt
- `Public Property FlatTaxAmount() As Double` [R/W] The maximum tax to be applied to a document for this jurisdiction, or the maximum tax to be applied for each item in a document for a jurisdiction if Single Item Tax (IsItemLevel property of the SalesTaxCodes object) is selected for the tax code. Field name: FlatAmount
  - remarks: For the United States only.
- `Public Property InclInFirstInstallment() As BoYesNoEnum` [R/W] property InclInFirstInstallment
- `Public Property InclInGrossRevenue() As BoYesNoEnum` [R/W] property InclInGrossRevenue
- `Public Property InclInPrice() As BoYesNoEnum` [R/W] property InclInPrice
- `Public Property MaxTaxableAmount() As Double` [R/W] Maximum amount for which to apply this tax. If the amount is above the value in this field, the tax is applied only to the value in this field. The maximum amount is by default compared to the document amount; if Single Item Tax is selected for the tax code (IsItemLevel property of the SalesTaxCodes object), the maximum amount is compared to each item's amount. Field name: MaxAmount
  - remarks: For the United States only.
- `Public Property MinTaxableAmount() As Double` [R/W] Minimum amount for which to apply this tax. If the amount is below the value in this field, the tax for this jurisdiction is 0. The minimum amount is by default compared to the document amount; if Single Item Tax is selected for the tax code (IsItemLevel property of the SalesTaxCodes object), the minimum amount is compared to each item's amount. Field name: MinAmount
  - remarks: For the United States only.
- `Public Property Name() As String` [R/W] Sets or returns the name of the sales tax authority. Field name: Name. Length: 100 characters.
- `Public Property NonDeductibleAccount() As String` [R/W] Sets or returns the G/L account for non deductible tax amounts. Field name: NonDdctAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property NonDeductiblePrecent() As Double` [R/W] Sets or returns the percentage of non deductible tax. Field name: NonDdctPrc.
- `Public Property Rate() As Double` [R/W] Sets or returns the tax percentage of the tax authority. Mandatory in SAP Business One. Field name: Rate.
  - remarks: In the United States and canada localizations, if you set a rate, the system creates a Tax Definition row with the rate and the current system date.
- `Public Property ReverseChargePercent() As Double` [R/W] property ReverseChargePercent
- `Public Property SalesTaxRCMAccount() As String` [R/W] property SalesTaxRCMAccount
- `Public Property SalesTaxRCMClrAccount() As String` [R/W] property SalesTaxRCMClrAccount
- `Public Property TaxDefinitions() As TaxDefinitions` [R] The tax definitions for this jurisdiction. A tax definition specifies a rate and the date from which it is in effect.
  - remarks: For the United States and Canada only.
- `Public Property TextCode() As Long` [R/W] property TextCode
- `Public Property Type() As Long` [R/W] Sets or returns the type of the sales tax authority as defined in SalesTaxAuthoritiesTypes object. Field name: Type. This is a foreign key to the SalesTaxAuthoritiesTypes object.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property UserSignature() As Long` [R] Returns the ID of the user who enters the object's details. Field name: UserSign. This is a foreign key to the Users object.
- `Public Property UseTaxAccount() As String` [R/W] Sets or returns the G/L account for Use Tax. Field name: UseTax. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property VATExemption() As BoYesNoEnum` [R/W] property VATExemption
- `Public Property VATExemptionBasePercent() As Double` [R/W] property VATExemptionBasePercent
- `Public Property VATExemptionPercent() As Double` [R/W] property VATExemptionPercent

## Methods (6)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal Code As String, ByVal Type As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `Code`: Sales tax authority code (Code).
  - param `Type`: Sales tax authority type (Type).
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
- `Public Function Update() As Long` Field name: . Updates the object data in the company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
