<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# AdminInfo (Object)

The AdminInfo is a data structure related to the CompanyService. It includes administration properties for system initialization (company details, document settings, and general settings), and various definitions, such as financials and banking. The properties default values vary according to the country localization. Source table: OADM.

**Remarks:** The AdminInfo fields appear in various forms of the Administration module. For example: - Administration --> Setup --> Banking - Administration --> Setup --> Financials - Administration --> Authorizations --> General Authorizations - Administration --> System Initialization --> Company Details - Administration --> System Initialization --> Document Settings

## Properties (274)
- `Public Property Account() As String` [R/W] property Account
- `Public Property AccountSegmentsSeparator() As String` [R/W] Sets or returns the Separator character displayed between the account segments (for example:"-" or "_"). Country-specific for US. Field name: ActSep. Length: 1 character.
  - remarks: Field name in the application: Account Segment Separator. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab
- `Public Property AccuracyofQuantities() As Long` [R/W] Sets or returns the respective number of decimal places displayed for quantities. This setting only affects the display. The system always calculates precisely to six decimal places. Field name: QtyDec.
  - remarks: Field name in the application: Decimal Places (0..6) - Quantities. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab
- `Public Property ActionWhenDeviateFromBAForAccounting() As BADivationAlertLevelEnum` [R/W] property ActionWhenDeviateFromBAForAccounting
- `Public Property ActionWhenDeviateFromBAForGRPO() As BADivationAlertLevelEnum` [R/W] property ActionWhenDeviateFromBAForGRPO
- `Public Property ActionWhenDeviateFromBAForPO() As BADivationAlertLevelEnum` [R/W] property ActionWhenDeviateFromBAForPO
- `Public Property AdditionalIdNumber() As String` [R/W] Sets or returns the additional ID number of the company. For example, the tax authority identifies the company as part of a group of companies by this number. Length: 32 characters. Field name: FreeZoneNo.
  - remarks: Field name in the application: Additional ID. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab
- `Public Property Address() As String` [R] Sets or returns the company address in local language. Length: 254 characters. Field name: CompnyAddr.
  - remarks: Field name in the application: Address. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> General tab --> Local Language tab
- `Public Property AddressinForeignLanguage() As String` [R/W] Returns the company address in foreign language. Length: 254 characters. Field name: CmpnyAddrF.
  - remarks: Field name in the application: Address To display the form in the application: - Select Administration --> System Initialization --> Company Details --> General tab --> Foreign Language tab
- `Public Property AdressFromWH() As BoYesNoEnum` [R/W] Determines whether or not to display the full warehouse address in purchase documents. Field name: AdrsFromWH.
  - remarks: Field name in the application: Use Warehouse Address. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab
- `Public Property AdvancesonCorpIncomeTax() As Double` [R/W] Sets or returns the percentage that must be advanced on account of corporate income tax. Country-specific for Israel. Field name: DpsitPrcnt.
  - remarks: Field name in the application: Advances on Corp. Income Tax %. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab
- `Public Property AlertbyWarehouse() As BoYesNoEnum` [R/W] Determines whether or not the system checks the inventory in a specific warehouse or in all warehouses where the item is stored. Field name: WarnByWhs. tYES - the system checks the inventory level in the specified warehouse when the sales document is entered. If the current transaction results in this level falling below a set minimum, a warning message is displayed - even if the inventory for the item in all warehouses is greater than the minimum. tNO - the inventory level is checked in all warehouses where the item is stored.
  - remarks: Field name in the application: Alert By Warehouse. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab. tYES - the system checks the inventory level in the specified warehouse when the sales document is entered. If the current transaction results in this level falling below a set minimum, a warning message is displayed - even if the inventory for the item in all warehouses is greater than the minimum. tNO - the inventory level is checked in all warehouses where the item is stored.
- `Public Property AlertTypeforWHStock() As BoAlertTypeforWHStockEnum` [R/W] Determines the type of system's response when the inventory level falls below this minimum as the result of a sales document, such as a delivery note or an invoice. Field name: LevelWarn.
  - remarks: Field name in the application: Alert Type when attempting to Release Stock Below the Minimum Level. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab
- `Public Property AliasName() As String` [R/W] property AliasName
- `Public Property AllowBPWithNoOwner() As BoYesNoEnum` [R/W] property AllowBPWithNoOwner
- `Public Property AllowClosedSalesQuotations() As BoYesNoEnum` [R/W] Determines whether sales quotation documents remain open or closed after being copied (in full) to a follow-up document. Field name: ClosedQuot.
  - remarks: Field name in the application: Allow Copying Closed Quotations to Target Document. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Sales Quatation. tNO - the quotation is not available for selection when you create a sales document by reference. tYES - the quotation is repeatedly available for reference when creating follow-up documents.
- `Public Property AllowFuturePostingDate() As BoYesNoEnum` [R/W] Determines whether or not to allow future posting dates at the company level. Field name: AllowFuPos.
  - remarks: Field name in the application: Allow Future Posting Date. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property AllowInBoundPostingWithZeroPrice() As BoYesNoEnum` [R/W] property AllowInBoundPostingWithZeroPrice
- `Public Property AllowMultipleBAOnSamePeriod() As BoYesNoEnum` [R/W] property AllowMultipleBAOnSamePeriod
- `Public Property AltNameForApInvoice() As String` [R/W] Sets or returns the alternative name for A/P invoice documents. Length: 20 characters. Field name: A/P Invoice.
  - remarks: To display the form in the application: - Select Administration --> System Initialization --> Document Numbering. - Click Name Change.
- `Public Property AltNameforCreditMemo() As String` [R/W] Sets or returns the alternative name for A/P credit memo documents. Length: 20 characters. Field name: RpcName.
  - remarks: Field name in the application: A/P Credit Memo. To display the form in the application: - Select Administration --> System Initialization --> Document Numbering. - Click Name Change.
- `Public Property AltNameForGoodsReceipt() As String` [R/W] Sets or returns the alternative name for goods receipt PO documents. Length: 20 characters. Field name: PdnName.
  - remarks: Field name in the application: Goods Receipt PO. To display the form in the application: - Select Administration --> System Initialization --> Document Numbering. - Click Name Change.
- `Public Property AltNameForGoodsReturn() As String` [R/W] Sets or returns the alternative name for goods returns documents. Length: 20 characters. Field name: RpdName.
  - remarks: Field name in the application: Goods Returns. To display the form in the application: - Select Administration --> System Initialization --> Document Numbering. - Click Name Change.
- `Public Property AltNameForPurchase() As String` [R/W] Sets or returns the alternative name for Purchase documents. Length: 20 characters. Field name: .
- `Public Property ApplicationOfIFRS() As BoYesNoEnum` [R/W] property ApplicationOfIFRS
- `Public Property ApplyBaseInactiveStatusToPeriodVolumeDiscounts() As BoYesNoEnum` [R/W] property ApplyBaseInactiveStatusToPeriodVolumeDiscounts
- `Public Property ApplyBaseInactiveStatusToPriceLists() As BoYesNoEnum` [R/W] property ApplyBaseInactiveStatusToPriceLists
- `Public Property ApplyBaseInactiveStatusToSpecialPrices() As BoYesNoEnum` [R/W] property ApplyBaseInactiveStatusToSpecialPrices
- `Public Property AutoAddPackage() As BoYesNoEnum` [R/W] Indicates whether to add all package definitions each time you create a new item, or to automatically add a new package definition to existing items. Field name: AutoAddPkg.
- `Public Property AutoAddUoM() As BoYesNoEnum` [R/W] Indicates whether to add all UoM (Unit of Measurement) group definitions each time you create a new item, or to automatically add a new UoM group definition to existing items. Field name: AutoAddUoM.
- `Public Property AutoAssignOnlyValidAPBA() As BoYesNoEnum` [R/W] property AutoAssignOnlyValidAPBA
- `Public Property AutoAssignOnlyValidARBA() As BoYesNoEnum` [R/W] property AutoAssignOnlyValidARBA
- `Public Property BankCountry() As String` [R/W] Sets or returns the country of the default house bank (the company bank) as defined in the Banks object. Length: 3 characters. Field name: BankCountr.
  - remarks: Field name in the application: Default Bank Country. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property BankStatementInstalled() As BoYesNoEnum` [R] Returns a boolean value specifying whether or not the BankStatementService is activated. Yes = service is activated (default for 2006 A new installation) No = service is not activated (default for upgraded companies).
  - remarks: To activate: Administration > System Initialization > Company Details > Basic Initialization > Install Bank Statement Process.
- `Public Property BaseField() As BoYesNoEnum` [R/W] Determines the reference number to include in the Remarks area of sales documents, whether Base Document Number (tYES) or Customer/Vendor Reference Number (tNO, in case the Customer/Vendor Reference Number does not exist in the base document, the Remarks field remains blank in the sales document). Field name: BaseFld.
  - remarks: Field name in the application: Remarks on the Documents will Include: Base Document Number or Customer/Vendor Reference Number. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab. Note: This property is replaced by the DocumentRemarksInclude property in the ExtendedAdminInfo object.
- `Public Property BlockBookkeeping() As BoYesNoEnum` [R/W] Determines whether or not to block deviation from budget in accounting transactions that involves a G/L account relevant to budget. Applicable in case the valid value of CalculateBudget is tYES and the valid value of BlockBudget is either bb_Block or bb_MonthlyAlertOnly (the system displays a warning about any deviation from budget). Field name: BdgtAcctng.
  - remarks: Field name in the application: Accounting. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Budget tab.
- `Public Property BlockBudget() As BoBlockBudget` [R/W] Determines how the system manages deviations from budget in documents. Applicable in case the valid value of CalculateBudget is tYES. Field name: BgtBlock.
  - remarks: Field name in the application: For a Document that Deviates from the Budget: - Block Deviation from Budget, - Warning, or - Without Warning. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Budget tab.
- `Public Property BlockDelNotesforPurchase() As BoYesNoEnum` [R/W] Determines whether or not to block deviation from budget in goods receipt POs. Applicable in case the valid value of CalculateBudget is tYES and the valid value of BlockBudget is either bb_Block or bb_MonthlyAlertOnly (the system displays a warning about any deviation from budget). Field name: BdgtPDNDo. LDiscTotal
  - remarks: Field name in the application: Goods Receipt Pos. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Budget tab.
- `Public Property BlockMultipleBAOnSameAPDocument() As BoYesNoEnum` [R/W] property BlockMultipleBAOnSameAPDocument
- `Public Property BlockMultipleBAOnSameARDocument() As BoYesNoEnum` [R/W] property BlockMultipleBAOnSameARDocument
- `Public Property BlockPostingDateEditing() As BoYesNoEnum` [R/W] Determines whether or not to block posting dates editing for individual rows in Journal Entry documents. Field name: RefDNoEdit.
  - remarks: Field name in the application: Block Posting Date Editing per Row. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Journal Entry. tNO - the system sets the reference date for the entire document, but the user can modify reference date for each row. tYES - the dates for each row cannot be modified.
- `Public Property BlockPurchaseOrders() As BoYesNoEnum` [R/W] Determines whether or not to block deviation from budget in purchase orders. Applicable in case the valid value of CalculateBudget is tYES and the valid value of BlockBudget is either bb_Block or bb_MonthlyAlertOnly (the system displays a warning about any deviation from budget). Field name: BdgtPORDoc.
  - remarks: Field name in the application: Purchase Orders. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Budget tab.
- `Public Property BlockStockNegativeQuantity() As BoYesNoEnum` [R/W] property BlockStockNegativeQuantity
- `Public Property BlockSystemCurrencyEditing() As BoYesNoEnum` [R/W] Determines whether or not to block editing of total amounts in system currency in Journal Entry documents. Field name: SysCNoEdit.
  - remarks: Field name in the application: Block Editing of Totals in System Currency. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Journal Entry.
- `Public Property BlockTaxDate() As BoYesNoEnum` [R/W] Determines whether or not to block document date editing per row in Journal Entry documents. Field name: TaxDNoEdit.
  - remarks: Field name in the application: Block Document Date Editing per Row. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Journal Entry.
- `Public Property BoletoFolderPath() As String` [R/W] property BoletoFolderPath
- `Public Property BPTypeCode() As String` [R/W] Determines the string length of the Payment Reference, which is used in payment slips. Country-specific for Nordic countries. Field name: CaredType.
  - remarks: To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab. The options include: <none> - (no payment reference) 01, 73 - 16 characters 04, 15, 75 - 15 characters. 71 - 0 characters (no payment reference).
- `Public Property BudgetAlert() As BoBudgetAlert` [R/W] Determines the alert type in case of deviation from budget. Applicable in case the valid value of CalculateBudget is tYES and the valid value of BlockBudget is either bb_Block or bb_MonthlyAlertOnly. Field name: BgtWarning.
  - remarks: To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Budget tab. The options include: - For Annual Budget, or - For Monthly Budget.
- `Public Property CalculateBudget() As BoYesNoEnum` [R/W] Determines whether or not to enable budget management. Field name: DoBudget.
  - remarks: Field name in the application: Budget Initialization. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Budget tab.
- `Public Property CalculateGrossProfitperTra() As BoYesNoEnum` [R/W] Determines whether or not to enable gross profit calculation for sales documents. Field name: SaleProfit.
  - remarks: The gross profit calculation in sales documents consists on the specified base price origin (PriceListforCostPrice). Field name in the application: Calculate Gross Profit. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property CalculateInWhseQtyBasedOnPostingDate() As BoYesNoEnum` [R/W] property CalculateInWhseQtyBasedOnPostingDate
- `Public Property CalculateRowDiscount() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to calculate row discount. Field name: LDiscTotal.
- `Public Property CalculateTaxinSalesQuotati() As BoYesNoEnum` [R/W] Determines whether or not to calculate tax in sales-quotation documents. When set to tNO, the system does not calculate or display the tax in quotations. however, if the user creates an order that refers to a quotation, the system calculates the tax according to the rules for the customer and the item. Field name: AddVat.
  - remarks: Field name in the application: Include Tax in Quotation. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Sales Quotation.
- `Public Property CertificateNo() As String` [R/W] Sets or returns the certificate number of the withholding tax that applies to sales documents. Applicable when SHandleWT is set to tYES. Length: 20 characters. Field name: CrtfcateNO.
  - remarks: Field name in the application: Certificate No. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determination --> Sales tab --> Tax tab. - Select Withholding Tax box.
- `Public Property ChangeDefReconAPAccounts() As BoYesNoEnum` [R/W] Determines whether or not to enable assignment of different control accounts to different vendors. Assignment of control accounts to each vendor can be done through the BusinessPartners object. The default value is tNO, which means the control accounts defined in the Control Accounts - Accounts Payable window are used for all vendors. Field name: ChCtrAPAct.
  - remarks: Field name in the application: Permit Change of Ctrl Accts. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determination --> Purchase tab --> General tab.
- `Public Property ChangeDefReconARAccounts() As BoYesNoEnum` [R/W] Determines whether or not to enable assignment of different control accounts to different customers. Assignment of control accounts to each customer can be done through the BusinessPartners object. The default value is tNO, which means the control accounts defined in the Control Accounts - Accounts Receivable window are used for all customers. Field name: ChCtrARAct.
  - remarks: Field name in the application: Permit Change of Ctrl Accts. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determination --> Sales tab --> General tab.
- `Public Property ChangedExistingOrders() As BoYesNoEnum` [R/W] Determines whether or not to allow changes to existing sales orders. The default value is tYES. If set to tNO, sales orders, once created, cannot be modified. Field name: ChangeRdr.
  - remarks: Field name in the application: Allow Changes to Existing Orders. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Sales Order.
- `Public Property ChartofAccountsTemplate() As String` [R/W] Determines the chart of accounts for the company. The available chart of accounts templates are according to the country localization. The default value is U, that means user defined chart of accounts. Modification to the template is allowed only when creating a new company database. Once the chart of accounts is applied, modification to template is not allowed. Field name: CompType.
  - remarks: Field name in the application: Chart of Accounts Template. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property CloseCountedRowsWithoutConfirmation() As BoYesNoEnum` [R/W] property CloseCountedRowsWithoutConfirmation
- `Public Property CloseCountedRowsWithZeroDifference() As BoYesNoEnum` [R/W] property CloseCountedRowsWithZeroDifference
- `Public Property Code() As Long` [R] The key for the set of administration settings. For internal use. Field name: Code
- `Public Property CommitmentRestriction() As BoYesNoEnum` [R/W] Determines whether or not to restrict the creation of sales documents for customers and prompt a warning message according to the specified MaxCommitment to the customer. The commitment limit applies to specified types of documents (A/R Invoice, Delivery, and Sales Order). Field name: ObligLimit.
  - remarks: Field name in the application: Customer Activity Restrictions - Commitment Limit. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> BP tab. The system displays a warning message in case <the customer's account balance> + <the total amount of un-deposited checks> + <the amount of the current document> exceed the customer's commitment limit.
- `Public Property CompanyColor() As Long` [R/W] Sets or returns the number of the background color for active windows. Field name: Color.
  - remarks: Field name in the application: Company Color. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab. The applicable values are: 0 - Combined 1 - Classic (default) 2 - Gray 3 - Violet 4 - Blue 5 - Green 6 - Yellow 7 - Orange 8 - Red 9 - Brown
- `Public Property CompanyName() As String` [R/W] Returns the company name (can be an abbreviation). This name appears at the top of the SAP Business One menu. However, this name is not used in printed documents. Field name: CompnyName. Length: 100 characters. Field name: CompnyName.
  - remarks: Field name in the application: Company Name. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> General tab.
- `Public Property ConsiderDelNotesinSalesR() As BoYesNoEnum` [R/W] Determines whether or not to include delivery notes - for which invoices have not yet been issued - in the total for a specified restriction. Field name: AddDlnBlnc.
  - remarks: Field name in the application: Consider Deliveries Balance. To display the form in the application: - Select Administration --> System Initialization --> General Settings--> BP tab.
- `Public Property ConsumeForecast() As BoYesNoEnum` [R/W] Determines whether to subtract (tYES) or to add (tNO) item quantities of sales orders and reverse invoices from the forecast. Field name: ConsumeFCT.
  - remarks: Field name in the application: Consume Forecast. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Planning tab.
- `Public Property ConsumptionMethod() As BoConsumptionMethod` [R/W] Sets or returns the default method for forecast consumption, either Backward-to-Forward or Forward-to-Backward. Field name: ConsumeMtd.
  - remarks: Field name in the application: Consumption Method. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Planning tab.
- `Public Property ContinuousStockManagement() As BoYesNoEnum` [R/W] Determines whether or not to manage the inventory as Perpetual Inventory. Field name: ContInvnt.
  - remarks: Field name in the application: Default Valuation Method (Perpetual Inventory Management). To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property ContinuousStockSystem() As BoInventorySystem` [R/W] Sets or returns the default inventory valuation method, either Moving Average, Standard Price, or FIFO. Applicable is case the value of ContinuousStockManagement is tYES. Field name: InvntSystm.
  - remarks: Field name in the application: Default Valuation Method (Perpetual Inventory System). To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property CopyAttachmentsFromBaseToTarget() As BoYesNoEnum` [R/W] Copy automatically attachments from base to target document. Field name: CpyBaseAtc.
  - C# example (from SAP's help):
    ```csharp
    SAPbobsCOM.CompanyService cs = oCompany.GetCompanyService();
    SAPbobsCOM.AdminInfo info = (SAPbobsCOM.AdminInfo)cs.GetAdminInfo();
    info.CopyAttachmentsFromBaseToTarget = BoYesNoEnum.tYES;
    info.CopyAttachmentsFromBOM = BoYesNoEnum.tYES;
    info.DontOverwriteAtcWithSameName = BoYesNoEnum.tYES;
    SAPbobsCOM.Documents productionOrder = SAPbobsCOM.Documents)oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oProductionOrders);
    bool success = productionOrder.GetByKey(1);
    if(success)
    {
    SAPbobsCOM.Attachments2 att = oCompany.GetBusinessObject(SAPbobsCOM.BoObjectTypes.oAttachments2); success = att.GetByKey(productionOrder.AttachmentEntry);
    att.Lines.SetCurrentLine(0);
    att.Lines.CopyToProductionOrder = BoYesNoEnum.tYES;
    }
    ```
- `Public Property CopyAttachmentsFromBOM() As BoYesNoEnum` [R/W] Copy attachments automatically from BOM to production order. Field name: CpyBomAtc.
- `Public Property CopyExchangeRateInCopyTo() As BoYesNoEnum` [R/W] Indicates whether to copy the exchange rate to the target document. Field name: CpyExhRate.
- `Public Property CopyOpenRowsToDelivery() As BoYesNoEnum` [R/W] property CopyOpenRowsToDelivery
- `Public Property CopySingleCounterToIndividualCounter() As BoYesNoEnum` [R/W] Indicates whether to copy the single counter to the individual counter (multiple counters). Field name: INCSingToV.
- `Public Property Country() As String` [R/W] Sets or returns the company Country. Field name: Country). This a foreign key to the Countries table (OCRY - not exposed through the DI API).
- `Public Property CreateAutoVATLineinJDT() As BoYesNoEnum` [R/W] Determines whether or not to calculate VAT automatically based on the VAT group defined for the account. Field name: AutoVat.
  - remarks: Field name in the application: Use Automatic VAT. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Journal Entry.
- `Public Property CreateOnlineQuotation() As BoYesNoEnum` [R/W] property CreateOnlineQuotation
- `Public Property CreditBalancewithMinusSign() As BoYesNoEnum` [R/W] Determines whether credit balances are displayed as negative (tYES) or positive (tNO) amounts for G/L accounts and business partners. The default setting is tYES. That is, credit balances for G/L accounts and business partners are displayed as negative amounts. Field name: DispPosDeb.
  - remarks: Field name in the application: Display Credit Balance with Negative Sign. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab. Note: once a journal entry has been made in SAP Business One, this setting cannot be modified.
- `Public Property CreditDepositType() As BoYesNoEnum` [R/W] Determines whether the credit vouchers are submitted automatically or manually. If credit vouchers are submitted manually, the system records the voucher date as the posting date. If credit vouchers are submitted automatically, they are entered by the system when the deposit is made, and the deposit date is recorded as the credit-voucher posting date. Field name: CreditDpst.
  - remarks: Field name in the database: CreditDpst. Field name in the application: Submit Credit Vouchers. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> BP tab.
- `Public Property CreditRestriction() As BoYesNoEnum` [R/W] Determines whether or not to restrict the creation of sales documents for customers and prompt a warning message according to the specified CreditLimit;of the customer. The credit limit applies to specified types of documents (A/R Invoice, Delivery, and Sales Order). Field name: CreditLimit.
  - remarks: Field name in the application: Customer Activity Restrictions - Credit Limit. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> BP tab.
- `Public Property CustomerIdNumber() As String` [R/W] Sets the default customer ID number (applies only when ISRType is BISR). Used by the automatic payment system in Switzerland. Field name: CustmrDdct.
  - remarks: Field name in the application: Customer's Deduction at Source. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determenation --> Sales tab --> Tax tab tab.
- `Public Property CustomersDeductionatSource() As BoYesNoEnum` [R/W] Determines whether or not to withhold tax on amounts paid by customers. Country-specfic for Israel. Field name: CustmrDdct.
  - remarks: Field name in the application: Customer's Deduction at Source. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determenation --> Sales tab --> Tax tab.
- `Public Property DataOwnershipManageBy() As BoDataOwnershipManageMethodEnum` [R/W] property DataOwnershipManageBy
- `Public Property DateSeparator() As String` [R/W] Sets the character displayed between the date fields. Field name: DateSep.
  - remarks: Field name in the application: Date Separator. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab.
- `Public Property DateTemplate() As BoDateTemplate` [R/W] Determines how dates are displayed. The setting does not affect how dates are entered. DD = day, with two digits. MM = month, with two digits. Month = month, in words. YY = year, with two digits. YYYY = year, with four digits. CCYY = year, begining with 20__ (21st century) Field name: DateFormat.
  - remarks: Field name in the application: Date Format. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab.
- `Public Property DaysBackward() As Long` [R/W] Sets or returns the number of days to go backward while searching for a forecast to consume. Field name: DaysBack.
  - remarks: Field name in the application: Days Backward. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Planning tab.
- `Public Property DaysForward() As Long` [R/W] Sets or returns the number of days to go forward while searching for a forecast to consume. Field name: DaysFwrd.
  - remarks: Field name in the application: Days Forward. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Planning tab.
- `Public Property DecimalSeparator() As String` [R/W] Determines the character that is used to separate an integer from decimals. In the U.S. and U.K., a dot is used; in German-speaking countries, a comma is generally used. Field name: DecSep.
  - remarks: Field name in the application: Decimal Places (0..6) - Separator. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab.
- `Public Property DeductionFileNo() As String` [R/W] Sets and returns the Deduction File No. Length: 50 characters. Field name: .
- `Public Property DefaultAccountCurrency() As BoYesNoEnum` [R/W] Determines whether or not default AcctCurrency is set for current account. Field name: .
- `Public Property DefaultBankAccount() As String` [R/W] Sets or returns the default BankAccount number. Field name: DflBnkAcct.
  - remarks: Field name in the application: Default Account No. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property DefaultBankAccountKey() As Long` [R/W] Sets or returns the key of the default bank account. Field name: DflBnkCode.
  - remarks: Field name in the application: Default Bank. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property DefaultBankNo() As String` [R/W] Sets or returns the default bank number. Field name: DflBnkCode.
  - remarks: Field name in the application: Decimal Places (0..6) - Default Bank. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property DefaultBranch() As String` [R] Sets or returns the default number of bank branch. Field name: DflBranch. Field name: DflBranch.
  - remarks: Field name in the application: Default Branch. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property DefaultBudgetCostAssessMt() As Long` [R/W] Sets or returns the default budget method key. Field name: BdgtDflt.
  - remarks: Field name in the application: Default Budget Key. To display the form in the application: - Select Financials --> Budget Define Budget Distribution Method --> click the Set As Default button
- `Public Property DefaultCustomerPaymentTerms() As Long` [R/W] Sets or returns the default payment terms displayed when a new customer master record is entered. Field name: DfCustTerm.
  - remarks: Field name in the application: Default Customer Payment Terms. To display the form in the application: - Select Administration --> System Initialization --> General Settings--> BP tab.
- `Public Property DefaultCustomerPriceList() As Long` [R/W] Set default Price List for Customer. Field name: DfltCustPL.
- `Public Property DefaultDunningTerm() As String` [R/W] Sets or returns the default DunningTerm displayed when a new customer master record is entered. Field name: .
- `Public Property DefaultforBatchStatus() As BoDefaultBatchStatus` [R/W] Sets or returns the default batch status. The valid values are: Released, Not Accessible, and Locked. Field name: BtchStatus.
  - remarks: Not Accessible and Locked are for information only it does not prevent from working with batches, and no warning is displayed. Field name in the application: Basic Setting for Batch Status. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Items tab.
- `Public Property DefaultTaxCode() As String` [R/W] Sets or returns the default sales tax Code. This is a foreign key to Code of the SalesTaxCodes object. Length: 8 characters. Field name: DflTaxCode.
  - remarks: Field name in the application: Default Tax Code. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property DefaultVendorPaymentTerms() As Long` [R/W] Sets or returns the default payment terms displayed when a new vendor master record is entered. Field name: DfVendTerm.
  - remarks: Field name in the application: Default Vendor Payment Terms. To display the form in the application: - Select Administration --> System Initialization --> General Settings--> BP tab.
- `Public Property DefaultVendorPriceList() As Long` [R/W] Set default Price List for Vendor. Field name: DfltVendPL.
- `Public Property DefaultWarehouse() As String` [R/W] Sets or returns the DefaultWarehouse to be used for new items. Field name: DfltWhs.
  - remarks: Field name in the application: Default Warehouse. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab.
- `Public Property DeferredTax() As BoYesNoEnum` [R/W] Determines whether or not the system allows DeferredTax. The deferred tax represents a tax on a current book year earnings that will be paid in a future year. Field name: DeferrTax.
  - remarks: Field name in the application: Deferred Tax. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property DeferredTaxforVendors() As BoYesNoEnum` [R/W] Determines whether or not the system allows the use of Deferred Tax account by Vendors. Field name: defTaxVend.
- `Public Property DirectIndirectRate() As BoYesNoEnum` [R/W] Determines the exchange rate posting: Direct or Indirect. That is, the method for calculating the amount of a transaction in local and foreign currencies. Once a journal entry is posted, this setting cannot be modified. Field name: DirectRate.
  - remarks: Field name in the application: Exchange Rate Posting - Direct/Indirect. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab. tYES - Direct rate. The system multiplies the amount in the foreign currency with the exchange rate. tNO - Indirect rate. The system divides the amount in the foreign currency with the exchange rate. For example, if the local currency is Euro and 1 Euro = $1.33 US, for direct posting the user should set an exchange rate of 1.33; for Indirect posting the user should set 0.75 (1/1.33).
- `Public Property DisplayBatchQtyUoMBy() As DisplayBatchQtyUoMByEnum` [R/W] property DisplayBatchQtyUoMBy
- `Public Property DisplayBookkeepingWindow() As BoYesNoEnum` [R/W] Determines whether or not to display account balance by control account. Field name: DspBokpWin.
  - remarks: Field name in the application: Display Accounts Balance by Control Accounts. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> BP tab.
- `Public Property DisplayCancelDocInReport() As BoYesNoEnum` [R/W] Indicates whether or not to report cancelled and cancellation documents. Field name: CmdDisBoth.
- `Public Property DisplayCurrencyontheRight() As BoYesNoEnum` [R/W] Determines on which side of an amount the currency symbol is displayed. Field name: CurOnRight.
  - remarks: Field name in the application: Display Currency on te Right. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab. tYES - the currency symbol is displayed to the right of the amount. tNO - the currency symbol is displayed to the left of the amount (default value).
- `Public Property DisplayInactivePriceListInDocuments() As BoYesNoEnum` [R/W] property DisplayInactivePriceListInDocuments
- `Public Property DisplayInactivePriceListInReports() As BoYesNoEnum` [R/W] property DisplayInactivePriceListInReports
- `Public Property DisplayInactivePriceListInSettings() As BoYesNoEnum` [R/W] property DisplayInactivePriceListInSettings
- `Public Property DisplayPriceforPriceOnly() As BoYesNoEnum` [R/W] Determines whether or not to include VAT amount in sales quotations. Field name: TreePricOn.
  - remarks: Field name in the application: Display Price for Price Only. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> BP tab.
- `Public Property DisplayRoundingRemark() As BoYesNoEnum` [R/W] Determines whether or not a note is displayed in the Remarks field of a foreign-currency invoice when the discount amount is different from the discount percentage due to rounding. Field name: RoundRmrk.
  - remarks: Field name in the application: Display Rounding Remark To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property DocConfirmation() As BoYesNoEnum` [R/W] Determines whether or not the system validates the authorization of purchase and sales documents. Field name: useDocWrf.
  - remarks: Field name in the application: Manage Document Generation Authorizations. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> BP tab.
- `Public Property DontOverwriteAtcWithSameName() As BoYesNoEnum` [R/W] Do not overwrite attachments with the same name. Field name: DnOvrwrAtc.
- `Public Property ElectronicReportInfo() As ElectronicReportInfo` [R] Setup values for electronic reports.
  - remarks: Specific to localization for France.
- `Public Property eMail() As String` [R/W] Sets or returns the default email address of the user. Length: 100 characters. Field name: E_Mail.
  - remarks: The user can override this email address by setting the eMail address in the UserDefaultGroups Object
- `Public Property EmployerReference() As String` [R/W] Sets or returns the Employer's Reference. Country-Specific for UK. Field name: EmployerRf. Length: 32 characters.
- `Public Property EnableAdvancedGLAccountDetermination() As BoYesNoEnum` [R] Whether to manage the inventory G/L account determination according to a flexible and centralized method. Field name: NewAcctDe.
  - remarks: By setting a hierarchy of rules you can assign inventory G/L accounts by: Item groups Items Warehouses Business partner groups Ship-to countries Ship to states Various combinations of all the above criteria For additional information, see the How To Setup and Work with Advanced G/L Account Determination guide in the documentation resource center.
- `Public Property EnableApprovalProcedureInDI() As BoYesNoEnum` [R/W] Determines whether or not the approval procedure is enabled in DI. Field name: EnbApprDI.
  - remarks: After the global flag EnableApprovalProcedureInDI is turned on, we strongly recommend that you call the GetNewObjectType method each time you add any document or payment to make sure that your Documents(Payments) have been added as Document(Payment) or Draft(PaymentDraft).
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    'Enable Approval Procedure flags
    Dim oAdminInfo As SAPbobsCOM.AdminInfo = oCompany.GetCompanyService().GetAdminInfo()

    oAdminInfo.EnableApprovalProcedureInDI = SAPbobsCOM.BoYesNoEnum.tYES
    oAdminInfo.DocConfirmation = SAPbobsCOM.BoYesNoEnum.tYES
    oCompany.GetCompanyService().UpdateAdminInfo(oAdminInfo)
    ```
- `Public Property EnableAuthorizerUpdatePendingDraft() As BoYesNoEnum` [R/W] property EnableAuthorizerUpdatePendingDraft
- `Public Property EnableBranches() As BoYesNoEnum` [R/W] property EnableBranches
- `Public Property EnableCentralizedIncomingPayments() As BoYesNoEnum` [R/W] property EnableCentralizedIncomingPayments
- `Public Property EnableCentralizedOutgoingPayments() As BoYesNoEnum` [R/W] property EnableCentralizedOutgoingPayments
- `Public Property EnableExternalTax() As BoYesNoEnum` [R/W] property EnableExternalTax
- `Public Property EnableMultipleSchedulings() As BoYesNoEnum` [R/W] property EnableMultipleSchedulings
- `Public Property EnablePaymentDueDates() As BoYesNoEnum` [R/W] property EnablePaymentDueDates
- `Public Property EnableSeparatePriceMode() As BoYesNoEnum` [R/W] property EnableSeparatePriceMode
- `Public Property EnableUpdateBAPriceAndPlannedAmount() As BoYesNoEnum` [R/W] property EnableUpdateBAPriceAndPlannedAmount
- `Public Property EnableUpdateDocAfterApproval() As BoYesNoEnum` [R/W] property EnableUpdateDocAfterApproval
- `Public Property EnableUpdateDraftDuringApproval() As BoYesNoEnum` [R/W] property EnableUpdateDraftDuringApproval
- `Public Property EORINumber() As String` [R/W] property EORINumber
- `Public Property ExcelFolderPath() As String` [R/W] Sets or returns the path to the Microsoft Excel documents exported from the SAP Business One application. Field name: ExcelPath. Length: 16 characters.
  - remarks: To set the Excel path in the application, go to Administration --> System Initialization --> General Settings --> Path tab.
- `Public Property ExpirationDate() As Date` [R/W] Sets or returns the expiration date of the withholding tax certificate that applies to sales documents. Applicable when SHandleWT is set to tYES. Field name: DdctExpire.
  - remarks: Field name in the database: DdctExpire. Field name in the application: Withholding Tax % - Valid Until. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determenation --> Sales tab --> Tax tab
- `Public Property ExtendedAdminInfo() As ExtendedAdminInfo` [R] Provides access to extended administration properties.
- `Public Property FaxNumber() As String` [R/W] Sets or returns the recipient fax number. Length: 50 characters. Field name: Fax.
  - remarks: See Also: Recipients Object, Users Object
- `Public Property FaxNumberForeignLang() As String` [R/W] Sets or returns the default fax number in foreign language. Field name: FaxF. Length: 50 characters.
  - remarks: See Also: UserDefaultGroups
- `Public Property FCCheckAccount() As BoCurrencyCheck` [R/W] Determines whether or not to the use of Foreign Currency Check Account is permitted. Field name: FcNoBlnc.
- `Public Property FederalTaxID() As String` [R/W] Sets or returns the main federal tax ID of the company. Length: 32 characters. See also:Documents Object, Warehouses Object, BPAddresses Object. Field name: TaxIdNum.
  - remarks: Field name in the application: Federal Tax ID 1. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property FederalTaxID2() As String` [R/W] Sets or returns the second federal tax ID (if relevant) of the company. Field name: TaxIdNum2.
  - remarks: Field name in the application: Federal Tax ID 2. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property FederalTaxID3() As String` [R/W] Sets or returns the third federal tax ID (if relevant) of the company. Field name: TaxIdNum3.
  - remarks: Field name in the application: Federal Tax ID 3. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property FileNumberinIncomeTax() As String` [R/W] Sets or returns the IRS file number of the company. Country-specfic for US only. Field name: IRSFileNo.
  - remarks: Field name in the application: Federal Tax ID 3 File Number in Income Tax. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property GeneralManager() As String` [R/W] The general manager (local). Field name: Manager1 Length: 100 characters
- `Public Property GeneralManagerForeignLanguage() As String` [R/W] The general manager (foreign language). Field name: Manager1F Length: 100 characters
- `Public Property GLMethod() As BoGLMethods` [R/W] Sets or returns a valid value of BoGLMethods type that specifies the default G/L accounts for posting transactions related to the item. source: Warehouses, ItemGroups, or specified in the item level. Field name: GLMethod.
  - remarks: Field name in the application: Set G/L Accounts by. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Items tab.
- `Public Property GrossProfitAfterSale() As BoYesNoEnum` [R/W] Determines whether or not to enable gross profit calculation for sales documents. See also CalculateGrossProfitperTra Field name: GrossBySal.
  - remarks: Field name in the application: Calculate % Gross Profit as: Profit/Sale Price or Profit/Cost Price. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property GrossProfitPercentForServiceDocuments() As Double` [R/W] The default gross profit percentage rate for calculating gross profit in sales documents of service type. Field name: GPPrcntSrv
- `Public Property GTSDefaultChecker() As Long` [R/W] property GTSDefaultChecker
- `Public Property GTSDefaultPayee() As Long` [R/W] property GTSDefaultPayee
- `Public Property GTSInboundFolder() As String` [R/W] property GTSInboundFolder
- `Public Property GTSMaxAmount() As Double` [R/W] property GTSMaxAmount
- `Public Property GTSOutboundFolder() As String` [R/W] property GTSOutboundFolder
- `Public Property GTSResponseToExceeding() As GTSResponseToExceedingEnum` [R/W] property GTSResponseToExceeding
- `Public Property GTSSeparateCode() As String` [R/W] property GTSSeparateCode
- `Public Property HolidaysName() As String` [R/W] Sets or returns a foreign key to the OHLD table that defines the holidays of one year. Field name: HldCode.
  - remarks: Field name in the application: Holidays. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property IEMandatoryValidation() As BoYesNoEnum` [R/W] property IEMandatoryValidation
- `Public Property InstitutionCode() As String` [R/W] property InstitutionCode
- `Public Property InventoryCountingHighlightCountersDifference() As Double` [R/W] property InventoryCountingHighlightCountersDifference
- `Public Property InventoryCountingHighlightMaxVariance() As Double` [R/W] property InventoryCountingHighlightMaxVariance
- `Public Property InventoryCountingHighlightVariance() As Double` [R/W] property InventoryCountingHighlightVariance
- `Public Property InventoryPostingHighlightVariance() As Double` [R/W] property InventoryPostingHighlightVariance
- `Public Property InventoryPostingReleaseOnlySerialAndBatch() As BoYesNoEnum` [R/W] property InventoryPostingReleaseOnlySerialAndBatch
- `Public Property IsPrinterConnected() As BoYesNoEnum` [R/W] property IsPrinterConnected
- `Public Property ISRBillerID() As String` [R/W] Sets or returns the ISRBillerId. (country-specific for Switzerland only). Length: 9 Characters. Field name: ISRBillerID.
  - remarks: Field name in the application: ISR Biller ID. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property IsRemoveUnpricedValue() As BoYesNoEnum` [R] property IsRemoveUnpricedValue
- `Public Property ISRType() As Long` [R/W] Sets or returns the ISRType value. (country-specific for Switzerland only). See also: UseTax Field name: ISRBillerI.
  - remarks: Field name in the database: . Field name in the application: ISR Biller ID. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data tab. Posible values are: ISR BISR ISR+ BISR
- `Public Property IssuePrimarilyBy() As IssuePrimarilyByEnum` [R/W] Specify whether you want to pick the serial or batch items for issuing according to their bin locations or their serial or batch information.
  - remarks: The field is available only if you have enabled bin locations for at least one warehouse.
- `Public Property LetterHeaderinForeignLangu() As String` [R/W] Sets or returns the header (full company name in foreign language) in printed documents. Length: 100 characters. Field name: PrintHdrF.
  - remarks: Field name in the application: Printing Header. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> General tab --> Foreign Language tab.
- `Public Property LocalCurrency() As String` [R/W] The currency of a company code (country currency) in which the local ledgers are managed. The company uses the local currency for reporting to the local tax authorities. Note: once a journal entry for an item or its master data record has been entered in SAP Business One, the local currency cannot be modified. Field name: MainCurncy.
  - remarks: Field name in the application: Local Currency. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Basic Initializatio tab.
- `Public Property ManagingDirector() As String` [R/W] Sets or returns the Managing Director's name. Length: 100 characters. Field name: Manager.
- `Public Property ManagingDirectorForeignLan() As String` [R/W] Sets or returns the Managing Director's name in Foreign Language. Field name: ManagerF. Length: 100 characters.
- `Public Property MaxDaysForCancel() As Long` [R/W] The maximum number of days for cancelling marketing documents after posting. Field name: CnclMaxDay.
  - remarks: - -1 stand for unlimited - 0 stand for cannot cancel - Positive number stand for max days
- `Public Property MaxHistory() As Long` [R/W] Determines the maximum number of records saved in the log file (default: 99). The log file saves the history of changes made in master records (items, business partners and G/L accounts) and in payments. Field name: MaxHistory.
  - remarks: Field name in the application: Local Currency. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Services tab.
- `Public Property MaximumNumberOfDaysForDueDate() As Long` [R/W] property MaximumNumberOfDaysForDueDate
- `Public Property MeasuringAccuracy() As Long` [R/W] Determines the respective number of decimal places displayed for measurment units. This setting only affects the display. The system always calculates precisely to six decimal places. Field name: MeasureDec.
  - remarks: Field name in the application: Decimal Places (0..6) - Units. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Display tab.
- `Public Property MinimumAmountfor347Report() As Double` [R/W] Sets the minimum reporting threshhold amount to include in the 347 Report. Country-specfic for Spain. Field name: MinAmnt347.
  - remarks: Field name in the application: Minimum Amount for 347 Report. To display the form in the application: - Select Administration --> System Initialization --> Company Details--> Accounting Data tab.
- `Public Property MultiCurrencyCheck() As BoCurrencyCheck` [R/W] Determines whether or not to block Multi Currency Journal Entry. Field name: MultiCurr.
  - remarks: Field name in the application: Block Multi Currency Journal Entry. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Journal Entry tab.
- `Public Property MultiLanguageSupportEnable() As BoYesNoEnum` [R/W] Determines whether or not to enable multi language support. See also: MultiLanguageTranslations. Field name: MultiCurr.
  - remarks: Field name in the application: Block Multi Currency Journal Entry. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> Per Document tab --> Journal Entry tab.
- `Public Property NationalInsuranceNo() As String` [R/W] Sets or returns the national insurance number that applies to sales documents. Applicable when SHandleWT is set to tYES. Length: 20 characters. Field name: NINum.
- `Public Property NumberOfCharInMonth() As Long` [R/W] property NumberOfCharInMonth
- `Public Property OrderBlock() As String` [R/W] Determines whether or not to block posting of documents that automatically create journal entries (invoices, credit memos, deposits, and payments). Field name: OrderBlock.
  - remarks: Field name in the application: Block Documents with Earlier Dates. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property OrderingParty() As String` [R/W] Sets the ordering party ID for the Payment Engine add-on. Field name: OrderParty.
  - remarks: Field name in the application: Block Documents with Earlier DatesOrdering Party To display the form in the application: Administration -->Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property OrganizationNumber() As String` [R/W] Determines the organization number, which is used for the payment generator (Country-specfic for some EU countries). Field name: OrgNumber Length: 100 characters
  - remarks: Field name in the application: Organization Number To display the form in the application: Administration --> System Initialization --> Company Details --> Accounting Data tab.
- `Public Property ParamFolderPath() As String` [R/W] Sets or returns the Parameters Folder Path. Field name: ParamPath. Length: 16 characters. Field name: ParamPath.
- `Public Property PBSGroupNumber() As String` [R/W] >Determines the customer group number, which is used by the PBS (Country-specific for Denmark). Field name: PBSGroupNo.
  - remarks: Field name in the application: PBS Group Number. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> General tab.
- `Public Property PBSNumber() As String` [R/W] Determines the customer identification number, which is used by the PBS. (Country-specific for Denmark.) Field name: PBSNumber.
  - remarks: Field name in the application: PBS Number. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> General tab.
- `Public Property PDefaultWTCode() As String` [R/W] Sets or returns the default withholding tax code that applies to purchase documents. This is a foreign key to WithholdingTaxCodes object. Applicable when WithholdingTax is set to tYES. Length: 4 characters. Field name: PDfltWT.
  - remarks: Field name in the application: Default WTax Code. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determination --> Purchase tab --> Tax tab. - Select Withholding Tax box.
- `Public Property PDfltITWT() As String` [R/W] Sets or returns Default Income Tax WTax Code for Purchase documents. Field name: CrdCommUse.
  - remarks: Field name in the application: Default Income Tax WTax Code. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determination --> Sales tab --> Tax tab. - Select Withholding Tax box.
- `Public Property PercentageAccuracy() As Long` [R/W] Sets or returns the percentage accuracy. Field name: PercentDec.
- `Public Property PeriodStatusAutoChange() As BoYesNoEnum` [R/W] Determines whether or not to automatically change the Period Status to 'Closing Period'. Field name: PStatAutCh.
  - remarks: To display the form in the application: Choose Administration > System Initialization > Posting Periods.
- `Public Property PeriodStatusChangeDelay() As Long` [R/W] Sets or returns the delay in days for changing the Period Status to 'Closing Period'. Applicable when the PeriodStatusAutoChange property is set to Y. Field name: PStatDelay.
- `Public Property PhoneNumber1() As String` [R/W] Sets or returns the company's first default phone number. Length: 50 characters. Field name: Phone1.
- `Public Property PhoneNumber1ForeignLang() As String` [R/W] Sets or returns the first default phone number in foreign language. Length: 50 characters. Field name: Phone1F.
- `Public Property PhoneNumber2() As String` [R/W] Sets or returns the second default phone number. Length: 50 characters. Field name: Phone2.
- `Public Property PhoneNumber2ForeignLang() As String` [R/W] Sets or returns the second default phone number in foreign language. Length: 50 characters. Field name: Phone2F.
- `Public Property PickList() As BoYesNoEnum` [R/W] Indicates whether to enforce the credit\commitment limit check when creating pick lists. Field name: PickLimit
- `Public Property PriceAccuracy() As Long` [R/W] Sets or returns the respective number of decimal places displayed for prices. This setting only affects the display. The system always calculates precisely to six decimal places. Field name: PriceDec.
  - remarks: Field name in the application: Decimal Places (0..6) - Prices. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Display tab
- `Public Property PriceListforCostPrice() As Long` [R/W] Determines the price list on which the gross profit calculation is based. Applicable when CalculateGrossProfitperTra is set to tYES. Field name: CostPrcLst.
  - remarks: Field name in the application: Base Price Origin. To display the form in the application: - Select Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property PriceProceedMethod() As PriceProceedMethodEnum` [R/W] property PriceProceedMethod
- `Public Property PriceSystem() As BoYesNoEnum` [R/W] Determines whether or not to enable selection of specific warehoses for stock revaluation. This field is applicable only ContinuousStockManagement is set to tYES. Field name: PriceSys.
  - remarks: Field name in the application: Base Price Origin. To display the form in the application: - Administration --> System Initialization --> Company Details --> Basic Initialization tab.
- `Public Property PrintingHeader() As String` [R/W] Sets or returns the header (full company name in local language) in printed documents. Length: 100 characters. Field name: PrintHeadr.
  - remarks: Field name in the application: Printing Header. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> General tab --> Local Language tab.
- `Public Property PurchaseApplyExhRatesLnWTax() As BoYesNoEnum` [R/W] Apply Purchasing Exchange Rate to WTax Field name: AplyAPExhR.
- `Public Property PurchaseLnWTax() As BoYesNoEnum` [R/W] Enable Withholding Tax in Document Rows for purchasing documents. Field name: EnAPWTLnMX.
- `Public Property PurchaseOrderConfirmed() As BoYesNoEnum` [R/W] Determines whether or not to enable drawing of purchase orders to target documents. Field name: PriceDec.
  - remarks: Field name in the application: Decimal Places (0..6) - Prices. To display the form in the application: - Select Administration -->System Initialization -->General Settings -->Display tab
- `Public Property PurchasePostPaymentCategoryLnWTax() As BoYesNoEnum` [R/W] Post Purchase Payment Category WTax. Field name: PoAPPayCat.
- `Public Property QueryAccuracy() As Long` [R/W] Determines the number of decimal places for calculated fields in queries. Field name: QueryDec.
  - remarks: Field name in the application: Decimal Places (0..6) - Decimals in Query. To display the form in the application: - Administration --> System Initialization --> General Settings --> Display tab.
- `Public Property RateAccuracy() As Long` [R/W] Determines the respective number of decimal places displayed for exchange rates. This setting only affects the display. The system always calculates precisely to six decimal places. Field name: RateDec.
  - remarks: Field name in the application: Decimal Places (0..6) - Prices. To display the form in the application: - Administration --> System Initialization --> General Settings --> Display tab.
- `Public Property RefreshInWhseQtyInDI() As BoYesNoEnum` [R/W] property RefreshInWhseQtyInDI
- `Public Property RemoveUpdatePricesBasedOnNonStandardPriceLists() As BoYesNoEnum` [R/W] property RemoveUpdatePricesBasedOnNonStandardPriceLists
- `Public Property ReportAccordingTo() As Long` [R/W] property ReportAccordingTo
- `Public Property RestrictDelNotesPO() As BoYesNoEnum` [R/W] Determines if delivery documents are blocked when a limit is applied to the customer and it has been exceeded. Field name: DlnLimit.
  - remarks: Field name in the application: Customer Activity Restrictions - Delivery Restriction. To display the form in the application: - Administration --> System Initialization --> General Settings--> BP tab.
- `Public Property RestrictOrders() As BoYesNoEnum` [R/W] Determines if orders are blocked when a limit is applied to the customer and it has been exceeded. Field name: OrderLimit.
  - remarks: Field name in the application: Customer Activity Restrictions - Delivery Restriction. To display the form in the application: - Administration --> System Initialization --> General Settings--> BP tab.
- `Public Property RestrictSales() As BoYesNoEnum` [R/W] Determines if all sales documents are blocked when a limit is applied to the customer and it has been exceeded. Field name: SalesLimit.
  - remarks: Field name in the application: Customer Activity Restrictions - Sales Restriction. To display the form in the application: - Administration --> System Initialization --> General Settings--> BP tab tab.
- `Public Property ReuseDocumentNum() As BoYesNoEnum` [R/W] property ReuseDocumentNum
- `Public Property ReuseNotaFiscalNum() As BoYesNoEnum` [R/W] property ReuseNotaFiscalNum
- `Public Property RoundingMethod() As BoYesNoEnum` [R/W] Determines whether the amounts in marketing documents are rounded by currency or by document. Field name: RoundMthd.
  - remarks: Field name in the application: Rounding Method. To display the form in the application: - Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property RoundTaxAmounts() As BoYesNoEnum` [R/W] Determines whether the amounts in marketing documents are rounded by currency or by document. Field name: RoundMthd.
  - remarks: Field name in the application: Rounding Method. To display the form in the application: - Administration --> System Initialization --> Document Settings --> General tab.
- `Public Property SalesApplyExhRatesLnWTax() As BoYesNoEnum` [R/W] Apply Sales Exchange Rate to WTax. Field name: AplyARExhR.
- `Public Property SalesLnWTax() As BoYesNoEnum` [R/W] Enable Withholding Tax in Document Rows for sales documents. Field name: EnARWTLnMX.
- `Public Property SalesOrderConfirmed() As BoYesNoEnum` [R/W] Determines whether or not to enable drawing of sales orders to target documents. Field name: RdrConfrmd.
  - remarks: Field name in the database: RdrConfrmd . Field name in the application: Sales Order Approved. To display the form in the application: - Administration --> System Initialization --> Document Settings --> Per Document tab --> Sales Order tab. Field name: .
- `Public Property SalesPostPaymentCategoryLnWTax() As BoYesNoEnum` [R/W] Post Sales Payment Category WTax. Field name: PoARPayCat.
- `Public Property SDefaultWTCode() As String` [R/W] Sets or returns the default withholding tax code that applies to sales documents. This is a foreign key to WithholdingTaxCodes object. Applicable when SHandleWT is set to tYES. Field name: SDfltWT. Length: 4 characters.
  - remarks: Field name in the application: Default WTax Code. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determination --> Sales tab --> Tax tab. - Select Withholding Tax box.
- `Public Property SDfltITWT() As String` [R/W] Sets or returns Default Income Tax WTax Code for Sales documents. Field name: CrdCommUse.
  - remarks: Field name in the application: Default WTax Code. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determination --> Sales tab --> Tax tab. - Select Withholding Tax box.
- `Public Property SEPACreditorID() As String` [R/W] property SEPACreditorID
- `Public Property Series() As Long` [R/W] property Series
- `Public Property ServiceCode() As String` [R/W] Determines whether or not to encrypt data when displaying confidential data. The data includes: G/L account balances, customer and vendor account balances, price lists, and gross profits for the transactions. When selected (Y), the system displays the Encoding Table button. The user can click this button to open the Encoding window for setting the encoding. A different display character can be defined for each character in the table. Field name: UseCode.
  - remarks: Field name in the application:Use Encryption. To display the form in the application: - Administration --> Authorizations --> General Authorizations TAB.
- `Public Property ServicePassword() As String` [R/W] Determines whether or not to encrypt data when displaying confidential data. The data includes: G/L account balances, customer and vendor account balances, price lists, and gross profits for the transactions. When set to tYES, the system displays the Encoding Table button. The user can click this button to open the Encoding window for setting the encoding. A different display character can be defined for each character in the table. Field name: UseCode.
  - remarks: Field name in the application: Use Encryption. To display the form in the application: - Administration --> Setup --> Banking --> Credit Vendors Tab.
- `Public Property SetCommissionbyCustomer() As BoYesNoEnum` [R/W] Determines whether or not to calculate commissions by customer specified in the document. Field name: CrdCommUse
  - remarks: Field name in the application: Auto. Add All Warehouses to New Items. To display the form in the application: - Administration --> System Initialization --> General Settings--> Inventory tab--> Items tab.
- `Public Property SetCommissionbyItem() As BoYesNoEnum` [R/W] Determines whether or not to calculate commision by Item. Field name: ItmCommUse.
- `Public Property SetCommissionbySE() As BoYesNoEnum` [R/W] Determines whether or not to calculate commision by sales emploee Field name: SlpCommUse.
- `Public Property SetItemsWarehouses() As BoYesNoEnum` [R/W] Determines whether or no to add all warehouses each time the user creates a new item; and automatically to add a newly defined warehouse to the existing items. Field name: AutoITW.
  - remarks: Field name in the application: Auto. Add All Warehouses to New Items. To display the form in the application: - Administration --> System Initialization --> General Settings--> Inventory tab--> Items Tab.
- `Public Property SetResourcesWarehouses() As BoYesNoEnum` [R/W] property SetResourcesWarehouses
- `Public Property SHandleWT() As BoYesNoEnum` [R/W] Determines whether or not to enable withholding tax in sales documents. Field name: SHandleWT.
  - remarks: Field name in the application: Withholding Tax. To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determination --> Sales tab --> Tax tab.
- `Public Property SirenNo() As String` [R/W] property SirenNo
- `Public Property SplitPO() As BoYesNoEnum` [R/W] Determines whether or not to split a purchase order that relates to more than one warehouse. If set to yes, the system enables to create seoarate purchase orders for each warehouse. Field name: RevisionPo.
  - remarks: Field name in the application: Split PO. To display the form in the application: - Administration --> System Initialization --> Document Settings --> Per Document tab --> Purchase Order Tab.
- `Public Property StandardUnitofLength() As Long` [R/W] Sets the default units of length measurement for items. When a new item is defined in SAP Business One, these measurement units are displayed automatically. See Also: Items. Field name: DefLengthU.
  - remarks: Field name in the application: Default Length Unit. To display the form in the application: - Administration --> System Initialization --> General Settings --> Display Tab.
- `Public Property StartingInFiscalYear() As Long` [R/W] property StartingInFiscalYear
- `Public Property State() As String` [R/W] Sets or returns the state code of the company. Field name: State. Length: 3 characters. This is a foreign key to the States table (OCST), which is not exposed through the DI API.
  - remarks: Only state codes that are defined in the States table are applicable.
- `Public Property SystemCurrency() As String` [R/W] Currency in which the system manages all transactions parallel to the local currency. If the system currency is not identical to the local currency, an exchange rate has to be defined. In Accounting, every document is posted in both the system and the local currency. Company reports than can be generated for both local and system currencies. Field name: BankCountr.
  - remarks: Field name in the application: Default Bank Country. To display the form in the application: - Administration --> System Initialization --> Company Details --> Basic Initialization Tab.
- `Public Property TaxCollection() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to collect vat tax. Field name: VatCharge.
  - remarks: Field name in the application: Tax Liable . To display the form in the application: - Administration --> System Initialization --> Company Details --> Accounting Data Tab.
- `Public Property TaxDefinition() As BoYesNoEnum` [R/W] Determines whether or not this company pays VAT. Field name: PayOutVat.
- `Public Property TaxDefinitionforVatitem() As String` [R/W] Determines the default tax group to be used when selling items. Field name: DfSVatItem.
  - remarks: Field name in the application: Sales Tax Group (Item). To display the form in the application: - Administration --> Setup --> Financials --> G/L Account Determenation --> Sales tab --> Tax Tab.
- `Public Property TaxDefinitionforVatservice() As String` [R/W] Determines the default tax group to be used when selling services. Field name: DfSVatServ.
  - remarks: Field name in the application: Saless Tax Group (Service). To display the form in the application: - Select Administration --> Setup --> Financials --> G/L Account Determenation --> Sales tab --> Tax tab.
- `Public Property TaxGroupforPurchaseItem() As String` [R/W] Determines the default tax group to be used when purchasing items. Field name: DfPVatItem.
  - remarks: Field name in the application: Purchases Tax Group (Item). To display the form in the application: - Administration --> Setup --> Financials --> G/L Account Determenation --> Purchase tab --> Tax Tab.
- `Public Property TaxGroupforServicePurchase() As String` [R/W] Determines the default tax group to be used when purchasing services. Field name: DfPVatServ.
  - remarks: Field name in the database: . Field name in the application: Purchases Tax Group (Service). To display the form in the application: - Administration --> Setup --> Financials --> G/L Account Determenation --> Purchase tab --> Tax Tab.
- `Public Property TaxOffice() As String` [R/W] Sets or returns the name of the tax authority. Field name: Revoffice.
  - remarks: Field name in the application: Sets the name of the tax authority. To display the form in the application: - Administration --> System Initialization --> Company Details --> Accounting Data Tab.
- `Public Property TaxPercentage() As Double` [R/W] Sets the percentage of tax the company is required to pay and collect. Country-specfic for Israel. Field name: VatPrcnt.
  - remarks: Field name in the application: Tax %. To display the form in the application: - Administration --> System Initialization --> Company Details --> Accounting Data Tab.
- `Public Property TaxRateDetermination() As TaxRateDeterminationEnum` [R/W] property TaxRateDetermination
- `Public Property ThousandsSeparator() As String` [R/W] Sets or returns the character that is used to separate thousands. In the U.S. and U.K., a comma is used; in German-speaking countries, a dot is generally used. Field name: ThousSep.
  - remarks: Field name in the application: Decimal Places (0..6) - Thousands Separator . To display the form in the application: - Administration --> System Initialization --> General Settings --> Display Tab.
- `Public Property TimeTemplate() As BoTimeTemplate` [R/W] Determines whether the system displays time in 12-hour or 24-hour format. Field name: TimeFormat.
  - remarks: Field name in the application:Time Format . To display the form in the application: - Administration --> System Initialization --> General Settings --> Display Tab.
- `Public Property TotalsAccuracy() As Long` [R/W] Determines the respective number of decimal places displayed for amounts. This setting only affects the display. The system always calculates precisely to six decimal places. Field name: SumDec.
  - remarks: Field name in the application:Decimal Places (0..6) - Amounts. To display the form in the application: - Administration --> System Initialization --> General Settings --> Display Tab.
- `Public Property UniqueSerialNo() As BoUniqueSerialNumber` [R/W] Determines by which value the system sets serial numbers as unique. The options are: 0 - None 2 - Manufacturer Serial Number 3 - Serial Number 4 - Lot Number Field name: SriUniqFld.
  - remarks: Field name in the database: . Field name in the application: Unique Serial Numbers by. To display the form in the application: - Select Administration --> System Initialization --> General Settings --> Inventory tab --> Itemsy tab.
- `Public Property UniqueTaxPayerReference() As String` [R/W] Sets or returns the Unique Taxpayer Reference (UTR). Country-Specific for UK. Field name: TaxPayerRf. Length: 32 characters.
- `Public Property UseDefaultPriceList() As BoYesNoEnum` [R/W] Use Default Price List. Field name: UseDfltPL.
- `Public Property UseNegativeAmounts() As BoYesNoEnum` [R/W] Determines whether to use negative amounts or a debit/credit switch in reverse transaction. This setting can be changed at any time. Field name in the database: NegAmount.
  - remarks: Field name in the application: Use Negative Amounts for Reverse Transaction. To display the form in the application: - Administration --> System Initialization --> Company Details --> Basic Initialization Tab.
- `Public Property UseParentWIPInComponents() As BoYesNoEnum` [R/W] property UseParentWIPInComponents
- `Public Property UsePASystem() As BoYesNoEnum` [R/W] Determines whether or not to create a record for purchase account in journal entries that are related to continuous stock. Note: Once a journal entries has been made, this setting cannot be changed. Field name: UsePaSys.
  - remarks: Field name in the application: Use Purchase Accounts Posting System. To display the form in the application: - Administration --> System Initialization --> Company Details --> Basic Initialization Tab.
- `Public Property UseProductionProfitAndLossAccount() As BoYesNoEnum` [R/W] The application uses the WIP accounts, inventory accounts, WIP offset accounts, and inventory offset accounts for journal entries of the component transactions between inventory and production. Field: UseProdPL.
  - remarks: For the Czech Republic, Hungary, and Slovakia localizations.
- `Public Property UserConversionCode() As BoYesNoEnum` [R/W] Determines whether or not to encrypt data when displaying confidential data. The data includes: G/L account balances, customer and vendor account balances, price lists, and gross profits for the transactions. When selected (Y), the system displays the Encoding Table button. The user can click this button to open the Encoding window for setting the encoding. A different display character can be defined for each character in the table. Field name: UseCode.
  - remarks: Field name in the application: Use Encryption. To display the form in the application: - Administration --> Authorizations --> General Authorizations Tab.
- `Public Property UseTax() As BoYesNoEnum` [R/W] Determines the fields to be printed on invoices. Used by the automatic payment system in Switzerland. The options include: ISR = with pre-printed amounts. BISR = with pre-printed amounts. ISR+ = with blank amount fields. BISR+ = with blank amount fields. Field name: ISRType.
  - remarks: Field name in the application: ISR Type. To display the form in the application: - Select Administration --> System Initialization --> Company Details --> Accounting Data Tab.
- `Public Property WeightUnitDefault() As Long` [R/W] Sets the default units of weight measurement for items in the Item Master Data form. When a new item is defined in SAP Business One, these weight units are displayed automatically. Field name: DefWeightU.
  - remarks: Field name in the application: Default Weight Unit. To display the form in the application: - Administration --> System Initialization --> General Settings --> Display Tab.
- `Public Property WholdingTaxDedHierarchy() As BoYesNoEnum` [R/W] Determines whether or not to use Withholding Tax deduction hierarch. Country specific for Israel. Field name: useDdctTrc.
  - remarks: Field name in the application: Hierarchial Deduction at Source. To display the form in the application: - Administration --> System Initialization --> Company Details --> Basic Initialization Tab.
- `Public Property WithholdingTaxDdctExpired() As Date` [R/W] Sets or returns the date when withholding tax deduction expires. Field name: DdctExpire.
- `Public Property WithholdingTaxDdctOffice() As String` [R/W] Sets or returns the withholding tax deduction office address. Length: 100 characters. Field name: DdctOffice.
- `Public Property WithholdingTaxPHandle() As String` [R/W] Determines whether or not to enable withholding tax in purchasing documents. Set this field to 'Y' or 'N'. Field name: PHandleWT Length: 1 characters.
- `Public Property WithholdingTaxTdctPercnt() As Double` [R/W] Sets or returns the withholding tax deduction percent. Field name: DdctPercnt.
- `Public Property WithholdingTaxVendorDdct() As BoYesNoEnum` [R/W] Determines wether or not vendor deduction exist. Field name: VendorDdct.
- `Public Property WithTax() As Double` [R/W] Sets the percentage of tax that must be withheld from amounts paid to the company. Field name: IncomeTax.
  - remarks: Field name in the application: Company Tax Rate. To display the form in the application, choose Administration --> System Initialization --> Company Details --> Accounting Data Tab.
- `Public Property WTAccumAmountAP() As Double` [R/W] Sets the minimum limit for posting the WTax of outgoing payments in local currency, as defined by the government. Field name: WTAccumAmt.
  - remarks: Field name in the application: Accum Amt for WTax Outgoing Payments. To display the form in the application, choose the Accounting Data tab in Administration --> System Initialization --> Company Details. Note: If the accumulated amount paid to one specific vendor within a calendar month is lower than the amount you defined in this field, the system does not post the WTax. If a certain payment causes the accumulated amount to become higher than the amount you defined in this field, the application posts WTax both for the current transaction and for the previous payments. If you cancel a payment, and the accumulated amount becomes lower than the amount you defined in this field, the application creates journal entries to reverse the following: This payment The WTax amount related to this payment The other WTax amount related to this vendor within the month
- `Public Property WTAccumAmountAR() As Double` [R/W] Sets the minimum limit for posting the WTax of incoming payments in local currency, as defined by the government. Field name: WTAccAmtAR.
  - remarks: Field name in the application: Accum Amt for WTax Incoming Payments. To display the form in the application, choose the Accounting Data tab in Administration --> System Initialization --> Company Details. Note: If the accumulated amount paid to one specific vendor within a calendar month is lower than the amount you defined in this field, the system does not post the WTax. If a certain payment causes the accumulated amount to become higher than the amount you defined in this field, the application posts WTax both for the current transaction and for the previous payments. If you cancel a payment, and the accumulated amount becomes lower than the amount you defined in this field, the application creates journal entries to reverse the following: This payment The WTax amount related to this payment The other WTax amount related to this vendor within the month
- `Public Property WTLiableExpense() As BoYesNoEnum` [R/W] Not Used. Field name: ExWTLiab.
  - remarks: Field name in the database: ExWTLiab. Field name in the application: WT Liable Expense. To display the form in the application: - N/A.
- `Public Property XMLFileFolderPath() As String` [R/W] Sets or returns the path to the XML files created with the Export Form to XML function. Field name: XmlPath
  - remarks: To set the XML path in the application, go to Administration --> System Initialization --> General Settings --> Path tab.
  - C# example (from SAP's help):
    ```csharp
    // Get the AdminInfo object
    CompanyService com_service = DICompany.GetCompanyService();
    oAdminInfo = com_service.GetAdminInfo();

    // Set Excel and XML attachment paths
    oAdminInfo.ExcelFolderPath = "c:\Excel\";
    oAdminInfo.XMLFileFolderPath = "c:\XML\";
    ```

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML data.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the XML file name including path.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AdvancedGLAccountParams (Object)

AdvancedGLAccountParams Class

## Properties (15)
- `Public Property AccountType() As InventoryAccountTypeEnum` [R/W] property AccountType
- `Public Property BPCode() As String` [R/W] property BPCode
- `Public Property FederalTaxID() As String` [R/W] property FederalTaxID
- `Public Property ItemCode() As String` [R/W] property ItemCode
- `Public Property PostingDate() As Date` [R/W] property PostingDate
- `Public Property ShipToCountry() As String` [R/W] property ShipToCountry
- `Public Property ShipToState() As String` [R/W] property ShipToState
- `Public Property UDF1() As String` [R/W] property UDF1
- `Public Property UDF2() As String` [R/W] property UDF2
- `Public Property UDF3() As String` [R/W] property UDF3
- `Public Property UDF4() As String` [R/W] property UDF4
- `Public Property UDF5() As String` [R/W] property UDF5
- `Public Property Usage() As Long` [R/W] property Usage
- `Public Property VatGroup() As String` [R/W] property VatGroup
- `Public Property Warehouse() As String` [R/W] property Warehouse

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# AdvancedGLAccountReturnParams (Object)

AdvancedGLAccountReturnParams Class

## Properties (1)
- `Public Property AccountCode() As String` [R] property AccountCode

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` method FromXMLFile
  - param `bstrFileName`: 
- `Public Sub FromXMLString(ByVal bstrXML As String)` method FromXMLString
  - param `bstrXML`: 
- `Public Function GetXMLSchema() As String` method GetXMLSchema
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` method ToXMLFile
  - param `bstrFileName`: 
- `Public Function ToXMLString() As String` method ToXMLString

# AlertManagement (Object)

AlertManagement is Data structure related to the AlertManagementService. Source table: OALT.

## Properties (19)
- `Public Property Active() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not this is Active Alert. Field name: Active.
- `Public Property AlertManagementDocuments() As AlertManagementDocuments` [R] Returns the AlertManagementDocuments object, a DataCollection that defines the Collection of documents attached to this alert.
- `Public Property AlertManagementRecipients() As AlertManagementRecipients` [R] Returns the AlertManagementRecipients object, a DataCollection that defines the Collection of recipients attached to this alert.
- `Public Property Code() As Long` [R] Returns the internal number of this alert. Field name: Code.
- `Public Property DayOfExecution() As Long` [R/W] Sets or Returns the number of days remains until the day of execution of this alert. Field name: ExecDaY.
- `Public Property ExecutionTime() As Date` [R/W] Returns the time remaining until the execution hour of this alert. Field name: ExecTime.
- `Public Property FrequencyInterval() As Long` [R/W] Returns the time unit used to define the cycle Frequency of this alert. Field name: FrqncyIntr.
- `Public Property FrequencyType() As AlertManagementFrequencyType` [R/W] Sets or returns a valid value that determines this allert frequency type. Field name: FrqncyType.
- `Public Property LastExecutionDate() As Date` [R] Returns the last Execution Date of this alert. Field name: LastDate.
- `Public Property LastExecutionTime() As Long` [R] Returns the last Execution Time of this alert. Field name: LastTIME.
- `Public Property Name() As String` [R/W] Sets or returns the Name of this Alert. Field name: Name.
- `Public Property NextExecutionDate() As Date` [R] Returns the Next Date this alert will be activated. Field name: NextDate.
- `Public Property NextExecutionTime() As Date` [R] Returns the next time this alert will be activated. Field name: NextTime.
- `Public Property Param() As String` [R/W] Sets or returns the Parameters that define this Alert. Field name: Params.
- `Public Property Priority() As AlertManagementPriorityEnum` [R/W] Sets or returns valid value for this alert Priority. Field name: Priority.
- `Public Property QueryID() As Long` [R/W] Sets or returns this query Id. Field name: QueryId.
- `Public Property SaveHistory() As BoYesNoEnum` [R/W] Determines whether or not to save history for this Alert. Field name: History.
- `Public Property Type() As AlertManagementTypeEnum` [R] Sets or returns valid value that determines whether this alert is System Alert or User Alert. Field name: Type.
- `Public Property UserFields() As Fields` [R] Get User Fields

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Exports data from the object to an XML string.

# AlertManagementDocument (Object)

AlertManagementDocument is a data structure related to the AlertManagementService. Source table: OALT.

## Properties (2)
- `Public Property Active() As BoYesNoEnum` [R/W] Determines whether or not the Alert Template Document is Active. Field name: Active.
- `Public Property Document() As AlertManagementDocumentEnum` [R/W] Sets or returns valid value of the Alert Template Document type. Field name: Document.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AlertManagementDocuments (Collection)

AlertManagementDocuments is a Data Collection of AlertManagementDocument data structures. Source table: OALT.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of AlertManagementDocument in the AlertManagementDocuments data collection. Field name: NumOfDocs.

## Methods (5)
- `Public Function Add() As AlertManagementDocument` Adds new AlertManagementDocument to the data-collection object.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As AlertManagementDocument` Returns reference to existing AlertManagementDocument in the collection by its index.
  - param `vtIndex`: Specifies the index of the new AlertManagementDocument you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# AlertManagementParams (Object)

This object specifies the identification key combination (Code, Name and Type) for which the AlertManagementService is related. Source table: OALT.

## Properties (3)
- `Public Property Code() As Long` [R/W] Sets or returns the Internal Number of this alert. Field name: Code.
- `Public Property Name() As String` [R] Sets or returns the Name of this Alert. Field name: Name. Length: 50 characters.
- `Public Property Type() As AlertManagementTypeEnum` [R/W] Sets or returns valid value that determines whether this alert is System Alert or a User Alert. Field name: Type.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AlertManagementParamsCollection (Collection)

AlertManagementParamsCollection is a Data Collection of AlertManagementParams Identification Keys. Source table: ALT1.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of AlertManagementParams in the AlertManagementRecipients data collection.

## Methods (5)
- `Public Function Add() As AlertManagementParams` Adds a new object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As AlertManagementParams` Returns a reference to the item that you want to get.
  - param `vtIndex`: Specifies the index of the collection.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AlertManagementRecipient (Object)

AlertManagementRecipient is a data structure related to the AlertManagementService and defines the properties of the AlertManagementService's recipient. Source table: ALT1.

## Properties (6)
- `Public Property Code() As Long` [R] Returns the Internal Number of this alert's Recipient. Field name: Code.
- `Public Property SendEmail() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not to alert the recipient by sending an email. Field name: SendEMail.
- `Public Property SendFax() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not to alert the recipient by sending a FAX. Field name: SendFax.
- `Public Property SendInternal() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not to alert the recipient by sending Internal message. Field name: SendIntrnl.
- `Public Property SendSMS() As BoYesNoEnum` [R/W] Sets or returns valid value that determines whether or not to alert the recipient by sending an SMS message. Field name: SendSMS.
- `Public Property UserCode() As Long` [R/W] Sets or returns the User Signature. Field name: UserSign. This is foreign key to the Users object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object's data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object's data.

# AlertManagementRecipients (Collection)

AlertManagementRecipients is a Data Collection of AlertManagementRecipient data structures. Source table: ALT1.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of instances in the data collection.

## Methods (5)
- `Public Function Add() As AlertManagementRecipient` Adds new object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As AlertManagementRecipient` Returns reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# AlertManagementService (Object)

AlertManagementService is a business object that manages alert system for SAP Business One application. This object enables you to: - Manage system and user alerts. - Manage alert's recipients. - Define event driven alerts and cyclic alerts. - Delivere alerts by the use of email, SMS or FAX. - Save the object in XML format. Source table: OALT.

**Remarks:** To use the service: - Connect to a valid company. - Call the CompanyService, which is the main DI service that you must call before using any other service. - Call the method GetBusinessService for the required service. - Create an empty data structure related to the required service. - or- You can create a data structure from an XML file or XML string. - Set the required properties of the specified data structure. - Call the required service method. To display the form in the application: Administration--Alert Management.

## Methods (7)
- `Public Function AddAlertManagement(ByVal pAlertManagement As AlertManagement) As AlertManagementParams` Creates new instance of AlertManagementParams (Code, Name and Type) Object that match the input parameter AlertManagement.
  - param `pAlertManagement`: Specifies the required AlertManagement.
  - example note: Add a user alert
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    'get alert

    Dim oAlertManagement As AlertManagement

    Dim oAlertManagementParams As AlertManagementParams

    Dim oAlertManagementRecipients As AlertManagementRecipients

    Dim oAlertRecipient As AlertManagementRecipient

    'Assuming that oAlertManagementService is already defined!

    'Get alert

    oAlertManagement  =

    oAlertManagementService.GetDataInterface(AlertManagementServiceDataInterfaces.atsdiAlertManagement)

    'set alert name

    oAlertManagement.Name = Alert1

    'set query

    oAlertManagement.QueryID = 34

    'activate the alert

    oAlertManagement.Active = BoYesNoEnum.tYES

    'set priority

    oAlertManagement .Priority = AlertManagementPriorityEnum.atp_High

    'Set the Frequency

    oAlertManagement .FrequencyInterval = 1

    ' set the Frequency type to hours

    oAlertManagement.FrequencyType = AlertManagementFrequencyType.atfi_Hours

    'get Recipients collection

    oAlertManagementRecipients = oAlertManagement.AlertManagementRecipients

    'add recipient

    oAlertRecipient = oAlertManagementRecipients.Add()

    'set recipient code(manager=1)

    oAlertRecipient.UserCode = 1

    'set internal message

    oAlertRecipient.SendInternal = BoYesNoEnum.tYES

    'add alert

    oAlertManagementParams=oAlertManagementService. AddAlertManagement (oAlertManagement )
    ```
- `Public Function GetAlertManagement(ByVal pAlertManagementParams As AlertManagementParams) As AlertManagement` Gets instance of AlertManagement Object according to AlertManagementParams (Code, Name and Type).
  - param `pAlertManagementParams`: Specifies the AlertManagementParams identification key combination (Code, Name and Type).
- `Public Function GetAlertManagementList(ByVal pAlertManagementParams As AlertManagementParams) As AlertManagementParamsCollection` Returns a AlertManagementParamsCollection object, a data collection of all the instances of AlertManagementParams Identification keys that match a given AlertManagementParams identification key (Code, Name and Type).
  - param `pAlertManagementParams`: The AlertManagementParams Identification key that function as a filter.
  - example note: Get a list of System alerts
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oAlertManagementParamsCollection As AlertManagementParamsCollection

    Dim oAlertManagementParams As AlertManagementParams

    'Assuming that oAlertManagementService is already defined!

    'get Alert Params

    oAlertManagementParams = oAlertManagementService.GetDataInterface(AlertManagementServiceDataInterfaces.atsdiAlertManagementParams)

    'set the type of the alarm to system

    oAlertManagementParams.Type = AlertManagementTypeEnum.att_System

    'get collection of system alerts

    oAlertManagementParamsCollection = oAlertManagementService.GetAlertManagementList(oAlertManagementParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As AlertManagementServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AlertManagementServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: Specifies the XML string.
- `Public Sub UpdateAlertManagement(ByVal pIAlertManagement As AlertManagement)` Update this ApprovalTemplate by another ApprovalTemplate.
  - param `pIAlertManagement`: Specifies the target ApprovalTemplate.
  - example note: Update a system alert
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    Dim oAlertManagement As AlertManagement

    Dim AlertManagementParams As AlertManagementParams

    Dim OAlertManagementRecipients As AlertManagementRecipients

    Dim oAlertRecipient As AlertManagementRecipient

    Dim j As Integer

    'Assuming that oAlertManagementService is already defined!

    'get alert params

    AlertManagementParams = oAlertManagementService.GetDataInterface(AlertManagementServiceDataInterfaces.atsdiAlertManagementParams)

    'set system alert code

    AlertManagementParams.Code = -5

    'get alert

    oAlertManagement = oAlertManagementService.GetAlertManagement(AlertManagementParams)

    oAlertManagement.Active = BoYesNoEnum.tYES

    'set % Discount

    oAlertManagement.Param = 15

    'set priority

    oAlertManagement.Priority = AlertManagementPriorityEnum.atp_High

    'choose Quotation document

    For j = 0 To oAlertManagement.AlertManagementDocuments.Count - 1

        If oAlertManagement.AlertManagementDocuments.Item(j).Document =                                   AlertManagementDocumentEnum.atd_Quotations Then

            oAlertManagement.AlertManagementDocuments.Item(j).Active =BoYesNoEnum.tYES

            Exit For

        End If

    Next j

    'get recipient collection

    OAlertManagementRecipients = oAlertManagement.AlertManagementRecipients

    'add recipient

    oAlertRecipient = oAlertManagementRecipients.Add()

    'set recipient code(manager=1)

    oAlertRecipient.UserCode = 1

    'set internal message

    oAlertRecipient.SendInternal = BoYesNoEnum.tYES

    'update system alert

    Call oAlertManagementService.UpdateAlertManagement(oAlertManagement)
    ```

# AlternateCatNum (Object)

AlternateCatNum is a business object that represents the alternative catalog numbers in the Business Partners module. This object enables you to: - Add an alternative catalog number. - Retrieve an alternative catalog number by its key. - Update an alternative catalog number. - Save the object in XML format. Source table: OSCN.

**Remarks:** Customers or vendors usually maintain their own catalog numbers for items. You can define and use these catalog numbers instead of the item numbers. Mandatory fields in SAP Business One: CardCode, ItemCode, and Substitute. To display the form in the application: - Select Inventory --> Item Management --> Batches --> Define Business Partner Catalog Numbers.

## Properties (8)
- `Public Property Browser() As DataBrowser` [R] Returns the DataBrowser object.
- `Public Property CardCode() As String` [R/W] Sets or returns the business partner identification number in SAP Business One. Field name: CardCode. Length: 15 characters. This is a foreign key to the BusinessPartners Object
  - remarks: Mandatory property. SAP Business One validates the CardCode, and if not valid, returns an error code.
- `Public Property Description() As String` [R/W] BP Catalog description. Field name: Descriptio. Length: 200 characters.
- `Public Property DisplayBPCatalogNumber() As BoYesNoEnum` [R/W] Sets or returns a valid value that determines wether or not to display business partner catalog number. Field name: ShowSCN.
- `Public Property IsDefault() As BoYesNoEnum` [R/W] The default Business Partner Catalog Number for each combination of Business Partner and Item Code. Field name: IsDefault.
  - C# example (from SAP's help):
    ```csharp
    AlternateCatNum cat = (AlternateCatNum)oCompany.GetBusinessObject(BoObjectTypes.oAlternateCatNum);
    bool res = cat.GetByKey(""I001"", ""C001"", ""sss"");
    if(res)
    cat.IsDefault = BoYesNoEnum.tYES;
    ```
- `Public Property ItemCode() As String` [R/W] Sets or returns the item code in the inventory. The item code must be unique. Mandatory property. Length: 20 characters.
  - remarks: ItemCode is the primary key of item records in SAP Business One and used to distinguish between items in the system.
- `Public Property Substitute() As String` [R/W] Sets or returns the substitute catalog number. Field name: Substitute. Length: 20 characters.
- `Public Property UserFields() As UserFields` [R] Returns the UserFields object.

## Methods (7)
- `Public Function Add() As Long` Adds a record to the object table in SAP Business One company database.
  - returns: Returns a result value that indicates success or failure. If the method succeeds, it returns 0. Otherwise, it returns an error code. You can retrieve the last error code and its description using the method GetLastError.
  - remarks: You must values for the mandatory properties, and then call the Add method. The auto-complete feature completes all the default values of the other properties. In the DI API, the auto-complete feature operates the same way as in the SAP Business One application.
- `Public Function GetAsXML() As String` Returns the object from XML data, which is stored as string in a buffer.
  - remarks: You can use this method for development technologies that do not support return value as an Out parameter, such as ASP. You do not have to set the XMLAsString property of the Company object.
- `Public Function GetByKey(ByVal ItemCode As String, ByVal CardCode As String, ByVal Substitute As String) As Boolean` Retrieves and sets the values of the object's properties by the object's absolute key from the Company database.
  - param `ItemCode`: Specifies the item key in the database.
  - param `CardCode`: Specifies the card key in the database. Specifies the identification key of the business object (CardCode).
  - param `Substitute`: Specifies the key of the replacement item in the database.
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

# AlternativeItem (Object)

A data structure object related to the AlternativeItemsService service. Source table: OALI.

## Properties (3)
- `Public Property AlternativeItemCode() As String` [R/W] Sets or returns unique ID of the alternative item.
- `Public Property MatchFactor() As Double` [R/W] Returns or sets a value specifying the matching degree of this item with the original item. A higher value represents a higher match.
- `Public Property Remarks() As String` [R/W] Returns or sets a string specifying comments to this alternative item.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name for the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# AlternativeItems (Collection)

A data collection of AlternativeItem object.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of instances in the data collection.

## Methods (6)
- `Public Function Add() As AlternativeItem` Adds new object to the collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Function Item(ByVal vtIndex As Variant) As AlternativeItem` Returns reference to an existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item you want to get.
- `Public Sub Remove(ByVal vtIndex As Variant)` Deletes the specified record from the data collection.
  - param `vtIndex`: Specifies the index of the record.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML file.
- `Public Function ToXMLString() As String` Creates XML string that represents the object data.

# AlternativeItemsService (Object)

This service manages alternative items in SAP Business One (add, delete, get by key, and update). Source table: OALI.

**Remarks:** To access Alternative Items in the application, choose Inventory > Item Management > Alternative Items.

## Methods (7)
- `Public Function AddItem(ByVal pIOriginalItem As OriginalItem) As OriginalItemParams` Adds an alternative item specified in the data structure OriginalItem (ItemCode and ItemName).
  - param `pIOriginalItem`: Specifies the alternative item data structure you want to add.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    ' Alternative Items Code Sample

    ' This sample assumes you have SBODemo_US database installed

    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim AltItemsService As SAPbobsCOM.AlternativeItemsService

    Dim OriItem As SAPbobsCOM.OriginalItem

    Dim OriItemParams As SAPbobsCOM.OriginalItemParams

    Dim AltItem As SAPbobsCOM.AlternativeItem

    oCompanyService = oCompany.GetCompanyService

    AltItemsService = oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.AlternativeItemsService)

    OriItem = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItem)

    OriItemParams = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItemParams)

    'Add 2 Alternative Items to Item A00003

    OriItem.ItemCode = "A00003" ' This item has no Alternative Items

    ' Adding first Alternative Item

    OriItem.AlternativeItems.Add()

    AltItem = OriItem.AlternativeItems.Item(0)

    AltItem.AlternativeItemCode = "A00001"

    AltItem.MatchFactor = 200

    ' Adding second Alternative Item

    OriItem.AlternativeItems.Add()

    AltItem = OriItem.AlternativeItems.Item(1)

    AltItem.AlternativeItemCode = "A00002"

    AltItem.MatchFactor = 400

    ' Adding the new Alternative Items

    OriItemParams = AltItemsService.AddItem(OriItem)
    ```
- `Public Sub DeleteItem(ByVal pIOriginalItemParams As OriginalItemParams)` Deletes the alternative item specified in data structure OriginalItemParams (ItemCode and ItemName).
  - param `pIOriginalItemParams`: Specifies the alternative item data structure you want to delete.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    ' Alternative Items Code Sample

    ' This sample assumes you have SBODemo_US database installed

    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim AltItemsService As SAPbobsCOM.AlternativeItemsService

    Dim OriItem As SAPbobsCOM.OriginalItem

    Dim OriItemParams As SAPbobsCOM.OriginalItemParams

    Dim AltItem As SAPbobsCOM.AlternativeItem

    oCompanyService = oCompany.GetCompanyService

    AltItemsService = oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.AlternativeItemsService)

    OriItem = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItem)

    OriItemParams = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItemParams)

    'Delete Alternative Item

    OriItemParams.ItemCode = "A00001"

    AltItemsService.DeleteItem(OriItemParams)
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As AlternativeItemsServiceDataInterfaces) As Object` Creates empty data structure. This means the structure contains the default setting/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `AlternativeItemsServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates data structure from specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates data structure from specified XML string.
  - param `bstrXMLString`: Specifies the XML string.
- `Public Function GetItem(ByVal pIOriginalItemParams As OriginalItemParams) As OriginalItem` Returns an instance of the data structure OriginalItem.
  - param `pIOriginalItemParams`: Specifies the properties of the data structure you want to get (ItemName and ItemCode).
- `Public Sub UpdateItem(ByVal pIOriginalItem As OriginalItem)` Replaces an alternative item with the specified OriginalItem data structure.
  - param `pIOriginalItem`: Specifies the data structure (ItemCode and ItemName) that will replace the alternative item.
  - VB example (SAP provides no C# sample for this - translate, don't paste):
    ```vb
    ' Alternative Items Code Sample

    ' This sample assumes you have SBODemo_US database installed

    Dim oCompanyService As SAPbobsCOM.CompanyService

    Dim AltItemsService As SAPbobsCOM.AlternativeItemsService

    Dim OriItem As SAPbobsCOM.OriginalItem

    Dim OriItemParams As SAPbobsCOM.OriginalItemParams

    Dim AltItem As SAPbobsCOM.AlternativeItem

    oCompanyService = oCompany.GetCompanyService

    AltItemsService = oCompanyService.GetBusinessService(SAPbobsCOM.ServiceTypes.AlternativeItemsService)

    OriItem = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItem)

    OriItemParams = AltItemsService.GetDataInterface(SAPbobsCOM.AlternativeItemsServiceDataInterfaces.aisOriginalItemParams)

    'Update Alternative Item

    OriItemParams.ItemCode = "A00001"

    OriItem = AltItemsService.GetItem(OriItemParams)

    'Getting the first alternative item

    AltItem = OriItem.AlternativeItems.Item(0)

    'Updating Alternative Item A00004 to have match factor 400

    AltItem.AlternativeItemCode = "A00004"

    AltItem.MatchFactor = 300

    AltItemsService.UpdateItem(OriItem)
    ```

# ApprovalRequest (Object)

Represents an approval request. Source table: OWDD.

## Properties (15)
- `Public Property ApprovalRequestDecisions() As ApprovalRequestDecisions` [R] Returns the ApprovalRequestDecisions object.
- `Public Property ApprovalRequestLines() As ApprovalRequestLines` [R] Returns the ApprovalRequestLines object.
- `Public Property ApprovalTemplatesID() As Long` [R] property ApprovalTemplatesID
- `Public Property Code() As Long` [R] The key for a specific approval request. Field name: WddCode.
- `Public Property CreationDate() As Date` [R] property CreationDate
- `Public Property CreationTime() As Date` [R] property CreationTime
- `Public Property CurrentStage() As Long` [R] The current approval stage. Field name: CurrStep.
- `Public Property DraftEntry() As Long` [R] property DraftEntry
- `Public Property DraftType() As String` [R] property DraftType
- `Public Property IsDraft() As String` [R] The document requiring approval is a draft document. Field name: IsDraft.
- `Public Property ObjectEntry() As Long` [R] The internal key of the document. Field name: DocEntry.
- `Public Property ObjectType() As String` [R] The type of the document. Field name: ObjType.
- `Public Property OriginatorID() As Long` [R] The document originator. Field name: OwnerID.
- `Public Property Remarks() As String` [R] Any remarks entered in the approval request. Field name: Remarks.
- `Public Property Status() As BoApprovalRequestStatusEnum` [R] Status of the approval request. Field name: Status.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ApprovalRequestDecision (Object)

ApprovalRequestDecision is a child object of the ApprovalRequest object that represents the approval decision of an approval request.

## Properties (4)
- `Public Property ApproverPassword() As String` [R/W] The password of the authorizer.
- `Public Property ApproverUserName() As String` [R/W] The user name of the authorizer.
- `Public Property Remarks() As String` [R/W] The remarks for the approval decision.
- `Public Property Status() As BoApprovalRequestDecisionEnum` [R/W] Specifies the approval decision (pending, approved, or not approved). Field name: Status.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ApprovalRequestDecisions (Collection)

A collection of ApprovalRequestDecision objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ApprovalRequestDecision` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalRequestDecision` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ApprovalRequestLine (Object)

ApprovalRequestLine is a child object of the ApprovalRequest object. Since one approval request may have more than one authorizer, each line represents the details of the approval request to the authorizer. Source table: WDD1.

## Properties (8)
- `Public Property CreationDate() As Date` [R] property CreationDate
- `Public Property CreationTime() As Date` [R] property CreationTime
- `Public Property Remarks() As String` [R] Any remarks entered by the authorizer in the approval request. Field name: Remarks.
- `Public Property StageCode() As Long` [R] The code of the approval stage. Field name: StepCode.
- `Public Property Status() As BoApprovalRequestDecisionEnum` [R] Indicates the approval decision (pending, approved, or not approved). Field name: Status.
- `Public Property UpdateDate() As Date` [R] property UpdateDate
- `Public Property UpdateTime() As Date` [R] property UpdateTime
- `Public Property UserID() As Long` [R] The user ID of the authorizer. Field name: UserID.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ApprovalRequestLines (Collection)

A collection of ApprovalRequestLine objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ApprovalRequestLine` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalRequestLine` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ApprovalRequestParams (Object)

Holds the key, remarks, and status of an approval request. This object is used to pass keys to and retrieve keys from ApprovalRequestsService methods. Source table: OWDD.

## Properties (3)
- `Public Property Code() As Long` [R/W] The key for a specific approval request. Field name: WddCode.
- `Public Property Remarks() As String` [R] Any remarks entered in the approval request. Field name: Remarks.
- `Public Property Status() As BoApprovalRequestStatusEnum` [R] Returns a value specifying the approval request status. Field name: Status.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Sets the object's properties using data from an XML file. The XML file can be created using the object's ToXMLFile method.
  - param `bstrFileName`: The path and name of the XML file from which to retrieve the object's data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Sets the object's properties using data from an XML string. The XML string can be created using the object's ToXMLString method.
  - param `bstrXML`: The XML from which to retrieve the object's data.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ApprovalRequestsParams (Collection)

A collection of ApprovalRequestParams objects.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of objects in the collection.

## Methods (5)
- `Public Function Add() As ApprovalRequestParams` Adds an empty object to the collection.
  - remarks: After an object is added to this collection, the database is not automatically updated. You must then update the GeneralData object to which this collection belongs, by executing the Update method of the GeneralService service.
- `Public Function GetXMLSchema() As String` Returns the XML schema for the XML generated by the ToXMLFile and ToXMLString methods.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalRequestParams` Returns the object at the specified index.
  - param `vtIndex`: The index of the object to be returned (0-based)
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object.
  - param `bstrFileName`: The path and file name of the XML file.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.
- `Public Function ToXMLString() As String` Creates and returns an XML string that represents the object.
  - remarks: The schema of the XML can be retrieved with the GetXMLSchema method.

# ApprovalRequestsService (Object)

ApprovalRequestsService is a business object that manages the approval requests process in the SAP Business One environment. This object enables users to do the following: - Get an approval request from the approval process. - Get a list of approval requests from the approval process. - Get a list of open approval requests from the approval process. - Update an approval request within the approval process. - Get data interfaces. Source table: OWDD.

**Remarks:** From the SAP Business One application, you can do the following: Approve draft documents in the Request for Approval window when you are reviewing messages in the Messages/Alert Overview window. Approve draft documents in the Approval Decision Report window when you generate a report of the status of draft documents requiring approval. Approving draft documents from the Request for Approval window: - Choose Window --> Messages/Alert Overview. The Messages/Alert Overview window appears. - To display the details of the message in the Request for Document Approval area, select the required message. To open the Request for Approval window, click the link arrow. In the Decision list, select your decision for the approval request. Choose the Update button. An internal message is sent to the document originator regarding the approval. Approving draft documents from the Approval Decision Report window: Choose Administration --> Approval Procedures --> Approval Decision Report. The Approval Decision Report - Selection Criteria window appears. To generate the report, choose the required criteria. Choose the OK button. The Approval Decision Report window appears. In the Answer column, select your decision for the approval request. Choose the Update button. An internal message is sent to the document originator regarding the approval.

**Example:**
- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
  ```vb
  Dim oApprovalRequestsService As ApprovalRequestsService = oCompany.GetCompanyService().GetBusinessService(ServiceTypes.ApprovalRequestsService)
  Dim oApprovalRequest As ApprovalRequest = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequest)
  Dim oApprovalRequestParams As ApprovalRequestParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestParams)

  oApprovalRequestParams.Code = indexNum ' The approval index

  ' Get approval request details
  oApprovalRequest = oApprovalRequestsService.GetApprovalRequest(oApprovalRequestParams)

  txtDocType.Text = oApprovalRequest.ObjectType
  txtDocNo.Text = oApprovalRequest.ObjectEntry
  txtUser.Text = oApprovalRequest.OriginatorID.ToString
  txtCurrStage.Text = oApprovalRequest.CurrentStage
  txtRemarks.Text = oApprovalRequest.ApprovalRequestLines.Item(0).Remarks

  ' Get draft document
  Dim oDraft As Documents = oCompany.GetBusinessObject(BoObjectTypes.oDrafts)

  If oApprovalRequest.ObjectType = 112 Then
      oDraft.GetByKey(oApprovalRequest.ObjectEntry)

      'Get actual document type.
      txtRealDocType.Text = oDraft.DocObjectCode
          End If
  ```
- VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
  ```vb
  Dim oApprovalRequestsService As ApprovalRequestsService = oCompany.GetCompanyService().GetBusinessService(ServiceTypes.ApprovalRequestsService)
  Dim oApprovalRequestsParams As ApprovalRequestsParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestsParams)
  Dim oApprovalRequest As ApprovalRequest = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequest)
  Dim oApprovalRequestParams As ApprovalRequestParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestParams)

  'Get request list
  oApprovalRequestsParams = oApprovalRequestsService.GetAllApprovalRequestsList()
  oApprovalRequestParams = oApprovalRequestsParams.Item(oApprovalRequestsParams.Count - 1)

  'Approve request
  oApprovalRequest = oApprovalRequestsService.GetApprovalRequest(oApprovalRequestParams)
  oApprovalRequest.ApprovalRequestDecisions.Add()
  oApprovalRequest.ApprovalRequestDecisions.Item(0).Remarks = "Approved"
  oApprovalRequest.ApprovalRequestDecisions.Item(0).Status = BoApprovalRequestStatusEnum.arsApproved

  ' Incase we want to approve with another user, uncomment the following 2 lines
  'oApprovalRequest.ApprovalRequestDecisions.Item(0).ApproverUserName = B1User
  'oApprovalRequest.ApprovalRequestDecisions.Item(0).ApproverPassword = B1Password

  Try
      oApprovalRequestsService.UpdateRequest(oApprovalRequest)
  Catch ex As Exception
      MessageBox.Show(ex.Message)
  End Try
  ```

## Methods (10)
- `Public Sub CancelApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams)` CancelApprovalRequest
  - param `pIApprovalRequestParams`: 
- `Public Function GetAllApprovalRequestsList() As ApprovalRequestsParams` Returns all approval requests in your company.
  - VB example (SAP's help labels this C#, but it is Visual Basic - translate before use):
    ```vb
    'Get full list of approval request
    Dim oApprovalRequestsService As ApprovalRequestsService = oCompany.GetCompanyService().GetBusinessService(ServiceTypes.ApprovalRequestsService)
    Dim oApprovalRequest As ApprovalRequest = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequest)
    Dim oApprovalRequestsParams As ApprovalRequestsParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestsParams)
    Dim oApprovalRequestParams As ApprovalRequestParams = oApprovalRequestsService.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestParams)

    'Get full list
    oApprovalRequestsParams = oApprovalRequestsService.GetAllApprovalRequestsList()

    Dim i As Integer
    Dim approvalcode As Integer
    Dim sRemarks, sXML, sStatus As String
    Dim sReqStatus As SAPbobsCOM.BoApprovalRequestStatusEnum

    For i = 0 To oApprovalRequestsParams.Count - 1

        ' Get request information in order to find the request you want to approve
        approvalcode = oApprovalRequestsParams.Item(i).Code
        sRemarks = oApprovalRequestsParams.Item(i).Remarks
        sReqStatus = oApprovalRequestsParams.Item(i).Status

        sStatus = ""
        Select Case sReqStatus
            Case BoApprovalRequestStatusEnum.arsApproved
                sStatus = "Approved"
            Case BoApprovalRequestStatusEnum.arsCancelled
                sStatus = "Cancelled"
            Case BoApprovalRequestStatusEnum.arsGenerated
                sStatus = "Approved"
            Case BoApprovalRequestStatusEnum.arsGeneratedByAuthorizer
                sStatus = "GeneratedByAuthorizer"
            Case BoApprovalRequestStatusEnum.arsNotApproved
                sStatus = "NotApproved"
            Case BoApprovalRequestStatusEnum.arsPending
                sStatus = "Pending"
        End Select
        sXML = oApprovalRequestsParams.Item(i).ToXMLString

    Next
    ```
- `Public Function GetApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams) As ApprovalRequest` Retrieves an ApprovalRequest. The approval request is specified by its key (WddCode), which is contained in the ApprovalRequestParams object passed to the method.
  - param `pIApprovalRequestParams`: The ApprovalRequestParams of the ApprovalRequest you want to get.
- `Public Function GetApprovalRequestList() As ApprovalRequestsParams` Returns approval requests of the logged-on user as authorizer.
  - C# example (from SAP's help):
    ```csharp
    ApprovalRequestsService approvalSrv = MainModule.oCmpSrv.GetBusinessService(ServiceTypes.ApprovalRequestsService) As ApprovalRequestsService;
    ApprovalRequestsParams oList = approvalSrv.GetApprovalRequestList();
    String result = "";
    foreach (ApprovalRequestParams oParams In oList)
    {
      result += oParams.Code + " " + oParams.Remarks + " " + oParams.Status + "\n";
    }
    Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    ```
- `Public Function GetDataInterface(ByVal enumMSDI As ApprovalRequestsServiceDataInterfaces) As Object` Creates an empty data structure. This means the structure contains the default settings/values of the database.
  - param `enumMSDI`: one of the enumeration's values (see the enum file)
  - enum: `ApprovalRequestsServiceDataInterfaces` in `../enums/enums-01.md`
- `Public Function GetDataInterfaceFromXMLFile(ByVal bstrFileName As String) As Object` Creates a data structure from a specified XML file.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function GetDataInterfaceFromXMLString(ByVal bstrXMLString As String) As Object` Creates a data structure from a specified XML string.
  - param `bstrXMLString`: Specifies the XML String.
- `Public Function GetOpenApprovalRequestList() As ApprovalRequestsParams` Returns the open approval requests of the logged-on user as authorizer.
  - returns: Returns the ApprovalRequestsParams object, a DataCollection of ApprovalRequestParams data structures.
  - C# example (from SAP's help):
    ```csharp
    ApprovalRequestsService approvalSrv = MainModule.oCmpSrv.GetBusinessService(ServiceTypes.ApprovalRequestsService) As ApprovalRequestsService;
    ApprovalRequestsParams oList = approvalSrv.GetOpenApprovalRequestList();
    String result = "";

    foreach (ApprovalRequestParams oParams In oList)
    {
      result += oParams.Code + " " + oParams.Remarks + "\n";
    }
    Interaction.MsgBox(result, (Microsoft.VisualBasic.MsgBoxStyle)(0), null);
    ```
- `Public Sub RestoreApprovalRequest(ByVal pIApprovalRequestParams As ApprovalRequestParams)` RestoreApprovalRequest
  - param `pIApprovalRequestParams`: 
- `Public Sub UpdateRequest(ByVal pIApprovalRequest As ApprovalRequest)` Reply this ApprovalRequest with the approval decision.
  - param `pIApprovalRequest`: The target ApprovalRequest Object.
  - C# example (from SAP's help):
    ```csharp
    ApprovalRequestsService approvalSrv = MainModule.oCmpSrv.GetBusinessService(ServiceTypes.ApprovalRequestsService) As ApprovalRequestsService;
    ApprovalRequestParams oParams = approvalSrv.GetDataInterface(ApprovalRequestsServiceDataInterfaces.arsApprovalRequestParams) As ApprovalRequestParams;
    oParams.Code = 1;
    ApprovalRequest oData = approvalSrv.GetApprovalRequest(oParams);

    //Add an approval decision
      oData.ApprovalRequestDecisions.Add();
      oData.ApprovalRequestDecisions.Item(0).ApproverUserName = "manager";
      oData.ApprovalRequestDecisions.Item(0).ApproverPassword = "manager";
      oData.ApprovalRequestDecisions.Item(0).Status = BoApprovalRequestDecisionEnum.ardApproved;
      oData.ApprovalRequestDecisions.Item(0).Remarks = "ok";

    //Update the approval request
      approvalSrv.UpdateRequest(oData);
    ```

# ApprovalStage (Object)

ApprovalStage is a Data structure related to the ApprovalStagesService. Source table: OWST.

## Properties (5)
- `Public Property ApprovalStageApprovers() As ApprovalStageApprovers` [R] Returns the ApprovalStageApprovers object, a DataCollection of ApprovalStageApprover data structures.
- `Public Property Code() As Long` [R] Returns this approval stage code. Field name: WstCode. This is a key to the ApprovalStage Object.
- `Public Property Name() As String` [R/W] Sets or returns the stage approver's name. Field name: Name. Length: 20 characters.
- `Public Property NoOfApproversRequired() As Long` [R/W] Returns the No. of authorizes required for this Approval Stage. Field name: MaxReqr.
- `Public Property Remarks() As String` [R/W] Sets or returns the Description of this approval stage. Field name: Remarks. Length: 100 characters.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Imports data from an XML file to the object.
  - param `bstrFileName`: Specifies the the XML file.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalStageApprover (Object)

ApprovalStageApprover is a Data structure that define the user Id of the ApprovalStage approver. Source table: WST1.

## Properties (1)
- `Public Property UserID() As Long` [R/W] Sets or returns the approver User code. Field name: UserID. This is a foreign key to the Users object.

## Methods (5)
- `Public Sub FromXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Sub FromXMLString(ByVal bstrXML As String)` Imports data from an XML string to the object.
  - param `bstrXML`: Specifies the the XML string.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the data structure.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.

# ApprovalStageApprovers (Collection)

ApprovalStageApprovers is a Data Collection of ApprovalStageApprover data structures.

## Properties (1)
- `Public Property Count() As Long` [R] Returns the number of ApprovalStageApprover data structures, in the ApprovalStageApprovers data collection.

## Methods (5)
- `Public Function Add() As ApprovalStageApprover` Adds a new ApprovalStageApprover to the ApprovalStageApprovers Data Collection.
- `Public Function GetXMLSchema() As String` Retrieves the XML schema of the ApprovalStageApprover data structure.
- `Public Function Item(ByVal vtIndex As Variant) As ApprovalStageApprover` Returns reference to existing item in the collection by its index.
  - param `vtIndex`: Specifies the index of the item that you want to get.
- `Public Sub ToXMLFile(ByVal bstrFileName As String)` Creates an XML file that represents the object data.
  - param `bstrFileName`: Specifies the path and file name of the XML data.
- `Public Function ToXMLString() As String` Creates an XML string that represents the object data.
