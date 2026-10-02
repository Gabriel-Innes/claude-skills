# Sage 200 Evolution table dictionary - Business modules

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _btblAgentOptions
PK: IDAgentOptions
Columns (34):
  IDAgentOptions int NOT NULL identity PK
  iAgentID int NOT NULL
  iCalTimeFormat int NULL
  iCalDVDaysVisible int NULL
  iCalDVTimeInterval int NULL
  bCalDVShowWeekends bit NOT NULL default (1)
  bCalWVShowEventTimes bit NOT NULL default (0)
  bCalMVShowEvents bit NOT NULL default (1)
  bCalMVShowEventTimes bit NOT NULL default (0)
  bAlarmSet bit NOT NULL default (0)
  iAlarmAdvance int NULL
  iAlarmAdvanceType int NULL
  cDingPath varchar(255) NULL
  bShowContactPerson bit NOT NULL default (1)
  bShowIncTypeGroup bit NOT NULL default (1)
  bShowWorkflow bit NOT NULL default (1)
  bShowEscGroup bit NOT NULL default (1)
  bShowInvItem bit NOT NULL default (1)
  bShowSupplier bit NOT NULL default (1)
  bShowWorker bit NOT NULL default (1)
  bShowFixedAssets bit NOT NULL default (1)
  bShowProject bit NOT NULL default (1)
  bShowJobCosting bit NOT NULL default (1)
  bShowProspect bit NOT NULL default (1)
  bShowOpportunity bit NULL default (1)
  _btblAgentOptions_iBranchID int NULL
  _btblAgentOptions_dCreatedDate datetime NULL
  _btblAgentOptions_dModifiedDate datetime NULL
  _btblAgentOptions_iCreatedBranchID int NULL
  _btblAgentOptions_iModifiedBranchID int NULL
  _btblAgentOptions_iCreatedAgentID int NULL
  _btblAgentOptions_iModifiedAgentID int NULL
  _btblAgentOptions_iChangeSetID int NULL
  _btblAgentOptions_Checksum binary(20) NULL

## _btblAgentOutOffice - Agent Out Of Office (AgentOutOfOffice)
Alias: Agent Out Of Office | Freedom Name: AgentOutOfOffice | Record Identifier: 
Notes: Agent Out Of Office. Agents marked as out of office.
PK: IDAgentOutOffice
Columns (14):
  IDAgentOutOffice int NOT NULL identity PK
  iAgentID int NOT NULL
  dDateFrom datetime NULL
  dDateTo datetime NULL
  iReason int NULL
  _btblAgentOutOffice_iBranchID int NULL
  _btblAgentOutOffice_dCreatedDate datetime NULL
  _btblAgentOutOffice_dModifiedDate datetime NULL
  _btblAgentOutOffice_iCreatedBranchID int NULL
  _btblAgentOutOffice_iModifiedBranchID int NULL
  _btblAgentOutOffice_iCreatedAgentID int NULL
  _btblAgentOutOffice_iModifiedAgentID int NULL
  _btblAgentOutOffice_iChangeSetID int NULL
  _btblAgentOutOffice_Checksum binary(20) NULL

## _btblAgentOutOfficeReasons - Agent Out Office Reasons (AgentOutOfOfficeReasons)
Alias: Agent Out Office Reasons | Freedom Name: AgentOutOfOfficeReasons | Record Identifier: 
Notes: Agent Out Office Reasons.
PK: iAgentOutOfficeID
Columns (11):
  iAgentOutOfficeID int NOT NULL identity PK
  cReason varchar(50) NOT NULL
  _btblAgentOutOfficeReasons_iBranchID int NULL
  _btblAgentOutOfficeReasons_dCreatedDate datetime NULL
  _btblAgentOutOfficeReasons_dModifiedDate datetime NULL
  _btblAgentOutOfficeReasons_iCreatedBranchID int NULL
  _btblAgentOutOfficeReasons_iModifiedBranchID int NULL
  _btblAgentOutOfficeReasons_iCreatedAgentID int NULL
  _btblAgentOutOfficeReasons_iModifiedAgentID int NULL
  _btblAgentOutOfficeReasons_iChangeSetID int NULL
  _btblAgentOutOfficeReasons_Checksum binary(20) NULL

## _btblAgentSystemFunctions - Agent System Function (AgentSystemFunctions)
Alias: Agent System Function | Freedom Name: AgentSystemFunctions | Record Identifier: 
Notes: User rigths set up for the users - for internal use only
PK: iAgentID+cAgentType+iSystemFunctionID
Columns (17):
  iAgentID int NOT NULL PK
  cAgentType char(1) NOT NULL PK
  iSystemFunctionID int NOT NULL PK
  iReadAccess int NULL
  iEditAccess int NULL
  iAddAccess int NULL
  iDeleteAccess int NULL
  iRuleAccess int NULL
  _btblAgentSystemFunctions_iBranchID int NULL
  _btblAgentSystemFunctions_dCreatedDate datetime NULL
  _btblAgentSystemFunctions_dModifiedDate datetime NULL
  _btblAgentSystemFunctions_iCreatedBranchID int NULL
  _btblAgentSystemFunctions_iModifiedBranchID int NULL
  _btblAgentSystemFunctions_iCreatedAgentID int NULL
  _btblAgentSystemFunctions_iModifiedAgentID int NULL
  _btblAgentSystemFunctions_iChangeSetID int NULL
  _btblAgentSystemFunctions_Checksum binary(20) NULL

## _btblAgentSystemTree - Agent System Tree (AgentSystemTree)
Alias: Agent System Tree | Freedom Name: AgentSystemTree | Record Identifier: 
Notes: Agent System Tree. Accesss permissions set up per agent.
PK: idAgentSystemTree
Columns (20):
  idAgentSystemTree int NOT NULL identity PK
  iAgentID int NOT NULL
  cAgentType char(1) NOT NULL
  iSystemTreeID int NOT NULL
  iParentAgentSystemTreeID int NOT NULL
  iOrder int NOT NULL
  cDescription varchar(64) NULL
  cToolbar varchar(50) NULL
  cMenu varchar(50) NULL
  cMenuName varchar(50) NULL
  bMenuSub bit NOT NULL default (0)
  _btblAgentSystemTree_iBranchID int NULL
  _btblAgentSystemTree_dCreatedDate datetime NULL
  _btblAgentSystemTree_dModifiedDate datetime NULL
  _btblAgentSystemTree_iCreatedBranchID int NULL
  _btblAgentSystemTree_iModifiedBranchID int NULL
  _btblAgentSystemTree_iCreatedAgentID int NULL
  _btblAgentSystemTree_iModifiedAgentID int NULL
  _btblAgentSystemTree_iChangeSetID int NULL
  _btblAgentSystemTree_Checksum binary(20) NULL

## _btblAges - Ages (Age)
Alias: Ages | Freedom Name: Age | Record Identifier: 
PK: idAges
Columns (12):
  idAges int NOT NULL identity PK
  nARAges image NULL
  nAPAges image NULL
  _btblAges_iBranchID int NULL
  _btblAges_dCreatedDate datetime NULL
  _btblAges_dModifiedDate datetime NULL
  _btblAges_iCreatedBranchID int NULL
  _btblAges_iModifiedBranchID int NULL
  _btblAges_iCreatedAgentID int NULL
  _btblAges_iModifiedAgentID int NULL
  _btblAges_iChangeSetID int NULL
  _btblAges_Checksum binary(20) NULL

## _btblBatchCheckout - Batch Checkout (BatchCheckout)
Alias: Batch Checkout | Freedom Name: BatchCheckout | Record Identifier: 
Notes: Batch Checkout. Batches currently open and in use by Agents.
PK: idBatchCheckout
Columns (16):
  idBatchCheckout int NOT NULL identity PK
  cBatchClass varchar(32) NOT NULL
  iBatchID bigint NOT NULL
  cNetworkUser varchar(32) NOT NULL
  cAgentName varchar(50) NULL
  cCheckoutGUID varchar(50) NOT NULL
  bIncludeOpenBatches bit NOT NULL default (0)
  _btblBatchCheckout_iBranchID int NULL
  _btblBatchCheckout_dCreatedDate datetime NULL
  _btblBatchCheckout_dModifiedDate datetime NULL
  _btblBatchCheckout_iCreatedBranchID int NULL
  _btblBatchCheckout_iModifiedBranchID int NULL
  _btblBatchCheckout_iCreatedAgentID int NULL
  _btblBatchCheckout_iModifiedAgentID int NULL
  _btblBatchCheckout_iChangeSetID int NULL
  _btblBatchCheckout_Checksum binary(20) NULL

## _btblBINLocation
PK: idBinLocation
Columns (12):
  idBinLocation int NOT NULL identity PK
  cBinLocationName varchar(125) NULL
  cBinLocationDescription varchar(125) NULL
  _btblBINLocation_iBranchID int NULL
  _btblBINLocation_dCreatedDate datetime NULL
  _btblBINLocation_dModifiedDate datetime NULL
  _btblBINLocation_iCreatedBranchID int NULL
  _btblBINLocation_iModifiedBranchID int NULL
  _btblBINLocation_iCreatedAgentID int NULL
  _btblBINLocation_iModifiedAgentID int NULL
  _btblBINLocation_iChangeSetID int NULL
  _btblBINLocation_Checksum binary(20) NULL

## _btblBINLocationWhseLinks
PK: idBinLocationWhseLinks
Columns (27):
  idBinLocationWhseLinks int NOT NULL identity PK
  iBinLocationID int NOT NULL
  iBinLevelWarehouseID int NOT NULL default (-1)
  iBinLevel0ValueID int NOT NULL default (0)
  iBinLevel1ValueID int NOT NULL default (0)
  iBinLevel2ValueID int NOT NULL default (0)
  iBinLevel3ValueID int NOT NULL default (0)
  iBinLevel4ValueID int NOT NULL default (0)
  iBinLevel5ValueID int NOT NULL default (0)
  iBinLevel6ValueID int NOT NULL default (0)
  iBinLevel7ValueID int NOT NULL default (0)
  iBinLevel8ValueID int NOT NULL default (0)
  iBinLevel9ValueID int NOT NULL default (0)
  bAllowSales bit NOT NULL default (1)
  bAllowPurchases bit NOT NULL default (1)
  bAlwaysAdd bit NOT NULL default (1)
  bActiveBin bit NOT NULL default (1)
  bAlwaysAddToExistingItems bit NOT NULL default (0)
  _btblBINLocationWhseLinks_iBranchID int NULL
  _btblBINLocationWhseLinks_dCreatedDate datetime NULL
  _btblBINLocationWhseLinks_dModifiedDate datetime NULL
  _btblBINLocationWhseLinks_iCreatedBranchID int NULL
  _btblBINLocationWhseLinks_iModifiedBranchID int NULL
  _btblBINLocationWhseLinks_iCreatedAgentID int NULL
  _btblBINLocationWhseLinks_iModifiedAgentID int NULL
  _btblBINLocationWhseLinks_iChangeSetID int NULL
  _btblBINLocationWhseLinks_Checksum binary(20) NULL

## _btblCBBankImportDefaults
PK: idCBBankImportDefaults
Columns (26):
  idCBBankImportDefaults int NOT NULL identity PK
  bFixedLength bit NOT NULL default (0)
  cDelimiter varchar(3) NULL
  bImpliedDecimals bit NOT NULL default (0)
  iTxDateStartPos int NULL
  iTxDateLength int NULL
  iTxDatePosition int NULL
  iReferenceStartPos int NULL
  iReferenceLength int NULL
  iReferencePosition int NULL
  iAmountStartPos int NULL
  iAmountLength int NULL
  iAmountPosition int NULL
  bWindowsDateFormat bit NOT NULL default (1)
  cCustomDateFormat varchar(8) NULL
  cDateSeparator varchar(1) NULL
  iHeaderRecords int NULL
  _btblCBBankImportDefaults_iBranchID int NULL
  _btblCBBankImportDefaults_dCreatedDate datetime NULL
  _btblCBBankImportDefaults_dModifiedDate datetime NULL
  _btblCBBankImportDefaults_iCreatedBranchID int NULL
  _btblCBBankImportDefaults_iModifiedBranchID int NULL
  _btblCBBankImportDefaults_iCreatedAgentID int NULL
  _btblCBBankImportDefaults_iModifiedAgentID int NULL
  _btblCBBankImportDefaults_iChangeSetID int NULL
  _btblCBBankImportDefaults_Checksum binary(20) NULL

## _btblCbBatchDefs
PK: idBatchDefs
Columns (38):
  idBatchDefs int NOT NULL identity PK
  bAutoNumbers bit NOT NULL
  iPadLength int NULL
  cPrefix varchar(25) NULL
  iInputTaxID int NULL
  iInputTaxAccID int NULL
  iOutputTaxID int NULL
  iOutputTaxAccID int NULL
  iTrCodeID int NULL
  iGLBankAccID int NULL
  iGLARAccID int NULL
  iGLAPAccID int NULL
  iARDiscTrCodeID int NULL
  iAPDiscTrCodeID int NULL
  bBatchRefAutoNumbers bit NOT NULL default (1)
  iBatchRefPadLength int NULL
  cBatchRefPrefix varchar(25) NULL
  iNextBatchRefNo int NULL
  bForceBatchRefNo bit NOT NULL default (1)
  iCurrencyID int NULL
  bForceProject bit NOT NULL default (0)
  bForceRep bit NOT NULL default (0)
  iEFTSLayoutID int NULL
  cEFTSPathOutFile varchar(100) NULL
  _btblCbBatchDefs_iBranchID int NULL
  _btblCbBatchDefs_dCreatedDate datetime NULL
  _btblCbBatchDefs_dModifiedDate datetime NULL
  _btblCbBatchDefs_iCreatedBranchID int NULL
  _btblCbBatchDefs_iModifiedBranchID int NULL
  _btblCbBatchDefs_iCreatedAgentID int NULL
  _btblCbBatchDefs_iModifiedAgentID int NULL
  _btblCbBatchDefs_iChangeSetID int NULL
  _btblCbBatchDefs_Checksum binary(20) NULL
  xBankAccAttribute xml NULL
  xARAccAttribute xml NULL
  xAPAccAttribute xml NULL
  xInputTaxAccAttribute xml NULL
  xOutputTaxAccAttribute xml NULL

## _btblCbBatches
PK: idBatches
Columns (67):
  idBatches int NOT NULL identity PK
  cBatchNo varchar(50) NULL
  cBatchDesc varchar(40) NULL
  bModuleGL bit NOT NULL
  bModuleAR bit NOT NULL
  bModuleAP bit NOT NULL
  iInputTaxID int NULL
  iInputTaxAccID int NULL
  iOutputTaxID int NULL
  iOutputTaxAccID int NULL
  bCalcTax bit NOT NULL
  iTrCodeID int NULL
  bClearBatch bit NOT NULL
  iDateLineOpt int NULL
  dDefDate smalldatetime NULL
  iRefLineOpt int NULL
  cDefRef varchar(20) NULL
  iDescLineOpt int NULL
  cDefDesc varchar(40) NULL
  iGLBankAccID int NULL
  iGLARAccID int NULL
  iGLAPAccID int NULL
  iDefModule int NULL
  bAllowDisc bit NOT NULL default (1)
  iARDiscTrCodeID int NULL
  iAPDiscTrCodeID int NULL
  cDiscDesc varchar(40) NULL
  bCheckedOut bit NULL default (0)
  bDupRefs bit NULL default (1)
  bPrintCheque bit NOT NULL default (0)
  bIncludeBankStatement bit NOT NULL default (0)
  iMaxRecur int NULL
  iBatchPosted int NULL
  cBatchRef varchar(50) NULL
  fValidationTotDeposits float NULL
  fValidationTotPayments float NULL
  iCurrencyID int NULL
  bPromptGlobalChanges bit NULL default (0)
  bTransDateOnCheque bit NOT NULL default (0)
  dDateBatchCreated datetime NULL
  iAgentBatchCreated int NOT NULL default (1)
  iAgentCheckedOut int NOT NULL default (0)
  bApplySettDisc bit NOT NULL default (0)
  bAllowZeroValues bit NOT NULL default (0)
  bARAllowLinkedAccounts bit NOT NULL default (0)
  bInterBranchBatch bit NOT NULL default (0)
  iBranchLoanAccountID int NULL
  bOnlyAllowForCurrency bit NOT NULL default (0)
  dProcessedDate datetime NULL
  bAutoAllocBBForward bit NULL
  bAutoAllocOpenItem bit NOT NULL default (0)
  bEFTSExport bit NOT NULL default (0)
  _btblCbBatches_iBranchID int NULL
  _btblCbBatches_dCreatedDate datetime NULL
  _btblCbBatches_dModifiedDate datetime NULL
  _btblCbBatches_iCreatedBranchID int NULL
  _btblCbBatches_iModifiedBranchID int NULL
  _btblCbBatches_iCreatedAgentID int NULL
  _btblCbBatches_iModifiedAgentID int NULL
  _btblCbBatches_iChangeSetID int NULL
  _btblCbBatches_Checksum binary(20) NULL
  bAutoAllocByReference bit NULL
  xBankAccAttribute xml NULL
  xARAccAttribute xml NULL
  xAPAccAttribute xml NULL
  xInputTaxAccAttribute xml NULL
  xOutputTaxAccAttribute xml NULL

## _btblCbBatchLines - Cashbook Batch Line (CashBookBatchLines)
Alias: Cashbook Batch Line | Freedom Name: CashBookBatchLines | Record Identifier: 
Notes: Cashbook Batch Line
PK: idBatchLines
Columns (65):
  idBatchLines int NOT NULL identity PK
  iBatchesID int NOT NULL
  iSplitType int NULL default (0)
  iSplitGroup int NULL
  dTxDate smalldatetime NOT NULL
  iModule int NOT NULL
  iAccountID int NOT NULL
  cDescription varchar(100) NULL
  cReference varchar(50) NULL
  fDebit float NULL
  fCredit float NULL
  bReconcile bit NOT NULL
  fTaxAmount float NULL
  iTaxTypeID int NULL
  iTaxAccountID int NULL
  iProjectID int NULL
  bPostDated bit NOT NULL
  fDiscPerc float NULL
  iDiscTrCodeID int NULL
  cDiscDesc varchar(35) NULL
  iDiscTaxTypeID int NULL
  iDiscTaxAccID int NULL
  fDiscTaxAmount float NULL
  cPayeeName varchar(100) NULL
  bPrintCheque bit NOT NULL default (0)
  bChequePrinted bit NOT NULL default (0)
  iRepID int NULL
  fExchangeRate float NULL
  fDebitForeign float NULL
  fCreditForeign float NULL
  fTaxAmountForeign float NULL
  fDiscTaxAmountForeign float NULL
  iCBBatchLinesReconID int NULL
  fFCAccountAmount float NOT NULL default (0)
  fFCAccountExchange float NOT NULL default (1)
  fFCAccountDiscAmount float NOT NULL default (0)
  fFCAccountDiscTax float NOT NULL default (0)
  iSettDiscGroupID int NOT NULL default (0)
  iSettDiscPostARAPID bigint NOT NULL default (0)
  cBankRef varchar(20) NULL
  bIsPosted bit NOT NULL default (0)
  iMBPropertyID int NULL default (0)
  iMBPortionID int NULL default (0)
  iMBServiceID int NULL default (0)
  iMBPropertyPortionServiceID int NULL default (0)
  bMBOverride bit NOT NULL default (0)
  iMBMeterID int NULL default (0)
  _btblCbBatchLines_iBranchID int NULL
  _btblCbBatchLines_dCreatedDate datetime NULL
  _btblCbBatchLines_dModifiedDate datetime NULL
  _btblCbBatchLines_iCreatedBranchID int NULL
  _btblCbBatchLines_iModifiedBranchID int NULL
  _btblCbBatchLines_iCreatedAgentID int NULL
  _btblCbBatchLines_iModifiedAgentID int NULL
  _btblCbBatchLines_iChangeSetID int NULL
  _btblCbBatchLines_Checksum binary(20) NULL
  fFCAccountTaxAmount float NOT NULL default (0)
  SagePayExtra1 varchar(max) NULL
  SagePayExtra2 varchar(max) NULL
  SagePayExtra3 varchar(max) NULL
  cTaxCompanyName varchar(150) NULL
  cTaxCompanyRegistration varchar(50) NULL
  cTaxRegistration varchar(50) NULL
  xAttribute xml NULL
  iMajorIndustryCodeID int NULL default (0)

## _btblCbImportHistory - CB Import History (CashBookImportHistory)
Alias: CB Import History | Freedom Name: CashBookImportHistory | Record Identifier: 
Notes: Cash Book Batch Bank manager import history
PK: ID
Columns (5):
  ID int NOT NULL identity PK
  DateTime datetime NULL
  FileName nvarchar(100) NULL
  FileDateTime datetime NULL
  BatchID int NULL

## _btblCbMatchRules - CB Match Rules (CashBookMatchRules)
Alias: CB Match Rules | Freedom Name: CashBookMatchRules | Record Identifier: 
Notes: Bank Manager CB Match rules
PK: ID
Columns (14):
  ID int NOT NULL identity PK
  Keywords varchar(100) NULL
  Module int NULL
  AccountID int NULL
  Account varchar(100) NULL
  Reference varchar(50) NULL
  TaxRate varchar(10) NULL
  Priority int NULL
  Project varchar(21) NULL
  Effect int NULL
  CashbookID int NULL
  LastUsed datetime NULL
  LedgerDescription varchar(100) NULL
  Source varchar(50) NULL

## _btblCbStatement - CB Statement (CashBookStatement)
Alias: CB Statement | Freedom Name: CashBookStatement | Record Identifier: 
Notes: Bank Manager. Saved Bank Statement Not Yet imported
PK: ID
Columns (22):
  BatchID int NOT NULL
  Date datetime NOT NULL
  Description varchar(100) NULL
  Module int NULL
  AccountID int NULL
  Account varchar(100) NULL
  Reference varchar(50) NULL
  LedgerDescription varchar(100) NULL
  TaxRate varchar(10) NULL
  ID int NOT NULL identity PK
  Debit float NULL
  Credit float NULL
  UniqueID varchar(60) NULL
  Posted bit NULL
  Project varchar(21) NULL
  Batch int NULL
  RowNumber int NULL
  AutoMapped int NULL
  SagePayExtra1 varchar(max) NULL
  SagePayExtra2 varchar(max) NULL
  SagePayExtra3 varchar(max) NULL
  cSBFBankAccountID nvarchar(200) NULL

## _btblCMEvent - Contact Management Event (ContactManagementEvent)
Alias: Contact Management Event | Freedom Name: ContactManagementEvent | Record Identifier: 
Notes: Contact Management Event.
PK: idEvent
Columns (20):
  idEvent int NOT NULL identity PK
  dStartTime datetime NULL
  dEndTime datetime NULL
  iAgentID int NOT NULL
  cDescription varchar(1024) NULL
  bAllDayEvent bit NOT NULL default (0)
  iRepeatCode int NULL
  dRepeatRangeEnd datetime NULL
  iCustomInterval int NULL
  iIncidentID int NULL
  cEventOutline varchar(255) NULL
  _btblCMEvent_iBranchID int NULL
  _btblCMEvent_dCreatedDate datetime NULL
  _btblCMEvent_dModifiedDate datetime NULL
  _btblCMEvent_iCreatedBranchID int NULL
  _btblCMEvent_iModifiedBranchID int NULL
  _btblCMEvent_iCreatedAgentID int NULL
  _btblCMEvent_iModifiedAgentID int NULL
  _btblCMEvent_iChangeSetID int NULL
  _btblCMEvent_Checksum binary(20) NULL

## _btblCMEventAttendees - Contact Management Event Attendee (ContactManagementEventAttendee)
Alias: Contact Management Event Attendee | Freedom Name: ContactManagementEventAttendee | Record Identifier: 
Notes: Contact Management Event Attendee.
PK: idCMEventAttendees
Columns (22):
  iEventID int NOT NULL
  iAttendeeID int NOT NULL
  cAttendeeType char(1) NOT NULL
  cAttendeeName varchar(255) NULL
  iResponse int NULL
  cComment varchar(255) NULL
  dSnoozeTime datetime NULL
  bAlarmSet bit NOT NULL default (0)
  iAlarmAdvance int NULL
  iAlarmAdvanceType int NULL
  cAlarmWavPath varchar(255) NULL
  cAttendeeEmail varchar(255) NULL
  idCMEventAttendees int NOT NULL identity PK
  _btblCMEventAttendees_iBranchID int NULL
  _btblCMEventAttendees_dCreatedDate datetime NULL
  _btblCMEventAttendees_dModifiedDate datetime NULL
  _btblCMEventAttendees_iCreatedBranchID int NULL
  _btblCMEventAttendees_iModifiedBranchID int NULL
  _btblCMEventAttendees_iCreatedAgentID int NULL
  _btblCMEventAttendees_iModifiedAgentID int NULL
  _btblCMEventAttendees_iChangeSetID int NULL
  _btblCMEventAttendees_Checksum binary(20) NULL

## _btblCMIncidentTypeGroup - Incident Type Group (ContactManagementIncidentTypeGroup)
Alias: Incident Type Group | Freedom Name: ContactManagementIncidentTypeGroup | Record Identifier: 
Notes: Incident Type Group.
PK: idIncidentTypeGroup
Columns (12):
  idIncidentTypeGroup int NOT NULL identity PK
  cName varchar(30) NOT NULL
  cDescription varchar(50) NULL
  _btblCMIncidentTypeGroup_iBranchID int NULL
  _btblCMIncidentTypeGroup_dCreatedDate datetime NULL
  _btblCMIncidentTypeGroup_dModifiedDate datetime NULL
  _btblCMIncidentTypeGroup_iCreatedBranchID int NULL
  _btblCMIncidentTypeGroup_iModifiedBranchID int NULL
  _btblCMIncidentTypeGroup_iCreatedAgentID int NULL
  _btblCMIncidentTypeGroup_iModifiedAgentID int NULL
  _btblCMIncidentTypeGroup_iChangeSetID int NULL
  _btblCMIncidentTypeGroup_Checksum binary(20) NULL

## _btblCMWorkflow - Workflow (ContactManagementWorkflow)
Alias: Workflow | Freedom Name: ContactManagementWorkflow | Record Identifier: 
Notes: Workflow.
PK: idWorkflow
Columns (13):
  idWorkflow int NOT NULL identity PK
  cName varchar(30) NOT NULL
  cDescription varchar(50) NULL
  bPOWorkflow bit NOT NULL default (0)
  _btblCMWorkflow_iBranchID int NULL
  _btblCMWorkflow_dCreatedDate datetime NULL
  _btblCMWorkflow_dModifiedDate datetime NULL
  _btblCMWorkflow_iCreatedBranchID int NULL
  _btblCMWorkflow_iModifiedBranchID int NULL
  _btblCMWorkflow_iCreatedAgentID int NULL
  _btblCMWorkflow_iModifiedAgentID int NULL
  _btblCMWorkflow_iChangeSetID int NULL
  _btblCMWorkflow_Checksum binary(20) NULL

## _btblCMWorkflowMembers - Workflow Member (ContactManagementWorkflowMembers)
Alias: Workflow Member | Freedom Name: ContactManagementWorkflowMembers | Record Identifier: 
Notes: Workflow Member.
PK: idWorkflowMembers
Columns (22):
  idWorkflowMembers int NOT NULL identity PK
  iWorkflowID int NOT NULL
  iAgentID int NOT NULL
  cAgentType char(1) NOT NULL
  iWorkflowStatusID int NOT NULL
  iSequenceNo int NOT NULL
  bAllowReject bit NOT NULL default (0)
  bAllowCloseAfterReject bit NOT NULL default (1)
  iEscGroupID int NULL
  bOverrideAutoAssign bit NOT NULL default (0)
  bPOApprove bit NOT NULL default (0)
  bPOCancelonReject bit NOT NULL default (0)
  iPOCancelReasonID int NULL
  _btblCMWorkflowMembers_iBranchID int NULL
  _btblCMWorkflowMembers_dCreatedDate datetime NULL
  _btblCMWorkflowMembers_dModifiedDate datetime NULL
  _btblCMWorkflowMembers_iCreatedBranchID int NULL
  _btblCMWorkflowMembers_iModifiedBranchID int NULL
  _btblCMWorkflowMembers_iCreatedAgentID int NULL
  _btblCMWorkflowMembers_iModifiedAgentID int NULL
  _btblCMWorkflowMembers_iChangeSetID int NULL
  _btblCMWorkflowMembers_Checksum binary(20) NULL

## _btblCMWorkflowStatus - Workflow Status (ContactManagementWorkflowStatus)
Alias: Workflow Status | Freedom Name: ContactManagementWorkflowStatus | Record Identifier: 
Notes: Workflow Status.
PK: idWorkflowStatus
Columns (12):
  idWorkflowStatus int NOT NULL identity PK
  cStatusCode varchar(20) NOT NULL
  cDescription varchar(50) NULL
  _btblCMWorkflowStatus_iBranchID int NULL
  _btblCMWorkflowStatus_dCreatedDate datetime NULL
  _btblCMWorkflowStatus_dModifiedDate datetime NULL
  _btblCMWorkflowStatus_iCreatedBranchID int NULL
  _btblCMWorkflowStatus_iModifiedBranchID int NULL
  _btblCMWorkflowStatus_iCreatedAgentID int NULL
  _btblCMWorkflowStatus_iModifiedAgentID int NULL
  _btblCMWorkflowStatus_iChangeSetID int NULL
  _btblCMWorkflowStatus_Checksum binary(20) NULL

## _btblFAAsset - Asset (FixedAssetsAsset)
Alias: Asset | Freedom Name: FixedAssetsAsset | Record Identifier: 
Notes: Asset.
PK: idAssetNo
Columns (80):
  idAssetNo int NOT NULL identity PK
  cAssetCode varchar(30) NOT NULL
  cTransferInd char(1) NULL
  iFromAssetNo int NULL
  dFromTransferDate smalldatetime NULL
  iFromTransferPeriodNo int NULL
  iToAssetNo int NULL
  dToTransferDate smalldatetime NULL
  iToTransferPeriodNo int NULL
  cAssetDesc varchar(80) NOT NULL
  iAssetTypeNo int NOT NULL
  iCostCenterNo int NULL
  iLocationNo int NULL
  iSupplierNo int NULL
  iCapexBudgetNo int NULL
  iCapexOrderNo int NULL
  fNoOfUnits float NOT NULL
  dPurchaseDate smalldatetime NOT NULL
  dDepreciationStartDate smalldatetime NOT NULL
  iDepreciationStartPeriodNo int NULL
  dWTStartDate smalldatetime NOT NULL
  iWTStartPeriodNo int NULL
  fPurchaseValue float NOT NULL
  fRevalueValue float NOT NULL
  fInsuredValue float NOT NULL
  fResidualValue float NOT NULL
  fScrapValue float NOT NULL
  fDeprPriorYearsTakeOn float NULL
  fDeprCurrYearTakeOn float NULL
  fWTPriorYearsTakeOn float NULL
  fWTCurrYearTakeOn float NULL
  fSellingPrice float NULL
  dSellingDate smalldatetime NULL
  dReplacementDate smalldatetime NULL
  fReplacementCost float NULL
  iBookOverrideMonths int NULL
  iTaxOverrideMonths int NULL
  dLastImportDate smalldatetime NULL
  iToAssetNo2 int NULL
  cCurrentInd char(1) NULL
  cBarCode varchar(80) NULL
  dOverrideDate smalldatetime NULL
  dOriginalWTStartDate smalldatetime NOT NULL
  dOriginalDeprStartDate smalldatetime NOT NULL
  iMasterAssetID int NULL
  cMasterAssetCode varchar(30) NULL
  fBookInitialAllowance float NULL
  fTaxInitialAllowance float NULL
  bInitialAllowancePosted bit NOT NULL default (0)
  fDivAssetBookPriorYearDepr float NULL
  fDivAssetBookCurrYearDepr float NULL
  fDivAssetTaxPriorYearDepr float NULL
  fDivAssetTaxCurrYearDepr float NULL
  iDivAssetBookBlockPeriods int NULL
  iDivAssetTaxBlockPeriods int NULL
  cSellOrScrap varchar(1) NULL
  cSellScrapReason varchar(256) NULL
  dDivDate datetime NULL
  fWTResidualValue float NULL default (0)
  bWTWriteOffAsset bit NULL default (0)
  fCGTBaseCost float NULL default (0)
  bCGTRolloverRelief bit NULL default (0)
  idFinMethod int NULL default (0)
  fFinRate float NULL default (0)
  fFinResidual float NULL default (0)
  cFinSecurities varchar(50) NULL
  fFinPeriod int NULL default (0)
  cFinAccountNumber varchar(50) NULL
  cFinWhere varchar(50) NULL
  fImpairmentCost float NULL default (0)
  cRevaluationMethod varchar(50) NULL
  _btblFAAsset_iBranchID int NULL
  _btblFAAsset_dCreatedDate datetime NULL
  _btblFAAsset_dModifiedDate datetime NULL
  _btblFAAsset_iCreatedBranchID int NULL
  _btblFAAsset_iModifiedBranchID int NULL
  _btblFAAsset_iCreatedAgentID int NULL
  _btblFAAsset_iModifiedAgentID int NULL
  _btblFAAsset_iChangeSetID int NULL
  _btblFAAsset_Checksum binary(20) NULL

## _btblFAAssetBlock - Asset Block
Alias: Asset Block | Freedom Name:  | Record Identifier: 
Notes: Asset Block. This table contains a list of the suspended assets.
PK: idAssetBlockNo
Columns (16):
  idAssetBlockNo int NOT NULL identity PK
  dFromDate smalldatetime NULL
  dToDate smalldatetime NULL
  iAssetNo int NOT NULL
  cAssetCode varchar(30) NULL
  dTaxFromDate smalldatetime NULL
  dTaxToDate smalldatetime NULL
  _btblFAAssetBlock_iBranchID int NULL
  _btblFAAssetBlock_dCreatedDate datetime NULL
  _btblFAAssetBlock_dModifiedDate datetime NULL
  _btblFAAssetBlock_iCreatedBranchID int NULL
  _btblFAAssetBlock_iModifiedBranchID int NULL
  _btblFAAssetBlock_iCreatedAgentID int NULL
  _btblFAAssetBlock_iModifiedAgentID int NULL
  _btblFAAssetBlock_iChangeSetID int NULL
  _btblFAAssetBlock_Checksum binary(20) NULL

## _btblFAAssetImages - Asset Image
Alias: Asset Image | Freedom Name:  | Record Identifier: 
Notes: Asset Image. This table contains a list of all the images linked to individual assets.
PK: idImageNo
Columns (15):
  idImageNo int NOT NULL identity PK
  iAssetNo int NOT NULL
  cImageDesc varchar(80) NOT NULL
  nImage image NOT NULL
  cAssetCode varchar(30) NULL
  cImageType varchar(10) NULL
  _btblFAAssetImages_iBranchID int NULL
  _btblFAAssetImages_dCreatedDate datetime NULL
  _btblFAAssetImages_dModifiedDate datetime NULL
  _btblFAAssetImages_iCreatedBranchID int NULL
  _btblFAAssetImages_iModifiedBranchID int NULL
  _btblFAAssetImages_iCreatedAgentID int NULL
  _btblFAAssetImages_iModifiedAgentID int NULL
  _btblFAAssetImages_iChangeSetID int NULL
  _btblFAAssetImages_Checksum binary(20) NULL

## _btblFAAssetSerialNo - Asset Serial Number
Alias: Asset Serial Number | Freedom Name:  | Record Identifier: 
Notes: Asset Serial Number.
PK: idSerialNo
Columns (15):
  idSerialNo int NOT NULL identity PK
  cAssetCode varchar(30) NOT NULL
  iUnitNo int NOT NULL
  cSerialNo varchar(80) NULL
  cBarcode varchar(80) NULL
  iLocationNo int NULL
  _btblFAAssetSerialNo_iBranchID int NULL
  _btblFAAssetSerialNo_dCreatedDate datetime NULL
  _btblFAAssetSerialNo_dModifiedDate datetime NULL
  _btblFAAssetSerialNo_iCreatedBranchID int NULL
  _btblFAAssetSerialNo_iModifiedBranchID int NULL
  _btblFAAssetSerialNo_iCreatedAgentID int NULL
  _btblFAAssetSerialNo_iModifiedAgentID int NULL
  _btblFAAssetSerialNo_iChangeSetID int NULL
  _btblFAAssetSerialNo_Checksum binary(20) NULL

## _btblFAAssetTracking - Asset Tracking
Alias: Asset Tracking | Freedom Name:  | Record Identifier: 
Notes: Asset Tracking.
PK: idAssetTracking
Columns (22):
  idAssetTracking int NOT NULL identity PK
  cAssetTrackingNo varchar(50) NULL
  cDescription varchar(60) NULL
  dPrepared datetime NULL
  cReference varchar(20) NULL
  cStartAssetCode varchar(255) NULL
  cEndAssetCode varchar(255) NULL
  iCount int NOT NULL default (0)
  iUncounted int NOT NULL default (0)
  iAgentID int NULL
  cLocations varchar(1024) NULL
  bDeleteAftComplete bit NOT NULL default (1)
  bCompleted bit NOT NULL default (0)
  _btblFAAssetTracking_iBranchID int NULL
  _btblFAAssetTracking_dCreatedDate datetime NULL
  _btblFAAssetTracking_dModifiedDate datetime NULL
  _btblFAAssetTracking_iCreatedBranchID int NULL
  _btblFAAssetTracking_iModifiedBranchID int NULL
  _btblFAAssetTracking_iCreatedAgentID int NULL
  _btblFAAssetTracking_iModifiedAgentID int NULL
  _btblFAAssetTracking_iChangeSetID int NULL
  _btblFAAssetTracking_Checksum binary(20) NULL

## _btblFAAssetTrackingLines - Asset Tracking Line
Alias: Asset Tracking Line | Freedom Name:  | Record Identifier: 
Notes: Asset Tracking Line.
PK: idAssetTrackingLines
Columns (25):
  idAssetTrackingLines int NOT NULL identity PK
  iAssetTrackingID int NOT NULL
  cAssetCode varchar(30) NULL
  cSerialNo varchar(50) NULL
  cBarCode varchar(50) NULL
  cLocationCode varchar(35) NULL
  iSystemUnitNoID int NULL
  cSystemAssetCode varchar(30) NULL
  cSystemSerialNo varchar(50) NULL
  cSystemBarCode varchar(50) NULL
  cSystemLocationCode varchar(35) NULL
  fCountQty float NULL
  bModified bit NOT NULL default (0)
  iTrackingStatus int NULL default (0)
  iTrackingDifference int NULL default (0)
  iTrackingAdjustment int NULL default (0)
  _btblFAAssetTrackingLines_iBranchID int NULL
  _btblFAAssetTrackingLines_dCreatedDate datetime NULL
  _btblFAAssetTrackingLines_dModifiedDate datetime NULL
  _btblFAAssetTrackingLines_iCreatedBranchID int NULL
  _btblFAAssetTrackingLines_iModifiedBranchID int NULL
  _btblFAAssetTrackingLines_iCreatedAgentID int NULL
  _btblFAAssetTrackingLines_iModifiedAgentID int NULL
  _btblFAAssetTrackingLines_iChangeSetID int NULL
  _btblFAAssetTrackingLines_Checksum binary(20) NULL

## _btblFAAssetType - Asset Type
Alias: Asset Type | Freedom Name:  | Record Identifier: 
Notes: Asset Type. This table contains list of all the various asset types created on the database. Standard Asset types are created at time of creating the database: Furniture, Motor vehicles, Computers, Machines, Software, Office Equipment
PK: idAssetTypeNo
Columns (21):
  idAssetTypeNo int NOT NULL identity PK
  cAssetTypeCode varchar(30) NOT NULL
  cAssetTypeDesc varchar(80) NOT NULL
  iDepreciationNo int NOT NULL
  iTaxDepreciationNo int NOT NULL
  fRevaluationIndex float NOT NULL
  fInsuranceIndex float NOT NULL
  iGLAccountNo int NULL
  fInsuranceCostFactor float NOT NULL
  fResidualFactor float NOT NULL
  iCreditGLAccountID int NULL
  iAssetGLAccountID int NULL
  _btblFAAssetType_iBranchID int NULL
  _btblFAAssetType_dCreatedDate datetime NULL
  _btblFAAssetType_dModifiedDate datetime NULL
  _btblFAAssetType_iCreatedBranchID int NULL
  _btblFAAssetType_iModifiedBranchID int NULL
  _btblFAAssetType_iCreatedAgentID int NULL
  _btblFAAssetType_iModifiedAgentID int NULL
  _btblFAAssetType_iChangeSetID int NULL
  _btblFAAssetType_Checksum binary(20) NULL

## _btblFAAssetUnitsOfUsage - Asset Units Of Usage
Alias: Asset Units Of Usage | Freedom Name:  | Record Identifier: 
Notes: Some assets depreciate based on their usage, rather than on a time basis. Enter the assets hourly usage for the period. The system then calculates its depreciation in proportion to its rated life.
PK: idAssetUnitNo
Columns (15):
  idAssetUnitNo int NOT NULL identity PK
  fNoOfUnits float NOT NULL
  iAssetNo int NOT NULL
  iGLPeriodNo int NOT NULL
  cAssetCode varchar(30) NULL
  cDeprTypeInd char(1) NOT NULL default 'B'
  _btblFAAssetUnitsOfUsage_iBranchID int NULL
  _btblFAAssetUnitsOfUsage_dCreatedDate datetime NULL
  _btblFAAssetUnitsOfUsage_dModifiedDate datetime NULL
  _btblFAAssetUnitsOfUsage_iCreatedBranchID int NULL
  _btblFAAssetUnitsOfUsage_iModifiedBranchID int NULL
  _btblFAAssetUnitsOfUsage_iCreatedAgentID int NULL
  _btblFAAssetUnitsOfUsage_iModifiedAgentID int NULL
  _btblFAAssetUnitsOfUsage_iChangeSetID int NULL
  _btblFAAssetUnitsOfUsage_Checksum binary(20) NULL

## _btblFACapexBudget - Capex Budget
Alias: Capex Budget | Freedom Name:  | Record Identifier: 
Notes: The system lets you track budgets for capital expenditure. You can create a budget per asset type and optionally per cost centre. You can also create timed bands of expenditure - you specify by date how much you expect to use. This table contains all the capex budgets created in the database.
PK: idCapexBudgetNo
Columns (18):
  idCapexBudgetNo int NOT NULL identity PK
  cCapexDesc varchar(80) NOT NULL
  cReplacementNewInd char(1) NOT NULL
  iAssetTypeNo int NOT NULL
  iCostCenterNo int NULL
  fBudgetAmount float NOT NULL
  fAmountSpent float NULL
  fAmountCommited float NULL
  dCapitalisationDate smalldatetime NOT NULL
  _btblFACapexBudget_iBranchID int NULL
  _btblFACapexBudget_dCreatedDate datetime NULL
  _btblFACapexBudget_dModifiedDate datetime NULL
  _btblFACapexBudget_iCreatedBranchID int NULL
  _btblFACapexBudget_iModifiedBranchID int NULL
  _btblFACapexBudget_iCreatedAgentID int NULL
  _btblFACapexBudget_iModifiedAgentID int NULL
  _btblFACapexBudget_iChangeSetID int NULL
  _btblFACapexBudget_Checksum binary(20) NULL

## _btblFACapexOrder - Capex Order
Alias: Capex Order | Freedom Name:  | Record Identifier: 
Notes: If you create a capex budget for an asset type, then, when you create a new asset that belongs to that asset type, you can link the asset to a capex order. If you do this, the system can then produce budget variance reports. This table contains a list of all capex orders on the database.
PK: idCapexOrderNo
Columns (15):
  idCapexOrderNo int NOT NULL identity PK
  cCapexOrderCode varchar(30) NOT NULL
  iCapexBudgetNo int NOT NULL
  dCapexOrderDate smalldatetime NOT NULL
  fCapexOrderAmount float NOT NULL
  cCapexOrderDesc varchar(80) NOT NULL
  _btblFACapexOrder_iBranchID int NULL
  _btblFACapexOrder_dCreatedDate datetime NULL
  _btblFACapexOrder_dModifiedDate datetime NULL
  _btblFACapexOrder_iCreatedBranchID int NULL
  _btblFACapexOrder_iModifiedBranchID int NULL
  _btblFACapexOrder_iCreatedAgentID int NULL
  _btblFACapexOrder_iModifiedAgentID int NULL
  _btblFACapexOrder_iChangeSetID int NULL
  _btblFACapexOrder_Checksum binary(20) NULL

## _btblFACapexPhasing
PK: idCapexPhasingNo
Columns (13):
  idCapexPhasingNo int NOT NULL identity PK
  dPhaseDate smalldatetime NOT NULL
  fPhaseAmount float NOT NULL
  iCapexBudgetNo int NOT NULL
  _btblFACapexPhasing_iBranchID int NULL
  _btblFACapexPhasing_dCreatedDate datetime NULL
  _btblFACapexPhasing_dModifiedDate datetime NULL
  _btblFACapexPhasing_iCreatedBranchID int NULL
  _btblFACapexPhasing_iModifiedBranchID int NULL
  _btblFACapexPhasing_iCreatedAgentID int NULL
  _btblFACapexPhasing_iModifiedAgentID int NULL
  _btblFACapexPhasing_iChangeSetID int NULL
  _btblFACapexPhasing_Checksum binary(20) NULL

## _btblFACompanySetup - FA Company Setup (FixedAssetsCompanySetup)
Alias: FA Company Setup | Freedom Name: FixedAssetsCompanySetup | Record Identifier: 
Notes: This table contains all the default settings created in the Defaults function.
PK: iFACompanyNo
Columns (41):
  iFACompanyNo int NOT NULL identity PK
  cDebitMethod char(1) NULL
  cCapexInd char(1) NOT NULL
  cDecimalInd char(1) NOT NULL
  dLastYearEndRun smalldatetime NULL
  dLastImportDate smalldatetime NULL
  cGLIntegrationInd char(1) NOT NULL
  cCalcStartDateInd char(1) NOT NULL
  iCalcDateDayNo int NULL
  iNoPeriodsInYear int NULL
  bCCRequired bit NULL
  bLocationRequired bit NULL
  cIntegrationMethod char(1) NULL
  iGLPeriodID int NULL
  iGLIntegrationOption int NULL
  iPastelJrTypeNo int NULL
  cPastelDataPath varchar(256) NULL
  cPastelAppPath varchar(256) NULL
  iJrBatchID int NULL
  cAutoYN varchar(1) NULL
  iAutoLength int NULL
  iAutoAlphaLength int NULL
  cUpperAccNo varchar(1) NULL
  iPastelTxJrTypeNo int NULL
  iTxJrBatchID int NULL
  bCreateTxJrEntries bit NOT NULL default (0)
  iPastelSDKVersionID int NULL
  bTrackingAuto bit NULL
  cTrackingNum varchar(15) NULL
  cTrackingPrefix varchar(20) NULL
  iTrackingPad int NULL
  bDepreciateByAccPeriod bit NOT NULL
  _btblFACompanySetup_iBranchID int NULL
  _btblFACompanySetup_dCreatedDate datetime NULL
  _btblFACompanySetup_dModifiedDate datetime NULL
  _btblFACompanySetup_iCreatedBranchID int NULL
  _btblFACompanySetup_iModifiedBranchID int NULL
  _btblFACompanySetup_iCreatedAgentID int NULL
  _btblFACompanySetup_iModifiedAgentID int NULL
  _btblFACompanySetup_iChangeSetID int NULL
  _btblFACompanySetup_Checksum binary(20) NULL

## _btblFADepreciationMethod
PK: idDepreciationNo
Columns (18):
  idDepreciationNo int NOT NULL identity PK
  cDepreciationDesc varchar(80) NOT NULL
  cBasisInd char(1) NOT NULL
  fPercentage float NOT NULL
  iNoYears int NULL
  iUnitsUsage int NULL
  fInitialPercentage float NULL
  fResidualValue float NULL
  cSystemInd char(1) NOT NULL
  _btblFADepreciationMethod_iBranchID int NULL
  _btblFADepreciationMethod_dCreatedDate datetime NULL
  _btblFADepreciationMethod_dModifiedDate datetime NULL
  _btblFADepreciationMethod_iCreatedBranchID int NULL
  _btblFADepreciationMethod_iModifiedBranchID int NULL
  _btblFADepreciationMethod_iCreatedAgentID int NULL
  _btblFADepreciationMethod_iModifiedAgentID int NULL
  _btblFADepreciationMethod_iChangeSetID int NULL
  _btblFADepreciationMethod_Checksum binary(20) NULL

## _btblFADepreciationYear - Depreciation Year
Alias: Depreciation Year | Freedom Name:  | Record Identifier: 
Notes: Depreciation Year Listing
PK: idDepreciationYearNo
Columns (13):
  idDepreciationYearNo int NOT NULL identity PK
  iYearNo int NOT NULL
  fPercentage float NOT NULL
  iDepreciationNo int NOT NULL
  _btblFADepreciationYear_iBranchID int NULL
  _btblFADepreciationYear_dCreatedDate datetime NULL
  _btblFADepreciationYear_dModifiedDate datetime NULL
  _btblFADepreciationYear_iCreatedBranchID int NULL
  _btblFADepreciationYear_iModifiedBranchID int NULL
  _btblFADepreciationYear_iCreatedAgentID int NULL
  _btblFADepreciationYear_iModifiedAgentID int NULL
  _btblFADepreciationYear_iChangeSetID int NULL
  _btblFADepreciationYear_Checksum binary(20) NULL

## _btblFAFinanceMethod
PK: idFinMethod
Columns (11):
  idFinMethod int NOT NULL identity PK
  cDescription varchar(50) NULL
  _btblFAFinanceMethod_iBranchID int NULL
  _btblFAFinanceMethod_dCreatedDate datetime NULL
  _btblFAFinanceMethod_dModifiedDate datetime NULL
  _btblFAFinanceMethod_iCreatedBranchID int NULL
  _btblFAFinanceMethod_iModifiedBranchID int NULL
  _btblFAFinanceMethod_iCreatedAgentID int NULL
  _btblFAFinanceMethod_iModifiedAgentID int NULL
  _btblFAFinanceMethod_iChangeSetID int NULL
  _btblFAFinanceMethod_Checksum binary(20) NULL

## _btblFAGLBatch - FA GL Batch
Alias: FA GL Batch | Freedom Name:  | Record Identifier: 
Notes: FA GL Batch. List of all GL batches created.
PK: idBatch
Columns (15):
  idBatch int NOT NULL identity PK
  cDescription varchar(50) NOT NULL
  dDateRun datetime NOT NULL
  bPosted bit NOT NULL
  dBatchDate smalldatetime NULL
  iBatchType int NOT NULL default (0)
  _btblFAGLBatch_iBranchID int NULL
  _btblFAGLBatch_dCreatedDate datetime NULL
  _btblFAGLBatch_dModifiedDate datetime NULL
  _btblFAGLBatch_iCreatedBranchID int NULL
  _btblFAGLBatch_iModifiedBranchID int NULL
  _btblFAGLBatch_iCreatedAgentID int NULL
  _btblFAGLBatch_iModifiedAgentID int NULL
  _btblFAGLBatch_iChangeSetID int NULL
  _btblFAGLBatch_Checksum binary(20) NULL

## _btblFAGLBatchAssetValues - FA GL Batch Asset Value
Alias: FA GL Batch Asset Value | Freedom Name:  | Record Identifier: 
Notes: Total GL asset values in a batch.
PK: idBatchAssetValues
Columns (16):
  idBatchAssetValues int NOT NULL identity PK
  iBatchID int NULL
  iAssetID int NULL
  dDate datetime NULL
  fAmount float NULL
  cAssetCode varchar(30) NULL
  bInitialAllowance bit NOT NULL default (0)
  _btblFAGLBatchAssetValues_iBranchID int NULL
  _btblFAGLBatchAssetValues_dCreatedDate datetime NULL
  _btblFAGLBatchAssetValues_dModifiedDate datetime NULL
  _btblFAGLBatchAssetValues_iCreatedBranchID int NULL
  _btblFAGLBatchAssetValues_iModifiedBranchID int NULL
  _btblFAGLBatchAssetValues_iCreatedAgentID int NULL
  _btblFAGLBatchAssetValues_iModifiedAgentID int NULL
  _btblFAGLBatchAssetValues_iChangeSetID int NULL
  _btblFAGLBatchAssetValues_Checksum binary(20) NULL

## _btblFAGLBatchGLEntries - FA GL Batch GL Entries
Alias: FA GL Batch GL Entries | Freedom Name:  | Record Identifier: 
Notes: This table contains the transactions to the relevant GL accounts for depreciation.
PK: idBatchGLEntries
Columns (19):
  idBatchGLEntries int NOT NULL identity PK
  iBatchID int NULL
  iGLAccountID int NULL
  dDate datetime NULL
  fDrAmount float NULL
  fCrAmount float NULL
  iAssetTypeID int NULL
  iCostCentreID int NULL
  iAssetCount int NULL
  cGLDescription varchar(100) NULL
  _btblFAGLBatchGLEntries_iBranchID int NULL
  _btblFAGLBatchGLEntries_dCreatedDate datetime NULL
  _btblFAGLBatchGLEntries_dModifiedDate datetime NULL
  _btblFAGLBatchGLEntries_iCreatedBranchID int NULL
  _btblFAGLBatchGLEntries_iModifiedBranchID int NULL
  _btblFAGLBatchGLEntries_iCreatedAgentID int NULL
  _btblFAGLBatchGLEntries_iModifiedAgentID int NULL
  _btblFAGLBatchGLEntries_iChangeSetID int NULL
  _btblFAGLBatchGLEntries_Checksum binary(20) NULL

## _btblFAGLPeriod - FA GL Period
Alias: FA GL Period | Freedom Name:  | Record Identifier: 
Notes: FA GL Period
PK: idGLPeriodNo
Columns (18):
  idGLPeriodNo int NOT NULL identity PK
  dStartDate smalldatetime NOT NULL
  dEndDate smalldatetime NOT NULL
  cDescription varchar(80) NOT NULL
  iYear int NOT NULL
  iPeriodNo int NOT NULL
  bBlockInd bit NULL
  bClosedInd bit NULL default (0)
  bReopened bit NULL default (0)
  _btblFAGLPeriod_iBranchID int NULL
  _btblFAGLPeriod_dCreatedDate datetime NULL
  _btblFAGLPeriod_dModifiedDate datetime NULL
  _btblFAGLPeriod_iCreatedBranchID int NULL
  _btblFAGLPeriod_iModifiedBranchID int NULL
  _btblFAGLPeriod_iCreatedAgentID int NULL
  _btblFAGLPeriod_iModifiedAgentID int NULL
  _btblFAGLPeriod_iChangeSetID int NULL
  _btblFAGLPeriod_Checksum binary(20) NULL

## _btblFAGLTotalAssetValues - FA GL Total Asset Value
Alias: FA GL Total Asset Value | Freedom Name:  | Record Identifier: 
Notes: Total values of assets in the database
PK: idTotalAssetValues
Columns (15):
  idTotalAssetValues int NOT NULL identity PK
  iAssetID int NULL
  dDate datetime NULL
  iPeriodID int NULL
  fAmount float NULL
  cAssetCode varchar(30) NULL
  _btblFAGLTotalAssetValues_iBranchID int NULL
  _btblFAGLTotalAssetValues_dCreatedDate datetime NULL
  _btblFAGLTotalAssetValues_dModifiedDate datetime NULL
  _btblFAGLTotalAssetValues_iCreatedBranchID int NULL
  _btblFAGLTotalAssetValues_iModifiedBranchID int NULL
  _btblFAGLTotalAssetValues_iCreatedAgentID int NULL
  _btblFAGLTotalAssetValues_iModifiedAgentID int NULL
  _btblFAGLTotalAssetValues_iChangeSetID int NULL
  _btblFAGLTotalAssetValues_Checksum binary(20) NULL

## _btblFAGLTotalGLEntries
PK: idTotalGLEntries
Columns (15):
  idTotalGLEntries int NOT NULL identity PK
  iGLAccountID int NULL
  dDate datetime NULL
  iPeriodID int NULL
  fDrAmount float NULL
  fCrAmount float NULL
  _btblFAGLTotalGLEntries_iBranchID int NULL
  _btblFAGLTotalGLEntries_dCreatedDate datetime NULL
  _btblFAGLTotalGLEntries_dModifiedDate datetime NULL
  _btblFAGLTotalGLEntries_iCreatedBranchID int NULL
  _btblFAGLTotalGLEntries_iModifiedBranchID int NULL
  _btblFAGLTotalGLEntries_iCreatedAgentID int NULL
  _btblFAGLTotalGLEntries_iModifiedAgentID int NULL
  _btblFAGLTotalGLEntries_iChangeSetID int NULL
  _btblFAGLTotalGLEntries_Checksum binary(20) NULL

## _btblFALocation - FA Location
Alias: FA Location | Freedom Name:  | Record Identifier: 
Notes: This table contains a list of all the FA locations created in the database.
PK: idLocationNo
Columns (12):
  idLocationNo int NOT NULL identity PK
  cLocationCode varchar(30) NOT NULL
  cLocationDesc varchar(80) NOT NULL
  _btblFALocation_iBranchID int NULL
  _btblFALocation_dCreatedDate datetime NULL
  _btblFALocation_dModifiedDate datetime NULL
  _btblFALocation_iCreatedBranchID int NULL
  _btblFALocation_iModifiedBranchID int NULL
  _btblFALocation_iCreatedAgentID int NULL
  _btblFALocation_iModifiedAgentID int NULL
  _btblFALocation_iChangeSetID int NULL
  _btblFALocation_Checksum binary(20) NULL

## _btblFAMovementTransaction - FA Movement Transaction
Alias: FA Movement Transaction | Freedom Name:  | Record Identifier: 
PK: idMovementTransactionNo
Columns (24):
  idMovementTransactionNo int NOT NULL identity PK
  iAssetID int NOT NULL
  iTransactionTypeID int NOT NULL
  fNoOfUnits float NOT NULL
  fAmount float NOT NULL
  dMovementDate smalldatetime NOT NULL
  cReference varchar(200) NULL
  iPeopleID int NULL
  cAssetCode varchar(30) NULL
  iAssetTypeID int NULL
  iCostCentreID int NULL
  iLocationID int NULL
  DTStamp datetime NULL
  UserName varchar(50) NULL
  cDeprTypeInd varchar(1) NULL
  _btblFAMovementTransaction_iBranchID int NULL
  _btblFAMovementTransaction_dCreatedDate datetime NULL
  _btblFAMovementTransaction_dModifiedDate datetime NULL
  _btblFAMovementTransaction_iCreatedBranchID int NULL
  _btblFAMovementTransaction_iModifiedBranchID int NULL
  _btblFAMovementTransaction_iCreatedAgentID int NULL
  _btblFAMovementTransaction_iModifiedAgentID int NULL
  _btblFAMovementTransaction_iChangeSetID int NULL
  _btblFAMovementTransaction_Checksum binary(20) NULL

## _btblFAPeriodClose - FA Period Close
Alias: FA Period Close | Freedom Name:  | Record Identifier: 
Notes: FA Period Close
PK: none
Columns (20):
  idPeriodClose int NOT NULL identity
  cAssetCode nchar(30) NULL
  dPeriodCloseDate datetime NULL
  iGLPeriodNoID int NOT NULL
  fBookCurrentYearDepreciation float NULL
  fBookPriorYearDepreciation float NULL
  fWTCurrentYearDepreciation float NULL
  fWTPriorYearDepreciation float NULL
  fTotalBookBlockPeriod float NULL
  fTotalWTBlockPeriod float NULL
  bReopened bit NULL default (0)
  _btblFAPeriodClose_iBranchID int NULL
  _btblFAPeriodClose_dCreatedDate datetime NULL
  _btblFAPeriodClose_dModifiedDate datetime NULL
  _btblFAPeriodClose_iCreatedBranchID int NULL
  _btblFAPeriodClose_iModifiedBranchID int NULL
  _btblFAPeriodClose_iCreatedAgentID int NULL
  _btblFAPeriodClose_iModifiedAgentID int NULL
  _btblFAPeriodClose_iChangeSetID int NULL
  _btblFAPeriodClose_Checksum binary(20) NULL

## _btblFATxDefaultGLAccounts - FA Tax Default GL Account
Alias: FA Tax Default GL Account | Freedom Name:  | Record Identifier: 
Notes: FA Tax Default GL Account
PK: idTXDefaultGLAccount
Columns (16):
  idTXDefaultGLAccount int NOT NULL identity PK
  cTransactionType varchar(1) NULL
  iDebitGLAccountID int NULL
  iProfitGLAccountID int NULL
  iLossGLAccountID int NULL
  iRevaluationGLAccountID int NULL
  iCreditGLAccountID int NULL
  _btblFATxDefaultGLAccounts_iBranchID int NULL
  _btblFATxDefaultGLAccounts_dCreatedDate datetime NULL
  _btblFATxDefaultGLAccounts_dModifiedDate datetime NULL
  _btblFATxDefaultGLAccounts_iCreatedBranchID int NULL
  _btblFATxDefaultGLAccounts_iModifiedBranchID int NULL
  _btblFATxDefaultGLAccounts_iCreatedAgentID int NULL
  _btblFATxDefaultGLAccounts_iModifiedAgentID int NULL
  _btblFATxDefaultGLAccounts_iChangeSetID int NULL
  _btblFATxDefaultGLAccounts_Checksum binary(20) NULL

## _btblInvCount - Inventory Count (InventoryCount)
Alias: Inventory Count | Freedom Name: InventoryCount | Record Identifier: 
Notes: Inventory Count.
PK: idInvCount
Columns (63):
  idInvCount int NOT NULL identity PK
  cInvCountNo varchar(50) NULL
  cDescription varchar(60) NULL
  dPrepared datetime NULL
  cReference varchar(20) NULL
  cStartCode varchar(255) NULL
  cEndCode varchar(255) NULL
  cGroups varchar(1024) NULL
  cPacks varchar(1024) NULL
  bIgnoreZero bit NOT NULL default (0)
  bIgnoreInactive bit NOT NULL default (1)
  iCount int NOT NULL default (0)
  iUncounted int NOT NULL default (0)
  iGroupBy int NOT NULL default (0)
  iSortBy int NOT NULL default (0)
  bIncludeSystemQty bit NOT NULL default (1)
  cWarehouses varchar(1024) NULL
  iAgentID int NULL
  cItemCategories varchar(1024) NULL
  iStartItemCategoryID int NULL
  iEndItemCategoryID int NULL
  cInventoryTypes varchar(1024) NULL
  cLotStatus varchar(1024) NULL
  bIncludeJCWIP bit NOT NULL default (1)
  bIncludeMFWIP bit NOT NULL default (1)
  bIncludeOrdResQty bit NOT NULL default (0)
  bDeleteAftComplete bit NOT NULL default (1)
  bIncludeDelivery bit NOT NULL default (0)
  bSpotCount bit NOT NULL default (0)
  bScheduledCount bit NOT NULL default (0)
  dScheduledDate datetime NULL
  iStatus int NULL
  bForceCapture bit NOT NULL default (0)
  cGroupsChkLstInd char(1) NULL
  cPacksChkLstInd char(1) NULL
  cWarehousesChkLstInd char(1) NULL
  cItemCategoriesChkLstInd char(1) NULL
  cInventoryTypesChkLstInd char(1) NULL
  cLotStatusChkLstInd char(1) NULL
  bTakeSnapshot bit NULL
  cFromItemCategoryName varchar(30) NULL
  cToItemCategoryName varchar(30) NULL
  _btblInvCount_iBranchID int NULL
  _btblInvCount_dCreatedDate datetime NULL
  _btblInvCount_dModifiedDate datetime NULL
  _btblInvCount_iCreatedBranchID int NULL
  _btblInvCount_iModifiedBranchID int NULL
  _btblInvCount_iCreatedAgentID int NULL
  _btblInvCount_iModifiedAgentID int NULL
  _btblInvCount_iChangeSetID int NULL
  _btblInvCount_Checksum binary(20) NULL
  bSummaryCount bit NOT NULL default (0)
  iSummaryGroupBy int NULL
  cAttributeGroups nvarchar(max) NULL
  cAttributeTypes nvarchar(max) NULL
  AttributeTypeGroupBy varchar(50) NULL
  bVariance bit NOT NULL default (1)
  xAttributeFilterValues xml NULL
  bIgnoreInactiveBins bit NOT NULL default (0)
  bIgnoreZeroBins bit NOT NULL default (0)
  cTransBinFromCode varchar(125) NULL
  cTransBinToCode varchar(125) NULL
  bExcludeInvoicedSN bit NOT NULL default (0)

## _btblInvCountLines - Inventory Count Lines (InventoryCountLines)
Alias: Inventory Count Lines | Freedom Name: InventoryCountLines | Record Identifier: 
Notes: Inventory Count Lines. Detail of each inventory item counted.
PK: idInvCountLines
Columns (32):
  idInvCountLines bigint NOT NULL identity PK
  iInvCountID int NOT NULL
  cItemGroup varchar(20) NULL
  cPack varchar(5) NULL
  cBarcode varchar(255) NULL
  fSystemQty float NULL
  fCountQty float NULL
  bModified bit NOT NULL default (0)
  bWhseItem bit NOT NULL default (0)
  bSerialItem bit NOT NULL default (0)
  tSerialList text NULL
  bSNAllowDups bit NOT NULL default (0)
  iItemCategoryID int NULL
  iLotTrackingID int NULL
  bLotItem bit NOT NULL default (0)
  iStockID int NOT NULL default (0)
  iWarehouseID int NOT NULL default (0)
  bUOMCounted bit NOT NULL default (0)
  bDimensionItem bit NOT NULL default (0)
  _btblInvCountLines_iBranchID int NULL
  _btblInvCountLines_dCreatedDate datetime NULL
  _btblInvCountLines_dModifiedDate datetime NULL
  _btblInvCountLines_iCreatedBranchID int NULL
  _btblInvCountLines_iModifiedBranchID int NULL
  _btblInvCountLines_iCreatedAgentID int NULL
  _btblInvCountLines_iModifiedAgentID int NULL
  _btblInvCountLines_iChangeSetID int NULL
  _btblInvCountLines_Checksum binary(20) NULL
  AttributeValue varchar(50) NULL
  xAttributeSystem xml NULL
  xAttributeCount xml NULL
  iTransBinLocationID int NOT NULL default (0)

## _btblInvCountLinesUOM - Inventory Count Lines UOM (InventoryCountLinesUnitOfMeasure)
Alias: Inventory Count Lines UOM | Freedom Name: InventoryCountLinesUnitOfMeasure | Record Identifier: 
Notes: Inventory Count Lines UOM
PK: IDInvCountLinesUOM
Columns (18):
  IDInvCountLinesUOM bigint NOT NULL identity PK
  iInvCountID int NOT NULL
  iInvCountLinesID bigint NOT NULL
  iUnitsID int NOT NULL default (0)
  fUnitCountQty float NULL
  iCountedPieces int NOT NULL default (0)
  fLength float NOT NULL default (0)
  fHeight float NOT NULL default (0)
  fWidth float NOT NULL default (0)
  _btblInvCountLinesUOM_iBranchID int NULL
  _btblInvCountLinesUOM_dCreatedDate datetime NULL
  _btblInvCountLinesUOM_dModifiedDate datetime NULL
  _btblInvCountLinesUOM_iCreatedBranchID int NULL
  _btblInvCountLinesUOM_iModifiedBranchID int NULL
  _btblInvCountLinesUOM_iCreatedAgentID int NULL
  _btblInvCountLinesUOM_iModifiedAgentID int NULL
  _btblInvCountLinesUOM_iChangeSetID int NULL
  _btblInvCountLinesUOM_Checksum binary(20) NULL

## _btblInvCountSegFilters
PK: idInvCountSegFilter
Columns (16):
  idInvCountSegFilter bigint NOT NULL identity PK
  iInvCountID int NOT NULL
  iSegmentLevel int NOT NULL
  cSegGroups varchar(1024) NULL
  cSegGroupsChkListInd char(1) NULL
  cSegValues varchar(1024) NULL
  cSegValuesChkListInd char(1) NULL
  _btblInvCountSegFilters_iBranchID int NULL
  _btblInvCountSegFilters_dCreatedDate datetime NULL
  _btblInvCountSegFilters_dModifiedDate datetime NULL
  _btblInvCountSegFilters_iCreatedBranchID int NULL
  _btblInvCountSegFilters_iModifiedBranchID int NULL
  _btblInvCountSegFilters_iCreatedAgentID int NULL
  _btblInvCountSegFilters_iModifiedAgentID int NULL
  _btblInvCountSegFilters_iChangeSetID int NULL
  _btblInvCountSegFilters_Checksum binary(20) NULL

## _btblInvoiceFiscalTaxes
PK: idInvoiceTaxes
Columns (62):
  idInvoiceTaxes bigint NOT NULL identity PK
  iInvoiceID bigint NOT NULL
  iTaxTypeA int NULL
  FTaxTypeAAm float NULL
  fTaxTypeATax float NULL
  iTaxTypeB int NULL
  fTaxTypeBAm float NULL
  fTaxTypeBTax float NULL
  iTaxTypeC int NULL
  fTaxTypeCAm float NULL
  fTaxTypeCTax float NULL
  iTaxTypeD int NULL
  fTaxTypeDAm float NULL
  fTaxTypeDTax float NULL
  iTaxTypeE int NULL
  fTaxTypeEAm float NULL
  fTaxTypeETax float NULL
  iTaxTypeF int NULL
  fTaxTypeFAm float NULL
  fTaxTypeFTax float NULL
  cSignatureNormal nvarchar(1000) NULL
  DeviceDateNormalDoc smalldatetime NULL
  cSignatureCopy nvarchar(1000) NULL
  DeviceDateCopyDoc smalldatetime NULL
  bDocType bit NOT NULL default (0)
  cMRCNormalDoc nvarchar(50) NULL
  cMRCCopyDoc nvarchar(50) NULL
  _btblInvoiceFiscalTaxes_iBranchID int NULL
  _btblInvoiceFiscalTaxes_dCreatedDate datetime NULL
  _btblInvoiceFiscalTaxes_dModifiedDate datetime NULL
  _btblInvoiceFiscalTaxes_iCreatedBranchID int NULL
  _btblInvoiceFiscalTaxes_iModifiedBranchID int NULL
  _btblInvoiceFiscalTaxes_iCreatedAgentID int NULL
  _btblInvoiceFiscalTaxes_iModifiedAgentID int NULL
  _btblInvoiceFiscalTaxes_iChangeSetID int NULL
  _btblInvoiceFiscalTaxes_Checksum binary(20) NULL
  iTaxTypeG int NULL
  FTaxTypeGAm float NULL
  fTaxTypeGTax float NULL
  iTaxTypeH int NULL
  FTaxTypeHAm float NULL
  fTaxTypeHTax float NULL
  dTrTime datetime NULL
  cInvoiceCode nvarchar(20) NULL
  cInvoiceNumber nvarchar(20) NULL
  cTerminalID nvarchar(20) NULL
  cFiscalCode varchar(50) NULL
  fFiscalTotal float NULL default (0)
  cQRCode nvarchar(max) NULL
  cVerificationUrl nvarchar(max) NULL
  bCreditedInv bit NULL default (0)
  cTPIN varchar(20) NULL
  cTaxpayerName varchar(200) NULL
  cTaxpayerAddress varchar(500) NULL
  cTelecomOperator varchar(200) NULL
  cLPONumber varchar(20) NULL
  iLinkedDocID int NULL default (0)
  cFiscalCodeCopy varchar(50) NULL
  cQRCodeCopy nvarchar(max) NULL
  cFiscalDocument nvarchar(30) NULL
  cFiscalDocumentCopy nvarchar(30) NULL
  cMemo nvarchar(50) NULL

## _btblInvoiceGrvSplit - Invoice GRV Split (InvoiceGoodsReceivedVoucherSplit)
Alias: Invoice GRV Split | Freedom Name: InvoiceGoodsReceivedVoucherSplit | Record Identifier: 
Notes: Invoice GRV Split
PK: idInvoiceGrvSplit
Columns (21):
  idInvoiceGrvSplit int NOT NULL identity PK
  iGrvSplitInvoiceID bigint NOT NULL
  iGrvSplitVendorID int NOT NULL
  cGRVSplitReference varchar(20) NULL
  cGrvSplitDescription varchar(30) NULL
  fGrvSplitAmount float NULL
  iGrvSplitTaxTypeID int NULL
  fGrvSplitTaxAmnt float NULL
  iCurrencyID int NULL
  fForexRate float NULL
  fForexAmount float NULL
  _btblInvoiceGrvSplit_iBranchID int NULL
  _btblInvoiceGrvSplit_dCreatedDate datetime NULL
  _btblInvoiceGrvSplit_dModifiedDate datetime NULL
  _btblInvoiceGrvSplit_iCreatedBranchID int NULL
  _btblInvoiceGrvSplit_iModifiedBranchID int NULL
  _btblInvoiceGrvSplit_iCreatedAgentID int NULL
  _btblInvoiceGrvSplit_iModifiedAgentID int NULL
  _btblInvoiceGrvSplit_iChangeSetID int NULL
  _btblInvoiceGrvSplit_Checksum binary(20) NULL
  fForexTaxAmount float NOT NULL default (0)

## _btblInvoiceLineDetails
PK: idInvoiceLineDetails
Columns (26):
  idInvoiceLineDetails bigint NOT NULL identity PK
  iLDInvoiceID bigint NOT NULL
  iLDInvoiceLineID bigint NOT NULL
  bMatrixEntry bit NOT NULL default (0)
  iLDInvoiceLineMatrixID int NOT NULL default (0)
  iLotID int NOT NULL default (0)
  cLotNumber varchar(50) NOT NULL default ''
  dLotExpiryDate datetime NULL
  iStockBinLocationID int NOT NULL default (0)
  iUnitsOfMeasureID int NOT NULL default (0)
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL
  fldQty float NOT NULL default (0)
  fldQtyToProcess float NOT NULL default (0)
  fldQtyReserved float NOT NULL default (0)
  fldQtyLastProcess float NOT NULL default (0)
  fldQtyProcessed float NOT NULL default (0)
  _btblInvoiceLineDetails_iBranchID int NULL
  _btblInvoiceLineDetails_dCreatedDate datetime NULL
  _btblInvoiceLineDetails_dModifiedDate datetime NULL
  _btblInvoiceLineDetails_iCreatedBranchID int NULL
  _btblInvoiceLineDetails_iModifiedBranchID int NULL
  _btblInvoiceLineDetails_iCreatedAgentID int NULL
  _btblInvoiceLineDetails_iModifiedAgentID int NULL
  _btblInvoiceLineDetails_iChangeSetID int NULL
  _btblInvoiceLineDetails_Checksum binary(20) NULL

## _btblInvoiceLines - Invoice Lines (DocumentLines)
Alias: Invoice Lines | Freedom Name: DocumentLines | Record Identifier: 
Notes: Invoice Lines.
PK: idInvoiceLines
Columns (170):
  idInvoiceLines bigint NOT NULL identity PK
  iInvoiceID bigint NOT NULL
  iOrigLineID bigint NULL
  iGrvLineID bigint NULL
  iLineDocketMode int NULL
  cDescription varchar(100) NULL
  iUnitsOfMeasureStockingID int NULL
  iUnitsOfMeasureCategoryID int NULL default (0)
  iUnitsOfMeasureID int NULL default (0)
  fQuantity float NULL
  fQtyChange float NULL
  fQtyToProcess float NULL
  fQtyLastProcess float NULL
  fQtyProcessed float NULL
  fQtyReserved float NULL
  fQtyReservedChange float NULL
  cLineNotes varchar(max) NULL
  fUnitPriceExcl float NULL
  fUnitPriceIncl float NULL
  iUnitPriceOverrideReasonID int NULL
  fUnitCost float NULL
  fLineDiscount float NULL
  iLineDiscountReasonID int NULL
  iReturnReasonID int NULL
  fTaxRate float NULL
  bIsSerialItem bit NOT NULL default (0)
  bIsWhseItem bit NOT NULL default (0)
  fAddCost float NULL
  cTradeinItem varchar(20) NULL
  iStockCodeID int NULL
  iJobID int NULL default (0)
  iWarehouseID int NULL
  iTaxTypeID int NULL
  iPriceListNameID int NULL
  fQuantityLineTotIncl float NULL
  fQuantityLineTotExcl float NULL
  fQuantityLineTotInclNoDisc float NULL
  fQuantityLineTotExclNoDisc float NULL
  fQuantityLineTaxAmount float NULL
  fQuantityLineTaxAmountNoDisc float NULL
  fQtyChangeLineTotIncl float NULL
  fQtyChangeLineTotExcl float NULL
  fQtyChangeLineTotInclNoDisc float NULL
  fQtyChangeLineTotExclNoDisc float NULL
  fQtyChangeLineTaxAmount float NULL
  fQtyChangeLineTaxAmountNoDisc float NULL
  fQtyToProcessLineTotIncl float NULL
  fQtyToProcessLineTotExcl float NULL
  fQtyToProcessLineTotInclNoDisc float NULL
  fQtyToProcessLineTotExclNoDisc float NULL
  fQtyToProcessLineTaxAmount float NULL
  fQtyToProcessLineTaxAmountNoDisc float NULL
  fQtyLastProcessLineTotIncl float NULL
  fQtyLastProcessLineTotExcl float NULL
  fQtyLastProcessLineTotInclNoDisc float NULL
  fQtyLastProcessLineTotExclNoDisc float NULL
  fQtyLastProcessLineTaxAmount float NULL
  fQtyLastProcessLineTaxAmountNoDisc float NULL
  fQtyProcessedLineTotIncl float NULL
  fQtyProcessedLineTotExcl float NULL
  fQtyProcessedLineTotInclNoDisc float NULL
  fQtyProcessedLineTotExclNoDisc float NULL
  fQtyProcessedLineTaxAmount float NULL
  fQtyProcessedLineTaxAmountNoDisc float NULL
  fUnitPriceExclForeign float NULL
  fUnitPriceInclForeign float NULL
  fUnitCostForeign float NULL
  fAddCostForeign float NULL
  fQuantityLineTotInclForeign float NULL
  fQuantityLineTotExclForeign float NULL
  fQuantityLineTotInclNoDiscForeign float NULL
  fQuantityLineTotExclNoDiscForeign float NULL
  fQuantityLineTaxAmountForeign float NULL
  fQuantityLineTaxAmountNoDiscForeign float NULL
  fQtyChangeLineTotInclForeign float NULL
  fQtyChangeLineTotExclForeign float NULL
  fQtyChangeLineTotInclNoDiscForeign float NULL
  fQtyChangeLineTotExclNoDiscForeign float NULL
  fQtyChangeLineTaxAmountForeign float NULL
  fQtyChangeLineTaxAmountNoDiscForeign float NULL
  fQtyToProcessLineTotInclForeign float NULL
  fQtyToProcessLineTotExclForeign float NULL
  fQtyToProcessLineTotInclNoDiscForeign float NULL
  fQtyToProcessLineTotExclNoDiscForeign float NULL
  fQtyToProcessLineTaxAmountForeign float NULL
  fQtyToProcessLineTaxAmountNoDiscForeign float NULL
  fQtyLastProcessLineTotInclForeign float NULL
  fQtyLastProcessLineTotExclForeign float NULL
  fQtyLastProcessLineTotInclNoDiscForeign float NULL
  fQtyLastProcessLineTotExclNoDiscForeign float NULL
  fQtyLastProcessLineTaxAmountForeign float NULL
  fQtyLastProcessLineTaxAmountNoDiscForeign float NULL
  fQtyProcessedLineTotInclForeign float NULL
  fQtyProcessedLineTotExclForeign float NULL
  fQtyProcessedLineTotInclNoDiscForeign float NULL
  fQtyProcessedLineTotExclNoDiscForeign float NULL
  fQtyProcessedLineTaxAmountForeign float NULL
  fQtyProcessedLineTaxAmountNoDiscForeign float NULL
  iLineRepID int NULL
  iLineProjectID int NULL
  iLedgerAccountID int NULL
  iModule int NOT NULL default (0)
  bChargeCom bit NOT NULL default (1)
  bIsLotItem bit NOT NULL default (0)
  iMFPID int NULL
  iLineID int NOT NULL default (0)
  iLinkedLineID bigint NOT NULL default (0)
  fQtyLinkedUsed float NULL
  fUnitPriceInclOrig float NULL
  fUnitPriceExclOrig float NULL
  fUnitPriceInclForeignOrig float NULL
  fUnitPriceExclForeignOrig float NULL
  iDeliveryMethodID int NULL
  fQtyDeliver float NULL
  dDeliveryDate datetime NULL
  iDeliveryStatus int NULL
  fQtyForDelivery float NULL
  bPromotionApplied bit NOT NULL default (0)
  fPromotionPriceExcl float NULL
  fPromotionPriceIncl float NULL
  cPromotionCode varchar(20) NULL
  iSOLinkedPOLineID bigint NOT NULL default (0)
  fLength float NULL default (0)
  fWidth float NULL default (0)
  fHeight float NULL default (0)
  iPieces int NULL default (0)
  iPiecesToProcess int NULL default (0)
  iPiecesLastProcess int NULL default (0)
  iPiecesProcessed int NULL default (0)
  iPiecesReserved int NULL default (0)
  iPiecesDeliver int NULL default (0)
  iPiecesForDelivery int NULL default (0)
  fQuantityUR float NULL
  fQtyChangeUR float NULL
  fQtyToProcessUR float NULL
  fQtyLastProcessUR float NULL
  fQtyProcessedUR float NULL
  fQtyReservedUR float NULL
  fQtyReservedChangeUR float NULL
  fQtyDeliverUR float NULL
  fQtyForDeliveryUR float NULL
  fQtyLinkedUsedUR float NULL
  iPiecesLinkedUsed int NULL
  iSalesWhseID int NULL
  _btblInvoiceLines_iBranchID int NULL
  _btblInvoiceLines_dCreatedDate datetime NULL
  _btblInvoiceLines_dModifiedDate datetime NULL
  _btblInvoiceLines_iCreatedBranchID int NULL
  _btblInvoiceLines_iModifiedBranchID int NULL
  _btblInvoiceLines_iCreatedAgentID int NULL
  _btblInvoiceLines_iModifiedAgentID int NULL
  _btblInvoiceLines_iChangeSetID int NULL
  _btblInvoiceLines_Checksum binary(20) NULL
  ucIDCrnTxSTRollNumber varchar(30) NULL
  ucIDInvTxSTRollNumber varchar(30) NULL
  ucIDRtsTxSTRollNumber varchar(30) NULL
  ucIDSOrdTxSTRollNumber varchar(30) NULL
  bReverseChargeApplied bit NOT NULL default (0)
  fRecommendedRetailPrice float NULL default (0)
  ucIDSOrdTxSTSCF varchar(30) NULL
  ucIDSOrdTxSTNoofitems varchar(30) NULL
  ucIDGrvTxSTscfno varchar(30) NULL
  ucIDPOrdTxSTscfno varchar(30) NULL
  ucIDSOrdTxCMTransporter varchar(30) NULL
  iMajorIndustryCodeID int NULL default (0)
  iCancellationReasonID int NULL
  iSelectedBarcodeID int NULL default (0)
  ufIDSOrdTxCMQTP float NULL
  ubIDSOrdTxSTDateChanged bit NULL
  udIDSOrdTxSTRequiredDate datetime NULL

## _btblInvoiceLineSN - Invoice Line Serial Number (DocumentSerialNumberLines)
Alias: Invoice Line Serial Number | Freedom Name: DocumentSerialNumberLines | Record Identifier: 
Notes: Invoice Line Serial Number.
PK: idInvoiceLineSN
Columns (15):
  idInvoiceLineSN int NOT NULL identity PK
  iSerialInvoiceID bigint NOT NULL
  iSerialInvoiceLineID bigint NOT NULL
  cSerialNumber varchar(50) NULL
  _btblInvoiceLineSN_iBranchID int NULL
  _btblInvoiceLineSN_dCreatedDate datetime NULL
  _btblInvoiceLineSN_dModifiedDate datetime NULL
  _btblInvoiceLineSN_iCreatedBranchID int NULL
  _btblInvoiceLineSN_iModifiedBranchID int NULL
  _btblInvoiceLineSN_iCreatedAgentID int NULL
  _btblInvoiceLineSN_iModifiedAgentID int NULL
  _btblInvoiceLineSN_iChangeSetID int NULL
  _btblInvoiceLineSN_Checksum binary(20) NULL
  iSerialGroupID int NOT NULL default (0)
  iDeliveryStatus int NULL

## _btblInvoiceMessages - Invoice Message
Alias: Invoice Message | Freedom Name:  | Record Identifier: 
Notes: Invoice Message
PK: idInvoiceMessages
Columns (16):
  idInvoiceMessages int NOT NULL identity PK
  iType int NOT NULL
  cDescription varchar(50) NOT NULL
  cMessage1 varchar(255) NULL
  cMessage2 varchar(255) NULL
  cMessage3 varchar(255) NULL
  bIsExcessInvoice bit NOT NULL default (0)
  _btblInvoiceMessages_iBranchID int NULL
  _btblInvoiceMessages_dCreatedDate datetime NULL
  _btblInvoiceMessages_dModifiedDate datetime NULL
  _btblInvoiceMessages_iCreatedBranchID int NULL
  _btblInvoiceMessages_iModifiedBranchID int NULL
  _btblInvoiceMessages_iCreatedAgentID int NULL
  _btblInvoiceMessages_iModifiedAgentID int NULL
  _btblInvoiceMessages_iChangeSetID int NULL
  _btblInvoiceMessages_Checksum binary(20) NULL

## _btblJCInvoiceLines - Job Costing Invoice Lines
Alias: Job Costing Invoice Lines | Freedom Name:  | Record Identifier: 
Notes: Job Costing Invoice Lines.
PK: idJCInvoiceLines
Columns (63):
  idJCInvoiceLines bigint NOT NULL identity PK
  iJobNumID int NOT NULL
  iJobTxTpID int NULL
  bAdded bit NOT NULL default (0)
  iStockID int NULL
  iSupplierID int NULL
  iLedgerID int NULL
  iEmployeeId int NULL
  cDescription varchar(150) NULL
  fQuantity float NULL
  iUnitsOfMeasureStockingID int NULL
  iUnitsOfMeasureCategoryID int NULL
  iUnitsOfMeasureID int NULL
  fUnitPriceExcl float NULL
  fUnitPriceIncl float NULL
  fUnitCost float NULL
  fLineDiscount float NULL
  iTaxTypeID int NULL
  fTaxRate float NULL
  iWarehouseID int NULL
  iPriceListNameID int NULL
  fLineTotIncl float NULL
  fLineTotExcl float NULL
  fLineTotInclNoDisc float NULL
  fLineTotExclNoDisc float NULL
  fLineTotTaxAmount float NULL
  fLineTotTaxAmountNoDisc float NULL
  iJobStockGroupID int NULL
  iSerialNumberGroupID int NULL
  iSource int NULL
  cLineNotes varchar(1024) NULL
  fExchangeRate float NULL
  fUnitPriceExclForeign float NULL
  fUnitPriceInclForeign float NULL
  fLineTotInclForeign float NULL
  fLineTotExclForeign float NULL
  fLineTotInclNoDiscForeign float NULL
  fLineTotExclNoDiscForeign float NULL
  fLineTotTaxAmountForeign float NULL
  fLineTotTaxAmountNoDiscForeign float NULL
  iLineRepID int NULL
  iLineProjectID int NULL
  bChargeCom bit NOT NULL default (1)
  bLotItem bit NOT NULL default (0)
  iLotID int NULL
  cLotNumber varchar(50) NULL
  dLotExpiryDate datetime NULL
  cReference varchar(20) NULL
  iAPSettlementTermsID int NOT NULL default (0)
  iInvEUNoTCID int NOT NULL default (0)
  iJCTxLinesID bigint NULL
  _btblJCInvoiceLines_iBranchID int NULL
  _btblJCInvoiceLines_dCreatedDate datetime NULL
  _btblJCInvoiceLines_dModifiedDate datetime NULL
  _btblJCInvoiceLines_iCreatedBranchID int NULL
  _btblJCInvoiceLines_iModifiedBranchID int NULL
  _btblJCInvoiceLines_iCreatedAgentID int NULL
  _btblJCInvoiceLines_iModifiedAgentID int NULL
  _btblJCInvoiceLines_iChangeSetID int NULL
  _btblJCInvoiceLines_Checksum binary(20) NULL
  iStockBinLocationID int NOT NULL default (0)
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL

## _btblJCMaster
PK: IdJCMaster
Columns (64):
  IdJCMaster int NOT NULL identity PK
  cJobCode varchar(50) NULL
  cDescription varchar(40) NULL
  iStatus int NULL
  iPostingMethod int NULL
  iAccountsIdWIP int NULL
  iAccountsIdSales int NOT NULL
  iAccountsIdCOS int NULL
  iAccountsIdRecovery int NULL
  iClientId int NULL
  cOrderNo varchar(50) NULL
  cFinalInvoiceNo varchar(50) NULL
  cDeliveryNoteNo varchar(50) NULL
  cFinalCheck varchar(20) NULL
  cAuthorised varchar(20) NULL
  dStartDate datetime NULL
  dCompletionDate datetime NULL
  dDeliveryDate datetime NULL
  dClosingDate datetime NULL
  fQuoteAmount float NULL
  bIsTemplate bit NOT NULL default (0)
  bFinal bit NOT NULL default (0)
  iDeliveryMethodID int NULL
  iProjectID int NULL
  bInclusiveEntry bit NOT NULL default (0)
  bTaxPerLineEntry bit NOT NULL default (1)
  fDiscountPercent float NULL
  iSalesRepId int NULL
  dInvDate datetime NULL
  cAddress1 varchar(40) NULL
  cAddress2 varchar(40) NULL
  cAddress3 varchar(40) NULL
  cAddress4 varchar(40) NULL
  cAddress5 varchar(40) NULL
  cAddress6 varchar(40) NULL
  cPAddress1 varchar(40) NULL
  cPAddress2 varchar(40) NULL
  cPAddress3 varchar(40) NULL
  cPAddress4 varchar(40) NULL
  cPAddress5 varchar(40) NULL
  cPAddress6 varchar(40) NULL
  cMessage1 varchar(255) NULL
  cMessage2 varchar(255) NULL
  cMessage3 varchar(255) NULL
  tNarration text NULL
  cExtOrderNo varchar(50) NULL
  iCurrencyID int NULL
  iJobSettlementTermsID int NOT NULL default (0)
  iTxAddEUNoTCID int NOT NULL default (0)
  iTxRemEUNoTCID int NOT NULL default (0)
  iSortDocID int NULL
  bInventoryMade bit NOT NULL default (0)
  cJMAuditNumber varchar(50) NULL
  _btblJCMaster_iBranchID int NULL
  _btblJCMaster_dCreatedDate datetime NULL
  _btblJCMaster_dModifiedDate datetime NULL
  _btblJCMaster_iCreatedBranchID int NULL
  _btblJCMaster_iModifiedBranchID int NULL
  _btblJCMaster_iCreatedAgentID int NULL
  _btblJCMaster_iModifiedAgentID int NULL
  _btblJCMaster_iChangeSetID int NULL
  _btblJCMaster_Checksum binary(20) NULL
  iWIPVarianceAccountLink int NULL default (0)
  fWIPVarianceValue float NULL default (0)

## _btblJCTxLines - Job Card Transaction Line (JobCardLine)
Alias: Job Card Transaction Line | Freedom Name: JobCardLine | Record Identifier: 
Notes: Job Card Transaction Line.
PK: idJCTxLines
Columns (111):
  idJCTxLines bigint NOT NULL identity PK
  iJCMasterID int NULL
  iJobTxTpID int NULL
  iSource int NULL
  iStockID int NULL
  iSupplierID int NULL
  iLedgerID int NULL
  cDescription varchar(150) NULL
  iStatus int NULL
  iDuration int NULL
  dStartDate datetime NULL
  dEndDate datetime NULL
  fMainDiscount float NULL
  fUnitPriceExcl float NULL
  fUnitPriceIncl float NULL
  fUnitCost float NULL
  fLineDiscount float NULL
  iTaxTypeIDInv int NULL
  fTaxRateInv float NULL
  fTransQty float NULL
  fTransQtyToInvoice float NULL
  fTransQtyInvoiced float NULL
  fTransQtyAvailable float NULL
  fTransWIPAvailable float NOT NULL default (0)
  fTransQtyAdjusted float NOT NULL default (0)
  iUnitsOfMeasureStockingID int NULL
  iUnitsOfMeasureCategoryID int NULL
  iUnitsOfMeasureID int NULL
  iWarehouseID int NULL
  iPriceListNameID int NULL
  iTaxTypeIDGrv int NULL
  fTaxRateGrv float NULL
  fTaxAmountGrv float NULL
  iEmployeeID int NULL
  fBudgetUnitPriceExcl float NULL
  fBudgetUnitPriceIncl float NULL
  fBudgetUnitCost float NULL
  fBudgetLineTotalExcl float NULL
  fBudgetLineTotalIncl float NULL
  fBudgetLineTotalTaxAmountInv float NULL
  fBudgetLineTotalTaxAmountGrv float NULL
  fBudgetLineTotalCost float NULL
  fLineTotalExcl float NULL
  fLineTotalIncl float NULL
  fLineTotalTaxAmountInv float NULL
  fLineTotalExclToInvoice float NULL
  fLineTotalInclToInvoice float NULL
  fLineTotalExclForeign float NULL
  fLineTotalInclForeign float NULL
  fLineTotalTaxAmountInvForeign float NULL
  fLineTotalExclForeignToInvoice float NULL
  fLineTotalInclForeignToInvoice float NULL
  fLineTotalTaxAmountInvForeignToInvoice float NULL
  fLineTotalTaxAmountInvToInvoice float NULL
  fLineTotalExclInvoiced float NULL
  fLineTotalInclInvoiced float NULL
  fLineTotalTaxAmountInvInvoiced float NULL
  fLineTotalExclForeignInvoiced float NULL
  fLineTotalInclForeignInvoiced float NULL
  fLineTotalTaxAmountInvForeignInvoiced float NULL
  fLineTotalCost float NULL
  fLineTotalCostInvoiced float NULL
  bPosted bit NOT NULL default (0)
  bInvoiced bit NOT NULL default (0)
  iJobNumID int NULL
  cinvNumber varchar(50) NULL
  cUserName varchar(50) NULL
  iJobStockGroupID int NULL
  iSerialNumberGroupID int NULL
  iSerialNumberInvoicedGroupID int NULL
  iSerialNumberToInvoiceGroupID int NULL
  cLineNotes varchar(1024) NULL
  iInvNumID bigint NULL
  bPicked bit NOT NULL default (0)
  fExchangeRate float NULL
  fUnitPriceExclForeign float NULL
  fUnitPriceInclForeign float NULL
  fExchangeRateGrv float NULL
  fTaxAmountGrvForeign float NULL
  fBudgetUnitPriceExclForeign float NULL
  fBudgetUnitPriceInclForeign float NULL
  fBudgetLineTotalExclForeign float NULL
  fBudgetLineTotalInclForeign float NULL
  fBudgetLineTotalTaxAmountInvForeign float NULL
  fBudgetLineTotalTaxAmountGrvForeign float NULL
  iGrvCurrencyID int NULL
  iLineRepID int NULL
  iLineProjectID int NULL
  bChargeCom bit NOT NULL default (1)
  iMFPID int NULL
  iLotID int NULL
  cReference varchar(50) NULL
  iInvSettlementTermsID int NOT NULL default (0)
  iAPSettlementTermsID int NOT NULL default (0)
  iEUNoTCID int NOT NULL default (0)
  iLineID int NULL
  _btblJCTxLines_iBranchID int NULL
  _btblJCTxLines_dCreatedDate datetime NULL
  _btblJCTxLines_dModifiedDate datetime NULL
  _btblJCTxLines_iCreatedBranchID int NULL
  _btblJCTxLines_iModifiedBranchID int NULL
  _btblJCTxLines_iCreatedAgentID int NULL
  _btblJCTxLines_iModifiedAgentID int NULL
  _btblJCTxLines_iChangeSetID int NULL
  _btblJCTxLines_Checksum binary(20) NULL
  fTransQtyLastInvoiced float NULL default (0)
  bFiscalInvoiced bit NULL default (0)
  fRecommendedRetailPrice float NULL default (0)
  iStockBinLocationID int NOT NULL default (0)
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL

## _btblJobFiscalTaxes
PK: idInvoiceTaxes
Columns (58):
  idInvoiceTaxes bigint NOT NULL identity PK
  iInvoiceID bigint NOT NULL
  iTaxTypeA int NULL
  FTaxTypeAAm float NULL
  fTaxTypeATax float NULL
  iTaxTypeB int NULL
  fTaxTypeBAm float NULL
  fTaxTypeBTax float NULL
  iTaxTypeC int NULL
  fTaxTypeCAm float NULL
  fTaxTypeCTax float NULL
  iTaxTypeD int NULL
  fTaxTypeDAm float NULL
  fTaxTypeDTax float NULL
  iTaxTypeE int NULL
  fTaxTypeEAm float NULL
  fTaxTypeETax float NULL
  iTaxTypeF int NULL
  fTaxTypeFAm float NULL
  fTaxTypeFTax float NULL
  cSignatureNormal nvarchar(1000) NULL
  DeviceDateNormalDoc smalldatetime NULL
  cSignatureCopy nvarchar(1000) NULL
  DeviceDateCopyDoc smalldatetime NULL
  bDocType bit NOT NULL default (0)
  cMRCNormalDoc nvarchar(50) NULL
  cMRCCopyDoc nvarchar(50) NULL
  _btblJobFiscalTaxes_iBranchID int NULL
  _btblJobFiscalTaxes_dCreatedDate datetime NULL
  _btblJobFiscalTaxes_dModifiedDate datetime NULL
  _btblJobFiscalTaxes_iCreatedBranchID int NULL
  _btblJobFiscalTaxes_iModifiedBranchID int NULL
  _btblJobFiscalTaxes_iCreatedAgentID int NULL
  _btblJobFiscalTaxes_iModifiedAgentID int NULL
  _btblJobFiscalTaxes_iChangeSetID int NULL
  _btblJobFiscalTaxes_Checksum binary(20) NULL
  iTaxTypeG int NULL
  FTaxTypeGAm float NULL
  fTaxTypeGTax float NULL
  iTaxTypeH int NULL
  FTaxTypeHAm float NULL
  fTaxTypeHTax float NULL
  dTrTime datetime NULL
  cInvoiceCode nvarchar(20) NULL
  cInvoiceNumber nvarchar(20) NULL
  cTerminalID nvarchar(20) NULL
  cFiscalCode nvarchar(20) NULL
  fFiscalTotal float NULL default (0)
  cQRCode nvarchar(max) NULL
  cVerificationUrl nvarchar(max) NULL
  bCreditedInv bit NULL default (0)
  cTPIN varchar(20) NULL
  cTaxpayerName varchar(200) NULL
  cTaxpayerAddress varchar(500) NULL
  cTelecomOperator varchar(200) NULL
  cLPONumber varchar(20) NULL
  iLinkedDocID int NULL default (0)
  cMemo nvarchar(50) NULL

## _btblJrBatchDefs - Journal Batch Defaults (JournalBatchDefaults)
Alias: Journal Batch Defaults | Freedom Name: JournalBatchDefaults | Record Identifier: 
Notes: Journal Batch Defaults. Default settings when creating a new joural batch.
PK: idBatchDefs
Columns (27):
  idBatchDefs int NOT NULL identity PK
  bAutoNumbers bit NOT NULL
  iPadLength int NULL
  cPrefix varchar(25) NULL
  iInputTaxID int NULL
  iInputTaxAccID int NULL
  iOutputTaxID int NULL
  iOutputTaxAccID int NULL
  iTrCodeID int NULL
  bBatchRefAutoNumbers bit NOT NULL default (1)
  iBatchRefPadLength int NULL
  cBatchRefPrefix varchar(25) NULL
  iNextBatchRefNo int NULL
  bForceBatchRefNo bit NOT NULL default (1)
  bForceProject bit NOT NULL default (0)
  iRevBatchID int NULL
  _btblJrBatchDefs_iBranchID int NULL
  _btblJrBatchDefs_dCreatedDate datetime NULL
  _btblJrBatchDefs_dModifiedDate datetime NULL
  _btblJrBatchDefs_iCreatedBranchID int NULL
  _btblJrBatchDefs_iModifiedBranchID int NULL
  _btblJrBatchDefs_iCreatedAgentID int NULL
  _btblJrBatchDefs_iModifiedAgentID int NULL
  _btblJrBatchDefs_iChangeSetID int NULL
  _btblJrBatchDefs_Checksum binary(20) NULL
  xInputTaxAccAttribute xml NULL
  xOutputTaxAccAttribute xml NULL

## _btblJrBatches - Journal Batch (JournalBatchHeader)
Alias: Journal Batch | Freedom Name: JournalBatchHeader | Record Identifier: 
Notes: Journal Batch.
PK: idBatches
Columns (45):
  idBatches int NOT NULL identity PK
  cBatchNo varchar(50) NULL
  cBatchDesc varchar(40) NULL
  iInputTaxID int NULL
  iInputTaxAccID int NULL
  iOutputTaxID int NULL
  iOutputTaxAccID int NULL
  bCalcTax bit NOT NULL
  iTrCodeID int NULL
  bClearBatch bit NOT NULL
  iDateLineOpt int NULL
  dDefDate smalldatetime NULL
  iRefLineOpt int NULL
  cDefRef varchar(20) NULL
  iDescLineOpt int NULL
  cDefDesc varchar(40) NULL
  bCheckedOut bit NULL default (0)
  iMaxRecur int NULL
  iBatchPosted int NULL
  cBatchRef varchar(50) NULL
  bPromptGlobalChanges bit NULL default (0)
  dDateBatchCreated datetime NULL
  iAgentBatchCreated int NOT NULL default (1)
  iAgentCheckedOut int NOT NULL default (0)
  bAccrualBatch bit NULL default (0)
  iAccrualDateOpt int NULL
  dDefAccrualDay int NULL
  iAccrualRefOpt int NULL
  cDefAccrualRefPrefixOrSuffix varchar(20) NULL
  dProcessedDate datetime NULL
  bInterBranchBatch bit NOT NULL default (0)
  iBranchLoanAccountID int NULL
  bRevaluationBatch bit NOT NULL default (0)
  _btblJrBatches_iBranchID int NULL
  _btblJrBatches_dCreatedDate datetime NULL
  _btblJrBatches_dModifiedDate datetime NULL
  _btblJrBatches_iCreatedBranchID int NULL
  _btblJrBatches_iModifiedBranchID int NULL
  _btblJrBatches_iCreatedAgentID int NULL
  _btblJrBatches_iModifiedAgentID int NULL
  _btblJrBatches_iChangeSetID int NULL
  _btblJrBatches_Checksum binary(20) NULL
  imSCOAVerID int NOT NULL default (0)
  xInputTaxAccAttribute xml NULL
  xOutputTaxAccAttribute xml NULL

## _btblJrBatchLines - Journal Batch Lines (JournalBatchLines)
Alias: Journal Batch Lines | Freedom Name: JournalBatchLines | Record Identifier: 
Notes: Journal Batch Lines.
PK: idBatchLines
Columns (32):
  idBatchLines int NOT NULL identity PK
  iBatchesID int NOT NULL
  dTxDate smalldatetime NULL
  iAccountID int NULL
  cDescription varchar(100) NULL
  cReference varchar(50) NULL
  fDebit float NULL
  fCredit float NULL
  fTaxAmount float NULL
  iTaxTypeID int NULL
  iTaxAccountID int NULL
  iProjectID int NULL
  bAccrual bit NULL default (0)
  _btblJrBatchLines_iBranchID int NULL
  _btblJrBatchLines_dCreatedDate datetime NULL
  _btblJrBatchLines_dModifiedDate datetime NULL
  _btblJrBatchLines_iCreatedBranchID int NULL
  _btblJrBatchLines_iModifiedBranchID int NULL
  _btblJrBatchLines_iCreatedAgentID int NULL
  _btblJrBatchLines_iModifiedAgentID int NULL
  _btblJrBatchLines_iChangeSetID int NULL
  _btblJrBatchLines_Checksum binary(20) NULL
  iFCAccCurrencyID int NOT NULL default (0)
  fExchangeRate float NOT NULL default (0)
  fDebitForeign float NOT NULL default (0)
  fCreditForeign float NOT NULL default (0)
  fTaxAmountForeign float NOT NULL default (0)
  cTaxCompanyName varchar(150) NULL
  cTaxCompanyRegistration varchar(50) NULL
  cTaxRegistration varchar(50) NULL
  xAttribute xml NULL
  iMajorIndustryCodeID int NULL default (0)

## _btblLogDetails
PK: idLogDetails
Columns (17):
  idLogDetails int NOT NULL identity PK
  iLogMasterID int NOT NULL
  dGroupTime smalldatetime NOT NULL
  dTimeLogged datetime NOT NULL
  iAgentID int NOT NULL
  iSeverity int NOT NULL
  cDetails varchar(1024) NULL
  cAddInfo varchar(1024) NULL
  _btblLogDetails_iBranchID int NULL
  _btblLogDetails_dCreatedDate datetime NULL
  _btblLogDetails_dModifiedDate datetime NULL
  _btblLogDetails_iCreatedBranchID int NULL
  _btblLogDetails_iModifiedBranchID int NULL
  _btblLogDetails_iCreatedAgentID int NULL
  _btblLogDetails_iModifiedAgentID int NULL
  _btblLogDetails_iChangeSetID int NULL
  _btblLogDetails_Checksum binary(20) NULL

## _btblLogMaster - Log Master
Alias: Log Master | Freedom Name:  | Record Identifier: 
Notes: Log Master.
PK: iLogOrdinal
Columns (12):
  idLogMaster int NOT NULL identity
  iLogOrdinal int NOT NULL PK
  cLogName varchar(50) NOT NULL
  _btblLogMaster_iBranchID int NULL
  _btblLogMaster_dCreatedDate datetime NULL
  _btblLogMaster_dModifiedDate datetime NULL
  _btblLogMaster_iCreatedBranchID int NULL
  _btblLogMaster_iModifiedBranchID int NULL
  _btblLogMaster_iCreatedAgentID int NULL
  _btblLogMaster_iModifiedAgentID int NULL
  _btblLogMaster_iChangeSetID int NULL
  _btblLogMaster_Checksum binary(20) NULL

## _btblNotes - Notes (GeneralNotes)
Alias: Notes | Freedom Name: GeneralNotes | Record Identifier: 
Notes: Notes
PK: idNotes
Columns (17):
  idNotes int NOT NULL identity PK
  cNOTETBLTableName varchar(30) NULL
  cNOTETBLTableID varchar(50) NULL
  dNOTETBLCreated datetime NULL
  dNOTETBLModified datetime NULL
  iNOTETBLAgentID int NULL
  nNOTETBLText text NULL
  cNOTETBLTableKeyField varchar(64) NULL
  _btblNotes_iBranchID int NULL
  _btblNotes_dCreatedDate datetime NULL
  _btblNotes_dModifiedDate datetime NULL
  _btblNotes_iCreatedBranchID int NULL
  _btblNotes_iModifiedBranchID int NULL
  _btblNotes_iCreatedAgentID int NULL
  _btblNotes_iModifiedAgentID int NULL
  _btblNotes_iChangeSetID int NULL
  _btblNotes_Checksum binary(20) NULL

## _btblPOSTenderTx - POS Tender Transaction
Alias: POS Tender Transaction | Freedom Name:  | Record Identifier: 
Notes: POS Tender Transaction.
PK: IDPOSTenderTx
Columns (35):
  IDPOSTenderTx int NOT NULL identity PK
  iTenderID int NOT NULL
  cNarrative varchar(30) NULL
  fTxAmount float NULL
  iPOSXZTableID int NULL
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
  _btblPOSTenderTx_iBranchID int NULL
  _btblPOSTenderTx_dCreatedDate datetime NULL
  _btblPOSTenderTx_dModifiedDate datetime NULL
  _btblPOSTenderTx_iCreatedBranchID int NULL
  _btblPOSTenderTx_iModifiedBranchID int NULL
  _btblPOSTenderTx_iCreatedAgentID int NULL
  _btblPOSTenderTx_iModifiedAgentID int NULL
  _btblPOSTenderTx_iChangeSetID int NULL
  _btblPOSTenderTx_Checksum binary(20) NULL

## _btblPOSXZTable - POS XZ Table
Alias: POS XZ Table | Freedom Name:  | Record Identifier: 
Notes: POS XZ Table
PK: IDPOSXZTable
Columns (21):
  IDPOSXZTable int NOT NULL identity PK
  dTranDate datetime NULL
  iTillTxType int NULL
  iTillsID int NULL
  iAgentsID int NULL
  iTrCodesID int NULL
  iAccountID int NULL
  cXZAuditNumber varchar(50) NULL
  fAmtTendered float NULL
  fTranAmount float NULL
  fChange float NULL
  _btblPOSXZTable_iBranchID int NULL
  _btblPOSXZTable_dCreatedDate datetime NULL
  _btblPOSXZTable_dModifiedDate datetime NULL
  _btblPOSXZTable_iCreatedBranchID int NULL
  _btblPOSXZTable_iModifiedBranchID int NULL
  _btblPOSXZTable_iCreatedAgentID int NULL
  _btblPOSXZTable_iModifiedAgentID int NULL
  _btblPOSXZTable_iChangeSetID int NULL
  _btblPOSXZTable_Checksum binary(20) NULL
  iInvNumID bigint NOT NULL default (0)

## _btblRBFolder - RB Folder
Alias: RB Folder | Freedom Name:  | Record Identifier: 
PK: cFolderName+iParentId
Columns (12):
  IdFolder int NOT NULL identity
  cFolderName varchar(60) NOT NULL PK
  iParentId int NOT NULL PK
  _btblRBFolder_iBranchID int NULL
  _btblRBFolder_dCreatedDate datetime NULL
  _btblRBFolder_dModifiedDate datetime NULL
  _btblRBFolder_iCreatedBranchID int NULL
  _btblRBFolder_iModifiedBranchID int NULL
  _btblRBFolder_iCreatedAgentID int NULL
  _btblRBFolder_iModifiedAgentID int NULL
  _btblRBFolder_iChangeSetID int NULL
  _btblRBFolder_Checksum binary(20) NULL

## _btblRBItem
PK: iFolderId+iItemType+cItemName+dModified
Columns (17):
  IdItem int NOT NULL identity
  iFolderId int NOT NULL PK
  cItemName varchar(60) NOT NULL PK
  iItemSize int NULL
  iItemType int NOT NULL PK
  dModified datetime NOT NULL PK
  dDeleted datetime NULL
  imgTemplate image NULL
  _btblRBItem_iBranchID int NULL
  _btblRBItem_dCreatedDate datetime NULL
  _btblRBItem_dModifiedDate datetime NULL
  _btblRBItem_iCreatedBranchID int NULL
  _btblRBItem_iModifiedBranchID int NULL
  _btblRBItem_iCreatedAgentID int NULL
  _btblRBItem_iModifiedAgentID int NULL
  _btblRBItem_iChangeSetID int NULL
  _btblRBItem_Checksum binary(20) NULL

## _btblRBUDefField
PK: cTableName+cFieldName
Columns (18):
  cTableName varchar(60) NOT NULL PK
  cFieldName varchar(60) NOT NULL PK
  cFieldAlias varchar(60) NULL
  cDataType varchar(60) NULL
  cSelectable char(1) NULL
  cSearchable char(1) NULL
  cSortable char(1) NULL
  cAutoSearch char(1) NULL
  cMandatory char(1) NULL
  _btblRBUDefField_iBranchID int NULL
  _btblRBUDefField_dCreatedDate datetime NULL
  _btblRBUDefField_dModifiedDate datetime NULL
  _btblRBUDefField_iCreatedBranchID int NULL
  _btblRBUDefField_iModifiedBranchID int NULL
  _btblRBUDefField_iCreatedAgentID int NULL
  _btblRBUDefField_iModifiedAgentID int NULL
  _btblRBUDefField_iChangeSetID int NULL
  _btblRBUDefField_Checksum binary(20) NULL

## _btblSerialNumberLink - Serial Number Link (SerialNumberLink)
Alias: Serial Number Link | Freedom Name: SerialNumberLink | Record Identifier: 
Notes: Serial Number Link.
PK: IDSerialNumberLink
Columns (12):
  IDSerialNumberLink int NOT NULL identity PK
  iSerialNumberGroupID int NOT NULL
  iSerialMfID int NOT NULL
  _btblSerialNumberLink_iBranchID int NULL
  _btblSerialNumberLink_dCreatedDate datetime NULL
  _btblSerialNumberLink_dModifiedDate datetime NULL
  _btblSerialNumberLink_iCreatedBranchID int NULL
  _btblSerialNumberLink_iModifiedBranchID int NULL
  _btblSerialNumberLink_iCreatedAgentID int NULL
  _btblSerialNumberLink_iModifiedAgentID int NULL
  _btblSerialNumberLink_iChangeSetID int NULL
  _btblSerialNumberLink_Checksum binary(20) NULL

## _btblSimpleTree
PK: idSimpleTree
Columns (12):
  idSimpleTree int NOT NULL PK
  idSystemTree int NOT NULL
  cDescription varchar(64) NULL
  _btblSimpleTree_iBranchID int NULL
  _btblSimpleTree_dCreatedDate datetime NULL
  _btblSimpleTree_dModifiedDate datetime NULL
  _btblSimpleTree_iCreatedBranchID int NULL
  _btblSimpleTree_iModifiedBranchID int NULL
  _btblSimpleTree_iCreatedAgentID int NULL
  _btblSimpleTree_iModifiedAgentID int NULL
  _btblSimpleTree_iChangeSetID int NULL
  _btblSimpleTree_Checksum binary(20) NULL

## _btblState
PK: idState
Columns (12):
  idState int NOT NULL identity PK
  cStateCode varchar(10) NOT NULL
  cStateDescription varchar(50) NULL
  _btblState_iBranchID int NULL
  _btblState_dCreatedDate datetime NULL
  _btblState_dModifiedDate datetime NULL
  _btblState_iCreatedBranchID int NULL
  _btblState_iModifiedBranchID int NULL
  _btblState_iCreatedAgentID int NULL
  _btblState_iModifiedAgentID int NULL
  _btblState_iChangeSetID int NULL
  _btblState_Checksum binary(20) NULL

## _btblSystemFunction - System Function (SystemFunction)
Alias: System Function | Freedom Name: SystemFunction | Record Identifier: 
Notes: Used for internal purposes only
PK: idSystemFunction
Columns (19):
  idSystemFunction int NOT NULL PK
  cFunctionDesc varchar(100) NULL
  iParentSystemFunctionID int NULL
  iModulesHi int NULL
  iModulesLo int NULL
  bIsBusinessRule bit NOT NULL default (0)
  bCanDelete bit NOT NULL default (0)
  bIsSystemRule bit NOT NULL default (1)
  iAppID int NULL
  gIdentifier uniqueidentifier NULL
  _btblSystemFunction_iBranchID int NULL
  _btblSystemFunction_dCreatedDate datetime NULL
  _btblSystemFunction_dModifiedDate datetime NULL
  _btblSystemFunction_iCreatedBranchID int NULL
  _btblSystemFunction_iModifiedBranchID int NULL
  _btblSystemFunction_iCreatedAgentID int NULL
  _btblSystemFunction_iModifiedAgentID int NULL
  _btblSystemFunction_iChangeSetID int NULL
  _btblSystemFunction_Checksum binary(20) NULL

## _btblSystemTree - System Tree (SystemTree)
Alias: System Tree | Freedom Name: SystemTree | Record Identifier: 
Notes: System Tree
PK: idSystemTree
Columns (35):
  idSystemTree int NOT NULL PK
  iModuleLo int NULL
  iModuleHi int NULL
  iForceModulesLo int NULL
  iForceModulesHi int NULL
  mDisableForModulesLo int NULL
  mDisableForModulesHi int NULL
  iOrder int NOT NULL
  cPackage varchar(32) NOT NULL
  cDescription varchar(64) NULL
  iType int NOT NULL
  cObject varchar(50) NULL
  cCommand varchar(256) NULL
  bAlwaysLoad bit NOT NULL default (0)
  cToolbar varchar(32) NULL
  cMenu varchar(32) NULL
  cMenuName varchar(50) NULL
  bMenuSub bit NOT NULL default (0)
  bHideNoChild bit NOT NULL default (0)
  bAllowDesign bit NOT NULL default (1)
  bAdminOnly bit NOT NULL default (0)
  bSysNode bit NOT NULL default (0)
  bExcludeBranches bit NOT NULL default (0)
  iAppID int NULL
  gIdentifier uniqueidentifier NULL
  _btblSystemTree_iBranchID int NULL
  _btblSystemTree_dCreatedDate datetime NULL
  _btblSystemTree_dModifiedDate datetime NULL
  _btblSystemTree_iCreatedBranchID int NULL
  _btblSystemTree_iModifiedBranchID int NULL
  _btblSystemTree_iCreatedAgentID int NULL
  _btblSystemTree_iModifiedAgentID int NULL
  _btblSystemTree_iChangeSetID int NULL
  _btblSystemTree_Checksum binary(20) NULL
  bEvolutionHandled int NULL default (0)

## _btblTMCalcSheet - Tax Manager Calc Sheet
Alias: Tax Manager Calc Sheet | Freedom Name:  | Record Identifier: 
Notes: Tax Manager Calc Sheet
PK: idCalcSheet
Columns (22):
  idCalcSheet int NOT NULL identity PK
  iTaxTypeID int NULL
  cOperation char(1) NOT NULL
  cDescription varchar(100) NOT NULL
  bEditable bit NOT NULL default (0)
  iTaxBoxID int NULL
  iTaxBoxDestID int NOT NULL default (0)
  iOrder int NOT NULL default (1)
  fValue float NULL
  bDirect bit NOT NULL default (0)
  fTaxRate float NULL
  dStartDate datetime NULL
  dEndDate datetime NULL
  _btblTMCalcSheet_iBranchID int NULL
  _btblTMCalcSheet_dCreatedDate datetime NULL
  _btblTMCalcSheet_dModifiedDate datetime NULL
  _btblTMCalcSheet_iCreatedBranchID int NULL
  _btblTMCalcSheet_iModifiedBranchID int NULL
  _btblTMCalcSheet_iCreatedAgentID int NULL
  _btblTMCalcSheet_iModifiedAgentID int NULL
  _btblTMCalcSheet_iChangeSetID int NULL
  _btblTMCalcSheet_Checksum binary(20) NULL

## _btblTMTaxBox - Tax Manager Tax Box
Alias: Tax Manager Tax Box | Freedom Name:  | Record Identifier: 
Notes: Tax ManagerTax Box
PK: idTaxBox
Columns (18):
  idTaxBox int NOT NULL identity PK
  cCode varchar(4) NOT NULL
  cDescription varchar(100) NOT NULL
  bTax bit NOT NULL default (1)
  bPayroll bit NOT NULL default (1)
  bWithHolding bit NOT NULL default (1)
  iGLSign int NULL default (1)
  dStartDate datetime NULL
  dEndDate datetime NULL
  _btblTMTaxBox_iBranchID int NULL
  _btblTMTaxBox_dCreatedDate datetime NULL
  _btblTMTaxBox_dModifiedDate datetime NULL
  _btblTMTaxBox_iCreatedBranchID int NULL
  _btblTMTaxBox_iModifiedBranchID int NULL
  _btblTMTaxBox_iCreatedAgentID int NULL
  _btblTMTaxBox_iModifiedAgentID int NULL
  _btblTMTaxBox_iChangeSetID int NULL
  _btblTMTaxBox_Checksum binary(20) NULL

## _btblTMTaxPeriod - Tax Manager Tax Period
Alias: Tax Manager Tax Period | Freedom Name:  | Record Identifier: 
Notes: Tax Manager Tax Period
PK: idTaxPeriod
Columns (21):
  idTaxPeriod int NOT NULL identity PK
  dStartDate smalldatetime NOT NULL
  dEndDate smalldatetime NOT NULL
  cDescription varchar(80) NOT NULL
  iYear int NOT NULL
  iPeriodNo int NOT NULL
  bWithHolding bit NOT NULL default (1)
  bPayroll bit NOT NULL default (1)
  bTax bit NOT NULL default (1)
  bClosed bit NOT NULL default (0)
  _btblTMTaxPeriod_iBranchID int NULL
  _btblTMTaxPeriod_dCreatedDate datetime NULL
  _btblTMTaxPeriod_dModifiedDate datetime NULL
  _btblTMTaxPeriod_iCreatedBranchID int NULL
  _btblTMTaxPeriod_iModifiedBranchID int NULL
  _btblTMTaxPeriod_iCreatedAgentID int NULL
  _btblTMTaxPeriod_iModifiedAgentID int NULL
  _btblTMTaxPeriod_iChangeSetID int NULL
  _btblTMTaxPeriod_Checksum binary(20) NULL
  iTaxYearID int NOT NULL default (0)
  dDueDate datetime NULL

## _btblTMTaxPeriodYear
PK: idTaxPeriodYear
Columns (13):
  idTaxPeriodYear int NOT NULL identity PK
  cTaxYearDescription varchar(50) NOT NULL
  dTaxYearEndDate datetime NOT NULL
  _btblTMTaxPeriodYear_iBranchID int NULL
  _btblTMTaxPeriodYear_dCreatedDate datetime NULL
  _btblTMTaxPeriodYear_dModifiedDate datetime NULL
  _btblTMTaxPeriodYear_iCreatedBranchID int NULL
  _btblTMTaxPeriodYear_iModifiedBranchID int NULL
  _btblTMTaxPeriodYear_iCreatedAgentID int NULL
  _btblTMTaxPeriodYear_iModifiedAgentID int NULL
  _btblTMTaxPeriodYear_iChangeSetID int NULL
  _btblTMTaxPeriodYear_Checksum binary(20) NULL
  iTaxPeriodFrequency int NOT NULL default (0)

## _btblTMTaxTotals - Tax Manager Tax Totals (TaxTotal)
Alias: Tax Manager Tax Totals | Freedom Name: TaxTotal | Record Identifier: 
Notes: Tax Manager Tax Totals
PK: idTaxTotals
Columns (13):
  idTaxTotals int NOT NULL identity PK
  fTotal float NOT NULL
  iTaxPeriodID int NOT NULL
  iTaxBoxID int NOT NULL
  _btblTMTaxTotals_iBranchID int NULL
  _btblTMTaxTotals_dCreatedDate datetime NULL
  _btblTMTaxTotals_dModifiedDate datetime NULL
  _btblTMTaxTotals_iCreatedBranchID int NULL
  _btblTMTaxTotals_iModifiedBranchID int NULL
  _btblTMTaxTotals_iCreatedAgentID int NULL
  _btblTMTaxTotals_iModifiedAgentID int NULL
  _btblTMTaxTotals_iChangeSetID int NULL
  _btblTMTaxTotals_Checksum binary(20) NULL
