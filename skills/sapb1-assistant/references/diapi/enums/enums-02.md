<!-- source: REFDI.chm, SAP Business One DI API 10.0 (10.00.190) | version: DI API 10.0 | verified: 2026-10-01 -->

# BoProductionOrderTypeEnum (Enumeration)

Specifies the production order types.

| Member | Value | Description |
|---|---|---|
| bopotStandard | 0 | A production order type for producing a regular production item (default), using a production bill of materials. |
| bopotSpecial | 1 | A production order type for producing and repairing items that can be any inventory item. |
| bopotDisassembly | 2 | A production order type for dismantling a parent item to its components, using a production Bill of Materials. |

# BoQueryConditions (Enumeration)

Specifies the query conditions.

| Member | Value | Description |
|---|---|---|
| bqc_Equal | 0 | The query conditions is set to Equal. |
| bqc_NotEqual | 1 | The query conditions is set to Not Equal. |
| bqc_Like | 2 | The query conditions is set to Like. |

# BoQueryTypeEnum (Enumeration)

Specifies Query Type.

| Member | Value | Description |
|---|---|---|
| qtRegular | 0 | Regular query type |
| qtWizard | 1 | Wizard query type. |

# BoRcptCredTypes (Enumeration)

Specifies the way for providing the credit card details.

| Member | Value | Description |
|---|---|---|
| cr_Regular | 0 | The client provides the credit card details directly. |
| cr_Telephone | 1 | The client provides the credit card details through the telephone or the Internet. |
| cr_InternetTransaction | 2 | The client provides the credit card details using Internet Transaction. |

# BoRcptInvTypes (Enumeration)

Invoice types.

| Member | Value | Description |
|---|---|---|
| it_AllTransactions | -1 | All transactions |
| it_OpeningBalance | -2 | Transactions with open balance |
| it_ClosingBalance | -3 | Transactions with closing balance |
| it_Invoice | 13 | Sales invoice transaction |
| it_CredItnote | 14 | Sales credit memo transaction |
| it_TaxInvoice | 15 | Tax invoice transaction |
| it_Return | 16 | Sales goods returned transaction |
| it_PurchaseInvoice | 18 | Purchase transaction |
| it_PurchaseCreditNote | 19 | Purchase credit memo transaction |
| it_PurchaseDeliveryNote | 20 | Purchase good receipt PO transaction |
| it_PurchaseReturn | 21 | Purchase goods return transaction |
| it_Receipt | 24 | Incoming payment transaction |
| it_Deposit | 25 | Deposit transaction |
| it_JournalEntry | 30 | Journal entry transaction |
| it_PaymentAdvice | 46 | Vendor payment transaction |
| it_ChequesForPayment | 57 | Check for payment transaction |
| it_StockReconciliations | 58 | Stock reconciliation transaction |
| it_GeneralReceiptToStock | 59 | Goods receipt PO transaction |
| it_GeneralReleaseFromStock | 60 | Goods issue transaction |
| it_TransferBetweenWarehouses | 67 | Stock transfer transaction |
| it_WorkInstructions | 68 | Work instruction |
| it_DeferredDeposit | 76 | Predated deposit transaction |
| it_CorrectionInvoice | 132 | Correction invoice |
| it_APCorrectionInvoice | 163 | A/P correction invoice |
| it_ARCorrectionInvoice | 165 | A/R correction invoice |
| it_DownPayment | 203 | Down payment |
| it_PurchaseDownPayment | 204 | Purchase down payment. |

# BoRcptTypes (Enumeration)

Indicates the type of the payment recipient.

| Member | Value | Description |
|---|---|---|
| rCustomer | 0 | Payment to or from a customer. |
| rAccount | 1 | Payment is not directly connected with customer or vendor. |
| rSupplier | 2 | Payment to or from a Vendor. |

# BoRecCommParamTypes (Enumeration)

Indicates the command parameter types.

| Member | Value | Description |
|---|---|---|
| rcpt_In | 0 | In Parameter type. |
| rcpt_Out | 1 | Out Parameter type. |

# BoRemindUnits (Enumeration)

Specifies the reminder time units.

| Member | Value | Description |
|---|---|---|
| reu_Days | 0 | Days. |
| reu_Weeks | 1 | Weeks. |
| reu_Month | 2 | Months. |

# BoReportLayoutItemTypeEnum (Enumeration)

Specifies Report Layout items type.

| Member | Value | Description |
|---|---|---|
| rlitPageHeader | 0 | Report layout Header item type. |
| rlitStartOfReport | 1 | Report layout Start Of Report item type. |
| rlitRepetitiveAreaHeader | 2 | Report layout Repetitive Area Header item type. |
| rlitRepetitiveArea | 3 | Report layout Repetitive Area item type. |
| rlitRepetitiveAreaFooter | 4 | Report layout Repetitive Area Footer item type. |
| rlitEndOfReport | 5 | Report layout End Of Report item type. |
| rlitPageFooter | 6 | Report layout Page Footer item type. |
| rlitTextField | 7 | Report layout Text Field item type. |
| rlitPictureField | 8 | Report layout Picture Field item type. |
| rlitUserField | 9 | Report layout User Field item type. |

# BoResolutionUnits (Enumeration)

Specifies the units for the maximum time required to resolve a service call.

| Member | Value | Description |
|---|---|---|
| rsu_Days | 0 | Days |
| rsu_Hours | 1 | Hours |

# BoResponseUnit (Enumeration)

Specifies the units for the maximum time required to response to a service call.

| Member | Value | Description |
|---|---|---|
| boru_Hour | 0 | Hours |
| boru_Day | 1 | Days |

# BoRoleInTeam (Enumeration)

Specifies whether the employee is a Member or a Leader of the team.

| Member | Value | Description |
|---|---|---|
| borit_Member | 0 | The employee is a Member of the team. |
| borit_Leader | 1 | The employee is a Leader of the team. |

# BoRoundingMethod (Enumeration)

Defines the rounding methods of the of the item prices calculation.

| Member | Value | Description |
|---|---|---|
| borm_NoRounding | 0 | No rounding. |
| borm_RoundToFullDecAmount | 1 | Round to full decimal amount. |
| borm_RoundToFullAmount | 2 | Round to full amount. |
| borm_RoundToFullTensAmount | 3 | Round to full tens amount. |
| borm_FixedEnding | 4 |  |
| borm_FixedInterval | 5 |  |

# BoRoundingRule (Enumeration)

| Member | Value | Description |
|---|---|---|
| borrRoundDown | 0 |  |
| borrRoundUp | 1 |  |
| borrRoundOff | 2 |  |

# BoSalaryCostUnits (Enumeration)

Specifies the salary cost units.

| Member | Value | Description |
|---|---|---|
| scu_Hour | 0 | Salary cost per Hour. |
| scu_Day | 1 | Salary cost per Day. |
| scu_Week | 2 | Salary cost per Week. |
| scu_Month | 3 | Salary cost per Month. |
| scu_Year | 4 | Salary cost per Year. |
| scu_Semimonthly | 5 |  |
| scu_Biweekly | 6 |  |

# BoSerialNumberStatus (Enumeration)

Specifies the location of the equipment.

| Member | Value | Description |
|---|---|---|
| sns_Active | 0 | This equipment is active at the customer premises. |
| sns_Returned | 1 | This equipment is returned from the customer premises. |
| sns_Terminated | 2 | This equipment is out of the customer inventory. |
| sns_Loaned | 3 | This equipment is loaned to the customer in return or as a replacement equipment. |
| sns_InLab | 4 | This equipment is in the lab for repair. |

# BoSeriesGroupEnum (Enumeration)

Specifies Report's series-group parameter.

| Member | Value | Description |
|---|---|---|
| sg_Group1 | 1 | Series group 1. |
| sg_Group2 | 2 | Series group 2. |
| sg_Group3 | 3 | Series group 3. |
| sg_Group4 | 4 | Series group 4. |
| sg_Group5 | 5 | Series group 5. |
| sg_Group6 | 6 | Series group 6. |
| sg_Group7 | 7 | Series group 7. |
| sg_Group8 | 8 | Series group 8. |
| sg_Group9 | 9 | Series group 10. |
| sg_Group10 | 10 | Series group 10. |

# BoSeriesTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| stDocument | 0 |  |
| stBusinessPartner | 1 |  |
| stItem | 2 |  |
| stResource | 3 |  |

# BoServicePaymentMethods (Enumeration)

| Member | Value | Description |
|---|---|---|
| spmAcreditedToBankAccount | 0 |  |
| spmBankTransfer | 1 |  |
| spmOther | 2 |  |

# BoServiceSupplyMethods (Enumeration)

| Member | Value | Description |
|---|---|---|
| ssmImmediate | 0 |  |
| ssmToMoreResumptions | 1 |  |

# BoServiceTypes (Enumeration)

Specifies the service type for the service contract.

| Member | Value | Description |
|---|---|---|
| bst_Regular | 0 | Regular service. |
| bst_Warranty | 1 | Warranty service. |

# BoSoClosedInTypes (Enumeration)

Defines the date types for closing sales opportunities.

| Member | Value | Description |
|---|---|---|
| sos_Months | 0 | Months. |
| sos_Weeks | 1 | Weeks. |
| sos_Days | 2 | Days. |

# BoSoOsStatus (Enumeration)

Specifies the summary status of the sales opportunity.

| Member | Value | Description |
|---|---|---|
| sos_Open | 0 | The sales opportunity summary status is Open. |
| sos_Missed | 1 | The sales opportunity summary status is Lost. |
| sos_Sold | 2 | The sales opportunity summary status is Won. |

# BoSortTypeEnum (Enumeration)

Specifies sort types options.

| Member | Value | Description |
|---|---|---|
| rlstAlpha | 0 | Alphabetic sort type. |
| rlstNumeric | 1 | Numeric sort type. |
| rlstMoney | 2 | Money sort type. |
| rlstDate | 3 | Date sort type. |

# BoSoStatus (Enumeration)

Specifies the stage status of the sales opportunity.

| Member | Value | Description |
|---|---|---|
| so_Open | 0 | The sales opportunity stage status is Open. |
| so_Closed | 1 | The sales opportunity stage status is Closed. |

# BoStatus (Enumeration)

Document statuses.

| Member | Value | Description |
|---|---|---|
| bost_Open | 0 | Open |
| bost_Close | 1 | Closed |
| bost_Paid | 2 | Paid |
| bost_Delivered | 3 | Delivered |

# BoStckTrnDir (Enumeration)

Specifies the direction of moving items, related to the service call, to or from the technician.

| Member | Value | Description |
|---|---|---|
| bos_TransferToTechnician | 0 | Items are transferred from the stock to the technician. |
| bos_TransferFromTechnician | 1 | Items are returned from the technician to the stock. |

# BoSubFrequencyTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# BoSubPeriodTypeEnum (Enumeration)

Specifies the sub periods supported by the system.

| Member | Value | Description |
|---|---|---|
| spt_Year | 0 | Year sub period. |
| spt_Quarters | 1 | Quarter sub period. |
| spt_Months | 2 | Month sub period. |
| spt_Days | 3 | Day sub period. |

# BoSuppLangs (Enumeration)

Defines the current resource language. Note: The languages marked with * (asterisk) are country-specific only.

| Member | Value | Description |
|---|---|---|
| ln_Null | 0 |  |
| ln_Hebrew | 1 | Hebrew |
| ln_Spanish_Ar | 2 | Spanish (Argentina) * |
| ln_English | 3 | English (US) |
| ln_Polish | 5 | Polish * |
| ln_English_Sg | 6 | English (Singapore) * |
| ln_Spanish_Pa | 7 | Spanish (Panama) * |
| ln_English_Gb | 8 | English (Great Britain) |
| ln_German | 9 | German |
| ln_Serbian | 10 | Serbian * |
| ln_Danish | 11 | Danish |
| ln_Norwegian | 12 | Norwegian |
| ln_Italian | 13 | Italian |
| ln_Hungarian | 14 | Hungarian * |
| ln_Chinese | 15 | Chinese * |
| ln_Dutch | 16 | Dutch |
| ln_Finnish | 17 | Finnish |
| ln_Greek | 18 | Greek * |
| ln_Portuguese | 19 | Portuguese |
| ln_Swedish | 20 | Swedish |
| ln_English_Cy | 21 | English (Cyprus) * |
| ln_French | 22 | French |
| ln_Spanish | 23 | Spanish |
| ln_Russian | 24 | Russian * |
| ln_Spanish_La | 25 | Spanish (Latin America) |
| ln_Czech_Cz | 26 | Czech (Czech) * |
| ln_Slovak_Sk | 27 | Slovak (Slovakia) * |
| ln_Korean_Kr | 28 | Korean (Korea) * |
| ln_Portuguese_Br | 29 | Portuguese (Brazil) * |
| ln_Japanese_Jp | 30 | Japanese (Japan) * |
| ln_Turkish_Tr | 31 | Turkish (Turky) * |
| ln_Arabic | 32 |  |
| ln_Ukrainian | 33 |  |
| ln_TrdtnlChinese_Hk | 35 | Traditional Chinese (China) * |

# BoSvcCallPriorities (Enumeration)

Specifies the service call priority.

| Member | Value | Description |
|---|---|---|
| scp_Low | 0 | Low priority. |
| scp_Medium | 1 | Medium priority. |
| scp_High | 2 | High priority. |

# BoSvcContractStatus (Enumeration)

Specifies the service contract status.

| Member | Value | Description |
|---|---|---|
| scs_Approved | 0 | Approved - ready to provide service. |
| scs_Frozen | 1 | On hold (the contract is suspended). |
| scs_Draft | 2 | Draft - the contract is not approved yet. |
| scs_Terminated | 3 | The contract is terminated. |

# BoSvcEpxDocTypes (Enumeration)

Specifies the document type for Service Call Inventory Expenses.

| Member | Value | Description |
|---|---|---|
| edt_Invoice | 13 | Invoice document type. |
| edt_Delivery | 15 | Delivery document type. |
| edt_Return | 16 | Return document type. |
| edt_StockTransfer | 67 | Stock Transfer document type. |
| edt_CreditMemo | 14 | Credit memo document type. |
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

# BoSvcExpPartTypes (Enumeration)

Specifies the type of the replacing part used for closing the service call.

| Member | Value | Description |
|---|---|---|
| sep_Inventory | 0 | The replacing part is an Inventory type. |
| sep_NonInventory | 1 | The replacing part is a Non-inventory type. |

# BoTaxInvoiceTypes (Enumeration)

Specifies the tax invoice types. Country-specific for Poland.

| Member | Value | Description |
|---|---|---|
| botit_Invoice | 0 | Invoice document type. |
| botit_Payment | 1 | Payment document type. |
| botit_JournalEntry | 2 | Journal Entry document type. |
| botit_CorrectionInvoice | 3 |  |
| botit_DownPayment | 4 |  |
| botit_AlterationInvoice | 5 |  |
| botit_AlterationCorrectionInvoice | 6 |  |

# BoTaxPostAccEnum (Enumeration)

Specifies the tax posting account types for journal entry lines. Country-specific for Canada and USA.

| Member | Value | Description |
|---|---|---|
| tpa_Default | 0 | Default posting account. |
| tpa_SalesTaxAccount | 1 | Sales tax posing account. |
| tpa_PurchaseTaxAccount | 2 | Purchase tax posting account. |

# BoTaxPostingAccountTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| tpatEmpty | 0 |  |
| tpatSalesTaxAccount | 1 |  |
| tpatPurchasingTaxAccount | 2 |  |

# BoTaxRoundingRuleTypes (Enumeration)

Specifies the rounding rule types for tax amounts. This property is applicable for cluster B only (country-specific for Japan and Korea).

| Member | Value | Description |
|---|---|---|
| trr_RoundDown | 0 | Company Default. |
| trr_RoundUp | 1 | Rounding Up. |
| trr_RoundOff | 2 | Rounding Off. |
| trr_CompanyDefault | 3 | Rounding Down. |

# BoTaxTypes (Enumeration)

Defines the sales tax system for USA and Canada.

| Member | Value | Description |
|---|---|---|
| tt_Yes | 0 | Yes. |
| tt_No | 1 | No. |
| tt_UseTax | 2 | Use Tax. |
| tt_OffsetTax | 3 |  |

# BoTCDConditionEnum (Enumeration)

Specifies a condition based upon which the tax code is determined.

| Member | Value | Description |
|---|---|---|
| tcdcNone | 0 | None. |
| tcdcFederalTaxID | 1 | Federal Tax ID. |
| tcdcShipToAddress | 2 | Ship-to address. |
| tcdcShipToStreePOBox | 3 | Ship-to street or post office box. |
| tcdcShipToCity | 4 | Ship-to city. |
| tcdcShipToZipCode | 5 | Ship-to ZIP code. |
| tcdcShipToCounty | 6 | Ship-to county. |
| tcdcShipToState | 7 | Ship-to state. |
| tcdcShipToCountry | 8 | Ship-to country. |
| tcdcItem | 9 | Item. |
| tcdcItemGroup | 10 | Item group. |
| tcdcBusinessPartner | 11 | Business partner. |
| tcdcCustomerGroup | 12 | Customer group. |
| tcdcVendorGroup | 13 | Vendor group. |
| tcdcWarehouse | 14 | Warehouse. |
| tcdcGLAccount | 15 | G/L account. |
| tcdcCustomerEquTax | 16 | Customer equalization tax. |
| tcdcTaxStatus | 17 | Tax status. |
| tcdcFreight | 18 | Freight. |
| tcdcUDF | 19 | User-defined field. |
| tcdcBranchNumber | 20 |  |
| tcdcTypeOfBusiness | 21 |  |

# BoTCDDocumentTypeEnum (Enumeration)

Specifies for which type of document the tax code determination rule is relevant.

| Member | Value | Description |
|---|---|---|
| tcddtItem | 0 | Item type documents. |
| tcddtService | 1 | Service type documents. |
| tcddtItemAndService | 2 | Both item type and service type. |

# BoTimeTemplate (Enumeration)

Specify the Time temolate the system supports.

| Member | Value | Description |
|---|---|---|
| tt_24H | 0 | One 24 Houres scale. |
| tt_12H | 1 | Transuction rejected. |

# BoTransactionTypeEnum (Enumeration)

Transaction type by ststus.

| Member | Value | Description |
|---|---|---|
| botrntComplete | 0 | Transaction scceed |
| botrntReject | 1 | Transaction Rejected |

# BoUDOObjType (Enumeration)

Specifies the object types for user defined objects.

| Member | Value | Description |
|---|---|---|
| boud_MasterData | 1 | A Master Data type object refers to a collection of information about a person or an object, such as a cost object, business partner, or G/L account. For example, a business partner master record contains not only general information such as the business partner's name and address, but also specific information, such as payment terms and delivery instructions. Generally for end-users, master data is reference data that you will look up and use, but not create or change. |
| boud_Document | 3 | A Document type object refers to transactional data, which is data related to a single business event such as a purchase requisition or a request for payment. When you create a requisition, for example, SAP creates an electronic document for that particular transaction. SAP gives the transaction a document number and adds the document to the transaction data that is already in the system. Whenever you complete a transaction in SAP, that is, when you create, change, or print a document in SAP, this document number appears at the bottom of the screen. |

**Remarks:** For details, see User Defined Object documentation. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.

# BoUniqueSerialNumber (Enumeration)

Specifies serial number level

| Member | Value | Description |
|---|---|---|
| usn_None | 0 | No Serial Number. |
| usn_MfrSerialNumber | 1 | Manufactor Serial Number exists. |
| usn_SerialNumber | 2 | Serial Number exists. |
| usn_LotNumber | 3 | Lot Number exists. |

# BoUpdateAllocationEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| bouaManual | 0 |  |
| bouaCalculated | 1 |  |
| bouaRunCalculation | 2 |  |

# BoUPTOptions (Enumeration)

Specifies the permission options available for users.

| Member | Value | Description |
|---|---|---|
| bou_FullReadNone | 0 | Read/Write, Read Only, and no permission. |
| bou_FullNone | 1 | Read/Write and no permission. |

# BoUserGroup (Enumeration)

Specifies the user group statuses.

| Member | Value | Description |
|---|---|---|
| ug_Regular | 0 | Regular user group. |
| ug_Deleted | 1 | Deleted user group. |

# BoUTBTableType (Enumeration)

Specifies the table types for user defined tables.

| Member | Value | Description |
|---|---|---|
| bott_NoObject | 0 | (Default) A No Object type refers to a user table that cannot be linked to a user defined object. The default table includes Code and Name fields only. |
| bott_MasterData | 1 | A Master Data type table refers to a collection of information about a person or an object, such as a cost object, business partner, or G/L account. For example, a business partner master record contains not only general information such as the business partner's name and address, but also specific information, such as payment terms and delivery instructions. Generally for end-users, master data is reference data that you will look up and use, but not create or change. |
| bott_MasterDataLines | 2 | A Master Data Lines type refers as a child of Master Data type. For example, list of addresses related to a business partner. |
| bott_Document | 3 | A Document type table refers to transactional data, which is data related to a single business event such as a purchase requisition or a request for payment. When you create a requisition, for example, SAP creates an electronic document for that particular transaction. SAP gives the transaction a document number and adds the document to the transaction data that is already in the system. Whenever you complete a transaction in SAP, that is, when you create, change, or print a document in SAP, this document number appears at the bottom of the screen. |
| bott_DocumentLines | 4 | A Document Lines type refers as a child of Document type. For example, Content tab in Invoice document. |
| bott_NoObjectAutoIncrement | 5 |  |

**Remarks:** For each user table type, SAP Business One provides a default table. You can add user fields to the default user fields but not remove them. For the default fields provided for each table type, see User Defined Object documentation. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.

# BoVatCategoryEnum (Enumeration)

Specifies the tax group categories.

| Member | Value | Description |
|---|---|---|
| bovcInputTax | 1 | The tax group applies purchase documents. |

# BoVatStatus (Enumeration)

Defines the possible values for tax status.

| Member | Value | Description |
|---|---|---|
| vExempted | 0 | The transaction with this business partner is tax free. |
| vLiable | 1 | Transactions with this business partner are liable to tax. |
| vEC | 2 | Sets transactions with this customer to exempted. |

# BoVerticalAlignmentEnum (Enumeration)

Defines the possible values for Report Layout Vertical alignments.

| Member | Value | Description |
|---|---|---|
| rlvaTop | 0 | Defines the value for Report Layout TOP alignment. |
| rlvaBottom | 1 | Defines the value for Report Layout Bottom alignment. |
| rlvaCentralized | 2 | Defines the value for Report Layout Centralized alignment. |

# BoWeekEnum (Enumeration)

Days in a week.

| Member | Value | Description |
|---|---|---|
| Sunday | 1 | Sunday |
| Monday | 2 | Monday |
| Tuesday | 3 | Tuesday |
| Wednesday | 4 | Wednesday |
| Thursday | 5 | Thursday |
| Friday | 6 | Friday |
| Saturday | 7 | Saturday |

# BoWeekNoRuleEnum (Enumeration)

The rule of calculating week numbers.

| Member | Value | Description |
|---|---|---|
| fromJanFirst | 0 | First week starts on January 1. |
| fromFirstFourDayWeek | 1 | First week starts in first 4-day week. |
| fromFirstFullWeek | 2 | First week starts in first full week. |

# BoWfTransOpt (Enumeration)

Specifies the options for a database transaction.

| Member | Value | Description |
|---|---|---|
| wf_RollBack | 1 | Rolls back the transaction so that the data is discarded. |
| wf_Commit | 0 | Commits the transaction so that the data is saved. |

# BoWorkOrderStat (Enumeration)

Specifies the work order status.

| Member | Value | Description |
|---|---|---|
| wk_WorkOrder | 0 | The work order is open. |
| wk_WorkInstruction | 1 | Production Instruction stage. |
| wk_ProductComplete | 2 | The production is completed. |

# BoXmlExportTypes (Enumeration)

Defines the type for exporting an object to XML.

| Member | Value | Description |
|---|---|---|
| xet_AllNodes | 0 | Export to XML all fields (both read only and read/write fields) from the database. (XML files exported using this type cannot be read by the ReadXml method.) |
| xet_ValidNodesOnly | 1 | Export to XML only valid fields that support XML import (read/write fields only) from the database. (XML files exported using this type cannot be read by the ReadXml method.) |
| xet_NodesAsProperties | 2 | Export to XML all fields as properties from the database. (XML files exported using this type cannot be read by the ReadXml method.) |
| xet_ExportImportMode | 3 | Export to XML only valid fields that support XML import and export (read/write fields only that do not contain null values) from the database. (XML files exported using this type can be read by the ReadXml method.) |

# BoYesNoEnum (Enumeration)

Boolean values, for providing a value for a variety of properties.

| Member | Value | Description |
|---|---|---|
| tNO | 0 | Sets the answer to negative. |
| tYES | 1 | Sets the answer to positive. |

# BoYesNoNoneEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| boNO | 0 |  |
| boYES | 1 |  |
| boNONE | 2 |  |

# BPVatExemptionsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| bpvesBPVatExemptions | 0 |  |
| bpvesBPVatExemptionsParamsCollection | 1 |  |
| bpvesBPVatExemptionsParams | 2 |  |

# BranchesServiceDataInterfaces (Enumeration)

BranchesService data interfaces.

| Member | Value | Description |
|---|---|---|
| bsBranch | 0 | Branch data interface |
| bsBranchesParams | 1 | BranchesParams data interface |
| bsBranchParams | 2 | BranchParams data interface |

# BrazilBeverageIndexersServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| bbisBrazilBeverageIndexer | 0 |  |
| bbisBrazilBeverageIndexersParams | 1 |  |
| bbisBrazilBeverageIndexerParams | 2 |  |

# BrazilFuelIndexersServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| bfisBrazilFuelIndexer | 0 |  |
| bfisBrazilFuelIndexersParams | 1 |  |
| bfisBrazilFuelIndexerParams | 2 |  |

# BrazilIndexerTypes (Enumeration)

| Member | Value | Description |
|---|---|---|
| bitUnknown | 0 |  |
| bitNumeric | 1 |  |
| bitString | 2 |  |
| bitMulti | 3 |  |

# BrazilMultiIndexersServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| bmisBrazilMultiIndexer | 0 |  |
| bmisBrazilMultiIndexersParams | 1 |  |
| bmisBrazilMultiIndexerParams | 2 |  |

# BrazilMultiIndexerTypes (Enumeration)

| Member | Value | Description |
|---|---|---|
| bmitInvalid | 0 |  |
| bmitIncomeNature | 1 |  |

# BrazilNumericIndexersServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| bnisBrazilNumericIndexer | 0 |  |
| bnisBrazilNumericIndexersParams | 1 |  |
| bnisBrazilNumericIndexerParams | 2 |  |

# BrazilNumericIndexerTypes (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# BrazilStringIndexersServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| bsisBrazilStringIndexer | 0 |  |
| bsisBrazilStringIndexersParams | 1 |  |
| bsisBrazilStringIndexerParams | 2 |  |

# BrazilStringIndexerTypes (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# BusinessPartnerPropertiesServiceDataInterfaces (Enumeration)

BusinessPartnerPropertiesService data interfaces.

| Member | Value | Description |
|---|---|---|
| bppsBusinessPartnerProperty | 0 | BusinessPartnerProperty data interface |
| bppsBusinessPartnerPropertiesParams | 1 | BusinessPartnerPropertiesParams data interface |
| bppsBusinessPartnerPropertyParams | 2 | BusinessPartnerPropertyParams data interface |

# BusinessPartnersServiceDataInterfaces (Enumeration)

BusinessPartnersService data interfaces.

| Member | Value | Description |
|---|---|---|
| bpsdiOpenningBalanceAccount | 0 | OpenningBalanceAccount data interface |
| bpsdiBPCodes | 1 | BPCodes data interface |

# CalculateInterestMethodEnum (Enumeration)

Indicates whether to calculate interest for dunning letters based on the remaining amount or on the original total.

| Member | Value | Description |
|---|---|---|
| cimOnRemainingAmount | 0 | Calculate interest based on the remaining amount. |
| cimOnOriginalSum | 1 | Calculate interest based on the original total. |

# CalculationBaseEnum (Enumeration)

The base with which you want to calculate the depreciation of assets.

| Member | Value | Description |
|---|---|---|
| cbYearly | 0 | Calculates the depreciation of the year first, and then uses the yearly depreciation as the base to calculate the depreciation of each period. |
| cbMonthly | 1 | Calculates the depreciation of the month first, and then uses the monthly depreciation as the base to calculate the depreciation of each period. |

# CallMessageStatusEnum (Enumeration)

Statuses of call messages.

| Member | Value | Description |
|---|---|---|
| cmsUnread | 0 | The message is not read. |
| cmsRead | 1 | The message is read. |

# CallMessageTypeEnum (Enumeration)

Types of call messages.

| Member | Value | Description |
|---|---|---|
| cmtInformation | 0 | Information message type. |
| cmtWarning | 1 | Warning message type. |
| cmtError | 2 | Error message type. |

# CampaignAssignToEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| catUser | 0 |  |
| catEmployee | 1 |  |

# CampaignItemTypeEnum (Enumeration)

The campaign item types.

| Member | Value | Description |
|---|---|---|
| citItems | 0 | Physical items. |
| citLabel | 1 | Labor per item type. |
| citTravel | 2 | Travel per item type. |

# CampaignResponseTypeServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| crtsCampaignResponseType | 0 |  |
| crtsCampaignResponseTypeParamsCollection | 1 |  |
| crtsCampaignResponseTypeParams | 2 |  |

# CampaignsServiceDataInterfaces (Enumeration)

CampaignsService data interfaces.

| Member | Value | Description |
|---|---|---|
| csCampaign | 0 | Campaign data interface |
| csCampaignsParams | 1 | CampaignsParams data interface |
| csCampaignParams | 2 | CampaignPartners data interface |

# CampaignStatusEnum (Enumeration)

Status of this campaign.

| Member | Value | Description |
|---|---|---|
| csOpen | 0 | Open Default status. |
| csFinished | 1 | Finished |
| csCanceled | 2 | Cancelled |

# CampaignTypeEnum (Enumeration)

The type of the campaign.

| Member | Value | Description |
|---|---|---|
| ctEmail | 0 | E-Mail The default type. |
| ctMail | 1 | Mail |
| ctFax | 2 | Fax |
| ctPhoneCall | 3 | Phone call |
| ctMeeting | 4 | Meeting |
| ctSMS | 5 | Short message |
| ctWeb | 6 | Web |
| ctOthers | 7 | Others |

# CancelStatusEnum (Enumeration)

The document cancel status.

| Member | Value | Description |
|---|---|---|
| csYes | 0 | The document is cancelled. |
| csNo | 1 | The document is not cancelled. |
| csCancellation | 2 | The document is a cancellation document. |

# CardOrAccountEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| coaCard | 0 |  |
| coaAccount | 1 |  |

# CashDiscountsServiceDataInterfaces (Enumeration)

CashDiscountsService data interfaces.

| Member | Value | Description |
|---|---|---|
| cdsCashDiscount | 0 | CashDiscount Object data interface |
| cdsCashDiscountsParams | 1 | CashDiscountsParams data interface |
| cdsCashDiscountParams | 2 | CashDiscountParams data interface |

# CashFlowLineItemsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| cflisCashFlowLineItem | 0 |  |
| cflisCashFlowLineItemsParams | 1 |  |
| cflisCashFlowLineItemParams | 2 |  |

# CertificateSeriesServiceDataInterfaces (Enumeration)

CertificateSeriesService data interfaces.

| Member | Value | Description |
|---|---|---|
| cssCertificateSeries | 0 | CertificateSeries data interface |
| cssCertificateSeriesParamsCollection | 1 | CertificateSeriesParamsCollection data interface |
| cssCertificateSeriesParams | 2 | CertificateSeriesParams data interface |

# CESTCodeServiceDataInterfaces (Enumeration)

CESTCodeService data interfaces.

| Member | Value | Description |
|---|---|---|
| cestcsCESTCodeData | 0 | CESTCodeData data interface |
| cestcsCESTCodeParams | 1 | CESTCodeParams data interface |

# ChangeLogsServiceDataInterfaces (Enumeration)

ChangeLogsService data interfaces.

| Member | Value | Description |
|---|---|---|
| clsGetChangeLogParams | 0 | GetChangeLogParams data interface |
| clsShowDifferenceParams | 1 | ShowDifferenceParams data interface |

# CheckLinesServiceDataInterfaces (Enumeration)

CheckLinesService data interfaces.

| Member | Value | Description |
|---|---|---|
| clsCheckLinesParams | 0 | CheckLinesParams data interface |
| clsCheckLineParams | 1 | CheckLineParams data interface |

# ClosingOptionEnum (Enumeration)

Specify a posting date to be used in the clearing journal entry.

| Member | Value | Description |
|---|---|---|
| coByCurrentSystemDate | 1 | Use the current system date. |
| coByOriginalDocumentDate | 2 | Use the original posting date in the document. |
| coBySpecifiedDate | 3 | Use a specified date other than the above two dates. |

# CockpitsServiceDataInterfaces (Enumeration)

CockpitsService data interfaces.

| Member | Value | Description |
|---|---|---|
| csCockpit | 0 | Cockpit data interface |
| csCockpitsParams | 1 | CockpitsParams data interface |
| csCockpitParams | 2 | CockpitParams data interface |

# CommissionTradeTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ct_Empty | 0 |  |
| ct_SalesAgent | 1 |  |
| ct_PurchaseAgent | 2 |  |
| ct_Consignor | 3 |  |

# CompanyServiceDataInterfaces (Enumeration)

CompanyService data interfaces.

| Member | Value | Description |
|---|---|---|
| csdiCompanyInfo | 0 | Company data interface |
| csdiAdminInfo | 1 | AdminInfo data interface |
| csdiPeriodCategory | 2 | PeriodCategory data interface |
| csdiPeriodCategoryParams | 3 | PeriodCategoryParams data interface |
| csdiFinancePeriod | 4 | FinancePeriod data interface |
| csdiFinancePeriods | 5 | FinancePeriods data interface |
| csdiFinancePeriodParams | 6 | FinancePeriodParams data interface |
| csdiBlob | 7 | Blob data interface |
| csdiBlobParams | 8 | BlobParams data interface |
| csdiPathAdmin | 9 | PathAdmin data interface |
| csdiUserLicenseParams | 10 | UserLicenseParams data interface |
| csdiDecimalData | 11 |  |
| csdiItemPriceParams | 12 |  |
| csdiItemPriceReturnParams | 13 |  |
| csdiAdvancedGLAccountParams | 14 |  |
| csdiAdvancedGLAccountReturnParams | 15 |  |

# ContractSequenceEnum (Enumeration)

The contract sequence.

| Member | Value | Description |
|---|---|---|
| cs_Monthly | 0 | Monthly. |
| cs_Quarterly | 1 | Quarterly. |
| cs_SemiAnnually | 2 | Semi-annually. |
| cs_Yearly | 3 | Yearly. |

# CostCenterTypesServiceDataInterfaces (Enumeration)

CostCenterTypesService data interfaces.

| Member | Value | Description |
|---|---|---|
| cctsCostCenterType | 0 | CostCenterType data interface |
| cctsCostCenterTypesParams | 1 | CostCenterTypesParams data interface |
| cctsCostCenterTypeParams | 2 | CostCenterTypeParams data interface |

# CostElementServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| cesCostElement | 0 |  |
| cesCostElementsParams | 1 |  |
| cesCostElementParams | 2 |  |

# CounterTypeEnum (Enumeration)

The inventory counter type.

| Member | Value | Description |
|---|---|---|
| ctUser | 0 | The counter is a user of the SAP Business One application. |
| ctEmployee | 1 | The counter is an employee of the company, but is not an SAP Business One user. If a counter does not have an SAP Business One user account and you want to maintain his or her information in the counting documents, you must maintain this counter's employment information in the system. |

# CountingDocumentStatusEnum (Enumeration)

The status of the inventory counting document.

| Member | Value | Description |
|---|---|---|
| cdsOpen | 0 | Open Default status. |
| cdsClosed | 1 | Closed |

# CountingLineStatusEnum (Enumeration)

The status of the counting line.

| Member | Value | Description |
|---|---|---|
| clsOpen | 0 | Open |
| clsClosed | 1 | Closed |

# CountingTypeEnum (Enumeration)

The counting type.

| Member | Value | Description |
|---|---|---|
| ctSingleCounter | 0 | There is one inventory counter who counts item quantities in warehouses. |
| ctMultipleCounters | 1 | There are multiple inventory counters who count item quantities in the same warehouses. |

# CountriesServiceDataInterfaces (Enumeration)

CountriesService data interfaces.

| Member | Value | Description |
|---|---|---|
| csCountry | 0 | Country data interface |
| csCountriesParams | 1 | CountriesParams data interface |
| csCountryParams | 2 | CountryParams data interface |

# CreateMethodEnum (Enumeration)

Methods for creating statements.

| Member | Value | Description |
|---|---|---|
| cmManual | 0 | The system creates the bank statement manualy. |
| cmAutomatic | 1 | The system creates the bank statement automaticaly. |

# CreditLinesServiceDataInterfaces (Enumeration)

CreditLinesService data interfaces.

| Member | Value | Description |
|---|---|---|
| clsCreditLinesParams | 0 | CreditLinesParams data interface |
| clsCreditLineParams | 1 | CreditLineParams data interface |

# CreditOrDebitEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| codCredit | 0 |  |
| codDebit | 1 |  |

# CurrenciesDecimalsEnum (Enumeration)

Rounding methods for currencies.

| Member | Value | Description |
|---|---|---|
| cdDefault | 0 | Specifies rounding as defined in Administration > General Settings > Display tab. |
| cdWithoutDecimals | 1 | Specifies no decimal display. |
| cd1Digit | 2 | Specifies rounding to 1 decimal digit. |
| cd2Digits | 3 | Specifies rounding to 2 decimal digits. |
| cd3Digits | 4 | Specifies rounding to 3 decimal digits. |
| cd4Digits | 5 | Specifies rounding to 4 decimal digits. |
| cd5Digits | 6 | Specifies rounding to 5 decimal digits. |
| cd6Digits | 7 | Specifies rounding to 6 decimal digits. |

# CustomsDeclarationServiceDataInterfaces (Enumeration)

CustomsDeclarationService data interfaces.

| Member | Value | Description |
|---|---|---|
| cdsCustomsDeclaration | 0 | CustomsDeclaration data interface |
| cdsCustomsDeclarationParams | 1 | CustomsDeclarationParams data interface |

# CycleCountDeterminationCycleByEnum (Enumeration)

Specifies the warehouse sublevel or item group for cycle counting.

| Member | Value | Description |
|---|---|---|
| ccdcbItemGroup | 0 | Sets the cycle counting by item group. |
| ccdcbWarehouseSublevel1 | 1 | Sets the cycle counting by WarehouseSublevel1. |
| ccdcbWarehouseSublevel2 | 2 | Sets the cycle counting by WarehouseSublevel2. |
| ccdcbWarehouseSublevel3 | 3 | Sets the cycle counting by WarehouseSublevel3. |
| ccdcbWarehouseSublevel4 | 4 | Sets the cycle counting by WarehouseSublevel4. |

# CycleCountDeterminationsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ccdsCycleCountDetermination | 0 | CycleCountDeterminationParams data interface |
| ccdsCycleCountDeterminationParamsCollection | 1 | CycleCountDeterminationParams data interface |
| ccdsCycleCountDeterminationParams | 2 | CycleCountDeterminationParamsCollection data interface |

# DashboardPackagesServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| dpsDashboardPackagesParams | 0 |  |
| dpsDashboardPackageParams | 1 |  |
| dpsDashboardPackageImportParams | 2 |  |

# DataSensitiveStatusEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| dss_FieldNotSentive | 0 |  |
| dss_DataSubjectNotNaturalPerson | 1 |  |
| dss_DataSubjectIsBlockedOrErased | 2 |  |
| dss_DataIsSensitive | 3 |  |
| dss_Error | 4 |  |
| dss_TransactionIsErased | 5 |  |

# DeductionTaxSubGroupsServiceDataInterfaces (Enumeration)

DeductionTaxSubGroupsService data interfaces.

| Member | Value | Description |
|---|---|---|
| dtsgsDeductionTaxSubGroup | 0 | DeductionTaxSubGroup data interface |
| dtsgsDeductionTaxSubGroupsParams | 1 | DeductionTaxSubGroupsParams data interface |
| dtsgsDeductionTaxSubGroupParams | 2 | DeductionTaxSubGroupParams data interface |

# DefaultElementsforCRServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| pdsDefaultElementsforCR | 0 | DefaultElementsforCR data interface. |
| pdsDefaultElementsforCRParams | 1 | DefaultElementsforCRParams data interface. |

# DepartmentsServiceDataInterfaces (Enumeration)

DepartmentsService data interfaces.

| Member | Value | Description |
|---|---|---|
| dsDepartment | 0 | Department data interface |
| dsDepartmentsParams | 1 | DepartmentsParams data interface |
| dsDepartmentParams | 2 | DepartmentParams data interface |

# DepositsServiceDataInterfaces (Enumeration)

DepositsService data interfaces.

| Member | Value | Description |
|---|---|---|
| dsDeposit | 0 | Deposit data interface |
| dsDepositsParams | 1 | DepositsParams data interface |
| dsDepositParams | 2 | DepositParams data interface |
| dsCancelCheckRowParams | 3 |  |

# DepreciationAreasServiceDataInterfaces (Enumeration)

DepreciationAreasService data interfaces.

| Member | Value | Description |
|---|---|---|
| dasDepreciationArea | 0 | DepreciationArea data interface |
| dasDepreciationAreaParamsCollection | 1 | DepreciationAreaParamsCollection data interface |
| dasDepreciationAreaParams | 2 | DepreciationAreaParams data interface |

# DepreciationCalculationBaseEnum (Enumeration)

The base for the depreciation calculation in each phase of an asset's useful life.

| Member | Value | Description |
|---|---|---|
| dcbAcquisitionValue | 0 | The annual depreciation in each phase is calculated using the following formula: (Acquisition Value – Salvage Value) * Annual Percentage |
| dcbNetBookValue | 1 | The annual depreciation in each phase is calculated using the following formula: (Net Book Value – Salvage Value) * Annual Percentage |

# DepreciationMethodEnum (Enumeration)

The depreciation method of the asset.

| Member | Value | Description |
|---|---|---|
| dmNoDepreciation | 0 | No depreciation is carried out |
| dmStraightLine | 1 | A method of distributing an asset's value evenly across its useful life. That is, the asset is depreciated by the same amount in each period. |
| dmStraightLinePeriodControl | 2 | A method that entails defining different factors used in depreciation calculation for different periods of an asset's useful life. |
| dmDecliningBalance | 3 | A method that entails applying a depreciation rate against the non-depreciated balance of an asset. Instead of spreading the cost of the asset evenly over its useful life, the method depreciates the asset at a constant rate, which results in declining depreciation charges each successive period. |
| dmMultilevel | 4 | A method of applying different depreciation rates to an asset for different stages of an asset's useful life. |
| dmImmediateWriteOff | 5 | A method generally applied to low-value assets whose full value can be depreciated in the acquisition year. |
| dmSpecialDepreciation | 6 | A method of carrying out automatic special depreciation. |
| dmManualDepreciation | 7 | A method of carrying out manual special depreciation. |
| dmAccelerated | 8 | A method of carrying out accelerated depreciation. |

# DepreciationRoundingMethodEnum (Enumeration)

The rounding method of Round Year End Book Value.

| Member | Value | Description |
|---|---|---|
| drmTruncate | 0 | Truncate to Integer. |
| drmRoundUp | 1 | Round Up to Integer. |
| drmRoundDown | 2 | Round Down to Integer. |

# DepreciationTypePoolsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| dtpsDepreciationTypePool | 0 |  |
| dtpsDepreciationTypePoolParamsCollection | 1 |  |
| dtpsDepreciationTypePoolParams | 2 |  |

# DepreciationTypesServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| dtsDepreciationType | 0 |  |
| dtsDepreciationTypeParamsCollection | 1 |  |
| dtsDepreciationTypeParams | 2 |  |

# DeterminationCriteriasServiceDataInterfaces (Enumeration)

DeterminationCriteriasService data interfaces.

| Member | Value | Description |
|---|---|---|
| dcsDeterminationCriteria | 0 | DeterminationCriteria data interface |
| dcsDeterminationCriteriaParamsCollection | 1 | DeterminationCriteriaParamsCollection data interface |
| dcsDeterminationCriteriaParams | 2 | DeterminationCriteriaParams data interface |

# DimensionsServiceDataInterfaces (Enumeration)

DimensionsService data interfaces.

| Member | Value | Description |
|---|---|---|
| dsDimension | 0 | Dimension data interface |
| dsDimensionsParams | 1 | DimensionsParams data interface |
| dsDimensionParams | 2 | DimensionParams data interface |

# DirectDebitTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ddtCORE | 0 |  |
| ddtB2B | 1 |  |
| ddtCOR1 | 2 |  |

# DiscountGroupBaseObjectEnum (Enumeration)

Types of discount groups.

| Member | Value | Description |
|---|---|---|
| dgboNone | 0 | No discounts |
| dgboItemGroups | 1 | Discounts based on item groups |
| dgboItemProperties | 2 | Discounts based on item properties |
| dgboManufacturer | 3 | Discounts based on manufacturers |
| dgboItems | 4 |  |

# DiscountGroupDiscountTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| dgdt_Fixed | 0 |  |
| dgdt_Variable | 1 |  |

# DiscountGroupRelationsEnum (Enumeration)

Methods for calculating discounts if more than one discount applies to an item.

| Member | Value | Description |
|---|---|---|
| dgrLowestDiscount | 0 | Applies the lowest discount |
| dgrHighestDiscount | 1 | Applies the highest discount |
| dgrAverageDiscount | 2 | Applies an average of the discounts |
| dgrDiscountTotals | 3 | Applies the sum of all discounts (up to 100 percent) |
| dgrMultipliedDiscount | 4 |  |

# DiscountGroupTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| dgt_AllBPs | 0 |  |
| dgt_CustomerGroup | 1 |  |
| dgt_VendorGroup | 2 |  |
| dgt_SpecificBP | 3 |  |

# DisplayBatchQtyUoMByEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| dispBatchQtyByDocRowUoM | 0 |  |
| dispBatchQtyByInventoryUoM | 1 |  |

# DistributionRulesServiceDataInterfaces (Enumeration)

DistributionRulesService data interfaces.

| Member | Value | Description |
|---|---|---|
| drsDistributionRule | 0 | DistributionRule data interface |
| drsDistributionRulesParams | 1 | DistributionRulesParams data interface |
| drsDistributionRuleParams | 2 | DistributionRuleParams data interface |

# DNFCodeSetupServiceDataInterfaces (Enumeration)

NCMCodesSetupService data interfaces.

| Member | Value | Description |
|---|---|---|
| dnfcssDNFCodeSetup | 0 | DNFCodeSetup data interface |
| dnfcssDNFCodeSetupParamsCollection | 1 | DNFCodeSetupParamsCollection data interface |
| dnfcssDNFCodeSetupParams | 2 | DNFCodeSetupParams data interface |

# DocumentAuthorizationStatusEnum (Enumeration)

Status of the document and authorization.

| Member | Value | Description |
|---|---|---|
| dasWithout | 0 | Without a status. |
| dasPending | 1 | The status of a transaction awaiting approval. |
| dasApproved | 2 | The status of a transaction that has been approved, but not yet converted from a draft to a regular document. |
| dasRejected | 3 | The status of a transaction that was not approved and remains a draft. The authorizer can grant approval for a rejected transaction by changing the status accordingly. |
| dasGenerated | 4 | The status of a transaction that has been approved and converted from a draft to a regular document by the originator. |
| dasGeneratedbyAuthorizer | 5 | The status of a transaction that has been approved and converted from a draft to a regular document by the authorizer. |
| dasCancelled | 6 | An approval procedure can be cancelled and restarted as necessary. If the approval procedure is cancelled, the draft document cannot be converted to a regular document. |

# DocumentDeliveryTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ddtNoneSelected | 0 |  |
| ddtCreateOnlineDocument | 1 |  |
| ddtPostToAribaNetwork | 2 |  |

# DocumentObjectTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| dc_ArInvoice | 13 |  |
| dc_Delivery | 15 |  |
| dc_GoodsReturn | 21 |  |
| dc_InventoryTransfer | 67 |  |

# DocumentRemarksIncludeTypeEnum (Enumeration)

Determines the Remarks field when you copy a base marketing document to a target document.

| Member | Value | Description |
|---|---|---|
| driBaseDocumentNumber | 0 | Base document number: When you copy a base marketing document to a target document, the base document number is copied as well and is included in the Remarks field. |
| driBPReferenceNumber | 1 | BP reference number: When you copy a base marketing document to a target document, the customer or vendor reference number is copied as well and is included in the Remarks field. If the customer or vendor reference number doesn’t exist, the Remarks field remains unchanged. |
| driManualRemarksOnly | 2 | Manual remarks only: When you copy a base marketing document to a target document, the target Remarks field only includes the manual remarks from the base document. |

# DomesticBankAccountValidationEnum (Enumeration)

Validation algorithms for bank accounts.

| Member | Value | Description |
|---|---|---|
| dbavNone | 0 | No validation. |
| dbavBelgium | 1 | Belgium validation. |
| dbavSpain | 2 | Spain validation. |
| dbavFrance | 3 | France validation. |
| dbavItaly | 4 | Italy validation. |
| dbavNetherlands | 5 | Netherlands validation. |
| dbavPortugal | 6 | Portugal validation. |

# DownPaymentTypeEnum (Enumeration)

Down payment document types.

| Member | Value | Description |
|---|---|---|
| dptRequest | 0 | Type is Down Payment Request. |
| dptInvoice | 1 | Type is Down Payment Invoice. |

**Remarks:** Relevant for Czech, Slovak, Hungary, and Poland only. © Copyright 2022 SAP SE or an SAP affiliate company. All rights reserved.

# DrawingMethodEnum (Enumeration)

Methods of calculating freight per row in a document. The calculation method is relevant when you copy rows from a base document to a target document.

| Member | Value | Description |
|---|---|---|
| dmNone | 0 | No freight is copied. |
| dmQuantity | 1 | The amount is divided by the item quantity and each unit is charged the same amount of freight. |
| dmTotal | 2 | SAP Business One calculates the portion of the document total or row total is copied to the target document, and then adds the relative amount of the document or row freight to the target document. |
| dmAll | 3 | All freight is copied. |

# DueDateTypesEnum (Enumeration)

Methods for calculating the due date.

| Member | Value | Description |
|---|---|---|
| ddtByDates | 0 | Due Date Types By Dates. |
| ddtAfterTimePeriod | 1 | Due Date Types After Time period. |

# DunningLetterTypeEnum (Enumeration)

Dunning letter types

| Member | Value | Description |
|---|---|---|
| dltDunningLetter1 | 0 | Letter 1 |
| dltDunningLetter2 | 1 | Letter 2 |
| dltDunningLetter3 | 2 | Letter 3 |
| dltDunningLetter4 | 3 | Letter 4 |
| dltDunningLetter5 | 4 | Letter 5 |
| dltDunningLetter6 | 5 | Letter 6 |
| dltDunningLetter7 | 6 | Letter 7 |
| dltDunningLetter8 | 7 | Letter 8 |
| dltDunningLetter9 | 8 | Letter 9 |
| dltDunningLetter10 | 9 | Letter 10 |
| dltDunningALL | 10 | Indicates all dunning letters |

# DunningTermsServiceDataInterfaces (Enumeration)

DunningTermsService data interfaces.

| Member | Value | Description |
|---|---|---|
| dtsDunningTerm | 0 | DunningTerm data interface |
| dtsDunningTermLines | 1 | DunningTermLines data interface |
| dtsDunningTermLine | 2 | DunningTermLine data interface |
| dtsDunningTermsParams | 3 | DunningTermsParams data interface |
| dtsDunningTermParams | 4 | DunningTermsParams data interface |

# EBooksServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ebkEBooks | 0 |  |
| ebkEBooksParamsCollection | 1 |  |
| ebkEBooksParams | 2 |  |

# ECDPostingTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ecdNormal | 0 |  |
| ecdStatement | 1 |  |

# EcmActionGenerationTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| lgtNotRelevant | 1 |  |
| lgtGenerateLater | 2 |  |
| lgtGenerate | 3 |  |

# EcmActionLogTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| altSend | 1 |  |
| altReceive | 2 |  |
| altImport | 3 |  |
| altNote | 4 |  |
| altWarning | 5 |  |
| altError | 6 |  |

# EcmActionPeriodTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| aptIgnore | 0 |  |
| aptYear | 1 |  |
| aptQuarter | 2 |  |
| aptMonth | 3 |  |
| aptDateRange | 4 |  |

# EcmActionStatusEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# EcmActionTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# EDocGenerationTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| edocGenerate | 0 |  |
| edocGenerateLater | 1 |  |
| edocNotRelevant | 2 |  |

# EDocStatusEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| edoc_New | 0 |  |
| edoc_Pending | 1 |  |
| edoc_Sent | 2 |  |
| edoc_Error | 3 |  |
| edoc_Ok | 4 |  |

# EDocTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| edocFE | 0 |  |
| edocFCE | 1 |  |

# EffectivePriceEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| epDefaultPriority | 0 |  |
| epLowestPrice | 1 |  |
| epHighestPrice | 2 |  |

# ElecCommStatusEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ecsApproved | 0 |  |
| ecsPendingApproval | 1 |  |
| ecsRejected | 2 |  |

# ElectronicCommunicationActionServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ecasECMCodeParamsCollection | 0 |  |
| ecasECMCodeParams | 1 |  |
| ecasECMActionStatusData | 2 |  |

# ElectronicCommunicationActionsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ecasEcmAction | 0 |  |
| ecasEcmActionParams | 1 |  |
| ecasEcmActionDocParams | 2 |  |
| ecasEcmActionLog | 3 |  |
| ecasEcmActionLogCollection | 4 |  |
| ecasEcmActionLogParams | 5 |  |

# ElectronicDocGenTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| edgt_NotRelevant | 0 |  |
| edgt_Generate | 1 |  |
| edgt_GenerateLater | 2 |  |

# ElectronicDocProcessingTargetEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# ElectronicDocProtocolCodeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# ElectronicDocProtocolCodeStrEnum (Enumeration)

Protocols for electronic documents. Source table: OECM.

| Member | Value | Description |
|---|---|---|
| edpcs_Invalid | 0 | Invalid protocol |
| edpcs_GEN | 1 | General protocol |
| edpcs_EET | 2 | EET protocol (CZ) |
| edpcs_CFDI | 3 | CFDI protocol (MX) |
| edpcs_FPA | 4 | FPA protocol (IT) |
| edpcs_MTD | 5 | MTD protocol (UK) |
| edpcs_EWB | 6 | E-Way Bill protocol (IN) |
| edpcs_PEPPOL | 7 | PEPPOL protocol |
| edpcs_HOI | 8 | On-line-invoicing protocol (HU) |
| edpcs_MYF | 9 | MYF protocol (GR) |
| edpcs_EIS | 10 | EIS protocol (ES) |
| edpcs_IIS | 11 | IIS protocol (ES) |
| edpcs_IIS_Annual | 12 | IIS annual protocol (ES) |
| edpcs_DIGIPOORT | 13 | DIGIPOORT protocol (NL) |
| edpcs_EBook | 14 | E-Books protocol (GR) |
| edpcs_DOX | 15 |  |
| edpcs_RTIE | 16 |  |
| edpcs_EBilling | 17 |  |

# ElectronicDocumentBlobContentTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| edbctDefault | -1 |  |
| edbctXML | 0 |  |
| edbctZippedXML | 1 |  |
| edbctJSON | 2 |  |
| edbctZippedJSON | 3 |  |
| edgctText | 4 |  |

# ElectronicDocumentEntryCancellationStatusEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| edecsInvalid | 0 |  |
| edecsNotSet | 1 |  |
| edecsNewRequest | 2 |  |
| edecsRequestSent | 3 |  |
| edescApproved | 4 |  |
| edescRejected | 5 |  |
| edescError | 6 |  |
| edescCancelled | 7 |  |
| edescInProcess | 8 |  |
| edescSentToAuthority | 9 |  |

# ElectronicDocumentEntryLogTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| edeltNone | 0 |  |
| edeltSend | 1 |  |
| edeltReceive | 2 |  |
| edeltImport | 3 |  |
| edeltNote | 4 |  |
| edeltWarning | 5 |  |
| edeltError | 6 |  |
| edeltWSData | 7 |  |

# ElectronicDocumentEntryPeriodTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| edeptIgnore | 0 |  |
| edeptYear | 1 |  |
| edeptQuarter | 2 |  |
| edeptMonth | 3 |  |
| edeptDateRange | 4 |  |

# ElectronicDocumentEntryStatusEnum (Enumeration)

Status of electronic document. Source table: ECM2.

| Member | Value | Description |
|---|---|---|
| edesNone | 0 | Invalid status |
| edesNew | 1 | New document |
| edesReadyToProcess | 2 | Document is ready for processing |
| edesPending | 3 | Document is being prepared for processing |
| edesError | 4 | Document processing error |
| edesOK | 5 | Document was accepted by authority |
| edesSent | 6 | Document has been sent to external authority |
| edesDocError | 7 | Sent document contains syntactic or semantic errors |
| edesTempError | 8 | Communication-releated error |
| edesWarning | 9 | Document processing warning |
| edesWaiting | 10 | Document is waiting for user action |
| edesAuthorized | 11 | Document has been accepted by authority |
| edesInProcess | 12 | Document is being processed |
| edesRejected | 13 | Document can be re-sent again |
| edesDenied | 14 | Document can't be re-sent again |
| edesCanceled | 15 | Document has been canceled |
| edesAborted | 16 | User changed electronic document type to 'not relevant' |
| edesUnused | 17 | Document number skipping |
| edesQueued | 18 | Document is waiting in queue to become "New" |
| edesImported | 19 | Manually imported electronic document |
| edesApproved | 20 | Document has been approved |
| edesApproving | 21 | Document is waiting for approval |
| edesRejecting | 22 | Document approval has been rejected |
| edesGenerated | 23 | Draft document has been used to generate electronic document |
| edesDetermined | 24 | Imported document has been reconciled with existing documents |
| edesImporting | 25 |  |

# ElectronicDocumentEntryTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# ElectronicDocumentServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ecsEDFProtocolsCollection | 0 |  |
| ecsEDFProtocol | 1 |  |
| ecsEDFProtocolWithParameters | 2 |  |
| ecsEDFProtocolInputParams | 3 |  |
| ecsEDFEntry | 4 |  |
| ecsEDFEntriesCollection | 5 |  |
| ecsEDFEntryInputParams | 6 |  |
| ecsEDFEntryListInputParams | 7 |  |
| ecsEDFEntryLog | 8 |  |
| ecsEDFEntryLogsCollection | 9 |  |
| ecsEDFEntryLogInputParams | 10 |  |
| ecsEDFEntryAddLogInputParams | 11 |  |
| ecsEDFMapping | 12 |  |
| ecsEDFMappingInputParams | 13 |  |
| ecsEDFImportEntry | 14 |  |
| ecsEDFDocMappingsCollection | 15 |  |
| ecsEDFDocMapping | 16 |  |
| ecsEDFDocMappingInputParams | 17 |  |

# ElectronicFileFormatsServiceDataInterfaces (Enumeration)

ElectronicFileFormatsService data interfaces.

| Member | Value | Description |
|---|---|---|
| effsImportFileParam | 0 | ImportFileParam data interface |
| effsElectronicFileFormat | 1 | ElectronicFileFormat data interface |
| effsElectronicFileFormatsParams | 2 | ElectronicFileFormatsParams data interface |
| effsElectronicFileFormatParams | 3 | ElectronicFileFormatParams data interface |

# EmailGroupsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| egsEmailGroup | 0 |  |
| egsEmailGroupParamsCollection | 1 |  |
| egsEmailGroupParams | 2 |  |

# EmployeeExemptionUnitEnum (Enumeration)

The time period unit of the exemption benifit.

| Member | Value | Description |
|---|---|---|
| eeu_None | 0 | Not use a unit. |
| eeu_Yearly | 1 | Once a year. |
| eeu_Monthly | 2 | Once a month. |
| eeu_Weekly | 3 | Once a week. |
| eeu_Daily | 4 | Once a day. |

# EmployeeIDTypeServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| eidtsEmployeeIDType | 0 |  |
| eidtsEmployeeIDTypeParamsCollection | 1 |  |
| eidtsEmployeeIDTypeParams | 2 |  |

# EmployeePaymentMethodEnum (Enumeration)

The payment method of the employee.

| Member | Value | Description |
|---|---|---|
| epm_None | 0 | No payment method. |
| epm_BankTransfer | 1 | Bank transfer. |

# EmployeePositionServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| epsEmployeePosition | 0 |  |
| epsEmployeePositionParamsCollection | 1 |  |
| epsEmployeePositionParams | 2 |  |

# EmployeeRolesSetupServiceDataInterfaces (Enumeration)

EmployeeRolesSetupService data interfaces.

| Member | Value | Description |
|---|---|---|
| erssEmployeeRoleSetup | 0 | EmployeeRoleSetup data interface |
| erssEmployeeRoleSetupParamsCollection | 1 | EmployeeRoleSetupParamsCollection data interface |
| erssEmployeeRoleSetupParams | 2 | EmployeeRoleSetupParams data interface |

# EmployeeStatusServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| essEmployeeStatus | 0 |  |
| essEmployeeStatusParamsCollection | 1 |  |
| essEmployeeStatusParams | 2 |  |

# EmployeeTransferProcessingStatusEnum (Enumeration)

The status of the employee transfer processing. When you add a new transfer, SAP Business One sets the status to New. B1iSN updates the status during the processing. Field name: Status.

| Member | Value | Description |
|---|---|---|
| etps_New | 0 | New |
| etps_Sent | 1 | Sent |
| etps_Accepted | 2 | Accepted |
| etps_Error | 3 | Error |

# EmployeeTransfersServiceDataInterfaces (Enumeration)

EmployeeTransfersService data interfaces.

| Member | Value | Description |
|---|---|---|
| etsEmployeeTransfer | 0 | EmployeeTransfer data interface |
| etsEmployeeTransferDetails | 1 | EmployeeTransferDetails data interface |
| etsEmployeeTransferDetail | 2 | EmployeeTransferDetail data interface |
| etsEmployeeTransfersParams | 3 | EmployeeTransfersParams data interface |
| etsEmployeeTransferParams | 4 | EmployeeTransferParams data interface |

# EmployeeTransferStatusEnum (Enumeration)

The status of the employee transfer. When you add a new transfer, SAP Business One sets the status to New. B1iSN updates the status during the processing.

| Member | Value | Description |
|---|---|---|
| ets_New | 0 | New |
| ets_Processing | 1 | Processing |
| ets_Sent | 2 | Sent |
| ets_Received | 3 | Received |
| ets_Accepted | 4 | Accepted |
| ets_Error | 5 | Error |

# EmploymentCategoryServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ecsEmploymentCategory | 0 |  |
| ecsEmploymentCategorysParams | 1 |  |
| ecsEmploymentCategoryParams | 2 |  |

# EndTypeEnum (Enumeration)

Specify the end type for the recurring activity.

| Member | Value | Description |
|---|---|---|
| etNoEndDate | 0 | Leave the end date open. |
| etByCounter | 1 | End the activity after a certain number of occurrences. |
| etByDate | 2 | End the activity by a certain date. |

# EnhancedDiscountGroupsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| edgsEnhancedDiscountGroup | 0 |  |
| edgsEnhancedDiscountGroupCollectionParams | 1 |  |
| edgsEnhancedDiscountGroupParams | 2 |  |

# EWBSupplyTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ewb_st_Inward | 0 |  |
| ewb_st_Outward | 1 |  |

# EWBTransactionTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ewb_tt_Regular | 0 |  |
| ewb_tt_BillToShipTo | 1 |  |
| ewb_tt_BillFromDispathFrom | 2 |  |
| ewb_tt_CombinationBillAndShip | 3 |  |

# EWBTransporterServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ewbtsEWBTransporter | 0 |  |
| ewbtsEWBTransporterParamsCollection | 1 |  |
| ewbtsEWBTransporterParams | 2 |  |

# ExceptionalEventServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| eesExceptionalEvent | 0 |  |
| eesExceptionalEventsParams | 1 |  |
| eesExceptionalEventParams | 2 |  |

# ExchangeRateSelectEnum (Enumeration)

Indicates whether to use the original exchange rate defined in the invoice, or to use the exchange rate defined for the day on which the dunning letters are created. This option is relevant when calculating interest in foreign currency for dunning letter.

| Member | Value | Description |
|---|---|---|
| ierFromInovice | 0 | Use exchange rate in invoice. |
| ierCurrentRate | 1 | Use current exchange rate. |

# ExemptionMaxAmountValidationTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| emaIndividual | 0 |  |
| emaAccumulated | 1 |  |

# ExpenseTypeServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| etsExpenseTypeData | 0 |  |
| etsExpenseTypeParams | 1 |  |

# ExportDeterminationServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| edsExportDeterminationsCollection | 0 |  |
| edsExportDetermination | 1 |  |
| edsExportDeterminationParams | 2 |  |
| edsExportDeterminationsParams | 3 |  |

# ExtendedTranslationsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| etsExtendedTranslation | 0 |  |
| etsExtendedTranslationsParams | 1 |  |
| etsExtendedTranslationParams | 2 |  |

# ExternalCallsServiceDataInterfaces (Enumeration)

ExternalCallsService data interfaces.

| Member | Value | Description |
|---|---|---|
| ecsExternalCall | 0 | ExternalCall data interface |
| ecsExternalCallParams | 1 | ExternalCallParams data interface |

# ExternalCallStatusEnum (Enumeration)

Statuses for a request call.

| Member | Value | Description |
|---|---|---|
| ecsNew | 0 | The request call is newly created and not processed by any applications. |
| ecsInProcess | 1 | The request call is received and is in process by the receiver applications. |
| ecsCompleted | 2 | The request call is completed successfully by the receiver applications. |
| ecsConfirmed | 3 | The request call is completed successfully and confirmed by the sender application (usually SAP Business One). |
| ecsFailed | 4 | The process of the request call failed. |

# ExternalReconciliationsServiceDataInterfaces (Enumeration)

ExternalReconciliationsService data interfaces.

| Member | Value | Description |
|---|---|---|
| ersExternalReconciliation | 0 | ExternalReconciliation data interface |
| ersExternalReconciliationsParamsCollection | 1 | ExternalReconciliationsParamsCollection data interface |
| ersExternalReconciliationParams | 2 | ExternalReconciliationParams data interface |
| ersExternalReconciliationFilterParams | 3 | ExternalReconciliationFilterParams data interface |

# FAAccountDeterminationsServiceDataInterfaces (Enumeration)

FAAccountDeterminationsService data interfaces.

| Member | Value | Description |
|---|---|---|
| faadsFAAccountDetermination | 0 | FAAccountDetermination data interface |
| faadsFAAccountDeterminationParamsCollection | 1 | FAAccountDeterminationParamsCollection data interface |
| faadsFAAccountDeterminationParams | 2 | FAAccountDeterminationParams data interface |

# FinancialYearsServiceDataInterfaces (Enumeration)

FinancialYearsService data interfaces.

| Member | Value | Description |
|---|---|---|
| fysFinancialYear | 0 | FinancialYear data interface |
| fysFinancialYearsParams | 1 | FinancialYearsService data interface |
| fysFinancialYearParams | 2 | FinancialYearParams data interface |

# FiscalPrinterServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| fpsFiscalPrinter | 0 |  |
| fpsFiscalPrintersParams | 1 |  |
| fpsFiscalPrinterParams | 2 |  |

# FixedAssetItemsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| faisFixedAssetValues | 0 |  |
| faisFixedAssetValuesCollection | 1 |  |
| faisFixedAssetValuesParams | 2 |  |
| faisFixedAssetEndBalance | 3 |  |

# FolioLetterEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| fLetterA | 0 |  |
| fLetterB | 1 |  |
| fLetterC | 2 |  |
| fLetterE | 3 |  |
| fLetterM | 4 |  |
| fLetterR | 5 |  |
| fLetterT | 6 |  |
| fLetterX | 7 |  |
| fLetterEMPTY | 8 |  |

# ForecastViewTypeEnum (Enumeration)

Types of time periods for sales forecasts, indicating whether the forecast contains daily, weekly, or monthly estimated sales figures.

| Member | Value | Description |
|---|---|---|
| fvtDaily | 0 | The forecast contains daily figures. |
| fvtWeekly | 1 | The forecast contains weekly figures. |
| fvtMonthly | 2 | The forecast contains monthly figures. |

# FormattedSearchByFieldEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| fsbfWhenExitingAlteredColumn | 0 |  |
| fsbfWhenFieldChanges | 1 |  |
| fsbfWhenColumnValueChanges | 2 |  |

# FormPreferencesServiceDataInterfaces (Enumeration)

FormPreferencesService data interfaces.

| Member | Value | Description |
|---|---|---|
| fpsdiColumnsPreferences | 0 | ColumnsPreferences data interface |
| fpsdiColumnsPreferencesParams | 1 | ColumnsPreferencesParams data interface |

# FreightTypeEnum (Enumeration)

Types of freight expense.

| Member | Value | Description |
|---|---|---|
| ftShipping | 0 | Shipping-related expense |
| ftInsurance | 1 | Insurance-related expense |
| ftOther | 2 | Other expense |

# FreightTypeForBolloEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ftStandard | 0 |  |
| ftBollo | 1 |  |

# GeneralServiceDataInterfaces (Enumeration)

GeneralService data interfaces.

| Member | Value | Description |
|---|---|---|
| gsGeneralDataCollection | 0 | GeneralDataCollection data interface |
| gsGeneralData | 1 | GeneralData data interface |
| gsGeneralCollectionParams | 2 | GeneralCollectionParams data interface |
| gsGeneralDataParams | 3 | GeneralDataParams data interface |
| gsInvokeParams | 4 | InvokeParams data interface |

# GeneratedAssetStatusEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| gasOpen | 0 |  |
| gasClosed | 1 |  |

# GetGLAccountByEnum (Enumeration)

The methods to get the G/L account.

| Member | Value | Description |
|---|---|---|
| gglab_General | 0 | General method. |
| gglab_Warehouse | 1 | By warehouse. |
| gglab_ItemGroup | 2 | By item group. |

# GLAccountAdvancedRulesServiceDataInterfaces (Enumeration)

GLAccountAdvancedRulesService data interfaces.

| Member | Value | Description |
|---|---|---|
| glaarsGLAccountAdvancedRule | 0 | GLAccountAdvancedRule data interface |
| glaarsGLAccountAdvancedRuleParamsCollection | 1 | GLAccountAdvancedRuleParamsCollection data interfaces |
| glaarsGLAccountAdvancedRuleParams | 2 | GLAccountAdvancedRuleParams data interfaces |

# GovPayCodePeriodicityEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| gpcpMonth | 0 |  |
| gpcpQuarter | 1 |  |
| gpcpHalfMonth | 2 |  |
| gpcpTenDays | 3 |  |

# GovPayCodesServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| gpcsGovPayCode | 0 |  |
| gpcsGovPayCodeParamsCollection | 1 |  |
| gpcsGovPayCodeParams | 2 |  |

# GroupingMethodEnum (Enumeration)

Indicates whether to produce dunning letters per invoice, per dunning level, or per business partner.

| Member | Value | Description |
|---|---|---|
| gmPerInvoice | 0 | Create a letter for each invoice. |
| gmPerDunningLevel | 1 | Create one letter for all invoices within a dunning level for each business partner. |
| gmPerBP | 2 | Create one letter for all invoices for each business partner. |

# GSTTaxCategoryEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| gtc_Regular | 0 |  |
| gtc_NilRated | 1 |  |
| gtc_Exempt | 2 |  |

# GSTTransactionTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| gsttrantyp_BillOfSupply | 0 |  |
| gsttrantyp_GSTTaxInvoice | 1 |  |
| gsttrantyp_GSTDebitMemo | 2 |  |

# GTIsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| gtisGTIParamsCollection | 0 |  |
| gtisGTIParams | 1 |  |

# GTSResponseToExceedingEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| Block | 0 |  |
| Split | 1 |  |

# HolidayServiceDataInterfaces (Enumeration)

HolidayService data interfaces.

| Member | Value | Description |
|---|---|---|
| hsHoliday | 0 | Holiday data interface |
| hsHolidaysParams | 1 | HolidaysParams data interface |
| hsHolidayParams | 2 | HolidayParams data interface |

# IdentificationCodeServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| icsIdentificationCodes | 0 |  |
| icsIdentificationCode | 1 |  |
| icsIdentificationCodeParams | 2 |  |

# IdentificationCodeTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| idctOrder | 0 |  |
| idctDelivery | 1 |  |
| idctInvoice | 2 |  |
| idctCreditNote | 3 |  |
| idctStandardItemTypeIdentification | 4 |  |
| idctItemCommodityClassification | 5 |  |

# ImportDeterminationServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| idsImportDeterminationsCollection | 0 |  |
| idsImportDetermination | 1 |  |
| idsImportDeterminationParams | 2 |  |
| idsImportDeterminationsParams | 3 |  |

# ImportFieldTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| iftInvalid | 0 |  |
| iftFederalTaxID | 1 |  |
| iftAdditionalID | 2 |  |
| iftUnifiedFederalTaxID | 3 |  |
| iftCNPJ | 4 |  |
| iftAliasName | 5 |  |
| iftIBAN | 6 |  |
| iftBPName | 7 |  |

# ImportOrExportTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| et_IpmortsOrExports | 0 |  |
| et_SEZ_Developer | 1 |  |
| et_SEZ_Unit | 2 |  |
| et_Deemed_ImportsOrExports | 3 |  |

# IndiaHsnServiceDataInterfaces (Enumeration)

IndiaHsnService data interfaces.

| Member | Value | Description |
|---|---|---|
| iscIndiaHsn | 0 | IndiaHsnService data interfaces |
| iscIndiaHsnParamsCollection | 1 | IndiaHsnParamsCollection data interfaces |
| iscIndiaHsnParams | 2 | IndiaHsnParams data interfaces |

# IndiaSacCodeServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| iscIndiaSacCode | 0 |  |
| iscIndiaSacCodeParamsCollection | 1 |  |
| iscIndiaSacCodeParams | 2 |  |

# InstallmentPaymentsPossiblityEnum (Enumeration)

Installment options for payments.

| Member | Value | Description |
|---|---|---|
| ippYes | 0 | The system allows installments. |
| ippNo | 1 | The system does not allow installments. |
| ippCr | 2 | Credit - The system allows equal installments related to the payment by the customer. However, the system writes a single row in the accounting document for this transaction, because the credit card company pays the entire amount with a single payment. |
| ippRd | 3 | Reduction - The system allows installments but also enables to change the first installment of the related payment by the customer. However, the system writes a single row in the accounting document for this transaction, because the credit card company pays the entire amount with a single payment. |

# IntegrationPackagesConfigureServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ipcsIntegrationPackageConfigure | 0 |  |
| ipcsIntegrationPackagesParams | 1 |  |
| ipcsIntegrationPackageParams | 2 |  |

# InternalReconciliationsServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| irsInternalReconciliation | 0 |  |
| irsInternalReconciliationParams | 1 |  |
| irsInternalReconciliationOpenTransParams | 2 |  |
| irsInternalReconciliationOpenTrans | 3 |  |

# IntrastatConfigurationEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# IntrastatConfigurationServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| icsIntrastatConfiguration | 0 |  |
| icsIntrastatConfigurationCollectionParams | 1 |  |
| icsIntrastatConfigurationParams | 2 |  |

# IntrastatConfigurationTriangDealEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| enNone | 0 |  |
| enType11 | 11 |  |
| enType21 | 21 |  |
| enType31 | 31 |  |

# InvBaseDocTypeEnum (Enumeration)

Specifies the document type for inventory transfer.

| Member | Value | Description |
|---|---|---|
| Default | 0 | Not specified, use the default value in the database. |
| Empty | 1 | Set to empty. |
| PurchaseDeliveryNotes | 2 | Goods receipt PO type |
| InventoryGeneralEntry | 3 |  |
| WarehouseTransfers | 4 |  |
| InventoryTransferRequest | 5 | Inventory transfer request |

# InventoryAccountTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
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

# InventoryCountingsServiceDataInterfaces (Enumeration)

InventoryCountingsService data interfaces.

| Member | Value | Description |
|---|---|---|
| icsInventoryCounting | 0 | InventoryCounting data interface |
| icsInventoryCountingParamsCollection | 1 | InventoryCountingParamsCollection data interface |
| icsInventoryCountingParams | 2 | InventoryCountingParams data interface |

# InventoryOpeningBalancePriceSourceEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| iobpsByPriceList | 0 |  |
| iobpsLastEvaluatedPrice | 1 |  |
| iobpsItemCost | 2 |  |

# InventoryOpeningBalancesServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| iobsInventoryOpeningBalance | 0 |  |
| iobsInventoryOpeningBalanceParamsCollection | 1 |  |
| iobsInventoryOpeningBalanceParams | 2 |  |

# InventoryPostingCopyOptionEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ipcoNoCountersDiff | 0 |  |
| ipcoIndividual1CountedQuantity | 1 |  |
| ipcoIndividual2CountedQuantity | 2 |  |
| ipcoIndividual3CountedQuantity | 3 |  |
| ipcoIndividual4CountedQuantity | 4 |  |
| ipcoIndividual5CountedQuantity | 5 |  |
| ipcoTeamCountedQuantity | 6 |  |

# InventoryPostingPriceSourceEnum (Enumeration)

The price source that the application uses to fill the Price field.

| Member | Value | Description |
|---|---|---|
| ippsByPriceList | 0 | Price List is for you to specify a price list or last purchase price. |
| ippsLastEvaluatedPrice | 1 | Last Evaluated Price if you use non-perpetual inventory. |
| ippsItemCost | 2 | Item Cost if you use perpetual inventory. |

# InventoryPostingsServiceDataInterfaces (Enumeration)

InventoryPostingsService data interfaces.

| Member | Value | Description |
|---|---|---|
| ipsInventoryPosting | 0 | InventoryPosting data interface |
| ipsInventoryPostingParamsCollection | 1 | InventoryPostingParamsCollection data interface |
| ipsInventoryPostingParams | 2 | InventoryPostingParams data interface |
| ipsInventoryPostingCopyOption | 3 | InventoryPostingCopyOption data interface |

# IssuePrimarilyByEnum (Enumeration)

Specify whether you want to pick the serial or batch items for issuing according to their bin locations or their serial or batch information.

| Member | Value | Description |
|---|---|---|
| ipbSerialAndBatchNumbers | 0 | By serial or batch numbers. |
| ipbBinLocations | 1 | By bin locations. |

# ItemClassEnum (Enumeration)

Item classes.

| Member | Value | Description |
|---|---|---|
| itcService | 1 | Service class |
| itcMaterial | 2 | Material class |

# ItemTypeEnum (Enumeration)

Item types.

| Member | Value | Description |
|---|---|---|
| itItems | 0 | Physical Items. |
| itLabor | 1 | Labor per Item Type. |
| itTravel | 2 | Travel per Item Type. |
| itFixedAssets | 3 | Fixed Assets. |

# ItemUoMTypeEnum (Enumeration)

The UoM type of the item.

| Member | Value | Description |
|---|---|---|
| iutPurchasing | 0 | Purchasing |
| iutSales | 1 | Sales |
| iutInventory | 2 | Inventory |

# JournalEntryDocumentTypeServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| jedtsJournalEntryDocumentType | 0 |  |
| jedtsJournalEntryDocumentTypeParamsCollection | 1 |  |
| jedtsJournalEntryDocumentTypeParams | 2 |  |

# KPIsServiceDataInterfaces (Enumeration)

KPIsService data interfaces.

| Member | Value | Description |
|---|---|---|
| kpisKPI | 0 | KPI data interface |
| kpisKPIsParams | 1 | KPIsParams data interface |
| kpisKPIParams | 2 | KPIParams data interface |

# KPITypeEnum (Enumeration)

The types for the parameter set.

| Member | Value | Description |
|---|---|---|
| asSingle | 0 | Use the Single type for parameters that contain only one value. |
| asQuarterly | 1 | Use the Quarterly type for parameters that contain one value for each of the four quarters of the year. |
| asMonthly | 2 | Use the Monthly type for parameters that contain one value for each of the 12 months of the year. |
| asMultiple | 3 | Use the Multiple type for parameters that contain multiple values that need to be defined in one parameter. |

# LandedCostAllocationByEnum (Enumeration)

Specify the distribution type for the landed cost.

| Member | Value | Description |
|---|---|---|
| asCashValueBeforeCustoms | 0 | The related costs are distributed in relation to the share of an item of the total FOB price of the delivery minus customs. |
| asCashValueAfterCustoms | 1 | The related costs are distributed in relation to the share of an item of the total FOB price of the delivery plus customs. |
| asQuantity | 2 | The related costs are distributed according to the quantity of an item in proportion to the total quantity of the delivery. |
| asWeight | 3 | The related costs are distributed according to the weight of an item in proportion to the total weight of the delivery. |
| asVolume | 4 | The related costs are distributed according to the volume of an item in proportion to the total volume of the delivery. |
| asEqual | 5 | The related costs are distributed equally among the delivery items. |
| asLegalCost | 6 |  |

# LandedCostBaseDocumentTypeEnum (Enumeration)

Specify the base document type of the landed costs document.

| Member | Value | Description |
|---|---|---|
| asDefault | 0 | Not specified, use the default value in the database. |
| asEmpty | 1 | Set to empty. |
| asGoodsReceiptPO | 2 | The landed costs document is based on a goods receipt PO. |
| asLandedCosts | 3 | The landed costs document is based on another landed costs document. |
| asPurchaseInvoice | 4 |  |

# LandedCostCostCategoryEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| lccc_CustomsVAT | 0 |  |
| lccc_ExciseCost | 1 |  |
| lccc_CustomsDuty | 2 |  |

# LandedCostDocStatusEnum (Enumeration)

The status of a landed costs document.

| Member | Value | Description |
|---|---|---|
| lcOpen | 0 | Open |
| lcClosed | 1 | Closed |

# LandedCostsServiceDataInterfaces (Enumeration)

LandedCostsService data interfaces.

| Member | Value | Description |
|---|---|---|
| lcsLandedCost | 0 | LandedCost data interface |
| lcsLandedCostsParams | 1 | LandedCostsParams data interface |
| lcsLandedCostParams | 2 | LandedCostParams data interface |

# LCCostTypeEnum (Enumeration)

Specifies the landed cost type.

| Member | Value | Description |
|---|---|---|
| asFixedCosts | 0 | Fixed costs per item. |
| asVariableCosts | 1 | Variable costs per item. Only relevant for companies not managing a perpetual inventory. |
| asLegalCosts | 2 |  |

# LegalDataLineTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| ldlt_DocumentTotal | 0 |  |
| ldlt_TaxPerLine | 1 |  |
| ldlt_TotalTax | 2 |  |

# LegalDataServiceDataInterfaces (Enumeration)

| Member | Value | Description |
|---|---|---|
| ldsLegalData | 0 |  |
| ldsLegalDataParamsCollection | 1 |  |
| ldsLegalDataParams | 2 |  |

# LicenseTypeEnum (Enumeration)

Types of SAP Business One licenses that can be assigned via the DI API.

| Member | Value | Description |
|---|---|---|
| ltIdirect | 25 | Indirect license |
| ltSOAIndirect | 20 | For internal use |
| ltSOA | 21 | For internal use |
| ltB1iIndirect | 22 | For internal use |
| ltB1i | 23 | For internal use |

# LicenseUpdateTypeEnum (Enumeration)

Indicates whether to assign or remove a license.

| Member | Value | Description |
|---|---|---|
| ultAssign | 0 | Assign license. |
| ultRemove | 1 | Remove license. |

# LineStatusTypeEnum (Enumeration)

| Member | Value | Description |
|---|---|---|
| lst_Open | 0 |  |
| lst_Closed | 1 |  |

# LineTypeEnum (Enumeration)

Types of detail lines for down payments to draw.

| Member | Value | Description |
|---|---|---|
| ltDocument | 0 | Standard line |
| ltRounding | 1 | Rounding line, added if the detail lines do not add up to the totals in the parent object |
| ltVat | 2 | Rounding line, added if rounding exists within the parent object |
