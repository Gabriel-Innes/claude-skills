<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Warehouses (Object)

Warehouses is a business object that represents the warehouses information in the Inventory module. This object enables you to: - Add a warehouse. - Retrieve a warehouse by its key. - Update a warehouse details. - Remove a warehouse. - Save the object in XML format. Source table: OWHS.

**Remarks:** Mandatory field in SAP Business One: WarehouseCode. To display the form in the application: - Select Administration --> Setup --> Inventory --> Warehouses. The warehouse definition includes: - Warehouse type - Warehouse address - G/L accounts, which are defined in ChartOfAccounts, used in Item Master Data - Inventory Data in case GLMethod property is set to WH.

## Properties (92)
- `Public Property AddressName2() As String` [R/W] property AddressName2
- `Public Property AddressName3() As String` [R/W] property AddressName3
- `Public Property AddressType() As String` [R/W] property AddressType
- `Public Property AllowUseTax() As BoYesNoEnum` [R/W] Determines whether or not to Allow Use Tax for items in marketing documents. Field name: UseTax.
  - remarks: Country-specific for US and Canada.
- `Public Property AutoAllocOnIssue() As BoDocWhsAutoIssueMethod` [R/W] The method by which items in bin locations are issued. Field name: AutoIssMtd.
- `Public Property AutoAllocOnReceipt() As AutoAllocOnReceiptMethodEnum` [R/W] property AutoAllocOnReceipt
- `Public Property BinLocCodeSeparator() As String` [R/W] The separator of bin location codes. Field name: BinSeptor. Length: 5 characters.
- `Public Property Block() As String` [R/W] Sets or returns the block subcomponent of the warehouse address. Field name: Block. Length: 100 characters.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property BuildingFloorRoom() As String` [R/W] Sets or returns the additional address details of the warehouse, such as building number, floor number, and room number. Field name: Building. Length: 64,000 characters. Building
- `Public Property BusinessPlaceID() As Long` [R/W] Returns the business place ID related to the warehouse. Field name: BPLid.
- `Public Property City() As String` [R/W] Sets or returns the city subcomponent of the warehouse address. Field name: City. Length: 100 characters.
- `Public Property CostInflationAccount() As String` [R/W] Sets or returns the G/L account associated with Cost Inflation. Field name: CostRvlAct. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property CostInflationOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Cost Inflation Offset. Field name: CstOffsAct. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property CostOfGoodsSold() As String` [R/W] Sets or returns the G/L account associated with Cost of Good Sold in continues stock system. Field name: SaleCostAc. Length: 15 characters.
- `Public Property Country() As String` [R/W] Sets or returns the country code subcomponent of the warehouse address. Field name: Country. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property County() As String` [R/W] Sets or returns the county subcomponent of the warehouse address. Field name: County. Length: 100 characters.
- `Public Property DecreaseGLAccount() As String` [R/W] Sets or returns the G/L account associated with Decrease G/L Account. Field name: DecresGlAc. Length: 15 characters.
- `Public Property DecreasingAccount() As String` [R/W] Sets or returns the G/L account associated with decreased stock transactions (inventory offset). Field name: DecreasAc. Length: 15 characters.
- `Public Property DefaultBin() As Long` [R/W] The default bin location in the warehouse for receiving items. Field name: DftBinAbs.
- `Public Property DefaultBinEnforced() As BoYesNoEnum` [R/W] Indicates whether to enforce the use of the default bin location during receipt of items to the warehouse. That is, when you receive an item to the warehouse, you must place it in the default bin location. Field name: DftBinEnfd.
- `Public Property DropShip() As BoYesNoEnum` [R/W] Determines whether or not to the warehouse type is virtual (no address) or real (with address). Field name: DropShip.
  - remarks: When set to Y, the warehouse is virtual and shipments to this warehouse are shipped automatically to the purchaser Ship To address. In addition, the warehouse does not participate in the Material Requirement Planning (MRP). When set to N, the warehouse is real and shipments to this warehouse are shipped to the warehouse address. In addition, the warehouse can participate in the Material Requirement Planning (MRP).
- `Public Property EnableBinLocations() As BoYesNoEnum` [R/W] Enables bin locations for the warehouse. Field name: BinActivat.
- `Public Property EnableReceivingBinLocations() As BoYesNoEnum` [R/W] Enables receiving bin locations for a warehouse. Field name: RecBinEnab.
- `Public Property EUExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with EU Expenses Account. Field name: EUExpensAc. Field name: ExpensesAc. Length: 15 characters.
- `Public Property EUPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with EU Purchase Credit Acc.. Field name: APCMEUAct. Field name: APCMEUAct. Length: 15 characters
- `Public Property EURevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with EU Revenues. Field name: EURevenuAc. Length: 15 characters.
- `Public Property ExchangeRateDifferencesAccount() As String` [R/W] Sets or returns the G/L account associated with Exchange Rate Differences between purchase delivery notes and A/P invoices. Field name: ExchangeAc. Length: 15 characters.
- `Public Property Excisable() As BoYesNoEnum` [R/W] Sets or returns the Excisable in Warehouses Definition. Applicable for cluster B only (country-specific for India). Field name: Excisable.
- `Public Property ExemptedCredits() As String` [R/W] Sets or returns the G/L account associated with Exempted Credits account. Field name: ARCMExpAct. Length: 15 characters.
- `Public Property ExemptRevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Exempted Revenues. Field name: ExmptIncom). Length: 15 characters.
- `Public Property ExpenseAccount() As String` [R/W] Sets or returns the G/L account associated with Expense Account. Field name: ExpensesAc. Length: 15 characters.
- `Public Property ExpenseOffsetingAct() As String` [R/W] Sets or returns the G/L account associated with Expense Offset Account. Field name: ExpOfstAct. Length: 15 characters.
  - remarks: This is a foreign key to the ChartOfAccounts Object.
- `Public Property ExpensesClearingAccount() As String` [R/W] Sets or returns the G/L account associated with Expenses clearing Account. Field name: ExpClrAct. Length: 15 characters.
  - remarks: This is a foreign key to the ChartOfAccounts Object.
- `Public Property External() As BoYesNoEnum` [R/W] property External
- `Public Property FederalTaxID() As String` [R/W] Sets or returns the Federal Tax ID related to the warehouse. Field name: FedTaxID. Length: 32 characters.
- `Public Property ForeignExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with Foreign Expenses account. Field name: FrExpensAc. Length: 15 characters.
- `Public Property ForeignPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with Foreign Purchase Credit Account. Field name: APCMFrnAct. Length: 15 characters.
- `Public Property ForeignRevenuesAcc() As String` [R/W] Sets or returns the G/L account associated with Sales Revenue - Foreign Account. Field name: FrRevenuAc. Length: 15 characters.
- `Public Property GlobalLocationNumber() As String` [R/W] property GlobalLocationNumber
- `Public Property GoodsClearingAcc() As String` [R/W] Sets or returns the G/L account associated with closing a purchase delivery note. Field name: BalanceAcc. Length: 15 characters.
- `Public Property Inactive() As BoYesNoEnum` [R/W] property Inactive
- `Public Property IncreaseGLAccount() As String` [R/W] Sets or returns the G/L account associated to Increase G/L Account. Field name: IncresGlAc. Length: 15 characters.
- `Public Property IncreasingAcc() As String` [R/W] Sets or returns the G/L account associated to increased stock transactions (inventory offset). Field name: IncresGlAc. Length: 15 characters.
- `Public Property InternalKey() As Long` [R] Returns the internal key of the warehouse as assigned by SAP Business One when adding a warehouse. Field name: IntrnalKey.
- `Public Property InventoryOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to an inventory account used within production transactions and for change of value of the inventory account during the production process. Field name: StockOffst. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property LegalText() As String` [R/W] Legal Text defined on the warehouse level. Field name: LegalText. Length: 250 characters.
- `Public Property Location() As Long` [R/W] Sets or returns the code of the geographical area inside the warehouse. The locations can be defined through the WarehouseLocations object. Field name: location.
- `Public Property ManageSerialAndBatchNumbers() As BoYesNoEnum` [R/W] property ManageSerialAndBatchNumbers
- `Public Property NegativeInventoryAdjustmentAccount() As String` [R/W] Sets or returns the negative stock adjustment Account. Field name: NegStckAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts object.
- `Public Property Nettable() As BoYesNoEnum` [R/W] property Nettable
  - remarks: Determines whether or not the warehouse participates in the Material Requirement Planning (MRP). Field name: Nettable.
- `Public Property PriceDifferencesAccount() As String` [R/W] Sets or returns the G/L account associated with Price Differences Account. Field name: PriceDifAc. Length: 15 characters.
- `Public Property PurchaseAccount() As String` [R/W] Sets or returns the G/L account associated with Purchases. Field name: PurchaseAc. Length: 15 characters.
- `Public Property PurchaseBalanceAccount() As String` [R/W] property PurchaseBalanceAccount
- `Public Property PurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with Purchase Credit Account. Field name: APCMAct. Length: 15 characters.
- `Public Property PurchaseOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Offsetting. Field name: PurchOfsAc. Length: 15 characters.
- `Public Property PurchaseReturningAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Returning account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property ReceiveUpToMaxQuantity() As BoYesNoEnum` [R/W] property ReceiveUpToMaxQuantity
- `Public Property ReceiveUpToMaxWeight() As BoYesNoEnum` [R/W] property ReceiveUpToMaxWeight
- `Public Property ReceiveUpToMethod() As ReceivingUpToMethodEnum` [R/W] property ReceiveUpToMethod
- `Public Property ReceivingBinLocationsBy() As ReceivingBinLocationsMethodEnum` [R/W] The method by which items are received at receiving bin locations. Field name: RecItemsBy.
- `Public Property RestrictReceiptToEmptyBinLocation() As BoYesNoEnum` [R/W] property RestrictReceiptToEmptyBinLocation
- `Public Property ReturningAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Returning Account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property RevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Revenues Account. Field name: RevenuesAc. Length: 15 characters.
- `Public Property SalesCreditAcc() As String` [R/W] Sets or returns the G/L account associated with Sales Credit EU Account. Field name: ARCMEUAct. Length: 15 characters.
- `Public Property SalesCreditEUAcc() As String` [R/W] Sets or returns the G/L account associated with Sales Credit EU Account. Field name: ARCMEUAct . Length: 15 characters.
- `Public Property SalesCreditForeignAcc() As String` [R/W] Sets or returns the G/L account associated withSales Credit EU Account. Field name: ARCMFrnAct . Length: 15 characters.
- `Public Property ShippedGoodsAccount() As String` [R/W] Sets or returns the G/L account associated with Shipping Goods Account. Field name: ShpdGdsAct. Length: 15 characters.
  - remarks: This is a foreign key to ChartOfAccounts Object.
- `Public Property Shipper() As String` [R/W] property Shipper
- `Public Property State() As String` [R/W] Sets or returns the state code of the sub-component of the warehouse address. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property StockAccount() As String` [R/W] Sets or returns the G/L account associated to stock in continues stock system. Length: 15 characters. Field name: BalInvntAc.
- `Public Property StockInflationAdjustAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Inflation Adjust. Length: 15 characters. Field name: IncreasAc.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property StockInflationOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Inflation Offset. Field name: DecreasAc. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property StockInTransitAccount() As String` [R/W] The stock in transit G/L account for this warehouse. Field name: StkInTnAct
- `Public Property Storekeeper() As Long` [R/W] property Storekeeper
- `Public Property Street() As String` [R/W] Sets or returns the street subcomponent of the warehouse address. Field name: street. Length: 100 characters.
- `Public Property StreetNo() As String` [R/W] property StreetNo
- `Public Property TaxGroup() As String` [R/W] Sets or returns the sales tax code as defined in SalesTaxCodes object. Field name: VatGroup. Length: 8 characters.
- `Public Property TaxOffice() As String` [R/W] property TaxOffice
- `Public Property TransfersAcc() As String` [R/W] Sets or returns the G/L account associated with Stock Transfers. Field name: TransferAc. Length: 15 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object. Field name: userSign2.
- `Public Property VarianceAccount() As String` [R/W] Sets or returns the G/L account associated with Variance Account. Field name: VarianceAc. Length: 15 characters.
- `Public Property VATInRevenueAccount() As String` [R/W] Sets or returns the G/L account associated with VAT in Revenues. Field name: VatRevAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the Warehouse identification key. Mandatory field. Field name: WhsCode. Length: 8 characters.
- `Public Property WarehouseName() As String` [R/W] Sets or returns the warehouse name. Field name: WhsName. Length: 100 characters.
- `Public Property WHIncomingCenvatAccount() As String` [R/W] Sets or returns the Incoming CENVAT Account (WH) for Account Setting in Warehouses Definition. Applicable for cluster B only (country-specific for India). Field name: WhICenAct.
- `Public Property WHOutgoingCenvatAccount() As String` [R/W] Sets or returns the Outgoing CENVAT Account (WH) for Account Setting in Warehouse Definition. Applicable for cluster B only (country-specific for India). Field name: WhOCenAct.
- `Public Property WHShipToName() As String` [R/W] Sets or returns the Ship-to Name (WH) in Warehouses Definition. Applicable for cluster B only (country-specific for India). Field name: WhShipTo.
- `Public Property WIPMaterialAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP). Field name: WipAcct. Length: 15 characters.
  - remarks: Work In Prog account is used for posting transactions such as, transferring row material from the warehouse to the production floor.
- `Public Property WIPMaterialVarianceAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP) differences. That is, the account for posting differences between the value of the row material (before production) and the value of the complete product (after production). Field name: WipVarAcct. Length: 15 characters.
- `Public Property WipOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to a WIP (work in progress) account used within production transactions and for change of value of the WIP account during the production process. Field name: WipOffset. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property ZipCode() As String` [R/W] Sets or returns the Zip Code of the warehouse address. Field name: ZipCode. Length: 20 characters.

## Methods (7)
- `Public Function Add() As Long` Adds a new record to the Warehouses table. Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Retrieves the XML schema of the data structure. Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal WhsCode As String) As Boolean` Retrieves the values of the object's properties by the object's absolute key from the Company database. Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `WhsCode`: Warehouse code as a string (WarehouseCode).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
  - remarks: To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key you can use the DataBrowser object. To use this method you must specify the object key. You can also use this method to find whether or not there is an object related to the key you specify. If you do not know the object key, you can use the DataBrowser object to retreive an object using more complex queries.
- `Public Function Remove() As Long` Removes a specified field from the table. Deletes a record from the object table.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Warning: when removing a field, all it's content is lost. You must use the GetByKey method to retrieve a valid object.
- `Public Sub SaveToFile(ByVal FileName As String)` Save the object to a file as XML data.
  - param `FileName`: Specifies the path and file name of the XML data. Specifies the path and file name of the XML data.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You can use this method for development technologies that do not support return value as an Out parameter, such as ASP.
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
- `Public Function Update() As Long` Updates the object data in the company database.
  - returns: Determines weather the update succeeded or failed. If the method succeeds, it returns 0. Otherwise, it returns an error code. Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: Updates the object data in the company database. Before using this method, you must use the GetByKey method to retrieve an existing record, and to set the values to the object mandatory properties. You can also use the SBObob object to browse lists of objects.
