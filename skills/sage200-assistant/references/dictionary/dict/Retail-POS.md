# Sage 200 Evolution table dictionary - Retail POS

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _retAgentSession - Retail Agent Session (RetailAgentSession)
Alias: Retail Agent Session | Freedom Name: RetailAgentSession | Record Identifier: 
Notes: Retail Agent Session
PK: idAgentSession
Columns (28):
  idAgentSession int NOT NULL identity PK
  iTradingSessionID int NULL
  bIsTillSession bit NOT NULL default (0)
  iTillSessionID int NULL
  iAgentID int NULL
  iTillID int NULL
  fAgentFloat float NULL
  dCurrentDate datetime NULL
  bCashedUp bit NULL default (0)
  cCashUpReference varchar(50) NULL
  dCashUpDate datetime NULL
  iCashUpTillID int NULL
  bCashUpFinalised bit NOT NULL default (0)
  iFinaliseAgentID int NULL
  dFinalisedDate datetime NULL
  fAgentFloatCounted float NULL
  fAgentFloatFinalised float NULL
  iFloatInitialiseAgentID int NULL
  iCashUpAgentID int NULL
  _retAgentSession_iBranchID int NULL
  _retAgentSession_dCreatedDate datetime NULL
  _retAgentSession_dModifiedDate datetime NULL
  _retAgentSession_iCreatedBranchID int NULL
  _retAgentSession_iModifiedBranchID int NULL
  _retAgentSession_iCreatedAgentID int NULL
  _retAgentSession_iModifiedAgentID int NULL
  _retAgentSession_iChangeSetID int NULL
  _retAgentSession_Checksum binary(20) NULL

## _retAgentSessionCashPickupTotals - Retail Agent Session Cash Pickup (RetailAgentSessionCashPickupTotals)
Alias: Retail Agent Session Cash Pickup | Freedom Name: RetailAgentSessionCashPickupTotals | Record Identifier: 
Notes: Retail Agent Session Cash Pickup
PK: idAgentSessionCashPickupTotals
Columns (16):
  idAgentSessionCashPickupTotals int NOT NULL identity PK
  iAgentSessionID int NULL
  fCashPickupTotalSystem float NULL
  fCashPickupTotalCounted float NULL
  fCashPickupTotalFinalised float NULL
  _retAgentSessionCashPickupTotals_iBranchID int NULL
  _retAgentSessionCashPickupTotals_dCreatedDate datetime NULL
  _retAgentSessionCashPickupTotals_dModifiedDate datetime NULL
  _retAgentSessionCashPickupTotals_iCreatedBranchID int NULL
  _retAgentSessionCashPickupTotals_iModifiedBranchID int NULL
  _retAgentSessionCashPickupTotals_iCreatedAgentID int NULL
  _retAgentSessionCashPickupTotals_iModifiedAgentID int NULL
  _retAgentSessionCashPickupTotals_iChangeSetID int NULL
  _retAgentSessionCashPickupTotals_Checksum binary(20) NULL
  iCurrencyID int NOT NULL default (0)
  fExchangeRate float NOT NULL default (0)

## _retAgentSessionDenomination - Retail Agent Session Denomination (RetailAgentSessionDenomination)
Alias: Retail Agent Session Denomination | Freedom Name: RetailAgentSessionDenomination | Record Identifier: 
Notes: Retail Agent Session Denomination
PK: idAgentSessionDenomination
Columns (20):
  idAgentSessionDenomination int NOT NULL identity PK
  iAgentSessionID int NULL
  iDenominationID int NULL
  iFloatCount int NULL
  iCashCount int NULL
  iFloatCountFinalised int NULL
  iCashCountFinalised int NULL
  _retAgentSessionDenomination_iBranchID int NULL
  _retAgentSessionDenomination_dCreatedDate datetime NULL
  _retAgentSessionDenomination_dModifiedDate datetime NULL
  _retAgentSessionDenomination_iCreatedBranchID int NULL
  _retAgentSessionDenomination_iModifiedBranchID int NULL
  _retAgentSessionDenomination_iCreatedAgentID int NULL
  _retAgentSessionDenomination_iModifiedAgentID int NULL
  _retAgentSessionDenomination_iChangeSetID int NULL
  _retAgentSessionDenomination_Checksum binary(20) NULL
  fFloatCountFinalisedForeign float NOT NULL default (0)
  fCashCountFinalised float NOT NULL default (0)
  iCurrencyID int NOT NULL default (0)
  fExchangeRate float NOT NULL default (0)

## _retAgentSessionForeign
PK: idAgentSessionForeign
Columns (17):
  idAgentSessionForeign bigint NOT NULL identity PK
  iAgentSessionID bigint NOT NULL
  fAgentFloatForeign float NULL default (0)
  fAgentFloatHome float NULL default (0)
  fExchangeRate float NULL default (0)
  iCurrencyID int NULL default (0)
  _retAgentSessionForeign_iBranchID int NULL
  _retAgentSessionForeign_dCreatedDate datetime NULL
  _retAgentSessionForeign_dModifiedDate datetime NULL
  _retAgentSessionForeign_iCreatedBranchID int NULL
  _retAgentSessionForeign_iModifiedBranchID int NULL
  _retAgentSessionForeign_iCreatedAgentID int NULL
  _retAgentSessionForeign_iModifiedAgentID int NULL
  _retAgentSessionForeign_iChangeSetID int NULL
  _retAgentSessionForeign_Checksum binary(20) NULL
  fAgentFloatCountedForeign float NOT NULL default (0)
  fAgentFloatFinalisedForeign float NOT NULL default (0)

## _retAgentSessionPettyCashTotals - Retail Agent Session Petty Cash (RetailAgentSessionPettyCashTotals)
Alias: Retail Agent Session Petty Cash | Freedom Name: RetailAgentSessionPettyCashTotals | Record Identifier: 
Notes: Retail Agent Session Petty Cash
PK: idAgentSessionPettyCashTotals
Columns (17):
  idAgentSessionPettyCashTotals int NOT NULL identity PK
  iAgentSessionID int NULL
  fAdvancedTotalSystem float NULL
  fAdvancedTotalCounted float NULL
  fAdvancedTotalFinalised float NULL
  fChangeTotalSystem float NULL
  fChangeTotalCounted float NULL
  fChangeTotalFinalised float NULL
  _retAgentSessionPettyCashTotals_iBranchID int NULL
  _retAgentSessionPettyCashTotals_dCreatedDate datetime NULL
  _retAgentSessionPettyCashTotals_dModifiedDate datetime NULL
  _retAgentSessionPettyCashTotals_iCreatedBranchID int NULL
  _retAgentSessionPettyCashTotals_iModifiedBranchID int NULL
  _retAgentSessionPettyCashTotals_iCreatedAgentID int NULL
  _retAgentSessionPettyCashTotals_iModifiedAgentID int NULL
  _retAgentSessionPettyCashTotals_iChangeSetID int NULL
  _retAgentSessionPettyCashTotals_Checksum binary(20) NULL

## _retAgentSessionTenderTotals - Retail Agent Session Tender (RetailAgentSessionTenderTotals)
Alias: Retail Agent Session Tender | Freedom Name: RetailAgentSessionTenderTotals | Record Identifier: 
Notes: Retail Agent Session Tender
PK: idAgentSessionTenderTotals
Columns (20):
  idAgentSessionTenderTotals int NOT NULL identity PK
  iAgentSessionID int NULL
  iTenderTypeID int NULL
  bCashTenderType bit NOT NULL default (0)
  iTenderCount int NULL
  fTenderAmountSystem float NULL
  fTenderAmountAdjusted float NULL
  fTenderAmountCounted float NULL
  fTenderAmountFinalised float NULL
  _retAgentSessionTenderTotals_iBranchID int NULL
  _retAgentSessionTenderTotals_dCreatedDate datetime NULL
  _retAgentSessionTenderTotals_dModifiedDate datetime NULL
  _retAgentSessionTenderTotals_iCreatedBranchID int NULL
  _retAgentSessionTenderTotals_iModifiedBranchID int NULL
  _retAgentSessionTenderTotals_iCreatedAgentID int NULL
  _retAgentSessionTenderTotals_iModifiedAgentID int NULL
  _retAgentSessionTenderTotals_iChangeSetID int NULL
  _retAgentSessionTenderTotals_Checksum binary(20) NULL
  iCurrencyID int NOT NULL default (0)
  fExchangeRate float NOT NULL default (0)

## _retCashPickup - Retail Cash Pickup (RetailCashPickup)
Alias: Retail Cash Pickup | Freedom Name: RetailCashPickup | Record Identifier: 
Notes: Retail Cash Pickup
PK: idCashPickup
Columns (14):
  idCashPickup int NOT NULL identity PK
  iAgentSessionID int NULL
  iTillID int NULL
  dPickupDate datetime NULL
  cCashPickupReference varchar(50) NULL
  _retCashPickup_iBranchID int NULL
  _retCashPickup_dCreatedDate datetime NULL
  _retCashPickup_dModifiedDate datetime NULL
  _retCashPickup_iCreatedBranchID int NULL
  _retCashPickup_iModifiedBranchID int NULL
  _retCashPickup_iCreatedAgentID int NULL
  _retCashPickup_iModifiedAgentID int NULL
  _retCashPickup_iChangeSetID int NULL
  _retCashPickup_Checksum binary(20) NULL

## _retCashPickupCurrency
PK: idCashPickupCurrency
Columns (14):
  idCashPickupCurrency int NOT NULL identity PK
  iCashPickupID int NOT NULL
  fPickupAmount float NULL default (0)
  fExchangeRate float NULL default (0)
  iCurrencyID int NULL default (0)
  _retCashPickupCurrency_iBranchID int NULL
  _retCashPickupCurrency_dCreatedDate datetime NULL
  _retCashPickupCurrency_dModifiedDate datetime NULL
  _retCashPickupCurrency_iCreatedBranchID int NULL
  _retCashPickupCurrency_iModifiedBranchID int NULL
  _retCashPickupCurrency_iCreatedAgentID int NULL
  _retCashPickupCurrency_iModifiedAgentID int NULL
  _retCashPickupCurrency_iChangeSetID int NULL
  _retCashPickupCurrency_Checksum binary(20) NULL

## _retCashPickupDenomination - Retail Cash Pickup Denomination (RetailCashPickupDenomination)
Alias: Retail Cash Pickup Denomination | Freedom Name: RetailCashPickupDenomination | Record Identifier: 
Notes: Retail Cash Pickup Denomination
PK: idCashPickupDenomination
Columns (14):
  idCashPickupDenomination int NOT NULL identity PK
  iCashPickupID int NULL
  iDenominationID int NULL
  iCashCount int NULL
  _retCashPickupDenomination_iBranchID int NULL
  _retCashPickupDenomination_dCreatedDate datetime NULL
  _retCashPickupDenomination_dModifiedDate datetime NULL
  _retCashPickupDenomination_iCreatedBranchID int NULL
  _retCashPickupDenomination_iModifiedBranchID int NULL
  _retCashPickupDenomination_iCreatedAgentID int NULL
  _retCashPickupDenomination_iModifiedAgentID int NULL
  _retCashPickupDenomination_iChangeSetID int NULL
  _retCashPickupDenomination_Checksum binary(20) NULL
  iCashPickupCurrencyID int NOT NULL default (0)

## _retDefaults - Retail Default (RetailPointOfSaleDefaults)
Alias: Retail Default | Freedom Name: RetailPointOfSaleDefaults | Record Identifier: 
Notes: Retail Default
PK: idRetailDefaults
Columns (103):
  idRetailDefaults int NOT NULL identity PK
  fDefaultFloatAmount float NULL
  fDefaultCashPickupAmount float NULL
  iDefaultCustomerID int NULL
  iModelCustomerID int NULL
  cAutoNumBranchPrefix varchar(3) NULL
  iDocketTrCodeID int NULL
  iDocketAdjTrCodeID int NULL
  iCashUpBankTrCodeID int NULL
  iCashUpExcessTrCodeID int NULL
  iCashUpShortageTrCodeID int NULL
  iPettyCashAdvancedTrCodeID int NULL
  iPettyCashProcessedTrCodeID int NULL
  cPoleDisplayDef1 varchar(20) NULL
  cPoleDisplayDef2 varchar(20) NULL
  iReceiptDiscountTrCodeID int NULL
  bAllocationPrompt bit NOT NULL default (0)
  bVariableBarcodesEnabled bit NOT NULL default (0)
  iVariableBarcodePriceListID int NULL
  iDeliveryMethodDefaultID int NULL
  bDocketForceReps bit NOT NULL default (0)
  bDocketPromptForCustomerAccount bit NOT NULL default (0)
  bPettyCashAdvanceAuthorisation bit NOT NULL default (0)
  fPettyCashAdvanceLimit float NULL
  bRestrictPettyCashAdvance bit NOT NULL default (0)
  bCashPickupWarning bit NOT NULL default (0)
  cCashPickupWarningMessage varchar(50) NULL
  fCashPickupMaxCashInTillLimit float NULL
  bDepositUse bit NOT NULL default (0)
  bDepositForce bit NOT NULL default (0)
  iDepositTrCodeID int NULL
  fDepositMinPerc float NULL
  fDepositMinAmnt float NULL
  bDepositAllow bit NOT NULL default (0)
  fDepositGreaterThan float NULL
  iInactivityTimeout int NULL
  iReversalInvJrBatchID int NULL
  iReversalAdjTrCodeID int NULL
  iLayByModelCustomerID int NULL
  iReversalAgentID int NULL
  iLayByPaymentTermCount int NULL
  iLayByPaymentTermOnDay int NULL
  iLayByPaymentTermOfEvery int NULL
  fLayByDepositMinPerc float NULL
  fLayByDepositMinAmnt float NULL
  fLayByCancellationPerc float NULL
  fLayByCancellationAmnt float NULL
  iLayByCancellationTrCodeID int NULL
  bReserveStockOrders bit NOT NULL default (0)
  bReserveStockLayBys bit NOT NULL default (0)
  bPromoAutoYN bit NOT NULL default (0)
  iPromoAutoLength int NOT NULL default (6)
  iPromoAutoAlphaLength int NOT NULL default (3)
  bUpperPromoNo bit NOT NULL default (0)
  iKeepAsideDaysToExpiry int NOT NULL default (7)
  iDisplayDocketPromptFields int NOT NULL default (0)
  iForceDocketPromptFields int NOT NULL default (0)
  bLayByFirstPaymentInCurrentPeriod bit NOT NULL default (0)
  bAutoAdjust bit NOT NULL default (0)
  cDocketModeDocketPromptFields varchar(400) NULL
  cTillConfigPassword varchar(160) NULL
  bDisplayDocketPromotionCode bit NOT NULL default (1)
  bDisplayDocketPromotionDescription bit NOT NULL default (0)
  fReturnLimit float NULL
  bReturnAuthorisation bit NOT NULL default (0)
  bRestrictReturn bit NOT NULL default (0)
  bPromoItemListAutoYN bit NOT NULL default (0)
  bUpperPromoItemListNo bit NOT NULL default (0)
  iPromoItemListAutoLength int NOT NULL default (6)
  iPromoItemListAutoAlphaLength int NOT NULL default (3)
  bLayByEdit bit NOT NULL default (0)
  bLineForceReps bit NOT NULL default (0)
  bFloatPerAgentOrTill bit NOT NULL default (0)
  iTradingSessionDuration int NULL
  bDisableTradeOnExpiry bit NOT NULL default (0)
  bForceSerialNumbers bit NOT NULL default (0)
  bUseDocketRoundingOnTender bit NULL default (0)
  bRoundingOnCashTenderOnly bit NULL default (0)
  iRoundingGLAccount int NULL
  bAllowCashDrawerHandover bit NULL
  iInvSplitProcessOption int NOT NULL default (0)
  bUseVASAirtime bit NULL default (0)
  cVASAirtimeMerchantID varchar(40) NULL
  cVASAirtimeHostURI nvarchar(150) NULL
  _retDefaults_iBranchID int NULL
  _retDefaults_dCreatedDate datetime NULL
  _retDefaults_dModifiedDate datetime NULL
  _retDefaults_iCreatedBranchID int NULL
  _retDefaults_iModifiedBranchID int NULL
  _retDefaults_iCreatedAgentID int NULL
  _retDefaults_iModifiedAgentID int NULL
  _retDefaults_iChangeSetID int NULL
  _retDefaults_Checksum binary(20) NULL
  bAutoReserveStockLayBys bit NOT NULL default (0)
  bForceOrigTenderTypeonReturn bit NOT NULL default (0)
  bLayBysAutoCalculatePayments bit NULL default (1)
  bSetLaybyOnPromotionOn bit NULL default (0)
  bAutoAdjustReserved bit NULL default (0)
  bUseCurrency bit NOT NULL default (0)
  bUseSellingRate bit NOT NULL default (1)
  fMultiCurrencyVariance float NULL default (0)
  bRoundingOnMultiCurrencyCashTenderOnly bit NOT NULL default (0)
  bUseUOMVolumeDiscount bit NOT NULL default (0)

## _retDenomination - Retail Denomination (RetailDenomination)
Alias: Retail Denomination | Freedom Name: RetailDenomination | Record Identifier: 
Notes: Retail Denomination
PK: idDenomination
Columns (14):
  idDenomination int NOT NULL identity PK
  cDenominationCode varchar(10) NULL
  mMultiple money NULL
  bIsCoin bit NULL
  bActive bit NOT NULL default (1)
  _retDenomination_iBranchID int NULL
  _retDenomination_dCreatedDate datetime NULL
  _retDenomination_dModifiedDate datetime NULL
  _retDenomination_iCreatedBranchID int NULL
  _retDenomination_iModifiedBranchID int NULL
  _retDenomination_iCreatedAgentID int NULL
  _retDenomination_iModifiedAgentID int NULL
  _retDenomination_iChangeSetID int NULL
  _retDenomination_Checksum binary(20) NULL

## _retDiscountReason - Retail Discount Reason
Alias: Retail Discount Reason | Freedom Name:  | Record Identifier: cDiscountReasonCode
Notes: Retail Discount Reason
PK: idDiscountReason
Columns (13):
  idDiscountReason int NOT NULL identity PK
  cDiscountReasonCode varchar(10) NULL
  cDiscountReasonDesc varchar(30) NULL
  bActive bit NOT NULL default (1)
  _retDiscountReason_iBranchID int NULL
  _retDiscountReason_dCreatedDate datetime NULL
  _retDiscountReason_dModifiedDate datetime NULL
  _retDiscountReason_iCreatedBranchID int NULL
  _retDiscountReason_iModifiedBranchID int NULL
  _retDiscountReason_iCreatedAgentID int NULL
  _retDiscountReason_iModifiedAgentID int NULL
  _retDiscountReason_iChangeSetID int NULL
  _retDiscountReason_Checksum binary(20) NULL

## _retDocketLock
PK: idDocketLock
Columns (3):
  idDocketLock int NOT NULL identity PK
  iDocketID bigint NOT NULL
  iTillID int NOT NULL

## _retEOD - Retail End of Day
Alias: Retail End of Day | Freedom Name:  | Record Identifier: 
Notes: Retail End of Day
Columns: none recorded yet (table seen in another Evolution database, not in the scripted one)

## _retLayBys
PK: idLayBys
Columns (28):
  idLayBys int NOT NULL identity PK
  iInvoiceID bigint NULL
  iTermCount int NULL
  iTermOnDay int NULL
  iTermOfEvery int NULL
  fLayByTotal float NULL
  dInceptionDate datetime NULL
  iTermsElapsed int NULL
  fPaidToDate float NULL
  dLastPaymentDate datetime NULL
  dNextPaymentDate datetime NULL
  dFinalPaymentDate datetime NULL
  fLayByDeposit float NULL
  fInstallmentAmount float NULL
  dLastUpdated datetime NULL
  fPaymentDue float NULL
  iInvoiceIDFinalised bigint NULL
  fCancellationFee float NULL
  fCancellationFeeTax float NULL
  _retLayBys_iBranchID int NULL
  _retLayBys_dCreatedDate datetime NULL
  _retLayBys_dModifiedDate datetime NULL
  _retLayBys_iCreatedBranchID int NULL
  _retLayBys_iModifiedBranchID int NULL
  _retLayBys_iCreatedAgentID int NULL
  _retLayBys_iModifiedAgentID int NULL
  _retLayBys_iChangeSetID int NULL
  _retLayBys_Checksum binary(20) NULL

## _retPettyCash - Retail Petty Cash (RetailPettyCash)
Alias: Retail Petty Cash | Freedom Name: RetailPettyCash | Record Identifier: 
Notes: Retail Petty Cash
PK: idPettyCash
Columns (22):
  idPettyCash int NOT NULL identity PK
  iPettyCashTypeID int NULL
  cComment varchar(128) NULL
  iAdvancedAgentSessionID int NULL
  dAdvancedDate datetime NULL
  fAdvancedAmount float NULL
  bProcessed bit NOT NULL default (0)
  iProcessedAgentSessionID int NULL
  dProcessedDate datetime NULL
  fChangeAmount float NULL
  cReference varchar(50) NULL
  iAdvancedTillID int NULL
  iProcessedTillID int NULL
  _retPettyCash_iBranchID int NULL
  _retPettyCash_dCreatedDate datetime NULL
  _retPettyCash_dModifiedDate datetime NULL
  _retPettyCash_iCreatedBranchID int NULL
  _retPettyCash_iModifiedBranchID int NULL
  _retPettyCash_iCreatedAgentID int NULL
  _retPettyCash_iModifiedAgentID int NULL
  _retPettyCash_iChangeSetID int NULL
  _retPettyCash_Checksum binary(20) NULL

## _retPettyCashLine - Retail Petty Cash Line (RetailPettyCashLine)
Alias: Retail Petty Cash Line | Freedom Name: RetailPettyCashLine | Record Identifier: 
Notes: Retail Petty Cash Line
PK: idPettyCashLine
Columns (16):
  idPettyCashLine int NOT NULL identity PK
  iPettyCashID int NULL
  cReference varchar(128) NULL
  fExclAmount float NULL
  iTaxTypeID int NULL
  fTaxRate float NULL
  fInclAmount float NULL
  _retPettyCashLine_iBranchID int NULL
  _retPettyCashLine_dCreatedDate datetime NULL
  _retPettyCashLine_dModifiedDate datetime NULL
  _retPettyCashLine_iCreatedBranchID int NULL
  _retPettyCashLine_iModifiedBranchID int NULL
  _retPettyCashLine_iCreatedAgentID int NULL
  _retPettyCashLine_iModifiedAgentID int NULL
  _retPettyCashLine_iChangeSetID int NULL
  _retPettyCashLine_Checksum binary(20) NULL

## _retPettyCashType - Retail Petty Cash Type (RetailPettyCashType)
Alias: Retail Petty Cash Type | Freedom Name: RetailPettyCashType | Record Identifier: 
Notes: Retail Petty Cash Type
PK: idPettyCashType
Columns (16):
  idPettyCashType int NOT NULL identity PK
  cPettyCashTypeCode varchar(10) NULL
  cPettyCashTypeDesc varchar(30) NULL
  bActive bit NOT NULL default (1)
  iPettyCashLedgerID int NULL
  iPettyCashTaxTypeID int NULL
  iPettyCashTaxLedgerID int NULL
  _retPettyCashType_iBranchID int NULL
  _retPettyCashType_dCreatedDate datetime NULL
  _retPettyCashType_dModifiedDate datetime NULL
  _retPettyCashType_iCreatedBranchID int NULL
  _retPettyCashType_iModifiedBranchID int NULL
  _retPettyCashType_iCreatedAgentID int NULL
  _retPettyCashType_iModifiedAgentID int NULL
  _retPettyCashType_iChangeSetID int NULL
  _retPettyCashType_Checksum binary(20) NULL

## _retPOSLogFile
PK: idPOSLogFile
Columns (17):
  idPOSLogFile int NOT NULL identity PK
  iSystemFunctionID int NULL
  iAgentID int NULL
  iTillID int NOT NULL
  iSupervisorAgentID int NULL
  dCurrentDate datetime NULL
  cDescription varchar(1000) NULL
  iTradingSessionID int NULL
  _retPOSLogFile_iBranchID int NULL
  _retPOSLogFile_dCreatedDate datetime NULL
  _retPOSLogFile_dModifiedDate datetime NULL
  _retPOSLogFile_iCreatedBranchID int NULL
  _retPOSLogFile_iModifiedBranchID int NULL
  _retPOSLogFile_iCreatedAgentID int NULL
  _retPOSLogFile_iModifiedAgentID int NULL
  _retPOSLogFile_iChangeSetID int NULL
  _retPOSLogFile_Checksum binary(20) NULL

## _retPOSLogLinks - Retail Log File Link
Alias: Retail Log File Link | Freedom Name:  | Record Identifier: 
Notes: Retail Log File Link
PK: idPOSLogLinks
Columns (13):
  idPOSLogLinks bigint NOT NULL identity PK
  iInvNumID bigint NOT NULL
  iInvLineID bigint NULL
  iLogID int NULL
  _retPOSLogLinks_iBranchID int NULL
  _retPOSLogLinks_dCreatedDate datetime NULL
  _retPOSLogLinks_dModifiedDate datetime NULL
  _retPOSLogLinks_iCreatedBranchID int NULL
  _retPOSLogLinks_iModifiedBranchID int NULL
  _retPOSLogLinks_iCreatedAgentID int NULL
  _retPOSLogLinks_iModifiedAgentID int NULL
  _retPOSLogLinks_iChangeSetID int NULL
  _retPOSLogLinks_Checksum binary(20) NULL

## _retPosMenu
PK: idPOSMenu
Columns (20):
  idPOSMenu bigint NOT NULL identity PK
  iPOSKeyIndex int NULL
  cPOSKeyCaption nvarchar(50) NULL
  iPOSKeyColor int NULL
  iPOSKeyFontColor int NULL
  iCustomIndex int NULL
  idPOSMenuSetup bigint NULL
  cSkinName nvarchar(50) NULL
  bUseDesignColour bit NULL
  iStockLink int NULL default (0)
  iMID int NULL default (0)
  _retPOSMenu_iBranchID int NULL
  _retPOSMenu_dCreatedDate datetime NULL
  _retPOSMenu_dModifiedDate datetime NULL
  _retPOSMenu_iCreatedBranchID int NULL
  _retPOSMenu_iModifiedBranchID int NULL
  _retPOSMenu_iCreatedAgentID int NULL
  _retPOSMenu_iModifiedAgentID int NULL
  _retPOSMenu_iChangeSetID int NULL
  _retPOSMenu_Checksum binary(20) NULL

## _retPOSMenuSetup
PK: idPOSMenuSetup
Columns (14):
  idPOSMenuSetup bigint NOT NULL identity PK
  cPOSMenuCode nvarchar(50) NULL
  cPOSMenuDescription nvarchar(50) NULL
  iBackgroundColour int NULL
  bTransparentDisabledButtons bit NULL
  _retPOSMenuSetup_iBranchID int NULL
  _retPOSMenuSetup_dCreatedDate datetime NULL
  _retPOSMenuSetup_dModifiedDate datetime NULL
  _retPOSMenuSetup_iCreatedBranchID int NULL
  _retPOSMenuSetup_iModifiedBranchID int NULL
  _retPOSMenuSetup_iCreatedAgentID int NULL
  _retPOSMenuSetup_iModifiedAgentID int NULL
  _retPOSMenuSetup_iChangeSetID int NULL
  _retPOSMenuSetup_Checksum binary(20) NULL

## _retPOSTender - Retail Tender (RetailTender)
Alias: Retail Tender | Freedom Name: RetailTender | Record Identifier: 
Notes: Retail Tender
PK: idPOSTender
Columns (38):
  idPOSTender bigint NOT NULL identity PK
  iPOSTransactionID bigint NULL
  iTenderTypeID int NULL
  fAmount float NULL
  cNarrative varchar(1024) NULL
  cCardNumber varchar(20) NULL
  cCardHolder varchar(100) NULL
  dExpiryDate datetime NULL
  cEMVApplicationID varchar(40) NULL
  cEMVVerification varchar(10) NULL
  cEMVTrCertificate varchar(20) NULL
  cEMVApplLabel varchar(20) NULL
  cCardType varchar(200) NULL
  cAuthCode varchar(6) NULL
  dEFTDateTime datetime NULL
  cEMVTSI varchar(4) NULL
  idInvoiceDeposits int NULL
  cEFTBudgetPeriod varchar(2) NOT NULL default (0)
  cAuthorisationID varchar(6) NULL
  cInstitutionID varchar(11) NULL
  cTransactionType varchar(2) NULL
  cAccountType varchar(2) NULL
  cE0210RespCode varchar(2) NULL
  cE0202RespCode varchar(2) NULL
  bChipCard bit NOT NULL default (0)
  cEFTReferenceNumber varchar(20) NULL
  bManualEFT bit NOT NULL default (0)
  _retPOSTender_iBranchID int NULL
  _retPOSTender_dCreatedDate datetime NULL
  _retPOSTender_dModifiedDate datetime NULL
  _retPOSTender_iCreatedBranchID int NULL
  _retPOSTender_iModifiedBranchID int NULL
  _retPOSTender_iCreatedAgentID int NULL
  _retPOSTender_iModifiedAgentID int NULL
  _retPOSTender_iChangeSetID int NULL
  _retPOSTender_Checksum binary(20) NULL
  iCurrencyID int NULL default (0)
  fAmountForeign float NULL default (0)

## _retPOSTransaction - Retail Transaction (RetailTransactions)
Alias: Retail Transaction | Freedom Name: RetailTransactions | Record Identifier: 
Notes: Retail Transaction
PK: idPOSTransaction
Columns (23):
  idPOSTransaction bigint NOT NULL identity PK
  iTillID int NULL
  dTransactionDate datetime NULL
  iAgentID int NULL
  iTrCodesID int NULL
  iAccountID int NULL
  iTillTxType int NULL
  cAuditNumber varchar(50) NULL
  fAmount float NULL
  fAmountTendered float NULL
  fAmountChange float NULL
  iAgentSessionID int NULL
  iInvNumID bigint NULL
  _retPOSTransaction_iBranchID int NULL
  _retPOSTransaction_dCreatedDate datetime NULL
  _retPOSTransaction_dModifiedDate datetime NULL
  _retPOSTransaction_iCreatedBranchID int NULL
  _retPOSTransaction_iModifiedBranchID int NULL
  _retPOSTransaction_iCreatedAgentID int NULL
  _retPOSTransaction_iModifiedAgentID int NULL
  _retPOSTransaction_iChangeSetID int NULL
  _retPOSTransaction_Checksum binary(20) NULL
  cTenderCurrencyList nvarchar(max) NULL

## _retPriceOverrideReason - Retail Price Override Reason
Alias: Retail Price Override Reason | Freedom Name:  | Record Identifier: cPriceOverrideReasonCode
Notes: Retail Price Override Reason
PK: idPriceOverrideReason
Columns (13):
  idPriceOverrideReason int NOT NULL identity PK
  cPriceOverrideReasonCode varchar(10) NULL
  cPriceOverrideReasonDesc varchar(30) NULL
  bActive bit NOT NULL default (1)
  _retPriceOverrideReason_iBranchID int NULL
  _retPriceOverrideReason_dCreatedDate datetime NULL
  _retPriceOverrideReason_dModifiedDate datetime NULL
  _retPriceOverrideReason_iCreatedBranchID int NULL
  _retPriceOverrideReason_iModifiedBranchID int NULL
  _retPriceOverrideReason_iCreatedAgentID int NULL
  _retPriceOverrideReason_iModifiedAgentID int NULL
  _retPriceOverrideReason_iChangeSetID int NULL
  _retPriceOverrideReason_Checksum binary(20) NULL

## _retReturnReason - Retail Return Reason (RetailReturnReason)
Alias: Retail Return Reason | Freedom Name: RetailReturnReason | Record Identifier: cReturnReasonCode
Notes: Retail Return Reason
PK: idReturnReason
Columns (13):
  idReturnReason int NOT NULL identity PK
  cReturnReasonCode varchar(10) NULL
  cReturnReasonDesc varchar(30) NULL
  bActive bit NOT NULL default (1)
  _retReturnReason_iBranchID int NULL
  _retReturnReason_dCreatedDate datetime NULL
  _retReturnReason_dModifiedDate datetime NULL
  _retReturnReason_iCreatedBranchID int NULL
  _retReturnReason_iModifiedBranchID int NULL
  _retReturnReason_iCreatedAgentID int NULL
  _retReturnReason_iModifiedAgentID int NULL
  _retReturnReason_iChangeSetID int NULL
  _retReturnReason_Checksum binary(20) NULL

## _retTenderType
PK: idTenderType
Columns (30):
  idTenderType int NOT NULL identity PK
  cTenderTypeCode varchar(10) NULL
  cTenderTypeDesc varchar(30) NULL
  bActive bit NOT NULL default (1)
  iDisplayOrder int NULL
  bAllowOverTender bit NOT NULL default (0)
  bOpenDrawer bit NOT NULL default (0)
  fHouseLimit float NULL
  bRequireNarration bit NOT NULL default (0)
  iReceiptTrCodeID int NULL
  iRefundTrCodeID int NULL
  iDepositTrCodeID float NULL
  iTypeOfTender int NULL
  iCardDisplayFirst int NULL
  iCardDisplayLast int NULL
  bForceCardNumber bit NOT NULL default (0)
  bForceCardHolder bit NOT NULL default (0)
  cExpiryFormat varchar(20) NULL
  bForceExpiry bit NOT NULL default (0)
  bUsePinPad bit NULL
  bApplyDocketRounding bit NULL default (0)
  _retTenderType_iBranchID int NULL
  _retTenderType_dCreatedDate datetime NULL
  _retTenderType_dModifiedDate datetime NULL
  _retTenderType_iCreatedBranchID int NULL
  _retTenderType_iModifiedBranchID int NULL
  _retTenderType_iCreatedAgentID int NULL
  _retTenderType_iModifiedAgentID int NULL
  _retTenderType_iChangeSetID int NULL
  _retTenderType_Checksum binary(20) NULL

## _retTill
PK: idTill
Columns (74):
  idTill int NOT NULL identity PK
  cTillCode varchar(6) NULL
  bActive bit NOT NULL default (1)
  iCurrentAgentID int NULL
  bAutoNumPrependBranch bit NOT NULL default (1)
  iAutoNumInvNext int NULL
  iAutoNumInvPad int NULL
  cAutoNumInvPrefix varchar(20) NULL
  iAutoNumOrdNext int NULL
  iAutoNumOrdPad int NULL
  cAutoNumOrdPrefix varchar(20) NULL
  iAutoNumCrnNext int NULL
  iAutoNumCrnPad int NULL
  cAutoNumCrnPrefix varchar(20) NULL
  iAutoNumQuoNext int NULL
  iAutoNumQuoPad int NULL
  cAutoNumQuoPrefix varchar(20) NULL
  iWarehouseID int NULL
  iAutoNumCashUpNext int NULL
  iAutoNumCashUpPad int NULL
  cAutoNumCashUpPrefix varchar(20) NULL
  iAutoNumPettyCashNext int NULL
  iAutoNumPettyCashPad int NULL
  cAutoNumPettyCashPrefix varchar(20) NULL
  iAutoNumCashPickupNext int NULL
  iAutoNumCashPickupPad int NULL
  cAutoNumCashPickupPrefix varchar(20) NULL
  iAutoNumReceiptNext int NULL
  iAutoNumReceiptPad int NULL
  cAutoNumReceiptPrefix varchar(20) NULL
  iAutoNumRefundNext int NULL
  iAutoNumRefundPad int NULL
  cAutoNumRefundPrefix varchar(20) NULL
  iAutoNumLayByReceiptNext int NULL
  iAutoNumLayByReceiptPad int NULL
  cAutoNumLayByReceiptPrefix varchar(20) NULL
  iAutoNumLayByRefundNext int NULL
  iAutoNumLayByRefundPad int NULL
  cAutoNumLayByRefundPrefix varchar(20) NULL
  iAutoNumDelivNoteNext int NULL
  iAutoNumDelivNotePad int NULL
  cAutoNumDelivNotePrefix varchar(20) NULL
  iAutoNumLayByNext int NULL
  iAutoNumLayByPad int NULL
  cAutoNumLayByPrefix varchar(20) NULL
  iAutoNumKeepAsideNext int NULL
  iAutoNumKeepAsidePad int NULL
  iAutoNumKeepAsidePrefix varchar(20) NULL
  iDocketInputMode int NOT NULL default (0)
  iAutoNumCashDrawerHandoverNext int NULL
  iAutoNumCashDrawerHandoverPad int NULL
  cAutoNumCashDrawerHandoverPrefix varchar(20) NULL
  bUseOnScreenKeyboard bit NULL default (0)
  idPOSMenuSetup bigint NULL
  iAutoNumGIVNext int NULL
  iAutoNumGIVPad int NULL
  cAutoNumGIVPrefix varchar(20) NULL
  iAutoNumCGRNext int NULL
  iAutoNumCGRPad int NULL
  cAutoNumCGRPrefix varchar(20) NULL
  _retTill_iBranchID int NULL
  _retTill_dCreatedDate datetime NULL
  _retTill_dModifiedDate datetime NULL
  _retTill_iCreatedBranchID int NULL
  _retTill_iModifiedBranchID int NULL
  _retTill_iCreatedAgentID int NULL
  _retTill_iModifiedAgentID int NULL
  _retTill_iChangeSetID int NULL
  _retTill_Checksum binary(20) NULL
  iTillLoginScreen int NOT NULL default (0)
  bAutoLogout bit NOT NULL default (0)
  iAutoNumAttrQtyAdjustmentNext int NULL
  iAutoNumAttrQtyAdjustmentPad int NULL
  cAutoNumAttrQtyAdjustmentPrefix varchar(20) NULL

## _retTillSecurity - Retail Till Security
Alias: Retail Till Security | Freedom Name:  | Record Identifier: 
Notes: Retail Till Security
PK: idTillSecurity
Columns (12):
  idTillSecurity int NOT NULL identity PK
  iSystemFunction int NOT NULL
  iPermission int NULL
  _retTillSecurity_iBranchID int NULL
  _retTillSecurity_dCreatedDate datetime NULL
  _retTillSecurity_dModifiedDate datetime NULL
  _retTillSecurity_iCreatedBranchID int NULL
  _retTillSecurity_iModifiedBranchID int NULL
  _retTillSecurity_iCreatedAgentID int NULL
  _retTillSecurity_iModifiedAgentID int NULL
  _retTillSecurity_iChangeSetID int NULL
  _retTillSecurity_Checksum binary(20) NULL

## _retTillStationery - Retail Till Stationery
Alias: Retail Till Stationery | Freedom Name:  | Record Identifier: 
Notes: Retail Till Stationery
PK: idTillStationery
Columns (23):
  idTillStationery int NOT NULL identity PK
  iSloTypeID int NULL
  iSloSource int NULL
  iSloLayoutID int NULL
  iPrinterPaperSize int NULL
  iPrinterCopies int NULL
  iPrinterCollate int NULL
  iPrinterDuplex int NULL
  iEmailFormatIndex int NULL
  bZip bit NULL
  cEmailDefaultSubject varchar(255) NULL
  cEmailDefaultBody varchar(1024) NULL
  bEmailDifferentLayout bit NULL
  iEmailLayoutIndex int NULL
  _retTillStationery_iBranchID int NULL
  _retTillStationery_dCreatedDate datetime NULL
  _retTillStationery_dModifiedDate datetime NULL
  _retTillStationery_iCreatedBranchID int NULL
  _retTillStationery_iModifiedBranchID int NULL
  _retTillStationery_iCreatedAgentID int NULL
  _retTillStationery_iModifiedAgentID int NULL
  _retTillStationery_iChangeSetID int NULL
  _retTillStationery_Checksum binary(20) NULL

## _retTradingSession
PK: idTradingSession
Columns (20):
  idTradingSession int NOT NULL identity PK
  iSessionStatus int NULL
  dTradingDate datetime NULL
  cSessionDescription varchar(50) NULL
  dStartTime datetime NULL
  iStartAgentID int NULL
  dEndTime datetime NULL
  iEndAgentID int NULL
  iFinaliseAgentID int NULL
  iExpectedDuration int NULL
  bDisableTradingOnExpiry bit NOT NULL default (0)
  _retTradingSession_iBranchID int NULL
  _retTradingSession_dCreatedDate datetime NULL
  _retTradingSession_dModifiedDate datetime NULL
  _retTradingSession_iCreatedBranchID int NULL
  _retTradingSession_iModifiedBranchID int NULL
  _retTradingSession_iCreatedAgentID int NULL
  _retTradingSession_iModifiedAgentID int NULL
  _retTradingSession_iChangeSetID int NULL
  _retTradingSession_Checksum binary(20) NULL

## _retVariableBarcode
PK: idVariableBarcode
Columns (20):
  idVariableBarcode int NOT NULL identity PK
  cCode varchar(10) NULL
  cDesc varchar(30) NULL
  cPrefix varchar(2) NULL
  iFullLength int NULL
  iItemStart int NULL
  iItemLength int NULL
  iValueStart int NULL
  iValueLength int NULL
  iValueDecimals int NULL
  _retVariableBarcode_iBranchID int NULL
  _retVariableBarcode_dCreatedDate datetime NULL
  _retVariableBarcode_dModifiedDate datetime NULL
  _retVariableBarcode_iCreatedBranchID int NULL
  _retVariableBarcode_iModifiedBranchID int NULL
  _retVariableBarcode_iCreatedAgentID int NULL
  _retVariableBarcode_iModifiedAgentID int NULL
  _retVariableBarcode_iChangeSetID int NULL
  _retVariableBarcode_Checksum binary(20) NULL
  iValueType int NOT NULL default (0)

## _retVariableBarcodeAGroups
PK: idVariableBarcodeAGroups
Columns (12):
  idVariableBarcodeAGroups int NOT NULL identity PK
  iVariableBarcodeID int NOT NULL
  iAttributeGroupID int NULL
  _retVariableBarcodeAGroups_iBranchID int NULL
  _retVariableBarcodeAGroups_dCreatedDate datetime NULL
  _retVariableBarcodeAGroups_dModifiedDate datetime NULL
  _retVariableBarcodeAGroups_iCreatedBranchID int NULL
  _retVariableBarcodeAGroups_iModifiedBranchID int NULL
  _retVariableBarcodeAGroups_iCreatedAgentID int NULL
  _retVariableBarcodeAGroups_iModifiedAgentID int NULL
  _retVariableBarcodeAGroups_iChangeSetID int NULL
  _retVariableBarcodeAGroups_Checksum binary(20) NULL

## _retVariableBarcodeATypes
PK: idVariableBarcodeATypes
Columns (14):
  idVariableBarcodeATypes int NOT NULL identity PK
  iVariableBarcodeID int NOT NULL
  iAttributeTypeID int NULL
  iAttributeStart int NULL
  iAttributeLength int NULL
  _retVariableBarcodeATypes_iBranchID int NULL
  _retVariableBarcodeATypes_dCreatedDate datetime NULL
  _retVariableBarcodeATypes_dModifiedDate datetime NULL
  _retVariableBarcodeATypes_iCreatedBranchID int NULL
  _retVariableBarcodeATypes_iModifiedBranchID int NULL
  _retVariableBarcodeATypes_iCreatedAgentID int NULL
  _retVariableBarcodeATypes_iModifiedAgentID int NULL
  _retVariableBarcodeATypes_iChangeSetID int NULL
  _retVariableBarcodeATypes_Checksum binary(20) NULL
