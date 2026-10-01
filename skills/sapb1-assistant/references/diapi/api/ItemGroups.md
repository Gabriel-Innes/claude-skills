<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ItemGroups (Object)

ItemGroups is a business object that represents the item groups definition in the Inventory and Production module. This object enables you to: - Add an item group. - Retrieve an item group by its key. - Update an item group details. - Remove an item group. - Save the object in XML format. Source table: OITB

**Remarks:** Mandatory field in SAP Business One: GroupName. To display the form in the application: - Select Administration --> Setup --> Inventory --> Item Groups. The item group definition includes: - General information about the group of items. - G/L accounts, which are defined in ChartOfAccounts, used in Item Master Data - Inventory Data in case GLMethod property is set to Item Group (Item Class).

## Properties (66)
- `Public Property Alert() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to activate an alert notification when the inventory count for the item group is due.
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property ComponentWarehouse() As BoMRPComponentWarehouse` [R/W] property ComponentWarehouse
- `Public Property CostAccount() As String` [R/W] Sets or returns the G/L account associated with Costs. Length: 15 characters.
- `Public Property CostInflationAccount() As String` [R/W] Sets or returns the G/L account associated with Cost Inflation. Field name: CostRvlAct. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property CostInflationOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Cost Inflation Offset. Field name: CstOffsAct. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property CycleCode() As Long` [R/W] Sets or returns the inventory cycle code as defined in SAP BUsiness One (OCYC table, which is not exposed through the DI API).
  - remarks: The inventory cycle schedules inventory counts and activates an alert when the inventory count is due.
- `Public Property DecreaseGLAccount() As String` [R/W] Sets or returns the G/L account associated with Decrease G/L Account. Field name: DecresGlAc. Length: 15 characters.
- `Public Property DecreasingAccount() As String` [R/W] Sets or returns the G/L account associated with decreased stock transactions (inventory offset). Field name: DecreasAc. Length: 15 characters.
- `Public Property DefaultInventoryUoM() As Long` [R/W] The default inventory UoM for the item group. Field name: IUomEntry.
- `Public Property DefaultUoMGroup() As Long` [R/W] The default UoM (Unit of Measurement) group for the item group. Field name: UgpEntry.
- `Public Property EUExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with EU Expenses Account. Field name: EUExpensAc. Field name: ExpensesAc. Length: 15 characters.
- `Public Property EUPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with EU Purchase Credit Account. Field name: APCMEUAct). Length: 15 characters.
- `Public Property EURevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with EU Revenues. Field name: EURevenuAc. Length: 15 characters.
- `Public Property ExchangeRateDifferencesAccount() As String` [R/W] Sets or returns the G/L account associated with Exchange Rate Differences between purchase delivery notes and A/P invoices. Field name: ExchangeAc. Length: 15 characters.
- `Public Property ExemptedCredits() As String` [R/W] Sets or returns the G/L account associated to the Exempted Credits. Field name: ARCMExpAct. Length: 15 characters.
- `Public Property ExemptRevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Exempted Revenues. Field name: ExmptIncom). Length: 15 characters.
- `Public Property ExpenseClearingAct() As String` [R/W] Sets or returns the G/L account associated with Expenses clearing Account. Field name: ExpClrAct. Length: 15 characters.
  - remarks: This is a foreign key to the ChartOfAccounts Object.
- `Public Property ExpenseOffsetAccount() As String` [R/W] Sets or returns the G/L account associated to the Expense Offset Account. Field name: ExpOfstAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
- `Public Property ExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with Expense Account. Field name: ExpensesAc. Length: 15 characters.
- `Public Property ForeignExpensesAccount() As String` [R/W] Sets or returns the G/L account associated with Foreign Expenses account. Field name: FrExpensAc. Length: 15 characters.
- `Public Property ForeignPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated with Foreign Purchase Credit Account. Field name: APCMFrnAct. Length: 15 characters.
- `Public Property ForeignRevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Sales Revenue - Foreign Account. Field name: FrRevenuAc. Length: 15 characters.
- `Public Property GoodsClearingAccount() As String` [R/W] Sets or returns the G/L account associated with closing a purchase delivery note. Field name: BalanceAcc. Length: 15 characters.
- `Public Property GroupName() As String` [R/W] Sets or returns the item group name. Mandatory property. Length: 20 characters.
- `Public Property IncreaseGLAccount() As String` [R/W] Sets or returns the G/L account associated to Increase G/L Account. Field name: IncresGlAc. Length: 15 characters.
- `Public Property IncreasingAccount() As String` [R/W] Sets or returns the G/L account associated to increased stock transactions (inventory offset). Field name: IncresGlAc. Length: 15 characters.
- `Public Property InventoryAccount() As String` [R/W] Sets or returns the G/L account associated to the inventory. Length: 15 characters.
- `Public Property InventoryOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to an inventory account used within production transactions and for change of value of the inventory account during the production process. Field name: StockOffst. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property InventorySystem() As BoInventorySystem` [R/W] Sets or returns a valid value of BoInventorySystem type that specifies the inventory evaluation method.
- `Public Property ItemClass() As ItemClassEnum` [R/W] property ItemClass
- `Public Property LeadTime() As Long` [R/W] Sets or returns the lead time in days for ordering items.
- `Public Property MinimumOrderQuantity() As Double` [R/W] Sets or returns the minimum quantity of items in a single order.
- `Public Property NegativeInventoryAdjustmentAccount() As String` [R/W] Sets or returns this item groups's Negative Inventory Adjustment Account. Field name: NegStckAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
- `Public Property Number() As Long` [R] Returns the item group code as assigned by SAP Business One.
- `Public Property OrderInterval() As Long` [R/W] Sets or returns the inventory cycle such as, every week on Monday, or every first day of the month. The inventory cycles are defined in SAP Business One (OCYC table, which is not exposed through the DI API).
- `Public Property OrderMultiple() As Double` [R/W] Sets or returns the multiple quantity in addition to the minimum quantity of items in a single order.
  - remarks: For example: If the minimum order quantity is 1000 items and multiple quantity is 500 items, then the allowed quantity in a single order can be: 1000, 1500, 2000, and so on.
- `Public Property PAReturnAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Returning account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property PlanningSystem() As BoPlanningSystem` [R/W] Sets or returns a valid value of BoPlanningSystem type that specifies the inventory planning system: MRP or None.
- `Public Property PriceDifferencesAccount() As String` [R/W] Sets or returns the G/L account associated with Price Differences Account. Field name: PriceDifAc. Length: 15 characters.
- `Public Property ProcurementMethod() As BoProcurementMethod` [R/W] Sets or returns a valid value of BoProcurementMethod type that specifies the procurement method of items: Buy or Make.
- `Public Property PurchaseAccount() As String` [R/W] Sets or returns the G/L account associated with Purchases. Field name: PurchaseAc. Length: 15 characters.
- `Public Property PurchaseBalanceAccount() As String` [R/W] property PurchaseBalanceAccount
- `Public Property PurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated to the Purchase Credit Account. Field name: APCMAct. Length: 15 characters.
- `Public Property PurchaseOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Offsetting. Field name: PurchOfsAc. Length: 15 characters.
- `Public Property RawMaterial() As BoYesNoEnum` [R/W] property RawMaterial
- `Public Property ReturningAccount() As String` [R/W] Sets or returns the G/L account associated with Purchase Returning Account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property RevenuesAccount() As String` [R/W] Sets or returns the G/L account associated with Revenues Account. Field name: RevenuesAc. Length: 15 characters.
- `Public Property SalesCreditAcc() As String` [R/W] Sets or returns the the G/L account associated to the Sales Credit Account. Field name: ARCMAct. Length: 15 characters.
- `Public Property SalesCreditEUAcc() As String` [R/W] Sets or returns the the G/L account associated to the Sales Credit EU Account. Field name: ARCMEUAct. Length: 15 characters.
- `Public Property SalesCreditForeignAcc() As String` [R/W] Sets or returns the the G/L account associated to the Sales Credit Foreign Account. Field name: ARCMFrnAct. Length: 15 characters.
- `Public Property ShippedGoodsAccount() As String` [R/W] Sets or returns the G/L account associated with shipped goods. Length: 15 characters.
- `Public Property StockInflationAdjustAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Inflation Adjust. Length: 15 characters. Field name: IncreasAc.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property StockInflationOffsetAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Inflation Offset. Field name: DecreasAc. Length: 15 characters.
  - remarks: Country-specific for Mexico, Chile, Guatemala, and Costa-Rica.
- `Public Property StockInTransitAccount() As String` [R/W] The stock in transit G/L account for this item group. Field name: StkInTnAct
- `Public Property ToleranceDays() As Long` [R/W] property ToleranceDays
- `Public Property TransfersAccount() As String` [R/W] Sets or returns the G/L account associated with Stock Transfers. Field name: TransferAc. Length: 15 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VarianceAccount() As String` [R/W] Sets or returns the G/L account associated with Variance Account. Field name: VarianceAc. Length: 15 characters.
- `Public Property VATInRevenueAccount() As String` [R/W] Sets or returns the G/L account associated with VAT in Revenues. Field name: VatRevAct. Length: 15 characters. This is a foreign key to the ChartOfAccounts Object.
- `Public Property WarehouseInfo() As ItemGroups_WarehouseInfo` [R] property WarehouseInfo
- `Public Property WHIncomingCenvatAccount() As String` [R/W] Sets or returns the Incoming CENVAT Account (WH) for Account Setting in Item Group Definition. Applicable for cluster B only (country-specific for India). Field name: WhICenAct.
- `Public Property WHOutgoingCenvatAccount() As String` [R/W] Sets or returns the Outgoing CENVAT Account (WH) for Account Setting in Item Groups Definition. Applicable for cluster B only (country-specific for India). Field name: WhOCenAct.
- `Public Property WIPMaterialAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP). Field name: WipAcct. Length: 15 characters.
  - remarks: Work In Prog account is used for posting transactions such as, transferring row material from the warehouse to the production floor.
- `Public Property WIPMaterialVarianceAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP) differences. That is, the account for posting differences between the value of the row material (before production) and the value of the complete product (after production). Field name: WipVarAcct. Length: 15 characters.
- `Public Property WipOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to a WIP (work in progress) account used within production transactions and for change of value of the WIP account during the production process. Field name: WipOffset. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal GroupCode As Long) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `GroupCode`: Item group code (Number).
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
