<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# ItemWarehouseInfo (Object)

ItemWarehouseInfo is a child object of the Items object that represents the items in the warehouse. This object is part of the Inventory and Production module. This object enables you to add an item to the warehouse. Source table: OITW.

**Remarks:** Mandatory fields in SAP Business One: WarehouseCode and ItemCode (Items object). To display the form in the application: - Select Inventory --> Item Master Data. - Select Inventory Data tab.

## Properties (66)
- `Public Property CNJPOfManufacturer() As String` [R/W] CNPJ of Manufacturer. Field name: CNJPMan. Length: 14 characters.
- `Public Property Committed() As Double` [R] Returns the quantity of items committed to customers.
- `Public Property CostAccount() As String` [R/W] Sets or returns the cost-of-sale of an item. Length: 15 characters.
  - remarks: Default value: when G/L method is 0 or 2, default returns from the table OWHS. when G/L method is 1, default returns from the table OITB. Valid value: when G/L method is 2, valid value returns from the table OACT (can be updated). when G/L method is 0 or 1, valid value cannot be modified.
- `Public Property CostInflationAccount() As String` [R/W] Sets or returns this warehouse G/L decrease account. Field name: DecresGlAc. Length: 15 characters.
- `Public Property CostInflationOffsetAccount() As String` [R/W] Sets or returns this warehouse cost inflation account. Field name: CostRvlAct. Length: 15 characters.
- `Public Property Count() As Long` [R] Returns the total rows in the ItemWarehouseInfo object.
  - remarks: When you add a new warehouse, the value is increased automatically.
- `Public Property Counted() As Double` [R] Returns the current number of the counted items in stock.
- `Public Property CountedQuantity() As Double` [R] Sets or returns the counted inventory quantity.
- `Public Property DecreasingAccount() As String` [R/W] Sets or returns the inventory decreasing. Length: 15 characters.
- `Public Property DefaultBin() As Long` [R/W] The default bin location in the warehouse for receiving items. Field name: DftBinAbs.
- `Public Property DefaultBinEnforced() As BoYesNoEnum` [R/W] Indicates whether to enforce the use of the default bin location during receipt of items to the warehouse. That is, when you receive an item to the warehouse, you must place it in the default bin location. Field name: DftBinEnfd.
- `Public Property EUExpensesAccount() As String` [R/W] Sets or returns the total expenses inside the European Union. Length: 15 characters.
- `Public Property EUPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated to the EU Purchase Credit Account. Field name: APCMEUAct. Length: 15 characters.
- `Public Property EURevenuesAccount() As String` [R/W] Sets or returns the total revenue inside the European Union. Length: 15 characters.
- `Public Property ExchangeRateDifferencesAcct() As String` [R/W] Sets or returns the G/L account associated to the Exchange Rate Differences Account. Field name: ExchangeAc. Length: 15 characters.
  - remarks: To display the form in the application: - Select Inventory --> Item Master Data --> Planning Data --> .
- `Public Property ExemptedCredits() As String` [R/W] Sets or returns the G/L account associated to the Tax Exempt Credits account. Field name: ARCMExpAct. Length: 15 characters.
- `Public Property ExemptIncomeAcc() As String` [R/W] Sets or returns the exempt revenue. Length: 15 characters.
  - remarks: Country-specific property for Israel.
- `Public Property ExpenseClearingAct() As String` [R/W] Sets or returns the G/L account associated with Expenses clearing Account. Field name: ExpClrAct. Length: 15 characters.
  - remarks: This is a foreign key to the ChartOfAccounts Object.
- `Public Property ExpenseOffsettingAccount() As String` [R/W] Sets or returns the G/L account associated to the Expense Offset Account. Field name: ExpOfstAct. Length: 15 characters. This is a Foreign Key to the ChartOfAccounts Object.
- `Public Property ExpensesAccount() As String` [R/W] Sets or returns the expenses account. Length: 15 characters.
- `Public Property ForeignExpensAcc() As String` [R/W] Sets or returns the total expenses outside the European Union. Length: 15 characters.
- `Public Property ForeignPurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated to the Foreign Purchase Credit Account. Field name: APCMFrnAct. Length: 15 characters.
- `Public Property ForeignRevenueAcc() As String` [R/W] Sets or returns the total revenue outside the European Union. Length: 15 characters.
- `Public Property GLDecreaseAcct() As String` [R/W] Sets or returns this warehouse G/L decrease account. Field name: DecresGlAc. Length: 15 characters.
- `Public Property GLIncreaseAcct() As String` [R/W] Sets or returns this warehouse PA return account. Field name: PAReturnAc. Length: 15 characters.
- `Public Property GoodsClearingAcct() As String` [R/W] Sets or returns the G/L account associated to the Goods Clearing Account. Field name: BalanceAcc. Length: 15 characters.
- `Public Property IncreasingAccount() As String` [R/W] Sets or returns the inventory increasing. Length: 15 characters.
- `Public Property IndicatorForRelevantScale() As BoYesNoEnum` [R/W] Indicator for Relevant Scale. Field name: IndEscala.
- `Public Property InStock() As Double` [R] Returns the items quantity in the warehouse.
- `Public Property InventoryAccount() As String` [R/W] Sets or returns the inventory account. Length: 15 characters.
- `Public Property InventoryOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to an inventory account used within production transactions and for change of value of the inventory account during the production process. Field name: StockOffst. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property ItemCode() As String` [R] property ItemCode
- `Public Property ItemCycleCount() As ItemCycleCount` [R] Returns the ItemCycleCount object.
- `Public Property Locked() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the item is locked entry or exit in the warehouse.
- `Public Property MaximalStock() As Double` [R/W] Sets or returns the maximum allowed quantity of an item in the warehouse.
  - remarks: Depends on the company type. When the maximum quantity has reached, the system blocks adding documents that enter stock.
- `Public Property MinimalOrder() As Double` [R/W] Sets or returns the minimum allowed quantity of an order.
  - remarks: Depends on the company type.
- `Public Property MinimalStock() As Double` [R/W] Sets or returns the minimum allowed quantity of an item in the warehouse.
  - remarks: Depends on the company type. The system issues alerts when quantity reaches below the minimum level.
- `Public Property NegativeInventoryAdjustmentAccount() As String` [R/W] Sets or returns the G/L account associated to the Negative Inventory Adjustment. Field name: NegStckAct. Length: 15 characters. This is a Foreign Key to the ChartOfAccounts Object.
- `Public Property Ordered() As Double` [R] Returns the quantity of items ordered from vendors.
- `Public Property PAReturnAcct() As String` [R/W] Sets or returns this warehouse PA return acct. Field name: PAReturnAc. Length: 15 characters.
- `Public Property PriceDifferenceAcc() As String` [R/W] Sets or returns the price difference between the invoice and the shipping document. Length: 15 characters.
- `Public Property PurchaseAcct() As String` [R/W] Sets or returns the G/L account associated to the Purchase Account. Field name: PurchaseAc. Length: 15 characters.
- `Public Property PurchaseBalanceAccount() As String` [R/W] property PurchaseBalanceAccount
- `Public Property PurchaseCreditAcc() As String` [R/W] Sets or returns the G/L account associated to the Purchase Credit Account. Field name: APCMAct. Length: 15 characters.
- `Public Property PurchaseOffsetAcct() As String` [R/W] Sets or returns this warehouse purchase offset account. Field name: PurchOfsAc. Length: 15 characters.
- `Public Property ReturningAccount() As String` [R/W] Sets or returns the inventory returned to the vendor. Length: 15 characters.
- `Public Property RevenuesAccount() As String` [R/W] Sets or returns the total revenue. Length: 15 characters.
- `Public Property SalesCreditAcc() As String` [R/W] Sets or returns the G/L account associated to the Sales Credit Account. Field name: ARCMAct. Length: 15 characters.
- `Public Property SalesCreditEUAcc() As String` [R/W] Sets or returns the G/L account associated to the Sales Credit EU Account. Field name: ARCMEUAct. Length: 15 characters.
- `Public Property SalesCreditForeignAcc() As String` [R/W] Sets or returns the G/L account associated to the Sales Credit Foreign Acct. Field name: ARCMFrnAct. Length: 15 characters.
- `Public Property ShippedGoodsAccount() As String` [R/W] Sets or returns this warehouse Shipped Goods Account. Field name: ShpdGdsAct. Length: 15 characters.
- `Public Property StandardAveragePrice() As Double` [R/W] Sets or returns the Item Cost. Field name: AvgPrice.
- `Public Property StockInflationAdjustAccount() As String` [R/W] Sets or returns this warehouse stock inflation adjust account. Field name: StokRvlAct. Length: 15 characters.
- `Public Property StockInflationOffsetAccount() As String` [R/W] Sets or returns this warehouse stock inflation offset account. Field name: StkOffsAct. Length: 15 characters.
- `Public Property StockInTransitAccount() As String` [R/W] The stock in transit G/L account for this item in a warehouse. Field name: StkInTnAct
- `Public Property TransferAccount() As String` [R/W] Sets or returns the transfer account number. Length: 15 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VarienceAccount() As String` [R/W] Sets or returns the variance between the actual price and the standard price. Length: 15 characters.
- `Public Property VATInRevenueAccount() As String` [R/W] Sets or returns this warehouse VAT in revenue account. Field name: VatRevAct. Length: 15 characters.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the warehouse code. Mandatory property. Length: 8 characters.
- `Public Property WasCounted() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether or not the inventory was counted.
- `Public Property WHIncomingCenvatAccount() As String` [R/W] Sets or returns the Incoming CENVAT Account (WH) for Account Setting in Item Master Data that G/L Accounts are managed by Item Level. Applicable for cluster B only (country-specific for India). Field name: WhICenAct.
- `Public Property WHOutgoingCenvatAccount() As String` [R/W] Sets or returns the Outgoing CENVAT Account (WH) for Account Setting in Item Master Data that G/L Accounts are managed by Item Level. Applicable for cluster B only (country-specific for India). Field name: WhOCenAct.
- `Public Property WipAccount() As String` [R/W] Sets or returns the G/L account associated to the WIP Material Account. Field name: WipAcct. Length: 15 characters.
- `Public Property WipOffsetProfitAndLossAccount() As String` [R/W] An offsetting account (contra-account) to a WIP (work in progress) account used within production transactions and for change of value of the WIP account during the production process. Field name: WipOffset. Length: 15 characters.
  - remarks: Apply for the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property WipVarianceAccount() As String` [R/W] Sets or returns the G/L account associated to Work In Progress (WIP) differences. That is, the account for posting differences between the value of the row material (before production) and the value of the complete product (after production). Field name: WipVarAcct. Length: 15 characters.

## Methods (3)
- `Public Sub Add()` Adds a record to the object table in SAP Business One company database.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.Items oItem;

    // Delete item warehouse info
    if(oItem.GetByKey("004") == true)
    {
        oItem.WhsInfo.SetCurrentLine(5);
        oItem.WhsInfo.Delete();
        oItem.Update();
    }
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
