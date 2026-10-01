<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# WithholdingTaxCodes (Object)

The WithholdingTaxCodes object enables to define the system withholding tax codes that can be applied to business partners, payments, and documents. Source table: OWHT.

**Remarks:** To display the form in the application: - Select Administration --> Setup --> Financials --> Tax --> Withholding Tax. Mandatory properties (for India): APCessAccount, APHSCAccount, APSurchargeAccount, APTDSAccount, ARCessAccount, ARHSCAccount, ARSurchargeAccount, ARTDSAccount, Assessee, Location, ReturnType, Section

## Properties (59)
- `Public Property Account() As String` [R/W] Sets or returns the G/L account for withholding tax postings. Field name: Account. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT).
- `Public Property APCessAccount() As String` [R/W] An A/P cess account associated with this withholding tax code. Field name: ApCessAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property APCessGSTAccount() As String` [R/W] property APCessGSTAccount
- `Public Property APCessInterimAccount() As String` [R/W] An A/P cess interim account associated with this withholding tax code. Field name: ApCesInAcc Length: 15 characters.
- `Public Property APCGSTAccount() As String` [R/W] property APCGSTAccount
- `Public Property APHSCAccount() As String` [R/W] An A/P HSC account associated with this withholding tax code. Field name: ApHscAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property APHSCInterimAccount() As String` [R/W] An A/P HSC interim account associated with this withholding tax code. Field name: ApHscInAcc Length: 15 characters.
- `Public Property APIGSTAccount() As String` [R/W] property APIGSTAccount
- `Public Property APSGSTAccount() As String` [R/W] property APSGSTAccount
- `Public Property APSurchargeAccount() As String` [R/W] An A/P surcharge account associated with this withholding tax code. Field name: ApSurAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property APSurchargeInterimAccount() As String` [R/W] An A/P surcharge interim account associated with this withholding tax code. Field name: ApSurInAcc Length: 15 characters.
- `Public Property APTCSInterimAccount() As String` [R/W] An A/P TCS interim account associated with this withholding tax code. Field name: ApTcsInAcc Length: 15 characters.
- `Public Property APTDSAccount() As String` [R/W] An A/P TDS account associated with this withholding tax code. Field name: ApTdsAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property APUTGSTAccount() As String` [R/W] property APUTGSTAccount
- `Public Property ARCessAccount() As String` [R/W] An A/R cess account associated with this withholding tax code. Field name: ArCessAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property ARCessGSTAccount() As String` [R/W] property ARCessGSTAccount
- `Public Property ARCessInterimAccount() As String` [R/W] An A/R cess interim account associated with this withholding tax code. Field name: ArCesInAcc Length: 15 characters.
- `Public Property ARCGSTAccount() As String` [R/W] property ARCGSTAccount
- `Public Property ARHSCAccount() As String` [R/W] An A/R HSC account associated with this withholding tax code. Field name: ArHscAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property ARHSCInterimAccount() As String` [R/W] An A/R HSC interim account associated with this withholding tax code. Field name: ArHscInAcc Length: 15 characters.
- `Public Property ARIGSTAccount() As String` [R/W] property ARIGSTAccount
- `Public Property ARSGSTAccount() As String` [R/W] property ARSGSTAccount
- `Public Property ARSurchargeAccount() As String` [R/W] An A/R surcharge account associated with this withholding tax code. Field name: ArSurAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property ARSurchargeInterimAccount() As String` [R/W] An A/R surcharge interim account associated with this withholding tax code. Field name: ArSurInAcc Length: 15 characters.
- `Public Property ARTCSInterimAccount() As String` [R/W] An A/R TCS interim account associated with this withholding tax code. Field name: ArTcsInAcc Length: 15 characters.
- `Public Property ARTDSAccount() As String` [R/W] An A/R TDS account associated with this withholding tax code. Field name: ArTdsAcc This is a foreign key to the ChartOfAccounts object.
  - remarks: For India only.
- `Public Property ARUTGSTAccount() As String` [R/W] property ARUTGSTAccount
- `Public Property Assessee() As Long` [R/W] An assessee associated with this withholding tax code. Field name: Assessee This is a foreign key to the ONOA (Nature of Assessee) table.
  - remarks: For India only.
- `Public Property BaseAmount() As Double` [R/W] Specifies the percentage of the base amount that is subject to withholding. Default value is 100%. Field name: PrctBsAmnt.
- `Public Property BaseType() As WithholdingTaxCodeBaseTypeEnum` [R/W] Sets or returns the base amount type on which to calculate withholding tax (Gross, Net, or VAT). Field name: BaseType.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property Category() As WithholdingTaxCodeCategoryEnum` [R/W] Determines when the withholding tax code is posted: upon payment or upon invoice. Field name: Category.
- `Public Property Concessional() As BoYesNoEnum` [R/W] Indicates whether concession rates are applied. Field name: Concess.
  - remarks: For India only.
- `Public Property CSTCodeIncomingID() As Long` [R/W] property CSTCodeIncomingID
- `Public Property CSTCodeOutgoingID() As Long` [R/W] property CSTCodeOutgoingID
- `Public Property Currency() As String` [R/W] property Currency
- `Public Property EBooksWTaxCategory() As Long` [R/W] property EBooksWTaxCategory
- `Public Property Effectivefrom() As Date` [R] property EffectiveFrom
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property IsProgressiveTax() As BoYesNoEnum` [R/W] property IsProgressiveTax
- `Public Property Lines() As WithholdingTaxCodes_Lines` [R] Returns the WithholdingTaxCodes_Lines child object.
- `Public Property Location() As Long` [R/W] The location associated with this withholding tax code. Field name: Location This is a foreign key to the WarehouseLocations object.
  - remarks: For India only.
- `Public Property MinimumTaxableAmount() As Double` [R/W] property MinimumTaxableAmount
- `Public Property NatureOfCalculationBaseCode() As String` [R/W] property NatureOfCalculationBaseCode
- `Public Property NonDeductThreshold() As BoYesNoEnum` [R/W] Apply tax exemption after threshold. Field name: NoDedThrsh.
- `Public Property OfficialCode() As String` [R/W] Sets or returns the code for the withholding tax declaration report. Field name: OffclCode. Length: 4 characters.
- `Public Property Rate() As Double` [R] property Rate
- `Public Property ReturnType() As ReturnTypeEnum` [R/W] The return type associated with this witholding tax code. Field name: ReturnType
  - remarks: For India only.
- `Public Property RoundingType() As RoundingTypeEnum` [R/W] Determines the rounding type - Truncated AU or Commercial Values - for the withholding tax calculation. Field name: RoundType.
  - remarks: Country-specific for Australia and New Zealand.
- `Public Property Section() As Long` [R/W] A section associated with this witholding tax code. Field name: Section. This is a foreign key to the Section object.
  - remarks: For India only.
- `Public Property Surcharge() As Double` [R/W] A threshold limit for surcharges for this witholding tax code. Field name: Surcharge.
  - remarks: For India only.
- `Public Property TdsType() As TdsTypeEnum` [R/W] property TdsType
- `Public Property Threshold() As Double` [R/W] A threshold limit for this witholding tax code. Field name: Threshold.
  - remarks: For India only.
- `Public Property TransactonThreshold() As Double` [R/W] property TransactonThreshold
- `Public Property TypeID() As Long` [R/W] property TypeID
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property WithholdingType() As WithholdingTypeEnum` [R/W] Determines whether the withholding tax code relates to VAT Withholding or Income Tax Withholding. Field name: Type.
  - remarks: Country-specific for Mexico and Chile.
- `Public Property WTCode() As String` [R/W] Sets or returns the withholding tax code (primary key). Field name: WTCode. Length: 4 characters.
- `Public Property WTName() As String` [R/W] Sets or returns the withholding tax name. Field name: WTName. Length: 50 characters.

## Methods (7)
- `Public Function Add() As Long` Adds a withholding tax code definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal bstrWtCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrWtCode`: WTCode.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You cannot delete a withholding tax code that is in use. You must use the GetByKey method to retrieve a valid object.
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
  - remarks: If the withholding tax code is in use, than only the eight A/R and A/P account fields can be updated. Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
