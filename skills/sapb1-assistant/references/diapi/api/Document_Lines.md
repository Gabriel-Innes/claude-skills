<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->
# Document_Lines (Object)

Document_Lines is a child object of Documents object and represents the line entries of a document in the Marketing Documents and Receipts module and the Inventory and Production module. The source table for each document is according to the document type as follows: INV1, RIN1, DLN1, RDN1, RDR1, QUT1, DPI1, PCH1, RPC1, PDN1, RPD1, POR1, PQT1, DPO1, IGN1, IGE1, and DRF1.

**Remarks:** To add a document, you must have at least one item line. Mandatory fields in SAP Business One: AccountCode and ItemCode. To display the form in the application: - For INV1 table, select Sales - A/R --> A/R Invoice. - For RIN1 table, select Sales - A/R --> A/R Credit Memo. - For DLN1 table, select Sales - A/R --> Delivery. - For RDN1 table, select Sales - A/R --> Returns. - For RDR1 table, select Sales - A/R --> Order. - For QUT1 table, select Sales - A/R --> Quotation. - For DPI1 table, select Sales - A/R --> A/R Down Payment Invoice. - For PCH1 table, select Purchasing - A/P --> A/P Invoice. - For RPC1 table, select Purchasing - A/P --> A/P Credit Memo. - For PDN1 table, select Purchasing - A/P --> Goods Receipt PO. - For RPD1 table, select Purchasing - A/P --> Goods Returns. - For POR1 table, select Purchasing - A/P --> Purchase Order. - For PQT1 table, select Purchasing - A/P --> Purchase Quotation. - For DPO1 table, select Purchasing - A/P --> A/P Down Payment Invoice. - For IGN1 table, select Inventory --> Inventory Transactions --> Goods Receipt. Or, in case of receipt from production, select Production --> Receipt from Production (see ProductionOrders). - For IGE1 table, select Inventory --> Inventory Transactions --> Goods Issue. Or, in case of issue for production, select Production --> Issue for Production (see ProductionOrders). - For DRF1 table, select Sales - A/R (or Purchasing - A/P) --> Document Draft. Set your selection criteria, and click OK.

## Properties (230)
- `Public Property AccountCode() As String` [R/W] Sets or returns the G/L account code of the business partner as defined in Chart of Accounts. Field name: AcctCode. Mandatory property. Length: 15 characters.
  - remarks: To set the AccountCode value when working with segmentation, use the FormatCode to find its key value (for example, _SYS00000000010) as follows: 1. Find the account key using the method GetObjectKeyBySingleValue. 2. Use the returned Recordset to retrieve the value of the key (for example, _SYS00000000010).
- `Public Property ActualBaseEntry() As Long` [R/W] Sets or returns the actual source document ID. Field name: ActBaseEnt.
  - remarks: This field is used to create credit memos for delivered items on reserve invoices.
- `Public Property ActualBaseLine() As Long` [R/W] Sets or returns the line number in the actual source document. Field name: ActBaseLn.
  - remarks: This field is used to create credit memos for delivered items on reserve invoices.
- `Public Property ActualDeliveryDate() As Date` [R/W] Sets or returns the actual delivery date of the item specified in the row.
- `Public Property Address() As String` [R/W] Sets or returns the Bill To address of the business partner in purchase documents only. Field name: Address. Length: 254 characters.
- `Public Property AgreementNo() As Long` [R/W] property AgreementNo
- `Public Property AgreementRowNumber() As Long` [R/W] property AgreementRowNumber
- `Public Property AppliedTax() As Double` [R] Returns the tax of a paid invoice in local currency. Field name: VatAppld.
  - remarks: Internal use.
- `Public Property AppliedTaxFC() As Double` [R] Returns the tax of a paid invoice in foreign currency. Field name: VatAppldFC.
  - remarks: Internal use.
- `Public Property AppliedTaxSC() As Double` [R] Returns the tax of a paid invoice in system currency. Field name: VatAppldSC.
  - remarks: Internal use.
- `Public Property BackOrder() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to enable partial quantities of items per row in the document. Field name: BackOrdr.
- `Public Property BarCode() As String` [R/W] Sets or returns the Bar Code (EAN code) for this item. Field name: CodeBars. Length: 16 characters.
- `Public Property BaseEntry() As Long` [R/W] Sets or returns the source Document ID. Field name: BaseEntry.
  - remarks: Use the BaseEntry, BaseLine, and BaseType properties to extract data from one document to another. For example, to extract data from a Quotation to an Order. To receive items from production or to issue items for production, you must specify the production order number (DocumentNumber) in the BaseEntry.
- `Public Property BaseLine() As Long` [R/W] Sets or returns the line number in the source document. Field name: BaseLine.
  - remarks: Use the BaseLine, BaseEntry, and BaseType properties to extract data from one document to another. For example, to extract data from a Quotation to an Order.
- `Public Property BaseOpenQuantity() As Double` [R] Returns the quantity in the base document at the time the user creates the target document. Field name: BaseOpnQty.
  - remarks: The field is available in database only. The field is not exposed in the application. The field can not be used via SDK.
- `Public Property BaseType() As Long` [R/W] Sets or returns a valid value of BoAPARDocumentTypes that determines the document type. Field name: BaseType.
  - remarks: Use the BaseType, BaseEntry, and BaseLine properties to extract data from one document to another. For example, to extract data from a Quotation to an Order.
- `Public Property BatchNumbers() As BatchNumbers` [R] Returns the BatchNumbers object.
- `Public Property BinAllocations() As DocumentLinesBinAllocations` [R] The bin allocation of items or serial items or batch items.
- `Public Property CCDNumbers() As CCDNumbers` [R] property CCDNumbers
- `Public Property CESTCode() As Long` [R/W] Specify the CEST Code that identifies material items which are subject to ST taxation.. Field name: CESTCode.
- `Public Property CFOPCode() As String` [R/W] Sets or returns the CFOP Code for Document. This is a foreign key to the NotaFiscalCFOP object, which applicable for cluster B only (country-specific for Brazil only). Field name: CFOPCode. Length: 6 characters.
  - remarks: The CFOP code describes the performed business transaction from the tax authorities point of view. A Nota Fiscal line including the taxes ICMS and/or IPI requires a CFOP.
- `Public Property ChangeAssemlyBoMWarehouse() As String` [R/W] Sets or returns a value that specifies whether or not the default warehouse was changed for an item that is part of bill-of-material assembly. This is relevant for the specified item in the specified document only. Field name: ChgAsmBoMW. Length: 1 character.
  - remarks: Logic Description - When user change warehouse of Assembly BoM in Marketing Document except Sales Order and A/R Reserve Invoice, the system displays a confirmation box to ask "Changing the warehouse for the Assembly BoM's parent item will update the warehouse for all the Assembly BoM's components. Continue?" - If user select "Yes", system generate posting with the new warehouse selected - If user select "No", warehouse setting in BoM will not be changed - If user change warehouse in Form Setting -> Document -> Table of Marketing Document except Sale Order, there will be pop up message "Update the warehouse for all the items?" and user click "Yes" button, system will also update warehouse for all the Assembly BoM's components.
- `Public Property ChangeInventoryQuantityIndependently() As BoYesNoEnum` [R/W] property ChangeInventoryQuantityIndependently
- `Public Property CNJPOfManufacturer() As String` [R/W] CNPJ of manufacturer. Field name: CNJPMan. Length: 14 characters.
- `Public Property COGSAccountCode() As String` [R/W] Sets or returns the code of the Cost of Goods Sold account. This is a foreign key to the ChartOfAccounts object. Field name: CogsAcct. Length: 15 characters.
  - remarks: This COGS Account Manual selection task adds COGS account code on item lines, so that the user is able to override default COGS account set on item master data. Because of definition of COGS account on line, COGS profit center (COGSCostingCode) and revenue profit center are affected by the new auto-complete logics, too.
- `Public Property COGSCostingCode() As String` [R/W] Sets or returns the code of the Cost of Goods Sold cost center. This is a foreign key to the Loading Factors table (field name OcrCode in OOCR table). Field name: CogsOcrCod. Length: 8 characters.
- `Public Property COGSCostingCode2() As String` [R/W] Multiple cost centers assigned to the Cost of Goods Sold accounts. Field name: CogsOcrCod2. Length: 8 characters.
- `Public Property COGSCostingCode3() As String` [R/W] Multiple cost centers assigned to the Cost of Goods Sold accounts. Field name: CogsOcrCod3. Length: 8 characters.
- `Public Property COGSCostingCode4() As String` [R/W] Multiple cost centers assigned to the Cost of Goods Sold accounts. Field name: CogsOcrCod4. Length: 8 characters.
- `Public Property COGSCostingCode5() As String` [R/W] Multiple cost centers assigned to the Cost of Goods Sold accounts. Field name: CogsOcrCod5. Length: 8 characters.
- `Public Property CommisionPercent() As Double` [R/W] Sets or returns the commission percentage for this item. Field name: Commission.
- `Public Property CommodityClassification() As Long` [R/W] property CommodityClassification
- `Public Property ConsiderQuantity() As BoYesNoEnum` [R/W] property ConsiderQuantity
- `Public Property ConsumerSalesForecast() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to include this line in the sales forecast. Field name: ConsumeFCT.
- `Public Property CorrectionInvoiceItem() As BoCorInvItemStatus` [R/W] Sets or returns a valid value of BoCorInvItemStatus type that specifies the status of the correction invoice. Field name: CEECFlag.
  - remarks: Country-specific property for Poland.
- `Public Property CorrInvAmountToDiffAcct() As Double` [R/W] Sets or returns the amount of the correction invoice for the Difference Account. Field name: ToDiff.
  - remarks: Country-specific property for Poland.
- `Public Property CorrInvAmountToStock() As Double` [R/W] Sets or returns the amount of the correction invoice for the Stock Account. Field name: ToStock.
  - remarks: Country-specific property for Poland.
- `Public Property CostingCode() As String` [R/W] The distribution rule for dimension 1 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode This is a foreign key to the DistributionRule object.
- `Public Property CostingCode2() As String` [R/W] The distribution rule for dimension 2 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode2.
- `Public Property CostingCode3() As String` [R/W] The distribution rule for dimension 3 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode3.
- `Public Property CostingCode4() As String` [R/W] The distribution rule for dimension 4 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode4.
- `Public Property CostingCode5() As String` [R/W] The distribution rule for dimension 5 for allocating costs and revenues (both direct and indirect) to one or more profit centers. Field name: OcrCode5.
- `Public Property Count() As Long` [R] Returns the total number of records in the table.
  - remarks: When adding a new row, the system increments the value of this property automatically.
- `Public Property CountryOrg() As String` [R/W] Sets or returns the origin country. Field name: CountryOrg. Length: 3 characters. This is a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property CreditOriginCode() As String` [R/W] property CreditOriginCode
- `Public Property CSTCode() As String` [R/W] Sets or returns the CST Code for Document. This is a foreign key to the NotaFiscalCST object that enables to define CST codes for Nota Fiscal. The NotaFiscalCST object is applicable for cluster B only (country-specific for Brazil only). Field name: CSTCode. Length: 4 characters.
  - remarks: CST is a required code by the Nota Fiscal and describes the tributary situation of an item for the ICMS (state tax). CST is composed of two parts, where the first part indicates the origin of the merchandise and the second part indicates the specific taxation. The CST code must be assigned at the line level, as a different code can exist for each item. Need to maintain a table of CST values that will be suggested by the system.
- `Public Property CSTforCOFINS() As String` [R/W] property CSTforCOFINS
- `Public Property CSTforIPI() As String` [R/W] property CSTforIPI
- `Public Property CSTforPIS() As String` [R/W] property CSTforPIS
- `Public Property CtrSealQty() As Double` [R/W] Specify Control Seal Quantity for document line. Field name: CtrSealQty.
- `Public Property Currency() As String` [R/W] Sets or returns the price currency used in the document row. Field name: Currency. Length: 3 characters.
  - remarks: You must define the currency strings before using this property. One business transaction may include more than one currency. In multiple currencies transaction, first call the GetCurrencyRate method to unify the total amount in different currencies into one currency. The value for multiple currencies is ##.
- `Public Property CUSplit() As BoYesNoEnum` [R/W] If this flag is set to true, the amounts that are not subject to withholding tax and are not supplier income amounts are distinguished and split in a standalone report page.
  - remarks: Italy only, for the withholding tax single certification (Certificazione Unica).
- `Public Property DefectAndBreakup() As Double` [R/W] property DefectAndBreakup
- `Public Property DeferredTax() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not to apply deferred tax for the item specified in the row. Field name: DeferrTax.
  - remarks: You can modify the value of this property only if the invoice is not yet posted. Country-specific for Spain, Italy, Portugal, and France. Source code !UNRECOGNISED ELEMENT TYPE 'sourcecode'! " -->Example!UNRECOGNISED ELEMENT TYPE 'filtereditemlist'!" -->See Also !UNRECOGNISED ELEMENT TYPE 'filtereditemlist'! " -->
- `Public Property DestinationCountryForImport() As String` [R/W] property DestinationCountryForImport
- `Public Property DestinationRegionForImport() As Long` [R/W] property DestinationRegionForImport
- `Public Property DiscountPercent() As Double` [R/W] Sets or returns the discount percentage you specify for a customer, or the discount percentage a supplier specifies for you. Field name: Discount.
  - remarks: You can either set the DiscountPercent property and let the application calculates the PriceAfterVAT property accordingly, or set PriceAfterVAT and let the application calculates the DiscountPercent property accordingly. But not both properties at the same script. SAP Business One automatically completes the value for this property from PaymentTermsTypes object (OCTG table) according to the selected payment terms (PayTermsGrpCode property). For business partners defined as type 'Other' (neither a customer nor a supplier) you do not have to set this property. (For 5% discount set the value 5, not 0.05.)
- `Public Property DistributeExpense() As BoYesNoEnum` [R/W] Determines whether or not to use Distribute Expense. Field name: DistribExp.
- `Public Property DocEntry() As Long` [R] property DocEntry
- `Public Property EBooksDetails() As EBooks_Doc_Details` [R] property EBooksDetails
- `Public Property EnableReturnCost() As BoYesNoEnum` [R/W] property EnableReturnCost
- `Public Property EqualizationTaxPercent() As Double` [R] Returns the equalization tax percentage for this item in the row. This equalization tax is an additional tax to the regular tax (NetTaxAmount property). Field name: EquVatPer.
  - remarks: Country-specific property for Spain, Italy, Portugal, and France. This property applies only to customers.
- `Public Property ExciseAmount() As Double` [R/W] Sets or returns the excise (tax) amount. Field name: ExciseAmt.
  - remarks: Country-specific for Poland.
- `Public Property ExLineNo() As String` [R/W] Specify the ExLineNo field of the marketing document tables. The marketing document tables include INV1, RIN1, DLN1, RDN1, RDR1, QUT1, PCH1, RPC1, PDN1, RPD1, POR1, IGN1, IGE1, and DRF1. Length: 10 characters.
  - remarks: The property is for SAP Business One integration for SAP NetWeaver - Subsidiary Integration. This is a technical field that does not appear in the SAP Business One application. You can modify the field through the DI-API only.
- `Public Property ExpenseOperationType() As BoExpenseOperationTypeEnum` [R/W] property ExpenseOperationType
- `Public Property Expenses() As Document_LinesAdditionalExpenses` [R] Returns the Document_LinesAdditionalExpenses child object.
- `Public Property ExpenseType() As String` [R/W] property ExpenseType
- `Public Property ExportProcesses() As ExportProcesses` [R] property ExportProcesses
- `Public Property ExternalCalcTaxAmount() As Double` [R/W] property ExternalCalcTaxAmount
- `Public Property ExternalCalcTaxAmountFC() As Double` [R] property ExternalCalcTaxAmountFC
- `Public Property ExternalCalcTaxAmountSC() As Double` [R] property ExternalCalcTaxAmountSC
- `Public Property ExternalCalcTaxRate() As Double` [R/W] property ExternalCalcTaxRate
- `Public Property Factor1() As Double` [R/W] Sets or returns the value of the first factor for calculating the item's quantity in the row. Field name: Factor1.
  - remarks: Example: A 1.20 m high fence is sold in square meters. To calculate the quantity on which the price is based, the system must multiply the sold length by the height of the fence. In this case, the length of the fence is multiplied by Factor1 and the height is multiplied by Factor2. The values of Factor1, Factor2, Factor3, Factor4 properties are used in purchase and sales documents. If the Quantity property is set, Factor 1, Factor 2, Factor 3, and Factor 4 properties are automatically set to 1 by default because the quantity overrides the factor fields. To set the factor fields, quantity must be empty.
- `Public Property Factor2() As Double` [R/W] Sets or returns the value of the second factor for calculating the item's quantity in the row. Field name: Factor2.
  - remarks: Example: A 1.20 m high fence is sold in square meters. To calculate the quantity on which the price is based, the system must multiply the sold length by the height of the fence. In this case, the length of the fence is multiplied by Factor1 and the height is multiplied by Factor2. The values of Factor1, Factor2, Factor3, Factor4 properties are used in purchase and sales documents. If the Quantity property is set, Factor 1, Factor 2, Factor 3, and Factor 4 properties are automatically set to 1 by default because the quantity overrides the factor fields. To set the factor fields, quantity must be empty.
- `Public Property Factor3() As Double` [R/W] Sets or returns the value of the third factor for calculating the item's quantity in the row. Field name: Factor3.
  - remarks: Example: A 1.20 m high fence is sold in square meters. To calculate the quantity on which the price is based, the system must multiply the sold length by the height of the fence. In this case, the length of the fence is multiplied by Factor1 and the height is multiplied by Factor2. The values of Factor1, Factor2, Factor3, Factor4 properties are used in purchase and sales documents. If the Quantity property is set, Factor 1, Factor 2, Factor 3, and Factor 4 properties are automatically set to 1 by default because the quantity overrides the factor fields. To set the factor fields, quantity must be empty.
- `Public Property Factor4() As Double` [R/W] Sets or returns the value of the forth factor for calculating the item's quantity in the row. Field name: Factor4.
  - remarks: Example: A 1.20 m high fence is sold in square meters. To calculate the quantity on which the price is based, the system must multiply the sold length by the height of the fence. In this case, the length of the fence is multiplied by Factor1 and the height is multiplied by Factor2. The values of Factor1, Factor2, Factor3, Factor4 properties are used in purchase and sales documents. If the Quantity property is set, Factor 1, Factor 2, Factor 3, and Factor 4 properties are automatically set to 1 by default because the quantity overrides the factor fields. To set the factor fields, quantity must be empty.
- `Public Property FederalTaxID() As String` [R/W] property FederalTaxID
- `Public Property FreeOfChargeBP() As BoYesNoEnum` [R/W] property FreeOfChargeBP
- `Public Property FreeText() As String` [R/W] Sets or returns comments related to the specified item in the row. Field name: FreeTxt. Length: 100 characters.
- `Public Property GeneratedAssets() As GeneratedAssets` [R] property GeneratedAssets
- `Public Property GrossBase() As Long` [R/W] Specifies how to retrieve the base price for calculating gross profit. The base price can be derived, for example, from the last purchase price, from a price list, or from the current item cost. Field name: GrossBase.
  - remarks: The the following are the valid values: - Any key of a price list (PriceListNo property of the PriceLists object) - -1: Last Purchase Price - -2: Last Calculated Price - -5: Item Cost - -10: Manual Price
- `Public Property GrossBuyPrice() As Double` [R/W] The cost for calculating the gross profit for each item in the current row. Field name: GrossBuyPr.
- `Public Property GrossPrice() As Double` [R/W] property GrossPrice
- `Public Property GrossProfit() As Double` [R] property GrossProfit
- `Public Property GrossProfitFC() As Double` [R] property GrossProfitFC
- `Public Property GrossProfitSC() As Double` [R] property GrossProfitSC
- `Public Property GrossProfitTotalBasePrice() As Double` [R/W] The total cost for calculating the gross profit for the current row. This property is equal to the GrossBuyPrice property times the Quantity property. Field name: GPTtlBasPr.
- `Public Property GrossTotal() As Double` [R/W] property GrossTotal
- `Public Property GrossTotalFC() As Double` [R/W] property GrossTotalFC
- `Public Property GrossTotalSC() As Double` [R] property GrossTotalSC
- `Public Property Height1() As Double` [R/W] Sets or returns the primary height of the item specified in the row. Field name: Height1.
- `Public Property Height2() As Double` [R/W] Sets or returns the secondary height of the item specified in the row. Field name: Height2.
- `Public Property Height2Unit() As Long` [R/W] Sets or returns the measurement units for Height2 property. Field name: Hght2Unit.
- `Public Property Hight1Unit() As Long` [R/W] Sets or returns the measurement units for Height1 property. Field name: Hght1Unit.
- `Public Property HSNEntry() As Long` [R/W] property HSNEntry
- `Public Property ImportProcesses() As ImportProcesses` [R] property ImportProcesses
- `Public Property Incoterms() As Long` [R/W] property Incoterms
- `Public Property IndicatorForRelevantScale() As BoYesNoEnum` [R/W] Indicator for relevant scale. Field name: IndEscala.
- `Public Property InventoryQuantity() As Double` [R/W] The inventory quantity. Field name: InvQty.
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. The item code must be unique. This is a foreign key to the Items object. Field name: ItemCode. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property ItemDescription() As String` [R/W] Sets or returns the item name/description. Field name: Dscription. Length: 100 characters.
- `Public Property ItemDetails() As String` [R/W] Sets or returns the item details in the marketing document line. Field name: Text. Length: 16 characters.
- `Public Property ItemType() As BoDocItemType` [R] property ItemType
- `Public Property LastBuyDistributeSum() As Double` [R] Returns the Last Buy Distribute Sum. Field name: LstByDsSum.
  - remarks: CIN1
- `Public Property LastBuyDistributeSumFc() As Double` [R] Returns the Last Buy Distribute Sum in Foreign Currency. Field name: LstByDsFc.
  - remarks: CIN1
- `Public Property LastBuyDistributeSumSc() As Double` [R] Returns the Last Buy Distribute Sum Sc in System Currency. Field name: LstByDsSc.
  - remarks: CIN1
- `Public Property LastBuyInmPrice() As Double` [R] Returns the last sales price of the item according to OIVL table (Warehouse Journal). Field name: LstBINMPr.
  - remarks: CIN1
- `Public Property Lengh1() As Double` [R/W] Sets or returns the primary length of the item specified in the row. Field name: Length1.
- `Public Property Lengh1Unit() As Long` [R/W] Sets or returns the measurement units for Lengh1 property. Field name: Len1Unit.
- `Public Property Lengh2() As Double` [R/W] Sets or returns the secondary length of the item specified in the row. Field name: length2.
- `Public Property Lengh2Unit() As Long` [R/W] Sets or returns the measurement units for Lengh2 property. Field name: Len2Unit.
- `Public Property LineNum() As Long` [R] Returns the current row number in the list. Field name: LineNum.
- `Public Property LineStatus() As BoStatus` [R/W] Sets or returns a valid value that determines wether or not this document is open or close. Field name: LineStatus.
- `Public Property LineTotal() As Double` [R/W] Returns the total amount (not including tax) per row. Field name: LineTotal.
- `Public Property LineType() As BoDocLineType` [R/W] Sets or returns a value specifying whether the line is a regular item line or an alternative item line.
  - remarks: Alternative item line is supported for Quotation only, other marketing documents will raise an error.
- `Public Property LineVendor() As String` [R/W] property LineVendor
- `Public Property ListNum() As Long` [R] property ListNum
- `Public Property LocationCode() As Long` [R/W] Sets or returns the location code in invoices (INV1). Applicable for cluster B. Field name: LocCode.
- `Public Property MeasureUnit() As String` [R/W] The measurement unit (e.g., inch, cm). Field name: unitMsr. Length: 20 characters.
- `Public Property NatureOfTransaction() As Long` [R/W] property NatureOfTransaction
- `Public Property NCMCode() As Long` [R/W] property NCMCode
- `Public Property NetTaxAmount() As Double` [R/W] Returns the standard tax amount (not including equalization tax) in local currency. Field name: LineVat.
  - remarks: Use this property as read-only.
- `Public Property NetTaxAmountFC() As Double` [R/W] Returns the standard tax amount (not including equalization tax) in foreign currency. Field name: LineVatlF.
  - remarks: Use this property as read-only.
- `Public Property NetTaxAmountSC() As Double` [R] Returns the standard tax amount (not including equalization tax) in system currency. Field name: LineVatS.
- `Public Property NVECode() As String` [R/W] Enter the NVE Code. Field name: NVECode. Length: 6 characters.
- `Public Property OpenAmount() As Double` [R] The open amount for this line. Only relevant for service-type documents. The open amount is the original amount (from the LineTotal property) minus any amount received or credited. For example, in an A/R invoice, if the amount is $200 and then a credit memo is issued for $50, the open amount is $150. Field name: OpenSum.
- `Public Property OpenAmountFC() As Double` [R] The open amount for this line in foreign currency. Only relevant for service-type documents. Field name: OpenSumFC.
- `Public Property OpenAmountSC() As Double` [R] The open amount for this line in system currency. Only relevant for service-type documents. Field name: OpenSumSys.
- `Public Property OriginalItem() As String` [R] Returns the code of the item originally ordered, but due to lack in the stock it was replaced by its alternative item as defined in SAP Business One. Field name: OrigItem. Length: 20 characters. This is a foreign key to the Items object.
- `Public Property OriginCountryForExport() As String` [R/W] property OriginCountryForExport
- `Public Property OriginRegionForExport() As Long` [R/W] property OriginRegionForExport
- `Public Property OwnerCode() As Long` [R/W] property OwnerCode
- `Public Property PackageQuantity() As Double` [R/W] Returns the number of lines in a package. Field name: PackQty.
- `Public Property ParentLineNum() As Long` [R/W] property ParentLineNum
- `Public Property PartialRetirement() As BoYesNoEnum` [R/W] property PartialRetirement
- `Public Property PickListIdNumber() As Long` [R] Returns the pick list ID number. Field name: PickIdNo.
  - remarks: Country specific property for USA.
- `Public Property PickQuantity() As Double` [R] Returns the item's quantity specified in the row. Field name: PickOty.
  - remarks: Country specific property for USA.
- `Public Property PickStatus() As BoYesNoEnum` [R] Returns a valid value of BoYesNoEnum type that specifies whether all quantity of the item specified in the row was picked or partially picked from the warehouse. Field name: PickStatus.
  - remarks: Country specific property for USA. - This property refers to the pickstatus as BoYesNoEnum and is used for compatibility purpose. - The pickstatus is actually implemented as BoPickStatus enumeration that has 5 values where the first two values are compatible to BoYesNoEnum. - The PickStatusEx property is backward compatible to pickstatus and enables the use BoPickStatus.
- `Public Property PickStatusEx() As BoDocumentLinePickStatus` [R] Returns a valid value of BoPickStatus enumeration type that specifies whether all quantity of the item specified in the row was picked or partially picked from the warehouse. Field name: PickStatus.
  - remarks: Country specific property for USA. - This property extends the use of the PickStatus property (implemented as BoYesNoEnum). - The PickStatusEx property is backward compatible to pickstatus and enables the use BoPickStatus.
- `Public Property PoItemNum() As Long` [R/W] Customer's purchase order item number. This number is relevant for all items and services. Field name: PoItmNum.
- `Public Property PoNum() As String` [R/W] Customer's purchase order number. This number is relevant for all items and services. Field name: PoNum. Length: 20 characters.
- `Public Property POTargetEntry() As String` [R] The internal ID of the PO target. Field name: PoTrgEntry.
- `Public Property POTargetNum() As Long` [R] The PO target Number. Field name: PoTrgNum.
- `Public Property POTargetRowNum() As String` [R] The row number of the PO target. Field name: PoLineNum.
- `Public Property Price() As Double` [R/W] Sets or returns the item price before taxation. Field name: Price.
- `Public Property PriceAfterVAT() As Double` [R/W] Sets or returns the item price after taxation. Field name: PriceAfVAT.
  - remarks: You can either set the PriceAfterVAT property and let the application calculates the DiscountPercent property accordingly, or set DiscountPercent and let the application calculates the PriceAfterVAT property accordingly. But not both properties at the same script.
- `Public Property ProjectCode() As String` [R/W] Sets or returns the project code related to the document. Field name: Project. Length: 8 characters. This is a foreign key to the OPRJ object.
  - remarks: In SAP Business One, you can relate business transactions to projects. This can help you to create cost/income analyzes reports based on projects.
- `Public Property Quantity() As Double` [R/W] Sets or returns the quantity of items in the current business transaction. Field name: Quantity.
- `Public Property Rate() As Double` [R/W] Sets or returns the exchange rate between the current currency used in this row and the local currency. Field name: Rate.
  - remarks: You can use the GetCurrencyRate method to get the exchange rate for a specified date and currency code.
- `Public Property ReceiptNumber() As String` [R/W] property ReceiptNumber
- `Public Property RemainingOpenInventoryQuantity() As Double` [R] The remaining open inventory quantity. Field name: OpenInvQty.
- `Public Property RemainingOpenQuantity() As Double` [R] The open quantity for this line. The open quantity is the original quantity (from the Quantity property) minus any quantity that has been delivered or credited. For example, in an A/P invoice, if the quantity is 10 and then a goods receipt is executed for the invoice for a quantity of 3, the open quantity is 7. Field name: OpenQty.
- `Public Property RequiredDate() As Date` [R/W] The date by which the items should be delivered. Field: PQTReqDate.
- `Public Property RequiredQuantity() As Double` [R/W] Number of the items to be procured. Field: PQTReqQty.
- `Public Property RetirementAPC() As Double` [R/W] property RetirementAPC
- `Public Property RetirementQuantity() As Double` [R/W] property RetirementQuantity
- `Public Property ReturnAction() As Long` [R/W] property ReturnAction
- `Public Property ReturnCost() As Double` [R/W] property ReturnCost
- `Public Property ReturnReason() As Long` [R/W] property ReturnReason
- `Public Property ReverseCharge() As BoYesNoEnum` [R/W] Field: RevCharge.
- `Public Property RowTotalFC() As Double` [R/W] Sets or returns the Row Total in foreign currency. Field name: TotalFrgn.
- `Public Property RowTotalSC() As Double` [R] Sets or returns the Row Total in System currency. Field name: TotalSumSy.
  - remarks: Table: CSI1
- `Public Property SACEntry() As Long` [R/W] property SACEntry
- `Public Property SalesPersonCode() As Long` [R/W] Sets or returns the code of the sales employee who has created this document. Field name: SlpCode. This is a foreign key to the SalesPersons object.
  - remarks: Can be updated in open sales quotations and open purchase orders only. If a sales employee is defined for the selected business partner, the value for this property is retrieved from the SalesPersonCode property (BusinessPartners object), else the value is retrieved from the SalesEmployeeCode property (SalesPersons object). This property is not relevant for oInventoryGenEntry and oInventoryGenExit document types.
- `Public Property SerialNum() As String` [R/W] Sets or returns the serial number of the document line. Field name: SerialNum. Length: 17 characters.
- `Public Property SerialNumbers() As SerialNumbers` [R] Returns the SerialNumbers object.
- `Public Property ShipDate() As Date` [R/W] Sets or returns the row delivery date. Field name: ShipDate.
- `Public Property ShipFromCode() As String` [R/W] property ShipFromCode
- `Public Property ShipFromDescription() As String` [R/W] property ShipFromDescription
- `Public Property ShippingMethod() As Long` [R/W] Sets or returns the code of the shipping type (such as, Courier or Air Cargo). Field name: ShipType. This is a foreign key to the ShippingTypes object.
- `Public Property ShipToCode() As String` [R/W] Returns the address Ship To Code. Field name: ShipToCode. Length: 50 characters.
  - remarks: CIN1
- `Public Property ShipToDescription() As String` [R/W] property ShipToDescription
- `Public Property Shortages() As Double` [R/W] property Shortages
- `Public Property StandardItemIdentification() As Long` [R/W] property StandardItemIdentification
- `Public Property StgDesc() As String` [R] property StgDesc
- `Public Property StgEntry() As Long` [R] property StgEntry
- `Public Property StgSeqNum() As Long` [R] property StgSeqNum
- `Public Property StockDistributesum() As Double` [R] Returns the Stock Distribute sum. Field name: StckDstSum.
  - remarks: CIN1
- `Public Property StockDistributesumForeign() As Double` [R] Returns the Stock Distribute sum in Foreign currency. Field name: StckDstFc.
  - remarks: CIN1
- `Public Property StockDistributesumSystem() As Double` [R] Returns the Stock Distribute sum in System currency. Field name: StckDstSc.
  - remarks: CIN1
- `Public Property StockInmPrice() As Double` [R] Returns the Stock's last sale price according to the INM table. Field name: StckINMPr.
- `Public Property SupplierCatNum() As String` [R/W] Sets or returns the Vendor Catalog No. Field name: SubCatNum. Length: 14 characters.
- `Public Property Surpluses() As Double` [R/W] property Surpluses
- `Public Property SWW() As String` [R/W] Sets or returns an additional identifier of the item in the line. Field name: SWW. Length: 16 characters.
- `Public Property TaxBeforeDPM() As Double` [R] Returns the total tax amount, in local currency, before down payments are applied. Field name: VatWoDpm.
  - remarks: The proprety is relevant for Czech, Slovak, Hungary, and Poland localiztions.
- `Public Property TaxBeforeDPMFC() As Double` [R] Returns the total tax amount, in foreign currency, before down payments are applied. Field name: VatWoDpmFc.
  - remarks: The proprety is relevant for Czech, Slovak, Hungary, and Poland localiztions.
- `Public Property TaxBeforeDPMSC() As Double` [R] Returns the total tax amount, in System currency, before down payments are applied. Field name: VatWoDpmSc.
  - remarks: The proprety is relevant for Czech, Slovak, Hungary, and Poland localiztions.
- `Public Property TaxCode() As String` [R/W] Sets or returns the sales tax code for the item specified in the row. Field name: TaxCode. Length: 8 characters. This is a foreign key to the SalesTaxCodes object.
  - remarks: Country-specific property for USA. The tax code represents the sales tax related to specific locations where the business transaction occurs. Tax codes are defined in SAP Business One.
- `Public Property TaxJurisdictions() As TaxJurisdictions` [R] Returns the TaxJurisdictions object.
- `Public Property TaxLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value that specifies whether or not the item is VAT liable. Field name: WtLiable.
- `Public Property TaxOnly() As BoYesNoEnum` [R/W] Sets or returns a valid value that Determines whether or not the item is marked as Tax Only. Field name: TaxOnly. The object is applicable for cluster B only (country-specific for Brazil only).
- `Public Property TaxPercentagePerRow() As Double` [R/W] Sets or returns the tax percentage per row. Field name: VatPrcnt.
  - remarks: Country-specific property for UK. Internal use.
- `Public Property TaxPerUnit() As Double` [R] Returns the tax per unit. Field name: TaxPerUnit.
- `Public Property TaxTotal() As Double` [R/W] The total tax amount. The application calculates the tax amount as follows: TaxTotal = NetTaxAmount + TotalEqualizationTax. You can manually adjust the tax amount according to the business need. Field name: VatSum.
- `Public Property TaxType() As BoTaxTypes` [R/W] Sets or returns a valid value of BoTaxTypes type that specifies the sales tax system for the item. Field name: VatSum.
  - remarks: Country-specific property for USA and Canada.
- `Public Property Text() As String` [R] Returns the text property. Field name: text.
- `Public Property ThirdParty() As BoYesNoEnum` [R/W] property ThirdParty
- `Public Property TotalEqualizationTax() As Double` [R] Returns the equalization tax amount in local currency. Field name: EquVatSum.
  - remarks: Country-specific property for Spain, Italy, Portugal, and France. This property applies only to customers.
- `Public Property TotalEqualizationTaxFC() As Double` [R] Returns the equalization tax amount in foreign currency. Field name: EquVatSumF.
  - remarks: Country-specific property for Spain, Italy, Portugal, and France. This property applies only to customers.
- `Public Property TotalEqualizationTaxSC() As Double` [R] Returns the equalization tax amount in system currency. Field name: EquVatSumS.
  - remarks: Country-specific property for Spain, Italy, Portugal, and France. This property applies only to customers.
- `Public Property TotalInclTax() As Double` [R] Returns the total amount including tax. Field name: TotInclTax.
- `Public Property TransactionType() As BoTransactionTypeEnum` [R/W] Sets or returns a valid value of the Transaction Type. Field name: TranType.
- `Public Property TransportMode() As Long` [R/W] property TransportMode
- `Public Property TreeType() As BoItemTreeTypes` [R] Returns a valid value of BoItemTreeTypes type that specifies the product tree type of the item (also known as bill of material type). Field name: TreeType.
- `Public Property UFFiscalBenefitCode() As String` [R/W] Enter the UF Fiscal Benefit Code. This code is relevant for all items and services.. Field name: UFFiscBene. Length: 10 characters.
- `Public Property UnencumberedReason() As Long` [R/W] Choose the Reason for Unencumbered ICMS Exemption. The unencumbered ICMS exemption reason is defined based on the specific CST for ICMS suffix. Field name: UnencReasn.
- `Public Property UnitPrice() As Double` [R/W] Sets or returns this tax invoice raw unit price. Field name: UnitPrice.
- `Public Property UnitsOfMeasurment() As Double` [R/W] The number of items per measurement unit. The measurement unit is defined in the MeasureUnit property. Field name: NumPerMsr.
- `Public Property UoMCode() As String` [R] The unique code for the UoM. Field name: UomCode. Length: 20 characters.
- `Public Property UoMEntry() As Long` [R/W] The internal key of the UoM. Field name: UomEntry.
- `Public Property Usage() As String` [R/W] Sets or returns the Usage Code for Document. Field name: Usage. This is a foreign key to the NotaFiscalUsage object. The object is applicable for cluster B only (country-specific for Brazil only).
- `Public Property UseBaseUnits() As BoYesNoEnum` [R/W] Indicates whether to use the base units as defined in SAP Business One. Field name: UseBaseUn.
  - remarks: In SAP Business One, users can define whether an item is sold or purchased in discrete units or in boxes, cases, and so on. For example, a 100 screws can be sold or purchased as one unit.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.
- `Public Property VatGroup() As String` [R/W] Sets or returns the VAT group for the item specified in the row. Field name: VatGroup. Length: 8 characters.
  - remarks: Country-specific property for EU.
- `Public Property VendorNum() As String` [R/W] Sets or returns the number of the vendor who supplied this item. Field name: VendorNum. Length: 17 characters.
- `Public Property VisualOrder() As Long` [R] Returns the visual order number. The value for the first row is null, and from the second row the number starts from 1. Field name: VisOrder.
- `Public Property Volume() As Double` [R/W] Sets or returns the item volume. Field name: Volume.
- `Public Property VolumeUnit() As Long` [R/W] Sets or returns the calculation unit for Volume (ci, cc, cmm, and so on). Field name: VolUnit.
- `Public Property WarehouseCode() As String` [R/W] Sets or returns the warehouse code where the item is stored. Field name: WhsCode. Length: 8 characters.
- `Public Property Weight1() As Double` [R/W] Sets or returns the primary weight of the item specified in the row. Field name: Weight1.
- `Public Property Weight1Unit() As Long` [R/W] Sets or returns the measurement units for Weight1 property. Field name: Wght1Unit.
- `Public Property Weight2() As Double` [R/W] Sets or returns the secondary weight of the item specified in the row. Field name: Weight2.
- `Public Property Weight2Unit() As Long` [R/W] Sets or returns the measurement units for Weight2 property. Field name: Wght2Unit.
- `Public Property Width1() As Double` [R/W] Sets or returns the primary width of the item specified in the row. Field name: Width1.
- `Public Property Width1Unit() As Long` [R/W] Sets or returns the measurement units for Width1 property. Field name: Wdth1Unit.
- `Public Property Width2() As Double` [R/W] Sets or returns the secondary width of the item specified in the row. Field name: Width2.
- `Public Property Width2Unit() As Long` [R/W] Sets or returns the measurement units for Width2 property. Field name: Wdth2Unit.
- `Public Property WithholdingTaxLines() As WithholdingTaxLines` [R] Returns the WithholdingTaxLines object which support withholding tax on line level (as opposed to WithholdingTaxData object, which supports Withholding Tax in a document level). The object is applicable for cluster B only (country-specific for Brazil only).
- `Public Property WithoutInventoryMovement() As BoYesNoEnum` [R/W] To indicate that there is no inventory movement involved, that is, the credit memo does not affect the inventory quantity of the item. In this case, only the inventory value of the item is adjusted, if the quantity is positive. Field name: NoInvtryMv.
  - remarks: The field is only available in the following cases: A/P credit memos not based on other documents or A/P credit memos based on an A/P invoice or A/P credit memos based on an A/P reserve invoice, for which items have been received, and if non drop-ship warehouses are used
- `Public Property WTLiable() As BoYesNoEnum` [R/W] Sets or returns a valid value of BoYesNoEnum type that specifies whether or not this item is subject to Withholding tax. Field name: WtLiable.
  - remarks: tNES - the item in this row is not included in the withholding tax calculation. tYES - the item in this row is included in the withholding tax calculation.

## Methods (3)
- `Public Sub Add()` Adds a new data line to the object.
  - remarks: You can use this method to add an empty line to the current object. After the line is added, you can set values to the properties of this line. Note: When a new object is created, it already contains one data line, so you can set the properties of the first line directly without adding a new line. However, if the object contains more than one line, you must use the Add method.
- `Public Sub Delete()` Deletes the current line. Returns a result value that indicates success or failure.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oOrder As SAPbobsCOM.Documents ' Order object

            Dim lRetCode As Integer ' Return Code

            ' New Order

            oOrder = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oOrders)

            ' Fill Order details

            oOrder.CardCode = "C40000"

            oOrder.CardName = "Earthshaker Corporation"

            oOrder.HandWritten = SAPbobsCOM.BoYesNoEnum.tNO

            oOrder.DocDate = Today()

            oOrder.DocDueDate = Today()

            oOrder.DocCurrency = "USD"

            'Fill 2 lines in the order

            oOrder.Lines.ItemCode = "A00001"

            oOrder.Lines.ItemDescription = "IBM Inforprint 1312"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            oOrder.Lines.Add()

            oOrder.Lines.ItemCode = "A00002"

            oOrder.Lines.ItemDescription = "IBM Infoprint 1222"

            oOrder.Lines.Quantity = 1

            oOrder.Lines.Price = 380

            oOrder.Lines.TaxCode = "0"

            oOrder.Lines.LineTotal = 380

            ' Now we want to delete the second line in the Order

            oOrder.Lines.Delete()

            ' The Order will be added without the second line

            lRetCode = oOrder.Add
    ```
- `Public Sub SetCurrentLine(ByVal LineNum As Long)` Sets the active row to a specified row number.
  - param `LineNum`: Specifies the row number. The count starts from 0.
