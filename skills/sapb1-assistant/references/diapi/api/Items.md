<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Items (Object)

Items is a business object that represents the items master data in the Inventory and Production module. This object enables you to: - Add an item details. - Retrieve an item by its key. - Update item details. - Save the object in XML format. Source table: OITM.

**Remarks:** Mandatory fields in SAP Business One: ItemCode and Manufacturer. To display the Item Master Data window, from the SAP Business One Main Menu, choose Inventory --> Item Master Data. SAP Business One also lets you manage all fixed assets in the asset master data. To access the Asset Master Data window, from the SAP Business One Main Menu, choose Financials --> Fixed Assets --> Asset Master Data.

## Properties (223)
- `Public Property ApTaxCode() As String` [R/W] Sets or returns the Tax Code (AP) for purchase documents. Field name: TaxCodeAP. This is a foreign key to the SalesTaxCodes Object. Length: 8 characters.
  - remarks: Country-specific property for Mexico and Chile.
- `Public Property ArTaxCode() As String` [R/W] Sets or returns the Tax Code (AR) for sales documents. Field name: TaxCodeAR. This is a foreign key to the SalesTaxCodes Object Length: 8 characters.
  - remarks: Country-specific property for Mexico and Chile.
- `Public Property AssessableValue() As Double` [R/W] property AssessableValue
- `Public Property AssetClass() As String` [R/W] The asset class to which the asset belongs. Field name: AssetClass. Length: 20 characters.
  - remarks: After you assign an asset class to the asset, the following depreciation parameters of the asset class are copied to the asset as the defaults: Depreciation area Depreciation type Useful life
- `Public Property AssetGroup() As String` [R/W] The asset group to which the asset belongs. Field name: AssetGroup. Length: 15 characters.
- `Public Property AssetItem() As BoYesNoEnum` [R/W] Determines whether or not this item is a Fixed Assets. Field name: AssetItem.
- `Public Property AssetSerialNumber() As String` [R/W] The serial number of the asset. Field name: AssetSerNo. Length: 30 characters.
- `Public Property AssetStatus() As AssetStatusEnum` [R] The asset's status. Field name: AsstStatus.
- `Public Property AssVal4WTR() As Double` [R/W] property AssVal4WTR
- `Public Property AttachmentEntry() As Long` [R/W] property AttachmentEntry
- `Public Property AttributeGroups() As ItemsAttributeGroups` [R] Returns the ItemsAttributeGroups child object.
- `Public Property AutoCreateSerialNumbersOnRelease() As BoYesNoEnum` [R/W] Determines whether or not to create automatically a serial number when releasing the item. Applicable for cluster B only.
- `Public Property AvgStdPrice() As Double` [R/W] Sets or returns the Item Cost. Field name: AvgPrice.
- `Public Property BarCode() As String` [R/W] Sets or returns the Bar Code (EAN code) for this item. Field name: CodeBars. Length: 16 characters.
- `Public Property BarCodes() As ItemBarCodes` [R] property BarCodes
- `Public Property BaseUnitName() As String` [R/W] Sets or returns the inventory Unit Name. Field name: BaseUnit. Length: 20 characters.
- `Public Property BeverageCommercialBrandCode() As Long` [R/W] property BeverageCommercialBrandCode
- `Public Property BeverageGroupCode() As String` [R/W] property BeverageGroupCode
- `Public Property BeverageTableCode() As String` [R/W] property BeverageTableCode
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CapitalGoodsOnHoldLimit() As Double` [R/W] property CapitalGoodsOnHoldLimit
- `Public Property CapitalGoodsOnHoldPercent() As Double` [R/W] property CapitalGoodsOnHoldPercent
- `Public Property CapitalizationDate() As Date` [R/W] The date on which the asset is capitalized. Field name: CapDate.
- `Public Property Cession() As BoYesNoEnum` [R/W] Indicates whether the asset is owned by your company but financed by a bank mortgage. Field name: Cession.
- `Public Property CESTCode() As Long` [R/W] CEST Code. Field name: CESTCode.
- `Public Property ChapterID() As Long` [R/W] property ChapterID
- `Public Property CommissionGroup() As Long` [R/W] Sets or returns the Commission Group code. Field name: CommisGrp.
- `Public Property CommissionPercent() As Double` [R/W] Sets or returns the commission percentage for the specified Business Partner. Field name: CommisPcnt.
- `Public Property CommissionSum() As Double` [R/W] Sets or returns the Total Commission for Item. Field name: CommisSum.
- `Public Property CommodityClassification() As Long` [R/W] Commodity classification. Field name: CommClass.
- `Public Property ComponentWarehouse() As BoMRPComponentWarehouse` [R/W] property ComponentWarehouse
- `Public Property CostAccountingMethod() As BoInventorySystem` [R/W] Sets or returns the Valuation Method used to evaluate inventory. Field name: EvalSystem.
- `Public Property CountingItemsPerUnit() As Double` [R] The number of items per counting unit. Field name: NumInCnt.
- `Public Property CreateDate() As Date` [R] The date when the item master data created. Field name: CreateDate.
- `Public Property CreateQRCodeFrom() As String` [R/W] Provide data source that is used to create a QR Code. Field name: QRCodeSrc.
- `Public Property CreateTime() As Date` [R] The timestamp of the item master data created is recorded in the hhmmss format. Field name: CreateTS.
- `Public Property CtrSealQty() As Double` [R/W] Specify the Control Seal Quantity for Item Master Data. Field name: CtrSealQty.
- `Public Property CustomsGroupCode() As Long` [R/W] Sets or returns the Customs Group code. Customs groups determine the customs duty for an item purchased abroad. Field name: CstGrpCode.
- `Public Property DataExportCode() As String` [R/W] Sets or returns the Data Export Code. Field name: ExportCode. Length: 20 characters.
- `Public Property DeactivateAfterUsefulLife() As BoYesNoEnum` [R/W] Deactivate a low value asset when the asset's useful life ends. Field name: DeacAftUL.
  - remarks: The field is available only in the Germany localization when the following conditions are met: The asset is a low value asset. That is, the asset class of the asset has the Low Value Asset type. The asset's main depreciation area uses a depreciation type that has the After End of Useful Life retirement convention.
- `Public Property DefaultCountingUnit() As String` [R] The name of the default inventory counting unit. Field name: CntUnitMsr. Length: 100 characters.
- `Public Property DefaultCountingUoMEntry() As Long` [R/W] Specify a UoM to be used as the default inventory counting UoM. Field name: INUoMEntry.
  - remarks: Available only when the UoM group is not Manual.
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    Dim item As SAPbobsCOM.Items
    item = oCompany.GetBusinessObject(BoObjectTypes.oItems)
    Dim ret As Long

    ret = item.GetByKey("I001")
    item.DefaultCountingUoMEntry = 1 -- "SmallBox"

    ret = item.Update()
    ```
- `Public Property DefaultPurchasingUoMEntry() As Long` [R/W] The internal key of the default purchasing UoM. Field name: PUoMEntry.
- `Public Property DefaultSalesUoMEntry() As Long` [R/W] The internal key of the default sales UoM. Field name: SUoMEntry.
- `Public Property DefaultWarehouse() As String` [R/W] Sets or returns the Default Warehouse. Field name: DfltWH. Length: 8 characters.
- `Public Property DepreciationGroup() As String` [R/W] The depreciation areas you have specified in the asset class. Field name: DeprGroup. Length: 15 characters.
- `Public Property DepreciationParameters() As ItemsDepreciationParameters` [R] Returns the ItemsDepreciationParameters child object.
- `Public Property DesiredInventory() As Double` [R/W] Sets or returns the Preferred Quantity in Purchase Units. Field name: ReorderQty.
- `Public Property DistributionRules() As ItemsDistributionRules` [R] Returns the ItemsDistributionRules child object.
- `Public Property DNFEntry() As Long` [R/W] The DNF code for this item. Field name: DNFEntry This is a foreign key to the DNFCodeSetup object.
  - remarks: For Brazil only.
- `Public Property ECExpensesAccount() As String` [R/W] Sets or returns the EU Expense Account. Field name: ECExpAcc. Length: 15 characters.
  - remarks: Not relevant to DI API from version 6.2 and up.
- `Public Property ECRevenuesAccount() As String` [R/W] Sets or returns the EU revenues account. Field name: ECInAcct. Length: 15 characters.
  - remarks: Not relevant to DI API from version 6.2 and up.
- `Public Property Employee() As Long` [R/W] The employee to whom the asset is physically assigned. Field name: Technician.
- `Public Property EnforceAssetSerialNumbers() As BoYesNoEnum` [R/W] property EnforceAssetSerialNumbers
- `Public Property Excisable() As BoYesNoEnum` [R/W] property Excisable
- `Public Property ExemptIncomeAccount() As String` [R/W] Not used from DI API version 6.2 and up.
- `Public Property ExpanseAccount() As String` [R/W] Not used from DI API version 6.2 and up.
- `Public Property ForceSelectionOfSerialNumber() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to force selection of serial numbers for documents. Field name: BlockOut.
  - remarks: - This property, if set to Yes, blocks the generation of release documents, containing items with serial numbers management, for which serial numbers were not chosen.
- `Public Property ForeignExpensesAccount() As String` [R/W] Sets or returns the foreign expenses account. Length: 15 characters.
  - remarks: Not relevant to DI API from version 6.2 and up.
- `Public Property ForeignName() As String` [R/W] Sets or returns the item name or a description in foreign language. Field name: FrgnName. Length: 200 characters.
- `Public Property ForeignRevenuesAccount() As String` [R/W] Sets or returns the foreign revenues account. Length: 15 characters.
  - remarks: Not relevant to DI API from version 6.2 and up.
- `Public Property Frozen() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is on hold.
  - remarks: For items set to on hold, the end-user can specify the period when the item is on hold (FrozenFrom and FrozenTo), and also add remarks (FrozenRemarks).
- `Public Property FrozenFrom() As Date` [R/W] Sets or returns the start date for keeping the item on hold.
- `Public Property FrozenRemarks() As String` [R/W] Sets or returns the remarks regarding the on hold period. Length: 30 characters.
- `Public Property FrozenTo() As Date` [R/W] Sets or returns the end date for keeping the item on hold.
- `Public Property FuelID() As Long` [R/W] property FuelID
- `Public Property GLMethod() As BoGLMethods` [R/W] Sets or returns a valid value of BoGLMethods type that specifies the default G/L accounts for posting transactions related to the item. source: Warehouses, ItemGroups, or specified in the item level.
- `Public Property GSTRelevnt() As BoYesNoEnum` [R/W] property GSTRelevnt
- `Public Property GSTTaxCategory() As GSTTaxCategoryEnum` [R/W] property GSTTaxCategory
- `Public Property GTSItemSpec() As String` [R/W] property GTSItemSpec
- `Public Property GTSItemTaxCategory() As String` [R/W] property GTSItemTaxCategory
- `Public Property ImportedItem() As BoYesNoEnum` [R/W] property ImportedItem
- `Public Property IncomeAccount() As String` [R/W] Not used from DI API version 6.2 and up.
- `Public Property IncomingServiceCode() As Long` [R/W] Sets or returns the Item's incoming service code. Field name: ISvcCode. This is a foreign key to the Service Code table (OSCD), not exposed through the DI API.
  - remarks: The IncomingServiceCode Property is applicable for cluster B only (country-specific for Brazil only).
- `Public Property InCostRollup() As BoYesNoEnum` [R/W] property InCostRollup
- `Public Property IndirectTax() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to apply indirect tax.
  - remarks: Country-specific property for Mexico and Chile.
- `Public Property IntrastatExtension() As ItemIntrastatExtension` [R] Returns the ItemIntrastatExtension child object.
- `Public Property InventoryItem() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is a warehouse item (not a service).
- `Public Property InventoryNumber() As String` [R/W] The inventory number of the asset. Field name: InventoryNo. Length: 12 characters.
  - remarks: You can use the inventory number as an alternative to the asset number. This enables you to retain previously used numbers when transferring legacy fixed asset data, for example, from the Fixed Assets add-on.
- `Public Property InventoryUOM() As String` [R/W] Sets or returns the Unit of Measurement for the item (for example, box, case, piece.) Length: 5 characters.
- `Public Property InventoryUoMEntry() As Long` [R/W] The internal key of an inventory UoM. Field name: IUoMEntry.
- `Public Property InventoryWeight() As Double` [R/W] property InventoryWeight
- `Public Property InventoryWeight1() As Double` [R/W] property InventoryWeight1
- `Public Property InventoryWeightUnit() As Long` [R/W] property InventoryWeightUnit
- `Public Property InventoryWeightUnit1() As Long` [R/W] property InventoryWeightUnit1
- `Public Property IsPhantom() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the item is a phantom item.
  - remarks: Phantom items are considered as non-real items and are not part of the inventory (and therefore not managed). The purpose of defining an item as phantom is to facilitate the bill of material for manufacturing a product. For example, to manufacture a car, the bill of material can include a phantom item called electrical system. This item does not really exist in the inventory, but the items that are parts of the electrical system do exist.
- `Public Property IssueMethod() As BoIssueMethod` [R/W] Sets or returns a valid value that specifies the method for issuing the item from the inventory: Backflash (automatic) or Manual.
  - remarks: When one of the properties ManageBatchNumbers and ManageSerialNumbers is set to 1, you must set the IssueMethod property to Manual.
- `Public Property IssuePrimarilyBy() As IssuePrimarilyByEnum` [R/W] Specify whether you want to pick the serial or batch items for issuing according to their bin locations or their serial or batch information. Field name: IssuePriBy.
  - remarks: The field is available only if you have done the following: You have enabled bin locations for at least one warehouse. You have selected Serial Numbers or Batches in the Manage Item by field.
- `Public Property ItemClass() As ItemClassEnum` [R/W] Sets or returns a valid value of ItemClassEnum that determines wether or not current Item is a Service or Material. Field name: ItemClass.
  - remarks: The ItemClass property is applicable for cluster B (country-specific for Brazil only).
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. The item code must be unique. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property ItemCountryOrg() As String` [R/W] Sets or returns the origin country of the item. Length: 3 characters.
- `Public Property ItemName() As String` [R/W] Sets or returns the item name/description. Length: 200 characters.
- `Public Property ItemsGroupCode() As Long` [R/W] Sets or returns the items group code. The user can classify items by groups. Each item can be assigned to one group only. The items group is used for reports and evaluations.
- `Public Property ItemType() As ItemTypeEnum` [R/W] Sets or returns a valid value of this Item Type. Field name: ItemType.
  - remarks: To display the form in the application: - Select Inventory --> Item Master Data--> Item Type.
- `Public Property LeadTime() As Long` [R/W] Sets or returns the lead time in days for ordering the item. Property type Read-write property " -->
- `Public Property LegalText() As String` [R/W] Legal text. Field name: LegalText. Length: 250 characters.
- `Public Property LinkedResource() As String` [R] property LinkedResource
- `Public Property LocalizationInfos() As ItemLocalizationInfos` [R] Returns the ItemLocalizationInfos child object.
- `Public Property Location() As Long` [R/W] The location of the asset. Field name: Location.
- `Public Property Mainsupplier() As String` [R/W] Sets or returns the card code of the main supplier of this item. Length: 15 characters.
- `Public Property ManageBatchNumbers() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is managed by batch numbers.
  - remarks: ManageBatchNumbers cannot be set to 1 when ManageSerialNumbers is set to 1.
- `Public Property ManageByQuantity() As BoYesNoEnum` [R] Indicates whether the asset is managed by quantity. Field name: MgrByQty.
- `Public Property ManageSerialNumbers() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is managed by serial numbers.
  - remarks: ManageSerialNumbers cannot be set to 1 when ManageBatchNumbers is set to 1.
- `Public Property ManageSerialNumbersOnReleaseOnly() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that determines whether or not to create automatic serial numbers upon reception. Field name: ManOutOnly.
  - remarks: When this property is set to Yes, SAP Business One creates successive serial numbers (according to a successive numerator) and allows the end-user to select these numbers. - This method does not determine the management method. This is done by the SRIAndBatchManageMethod property. The property is relevant only when: - The item is managed by Serial Numbers (by setting ManageSerialNumbers to Yes). - The management method is On Release only (by setting the SRIAndBatchManageMethod to bomm_OnReleaseOnly). The property is set by the Automatic Serial Number Creation On Receipt check box.
- `Public Property ManageStockByWarehouse() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not the inventory is managed by the warehouse quantity levels.
  - remarks: This property determines how the system calculates minimal and maximal stock quantities. When set to Yes, the system refers to the values of the MinInventoy, DesiredInventory, and MaxInventory in the warehouse.
- `Public Property Manufacturer() As Long` [R/W] Sets or returns the manufacturer code of the item (foreign key of the Manufacturers object). Mandatory property.
- `Public Property MaterialGroup() As Long` [R/W] Sets or returns the Item's Material Group. Field name: MatGrp. This is a foreign key to the Material Group OMGP object, not exposed through the DI API.
  - remarks: For Brazil only.
- `Public Property MaterialType() As BoMaterialTypes` [R/W] Sets or returns a valid value of BoMaterialTypes that determines current material state from Raw Material to Finished Goods. Field name: MatType.
  - remarks: For Brazil only.
- `Public Property MaxInventory() As Double` [R/W] Sets or returns the maximum inventory quantity for this item.
  - remarks: The maximum inventory quantity can be used as a threshold to provide an alert message.
- `Public Property MinInventory() As Double` [R/W] Sets or returns the minimum inventory quantity for this item.
  - remarks: The minimum inventory quantity can be used as a threshold to provide an alert message or a recommendation for purchasing.
- `Public Property MinOrderQuantity() As Double` [R/W] Sets or returns this Item Minimum Order Quantity limitation . Field name: MinOrdrQty.
  - remarks: To display the form in the application: - Select Inventory --> Item Master Data --> Planning Data --> Minimum Order Qty .
- `Public Property MovingAveragePrice() As Double` [R] Returns the average price of an item calculated according to quantities and prices.
  - remarks: SAP Business One evaluates inventories with the moving average price on an ongoing basis. This means a valuation takes place based on the corresponding quantities and prices for each goods receipt and issue, and the moving average price is updated accordingly. The valuation price is calculated as the quantity multiplied by the average price. Assuming prices will increase over time, the items in stock will be overvalue. This gain is not as high as under the FIFO method, but greater than under the LIFO method.
- `Public Property NCMCode() As Long` [R/W] Returns the item classification issued by the Brazilian government and used to determine the IPI tax rate. NCM stands for Nomenclatura Commun do Mercosul. Field name: NCMCode This is a foreign key to the NCM Code table (ONCM), which is exposed via the NCMCodesSetupService object.
  - remarks: Relevant for Brazil only.
- `Public Property NoDiscounts() As BoYesNoEnum` [R/W] property NoDiscounts
- `Public Property NVECode() As String` [R/W] Enter the NVE code. Field name: NVECode. Length: 6 characters.
- `Public Property OrderIntervals() As String` [R/W] Sets or returns the inventory cycle such as, every week on Monday, or every first day of the month. The inventory cycles are defined in SAP Business One (OCYC table, which is not exposed through the DI API).
- `Public Property OrderMultiple() As Double` [R/W] Sets or returns the multiple quantity in addition to the minimum quantity of items in a single order.
  - remarks: For example: If the minimum order quantity is 1000 items and multiple quantity is 500 items, then the allowed quantity in a single order can be: 1000, 1500, 2000, and so on.
- `Public Property OutgoingServiceCode() As Long` [R/W] Sets or returns the Outgoing Service Code. Field name: OSvcCode. This is a foreign key to the Service Code Table (OSCD), not exposed through the DI API.
  - remarks: The OutgoingServiceCode Property is applicable for cluster B only (country-specific for Brazil only).
- `Public Property PeriodControls() As ItemsPeriodControls` [R] Returns the ItemsPeriodControls child object.
- `Public Property Picture() As String` [R/W] Sets or returns the picture file name to attach to an item. Field name: PicturName. Length: 200 characters.
  - remarks: Do not include the full path , only the file name. You can use BitMapPath property to read or change the path.
- `Public Property PlanningSystem() As BoPlanningSystem` [R/W] Sets or returns a valid value of BoPlanningSystem type that specifies the inventory planning system: MRP or None.
- `Public Property PreferredVendors() As Items_PreferredVendors` [R] Returns the Items_PreferredVendors child object.
- `Public Property PriceList() As Items_Prices` [R] Returns the Items_Prices child object.
- `Public Property PricingUnit() As Long` [R/W] property PricingUnit
- `Public Property ProcurementMethod() As BoProcurementMethod` [R/W] Sets or returns a valid value of BoProcurementMethod type that specifies the procurement method of items: Buy or Make.
- `Public Property ProdStdCost() As Double` [R/W] property ProdStdCost
- `Public Property ProductSource() As Long` [R/W] Sets or returns a valid value of BoProductSources that determines the product source. Field name: ProductSrc.
  - remarks: The ProductSource Property applicable for cluster B only (country-specific for Brazil only).
- `Public Property Projects() As ItemsProjects` [R] Returns the ItemsProjects child object.
- `Public Property Properties(ByVal GroupNum As Long) As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item belongs to one or more query groups.
  - remarks: In SAP Business One, there are 64 properties users can assign to an item. These properties are typically used for creating cross-section reports. Additionally, each item can be assigned to a group describing the different characteristic of the item. By grouping items, users can create reports based on these groups.
- `Public Property PurchaseFactor1() As Double` [R/W] Sets or returns the factor #1 by which the base price list is multiplied to calculate the purchase prices.
  - remarks: The price calculation takes into account all purchase factors 1-4. Therefore, the default factor must be 1.
- `Public Property PurchaseFactor2() As Double` [R/W] Sets or returns the factor #2 by which the base price list is multiplied to calculate the purchase prices.
  - remarks: The price calculation takes into account all purchase factors 1-4. Therefore, the default factor must be 1.
- `Public Property PurchaseFactor3() As Double` [R/W] Sets or returns the factor #3 by which the base price list is multiplied to calculate the purchase prices.
  - remarks: The price calculation takes into account all purchase factors 1-4. Therefore, the default factor must be 1.
- `Public Property PurchaseFactor4() As Double` [R/W] Sets or returns the factor #4 by which the base price list is multiplied to calculate the purchase prices.
  - remarks: The price calculation takes into account all purchase factors 1-4. Therefore, the default factor must be 1.
- `Public Property PurchaseHeightUnit() As Long` [R/W] Sets or returns the units for the purchase unit width (cm, inch, etc.). Length: 6 characters.
- `Public Property PurchaseHeightUnit1() As Long` [R/W] Sets or returns the secondary units for the purchase unit width (cm, inch, etc.).
- `Public Property PurchaseItem() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is for purchase (for example, an item can be defined as an asset).
- `Public Property PurchaseItemsPerUnit() As Double` [R/W] Sets or returns the number of items per purchasing unit.
  - remarks: For example, an item, which is sold in bottles, is purchased in crates of 12 bottles. The items per purchasing unit is, in this case, 12.
- `Public Property PurchaseLengthUnit() As Long` [R/W] Sets or returns the units for the purchase unit length (cm, inches, etc.).
- `Public Property PurchaseLengthUnit1() As Long` [R/W] Sets or returns the secondary units for the purchase unit length (cm, inches, etc.).
- `Public Property PurchasePackagingUnit() As String` [R/W] Sets or returns the purchase packaging unit. Length: 8 characters.
- `Public Property PurchaseQtyPerPackUnit() As Double` [R/W] Sets or returns the number of items per purchase packaging unit.
- `Public Property PurchaseUnit() As String` [R/W] Sets or returns the purchasing unit. For example, an item, which is sold in bottles, is purchased in crates of 12 bottles. The purchasing unit is, in this case, a crate. Length: 5 characters.
- `Public Property PurchaseUnitHeight() As Double` [R/W] Sets or returns the height of the purchase unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property PurchaseUnitHeight1() As Double` [R/W] Sets or returns the secondary height of the purchase unit.
- `Public Property PurchaseUnitLength() As Double` [R/W] Sets or returns the length of the purchase unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property PurchaseUnitLength1() As Double` [R/W] Sets or returns the secondary length of the purchase unit.
- `Public Property PurchaseUnitVolume() As Double` [R/W] Sets or returns the volume of the purchase unit.
  - remarks: The system calculates the item's volume automatically if the HxWxL dimensions are set.
- `Public Property PurchaseUnitWeight() As Double` [R/W] Sets or returns the weight of the purchase unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property PurchaseUnitWeight1() As Double` [R/W] Sets or returns the secondary weight of the purchase unit.
- `Public Property PurchaseUnitWidth() As Double` [R/W] Sets or returns the width of the purchase unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property PurchaseUnitWidth1() As Double` [R/W] Sets or returns the secondary width of the purchase unit.
- `Public Property PurchaseVATGroup() As String` [R/W] Sets or returns the VAT group for a purchase item. Length: 8 characters.
  - remarks: This property is mandatory only for countries that calculate VAT per line/item.
- `Public Property PurchaseVolumeUnit() As Long` [R/W] Sets or returns the units for the purchase unit volume (m3, ft3, litter, gallon, etc.).
- `Public Property PurchaseWeightUnit() As Long` [R/W] Sets or returns the units for the purchase unit weight (kg, lb, etc.).
- `Public Property PurchaseWeightUnit1() As Long` [R/W] Sets or returns the secondary units for the purchase unit weight (kg, lb, etc.).
- `Public Property PurchaseWidthUnit() As Long` [R/W] Sets or returns the units for the purchase unit width (cm, inch, etc.).
- `Public Property PurchaseWidthUnit1() As Long` [R/W] Sets or returns the secondary units for the purchase unit width (cm, inch, etc.).
- `Public Property QuantityOnStock() As Double` [R] Sets or returns the total quantity of the item in the warehouse.
  - remarks: In these fields, the system displays the physical stock levels actually in the warehouse, the quantities that have been ordered from vendors, and the quantities promised to customers.On the basis of this information, the system calculates the actual quantity that is available in stock.
- `Public Property QuantityOrderedByCustomers() As Double` [R] Sets or returns the total quantity of the items ordered by customers.
- `Public Property QuantityOrderedFromVendors() As Double` [R] Sets or returns the total quantity of the items ordered from vendors.
- `Public Property SACEntry() As Long` [R/W] property SACEntry
- `Public Property SalesFactor1() As Double` [R/W] Sets or returns the factor #1 by which the base price list is multiplied to calculate the sale prices.
  - remarks: The price calculation takes into account all sales factors 1-4. Therefore, the default factor must be 1.
- `Public Property SalesFactor2() As Double` [R/W] Sets or returns the factor #2 by which the base price list is multiplied to calculate the sale prices.
  - remarks: The price calculation takes into account all sales factors 1-4. Therefore, the default factor must be 1.
- `Public Property SalesFactor3() As Double` [R/W] Sets or returns the factor #3 by which the base price list is multiplied to calculate the sale prices.
  - remarks: The price calculation takes into account all sales factors 1-4. Therefore, the default factor must be 1.
- `Public Property SalesFactor4() As Double` [R/W] Sets or returns the factor #4 by which the base price list is multiplied to calculate the sale prices.
  - remarks: The price calculation takes into account all sales factors 1-4. Therefore, the default factor must be 1.
- `Public Property SalesHeightUnit() As Long` [R/W] Sets or returns the units for the sales unit height (cm, inch, etc.).
- `Public Property SalesHeightUnit1() As Long` [R/W] Sets or returns the secondary units for the sales unit height (cm, inch, etc.).
- `Public Property SalesItem() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is a sales item.
- `Public Property SalesItemsPerUnit() As Double` [R/W] Sets or returns the number of items per sales unit.
- `Public Property SalesLengthUnit() As Long` [R/W] Sets or returns the units for the sales unit length (cm, inch, etc.).
- `Public Property SalesLengthUnit1() As Long` [R/W] Sets or returns the secondary units for the sales unit length (cm, inch, etc.).
- `Public Property SalesPackagingUnit() As String` [R/W] Sets or returns the sales packaging unit. Length: 8 characters.
- `Public Property SalesQtyPerPackUnit() As Double` [R/W] Sets or returns the number of items per sales packaging unit.
- `Public Property SalesUnit() As String` [R/W] Sets or returns the sales unit. Length: 5 characters.
  - remarks: In SAP Business One, users can distinguish between sales unit and purchasing using. For example, an item that is purchased in creates of 12 bottles is sold in packages of 6 bottles. The purchasing unit is "crate with 12 bottles", and the sales unit "package with 6 bottles". One sales unit contains half a unit of the purchasing unit. All sales transactions, including the associated documents, are performed with the sales unit. However, the warehouse stock is managed on the basis of the smallest unit, which, in this example, is a bottle.
- `Public Property SalesUnitHeight() As Double` [R/W] Sets or returns the height of the sales unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitHeight1() As Double` [R/W] Sets or returns the secondary height of the sales unit.
- `Public Property SalesUnitLength() As Double` [R/W] Sets or returns the length of the sales unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitLength1() As Double` [R/W] Sets or returns the secondary length of the sales unit.
- `Public Property SalesUnitVolume() As Double` [R/W] Sets or returns the volume of the sales unit.
  - remarks: The system calculates the item's volume automatically if the HxWxL dimensions are set. If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitWeight() As Double` [R/W] Sets or returns the weight of the sales unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitWeight1() As Double` [R/W] Sets or returns the secondary weight of the sales unit.
- `Public Property SalesUnitWidth() As Double` [R/W] Sets or returns the width of the sales unit.
  - remarks: If the volume is set, the end-user do not need to set HxWxL dimensions.
- `Public Property SalesUnitWidth1() As Double` [R/W] Sets or returns the secondary width of the sales unit.
- `Public Property SalesVATGroup() As String` [R/W] Sets or returns the VAT group for a sales item. Length: 8 characters.
  - remarks: This property is mandatory only for countries that calculate VAT per line/item.
- `Public Property SalesVolumeUnit() As Long` [R/W] Sets or returns the units for the sales unit volume (m3, ft3, litter, gallon, etc.).
- `Public Property SalesWeightUnit() As Long` [R/W] Sets or returns the units for the sales unit weight (kg, lb, etc.).
- `Public Property SalesWeightUnit1() As Long` [R/W] Sets or returns the secondary units for the sales unit weight (kg, lb, etc.). Length: 6 characters.
- `Public Property SalesWidthUnit() As Long` [R/W] Sets or returns the units for the sales unit width (cm, inch, etc.). Length: 6 characters.
- `Public Property SalesWidthUnit1() As Long` [R/W] Sets or returns the secondary units for the sales unit width (cm, inch, etc.).
- `Public Property ScsCode() As String` [R/W] property ScsCode
- `Public Property SerialNum() As String` [R/W] Sets or returns the serial number of the item. Length: 17 characters.
  - remarks: In SAP Business One, users can manage items by serial numbers so that providing additional information such as, items location in the warehouse, manufacturing date, warranty data, and so on. The work method is to enter serial numbers during stock entries for items that have a definition of serial numbers management, and to choose relevant serial numbers during sales or release documents.
- `Public Property Series() As Long` [R/W] property Series
- `Public Property ServiceCategoryEntry() As Long` [R/W] property ServiceCategoryEntry
- `Public Property ServiceGroup() As Long` [R/W] Sets or returns the Item's Service Group. Field name: ServiceGrp. This is a foreign key to the OSGP object, not exposed through the DI API.
  - remarks: The ServiceGroup Property is applicable for cluster B only (country-specific for Brazil only).
- `Public Property ShipType() As Long` [R/W] Sets or returns the shipping type of the item (air cargo, courier, etc.).
- `Public Property SOIExcisable() As SOIExcisableTypeEnum` [R/W] property SOIExcisable
- `Public Property SpProdType() As SpecialProductTypeEnum` [R/W] property SpProdType
- `Public Property SRIAndBatchManageMethod() As BoManageMethod` [R/W] Sets or returns a valid value that specifies the method for managing serial numbers and batch numbers.
  - remarks: Relevant only when one of the properties ManageBatchNumbers and ManageSerialNumbers is set to 1.
- `Public Property StatisticalAsset() As BoYesNoEnum` [R/W] Indicates whether the asset is only a statistical asset that is not owned by your company. Field name: StatAsset.
- `Public Property SupplierCatalogNo() As String` [R/W] Sets or returns the item catalog number as provided by the main supplier. Length: 17 characters.
- `Public Property SWW() As String` [R/W] Sets or returns an additional identifier of the item. Length: 16 characters.
- `Public Property TaxType() As BoTaxTypes` [R/W] Sets or returns a valid value of BoTaxTypes type that specifies the sales tax system for the item.
  - remarks: Country-specific property for USA and Canada.
- `Public Property Technician() As Long` [R/W] Assign an employee for maintenance of the asset. Field name: Technician.
- `Public Property TNVED() As String` [R/W] property TNVED
- `Public Property ToleranceDays() As Long` [R/W] property ToleranceDays
- `Public Property TraceableItem() As BoYesNoEnum` [R/W] Indicate whether the item is traceable. Field name: Traceable.
- `Public Property TreeType() As BoItemTreeTypes` [R] Returns a valid value of BoItemTreeTypes type that specifies the product tree type of the item (also known as bill of material type).
- `Public Property TypeOfAdvancedRules() As TypeOfAdvancedRulesEnum` [R/W] Indicates whether the advanced rule type assigned to an item is General, Warehouse, or Item Group. You can change the advanced rule type if required. Field name: GLPickMeth.
  - remarks: For additional information about advanced rule type assignment, see the How To Setup and Work with Advanced G/L Account Determination guide in the documentation resource center.
- `Public Property UnitOfMeasurements() As ItemUnitOfMeasurements` [R] Returns the ItemUnitOfMeasurements child object.
- `Public Property UoMGroupEntry() As Long` [R/W] The internal key of a unit of measurement group. Field name: UgpEntry.
- `Public Property UpdateDate() As Date` [R] The date when the item master data updated. Field name: UpdateDate.
- `Public Property UpdateTime() As Date` [R] The timestamp of the item master data updated is recorded in the hhmmss format. Field name: UpdateTS.
- `Public Property User_Text() As String` [R/W] Sets or returns a free text string for this item. Length: 10 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property Valid() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is valid.
  - remarks: For items set to not valid, the end-user can specify the period when the item is valid (ValidFrom and ValidTo), and also add remarks (ValidRemarks).
- `Public Property ValidFrom() As Date` [R/W] Sets or returns the start date of the item's validity.
- `Public Property ValidRemarks() As String` [R/W] Sets or returns the remarks regarding the validity period. Length: 30 characters.
- `Public Property ValidTo() As Date` [R/W] Sets or returns the end date of the item's validity.
- `Public Property VatLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is subject to VAT.
  - remarks: Set to to Yes, if business transactions with this item are liable to VAT.
- `Public Property VirtualAssetItem() As BoYesNoEnum` [R/W] property VirtualAssetItem
- `Public Property WarrantyTemplate() As String` [R/W] Sets or returns the template for service warranty. Length: 20 characters.
- `Public Property WhsInfo() As ItemWarehouseInfo` [R] Returns the ItemWarehouseInfo object.
- `Public Property WTLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is subject to Withholding tax.
  - remarks: Set to to Yes, if business transactions with this item are liable to the Withholding tax.

## Methods (10)
- `Public Function Add() As Long` Adds a new record to the OITM table. Adds a record to the object table in SAP Business One company database.
- `Public Function Cancel() As Long` Cancels a record from the object table.
- `Public Function Close() As Long` Not supported.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ItemCode As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ItemCode`: Specifies the identification key of the item (see ItemCode property).
  - returns: If the object with the key you specified is found, the method returns True and the properties of the object will be filled with object's data. If the object with the key you specified is not found, the method returns False and the properties of the object remain unchanged.
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
- `Public Function UpdateFromXML(ByVal FileName As String) As Long` Receives and processes the XML content. You can remove sub-object lines from the Items object via the XML file.
  - param `FileName`: 
  - C# example (from SAP's help):
    ```csharp
    vComp.XmlExportType = BoXmlExportTypes.xet_ExportImportMode;
    Items myitems = (Items)vComp.GetBusinessObject(BoObjectTypes.oItems);
    //save an item to XML
    myitems.GetByKey("item0");
    myitems.SaveXML(@"C:\Test\mytest1.xml");

    //Delete sub line directly from C:\Test\mytest1.xml by manual

    //Update the item
    myitems.UpdateFromXML(@"C:\Test\mytest1.xml");
    ```
