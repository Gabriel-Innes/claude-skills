# Sage 200 Evolution table dictionary - Evolution extended

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _etblAccBlnc - General Ledger Account Balances (GeneralLedgerAccountBalance)
Alias: General Ledger Account Balances | Freedom Name: GeneralLedgerAccountBalance | Record Identifier: 
Notes: General Ledger Account Balances. Stores general ledger account balances Per Period
PK: idAccBlnc
Columns (19):
  idAccBlnc int NOT NULL identity PK
  iAccBlncAccountID int NOT NULL
  iAccBlncProjectID int NOT NULL
  iAccBlncPeriodID int NOT NULL
  iAccBlncTxBranchID int NOT NULL
  iAccBlncAccountType int NOT NULL
  fActualDebit float NULL
  fActualCredit float NULL
  _etblAccBlnc_iBranchID int NULL
  _etblAccBlnc_dCreatedDate datetime NULL
  _etblAccBlnc_dModifiedDate datetime NULL
  _etblAccBlnc_iCreatedBranchID int NULL
  _etblAccBlnc_iModifiedBranchID int NULL
  _etblAccBlnc_iCreatedAgentID int NULL
  _etblAccBlnc_iModifiedAgentID int NULL
  _etblAccBlnc_iChangeSetID int NULL
  _etblAccBlnc_Checksum binary(20) NULL
  iAccBlncCurrencyID int NOT NULL default (0)
  xAttribute xml NULL

## _etblAccPrev - Previous Account Balances (AccountPreviousBalance)
Alias: Previous Account Balances | Freedom Name: AccountPreviousBalance | Record Identifier: 
Notes: Previous Account Balances for Purged Years
PK: idAccPrev
Columns (19):
  idAccPrev int NOT NULL identity PK
  iAccPrevAccountID int NOT NULL
  iAccPrevProjectID int NOT NULL
  iAccPrevPeriodID int NOT NULL
  iAccPrevTxBranchID int NOT NULL
  fBFDebit float NULL
  fBFCredit float NULL
  iAccPrevAccountType int NOT NULL default (0)
  _etblAccPrev_iBranchID int NULL
  _etblAccPrev_dCreatedDate datetime NULL
  _etblAccPrev_dModifiedDate datetime NULL
  _etblAccPrev_iCreatedBranchID int NULL
  _etblAccPrev_iModifiedBranchID int NULL
  _etblAccPrev_iCreatedAgentID int NULL
  _etblAccPrev_iModifiedAgentID int NULL
  _etblAccPrev_iChangeSetID int NULL
  _etblAccPrev_Checksum binary(20) NULL
  iAccPrevCurrencyID int NOT NULL default (0)
  xAttribute xml NULL

## _etblAddInRegister - Add In Register
Alias: Add In Register | Freedom Name:  | Record Identifier: 
Notes: Third Party Applications. Add in Register
PK: idAddIn
Columns (19):
  idAddIn int NOT NULL identity PK
  cAddInGuid uniqueidentifier NOT NULL
  cName nvarchar(200) NOT NULL
  cPublisher nvarchar(200) NOT NULL
  cPublisherContact nvarchar(15) NOT NULL
  cPublisherTel nvarchar(15) NOT NULL
  cPublisherHomePage nvarchar(200) NOT NULL
  cPublisherEmail nvarchar(200) NOT NULL
  bAddInEnabled bit NOT NULL
  fAddInVersion float NULL
  _etblAddinRegister_iBranchID int NULL
  _etblAddinRegister_dCreatedDate datetime NULL
  _etblAddinRegister_dModifiedDate datetime NULL
  _etblAddinRegister_iCreatedBranchID int NULL
  _etblAddinRegister_iModifiedBranchID int NULL
  _etblAddinRegister_iCreatedAgentID int NULL
  _etblAddinRegister_iModifiedAgentID int NULL
  _etblAddinRegister_iChangeSetID int NULL
  _etblAddinRegister_Checksum binary(20) NULL

## _etblAdditionalCharges - Additional Charges
Alias: Additional Charges | Freedom Name:  | Record Identifier: 
Notes: AR Additional Charges
PK: idAdditionalCharge
Columns (19):
  idAdditionalCharge int NOT NULL identity PK
  cCode varchar(20) NULL
  cDescription varchar(120) NULL
  bActive bit NOT NULL
  bIsPercent bit NOT NULL default (0)
  bInclusive bit NOT NULL
  fMinAmt float NULL
  fMinPct float NULL
  iTaxTypeID int NULL
  iAccountLink int NULL
  _etblAdditionalCharges_iBranchID int NULL
  _etblAdditionalCharges_dCreatedDate datetime NULL
  _etblAdditionalCharges_dModifiedDate datetime NULL
  _etblAdditionalCharges_iCreatedBranchID int NULL
  _etblAdditionalCharges_iModifiedBranchID int NULL
  _etblAdditionalCharges_iCreatedAgentID int NULL
  _etblAdditionalCharges_iModifiedAgentID int NULL
  _etblAdditionalCharges_iChangeSetID int NULL
  _etblAdditionalCharges_Checksum binary(20) NULL

## _etblAdditionalChargeSettings - Additional Charge Settings
Alias: Additional Charge Settings | Freedom Name:  | Record Identifier: 
Notes: Additional Charge Settings
PK: idAdditionalChargeSettings
Columns (16):
  idAdditionalChargeSettings int NOT NULL identity PK
  iAdditionalChargeID int NULL
  iSettingTypeID int NULL
  bDefault bit NOT NULL default (0)
  bForce bit NOT NULL default (0)
  bInvoiceCharge bit NOT NULL default (0)
  bReturnCharge bit NOT NULL default (0)
  _etblAdditionalChargeSettings_iBranchID int NULL
  _etblAdditionalChargeSettings_dCreatedDate datetime NULL
  _etblAdditionalChargeSettings_dModifiedDate datetime NULL
  _etblAdditionalChargeSettings_iCreatedBranchID int NULL
  _etblAdditionalChargeSettings_iModifiedBranchID int NULL
  _etblAdditionalChargeSettings_iCreatedAgentID int NULL
  _etblAdditionalChargeSettings_iModifiedAgentID int NULL
  _etblAdditionalChargeSettings_iChangeSetID int NULL
  _etblAdditionalChargeSettings_Checksum binary(20) NULL

## _etblAdditionalInvoiceCharges - Additional Invoice Charges (AdditionalInvoiceCharges)
Alias: Additional Invoice Charges | Freedom Name: AdditionalInvoiceCharges | Record Identifier: 
Notes: Additional Invoice Charges
PK: idAdditionalInvoiceCharges
Columns (29):
  idAdditionalInvoiceCharges int NOT NULL identity PK
  iAdditionalChargeID int NOT NULL
  iInvNumID bigint NULL
  iGLAccountID int NOT NULL
  bInclusive bit NOT NULL
  fPercentage float NULL
  fAdditionalAmt float NULL
  fAmountExcl float NULL
  fAmountIncl float NULL
  fAdditionalForeignAmt float NOT NULL default (0)
  fForeignAmountExcl float NOT NULL default (0)
  fForeignAmountIncl float NOT NULL default (0)
  iProjectID int NULL
  iRepID int NULL
  iTaxTypeID int NULL
  iCurrencyID int NOT NULL default (0)
  fCurrencyRate float NOT NULL default (0)
  idAdditionalChgSettings int NOT NULL default (0)
  bIsInvoiceCharge bit NOT NULL default (0)
  bIsReturnCharge bit NOT NULL default (0)
  _etblAdditionalInvoiceCharges_iBranchID int NULL
  _etblAdditionalInvoiceCharges_dCreatedDate datetime NULL
  _etblAdditionalInvoiceCharges_dModifiedDate datetime NULL
  _etblAdditionalInvoiceCharges_iCreatedBranchID int NULL
  _etblAdditionalInvoiceCharges_iModifiedBranchID int NULL
  _etblAdditionalInvoiceCharges_iCreatedAgentID int NULL
  _etblAdditionalInvoiceCharges_iModifiedAgentID int NULL
  _etblAdditionalInvoiceCharges_iChangeSetID int NULL
  _etblAdditionalInvoiceCharges_Checksum binary(20) NULL

## _etblAgentDocProfiles - Agent Document Profiles (AgentDocumentProfile)
Alias: Agent Document Profiles | Freedom Name: AgentDocumentProfile | Record Identifier: 
Notes: Agent Document Profiles
PK: idAgentDocProfiles
Columns (13):
  idAgentDocProfiles int NOT NULL identity PK
  iAgentID int NOT NULL
  iDocProfileID int NOT NULL
  bActiveDocProfile bit NOT NULL default (0)
  _etblAgentDocProfiles_iBranchID int NULL
  _etblAgentDocProfiles_dCreatedDate datetime NULL
  _etblAgentDocProfiles_dModifiedDate datetime NULL
  _etblAgentDocProfiles_iCreatedBranchID int NULL
  _etblAgentDocProfiles_iModifiedBranchID int NULL
  _etblAgentDocProfiles_iCreatedAgentID int NULL
  _etblAgentDocProfiles_iModifiedAgentID int NULL
  _etblAgentDocProfiles_iChangeSetID int NULL
  _etblAgentDocProfiles_Checksum binary(20) NULL

## _etblAgentPwdHistory - Agent Password History
Alias: Agent Password History | Freedom Name:  | Record Identifier: 
Notes: Agent Password History
PK: iAgentID+cPassword
Columns (12):
  iAgentID int NOT NULL PK
  cPassword varchar(24) NOT NULL PK
  dPwdLastUsed smalldatetime NULL
  _etblAgentPwdHistory_iBranchID int NULL
  _etblAgentPwdHistory_dCreatedDate datetime NULL
  _etblAgentPwdHistory_dModifiedDate datetime NULL
  _etblAgentPwdHistory_iCreatedBranchID int NULL
  _etblAgentPwdHistory_iModifiedBranchID int NULL
  _etblAgentPwdHistory_iCreatedAgentID int NULL
  _etblAgentPwdHistory_iModifiedAgentID int NULL
  _etblAgentPwdHistory_iChangeSetID int NULL
  _etblAgentPwdHistory_Checksum binary(20) NULL

## _etblAllocsDCLinkRangeTemp - Allocs DC Link Range Temp
Alias: Allocs DC Link Range Temp | Freedom Name:  | Record Identifier: 
Notes: Allocs DC Link Range Temp
PK: DCLink
Columns (1):
  DCLink int NOT NULL PK

## _etblAllocsTemp - AllocsTemp
Alias: AllocsTemp | Freedom Name:  | Record Identifier: 
Notes: AllocsTemp
PK: idAllocsTemp
Columns (9):
  idAllocsTemp int NOT NULL identity PK
  iAccountID int NULL
  iFromRecID bigint NULL
  iToRecID bigint NULL
  fAmount float NULL
  fAmountForeign float NULL
  dFromRecDate datetime NULL
  dToRecDate datetime NULL
  iPLRecID bigint NULL

## _etblAllocTemp - AllocTemp
Alias: AllocTemp | Freedom Name:  | Record Identifier: 
Notes: AllocTemp
PK: none
Columns (19):
  TmpAutoIdx bigint NULL
  TmpTxTerm int NULL
  TmpAllocID bigint NULL
  TmpAllocAmt float NULL
  TmpAllocDate datetime NULL
  TmpTotCredits float NULL
  TmpTotDebits float NULL
  TmpAllUACredits float NULL
  TmpAllUADebits float NULL
  TmpDCLink int NULL
  TmpPas_Cursor int NULL
  TmpTranModule varchar(2) NULL
  TmpLinkedID bigint NULL
  TmpLineID int NOT NULL identity
  TmpRepID int NULL
  TmpStockAllocAmtExc float NULL
  TmpStockCost float NULL
  iTxBranchID int NULL
  TmpAPRBatchID int NOT NULL default (0)

## _etblAPShareholderLinks - AP Shareholder Links
Alias: AP Shareholder Links | Freedom Name:  | Record Identifier: 
Notes: Accounts payable Shareholder links
PK: idAPShareholderLinks
Columns (15):
  idAPShareholderLinks int NOT NULL identity PK
  iAPShareholderID int NOT NULL
  iSupplierID int NOT NULL
  fPercentage float NOT NULL
  cPositionHeld varchar(50) NOT NULL
  bDirector bit NULL default (0)
  _etblAPShareholderLinks_iBranchID int NULL
  _etblAPShareholderLinks_dCreatedDate datetime NULL
  _etblAPShareholderLinks_dModifiedDate datetime NULL
  _etblAPShareholderLinks_iCreatedBranchID int NULL
  _etblAPShareholderLinks_iModifiedBranchID int NULL
  _etblAPShareholderLinks_iCreatedAgentID int NULL
  _etblAPShareholderLinks_iModifiedAgentID int NULL
  _etblAPShareholderLinks_iChangeSetID int NULL
  _etblAPShareholderLinks_Checksum binary(20) NULL

## _etblAPShareholders - AP Shareholders
Alias: AP Shareholders | Freedom Name:  | Record Identifier: 
Notes: AccountsPayable Shareholders
PK: idAPShareholders
Columns (20):
  idAPShareholders int NOT NULL identity PK
  cName varchar(50) NOT NULL
  cIDNumber varchar(20) NOT NULL
  cCitizenship varchar(50) NULL
  dCitizenshipAquired datetime NULL
  cRace varchar(30) NULL
  cGender varchar(1) NULL
  bDisabled bit NULL default (0)
  bYouth bit NULL default (0)
  cGovernmentEmployeeNumber varchar(50) NULL
  cTaxNumber varchar(50) NULL
  _etblAPShareholders_iBranchID int NULL
  _etblAPShareholders_dCreatedDate datetime NULL
  _etblAPShareholders_dModifiedDate datetime NULL
  _etblAPShareholders_iCreatedBranchID int NULL
  _etblAPShareholders_iModifiedBranchID int NULL
  _etblAPShareholders_iCreatedAgentID int NULL
  _etblAPShareholders_iModifiedAgentID int NULL
  _etblAPShareholders_iChangeSetID int NULL
  _etblAPShareholders_Checksum binary(20) NULL

## _etblARAPBatchContraSplit - AR AP Batch Contra Split
Alias: AR AP Batch Contra Split | Freedom Name:  | Record Identifier: 
Notes: AR AP Batch Contra Split
PK: idARAPBatchContraSplit
Columns (25):
  idARAPBatchContraSplit int NOT NULL identity PK
  iBatchID int NOT NULL
  iLinePermID int NOT NULL
  iGLAccountID int NOT NULL
  cDescription varchar(40) NULL
  fAmount float NULL
  fAmountForeign float NULL
  iProjectID int NULL
  iTaxTypeID int NOT NULL default (0)
  fAmountIncl float NULL default (0)
  fAmountInclForeign float NULL default (0)
  iTaxAccountID int NULL
  _etblARAPBatchContraSplit_iBranchID int NULL
  _etblARAPBatchContraSplit_dCreatedDate datetime NULL
  _etblARAPBatchContraSplit_dModifiedDate datetime NULL
  _etblARAPBatchContraSplit_iCreatedBranchID int NULL
  _etblARAPBatchContraSplit_iModifiedBranchID int NULL
  _etblARAPBatchContraSplit_iCreatedAgentID int NULL
  _etblARAPBatchContraSplit_iModifiedAgentID int NULL
  _etblARAPBatchContraSplit_iChangeSetID int NULL
  _etblARAPBatchContraSplit_Checksum binary(20) NULL
  cTaxCompanyName varchar(150) NULL
  cTaxCompanyRegistration varchar(50) NULL
  cTaxRegistration varchar(50) NULL
  iMajorIndustryCodeID int NULL default (0)

## _etblARAPBatchContraSplitHistory - AR AP Batch Contra Split History
Alias: AR AP Batch Contra Split History | Freedom Name:  | Record Identifier: 
Notes: AR AP Batch Contra Split History
PK: idARAPBatchContraSplitHistory
Columns (26):
  idARAPBatchContraSplitHistory int NOT NULL identity PK
  iBatchHistoryID int NOT NULL
  iBatchID int NOT NULL
  iLinePermID int NOT NULL
  iGLAccountID int NOT NULL
  cDescription varchar(40) NULL
  fAmount float NULL
  fAmountForeign float NULL
  iProjectID int NULL
  iTaxTypeID int NOT NULL default (0)
  fAmountIncl float NOT NULL default (0)
  fAmountInclForeign float NULL default (0)
  iTaxAccountID int NULL
  _etblARAPBatchContraSplitHistory_iBranchID int NULL
  _etblARAPBatchContraSplitHistory_dCreatedDate datetime NULL
  _etblARAPBatchContraSplitHistory_dModifiedDate datetime NULL
  _etblARAPBatchContraSplitHistory_iCreatedBranchID int NULL
  _etblARAPBatchContraSplitHistory_iModifiedBranchID int NULL
  _etblARAPBatchContraSplitHistory_iCreatedAgentID int NULL
  _etblARAPBatchContraSplitHistory_iModifiedAgentID int NULL
  _etblARAPBatchContraSplitHistory_iChangeSetID int NULL
  _etblARAPBatchContraSplitHistory_Checksum binary(20) NULL
  cTaxCompanyName varchar(150) NULL
  cTaxCompanyRegistration varchar(50) NULL
  cTaxRegistration varchar(50) NULL
  iMajorIndustryCodeID int NULL default (0)

## _etblARAPBatchDefaults - AR AP Batch Defaults
Alias: AR AP Batch Defaults | Freedom Name:  | Record Identifier: 
Notes: AR AP Batch Defaults
PK: idARAPBatchDefaults
Columns (17):
  idARAPBatchDefaults int NOT NULL identity PK
  iDCModule int NOT NULL
  bAutoNumbers bit NOT NULL default (0)
  iAutoNumPadLength int NULL
  cAutoNumPrefix varchar(25) NULL
  bAutoRefNumbers bit NOT NULL default (0)
  iAutoRefNumPadLength int NULL
  cAutoRefNumPrefix varchar(25) NULL
  _etblARAPBatchDefaults_iBranchID int NULL
  _etblARAPBatchDefaults_dCreatedDate datetime NULL
  _etblARAPBatchDefaults_dModifiedDate datetime NULL
  _etblARAPBatchDefaults_iCreatedBranchID int NULL
  _etblARAPBatchDefaults_iModifiedBranchID int NULL
  _etblARAPBatchDefaults_iCreatedAgentID int NULL
  _etblARAPBatchDefaults_iModifiedAgentID int NULL
  _etblARAPBatchDefaults_iChangeSetID int NULL
  _etblARAPBatchDefaults_Checksum binary(20) NULL

## _etblARAPBatches - AR AP Batch
Alias: AR AP Batch | Freedom Name:  | Record Identifier: 
Notes: AR AP Batch
PK: idARAPBatches
Columns (53):
  idARAPBatches int NOT NULL identity PK
  iDCModule int NOT NULL
  cBatchNo varchar(50) NULL
  cBatchDesc varchar(50) NOT NULL
  cBatchRef varchar(50) NULL
  bClearAfterPost bit NOT NULL default (0)
  bAllowDupRef bit NOT NULL default (0)
  iCurrencyID int NULL
  bCurrencySingle bit NOT NULL default (0)
  iNewLineDateOpt int NULL
  dNewLineDateDef datetime NULL
  iNewLineRefOpt int NULL
  cNewLineRefDef varchar(20) NULL
  bNewLineRefInc bit NOT NULL default (0)
  iNewLineDescOpt int NULL
  cNewLineDescDef varchar(40) NULL
  bNewLineDescInc bit NOT NULL default (0)
  iNewLineTrCodeOpt int NULL
  iNewLineTrCodeDefID int NULL
  bNewLineTrCodeForce bit NOT NULL default (0)
  cOriginalBatchNo varchar(50) NULL
  cOriginalbatchDesc varchar(50) NULL
  iAgentCreatorID int NULL
  fValidateDebits float NULL
  fValidateCredits float NULL
  bShowGLContra bit NOT NULL default (0)
  bEditGLContra bit NOT NULL default (0)
  bAllowGLContraSplit bit NOT NULL default (0)
  bEnterTaxOnGlContraSplit bit NOT NULL default (0)
  bIncludeLinkedAccounts bit NOT NULL default (0)
  bEnterExclOnGlContraSplit bit NOT NULL default (1)
  bValidateOverTerms bit NOT NULL default (1)
  bValidateOverLimit bit NOT NULL default (1)
  bInterBranchBatch bit NOT NULL default (0)
  iBranchLoanAccountID int NULL
  bModuleAR bit NOT NULL default (1)
  bModuleAP bit NOT NULL default (1)
  bModuleGL bit NOT NULL default (1)
  iInputTaxID int NULL
  iInputTaxAccID int NULL
  iOutputTaxID int NULL
  iOutputTaxAccID int NULL
  bCalcTax bit NOT NULL default (0)
  iDefaultModule int NULL
  _etblARAPBatches_iBranchID int NULL
  _etblARAPBatches_dCreatedDate datetime NULL
  _etblARAPBatches_dModifiedDate datetime NULL
  _etblARAPBatches_iCreatedBranchID int NULL
  _etblARAPBatches_iModifiedBranchID int NULL
  _etblARAPBatches_iCreatedAgentID int NULL
  _etblARAPBatches_iModifiedAgentID int NULL
  _etblARAPBatches_iChangeSetID int NULL
  _etblARAPBatches_Checksum binary(20) NULL

## _etblARAPBatchHistory
PK: idARAPBatchHistory
Columns (18):
  idARAPBatchHistory int NOT NULL identity PK
  iBatchID int NOT NULL
  dActionDate datetime NOT NULL
  iActionType int NOT NULL
  iAgentID int NOT NULL
  cBatchNo varchar(50) NULL
  cBatchDesc varchar(40) NOT NULL
  cBatchReference varchar(50) NULL
  iLineCount int NOT NULL
  _etblARAPBatchHistory_iBranchID int NULL
  _etblARAPBatchHistory_dCreatedDate datetime NULL
  _etblARAPBatchHistory_dModifiedDate datetime NULL
  _etblARAPBatchHistory_iCreatedBranchID int NULL
  _etblARAPBatchHistory_iModifiedBranchID int NULL
  _etblARAPBatchHistory_iCreatedAgentID int NULL
  _etblARAPBatchHistory_iModifiedAgentID int NULL
  _etblARAPBatchHistory_iChangeSetID int NULL
  _etblARAPBatchHistory_Checksum binary(20) NULL

## _etblARAPBatchHistoryLines - AR AP Batch History Line
Alias: AR AP Batch History Line | Freedom Name:  | Record Identifier: 
Notes: AR AP Batch History Line
PK: idARAPBatchHistoryLines
Columns (49):
  idARAPBatchHistoryLines int NOT NULL identity PK
  iBatchHistoryID int NULL
  iBatchID int NOT NULL
  idLinePermanent int NULL
  dTxDate datetime NULL
  iAccountID int NULL
  iAccountCurrencyID int NULL
  iTrCodeID int NULL
  iGLContraID int NULL
  bPostDated bit NOT NULL default (0)
  cReference varchar(50) NULL
  cDescription varchar(40) NULL
  cOrderNumber varchar(20) NULL
  fAmountExcl float NULL
  iTaxTypeID int NULL
  fAmountIncl float NULL
  fExchangeRate float NULL
  fAmountExclForeign float NULL
  fAmountInclForeign float NULL
  fAccountExchangeRate float NULL
  fAccountForeignAmountExcl float NULL
  fAccountForeignAmountIncl float NULL
  iDiscGLContraID int NULL
  fDiscPercent float NULL
  fDiscAmountExcl float NULL
  iDiscTaxTypeID int NULL
  fDiscAmountIncl float NULL
  fDiscAmountExclForeign float NULL
  fDiscAmountInclForeign float NULL
  fAccountForeignDiscAmountExcl float NULL
  fAccountForeignDiscAmountIncl float NULL
  iProjectID int NULL
  iSalesRepID int NULL
  iBatchSettlementTermsID int NOT NULL default (0)
  iModule int NULL
  iTaxAccountID int NULL
  bIsDebit bit NOT NULL default (0)
  _etblARAPBatchHistoryLines_iBranchID int NULL
  _etblARAPBatchHistoryLines_dCreatedDate datetime NULL
  _etblARAPBatchHistoryLines_dModifiedDate datetime NULL
  _etblARAPBatchHistoryLines_iCreatedBranchID int NULL
  _etblARAPBatchHistoryLines_iModifiedBranchID int NULL
  _etblARAPBatchHistoryLines_iCreatedAgentID int NULL
  _etblARAPBatchHistoryLines_iModifiedAgentID int NULL
  _etblARAPBatchHistoryLines_iChangeSetID int NULL
  _etblARAPBatchHistoryLines_Checksum binary(20) NULL
  cTaxCompanyName varchar(150) NULL
  cTaxCompanyRegistration varchar(50) NULL
  cTaxRegistration varchar(50) NULL

## _etblARAPBatchLines
PK: idARAPBatchLines
Columns (53):
  idARAPBatchLines int NOT NULL identity PK
  iBatchID int NOT NULL
  idLinePermanent int NULL
  dTxDate datetime NULL
  iAccountID int NULL
  iAccountCurrencyID int NULL
  iTrCodeID int NULL
  iGLContraID int NULL
  bPostDated bit NOT NULL default (0)
  cReference varchar(50) NULL
  cDescription varchar(100) NULL
  cOrderNumber varchar(20) NULL
  fAmountExcl float NULL
  iTaxTypeID int NULL
  fAmountIncl float NULL
  fExchangeRate float NULL
  fAmountExclForeign float NULL
  fAmountInclForeign float NULL
  fAccountExchangeRate float NULL
  fAccountForeignAmountExcl float NULL
  fAccountForeignAmountIncl float NULL
  iDiscGLContraID int NULL
  fDiscPercent float NULL
  fDiscAmountExcl float NULL
  iDiscTaxTypeID int NULL
  fDiscAmountIncl float NULL
  fDiscAmountExclForeign float NULL
  fDiscAmountInclForeign float NULL
  fAccountForeignDiscAmountExcl float NULL
  fAccountForeignDiscAmountIncl float NULL
  iProjectID int NULL
  iSalesRepID int NULL
  iBatchSettlementTermsID int NOT NULL default (0)
  iModule int NULL
  iTaxAccountID int NULL
  bIsDebit bit NOT NULL default (0)
  iMBPropertyID int NULL
  iMBPortionID int NULL
  iMBServiceID int NULL
  iMBPropertyPortionServiceID int NULL
  _etblARAPBatchLines_iBranchID int NULL
  _etblARAPBatchLines_dCreatedDate datetime NULL
  _etblARAPBatchLines_dModifiedDate datetime NULL
  _etblARAPBatchLines_iCreatedBranchID int NULL
  _etblARAPBatchLines_iModifiedBranchID int NULL
  _etblARAPBatchLines_iCreatedAgentID int NULL
  _etblARAPBatchLines_iModifiedAgentID int NULL
  _etblARAPBatchLines_iChangeSetID int NULL
  _etblARAPBatchLines_Checksum binary(20) NULL
  cTaxCompanyName varchar(150) NULL
  cTaxCompanyRegistration varchar(50) NULL
  cTaxRegistration varchar(50) NULL
  iMajorIndustryCodeID int NULL default (0)

## _etblARAPBatchSettDiscLines - AR AP Batch Settlement Discount Line
Alias: AR AP Batch Settlement Discount Line | Freedom Name:  | Record Identifier: 
Notes: AR AP Batch Settlement Discount Line
PK: idARAPBatchSettDiscLines
Columns (20):
  idARAPBatchSettDiscLines int NOT NULL identity PK
  iBatchId int NOT NULL
  iLinePermId int NOT NULL
  iPostARAPId bigint NOT NULL
  fAmount float NULL
  fAmountForeign float NULL
  fDiscPerc float NULL
  fDiscAmount float NULL
  fDiscAmountForeign float NULL
  fFCAccAmount float NULL
  fFCAccDiscAmount float NULL
  _etblARAPBatchSettDiscLines_iBranchID int NULL
  _etblARAPBatchSettDiscLines_dCreatedDate datetime NULL
  _etblARAPBatchSettDiscLines_dModifiedDate datetime NULL
  _etblARAPBatchSettDiscLines_iCreatedBranchID int NULL
  _etblARAPBatchSettDiscLines_iModifiedBranchID int NULL
  _etblARAPBatchSettDiscLines_iCreatedAgentID int NULL
  _etblARAPBatchSettDiscLines_iModifiedAgentID int NULL
  _etblARAPBatchSettDiscLines_iChangeSetID int NULL
  _etblARAPBatchSettDiscLines_Checksum binary(20) NULL

## _etblARStatementRun - AR Statement Run
Alias: AR Statement Run | Freedom Name:  | Record Identifier: 
Notes: AR Statement Run
PK: idStatementRun
Columns (13):
  idStatementRun int NOT NULL identity PK
  cReference varchar(255) NULL
  dRunGenerated datetime NOT NULL
  iAgentID int NOT NULL
  _etblARStatementRun_iBranchID int NULL
  _etblARStatementRun_dCreatedDate datetime NULL
  _etblARStatementRun_dModifiedDate datetime NULL
  _etblARStatementRun_iCreatedBranchID int NULL
  _etblARStatementRun_iModifiedBranchID int NULL
  _etblARStatementRun_iCreatedAgentID int NULL
  _etblARStatementRun_iModifiedAgentID int NULL
  _etblARStatementRun_iChangeSetID int NULL
  _etblARStatementRun_Checksum binary(20) NULL

## _etblARStatementRunOptions - AR Statement Run Options
Alias: AR Statement Run Options | Freedom Name:  | Record Identifier: 
PK: idStatementRunOptions
Columns (68):
  idStatementRunOptions int NOT NULL identity PK
  iStatementRunID int NOT NULL
  dFromDate datetime NULL
  dToDate datetime NULL
  bAgePerService bit NOT NULL default (0)
  bDebits bit NOT NULL default (0)
  bFullyAllocDebits bit NOT NULL default (0)
  bCreditAllocs bit NOT NULL default (0)
  bCredits bit NOT NULL default (0)
  bFullyAllocCredits bit NOT NULL default (0)
  bDebitAllocs bit NOT NULL default (0)
  bExclZeroBal bit NOT NULL default (0)
  bPrintZeroCurrMonth bit NOT NULL default (0)
  bExclBalLessAmt bit NOT NULL default (0)
  fExclBalLessAmt float NULL
  bExclNegBal bit NOT NULL default (0)
  bShowGrandTotals bit NOT NULL default (0)
  bShowZeroTx bit NOT NULL default (0)
  bPrintOpenItemBBF bit NOT NULL default (0)
  bGroupLinkedAccTx bit NOT NULL default (0)
  bPrintForCurrFor bit NOT NULL default (0)
  bPrintUnallocLast bit NOT NULL default (0)
  bPrintFullAmount bit NOT NULL default (0)
  bPrintPDCheques bit NOT NULL default (0)
  bPrintDocDetail bit NOT NULL default (0)
  cFromCustomer varchar(255) NULL
  cToCustomer varchar(255) NULL
  cGroups varchar(255) NULL
  cAreas varchar(255) NULL
  cSalesReps varchar(255) NULL
  cAgeingPeriods varchar(255) NULL
  cForCurrency varchar(255) NULL
  cSort varchar(255) NULL
  cSecondarySort varchar(255) NULL
  cPrintTotals varchar(255) NULL
  cAgeAllBy varchar(255) NULL
  bInclEmailCustPreview bit NOT NULL default (0)
  bInclEmailCustPrint bit NOT NULL default (0)
  bEmailIndiv bit NOT NULL default (0)
  bPrintOnHold bit NOT NULL default (0)
  bPrintCash bit NOT NULL default (0)
  cAge1Message1 varchar(1) NULL
  cAge1Message2 varchar(1) NULL
  cAge2Message1 varchar(1) NULL
  cAge2Message2 varchar(1) NULL
  cAge3Message1 varchar(1) NULL
  cAge3Message2 varchar(1) NULL
  cAge4Message1 varchar(1) NULL
  cAge4Message2 varchar(1) NULL
  cAge5Message1 varchar(1) NULL
  cAge5Message2 varchar(1) NULL
  cAge6Message1 varchar(1) NULL
  cAge6Message2 varchar(1) NULL
  cAge7Message1 varchar(1) NULL
  cAge7Message2 varchar(1) NULL
  cCustSortPrimary varchar(255) NULL
  cCustSortSecondary varchar(255) NULL
  cDefaultMessage varchar(255) NULL
  cDefaultSubject varchar(255) NULL
  _etblARStatementRunOptions_iBranchID int NULL
  _etblARStatementRunOptions_dCreatedDate datetime NULL
  _etblARStatementRunOptions_dModifiedDate datetime NULL
  _etblARStatementRunOptions_iCreatedBranchID int NULL
  _etblARStatementRunOptions_iModifiedBranchID int NULL
  _etblARStatementRunOptions_iCreatedAgentID int NULL
  _etblARStatementRunOptions_iModifiedAgentID int NULL
  _etblARStatementRunOptions_iChangeSetID int NULL
  _etblARStatementRunOptions_Checksum binary(20) NULL

## _etblARStatements
PK: idStatements
Columns (13):
  idStatements int NOT NULL identity PK
  iStatementRunID int NOT NULL
  iClientID int NOT NULL
  nPDFDocument image NULL
  _etblARStatements_iBranchID int NULL
  _etblARStatements_dCreatedDate datetime NULL
  _etblARStatements_dModifiedDate datetime NULL
  _etblARStatements_iCreatedBranchID int NULL
  _etblARStatements_iModifiedBranchID int NULL
  _etblARStatements_iCreatedAgentID int NULL
  _etblARStatements_iModifiedAgentID int NULL
  _etblARStatements_iChangeSetID int NULL
  _etblARStatements_Checksum binary(20) NULL

## _etblAttributeGroupLinks
PK: idAttributeGroupLink
Columns (20):
  idAttributeGroupLink int NOT NULL identity PK
  iAttributeGroupID int NOT NULL
  iAttributeTypeID int NOT NULL
  iDefaultAttributeValueID int NOT NULL
  bColumnEntry bit NOT NULL default (0)
  bForceEntry bit NOT NULL default (1)
  bTrackBalances bit NOT NULL default (0)
  bTrackQty bit NOT NULL default (0)
  bTrackCost bit NOT NULL default (0)
  _etblAttributeGroupLinks_iBranchID int NULL
  _etblAttributeGroupLinks_dCreatedDate datetime NULL
  _etblAttributeGroupLinks_dModifiedDate datetime NULL
  _etblAttributeGroupLinks_iCreatedBranchID int NULL
  _etblAttributeGroupLinks_iModifiedBranchID int NULL
  _etblAttributeGroupLinks_iCreatedAgentID int NULL
  _etblAttributeGroupLinks_iModifiedAgentID int NULL
  _etblAttributeGroupLinks_iChangeSetID int NULL
  _etblAttributeGroupLinks_Checksum binary(20) NULL
  bActiveGroupType bit NOT NULL default (1)
  iEntryType int NOT NULL default (0)

## _etblAttributeGroups
PK: idAttributeGroup
Columns (13):
  idAttributeGroup int NOT NULL identity PK
  cGroupCode varchar(50) NOT NULL
  cGroupDescription varchar(100) NOT NULL
  _etblAttributeGroups_iBranchID int NULL
  _etblAttributeGroups_dCreatedDate datetime NULL
  _etblAttributeGroups_dModifiedDate datetime NULL
  _etblAttributeGroups_iCreatedBranchID int NULL
  _etblAttributeGroups_iModifiedBranchID int NULL
  _etblAttributeGroups_iCreatedAgentID int NULL
  _etblAttributeGroups_iModifiedAgentID int NULL
  _etblAttributeGroups_iChangeSetID int NULL
  _etblAttributeGroups_Checksum binary(20) NULL
  iModuleType int NOT NULL default (-1)

## _etblAttributeTypes
PK: idAttributeType
Columns (14):
  idAttributeType int NOT NULL identity PK
  cAttributeName varchar(100) NOT NULL
  cAttributeDescription varchar(500) NOT NULL
  iAttributeLinkedID int NOT NULL default (0)
  bActiveAttribute bit NOT NULL default (1)
  _etblAttributeTypes_iBranchID int NULL
  _etblAttributeTypes_dCreatedDate datetime NULL
  _etblAttributeTypes_dModifiedDate datetime NULL
  _etblAttributeTypes_iCreatedBranchID int NULL
  _etblAttributeTypes_iModifiedBranchID int NULL
  _etblAttributeTypes_iCreatedAgentID int NULL
  _etblAttributeTypes_iModifiedAgentID int NULL
  _etblAttributeTypes_iChangeSetID int NULL
  _etblAttributeTypes_Checksum binary(20) NULL

## _etblAttributeValues
PK: idAttributeValue
Columns (12):
  idAttributeValue int NOT NULL identity PK
  cAttributeValue varchar(500) NOT NULL
  _etblAttributeValues_iBranchID int NULL
  _etblAttributeValues_dCreatedDate datetime NULL
  _etblAttributeValues_dModifiedDate datetime NULL
  _etblAttributeValues_iCreatedBranchID int NULL
  _etblAttributeValues_iModifiedBranchID int NULL
  _etblAttributeValues_iCreatedAgentID int NULL
  _etblAttributeValues_iModifiedAgentID int NULL
  _etblAttributeValues_iChangeSetID int NULL
  _etblAttributeValues_Checksum binary(20) NULL
  cAttributeCode varchar(20) NULL

## _etblAttributeValueTypeLinks
PK: idAttributeValueTypeLink
Columns (12):
  idAttributeValueTypeLink int NOT NULL identity PK
  iAttributeTypeLinkID int NOT NULL
  iAttributeValueLinkID int NOT NULL
  _etblAttributeValueTypeLinks_iBranchID int NULL
  _etblAttributeValueTypeLinks_dCreatedDate datetime NULL
  _etblAttributeValueTypeLinks_dModifiedDate datetime NULL
  _etblAttributeValueTypeLinks_iCreatedBranchID int NULL
  _etblAttributeValueTypeLinks_iModifiedBranchID int NULL
  _etblAttributeValueTypeLinks_iCreatedAgentID int NULL
  _etblAttributeValueTypeLinks_iModifiedAgentID int NULL
  _etblAttributeValueTypeLinks_iChangeSetID int NULL
  _etblAttributeValueTypeLinks_Checksum binary(20) NULL

## _etblAttributeValueValueLinks
PK: idAttributeValueValueLink
Columns (12):
  idAttributeValueValueLink int NOT NULL identity PK
  iAttributeMainValueID int NOT NULL
  iAttributeLinkedValueID int NOT NULL
  _etblAttributeValueValueLinks_iBranchID int NULL
  _etblAttributeValueValueLinks_dCreatedDate datetime NULL
  _etblAttributeValueValueLinks_dModifiedDate datetime NULL
  _etblAttributeValueValueLinks_iCreatedBranchID int NULL
  _etblAttributeValueValueLinks_iModifiedBranchID int NULL
  _etblAttributeValueValueLinks_iCreatedAgentID int NULL
  _etblAttributeValueValueLinks_iModifiedAgentID int NULL
  _etblAttributeValueValueLinks_iChangeSetID int NULL
  _etblAttributeValueValueLinks_Checksum binary(20) NULL

## _etblAuditingLog
PK: idAuditingLog
Columns (6):
  idAuditingLog int NOT NULL identity PK
  dModificationDate datetime NOT NULL
  iAgentID int NULL
  cTableName varchar(128) NULL
  iActionType int NULL
  cComment varchar(max) NULL

## _etblAuthToken
PK: idToken
Columns (16):
  idToken int NOT NULL identity PK
  cAccountName varchar(256) NULL
  cAccessToken varchar(max) NULL
  cTokenType varchar(64) NULL
  dTokenExpires datetime NULL
  cRefreshToken varchar(max) NULL
  cScope varchar(512) NULL
  _etblAuthToken_iBranchID int NULL
  _etblAuthToken_dCreatedDate datetime NULL
  _etblAuthToken_dModifiedDate datetime NULL
  _etblAuthToken_iCreatedBranchID int NULL
  _etblAuthToken_iModifiedBranchID int NULL
  _etblAuthToken_iCreatedAgentID int NULL
  _etblAuthToken_iModifiedAgentID int NULL
  _etblAuthToken_iChangeSetID int NULL
  _etblAuthToken_Checksum binary(20) NULL

## _etblAutoLevelUpdateItem
PK: idAutolevelUpdateItem
Columns (29):
  idAutolevelUpdateItem int NOT NULL identity PK
  iItemID int NOT NULL
  cItemType char(1) NOT NULL
  iNoOfDays int NULL
  bUseAveragePerDay bit NOT NULL default (1)
  iCat1From int NULL
  iCat1To int NULL
  fCat1NewReOrderQty float NULL
  fCat1NewReOrderLvl float NULL
  iCat2From int NULL
  iCat2To int NULL
  fCat2NewReOrderQty float NULL
  fCat2NewReOrderLvl float NULL
  iCat3From int NULL
  iCat3To int NULL
  fCat3NewReOrderQty float NULL
  fCat3NewReOrderLvl float NULL
  fCat1NewMinReOrderLvl float NULL
  fCat2NewMinReOrderLvl float NULL
  fCat3NewMinReOrderLvl float NULL
  _etblAutoLevelUpdateItem_iBranchID int NULL
  _etblAutoLevelUpdateItem_dCreatedDate datetime NULL
  _etblAutoLevelUpdateItem_dModifiedDate datetime NULL
  _etblAutoLevelUpdateItem_iCreatedBranchID int NULL
  _etblAutoLevelUpdateItem_iModifiedBranchID int NULL
  _etblAutoLevelUpdateItem_iCreatedAgentID int NULL
  _etblAutoLevelUpdateItem_iModifiedAgentID int NULL
  _etblAutoLevelUpdateItem_iChangeSetID int NULL
  _etblAutoLevelUpdateItem_Checksum binary(20) NULL

## _etblAutoStrings - Auto Strings
Alias: Auto Strings | Freedom Name:  | Record Identifier: 
Notes: Auto Text
PK: idAutoStrings
Columns (14):
  idAutoStrings int NOT NULL identity PK
  cAutoString varchar(5) NOT NULL
  bPublic bit NOT NULL default (1)
  cAutoText varchar(120) NOT NULL
  iAgentID int NOT NULL
  _etblAutoStrings_iBranchID int NULL
  _etblAutoStrings_dCreatedDate datetime NULL
  _etblAutoStrings_dModifiedDate datetime NULL
  _etblAutoStrings_iCreatedBranchID int NULL
  _etblAutoStrings_iModifiedBranchID int NULL
  _etblAutoStrings_iCreatedAgentID int NULL
  _etblAutoStrings_iModifiedAgentID int NULL
  _etblAutoStrings_iChangeSetID int NULL
  _etblAutoStrings_Checksum binary(20) NULL

## _etblBankDetails
PK: idBankDetail
Columns (27):
  idBankDetail int NOT NULL identity PK
  cBankName varchar(50) NOT NULL
  cBankAccName varchar(50) NULL
  cBankCode varchar(20) NULL
  cBankAccNumber varchar(50) NULL
  cBranchName varchar(50) NULL
  cBranchCode varchar(20) NULL
  cBankRefNumber varchar(50) NULL
  fAccLimit float NULL
  cEFTSCode varchar(20) NULL
  cEFTSName varchar(50) NULL
  cEFTSReference varchar(20) NULL
  iEFTSLayoutID int NULL
  cEFTSFile varchar(50) NULL
  _etblBankDetails_iBranchID int NULL
  _etblBankDetails_dCreatedDate datetime NULL
  _etblBankDetails_dModifiedDate datetime NULL
  _etblBankDetails_iCreatedBranchID int NULL
  _etblBankDetails_iModifiedBranchID int NULL
  _etblBankDetails_iCreatedAgentID int NULL
  _etblBankDetails_iModifiedAgentID int NULL
  _etblBankDetails_iChangeSetID int NULL
  _etblBankDetails_Checksum binary(20) NULL
  bEFTSAutoNum bit NOT NULL default (0)
  cEFTSAutoNumPrefix varchar(20) NULL
  iEFTSAutoNumPadLength int NOT NULL default (3)
  cEFTSAutoFile varchar(100) NULL

## _etblBarcodes
PK: idBarcode
Columns (14):
  idBarcode int NOT NULL identity PK
  Barcode varchar(400) NOT NULL
  StockID int NOT NULL
  WhseID int NOT NULL default (0)
  UOMID int NOT NULL default (0)
  _etblBarcodes_iBranchID int NULL
  _etblBarcodes_dCreatedDate datetime NULL
  _etblBarcodes_dModifiedDate datetime NULL
  _etblBarcodes_iCreatedBranchID int NULL
  _etblBarcodes_iModifiedBranchID int NULL
  _etblBarcodes_iCreatedAgentID int NULL
  _etblBarcodes_iModifiedAgentID int NULL
  _etblBarcodes_iChangeSetID int NULL
  _etblBarcodes_Checksum binary(20) NULL

## _etblBatchPermissions - Batch Permission
Alias: Batch Permission | Freedom Name:  | Record Identifier: 
Notes: Batch Permission
PK: idBatchPermissions
Columns (17):
  idBatchPermissions int NOT NULL identity PK
  iBatchID int NOT NULL default (0)
  cBatchType varchar(1) NOT NULL default 'C'
  cAgentType varchar(1) NOT NULL default 'A'
  iAgentID int NOT NULL default (0)
  bBatchVisible bit NOT NULL default (1)
  dDatePermissionCreated datetime NOT NULL default getdate()
  iAgentPermissionCreated int NOT NULL default (0)
  _etblBatchPermissions_iBranchID int NULL
  _etblBatchPermissions_dCreatedDate datetime NULL
  _etblBatchPermissions_dModifiedDate datetime NULL
  _etblBatchPermissions_iCreatedBranchID int NULL
  _etblBatchPermissions_iModifiedBranchID int NULL
  _etblBatchPermissions_iCreatedAgentID int NULL
  _etblBatchPermissions_iModifiedAgentID int NULL
  _etblBatchPermissions_iChangeSetID int NULL
  _etblBatchPermissions_Checksum binary(20) NULL

## _etblBinLocationLevelSetup
PK: idLevelSetup
Columns (13):
  idLevelSetup int NOT NULL identity PK
  iLevelNumber int NULL
  cLevelName varchar(50) NULL
  iLevelLength int NULL default (0)
  _etblBinLocationLevelSetup_iBranchID int NULL
  _etblBinLocationLevelSetup_dCreatedDate datetime NULL
  _etblBinLocationLevelSetup_dModifiedDate datetime NULL
  _etblBinLocationLevelSetup_iCreatedBranchID int NULL
  _etblBinLocationLevelSetup_iModifiedBranchID int NULL
  _etblBinLocationLevelSetup_iCreatedAgentID int NULL
  _etblBinLocationLevelSetup_iModifiedAgentID int NULL
  _etblBinLocationLevelSetup_iChangeSetID int NULL
  _etblBinLocationLevelSetup_Checksum binary(20) NULL

## _etblBinLocationLevelValueSetup
PK: idLevelValueSetup
Columns (12):
  idLevelValueSetup int NOT NULL identity PK
  cLevelValueCode varchar(50) NULL
  cLevelValueDescription varchar(100) NULL
  _etblBinLocationLevelValueSetup_iBranchID int NULL
  _etblBinLocationLevelValueSetup_dCreatedDate datetime NULL
  _etblBinLocationLevelValueSetup_dModifiedDate datetime NULL
  _etblBinLocationLevelValueSetup_iCreatedBranchID int NULL
  _etblBinLocationLevelValueSetup_iModifiedBranchID int NULL
  _etblBinLocationLevelValueSetup_iCreatedAgentID int NULL
  _etblBinLocationLevelValueSetup_iModifiedAgentID int NULL
  _etblBinLocationLevelValueSetup_iChangeSetID int NULL
  _etblBinLocationLevelValueSetup_Checksum binary(20) NULL

## _etblBinLocationWhseLevels
PK: idWhseLevel
Columns (13):
  idWhseLevel int NOT NULL identity PK
  iLevelWarehouseID int NOT NULL
  iLevelSetupID int NULL
  bUseLevel bit NULL default (1)
  _etblBinLocationWhseLevels_iBranchID int NULL
  _etblBinLocationWhseLevels_dCreatedDate datetime NULL
  _etblBinLocationWhseLevels_dModifiedDate datetime NULL
  _etblBinLocationWhseLevels_iCreatedBranchID int NULL
  _etblBinLocationWhseLevels_iModifiedBranchID int NULL
  _etblBinLocationWhseLevels_iCreatedAgentID int NULL
  _etblBinLocationWhseLevels_iModifiedAgentID int NULL
  _etblBinLocationWhseLevels_iChangeSetID int NULL
  _etblBinLocationWhseLevels_Checksum binary(20) NULL

## _etblBinLocationWhseLevelValues
PK: idWhseLevelValue
Columns (13):
  idWhseLevelValue int NOT NULL identity PK
  iLevelWarehouseID int NOT NULL
  iLevelWhseLevelID int NOT NULL
  iLevelValueID int NOT NULL
  _etblBinLocationWhseLevelValues_iBranchID int NULL
  _etblBinLocationWhseLevelValues_dCreatedDate datetime NULL
  _etblBinLocationWhseLevelValues_dModifiedDate datetime NULL
  _etblBinLocationWhseLevelValues_iCreatedBranchID int NULL
  _etblBinLocationWhseLevelValues_iModifiedBranchID int NULL
  _etblBinLocationWhseLevelValues_iCreatedAgentID int NULL
  _etblBinLocationWhseLevelValues_iModifiedAgentID int NULL
  _etblBinLocationWhseLevelValues_iChangeSetID int NULL
  _etblBinLocationWhseLevelValues_Checksum binary(20) NULL

## _etblBinTransferBatches
PK: idBinTransferBatch
Columns (32):
  idBinTransferBatch int NOT NULL identity PK
  cBatchNo varchar(50) NULL
  cBatchDescription varchar(40) NULL
  cBatchRefNo varchar(50) NULL
  iTrCodeID int NULL
  iCreateAgentID int NULL
  bClearBatchAfterPost bit NOT NULL default (1)
  bAllowDuplicateRef bit NOT NULL default (1)
  bPrintJournal bit NOT NULL default (1)
  iNewLineRefOpt int NULL
  cNewLineRefDef varchar(20) NULL
  bNewLineRefIncr bit NOT NULL default (0)
  iNewLineDescOpt int NULL
  cNewLineDescDef varchar(40) NULL
  bNewLineDescIncr bit NOT NULL default (0)
  iNewLineWHBinOpt int NULL
  iNewLineWHBinDefID int NULL
  iNewLineBinFromOpt int NULL
  iNewLineBinFromDefID int NULL
  iNewLineBinToOpt int NULL
  iNewLineBinToDefID int NULL
  iNewLineProjectOpt int NULL
  iNewLineProjectDefID int NULL
  _etblBinTransferBatches_iBranchID int NULL
  _etblBinTransferBatches_dCreatedDate datetime NULL
  _etblBinTransferBatches_dModifiedDate datetime NULL
  _etblBinTransferBatches_iCreatedBranchID int NULL
  _etblBinTransferBatches_iModifiedBranchID int NULL
  _etblBinTransferBatches_iCreatedAgentID int NULL
  _etblBinTransferBatches_iModifiedAgentID int NULL
  _etblBinTransferBatches_iChangeSetID int NULL
  _etblBinTransferBatches_Checksum binary(20) NULL

## _etblBinTransferBatchLines
PK: idBinTransferBatchLines
Columns (31):
  idBinTransferBatchLines int NOT NULL identity PK
  iBinTransferBatchID int NULL
  iStockID int NULL
  iWarehouseID int NULL
  iFromStockBinLocationID int NOT NULL default (0)
  iToStockBinLocationID int NOT NULL default (0)
  fQuantity float NULL
  fCost float NULL
  cReference varchar(20) NULL
  cDescription varchar(40) NULL
  bIsSerialItem bit NOT NULL default (0)
  iSerialNumberGroupID int NULL
  bIsLotItem bit NOT NULL default (0)
  iLotID int NOT NULL default (0)
  cLotNumber varchar(50) NULL
  dLotExpiryDate datetime NULL
  iProjectID int NOT NULL default (0)
  cLineNotes varchar(1024) NULL
  iUnitsOfMeasureStockingID int NULL
  iUnitsOfMeasureCategoryID int NULL
  iUnitsOfMeasureID int NULL
  xBTAttribute xml NULL
  _etblBinTransferBatchLines_iBranchID int NULL
  _etblBinTransferBatchLines_dCreatedDate datetime NULL
  _etblBinTransferBatchLines_dModifiedDate datetime NULL
  _etblBinTransferBatchLines_iCreatedBranchID int NULL
  _etblBinTransferBatchLines_iModifiedBranchID int NULL
  _etblBinTransferBatchLines_iCreatedAgentID int NULL
  _etblBinTransferBatchLines_iModifiedAgentID int NULL
  _etblBinTransferBatchLines_iChangeSetID int NULL
  _etblBinTransferBatchLines_Checksum binary(20) NULL

## _etblBranch - Branch (Branch)
Alias: Branch | Freedom Name: Branch | Record Identifier: 
Notes: Branch - Branch Accounting Branches
PK: idBranch
Columns (21):
  idBranch int NOT NULL identity PK
  cBranchCode varchar(20) NULL
  cBranchDescription varchar(50) NULL
  bBranchActive bit NOT NULL default (1)
  bSyncEnabled bit NOT NULL default (1)
  dLastExport datetime NULL
  dLastImport datetime NULL
  iLastImportSeq int NULL
  iLastExportSeq int NULL
  iLastExportChangeSetID int NULL
  bIsDCBranch bit NOT NULL default (0)
  iDCWarehouseID int NOT NULL default (0)
  _etblBranch_iBranchID int NULL
  _etblBranch_dCreatedDate datetime NULL
  _etblBranch_dModifiedDate datetime NULL
  _etblBranch_iCreatedBranchID int NULL
  _etblBranch_iModifiedBranchID int NULL
  _etblBranch_iCreatedAgentID int NULL
  _etblBranch_iModifiedAgentID int NULL
  _etblBranch_iChangeSetID int NULL
  _etblBranch_Checksum binary(20) NULL

## _etblBudgets - Budgets (Budgets)
Alias: Budgets | Freedom Name: Budgets | Record Identifier: 
Notes: GL Budgets
PK: idBudgets
Columns (25):
  idBudgets int NOT NULL identity PK
  iBudgetAccountID int NOT NULL
  iBudgetProjectID int NOT NULL
  iBudgetPeriodID int NOT NULL
  iBudgetTxBranchID int NOT NULL
  iBudgetAccountType int NOT NULL
  fBudget float NULL
  fUnprocessedPOValue float NULL
  dBudgetDTStamp datetime NULL
  fForecast float NOT NULL default (0)
  _etblBudgets_iBranchID int NULL
  _etblBudgets_dCreatedDate datetime NULL
  _etblBudgets_dModifiedDate datetime NULL
  _etblBudgets_iCreatedBranchID int NULL
  _etblBudgets_iModifiedBranchID int NULL
  _etblBudgets_iCreatedAgentID int NULL
  _etblBudgets_iModifiedAgentID int NULL
  _etblBudgets_iChangeSetID int NULL
  _etblBudgets_Checksum binary(20) NULL
  fBudgetForeign float NOT NULL default (0)
  fUnprocessedPOValueForeign float NOT NULL default (0)
  fForecastForeign float NOT NULL default (0)
  fBudgetCurrency float NOT NULL default (0)
  fUnprocessedPOValueCurrency float NOT NULL default (0)
  fForecastCurrency float NOT NULL default (0)

## _etblBudgetsPrev - Budgets Prev
Alias: Budgets Prev | Freedom Name:  | Record Identifier: 
Notes: Previous Budgets
PK: idBudgetsPrev
Columns (22):
  idBudgetsPrev int NOT NULL identity PK
  iBudgetPrevAccountID int NOT NULL
  iBudgetPrevProjectID int NOT NULL
  iBudgetPrevPeriodID int NOT NULL
  iBudgetPrevTxBranchID int NOT NULL
  iBudgetPrevAccountType int NOT NULL
  fBudgetPrev float NULL
  fUnprocessedPOValuePrev float NULL
  dBudgetPrevDTStamp datetime NULL
  _etblBudgetsPrev_iBranchID int NULL
  _etblBudgetsPrev_dCreatedDate datetime NULL
  _etblBudgetsPrev_dModifiedDate datetime NULL
  _etblBudgetsPrev_iCreatedBranchID int NULL
  _etblBudgetsPrev_iModifiedBranchID int NULL
  _etblBudgetsPrev_iCreatedAgentID int NULL
  _etblBudgetsPrev_iModifiedAgentID int NULL
  _etblBudgetsPrev_iChangeSetID int NULL
  _etblBudgetsPrev_Checksum binary(20) NULL
  fBudgetPrevForeign float NOT NULL default (0)
  fUnprocessedPOValuePrevForeign float NOT NULL default (0)
  fBudgetPrevCurrency float NOT NULL default (0)
  fUnprocessedPOValuePrevCurrency float NOT NULL default (0)

## _etblCMAgentContact - CM Agent Contact (ContactManagementAgentContact)
Alias: CM Agent Contact | Freedom Name: ContactManagementAgentContact | Record Identifier: 
Notes: CM Agent Contact
PK: idContact
Columns (17):
  idContact int NOT NULL identity PK
  iAgentID int NOT NULL
  cContactType char(1) NULL
  iSourceID int NULL
  cLastName varchar(255) NOT NULL
  cFirstName varchar(255) NULL
  cEmailAddress varchar(255) NULL
  cPhone varchar(50) NULL
  _etblCMAgentContact_iBranchID int NULL
  _etblCMAgentContact_dCreatedDate datetime NULL
  _etblCMAgentContact_dModifiedDate datetime NULL
  _etblCMAgentContact_iCreatedBranchID int NULL
  _etblCMAgentContact_iModifiedBranchID int NULL
  _etblCMAgentContact_iCreatedAgentID int NULL
  _etblCMAgentContact_iModifiedAgentID int NULL
  _etblCMAgentContact_iChangeSetID int NULL
  _etblCMAgentContact_Checksum binary(20) NULL

## _etblCMRejectReason - CM Reject Reason (ContactManagementRejectReason)
Alias: CM Reject Reason | Freedom Name: ContactManagementRejectReason | Record Identifier: 
Notes: Contact Management Reject Reasons
PK: idRejectReason
Columns (12):
  idRejectReason int NOT NULL identity PK
  cRejectCode varchar(20) NOT NULL
  cDescription varchar(50) NULL
  _etblCMRejectReason_iBranchID int NULL
  _etblCMRejectReason_dCreatedDate datetime NULL
  _etblCMRejectReason_dModifiedDate datetime NULL
  _etblCMRejectReason_iCreatedBranchID int NULL
  _etblCMRejectReason_iModifiedBranchID int NULL
  _etblCMRejectReason_iCreatedAgentID int NULL
  _etblCMRejectReason_iModifiedAgentID int NULL
  _etblCMRejectReason_iChangeSetID int NULL
  _etblCMRejectReason_Checksum binary(20) NULL

## _etblDashboardLayouts - Dashboard Layouts
Alias: Dashboard Layouts | Freedom Name:  | Record Identifier: 
PK: idDashboardLayouts
Columns (13):
  idDashboardLayouts int NOT NULL identity PK
  iAgentID int NOT NULL
  iAgentGroupID int NOT NULL
  nLayout varchar(max) NOT NULL
  _etblDashboardLayouts_iBranchID int NULL
  _etblDashboardLayouts_dCreatedDate datetime NULL
  _etblDashboardLayouts_dModifiedDate datetime NULL
  _etblDashboardLayouts_iCreatedBranchID int NULL
  _etblDashboardLayouts_iModifiedBranchID int NULL
  _etblDashboardLayouts_iCreatedAgentID int NULL
  _etblDashboardLayouts_iModifiedAgentID int NULL
  _etblDashboardLayouts_iChangeSetID int NULL
  _etblDashboardLayouts_Checksum binary(20) NULL

## _etblDelAddress - Delivery Address (DeliveryAddress)
Alias: Delivery Address | Freedom Name: DeliveryAddress | Record Identifier: 
Notes: Delivery Address
PK: idDelAddress
Columns (32):
  idDelAddress int NOT NULL identity PK
  iDelAddressCodeID int NOT NULL default (0)
  iAccountID int NOT NULL
  iDCModule int NOT NULL
  cDescription varchar(60) NULL
  cDelAddress1 varchar(40) NULL
  cDelAddress2 varchar(40) NULL
  cDelAddress3 varchar(40) NULL
  cDelAddress4 varchar(40) NULL
  cDelAddress5 varchar(40) NULL
  cDelAddressPC varchar(15) NULL
  cDelContact1 varchar(30) NULL
  cDelContact2 varchar(30) NULL
  cDelTelephone1 varchar(25) NULL
  cDelTelephone2 varchar(25) NULL
  cDelCellular varchar(25) NULL
  cDelFax varchar(25) NULL
  cEmail varchar(200) NULL
  bDefault bit NOT NULL default (0)
  iSalesRepID int NULL
  iChargeTaxOpt int NULL
  dDelAddressTimeStamp datetime NULL
  iDefDeliveryMethodID int NOT NULL default (0)
  _etblDelAddress_iBranchID int NULL
  _etblDelAddress_dCreatedDate datetime NULL
  _etblDelAddress_dModifiedDate datetime NULL
  _etblDelAddress_iCreatedBranchID int NULL
  _etblDelAddress_iModifiedBranchID int NULL
  _etblDelAddress_iCreatedAgentID int NULL
  _etblDelAddress_iModifiedAgentID int NULL
  _etblDelAddress_iChangeSetID int NULL
  _etblDelAddress_Checksum binary(20) NULL

## _etblDelAddressCode
PK: IDDelAddressCode
Columns (12):
  IDDelAddressCode int NOT NULL identity PK
  cDelAddressCode varchar(20) NULL
  cDescription varchar(100) NULL
  _etblDelAddressCode_iBranchID int NULL
  _etblDelAddressCode_dCreatedDate datetime NULL
  _etblDelAddressCode_dModifiedDate datetime NULL
  _etblDelAddressCode_iCreatedBranchID int NULL
  _etblDelAddressCode_iModifiedBranchID int NULL
  _etblDelAddressCode_iCreatedAgentID int NULL
  _etblDelAddressCode_iModifiedAgentID int NULL
  _etblDelAddressCode_iChangeSetID int NULL
  _etblDelAddressCode_Checksum binary(20) NULL

## _etblDeleted - Deleted
Alias: Deleted | Freedom Name:  | Record Identifier: 
Notes: Deleted
PK: idDeleted
Columns (13):
  idDeleted int NOT NULL identity PK
  cTableName varchar(128) NULL
  cPKFields varchar(512) NULL
  cPKValues varchar(128) NULL
  iRowBranchID int NULL
  iDeletedAtBranchID int NULL
  _auditDate datetime NULL
  _auditHostName varchar(64) NULL
  _auditSystemUser varchar(64) NULL
  _auditUserName varchar(64) NULL
  _auditAppName varchar(128) NULL
  iChangeSetID int NULL
  _KeyFields_Checksum binary(20) NULL

## _etblDiagnosticChecks
PK: idDiagnosticCheck
Columns (7):
  idDiagnosticCheck int NOT NULL identity PK
  cName varchar(50) NOT NULL
  iDiagnosticTestID int NOT NULL
  cScript varchar(max) NOT NULL
  cScriptDescription varchar(max) NOT NULL
  uScriptIdentifier uniqueidentifier NOT NULL
  iVersion int NOT NULL

## _etblDiagnosticLogDetails
PK: idLogDetails
Columns (7):
  idLogDetails int NOT NULL identity PK
  iLogMasterID int NOT NULL
  iCheckID int NOT NULL
  dLoggedDate datetime NOT NULL
  cDetail varchar(max) NOT NULL
  iRowCount int NOT NULL
  cScript varchar(max) NOT NULL

## _etblDiagnosticLogMaster
PK: idLogMaster
Columns (2):
  idLogMaster int NOT NULL identity PK
  dTimeStamp datetime NOT NULL

## _etblDiagnosticModules
PK: idDiagnosticModule
Columns (2):
  idDiagnosticModule int NOT NULL identity PK
  cModule varchar(50) NOT NULL

## _etblDiagnosticTests
PK: idDiagnosticTest
Columns (6):
  idDiagnosticTest int NOT NULL identity PK
  cName varchar(50) NOT NULL
  cPreRequisiteScript varchar(max) NOT NULL
  iModuleID int NOT NULL
  iCheckType int NOT NULL
  uTestIdentifier uniqueidentifier NOT NULL

## _etblDocCat
PK: idDocCat
Columns (14):
  idDocCat int NOT NULL identity PK
  cDocCatCode varchar(30) NOT NULL
  cDocCatDescription varchar(100) NULL
  cDocCatLocation varchar(256) NULL
  iDocCatGroupID int NULL default (0)
  _etblDocCat_iBranchID int NULL
  _etblDocCat_dCreatedDate datetime NULL
  _etblDocCat_dModifiedDate datetime NULL
  _etblDocCat_iCreatedBranchID int NULL
  _etblDocCat_iModifiedBranchID int NULL
  _etblDocCat_iCreatedAgentID int NULL
  _etblDocCat_iModifiedAgentID int NULL
  _etblDocCat_iChangeSetID int NULL
  _etblDocCat_Checksum binary(20) NULL

## _etblDocCatGroup
PK: idDocCatGroup
Columns (13):
  idDocCatGroup int NOT NULL identity PK
  cDocCatGroupCode varchar(30) NOT NULL
  cDocCatGroupDescription varchar(100) NULL
  cDocCatGroupLocation varchar(256) NULL
  _etblDocCatGroup_iBranchID int NULL
  _etblDocCatGroup_dCreatedDate datetime NULL
  _etblDocCatGroup_dModifiedDate datetime NULL
  _etblDocCatGroup_iCreatedBranchID int NULL
  _etblDocCatGroup_iModifiedBranchID int NULL
  _etblDocCatGroup_iCreatedAgentID int NULL
  _etblDocCatGroup_iModifiedAgentID int NULL
  _etblDocCatGroup_iChangeSetID int NULL
  _etblDocCatGroup_Checksum binary(20) NULL

## _etblDocProfiles - Document Profiles (DocumentProfiles)
Alias: Document Profiles | Freedom Name: DocumentProfiles | Record Identifier: 
Notes: Document Profiles
PK: idDocProfiles
Columns (37):
  idDocProfiles int NOT NULL identity PK
  cCode varchar(20) NOT NULL
  cDescription varchar(120) NULL
  bActive bit NOT NULL default (0)
  iDocType int NOT NULL
  iDocSubType int NOT NULL
  bUseDefaults bit NOT NULL default (0)
  bAutoNum bit NOT NULL default (1)
  iNextAutoNum int NULL
  iAutoNumPadLength int NULL
  cAutoNumPrefix varchar(20) NULL
  bUniqueNum bit NULL default (0)
  iDocTrCodeID int NULL
  iDocHomeLayoutID int NULL
  bDocHomeLayoutPrompt bit NOT NULL default (0)
  iDocForeignLayoutID int NULL
  bDocForeignLayoutPrompt bit NOT NULL default (0)
  iExclusiveDoc int NULL
  iTaxPerDoc int NULL
  bHasBeenUsed bit NOT NULL default (0)
  bIsUserLayout bit NOT NULL default (0)
  bIsUserForeignLayout bit NOT NULL default (0)
  iDocHomeEmailLayoutID int NULL
  bDocHomeEmailLayoutPrompt bit NOT NULL default (0)
  bIsUserEmailLayout bit NOT NULL default (0)
  iDocForeignEmailLayoutID int NULL
  bDocForeignEmailLayoutPrompt bit NOT NULL default (0)
  bIsUserForeignEmailLayout bit NOT NULL default (0)
  _etblDocProfiles_iBranchID int NULL
  _etblDocProfiles_dCreatedDate datetime NULL
  _etblDocProfiles_dModifiedDate datetime NULL
  _etblDocProfiles_iCreatedBranchID int NULL
  _etblDocProfiles_iModifiedBranchID int NULL
  _etblDocProfiles_iCreatedAgentID int NULL
  _etblDocProfiles_iModifiedAgentID int NULL
  _etblDocProfiles_iChangeSetID int NULL
  _etblDocProfiles_Checksum binary(20) NULL

## _etblDuration
PK: iDuration
Columns (5):
  iDuration int NOT NULL identity PK
  iType varchar(20) NULL
  iDueType varchar(40) NULL
  dDateDue datetime NULL
  iTimeTaken int NULL

## _etblEFTGatewayType - EFT Gateway Type
Alias: EFT Gateway Type | Freedom Name:  | Record Identifier: 
Notes: EFT Pos Gateway Type
PK: GatewayID
Columns (12):
  GatewayID int NOT NULL identity PK
  cCode smallint NULL
  cGatewayName nvarchar(30) NULL
  _etblEFTGatewayType_iBranchID int NULL
  _etblEFTGatewayType_dCreatedDate datetime NULL
  _etblEFTGatewayType_dModifiedDate datetime NULL
  _etblEFTGatewayType_iCreatedBranchID int NULL
  _etblEFTGatewayType_iModifiedBranchID int NULL
  _etblEFTGatewayType_iCreatedAgentID int NULL
  _etblEFTGatewayType_iModifiedAgentID int NULL
  _etblEFTGatewayType_iChangeSetID int NULL
  _etblEFTGatewayType_Checksum binary(20) NULL

## _etblEFTReference - EFT Reference
Alias: EFT Reference | Freedom Name:  | Record Identifier: 
Notes: EFT Reference
PK: idNumber
Columns (11):
  idNumber int NOT NULL identity PK
  iAgentID int NULL
  _etblEFTReference_iBranchID int NULL
  _etblEFTReference_dCreatedDate datetime NULL
  _etblEFTReference_dModifiedDate datetime NULL
  _etblEFTReference_iCreatedBranchID int NULL
  _etblEFTReference_iModifiedBranchID int NULL
  _etblEFTReference_iCreatedAgentID int NULL
  _etblEFTReference_iModifiedAgentID int NULL
  _etblEFTReference_iChangeSetID int NULL
  _etblEFTReference_Checksum binary(20) NULL

## _etblEFTSFileLayout - EFTS File Layout
Alias: EFTS File Layout | Freedom Name:  | Record Identifier: 
Notes: EFTS File Layout
PK: idEFTSLayout
Columns (34):
  idEFTSLayout int NOT NULL identity PK
  cDescription varchar(200) NOT NULL
  bSystemLayout bit NOT NULL default (1)
  cNameOutFile varchar(50) NULL
  cTypeOutFile varchar(3) NULL
  iDelimiterOutFile int NULL
  iEOLCharOutFile int NULL
  iCountryCode int NOT NULL default (0)
  iNoOfHeaders int NULL
  iNoOFTransactions int NULL
  iNoOfFooters int NULL
  iMaxNoOfRecords int NULL
  iHashTotalCalc int NOT NULL default (0)
  cSeedNumber varchar(32) NULL
  bAllowTestRun bit NOT NULL default (0)
  bAskBatchNo bit NOT NULL default (0)
  iDayDifference int NOT NULL default (0)
  iACBServiceType int NOT NULL default (0)
  bIncrementFileName bit NOT NULL default (0)
  cUserName varchar(50) NULL
  cPassword varchar(160) NULL
  cPin varchar(160) NULL
  iEFTSOrderLetterID int NOT NULL default (0)
  iSourceLayoutID int NULL default (0)
  cXSLT varchar(max) NULL
  _etblEFTSFileLayout_iBranchID int NULL
  _etblEFTSFileLayout_dCreatedDate datetime NULL
  _etblEFTSFileLayout_dModifiedDate datetime NULL
  _etblEFTSFileLayout_iCreatedBranchID int NULL
  _etblEFTSFileLayout_iModifiedBranchID int NULL
  _etblEFTSFileLayout_iCreatedAgentID int NULL
  _etblEFTSFileLayout_iModifiedAgentID int NULL
  _etblEFTSFileLayout_iChangeSetID int NULL
  _etblEFTSFileLayout_Checksum binary(20) NULL

## _etblEFTSFileLayoutDetails - EFTS File Layout Detail
Alias: EFTS File Layout Detail | Freedom Name:  | Record Identifier: 
Notes: EFTS File Layout Detail
PK: idEFTSLayoutDetails
Columns (20):
  idEFTSLayoutDetails int NOT NULL identity PK
  iEFTSLayoutID int NOT NULL
  cRecordType varchar(50) NOT NULL
  cDescription varchar(30) NOT NULL
  iFieldLength int NOT NULL
  iDecimalPlaces int NULL
  cFieldFormat varchar(30) NULL
  iFiller int NULL
  bFieldInUse bit NOT NULL default (1)
  cValueType varchar(1) NULL
  cDefaultValue varchar(120) NULL
  _etblEFTSFileLayoutDetails_iBranchID int NULL
  _etblEFTSFileLayoutDetails_dCreatedDate datetime NULL
  _etblEFTSFileLayoutDetails_dModifiedDate datetime NULL
  _etblEFTSFileLayoutDetails_iCreatedBranchID int NULL
  _etblEFTSFileLayoutDetails_iModifiedBranchID int NULL
  _etblEFTSFileLayoutDetails_iCreatedAgentID int NULL
  _etblEFTSFileLayoutDetails_iModifiedAgentID int NULL
  _etblEFTSFileLayoutDetails_iChangeSetID int NULL
  _etblEFTSFileLayoutDetails_Checksum binary(20) NULL

## _etblEUCommodity
PK: IDEUCommodity
Columns (12):
  IDEUCommodity int NOT NULL identity PK
  cEUCommodityCode varchar(20) NULL
  cEUCommodityDescription varchar(1000) NULL
  _etblEUCommodity_iBranchID int NULL
  _etblEUCommodity_dCreatedDate datetime NULL
  _etblEUCommodity_dModifiedDate datetime NULL
  _etblEUCommodity_iCreatedBranchID int NULL
  _etblEUCommodity_iModifiedBranchID int NULL
  _etblEUCommodity_iCreatedAgentID int NULL
  _etblEUCommodity_iModifiedAgentID int NULL
  _etblEUCommodity_iChangeSetID int NULL
  _etblEUCommodity_Checksum binary(20) NULL

## _etblEUCountry - EU Country
Alias: EU Country | Freedom Name:  | Record Identifier: cEUCountryCode
Notes: EU Country
PK: IDEUCountry
Columns (12):
  IDEUCountry int NOT NULL identity PK
  cEUCountryCode varchar(2) NOT NULL
  cEUCountryName varchar(30) NULL
  _etblEUCountry_iBranchID int NULL
  _etblEUCountry_dCreatedDate datetime NULL
  _etblEUCountry_dModifiedDate datetime NULL
  _etblEUCountry_iCreatedBranchID int NULL
  _etblEUCountry_iModifiedBranchID int NULL
  _etblEUCountry_iCreatedAgentID int NULL
  _etblEUCountry_iModifiedAgentID int NULL
  _etblEUCountry_iChangeSetID int NULL
  _etblEUCountry_Checksum binary(20) NULL

## _etblEUNoTC - EU Nature of Transaction (EuropeanUnionNatureOfTransaction)
Alias: EU Nature of Transaction | Freedom Name: EuropeanUnionNatureOfTransaction | Record Identifier: cEUNoTCCode
Notes: EU Nature of Transaction
PK: IDEUNoTC
Columns (12):
  IDEUNoTC int NOT NULL identity PK
  cEUNoTCCode varchar(2) NULL
  cEUNoTCDescription varchar(200) NULL
  _etblEUNoTC_iBranchID int NULL
  _etblEUNoTC_dCreatedDate datetime NULL
  _etblEUNoTC_dModifiedDate datetime NULL
  _etblEUNoTC_iCreatedBranchID int NULL
  _etblEUNoTC_iModifiedBranchID int NULL
  _etblEUNoTC_iCreatedAgentID int NULL
  _etblEUNoTC_iModifiedAgentID int NULL
  _etblEUNoTC_iChangeSetID int NULL
  _etblEUNoTC_Checksum binary(20) NULL

## _etblEUSupplementaryUnit - EU Supplementary Unit
Alias: EU Supplementary Unit | Freedom Name:  | Record Identifier: cEUSupplementaryUnitCode
Notes: EU Supplementary Unit
PK: IDEUSupplementaryUnit
Columns (12):
  IDEUSupplementaryUnit int NOT NULL identity PK
  cEUSupplementaryUnitCode varchar(20) NULL
  cEUSupplementaryUnitDescription varchar(100) NULL
  _etblEUSupplementaryUnit_iBranchID int NULL
  _etblEUSupplementaryUnit_dCreatedDate datetime NULL
  _etblEUSupplementaryUnit_dModifiedDate datetime NULL
  _etblEUSupplementaryUnit_iCreatedBranchID int NULL
  _etblEUSupplementaryUnit_iModifiedBranchID int NULL
  _etblEUSupplementaryUnit_iCreatedAgentID int NULL
  _etblEUSupplementaryUnit_iModifiedAgentID int NULL
  _etblEUSupplementaryUnit_iChangeSetID int NULL
  _etblEUSupplementaryUnit_Checksum binary(20) NULL

## _etblFAAssetBarCode - Asset Barcode
Alias: Asset Barcode | Freedom Name:  | Record Identifier: 
Notes: Asset Barcode
Columns: none recorded yet (table seen in another Evolution database, not in the scripted one)

## _etblFiscalData
PK: idFiscalData
Columns (33):
  idFiscalData int NOT NULL identity PK
  cDeviceTPIN nvarchar(20) NULL
  iTaxAID int NULL
  fTaxARate float NULL
  iTaxBID int NULL
  fTaxBRate float NULL
  iTaxCID int NULL
  fTaxCRate float NULL
  iTaxDID int NULL
  fTaxDRate float NULL
  iTaxEID int NULL
  fTaxERate float NULL
  iTaxFID int NULL
  fTaxFRate float NULL
  iTaxGID int NULL
  fTaxGRate float NULL
  iTaxHID int NULL
  fTaxHRate float NULL
  cTaxJSON nvarchar(1000) NULL
  cTaxpayerName varchar(200) NULL
  cTaxpayerAddress varchar(500) NULL
  cESDSerialNumber varchar(200) NULL
  cSerialNumber nvarchar(10) NULL
  bIsLocked bit NULL
  _etblFiscalData_iBranchID int NULL
  _etblFiscalData_dCreatedDate datetime NULL
  _etblFiscalData_dModifiedDate datetime NULL
  _etblFiscalData_iCreatedBranchID int NULL
  _etblFiscalData_iModifiedBranchID int NULL
  _etblFiscalData_iCreatedAgentID int NULL
  _etblFiscalData_iModifiedAgentID int NULL
  _etblFiscalData_iChangeSetID int NULL
  _etblFiscalData_Checksum binary(20) NULL

## _etblFiscalPrinterModels
PK: iFiscalPrinterModelsId
Columns (15):
  iFiscalPrinterModelsId int NOT NULL identity PK
  cPrinterModelName varchar(50) NULL
  cPrinterModelManufacture varchar(15) NULL
  cFiscalDriverName nvarchar(20) NULL
  bAllowAlphaNumDoc bit NOT NULL default (1)
  bIsPrinter bit NOT NULL default (1)
  _etblFiscalPrinterModels_iBranchID int NULL
  _etblFiscalPrinterModels_dCreatedDate datetime NULL
  _etblFiscalPrinterModels_dModifiedDate datetime NULL
  _etblFiscalPrinterModels_iCreatedBranchID int NULL
  _etblFiscalPrinterModels_iModifiedBranchID int NULL
  _etblFiscalPrinterModels_iCreatedAgentID int NULL
  _etblFiscalPrinterModels_iModifiedAgentID int NULL
  _etblFiscalPrinterModels_iChangeSetID int NULL
  _etblFiscalPrinterModels_Checksum binary(20) NULL

## _etblFiscalPrinters
PK: iFiscalPrinterId
Columns (28):
  iFiscalPrinterId int NOT NULL identity PK
  iPOSDeviceId int NULL
  cIPAddress varchar(15) NULL
  cPortNumber varchar(15) NULL
  cSubnetMask varchar(15) NULL
  cDefaultGateway varchar(15) NULL
  cMACAddress varchar(17) NULL
  iTaxTypeA int NULL
  iTaxTypeB int NULL
  iTaxTypeC int NULL
  iTaxTypeD int NULL
  iTaxTypeE int NULL
  iTaxTypeF int NULL
  bDeviceConfigured bit NULL
  cRegistrationKey varchar(50) NULL
  cTINNumber varchar(50) NULL
  cMRCNumber varchar(50) NULL
  _etblFiscalPrinters_iBranchID int NULL
  _etblFiscalPrinters_dCreatedDate datetime NULL
  _etblFiscalPrinters_dModifiedDate datetime NULL
  _etblFiscalPrinters_iCreatedBranchID int NULL
  _etblFiscalPrinters_iModifiedBranchID int NULL
  _etblFiscalPrinters_iCreatedAgentID int NULL
  _etblFiscalPrinters_iModifiedAgentID int NULL
  _etblFiscalPrinters_iChangeSetID int NULL
  _etblFiscalPrinters_Checksum binary(20) NULL
  iTaxTypeG int NULL
  iTaxTypeH int NULL

## _etblGLAccountTypes
PK: idGLAccountType
Columns (16):
  idGLAccountType int NOT NULL PK
  cAccountTypeDescription varchar(100) NOT NULL
  bIsBalanceSheet bit NOT NULL default (1)
  bIsDebit bit NOT NULL default (1)
  iReportingGroup int NOT NULL default (1)
  iReportingGroupSort int NOT NULL default (1)
  bDualPrinting bit NOT NULL default (0)
  _etblGLAccountTypes_iBranchID int NULL
  _etblGLAccountTypes_dCreatedDate datetime NULL
  _etblGLAccountTypes_dModifiedDate datetime NULL
  _etblGLAccountTypes_iCreatedBranchID int NULL
  _etblGLAccountTypes_iModifiedBranchID int NULL
  _etblGLAccountTypes_iCreatedAgentID int NULL
  _etblGLAccountTypes_iModifiedAgentID int NULL
  _etblGLAccountTypes_iChangeSetID int NULL
  _etblGLAccountTypes_Checksum binary(20) NULL

## _etblGLLoanAccountLinks - GL Loan Account Links (GeneralLedgerLoanAccountLinks)
Alias: GL Loan Account Links | Freedom Name: GeneralLedgerLoanAccountLinks | Record Identifier: 
Notes: GL Loan Account
PK: idGLLoanAccountLinks
Columns (12):
  idGLLoanAccountLinks int NOT NULL identity PK
  iABLoanAccountID int NULL
  iBranchLoanAccountID int NULL
  _etblGLLoanAccountLinks_iBranchID int NULL
  _etblGLLoanAccountLinks_dCreatedDate datetime NULL
  _etblGLLoanAccountLinks_dModifiedDate datetime NULL
  _etblGLLoanAccountLinks_iCreatedBranchID int NULL
  _etblGLLoanAccountLinks_iModifiedBranchID int NULL
  _etblGLLoanAccountLinks_iCreatedAgentID int NULL
  _etblGLLoanAccountLinks_iModifiedAgentID int NULL
  _etblGLLoanAccountLinks_iChangeSetID int NULL
  _etblGLLoanAccountLinks_Checksum binary(20) NULL

## _etblGLmSCOAAccounts - GL mSCOA Accounts (GeneralLedgermSCOAAccounts)
Alias: GL mSCOA Accounts | Freedom Name: GeneralLedgermSCOAAccounts | Record Identifier: 
PK: idGLmSCOAAccount
Columns (42):
  idGLmSCOAAccount int NOT NULL identity PK
  SCOAId varchar(50) NOT NULL
  ParentSCOAId varchar(50) NULL
  DefinitionDescription varchar(max) NULL
  SCOAFile varchar(20) NULL
  SCOAAccount varchar(255) NULL
  SCOALevel int NULL
  ExcelRowNumber int NULL
  ShortDescription varchar(255) NULL
  VATStatus varchar(50) NULL
  BreakDownAllowed varchar(20) NULL
  Principle varchar(255) NULL
  ApplicableTo varchar(50) NULL
  bPostingLevel bit NULL default (1)
  PostingLevelDescription varchar(20) NULL
  AccountNumber varchar(50) NULL
  AccountNumberPrefix varchar(10) NULL
  AccountNumber1 int NULL
  AccountNumber2 int NULL
  AccountNumber3 int NULL
  AccountNumber4 int NULL
  AccountNumber5 int NULL
  AccountNumber6 int NULL
  AccountNumber7 int NULL
  AccountNumber8 int NULL
  AccountNumber9 int NULL
  AccountNumber10 int NULL
  AccountNumber11 int NULL
  AccountNumber12 int NULL
  GFSCode varchar(20) NULL
  MSCOACheck binary(20) NULL
  NextSubAccountNumber int NULL default (1)
  _etblGLmSCOAAccounts_iBranchID int NULL
  _etblGLmSCOAAccounts_dCreatedDate datetime NULL
  _etblGLmSCOAAccounts_dModifiedDate datetime NULL
  _etblGLmSCOAAccounts_iCreatedBranchID int NULL
  _etblGLmSCOAAccounts_iModifiedBranchID int NULL
  _etblGLmSCOAAccounts_iCreatedAgentID int NULL
  _etblGLmSCOAAccounts_iModifiedAgentID int NULL
  _etblGLmSCOAAccounts_iChangeSetID int NULL
  _etblGLmSCOAAccounts_Checksum binary(20) NULL
  imSCOAVerID int NOT NULL default (0)

## _etblGLmSCOAGLAccVerLinks
PK: idGLAccVerLink
Columns (12):
  idGLAccVerLink int NOT NULL identity PK
  iGLAccountID int NOT NULL
  imSCOAVersionID int NOT NULL
  _etblGLmSCOAGLAccVerLinks_iBranchID int NULL
  _etblGLmSCOAGLAccVerLinks_dCreatedDate datetime NULL
  _etblGLmSCOAGLAccVerLinks_dModifiedDate datetime NULL
  _etblGLmSCOAGLAccVerLinks_iCreatedBranchID int NULL
  _etblGLmSCOAGLAccVerLinks_iModifiedBranchID int NULL
  _etblGLmSCOAGLAccVerLinks_iCreatedAgentID int NULL
  _etblGLmSCOAGLAccVerLinks_iModifiedAgentID int NULL
  _etblGLmSCOAGLAccVerLinks_iChangeSetID int NULL
  _etblGLmSCOAGLAccVerLinks_Checksum binary(20) NULL

## _etblGLmSCOAVersions
PK: idmSCOAVersion
Columns (13):
  idmSCOAVersion int NOT NULL identity PK
  cVersionDescription varchar(50) NOT NULL
  bTransactingVersion bit NOT NULL default (0)
  bActive bit NOT NULL default (1)
  _etblGLmSCOAVersions_iBranchID int NULL
  _etblGLmSCOAVersions_dCreatedDate datetime NULL
  _etblGLmSCOAVersions_dModifiedDate datetime NULL
  _etblGLmSCOAVersions_iCreatedBranchID int NULL
  _etblGLmSCOAVersions_iModifiedBranchID int NULL
  _etblGLmSCOAVersions_iCreatedAgentID int NULL
  _etblGLmSCOAVersions_iModifiedAgentID int NULL
  _etblGLmSCOAVersions_iChangeSetID int NULL
  _etblGLmSCOAVersions_Checksum binary(20) NULL

## _etblGLProjectBalances - GL Project Balance
Alias: GL Project Balance | Freedom Name:  | Record Identifier: 
Notes: GL Project Balance
Columns: none recorded yet (table seen in another Evolution database, not in the scripted one)

## _etblGLProjectBudgets - GL Project Budget
Alias: GL Project Budget | Freedom Name:  | Record Identifier: 
Notes: GL Project Budget
Columns: none recorded yet (table seen in another Evolution database, not in the scripted one)

## _etblGLProjectPrevBalances - GL Project Previous Balance
Alias: GL Project Previous Balance | Freedom Name:  | Record Identifier: 
Notes: GL Project Previous Balance
Columns: none recorded yet (table seen in another Evolution database, not in the scripted one)

## _etblGLReportCategory - GL Report Category (GeneralLedgerReportCategory)
Alias: GL Report Category | Freedom Name: GeneralLedgerReportCategory | Record Identifier: 
Notes: GL Report Category
PK: idReportCategory
Columns (12):
  idReportCategory int NOT NULL identity PK
  cCode varchar(40) NOT NULL
  cDescription varchar(100) NULL
  _etblGLReportCategory_iBranchID int NULL
  _etblGLReportCategory_dCreatedDate datetime NULL
  _etblGLReportCategory_dModifiedDate datetime NULL
  _etblGLReportCategory_iCreatedBranchID int NULL
  _etblGLReportCategory_iModifiedBranchID int NULL
  _etblGLReportCategory_iCreatedAgentID int NULL
  _etblGLReportCategory_iModifiedAgentID int NULL
  _etblGLReportCategory_iChangeSetID int NULL
  _etblGLReportCategory_Checksum binary(20) NULL

## _etblGLReviseBudget - GL Revised Budget (GeneralLedgerReviseBudget)
Alias: GL Revised Budget | Freedom Name: GeneralLedgerReviseBudget | Record Identifier: 
Notes: GL Revised Budget. Updated Budgets
PK: idGLReviseBudget
Columns (23):
  idGLReviseBudget int NOT NULL identity PK
  iGLAccountID int NOT NULL
  iProjectID int NOT NULL default (0)
  iPeriod int NOT NULL
  fNewBudget float NOT NULL default (0)
  fOldBudget float NOT NULL default (0)
  cReason varchar(50) NOT NULL
  dDate datetime NOT NULL
  iAgentID int NOT NULL
  iTxBranchRevisedBudgetID int NOT NULL default (0)
  _etblGLReviseBudget_iBranchID int NULL
  _etblGLReviseBudget_dCreatedDate datetime NULL
  _etblGLReviseBudget_dModifiedDate datetime NULL
  _etblGLReviseBudget_iCreatedBranchID int NULL
  _etblGLReviseBudget_iModifiedBranchID int NULL
  _etblGLReviseBudget_iCreatedAgentID int NULL
  _etblGLReviseBudget_iModifiedAgentID int NULL
  _etblGLReviseBudget_iChangeSetID int NULL
  _etblGLReviseBudget_Checksum binary(20) NULL
  fNewBudgetForeign float NOT NULL default (0)
  fOldBudgetForeign float NOT NULL default (0)
  fNewBudgetCurrency float NOT NULL default (0)
  fOldBudgetCurrency float NOT NULL default (0)

## _etblGLReviseBudgetPrev - GL Revised Budget Previous
Alias: GL Revised Budget Previous | Freedom Name:  | Record Identifier: 
Notes: GL Revised Budget Previous. Prior year Revised Budgets
PK: idGLReviseBudgetPrev
Columns (22):
  idGLReviseBudgetPrev int NOT NULL identity PK
  iGLAccountPrevID int NOT NULL
  iProjectPrevID int NOT NULL
  iPeriodPrevID int NOT NULL
  fNewBudgetPrev float NULL
  fOldBudgetPrev float NULL
  cReasonPrev varchar(50) NOT NULL
  dDatePrev datetime NULL
  iAgentIDPrev int NULL
  _etblGLReviseBudgetPrev_iBranchID int NULL
  _etblGLReviseBudgetPrev_dCreatedDate datetime NULL
  _etblGLReviseBudgetPrev_dModifiedDate datetime NULL
  _etblGLReviseBudgetPrev_iCreatedBranchID int NULL
  _etblGLReviseBudgetPrev_iModifiedBranchID int NULL
  _etblGLReviseBudgetPrev_iCreatedAgentID int NULL
  _etblGLReviseBudgetPrev_iModifiedAgentID int NULL
  _etblGLReviseBudgetPrev_iChangeSetID int NULL
  _etblGLReviseBudgetPrev_Checksum binary(20) NULL
  fNewBudgetPrevForeign float NOT NULL default (0)
  fOldBudgetPrevForeign float NOT NULL default (0)
  fNewBudgetPrevCurrency float NOT NULL default (0)
  fOldBudgetPrevCurrency float NOT NULL default (0)

## _etblGLSegment - General Ledger Segment (GeneralLedgerSegment)
Alias: General Ledger Segment | Freedom Name: GeneralLedgerSegment | Record Identifier: 
Notes: General Ledger Segment. Only applicable on Segmented General Ledger Structure
PK: idSegment
Columns (16):
  idSegment int NOT NULL identity PK
  iSegmentNo int NOT NULL
  cCode varchar(40) NOT NULL
  cDescription varchar(40) NULL
  iSegmentBranchID int NULL
  _etblGLSegment_iBranchID int NULL
  _etblGLSegment_dCreatedDate datetime NULL
  _etblGLSegment_dModifiedDate datetime NULL
  _etblGLSegment_iCreatedBranchID int NULL
  _etblGLSegment_iModifiedBranchID int NULL
  _etblGLSegment_iCreatedAgentID int NULL
  _etblGLSegment_iModifiedAgentID int NULL
  _etblGLSegment_iChangeSetID int NULL
  _etblGLSegment_Checksum binary(20) NULL
  imSCOAAccountID int NULL
  mSCOAId varchar(50) NULL

## _etblGLSegmentSetup - General Ledger Segment Setup (GeneralLedgerSegmentSetup)
Alias: General Ledger Segment Setup | Freedom Name: GeneralLedgerSegmentSetup | Record Identifier: 
Notes: General Ledger Segment Setup. Only applicable on Segmented General Ledger Structure
PK: idSegmentNo
Columns (16):
  idSegmentNo int NOT NULL PK
  bForceValue bit NOT NULL default (0)
  bSegmentUsed bit NOT NULL default (0)
  cSegmentLabel varchar(35) NOT NULL
  cSegmentMask varchar(40) NULL
  bInUse bit NOT NULL default (1)
  bIsBranchSegment bit NOT NULL default (0)
  _etblGLSegmentSetup_iBranchID int NULL
  _etblGLSegmentSetup_dCreatedDate datetime NULL
  _etblGLSegmentSetup_dModifiedDate datetime NULL
  _etblGLSegmentSetup_iCreatedBranchID int NULL
  _etblGLSegmentSetup_iModifiedBranchID int NULL
  _etblGLSegmentSetup_iCreatedAgentID int NULL
  _etblGLSegmentSetup_iModifiedAgentID int NULL
  _etblGLSegmentSetup_iChangeSetID int NULL
  _etblGLSegmentSetup_Checksum binary(20) NULL

## _etblGSTPrepayments
PK: idGSTPrepayments
Columns (26):
  idGSTPrepayments int NOT NULL identity PK
  iPostARPrepayID int NULL
  iPostARInvID int NULL
  iTaxPeriodID int NULL
  fAmount float NULL
  fTaxAmount float NULL
  _etblGSTPrepayments_iBranchID int NULL
  _etblGSTPrepayments_dCreatedDate datetime NULL
  _etblGSTPrepayments_dModifiedDate datetime NULL
  _etblGSTPrepayments_iCreatedBranchID int NULL
  _etblGSTPrepayments_iModifiedBranchID int NULL
  _etblGSTPrepayments_iCreatedAgentID int NULL
  _etblGSTPrepayments_iModifiedAgentID int NULL
  _etblGSTPrepayments_iChangeSetID int NULL
  _etblGSTPrepayments_Checksum binary(20) NULL
  TxDate datetime NOT NULL default getdate()
  iUnallocTaxPeriodID int NOT NULL default (0)
  fAmountForeign float NOT NULL default (0)
  fTaxAmountForeign float NOT NULL default (0)
  fUnAllocAmountForeign float NOT NULL default (0)
  fUnAllocTaxAmountForeign float NOT NULL default (0)
  AllocTxDate datetime NOT NULL default getdate()
  fUnAllocAmount float NOT NULL default (0)
  fUnAllocTaxAmount float NOT NULL default (0)
  UnallocTxDate datetime NULL
  iAllocatedInvID bigint NOT NULL default (0)

## _etblGSTReturnProcess
PK: idGSTReturnProcess
Columns (24):
  idGSTReturnProcess int NOT NULL identity PK
  iStatusID int NULL
  iTaxPeriodID int NULL
  iCreatedUserID int NULL
  iFinalizedUserID int NULL
  iVersion int NULL
  nGSTReturnDoc image NULL
  _etblGSTReturnProcess_iBranchID int NULL
  _etblGSTReturnProcess_dCreatedDate datetime NULL
  _etblGSTReturnProcess_dModifiedDate datetime NULL
  _etblGSTReturnProcess_iCreatedBranchID int NULL
  _etblGSTReturnProcess_iModifiedBranchID int NULL
  _etblGSTReturnProcess_iCreatedAgentID int NULL
  _etblGSTReturnProcess_iModifiedAgentID int NULL
  _etblGSTReturnProcess_iChangeSetID int NULL
  _etblGSTReturnProcess_Checksum binary(20) NULL
  cAuthorisedName varchar(1) NULL
  cNationality varchar(1) NULL
  cNewIDCard varchar(1) NULL
  cOldIDCard varchar(1) NULL
  cPassport varchar(1) NULL
  dDate datetime NULL
  bCarryForwardRefund bit NOT NULL
  bMalaysian bit NOT NULL default (1)

## _etblImportDeclaration
PK: idImportDeclaration
Columns (32):
  idImportDeclaration int NOT NULL identity PK
  cImportDeclarationNo nvarchar(50) NOT NULL
  cImportDeclarationShipNo nvarchar(50) NOT NULL
  dImpDate datetime NOT NULL
  iVendorID int NOT NULL
  iCurrencyID int NOT NULL
  cPurchDescr nvarchar(100) NULL
  cInvList text NOT NULL
  fTotalAmount float NULL default (0)
  fForeignTotalAmount float NULL default (0)
  fExRate float NULL default (0)
  fGSTAmount float NULL default (0)
  iTaxCodeID int NOT NULL
  iTaxRate float NULL default (0)
  fTaxAmount float NULL default (0)
  iDocStatus int NULL
  _etblImportDeclaration_iBranchID int NULL
  _etblImportDeclaration_dCreatedDate datetime NULL
  _etblImportDeclaration_dModifiedDate datetime NULL
  _etblImportDeclaration_iCreatedBranchID int NULL
  _etblImportDeclaration_iModifiedBranchID int NULL
  _etblImportDeclaration_iCreatedAgentID int NULL
  _etblImportDeclaration_iModifiedAgentID int NULL
  _etblImportDeclaration_iChangeSetID int NULL
  _etblImportDeclaration_Checksum binary(20) NULL
  cAuditNumber nvarchar(50) NULL
  iForAgentID int NOT NULL default (0)
  cReversalReason nvarchar(100) NULL
  dReversalDate datetime NULL
  cReversalAuditNumber nvarchar(50) NULL
  iInvNumID bigint NOT NULL default (0)
  iTaxPeriodID int NOT NULL default (0)

## _etblImportDeclarationLine
PK: idImportDeclarationLine
Columns (18):
  idImportDeclarationLine int NOT NULL identity PK
  iImportDeclarationID int NOT NULL
  iImportDeclItemID int NOT NULL
  fTotalAmount float NULL default (0)
  fForeignTotalAmount float NULL default (0)
  fExRate float NULL default (0)
  cCostItemDesc nvarchar(50) NULL
  cRemarks nvarchar(100) NULL
  _etblImportDeclarationLine_iBranchID int NULL
  _etblImportDeclarationLine_dCreatedDate datetime NULL
  _etblImportDeclarationLine_dModifiedDate datetime NULL
  _etblImportDeclarationLine_iCreatedBranchID int NULL
  _etblImportDeclarationLine_iModifiedBranchID int NULL
  _etblImportDeclarationLine_iCreatedAgentID int NULL
  _etblImportDeclarationLine_iModifiedAgentID int NULL
  _etblImportDeclarationLine_iChangeSetID int NULL
  _etblImportDeclarationLine_Checksum binary(20) NULL
  iAccountLinkID int NOT NULL default (0)

## _etblImportDeclItems
PK: idImportDeclItems
Columns (11):
  idImportDeclItems int NOT NULL identity PK
  cImportDeclName nvarchar(50) NOT NULL
  _etblImportDeclItems_iBranchID int NULL
  _etblImportDeclItems_dCreatedDate datetime NULL
  _etblImportDeclItems_dModifiedDate datetime NULL
  _etblImportDeclItems_iCreatedBranchID int NULL
  _etblImportDeclItems_iModifiedBranchID int NULL
  _etblImportDeclItems_iCreatedAgentID int NULL
  _etblImportDeclItems_iModifiedAgentID int NULL
  _etblImportDeclItems_iChangeSetID int NULL
  _etblImportDeclItems_Checksum binary(20) NULL

## _etblImportDeclItemsGLLink
PK: idImportDeclItemsGLLink
Columns (12):
  idImportDeclItemsGLLink int NOT NULL identity PK
  iImportDeclItemID int NOT NULL
  iAccountLinkID int NOT NULL
  _etblImportDeclItemsGLLink_iBranchID int NULL
  _etblImportDeclItemsGLLink_dCreatedDate datetime NULL
  _etblImportDeclItemsGLLink_dModifiedDate datetime NULL
  _etblImportDeclItemsGLLink_iCreatedBranchID int NULL
  _etblImportDeclItemsGLLink_iModifiedBranchID int NULL
  _etblImportDeclItemsGLLink_iCreatedAgentID int NULL
  _etblImportDeclItemsGLLink_iModifiedAgentID int NULL
  _etblImportDeclItemsGLLink_iChangeSetID int NULL
  _etblImportDeclItemsGLLink_Checksum binary(20) NULL

## _etblIncidentSourceDocLinks - Incident Source Document Links
Alias: Incident Source Document Links | Freedom Name:  | Record Identifier: 
Notes: Incident Source Document Links
PK: idIncidentSourceDocLinks
Columns (12):
  idIncidentSourceDocLinks int NOT NULL identity PK
  iIncidentID int NOT NULL
  iSourceDocID bigint NULL
  _etblIncidentSourceDocLinks_iBranchID int NULL
  _etblIncidentSourceDocLinks_dCreatedDate datetime NULL
  _etblIncidentSourceDocLinks_dModifiedDate datetime NULL
  _etblIncidentSourceDocLinks_iCreatedBranchID int NULL
  _etblIncidentSourceDocLinks_iModifiedBranchID int NULL
  _etblIncidentSourceDocLinks_iCreatedAgentID int NULL
  _etblIncidentSourceDocLinks_iModifiedAgentID int NULL
  _etblIncidentSourceDocLinks_iChangeSetID int NULL
  _etblIncidentSourceDocLinks_Checksum binary(20) NULL

## _etblInstructionTypes
PK: iInstructionTypeID
Columns (12):
  iInstructionTypeID int NOT NULL identity PK
  cDescription varchar(50) NULL
  cEFTSOutValue varchar(50) NULL
  _etblInstructionTypes_iBranchID int NULL
  _etblInstructionTypes_dCreatedDate datetime NULL
  _etblInstructionTypes_dModifiedDate datetime NULL
  _etblInstructionTypes_iCreatedBranchID int NULL
  _etblInstructionTypes_iModifiedBranchID int NULL
  _etblInstructionTypes_iCreatedAgentID int NULL
  _etblInstructionTypes_iModifiedAgentID int NULL
  _etblInstructionTypes_iChangeSetID int NULL
  _etblInstructionTypes_Checksum binary(20) NULL

## _etblInvCostTracking - Inv Cost Tracking
Alias: Inv Cost Tracking | Freedom Name:  | Record Identifier: 
Notes: Inventory Cost Tracking
PK: idCostTracking
Columns (15):
  idCostTracking bigint NOT NULL identity PK
  iStockID int NOT NULL
  iWarehouseID int NOT NULL
  iLotID int NOT NULL
  iAutoIdx bigint NOT NULL
  dTxDate datetime NOT NULL
  dDateStamp datetime NOT NULL
  fAverageCost float NOT NULL
  fLatestCost float NOT NULL
  fLowestCost float NOT NULL
  fHighestCost float NOT NULL
  fManualCost float NOT NULL
  fQtyOnHand float NOT NULL
  fJobQty float NOT NULL
  fMFPQty float NOT NULL

## _etblInvImages - Inventory Image (InventoryImages)
Alias: Inventory Image | Freedom Name: InventoryImages | Record Identifier: 
Notes: Inventory Image
PK: idInvImage
Columns (23):
  idInvImage int NOT NULL identity PK
  iStockLink int NOT NULL
  nInvImage image NULL
  cInvImageType varchar(10) NULL
  cInvImageDesc varchar(50) NULL
  bDisplayProportion bit NULL
  bDisplayStretch bit NULL
  iWidth int NULL
  iHeight int NULL
  cActualType varchar(20) NULL
  fLongtitude float NULL
  fLatitude float NULL
  fSize float NULL
  cTitle varchar(50) NULL
  _etblInvImages_iBranchID int NULL
  _etblInvImages_dCreatedDate datetime NULL
  _etblInvImages_dModifiedDate datetime NULL
  _etblInvImages_iCreatedBranchID int NULL
  _etblInvImages_iModifiedBranchID int NULL
  _etblInvImages_iCreatedAgentID int NULL
  _etblInvImages_iModifiedAgentID int NULL
  _etblInvImages_iChangeSetID int NULL
  _etblInvImages_Checksum binary(20) NULL

## _etblInvJrBatches
PK: IDInvJrBatches
Columns (31):
  IDInvJrBatches int NOT NULL identity PK
  cInvJrNumber varchar(50) NULL
  cInvJrDescription varchar(40) NULL
  cInvJrReference varchar(50) NULL
  iCreateAgentID int NOT NULL default (0)
  bClearAfterPost bit NOT NULL default (1)
  bAllowDupRef bit NOT NULL default (1)
  bAllowEditGLContra bit NOT NULL default (0)
  iNewLineDateOpt int NULL
  dNewLineDateDef datetime NULL
  iNewLineRefOpt int NULL
  cNewLineRefDef varchar(20) NULL
  bNewLineRefInc bit NOT NULL default (0)
  iNewLineDescOpt int NULL
  cNewLineDescDef varchar(40) NULL
  bNewLineDescInc bit NOT NULL default (0)
  iNewLineProjectOpt int NULL
  iNewLineProjectDefID int NOT NULL default (0)
  iNewLineWarehouseOpt int NULL
  iNewLineWarehouseDefID int NOT NULL default (0)
  bJustCleared bit NOT NULL default (0)
  iTransactionCode int NULL
  _etblInvJrBatches_iBranchID int NULL
  _etblInvJrBatches_dCreatedDate datetime NULL
  _etblInvJrBatches_dModifiedDate datetime NULL
  _etblInvJrBatches_iCreatedBranchID int NULL
  _etblInvJrBatches_iModifiedBranchID int NULL
  _etblInvJrBatches_iCreatedAgentID int NULL
  _etblInvJrBatches_iModifiedAgentID int NULL
  _etblInvJrBatches_iChangeSetID int NULL
  _etblInvJrBatches_Checksum binary(20) NULL

## _etblInvJrBatchLineDetails
PK: idInvJrBatchLineDetails
Columns (21):
  idInvJrBatchLineDetails bigint NOT NULL identity PK
  iInvJrLDBatchID bigint NOT NULL
  iInvJrLDBatchLineID bigint NOT NULL
  iSNGroupID int NOT NULL
  iLotID int NOT NULL default (0)
  cLotNumber varchar(50) NOT NULL default ''
  dLotExpiryDate datetime NULL
  iStockBinLocationID int NOT NULL default (0)
  iUnitsOfMeasureID int NOT NULL default (0)
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL
  fQuantity float NOT NULL default (0)
  _etblInvJrBatchLineDetails_iBranchID int NULL
  _etblInvJrBatchLineDetails_dCreatedDate datetime NULL
  _etblInvJrBatchLineDetails_dModifiedDate datetime NULL
  _etblInvJrBatchLineDetails_iCreatedBranchID int NULL
  _etblInvJrBatchLineDetails_iModifiedBranchID int NULL
  _etblInvJrBatchLineDetails_iCreatedAgentID int NULL
  _etblInvJrBatchLineDetails_iModifiedAgentID int NULL
  _etblInvJrBatchLineDetails_iChangeSetID int NULL
  _etblInvJrBatchLineDetails_Checksum binary(20) NULL

## _etblInvJrBatchLines - Inventory Journal Batch Line
Alias: Inventory Journal Batch Line | Freedom Name:  | Record Identifier: 
Notes: Inventory Journal Batch Line
PK: idInvJrBatchLines+iInvJrBatchID
Columns (29):
  idInvJrBatchLines int NOT NULL identity PK
  iInvJrBatchID int NOT NULL PK
  iStockID int NOT NULL
  iWarehouseID int NOT NULL default (0)
  dTrDate datetime NOT NULL
  iTrCodeID int NOT NULL
  iGLContraID int NOT NULL default (0)
  cReference varchar(20) NULL
  cDescription varchar(40) NULL
  fQtyIn float NULL
  fQtyOut float NULL
  fNewCost float NULL
  iProjectID int NOT NULL default (0)
  bIsSerialItem bit NOT NULL default (0)
  bIsLotItem bit NOT NULL default (0)
  iJobID int NOT NULL default (0)
  cLineNotes varchar(1024) NULL
  iUnitsOfMeasureStockingID int NULL
  iUnitsOfMeasureCategoryID int NULL
  _etblInvJrBatchLines_iBranchID int NULL
  _etblInvJrBatchLines_dCreatedDate datetime NULL
  _etblInvJrBatchLines_dModifiedDate datetime NULL
  _etblInvJrBatchLines_iCreatedBranchID int NULL
  _etblInvJrBatchLines_iModifiedBranchID int NULL
  _etblInvJrBatchLines_iCreatedAgentID int NULL
  _etblInvJrBatchLines_iModifiedAgentID int NULL
  _etblInvJrBatchLines_iChangeSetID int NULL
  _etblInvJrBatchLines_Checksum binary(20) NULL
  bMatrixEntry bit NOT NULL default (0)

## _etblInvJrBatchLineSN - Inventory Journal Batch Line Serial Number
Alias: Inventory Journal Batch Line Serial Number | Freedom Name:  | Record Identifier: 
Notes: Inventory Journal Batch Line Serial Number
PK: none
Columns (14):
  IDInvJrBatchLineSN int NOT NULL identity
  iInvJrBatchID int NULL
  iSNGroupID int NULL
  iSerialMFID int NULL
  cSerialNumber varchar(50) NULL
  _etblInvJrBatchLineSN_iBranchID int NULL
  _etblInvJrBatchLineSN_dCreatedDate datetime NULL
  _etblInvJrBatchLineSN_dModifiedDate datetime NULL
  _etblInvJrBatchLineSN_iCreatedBranchID int NULL
  _etblInvJrBatchLineSN_iModifiedBranchID int NULL
  _etblInvJrBatchLineSN_iCreatedAgentID int NULL
  _etblInvJrBatchLineSN_iModifiedAgentID int NULL
  _etblInvJrBatchLineSN_iChangeSetID int NULL
  _etblInvJrBatchLineSN_Checksum binary(20) NULL

## _etblInvoiceDeposits
PK: idInvoiceDeposits
Columns (15):
  idInvoiceDeposits int NOT NULL identity PK
  iInvoiceID bigint NULL
  fDepositAmount float NULL
  fUnallocatedAmount float NULL
  iPostARID bigint NULL
  iInvoiceIDOrig bigint NULL
  _etblInvoiceDeposits_iBranchID int NULL
  _etblInvoiceDeposits_dCreatedDate datetime NULL
  _etblInvoiceDeposits_dModifiedDate datetime NULL
  _etblInvoiceDeposits_iCreatedBranchID int NULL
  _etblInvoiceDeposits_iModifiedBranchID int NULL
  _etblInvoiceDeposits_iCreatedAgentID int NULL
  _etblInvoiceDeposits_iModifiedAgentID int NULL
  _etblInvoiceDeposits_iChangeSetID int NULL
  _etblInvoiceDeposits_Checksum binary(20) NULL

## _etblInvPriceUpdateBatches
PK: idInvPriceUpdateBatches
Columns (34):
  idInvPriceUpdateBatches int NOT NULL identity PK
  cInvPriceUpdateNumber varchar(50) NULL
  cInvPriceUpdateDescription varchar(40) NULL
  cInvPriceUpdateReference varchar(50) NULL
  cStartCode varchar(255) NULL
  cEndCode varchar(255) NULL
  cGroups varchar(1024) NULL
  cWarehouses varchar(1024) NULL
  bUpdateAllWarehouses bit NOT NULL default (0)
  bSalesWarehouses bit NOT NULL default (0)
  bIgnoreInactive bit NOT NULL default (1)
  cPriceLists varchar(1024) NULL
  iUpdateType int NULL
  iUpdateAction int NULL
  iRounding int NULL
  iToNearest int NULL
  bPosted bit NOT NULL default (0)
  _etblInvPriceUpdateBatches_iBranchID int NULL
  _etblInvPriceUpdateBatches_dCreatedDate datetime NULL
  _etblInvPriceUpdateBatches_dModifiedDate datetime NULL
  _etblInvPriceUpdateBatches_iCreatedBranchID int NULL
  _etblInvPriceUpdateBatches_iModifiedBranchID int NULL
  _etblInvPriceUpdateBatches_iCreatedAgentID int NULL
  _etblInvPriceUpdateBatches_iModifiedAgentID int NULL
  _etblInvPriceUpdateBatches_iChangeSetID int NULL
  _etblInvPriceUpdateBatches_Checksum binary(20) NULL
  cAttributeGroups nvarchar(max) NULL
  cAttributeTypes nvarchar(max) NULL
  xAttributeFilterValues xml NULL
  bOnlyGlobalPrices bit NOT NULL default (0)
  bOnlyExistingPrices bit NOT NULL default (0)
  bBatchScheduling bit NOT NULL default (0)
  bBatchValidated bit NOT NULL default (0)
  bCreatePUBFromImport bit NOT NULL default (0)

## _etblInvPriceUpdateBatchLines
PK: idInvPriceUpdateBatchLines
Columns (31):
  idInvPriceUpdateBatchLines int NOT NULL identity PK
  iInvPriceUpdateBatchID int NOT NULL
  iStockID int NOT NULL
  iWarehouseID int NOT NULL default (0)
  iPriceListID int NOT NULL
  fExclPrice float NULL
  fInclPrice float NULL
  iCostMethod int NULL
  fUnitCost float NULL
  fGrossMargin float NULL
  fGMPercentage float NULL
  iUpdateType int NULL
  iUpdateAction int NULL
  fPercentageChange float NULL
  iRounding int NULL
  iToNearest int NULL
  fUpdatePrice float NULL
  fNewExclPrice float NULL
  fNewInclPrice float NULL
  fNewGrossMargin float NULL
  fNewGMPercentage float NULL
  _etblInvPriceUpdateBatchLines_iBranchID int NULL
  _etblInvPriceUpdateBatchLines_dCreatedDate datetime NULL
  _etblInvPriceUpdateBatchLines_dModifiedDate datetime NULL
  _etblInvPriceUpdateBatchLines_iCreatedBranchID int NULL
  _etblInvPriceUpdateBatchLines_iModifiedBranchID int NULL
  _etblInvPriceUpdateBatchLines_iCreatedAgentID int NULL
  _etblInvPriceUpdateBatchLines_iModifiedAgentID int NULL
  _etblInvPriceUpdateBatchLines_iChangeSetID int NULL
  _etblInvPriceUpdateBatchLines_Checksum binary(20) NULL
  xAttribute xml NULL

## _etblInvSegGroup - Inventory Segment Group (InventorySegmentGroup)
Alias: Inventory Segment Group | Freedom Name: InventorySegmentGroup | Record Identifier: 
Notes: Inventory Segment Group
PK: idInvSegGroup
Columns (12):
  idInvSegGroup int NOT NULL identity PK
  iInvSegTypeID int NOT NULL
  cDescription varchar(50) NULL
  _etblInvSegGroup_iBranchID int NULL
  _etblInvSegGroup_dCreatedDate datetime NULL
  _etblInvSegGroup_dModifiedDate datetime NULL
  _etblInvSegGroup_iCreatedBranchID int NULL
  _etblInvSegGroup_iModifiedBranchID int NULL
  _etblInvSegGroup_iCreatedAgentID int NULL
  _etblInvSegGroup_iModifiedAgentID int NULL
  _etblInvSegGroup_iChangeSetID int NULL
  _etblInvSegGroup_Checksum binary(20) NULL

## _etblInvSegType - Inventory Segment Type (InventorySegmentType)
Alias: Inventory Segment Type | Freedom Name: InventorySegmentType | Record Identifier: 
Notes: Inventory Segment Type
PK: idInvSegType
Columns (11):
  idInvSegType int NOT NULL identity PK
  cDescription varchar(50) NULL
  _etblInvSegType_iBranchID int NULL
  _etblInvSegType_dCreatedDate datetime NULL
  _etblInvSegType_dModifiedDate datetime NULL
  _etblInvSegType_iCreatedBranchID int NULL
  _etblInvSegType_iModifiedBranchID int NULL
  _etblInvSegType_iCreatedAgentID int NULL
  _etblInvSegType_iModifiedAgentID int NULL
  _etblInvSegType_iChangeSetID int NULL
  _etblInvSegType_Checksum binary(20) NULL

## _etblInvSegValue - Inventory Segment Value (InventorySegmentValue)
Alias: Inventory Segment Value | Freedom Name: InventorySegmentValue | Record Identifier: cValue
Notes: Inventory Segment Value
PK: idInvSegValue
Columns (13):
  idInvSegValue int NOT NULL identity PK
  iInvSegGroupID int NOT NULL
  cValue varchar(50) NULL
  cDescription varchar(50) NULL
  _etblInvSegValue_iBranchID int NULL
  _etblInvSegValue_dCreatedDate datetime NULL
  _etblInvSegValue_dModifiedDate datetime NULL
  _etblInvSegValue_iCreatedBranchID int NULL
  _etblInvSegValue_iModifiedBranchID int NULL
  _etblInvSegValue_iCreatedAgentID int NULL
  _etblInvSegValue_iModifiedAgentID int NULL
  _etblInvSegValue_iChangeSetID int NULL
  _etblInvSegValue_Checksum binary(20) NULL

## _etblLotStatus - Inventory Lot Status (LotTrackingStatus)
Alias: Inventory Lot Status | Freedom Name: LotTrackingStatus | Record Identifier: cLotStatusDescription
Notes: Inventory Lot Status
PK: idLotStatus
Columns (13):
  idLotStatus int NOT NULL identity PK
  cLotStatusDescription varchar(50) NULL
  bAllowPurchases bit NOT NULL default (1)
  bAllowSales bit NOT NULL default (1)
  _etblLotStatus_iBranchID int NULL
  _etblLotStatus_dCreatedDate datetime NULL
  _etblLotStatus_dModifiedDate datetime NULL
  _etblLotStatus_iCreatedBranchID int NULL
  _etblLotStatus_iModifiedBranchID int NULL
  _etblLotStatus_iCreatedAgentID int NULL
  _etblLotStatus_iModifiedAgentID int NULL
  _etblLotStatus_iChangeSetID int NULL
  _etblLotStatus_Checksum binary(20) NULL

## _etblLotTracking - Inventory Lot Tracking (LotTracking)
Alias: Inventory Lot Tracking | Freedom Name: LotTracking | Record Identifier: cLotDescription
Notes: Inventory Lot Tracking
PK: idLotTracking
Columns (16):
  idLotTracking int NOT NULL identity PK
  cLotDescription varchar(50) NULL
  iStockID int NULL
  iLotStatusID int NULL
  dExpiryDate datetime NULL
  bIsActive bit NOT NULL default (1)
  dLastGRVDate datetime NULL
  _etblLotTracking_iBranchID int NULL
  _etblLotTracking_dCreatedDate datetime NULL
  _etblLotTracking_dModifiedDate datetime NULL
  _etblLotTracking_iCreatedBranchID int NULL
  _etblLotTracking_iModifiedBranchID int NULL
  _etblLotTracking_iCreatedAgentID int NULL
  _etblLotTracking_iModifiedAgentID int NULL
  _etblLotTracking_iChangeSetID int NULL
  _etblLotTracking_Checksum binary(20) NULL

## _etblLotTrackingQty - Inventory Lot Tracking Quantity (LotTrackingQuantities)
Alias: Inventory Lot Tracking Quantity | Freedom Name: LotTrackingQuantities | Record Identifier: 
Notes: Inventory Lot Tracking Quantity
PK: idLotTrackingQty
Columns (25):
  idLotTrackingQty int NOT NULL identity PK
  iLotTrackingID int NULL
  iWarehouseID int NULL
  fQtyOnHand float NULL
  fQtyPurchased float NULL
  fQtySold float NULL
  fQtyAdjustOut float NULL
  fQtyAdjustIn float NULL
  fQtyToSupplier float NULL
  fQtyFromClient float NULL
  fQtyFromWarehouse float NULL
  fQtyToWarehouse float NULL
  fQtyReserved float NULL
  fQtyJCWIP float NULL
  fQtyMFWIP float NULL
  _etblLotTrackingQty_iBranchID int NULL
  _etblLotTrackingQty_dCreatedDate datetime NULL
  _etblLotTrackingQty_dModifiedDate datetime NULL
  _etblLotTrackingQty_iCreatedBranchID int NULL
  _etblLotTrackingQty_iModifiedBranchID int NULL
  _etblLotTrackingQty_iCreatedAgentID int NULL
  _etblLotTrackingQty_iModifiedAgentID int NULL
  _etblLotTrackingQty_iChangeSetID int NULL
  _etblLotTrackingQty_Checksum binary(20) NULL
  iBinLocationID int NOT NULL default (0)

## _etblLotTrackingTx
PK: idLotTrackingTx
Columns (24):
  idLotTrackingTx bigint NOT NULL identity PK
  iLotTrackingID int NULL
  dLTTxDate datetime NULL
  iLTTxAccountID int NULL
  cLTTxReference varchar(50) NULL
  cLTTxReference2 varchar(50) NULL
  iLTTxTrCodeID int NULL
  iLTTxTransTypeID int NULL
  iLTTxWarehouseID int NULL
  cLTTxAuditNumber varchar(50) NULL
  dLTTxExpiryDate datetime NULL
  iLTTxStatusID int NULL
  fLTTxQty float NULL
  iTxBranchID int NULL
  _etblLotTrackingTx_iBranchID int NULL
  _etblLotTrackingTx_dCreatedDate datetime NULL
  _etblLotTrackingTx_dModifiedDate datetime NULL
  _etblLotTrackingTx_iCreatedBranchID int NULL
  _etblLotTrackingTx_iModifiedBranchID int NULL
  _etblLotTrackingTx_iCreatedAgentID int NULL
  _etblLotTrackingTx_iModifiedAgentID int NULL
  _etblLotTrackingTx_iChangeSetID int NULL
  _etblLotTrackingTx_Checksum binary(20) NULL
  iLTTxBinLocationID int NOT NULL default (0)

## _etblMajorIndustryCodes
PK: idMajorIndustryCode
Columns (13):
  idMajorIndustryCode int NOT NULL identity PK
  cMajorIndustryCode varchar(20) NOT NULL
  cMajorIndustryDescription varchar(100) NULL
  _etblMajorIndustryCodes_iBranchID int NULL
  _etblMajorIndustryCodes_dCreatedDate datetime NULL
  _etblMajorIndustryCodes_dModifiedDate datetime NULL
  _etblMajorIndustryCodes_iCreatedBranchID int NULL
  _etblMajorIndustryCodes_iModifiedBranchID int NULL
  _etblMajorIndustryCodes_iCreatedAgentID int NULL
  _etblMajorIndustryCodes_iModifiedAgentID int NULL
  _etblMajorIndustryCodes_iChangeSetID int NULL
  _etblMajorIndustryCodes_Checksum binary(20) NULL
  iMajorIndustryCategory int NULL default (0)

## _etblManufProcess
PK: idManufProcess
Columns (32):
  idManufProcess int NOT NULL identity PK
  iStatus char(1) NOT NULL
  cProcessRefNumber varchar(50) NOT NULL
  cOtherRefNumber varchar(50) NULL
  iBOMMasterID int NOT NULL
  cManufDescription varchar(50) NULL
  dCreated datetime NOT NULL
  dLastUpdated datetime NOT NULL
  fManufQuantity float NULL
  fQtyManufactured float NULL
  iProjectID int NULL
  iManufWarehouseID int NULL
  bOverrideCompWhse bit NOT NULL default (1)
  iInvoiceLineID bigint NOT NULL
  bIsLinkedToOrder bit NOT NULL default (0)
  iInvNumID bigint NULL
  iJCMasterID int NULL
  dProjectedCompletionDate datetime NULL
  dActualCompletionDate datetime NULL
  _etblManufProcess_fLeadDays float NULL
  _etblManufProcess_iBranchID int NULL
  _etblManufProcess_dCreatedDate datetime NULL
  _etblManufProcess_dModifiedDate datetime NULL
  _etblManufProcess_iCreatedBranchID int NULL
  _etblManufProcess_iModifiedBranchID int NULL
  _etblManufProcess_iCreatedAgentID int NULL
  _etblManufProcess_iModifiedAgentID int NULL
  _etblManufProcess_iChangeSetID int NULL
  _etblManufProcess_Checksum binary(20) NULL
  ucMANUInstructions varchar(250) NULL
  iBOMAttributeGroupID int NOT NULL default (0)
  xBOMAttribute xml NULL

## _etblManufProcessItem
PK: idManufProcessItem
Columns (22):
  idManufProcessItem bigint NOT NULL identity PK
  iMFPItemID float NULL
  iParentMFPItemID int NOT NULL
  iManufProcessID int NOT NULL
  iInvItemID int NULL
  cDescription varchar(50) NULL
  fProductionQty float NULL
  cUnitOfMeasure varchar(50) NULL
  fUnitCost float NULL
  bActive bit NOT NULL default (1)
  iDefaultWhseID int NULL
  _etblManufProcessItem_iBranchID int NULL
  _etblManufProcessItem_dCreatedDate datetime NULL
  _etblManufProcessItem_dModifiedDate datetime NULL
  _etblManufProcessItem_iCreatedBranchID int NULL
  _etblManufProcessItem_iModifiedBranchID int NULL
  _etblManufProcessItem_iCreatedAgentID int NULL
  _etblManufProcessItem_iModifiedAgentID int NULL
  _etblManufProcessItem_iChangeSetID int NULL
  _etblManufProcessItem_Checksum binary(20) NULL
  iDefaultStockBinID int NULL default (0)
  xDefaultAttribute xml NULL

## _etblManufProcessLine - Manufacture Process Line (ManufactureProcessLine)
Alias: Manufacture Process Line | Freedom Name: ManufactureProcessLine | Record Identifier: 
Notes: Manufacture Process Line
PK: idManufProcessLine
Columns (35):
  idManufProcessLine bigint NOT NULL identity PK
  iManufProcessID int NOT NULL
  iAction int NOT NULL
  iLineNo int NOT NULL
  cReference varchar(20) NULL
  iMFPItemID float NULL
  iInvItemID int NOT NULL
  iWarehouseID int NULL
  iNewInvItemID int NULL
  iNewWarehouseID int NULL
  fQuantity float NULL
  fCost float NULL
  bProcessed bit NOT NULL default (0)
  dTransactionDate datetime NULL
  dLastUpdateDate datetime NULL
  fQtyAvailable float NULL
  cDescription varchar(255) NULL
  iLotID int NULL
  iPickingSlipPrinted int NOT NULL default (0)
  iUnmanufactureLineNo int NOT NULL default (0)
  iDocVersion int NOT NULL default (0)
  fLineCost float NOT NULL default (0)
  _etblManufProcessLine_iBranchID int NULL
  _etblManufProcessLine_dCreatedDate datetime NULL
  _etblManufProcessLine_dModifiedDate datetime NULL
  _etblManufProcessLine_iCreatedBranchID int NULL
  _etblManufProcessLine_iModifiedBranchID int NULL
  _etblManufProcessLine_iCreatedAgentID int NULL
  _etblManufProcessLine_iModifiedAgentID int NULL
  _etblManufProcessLine_iChangeSetID int NULL
  _etblManufProcessLine_Checksum binary(20) NULL
  iStockBinLocationID int NULL default (0)
  iNewStockBinLocationID int NULL default (0)
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL

## _etblMCAgentCriteria - Info Alert Agent Criteria
Alias: Info Alert Agent Criteria | Freedom Name:  | Record Identifier: 
Notes: Info Alert Agent Criteria
PK: idAgentCriteria
Columns (41):
  idAgentCriteria int NOT NULL identity PK
  cAgentCriteriaDesc varchar(100) NULL
  cAgent varchar(50) NULL
  cModule varchar(40) NOT NULL
  cMonitorValue varchar(100) NOT NULL
  cOperator varchar(30) NULL
  cResultValue varchar(250) NULL
  cOwnResultValue varchar(50) NULL
  cSQL text NULL
  cFrequencyDescription varchar(50) NULL
  iFrequencyTimeInMin int NULL
  dFrequencyStartTime smalldatetime NULL
  dFrequencyEndTime smalldatetime NULL
  cNotificationFrequency varchar(1) NULL
  bNotifyTrayIcon bit NOT NULL default (0)
  bNotifyEmail bit NOT NULL default (0)
  bNotifySMS bit NOT NULL default (0)
  bLogNotification bit NOT NULL default (0)
  bAddToMyNotifications bit NOT NULL default (0)
  cEmailToAddress text NULL
  cEmailFromAddress varchar(60) NULL
  cEmailSubject varchar(120) NULL
  cEmailMessage text NULL
  cSMSToAddress text NULL
  cSMSMessage text NULL
  cTrayIconMessage text NULL
  cMyNotificationsMessage text NULL
  dLastNotificationDateTime smalldatetime NULL
  cProcessing varchar(1) NULL
  cEmailCC text NULL
  cEmailBcc text NULL
  iWarehouseID int NOT NULL default (0)
  _etblMCAgentCriteria_iBranchID int NULL
  _etblMCAgentCriteria_dCreatedDate datetime NULL
  _etblMCAgentCriteria_dModifiedDate datetime NULL
  _etblMCAgentCriteria_iCreatedBranchID int NULL
  _etblMCAgentCriteria_iModifiedBranchID int NULL
  _etblMCAgentCriteria_iCreatedAgentID int NULL
  _etblMCAgentCriteria_iModifiedAgentID int NULL
  _etblMCAgentCriteria_iChangeSetID int NULL
  _etblMCAgentCriteria_Checksum binary(20) NULL

## _etblMCAgentNotifications - Info Alert Agent Notification
Alias: Info Alert Agent Notification | Freedom Name:  | Record Identifier: 
Notes: Info Alert Agent Notification
PK: idAgentNotification
Columns (18):
  idAgentNotification int NOT NULL identity PK
  cAgent varchar(50) NULL
  AgentCriteriaID int NOT NULL
  cNotificationDesc varchar(50) NOT NULL
  cNotificationMessage varchar(1024) NOT NULL
  dNotificationDate smalldatetime NOT NULL
  bAcknowledged bit NOT NULL default (0)
  bProcessed bit NOT NULL default (0)
  cProcessActions varchar(1) NULL
  _etblMCAgentNotifications_iBranchID int NULL
  _etblMCAgentNotifications_dCreatedDate datetime NULL
  _etblMCAgentNotifications_dModifiedDate datetime NULL
  _etblMCAgentNotifications_iCreatedBranchID int NULL
  _etblMCAgentNotifications_iModifiedBranchID int NULL
  _etblMCAgentNotifications_iCreatedAgentID int NULL
  _etblMCAgentNotifications_iModifiedAgentID int NULL
  _etblMCAgentNotifications_iChangeSetID int NULL
  _etblMCAgentNotifications_Checksum binary(20) NULL

## _etblMCDefaultCriteria - Info Alert Default Criteria
Alias: Info Alert Default Criteria | Freedom Name:  | Record Identifier: 
Notes: Info Alert Default Criteria
PK: idDefaultCriteria
Columns (20):
  idDefaultCriteria int NOT NULL identity PK
  cModule varchar(100) NOT NULL
  cMonitorValue varchar(200) NOT NULL
  cMonitorField varchar(200) NULL
  cMonitorFieldType varchar(15) NULL
  cOperator varchar(30) NULL
  cResultValue varchar(1024) NULL
  cFieldsForResult varchar(1024) NULL
  cMessageValueDesc varchar(1024) NULL
  cMessageValueField varchar(1024) NULL
  cCriteriaSQLText varchar(1024) NULL
  _etblMCDefaultCriteria_iBranchID int NULL
  _etblMCDefaultCriteria_dCreatedDate datetime NULL
  _etblMCDefaultCriteria_dModifiedDate datetime NULL
  _etblMCDefaultCriteria_iCreatedBranchID int NULL
  _etblMCDefaultCriteria_iModifiedBranchID int NULL
  _etblMCDefaultCriteria_iCreatedAgentID int NULL
  _etblMCDefaultCriteria_iModifiedAgentID int NULL
  _etblMCDefaultCriteria_iChangeSetID int NULL
  _etblMCDefaultCriteria_Checksum binary(20) NULL

## _etblOrderCancelReason - Sales Order Cancel Reason
Alias: Sales Order Cancel Reason | Freedom Name:  | Record Identifier: cCancellationReasonCode
Notes: Sales Order Cancel Reason
PK: idOrderCancelReason
Columns (13):
  idOrderCancelReason int NOT NULL identity PK
  cCancellationReasonCode varchar(10) NULL
  cCancellationReasonDesc varchar(30) NOT NULL
  bActive bit NOT NULL default (1)
  _etblOrderCancelReason_iBranchID int NULL
  _etblOrderCancelReason_dCreatedDate datetime NULL
  _etblOrderCancelReason_dModifiedDate datetime NULL
  _etblOrderCancelReason_iCreatedBranchID int NULL
  _etblOrderCancelReason_iModifiedBranchID int NULL
  _etblOrderCancelReason_iCreatedAgentID int NULL
  _etblOrderCancelReason_iModifiedAgentID int NULL
  _etblOrderCancelReason_iChangeSetID int NULL
  _etblOrderCancelReason_Checksum binary(20) NULL

## _etblPaymentsBasedTax
PK: idPaymentsBasedTax
Columns (20):
  idPaymentsBasedTax int NOT NULL identity PK
  iFromPeriod int NULL
  iToPeriod int NULL
  dProcessDate datetime NULL
  cNumber varchar(50) NULL
  cDescription varchar(50) NULL
  cReference varchar(50) NULL
  iTrCodeID int NULL
  fExcludeLessThan float NULL
  bProcessed bit NOT NULL default (0)
  cProcessedAuditNumber varchar(50) NULL
  _etblPaymentsBasedTax_iBranchID int NULL
  _etblPaymentsBasedTax_dCreatedDate datetime NULL
  _etblPaymentsBasedTax_dModifiedDate datetime NULL
  _etblPaymentsBasedTax_iCreatedBranchID int NULL
  _etblPaymentsBasedTax_iModifiedBranchID int NULL
  _etblPaymentsBasedTax_iCreatedAgentID int NULL
  _etblPaymentsBasedTax_iModifiedAgentID int NULL
  _etblPaymentsBasedTax_iChangeSetID int NULL
  _etblPaymentsBasedTax_Checksum binary(20) NULL

## _etblPaymentsBasedTaxPayments
PK: idPaymentsBasedTaxPayments
Columns (22):
  idPaymentsBasedTaxPayments int NOT NULL identity PK
  iPBTBatchID int NULL
  iModule int NULL
  iAccountID int NULL
  iPostingID bigint NULL
  fExclusive float NULL
  fTax float NULL
  fInclusive float NULL
  iTaxTypeID int NULL
  iGLTaxAccountID int NULL
  cAllocatedToReference nvarchar(50) NULL
  iAllocatedPostingID bigint NULL default (0)
  iAllocatedStatus int NOT NULL default (0)
  _etblPaymentsBasedTaxPayments_iBranchID int NULL
  _etblPaymentsBasedTaxPayments_dCreatedDate datetime NULL
  _etblPaymentsBasedTaxPayments_dModifiedDate datetime NULL
  _etblPaymentsBasedTaxPayments_iCreatedBranchID int NULL
  _etblPaymentsBasedTaxPayments_iModifiedBranchID int NULL
  _etblPaymentsBasedTaxPayments_iCreatedAgentID int NULL
  _etblPaymentsBasedTaxPayments_iModifiedAgentID int NULL
  _etblPaymentsBasedTaxPayments_iChangeSetID int NULL
  _etblPaymentsBasedTaxPayments_Checksum binary(20) NULL

## _etblPeriod (Period)
Alias:  | Freedom Name: Period | Record Identifier: 
PK: idPeriod
Columns (15):
  idPeriod int NOT NULL PK
  dPeriodDate datetime NOT NULL
  bBlocked bit NOT NULL default (0)
  bPBTProcessed bit NOT NULL default (0)
  bPeriodProcessed bit NOT NULL default (0)
  iYearID int NOT NULL default (0)
  _etblPeriod_iBranchID int NULL
  _etblPeriod_dCreatedDate datetime NULL
  _etblPeriod_dModifiedDate datetime NULL
  _etblPeriod_iCreatedBranchID int NULL
  _etblPeriod_iModifiedBranchID int NULL
  _etblPeriod_iCreatedAgentID int NULL
  _etblPeriod_iModifiedAgentID int NULL
  _etblPeriod_iChangeSetID int NULL
  _etblPeriod_Checksum binary(20) NULL

## _etblPeriodTxIDs
PK: idPeriodTxIDs
Columns (19):
  idPeriodTxIDs int NOT NULL identity PK
  iTxModule int NOT NULL
  iTxPeriodID int NOT NULL
  iTxTaxClosePeriodID int NOT NULL
  iPostingTxID bigint NOT NULL
  iPostingTaxTypeID int NOT NULL
  fPostingExclusive float NOT NULL
  fPostingTax float NOT NULL
  fPostingInclusive float NOT NULL
  _etblPeriodTxIDs_iBranchID int NULL
  _etblPeriodTxIDs_dCreatedDate datetime NULL
  _etblPeriodTxIDs_dModifiedDate datetime NULL
  _etblPeriodTxIDs_iCreatedBranchID int NULL
  _etblPeriodTxIDs_iModifiedBranchID int NULL
  _etblPeriodTxIDs_iCreatedAgentID int NULL
  _etblPeriodTxIDs_iModifiedAgentID int NULL
  _etblPeriodTxIDs_iChangeSetID int NULL
  _etblPeriodTxIDs_Checksum binary(20) NULL
  iIncludedInTaxPeriodCloseID int NOT NULL default (0)

## _etblPeriodTxSummary
PK: idPeriodTxSummary
Columns (22):
  idPeriodTxSummary int NOT NULL identity PK
  dTaxPeriodClose datetime NOT NULL
  iTaxPeriodCloseID int NOT NULL
  fExclusiveTotal float NOT NULL
  fTaxTotal float NOT NULL
  fInclusiveTotal float NOT NULL
  iStatusID int NOT NULL
  dStatusUpdated datetime NULL
  _etblPeriodTxSummary_iBranchID int NULL
  _etblPeriodTxSummary_dCreatedDate datetime NULL
  _etblPeriodTxSummary_dModifiedDate datetime NULL
  _etblPeriodTxSummary_iCreatedBranchID int NULL
  _etblPeriodTxSummary_iModifiedBranchID int NULL
  _etblPeriodTxSummary_iCreatedAgentID int NULL
  _etblPeriodTxSummary_iModifiedAgentID int NULL
  _etblPeriodTxSummary_iChangeSetID int NULL
  _etblPeriodTxSummary_Checksum binary(20) NULL
  cIncludedTaxPeriodCloseIDs nvarchar(100) NOT NULL default (0)
  iSubmittedID int NOT NULL default (0)
  iSubmissionType int NOT NULL default (0)
  vbPdfFile varbinary(max) NULL
  bHasFiles bit NOT NULL default (0)

## _etblPeriodYear - Period Year (PeriodYear)
Alias: Period Year | Freedom Name: PeriodYear | Record Identifier: 
Notes: Period Year
PK: idYear
Columns (14):
  idYear int NOT NULL PK
  cYearDescription varchar(50) NOT NULL
  dYearStartDate datetime NOT NULL
  bArchived bit NOT NULL default (0)
  bPurged bit NOT NULL default (0)
  _etblPeriodYear_iBranchID int NULL
  _etblPeriodYear_dCreatedDate datetime NULL
  _etblPeriodYear_dModifiedDate datetime NULL
  _etblPeriodYear_iCreatedBranchID int NULL
  _etblPeriodYear_iModifiedBranchID int NULL
  _etblPeriodYear_iCreatedAgentID int NULL
  _etblPeriodYear_iModifiedAgentID int NULL
  _etblPeriodYear_iChangeSetID int NULL
  _etblPeriodYear_Checksum binary(20) NULL

## _etblPOPDefaults - Procurement Default (ProcurementDefaults)
Alias: Procurement Default | Freedom Name: ProcurementDefaults | Record Identifier: 
Notes: Procurement Default
PK: idPOPDefaults
Columns (18):
  idPOPDefaults int NOT NULL identity PK
  bAutoRequisition bit NOT NULL default (1)
  cRequisitionPrefix varchar(25) NULL
  iNextRequisitionNo int NULL
  iPadRequisitionLength int NULL
  bReqBudgetCheck bit NOT NULL default (0)
  bReqBudgetAnnual bit NOT NULL default (0)
  bReqToPOIgnoreExpDate bit NOT NULL default (0)
  bForceProject bit NOT NULL default (0)
  _etblPOPDefaults_iBranchID int NULL
  _etblPOPDefaults_dCreatedDate datetime NULL
  _etblPOPDefaults_dModifiedDate datetime NULL
  _etblPOPDefaults_iCreatedBranchID int NULL
  _etblPOPDefaults_iModifiedBranchID int NULL
  _etblPOPDefaults_iCreatedAgentID int NULL
  _etblPOPDefaults_iModifiedAgentID int NULL
  _etblPOPDefaults_iChangeSetID int NULL
  _etblPOPDefaults_Checksum binary(20) NULL

## _etblPOPRequisitionLines - Requisition Line (ProcurementRequisitionLines)
Alias: Requisition Line | Freedom Name: ProcurementRequisitionLines | Record Identifier: 
Notes: Requisition Line
PK: idPOPRequisitionLines
Columns (39):
  idPOPRequisitionLines int NOT NULL identity PK
  iRequisitionID int NOT NULL
  iModuleID int NOT NULL
  iAccountID int NOT NULL
  cDescription varchar(100) NULL
  iSupplierID int NOT NULL
  fQuantity float NOT NULL default (0)
  fExpectedPrice float NOT NULL default (0)
  dExpectedDate datetime NULL
  iProjectID int NOT NULL
  iJobID int NOT NULL
  iIncidentTypeID int NOT NULL
  iEscalateGroupID int NOT NULL
  iAgentID int NOT NULL
  cLineNotes varchar(1024) NULL
  iLineStatus int NOT NULL default (0)
  iIncidentID int NOT NULL default (0)
  iPOInvoiceID bigint NOT NULL default (0)
  fActualPrice float NULL default (0)
  fExchangeRate float NULL
  fExpectedPriceForeign float NULL
  fActualPriceForeign float NULL
  dApprovalDate datetime NULL
  iActionAgentID int NULL
  _etblPOPRequisitionLines_iBranchID int NULL
  _etblPOPRequisitionLines_dCreatedDate datetime NULL
  _etblPOPRequisitionLines_dModifiedDate datetime NULL
  _etblPOPRequisitionLines_iCreatedBranchID int NULL
  _etblPOPRequisitionLines_iModifiedBranchID int NULL
  _etblPOPRequisitionLines_iCreatedAgentID int NULL
  _etblPOPRequisitionLines_iModifiedAgentID int NULL
  _etblPOPRequisitionLines_iChangeSetID int NULL
  _etblPOPRequisitionLines_Checksum binary(20) NULL
  cSector varchar(100) NULL
  cCostCentre varchar(100) NULL
  iGenRFQAgentID int NULL
  iAreaID int NULL
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL

## _etblPOPRequisitionLinesHist - Requisition Line History
Alias: Requisition Line History | Freedom Name:  | Record Identifier: 
Notes: Requisition Line History
PK: idPOPRequisitionLinesHist
Columns (36):
  idPOPRequisitionLinesHist int NOT NULL identity PK
  iRequisitionHistID int NOT NULL
  iRequisitionID int NOT NULL
  iModuleID int NOT NULL
  iAccountID int NOT NULL
  cDescription varchar(100) NULL
  iSupplierID int NOT NULL
  fQuantity float NOT NULL
  fExpectedPrice float NOT NULL
  dExpectedDate datetime NULL
  iProjectID int NOT NULL
  iJobID int NOT NULL
  iIncidentTypeID int NOT NULL
  iEscalateGroupID int NOT NULL
  iAgentID int NOT NULL
  cLineNotes varchar(1024) NULL
  iLineStatus int NOT NULL
  iIncidentID int NOT NULL
  iPOInvoiceID bigint NOT NULL
  fActualPrice float NULL
  fExchangeRate float NULL
  fExpectedPriceForeign float NULL
  fActualPriceForeign float NULL
  dApprovalDate datetime NULL
  iActionAgentID int NULL
  _etblPOPRequisitionLinesHist_iBranchID int NULL
  _etblPOPRequisitionLinesHist_dCreatedDate datetime NULL
  _etblPOPRequisitionLinesHist_dModifiedDate datetime NULL
  _etblPOPRequisitionLinesHist_iCreatedBranchID int NULL
  _etblPOPRequisitionLinesHist_iModifiedBranchID int NULL
  _etblPOPRequisitionLinesHist_iCreatedAgentID int NULL
  _etblPOPRequisitionLinesHist_iModifiedAgentID int NULL
  _etblPOPRequisitionLinesHist_iChangeSetID int NULL
  _etblPOPRequisitionLinesHist_Checksum binary(20) NULL
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL

## _etblPOPRequisitions - Requisition (ProcurementRequisitions)
Alias: Requisition | Freedom Name: ProcurementRequisitions | Record Identifier: 
Notes: Requisition
PK: idPOPRequisitions
Columns (18):
  idPOPRequisitions int NOT NULL identity PK
  cRequisitionNo varchar(50) NULL
  dRequisitionDate datetime NOT NULL
  iProjectDefaultID int NOT NULL
  cRequestedBy varchar(50) NULL
  iIncidentTypeDefaultID int NOT NULL
  iStatus int NOT NULL default (0)
  iAgentID int NULL default (0)
  _etblPOPRequisitions_iBranchID int NULL
  _etblPOPRequisitions_dCreatedDate datetime NULL
  _etblPOPRequisitions_dModifiedDate datetime NULL
  _etblPOPRequisitions_iCreatedBranchID int NULL
  _etblPOPRequisitions_iModifiedBranchID int NULL
  _etblPOPRequisitions_iCreatedAgentID int NULL
  _etblPOPRequisitions_iModifiedAgentID int NULL
  _etblPOPRequisitions_iChangeSetID int NULL
  _etblPOPRequisitions_Checksum binary(20) NULL
  cSector varchar(100) NULL

## _etblPOPRequisitionsHist - Requisition History
Alias: Requisition History | Freedom Name:  | Record Identifier: 
Notes: Requisition History
PK: idPOPRequisitionsHist
Columns (19):
  idPOPRequisitionsHist int NOT NULL identity PK
  iRequisitionID int NOT NULL
  cRequisitionNo varchar(50) NULL
  dRequisitionDate datetime NOT NULL
  iProjectDefaultID int NOT NULL
  cRequestedBy varchar(50) NULL
  iIncidentTypeDefaultID int NOT NULL
  iStatus int NOT NULL
  iAgentID int NOT NULL
  iVersion int NOT NULL
  _etblPOPRequisitionsHist_iBranchID int NULL
  _etblPOPRequisitionsHist_dCreatedDate datetime NULL
  _etblPOPRequisitionsHist_dModifiedDate datetime NULL
  _etblPOPRequisitionsHist_iCreatedBranchID int NULL
  _etblPOPRequisitionsHist_iModifiedBranchID int NULL
  _etblPOPRequisitionsHist_iCreatedAgentID int NULL
  _etblPOPRequisitionsHist_iModifiedAgentID int NULL
  _etblPOPRequisitionsHist_iChangeSetID int NULL
  _etblPOPRequisitionsHist_Checksum binary(20) NULL

## _etblPOSDevices - POS Devices
Alias: POS Devices | Freedom Name:  | Record Identifier: 
Notes: POS Devices
PK: idPOSDevices
Columns (22):
  idPOSDevices int NOT NULL identity PK
  cDeviceCode varchar(12) NULL
  cDeviceDescription varchar(50) NULL
  iDeviceType int NULL
  iPortType int NULL
  iPortNum int NULL
  iBaudrate int NULL
  cControlCodes varchar(120) NULL
  iPoleDisplayWidth int NULL
  iFiscalPrinterId int NULL
  cPrinterName varchar(100) NULL
  iFiscalPrinterModelsId int NULL
  cPrinterCOMName varchar(50) NULL
  _etblPOSDevices_iBranchID int NULL
  _etblPOSDevices_dCreatedDate datetime NULL
  _etblPOSDevices_dModifiedDate datetime NULL
  _etblPOSDevices_iCreatedBranchID int NULL
  _etblPOSDevices_iModifiedBranchID int NULL
  _etblPOSDevices_iCreatedAgentID int NULL
  _etblPOSDevices_iModifiedAgentID int NULL
  _etblPOSDevices_iChangeSetID int NULL
  _etblPOSDevices_Checksum binary(20) NULL

## _etblPostDatedCheques - Post Dated Cheque (PostDatedCheques)
Alias: Post Dated Cheque | Freedom Name: PostDatedCheques | Record Identifier: 
Notes: Post Dated Cheque
PK: idPostDatedCheques
Columns (44):
  idPostDatedCheques int NOT NULL identity PK
  dpdcDate smalldatetime NULL
  ipdcAccountID int NOT NULL default (0)
  ipdcTrCodeID int NOT NULL default (0)
  ipdcTaxTypeID int NOT NULL default (0)
  ipdcProjectID int NOT NULL default (0)
  ipdcRepID int NOT NULL default (0)
  ipdcContraLedgerID int NOT NULL default (0)
  cpdcReference varchar(50) NULL
  cpdcReference2 varchar(50) NULL
  cpdcDescription varchar(100) NULL
  cpdcOrderNo varchar(50) NULL
  fpdcInclusive float NOT NULL default (0)
  fpdcExclusive float NOT NULL default (0)
  fpdcTax float NOT NULL default (0)
  fpdcFCInclusive float NOT NULL default (0)
  fpdcFCExclusive float NOT NULL default (0)
  fpdcFCTax float NOT NULL default (0)
  ipdcDiscTrCodeID int NOT NULL default (0)
  ipdcDiscTaxTypeID int NOT NULL default (0)
  ipdcDiscTaxLedgerID int NOT NULL default (0)
  ipdcDiscContraLedgerID int NOT NULL default (0)
  cpdcDiscDescription varchar(35) NOT NULL
  fpdcDiscInclusive float NOT NULL default (0)
  fpdcDiscExclusive float NOT NULL default (0)
  fpdcDiscTax float NOT NULL default (0)
  fpdcDiscFCInclusive float NOT NULL default (0)
  fpdcDiscFCExclusive float NOT NULL default (0)
  fpdcDiscFCTax float NOT NULL default (0)
  fpdcExchangeRate float NOT NULL default (0)
  ipdcGLControlID int NOT NULL default (0)
  bpdcCancelled bit NOT NULL default (0)
  cpdcCancellationReason varchar(40) NULL
  iVMVoucherID int NOT NULL default (0)
  ipdcDCModule int NOT NULL default (0)
  _etblPostDatedCheques_iBranchID int NULL
  _etblPostDatedCheques_dCreatedDate datetime NULL
  _etblPostDatedCheques_dModifiedDate datetime NULL
  _etblPostDatedCheques_iCreatedBranchID int NULL
  _etblPostDatedCheques_iModifiedBranchID int NULL
  _etblPostDatedCheques_iCreatedAgentID int NULL
  _etblPostDatedCheques_iModifiedAgentID int NULL
  _etblPostDatedCheques_iChangeSetID int NULL
  _etblPostDatedCheques_Checksum binary(20) NULL

## _etblPostGLHist - PostGL History (PostGeneralLedgerHistory)
Alias: PostGL History | Freedom Name: PostGeneralLedgerHistory | Record Identifier: 
Notes: Archived postgl transactions
PK: AutoIdx
Columns (58):
  AutoIdx bigint NOT NULL identity PK
  TxDate smalldatetime NULL
  Id varchar(5) NOT NULL
  AccountLink int NULL
  TrCodeID int NULL
  Debit float NULL
  Credit float NULL
  iCurrencyID int NULL
  fExchangeRate float NULL
  fForeignDebit float NULL
  fForeignCredit float NULL
  Description varchar(100) NULL
  TaxTypeID int NULL
  Reference varchar(50) NULL
  Order_No varchar(50) NULL
  ExtOrderNum varchar(50) NULL
  cAuditNumber varchar(50) NULL
  Tax_Amount float NULL
  fForeignTax float NULL
  Project int NULL
  Period int NULL
  DrCrAccount int NULL
  JobCodeLink int NULL
  CRCCheck float NULL
  DTStamp datetime NULL
  UserName varchar(50) NULL
  iTaxPeriodID int NULL
  cPayeeName varchar(100) NULL
  bPrintCheque bit NOT NULL
  cReference2 varchar(50) NULL
  RepID int NULL
  fJCRepCost float NULL
  iMFPID int NULL
  bIsJCDocLine bit NOT NULL
  bIsSTGLDocLine bit NOT NULL
  iInvLineID bigint NOT NULL
  iTxBranchID int NULL
  cBankRef varchar(20) NULL
  bPBTPaid bit NOT NULL
  iGLTaxAccountID int NULL
  bReconciled bit NOT NULL default (0)
  _etblPostGLHist_iBranchID int NULL
  _etblPostGLHist_dCreatedDate datetime NULL
  _etblPostGLHist_dModifiedDate datetime NULL
  _etblPostGLHist_iCreatedBranchID int NULL
  _etblPostGLHist_iModifiedBranchID int NULL
  _etblPostGLHist_iCreatedAgentID int NULL
  _etblPostGLHist_iModifiedAgentID int NULL
  _etblPostGLHist_iChangeSetID int NULL
  _etblPostGLHist_Checksum binary(20) NULL
  iImportDeclarationID int NULL default (0)
  ucIDSOrdTxCMTransporter varchar(30) NULL
  xAttribute xml NULL
  iMajorIndustryCodeID int NULL default (0)
  cHash varchar(200) NULL
  iKeyVersion int NULL
  uiIDSOrdTxCMQTP int NULL
  ufIDSOrdTxCMQTP float NULL

## _etblPostOutstandingExclAP
PK: none
Columns (13):
  idPostOutstandingExcl int NOT NULL identity
  iPostLnk int NOT NULL
  fLnkAmount float NOT NULL
  fFCLnkAmount float NULL
  _etblPostOutstandingExclAP_iBranchID int NULL
  _etblPostOutstandingExclAP_dCreatedDate datetime NULL
  _etblPostOutstandingExclAP_dModifiedDate datetime NULL
  _etblPostOutstandingExclAP_iCreatedBranchID int NULL
  _etblPostOutstandingExclAP_iModifiedBranchID int NULL
  _etblPostOutstandingExclAP_iCreatedAgentID int NULL
  _etblPostOutstandingExclAP_iModifiedAgentID int NULL
  _etblPostOutstandingExclAP_iChangeSetID int NULL
  _etblPostOutstandingExclAP_Checksum binary(20) NULL

## _etblPostOutstandingExclAR - _etblPostOutstandingExclAR
Alias: _etblPostOutstandingExclAR | Freedom Name:  | Record Identifier: 
Notes: _etblPostOutstandingExclAR
PK: none
Columns (13):
  idPostOutstandingExcl int NOT NULL identity
  iPostLnk int NOT NULL
  fLnkAmount float NOT NULL
  fFCLnkAmount float NULL
  _etblPostOutstandingExclAR_iBranchID int NULL
  _etblPostOutstandingExclAR_dCreatedDate datetime NULL
  _etblPostOutstandingExclAR_dModifiedDate datetime NULL
  _etblPostOutstandingExclAR_iCreatedBranchID int NULL
  _etblPostOutstandingExclAR_iModifiedBranchID int NULL
  _etblPostOutstandingExclAR_iCreatedAgentID int NULL
  _etblPostOutstandingExclAR_iModifiedAgentID int NULL
  _etblPostOutstandingExclAR_iChangeSetID int NULL
  _etblPostOutstandingExclAR_Checksum binary(20) NULL

## _etblPriceListName
PK: IDPriceListName
Columns (15):
  IDPriceListName int NOT NULL identity PK
  cName varchar(30) NOT NULL
  cDescription varchar(60) NULL
  bDefault bit NOT NULL default (0)
  iCurrencyID int NULL
  dPLNameTimeStamp datetime NULL
  _etblPriceListName_iBranchID int NULL
  _etblPriceListName_dCreatedDate datetime NULL
  _etblPriceListName_dModifiedDate datetime NULL
  _etblPriceListName_iCreatedBranchID int NULL
  _etblPriceListName_iModifiedBranchID int NULL
  _etblPriceListName_iCreatedAgentID int NULL
  _etblPriceListName_iModifiedAgentID int NULL
  _etblPriceListName_iChangeSetID int NULL
  _etblPriceListName_Checksum binary(20) NULL

## _etblPriceListName2
PK: none
Columns (15):
  IDPriceListName int NOT NULL identity
  cName varchar(30) NOT NULL
  cDescription varchar(60) NULL
  bDefault bit NOT NULL
  iCurrencyID int NULL
  dPLNameTimeStamp datetime NULL
  _etblPriceListName_iBranchID int NULL
  _etblPriceListName_dCreatedDate datetime NULL
  _etblPriceListName_dModifiedDate datetime NULL
  _etblPriceListName_iCreatedBranchID int NULL
  _etblPriceListName_iModifiedBranchID int NULL
  _etblPriceListName_iCreatedAgentID int NULL
  _etblPriceListName_iModifiedAgentID int NULL
  _etblPriceListName_iChangeSetID int NULL
  _etblPriceListName_Checksum binary(20) NULL

## _etblPriceListPrices - Price List Prices (PriceListPrices)
Alias: Price List Prices | Freedom Name: PriceListPrices | Record Identifier: 
Notes: Price List Prices
PK: IDPriceListPrices
Columns (21):
  IDPriceListPrices bigint NOT NULL identity PK
  iPriceListNameID int NOT NULL
  iStockID int NOT NULL
  iWarehouseID int NULL default (0)
  bUseMarkup bit NOT NULL default (0)
  iMarkupOnCost int NOT NULL default (0)
  fMarkupRate float NULL
  fExclPrice float NULL
  fInclPrice float NULL
  dPLPricesTimeStamp datetime NULL
  _etblPriceListPrices_iBranchID int NULL
  _etblPriceListPrices_dCreatedDate datetime NULL
  _etblPriceListPrices_dModifiedDate datetime NULL
  _etblPriceListPrices_iCreatedBranchID int NULL
  _etblPriceListPrices_iModifiedBranchID int NULL
  _etblPriceListPrices_iCreatedAgentID int NULL
  _etblPriceListPrices_iModifiedAgentID int NULL
  _etblPriceListPrices_iChangeSetID int NULL
  _etblPriceListPrices_Checksum binary(20) NULL
  iUOMID int NOT NULL default (0)
  xAttribute xml NULL

## _etblPriceListPrices2
PK: none
Columns (21):
  IDPriceListPrices bigint NOT NULL identity
  iPriceListNameID int NOT NULL
  iStockID int NOT NULL
  iWarehouseID int NULL
  bUseMarkup bit NOT NULL
  iMarkupOnCost int NOT NULL
  fMarkupRate float NULL
  fExclPrice float NULL
  fInclPrice float NULL
  dPLPricesTimeStamp datetime NULL
  _etblPriceListPrices_iBranchID int NULL
  _etblPriceListPrices_dCreatedDate datetime NULL
  _etblPriceListPrices_dModifiedDate datetime NULL
  _etblPriceListPrices_iCreatedBranchID int NULL
  _etblPriceListPrices_iModifiedBranchID int NULL
  _etblPriceListPrices_iCreatedAgentID int NULL
  _etblPriceListPrices_iModifiedAgentID int NULL
  _etblPriceListPrices_iChangeSetID int NULL
  _etblPriceListPrices_Checksum binary(20) NULL
  iUOMID int NOT NULL
  xAttribute xml NULL

## _etblPriceListPrices3
PK: none
Columns (21):
  IDPriceListPrices bigint NOT NULL identity
  iPriceListNameID int NOT NULL
  iStockID int NOT NULL
  iWarehouseID int NULL
  bUseMarkup bit NOT NULL
  iMarkupOnCost int NOT NULL
  fMarkupRate float NULL
  fExclPrice float NULL
  fInclPrice float NULL
  dPLPricesTimeStamp datetime NULL
  _etblPriceListPrices_iBranchID int NULL
  _etblPriceListPrices_dCreatedDate datetime NULL
  _etblPriceListPrices_dModifiedDate datetime NULL
  _etblPriceListPrices_iCreatedBranchID int NULL
  _etblPriceListPrices_iModifiedBranchID int NULL
  _etblPriceListPrices_iCreatedAgentID int NULL
  _etblPriceListPrices_iModifiedAgentID int NULL
  _etblPriceListPrices_iChangeSetID int NULL
  _etblPriceListPrices_Checksum binary(20) NULL
  iUOMID int NOT NULL
  xAttribute xml NULL

## _etblPromotion
PK: iPromotionID
Columns (32):
  iPromotionID bigint NOT NULL identity PK
  cPromotionCode varchar(20) NOT NULL
  cDescription varchar(50) NULL
  iTriggerQTY int NULL
  iQualifyingQTY int NULL
  fDiscount float NULL
  fFixedPrice float NULL
  dStartDate datetime NULL
  dEndDate datetime NULL
  bProportion bit NULL
  bLimit bit NOT NULL default (0)
  iLimitQTY int NULL
  iPromotionType int NOT NULL default (0)
  fTriggerValue float NULL
  bActive bit NOT NULL default (1)
  iTriggerUOM int NULL
  iQualifyingUOM int NULL
  iCustomerType int NULL
  bInclusive bit NOT NULL default (1)
  _etblPromotion_iBranchID int NULL
  _etblPromotion_dCreatedDate datetime NULL
  _etblPromotion_dModifiedDate datetime NULL
  _etblPromotion_iCreatedBranchID int NULL
  _etblPromotion_iModifiedBranchID int NULL
  _etblPromotion_iCreatedAgentID int NULL
  _etblPromotion_iModifiedAgentID int NULL
  _etblPromotion_iChangeSetID int NULL
  _etblPromotion_Checksum binary(20) NULL
  bApplyOnLaybys bit NULL default (0)
  bAllowReturns bit NULL default (0)
  bForceFullBasketReturn bit NULL default (0)
  iReturnDays int NULL default (0)

## _etblPromotionItem
PK: iPromotionItemID
Columns (17):
  iPromotionItemID bigint NOT NULL identity PK
  iPromotionItemListID bigint NULL
  StockLink int NULL
  cItemGroup varchar(20) NULL
  iTriggerQTY int NULL
  iQualifyingQTY int NULL
  iUOMID int NULL
  iPriority int NULL
  _etblPromotionItem_iBranchID int NULL
  _etblPromotionItem_dCreatedDate datetime NULL
  _etblPromotionItem_dModifiedDate datetime NULL
  _etblPromotionItem_iCreatedBranchID int NULL
  _etblPromotionItem_iModifiedBranchID int NULL
  _etblPromotionItem_iCreatedAgentID int NULL
  _etblPromotionItem_iModifiedAgentID int NULL
  _etblPromotionItem_iChangeSetID int NULL
  _etblPromotionItem_Checksum binary(20) NULL

## _etblPromotionItemList
PK: iPromotionItemListID
Columns (16):
  iPromotionItemListID bigint NOT NULL identity PK
  iPromotionID bigint NULL
  cListCode varchar(20) NULL
  cDescription varchar(50) NULL
  bTriggerItem bit NULL
  bQualifyingItem bit NULL
  bActive bit NOT NULL default (1)
  _etblPromotionItemList_iBranchID int NULL
  _etblPromotionItemList_dCreatedDate datetime NULL
  _etblPromotionItemList_dModifiedDate datetime NULL
  _etblPromotionItemList_iCreatedBranchID int NULL
  _etblPromotionItemList_iModifiedBranchID int NULL
  _etblPromotionItemList_iCreatedAgentID int NULL
  _etblPromotionItemList_iModifiedAgentID int NULL
  _etblPromotionItemList_iChangeSetID int NULL
  _etblPromotionItemList_Checksum binary(20) NULL

## _etblPromotionItemListLink
PK: iPromotionItemListLinkID
Columns (15):
  iPromotionItemListLinkID bigint NOT NULL identity PK
  iPromotionID bigint NULL
  iPromotionItemListID bigint NULL
  bLimit bit NOT NULL default (0)
  iLimitQTY int NULL
  bMultiBuy bit NOT NULL default (0)
  _etblPromotionItemListLink_iBranchID int NULL
  _etblPromotionItemListLink_dCreatedDate datetime NULL
  _etblPromotionItemListLink_dModifiedDate datetime NULL
  _etblPromotionItemListLink_iCreatedBranchID int NULL
  _etblPromotionItemListLink_iModifiedBranchID int NULL
  _etblPromotionItemListLink_iCreatedAgentID int NULL
  _etblPromotionItemListLink_iModifiedAgentID int NULL
  _etblPromotionItemListLink_iChangeSetID int NULL
  _etblPromotionItemListLink_Checksum binary(20) NULL

## _etblPromotionItemListQTY
PK: iPromotionItemListQTYID
Columns (15):
  iPromotionItemListQTYID bigint NOT NULL identity PK
  iPromotionItemListLinkID bigint NULL
  fDiscountValue float NULL
  iValueType int NULL
  fTriggerQTY float NULL
  fQualifyingQTY float NULL
  _etblPromotionItemListQTY_iBranchID int NULL
  _etblPromotionItemListQTY_dCreatedDate datetime NULL
  _etblPromotionItemListQTY_dModifiedDate datetime NULL
  _etblPromotionItemListQTY_iCreatedBranchID int NULL
  _etblPromotionItemListQTY_iModifiedBranchID int NULL
  _etblPromotionItemListQTY_iCreatedAgentID int NULL
  _etblPromotionItemListQTY_iModifiedAgentID int NULL
  _etblPromotionItemListQTY_iChangeSetID int NULL
  _etblPromotionItemListQTY_Checksum binary(20) NULL

## _etblRemittanceBatchDefaults
PK: idRemittanceBatchDefaults
Columns (19):
  idRemittanceBatchDefaults int NOT NULL identity PK
  bAutoNumbers bit NULL default (0)
  iAutoNumPadLength int NULL
  cAutoNumPrefix varchar(25) NULL
  bAutoRefNumbers bit NULL default (0)
  iAutoRefNumPadLength int NULL
  cAutoRefNumPrefix varchar(25) NULL
  _etblRemittanceBatchDefaults_iBranchID int NULL
  _etblRemittanceBatchDefaults_dCreatedDate datetime NULL
  _etblRemittanceBatchDefaults_dModifiedDate datetime NULL
  _etblRemittanceBatchDefaults_iCreatedBranchID int NULL
  _etblRemittanceBatchDefaults_iModifiedBranchID int NULL
  _etblRemittanceBatchDefaults_iCreatedAgentID int NULL
  _etblRemittanceBatchDefaults_iModifiedAgentID int NULL
  _etblRemittanceBatchDefaults_iChangeSetID int NULL
  _etblRemittanceBatchDefaults_Checksum binary(20) NULL
  bLineRefAutoRefNumbers bit NOT NULL default (0)
  iLineRefAutoRefNumPadLength int NOT NULL default (3)
  cLineRefAutoRefNumPrefix nvarchar(25) NULL

## _etblRemittanceBatches
PK: idRemittanceBatches
Columns (69):
  idRemittanceBatches int NOT NULL identity PK
  cBatchNo varchar(50) NULL
  cBatchDesc varchar(50) NOT NULL
  cBatchRef varchar(50) NULL
  bClearAfterPost bit NOT NULL
  bCheckedOut bit NULL
  iAgentCheckedOut int NULL
  dProcessedDate datetime NULL
  bChequeEFTSRun bit NULL default (1)
  idefaultTranType int NULL
  cDescription varchar(40) NULL
  bIncDescription bit NULL default (0)
  cReference varchar(20) NULL
  bIncReference bit NULL default (0)
  bdefaultPrintCheque bit NULL default (1)
  bAllInvoicesPaid bit NULL default (1)
  bPrintChequeOrEFTSOnly bit NULL default (0)
  bPrintRemittance bit NULL default (1)
  bPrintAlsoChequeOrEFTS bit NULL default (1)
  bPrintSamePageRemCheq bit NULL default (0)
  cEFTSFileName varchar(100) NULL
  iDiscTranType int NULL
  bPromptValidationOnClose bit NULL default (1)
  bWarnNotIncludedInRun bit NULL default (1)
  bPreviewBeforePrint bit NULL default (1)
  iDiscTaxType int NULL
  bdefaultEFTSProc bit NULL default (0)
  dEFTSActionDate datetime NULL
  bApplyTerms bit NULL default (1)
  cEFTSBatchDescription varchar(30) NULL
  iEFTSBatchNumber int NULL
  ddefaultPaymentDate datetime NULL
  cEFTSACBServiceType varchar(100) NULL
  iEFTSType int NULL
  bIncludeSupOnHold bit NULL default (1)
  fMaxAmt float NULL
  fMinAmt float NULL
  dPayDueDate datetime NULL
  cSupArea varchar(255) NULL
  cSupFrom varchar(100) NULL
  cSupGrp varchar(255) NULL
  cSupTo varchar(100) NULL
  cEFTSTransactionDesc varchar(30) NULL
  cTrCodes varchar(255) NULL
  cEFTSLayoutDesc varchar(200) NULL
  bAllocateToOldest bit NULL default (0)
  bAllowSettDisc bit NULL default (0)
  cEFTSBatchTypeString varchar(5) NULL
  bEFTSAutoDateForward bit NULL default (0)
  bEFTSTxProofOfPayment bit NULL default (0)
  bEFTSDuplicateFile bit NULL default (0)
  bEFTSExportOrderLetter bit NULL default (0)
  cEFTSOrderLetter varchar(10) NULL
  bInclOutstandingDebits bit NULL default (0)
  bAutoAllocOutstanding bit NULL default (0)
  bTxOnHold bit NULL default (0)
  bTxOnHoldRemove bit NULL default (0)
  iStatus int NOT NULL default (1)
  iBankDetailID int NULL
  _etblRemittanceBatches_iBranchID int NULL
  _etblRemittanceBatches_dCreatedDate datetime NULL
  _etblRemittanceBatches_dModifiedDate datetime NULL
  _etblRemittanceBatches_iCreatedBranchID int NULL
  _etblRemittanceBatches_iModifiedBranchID int NULL
  _etblRemittanceBatches_iCreatedAgentID int NULL
  _etblRemittanceBatches_iModifiedAgentID int NULL
  _etblRemittanceBatches_iChangeSetID int NULL
  _etblRemittanceBatches_Checksum binary(20) NULL
  iProjectID int NULL default (0)

## _etblRemittanceCriteria - Batch Remittance Criteria
Alias: Batch Remittance Criteria | Freedom Name:  | Record Identifier: 
Notes: Batch Remittance Criteria
Columns: none recorded yet (table seen in another Evolution database, not in the scripted one)

## _etblRemittanceDefaults
PK: IDRemittanceDefaults
Columns (60):
  IDRemittanceDefaults int NOT NULL identity PK
  bChequeEFTSRun bit NOT NULL default (1)
  iDefaultTranType int NULL
  cDescription varchar(40) NULL
  bIncDescription bit NOT NULL default (0)
  cReference varchar(20) NULL
  bIncReference bit NOT NULL default (0)
  bDefaultPrintCheque bit NOT NULL default (1)
  bAllInvoicesPaid bit NOT NULL default (1)
  bPrintChequeOrEFTSOnly bit NOT NULL default (0)
  bPrintRemittance bit NOT NULL default (1)
  bPrintAlsoChequeOrEFTS bit NOT NULL default (1)
  bPrintSamePageRemCheq bit NOT NULL default (0)
  cEFTSFileName varchar(100) NULL
  iDiscTranType int NULL
  bPromptValidationOnClose bit NOT NULL default (1)
  bWarnNotIncludedInRun bit NOT NULL default (1)
  bPreviewBeforePrint bit NOT NULL default (1)
  iDiscTaxType int NULL
  bDefaultEFTSProc bit NOT NULL default (0)
  dEFTSActionDate datetime NULL
  bApplyTerms bit NOT NULL default (1)
  cEFTSBatchDescription varchar(30) NULL
  iEFTSBatchNumber int NULL
  dDefaultPaymentDate datetime NULL
  cEFTSACBServiceType varchar(100) NULL
  iEFTSType int NULL
  bIncludeSupOnHold bit NOT NULL default (1)
  fMaxAmt float NULL
  fMinAmt float NULL
  dPayDueDate datetime NULL
  cSupArea varchar(255) NULL
  cSupFrom varchar(100) NULL
  cSupGrp varchar(255) NULL
  cSupTo varchar(100) NULL
  cEFTSTransactionDesc varchar(30) NULL
  cTrCodes varchar(255) NULL
  cEFTSLayoutDesc varchar(200) NULL
  bAllocateToOldest bit NOT NULL default (0)
  bAllowSettDisc bit NOT NULL default (0)
  cEFTSBatchTypeString varchar(5) NULL
  bEFTSAutoDateForward bit NOT NULL default (0)
  bEFTSTxProofOfPayment bit NOT NULL default (0)
  bEFTSDuplicateFile bit NOT NULL default (0)
  bEFTSExportOrderLetter bit NOT NULL default (0)
  cEFTSOrderLetter varchar(10) NULL
  bInclOutsandingDebits bit NOT NULL default (0)
  bAutoAllocOutstanding bit NOT NULL default (0)
  bLoadDefaults bit NULL default (0)
  bTxOnHold bit NOT NULL default (0)
  bTxOnHoldRemove bit NOT NULL default (0)
  _etblRemittanceDefaults_iBranchID int NULL
  _etblRemittanceDefaults_dCreatedDate datetime NULL
  _etblRemittanceDefaults_dModifiedDate datetime NULL
  _etblRemittanceDefaults_iCreatedBranchID int NULL
  _etblRemittanceDefaults_iModifiedBranchID int NULL
  _etblRemittanceDefaults_iCreatedAgentID int NULL
  _etblRemittanceDefaults_iModifiedAgentID int NULL
  _etblRemittanceDefaults_iChangeSetID int NULL
  _etblRemittanceDefaults_Checksum binary(20) NULL

## _etblRemittanceLines - Batch Remittance Line
Alias: Batch Remittance Line | Freedom Name:  | Record Identifier: 
Notes: Batch Remittance Line
PK: IDRemittanceLines
Columns (37):
  IDRemittanceLines int NOT NULL identity PK
  iSupplierID int NULL
  cDocumentNumber varchar(50) NULL
  fAmountOutstanding float NULL
  fDiscAmount float NULL
  fAmountToPay float NULL
  bPayTransaction bit NOT NULL default (0)
  fDiscAmountExcl float NULL
  fDiscTaxAmount float NULL
  dDocumentDate datetime NULL
  fDocumentAmount float NULL
  bAllocated bit NOT NULL default (0)
  iInvRecID bigint NULL
  cInvDescription varchar(255) NULL default ''
  cInvReference1 varchar(255) NULL default ''
  cInvReference2 varchar(255) NULL default ''
  iInvSettlementTermsID int NOT NULL default (0)
  fSettDiscAmount float NOT NULL default (0)
  cSettTermCode varchar(20) NULL
  fSettTermDiscPerc float NOT NULL default (0)
  iSettTermDays int NOT NULL default (0)
  iSettTermPayMethod int NOT NULL default (0)
  bApplyDisc bit NOT NULL default (0)
  fDiscPerc float NOT NULL default (0)
  cInvOrderNumber varchar(20) NULL
  bTxOnHold bit NOT NULL default (0)
  iBatchID int NOT NULL default (0)
  fAmountPaid float NOT NULL default (0)
  _etblRemittanceLines_iBranchID int NULL
  _etblRemittanceLines_dCreatedDate datetime NULL
  _etblRemittanceLines_dModifiedDate datetime NULL
  _etblRemittanceLines_iCreatedBranchID int NULL
  _etblRemittanceLines_iModifiedBranchID int NULL
  _etblRemittanceLines_iCreatedAgentID int NULL
  _etblRemittanceLines_iModifiedAgentID int NULL
  _etblRemittanceLines_iChangeSetID int NULL
  _etblRemittanceLines_Checksum binary(20) NULL

## _etblRemittanceSuppliers
PK: IDRemittanceSuppliers
Columns (42):
  IDRemittanceSuppliers int NOT NULL identity PK
  iSupplierID int NULL
  cPayeeName varchar(255) NULL
  bPrintCheque bit NOT NULL default (0)
  cDescription varchar(40) NULL
  cReference varchar(20) NULL
  fDiscReceived float NULL
  fTotalPaid float NULL
  fDocumentTotal float NULL
  bIncludedInRun bit NOT NULL default (0)
  bChequePrinted bit NOT NULL default (0)
  bRemittancePrinted bit NOT NULL default (0)
  bEFTSProcessed bit NOT NULL default (0)
  fUnallocatedDebits float NULL
  fAllocatedDebits float NULL
  fDiscReceivedExcl float NULL
  fTotalPaidExcl float NULL
  fDiscTaxAmount float NULL
  bPosted bit NOT NULL default (0)
  bProduceEFTS bit NOT NULL default (0)
  iDiscTaxType int NULL
  iProjectID int NULL
  dPaymentDate datetime NULL
  cPayRecIDs varchar(255) NULL
  bDefaultPayAllInvoices bit NOT NULL default (0)
  cDCCode varchar(20) NULL
  cDCName varchar(50) NULL
  fUnallocatedCredits float NULL default (0)
  iInvoiceCount int NULL default (0)
  iConfiguredCount float NULL default (0)
  iBatchID int NOT NULL default (0)
  fAmountToPay float NOT NULL default (0)
  _etblRemittanceSuppliers_iBranchID int NULL
  _etblRemittanceSuppliers_dCreatedDate datetime NULL
  _etblRemittanceSuppliers_dModifiedDate datetime NULL
  _etblRemittanceSuppliers_iCreatedBranchID int NULL
  _etblRemittanceSuppliers_iModifiedBranchID int NULL
  _etblRemittanceSuppliers_iCreatedAgentID int NULL
  _etblRemittanceSuppliers_iModifiedAgentID int NULL
  _etblRemittanceSuppliers_iChangeSetID int NULL
  _etblRemittanceSuppliers_Checksum binary(20) NULL
  iInstructionType int NULL

## _etblReplLog - Replication Log
Alias: Replication Log | Freedom Name:  | Record Identifier: 
Notes: Replication Log
PK: idReplLog
Columns (6):
  idReplLog int NOT NULL identity PK
  iChangeSetID int NOT NULL
  iBranchID int NOT NULL
  cAction char(1) NOT NULL
  dInitDateUtc datetime NULL default getutcdate()
  cFileName varchar(25) NULL

## _etblReportJobLog - Report Job Log
Alias: Report Job Log | Freedom Name:  | Record Identifier: 
Notes: Report Job Log
PK: idReportJobLog
Columns (16):
  idReportJobLog int NOT NULL identity PK
  iJobType int NULL
  iReportJobID int NULL
  dLogTime datetime NULL
  iLogType int NULL
  cLogDescription varchar(1024) NULL
  nLogData image NULL
  _etblReportJobLog_iBranchID int NULL
  _etblReportJobLog_dCreatedDate datetime NULL
  _etblReportJobLog_dModifiedDate datetime NULL
  _etblReportJobLog_iCreatedBranchID int NULL
  _etblReportJobLog_iModifiedBranchID int NULL
  _etblReportJobLog_iCreatedAgentID int NULL
  _etblReportJobLog_iModifiedAgentID int NULL
  _etblReportJobLog_iChangeSetID int NULL
  _etblReportJobLog_Checksum binary(20) NULL

## _etblReportJobs - Report Job
Alias: Report Job | Freedom Name:  | Record Identifier: 
Notes: Report Job
PK: idReportJobs
Columns (17):
  idReportJobs int NOT NULL identity PK
  iReportJobParentID int NULL
  cReportJobName varchar(64) NULL
  iReportJobType int NULL
  nReportJobProps text NULL
  iReportJobAgentID int NULL
  _etblReportJobs_iBranchID int NULL
  _etblReportJobs_dCreatedDate datetime NULL
  _etblReportJobs_dModifiedDate datetime NULL
  _etblReportJobs_iCreatedBranchID int NULL
  _etblReportJobs_iModifiedBranchID int NULL
  _etblReportJobs_iCreatedAgentID int NULL
  _etblReportJobs_iModifiedAgentID int NULL
  _etblReportJobs_iChangeSetID int NULL
  _etblReportJobs_Checksum binary(20) NULL
  iBatchID int NOT NULL default (0)
  cBackupToPath varchar(max) NULL

## _etblRevaluationHistory
PK: idRevaluationHistory
Columns (30):
  idRevaluationHistory int NOT NULL identity PK
  iModule int NULL
  iAccountID int NULL
  dTransactionDate datetime NULL
  iAgentID int NOT NULL
  fRevaluationRate float NULL
  iCurrencyID int NULL
  bPosted bit NULL
  fRevaluationAmount float NULL
  fOldHomeBalance float NULL
  fNewHomeBalance float NULL
  cBatchNumber varchar(10) NULL
  cReference varchar(50) NULL
  cDescription varchar(50) NULL
  iGLAccountProfitLoss int NULL
  iGLAccountProvision int NULL
  cAccountName varchar(100) NULL
  iPeriodID int NOT NULL default (0)
  fForeignBalance float NOT NULL default (0)
  dUpToTxDate datetime NULL
  dRevalRateDate datetime NULL
  _etblRevaluationHistory_iBranchID int NULL
  _etblRevaluationHistory_dCreatedDate datetime NULL
  _etblRevaluationHistory_dModifiedDate datetime NULL
  _etblRevaluationHistory_iCreatedBranchID int NULL
  _etblRevaluationHistory_iModifiedBranchID int NULL
  _etblRevaluationHistory_iCreatedAgentID int NULL
  _etblRevaluationHistory_iModifiedAgentID int NULL
  _etblRevaluationHistory_iChangeSetID int NULL
  _etblRevaluationHistory_Checksum binary(20) NULL

## _etblSageBankFeedsHistory
PK: idSageBankFeedsHistory
Columns (19):
  idSageBankFeedsHistory int NOT NULL identity PK
  iGLBankAccID int NULL
  cSBFOrganisationID varchar(100) NULL
  cSBFAdminUser varchar(100) NULL
  cSBFCompanyID varchar(100) NULL
  cSBFCompanyName varchar(50) NULL
  cSBFBankAccountID varchar(100) NULL
  cBankAccountName varchar(200) NULL
  cConnOrDisconn varchar(15) NULL
  dModifiedDate datetime NULL
  _etblSageBankFeedsHistory_iBranchID int NULL
  _etblSageBankFeedsHistory_dCreatedDate datetime NULL
  _etblSageBankFeedsHistory_dModifiedDate datetime NULL
  _etblSageBankFeedsHistory_iCreatedBranchID int NULL
  _etblSageBankFeedsHistory_iModifiedBranchID int NULL
  _etblSageBankFeedsHistory_iCreatedAgentID int NULL
  _etblSageBankFeedsHistory_iModifiedAgentID int NULL
  _etblSageBankFeedsHistory_iChangeSetID int NULL
  _etblSageBankFeedsHistory_Checksum binary(20) NULL

## _etblSagePayBanks - Sage Pay Banks
Alias: Sage Pay Banks | Freedom Name:  | Record Identifier: 
Notes: This Table is used to translate the Bank Name Display field to Bank name file
PK: SagePayBankID
Columns (15):
  SagePayBankID int NOT NULL identity PK
  CountryCode smallint NULL
  BankNameDisplay varchar(100) NULL
  BankNameFile varchar(100) NULL
  BranchName varchar(100) NULL
  BranchCode varchar(100) NULL
  _etblSagePayBanks_iBranchID int NULL
  _etblSagePayBanks_dCreatedDate datetime NULL
  _etblSagePayBanks_dModifiedDate datetime NULL
  _etblSagePayBanks_iCreatedBranchID int NULL
  _etblSagePayBanks_iModifiedBranchID int NULL
  _etblSagePayBanks_iCreatedAgentID int NULL
  _etblSagePayBanks_iModifiedAgentID int NULL
  _etblSagePayBanks_iChangeSetID int NULL
  _etblSagePayBanks_Checksum binary(20) NULL

## _etblSagePayErrorCodes - Sage Pay Error Codes
Alias: Sage Pay Error Codes | Freedom Name:  | Record Identifier: 
Notes: Translates and stores the response code to human readable messages
PK: idSagePayErrorCode
Columns (14):
  idSagePayErrorCode int NOT NULL identity PK
  iServiceID int NULL
  iResponse int NULL
  bWebServiceFailure bit NULL
  cResponse varchar(50) NULL
  _etblSagePayErrorCodes_iBranchID int NULL
  _etblSagePayErrorCodes_dCreatedDate datetime NULL
  _etblSagePayErrorCodes_dModifiedDate datetime NULL
  _etblSagePayErrorCodes_iCreatedBranchID int NULL
  _etblSagePayErrorCodes_iModifiedBranchID int NULL
  _etblSagePayErrorCodes_iCreatedAgentID int NULL
  _etblSagePayErrorCodes_iModifiedAgentID int NULL
  _etblSagePayErrorCodes_iChangeSetID int NULL
  _etblSagePayErrorCodes_Checksum binary(20) NULL

## _etblSagePayNow - Sage Pay
Alias: Sage Pay | Freedom Name:  | Record Identifier: 
Notes: Data stored to create the Sage Pay banner
PK: idSagePayNow
Columns (22):
  idSagePayNow int NOT NULL identity PK
  InvNumID bigint NOT NULL
  UniqueReference varchar(10) NULL
  Amount decimal(18,2) NULL
  BankStatementRef varchar(50) NULL
  CardHoldersEmailAddress varchar(100) NULL
  Extra1DebtorsRef varchar(max) NULL
  Extra2 varchar(max) NULL
  Extra3 varchar(max) NULL
  AcceptDeclineURLParams varchar(200) NULL
  PCode varchar(15) NULL
  PayNowResponse xml NULL
  DocType int NOT NULL
  _etblSagePayNow_iBranchID int NULL
  _etblSagePayNow_dCreatedDate datetime NULL
  _etblSagePayNow_dModifiedDate datetime NULL
  _etblSagePayNow_iCreatedBranchID int NULL
  _etblSagePayNow_iModifiedBranchID int NULL
  _etblSagePayNow_iCreatedAgentID int NULL
  _etblSagePayNow_iModifiedAgentID int NULL
  _etblSagePayNow_iChangeSetID int NULL
  _etblSagePayNow_Checksum binary(20) NULL

## _etblSagePayQueue - Sage Pay Queue
Alias: Sage Pay Queue | Freedom Name:  | Record Identifier: 
Notes: Data Storage for submitions for Bank Validation and the responses received from Sage Pay
PK: idSPQueue
Columns (26):
  idSPQueue int NOT NULL identity PK
  iService int NULL
  cDescription varchar(50) NULL
  cInstruction varchar(50) NULL
  bTestOnly bit NULL
  iSubmissionStatus int NULL
  iResponseStatus int NULL
  dCreated datetime NULL
  dLastPolled datetime NULL
  cToken varchar(50) NULL
  cBatchName varchar(50) NULL
  cBatchData varchar(max) NULL
  iRecordID int NULL
  cModule varchar(50) NULL
  cSubmissionData varchar(max) NULL
  cResponseData varchar(max) NULL
  iAgentID int NULL
  _etblSagePayQueue_iBranchID int NULL
  _etblSagePayQueue_dCreatedDate datetime NULL
  _etblSagePayQueue_dModifiedDate datetime NULL
  _etblSagePayQueue_iCreatedBranchID int NULL
  _etblSagePayQueue_iModifiedBranchID int NULL
  _etblSagePayQueue_iCreatedAgentID int NULL
  _etblSagePayQueue_iModifiedAgentID int NULL
  _etblSagePayQueue_iChangeSetID int NULL
  _etblSagePayQueue_Checksum binary(20) NULL

## _etblSagePayServiceKeys - Sage Pay Service Keys
Alias: Sage Pay Service Keys | Freedom Name:  | Record Identifier: 
PK: idSagePayServiceKey
Columns (18):
  idSagePayServiceKey int NOT NULL identity PK
  iServiceType int NOT NULL
  cServiceKeyName varchar(50) NOT NULL
  cServiceDescription varchar(150) NULL
  cServiceKeyValue varchar(37) NULL
  iConnectionTimeout int NULL
  iReceiveTimeout int NULL
  iSendTimeout int NULL
  bIsActive bit NOT NULL
  _etblSagePayServiceKeys_iBranchID int NULL
  _etblSagePayServiceKeys_dCreatedDate datetime NULL
  _etblSagePayServiceKeys_dModifiedDate datetime NULL
  _etblSagePayServiceKeys_iCreatedBranchID int NULL
  _etblSagePayServiceKeys_iModifiedBranchID int NULL
  _etblSagePayServiceKeys_iCreatedAgentID int NULL
  _etblSagePayServiceKeys_iModifiedAgentID int NULL
  _etblSagePayServiceKeys_iChangeSetID int NULL
  _etblSagePayServiceKeys_Checksum binary(20) NULL

## _etblSageVATReportHistory
PK: idSageVATReportHistory
Columns (17):
  idSageVATReportHistory int NOT NULL identity PK
  cVATHistoryOrganisationID varchar(100) NULL
  cVATHistoryAdminUser varchar(100) NULL
  cVATHistorySigningKey varchar(100) NULL
  cVATHistoryCompanyID varchar(100) NULL
  cVATHistoryCompanyName varchar(100) NULL
  cVATHistoryExternalID varchar(100) NULL
  dVATHistoryModifiedDate datetime NULL
  _etblSageVATReportHistory_iBranchID int NULL
  _etblSageVATReportHistory_dCreatedDate datetime NULL
  _etblSageVATReportHistory_dModifiedDate datetime NULL
  _etblSageVATReportHistory_iCreatedBranchID int NULL
  _etblSageVATReportHistory_iModifiedBranchID int NULL
  _etblSageVATReportHistory_iCreatedAgentID int NULL
  _etblSageVATReportHistory_iModifiedAgentID int NULL
  _etblSageVATReportHistory_iChangeSetID int NULL
  _etblSageVATReportHistory_Checksum binary(20) NULL

## _etblSettlementTerms - Settlement Term (SettlementTerm)
Alias: Settlement Term | Freedom Name: SettlementTerm | Record Identifier: cSettlementCode
Notes: Settlement Term
PK: idSettlementTerms
Columns (16):
  idSettlementTerms int NOT NULL identity PK
  cSettlementCode varchar(20) NOT NULL
  cSettlementDescription varchar(100) NULL
  iPaymentMethod int NULL
  iSettlementDays int NULL
  fSettlementDisc float NOT NULL default (0)
  cInvMessage varchar(255) NULL
  _etblSettlementTerms_iBranchID int NULL
  _etblSettlementTerms_dCreatedDate datetime NULL
  _etblSettlementTerms_dModifiedDate datetime NULL
  _etblSettlementTerms_iCreatedBranchID int NULL
  _etblSettlementTerms_iModifiedBranchID int NULL
  _etblSettlementTerms_iCreatedAgentID int NULL
  _etblSettlementTerms_iModifiedAgentID int NULL
  _etblSettlementTerms_iChangeSetID int NULL
  _etblSettlementTerms_Checksum binary(20) NULL

## _etblStockBinLocations
PK: idStockBinLocations
Columns (15):
  idStockBinLocations int NOT NULL identity PK
  StockID int NOT NULL
  WhseID int NOT NULL
  BinID int NOT NULL
  MinLevel float NOT NULL
  MaxLevel float NOT NULL
  _etblStockBinLocations_iBranchID int NULL
  _etblStockBinLocations_dCreatedDate datetime NULL
  _etblStockBinLocations_dModifiedDate datetime NULL
  _etblStockBinLocations_iCreatedBranchID int NULL
  _etblStockBinLocations_iModifiedBranchID int NULL
  _etblStockBinLocations_iCreatedAgentID int NULL
  _etblStockBinLocations_iModifiedAgentID int NULL
  _etblStockBinLocations_iChangeSetID int NULL
  _etblStockBinLocations_Checksum binary(20) NULL

## _etblStockCategories
PK: idStockCategories
Columns (12):
  idStockCategories int NOT NULL identity PK
  cCategoryName varchar(30) NOT NULL
  cCategoryDescription varchar(100) NULL
  _etblStockCategories_iBranchID int NULL
  _etblStockCategories_dCreatedDate datetime NULL
  _etblStockCategories_dModifiedDate datetime NULL
  _etblStockCategories_iCreatedBranchID int NULL
  _etblStockCategories_iModifiedBranchID int NULL
  _etblStockCategories_iCreatedAgentID int NULL
  _etblStockCategories_iModifiedAgentID int NULL
  _etblStockCategories_iChangeSetID int NULL
  _etblStockCategories_Checksum binary(20) NULL

## _etblStockCosts
PK: idStockCosts
Columns (19):
  idStockCosts bigint NOT NULL identity PK
  StockID int NOT NULL
  WhseID int NOT NULL default (0)
  LotID int NOT NULL default (0)
  AverageCost float NOT NULL default (0)
  LatestCost float NOT NULL default (0)
  LowestCost float NOT NULL default (0)
  HighestCost float NOT NULL default (0)
  ManualCost float NOT NULL default (0)
  LastGRVCost float NOT NULL default (0)
  _etblStockCosts_iBranchID int NULL
  _etblStockCosts_dCreatedDate datetime NULL
  _etblStockCosts_dModifiedDate datetime NULL
  _etblStockCosts_iCreatedBranchID int NULL
  _etblStockCosts_iModifiedBranchID int NULL
  _etblStockCosts_iCreatedAgentID int NULL
  _etblStockCosts_iModifiedAgentID int NULL
  _etblStockCosts_iChangeSetID int NULL
  _etblStockCosts_Checksum binary(20) NULL

## _etblStockDetails
PK: idStockDetails
Columns (29):
  idStockDetails bigint NOT NULL identity PK
  StockID int NOT NULL
  WhseID int NOT NULL default (0)
  GroupID int NOT NULL default (0)
  BuyingAgentID int NOT NULL default (0)
  ItemCategoryID int NOT NULL default (0)
  TTInvID int NOT NULL
  TTCrnID int NOT NULL
  TTGrvID int NOT NULL
  TTRtsID int NOT NULL
  PackCodeID int NOT NULL default (0)
  AllowNegStock bit NOT NULL default (0)
  ReorderLevel float NOT NULL default (0)
  ReorderQty float NOT NULL default (0)
  MinLevel float NOT NULL default (0)
  MaxLevel float NOT NULL default (0)
  LeadDays float NOT NULL default (0)
  _etblStockDetails_iBranchID int NULL
  _etblStockDetails_dCreatedDate datetime NULL
  _etblStockDetails_dModifiedDate datetime NULL
  _etblStockDetails_iCreatedBranchID int NULL
  _etblStockDetails_iModifiedBranchID int NULL
  _etblStockDetails_iCreatedAgentID int NULL
  _etblStockDetails_iModifiedAgentID int NULL
  _etblStockDetails_iChangeSetID int NULL
  _etblStockDetails_Checksum binary(20) NULL
  BarcodeID int NOT NULL default (0)
  iDefaultSalesBinID int NULL
  iDefaultPurchasesBinID int NULL

## _etblStockQtys
PK: idStockQtys
Columns (27):
  idStockQtys bigint NOT NULL identity PK
  StockID int NOT NULL
  WhseID int NOT NULL default (0)
  LotID int NOT NULL default (0)
  BinLocationID int NOT NULL default (0)
  QtyOnHand float NOT NULL default (0)
  QtyOnSO float NOT NULL default (0)
  QtyOnPO float NOT NULL default (0)
  QtyReserved float NOT NULL default (0)
  QtyToDeliver float NOT NULL default (0)
  QtyJCWIP float NOT NULL default (0)
  QtyMFPWIP float NOT NULL default (0)
  QtyLastGrvCount float NOT NULL default (0)
  _etblStockQtys_iBranchID int NULL
  _etblStockQtys_dCreatedDate datetime NULL
  _etblStockQtys_dModifiedDate datetime NULL
  _etblStockQtys_iCreatedBranchID int NULL
  _etblStockQtys_iModifiedBranchID int NULL
  _etblStockQtys_iCreatedAgentID int NULL
  _etblStockQtys_iModifiedAgentID int NULL
  _etblStockQtys_iChangeSetID int NULL
  _etblStockQtys_Checksum binary(20) NULL
  QtyIBTToIssue float NOT NULL default (0)
  QtyIBTToReceive float NOT NULL default (0)
  xAttribute xml NULL
  QtyIBTIssued float NOT NULL default (0)
  QtyIBTReceived float NOT NULL default (0)

## _etblStockQtys2
PK: none
Columns (27):
  idStockQtys bigint NOT NULL identity
  StockID int NOT NULL
  WhseID int NOT NULL
  LotID int NOT NULL
  BinLocationID int NOT NULL
  QtyOnHand float NOT NULL
  QtyOnSO float NOT NULL
  QtyOnPO float NOT NULL
  QtyReserved float NOT NULL
  QtyToDeliver float NOT NULL
  QtyJCWIP float NOT NULL
  QtyMFPWIP float NOT NULL
  QtyLastGrvCount float NOT NULL
  _etblStockQtys_iBranchID int NULL
  _etblStockQtys_dCreatedDate datetime NULL
  _etblStockQtys_dModifiedDate datetime NULL
  _etblStockQtys_iCreatedBranchID int NULL
  _etblStockQtys_iModifiedBranchID int NULL
  _etblStockQtys_iCreatedAgentID int NULL
  _etblStockQtys_iModifiedAgentID int NULL
  _etblStockQtys_iChangeSetID int NULL
  _etblStockQtys_Checksum binary(20) NULL
  QtyIBTToIssue float NOT NULL
  QtyIBTToReceive float NOT NULL
  xAttribute xml NULL
  QtyIBTIssued float NOT NULL
  QtyIBTReceived float NOT NULL

## _etblSyncInfo
PK: idSyncInfo
Columns (4):
  idSyncInfo int NOT NULL identity PK
  iRecCount bigint NULL
  cTablename nvarchar(255) NULL
  iBranchID int NULL

## _etblSyncInfoDetails
PK: idSyncInfoDetails
Columns (3):
  idSyncInfoDetails bigint NOT NULL identity PK
  iSyncInfoID int NULL
  rowChecksum binary(20) NULL

## _etblSystem - System (EvoSystem)
Alias: System | Freedom Name: EvoSystem | Record Identifier: 
Notes: System
PK: idSystem
Columns (3):
  idSystem int NOT NULL identity PK
  cIdentity varchar(35) NOT NULL
  cValue varchar(1024) NULL

## _etblSystemDefaults - System Default (SystemDefault)
Alias: System Default | Freedom Name: SystemDefault | Record Identifier: 
Notes: System Default
PK: idSystemDefaults
Columns (65):
  idSystemDefaults int NOT NULL identity PK
  DefaultAccess varchar(5) NULL
  Security varchar(684) NULL
  CheckValue varchar(684) NULL
  SmartFilter bit NOT NULL default (1)
  SMTPAccount varchar(256) NULL
  SMTPAuthenticate bit NOT NULL default (0)
  SMTPAuthPass varchar(684) NULL
  SMTPAuthUser varchar(256) NULL
  SMTPFrom varchar(256) NULL
  SMTPName varchar(256) NULL
  SMTPOrg varchar(256) NULL
  SMTPPassword varchar(256) NULL
  SMTPPort int NULL
  SMTPReplyTo varchar(256) NULL
  SMTPServer varchar(256) NULL
  SMTPUseGlobalFromAddr bit NOT NULL default (0)
  SyncDataFolder varchar(256) NULL
  SyncDBServerDataFolder varchar(256) NULL
  UpdateCheck int NULL
  UpdateCheckInterval int NULL
  BICRepository varchar(256) NULL
  BICRptFinancialYear int NULL default (5)
  HtmlRoot varchar(256) NULL
  UseSegmentedGL bit NOT NULL default (0)
  bUseTLS int NULL default (0)
  bDisableRTF bit NOT NULL default (0)
  bUseCOM bit NULL default (0)
  bUseMapi bit NOT NULL default (1)
  cSMTPBccAddresss varchar(50) NULL
  bUpdateGLBalances bit NOT NULL default (1)
  iGLRelinkCheckInterval int NOT NULL default (1)
  iPwrNumberChar int NOT NULL default (0)
  iPwrLetterChar int NOT NULL default (0)
  iPwrSymbolChar int NOT NULL default (0)
  iPwrUppercaseChar int NOT NULL default (0)
  iPwrLowercaseChar int NOT NULL default (0)
  iLockOutAttempts int NOT NULL default (0)
  iLockOutDuration int NOT NULL default (0)
  bPwrComplexity bit NOT NULL default (0)
  bEnableLockOut bit NOT NULL default (0)
  cFreedomService varchar(250) NULL
  cFailOverService varchar(250) NULL
  bUseLocalService bit NOT NULL default (1)
  iFSSessionTimeOut int NOT NULL default (20)
  bExceptionTrapping bit NULL default (0)
  _etblSystemDefaults_iBranchID int NULL
  _etblSystemDefaults_dCreatedDate datetime NULL
  _etblSystemDefaults_dModifiedDate datetime NULL
  _etblSystemDefaults_iCreatedBranchID int NULL
  _etblSystemDefaults_iModifiedBranchID int NULL
  _etblSystemDefaults_iCreatedAgentID int NULL
  _etblSystemDefaults_iModifiedAgentID int NULL
  _etblSystemDefaults_iChangeSetID int NULL
  _etblSystemDefaults_Checksum binary(20) NULL
  bUseOutgoingServerSettings bit NOT NULL default (0)
  iSMTPProvider int NOT NULL default (0)
  bAppStatsDisabled bit NOT NULL default (0)
  bUseOAuth2 bit NOT NULL default (0)
  SMTPClientId varchar(256) NULL
  SMTPClientSecret varchar(256) NULL
  SMTPAuthUrl varchar(256) NULL
  SMTPTokenUrl varchar(256) NULL
  SMTPScope varchar(256) NULL
  SMTPRedirectUrl varchar(256) NULL

## _etblSystemUpdate - System Update (SystemUpdate)
Alias: System Update | Freedom Name: SystemUpdate | Record Identifier: 
Notes: System Update
PK: idSystemUpdate
Columns (12):
  idSystemUpdate int NOT NULL identity PK
  iUpdate int NOT NULL
  bForce bit NOT NULL
  _etblSystemUpdate_iBranchID int NULL
  _etblSystemUpdate_dCreatedDate datetime NULL
  _etblSystemUpdate_dModifiedDate datetime NULL
  _etblSystemUpdate_iCreatedBranchID int NULL
  _etblSystemUpdate_iModifiedBranchID int NULL
  _etblSystemUpdate_iCreatedAgentID int NULL
  _etblSystemUpdate_iModifiedAgentID int NULL
  _etblSystemUpdate_iChangeSetID int NULL
  _etblSystemUpdate_Checksum binary(20) NULL

## _etblTaxBadDebt
PK: iTaxBadDebtID
Columns (24):
  iTaxBadDebtID int NOT NULL identity PK
  iPeriodID int NULL
  iPostAR int NOT NULL default (0)
  iPostAP int NOT NULL default (0)
  ReliefAmt float NOT NULL default (0)
  ReliefTaxAmt float NOT NULL default (0)
  RecoveredAmt float NOT NULL default (0)
  RecoveredTaxAmt float NOT NULL default (0)
  RefundAmt float NOT NULL default (0)
  RefundTaxAmt float NOT NULL default (0)
  ReclaimAmt float NOT NULL default (0)
  ReclaimTaxAmt float NOT NULL default (0)
  iProcessedTaxPeriodID int NOT NULL default (0)
  ReliefAmtForeign float NOT NULL default (0)
  ReliefTaxAmtForeign float NOT NULL default (0)
  RecoveredAmtForeign float NOT NULL default (0)
  RecoveredTaxAmtForeign float NOT NULL default (0)
  RefundAmtForeign float NOT NULL default (0)
  RefundTaxAmtForeign float NOT NULL default (0)
  ReclaimAmtForeign float NOT NULL default (0)
  ReclaimTaxAmtForeign float NOT NULL default (0)
  iTaxTypeID int NOT NULL default (0)
  TxDate smalldatetime NOT NULL default getdate()
  AuditNumber varchar(50) NULL

## _etblTaxBoxLayout
PK: idTaxBoxLayout
Columns (13):
  idTaxBoxLayout int NOT NULL identity PK
  iTaxGroupID int NULL
  iTaxTypeID int NULL
  iTaxBoxSetupID int NULL
  _etblTaxBoxLayout_iBranchID int NULL
  _etblTaxBoxLayout_dCreatedDate datetime NULL
  _etblTaxBoxLayout_dModifiedDate datetime NULL
  _etblTaxBoxLayout_iCreatedBranchID int NULL
  _etblTaxBoxLayout_iModifiedBranchID int NULL
  _etblTaxBoxLayout_iCreatedAgentID int NULL
  _etblTaxBoxLayout_iModifiedAgentID int NULL
  _etblTaxBoxLayout_iChangeSetID int NULL
  _etblTaxBoxLayout_Checksum binary(20) NULL

## _etblTaxBoxSetup (TaxBoxSetup)
Alias:  | Freedom Name: TaxBoxSetup | Record Identifier: 
PK: idTaxBoxSetup
Columns (18):
  idTaxBoxSetup int NOT NULL identity PK
  iBoxNumber int NOT NULL
  cBoxLabel varchar(5) NULL
  cBoxHeading varchar(256) NULL
  cExamples varchar(256) NULL
  iValueTypeID int NULL
  iValueID int NULL
  iRoundingID int NULL
  _etblTaxBoxSetup_iBranchID int NULL
  _etblTaxBoxSetup_dCreatedDate datetime NULL
  _etblTaxBoxSetup_dModifiedDate datetime NULL
  _etblTaxBoxSetup_iCreatedBranchID int NULL
  _etblTaxBoxSetup_iModifiedBranchID int NULL
  _etblTaxBoxSetup_iCreatedAgentID int NULL
  _etblTaxBoxSetup_iModifiedAgentID int NULL
  _etblTaxBoxSetup_iChangeSetID int NULL
  _etblTaxBoxSetup_Checksum binary(20) NULL
  iTaxUID int NULL default (0)

## _etblTaxCountry
PK: idTaxCountry
Columns (12):
  idTaxCountry int NOT NULL identity PK
  cTaxCountryCode varchar(20) NOT NULL
  cTaxCountryDescription varchar(100) NULL
  _etblTaxCountry_iBranchID int NULL
  _etblTaxCountry_dCreatedDate datetime NULL
  _etblTaxCountry_dModifiedDate datetime NULL
  _etblTaxCountry_iCreatedBranchID int NULL
  _etblTaxCountry_iModifiedBranchID int NULL
  _etblTaxCountry_iCreatedAgentID int NULL
  _etblTaxCountry_iModifiedAgentID int NULL
  _etblTaxCountry_iChangeSetID int NULL
  _etblTaxCountry_Checksum binary(20) NULL

## _etblTaxDefaults (TaxDefaults)
Alias:  | Freedom Name: TaxDefaults | Record Identifier: 
PK: idTaxDefaults
Columns (52):
  idTaxDefaults int NOT NULL identity PK
  cTaxNumber varchar(15) NULL
  cRegistration varchar(20) NULL
  cCustomsCode varchar(8) NULL
  iTaxDueLedgerAccount int NULL
  iPBTStartPeriodID int NULL
  bPrincipalVendor bit NULL default (0)
  bValidateTaxGroups bit NULL default (1)
  cTaxContactName varchar(90) NULL
  cTaxContactSurname varchar(53) NULL
  cTaxContactTelephone1 varchar(15) NULL
  cTaxContactTelephone2 varchar(15) NULL
  cTaxContactCellular varchar(15) NULL
  cTaxContactFax varchar(15) NULL
  cTaxContactEmail varchar(60) NULL
  bForceClientTaxIdentification bit NULL default (0)
  bForceSupplierTaxIdentification bit NULL default (0)
  bValidateClientTaxIdentification bit NOT NULL default (0)
  bValidateSupplierTaxIdentification bit NOT NULL default (0)
  _etblTaxDefaults_iBranchID int NULL
  _etblTaxDefaults_dCreatedDate datetime NULL
  _etblTaxDefaults_dModifiedDate datetime NULL
  _etblTaxDefaults_iCreatedBranchID int NULL
  _etblTaxDefaults_iModifiedBranchID int NULL
  _etblTaxDefaults_iCreatedAgentID int NULL
  _etblTaxDefaults_iModifiedAgentID int NULL
  _etblTaxDefaults_iChangeSetID int NULL
  _etblTaxDefaults_Checksum binary(20) NULL
  iBadDebtRecovered int NOT NULL default (0)
  iBadDebtRelief int NOT NULL default (0)
  iBadDebtRefund int NOT NULL default (0)
  iBadDebtReclaim int NOT NULL default (0)
  iIDFTaxCodeID int NOT NULL default (0)
  iIDFTransTypeID int NOT NULL default (0)
  bIDFUseAgent bit NOT NULL default (0)
  iIDFForAgentTaxCodeID int NOT NULL default (0)
  iImportServiceSRPTaxCodeID int NOT NULL default (0)
  iImportServiceSRSTaxCodeID int NOT NULL default (0)
  bForceTaxDetails bit NOT NULL default (0)
  bShowInactiveTaxTypes bit NOT NULL default (1)
  iMajorIndustryCodeID int NULL default (0)
  iPrepaymentTaxLedgerID int NOT NULL default (0)
  iInputTaxCode int NOT NULL default (0)
  iOutputTaxCode int NOT NULL default (0)
  iTaxCountry int NOT NULL default (-1)
  iTaxClosePeriodFrequency int NOT NULL default (1)
  iTaxClosePeriodStartID int NOT NULL default (0)
  bRevenueIntegration bit NOT NULL default (0)
  cTaxPayerID varchar(50) NULL
  cTaxPractRegistrationNo varchar(50) NULL
  cTaxPractTelephoneNo varchar(25) NULL
  cContactCapacity varchar(50) NULL

## _etblTaxGroup (TaxGroup)
Alias:  | Freedom Name: TaxGroup | Record Identifier: 
PK: idTaxGroup
Columns (12):
  idTaxGroup int NOT NULL identity PK
  cCode varchar(50) NULL
  cDescription varchar(120) NULL
  _etblTaxGroup_iBranchID int NULL
  _etblTaxGroup_dCreatedDate datetime NULL
  _etblTaxGroup_dModifiedDate datetime NULL
  _etblTaxGroup_iCreatedBranchID int NULL
  _etblTaxGroup_iModifiedBranchID int NULL
  _etblTaxGroup_iCreatedAgentID int NULL
  _etblTaxGroup_iModifiedAgentID int NULL
  _etblTaxGroup_iChangeSetID int NULL
  _etblTaxGroup_Checksum binary(20) NULL

## _etblTaxGroupTransType
PK: idTaxGroupTransType
Columns (13):
  idTaxGroupTransType int NOT NULL identity PK
  iTaxGroupID int NOT NULL
  iTransTypeID int NOT NULL
  cModule varchar(30) NULL
  _etblTaxGroupTransType_iBranchID int NULL
  _etblTaxGroupTransType_dCreatedDate datetime NULL
  _etblTaxGroupTransType_dModifiedDate datetime NULL
  _etblTaxGroupTransType_iCreatedBranchID int NULL
  _etblTaxGroupTransType_iModifiedBranchID int NULL
  _etblTaxGroupTransType_iCreatedAgentID int NULL
  _etblTaxGroupTransType_iModifiedAgentID int NULL
  _etblTaxGroupTransType_iChangeSetID int NULL
  _etblTaxGroupTransType_Checksum binary(20) NULL

## _etblTaxReportTemp
PK: none
Columns (7):
  TxDate smalldatetime NULL
  Id varchar(5) NOT NULL
  TrCode varchar(20) NULL
  cAuditNumber varchar(50) NULL
  ExclAmount float NULL
  TaxAmount float NULL
  InclAmount float NULL

## _etblTaxSubmissionDetails
PK: idTaxSubmissionDetails
Columns (14):
  idTaxSubmissionDetails int NOT NULL identity PK
  cTaxCompanyName varchar(150) NOT NULL
  cTaxCompanyRegistrationNo varchar(150) NOT NULL
  cTaxRegistrationNo varchar(150) NOT NULL
  iTaxGLPostingID bigint NOT NULL
  _etblTaxSubmissionDetails_iBranchID int NULL
  _etblTaxSubmissionDetails_dCreatedDate datetime NULL
  _etblTaxSubmissionDetails_dModifiedDate datetime NULL
  _etblTaxSubmissionDetails_iCreatedBranchID int NULL
  _etblTaxSubmissionDetails_iModifiedBranchID int NULL
  _etblTaxSubmissionDetails_iCreatedAgentID int NULL
  _etblTaxSubmissionDetails_iModifiedAgentID int NULL
  _etblTaxSubmissionDetails_iChangeSetID int NULL
  _etblTaxSubmissionDetails_Checksum binary(20) NULL

## _etblTerms - Term (Term)
Alias: Term | Freedom Name: Term | Record Identifier: cCode
Notes: Term
PK: iTermID
Columns (52):
  iTermID int NOT NULL identity PK
  iModule int NOT NULL
  cCode varchar(20) NOT NULL
  cDescription varchar(100) NULL
  iTermDescOption int NULL
  cTermDesc1 varchar(50) NULL
  cTermDesc2 varchar(50) NULL
  cTermDesc3 varchar(50) NULL
  cTermDesc4 varchar(50) NULL
  cTermDesc5 varchar(50) NULL
  cTermDesc6 varchar(50) NULL
  cTermDesc7 varchar(50) NULL
  iAgeTypeOption int NULL
  iIntervalOption int NULL
  iInterval1Days int NULL
  iInterval2Days int NULL
  iInterval3Days int NULL
  iInterval4Days int NULL
  iInterval5Days int NULL
  iInterval6Days int NULL
  iInterval7Days int NULL
  dStateCloseDate1 datetime NULL
  dStateCloseDate2 datetime NULL
  dStateCloseDate3 datetime NULL
  dStateCloseDate4 datetime NULL
  dStateCloseDate5 datetime NULL
  dStateCloseDate6 datetime NULL
  dStateCloseDate7 datetime NULL
  bAutoSetToPeriod bit NOT NULL default (0)
  cAge1Message1 varchar(100) NULL
  cAge1Message2 varchar(100) NULL
  cAge2Message1 varchar(100) NULL
  cAge2Message2 varchar(100) NULL
  cAge3Message1 varchar(100) NULL
  cAge3Message2 varchar(100) NULL
  cAge4Message1 varchar(100) NULL
  cAge4Message2 varchar(100) NULL
  cAge5Message1 varchar(100) NULL
  cAge5Message2 varchar(100) NULL
  cAge6Message1 varchar(100) NULL
  cAge6Message2 varchar(100) NULL
  cAge7Message1 varchar(100) NULL
  cAge7Message2 varchar(100) NULL
  _etblTerms_iBranchID int NULL
  _etblTerms_dCreatedDate datetime NULL
  _etblTerms_dModifiedDate datetime NULL
  _etblTerms_iCreatedBranchID int NULL
  _etblTerms_iModifiedBranchID int NULL
  _etblTerms_iCreatedAgentID int NULL
  _etblTerms_iModifiedAgentID int NULL
  _etblTerms_iChangeSetID int NULL
  _etblTerms_Checksum binary(20) NULL

## _etblUnitCategory - Inventory Unit Category (UnitOfMeasureCategory)
Alias: Inventory Unit Category | Freedom Name: UnitOfMeasureCategory | Record Identifier: cUnitCatDescription
Notes: Inventory Unit Category
PK: idUnitCategory
Columns (11):
  idUnitCategory int NOT NULL identity PK
  cUnitCatDescription varchar(20) NOT NULL
  _etblUnitCategory_iBranchID int NULL
  _etblUnitCategory_dCreatedDate datetime NULL
  _etblUnitCategory_dModifiedDate datetime NULL
  _etblUnitCategory_iCreatedBranchID int NULL
  _etblUnitCategory_iModifiedBranchID int NULL
  _etblUnitCategory_iCreatedAgentID int NULL
  _etblUnitCategory_iModifiedAgentID int NULL
  _etblUnitCategory_iChangeSetID int NULL
  _etblUnitCategory_Checksum binary(20) NULL

## _etblUnitConversion - Inventory Unit Conversion (UnitOfMeasureConversion)
Alias: Inventory Unit Conversion | Freedom Name: UnitOfMeasureConversion | Record Identifier: 
Notes: Inventory Unit Conversion
PK: idUnitConversion
Columns (15):
  idUnitConversion int NOT NULL identity PK
  iUnitAID int NOT NULL
  fUnitAQty float NOT NULL
  iUnitBID int NOT NULL
  fUnitBQty float NOT NULL
  fMarkup float NULL
  _etblUnitConversion_iBranchID int NULL
  _etblUnitConversion_dCreatedDate datetime NULL
  _etblUnitConversion_dModifiedDate datetime NULL
  _etblUnitConversion_iCreatedBranchID int NULL
  _etblUnitConversion_iModifiedBranchID int NULL
  _etblUnitConversion_iCreatedAgentID int NULL
  _etblUnitConversion_iModifiedAgentID int NULL
  _etblUnitConversion_iChangeSetID int NULL
  _etblUnitConversion_Checksum binary(20) NULL

## _etblUnits - Unit (UnitOfMeasure)
Alias: Unit | Freedom Name: UnitOfMeasure | Record Identifier: cUnitCode
Notes: Unit
PK: idUnits
Columns (14):
  idUnits int NOT NULL identity PK
  cUnitCode varchar(10) NULL
  cUnitDescription varchar(50) NULL
  iUnitCategoryID int NULL
  bUnitRoundUp bit NOT NULL default (0)
  _etblUnits_iBranchID int NULL
  _etblUnits_dCreatedDate datetime NULL
  _etblUnits_dModifiedDate datetime NULL
  _etblUnits_iCreatedBranchID int NULL
  _etblUnits_iModifiedBranchID int NULL
  _etblUnits_iCreatedAgentID int NULL
  _etblUnits_iModifiedAgentID int NULL
  _etblUnits_iChangeSetID int NULL
  _etblUnits_Checksum binary(20) NULL

## _etblUserHistLink
PK: idUserHistLink
Columns (14):
  idUserHistLink bigint NOT NULL identity PK
  UserDictID int NOT NULL
  TableID bigint NOT NULL
  UserValue varchar(1024) NOT NULL
  LastModifiedDate datetime NOT NULL default getdate()
  _etblUserHistLink_iBranchID int NULL
  _etblUserHistLink_dCreatedDate datetime NULL
  _etblUserHistLink_dModifiedDate datetime NULL
  _etblUserHistLink_iCreatedBranchID int NULL
  _etblUserHistLink_iModifiedBranchID int NULL
  _etblUserHistLink_iCreatedAgentID int NULL
  _etblUserHistLink_iModifiedAgentID int NULL
  _etblUserHistLink_iChangeSetID int NULL
  _etblUserHistLink_Checksum binary(20) NULL

## _etblVASAirtimeItem
PK: idVASAirtimeItem
Columns (13):
  idVASAirtimeItem int NOT NULL identity PK
  idVASAirtimeMaster int NOT NULL
  iStockLink int NOT NULL
  dDiscountPercentage decimal(18,0) NULL
  _etblVASAirtimeItem_iBranchID int NULL
  _etblVASAirtimeItem_dCreatedDate datetime NULL
  _etblVASAirtimeItem_dModifiedDate datetime NULL
  _etblVASAirtimeItem_iCreatedBranchID int NULL
  _etblVASAirtimeItem_iModifiedBranchID int NULL
  _etblVASAirtimeItem_iCreatedAgentID int NULL
  _etblVASAirtimeItem_iModifiedAgentID int NULL
  _etblVASAirtimeItem_iChangeSetID int NULL
  _etblVASAirtimeItem_Checksum binary(20) NULL

## _etblVASAirtimeMaster
PK: idVASAirtimeMaster
Columns (15):
  idVASAirtimeMaster int NOT NULL identity PK
  cContractCode nvarchar(20) NOT NULL
  cContractDescription nvarchar(100) NOT NULL
  iSetupType int NOT NULL
  bActive bit NULL
  bDeleted bit NULL
  _etblVASAirtimeMaster_iBranchID int NULL
  _etblVASAirtimeMaster_dCreatedDate datetime NULL
  _etblVASAirtimeMaster_dModifiedDate datetime NULL
  _etblVASAirtimeMaster_iCreatedBranchID int NULL
  _etblVASAirtimeMaster_iModifiedBranchID int NULL
  _etblVASAirtimeMaster_iCreatedAgentID int NULL
  _etblVASAirtimeMaster_iModifiedAgentID int NULL
  _etblVASAirtimeMaster_iChangeSetID int NULL
  _etblVASAirtimeMaster_Checksum binary(20) NULL

## _etblVASAirtimeNetwork
PK: idVASAirtimeNetwork
Columns (16):
  idVASAirtimeNetwork int NOT NULL identity PK
  idVASAirtimeMaster int NOT NULL
  cNetworkCode nvarchar(20) NOT NULL
  cNetworkName nvarchar(50) NOT NULL
  cNetworkDescription nvarchar(100) NOT NULL
  iStockLink int NOT NULL
  dDiscountPercentage decimal(18,0) NULL
  _etblVASAirtimeNetwork_iBranchID int NULL
  _etblVASAirtimeNetwork_dCreatedDate datetime NULL
  _etblVASAirtimeNetwork_dModifiedDate datetime NULL
  _etblVASAirtimeNetwork_iCreatedBranchID int NULL
  _etblVASAirtimeNetwork_iModifiedBranchID int NULL
  _etblVASAirtimeNetwork_iCreatedAgentID int NULL
  _etblVASAirtimeNetwork_iModifiedAgentID int NULL
  _etblVASAirtimeNetwork_iChangeSetID int NULL
  _etblVASAirtimeNetwork_Checksum binary(20) NULL

## _etblVASAirtimeProduct
PK: idVASAirtimeProduct
Columns (16):
  idVASAirtimeProduct int NOT NULL identity PK
  idVASAirtimeNetwork int NOT NULL
  cProductCode nvarchar(20) NOT NULL
  cProductDescription nvarchar(100) NOT NULL
  dProductPrice decimal(18,0) NOT NULL
  iStockLink int NOT NULL
  dDiscountPercentage decimal(18,0) NULL
  _etblVASAirtimeProduct_iBranchID int NULL
  _etblVASAirtimeProduct_dCreatedDate datetime NULL
  _etblVASAirtimeProduct_dModifiedDate datetime NULL
  _etblVASAirtimeProduct_iCreatedBranchID int NULL
  _etblVASAirtimeProduct_iModifiedBranchID int NULL
  _etblVASAirtimeProduct_iCreatedAgentID int NULL
  _etblVASAirtimeProduct_iModifiedAgentID int NULL
  _etblVASAirtimeProduct_iChangeSetID int NULL
  _etblVASAirtimeProduct_Checksum binary(20) NULL

## _etblVATSubmission
PK: idVATSubmission
Columns (12):
  idVATSubmission int NOT NULL identity PK
  iSubmissionStatus int NOT NULL
  iPeriodTxSummary int NOT NULL
  _etblVATSubmission_iBranchID int NULL
  _etblVATSubmission_dCreatedDate datetime NULL
  _etblVATSubmission_dModifiedDate datetime NULL
  _etblVATSubmission_iCreatedBranchID int NULL
  _etblVATSubmission_iModifiedBranchID int NULL
  _etblVATSubmission_iCreatedAgentID int NULL
  _etblVATSubmission_iModifiedAgentID int NULL
  _etblVATSubmission_iChangeSetID int NULL
  _etblVATSubmission_Checksum binary(20) NULL

## _etblVATSubmissionStages
PK: idVATSubmissionStages
Columns (22):
  idVATSubmissionStages int NOT NULL identity PK
  iVATSubmission int NOT NULL
  cSubmissionStage varchar(100) NULL
  cExecutionID varchar(100) NULL
  cRequestID varchar(100) NULL
  cApiUserID varchar(100) NULL
  cBusinessInfoUrl varchar(2000) NULL
  cBusinessInfoID varchar(100) NULL
  cTransactionsInfoUrl varchar(2000) NULL
  cTransactionsInfoID varchar(100) NULL
  cPollingUrl varchar(2000) NULL
  cTokenUrl varchar(2000) NULL
  cNavigateToUrl varchar(2000) NULL
  _etblVATSubmissionStages_iBranchID int NULL
  _etblVATSubmissionStages_dCreatedDate datetime NULL
  _etblVATSubmissionStages_dModifiedDate datetime NULL
  _etblVATSubmissionStages_iCreatedBranchID int NULL
  _etblVATSubmissionStages_iModifiedBranchID int NULL
  _etblVATSubmissionStages_iCreatedAgentID int NULL
  _etblVATSubmissionStages_iModifiedAgentID int NULL
  _etblVATSubmissionStages_iChangeSetID int NULL
  _etblVATSubmissionStages_Checksum binary(20) NULL

## _etblVATUID
PK: idVATUID
Columns (11):
  idVATUID int NOT NULL identity PK
  cVATUIDName varchar(100) NULL
  _etblVATUID_iBranchID int NULL
  _etblVATUID_dCreatedDate datetime NULL
  _etblVATUID_dModifiedDate datetime NULL
  _etblVATUID_iCreatedBranchID int NULL
  _etblVATUID_iModifiedBranchID int NULL
  _etblVATUID_iCreatedAgentID int NULL
  _etblVATUID_iModifiedAgentID int NULL
  _etblVATUID_iChangeSetID int NULL
  _etblVATUID_Checksum binary(20) NULL

## _etblVDAP - AP Volume Discount
Alias: AP Volume Discount | Freedom Name:  | Record Identifier: 
Notes: AP Volume Discounts Header Listing. Rules: 1. The system uses the most specific volume discount contract available. 2. If the most specific level does not have any lines for the inventory item, the system would look at the next less specific level.
PK: IDVD
Columns (18):
  IDVD int NOT NULL identity PK
  iARAPID int NULL
  iGroupID int NULL default (0)
  iCurrencyID int NOT NULL default (0)
  cContractName varchar(40) NULL
  bOnHold bit NOT NULL default (0)
  tDescription text NULL
  bARAPAll bit NULL default (0)
  bIsTemplate bit NOT NULL default (0)
  _etblVDAP_iBranchID int NULL
  _etblVDAP_dCreatedDate datetime NULL
  _etblVDAP_dModifiedDate datetime NULL
  _etblVDAP_iCreatedBranchID int NULL
  _etblVDAP_iModifiedBranchID int NULL
  _etblVDAP_iCreatedAgentID int NULL
  _etblVDAP_iModifiedAgentID int NULL
  _etblVDAP_iChangeSetID int NULL
  _etblVDAP_Checksum binary(20) NULL

## _etblVDAR - AR Volume Discount
Alias: AR Volume Discount | Freedom Name:  | Record Identifier: 
Notes: AR Volume Discounts Header Listing. Rules: 1. The system uses the most specific volume discount contract available. 2. If the most specific level does not have any lines for the inventory item, the system would look at the next less specific level.
PK: IDVD
Columns (18):
  IDVD int NOT NULL identity PK
  iARAPID int NULL
  iGroupID int NULL default (0)
  iCurrencyID int NOT NULL default (0)
  cContractName varchar(40) NULL
  bOnHold bit NOT NULL default (0)
  tDescription text NULL
  bARAPAll bit NULL default (0)
  bIsTemplate bit NOT NULL default (0)
  _etblVDAR_iBranchID int NULL
  _etblVDAR_dCreatedDate datetime NULL
  _etblVDAR_dModifiedDate datetime NULL
  _etblVDAR_iCreatedBranchID int NULL
  _etblVDAR_iModifiedBranchID int NULL
  _etblVDAR_iCreatedAgentID int NULL
  _etblVDAR_iModifiedAgentID int NULL
  _etblVDAR_iChangeSetID int NULL
  _etblVDAR_Checksum binary(20) NULL

## _etblVDLnAP - AP Volume Discount Line
Alias: AP Volume Discount Line | Freedom Name:  | Record Identifier: 
Notes: AP Volume Discount Line
PK: IDVDLn
Columns (20):
  IDVDLn int NOT NULL identity PK
  iVDID int NULL
  iStockID int NULL
  iStGroupID int NULL default (0)
  iCurrencyID int NOT NULL default (0)
  dEffDate smalldatetime NULL
  dExpDate smalldatetime NULL
  bUseStockPrc bit NOT NULL default (0)
  cEnterInclExcl varchar(1) NULL default 'E'
  bIncremental bit NOT NULL default (0)
  bStockAll bit NULL default (0)
  _etblVDLnAP_iBranchID int NULL
  _etblVDLnAP_dCreatedDate datetime NULL
  _etblVDLnAP_dModifiedDate datetime NULL
  _etblVDLnAP_iCreatedBranchID int NULL
  _etblVDLnAP_iModifiedBranchID int NULL
  _etblVDLnAP_iCreatedAgentID int NULL
  _etblVDLnAP_iModifiedAgentID int NULL
  _etblVDLnAP_iChangeSetID int NULL
  _etblVDLnAP_Checksum binary(20) NULL

## _etblVDLnAR - AR Volume Discount Line
Alias: AR Volume Discount Line | Freedom Name:  | Record Identifier: 
Notes: AR Volume Discount Line
PK: IDVDLn
Columns (20):
  IDVDLn int NOT NULL identity PK
  iVDID int NULL
  iStockID int NULL
  iStGroupID int NULL default (0)
  iCurrencyID int NOT NULL default (0)
  dEffDate smalldatetime NULL
  dExpDate smalldatetime NULL
  bUseStockPrc bit NOT NULL default (0)
  cEnterInclExcl varchar(1) NULL default 'E'
  bIncremental bit NOT NULL default (0)
  bStockAll bit NULL default (0)
  _etblVDLnAR_iBranchID int NULL
  _etblVDLnAR_dCreatedDate datetime NULL
  _etblVDLnAR_dModifiedDate datetime NULL
  _etblVDLnAR_iCreatedBranchID int NULL
  _etblVDLnAR_iModifiedBranchID int NULL
  _etblVDLnAR_iCreatedAgentID int NULL
  _etblVDLnAR_iModifiedAgentID int NULL
  _etblVDLnAR_iChangeSetID int NULL
  _etblVDLnAR_Checksum binary(20) NULL

## _etblVDLnLvlAP - AP Volume Discount Line Level
Alias: AP Volume Discount Line Level | Freedom Name:  | Record Identifier: 
Notes: AP Volume Discount Line Level
PK: IDVDLnLvl
Columns (15):
  IDVDLnLvl int NOT NULL identity PK
  iVDLnID int NULL
  iLevel int NULL
  fQuantity float NULL
  fPriceDisc float NULL
  _etblVDLnLvlAP_iBranchID int NULL
  _etblVDLnLvlAP_dCreatedDate datetime NULL
  _etblVDLnLvlAP_dModifiedDate datetime NULL
  _etblVDLnLvlAP_iCreatedBranchID int NULL
  _etblVDLnLvlAP_iModifiedBranchID int NULL
  _etblVDLnLvlAP_iCreatedAgentID int NULL
  _etblVDLnLvlAP_iModifiedAgentID int NULL
  _etblVDLnLvlAP_iChangeSetID int NULL
  _etblVDLnLvlAP_Checksum binary(20) NULL
  iVDUOMID int NULL default (0)

## _etblVDLnLvlAR - AR Volume Discount Line Level
Alias: AR Volume Discount Line Level | Freedom Name:  | Record Identifier: 
Notes: AR Volume Discount Line Level
PK: IDVDLnLvl
Columns (15):
  IDVDLnLvl int NOT NULL identity PK
  iVDLnID int NULL
  iLevel int NULL
  fQuantity float NULL
  fPriceDisc float NULL
  _etblVDLnLvlAR_iBranchID int NULL
  _etblVDLnLvlAR_dCreatedDate datetime NULL
  _etblVDLnLvlAR_dModifiedDate datetime NULL
  _etblVDLnLvlAR_iCreatedBranchID int NULL
  _etblVDLnLvlAR_iModifiedBranchID int NULL
  _etblVDLnLvlAR_iCreatedAgentID int NULL
  _etblVDLnLvlAR_iModifiedAgentID int NULL
  _etblVDLnLvlAR_iChangeSetID int NULL
  _etblVDLnLvlAR_Checksum binary(20) NULL
  iVDUOMID int NULL default (0)

## _etblWhDefaults - Warehouse Default (WareHouseDefaults)
Alias: Warehouse Default | Freedom Name: WareHouseDefaults | Record Identifier: 
Notes: Warehouse Default
PK: IDWhDefaults
Columns (49):
  IDWhDefaults int NOT NULL identity PK
  bWhTfBatchAutoNum bit NOT NULL default (1)
  cWhTfBatchPrefix varchar(25) NULL
  iWhTfBatchPadLength int NULL
  iWhTfTrCodeID int NULL
  bWhTfRefAutoNum bit NOT NULL default (1)
  cWhTfRefPrefix varchar(25) NULL
  iWhTfRefPadLength int NULL
  bIBTNumAutoNum bit NOT NULL default (1)
  cIBTNumPrefix varchar(25) NULL
  iIBTNumPadLength int NULL
  iIBTTrCodeID int NULL
  iIBTAddCostTrCodeID int NULL
  bIBTDelNoteAutoNum bit NOT NULL default (1)
  cIBTDelNotePrefix varchar(25) NULL
  iIBTDelNotePadLength int NOT NULL
  iDefInTransitWHID int NULL
  iDefVarianceWHID int NULL
  iDefDamagedWHID int NULL
  bWhseIBTActivated bit NOT NULL default (0)
  bForceProject bit NOT NULL default (0)
  iBranchLoanAccountID int NULL
  bIBTDefaultCostToIssue bit NOT NULL default (0)
  bIBTAllowOverDelivery bit NOT NULL default (0)
  cIBTRequestNumPrefix varchar(25) NULL
  iIBTRequestNumPadLength int NULL
  bIBTRequestNumAutoNum bit NOT NULL default (1)
  _etblWhDefaults_iBranchID int NULL
  _etblWhDefaults_dCreatedDate datetime NULL
  _etblWhDefaults_dModifiedDate datetime NULL
  _etblWhDefaults_iCreatedBranchID int NULL
  _etblWhDefaults_iModifiedBranchID int NULL
  _etblWhDefaults_iCreatedAgentID int NULL
  _etblWhDefaults_iModifiedAgentID int NULL
  _etblWhDefaults_iChangeSetID int NULL
  _etblWhDefaults_Checksum binary(20) NULL
  bUseMultiBins bit NOT NULL default (0)
  cBinSeperator varchar(1) NULL
  bUseBinLocationLevels bit NOT NULL default (0)
  bBinTfBatchAutoNum bit NOT NULL default (1)
  cBinTfBatchPrefix varchar(25) NULL
  iBinTfBatchPadLength int NULL
  iBinTfTrCodeID int NULL
  bBinTfRefAutoNum bit NOT NULL default (1)
  cBinTfRefPrefix varchar(25) NULL
  iBinTfRefPadLength int NULL
  bBinTfForceProject bit NOT NULL default (0)
  bUpdateToItemCost bit NOT NULL default (0)
  bIBTOnlySyncProcessed bit NOT NULL default (0)

## _etblWhseIBT - Inventory IBT (InterBranchTransferHeader)
Alias: Inventory IBT | Freedom Name: InterBranchTransferHeader | Record Identifier: 
Notes: Inventory IBT
PK: IDWhseIBT
Columns (41):
  IDWhseIBT int NOT NULL identity PK
  cIBTNumber varchar(50) NULL
  cIBTDescription varchar(40) NULL
  iWhseIDFrom int NULL
  iWhseIDTo int NULL
  iWhseIDIntransit int NULL
  iWhseIDVariance int NULL
  iWhseIDDamaged int NULL
  iIBTStatus int NULL
  cDelNoteNumber varchar(50) NULL
  iProjectID int NOT NULL default (0)
  dDateIssued datetime NULL
  dDateReceived datetime NULL
  cAuditNumberIssued varchar(50) NULL
  cAuditNumberReceived varchar(50) NULL
  bUseAddCostPerLine bit NOT NULL default (0)
  fFixedAddCost float NOT NULL default (0)
  iAgentIDIssue int NOT NULL default (0)
  iAgentIDReceive int NOT NULL default (0)
  iBranchIDFrom int NULL
  dDateRequired datetime NULL
  dDateRequested datetime NULL
  dDateApproved datetime NULL
  iLinkedReqID int NULL
  _etblWhseIBT_iBranchID int NULL
  _etblWhseIBT_dCreatedDate datetime NULL
  _etblWhseIBT_dModifiedDate datetime NULL
  _etblWhseIBT_iCreatedBranchID int NULL
  _etblWhseIBT_iModifiedBranchID int NULL
  _etblWhseIBT_iCreatedAgentID int NULL
  _etblWhseIBT_iModifiedAgentID int NULL
  _etblWhseIBT_iChangeSetID int NULL
  _etblWhseIBT_Checksum binary(20) NULL
  iIBTAction int NULL
  cIBTReference1 nvarchar(100) NULL
  cIBTReference2 nvarchar(100) NULL
  dActionIssueStock datetime NULL
  dActionShipStock datetime NULL
  dActionAckStock datetime NULL
  dActionRecieveStock datetime NULL
  bVarianceCleared bit NOT NULL default (0)

## _etblWhseIBTAddCosts - Inventory IBT Additional Cost
Alias: Inventory IBT Additional Cost | Freedom Name:  | Record Identifier: 
Notes: Inventory IBT Additional Cost
PK: IDWhseIBTAddCosts
Columns (20):
  IDWhseIBTAddCosts int NOT NULL identity PK
  iWhseIBTID int NOT NULL
  iSupplierID int NOT NULL
  cReference varchar(20) NULL
  cDescription varchar(40) NULL
  fLineTotalExcl float NOT NULL default (0)
  iTaxTypeID int NOT NULL default (0)
  fLineTaxAmount float NOT NULL default (0)
  iCurrencyID int NOT NULL default (0)
  fExchangeRate float NOT NULL default (0)
  fLineTotalExclForeign float NOT NULL default (0)
  _etblWhseIBTAddCosts_iBranchID int NULL
  _etblWhseIBTAddCosts_dCreatedDate datetime NULL
  _etblWhseIBTAddCosts_dModifiedDate datetime NULL
  _etblWhseIBTAddCosts_iCreatedBranchID int NULL
  _etblWhseIBTAddCosts_iModifiedBranchID int NULL
  _etblWhseIBTAddCosts_iCreatedAgentID int NULL
  _etblWhseIBTAddCosts_iModifiedAgentID int NULL
  _etblWhseIBTAddCosts_iChangeSetID int NULL
  _etblWhseIBTAddCosts_Checksum binary(20) NULL

## _etblWhseIBTLines - Inventory IBT Line (InterBranchTransferLines)
Alias: Inventory IBT Line | Freedom Name: InterBranchTransferLines | Record Identifier: 
Notes: Inventory IBT Line
PK: IDWhseIBTLines
Columns (45):
  IDWhseIBTLines bigint NOT NULL identity PK
  iWhseIBTID int NULL
  iStockID int NULL
  cReference varchar(20) NULL
  cDescription varchar(40) NULL
  iProjectID int NOT NULL default (0)
  bIsSerialItem bit NOT NULL default (0)
  bIsLotItem bit NOT NULL default (0)
  iLotID int NULL
  cLotNumber varchar(50) NULL
  dLotExpiryDate datetime NULL
  fQtyIssued float NULL
  fQtyReceived float NULL
  fQtyDamaged float NULL
  fQtyVariance float NULL
  fQtyOverDelivered float NOT NULL default (0)
  fNewReceiveCost float NULL
  iSNIssuedGroupID int NULL
  iSNReceivedGroupID int NULL
  iSNDamagedGroupID int NULL
  iSNVarianceGroupID int NULL
  cLineNotes varchar(1024) NULL
  fAdditionalCost float NOT NULL default (0)
  fIssuedCost float NULL
  iUnitsOfMeasureStockingID int NULL
  iUnitsOfMeasureCategoryID int NULL
  iUnitsOfMeasureID int NULL
  fQtyRequired float NOT NULL default (0)
  fQtyApproved float NOT NULL default (0)
  iReqLineStatus int NULL
  _etblWhseIBTLines_iBranchID int NULL
  _etblWhseIBTLines_dCreatedDate datetime NULL
  _etblWhseIBTLines_dModifiedDate datetime NULL
  _etblWhseIBTLines_iCreatedBranchID int NULL
  _etblWhseIBTLines_iModifiedBranchID int NULL
  _etblWhseIBTLines_iCreatedAgentID int NULL
  _etblWhseIBTLines_iModifiedAgentID int NULL
  _etblWhseIBTLines_iChangeSetID int NULL
  _etblWhseIBTLines_Checksum binary(20) NULL
  xIBTAttribute xml NULL
  fQtyOverDamaged float NOT NULL default (0)
  bClearLineVariance bit NOT NULL default (0)
  iFromStockBinLocationID int NOT NULL default (0)
  iToStockBinLocationID int NOT NULL default (0)
  iDamageStockBinLocationID int NOT NULL default (0)

## _etblWhseIBTLineSN - Inventory IBT Line Serial Number (InterBranchTransferSerialNumberLines)
Alias: Inventory IBT Line Serial Number | Freedom Name: InterBranchTransferSerialNumberLines | Record Identifier: 
Notes: Inventory IBT Line Serial Number
PK: IDWhseIBTLineSN
Columns (13):
  IDWhseIBTLineSN bigint NOT NULL identity PK
  iWhseIBTID int NULL
  iSNGroupID int NULL
  iSerialMFID int NULL
  _etblWhseIBTLineSN_iBranchID int NULL
  _etblWhseIBTLineSN_dCreatedDate datetime NULL
  _etblWhseIBTLineSN_dModifiedDate datetime NULL
  _etblWhseIBTLineSN_iCreatedBranchID int NULL
  _etblWhseIBTLineSN_iModifiedBranchID int NULL
  _etblWhseIBTLineSN_iCreatedAgentID int NULL
  _etblWhseIBTLineSN_iModifiedAgentID int NULL
  _etblWhseIBTLineSN_iChangeSetID int NULL
  _etblWhseIBTLineSN_Checksum binary(20) NULL

## _etblWhseTransferBatches - Inventory Warehouse Transfer Batch
Alias: Inventory Warehouse Transfer Batch | Freedom Name:  | Record Identifier: cBatchNo
Notes: Inventory Warehouse Transfer Batch
PK: idWhseTransferBatch
Columns (30):
  idWhseTransferBatch int NOT NULL identity PK
  cBatchNo varchar(50) NULL
  cBatchDescription varchar(40) NULL
  iTrCodeID int NULL
  iCreateAgentID int NULL
  bClearBatchAfterPost bit NOT NULL default (1)
  bAllowDuplicateRef bit NOT NULL default (1)
  bPrintJournal bit NOT NULL default (1)
  iNewLineRefOpt int NULL
  cNewLineRefDef varchar(20) NULL
  bNewLineRefIncr bit NOT NULL default (0)
  iNewLineDescOpt int NULL
  cNewLineDescDef varchar(40) NULL
  bNewLineDescIncr bit NOT NULL default (0)
  iNewLineWHFromOpt int NULL
  iNewLineWHFromDefID int NULL
  iNewLineWHToOpt int NULL
  iNewLineWHToDefID int NULL
  iNewLineProjectOpt int NULL
  iNewLineProjectDefID int NULL
  cBatchRefNo varchar(50) NULL
  _etblWhseTransferBatches_iBranchID int NULL
  _etblWhseTransferBatches_dCreatedDate datetime NULL
  _etblWhseTransferBatches_dModifiedDate datetime NULL
  _etblWhseTransferBatches_iCreatedBranchID int NULL
  _etblWhseTransferBatches_iModifiedBranchID int NULL
  _etblWhseTransferBatches_iCreatedAgentID int NULL
  _etblWhseTransferBatches_iModifiedAgentID int NULL
  _etblWhseTransferBatches_iChangeSetID int NULL
  _etblWhseTransferBatches_Checksum binary(20) NULL

## _etblWhseTransferBatchLines - Inventory Warehouse Transfer Batch Line
Alias: Inventory Warehouse Transfer Batch Line | Freedom Name:  | Record Identifier: 
Notes: Inventory Warehouse Transfer Batch Line
PK: idWhseTransferBatchLines
Columns (32):
  idWhseTransferBatchLines int NOT NULL identity PK
  iWhseTransferBatchID int NULL
  iStockID int NULL
  iFromWhseID int NULL
  iToWhseID int NULL
  fQuantity float NULL
  fCost float NULL
  cReference varchar(20) NULL
  cDescription varchar(40) NULL
  bIsSerialItem bit NOT NULL default (0)
  iSerialNumberGroupID int NULL
  bIsLotItem bit NOT NULL default (0)
  iLotID int NOT NULL default (0)
  cLotNumber varchar(50) NULL
  dLotExpiryDate datetime NULL
  iProjectID int NOT NULL default (0)
  cLineNotes varchar(1024) NULL
  iUnitsOfMeasureStockingID int NULL
  iUnitsOfMeasureCategoryID int NULL
  iUnitsOfMeasureID int NULL
  _etblWhseTransferBatchLines_iBranchID int NULL
  _etblWhseTransferBatchLines_dCreatedDate datetime NULL
  _etblWhseTransferBatchLines_dModifiedDate datetime NULL
  _etblWhseTransferBatchLines_iCreatedBranchID int NULL
  _etblWhseTransferBatchLines_iModifiedBranchID int NULL
  _etblWhseTransferBatchLines_iCreatedAgentID int NULL
  _etblWhseTransferBatchLines_iModifiedAgentID int NULL
  _etblWhseTransferBatchLines_iChangeSetID int NULL
  _etblWhseTransferBatchLines_Checksum binary(20) NULL
  xWTAttribute xml NULL
  iFromStockBinLocationID int NOT NULL default (0)
  iToStockBinLocationID int NOT NULL default (0)

## _etblWorkers - Worker (PayrollWorker)
Alias: Worker | Freedom Name: PayrollWorker | Record Identifier: 
Notes: Worker
PK: idWorkers
Columns (15):
  idWorkers int NOT NULL identity PK
  cWorkerCode varchar(20) NOT NULL
  cWorkerName varchar(50) NULL
  bActive bit NOT NULL default (1)
  fWorkerCost float NULL
  fBillableRate float NULL
  _etblWorkers_iBranchID int NULL
  _etblWorkers_dCreatedDate datetime NULL
  _etblWorkers_dModifiedDate datetime NULL
  _etblWorkers_iCreatedBranchID int NULL
  _etblWorkers_iModifiedBranchID int NULL
  _etblWorkers_iCreatedAgentID int NULL
  _etblWorkers_iModifiedAgentID int NULL
  _etblWorkers_iChangeSetID int NULL
  _etblWorkers_Checksum binary(20) NULL
