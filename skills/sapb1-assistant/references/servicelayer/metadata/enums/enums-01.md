<!-- source: Service Layer /b1s/v2/$metadata | version: SAP Business One 10.0 FP 2602 | verified: 2026-10-05 -->

# SAPB1.AccountCategorySourceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| acsBalanceSheet | 0 |  |
| acsProfitAndLoss | 1 |  |
| acsTrialBalance | 2 |  |

# SAPB1.AccountSegmentationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ast_Alphanumeric | 0 |  |
| ast_Numeric | 1 |  |

# SAPB1.AcquisitionPeriodControlEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| apcProRataTemporis | 0 |  |
| apcFirstYearConvention | 1 |  |
| apcHalfYear | 2 |  |
| apcFullYear | 3 |  |

# SAPB1.AcquisitionProRataTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| aprtExactlyDailyBase | 0 |  |
| aprtFirstDayOfCurrentPeriod | 1 |  |
| aprtFirstDayOfNextPeriod | 2 |  |

# SAPB1.ActivityRecipientObjTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| arotUser | 0 |  |
| arotEmployee | 1 |  |
| arotRecipientList | 2 |  |

# SAPB1.AlertManagementDocumentEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atd_NOB | 0 |  |
| atd_Invoices | 1 |  |
| atd_RevertInvoice | 2 |  |
| atd_DeliveryNotes | 3 |  |
| atd_Returns | 4 |  |
| atd_Orders | 5 |  |
| atd_PurchaseInvoices | 6 |  |
| atd_PurchaseDeliveryNotes | 7 |  |
| atd_PurchaseOrders | 8 |  |
| atd_Quotations | 9 |  |
| atd_IncomingPayments | 10 |  |
| atd_JournalEntries | 11 |  |
| atd_OutgoingPayments | 12 |  |
| atd_ChecksForPayment | 13 |  |
| atd_CorrectionInvoice | 14 |  |
| atd_DownPaymentIncoming | 15 |  |
| atd_DownPaymentOutgoing | 16 |  |

# SAPB1.AlertManagementFrequencyType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atfi_Minutes | 0 |  |
| atfi_Hours | 1 |  |
| atfi_Days | 2 |  |
| atfi_Weeks | 3 |  |
| atfi_Monthly | 4 |  |

# SAPB1.AlertManagementPriorityEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atp_Low | 0 |  |
| atp_Normal | 1 |  |
| atp_High | 2 |  |

# SAPB1.AlertManagementTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| att_User | 0 |  |
| att_System | 1 |  |

# SAPB1.AmountCatTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| act_Open | 0 |  |
| act_Invoiced | 1 |  |

# SAPB1.ApprovalTemplateConditionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atctUndefined | 0 |  |
| atctDeviationFromCreditLine | 1 |  |
| atctDeviationFromObligo | 2 |  |
| atctGrossProfitPercent | 3 |  |
| atctDiscountPercent | 4 |  |
| atctDeviationFromBudget | 5 |  |
| atctTotalDocument | 6 |  |
| atctItemCode | 7 |  |
| atctTotalLine | 8 |  |
| atctCountedQuantity | 9 |  |
| atctQuantity | 10 |  |
| atctVariance | 11 |  |
| atctVariancePercent | 12 |  |

# SAPB1.ApprovalTemplateOperationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| opcodeUndefined | 0 |  |
| opcodeGreaterThan | 1 |  |
| opcodeGreaterOrEqual | 2 |  |
| opcodeLessThan | 3 |  |
| opcodeLessOrEqual | 4 |  |
| opcodeEqual | 5 |  |
| opcodeDoesNotEqual | 6 |  |
| opcodeInRange | 7 |  |
| opcodeNotInRange | 8 |  |

# SAPB1.ApprovalTemplatesDocumentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atdtQuotation | 23 |  |
| atdtOrder | 17 |  |
| atdtDelivery | 15 |  |
| atdtReturns | 16 |  |
| atdtArDownPayment | 203 |  |
| atdtArInvoice | 13 |  |
| atdtArCreditMemo | 14 |  |
| atdtCorrectionInvoice | 132 |  |
| atdtPurchaseOrder | 22 |  |
| atdtGoodsReceiptPO | 20 |  |
| atdtGoodsReturns | 21 |  |
| atdtApDownPayment | 204 |  |
| atdtApInvoice | 18 |  |
| atdtApCreditMemo | 19 |  |
| atdtGoodsReceipt | 59 |  |
| atdtGoodsIssue | 60 |  |
| atdtInventoryTransfer | 67 |  |
| atdtPurchaseQuotation | 540000006 |  |
| atdtInventoryTransferRequest | 1250000001 |  |
| atdtOutgoingPayment | 46 |  |
| atdtInventoryCounting | 1470000065 |  |
| atdtInventoryPosting | 10000071 |  |
| atdtInventoryOpeningBalance | 310000001 |  |
| atdtReturnRequest | 234000031 |  |
| atdtGoodsReturnRequest | 234000032 |  |
| atdtBlanketAgreement | 1250000025 |  |
| atdtSalesBlanketAgreement | 1250000026 |  |
| atdtPurchaseBlanketAgreement | 1250000027 |  |
| atdtPurchaseRequest | 1470000113 |  |
| atdtSelfInvoice | 254000065 |  |
| atdtSelfCreditMemo | 254000066 |  |

# SAPB1.AreaTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atPostingtoGL | 0 |  |
| atAdditionalArea | 1 |  |
| atDerivedArea | 2 |  |

# SAPB1.AssesseeTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atCompany | 0 |  |
| atOthers | 1 |  |

# SAPB1.AssetDocumentStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| adsPosted | 0 |  |
| adsDraft | 1 |  |
| adsCancelled | 2 |  |

# SAPB1.AssetDocumentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| adtOrdinaryDepreciation | 0 |  |
| adtUnplannedDepreciation | 1 |  |
| adtSpecialDepreciation | 2 |  |
| adtAppreciation | 3 |  |
| adtAssetTransfer | 4 |  |
| adtSales | 5 |  |
| adtScrapping | 6 |  |
| adtAssetClassTransfer | 7 |  |

# SAPB1.AssetOriginalTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| aotARInvoice | 0 |  |
| aotAPCreditMemo | 1 |  |
| aotAPInvoice | 2 |  |
| aotOutgoingPayment | 3 |  |
| aotAPCorrectionInvoice | 4 |  |
| aotCapitalization | 5 |  |
| aotFixedAssetsCreditMemo | 6 |  |
| aotAllTransactions | 7 |  |
| aotManualDepreciation | 8 |  |
| aotFixedAssetsTransfer | 9 |  |
| aotRetirement | 10 |  |

# SAPB1.AssetStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| New | 0 |  |
| Active | 1 |  |
| Inactive | 2 |  |

# SAPB1.AssetTransactionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| att_BeginningOfYear | 0 |  |
| att_Acquistion | 1 |  |
| att_Retirement | 2 |  |
| att_Transfer | 3 |  |
| att_WriteUp | 4 |  |
| att_OrdinaryDepreciation | 5 |  |
| att_UplannedDepreciation | 6 |  |
| att_SpecialDepreciation | 7 |  |
| att_EndOfYear | 8 |  |

# SAPB1.AssetTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atAssetTypeGeneral | 0 |  |
| atAssetTypeLowValueAsset | 1 |  |

# SAPB1.AttributeGroupFieldTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| agftText | 0 |  |
| agftNumeric | 1 |  |
| agftDate | 2 |  |
| agftAmount | 3 |  |
| agftPrice | 4 |  |
| agftQuantity | 5 |  |

# SAPB1.AuthenticateUserResultsEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| aturNoUserConnectedToCompany | 0 |  |
| aturUsernamePasswordMatched | 1 |  |
| aturLogOnUserNotAdmin | 2 |  |
| aturBadUserOrPassword | 3 |  |
| aturUserHasBeenLocked | 4 |  |
| aturPasswordExpired | 5 |  |
| aturDBErrors | 6 |  |
| aturWrongDomainName | 7 |  |

# SAPB1.AuthenticationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| None | 0 |  |
| Basic | 1 |  |
| OAuth | 2 |  |
| HMAC | 3 |  |

# SAPB1.AutoAllocOnReceiptMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| aaormDefaultBin | 0 |  |
| aaormItemCurrentAndHistoricalBins | 1 |  |
| aaormItemCurrentBins | 2 |  |
| aaormLastBinReceivedItem | 3 |  |

# SAPB1.AutomaticPostingEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| apNo | 0 |  |
| apInterestAndFee | 1 |  |
| apInterestOnly | 2 |  |
| apFeeOnly | 3 |  |

# SAPB1.BADivationAlertLevelEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| badal_NoWarning | 0 |  |
| badal_Warning | 1 |  |
| badal_Block | 2 |  |

# SAPB1.BADocumentStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bads_Open | 0 |  |
| bads_Closed | 1 |  |
| bads_Cancelled | 2 |  |

# SAPB1.BankStatementDocTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bsdtReceipts | 0 |  |
| bsdtPaymentToVendor | 1 |  |
| bsdtInvoices | 2 |  |
| bsdtPurchases | 3 |  |
| bsdtDownPaymentIncoming | 4 |  |
| bsdtDownPaymentOutgoing | 5 |  |
| bsdtRevertInvoices | 6 |  |
| bsdtRevertPurchases | 7 |  |
| bsdtJournalEntry | 8 |  |

# SAPB1.BankStatementRowSourceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bsImported | 0 |  |
| bsImportedAndAmended | 1 |  |
| bsManuallyEntered | 2 |  |

# SAPB1.BankStatementStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bssExecuted | 0 |  |
| bssDraft | 1 |  |
| bssOld | 2 |  |

# SAPB1.BaseDateSelectEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bdsFromDueDate | 0 |  |
| bdsFromLastDunningRun | 1 |  |

# SAPB1.BatchDetailServiceStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bdsStatus_Released | 0 |  |
| bdsStatus_NotAccessible | 1 |  |
| bdsStatus_Locked | 2 |  |

# SAPB1.BEMPeriodicTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bemPeriodic_Month | 0 |  |
| bemPeriodic_Year | 1 |  |

# SAPB1.BEMReplicationStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bemStatus_New | 0 |  |
| bemStatus_Initializing | 1 |  |
| bemStatus_InProcess | 2 |  |
| bemStatus_Complete | 3 |  |
| bemStatus_CompleteWithInconsistencies | 4 |  |
| bemStatus_Error | 5 |  |

# SAPB1.BinActionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| batToWarehouse | 1 |  |
| batFromWarehouse | 2 |  |

# SAPB1.BinLocationFieldTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| blftWarehouseSublevel | 0 |  |
| blftBinLocationAttribute | 1 |  |

# SAPB1.BinRestrictionBatchEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| brbNoRestrictions | 0 |  |
| brbSingleBatch | 1 |  |

# SAPB1.BinRestrictItemEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| briNone | 0 |  |
| briSpecificItem | 1 |  |
| briSingleItemOnly | 2 |  |
| briSpecificItemGroup | 3 |  |
| briSpecificItemGroupOnly | 4 |  |

# SAPB1.BinRestrictTransactionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| brtNoRestrictions | 0 |  |
| brtAllTrans | 1 |  |
| brtInboundTrans | 2 |  |
| brtOutboundTrans | 3 |  |
| brtAllExceptInventoryTrans | 4 |  |

# SAPB1.BinRestrictUoMEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bruNone | 0 |  |
| bruSpecificUoM | 1 |  |
| bruSingleUoMOnly | 2 |  |
| bruSpecificUoMGroup | 3 |  |
| bruSpecificUoMGroupOnly | 4 |  |

# SAPB1.BlanketAgreementBPTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atCustomer | 0 |  |
| atVendor | 1 |  |

# SAPB1.BlanketAgreementDatePeriodsEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| Daily | 0 |  |
| Weekly | 1 |  |
| Monthly | 2 |  |
| Quarterly | 3 |  |
| Semiannually | 4 |  |
| Annually | 5 |  |
| OneTime | 6 |  |

# SAPB1.BlanketAgreementDocTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ARInvoice | 0 |  |
| ARCreditMemo | 1 |  |
| Delivery | 2 |  |
| Return | 3 |  |
| SalesOrder | 4 |  |
| APInvoice | 5 |  |
| APCreditMemo | 6 |  |
| GoodsReceiptPO | 7 |  |
| GoodsReturn | 8 |  |
| PurchaseOrder | 9 |  |
| SalesQuotation | 10 |  |
| APCorrectionInvoice | 11 |  |
| APCorrectionInvoiceReversal | 12 |  |
| ARCorrectionInvoice | 13 |  |
| ARCorrectionInvoiceReversal | 14 |  |
| ARDownPayment | 15 |  |
| APDownPayment | 16 |  |
| PurchaseQuotation | 17 |  |

# SAPB1.BlanketAgreementMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| amItem | 0 |  |
| amMonetary | 1 |  |

# SAPB1.BlanketAgreementStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| asApproved | 0 |  |
| asOnHold | 1 |  |
| asDraft | 2 |  |
| asTerminated | 3 |  |
| asCancelled | 4 |  |

# SAPB1.BlanketAgreementTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atGeneral | 0 |  |
| atSpecific | 1 |  |

# SAPB1.BoAccountTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| at_Revenues | 0 |  |
| at_Expenses | 1 |  |
| at_Other | 2 |  |

# SAPB1.BoActivities (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cn_Conversation | 0 |  |
| cn_Meeting | 1 |  |
| cn_Task | 2 |  |
| cn_Other | 3 |  |
| cn_Note | 4 |  |
| cn_Campaign | 5 |  |
| cn_Email | 6 |  |

# SAPB1.BoAddressType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bo_ShipTo | 0 |  |
| bo_BillTo | 1 |  |

# SAPB1.BoAdEpnsDistribMethods (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| aedm_None | 0 |  |
| aedm_Quantity | 1 |  |
| aedm_Volume | 2 |  |
| aedm_Weight | 3 |  |
| aedm_Equally | 4 |  |
| aedm_RowTotal | 5 |  |

# SAPB1.BoAdEpnsTaxTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| aext_NormalTax | 0 |  |
| aext_NoTax | 1 |  |
| aext_UseTax | 2 |  |

# SAPB1.BoAeDistMthd (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| aed_Equally | 0 |  |
| aed_LineTotal | 1 |  |
| aed_None | 2 |  |
| aed_Quantity | 3 |  |
| aed_Volume | 4 |  |
| aed_Weight | 5 |  |

# SAPB1.BoAlertTypeforWHStockEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| atfwhs_WarningOnly | 0 |  |
| atfwhs_Block | 1 |  |
| atfwhs_NoMessage | 2 |  |

# SAPB1.BoAllocationByEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ab_CashValueAfterCustoms | 0 |  |
| ab_CashValueBeforeCustoms | 1 |  |
| ab_Equal | 2 |  |
| ab_Quantity | 3 |  |
| ab_Volume | 4 |  |
| ab_Weight | 5 |  |

# SAPB1.BoAPARDocumentTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bodt_Invoice | 13 |  |
| bodt_CreditNote | 14 |  |
| bodt_DeliveryNote | 15 |  |
| bodt_Return | 16 |  |
| bodt_Order | 17 |  |
| bodt_PurchaseInvoice | 18 |  |
| bodt_PurchaseCreditNote | 19 |  |
| bodt_PurchaseDeliveryNote | 20 |  |
| bodt_PurchaseReturn | 21 |  |
| bodt_PurchaseOrder | 22 |  |
| bodt_Quotation | 23 |  |
| bodt_CorrectionAPInvoice | 163 |  |
| bodt_CorrectionARInvoice | 165 |  |
| bodt_Zero | 166 |  |
| bodt_MinusOne | 167 |  |
| bodt_PurchaseQutation | 540000006 |  |

# SAPB1.BoApprovalRequestDecisionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ardPending | 0 |  |
| ardApproved | 1 |  |
| ardNotApproved | 2 |  |

# SAPB1.BoApprovalRequestStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| arsPending | 0 |  |
| arsApproved | 1 |  |
| arsNotApproved | 2 |  |
| arsGenerated | 3 |  |
| arsGeneratedByAuthorizer | 4 |  |
| arsCancelled | 5 |  |

# SAPB1.BoBarCodeStandardEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlbsan13 | 0 |  |
| rlbsCode39 | 1 |  |
| rlbsCode128 | 2 |  |

# SAPB1.BoBaseDateRateEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bdr_PostingDate | 0 |  |
| bdr_TaxDate | 1 |  |

# SAPB1.BoBaselineDate (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bld_PostingDate | 0 |  |
| bld_SystemDate | 1 |  |
| bld_TaxDate | 2 |  |
| bld_ClosingDate | 3 |  |

# SAPB1.BoBlockBudget (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bb_OnlyAnnualAlert | 0 |  |
| bb_MonthlyAlertOnly | 1 |  |
| bb_Block | 2 |  |

# SAPB1.BoBoeStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boes_Created | 0 |  |
| boes_Sent | 1 |  |
| boes_Deposited | 2 |  |
| boes_Paid | 3 |  |
| boes_Cancelled | 4 |  |
| boes_Closed | 5 |  |
| boes_Failed | 6 |  |

# SAPB1.BoBOETypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bobt_Incoming | 0 |  |
| bobt_Outgoing | 1 |  |

# SAPB1.BoBOTFromStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| btfs_Sent | 0 |  |
| btfs_Generated | 1 |  |
| btfs_Deposited | 2 |  |
| btfs_Paid | 3 |  |

# SAPB1.BoBOTToStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| btts_Canceled | 0 |  |
| btts_Generated | 1 |  |
| btts_Deposit | 2 |  |
| btts_Paid | 3 |  |
| btts_Failed | 4 |  |
| btts_Closed | 5 |  |

# SAPB1.BoBpAccountTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bpat_General | 0 |  |
| bpat_DownPayment | 1 |  |
| bpat_AssetsAccount | 2 |  |
| bpat_Receivable | 3 |  |
| bpat_Payable | 4 |  |
| bpat_OnCollection | 5 |  |
| bpat_Presentation | 6 |  |
| bpat_AssetsPayable | 7 |  |
| bpat_Discounted | 8 |  |
| bpat_Unpaid | 9 |  |
| bpat_OpenDebts | 10 |  |
| bpat_Domestic | 11 |  |
| bpat_Foreign | 12 |  |
| bpat_CashDiscountInterim | 13 |  |
| bpat_ExchangeRateInterim | 14 |  |

# SAPB1.BoBpsDocTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bpdt_PaymentReference | 0 |  |
| bpdt_ISR | 1 |  |
| bpdt_DocNum | 2 |  |

# SAPB1.BoBudgetAlert (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ba_AnnualAlert | 0 |  |
| ba_MonthlyAlert | 1 |  |

# SAPB1.BoBusinessAreaEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| baSales | 0 |  |
| baPurchase | 1 |  |
| baSalesAndPurchase | 2 |  |

# SAPB1.BoBusinessPartnerGroupTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bbpgt_CustomerGroup | 0 |  |
| bbpgt_VendorGroup | 1 |  |

# SAPB1.BoBusinessPartnerTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| garAll | 0 |  |
| garCompany | 1 |  |
| garPrivate | 2 |  |
| garGovernment | 3 |  |

# SAPB1.BoCardCompanyTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cCompany | 0 |  |
| cPrivate | 1 |  |
| cGovernment | 2 |  |
| cEmployee | 3 |  |
| cSoleTaxableSubject | 4 |  |

# SAPB1.BoCardTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cCustomer | 0 |  |
| cSupplier | 1 |  |
| cLid | 2 |  |

# SAPB1.BoChangeLogEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| clChartOfAccounts | 0 |  |
| clBusinessPartners | 1 |  |
| clItems | 2 |  |
| clVatGroups | 3 |  |
| clUsers | 4 |  |
| clInvoices | 5 |  |
| clCreditNotes | 6 |  |
| clDeliveryNotes | 7 |  |
| clReturns | 8 |  |
| clOrders | 9 |  |
| clPurchaseInvoices | 10 |  |
| clPurchaseCreditNotes | 11 |  |
| clPurchaseDeliveryNotes | 12 |  |
| clPurchaseReturns | 13 |  |
| clPurchaseOrders | 14 |  |
| clQuotations | 15 |  |
| clIncomingPayments | 16 |  |
| clJournalEntries | 17 |  |
| clCreditCards | 18 |  |
| clAdminInfo | 19 |  |
| clVendorPayments | 20 |  |
| clItemGroups | 21 |  |
| clInventoryGeneralEntry | 22 |  |
| clInventoryGeneralExit | 23 |  |
| clWarehouses | 24 |  |
| clProductTrees | 25 |  |
| clStockTransfers | 26 |  |
| clFinancePeriods | 27 |  |
| clAdditionalExpenses | 28 |  |
| clPickLists | 29 |  |
| clMaterialRevaluation | 30 |  |
| clCorrectionPurchaseInvoice | 31 |  |
| clCorrectionPurchaseInvoiceReversal | 32 |  |
| clCorrectionInvoice | 33 |  |
| clCorrectionInvoiceReversal | 34 |  |
| clEmployeesInfo | 35 |  |
| clCustomerEquipmentCards | 36 |  |
| clWithholdingTaxCodes | 37 |  |
| clBillOfExchange | 38 |  |
| clServiceCalls | 39 |  |
| clProductionOrders | 40 |  |
| clDownPayments | 41 |  |
| clPurchaseDownPayments | 42 |  |
| clPeriodCategory | 43 |  |
| clHouseBankAccounts | 44 |  |
| clSalesTaxInvoice | 45 |  |
| clPurchaseTaxInvoice | 46 |  |
| clExternalBankOperationCodes | 47 |  |
| clInternalBankOperationCodes | 48 |  |
| clOutgoingExciseInvoice | 49 |  |
| clIncomingExciseInvoice | 50 |  |
| clInventoryTransferRequests | 51 |  |
| clPurchaseQuotation | 52 |  |
| clActivities | 53 |  |
| clChecksForPayment | 54 |  |
| clServiceContract | 55 |  |
| clUDO | 100 |  |

# SAPB1.BoCheckDepositTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cdtCashChecks | 0 |  |
| cdtPostdatedChecks | 1 |  |

# SAPB1.BoClosingDateProcedureBaseDateEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bocpdbld_BaseSystemDate | 0 |  |
| bocpdbld_PostingDate | 1 |  |

# SAPB1.BoClosingDateProcedureDueMonthEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bocpddm_HalfMonth | 0 |  |
| bocpddm_MonthEnd | 1 |  |
| bocpddm_MonthStart | 2 |  |
| bocpddm_None | 3 |  |

# SAPB1.BoCockpitTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cptt_UserCockpit | 0 |  |
| cptt_TemplateCockpit | 1 |  |

# SAPB1.BoConsumptionMethod (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cm_BackwardForward | 0 |  |
| cm_ForwardBackward | 1 |  |

# SAPB1.BoContractTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ct_Customer | 0 |  |
| ct_ItemGroup | 1 |  |
| ct_SerialNumber | 2 |  |

# SAPB1.BoCorInvItemStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ciis_Was | 0 |  |
| ciis_ShouldBe | 1 |  |

# SAPB1.BoCpCardAcct (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cfp_Card | 0 |  |
| cfp_Account | 1 |  |

# SAPB1.BoCurrencyCheck (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cc_Block | 0 |  |
| cc_NoMessage | 1 |  |

# SAPB1.BoCurrencySources (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bocs_LocalCurrency | 0 |  |
| bocs_SystemCurrency | 1 |  |
| bocs_BPCurrency | 2 |  |

# SAPB1.BoDataOwnershipManageMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| doManageByDocOnly | 0 |  |
| doManageByBPOnly | 1 |  |
| doManageByBPnDoc | 2 |  |
| doManageByBranch | 3 |  |

# SAPB1.BoDataSourceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rldsFreeText | 0 |  |
| rldsSystemVariable | 1 |  |
| rldsDatabase | 2 |  |
| rldsFormula | 3 |  |

# SAPB1.BoDateTemplate (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dt_DDMMYY | 0 |  |
| dt_DDMMCCYY | 1 |  |
| dt_MMDDYY | 2 |  |
| dt_MMDDCCYY | 3 |  |
| dt_CCYYMMDD | 4 |  |
| dt_DDMonthYYYY | 5 |  |
| dt_YYMMDD | 6 |  |

# SAPB1.BoDeductionTaxGroupCodeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dtgcInterestReceivers | 1 |  |
| dtgcEmployeeReceivingCommission | 2 |  |
| dtgcWritersPrice | 3 |  |
| dtgcPaidServices | 6 |  |
| dtgcPaymentsToForeignCitizens | 7 |  |
| dtgcPaymentsForCitizensInForeignCountries | 8 |  |
| dtgcInvalidPaymentFromCompensationFund | 11 |  |
| dtgcRepaymentToEmployerFromCompensationFund | 12 |  |
| dtgcRentalPayments | 13 |  |
| dtgcPaymentsFromStudyFund | 14 |  |
| dtgcDividendPayments | 18 |  |

# SAPB1.BoDefaultBatchStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dbs_Released | 0 |  |
| dbs_NotAccessible | 1 |  |
| dbs_Locked | 2 |  |

# SAPB1.BoDepositAccountTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| datBankAccount | 0 |  |
| datBusinessPartner | 1 |  |

# SAPB1.BoDepositCheckEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dtNo | 0 |  |
| dcAsCash | 1 |  |
| dtAsPostdated | 2 |  |

# SAPB1.BoDepositPostingTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dpt_Collection | 0 |  |
| dpt_Discounted | 1 |  |

# SAPB1.BoDepositTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dtChecks | 0 |  |
| dtCredit | 1 |  |
| dtCash | 2 |  |
| dtBOE | 3 |  |

# SAPB1.BoDocItemType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dit_Item | 0 |  |
| dit_Resource | 1 |  |

# SAPB1.BoDocLineType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dlt_Regular | 0 |  |
| dlt_Alternative | 1 |  |
| dlt_Resource | 2 |  |

# SAPB1.BoDocSpecialLineType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dslt_Text | 0 |  |
| dslt_Subtotal | 1 |  |

# SAPB1.BoDocSummaryTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dNoSummary | 0 |  |
| dByItems | 1 |  |
| dByDocuments | 2 |  |

# SAPB1.BoDocumentLinePickStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dlps_Picked | 0 |  |
| dlps_NotPicked | 1 |  |
| dlps_ReleasedForPicking | 2 |  |
| dlps_PartiallyPicked | 3 |  |

# SAPB1.BoDocumentSubType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bod_None | 0 |  |
| bod_InvoiceExempt | 1 |  |
| bod_DebitMemo | 2 |  |
| bod_Bill | 3 |  |
| bod_ExemptBill | 4 |  |
| bod_PurchaseDebitMemo | 5 |  |
| bod_ExportInvoice | 6 |  |
| bod_GSTTaxInvoice | 7 |  |
| bod_GSTDebitMemo | 8 |  |
| bod_RefundVoucher | 9 |  |

# SAPB1.BoDocumentTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dDocument_Items | 0 |  |
| dDocument_Service | 1 |  |

# SAPB1.BoDocWhsAutoIssueMethod (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| whsBinSingleChoiceOnly | 0 |  |
| whsBinBinCodeOrder | 1 |  |
| whsBinAltSortCodeOrder | 2 |  |
| whsBinQtyDescendingOrder | 3 |  |
| whsBinQtyAscendingOrder | 4 |  |
| whsBinFIFO | 5 |  |
| whsBinLIFO | 6 |  |
| whsBinSingleBinPreferred | 7 |  |

# SAPB1.BoDocWhsUpdateTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dwh_No | 0 |  |
| dwh_OrdersFromVendors | 1 |  |
| dwh_CustomerOrders | 2 |  |
| dwh_Consignment | 3 |  |
| dwh_Stock | 4 |  |

# SAPB1.BoDueDateEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boddDateOfPaymentRun | 0 |  |
| boddDueDateOfInvoice | 1 |  |
| boddPaymentTerms | 2 |  |

# SAPB1.BoDurations (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| du_Seconds | -1 |  |
| du_Minuts | 0 |  |
| du_Hours | 1 |  |
| du_Days | 2 |  |

# SAPB1.BoEquipmentBPType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| et_Sales | 1 |  |
| et_Purchasing | 2 |  |
| et_SalesAndPurchasing | 3 |  |

# SAPB1.BoExpenseOperationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bo_ExpOpType_ProfessionalServices | 0 |  |
| bo_ExpOpType_RentingAssets | 1 |  |
| bo_ExpOpType_Others | 2 |  |
| bo_ExpOpType_None | 3 |  |
| bo_ExpOpType_DisposalOfGoods | 4 |  |
| bo_ExpOpType_ImportOfGoodsAndServices | 5 |  |
| bo_ExpOpType_ImportByVirtualTransfer | 6 |  |
| bo_ExpOpType_GlobalOperations | 7 |  |

# SAPB1.BoExtensionErrorActionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| eeaStop | 0 |  |
| eeaIgnore | 1 |  |
| eeaPrompt | 2 |  |

# SAPB1.BoFatherCardTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cPayments_sum | 0 |  |
| cDelivery_sum | 1 |  |

# SAPB1.BoFieldTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| db_Alpha | 0 |  |
| db_Memo | 1 |  |
| db_Numeric | 2 |  |
| db_Date | 3 |  |
| db_Float | 4 |  |

# SAPB1.BoFldSubTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| st_None | 0 |  |
| st_Address | 63 |  |
| st_Phone | 35 |  |
| st_Time | 84 |  |
| st_Rate | 82 |  |
| st_Sum | 83 |  |
| st_Price | 80 |  |
| st_Quantity | 81 |  |
| st_Percentage | 37 |  |
| st_Measurement | 77 |  |
| st_Link | 66 |  |
| st_Image | 73 |  |
| st_Checkbox | 67 |  |

# SAPB1.BoForecastViewType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| fvtDaily | 0 |  |
| fvtWeekly | 1 |  |
| fvtMonthly | 2 |  |

# SAPB1.BoFormattedSearchActionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bofsaNone | 0 |  |
| bofsaValidValues | 1 |  |
| bofsaQuery | 2 |  |

# SAPB1.BoFrequency (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bof_Daily | 0 |  |
| bof_Weekly | 1 |  |
| bof_Every4Weeks | 2 |  |
| bof_Monthly | 3 |  |
| bof_Quarterly | 4 |  |
| bof_HalfYearly | 5 |  |
| bof_Annually | 6 |  |
| bof_OneTime | 7 |  |
| bof_EveryXDays | 8 |  |

# SAPB1.BoFrequencyTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ftDaily | 0 |  |
| ftWeekly | 1 |  |
| ftMonthly | 2 |  |
| ftQuarterly | 3 |  |
| ftSemiannually | 4 |  |
| ftAnnually | 5 |  |
| ftOneTime | 6 |  |
| ftTemplate | 7 |  |
| ftNotExecuted | 8 |  |

# SAPB1.BoGenderTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gt_Female | 0 |  |
| gt_Male | 1 |  |
| gt_Undefined | 2 |  |
| gt_Masked | 3 |  |
| gt_Invalid | 4 |  |

# SAPB1.BoGLMethods (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| glm_WH | 0 |  |
| glm_ItemClass | 1 |  |
| glm_ItemLevel | 2 |  |

# SAPB1.BoGridTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gtCombination | 0 |  |
| gtContinuousLine | 1 |  |
| gtBrokenLine | 2 |  |
| gtDots | 3 |  |

# SAPB1.BoGSTRegnTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| invalid | 0 |  |
| gstRegularTDSISD | 1 |  |
| gstCasualTaxablePerson | 2 |  |
| gstCompositionLevy | 3 |  |
| gstGoverDepartPSU | 4 |  |
| gstNonResidentTaxablePerson | 5 |  |
| gstUNAgencyEmbassy | 6 |  |

# SAPB1.BoHorizontalAlignmentEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlhjRight | 0 |  |
| rlhjLeft | 1 |  |
| rlhjCentralized | 2 |  |
| rlhjLanguageDependent | 3 |  |

# SAPB1.BoInterimDocTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boidt_None | 0 |  |
| boidt_ExchangeRate | 1 |  |
| boidt_CashDiscount | 2 |  |

# SAPB1.BoInventorySystem (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bis_MovingAverage | 0 |  |
| bis_Standard | 1 |  |
| bis_FIFO | 2 |  |
| bis_SNB | 3 |  |

# SAPB1.BoIssueMethod (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| im_Backflush | 0 |  |
| im_Manual | 1 |  |

# SAPB1.BoItemTreeTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| iNotATree | 0 |  |
| iAssemblyTree | 1 |  |
| iSalesTree | 2 |  |
| iProductionTree | 3 |  |
| iTemplateTree | 4 |  |
| iIngredient | 5 |  |

# SAPB1.BoLineBreakEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlsAllowOverflow | 0 |  |
| rlsAdjustToCell | 1 |  |
| rlsDivideIntoRows | 2 |  |

# SAPB1.BoManageMethod (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bomm_OnEveryTransaction | 0 |  |
| bomm_OnReleaseOnly | 1 |  |

# SAPB1.BoMaterialTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| mt_GoodsForReseller | 0 |  |
| mt_FinishedGoods | 1 |  |
| mt_GoodsInProcess | 2 |  |
| mt_RawMaterial | 3 |  |
| mt_Package | 4 |  |
| mt_SubProduct | 5 |  |
| mt_IntermediateMaterial | 6 |  |
| mt_ConsumerMaterial | 7 |  |
| mt_FixedAsset | 8 |  |
| mt_Service | 9 |  |
| mt_OtherInput | 10 |  |
| mt_Other | 99 |  |

# SAPB1.BoMeritalStatuses (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| mts_Single | 0 |  |
| mts_Married | 1 |  |
| mts_Divorced | 2 |  |
| mts_Widowed | 3 |  |
| mts_NotSpecified | 4 |  |

# SAPB1.BoMoneyPrecisionTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| mpt_Sum | 0 |  |
| mpt_Price | 1 |  |
| mpt_Rate | 2 |  |
| mpt_Quantity | 3 |  |
| mpt_Percent | 4 |  |
| mpt_Measure | 5 |  |
| mpt_Tax | 6 |  |

# SAPB1.BoMRPComponentWarehouse (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bomcw_BOM | 0 |  |
| bomcw_Parent | 1 |  |

# SAPB1.BoMsgPriorities (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pr_Low | 0 |  |
| pr_Normal | 1 |  |
| pr_High | 2 |  |

# SAPB1.BoMsgRcpTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rt_RandomUser | -1 |  |
| rt_ContactPerson | 11 |  |
| rt_InternalUser | 12 |  |

# SAPB1.BoMYFTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| myft_WholesaleSales | 0 |  |
| myft_RetailSales | 1 |  |
| myft_WholesalePurchases | 2 |  |
| myft_OtherExpenseTransactions | 3 |  |

# SAPB1.BoObjectTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| oChartOfAccounts | 1 |  |
| oBusinessPartners | 2 |  |
| oBanks | 3 |  |
| oItems | 4 |  |
| oVatGroups | 5 |  |
| oPriceLists | 6 |  |
| oSpecialPrices | 7 |  |
| oItemProperties | 8 |  |
| oBusinessPartnerGroups | 10 |  |
| oUsers | 12 |  |
| oInvoices | 13 |  |
| oCreditNotes | 14 |  |
| oDeliveryNotes | 15 |  |
| oReturns | 16 |  |
| oOrders | 17 |  |
| oPurchaseInvoices | 18 |  |
| oPurchaseCreditNotes | 19 |  |
| oPurchaseDeliveryNotes | 20 |  |
| oPurchaseReturns | 21 |  |
| oPurchaseOrders | 22 |  |
| oQuotations | 23 |  |
| oIncomingPayments | 24 |  |
| oJournalVouchers | 28 |  |
| oJournalEntries | 30 |  |
| oStockTakings | 31 |  |
| oContacts | 33 |  |
| oCreditCards | 36 |  |
| oCurrencyCodes | 37 |  |
| oPaymentTermsTypes | 40 |  |
| oBankPages | 42 |  |
| oManufacturers | 43 |  |
| oVendorPayments | 46 |  |
| oLandedCostsCodes | 48 |  |
| oShippingTypes | 49 |  |
| oLengthMeasures | 50 |  |
| oWeightMeasures | 51 |  |
| oItemGroups | 52 |  |
| oSalesPersons | 53 |  |
| oCustomsGroups | 56 |  |
| oChecksforPayment | 57 |  |
| oInventoryGenEntry | 59 |  |
| oInventoryGenExit | 60 |  |
| oWarehouses | 64 |  |
| oCommissionGroups | 65 |  |
| oProductTrees | 66 |  |
| oStockTransfer | 67 |  |
| oWorkOrders | 68 |  |
| oCreditPaymentMethods | 70 |  |
| oCreditCardPayments | 71 |  |
| oAlternateCatNum | 73 |  |
| oBudget | 77 |  |
| oBudgetDistribution | 78 |  |
| oMessages | 81 |  |
| oBudgetScenarios | 91 |  |
| oUserDefaultGroups | 93 |  |
| oSalesOpportunities | 97 |  |
| oSalesStages | 101 |  |
| oActivityTypes | 103 |  |
| oActivityLocations | 104 |  |
| oDrafts | 112 |  |
| oDeductionTaxHierarchies | 116 |  |
| oDeductionTaxGroups | 117 |  |
| oAdditionalExpenses | 125 |  |
| oSalesTaxAuthorities | 126 |  |
| oSalesTaxAuthoritiesTypes | 127 |  |
| oSalesTaxCodes | 128 |  |
| oQueryCategories | 134 |  |
| oFactoringIndicators | 138 |  |
| oPaymentsDrafts | 140 |  |
| oAccountSegmentations | 142 |  |
| oAccountSegmentationCategories | 143 |  |
| oWarehouseLocations | 144 |  |
| oForms1099 | 145 |  |
| oInventoryCycles | 146 |  |
| oWizardPaymentMethods | 147 |  |
| oBPPriorities | 150 |  |
| oDunningLetters | 151 |  |
| oUserFields | 152 |  |
| oUserTables | 153 |  |
| oPickLists | 156 |  |
| oPaymentRunExport | 158 |  |
| oUserQueries | 160 |  |
| oMaterialRevaluation | 162 |  |
| oCorrectionPurchaseInvoice | 163 |  |
| oCorrectionPurchaseInvoiceReversal | 164 |  |
| oCorrectionInvoice | 165 |  |
| oCorrectionInvoiceReversal | 166 |  |
| oContractTemplates | 170 |  |
| oEmployeesInfo | 171 |  |
| oCustomerEquipmentCards | 176 |  |
| oWithholdingTaxCodes | 178 |  |
| oBillOfExchangeTransactions | 182 |  |
| oKnowledgeBaseSolutions | 189 |  |
| oServiceContracts | 190 |  |
| oServiceCalls | 191 |  |
| oUserKeys | 193 |  |
| oQueue | 194 |  |
| oSalesForecast | 198 |  |
| oTerritories | 200 |  |
| oIndustries | 201 |  |
| oProductionOrders | 202 |  |
| oDownPayments | 203 |  |
| oPurchaseDownPayments | 204 |  |
| oPackagesTypes | 205 |  |
| oUserObjectsMD | 206 |  |
| oTeams | 211 |  |
| oRelationships | 212 |  |
| oUserPermissionTree | 214 |  |
| oActivityStatus | 217 |  |
| oChooseFromList | 218 |  |
| oFormattedSearches | 219 |  |
| oAttachments2 | 221 |  |
| oUserLanguages | 223 |  |
| oMultiLanguageTranslations | 224 |  |
| oDynamicSystemStrings | 229 |  |
| oHouseBankAccounts | 231 |  |
| oBusinessPlaces | 247 |  |
| oLocalEra | 250 |  |
| oNotaFiscalCFOP | 258 |  |
| oNotaFiscalCST | 259 |  |
| oNotaFiscalUsage | 260 |  |
| oClosingDateProcedure | 261 |  |
| oBPFiscalRegistryID | 278 |  |
| oSalesTaxInvoice | 280 |  |
| oPurchaseTaxInvoice | 281 |  |
| oPurchaseQuotations | 540000006 |  |
| oStockTransferDraft | 1179 |  |
| oInventoryTransferRequest | 1250000001 |  |
| oPurchaseRequest | 1470000113 |  |
| oReturnRequest | 234000031 |  |
| oGoodsReturnRequest | 234000032 |  |
| oSelfInvoice | 254000065 |  |
| oSelfCreditMemo | 254000066 |  |

# SAPB1.BoOpenIncPayment (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| oip_No | 0 |  |
| oip_Cash | 1 |  |
| oip_Checks | 2 |  |
| oip_Credit | 3 |  |
| oip_BankTransfer | 4 |  |

# SAPB1.BoOperationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rloNone | 0 |  |
| rloAddition | 1 |  |
| rloSubtraction | 2 |  |
| rloMultiplication | 3 |  |
| rloDivision | 4 |  |
| rloPercentage | 5 |  |
| rloLeftPartCharacters | 6 |  |
| rloRightPartMantissa | 7 |  |
| rloRound | 8 |  |
| rloConcat | 9 |  |
| rloRight | 10 |  |
| rloLeft | 11 |  |
| rloSentence | 12 |  |
| rloLength | 13 |  |
| rloCurrency | 14 |  |
| rloNumber | 15 |  |
| rloLessThan | 16 |  |
| rloLessOrEqual | 17 |  |
| rloEqual | 18 |  |
| rloNotEqual | 19 |  |
| rloGreaterOrEqual | 20 |  |
| rloGreaterThan | 21 |  |

# SAPB1.BoOpexStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bos_Open | 0 |  |
| bos_Close | 1 |  |

# SAPB1.BoORCTPaymentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bopt_None | 0 |  |
| bopt_Electronic | 1 |  |
| bopt_Post | 2 |  |
| bopt_Telegraph | 3 |  |
| bopt_Express | 4 |  |

# SAPB1.BoOrientationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ortVertical | 0 |  |
| ortHorizontal | 1 |  |

# SAPB1.BoOSWACategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boswaMCAPrimaria | 0 |  |
| boswaPDLScelta | 1 |  |
| boswaMSEsterno | 2 |  |
| boswaMDMDSATDeterminato | 3 |  |
| boswaMDETATDeterminato | 4 |  |
| boswaMDCATDeterminato | 5 |  |
| boswaIPDOOccasionali | 6 |  |

# SAPB1.BoPaymentMeansEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bopmCheck | 0 |  |
| bopmBankTransfer | 1 |  |
| bopmBillOfExchange | 2 |  |

# SAPB1.BoPaymentPriorities (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bopp_Priority_1 | 0 |  |
| bopp_Priority_2 | 1 |  |
| bopp_Priority_3 | 2 |  |
| bopp_Priority_4 | 3 |  |
| bopp_Priority_5 | 4 |  |
| bopp_Priority_6 | 5 |  |

# SAPB1.BoPaymentsObjectType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bopot_IncomingPayments | 0 |  |
| bopot_OutgoingPayments | 1 |  |

# SAPB1.BoPaymentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boptIncoming | 0 |  |
| boptOutgoing | 1 |  |

# SAPB1.BoPayTermDueTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pdt_MonthEnd | 0 |  |
| pdt_HalfMonth | 1 |  |
| pdt_MonthStart | 2 |  |
| pdt_None | 3 |  |

# SAPB1.BoPermission (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boper_Full | 1 |  |
| boper_ReadOnly | 2 |  |
| boper_None | 3 |  |
| boper_Various | 4 |  |
| boper_Undefined | 6 |  |

# SAPB1.BoPickStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ps_Released | 0 |  |
| ps_Picked | 1 |  |
| ps_PartiallyPicked | 2 |  |
| ps_PartiallyDelivered | 3 |  |
| ps_Closed | 4 |  |

# SAPB1.BoPictureSizeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlpsOriginalSize | 0 |  |
| rlpsFitFieldSizeNonProportionally | 1 |  |
| rlpsFitFieldSizeProportionally | 2 |  |
| rlpsFitFieldHeight | 3 |  |
| rlpsFitFieldWidth | 4 |  |

# SAPB1.BoPlanningSystem (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bop_MRP | 0 |  |
| bop_None | 1 |  |

# SAPB1.BoPriceListGroupNum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boplgn_Group1 | 0 |  |
| boplgn_Group2 | 1 |  |
| boplgn_Group3 | 2 |  |
| boplgn_Group4 | 3 |  |

# SAPB1.BoPrintReceiptEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boprcAlways | 0 |  |
| boprcNo | 1 |  |
| boprcOnlyWhenAdding | 2 |  |

# SAPB1.BoProcurementMethod (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bom_Buy | 0 |  |
| bom_Make | 1 |  |

# SAPB1.BoProductionOrderOriginEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bopooManual | 0 |  |
| bopooMRP | 1 |  |
| bopooSalesOrder | 2 |  |
| bopooProductionOrder | 3 |  |

# SAPB1.BoProductionOrderStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boposPlanned | 0 |  |
| boposReleased | 1 |  |
| boposClosed | 2 |  |
| boposCancelled | 3 |  |

# SAPB1.BoProductionOrderTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bopotStandard | 0 |  |
| bopotSpecial | 1 |  |
| bopotDisassembly | 2 |  |

# SAPB1.BoProductSources (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bps_PurchasedFromDomVendor | 1 |  |
| bps_ImportedByCompany | 2 |  |
| bps_ImportedGoodsPurchasedFromDomVendor | 3 |  |
| bps_ProducedByCompany | 4 |  |

# SAPB1.BoPublicDirectoryStatusTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pds_ActivePrivateEntry | 0 |  |
| pds_ActivePublicEntry | 1 |  |
| pds_InactivePrivateEntry | 2 |  |
| pds_InactivePublicEntry | 3 |  |
| pds_NotRegistered | 4 |  |

# SAPB1.BoQueryTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| qtRegular | 0 |  |
| qtWizard | 1 |  |

# SAPB1.BoRcptCredTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cr_Regular | 0 |  |
| cr_Telephone | 1 |  |
| cr_InternetTransaction | 2 |  |

# SAPB1.BoRcptInvTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| it_AllTransactions | -1 |  |
| it_OpeningBalance | -2 |  |
| it_ClosingBalance | -3 |  |
| it_Invoice | 13 |  |
| it_CredItnote | 14 |  |
| it_TaxInvoice | 15 |  |
| it_Return | 16 |  |
| it_PurchaseInvoice | 18 |  |
| it_PurchaseCreditNote | 19 |  |
| it_PurchaseDeliveryNote | 20 |  |
| it_PurchaseReturn | 21 |  |
| it_Receipt | 24 |  |
| it_Deposit | 25 |  |
| it_JournalEntry | 30 |  |
| it_PaymentAdvice | 46 |  |
| it_ChequesForPayment | 57 |  |
| it_StockReconciliations | 58 |  |
| it_GeneralReceiptToStock | 59 |  |
| it_GeneralReleaseFromStock | 60 |  |
| it_TransferBetweenWarehouses | 67 |  |
| it_WorkInstructions | 68 |  |
| it_DeferredDeposit | 76 |  |
| it_CorrectionInvoice | 132 |  |
| it_APCorrectionInvoice | 163 |  |
| it_ARCorrectionInvoice | 165 |  |
| it_DownPayment | 203 |  |
| it_PurchaseDownPayment | 204 |  |

# SAPB1.BoRcptTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rCustomer | 0 |  |
| rAccount | 1 |  |
| rSupplier | 2 |  |

# SAPB1.BoRemindUnits (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| reu_Days | 0 |  |
| reu_Weeks | 1 |  |
| reu_Month | 2 |  |

# SAPB1.BoReportLayoutItemTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlitPageHeader | 0 |  |
| rlitStartOfReport | 1 |  |
| rlitRepetitiveAreaHeader | 2 |  |
| rlitRepetitiveArea | 3 |  |
| rlitRepetitiveAreaFooter | 4 |  |
| rlitEndOfReport | 5 |  |
| rlitPageFooter | 6 |  |
| rlitTextField | 7 |  |
| rlitPictureField | 8 |  |
| rlitUserField | 9 |  |

# SAPB1.BoResolutionUnits (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rsu_Days | 0 |  |
| rsu_Hours | 1 |  |

# SAPB1.BoResponseUnit (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boru_Day | 0 |  |
| boru_Hour | 1 |  |

# SAPB1.BoRoleInTeam (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| borit_Leader | 0 |  |
| borit_Member | 1 |  |

# SAPB1.BoRoundingMethod (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| borm_FixedEnding | 0 |  |
| borm_FixedInterval | 1 |  |
| borm_NoRounding | 2 |  |
| borm_RoundToFullAmount | 3 |  |
| borm_RoundToFullDecAmount | 4 |  |
| borm_RoundToFullTensAmount | 5 |  |

# SAPB1.BoRoundingRule (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| borrRoundDown | 0 |  |
| borrRoundOff | 1 |  |
| borrRoundUp | 2 |  |

# SAPB1.BoSalaryCostUnits (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| scu_Hour | 0 |  |
| scu_Day | 1 |  |
| scu_Week | 2 |  |
| scu_Month | 3 |  |
| scu_Year | 4 |  |
| scu_Semimonthly | 5 |  |
| scu_Biweekly | 6 |  |

# SAPB1.BoSerialNumberStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sns_Active | 0 |  |
| sns_Returned | 1 |  |
| sns_Terminated | 2 |  |
| sns_Loaned | 3 |  |
| sns_InLab | 4 |  |

# SAPB1.BoSeriesGroupEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sg_Group1 | 1 |  |
| sg_Group2 | 2 |  |
| sg_Group3 | 3 |  |
| sg_Group4 | 4 |  |
| sg_Group5 | 5 |  |
| sg_Group6 | 6 |  |
| sg_Group7 | 7 |  |
| sg_Group8 | 8 |  |
| sg_Group9 | 9 |  |
| sg_Group10 | 10 |  |

# SAPB1.BoSeriesTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| stDocument | 0 |  |
| stBusinessPartner | 1 |  |
| stItem | 2 |  |
| stResource | 3 |  |

# SAPB1.BoServicePaymentMethods (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| spmAccreditedToBankAccount | 0 |  |
| spmBankTransfer | 1 |  |
| spmOther | 2 |  |

# SAPB1.BoServiceSupplyMethods (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ssmImmediate | 0 |  |
| ssmToMoreResumptions | 1 |  |

# SAPB1.BoServiceTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bst_Regular | 0 |  |
| bst_Warranty | 1 |  |

# SAPB1.BoSoClosedInTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sos_Months | 0 |  |
| sos_Weeks | 1 |  |
| sos_Days | 2 |  |

# SAPB1.BoSoOsStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sos_Open | 0 |  |
| sos_Missed | 1 |  |
| sos_Sold | 2 |  |

# SAPB1.BoSortTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlstAlpha | 0 |  |
| rlstNumeric | 1 |  |
| rlstMoney | 2 |  |
| rlstDate | 3 |  |

# SAPB1.BoSoStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| so_Open | 0 |  |
| so_Closed | 1 |  |

# SAPB1.BoStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bost_Open | 0 |  |
| bost_Close | 1 |  |
| bost_Paid | 2 |  |
| bost_Delivered | 3 |  |

# SAPB1.BoStckTrnDir (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bos_TransferToTechnician | 0 |  |
| bos_TransferFromTechnician | 1 |  |

# SAPB1.BoSubFrequencyTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sftEmpty | 0 |  |
| sftDailyEvery1 | 1 |  |
| sftDailyEvery2 | 2 |  |
| sftDailyEvery3 | 3 |  |
| sftDailyEvery4 | 4 |  |
| sftDailyEvery5 | 5 |  |
| sftDailyEvery6 | 6 |  |
| sftDailyEvery7 | 7 |  |
| sftDailyEvery8 | 8 |  |
| sftDailyEvery9 | 9 |  |
| sftDailyEvery10 | 10 |  |
| sftDailyEvery15 | 15 |  |
| sftDailyEvery30 | 30 |  |
| sftDailyEvery45 | 45 |  |
| sftDailyEvery60 | 60 |  |
| sftWeeklyOnSunday | 1 |  |
| sftWeeklyOnMonday | 2 |  |
| sftWeeklyOnTuesday | 3 |  |
| sftWeeklyOnWednesday | 4 |  |
| sftWeeklyOnThursday | 5 |  |
| sftWeeklyOnFriday | 6 |  |
| sftWeeklyOnSaturday | 7 |  |
| sftMonthlyOn1 | 1 |  |
| sftMonthlyOn2 | 2 |  |
| sftMonthlyOn3 | 3 |  |
| sftMonthlyOn4 | 4 |  |
| sftMonthlyOn5 | 5 |  |
| sftMonthlyOn6 | 6 |  |
| sftMonthlyOn7 | 7 |  |
| sftMonthlyOn8 | 8 |  |
| sftMonthlyOn9 | 9 |  |
| sftMonthlyOn10 | 10 |  |
| sftMonthlyOn11 | 11 |  |
| sftMonthlyOn12 | 12 |  |
| sftMonthlyOn13 | 13 |  |
| sftMonthlyOn14 | 14 |  |
| sftMonthlyOn15 | 15 |  |
| sftMonthlyOn16 | 16 |  |
| sftMonthlyOn17 | 17 |  |
| sftMonthlyOn18 | 18 |  |
| sftMonthlyOn19 | 19 |  |
| sftMonthlyOn20 | 20 |  |
| sftMonthlyOn21 | 21 |  |
| sftMonthlyOn22 | 22 |  |
| sftMonthlyOn23 | 23 |  |
| sftMonthlyOn24 | 24 |  |
| sftMonthlyOn25 | 25 |  |
| sftMonthlyOn26 | 26 |  |
| sftMonthlyOn27 | 27 |  |
| sftMonthlyOn28 | 28 |  |
| sftMonthlyOn29 | 29 |  |
| sftMonthlyOn30 | 30 |  |
| sftMonthlyOn31 | 31 |  |

# SAPB1.BoSubPeriodTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| spt_Year | 0 |  |
| spt_Quarters | 1 |  |
| spt_Months | 2 |  |
| spt_Days | 3 |  |

# SAPB1.BoSuppLangs (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ln_Null | 0 |  |
| ln_Hebrew | 1 |  |
| ln_Spanish_Ar | 2 |  |
| ln_English | 3 |  |
| ln_Polish | 5 |  |
| ln_English_Sg | 6 |  |
| ln_Spanish_Pa | 7 |  |
| ln_English_Gb | 8 |  |
| ln_German | 9 |  |
| ln_Serbian | 10 |  |
| ln_Danish | 11 |  |
| ln_Norwegian | 12 |  |
| ln_Italian | 13 |  |
| ln_Hungarian | 14 |  |
| ln_Chinese | 15 |  |
| ln_Dutch | 16 |  |
| ln_Finnish | 17 |  |
| ln_Greek | 18 |  |
| ln_Portuguese | 19 |  |
| ln_Swedish | 20 |  |
| ln_English_Cy | 21 |  |
| ln_French | 22 |  |
| ln_Spanish | 23 |  |
| ln_Russian | 24 |  |
| ln_Spanish_La | 25 |  |
| ln_Czech_Cz | 26 |  |
| ln_Slovak_Sk | 27 |  |
| ln_Korean_Kr | 28 |  |
| ln_Portuguese_Br | 29 |  |
| ln_Japanese_Jp | 30 |  |
| ln_Turkish_Tr | 31 |  |
| ln_Arabic | 32 |  |
| ln_Ukrainian | 33 |  |
| ln_TrdtnlChinese_Hk | 35 |  |

# SAPB1.BoSvcCallPriorities (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| scp_Low | 0 |  |
| scp_Medium | 1 |  |
| scp_High | 2 |  |

# SAPB1.BoSvcContractStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| scs_Approved | 0 |  |
| scs_Frozen | 1 |  |
| scs_Draft | 2 |  |
| scs_Terminated | 3 |  |

# SAPB1.BoSvcEpxDocTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edt_Invoice | 13 |  |
| edt_Delivery | 15 |  |
| edt_Return | 16 |  |
| edt_StockTransfer | 67 |  |
| edt_CreditMemo | 14 |  |
| edt_Order | 17 |  |
| edt_Quotation | 23 |  |
| edt_AP_Invoice | 18 |  |
| edt_AP_CreditMemo | 19 |  |
| edt_GoodsReceipt | 20 |  |
| edt_GoodsReturn | 21 |  |
| edt_PurchaseOrder | 22 |  |
| edt_PurchaseQuotation | 540000006 |  |
| edt_AR_CorrectionInvoice | 165 |  |
| edt_AP_CorrectionInvoice | 163 |  |
| edt_Return_Request | 234000031 |  |
| edt_Goods_Return_Request | 234000032 |  |

# SAPB1.BoSvcExpPartTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sep_Inventory | 0 |  |
| sep_NonInventory | 1 |  |

# SAPB1.BoTaxInvoiceTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| botit_AlterationCorrectionInvoice | 0 |  |
| botit_AlterationInvoice | 1 |  |
| botit_CorrectionInvoice | 2 |  |
| botit_Invoice | 4 |  |
| botit_JournalEntry | 5 |  |
| botit_Payment | 6 |  |

# SAPB1.BoTaxOnInstallmentsTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| toiProportionally | 0 |  |
| toiTaxInFirst | 1 |  |
| toiTaxInFirstOnly | 2 |  |

# SAPB1.BoTaxPostAccEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tpa_Default | 0 |  |
| tpa_SalesTaxAccount | 1 |  |
| tpa_PurchaseTaxAccount | 2 |  |

# SAPB1.BoTaxPostingAccountTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tpatEmpty | 0 |  |
| tpatSalesTaxAccount | 1 |  |
| tpatPurchasingTaxAccount | 2 |  |

# SAPB1.BoTaxRoundingRuleTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trr_RoundDown | 0 |  |
| trr_RoundUp | 1 |  |
| trr_RoundOff | 2 |  |
| trr_CompanyDefault | 3 |  |

# SAPB1.BoTaxTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tt_Yes | 0 |  |
| tt_No | 1 |  |
| tt_UseTax | 2 |  |
| tt_OffsetTax | 3 |  |

# SAPB1.BoTCDConditionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tcdcNone | 0 |  |
| tcdcFederalTaxID | 1 |  |
| tcdcShipToAddress | 2 |  |
| tcdcShipToStreePOBox | 3 |  |
| tcdcShipToCity | 4 |  |
| tcdcShipToZipCode | 5 |  |
| tcdcShipToCounty | 6 |  |
| tcdcShipToState | 7 |  |
| tcdcShipToCountry | 8 |  |
| tcdcItem | 9 |  |
| tcdcItemGroup | 10 |  |
| tcdcBusinessPartner | 11 |  |
| tcdcCustomerGroup | 12 |  |
| tcdcVendorGroup | 13 |  |
| tcdcWarehouse | 14 |  |
| tcdcGLAccount | 15 |  |
| tcdcCustomerEquTax | 16 |  |
| tcdcTaxStatus | 17 |  |
| tcdcFreight | 18 |  |
| tcdcUDF | 19 |  |
| tcdcBranchNumber | 20 |  |
| tcdcTypeOfBusiness | 21 |  |

# SAPB1.BoTCDDocumentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tcddtItem | 0 |  |
| tcddtService | 1 |  |
| tcddtItemAndService | 2 |  |

# SAPB1.BoTimeTemplate (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tt_24H | 0 |  |
| tt_12H | 1 |  |

# SAPB1.BoTransactionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| botrntComplete | 0 |  |
| botrntReject | 1 |  |

# SAPB1.BoUDOObjType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boud_Document | 0 |  |
| boud_MasterData | 1 |  |

# SAPB1.BoUniqueSerialNumber (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| usn_None | 0 |  |
| usn_MfrSerialNumber | 1 |  |
| usn_SerialNumber | 2 |  |
| usn_LotNumber | 3 |  |

# SAPB1.BoUpdateAllocationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bouaManual | 0 |  |
| bouaCalculated | 1 |  |
| bouaRunCalculation | 2 |  |

# SAPB1.BoUPTOptions (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bou_FullNone | 0 |  |
| bou_FullReadNone | 1 |  |

# SAPB1.BoUserGroup (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ug_Regular | 0 |  |
| ug_Deleted | 1 |  |

# SAPB1.BoUTBTableType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bott_Document | 0 |  |
| bott_DocumentLines | 1 |  |
| bott_MasterData | 2 |  |
| bott_MasterDataLines | 3 |  |
| bott_NoObject | 4 |  |
| bott_NoObjectAutoIncrement | 5 |  |

# SAPB1.BoVatCategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bovcInputTax | 0 |  |
| bovcOutputTax | 1 |  |

# SAPB1.BoVatStatus (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| vExempted | 0 |  |
| vLiable | 1 |  |
| vEC | 2 |  |

# SAPB1.BoVerticalAlignmentEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlvaTop | 0 |  |
| rlvaBottom | 1 |  |
| rlvaCentralized | 2 |  |

# SAPB1.BoWeekEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| Sunday | 1 |  |
| Monday | 2 |  |
| Tuesday | 3 |  |
| Wednesday | 4 |  |
| Thursday | 5 |  |
| Friday | 6 |  |
| Saturday | 7 |  |

# SAPB1.BoWeekNoRuleEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| fromJanFirst | 0 |  |
| fromFirstFourDayWeek | 1 |  |
| fromFirstFullWeek | 2 |  |

# SAPB1.BoWorkOrderStat (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| wk_ProductComplete | 0 |  |
| wk_WorkInstruction | 1 |  |
| wk_WorkOrder | 2 |  |

# SAPB1.BoYesNoEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tNO | 0 |  |
| tYES | 1 |  |

# SAPB1.BoYesNoNoneEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boNO | 0 |  |
| boYES | 1 |  |
| boNONE | 2 |  |

# SAPB1.BrazilMultiIndexerTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bmitInvalid | 0 |  |
| bmitIncomeNature | 1 |  |

# SAPB1.BrazilNumericIndexerTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bnitInvalid | 0 |  |
| bnitBeverageCommercialBrand | 1 |  |
| bnitFuelGroup | 2 |  |
| bnitNatureOfCompany | 3 |  |
| bnitEconomicActivityType | 4 |  |
| bnitCooperativeAssociationType | 5 |  |
| bnitProfitTaxation | 6 |  |
| bnitCompanyQualification | 7 |  |
| bnitDeclarerType | 8 |  |
| bnitEnvironmentType | 9 |  |
| bnitTributaryType | 10 |  |
| bnitTributaryRegimeCode | 11 |  |
| bnitIncomeNatureTable | 12 |  |
| bnitIncomeNatureCode | 13 |  |
| bnitExportationDocumentType | 14 |  |
| bnitExportationNature | 15 |  |
| bnitLadingBillType | 16 |  |

# SAPB1.BrazilStringIndexerTypes (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| bsitInvalid | 0 |  |
| bsitBeverageTable | 1 |  |
| bsitNatureOfCalculationBase | 2 |  |
| bsitCreditOrigin | 3 |  |
| bsitBeverageGroup | 4 |  |
| bsitCreditContributionOrigin | 5 |  |
| bsitIPIPeriod | 6 |  |
| bsitSPEDProfile | 7 |  |
| bsitImportationDocumentType | 8 |  |
| bsitReferentialAccountCode | 9 |  |

# SAPB1.CalculateInterestMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cimOnRemainingAmount | 0 |  |
| cimOnOriginalSum | 1 |  |

# SAPB1.CalculationBaseEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cbYearly | 0 |  |
| cbMonthly | 1 |  |

# SAPB1.CallMessageStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cmsUnread | 0 |  |
| cmsRead | 1 |  |

# SAPB1.CallMessageTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cmtInformation | 0 |  |
| cmtWarning | 1 |  |
| cmtError | 2 |  |

# SAPB1.CampaignAssignToEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| catUser | 0 |  |
| catEmployee | 1 |  |

# SAPB1.CampaignBPStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cbpsActive | 0 |  |
| cbpsInactive | 1 |  |

# SAPB1.CampaignItemTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| citItems | 0 |  |
| citLabel | 1 |  |
| citTravel | 2 |  |

# SAPB1.CampaignStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| csOpen | 0 |  |
| csFinished | 1 |  |
| csCanceled | 2 |  |

# SAPB1.CampaignTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ctEmail | 0 |  |
| ctMail | 1 |  |
| ctFax | 2 |  |
| ctPhoneCall | 3 |  |
| ctMeeting | 4 |  |
| ctSMS | 5 |  |
| ctWeb | 6 |  |
| ctOthers | 7 |  |

# SAPB1.CancelStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| csYes | 0 |  |
| csNo | 1 |  |
| csCancellation | 2 |  |

# SAPB1.CardOrAccountEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| coaCard | 0 |  |
| coaAccount | 1 |  |

# SAPB1.ClosingOptionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| coByCurrentSystemDate | 1 |  |
| coByOriginalDocumentDate | 2 |  |
| coBySpecifiedDate | 3 |  |

# SAPB1.CommissionTradeTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ct_Empty | 0 |  |
| ct_SalesAgent | 1 |  |
| ct_PurchaseAgent | 2 |  |
| ct_Consignor | 3 |  |

# SAPB1.ContractSequenceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cs_Monthly | 0 |  |
| cs_Quarterly | 1 |  |
| cs_SemiAnnually | 2 |  |
| cs_Yearly | 3 |  |

# SAPB1.CounterTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ctUser | 0 |  |
| ctEmployee | 1 |  |

# SAPB1.CountingDocumentStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cdsOpen | 0 |  |
| cdsClosed | 1 |  |

# SAPB1.CountingLineStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| clsOpen | 0 |  |
| clsClosed | 1 |  |

# SAPB1.CountingTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ctSingleCounter | 0 |  |
| ctMultipleCounters | 1 |  |

# SAPB1.CreateMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cmManual | 0 |  |
| cmAutomatic | 1 |  |

# SAPB1.CreditOrDebitEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| codCredit | 0 |  |
| codDebit | 1 |  |

# SAPB1.CurrenciesDecimalsEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| cd1Digit | 0 |  |
| cd2Digits | 1 |  |
| cd3Digits | 2 |  |
| cd4Digits | 3 |  |
| cd5Digits | 4 |  |
| cd6Digits | 5 |  |
| cdDefault | 6 |  |
| cdWithoutDecimals | 7 |  |

# SAPB1.CycleCountDeterminationCycleByEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ccdcbItemGroup | 0 |  |
| ccdcbWarehouseSublevel1 | 1 |  |
| ccdcbWarehouseSublevel2 | 2 |  |
| ccdcbWarehouseSublevel3 | 3 |  |
| ccdcbWarehouseSublevel4 | 4 |  |

# SAPB1.DataPrivacyProtectionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dpp_None | 0 |  |
| dpp_Erased | 1 |  |
| dpp_Blocked | 2 |  |
| dpp_Unblocked | 3 |  |

# SAPB1.DataSensitiveStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dss_FieldNotSentive | 0 |  |
| dss_DataSubjectNotNaturalPerson | 1 |  |
| dss_DataSubjectIsBlockedOrErased | 2 |  |
| dss_DataIsSensitive | 3 |  |
| dss_Error | 4 |  |
| dss_TransactionIsErased | 5 |  |

# SAPB1.DepreciationCalculationBaseEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dcbAcquisitionValue | 0 |  |
| dcbNetBookValue | 1 |  |

# SAPB1.DepreciationMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dmNoDepreciation | 0 |  |
| dmStraightLine | 1 |  |
| dmStraightLinePeriodControl | 2 |  |
| dmDecliningBalance | 3 |  |
| dmMultilevel | 4 |  |
| dmImmediateWriteOff | 5 |  |
| dmSpecialDepreciation | 6 |  |
| dmManualDepreciation | 7 |  |
| dmAccelerated | 8 |  |

# SAPB1.DepreciationRoundingMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| drmTruncate | 0 |  |
| drmRoundUp | 1 |  |
| drmRoundDown | 2 |  |

# SAPB1.DirectDebitTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ddtCORE | 0 |  |
| ddtB2B | 1 |  |
| ddtCOR1 | 2 |  |

# SAPB1.DiscountGroupBaseObjectEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dgboNone | 0 |  |
| dgboItemGroups | 1 |  |
| dgboItemProperties | 2 |  |
| dgboManufacturer | 3 |  |
| dgboItems | 4 |  |

# SAPB1.DiscountGroupDiscountTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dgdt_Fixed | 0 |  |
| dgdt_Variable | 1 |  |

# SAPB1.DiscountGroupRelationsEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dgrLowestDiscount | 0 |  |
| dgrHighestDiscount | 1 |  |
| dgrAverageDiscount | 2 |  |
| dgrDiscountTotals | 3 |  |
| dgrMultipliedDiscount | 4 |  |

# SAPB1.DiscountGroupTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dgt_AllBPs | 0 |  |
| dgt_CustomerGroup | 1 |  |
| dgt_VendorGroup | 2 |  |
| dgt_SpecificBP | 3 |  |

# SAPB1.DisplayBatchQtyUoMByEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dispBatchQtyByDocRowUoM | 0 |  |
| dispBatchQtyByInventoryUoM | 1 |  |

# SAPB1.DistributionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dtUser | 0 |  |
| dtEmployee | 0 |  |
| dtContactPerson | 0 |  |
| dtDistributionList | 0 |  |
| dtOther | 0 |  |

# SAPB1.DocumentAuthorizationStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dasWithout | 0 |  |
| dasPending | 1 |  |
| dasApproved | 2 |  |
| dasRejected | 3 |  |
| dasGenerated | 4 |  |
| dasGeneratedbyAuthorizer | 5 |  |
| dasCancelled | 6 |  |

# SAPB1.DocumentDeliveryTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ddtNoneSeleted | 0 |  |
| ddtCreateOnlineDocument | 1 |  |
| ddtPostToAribaNetwork | 2 |  |

# SAPB1.DocumentObjectTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dc_ArInvoice | 13 |  |
| dc_Delivery | 15 |  |
| dc_GoodsReturn | 21 |  |
| dc_InventoryTransfer | 67 |  |

# SAPB1.DocumentPriceSourceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dpsSpecialPricesForBusinessPartner | 0 |  |
| dpsManual | 1 |  |
| dpsActivePriceListDiscountGroups | 2 |  |
| dpsActivePriceList | 3 |  |
| dpsInactivePriceList | 4 |  |
| dpsBlanketAgreement | 5 |  |
| dpsPeriodAndVolumeDiscounts | 6 |  |
| dpsPeriodAndVolumeDiscountsDiscountGroups | 7 |  |
| dpsInactivePriceListDiscountGroups | 8 |  |
| dpsNewSpecialPricesForBusinessPartner | 9 |  |
| dpsNewActivePriceListDiscountGroups | 10 |  |
| dpsNewActivePriceList | 11 |  |
| dpsNewInactivePriceList | 12 |  |
| dpsNewBlanketAgreement | 13 |  |
| dpsNewPeriodAndVolumeDiscounts | 14 |  |
| dpsNewPeriodAndVolumeDiscountsDiscountGroups | 15 |  |
| dpsNewInactivePriceListDiscountGroups | 16 |  |

# SAPB1.DocumentRemarksIncludeTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| driBaseDocumentNumber | 0 |  |
| driBPReferenceNumber | 1 |  |
| driManualRemarksOnly | 2 |  |

# SAPB1.DomesticBankAccountValidationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dbavNone | 0 |  |
| dbavBelgium | 1 |  |
| dbavSpain | 2 |  |
| dbavFrance | 3 |  |
| dbavItaly | 4 |  |
| dbavNetherlands | 5 |  |
| dbavPortugal | 6 |  |

# SAPB1.DownPaymentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dptRequest | 0 |  |
| dptInvoice | 1 |  |

# SAPB1.DrawingMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dmAll | 0 |  |
| dmNone | 1 |  |
| dmQuantity | 2 |  |
| dmTotal | 3 |  |

# SAPB1.DueDateTypesEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ddtAfterTimePeriod | 0 |  |
| ddtByDates | 1 |  |

# SAPB1.DunningLetterTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| dltDunningLetter1 | 0 |  |
| dltDunningLetter2 | 1 |  |
| dltDunningLetter3 | 2 |  |
| dltDunningLetter4 | 3 |  |
| dltDunningLetter5 | 4 |  |
| dltDunningLetter6 | 5 |  |
| dltDunningLetter7 | 6 |  |
| dltDunningLetter8 | 7 |  |
| dltDunningLetter9 | 8 |  |
| dltDunningLetter10 | 9 |  |
| dltDunningALL | 10 |  |

# SAPB1.ECDPostingTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ecdNormal | 0 |  |
| ecdStatement | 1 |  |

# SAPB1.EcmActionGenerationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| lgtNotRelevant | 1 |  |
| lasGenerateLater | 2 |  |
| lasGenerate | 3 |  |
| lasGenerateOffline | 4 |  |

# SAPB1.EcmActionLogTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| altSend | 1 |  |
| altReceive | 2 |  |
| altImport | 3 |  |
| altNote | 4 |  |
| altWarning | 5 |  |
| altError | 6 |  |

# SAPB1.EcmActionPeriodTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| aptIgnore | 0 |  |
| aptYear | 1 |  |
| aptQuarter | 2 |  |
| aptMonth | 3 |  |
| aptDateRange | 4 |  |

# SAPB1.EcmActionStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| lasNone | 0 |  |
| lasNew | 1 |  |
| lasPending | 2 |  |
| lasError | 3 |  |
| lasOK | 4 |  |
| lasSent | 5 |  |
| lasDocError | 6 |  |
| lasWaiting | 7 |  |
| lasAuthorized | 8 |  |
| lasInProcess | 9 |  |
| lasRejected | 10 |  |
| lasDenied | 11 |  |
| lasCanceled | 12 |  |
| lasAborted | 13 |  |
| lasQueued | 14 |  |
| lasImported | 15 |  |

# SAPB1.EcmActionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| latNone | 0 |  |
| latSetup | 1 |  |
| latReport | 2 |  |
| latDocumentAR | 3 |  |
| latDocumentAP | 4 |  |
| latDraft | 5 |  |
| latOther | 6 |  |
| latSkip | 7 |  |
| latContingency | 8 |  |
| latBpCheck | 9 |  |
| latPaymentIncoming | 10 |  |
| latPaymentOutgoing | 11 |  |
| latReconciliation | 12 |  |
| latDraftAP | 13 |  |
| latTransportation | 14 |  |
| latInvTransfer | 15 |  |

# SAPB1.EDocGenerationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edocGenerate | 0 |  |
| edocGenerateLater | 1 |  |
| edocNotRelevant | 2 |  |
| edocGenerateOffline | 3 |  |

# SAPB1.EDocStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edoc_New | 0 |  |
| edoc_Pending | 1 |  |
| edoc_Sent | 2 |  |
| edoc_Error | 3 |  |
| edoc_Ok | 4 |  |

# SAPB1.EDocTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edocFE | 0 |  |
| edocFCE | 1 |  |

# SAPB1.EffectivePriceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| epDefaultPriority | 0 |  |
| epLowestPrice | 1 |  |
| epHighestPrice | 2 |  |

# SAPB1.ElecCommStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ecsApproved | 0 |  |
| ecsPendingApproval | 1 |  |
| ecsRejected | 2 |  |

# SAPB1.ElectronicDocGenTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edgt_NotRelevant | 0 |  |
| edgt_Generate | 1 |  |
| edgt_GenerateLater | 2 |  |
| edgt_GenerateOffline | 3 |  |

# SAPB1.ElectronicDocProcessingTargetEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edpt_Invalid | -1 |  |
| edpt_All | 0 |  |
| edpt_None | 1 |  |
| edpt_LegacyB1iSender | 2 |  |
| edpt_B1iEventSender | 3 |  |
| edpt_LegacyXMLFile | 4 |  |
| edpt_ConnectorXML | 5 |  |
| edpt_ConnectorB1iWS | 6 |  |
| edpt_ConnectorPEPPOL | 7 |  |
| edpt_ConnectorEET | 8 |  |
| edpt_ConnectorEETv2 | 9 |  |
| edpt_ConnectorCFDi | 10 |  |
| edpt_ConnectorEBooks | 11 |  |
| edpt_ConnectorDOX | 12 |  |
| edpt_ConnectorDigipoort | 13 |  |
| edpt_ImportWizardManualFile | 14 |  |
| edpt_ImportWizardAutomaticFile | 15 |  |
| edpt_ImportWizardWebService | 16 |  |
| edpt_ConnectorFPA | 17 |  |
| edpt_ConnectorDocSign | 18 |  |
| edpt_ConnectorAFE | 19 |  |
| edpt_ConnectorGSTReturn | 20 |  |
| edpt_ConnectorKSeF | 21 |  |
| edpt_ConnectorPTDocSign | 22 |  |
| edpt_ConnectorSkatDK | 23 |  |
| edpt_ConnectorEII | 24 |  |
| edpt_ConnectorPTeInvoicing | 25 |  |
| edpt_ConnectorEBilling | 26 |  |
| edpt_ConnectorEDSHOI | 27 |  |
| edpt_ConnectorPTeCom | 28 |  |
| edpt_ConnectorVeriFactu | 29 |  |
| edpt_ManualImport | 30 |  |
| edpt_ConnectorFReINV | 32 |  |

# SAPB1.ElectronicDocProtocolCodeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edpc_Invalid | 0 |  |
| edpc_GEN | 1 |  |
| edpc_EET | 2 |  |
| edpc_CFDI | 3 |  |
| edpc_FPA | 4 |  |
| edpc_MTD | 5 |  |
| edpc_EWB | 6 |  |
| edpc_PEPPOL | 7 |  |
| edpc_HOI | 8 |  |
| edpc_MYF | 9 |  |
| edpc_EIS | 10 |  |
| edpc_IIS | 11 |  |
| edpc_IIS_Annual | 12 |  |
| edpc_DIGIPOORT | 13 |  |
| edpc_EBooks | 14 |  |
| edpc_DOX | 15 |  |
| edpc_RTIE | 16 |  |
| edpc_EBilling | 17 |  |
| edpc_TaxService | 18 |  |
| edpc_AFE | 19 |  |
| edpc_DocSign | 20 |  |
| edpc_KSeF | 21 |  |
| edpc_GSTReturn | 22 |  |
| edpc_PTDocSign | 23 |  |
| edpc_SkatDK | 24 |  |
| edpc_EII | 25 |  |
| edpc_NFe | 26 |  |
| edpc_PTeInvoicing | 27 |  |
| edpc_PTeCom | 28 |  |
| edpc_VeriFactu | 29 |  |
| edpc_BAS | 30 |  |
| edpc_PDFwithXML | 31 |  |
| edpc_FReINV | 32 |  |

# SAPB1.ElectronicDocProtocolCodeStrEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edpcs_Invalid | 0 |  |
| edpcs_GEN | 1 |  |
| edpcs_EET | 2 |  |
| edpcs_CFDI | 3 |  |
| edpcs_FPA | 4 |  |
| edpcs_MTD | 5 |  |
| edpcs_EWB | 6 |  |
| edpcs_PEPPOL | 7 |  |
| edpcs_HOI | 8 |  |
| edpcs_MYF | 9 |  |
| edpcs_EIS | 10 |  |
| edpcs_IIS | 11 |  |
| edpcs_IIS_Annual | 12 |  |
| edpcs_DIGIPOORT | 13 |  |
| edpcs_EBooks | 14 |  |
| edpcs_DOX | 15 |  |
| edpcs_RTIE | 16 |  |
| edpcs_EBilling | 17 |  |
| edpcs_TaxService | 18 |  |
| edpcs_AFE | 19 |  |
| edpcs_DocSign | 20 |  |
| edpcs_KSeF | 21 |  |
| edpcs_GSTReturn | 22 |  |
| edpcs_PTDocSign | 23 |  |
| edpcs_SkatDK | 24 |  |
| edpcs_EII | 25 |  |
| edpcs_NFe | 26 |  |
| edpcs_PTeInvoicing | 27 |  |
| edpcs_PTeCom | 28 |  |
| edpcs_VeriFactu | 29 |  |
| edpcs_BAS | 30 |  |
| edpcs_PDFwithXML | 31 |  |
| edpcs_FReINV | 32 |  |

# SAPB1.ElectronicDocumentAuthorityProcessEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edapNone | -1 |  |
| edapApproval | 0 |  |
| edapRejection | 1 |  |

# SAPB1.ElectronicDocumentBlobContentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edbctDefault | -1 |  |
| edbctXML | 0 |  |
| edbctZippedXML | 1 |  |
| edbctJSON | 2 |  |
| edbctZippedJSON | 3 |  |
| edbctText | 4 |  |
| edbctZippedP7M | 5 |  |
| edbctP7M | 6 |  |
| edbctZippedPDF | 7 |  |

# SAPB1.ElectronicDocumentEntryCancellationStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edecsInvalid | 0 |  |
| edecsNotSet | 1 |  |
| edecsNewRequest | 2 |  |
| edecsRequestSent | 3 |  |
| edecsApproved | 4 |  |
| edecsRejected | 5 |  |
| edecsError | 6 |  |
| edecsCancelled | 7 |  |
| edecsInProcess | 8 |  |
| edecsSentToAuthority | 9 |  |
| edescCancelledWOApproval | 10 |  |

# SAPB1.ElectronicDocumentEntryLogTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edeltNone | 0 |  |
| edeltSend | 1 |  |
| edeltReceive | 2 |  |
| edeltImport | 3 |  |
| edeltNote | 4 |  |
| edeltWarning | 5 |  |
| edeltError | 6 |  |
| edeltWSData | 7 |  |
| edeltAuthorityProcessBegins | 8 |  |
| edeltAuthorityProcessFinished | 9 |  |

# SAPB1.ElectronicDocumentEntryPeriodTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edeptIgnore | 0 |  |
| edeptYear | 1 |  |
| edeptQuarter | 2 |  |
| edeptMonth | 3 |  |
| edeptDateRange | 4 |  |

# SAPB1.ElectronicDocumentEntryStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edesNone | 0 |  |
| edesNew | 1 |  |
| edesReadyToProcess | 2 |  |
| edesPending | 3 |  |
| edesError | 4 |  |
| edesOK | 5 |  |
| edesSent | 6 |  |
| edesDocError | 7 |  |
| edesTempError | 8 |  |
| edesWarning | 9 |  |
| edesWaiting | 10 |  |
| edesAuthorized | 11 |  |
| edesInProcess | 12 |  |
| edesRejected | 13 |  |
| edesDenied | 14 |  |
| edesCanceled | 15 |  |
| edesAborted | 16 |  |
| edesUnused | 17 |  |
| edesQueued | 18 |  |
| edesImported | 19 |  |
| edesApproved | 20 |  |
| edesApproving | 21 |  |
| edesRejecting | 22 |  |
| edesGenerated | 23 |  |
| edesDetermined | 24 |  |
| edesImporting | 25 |  |
| edesInProcessToIntermediary | 26 |  |
| edesSentToIntermediary | 27 |  |
| edesApprovedByIntermediary | 28 |  |
| edesNotIntegratedCustomer | 29 |  |
| edesNotSentToCustomer | 30 |  |
| edesErrorSendingToCustomer | 31 |  |
| edesSentToCustomer | 32 |  |
| edesReceivedByCustomer | 33 |  |
| edesRejectedByCustomer | 34 |  |
| edesPaidByCustomer | 35 |  |
| edesCheckingIntegrationStatus | 36 |  |
| edesNotApproved | 37 |  |
| edesChargeReversal | 38 |  |
| edesCanceling | 39 |  |
| edesContinuing | 40 |  |
| edesContinued | 41 |  |
| edesFurtherObjecting | 42 |  |
| edesFurtherObjection | 43 |  |
| edesResending | 44 |  |
| edesPendingToCAEA | 45 |  |
| edesUpdatingResponse | 46 |  |

# SAPB1.ElectronicDocumentEntryTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| edetNone | 0 |  |
| edetSetup | 1 |  |
| edetReport | 2 |  |
| edetDocumentAR | 3 |  |
| edetDocumentAP | 4 |  |
| edetDraftAR | 5 |  |
| edetDraftAP | 6 |  |
| edetOther | 7 |  |
| edetSkip | 8 |  |
| edetContingency | 9 |  |
| edetBpCheck | 10 |  |
| edetIncomingPayment | 11 |  |
| edetOutgoingPayment | 12 |  |
| edetInternalReconciliation | 13 |  |
| edetTransportationDocument | 14 |  |
| edetInventoryTransfer | 15 |  |
| edetVATObligations | 16 |  |
| edetVATDeclarations | 17 |  |
| edetVATLiabilities | 18 |  |
| edetVATPayments | 19 |  |
| edetDelivery | 20 |  |
| edetReturn | 21 |  |
| edetARInvoice | 22 |  |
| edetARCreditMemo | 23 |  |
| edetGoodsReceiptPO | 24 |  |
| edetGoodsReturn | 25 |  |
| edetAPInvoice | 26 |  |
| edetAPCreditMemo | 27 |  |
| edetDraftIncomingPayment | 28 |  |
| edetDraftOutgoingPayment | 29 |  |
| edetJournalEntry | 30 |  |
| edetEBooksExpense | 31 |  |
| edetGSTReturnF5 | 32 |  |
| edetGSTReturnF7 | 33 |  |
| edetGSTReturnF8 | 34 |  |
| edetSkatDKPeriod | 35 |  |
| edetSkatDKDraftReport | 36 |  |
| edetSkatDKReport | 37 |  |
| edetINV | 38 |  |
| edetRIN | 39 |  |
| edetDLN | 40 |  |
| edetINVBasedOnDLN | 41 |  |
| edetSeries | 42 |  |
| edetInvoices | 43 |  |
| edetGoodsTransfers | 44 |  |
| edetGoodsIssue | 45 |  |
| edetGoodsReceipt | 46 |  |
| edetPickList | 47 |  |
| edetDraftGoodsIssue | 48 |  |
| edetDraftGoodsReceipt | 49 |  |
| edetRequestCAEA | 50 |  |

# SAPB1.EmployeeExemptionUnitEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| eeu_None | 0 |  |
| eeu_Yearly | 1 |  |
| eeu_Monthly | 2 |  |
| eeu_Weekly | 3 |  |
| eeu_Daily | 4 |  |

# SAPB1.EmployeePaymentMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| epm_None | 0 |  |
| epm_BankTransfer | 1 |  |

# SAPB1.EmployeeTransferProcessingStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| etps_New | 0 |  |
| etps_Sent | 1 |  |
| etps_Accepted | 2 |  |
| etps_Error | 3 |  |

# SAPB1.EmployeeTransferStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ets_New | 0 |  |
| ets_Processing | 1 |  |
| ets_Sent | 2 |  |
| ets_Received | 3 |  |
| ets_Accepted | 4 |  |
| ets_Error | 5 |  |

# SAPB1.EndTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| etNoEndDate | 0 |  |
| etByCounter | 1 |  |
| etByDate | 2 |  |

# SAPB1.EventReplayStateEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| None | 0 |  |
| Replaying | 1 |  |
| Completed | 2 |  |

# SAPB1.EventStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| New | 0 |  |
| Failed | 1 |  |
| PartiallyDelivered | 2 |  |
| Delivered | 3 |  |
| Archived | 4 |  |

# SAPB1.EWBSupplyTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ewb_st_Inward | 0 |  |
| ewb_st_Outward | 1 |  |

# SAPB1.EWBTransactionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ewb_tt_Regular | 0 |  |
| ewb_tt_BillToShipTo | 1 |  |
| ewb_tt_BillFromDispathFrom | 2 |  |
| ewb_tt_CombinationOfBillAndShip | 3 |  |

# SAPB1.ExchangeRateSelectEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ierFromInovice | 0 |  |
| ierCurrentRate | 1 |  |

# SAPB1.ExemptionMaxAmountValidationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| emaIndividual | 0 |  |
| emaAccumulated | 1 |  |

# SAPB1.ExternalCallStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ecsNew | 0 |  |
| ecsInProcess | 1 |  |
| ecsCompleted | 2 |  |
| ecsConfirmed | 3 |  |
| ecsFailed | 4 |  |

# SAPB1.FolioLetterEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| fLetterA | 0 |  |
| fLetterB | 1 |  |
| fLetterC | 2 |  |
| fLetterE | 3 |  |
| fLetterM | 4 |  |
| fLetterR | 5 |  |
| fLetterT | 5 |  |
| fLetterX | 5 |  |
| fLetterEMPTY | 5 |  |

# SAPB1.FormattedSearchByFieldEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| fsbfWhenExitingAlteredColumn | 0 |  |
| fsbfWhenFieldChanges | 1 |  |
| fsbfWhenColumnValueChanges | 2 |  |

# SAPB1.FreightTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ftShipping | 0 |  |
| ftInsurance | 1 |  |
| ftOther | 2 |  |
| ftSpecial | 3 |  |

# SAPB1.FreightTypeForBolloEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ftStandard | 0 |  |
| ftBollo | 1 |  |

# SAPB1.GeneratedAssetStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gasOpen | 0 |  |
| gasClosed | 1 |  |

# SAPB1.GetGLAccountByEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gglab_General | 0 |  |
| gglab_Warehouse | 1 |  |
| gglab_ItemGroup | 2 |  |

# SAPB1.GovPayCodePeriodicityEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gpcpMonth | 0 |  |
| gpcpQuarter | 1 |  |
| gpcpHalfMonth | 2 |  |
| gpcpTenDays | 3 |  |

# SAPB1.GovPayCodeSPEDCategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gpcscICMS | 1 |  |
| gpcscICMSST | 2 |  |
| gpcscIPI | 3 |  |
| gpcscISS | 4 |  |
| gpcscPIS | 5 |  |
| gpcscCOFINS | 6 |  |
| gpcsPISST | 7 |  |
| gpcsCONFINSST | 8 |  |

# SAPB1.GroupingMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gmPerInvoice | 0 |  |
| gmPerDunningLevel | 1 |  |
| gmPerBP | 2 |  |

# SAPB1.GSTTaxCategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gtc_Regular | 0 |  |
| gtc_NilRated | 1 |  |
| gtc_Exempt | 2 |  |

# SAPB1.GSTTransactionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gsttrantyp_BillOfSupply | 0 |  |
| gsttrantyp_GSTTaxInvoice | 1 |  |
| gsttrantyp_GSTDebitMemo | 2 |  |

# SAPB1.GTSResponseToExceedingEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| Block | 0 |  |
| Split | 1 |  |

# SAPB1.IdentificationCodeTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| idctOrder | 0 |  |
| idctDelivery | 1 |  |
| idctInvoice | 2 |  |
| idctCreditNote | 3 |  |
| idctStandardItemTypeIdentification | 4 |  |
| idctItemCommodityClassification | 5 |  |

# SAPB1.ImportFieldTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| iftInvalid | 0 |  |
| iftFederalTaxID | 1 |  |
| iftAdditionalID | 2 |  |
| iftUnifiedFederalTaxID | 3 |  |
| iftCNPJ | 4 |  |
| iftAliasName | 5 |  |
| iftIBAN | 6 |  |
| iftBPName | 7 |  |

# SAPB1.ImportOrExportTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| et_IpmortsOrExports | 0 |  |
| et_SEZ_Developer | 1 |  |
| et_SEZ_Unit | 2 |  |
| et_Deemed_ImportsOrExports | 3 |  |

# SAPB1.InstallmentPaymentsPossiblityEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ippCr | 0 |  |
| ippNo | 1 |  |
| ippRd | 2 |  |
| ippYes | 3 |  |

# SAPB1.IntrastatConfigurationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| enAdditionalMeasureUnit | 0 |  |
| enCommodityCodes | 1 |  |
| enCustomProcedures | 2 |  |
| enIncoterms | 3 |  |
| enNatureOfTransactions | 4 |  |
| enPortsOfEntryAndExit | 5 |  |
| enServiceCodes | 6 |  |
| enStatisticalProcedures | 7 |  |
| enTransportModes | 8 |  |
| enRegions | 9 |  |

# SAPB1.IntrastatConfigurationTriangDealEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| enNone | 0 |  |
| enType11 | 11 |  |
| enType21 | 21 |  |
| enType31 | 31 |  |

# SAPB1.InvBaseDocTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| Default | 0 |  |
| Empty | 1 |  |
| PurchaseDeliveryNotes | 2 |  |
| InventoryGeneralEntry | 3 |  |
| WarehouseTransfers | 4 |  |
| InventoryTransferRequest | 5 |  |

# SAPB1.InventoryAccountTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| iatExpenses | 0 |  |
| iatRevenues | 1 |  |
| iatExemptIncome | 2 |  |
| iatInventory | 3 |  |
| iatCost | 4 |  |
| iatTransfer | 5 |  |
| iatVarience | 6 |  |
| iatPriceDifference | 7 |  |
| iatNegativeInventoryAdjustment | 8 |  |
| iatDecreasing | 9 |  |
| iatIncreasing | 10 |  |
| iatReturning | 11 |  |
| iatEURevenues | 12 |  |
| iatEUExpenses | 13 |  |
| iatForeignRevenue | 14 |  |
| iatForeignExpens | 15 |  |
| iatPurchase | 16 |  |
| iatPAReturn | 17 |  |
| iatPurchaseOffset | 18 |  |
| iatExchangeRateDifferences | 19 |  |
| iatGoodsClearing | 20 |  |
| iatGLDecrease | 21 |  |
| iatGLIncrease | 22 |  |
| iatWip | 23 |  |
| iatWipVariance | 24 |  |
| iatWipOffsetProfitAndLoss | 25 |  |
| iatInventoryOffsetProfitAndLoss | 26 |  |
| iatStockInflationAdjust | 27 |  |
| iatStockInflationOffset | 28 |  |
| iatCostInflation | 29 |  |
| iatCostInflationOffset | 30 |  |
| iatExpenseClearing | 31 |  |
| iatExpenseOffsetting | 32 |  |
| iatStockInTransit | 33 |  |
| iatShippedGoods | 34 |  |
| iatVATInRevenue | 35 |  |
| iatSalesCredit | 36 |  |
| iatPurchaseCredit | 37 |  |
| iatExemptedCredits | 38 |  |
| iatSalesCreditForeign | 39 |  |
| iatForeignPurchaseCredit | 40 |  |
| iatSalesCreditEU | 41 |  |
| iatEUPurchaseCredit | 42 |  |
| iatPurchaseBalance | 43 |  |
| iatWHIncomingCenvat | 44 |  |
| iatWHOutgoingCenvat | 45 |  |
| iatFreeOfChargeSales | 46 |  |
| iatFreeOfChargePurchase | 47 |  |

# SAPB1.InventoryCycleTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ictCylce | 0 |  |
| ictMRP | 1 |  |

# SAPB1.InventoryOpeningBalancePriceSourceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| iobpsByPriceList | 0 |  |
| iobpsLastEvaluatedPrice | 1 |  |
| iobpsItemCost | 2 |  |

# SAPB1.InventoryPostingCopyOptionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ipcoNoCountersDiff | 0 |  |
| ipcoIndividual1CountedQuantity | 1 |  |
| ipcoIndividual2CountedQuantity | 2 |  |
| ipcoIndividual3CountedQuantity | 3 |  |
| ipcoIndividual4CountedQuantity | 4 |  |
| ipcoIndividual5CountedQuantity | 5 |  |
| ipcoTeamCountedQuantity | 6 |  |

# SAPB1.InventoryPostingPriceSourceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ippsByPriceList | 0 |  |
| ippsLastEvaluatedPrice | 1 |  |
| ippsItemCost | 2 |  |

# SAPB1.ISDDocStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| isd_Open | 0 |  |
| isd_Cancelled | 1 |  |

# SAPB1.ISDDocumentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| isd_GSTTaxInvoice | 18 |  |
| isd_GSTCreditMemo | 19 |  |
| isd_GSTDebitMemo | -18 |  |
| isd_GSTCreditMemoAndDebitMemo | -19 |  |

# SAPB1.ISDITCTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| isd_Eligible | 0 |  |
| isd_Ineligible | 1 |  |

# SAPB1.ISDSTATypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| isd_CGST | -100 |  |
| isd_SGST | -110 |  |
| isd_IGST | -120 |  |
| isd_CessGST | -130 |  |
| isd_UTGST | -150 |  |

# SAPB1.IssuePrimarilyByEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ipbSerialAndBatchNumbers | 0 |  |
| ipbBinLocations | 1 |  |

# SAPB1.ItemClassEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| itcService | 1 |  |
| itcMaterial | 2 |  |

# SAPB1.ItemTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| itItems | 0 |  |
| itLabor | 1 |  |
| itTravel | 2 |  |
| itFixedAssets | 3 |  |

# SAPB1.ItemUoMTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| iutPurchasing | 0 |  |
| iutSales | 1 |  |
| iutInventory | 2 |  |

# SAPB1.KPITypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| asSingle | 0 |  |
| asQuarterly | 1 |  |
| asMonthly | 2 |  |
| asMultiple | 3 |  |

# SAPB1.LandedCostAllocationByEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| asCashValueBeforeCustoms | 0 |  |
| asCashValueAfterCustoms | 1 |  |
| asQuantity | 2 |  |
| asWeight | 3 |  |
| asVolume | 4 |  |
| asEqual | 5 |  |
| asLegalCost | 6 |  |

# SAPB1.LandedCostBaseDocumentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| asDefault | 0 |  |
| asEmpty | 1 |  |
| asGoodsReceiptPO | 2 |  |
| asLandedCosts | 3 |  |
| asPurchaseInvoice | 4 |  |

# SAPB1.LandedCostCostCategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| lccc_CustomsVAT | 0 |  |
| lccc_ExciseCost | 1 |  |
| lccc_CustomsDuty | 2 |  |

# SAPB1.LandedCostDocStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| lcOpen | 0 |  |
| lcClosed | 1 |  |

# SAPB1.LCCostTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| asFixedCosts | 0 |  |
| asVariableCosts | 1 |  |
| asLegalCosts | 2 |  |

# SAPB1.LegalDataLineTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ldlt_DocumentTotal | 0 |  |
| ldlt_TaxPerLine | 1 |  |
| ldlt_TotalTax | 2 |  |

# SAPB1.LicenseTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| lkIdirect | 25 |  |
| lkSOAIndirect | 20 |  |
| lkSOA | 21 |  |
| lkB1iIndirect | 22 |  |
| lkB1i | 23 |  |

# SAPB1.LicenseUpdateTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ultAssign | 0 |  |
| ultRemove | 1 |  |

# SAPB1.LineStatusTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| lst_Open | 0 |  |
| lst_Closed | 1 |  |

# SAPB1.LineTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ltDocument | 0 |  |
| ltRounding | 1 |  |
| ltVat | 2 |  |

# SAPB1.LinkedDocTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ldtEmptyLink | 0 |  |
| ldtSalesOpportunitiesLink | 1 |  |
| ldtSalesQuotationsLink | 2 |  |
| ldtSalesOrdersLink | 3 |  |
| ldtDeliveriesLink | 4 |  |
| ldtARInvoicesLink | 5 |  |

# SAPB1.LinkReferenceTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| lrt_00 | 0 |  |
| lrt_01 | 1 |  |
| lrt_02 | 2 |  |
| lrt_03 | 3 |  |
| lrt_04 | 4 |  |
| lrt_05 | 5 |  |
| lrt_06 | 6 |  |
| lrt_07 | 7 |  |
| lrt_08 | 8 |  |
| lrt_MX_08 | 9 |  |
| lrt_MX_09 | 10 |  |

# SAPB1.LogonMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| lmBOneIntegrationFramework | 0 |  |
| lmStandardLogon | 1 |  |
| lmNoControl | 2 |  |

# SAPB1.MobileAddonSettingTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| mastModule | 0 |  |
| mastHome | 1 |  |

# SAPB1.MobileAppReportChoiceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| marSystemReport | 0 |  |
| marCustomizedReport | 1 |  |

# SAPB1.MultipleCounterRoleEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| mcrTeamCounter | 0 |  |
| mcrIndividualCounter | 1 |  |

# SAPB1.OperationCode347Enum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ocGoodsOrServiciesAcquisitions | 0 |  |
| ocPublicEntitiesAcquisitions | 1 |  |
| ocTravelAgenciesPurchases | 2 |  |
| ocSalesOrServicesRevenues | 3 |  |
| ocPublicSubsidies | 4 |  |
| ocTravelAgenciesSales | 5 |  |

# SAPB1.OperationCodeTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| octSummaryInvoicesEntry | 0 |  |
| octSummaryReceiptsEntry | 1 |  |
| octInvoicewithSeveralVATRates | 2 |  |
| octCorrectionInvoice | 3 |  |
| octDueVATPendingInvoiceIssuance | 4 |  |
| octExpensesIncurredbyTravelAgentforCustomers | 5 |  |
| octSpecialRegulationforVATGroup | 6 |  |
| octSpecialRegulationforGoldInvestment | 7 |  |
| octReverseChargeProcedure | 8 |  |
| octUnsummarizedReceipts | 9 |  |
| octIdentificationofErrorTransactions | 10 |  |
| octTransactionswithEntrepreneursIssuingReceiptsforAgriculturalCompensation | 11 |  |
| octServiceInvoicingbyTravelAgenciesonBehalfofThirdParties | 12 |  |
| octBusinessOfficeRental | 13 |  |
| octSubsidies | 14 |  |
| octIncomingPaymentsforIndustrialandIntellectualPropertyRights | 15 |  |
| octInsuranceTransactions | 16 |  |
| octPurchasesfromTravelAgencies | 17 |  |
| octTransactionsSubjecttoProductionServiceandImportTaxesinCeutaandMelilla | 18 |  |

# SAPB1.OpportunityTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| boOpSales | 1 |  |
| boOpPurchasing | 2 |  |

# SAPB1.PaymentInvoiceTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| itARInvoice | 0 |  |
| itARDownPaymentInvoice | 1 |  |

# SAPB1.PaymentMeansTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pmtNotAssigned | 0 |  |
| pmtChecks | 1 |  |
| pmtBankTransfer | 2 |  |
| pmtCash | 3 |  |
| pmtCreditCard | 4 |  |

# SAPB1.PaymentMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pm_Check | 0 |  |
| pm_BankTransfer | 1 |  |
| pm_BillOfExchange | 2 |  |
| pm_CreditCard | 3 |  |
| pm_Cash | 4 |  |

# SAPB1.PaymentRunExportRowTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| prtGeneral | 0 |  |
| prtPayOnAccount | 1 |  |
| prtPayToAccount | 2 |  |

# SAPB1.PaymentsAuthorizationStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pasWithout | 0 |  |
| pasPending | 1 |  |
| pasApproved | 2 |  |
| pasRejected | 3 |  |
| pasGenerated | 4 |  |
| pasGeneratedbyAuthorizer | 5 |  |
| pasCancelled | 6 |  |

# SAPB1.PaymentWizardTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pwt_Outgoing | 0 |  |
| pwt_Incoming | 1 |  |
| pwt_Both | 2 |  |

# SAPB1.PeriodStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ltUnlocked | 0 |  |
| ltUnlockedExceptSales | 1 |  |
| ltPeriodClosing | 2 |  |
| ltLocked | 3 |  |

# SAPB1.PMCategorizeTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pm_cat_Ignore | 0 |  |
| pm_cat_OpenAmountAP | 1 |  |
| pm_cat_OpenAmountAR | 2 |  |
| pm_cat_InvoicedAP | 3 |  |
| pm_cat_InvoicedAR | 4 |  |

# SAPB1.PMDocumentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pmdt_DocumentDraft | 112 |  |
| pmdt_ManualJournalEntry | 30 |  |
| pmdt_SalesQuotation | 23 |  |
| pmdt_SalesOrder | 17 |  |
| pmdt_Delivery | 15 |  |
| pmdt_Return | 16 |  |
| pmdt_ReturnRequest | 234000031 |  |
| pmdt_ARDownPaymentRequest | 203002 |  |
| pmdt_ARDownPaymentInvoice | 203 |  |
| pmdt_ARInvoice | 13 |  |
| pmdt_ARCreditMemo | 14 |  |
| pmdt_ARReserveInvoice | 13002 |  |
| pmdt_PurchaseQuotation | 540000006 |  |
| pmdt_PurchaseOrder | 22 |  |
| pmdt_PurchaseRequest | 1470000113 |  |
| pmdt_GoodsReceiptPO | 20 |  |
| pmdt_GoodsReturn | 21 |  |
| pmdt_GoodsReturnRequest | 234000032 |  |
| pmdt_APDownPaymentRequest | 204002 |  |
| pmdt_APDownPaymentInvoice | 204 |  |
| pmdt_APInvoice | 18 |  |
| pmdt_APCreditMemo | 19 |  |
| pmdt_APReserveInvoice | 18002 |  |
| pmdt_ServiceCall | 191 |  |
| pmdt_GoodsReceipt | 59 |  |
| pmdt_GoodsIssue | 60 |  |
| pmdt_ARCorrectionInvoice | 165 |  |
| pmdt_ARCorrectionInvoiceReversal | 166 |  |
| pmdt_APCorrectionInvoice | 163 |  |
| pmdt_APCorrectionInvoiceReversal | 164 |  |

# SAPB1.PMOperationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pm_op_Ignore | 0 |  |
| pm_op_Add | 1 |  |
| pm_op_Subtract | 2 |  |

# SAPB1.PostingMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pmGLAccountBankAccount | 0 |  |
| pmBussinessPartnerBankAccount | 1 |  |
| pmInterimAccountBankAccount | 2 |  |
| pmExternalReconciliation | 3 |  |
| pmIgnore | 4 |  |

# SAPB1.PostingOfDepreciationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| podDirectPosting | 0 |  |
| podIndirectPosting | 1 |  |

# SAPB1.PriceModeDocumentEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pmdNet | 0 |  |
| pmdGross | 1 |  |
| pmdNetAndGross | 2 |  |

# SAPB1.PriceModeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pmNet | 0 |  |
| pmGross | 1 |  |

# SAPB1.PriceProceedMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ppmRemove | 0 |  |
| ppmUpdate | 1 |  |
| ppmKeepCorresponding | 2 |  |
| ppmKeepAll | 3 |  |

# SAPB1.PrintOnEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| poBlankPaper | 0 |  |
| poDefault | 1 |  |
| poOverflowBlankPaper | 2 |  |
| poOverflowCheckStock | 3 |  |

# SAPB1.PrintStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| psNo | 0 |  |
| psYes | 1 |  |
| psAmended | 2 |  |

# SAPB1.ProductionItemType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pit_Item | 0 |  |
| pit_Resource | 1 |  |
| pit_Text | 2 |  |

# SAPB1.ProjectStatusTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pst_Started | 0 |  |
| pst_Paused | 1 |  |
| pst_Stopped | 2 |  |
| pst_Finished | 3 |  |
| pst_Canceled | 4 |  |

# SAPB1.ProjectTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| pt_External | 0 |  |
| pt_Internal | 1 |  |

# SAPB1.RclRecurringExecutionHandlingEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rehStopOnError | 1 |  |
| rehSkipTransaction | 2 |  |

# SAPB1.RclRecurringTransactionStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rtsNotExecuted | 1 |  |
| rtsExecuted | 2 |  |
| rtsRemoved | 3 |  |

# SAPB1.ReceivingBinLocationsMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rblmBinLocationCodeOrder | 0 |  |
| rblmAlternativeSortCodeOrder | 1 |  |

# SAPB1.ReceivingUpToMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rutmBothMaxQtyAndWeight | 0 |  |
| rutmMaximumQty | 1 |  |
| rutmMaximumWeight | 2 |  |

# SAPB1.RecipientTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rtUser | 0 |  |
| rtEmployee | 1 |  |

# SAPB1.ReconciliationAccountTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rat_GLAccount | 0 |  |
| rat_BusinessPartner | 1 |  |

# SAPB1.ReconSelectDateTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rsdtPostDate | 0 |  |
| rsdtDueDate | 1 |  |
| rsdtDocDate | 2 |  |

# SAPB1.ReconTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rtManual | 0 |  |
| rtAutomatic | 1 |  |
| rtSemiAutomatic | 2 |  |
| rtPayment | 3 |  |
| rtCreditMemo | 4 |  |
| rtReversal | 5 |  |
| rtZeroValue | 6 |  |
| rtCancellation | 7 |  |
| rtBoE | 8 |  |
| rtDeposit | 9 |  |
| rtBankStatementProcess | 10 |  |
| rtPeriodClosing | 11 |  |
| rtCorrectionInvoice | 12 |  |
| rtInventoryOrExpenseAllocation | 13 |  |
| rtWIP | 14 |  |
| rtDeferredTaxInterimAccount | 15 |  |
| rtDownPaymentAllocation | 16 |  |
| rtAutoConversionDifference | 17 |  |
| rtInterimDocument | 18 |  |

# SAPB1.RecurrenceDayOfWeekEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rdowDay | 0 |  |
| rdowWeekDay | 1 |  |
| rdowWeekendDay | 2 |  |
| rdowSun | 3 |  |
| rdowMon | 4 |  |
| rdowTue | 5 |  |
| rdowWed | 6 |  |
| rdowThu | 7 |  |
| rdowFri | 8 |  |
| rdowSat | 9 |  |

# SAPB1.RecurrencePatternEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rpNone | 0 |  |
| rpDaily | 1 |  |
| rpWeekly | 2 |  |
| rpMonthly | 3 |  |
| rpAnnually | 4 |  |

# SAPB1.RecurrenceSequenceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rsFirst | 0 |  |
| rsSecond | 1 |  |
| rsThird | 2 |  |
| rsFourth | 3 |  |
| rsLast | 4 |  |

# SAPB1.RecurringTransactionTemplateFrequencyEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rttf_Daily | 0 |  |
| rttf_Weekly | 1 |  |
| rttf_Every2Weeks | 2 |  |
| rttf_Monthly | 3 |  |
| rttf_Every2Months | 4 |  |
| rttf_Quarterly | 5 |  |
| rttf_Semiannually | 6 |  |
| rttf_Annually | 7 |  |
| rttf_OneTime | 8 |  |

# SAPB1.RecurringTransactionTemplateRemindEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rttr_Y | -1 |  |
| rttr_OnSunday | 1 |  |
| rttr_OnMonday | 2 |  |
| rttr_OnTuesday | 3 |  |
| rttr_OnWednesday | 4 |  |
| rttr_OnThursday | 5 |  |
| rttr_OnFriday | 6 |  |
| rttr_OnSaturday | 7 |  |
| rttr_Every1 | 101 |  |
| rttr_Every2 | 102 |  |
| rttr_Every3 | 103 |  |
| rttr_Every4 | 104 |  |
| rttr_Every5 | 105 |  |
| rttr_Every6 | 106 |  |
| rttr_Every7 | 107 |  |
| rttr_Every8 | 108 |  |
| rttr_Every9 | 109 |  |
| rttr_Every10 | 110 |  |
| rttr_Every11 | 111 |  |
| rttr_Every12 | 112 |  |
| rttr_Every13 | 113 |  |
| rttr_Every14 | 114 |  |
| rttr_Every15 | 115 |  |
| rttr_Every16 | 116 |  |
| rttr_Every17 | 117 |  |
| rttr_Every18 | 118 |  |
| rttr_Every19 | 119 |  |
| rttr_Every20 | 120 |  |
| rttr_Every21 | 121 |  |
| rttr_Every22 | 122 |  |
| rttr_Every23 | 123 |  |
| rttr_Every24 | 124 |  |
| rttr_Every25 | 125 |  |
| rttr_Every26 | 126 |  |
| rttr_Every27 | 127 |  |
| rttr_Every28 | 128 |  |
| rttr_Every29 | 129 |  |
| rttr_Every30 | 130 |  |
| rttr_Every31 | 131 |  |
| rttr_Every45 | 145 |  |
| rttr_Every60 | 160 |  |
| rttr_On1 | 1001 |  |
| rttr_On2 | 1002 |  |
| rttr_On3 | 1003 |  |
| rttr_On4 | 1004 |  |
| rttr_On5 | 1005 |  |
| rttr_On6 | 1006 |  |
| rttr_On7 | 1007 |  |
| rttr_On8 | 1008 |  |
| rttr_On9 | 1009 |  |
| rttr_On10 | 1010 |  |
| rttr_On11 | 1011 |  |
| rttr_On12 | 1012 |  |
| rttr_On13 | 1013 |  |
| rttr_On14 | 1014 |  |
| rttr_On15 | 1015 |  |
| rttr_On16 | 1016 |  |
| rttr_On17 | 1017 |  |
| rttr_On18 | 1018 |  |
| rttr_On19 | 1019 |  |
| rttr_On20 | 1020 |  |
| rttr_On21 | 1021 |  |
| rttr_On22 | 1022 |  |
| rttr_On23 | 1023 |  |
| rttr_On24 | 1024 |  |
| rttr_On25 | 1025 |  |
| rttr_On26 | 1026 |  |
| rttr_On27 | 1027 |  |
| rttr_On28 | 1028 |  |
| rttr_On29 | 1029 |  |
| rttr_On30 | 1030 |  |
| rttr_On31 | 1031 |  |

# SAPB1.ReferencedObjectTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rot_ExternalDocument | -1 |  |
| rot_SalesQuotation | 23 |  |
| rot_SalesOrder | 17 |  |
| rot_DeliveryNotes | 15 |  |
| rot_ReturnRequest | 234000031 |  |
| rot_Return | 16 |  |
| rot_DownPaymentIncoming | 203 |  |
| rot_SalesInvoice | 13 |  |
| rot_SalesCreditNote | 14 |  |
| rot_CorrectionSalesInvoice | 165 |  |
| rot_SalesTaxInvoice | 280 |  |
| rot_PurchaseQuotation | 540000006 |  |
| rot_PurchaseOrder | 22 |  |
| rot_GoodsReceiptPO | 20 |  |
| rot_GoodsReturnRequest | 234000032 |  |
| rot_GoodsReturn | 21 |  |
| rot_DownPaymentOutgoing | 204 |  |
| rot_PurchaseInvoice | 18 |  |
| rot_PurchaseCreditNote | 19 |  |
| rot_CorrectionPurchaseInvoice | 163 |  |
| rot_PurchaseTaxInvoice | 281 |  |
| rot_LandedCosts | 69 |  |
| rot_IncomingPayments | 24 |  |
| rot_JournalEntry | 30 |  |
| rot_ProductionOrder | 202 |  |
| rot_InternalReconciliation | 321 |  |
| rot_OriginalInvoice | 13001 |  |
| rot_OriginalARDownPayment | 20301 |  |
| rot_PurchaseRequest | 1470000113 |  |
| rot_GoodsReceipt | 59 |  |
| rot_GoodsIssue | 60 |  |
| rot_InventoryTransferRequest | 1250000001 |  |
| rot_InventoryTransfer | 67 |  |
| rot_ChecksforPayment | 57 |  |
| rot_MaterialRevaluation | 162 |  |
| rot_InventoryCounting | 1470000065 |  |
| rot_InventoryPosting | 10000071 |  |
| rot_OutgoingPayments | 46 |  |

# SAPB1.RelatedDocumentTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rdt_Payment | 24 |  |
| rdt_Reconciliation | 321 |  |

# SAPB1.RepeatOptionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| roByDate | 0 |  |
| roByWeekDay | 1 |  |

# SAPB1.Report349CodeListEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| r349cA | 0 |  |
| r349cE | 1 |  |
| r349cEmpty | 2 |  |
| r349cH | 3 |  |
| r349cI | 4 |  |
| r349cM | 5 |  |
| r349cS | 6 |  |
| r349cT | 7 |  |

# SAPB1.ReportLayoutCategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlcPLD | 0 |  |
| rlcCrystal | 1 |  |
| rlcLegalList | 2 |  |
| rlcUserDefinedType | 3 |  |

# SAPB1.ResidenceNumberTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rntSpanishFiscalID | 0 |  |
| rntVATRegistrationNumber | 1 |  |
| rntPassport | 2 |  |
| rntFiscalIDIssuedbytheResidenceCountry | 3 |  |
| rntCertificateofFiscalResidence | 4 |  |
| rntOtherDocument | 5 |  |

# SAPB1.ResourceAllocationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| raOnStartDate | 0 |  |
| raOnEndDate | 1 |  |
| raStartDateForwards | 2 |  |
| raEndDateBackwards | 3 |  |

# SAPB1.ResourceCapacityActionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rcaUnknown | 0 |  |
| rcaProductionOrderCreate | 1 |  |
| rcaProductionOrderClose | 2 |  |
| rcaProductionOrderReschedule | 3 |  |
| rcaProductionOrderAddLine | 4 |  |
| rcaProductionOrderDeleteLine | 5 |  |
| rcaProductionOrderUpdateLine | 6 |  |
| rcaIssueForProductionCreate | 7 |  |
| rcaReceiptFromProductionCreate | 8 |  |

# SAPB1.ResourceCapacityBaseTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rcbtNone | 0 |  |
| rcbtProductionOrder | 202 |  |

# SAPB1.ResourceCapacityMemoSourceEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rcmsUnknown | 0 |  |
| rcmsResourceCapacityForm | 1 |  |
| rcmsSetDailyInternalCapacitiesForm | 2 |  |

# SAPB1.ResourceCapacityOwningTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rcotNone | 0 |  |
| rcotProductionOrder | 202 |  |
| rcotIssueForProduction | 60 |  |
| rcotReceiptFromProduction | 59 |  |

# SAPB1.ResourceCapacityRevertedTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rcrtNone | 0 |  |
| rcrtIssueForProduction | 60 |  |

# SAPB1.ResourceCapacitySourceTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rcstNone | 0 |  |
| rcstProductionOrder | 202 |  |
| rcstIssueForProduction | 60 |  |
| rcstReceiptFromProduction | 59 |  |

# SAPB1.ResourceCapacityTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rctInternal | 0 |  |
| rctOrdered | 1 |  |
| rctCommitted | 2 |  |
| rctConsumed | 3 |  |

# SAPB1.ResourceDailyCapacityWeekdayEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rdcwFirst | 0 |  |
| rdcwSecond | 1 |  |
| rdcwThird | 2 |  |
| rdcwFourth | 3 |  |
| rdcwFifth | 4 |  |
| rdcwSixth | 5 |  |
| rdcwSeventh | 6 |  |

# SAPB1.ResourceIssueMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rimBackflush | 0 |  |
| rimManual | 1 |  |

# SAPB1.ResourceTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rtMachine | 0 |  |
| rtLabor | 1 |  |
| rtOther | 2 |  |

# SAPB1.RetirementMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rmGross | 0 |  |
| rmNet | 1 |  |

# SAPB1.RetirementPeriodControlEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rpcProRataTemporis | 0 |  |
| rpcHalfYearConvention | 1 |  |
| rpcOnlyAfterEndOfUsefulLife | 2 |  |

# SAPB1.RetirementProRataTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rprtExactlyDailyBase | 0 |  |
| rprtLastDayOfPriorPeriod | 1 |  |
| rprtLastDayOfCurrentPeriod | 2 |  |

# SAPB1.ReturnTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rt26Q | 0 |  |
| rt27Q | 1 |  |
| rt27EQ | 2 |  |

# SAPB1.RiskLevelTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rlt_Low | 0 |  |
| rlt_Medium | 1 |  |
| rlt_High | 2 |  |

# SAPB1.RoundingContextEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rcSum | 7 |  |
| rcPrice | 8 |  |
| rcRate | 9 |  |
| rcQuantity | 10 |  |
| rcMeasure | 11 |  |
| rcPercent | 12 |  |
| rcTax | 13 |  |
| rcTaxPerGroup | 14 |  |
| rcBudgetSum | 16 |  |
| rcPriceListSum | 17 |  |
| rcRealAmountInPayment | 18 |  |
| rcStockSumRoundUp | 19 |  |
| rcDocHeaderTotal | 20 |  |
| rcVatReportAmount | 21 |  |
| rcLineGrossTotal | 22 |  |
| rcExpenseTotal | 23 |  |
| rcWTax | 24 |  |
| rcBASCode | 25 |  |
| rcTaxForPrice | 26 |  |

# SAPB1.RoundingSysEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rsNoRounding | 0 |  |
| rsRoundToFiveHundredth | 1 |  |
| rsRoundToOne | 2 |  |
| rsRoundToTen | 3 |  |
| rsRoundToTenHundredth | 4 |  |

# SAPB1.RoundingTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| rt_TruncatedAU | 0 |  |
| rt_CommercialValues | 1 |  |
| rt_NoRounding | 2 |  |

# SAPB1.SAFTProductTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| saftpt_Products | 0 |  |
| saftpt_Services | 1 |  |
| saftpt_Other | 2 |  |
| saftpt_Taxes | 3 |  |
| saftpt_NonSystem | 4 |  |

# SAPB1.SAFTTaxCodeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| safttc_ReducedTax | 0 |  |
| safttc_MiddleTax | 1 |  |
| safttc_NormalTax | 2 |  |
| safttc_Exempt | 3 |  |
| safttt_Others | 4 |  |
| safttc_NonSystem | 5 |  |

# SAPB1.SAFTTransactionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| safttt_Default | 0 |  |
| safttt_Normal | 1 |  |
| safttt_AdjustmentsofTheTaxPeriod | 2 |  |
| safttt_MeasurementofResults | 3 |  |
| safttt_Adjustment | 4 |  |
| safttt_DoNotExport | 5 |  |
| safttt_NonSystem | 6 |  |

# SAPB1.SEPASequenceTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sstOOFF | 0 |  |
| sstFRST | 1 |  |
| sstRCUR | 2 |  |
| sstFNAL | 3 |  |

# SAPB1.Services (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| MessagesService | 81 |  |
| CompanyService | 1003 |  |
| SeriesService | 35 |  |
| ReportLayoutsService | 232 |  |
| FormPreferencesService | 41 |  |
| AccountsService | 1001 |  |
| BusinessPartnersService | 2 |  |

# SAPB1.ServiceTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| srvcSales | 1 |  |
| srvcPurchasing | 2 |  |

# SAPB1.ShaamGroupEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sgServicesAndAsset | 0 |  |
| sgAgriculturalProducts | 1 |  |
| sgInsuranceCommissions | 2 |  |
| sgWHTaxInstructions | 3 |  |
| sgInterestExchangeRateDiffs | 4 |  |
| sgRentalFees | 5 |  |

# SAPB1.SingleUserConnectionActionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sucaWarning | 0 |  |
| sucaBlock | 1 |  |

# SAPB1.SOIExcisableTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| se_Excisable | 1 |  |
| se_Exemption | 2 |  |
| se_PaidToOther | 3 |  |
| se_NotExcisable | 4 |  |

# SAPB1.SortOrderEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| soAscending | 0 |  |
| soDescending | 1 |  |

# SAPB1.SourceCurrencyEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sc_PrimaryCurrency | 0 |  |
| sc_AdditionalCurrency1 | 1 |  |
| sc_AdditionalCurrency2 | 2 |  |

# SAPB1.SpecialDepreciationCalculationMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| spcmAdditional | 0 |  |
| spcmAlternative | 1 |  |

# SAPB1.SpecialDepreciationMaximumFlagEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| spmfPercentage | 0 |  |
| spmfAmount | 1 |  |

# SAPB1.SpecialProductTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sptMT | 0 |  |
| sptIO | 1 |  |

# SAPB1.SPEDContabilAccountPurposeCode (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| spedContasDeAtivo | 0 |  |
| spedContasDePassivo | 1 |  |
| spedPatrimonioLiquido | 2 |  |
| spedContasDeResultado | 3 |  |
| spedContasDeCompensacao | 4 |  |
| spedOutras | 5 |  |

# SAPB1.SPEDContabilQualificationCodeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| spedNA | 0 |  |
| spedDiretor | 1 |  |
| spedConselheiroDeAdministracao | 2 |  |
| spedAdministrador | 3 |  |
| spedAdministradorDoGrupo | 4 |  |
| spedAdministradorDeSociedadeFiliada | 5 |  |
| spedAdministradorJudicialPessoaFisica | 6 |  |
| spedAdministradorJudicialPessoaJuridicaProfissionalResponsavel | 7 |  |
| spedAdministradorJudicialGestor | 8 |  |
| spedGestorJudicial | 9 |  |
| spedProcurador | 10 |  |
| spedInventariante | 11 |  |
| spedLiquidante | 12 |  |
| spedInterventor | 13 |  |
| spedEmpresario | 14 |  |
| spedContador | 15 |  |
| spedOutros | 16 |  |

# SAPB1.StageDepTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sdt_Project | 0 |  |
| sdt_Subproject | 1 |  |

# SAPB1.StockTransferAuthorizationStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sasWithout | 0 |  |
| sasPending | 1 |  |
| sasApproved | 2 |  |
| sasRejected | 3 |  |
| sasGenerated | 4 |  |
| sasGeneratedbyAuthorizer | 5 |  |
| sasCancelled | 6 |  |

# SAPB1.StraightLineCalculationMethodEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| slcmAuquisitionValueDividedByTotalUsefulLife | 0 |  |
| slcmPercentageOfAcquisitionValue | 1 |  |
| slcmNetBookValueDividedByRemainingLife | 2 |  |

# SAPB1.StraightLinePeriodControlDepreciationPeriodsEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| slpcdpStandard | 0 |  |
| slpcdpIndividual | 1 |  |
| slpcdpIndividualUsage | 2 |  |

# SAPB1.SubprojectStatusTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sst_Open | 0 |  |
| sst_Closed | 1 |  |

# SAPB1.SubsequentAcquisitionPeriodControlEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| sapcProRataTemporis | 0 |  |
| sapcHalfYearConvention | 1 |  |
| sapcFullYear | 2 |  |

# SAPB1.SubsequentAcquisitionProRataTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| saprtExactlyDailyBase | 0 |  |
| saprtFirstDayOfCurrentPeriod | 1 |  |
| saprtFirstDayOfNextPeriod | 2 |  |

# SAPB1.SupportUserLoginRecordLogReasonTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| reasonTransIssueAnaly | 0 |  |
| reasonSetupIssueAnaly | 1 |  |
| reasonDataIssueAnaly | 2 |  |
| reasonAddonIssueAnaly | 3 |  |
| reasonCustomerIssueAnaly | 4 |  |
| reasonSystemMaint | 5 |  |
| reasonConsulting | 6 |  |
| reasonOther | 7 |  |
| reasonAddonAccess | 8 |  |
| reasonRootCauseAnaly | 9 |  |
| reasonConsultSupport | 10 |  |

# SAPB1.TargetGroupsDetailStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tdsActive | 0 |  |
| tdsInactive | 1 |  |

# SAPB1.TargetGroupTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tgtCustomer | 0 |  |
| tgtVendor | 1 |  |

# SAPB1.TaxCalcSysEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| PreconfiguredFormulaWithJurisdictionSupport | 0 |  |
| UserDefinedFormula | 1 |  |
| PreconfiguredFormula | 2 |  |

# SAPB1.TaxCodeDeterminationTCDByUsageTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tcdbutDefaultSales | 0 |  |
| tcdbutDefaultPurchase | 1 |  |
| tcdbutLine | 2 |  |

# SAPB1.TaxCodeDeterminationTCDDefaultWTTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tcddwttDefaultSales | 0 |  |
| tcddwttDefaultPurchase | 1 |  |
| tcddwttLine | 2 |  |

# SAPB1.TaxCodeDeterminationTCDTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tcdtMaterialItem | 0 |  |
| tcdtServiceItem | 1 |  |
| tcdtServiceDocument | 2 |  |
| tcdtWithholdingTax | 3 |  |

# SAPB1.TaxInvoiceReportLineTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| LineOfBusinessPlace | 1 |  |
| LineOfBusinessPartner | 2 |  |
| LineOfDocument | 3 |  |
| LineOfItem | 4 |  |

# SAPB1.TaxInvoiceReportNTSApprovedEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| NotApproved | 0 |  |
| Approved | 1 |  |

# SAPB1.TaxRateDeterminationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trd_PostingDate | 0 |  |
| trd_DocumentDate | 1 |  |

# SAPB1.TaxReportFilterApArDocumentType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trfadt_APDocuments | 0 |  |
| trfadt_ARDocuments | 1 |  |

# SAPB1.TaxReportFilterDeclarationType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trfdt_Original | 0 |  |
| trfdt_Substitute | 1 |  |
| trfdt_Complementary | 2 |  |

# SAPB1.TaxReportFilterDocumentType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trfdt_ARInvoices | 0 |  |
| trfdt_ARCreditMemos | 1 |  |
| trfdt_APInvoices | 2 |  |
| trfdt_APCreditMemos | 3 |  |
| trfdt_IncomingPayments | 4 |  |
| trfdt_JournalEntries | 5 |  |
| trfdt_OutgoingPayments | 6 |  |
| trfdt_ChecksforPayment | 7 |  |
| trfdt_InventoryTransfers | 8 |  |
| trfdt_ARDownPayment | 9 |  |
| trfdt_APDownPayment | 10 |  |

# SAPB1.TaxReportFilterPeriod (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trfP_Quarter | 0 |  |
| trfP_Year | 1 |  |
| trfP_Month | 2 |  |
| trfP_NULL | 3 |  |

# SAPB1.TaxReportFilterQuarterOrDates (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trfqd_Interval | 0 |  |
| trfqd_Date | 1 |  |

# SAPB1.TaxReportFilterReportLayoutType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trfrlt_RegisterBookLayout | 0 |  |
| trfrlt_DeclarationLayout | 1 |  |

# SAPB1.TaxReportFilterType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| trft_TaxReport | 0 |  |
| trft_WTReport | 1 |  |
| trft_Report347 | 2 |  |
| trft_Report349 | 3 |  |
| trft_ReconciliationReport | 4 |  |
| trft_StampTax | 5 |  |
| trft_SalesReport | 6 |  |
| trft_None | 7 |  |
| trft_BoxReport | 8 |  |
| trft_AppendixOP | 9 |  |
| trft_AnnualSalesReport | 10 |  |
| trft_VATRefundReport | 11 |  |

# SAPB1.TaxTypeBlackListEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ttblExcluded | 0 |  |
| ttblExempt | 1 |  |
| ttblNonSubject | 2 |  |
| ttblNotTaxable | 3 |  |
| ttblTaxable | 4 |  |

# SAPB1.TCSAccumulationBaseEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tcsAccumulationOnInvoice | 0 |  |
| tcsAccumulationOnPayment | 1 |  |

# SAPB1.TdsTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| wtETds | 0 |  |
| wtGstTds | 1 |  |
| wtGstTcs | 2 |  |
| wtTcs | 3 |  |

# SAPB1.ThreatLevelEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tlLow | 0 |  |
| tlMedium | 1 |  |
| tlHigh | 2 |  |

# SAPB1.TimeSheetTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tsh_Employee | 0 |  |
| tsh_User | 1 |  |
| tsh_Other | 2 |  |

# SAPB1.TransactionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| Created | 0 |  |
| Updated | 1 |  |
| Deleted | 2 |  |
| Cancelled | 3 |  |
| Reopened | 4 |  |
| Closed | 5 |  |

# SAPB1.TransferSourcePeriodControlEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tspcProRataTemporis | 0 |  |

# SAPB1.TransferSourceProRataTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tsprtExactlyDailyBase | 0 |  |
| tsprtLastDayOfPriorPeriod | 1 |  |
| tsprtLastDayofCurrentPeriod | 2 |  |

# SAPB1.TransferTargetPeriodControlEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ttpcProRataTemporis | 0 |  |

# SAPB1.TransferTargetProRataTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ttprtExactlyDailyBase | 0 |  |
| ttprtFirstDayOfCurrentPeriod | 1 |  |
| ttprtFirstDayOfNextPeriod | 2 |  |

# SAPB1.TranslationCategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| asCRReport | 0 |  |
| asMenuItem | 1 |  |
| asEFMItem | 2 |  |

# SAPB1.TransTypesEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ttAllTransactions | 0 |  |
| ttOpeningBalance | 1 |  |
| ttClosingBalance | 2 |  |
| ttARInvoice | 3 |  |
| ttARCredItnote | 4 |  |
| ttDelivery | 5 |  |
| ttReturn | 6 |  |
| ttAPInvoice | 7 |  |
| ttAPCreditNote | 8 |  |
| ttPurchaseDeliveryNote | 9 |  |
| ttPurchaseReturn | 10 |  |
| ttReceipt | 11 |  |
| ttDeposit | 12 |  |
| ttJournalEntry | 13 |  |
| ttVendorPayment | 14 |  |
| ttChequesForPayment | 15 |  |
| ttStockList | 16 |  |
| ttGeneralReceiptToStock | 17 |  |
| ttGeneralReleaseFromStock | 18 |  |
| ttTransferBetweenWarehouses | 19 |  |
| ttWorkInstructions | 20 |  |
| ttLandedCosts | 21 |  |
| ttDeferredDeposit | 22 |  |
| ttCorrectionInvoice | 23 |  |
| ttInventoryValuation | 24 |  |
| ttAPCorrectionInvoice | 25 |  |
| ttAPCorrectionInvoiceReversal | 26 |  |
| ttARCorrectionInvoice | 27 |  |
| ttARCorrectionInvoiceReversal | 28 |  |
| ttBoETransaction | 29 |  |
| ttProductionOrder | 30 |  |
| ttDownPayment | 31 |  |
| ttPurchaseDownPayment | 32 |  |
| ttInternalReconciliation | 33 |  |
| ttInventoryPosting | 34 |  |
| ttInventoryOpeningBalance | 35 |  |

# SAPB1.TypeOfAdvancedRulesEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| toarGeneral | 0 |  |
| toarWarehouse | 1 |  |
| toarItemGroup | 2 |  |

# SAPB1.TypeOfOperationEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| tooProfessionalServices | 1 |  |
| tooRentingAssets | 2 |  |
| tooOthers | 3 |  |
| tooDisposalOfGoods | 4 |  |
| tooImportOfGoodsAndServices | 5 |  |
| tooImportByVirtualTransfer | 6 |  |
| tooGlobalOperations | 7 |  |

# SAPB1.UDFLinkedSystemObjectTypesEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| ulNone | 0 |  |
| ulChartOfAccounts | 1 |  |
| ulBusinessPartners | 2 |  |
| ulBanks | 3 |  |
| ulItems | 4 |  |
| ulUsers | 12 |  |
| ulInvoices | 13 |  |
| ulCreditNotes | 14 |  |
| ulDeliveryNotes | 15 |  |
| ulReturns | 16 |  |
| ulOrders | 17 |  |
| ulPurchaseInvoices | 18 |  |
| ulPurchaseCreditNotes | 19 |  |
| ulPurchaseDeliveryNotes | 20 |  |
| ulPurchaseReturns | 21 |  |
| ulPurchaseOrders | 22 |  |
| ulQuotations | 23 |  |
| ulIncomingPayments | 24 |  |
| ulDepositsService | 25 |  |
| ulJournalEntries | 30 |  |
| ulContacts | 33 |  |
| ulVendorPayments | 46 |  |
| ulChecksforPayment | 57 |  |
| ulInventoryGenEntry | 59 |  |
| ulInventoryGenExit | 60 |  |
| ulWarehouses | 64 |  |
| ulProductTrees | 66 |  |
| ulStockTransfer | 67 |  |
| ulSalesOpportunities | 97 |  |
| ulDrafts | 112 |  |
| ulMaterialRevaluation | 162 |  |
| ulEmployeesInfo | 171 |  |
| ulCustomerEquipmentCards | 176 |  |
| ulServiceContracts | 190 |  |
| ulServiceCalls | 191 |  |
| ulProductionOrders | 202 |  |
| ulInventoryTransferRequest | 1250000001 |  |
| ulBlanketAgreementsService | 1250000025 |  |
| ulProjectManagementService | 234000021 |  |
| ulReturnRequest | 234000031 |  |
| ulGoodsReturnRequest | 234000032 |  |
| ulSalesEmployee | 53 |  |
| ulLocations | 144 |  |
| ulStates | 130 |  |
| ulResources | 290 |  |
| ulUnitsofMeasure | 10000199 |  |
| ulPaymentTerms | 40 |  |
| ulPriceLists | 6 |  |
| ulBranches | 247 |  |

# SAPB1.UserAccessLogReasonIDTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| reasonPlanInitialSystConf | 0 |  |
| reasonPlanSystConfChang | 1 |  |
| reasonPlanSystMaint | 2 |  |
| reasonPlanKnowlTrans2EndUsr | 3 |  |
| reasonUnplanRootCauseAnaly | 4 |  |
| reasonUnplanKnowlTrans2EndUsr | 5 |  |
| reasonUnplanSystMaint | 6 |  |
| reasonUnplanSystConfChang | 7 |  |
| reasonSystMaint | 8 |  |
| reasonRootCauseAnaly | 9 |  |
| reasonConsultSupport | 10 |  |
| reasonOther | 11 |  |

# SAPB1.UserActionTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| actionLogin | 0 |  |
| actionLoginFail | 1 |  |
| actionLogoff | 2 |  |
| actionCreateUser | 3 |  |
| actionRemoveUser | 4 |  |
| actionSelectSU | 5 |  |
| actionDeselectSU | 6 |  |
| actionLock | 7 |  |
| actionUnlock | 8 |  |
| actionChPasswd | 9 |  |
| actionUnlockFail | 10 |  |

# SAPB1.UserGroupCategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| gc_Authorization | 0 |  |
| gc_Formsetting | 1 |  |
| gc_Alert | 2 |  |
| gc_UITmplate | 3 |  |
| gc_All | 4 |  |

# SAPB1.UserMenuItemTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| umitForm | 0 |  |
| umitQuery | 1 |  |
| umitFolder | 2 |  |
| umitReport | 3 |  |
| umitLink | 4 |  |

# SAPB1.UserQueryTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| uqtRegular | 0 |  |
| uqtWizard | 1 |  |
| uqtGenerator | 2 |  |
| uqtStoredProcedure | 3 |  |

# SAPB1.VatGroupsTaxRegionEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| vgtrPT | 0 |  |
| vgtrPT_AC | 1 |  |
| vgtrPT_MA | 2 |  |

# SAPB1.ViewStyleTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| vstPage | 0 |  |
| vstFullScreen | 1 |  |
| vstLandscape | 2 |  |

# SAPB1.VMCommunicationStatusEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| vmcs_Pending | 0 |  |
| vmcs_Error | 1 |  |
| vmcs_Successful | 2 |  |
| vmcs_New | 3 |  |
| vmcs_Rejected | 4 |  |

# SAPB1.VMCommunicationTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| vmct_MasterData | 0 |  |
| vmct_Transaction | 1 |  |

# SAPB1.WebhookStateEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| Active | 0 |  |
| Inactive | 1 |  |
| Exceptional | 2 |  |

# SAPB1.WebhookWorkModeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| Standard | 0 |  |
| Replay | 1 |  |

# SAPB1.WithholdingTaxCodeBaseTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| wtcbt_Gross | 0 |  |
| wtcbt_Net | 1 |  |
| wtcbt_VAT | 2 |  |
| wtcbt_Gross_VAT | 3 |  |
| wtcbt_UoM | 4 |  |

# SAPB1.WithholdingTaxCodeCategoryEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| wtcc_Invoice | 0 |  |
| wtcc_Payment | 1 |  |

# SAPB1.WithholdingTypeEnum (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| wt_VatWithholding | 0 |  |
| wt_IncomeTaxWithholding | 1 |  |

# SAPB1.WTDDetailType (EnumType)

UnderlyingType: Edm.Int32

| Member | Value | Scalar annotations |
|---|---:|---|
| Allowed | 0 |  |
| SpecialRate | 1 |  |
| Exemption | 2 |  |
