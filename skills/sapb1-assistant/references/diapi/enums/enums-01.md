<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# AccountCategoryServiceDataInterfaces (Enumeration)

AccountCategoryService data interfaces.

| Member | Value | Description |
|---|---|---|
| acsAccountCategory | 0 | AccountCategory data interface |
| acsAccountCategoriesParams | 1 | AccountCategoriesParams data interface |
| acsAccountCategoryParams | 2 | AccountCategoryParams data interface |

# AccountCategorySourceEnum (Enumeration)

Methods for linking accounts to categories.

| Member | Value | Description |
|---|---|---|
| acsBalanceSheet | 0 | Accounts from the Assets, Liabilities and Equity drawers are linked by default to the Balance Sheet category. |
| acsProfitAndLoss | 1 | Accounts located in the other drawers are linked to the Profit and Loss category. |
| acsTrialBalance | 2 |  |

# AccountSegmentationTypeEnum (Enumeration)

Data types for account segments.

| Member | Value | Description |
|---|---|---|
| ast_Alphanumeric | 0 | Alphanumeric. |
| ast_Numeric | 1 | Numeric. |

# AccountsServiceDataInterfaces (Enumeration)

AccountsService data interfaces.

| Member | Value | Description |
|---|---|---|
| asdiOpenningBalanceAccount | 0 | OpeningBalanceAccount data interface |
| asdiGLAccounts | 1 | GLAccounts data interface |

# AccrualTypesServiceDataInterfaces (Enumeration)

AccrualTypesService data interfaces.

| Member | Value | Description |
|---|---|---|
| atsAccrualType | 0 | AccrualType data interface |
| atsAccrualTypesParams | 1 | AccrualTypesParams data interface |
| atsAccrualTypeParams | 2 | AccrualTypeParams data interface |

# AcquisitionPeriodControlEnum (Enumeration)

Specify how the acquisition of an asset determines the asset's depreciation start date.

| Member | Value | Description |
|---|---|---|
| apcProRataTemporis | 0 | Specify one of the PR Temporis Type to determine the depreciation start date. |
| apcFirstYearConvention | 1 | Determines the depreciation start date as follows: When your fiscal year matches a calendar year: If the asset acquisition takes place before July 1st, the depreciation starts from January 1st. If the asset acquisition takes place after July 1st, the depreciation starts from July 1st. When your fiscal year does not match a calendar year: If the asset acquisition takes place in the first half of the fiscal year, the depreciation starts from the first day of the first half of the year. If the asset acquisition takes place in the second half of the fiscal year, the depreciation starts from the first day of the second half of the year. |
| apcHalfYear | 2 | The depreciation of the asset always starts from the first day of the second half of the fiscal year during which the asset acquisition takes place. |
| apcFullYear | 3 | The depreciation of the asset always starts from the first day of the fiscal year during which the asset acquisition takes place. |

# AcquisitionProRataTypeEnum (Enumeration)

Specify one of the PR Temporis Type to determine the depreciation start date.

| Member | Value | Description |
|---|---|---|
| aprtExactlyDailyBase | 0 | The depreciation of the asset starts from the day of the asset acquisition. |
| aprtFirstDayOfCurrentPeriod | 1 | The depreciation of the asset starts from the first day of the posting period within which the asset acquisition takes place. |
| aprtFirstDayOfNextPeriod | 2 | The depreciation of the asset starts from the first day of the posting period that follows the period of asset acquisition. |

# ActivitiesServiceDataInterfaces (Enumeration)

ActivitiesService data interfaces.

| Member | Value | Description |
|---|---|---|
| asActivity | 0 | Activity data interface |
| asActivitiesParams | 1 | ActivitiesParams data interface |
| asActivityParams | 2 | ActivityParams data interface |
| asActivityInstancesParams | 3 | ActivityInstancesParams data interface |
| asActivityInstanceParams | 4 | ActivityInstanceParams data interface |
| asActivityInstancesListParams | 5 |  |

# ActivityRecipientListsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| arlsdiActivityRecipientList | 0 |  |
| arlsdiActivityRecipientListParams | 1 |  |
| arlsdiActivityRecipientListParamsCollection | 2 |  |
| arlsdiActivityRecipient | 3 |  |
| arlsdiActivityRecipientCollection | 4 |  |

# ActivityRecipientObjTypeEnum (Enumeration)

Type of the recipient.

| Member | Value | Description |
|---|---|---|
| arotUser | 0 | User |
| arotEmployee | 1 | Employee |
| arotRecipientList | 2 | Recipient list |

# ActivitySubjectServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| assActivitySubject | 0 |  |
| assActivitySubjectsParams | 1 |  |
| assActivitySubjectParams | 2 |  |

# AddressServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| asAddressFormat | 0 | AddressFormat data interface |
| asAddressFormatParamsCollection | 1 | AddressFormatParamsCollection data interface |
| asAddressFormatParams | 2 | AddressFormatParams data interface |
| asAddressParams | 3 | AddressParams data interface |
| asAddressReturnParams | 4 | AddressReturnParams data interface |

# AlertManagementDocumentEnum (Enumeration)

Alert management document types.

| Member | Value | Description |
|---|---|---|
| atd_NOB | 0 | NOB |
| atd_Invoices | 1 | Invoice document |
| atd_RevertInvoice | 2 | Revert Invoice Document |
| atd_DeliveryNotes | 3 | Delivery Notes Document |
| atd_Returns | 4 | Returns document. |
| atd_Orders | 5 | Orders Document |
| atd_PurchaseInvoices | 6 | Purchases Invoice Document |
| atd_PurchaseDeliveryNotes | 7 | Purchase Delivery Notes Document |
| atd_PurchaseOrders | 8 | Purchase Orders Document |
| atd_Quotations | 9 | Quotations Document. |
| atd_IncomingPayments | 10 | Quotations Document. |
| atd_JournalEntries | 11 | Journal Entries Document. |
| atd_OutgoingPayments | 12 | Outgoing payments Document. |
| atd_ChecksForPayment | 13 | Checks for payment Document. |
| atd_CorrectionInvoice | 14 | Correction Invoice Document |
| atd_DownPaymentIncoming | 15 | Down payment incoming Document. |
| atd_DownPaymentOutgoing | 16 | Down payment outgoing Document. |

# AlertManagementFrequencyType (Enumeration)

Frequencies for alerts.

| Member | Value | Description |
|---|---|---|
| atfi_Minutes | 0 | Minutes frequency type. |
| atfi_Hours | 1 | Hours frequency type. |
| atfi_Days | 2 | Days frequency type. |
| atfi_Weeks | 3 | Weeks frequency type. |
| atfi_Monthly | 4 | Monthly frequency type. |

# AlertManagementPriorityEnum (Enumeration)

Priorities for alerts.

| Member | Value | Description |
|---|---|---|
| atp_Low | 0 | Low Priority type. |
| atp_Normal | 1 | Normal Priority type. |
| atp_High | 2 | High Priority type. |

# AlertManagementServiceDataInterfaces (Enumeration)

AlertManagementService data interfaces.

| Member | Value | Description |
|---|---|---|
| atsdiAlertManagement | 0 | AlertManagement data interface |
| atsdiAlertManagementParams | 1 | AlertManagementParams data interface |

# AlertManagementTypeEnum (Enumeration)

Types of alerts.

| Member | Value | Description |
|---|---|---|
| att_User | 0 | User alert management type. |
| att_System | 1 | System alert management type. |

# AlternativeItemsServiceDataInterfaces (Enumeration)

AlternativeItemsService data interfaces.

| Member | Value | Description |
|---|---|---|
| aisOriginalItem | 0 | OriginalItem data interface |
| aisOriginalItemParams | 1 | OriginalItemParams data interface |

# AmountCatTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| act_Open | 0 |  |
| act_Invoiced | 1 |  |

# ApprovalRequestsServiceDataInterfaces (Enumeration)

ApprovalRequestsService data interfaces.

| Member | Value | Description |
|---|---|---|
| arsApprovalRequest | 0 | ApprovalRequest data interfaces |
| arsApprovalRequestsParams | 1 | ApprovalRequestsParams data interfaces |
| arsApprovalRequestParams | 2 | ApprovalRequestParams data interfaces |

# ApprovalStagesServiceDataInterfaces (Enumeration)

ApprovalStagesService data interfaces.

| Member | Value | Description |
|---|---|---|
| assdiApprovalStageParams | 0 | ApprovalStageParams data interface |
| assdiApprovalStage | 1 | ApprovalStage data interface |

# ApprovalTemplateConditionTypeEnum (Enumeration)

Approval template conditions.

| Member | Value | Description |
|---|---|---|
| atctUndefined | 0 | Undefined condition type. |
| atctDeviationFromCreditLine | 1 | Deviation from credit line condition type. |
| atctDeviationFromObligo | 2 | Deviation from obligo condition type. |
| atctGrossProfitPercent | 3 | Gross profit percent condition type. |
| atctDiscountPercent | 4 | Discount percent condition type. |
| atctDeviationFromBudget | 5 | Deviation from budget condition type. |
| atctTotalDocument | 6 | Total document condition type. |
| atctItemCode | 7 | Item code condition type |
| atctTotalLine | 8 | Line total condition type |
| atctCountedQuantity | 9 | Counted quantity for Inventory Counting and Inventory Posting condition type |
| atctQuantity | 10 | Quantity condition type for Opening Balance |
| atctVariance | 11 | Variance condition type |
| atctVariancePercent | 12 | Variance percent condition type |

# ApprovalTemplateOperationTypeEnum (Enumeration)

Logical operations for defining the deviation that initiates an approval template.

| Member | Value | Description |
|---|---|---|
| opcodeUndefined | 0 | Undefined deviation. |
| opcodeGreaterThan | 1 | Value was greater then limit. |
| opcodeGreaterOrEqual | 2 | Value was greater then or equal to limit. |
| opcodeLessThan | 3 | Value was less then limit. |
| opcodeLessOrEqual | 4 | Value was less or equal then limit. |
| opcodeEqual | 5 | Value was equal to limit. |
| opcodeDoesNotEqual | 6 | Value was not equal to limit. |
| opcodeInRange | 7 | Value was within limitions range. |
| opcodeNotInRange | 8 | Value was outside limitions range. |

# ApprovalTemplatesDocumentTypeEnum (Enumeration)

Document types that initiate an approval template.

| Member | Value | Description |
|---|---|---|
| atdtQuotation | 23 | Quotation type document |
| atdtOrder | 17 | Order type document |
| atdtDelivery | 15 | Delivery type document |
| atdtReturns | 16 | Returns type document |
| atdtArDownPayment | 203 | A/R down payment type document |
| atdtArInvoice | 13 | A/R invoice type document |
| atdtArCreditMemo | 14 | Credit memo type document |
| atdtCorrectionInvoice | 132 | Correction invoice type document |
| atdtPurchaseOrder | 22 | Purchase order type document |
| atdtGoodsReceiptPO | 20 | Goods receipt PO type document |
| atdtGoodsReturns | 21 | Goods returns type document |
| atdtApDownPayment | 204 | A/P down payment type document |
| atdtApInvoice | 18 | A/P invoice type document |
| atdtApCreditMemo | 19 | A/P credit memo type document |
| atdtGoodsReceipt | 59 | Goods receipt type document |
| atdtGoodsIssue | 60 | Goods issue type document |
| atdtInventoryTransfer | 67 | Inventory transfer type document |
| atdtPurchaseQuotation | 540000006 | Purchase quotation type document |
| atdtInventoryTransferRequest | 1250000001 | Inventory transfer request type document |
| atdtOutgoingPayment | 46 | Outgoing payment type document |
| atdtInventoryCounting | 1470000065 | Inventory counting document |
| atdtInventoryPosting | 10000071 | Inventory posting document |
| atdtInventoryOpeningBalance | 310000001 | Inventory opening balance document |
| atdtReturnRequest | 234000031 |  |
| atdtGoodsReturnRequest | 234000032 |  |
| atdtBlanketAgreement | 1250000025 |  |
| atdtSalesBlanketAgreement | 1250000026 |  |
| atdtPurchaseBlanketAgreement | 1250000027 |  |
| atdtPurchaseRequest | 1470000113 |  |

# ApprovalTemplatesServiceDataInterfaces (Enumeration)

ApprovalTemplateUsers data interfaces.

| Member | Value | Description |
|---|---|---|
| atsdiApprovalTemplate | 0 | ApprovalTemplate data interface |
| atsdiApprovalTemplateParams | 1 | ApprovalTemplateParams data interface |

# AreaTypeEnum (Enumeration)

The types for the depreciation area.

| Member | Value | Description |
|---|---|---|
| atPostingtoGL | 0 | In this area, the asset depreciation is posted to the general ledger accounts. |
| atAdditionalArea | 1 | In this area, the asset depreciation is not posted to the general ledger accounts. The depreciation carried out in this area is for information purposes only. |
| atDerivedArea | 2 | The derived area of the main depreciation area. Generally, you use this area when carrying out special depreciation. SAP Business One lets you create only one depreciation area with the Derived Area type. |

# AssesseeTypeEnum (Enumeration)

A type of nature of assessee that is subject to TDS (withholding tax).

| Member | Value | Description |
|---|---|---|
| atCompany | 0 | Company |
| atOthers | 1 | Other |

**Remarks:** For India only. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.

# AssetClassesServiceDataInterfaces (Enumeration)

AssetClassesService data interfaces.

| Member | Value | Description |
|---|---|---|
| acsAssetClass | 0 | AssetClass data interface |
| acsAssetClassParamsCollection | 1 | AssetClassParamsCollection data interface |
| acsAssetClassParams | 2 | AssetClassParams data interface |

# AssetDepreciationGroupsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| adgsAssetDepreciationGroup | 0 |  |
| adgsAssetDepreciationGroupParamsCollection | 1 |  |
| adgsAssetDepreciationGroupParams | 2 |  |

# AssetDocumentServiceDataInterfaces (Enumeration)

AssetDocumentService data interfaces.

| Member | Value | Description |
|---|---|---|
| adsAssetDocument | 0 | AssetDocument data interface |
| adsAssetDocumentParamsCollection | 1 | AssetDocumentParamsCollection data interface |
| adsAssetDocumentParams | 2 | AssetDocumentParams data interface |

# AssetDocumentStatusEnum (Enumeration)

The status of the asset document.

| Member | Value | Description |
|---|---|---|
| adsPosted | 0 | Indicates the asset document is created. |
| adsDraft | 1 |  |
| adsCancelled | 2 | Indicates the asset document is cancelled. |

# AssetDocumentTypeEnum (Enumeration)

The transaction type of the asset document.

| Member | Value | Description |
|---|---|---|
| adtOrdinaryDepreciation | 0 | Ordinary depreciation includes the planned ordinary depreciation and the manual ordinary depreciation. The former is the depreciation calculated and carried out automatically by the system based on the depreciation type you assign to the asset. And the latter is the depreciation you manually perform using the manual depreciation document. |
| adtUnplannedDepreciation | 1 | Usually carried out when there is an unexpected reduction in the value of an asset resulting, for example, from an accident. |
| adtSpecialDepreciation | 2 | SAP Business One can carry out the special depreciation automatically for an asset, known as the automatic special depreciation. You can assign a depreciation type to an asset with the Special Depreciation method, and the system automatically calculates the special depreciation when it is due. |
| adtAppreciation | 3 | Increase in an asset's book value to offset the asset's unplanned depreciation. |
| adtAssetTransfer | 4 | Transfers an asset to another asset. |
| adtSales | 5 | Indicates an asset sold with a profit or loss. If you do not need to specify the customer information, use this type; otherwise, use an A/R invoice. |
| adtScrapping | 6 | Indicates a scrapped asset, with no revenue earned. SAP Business One posts the asset's remaining book value at the time of retirement as an expense. |
| adtAssetClassTransfer | 7 | Transfers an asset to a new asset class. You can perform the asset class transfer only if the asset uses the depreciation types with the No Depreciation method in all areas during the transfer period. |

# AssetGroupsServiceDataInterfaces (Enumeration)

AssetGroupsService data interfaces.

| Member | Value | Description |
|---|---|---|
| agsAssetGroup | 0 | AssetGroup data interface |
| agsAssetGroupParamsCollection | 1 | AssetGroupParamsCollection data interface |
| agsAssetGroupParams | 2 | AssetGroupParams data interface |

# AssetOriginalTypeEnum (Enumeration)

The original type of the asset document.

| Member | Value | Description |
|---|---|---|
| aotARInvoice | 0 | It indicates the asset document is automatically generated as a result of the creation of an A/R invoice with fixed assets. The abbreviation for the transaction type is IN. |
| aotAPCreditMemo | 1 | It indicates that the asset document is automatically generated as a result of the creation of an A/P credit memo with fixed assets. The abbreviation of the transaction type is PC. |
| aotAPInvoice | 2 | It indicates that the asset document is automatically generated as a result of the creation of an A/P invoice with fixed assets. The abbreviation for the transaction type is PU. |
| aotOutgoingPayment | 3 | It indicates that the asset document is automatically generated as a result of the outgoing payments. |
| aotAPCorrectionInvoice | 4 | It indicates that the asset document is automatically generated as a result of the creation of an A/P correction invoice with fixed assets. The abbreviation for the transaction type is CU. |
| aotCapitalization | 5 | It indicates that the capitalization document is manually created. The abbreviation for the transaction type is AC. |
| aotFixedAssetsCreditMemo | 6 | It indicates that the fixed assets credit memo is manually created. The abbreviation of the transaction type is AM. |
| aotAllTransactions | 7 | All transactions. |
| aotManualDepreciation | 8 | It indicates that the manual depreciation document is always manually created. The abbreviation for the transaction type is MD. |
| aotFixedAssetsTransfer | 9 | It indicates the transfer document is always manually created. The abbreviation for the transaction type is FT. |
| aotRetirement | 10 | It indicates the retirement document is manually created. The abbreviation for the transaction type is RT. |

# AssetRevaluationServiceDataInterfaces (Enumeration)

AssetRevaluationService data interfaces.

| Member | Value | Description |
|---|---|---|
| arsAssetRevaluation | 0 | AssetRevaluation data interface |
| arsAssetRevaluationParamsCollection | 1 | AssetRevaluationParamsCollection data interface |
| arsAssetRevaluationParams | 2 | AssetRevaluationParams data interface |

# AssetStatusEnum (Enumeration)

The asset's status.

| Member | Value | Description |
|---|---|---|
| asNew | 0 | Indicates the asset has been manually created and has not yet been capitalized. |
| asActive | 1 | Indicates the asset has been capitalized and is active. |
| asInActive | 2 | Indicates the asset has been retired and is now inactive. |

# AssetTransactionTypeEnum (Enumeration)

The transaction type of the fixed asset.

| Member | Value | Description |
|---|---|---|
| attBeginningOfYear | 0 | The asset values displayed in this row are the accumulated values at the beginning of the selected fiscal year. |
| attAcquistion | 1 | The amounts incurred in the selected fiscal year as a result of acquisition. |
| attRetirement | 2 | The amounts incurred in the selected fiscal year as a result of retirement. |
| attTransfer | 3 | The amounts incurred in the selected fiscal year as a result of transfer. |
| attWriteUp | 4 | The amounts incurred in the selected fiscal year as a result of write up. |
| attOrdinaryDepreciation | 5 | The amounts incurred in the selected fiscal year as a result of ordinary depreciation. |
| attUplannedDepreciation | 6 | The amounts incurred in the selected fiscal year as a result of unplanned depreciation. |
| attSpecialDepreciation | 7 | The amounts incurred in the selected fiscal year as a result of special depreciation. |
| attEndOfYear | 8 | The asset values displayed in this row are the accumulated values at the end of the selected fiscal year. |

# AssetTypeEnum (Enumeration)

The type of the asset.

| Member | Value | Description |
|---|---|---|
| atAssetTypeGeneral | 0 | Represents regular assets. |
| atAssetTypeLowValueAsset | 1 | Represents low value assets. |

# AttributeGroupFieldTypeEnum (Enumeration)

The predefined type of the attribute field.

| Member | Value | Description |
|---|---|---|
| agftText | 0 | Text |
| agftNumeric | 1 | Numeric |
| agftDate | 2 | Date |
| agftAmount | 3 | Amount |
| agftPrice | 4 | Price |
| agftQuantity | 5 | Quantity |

# AttributeGroupsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| agsAttributeGroup | 0 |  |
| agsAttributeGroupParamsCollection | 1 |  |
| agsAttributeGroupParams | 2 |  |

# AuthenticateUserResultsEnum (Enumeration)

The check results of the username and password.

| Member | Value | Description |
|---|---|---|
| aturNotConnectedToCompany | -8033 | Not connected to the SAP Business One company. |
| aturUsernamePasswordMatch | 0 | The username and the password matches. |
| aturLogOnUserNotAdmin | -8031 | The logon user is not a superuser. |
| aturBadUserOrPassword | -8023 | The username and the password do not match, or the username does not exist. |
| aturUserHasBeenLocked | -8024 | The username is locked. |
| aturPasswordExpired | -8025 | The password is expired. |
| aturDBErrors | -8032 | Run time error when you access the database. |
| aturWrongDomainName | -8034 |  |

# AutoAllocOnReceiptMethodEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| aaormDefaultBin | 0 |  |
| aaormLastBinReceivedItem | 1 |  |
| aaormItemCurrentBins | 2 |  |
| aaormItemCurrentAndHistoricalBins | 3 |  |

# AutomaticPostingEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| apNo | 0 |  |
| apInterestAndFee | 1 |  |
| apInterestOnly | 2 |  |
| apFeeOnly | 3 |  |

# BADivationAlertLevelEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| badal_NoWarning | 0 |  |
| badal_Warning | 1 |  |
| badal_Block | 2 |  |

# BADocumentStatus (Enumeration)

| Member | Value | Description |
|---|---|---|
| bads_Open | 0 |  |
| bads_Closed | 1 |  |
| bads_Cancelled | 2 |  |

# BankChargesAllocationCodesServiceDataInterfaces (Enumeration)

BankChargesAllocationCodesService data interfaces.

| Member | Value | Description |
|---|---|---|
| bcacsBankChargesAllocationCode | 0 | BankChargesAllocationCode data interface |
| bcacsBankChargesAllocationCodesParams | 1 | BankChargesAllocationCodesParams data interface |
| bcacsBankChargesAllocationCodeParams | 2 | BankChargesAllocationCodeParams data interface |

# BankStatementDocTypeEnum (Enumeration)

Document types for bank statements.

| Member | Value | Description |
|---|---|---|
| bsdtReceipts | 0 | Receipt document type. |
| bsdtPaymentToVendor | 1 | Payment to Vendor document type. |
| bsdtInvoices | 2 | Invoice document type. |
| bsdtPurchases | 3 | Purchase document type. |
| bsdtDownPaymentIncoming | 4 | Incoming Down Payment document type. |
| bsdtDownPaymentOutgoing | 5 | Outgoing Down Payment document type. |
| bsdtRevertInvoices | 6 | Revert Invoice document type. |
| bsdtRevertPurchases | 7 | Revert Purchase document type. |
| bsdtJournalEntry | 8 | Journal Entry document type. |

# BankStatementRowSourceEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| bsImported | 0 |  |
| bsImportedAndAmended | 1 |  |
| bsManuallyEntered | 2 |  |

# BankStatementsServiceDataInterfaces (Enumeration)

BankStatementsService data interfaces.

| Member | Value | Description |
|---|---|---|
| bssBankStatements | 0 | BankStatements data interface. |
| bssBankStatement | 1 | BankStatement data interface. |
| bssBankStatementsParams | 2 | BankStatementsParams data interface. |
| bssBankStatementParams | 3 | BankStatementParams data interface. |
| bssBankStatementsFilter | 4 | BankStatementsFilter data interface. |

# BankStatementStatusEnum (Enumeration)

Statuses of bank statements.

| Member | Value | Description |
|---|---|---|
| bssExecuted | 0 | The bank statement is executed and posted to G/L. |
| bssDraft | 1 | The bank statement is a draft document, no posting done. |
| bssOld | 2 | The bank statement is old. |

# BarCodesServiceDataInterfaces (Enumeration)

BarCodesService data interfaces.

| Member | Value | Description |
|---|---|---|
| bsBarCode | 0 | BarCode data interface |
| bsBarCodeParamsCollection | 1 | BarCodeParamsCollection data interface |
| bsBarCodeParams | 2 | BarCodeParams data interface |

# BaseDateSelectEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| bdsFromDueDate | 0 |  |
| bdsFromLastDunningRun | 1 |  |

# BatchNumberDetailsServiceDataInterfaces (Enumeration)

BatchNumberDetailsService data interfaces.

| Member | Value | Description |
|---|---|---|
| bndsBatchNumberDetail | 0 | BatchNumberDetail data interface |
| bndsBatchNumberDetailParams | 1 | BatchNumberDetailParams data interface |

# BinActionTypeEnum (Enumeration)

The type of the bin action.

| Member | Value | Description |
|---|---|---|
| batToWarehouse | 1 | To warehouse |
| batFromWarehouse | 2 | From warehouse |

# BinLocationAttributesServiceDataInterfaces (Enumeration)

BinLocationAttributesService data interfaces.

| Member | Value | Description |
|---|---|---|
| blasBinLocationAttribute | 0 | BinLocationAttribute data interface |
| blasBinLocationAttributeCollectionParams | 1 | BinLocationAttributeCollectionParams data interface |
| blasBinLocationAttributeParams | 2 | BinLocationAttributeParams data interface |

# BinLocationFieldsServiceDataInterfaces (Enumeration)

BinLocationFieldsService data interfaces.

| Member | Value | Description |
|---|---|---|
| blfsBinLocationField | 0 | BinLocationField data interface |
| blfsBinLocationFieldCollectionParams | 1 | BinLocationFieldCollectionParams data interface |
| blfsBinLocationFieldParams | 2 | BinLocationFieldParams data interface |

# BinLocationFieldTypeEnum (Enumeration)

The type of the bin location field.

| Member | Value | Description |
|---|---|---|
| blftWarehouseSublevel | 0 | Warehouse sublevel – The smaller units of space in a warehouse. SAP Business One lets you define up to 4 warehouse sublevels. |
| blftBinLocationAttribute | 1 | Bin location attribute – The attributes you maintain for your bin locations. SAP Business One lets you define up to 10 bin location attribute. |

# BinLocationsServiceDataInterfaces (Enumeration)

BinLocationsService data interfaces.

| Member | Value | Description |
|---|---|---|
| blcsBinLocation | 0 | BinLocation data interface |
| blcsBinLocationCollectionParams | 1 | BinLocationCollectionParams data interface |
| blcsBinLocationParams | 2 | BinLocationParams data interface |

# BinRestrictionBatchEnum (Enumeration)

The batch restriction status of the bin location.

| Member | Value | Description |
|---|---|---|
| brbNoRestrictions | 0 | No restriction - the bin location can store any items regardless of its batch information. |
| brbSingleBatch | 1 | Single batch - the bin location can only store items from one batch. |

# BinRestrictItemEnum (Enumeration)

The item restriction status of the bin location.

| Member | Value | Description |
|---|---|---|
| briNone | 0 | None - the bin location has no item restrictions, that is, the bin location can store any item. |
| briSpecificItem | 1 | Specific Item - the bin location is restricted to a specific item, that is, the bin location can only store a specific item. |
| briSingleItemOnly | 2 | Single Item Only - the bin location is restricted to a single item, that is, the bin location can only store one item. |
| briSpecificItemGroup | 3 | Specific Item Group - the bin location is restricted to a specific item group, that is, the bin location can only store items from a specific item group. |
| briSpecificItemGroupOnly | 4 | Single Item Group Only - the bin location is restricted to a single item group, that is, the bin location can only store items from one item group. |

# BinRestrictTransactionEnum (Enumeration)

The transaction restriction status of the bin location.

| Member | Value | Description |
|---|---|---|
| brtNoRestrictions | 0 | No restriction - the bin location can be used in any relevant transactions. |
| brtAllTrans | 1 | All transactions - the bin location is restricted from all transactions, that is, the bin location cannot be used in any transactions. |
| brtInboundTrans | 2 | Inbound transactions - the bin location is restricted from inbound transactions, that is, the bin location cannot be used to store any incoming flow of goods. |
| brtOutboundTrans | 3 | Outbound transactions - the bin location is restricted from outbound transactions, that is, the bin location cannot be used during the issuing of goods. |
| brtAllExceptInventoryTrans | 4 | All except inventory transfer and counting - the bin location is restricted to inventory transfer, counting and posting only. That is, the bin location can only be used during inventory transfer, counting and posting. |

# BinRestrictUoMEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| bruNone | 0 |  |
| bruSpecificUoM | 1 |  |
| bruSingleUoMOnly | 2 |  |
| bruSpecificUoMGroup | 3 |  |
| bruSingleUoMGroupOnly | 4 |  |

# BlanketAgreementDatePeriodsEnum (Enumeration)

Specifies the cycle interval options for item shipment.

| Member | Value | Description |
|---|---|---|
| Daily | 0 | Every day. |
| Weekly | 1 | Every week. |
| Monthly | 2 | Every month. |
| Quarterly | 3 | Every 3 months. |
| Semiannually | 4 | Every half year. |
| Annually | 5 | Every year. |
| OneTime | 6 | Single time. |

# BlanketAgreementDocTypeEnum (Enumeration)

Specifies the sales (A/R) and purchasing (A/P) document type for the blanket agreement.

| Member | Value | Description |
|---|---|---|
| ARInvoice | 0 | Sales invoice type |
| ARCreditMemo | 1 | Sales credit memo type |
| Delivery | 2 | Sales delivery note type |
| Return | 3 | Sales returns type |
| SalesOrder | 4 | Sales order type |
| APInvoice | 5 | Purchase invoice type |
| APCreditMemo | 6 | Purchase credit memo type |
| GoodsReceiptPO | 7 | Goods receipt PO type |
| GoodsReturn | 8 | Purchase goods returns type |
| PurchaseOrder | 9 | Purchase order type |
| SalesQuotation | 10 | Sales quotation type |
| APCorrectionInvoice | 11 | Purchase correction invoice type |
| APCorrectionInvoiceReversal | 12 | Purchase correction invoice reversal type |
| ARCorrectionInvoice | 13 | Sales correction invoice type |
| ARCorrectionInvoiceReversal | 14 | Sales correction invoice reversal type |
| ARDownPayment | 15 | Sales down payment type |
| APDownPayment | 16 | Purchase down payment type |
| PurchaseQuotation | 17 | Purchase quotation type |

# BlanketAgreementMethodEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| amItem | 0 |  |
| amMonetary | 1 |  |

# BlanketAgreementsServiceDataInterfaces (Enumeration)

BlanketAgreementsService data interfaces.

| Member | Value | Description |
|---|---|---|
| basBlanketAgreement | 0 | BlanketAgreement data interface |
| basBlanketAgreementsDocuments | 1 | BlanketAgreementsDocuments data interface |
| basBlanketAgreementsDocument | 2 | BlanketAgreementsDocument data interface |
| basBlanketAgreementsParams | 3 | BlanketAgreementsParams data interface |
| basBlanketAgreementParams | 4 | BlanketAgreementParams data interface |

# BlanketAgreementStatusEnum (Enumeration)

The status of the blanket agreement.

| Member | Value | Description |
|---|---|---|
| asApproved | 0 | You can sell or buy items and thus create sales or purchasing documents associated with the blanket agreement. |
| asOnHold | 1 | Blanket agreement is set to inactive, and you cannot sell or buy items and thus create sales or purchasing documents associated with the blanket agreement. |
| asDraft | 2 | The blanket agreement is not approved, and you cannot sell or buy items and thus create sales or purchasing documents associated with the blanket agreement. |
| asTerminated | 3 | The blanket agreement is terminated, and you can only sell or buy items and thus create sales or purchasing documents associated with the blanket agreement, if the posting date of the document lies within the date range of the agreement. That is, the document's posting date lies between the start date and the termination date of the agreement. To end the blanket agreement, you specify the termination date in the Termination Date field. SAP Business One sets the status to Terminated. |

# BlanketAgreementTypeEnum (Enumeration)

The type (category) of the agreement you have made with your business partner.

| Member | Value | Description |
|---|---|---|
| atGeneral | 0 | General blanket agreements are used to track fulfillment of terms to obtain a special bonus at year's end, for example, for achieving a certain quantity or turnover volume. |
| atSpecific | 1 | Specific blanket agreements are used to track fulfillment of terms to obtain a special discount for the individual sales or purchasing transaction. They are also used to determine a delivery schedule, for example, by defining the intervals at which products should be delivered. |

# BoAccountTypes (Enumeration)

Specifies the type of account in Chart of Accounts.

| Member | Value | Description |
|---|---|---|
| at_Revenues | 0 | Sets account as revenues account. |
| at_Expenses | 1 | Sets account as expenses account |
| at_Other | 2 | Set to accounts that are neither expenses nor revenues. |

# BoActivities (Enumeration)

Specifies the activity type with contacts (customers or vendors).

| Member | Value | Description |
|---|---|---|
| cn_Conversation | 0 | Defines the activity type as a conversation. |
| cn_Meeting | 1 | Defines the activity type as a meeting. |
| cn_Task | 2 | Defines the activity type as a task. |
| cn_Other | 3 | Any other type of activity. |
| cn_Note | 4 | Defines the activity type as a note. |
| cn_Campaign | 5 |  |

# BoAddressType (Enumeration)

Specifies address types.

| Member | Value | Description |
|---|---|---|
| bo_ShipTo | 0 | Ship To address type. |
| bo_BillTo | 1 | Bill To address type. |

# BoAdEpnsDistribMethods (Enumeration)

Specifies the distribution method of the additional expenses in documents.

| Member | Value | Description |
|---|---|---|
| aedm_None | 0 | No distribution method specified. |
| aedm_Quantity | 1 | Distribution by quantity. |
| aedm_Volume | 2 | Distribution by volume. |
| aedm_Weight | 3 | Distribution by weight. |
| aedm_Equally | 4 | Distribution by equal expenses. |
| aedm_RowTotal | 5 | Distribution by row total expenses. |

# BoAdEpnsTaxTypes (Enumeration)

Specifies the tax type of the additional expenses.

| Member | Value | Description |
|---|---|---|
| aext_NormalTax | 0 | Normal Tax type. |
| aext_NoTax | 1 | No tax. |
| aext_UseTax | 2 | Use Tax type. |

# BoAeDistMthd (Enumeration)

Specifies the distribution method of the additional expenses.

| Member | Value | Description |
|---|---|---|
| aed_None | 0 | No distribution method specified. |
| aed_Quantity | 1 | Distribution by quantity. |
| aed_Volume | 2 | Distribution by volume. |
| aed_Weight | 3 | Distribution by weight. |
| aed_Equally | 4 | Distribution by equal expenses. |
| aed_LineTotal | 5 | Distribution by line total expenses. |

# BoAlertTypeforWHStockEnum (Enumeration)

Specifies the system's response when the inventory level falls below this minimum as the result of a sales document, such as a delivery note or an invoice.

| Member | Value | Description |
|---|---|---|
| atfwhs_WarningOnly | 0 | A warning message appears when the sales document is entered. |
| atfwhs_Block | 1 | The sales document is blocked (default). |
| atfwhs_NoMessage | 2 | No system response is triggered. |

# BoAllocationByEnum (Enumeration)

Specifies the distribution types for landed costs.

| Member | Value | Description |
|---|---|---|
| ab_CashValueBeforeCustoms | 0 | The related costs are distributed in relation to the share of the item of the total FOB price of the delivery minus customs. |
| ab_CashValueAfterCustoms | 1 | The related costs are distributed in relation to the share of the item of the total FOB price of the delivery plus customs. |
| ab_Quantity | 2 | The related costs are distributed according to the quantity of the item in proportion to the total quantity of the delivery. |
| ab_Weight | 3 | The related costs are distributed according to the weight of the item in proportion to the total weight of the delivery. |
| ab_Volume | 4 | The related costs are distributed according to the volume of the item in proportion to the total volume of the delivery. |
| ab_Equal | 5 | The related costs are distributed equally among the items in the delivery. |

# BoAPARDocumentTypes (Enumeration)

Specifies the document type for sales (A/R) and purchasing (A/P).

| Member | Value | Description |
|---|---|---|
| bodt_Invoice | 13 | Sales invoice type |
| bodt_CreditNote | 14 | Sales credit memo type |
| bodt_DeliveryNote | 15 | Sales delivery note type |
| bodt_Return | 16 | Sales returns type |
| bodt_Order | 17 | Sales order type |
| bodt_PurchaseInvoice | 18 | Purchase invoice type |
| bodt_PurchaseCreditNote | 19 | Purchase credit memo type |
| bodt_PurchaseDeliveryNote | 20 | Goods receipt PO type |
| bodt_PurchaseReturn | 21 | Purchase goods returns type |
| bodt_PurchaseOrder | 22 | Purchase order type |
| bodt_Quotation | 23 | Sales quotation type |
| bodt_CorrectionAPInvoice | 163 | A/P correction invoice |
| bodt_CorrectionARInvoice | 165 | A/R correction invoice |
| bodt_PurchaseQutation | 540000006 |  |

# BoApprovalRequestDecisionEnum (Enumeration)

Specifies the status of the approval decision.

| Member | Value | Description |
|---|---|---|
| ardPending | 0 | Awaiting approval. |
| ardApproved | 1 | Approved. |
| ardNotApproved | 2 | Not approved. |

# BoApprovalRequestStatusEnum (Enumeration)

Specifies the status of the approval request.

| Member | Value | Description |
|---|---|---|
| arsPending | 0 | The status of a transaction awaiting approval. |
| arsApproved | 1 | The status of a transaction that has been approved, but not yet converted from a draft to a regular document. |
| arsNotApproved | 2 | The status of a transaction that was not approved and remains a draft. The authorizer can grant approval for a rejected transaction by changing the status accordingly. |
| arsGenerated | 3 | The status of a transaction that has been approved and converted from a draft to a regular document by the originator. |
| arsGeneratedByAuthorizer | 4 | The status of a transaction that has been approved and converted from a draft to a regular document by the authorizer. |
| arsCancelled | 5 | An approval procedure can be cancelled and restarted as necessary. If the approval procedure is cancelled, the draft document cannot be converted to a regular document. |

# BoBarCodeStandardEnum (Enumeration)

Determines whether or not to display Barcode in standard mode.

| Member | Value | Description |
|---|---|---|
| rlbsEan13 | 0 | EAN13 code is used for product identification. The code is numerical, its length is fixed, and it is made up of 13 characters. |
| rlbsCode39 | 1 | Code 39 is an easy to use alpha-numeric barcode. It is also commonly called LOGMARS, Code 3 of 9 or the 3 of 9 Code. |
| rlbsCode128 | 2 | Code 128 is a Barcode standard that uses very high-density linear symbology that can encode text, numbers, several functions and the entire 128 character ASCII character set. |

# BoBaseDateRateEnum (Enumeration)

Determines whether the exchange rate is based on the Posting Date (P) or the Tax Date (T).

| Member | Value | Description |
|---|---|---|
| bdr_PostingDate | 0 | Exchange rate is based on the Posting Date (P). |
| bdr_TaxDate | 1 | exchange rate is based on Tax Date (T). |

# BoBaselineDate (Enumeration)

Specifies the base line date that serves as the reference date for executing a transaction.

| Member | Value | Description |
|---|---|---|
| bld_PostingDate | 0 | Posting date. |
| bld_SystemDate | 1 | System date. |
| bld_TaxDate | 2 | Tax date. |
| bld_ClosingDate | 3 | Closing date. |

# BoBlockBudget (Enumeration)

Specifies the options for managing deviations from budget in documents.

| Member | Value | Description |
|---|---|---|
| bb_OnlyAnnualAlert | 0 | Without Warning - Enables to add transactions that have exceeded the budget. The system does not issue any alert for these transactions. |
| bb_MonthlyAlertOnly | 1 | Warning - the system issues a warning message for any transaction that exceeds the budget. Authorized users can ignore the message. Unauthorized users have to confirm the transaction by an authorized user. |
| bb_Block | 2 | Blocks the option to add transactions to accounts for which the budget was exceeded. |

# BoBoeStatus (Enumeration)

Specifies the bill of exchange (payment) status.

| Member | Value | Description |
|---|---|---|
| boes_Created | 0 | Bill Of Exchange was created. |
| boes_Sent | 1 | Bill Of Exchange was sent. |
| boes_Deposited | 2 | Bill Of Exchange was deposited. |
| boes_Paid | 3 | Bill Of Exchange was paid. |
| boes_Cancelled | 4 | Bill Of Exchange was cancelled. |
| boes_Closed | 5 | Bill Of Exchange was closed. |
| boes_Failed | 6 | Bill Of Exchange was failed. |

# BoBOETypes (Enumeration)

Specifies the bill of exchange type.

| Member | Value | Description |
|---|---|---|
| bobt_Incoming | 0 | Incoming Bill Of Exchange (payment from a customer). |
| bobt_Outgoing | 1 | Outgoing Bill Of Exchange (payment to a vendor). |

# BoBOTFromStatus (Enumeration)

Defines the current statuses for the Bill of Exchange Transaction.

| Member | Value | Description |
|---|---|---|
| btfs_Sent | 0 | The Bill Of Exchange was Sent. |
| btfs_Generated | 1 | The Bill Of Exchange was Generated. |
| btfs_Deposited | 2 | The Bill Of Exchange was Deposited. |
| btfs_Paid | 3 | The Bill Of Exchange was Paid. |

# BoBOTToStatus (Enumeration)

Defines the required statuses for the Bill of Exchange Transaction.

| Member | Value | Description |
|---|---|---|
| btts_Canceled | 0 | Change the Bill Of Exchange status to Canceled. |
| btts_Generated | 1 | Change the Bill Of Exchange status to Generated. |
| btts_Deposit | 2 | Change the Bill Of Exchange status to Deposit. |
| btts_Paid | 3 | Change the Bill Of Exchange status to Paid. |
| btts_Failed | 4 | Change the Bill Of Exchange status to Failed. |
| btts_Closed | 5 | Change the Bill Of Exchange status to Closed (used in France only). |

# BoBpAccountTypes (Enumeration)

Account types for business partners.

| Member | Value | Description |
|---|---|---|
| bpat_General | 0 | For internal use. |
| bpat_DownPayment | 1 | Down Payment (D) |
| bpat_AssetsAccount | 2 | Assets account (A) |
| bpat_Receivable | 3 | Bill of Exchange Account Receivable (R) |
| bpat_Payable | 4 | Bill of Exchange Account Payable (P) |
| bpat_OnCollection | 5 | Bill of Exchange On Collection (C) |
| bpat_Presentation | 6 | Bill of Exchange Presentation (S) |
| bpat_AssetsPayable | 7 | Assets Bill of Exchange Account Payable (Y) |
| bpat_Discounted | 8 | Bill of Exchange Discounted (I) |
| bpat_Unpaid | 9 | Unpaid Bill of Exchange (U) |
| bpat_OpenDebts | 10 | Doubtful Debts (O) |
| bpat_Domestic | 11 | Domestic (M) |
| bpat_Foreign | 12 | Foreign (F) |
| bpat_CashDiscountInterim | 13 |  |
| bpat_ExchangeRateInterim | 14 |  |

**Remarks:** The names of account types were changed in the SAP Business One application. The new names appear in the Description column in the table. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.

# BoBpsDocTypes (Enumeration)

Specifies the document types for identifying the invoice.

| Member | Value | Description |
|---|---|---|
| bpdt_PaymentReference | 0 | Document number for Sweden, Norway, Finland, and Denmark.For this document type, select the value from the table: OINV. |
| bpdt_ISR | 1 | Document number for Swiss.For this document type, select the value from the table: OINV. |
| bpdt_DocNum | 2 | Default document type. The invoice is identified by its number. |

# BoBudgetAlert (Enumeration)

Specifies the alert options in case of deviation from budget.

| Member | Value | Description |
|---|---|---|
| ba_AnnualAlert | 0 | Annual budget alert. |
| ba_MonthlyAlert | 1 | Mounthly budget alert. |

# BoBusinessAreaEnum (Enumeration)

Specifies for which area the tax code determination rule is relevant.

| Member | Value | Description |
|---|---|---|
| baSales | 0 | The tax code determination rule is relevant for sales documents. |
| baPurchase | 1 | The tax code determination rule is relevant for purchasing documents. |
| baSalesAndPurchase | 2 | The tax code determination rule is relevant for both sales and purchasing documents. |

# BoBusinessPartnerGroupTypes (Enumeration)

Specifies the alert options in case of deviation from budget.

| Member | Value | Description |
|---|---|---|
| bbpgt_CustomerGroup | 0 | Customer business partner group type. |
| bbpgt_VendorGroup | 1 | Vendor business partner group type. |

# BoBusinessPartnerTypes (Enumeration)

| Member | Value | Description |
|---|---|---|
| garAll | 0 |  |
| garCompany | 1 |  |
| garPrivate | 2 |  |
| garGovernment | 3 |  |

# BoCardCompanyTypes (Enumeration)

Determines whether or not this Card represent a company or a private person.

| Member | Value | Description |
|---|---|---|
| cCompany | 0 | Card represent a company. |
| cPrivate | 1 | Card represent a private person. |
| cGovernment | 2 |  |
| cEmployee | 3 |  |

# BoCardTypes (Enumeration)

Indicates the business partner's role in your company: customer, vendor, or lead (potential customer/vendor).

| Member | Value | Description |
|---|---|---|
| cCustomer | 0 | The business partner is a customer. |
| cSupplier | 1 | The business partner is a vendor. |
| cLid | 2 | The business partner is a potential customer/vendor. |

# BoChangeLogEnum (Enumeration)

Specifies the types of the changed object.

| Member | Value | Description |
|---|---|---|
| clChartOfAccounts | 0 | ChartOfAccounts object |
| clBusinessPartners | 1 | BusinessPartners object |
| clItems | 2 | Items object |
| clVatGroups | 3 | VatGroups object |
| clUsers | 4 | Users object |
| clInvoices | 5 | Documents object that represents a sales invoice document |
| clCreditNotes | 6 | Documents object that represents a sales credit note document |
| clDeliveryNotes | 7 | Documents object that represents a sales delivery note document |
| clReturns | 8 | Documents object that represents a sales return document |
| clOrders | 9 | Documents object that represents a sales order document |
| clPurchaseInvoices | 10 | Documents object that represents a purchase invoice document |
| clPurchaseCreditNotes | 11 | Documents object that represents a purchase credit note document |
| clPurchaseDeliveryNotes | 12 | Documents object that represents a purchase delivery note document |
| clPurchaseReturns | 13 | Documents object that represents a purchase return document |
| clPurchaseOrders | 14 | Documents object that represents a purchase order document |
| clQuotations | 15 | Documents object that represents a sales quotation document |
| clIncomingPayments | 16 | Payments object |
| clJournalEntries | 17 | JournalEntries object that represents a normal journal entry |
| clCreditCards | 18 | CreditCards object |
| clAdminInfo | 19 | AdminInfo object |
| clVendorPayments | 20 | Payments object that represents payments to vendors |
| clItemGroups | 21 | ItemGroups object |
| clInventoryGeneralEntry | 22 | Documents object for entering general items to inventory |
| clInventoryGeneralExit | 23 | Documents object for removing general items from inventory |
| clWarehouses | 24 | Warehouses object |
| clProductTrees | 25 | ProductTrees object |
| clStockTransfers | 26 | StockTransfer object |
| clFinancePeriods | 27 | FinancePeriod object |
| clAdditionalExpenses | 28 | AdditionalExpenses object |
| clPickLists | 29 | PickLists object |
| clMaterialRevaluation | 30 | MaterialRevaluation object |
| clCorrectionPurchaseInvoice | 31 | Documents object that represents a purchase invoice correction document |
| clCorrectionPurchaseInvoiceReversal | 32 | Documents object that represents a reverse purchase invoice correction document |
| clCorrectionInvoice | 33 | Documents object that represents a correction invoice document |
| clCorrectionInvoiceReversal | 34 | Documents object that represents a reverse invoice correction document |
| clEmployeesInfo | 35 | EmployeesInfo object |
| clCustomerEquipmentCards | 36 | CustomerEquipmentCards object |
| clWithholdingTaxCodes | 37 | WithholdingTaxCodes object |
| clBillOfExchange | 38 | BillOfExchange object |
| clServiceCalls | 39 | ServiceCalls object |
| clProductionOrders | 40 | ProductionOrders object |
| clDownPayments | 41 | Documents object that represents a down payment document |
| clPurchaseDownPayments | 42 | Documents object that represents a purchase down payment document |
| clPeriodCategory | 43 | PeriodCategory object that represents G/L Determination |
| clHouseBankAccounts | 44 | HouseBankAccounts object |
| clSalesTaxInvoice | 45 | Sales tax invoice object (see TaxInvoices object and DocType property with the valid value botit_Invoice) |
| clPurchaseTaxInvoice | 46 | Purchase tax invoice object (see TaxInvoices object and DocType property with the valid value botit_Payment) |
| clExternalBankOperationCodes | 47 | External bank operation codes |
| clInternalBankOperationCodes | 48 | Internal bank operation codes |
| clOutgoingExciseInvoice | 49 | Outgoing excise invoices |
| clIncomingExciseInvoice | 50 | Incoming excise invoices |
| clInventoryTransferRequests | 51 | Inventory transfer requests |
| clPurchaseQuotation | 52 |  |
| clActivities | 53 |  |
| clChecksForPayment | 54 |  |
| clServiceContract | 55 |  |
| clUDO | 100 | User-defined objects |

# BoCheckDepositTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| cdtCashChecks | 0 |  |
| cdtPostdatedChecks | 1 |  |

# BoClosingDateProcedureBaseDateEnum (Enumeration)

Specifies the base date that serves as the reference date for executing a transaction.

| Member | Value | Description |
|---|---|---|
| bocpdbld_PostingDate | 0 | Posting date. |
| bocpdbld_BaseSystemDate | 1 | System date. |

# BoClosingDateProcedureDueMonthEnum (Enumeration)

Specifies the start from date for calculating the transaction due date.

| Member | Value | Description |
|---|---|---|
| bocpddm_MonthEnd | 0 | End date of the month. |
| bocpddm_HalfMonth | 1 | Middle date of the month. |
| bocpddm_MonthStart | 2 | Begining date of the month. |
| bocpddm_None | 3 | None |

# BoCockpitTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| cptt_UserCockpit | 0 |  |
| cptt_TemplateCockpit | 1 |  |

# BoConsumptionMethod (Enumeration)

Specifies the default methods for forecast consumption.

| Member | Value | Description |
|---|---|---|
| cm_BackwardForward | 0 | The system starts to subtract from the forecast of -X days (DaysBackward) and then continue with the forecast of +Y days (DaysForward). |
| cm_ForwardBackward | 1 | The system starts to subtract from the forecast of +Y days (DaysForward) and then continue with the forecast of -X days (DaysBackward). |

# BoContractTypes (Enumeration)

Specifies the service contract types.

| Member | Value | Description |
|---|---|---|
| ct_Customer | 0 | Customer contract type that covers the service for all customer's purchased items, regardless of the group or serial numbers. |
| ct_ItemGroup | 1 | Item Group contract type that covers the service for the item groups defined in the service contract. |
| ct_SerialNumber | 2 | Serial Number contract type that covers the service for the serial numbers defined in the service contract. |

# BoCorInvItemStatus (Enumeration)

Specifies status of the correction invoice.

| Member | Value | Description |
|---|---|---|
| ciis_Was | 0 | A correction invoice was created. |
| ciis_ShouldBe | 1 | A correction invoice should be created. |

# BoCpCardAcct (Enumeration)

Specifies whether the vendor is identified by its code (vendor card) or by its account.

| Member | Value | Description |
|---|---|---|
| cfp_Card | 0 | The vendor is identified by its code (vendor card). |
| cfp_Account | 1 | The vendor is identified by its account. |

# BoCurrencyCheck (Enumeration)

Determines whether or not to block Multi Currency Journal Entry.

| Member | Value | Description |
|---|---|---|
| cc_Block | 0 | The use of Foreign Currency Check Account is blocked. |
| cc_NoMessage | 1 | The use of Foreign Currency Check Account is permitted. |

# BoCurrencySources (Enumeration)

Specifies the currency source.

| Member | Value | Description |
|---|---|---|
| bocs_LocalCurrency | 0 | Local currency. |
| bocs_SystemCurrency | 1 | System currency. |
| bocs_BPCurrency | 2 | Business partner currency. |

# BoDataOwnershipManageMethodEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| doManageByDocOnly | 0 |  |
| doManageByBPOnly | 1 |  |
| doManageByBPnDoc | 2 |  |
| doManageByBranch | 3 |  |

# BoDataServerTypes (Enumeration)

Database server types.

| Member | Value | Description |
|---|---|---|
| dst_MSSQL | 1 | Microsoft SQL Server 2000 (Not Supported from 8.8) |
| dst_DB_2 | 2 | DB2 (Not Supported from 8.8) |
| dst_SYBASE | 3 | Sybase (Not Supported from 8.8) |
| dst_MSSQL2005 | 4 | Microsoft SQL Server 2005 |
| dst_MAXDB | 5 | MaxDB (Not Supported from 8.8) |
| dst_MSSQL2008 | 6 | Microsoft SQL Server 2008 |
| dst_MSSQL2012 | 7 | Microsoft SQL Server 2012 |
| dst_MSSQL2014 | 8 | Microsoft SQL Server 2014 |
| dst_HANADB | 9 | SAP HANA Platform |
| dst_MSSQL2016 | 10 | Microsoft SQL Server 2016 |
| dst_MSSQL2017 | 11 | Microsoft SQL Server 2017 |
| dst_MSSQL2019 | 15 | Microsoft SQL Server 2019 |

# BoDataSourceEnum (Enumeration)

Determines the Report Layout data source nature.

| Member | Value | Description |
|---|---|---|
| rldsFreeText | 0 | Free text data source. |
| rldsSystemVariable | 1 | System variable data source. |
| rldsDatabase | 2 | Database data source. |
| rldsFormula | 3 | Formula data source. |

# BoDateTemplate (Enumeration)

Determines the template used to display Date field.

| Member | Value | Description |
|---|---|---|
| dt_DDMMYY | 0 | Displays the last day of the Twenty Century as: 31/12/00 |
| dt_DDMMCCYY | 1 | Displays the last day of the Twenty Century as: 31/12/2000 |
| dt_MMDDYY | 2 | Displays the last day of the Twenty Century as: 12/31/00 |
| dt_MMDDCCYY | 3 | Displays the last day of the Twenty Century as: 12/31/2000 |
| dt_CCYYMMDD | 4 | Displays the last day of the Twenty Century as: 2000/12/31 |
| dt_DDMonthYYYY | 5 | Displays the last day of the Twenty Century as: 31/December/2000 |
| dt_YYMMDD | 6 |  |

# BoDeductionTaxGroupCodeEnum (Enumeration)

Deduction tax groups.

| Member | Value | Description |
|---|---|---|
| dtgcInterestReceivers | 1 | Those receiving interest |
| dtgcEmployeeReceivingCommission | 2 | Employees receiving commissions |
| dtgcWritersPrice | 3 | Writers |
| dtgcPaidServices | 6 | Those receiving paid services |
| dtgcPaymentsToForeignCitizens | 7 | Non-citizens |
| dtgcPaymentsForCitizensInForeignCountries | 8 | Citizens in foreign countries |
| dtgcInvalidPaymentFromCompensationFund | 11 | Those receiving invalid Payments from a compensation fund |
| dtgcRepaymentToEmployerFromCompensationFund | 12 | Employers receiving repayment from a compensation fund |
| dtgcRentalPayments | 13 | Those receiving rental payments |
| dtgcPaymentsFromStudyFund | 14 | Those receiving payments from a study fund |
| dtgcDividendPayments | 18 | Those receiving dividend payments |

**Remarks:** For Israel only. The group code can be one of the following: 01 - Interest Receivers 02 - Employee Receiving Commission 03 - Writers Price 06 - Paid Services 07 - Payments for citizens in foreign countries transferred by the bank 08 - Payments for citizens in foreign countries transferred by the bank 11 - Invalid Payment from Compensation Fund 12 - Repayment to Employer from Compensation Fund 13 - Rental payments that can be claimed as an expense 14 - Payments from Study Fund for Self-Employed © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.

# BoDefaultBatchStatus (Enumeration)

Specifies the default batch statuses.

| Member | Value | Description |
|---|---|---|
| dbs_Released | 0 | Enables the running of batch processes. |
| dbs_NotAccessible | 1 | Prevents the running of batch processes for sales documents and A/P credit memos. This setting is used for batch processes in production or undergoing a quality check. It allows, however, the running of batch processes in stock-transfer documents. This status is used for reports to distinguish between locked batches and not accessible ones. |
| dbs_Locked | 2 | Enables the running of batch processes in stock documents only, such as stock transfers or goods issues. |

# BoDeferCommitmentLimitOnDueDateTypes (Enumeration)

Defer commitment limit on Due Date.

| Member | Value | Description |
|---|---|---|
| dcl_MonthEnd | 0 | Month end |
| dcl_HalfMonth | 1 | Half month |
| dcl_MonthStart | 2 | Month start |

# BoDepositAccountTypeEnum (Enumeration)

Specifies whether to perform the deposit to a bank account or business partner.

| Member | Value | Description |
|---|---|---|
| datBankAccount | 0 | Deposits to a bank account. Specify a G/L account. |
| datBusinessPartner | 1 | Deposits to a business partner. Specify a BP code. |

**Remarks:** For checks or credit cards. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.

# BoDepositCheckEnum (Enumeration)

Specifies the deposit status of the check.

| Member | Value | Description |
|---|---|---|
| dtNo | 0 | Not deposited. |
| dcAsCash | 1 | Deposited as cash (the due date of the check is earlier than or the same as the date entered in the Considered Until field). |
| dtAsPostdated | 2 | Deposited as postdated check (the due date of the check is later than or the same as the date entered in the Considered Until field). |

# BoDepositPostingTypes (Enumeration)

Defines the posting types for the deposit by the bank.

| Member | Value | Description |
|---|---|---|
| dpt_Collection | 0 | The bank deposits the payment on the due date of the Bill Of Exchange. |
| dpt_Discounted | 1 | The company requests from the bank to advance the deposit before the due date of the Bill Of Exchange (the bank deducts a commission and interest from the amount of the Bill Of Exchange). |

# BoDepositTypeEnum (Enumeration)

The type of the deposit.

| Member | Value | Description |
|---|---|---|
| dtChecks | 0 | Checks |
| dtCredit | 1 | Credit cards |
| dtCash | 2 | Cash |
| dtBOE | 3 | Bills of exchange |

# BoDocItemType (Enumeration)

| Member | Value | Description |
|---|---|---|
| dit_Item | 0 |  |
| dit_Resource | 1 |  |

# BoDocLineType (Enumeration)

Defines line type for Quatation.

| Member | Value | Description |
|---|---|---|
| dlt_Regular | 0 | Specifies regular item line. |
| dlt_Alternative | 1 | Specifies alternative item line. |

# BoDocSpecialLineType (Enumeration)

Defines the line type of special lines in marketing documents.

| Member | Value | Description |
|---|---|---|
| dslt_Text | 0 | Specifies text line type (for remarks, comments, etc.) |
| dslt_Subtotal | 1 | Specifies line type of subtotal. The line will calculate subtotal of the previous lines. |

# BoDocSummaryTypes (Enumeration)

Defines the summary type for displaying table rows in a document.

| Member | Value | Description |
|---|---|---|
| dNoSummary | 0 | The system does not show any summary in the document (the order of the rows remains unchanged). |
| dByItems | 1 | The system displays in a single row summary information of all the rows of the same item that includes the same price, description and warehouse. |
| dByDocuments | 2 | The system displays in a single row summary information of all the documents that are based on the same base document. The summary information includes the base document number and reference. |

# BoDocumentLinePickStatus (Enumeration)

Specifies document line pick status.

| Member | Value | Description |
|---|---|---|
| dlps_Picked | 0 | Picked |
| dlps_NotPicked | 1 | Not Picked |
| dlps_ReleasedForPicking | 2 | Released For Picking |
| dlps_PartiallyPicked | 3 | Partially Picked |

# BoDocumentSubType (Enumeration)

Defines document sub-types that are used for creating documents with separate numbering.

| Member | Value | Description |
|---|---|---|
| bod_None | 0 | None. |
| bod_InvoiceExempt | 1 | Exempt invoice. |
| bod_DebitMemo | 2 | Debit memo. |
| bod_Bill | 3 | Bill. |
| bod_ExemptBill | 4 | Exempt bill. |
| bod_PurchaseDebitMemo | 5 | Purchase debit memo. |
| bod_ExportInvoice | 6 | Export invoice. |
| bod_GSTTaxInvoice | 7 |  |
| bod_GSTDebitMemo | 8 |  |
| bod_RefundVoucher | 9 |  |

# BoDocumentTypes (Enumeration)

Defines the business transaction content types: item-based transaction, or service-based transaction.

| Member | Value | Description |
|---|---|---|
| dDocument_Items | 0 | The transaction is based on items. |
| dDocument_Service | 1 | The transaction is based on services. |

# BoDocWhsAutoIssueMethod (Enumeration)

The method by which items in bin locations are issued.

| Member | Value | Description |
|---|---|---|
| aimSingleChoiceOnly | 0 | Single Choice - Allocates items from bin locations when there is only one way of doing it. If there is more than one way to allocate items from bin locations, the single choice method is not effective. |
| aimBinCodeOrder | 1 | Bin Location Code Order - Allocates items from bin locations according to the alphanumeric order of the bin location codes. |
| aimAlternativeSortCodeOrder | 2 | Alternative Sort Code Order - Allocates items from bin locations according to the alphanumeric order of the bin locations' alternative sort codes. |
| aimQtyDescendingOrder | 3 | Descending Quantity - Allocates items from bin locations according to the descending order of the item quantity in the bin locations. |
| aimQtyAscendingOrder | 4 | Ascending Quantity - Allocates items from bin locations according to the ascending order of the item quantity in the bin locations. |
| aimBinFIFO | 5 |  |
| aimBinLIFO | 6 |  |
| aimSingleBinPreferred | 7 |  |

# BoDocWhsUpdateTypes (Enumeration)

Specifies the method for updating the warehouse information.

| Member | Value | Description |
|---|---|---|
| dwh_No | 0 | No method is specified. |
| dwh_OrdersFromVendors | 1 | The warehouse is updated by orders from vendors. |
| dwh_CustomerOrders | 2 | The warehouse is updated by customer orders. |
| dwh_Consignment | 3 | The warehouse is updated by consignment. |
| dwh_Stock | 4 | The warehouse is updated by stock. |

# BoDueDateEnum (Enumeration)

Specifies the Due Date selection type.

| Member | Value | Description |
|---|---|---|
| boddDateOfPaymentRun | 0 | Due date as date of payment run. |
| boddDueDateOfInvoice | 1 | Due date as date of Invoice. |
| boddPaymentTerms | 2 | Due date as date of payment terms. |

# BoDurations (Enumeration)

Specifies duration types.

| Member | Value | Description |
|---|---|---|
| du_Seconds | -1 |  |
| du_Minuts | 0 | Minutes. |
| du_Hours | 1 | Hours. |
| du_Days | 2 | Days. |

# BOEDocumentTypesServiceDataInterfaces (Enumeration)

BOEDocumentTypesService data interfaces.

| Member | Value | Description |
|---|---|---|
| boedtsBOEDocumentTypes | 0 | BOEDocumentTypes data interface |
| boedtsBOEDocumentType | 1 | BOEDocumentType data interface |
| boedtsBOEDocumentTypesParams | 2 | BOEDocumentTypesParams data interface |
| boedtsBOEDocumentTypeParams | 3 | BOEDocumentTypeParams data interface |

# BOEInstructionsServiceDataInterfaces (Enumeration)

BOEInstructionsService data interfaces.

| Member | Value | Description |
|---|---|---|
| boeisBOEInstructions | 0 | BOEInstructions data interface |
| boeisBOEInstruction | 1 | BOEInstruction data interface |
| boeisBOEInstructionsParams | 2 | BOEInstructionsParams data interface |
| boeisBOEInstructionParams | 3 | BOEInstructionParams data interface |

# BOELinesServiceDataInterfaces (Enumeration)

BOELinesService data interfaces.

| Member | Value | Description |
|---|---|---|
| boelsBOELinesParams | 0 | BOELinesParams data interface |
| boelsBOELineParams | 1 | BOELineParams data interface |

# BOEPortfoliosServiceDataInterfaces (Enumeration)

BOEPortfoliosService data interfaces.

| Member | Value | Description |
|---|---|---|
| boepsBOEPortfolios | 0 | BOEPortfolios data interface |
| boepsBOEPortfolio | 1 | BOEPortfolio data interface |
| boepsBOEPortfoliosParams | 2 | BOEPortfoliosParams data interface |
| boepsBOEPortfolioParams | 3 | BOEPortfolioParams data interface |

# BoEquipmentBPType (Enumeration)

| Member | Value | Description |
|---|---|---|
| et_Sales | 1 |  |
| et_Purchasing | 2 |  |
| et_SalesAndPurchasing | 3 |  |

# BoExpenseOperationTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| bo_ExpOpType_ProfessionalServices | 0 |  |
| bo_ExpOpType_RentingAssets | 1 |  |
| bo_ExpOpType_Others | 2 |  |
| bo_ExpOpType_None | 3 |  |

# BoExtensionErrorActionEnum (Enumeration)

Sets or returns current definition of the action to be taken upon printer extension error.

| Member | Value | Description |
|---|---|---|
| eeaStop | 0 | Stop the printer extension. |
| eeaIgnore | 1 | Ignore the printer extension error. |
| eeaPrompt | 2 | Prompt an error message to operator. |

# BoFatherCardTypes (Enumeration)

Specifies the methods of handling deliveries and payments used by the parent business partner.

| Member | Value | Description |
|---|---|---|
| cPayments_sum | 0 | Invoices that have been sent to the branches will be balanced by a payment from the head office. |
| cDelivery_sum | 1 | Sends delivery notes of branches in one invoice to the head office. |

# BoFieldTypes (Enumeration)

Specifies the field types in the system.

| Member | Value | Description |
|---|---|---|
| db_Alpha | 0 | Alphanumeric. |
| db_Memo | 1 | Memo. |
| db_Numeric | 2 | Numeric. |
| db_Date | 3 | Date. |
| db_Float | 4 | Foating point. |

# BoFldSubTypes (Enumeration)

Indicate special field types supported by the SAP Business One application. Use this enumeration when working with User Defined Fields.

| Member | Value | Description |
|---|---|---|
| st_None | 0 | No special sub-type. |
| st_Address | 63 | Address format. |
| st_Phone | 35 | Phone format. |
| st_Time | 84 | Time format. |
| st_Rate | 82 | Double format with the system's rate accuracy. |
| st_Sum | 83 | Double format with the system's summery accuracy. |
| st_Price | 80 | Double format with the system's price accuracy. |
| st_Quantity | 81 | Double format with the system's quantity accuracy. |
| st_Percentage | 37 | Double format with the system's percentage accuracy. |
| st_Measurement | 77 | Double format with the system's measurement accuracy. |
| st_Link | 66 | Link format (mostly used for a web site links). |
| st_Image | 73 | Image format. |

# BoFormattedSearchActionEnum (Enumeration)

Specifies the types of action to be taken by the system when activating the formatted search function.

| Member | Value | Description |
|---|---|---|
| bofsaNone | 0 | Without search - cancels a formatted search defined for the specified field. |
| bofsaValidValues | 1 | Search by user valid values. |
| bofsaQuery | 2 | Search by saved query. |

# BoFrequency (Enumeration)

Specifies the cycle interval options for inventory counts.

| Member | Value | Description |
|---|---|---|
| bof_Daily | 0 | Every day. |
| bof_Weekly | 1 | Every week (in a specified Day in the week). Used also for order interval planning. |
| bof_Every4Weeks | 2 | Every four weeks (in a specified Day in the week). |
| bof_Monthly | 3 | Every month (in a specified Day in the month). Used also for order interval planning. |
| bof_Quarterly | 4 | Quarterly. |
| bof_HalfYearly | 5 | Every half year. |
| bof_Annually | 6 | Every year. |
| bof_OneTime | 7 | Single time. |
| bof_EveryXDays | 8 | Every X days. You must specify also the number of days in the Day property. Used for order interval planning. |

# BoFrequencyTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ftDaily | 0 |  |
| ftWeekly | 1 |  |
| ftMonthly | 2 |  |
| ftQuarterly | 3 |  |
| ftSemiannually | 4 |  |
| ftAnnually | 5 |  |
| ftOneTime | 6 |  |
| ftTemplate | 7 |  |
| ftNotExecuted | 8 |  |

# BoGenderTypes (Enumeration)

Specifies the gender type.

| Member | Value | Description |
|---|---|---|
| gt_Female | 0 | Female gender. |
| gt_Male | 1 | Male gender. |
| gt_Undefined | 2 | Undefined gender. |
| gt_Masked | 3 |  |

# BoGLMethods (Enumeration)

Defines the default G/L accounts for posting transactions related to the item.

| Member | Value | Description |
|---|---|---|
| glm_WH | 0 | Default G/L accounts are set by the warehouse definition (Warehouses). |
| glm_ItemClass | 1 | Default G/L accounts are set by the item group definition (ItemGroups). |
| glm_ItemLevel | 2 | The G/L account is set in the item level. |

# BoGridTypeEnum (Enumeration)

Specifies the Grid type of reports layout.

| Member | Value | Description |
|---|---|---|
| gtCombination | 0 | Grid by a combination broken lines and dots. |
| gtContinuousLine | 1 | Grid by continuous lines. |
| gtBrokenLine | 2 | Grid by broken lines. |
| gtDots | 3 | Grid by dots. |

# BoGSTRegnTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| gstRegularTDSISD | 1 |  |
| gstCasualTaxablePerson | 2 |  |
| gstCompositionLevy | 3 |  |
| gstGoverDepartPSU | 4 |  |
| gstNonResidentTaxablePerson | 5 |  |
| gstUNAgencyEmbassy | 6 |  |

# BoHorizontalAlignmentEnum (Enumeration)

Specifies the horizontal alignment (justification).

| Member | Value | Description |
|---|---|---|
| rlhjRight | 0 | Right horizontal alignment. |
| rlhjLeft | 1 | Left horizontal alignment. |
| rlhjCentralized | 2 | Centralized horizontal alignment. |
| rlhjLanguageDependent | 3 | Language dependent horizontal alignment. |

# BoInterimDocTypes (Enumeration)

| Member | Value | Description |
|---|---|---|
| boidt_None | 0 |  |
| boidt_ExchangeRate | 1 |  |
| boidt_CashDiscount | 2 |  |

# BoInventorySystem (Enumeration)

Specifies the inventory evaluation methods.

| Member | Value | Description |
|---|---|---|
| bis_MovingAverage | 0 | The system evaluates the inventory based on the corresponding quantities and prices for each goods receipt and issue, and the moving average price is updated accordingly. |
| bis_Standard | 1 | The standard pricing system permits selection of a fixed price, which is then used for all transactions. |
| bis_FIFO | 2 | First-In-First-Out. Continuous stock system in which goods purchased first are sold or used first, regardless of the goods actual flow. |
| bis_SNB | 3 |  |

# BoIssueMethod (Enumeration)

Specifies the methods for issuing items from the inventory. Property type Read-write property " -->

| Member | Value | Description |
|---|---|---|
| im_Backflush | 0 | SAP Business One issues items automatically from the inventory. |
| im_Manual | 1 | The user issues specified items manually from the inventory. |

# BoItemTreeTypes (Enumeration)

Specifies the tree types for items.

| Member | Value | Description |
|---|---|---|
| iNotATree | 0 | The item is not a tree. |
| iAssemblyTree | 1 | Sets item to an assembly tree. |
| iSalesTree | 2 | Sets item to a sales tree. |
| iProductionTree | 3 | Sets item to a production tree. |
| iTemplateTree | 4 | Sets item to a template tree. |
| iIngredient | 5 | Sets item to ilngredient. |

# BoLineBreakEnum (Enumeration)

Specifies the Line Brake types.

| Member | Value | Description |
|---|---|---|
| rlsAllowOverflow | 0 | Allow Overflow at line brake. |
| rlsAdjustToCell | 1 | Adjust line to cell dimention at line brake. |
| rlsDivideIntoRows | 2 | Divite text to rows at line brake. |

# BoManageMethod (Enumeration)

Specifies the management method of serial numbers and batch numbers.

| Member | Value | Description |
|---|---|---|
| bomm_OnEveryTransaction | 0 | With this method, the user must assign a serial or batch number on every inventory transaction. |
| bomm_OnReleaseOnly | 1 | With this method, the user must assign a serial or batch number only on release transaction. For other transactions, assigning a serial or batch number is optional. |

# BoMaterialTypes (Enumeration)

Specifies the goods material type.

| Member | Value | Description |
|---|---|---|
| mt_GoodsForReseller | 0 | Goods for reseller material type |
| mt_FinishedGoods | 1 | Finished goods material type |
| mt_GoodsInProcess | 2 | Goods in process material type |
| mt_RawMaterial | 3 | Raw material type |
| mt_Package | 4 | Package material type |
| mt_SubProduct | 5 | Subproduct material type |
| mt_IntermediateMaterial | 6 | Intermediate material material type |
| mt_ConsumerMaterial | 7 | Consumer material type |
| mt_FixedAsset | 8 | Fixed asset material type |
| mt_Service | 9 | Service material type |
| mt_OtherInput | 10 | Other input material type |
| mt_Other | 99 | Other material type |

# BoMeritalStatuses (Enumeration)

Specifies the marital statuses.

| Member | Value | Description |
|---|---|---|
| mts_Single | 0 | Single. |
| mts_Married | 1 | Married. |
| mts_Divorced | 2 | Divorced. |
| mts_Widowed | 3 | Widowed. |
| mts_NotSpecified | 4 |  |

# BoMoneyPrecisionTypes (Enumeration)

Defines the precision type (number of decimal places, up to 6) for conversion of money (double integer) to string. The precision of each type depends on definitions in SAP Business One.

| Member | Value | Description |
|---|---|---|
| mpt_Sum | 0 | Amounts. |
| mpt_Price | 1 | Prices. |
| mpt_Rate | 2 | Rates. |
| mpt_Quantity | 3 | Quantities. |
| mpt_Percent | 4 | Percent. |
| mpt_Measure | 5 | Units. |
| mpt_Tax | 6 | Tax. |

# BoMRPComponentWarehouse (Enumeration)

| Member | Value | Description |
|---|---|---|
| bomcw_BOM | 0 |  |
| bomcw_Parent | 1 |  |

# BoMsgPriorities (Enumeration)

Defines a priority flag to a message or a contact activity.

| Member | Value | Description |
|---|---|---|
| pr_Low | 0 | Low priority. |
| pr_Normal | 1 | Normal priority. |
| pr_High | 2 | High priority. |

# BoMsgRcpTypes (Enumeration)

Defines the type of recipient for the message.

| Member | Value | Description |
|---|---|---|
| rt_RandomUser | -1 | Specifies any user of the SAP Business One application. |
| rt_InternalUser | 12 | Specifies a company-internal user. |
| rt_ContactPerson | 11 | Specifies a vendor or a customer user. |

# BoMYFTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| myft_WholesaleSales | 0 |  |
| myft_RetailSales | 1 |  |
| myft_WholesalePurchases | 2 |  |
| myft_OtherExpenseTransactions | 3 |  |

# BoObjectTypes (Enumeration)

Specifies the object types. Note: The right column indicates the object ID to use as a string for the DocObjectCodeEx property.

| Member | Value | Description |
|---|---|---|
| oChartOfAccounts | 1 | ChartOfAccounts object |
| oBusinessPartners | 2 | BusinessPartners object |
| oBanks | 3 | Banks object |
| oItems | 4 | Items object |
| oVatGroups | 5 | VatGroups object |
| oPriceLists | 6 | PriceLists object |
| oSpecialPrices | 7 | SpecialPrices object |
| oItemProperties | 8 | ItemProperties object |
| oUsers | 12 | Users object |
| oInvoices | 13 | Documents object that represents a sales invoice document |
| oCreditNotes | 14 | Documents object that represents a sales credit note document |
| oDeliveryNotes | 15 | Documents object that represents a sales delivery note document |
| oReturns | 16 | Documents object that represents a sales return document |
| oOrders | 17 | Documents object that represents a sales order document |
| oPurchaseInvoices | 18 | Documents object that represents a purchase invoice document |
| oPurchaseCreditNotes | 19 | Documents object that represents a purchase credit note document |
| oPurchaseDeliveryNotes | 20 | Documents object that represents a purchase delivery note document |
| oPurchaseReturns | 21 | Documents object that represents a a purchase return document |
| oPurchaseOrders | 22 | Documents object that represents a purchase order document |
| oQuotations | 23 | Documents object that represents a sales quotation document |
| oIncomingPayments | 24 | Payments object |
| oJournalVouchers | 28 | JournalVouchers object |
| oJournalEntries | 30 | JournalEntries object that represents a normal journal entry |
| oStockTakings | 31 | StockTaking object |
| oContacts | 33 | Contacts object |
| oCreditCards | 36 | CreditCards object |
| oCurrencyCodes | 37 | Currencies object |
| oPaymentTermsTypes | 40 | PaymentTermsTypes object |
| oBankPages | 42 | BankPages object |
| oManufacturers | 43 | Manufacturers object |
| oVendorPayments | 46 | Payments object that represents payments to vendors |
| oLandedCostsCodes | 48 | LandedCostsCodes object |
| oShippingTypes | 49 | ShippingTypes object |
| oLengthMeasures | 50 | LengthMeasures object |
| oWeightMeasures | 51 | WeightMeasures object |
| oItemGroups | 52 | ItemGroups object |
| oSalesPersons | 53 | SalesPersons object |
| oCustomsGroups | 56 | CustomsGroups object |
| oChecksforPayment | 57 | ChecksforPayment object |
| oInventoryGenEntry | 59 | Documents object for entering general items to inventory |
| oInventoryGenExit | 60 | Documents object for removing general items from inventory |
| oWarehouses | 64 | Warehouses object |
| oCommissionGroups | 65 | CommissionGroups object |
| oProductTrees | 66 | ProductTrees object |
| oStockTransfer | 67 | StockTransfer object |
| oWorkOrders | 68 | WorkOrders object |
| oCreditPaymentMethods | 70 | CreditPaymentMethods object |
| oCreditCardPayments | 71 | CreditCardPayments object |
| oAlternateCatNum | 73 | AlternateCatNum object |
| oBudget | 77 | Budget object |
| oBudgetDistribution | 78 | BudgetDistribution object |
| oMessages | 81 | Messages object |
| oBudgetScenarios | 91 | BudgetScenarios object |
| oSalesOpportunities | 97 | SalesOpportunities object |
| oUserDefaultGroups | 93 | UserDefaultGroups object |
| oSalesStages | 101 | SalesStages object |
| oActivityTypes | 103 | ActivityTypes object |
| oActivityLocations | 104 | ActivityLocations object |
| oDrafts | 112 | Documents object that represents a draft document (see Creating a draft document sample) |
| oDeductionTaxHierarchies | 116 | DeductionTaxHierarchies object |
| oDeductionTaxGroups | 117 | DeductionTaxGroups object |
| oAdditionalExpenses | 125 | AdditionalExpenses object |
| oSalesTaxAuthorities | 126 | SalesTaxAuthorities object |
| oSalesTaxAuthoritiesTypes | 127 | SalesTaxAuthoritiesTypes object |
| oSalesTaxCodes | 128 | SalesTaxCodes object |
| oQueryCategories | 134 | QueryCategories object |
| oFactoringIndicators | 138 | FactoringIndicators object |
| oPaymentsDrafts | 140 | Payments draft object |
| oAccountSegmentations | 142 | AccountSegmentations object |
| oAccountSegmentationCategories | 143 | AccountSegmentationCategories object |
| oWarehouseLocations | 144 | WarehouseLocations object |
| oForms1099 | 145 | Forms1099 object |
| oInventoryCycles | 146 | InventoryCycles object |
| oWizardPaymentMethods | 147 | WizardPaymentMethods object |
| oBPPriorities | 150 | BPPriorities object |
| oDunningLetters | 151 | DunningLetters object |
| oUserFields | 152 | UserFieldsMD object |
| oUserTables | 153 | UserTablesMD object |
| oPickLists | 156 | PickLists object |
| oPaymentRunExport | 158 | PaymentRunExport object |
| oUserQueries | 160 | UserQueries object |
| oMaterialRevaluation | 162 | MaterialRevaluation object |
| oCorrectionPurchaseInvoice | 163 | Documents object that represents a purchase invoice correction document |
| oCorrectionPurchaseInvoiceReversal | 164 | Documents object that represents a reverse purchase invoice correction document |
| oCorrectionInvoice | 165 | Documents object that represents a correction invoice document |
| oCorrectionInvoiceReversal | 166 | Documents object that represents a reverse invoice correction document |
| oContractTemplates | 170 | ContractTemplates object |
| oEmployeesInfo | 171 | EmployeesInfo object |
| oCustomerEquipmentCards | 176 | CustomerEquipmentCards object |
| oWithholdingTaxCodes | 178 | WithholdingTaxCodes object |
| oBillOfExchangeTransactions | 182 | BillOfExchangeTransaction object |
| oKnowledgeBaseSolutions | 189 | KnowledgeBaseSolutions object |
| oServiceContracts | 190 | ServiceContracts object |
| oServiceCalls | 191 | ServiceCalls object |
| oUserKeys | 193 | UserKeysMD object |
| oQueue | 194 | Queue object |
| oSalesForecast | 198 | SalesForecast object |
| oTerritories | 200 | Territories object |
| oIndustries | 201 | Industries object |
| oProductionOrders | 202 | ProductionOrders object |
| oPackagesTypes | 205 | PackagesTypes object |
| oUserObjectsMD | 206 | UserObjectsMD object |
| oTeams | 211 | Teams object |
| oRelationships | 212 | Relationships object |
| oUserPermissionTree | 214 | UserPermissionTree object |
| oActivityStatus | 217 | ActivityStatus object |
| oChooseFromList | 218 | ChooseFromList object |
| oFormattedSearches | 219 | FormattedSearches object |
| oAttachments2 | 221 | Attachments2 object |
| oUserLanguages | 223 | UserLanguages object |
| oMultiLanguageTranslations | 224 | MultiLanguageTranslations object |
| oDynamicSystemStrings | 229 | DynamicSystemStrings object |
| oHouseBankAccounts | 231 | HouseBankAccounts object |
| oBusinessPlaces | 247 | BusinessPlaces object |
| oLocalEra | 250 | LocalEra object |
| oSalesTaxInvoice | 280 | Sales tax invoice object (see TaxInvoices object and DocType property with the valid value botit_Invoice) |
| oPurchaseTaxInvoice | 281 | Purchase tax invoice object (see TaxInvoices object and DocType property with the valid value botit_Payment) |
| BoRecordset | 300 | Recordset object |
| BoRecordsetEx | 301 | RecordRecordsetExset object |
| BoBridge | 305 | SBObob object |
| oNotaFiscalUsage | 260 | NotaFiscalUsage object |
| oNotaFiscalCFOP | 258 | NotaFiscalCFOP object |
| oNotaFiscalCST | 259 | NotaFiscalCST object |
| oClosingDateProcedure | 261 | ClosingDateProcedure object |
| oBusinessPartnerGroups | 10 | BusinessPartnerGroups object |
| oBPFiscalRegistryID | 278 | BPFiscalRegistryID object |
| oDownPayments | 203 | Documents object that represents a down payments document |
| oPurchaseDownPayments | 204 | Documents object that represents a purchase down payments document |
| oStockTransferDraft | 1179 | StockTransfer draft object |
| oPurchaseQuotations | 540000006 | Documents object that represents a purchase quotation document |
| oInventoryTransferRequest | 1250000001 | StockTransfer request object |
| oPurchaseRequest | 1470000113 | Documents object that represents a purchase request document |
| oReturnRequest | 234000031 | Documents object that represents a return request document |
| oGoodsReturnRequest | 234000032 | Documents object that represents a goods return request document |

# BoOpenIncPayment (Enumeration)

Specifies the default means of payment.

| Member | Value | Description |
|---|---|---|
| oip_No | 0 | Default means of payment is not defined. |
| oip_Cash | 1 | Default means of payment is Cash. |
| oip_Checks | 2 | Default means of payment is Checks. |
| oip_Credit | 3 | Default means of payment is Credit. |
| oip_BankTransfer | 4 | Default means of payment is Bank Transfer. |

# BoOpexStatus (Enumeration)

Specifies the payment status for each row in the OPEX table (PaymentRunExport object).

| Member | Value | Description |
|---|---|---|
| bos_Open | 0 | The payment is open. |
| bos_Close | 1 | The payment is closed. |

# BoORCTPaymentTypeEnum (Enumeration)

Payment types.

| Member | Value | Description |
|---|---|---|
| bopt_None | 0 | No payment type |
| bopt_Electronic | 1 | Electronic payment type |
| bopt_Post | 2 | Post payment type |
| bopt_Telegraph | 3 | Telegraph payment type |
| bopt_Express | 4 | Express payment type |

# BoOrientationEnum (Enumeration)

Specifies Direction Orientation.

| Member | Value | Description |
|---|---|---|
| ortVertical | 0 | Vertical Orientation. |
| ortHorizontal | 1 | Horizontal Orientation. |

# BoPaymentMeansEnum (Enumeration)

Specifies paymene means type.

| Member | Value | Description |
|---|---|---|
| bopmCheck | 0 | Payment is by Check. |
| bopmBankTransfer | 1 | Payment is by Bank Transfer. |
| bopmBillOfExchange | 2 | Payment is by Bill Of Exchange. |

# BoPaymentPriorities (Enumeration)

Specifies the payment priority.

| Member | Value | Description |
|---|---|---|
| bopp_Priority_1 | 0 | Payment priority level 1 |
| bopp_Priority_2 | 1 | Payment priority level 2 |
| bopp_Priority_3 | 2 | Payment priority level 3 |
| bopp_Priority_4 | 3 | Payment priority level 4 |
| bopp_Priority_5 | 4 | Payment priority level 5 |
| bopp_Priority_6 | 5 | Payment priority level 6 |

# BoPaymentsObjectType (Enumeration)

Defines the type of the payment document.

| Member | Value | Description |
|---|---|---|
| bopot_IncomingPayments | 0 | Incoming payments document. |
| bopot_OutgoingPayments | 1 | Outgoing payments document. |

# BoPaymentTypeEnum (Enumeration)

Specifies the payment type.

| Member | Value | Description |
|---|---|---|
| boptIncoming | 0 | Incoming payment. |
| boptOutgoing | 1 | Outgoing Payment. |

# BoPayTermDueTypes (Enumeration)

Specifies the start time for calculating the payment due date.

| Member | Value | Description |
|---|---|---|
| pdt_MonthEnd | 0 | The payment due date starts from the end of the month. |
| pdt_HalfMonth | 1 | The payment due date starts from the half of the month. |
| pdt_MonthStart | 2 | The payment due date starts from the beginning of the month. |
| pdt_None | 3 | None. |

# BoPermission (Enumeration)

Specifies the permission type assigned to the user.

| Member | Value | Description |
|---|---|---|
| boper_Full | 1 | Full authorization (Read/Write). |
| boper_ReadOnly | 2 | Read only authorization. |
| boper_None | 3 | No authorization. |
| boper_Various | 4 | Various authorizations. Relevant when the node of the authorization tree contains few branches with different authorizations. For example, a user that has Full Authorization for Item Management form and Read Only for Price Lists form then the user permission for Inventory is Various Authorizations. |
| boper_Undefined | 6 | Authorization not defined. |

# BoPickStatus (Enumeration)

Specifies the options of the pick list status.

| Member | Value | Description |
|---|---|---|
| ps_Released | 0 | The pick list is released for picking. |
| ps_Picked | 1 | All the items have been picked. |
| ps_PartiallyPicked | 2 | Only part of the items, specified in the pick list, have been picked. |
| ps_PartiallyDelivered | 3 | Part of the items have been delivered. The lines for the delivered items cannot be updated. |
| ps_Closed | 4 | The pick list is closed. No additional items can be picked or delivered. |

# BoPictureSizeEnum (Enumeration)

Specifies the options available for modiffieng picture size in the Report Layout.

| Member | Value | Description |
|---|---|---|
| rlpsOriginalSize | 0 | Use the picture original size. |
| rlpsFitFieldSizeNonProportionally | 1 | Fit field size non proportionally. |
| rlpsFitFieldSizeProportionally | 2 | Fit field size proportionally. |
| rlpsFitFieldHeight | 3 | Fit field Hight. |
| rlpsFitFieldWidth | 4 | Fit field width. |

# BoPlanningSystem (Enumeration)

Defines the default inventory planning system.

| Member | Value | Description |
|---|---|---|
| bop_MRP | 0 | Material Requirement Planning system. |
| bop_None | 1 | No planning system. |

# BoPriceListGroupNum (Enumeration)

Defines the group numbers to which price lists are related.

| Member | Value | Description |
|---|---|---|
| boplgn_Group1 | 0 | Price list group 0. |
| boplgn_Group2 | 1 | Price list group 1. |
| boplgn_Group3 | 2 | Price list group 2. |
| boplgn_Group4 | 3 | Price list group 3. |

# BoPrintReceiptEnum (Enumeration)

Specifies when to print a payment with invoice.

| Member | Value | Description |
|---|---|---|
| boprcAlways | 0 | Always print the payment with the invoice. |
| boprcOnlyWhenAdding | 1 | Print a payment with the invoice only when adding the payment. |
| boprcNo | 2 | Do not print a payment with the invoice. |

# BoProcurementMethod (Enumeration)

Defines the procurement method of items.

| Member | Value | Description |
|---|---|---|
| bom_Buy | 0 | Buy the items from vendors. |
| bom_Make | 1 | Make the items. |

# BoProductionOrderOriginEnum (Enumeration)

Specifies the origin options for creating a production order.

| Member | Value | Description |
|---|---|---|
| bopooManual | 0 | The production order is created manually by an authorized user. |
| bopooMRP | 1 | The production order is created automatically based on an MRP report recommendation. |
| bopooSalesOrder | 2 | The production order is based on a sales order. |
| bopooProductionOrder | 3 |  |

# BoProductionOrderStatusEnum (Enumeration)

Specifies the status options of a production order.

| Member | Value | Description |
|---|---|---|
| boposPlanned | 0 | Indicates the initial stage of the production. |
| boposReleased | 1 | Indicates the release state of the product. That is, the order to the production floor for work. This is the status at which receipts and issues are transacted. |
| boposClosed | 2 | Closed: you close the production order when all transactions have been completed. |
| boposCancelled | 3 | Cancelled: the production order is removed from the list before the production process starts |
