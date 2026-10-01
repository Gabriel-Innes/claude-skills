<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# VatGroups (Object)

The VatGroups object enables to define tax groups that can be assigned to business partners and items in sales and purchase documents. Source table: OVTG.

**Remarks:** Country-specific for Europe. Mandatory properties: Code and Effectivefrom (VatGroups_Lines). To display the form in the application: - Select Administration --> Setup --> Financials --> Tax --> Tax Groups.

## Properties (31)
- `Public Property AcquisitionReverse() As BoYesNoEnum` [R/W] Determines whether or not the VAT group is related to Acquisition/Reverse. Field name: AcqstnRvrs.
  - remarks: Applicable for purchase documents (the value of Category is bovcInputTax)
- `Public Property AcquisitionReverseCorrespondingTaxCode() As String` [R/W] property AcquisitionReverseCorrespondingTaxCode
- `Public Property AcquisitionTax() As String` [R/W] Sets or returns the G/L account for acquisition tax posting. Field name: AcqsTax. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT). Applicable for purchase documents (the value of Category is bovcInputTax)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CashDiscountAccount() As String` [R/W] property CashDiscountAccount
- `Public Property Category() As BoVatCategoryEnum` [R/W] Determines whether the tax group applies to sales documents (output tax) or to purchase documents (input tax). Field name: Category.
- `Public Property Code() As String` [R/W] Sets or returns a tax group code (primary key). Field name: Code. Length: 8 characters.
- `Public Property Correction() As BoYesNoEnum` [R/W] Determines whether or not the tax group is a correction tax group. Field name: Correction.
  - remarks: Country-specific for Portugal.
- `Public Property DeferredTaxAcc() As String` [R/W] Sets or returns the G/L account for deferred tax postings. Field name: DeferrAcc. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT).
- `Public Property DownPaymentTaxOffsetAccount() As String` [R/W] property DownPaymentTaxOffsetAccount
- `Public Property EBooksVatCategory() As Long` [R/W] property EBooksVatCategory
- `Public Property EqualizationTaxAccount() As String` [R/W] The G/L account for equalization tax. Field name: EquAccount
  - remarks: For Spain only.
- `Public Property EU() As BoYesNoEnum` [R/W] Determines whether or not the tax group applies to European Union countries. Field name: IsEC.
  - remarks: Applicable for sales documents (the value of Category is bovcOutputTax).
- `Public Property ExcludedTaxSummary() As BoYesNoEnum` [R/W] property ExcludedTaxSummary
- `Public Property GoodsShipment() As String` [R/W] Sets or returns the goods shipment indicator, which appears in the EU Sales Report. This property is applicable when TriangularDeal is not set. Field name: GoddsShip. Length: 1 numeric character.
  - remarks: The value of this property is a foreign key to the OGSP table, which is not exposed through the DI API.
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property Name() As String` [R/W] Sets or returns a tax group name. Field name: Name. Length: 50 characters.
- `Public Property NonDeduct() As Double` [R/W] Sets or returns the non-deductable tax percentange. Field name: NonDedct.
  - remarks: Applicable for purchase documents (the value of Category is bovcInputTax) and when the value of AcquisitionReverse is tNO.
- `Public Property NonDeductAcc() As String` [R/W] Sets or returns the G/L account for non-deductable tax postings. Field name: NonDedAcc. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT). Applicable for purchase documents (the value of Category is bovcInputTax) and when the value of AcquisitionReverse is tNO.
- `Public Property Report349Code() As Report349CodeListEnum` [R/W] property Report349Code
- `Public Property ServiceSupply() As String` [R/W] Sets or returns the service supply indicator, which appears in the EU Sales Report. This property is applicable when TriangularDeal and GoodsShipment is not set. If you put a value in either TriangularDeal or GoodsShipment, it will cause the deletion of the value in ServiceSupply. Field name: ServSupply. Length: 1 numeric character.
- `Public Property StandardTaxCode() As String` [R/W] property StandardTaxCode
- `Public Property TaxAccount() As String` [R/W] Sets or returns the G/L account for the tax group. Field name: Account. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
  - remarks: This is a foreign key to ChartOfAccounts (OACT).
- `Public Property TaxRegion() As VatGroupsTaxRegionEnum` [R/W] property TaxRegion
- `Public Property TaxTypeBlackList() As TaxTypeBlackListEnum` [R/W] property TaxTypeBlackList
- `Public Property TriangularDeal() As String` [R/W] Sets or returns the triangular deal indicator, which enables to identify delivery of goods as part of triangular deals in the EU sales report. This property is applicable when GoodsShipment is not set. Field name: Indicator. Length: 1 numeric character.
  - remarks: Deliveries of goods as part of triangular deals must be listed separately in the EU sales report. The end-user must identify these deliveries as such when entering the line item. This indicator causes the transaction to be identified as a triangular deal in the EU sales report. The value of this property is a foreign key to the OIND table, which is not exposed through the DI API.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatCorrection() As String` [R/W] Sets or returns the tax group code (foreign key) that is used as a correction tax group. Field name: VatCrctn. Length: 8 characters. This is a foreign key to the VatGroups object.
  - remarks: Country-specific for Portugal.
- `Public Property VATDeductibleAccount() As String` [R/W] property VATDeductibleAccount
- `Public Property VatGroups_Lines() As VatGroups_Lines` [R] Returns the VatGroups_Lines child object.
- `Public Property VATInRevenueAccount() As String` [R/W] property VATInRevenueAccount

## Methods (7)
- `Public Function Add() As Long` Adds a tax group definition.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
- `Public Function GetByKey(ByVal bstrGroupCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `bstrGroupCode`: Code.
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Deletes the current record.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data.
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
