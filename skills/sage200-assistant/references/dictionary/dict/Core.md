# Sage 200 Evolution table dictionary - Core

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## ACCBLNC - General Ledger Account Balances
Alias: General Ledger Account Balances | Freedom Name:  | Record Identifier: 
Notes: Stores general ledger account balances. The amount of records in this table should equal the amount of records in the ACCOUNTS table.
Columns: none recorded yet (table seen in another Evolution database, not in the scripted one)

## Accounts - General Ledger Account (Account)
Alias: General Ledger Account | Freedom Name: Account | Record Identifier: Master_Sub_Account
Notes: General Ledger Account Listing.
PK: AccountLink
Columns (80):
  AccountLink int NOT NULL identity PK
  Master_Sub_Account varchar(91) NULL
  AccountLevel int NULL
  Account varchar(91) NULL
  iAccountType int NOT NULL default (0)
  SubAccOfLink int NULL
  Dept varchar(10) NULL
  Brch varchar(10) NULL
  Jr bit NOT NULL default (0)
  Description varchar(255) NULL
  CaseAcc varchar(10) NULL
  ActiveAccount bit NOT NULL default (1)
  dAccountsTimeStamp datetime NULL
  cNextChequeNum varchar(20) NULL
  iGLSegment0ID int NULL
  iGLSegment1ID int NULL
  iGLSegment2ID int NULL
  iGLSegment3ID int NULL
  iGLSegment4ID int NULL
  iGLSegment5ID int NULL
  iGLSegment6ID int NULL
  iGLSegment7ID int NULL
  iGLSegment8ID int NULL
  iGLSegment9ID int NULL
  iReportCategoryID int NULL
  fBankStatementBalance float NULL
  cExtDescription varchar(255) NULL
  iTaxTypeINVID int NULL
  iTaxTypeCRNID int NULL
  iTaxTypeGRVID int NULL
  iTaxTypeRTSID int NULL
  iAllowICSales bit NOT NULL default (0)
  iAllowICPurchases bit NOT NULL default (0)
  iMBReportingCategoryID int NULL
  iMBCashFlowCategoryID int NULL
  bMBIsAsset bit NOT NULL default (0)
  bMBIsGrant bit NOT NULL default (0)
  iMBAssetClassificationID int NULL
  iMBAssetCategoryID int NULL
  iMBAssetTypeID int NULL
  iMBGrantLevel1TypeID int NULL
  iMBGrantLevel2TypeID int NULL
  iMBGrantLevel3TypeID int NULL
  bIsBranchLoanAccount bit NOT NULL default (0)
  bForeignBankAcc bit NOT NULL default (0)
  iForeignBankCurrencyID int NULL
  iForeignBankPEXAccID int NULL
  iForeignBankLEXAccID int NULL
  bRevalueWithSellingRate bit NOT NULL default (1)
  bPaymentsBasedTax bit NOT NULL default (0)
  cBankName varchar(40) NULL
  cBankAccountName varchar(50) NULL
  cBankCode varchar(15) NULL
  cBankAccountNumber varchar(40) NULL
  cBranchName varchar(30) NULL
  cSEPABranchCode varchar(30) NULL
  cBankRefNr varchar(30) NULL
  Accounts_iBranchID int NULL
  Accounts_dCreatedDate datetime NULL
  Accounts_dModifiedDate datetime NULL
  Accounts_iCreatedBranchID int NULL
  Accounts_iModifiedBranchID int NULL
  Accounts_iCreatedAgentID int NULL
  Accounts_iModifiedAgentID int NULL
  Accounts_iChangeSetID int NULL
  Accounts_Checksum binary(20) NULL
  ulGLSector1 varchar(100) NULL
  ulGLSector2 varchar(100) NULL
  ulGLSector3 varchar(100) NULL
  ulGLSector4 varchar(100) NULL
  ulGLSector5 varchar(100) NULL
  ulGLSector6 varchar(100) NULL
  ulGLSector7 varchar(100) NULL
  ulGLSector8 varchar(100) NULL
  ulGLSector9 varchar(100) NULL
  ulGLSector10 varchar(100) NULL
  ulGLCostCentre varchar(100) NULL
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL
  cSBFBankAccountID varchar(100) NULL

## AccPrev - Prior Year GL Balance (AccountPreviousBalancesOld)
Alias: Prior Year GL Balance | Freedom Name: AccountPreviousBalancesOld | Record Identifier: 
Notes: Previous balances table. The amount of records in this table should equal the amount of records in the ACCOUNTS table.
PK: LedgerLink+iTxBranchPrevID
Columns (59):
  LedgerLink int NOT NULL PK
  BFDebits00 float NULL
  BFDebits01 float NULL
  BFDebits02 float NULL
  BFDebits03 float NULL
  BFDebits04 float NULL
  BFDebits05 float NULL
  BFCredits00 float NULL
  BFCredits01 float NULL
  BFCredits02 float NULL
  BFCredits03 float NULL
  BFCredits04 float NULL
  BFCredits05 float NULL
  PrevBal01 float NULL
  PrevBal02 float NULL
  PrevBal03 float NULL
  PrevBal04 float NULL
  PrevBal05 float NULL
  PrevBal06 float NULL
  PrevBal07 float NULL
  PrevBal08 float NULL
  PrevBal09 float NULL
  PrevBal10 float NULL
  PrevBal11 float NULL
  PrevBal12 float NULL
  BFForeignDebits00 float NULL
  BFForeignDebits01 float NULL
  BFForeignDebits02 float NULL
  BFForeignDebits03 float NULL
  BFForeignDebits04 float NULL
  BFForeignDebits05 float NULL
  BFForeignCredits00 float NULL
  BFForeignCredits01 float NULL
  BFForeignCredits02 float NULL
  BFForeignCredits03 float NULL
  BFForeignCredits04 float NULL
  BFForeignCredits05 float NULL
  PrevForeignBal01 float NULL
  PrevForeignBal02 float NULL
  PrevForeignBal03 float NULL
  PrevForeignBal04 float NULL
  PrevForeignBal05 float NULL
  PrevForeignBal06 float NULL
  PrevForeignBal07 float NULL
  PrevForeignBal08 float NULL
  PrevForeignBal09 float NULL
  PrevForeignBal10 float NULL
  PrevForeignBal11 float NULL
  PrevForeignBal12 float NULL
  iTxBranchPrevID int NOT NULL PK default (-1)
  AccPrev_iBranchID int NULL
  AccPrev_dCreatedDate datetime NULL
  AccPrev_dModifiedDate datetime NULL
  AccPrev_iCreatedBranchID int NULL
  AccPrev_iModifiedBranchID int NULL
  AccPrev_iCreatedAgentID int NULL
  AccPrev_iModifiedAgentID int NULL
  AccPrev_iChangeSetID int NULL
  AccPrev_Checksum binary(20) NULL

## Areas - Area (Area)
Alias: Area | Freedom Name: Area | Record Identifier: Code
Notes: Area table for Customers and Suppliers
PK: idAreas
Columns (12):
  idAreas int NOT NULL identity PK
  Code varchar(10) NOT NULL
  Description varchar(30) NULL
  Areas_iBranchID int NULL
  Areas_dCreatedDate datetime NULL
  Areas_dModifiedDate datetime NULL
  Areas_iCreatedBranchID int NULL
  Areas_iModifiedBranchID int NULL
  Areas_iCreatedAgentID int NULL
  Areas_iModifiedAgentID int NULL
  Areas_iChangeSetID int NULL
  Areas_Checksum binary(20) NULL

## BankMain - Bank (BankMain)
Alias: Bank | Freedom Name: BankMain | Record Identifier: BankName
Notes: Bank
PK: Counter
Columns (14):
  Counter int NOT NULL identity PK
  BankName varchar(40) NULL
  Branch varchar(12) NULL
  ActiveBank varchar(1) NULL
  BankMain_iBranchID int NULL
  BankMain_dCreatedDate datetime NULL
  BankMain_dModifiedDate datetime NULL
  BankMain_iCreatedBranchID int NULL
  BankMain_iModifiedBranchID int NULL
  BankMain_iCreatedAgentID int NULL
  BankMain_iModifiedAgentID int NULL
  BankMain_iChangeSetID int NULL
  BankMain_Checksum binary(20) NULL
  iSagePayBank int NULL

## BomComp - BOM Component (BillOfMaterialsComponents)
Alias: BOM Component | Freedom Name: BillOfMaterialsComponents | Record Identifier: 
Notes: BOM Component
PK: BomComponentKey
Columns (23):
  BomComponentKey int NOT NULL identity PK
  BomMasterKey int NULL
  ComponentStockLink int NULL
  ComponentIndex int NULL
  ProductionQty float NULL
  UnitOfMeasure varchar(4) NULL
  UnitCost float NULL
  Description varchar(50) NULL
  DefaultWhseID int NULL
  fBreakAllocCostPerc float NULL
  fOffsetLeadTime float NULL
  BomComp_iBranchID int NULL
  BomComp_dCreatedDate datetime NULL
  BomComp_dModifiedDate datetime NULL
  BomComp_iCreatedBranchID int NULL
  BomComp_iModifiedBranchID int NULL
  BomComp_iCreatedAgentID int NULL
  BomComp_iModifiedAgentID int NULL
  BomComp_iChangeSetID int NULL
  BomComp_Checksum binary(20) NULL
  bUseDefaultBinLevels bit NOT NULL default (0)
  DefaultStockBinLocationID int NOT NULL default (0)
  xDefaultAttribute xml NULL

## BomDef - BOM Default (BillOfMaterialsDefault)
Alias: BOM Default | Freedom Name: BillOfMaterialsDefault | Record Identifier: 
Notes: Bill of Material default
PK: idBomDef
Columns (46):
  TxCode varchar(20) NULL
  BrkUpTxCode varchar(20) NULL
  UpdCostTxCode varchar(20) NULL
  PromptToManuf int NULL
  TempNumber int NULL
  NextBillManufRef varchar(50) NULL
  NextBillBrkRef varchar(50) NULL
  NextBillUpdateRef varchar(50) NULL
  iBreakupOnGrvPrompt int NULL
  bShowComponentsOnGRV bit NULL
  iAccountsIDDefSurplus int NULL
  iMFTxCodeID int NULL
  iDRTxCodeID int NULL
  iBPTxCodeID int NULL
  iWATxCodeID int NULL
  iUMTxCodeID int NULL
  iVATxCodeID int NULL
  bShowAvailAllLevels bit NOT NULL default (0)
  bShowCompOnInv bit NOT NULL default (0)
  bAutoNumManuf bit NOT NULL default (0)
  bAutoNumBreakUp bit NOT NULL default (0)
  bAutoNumUpdateCosts bit NOT NULL default (0)
  bPromptPickSlip bit NOT NULL default (0)
  bAlwaysPrintPickSlip bit NOT NULL default (0)
  bManufAutoNumLine bit NOT NULL default (0)
  cNextManufRefLine varchar(50) NULL
  bOverwriteAutoManufRef bit NOT NULL default (0)
  iMFPFilterStLength int NOT NULL default (0)
  bPickSlipPrintAllLines bit NOT NULL default (0)
  bPickSlipPrintUnprintedLines bit NOT NULL default (0)
  bPickSlipPrintLastSessionLines bit NOT NULL default (1)
  bPickSlipPrintSubManuf bit NOT NULL default (0)
  bForceProject bit NOT NULL default (0)
  bUniqueManufRef bit NULL
  idBomDef int NOT NULL identity PK
  iDefaultComponentWhseID int NULL
  bOverDrawWarning bit NOT NULL default (0)
  BomDef_iBranchID int NULL
  BomDef_dCreatedDate datetime NULL
  BomDef_dModifiedDate datetime NULL
  BomDef_iCreatedBranchID int NULL
  BomDef_iModifiedBranchID int NULL
  BomDef_iCreatedAgentID int NULL
  BomDef_iModifiedAgentID int NULL
  BomDef_iChangeSetID int NULL
  BomDef_Checksum binary(20) NULL

## BomMast - Bill Master (BillOfMaterialsMaster)
Alias: Bill Master | Freedom Name: BillOfMaterialsMaster | Record Identifier: 
Notes: Bill Of Materials Master Item
PK: BomID
Columns (27):
  BomID int NOT NULL identity PK
  BomStockLink int NULL
  BomStockCode varchar(255) NULL
  BomDescription varchar(50) NULL
  BomProductionQty float NULL
  BomUnitCost float NULL
  ThisLevelCost float NULL
  DateLastCosted smalldatetime NULL
  bBreakOnGrv bit NOT NULL default (0)
  bBreakAllocCostsbyPerc bit NOT NULL default (0)
  bShowComponentsOnGRV bit NOT NULL default (0)
  bShowAvailAllLevels bit NOT NULL default (0)
  bShowCompOnInv bit NOT NULL default (0)
  bManufWithDefaultWH bit NOT NULL default (0)
  bBreakUpWithDefaultWH bit NOT NULL default (0)
  bAllowOverUnderManufacture bit NOT NULL default (0)
  BomMast_fLeadDays float NULL
  BomMast_iBranchID int NULL
  BomMast_dCreatedDate datetime NULL
  BomMast_dModifiedDate datetime NULL
  BomMast_iCreatedBranchID int NULL
  BomMast_iModifiedBranchID int NULL
  BomMast_iCreatedAgentID int NULL
  BomMast_iModifiedAgentID int NULL
  BomMast_iChangeSetID int NULL
  BomMast_Checksum binary(20) NULL
  bExplodeOnDocument bit NULL default (0)

## CCDefs - Credit Control Default (CreditControlDefaults)
Alias: Credit Control Default | Freedom Name: CreditControlDefaults | Record Identifier: 
Notes: Credit Control Default.
PK: idCCDefs
Columns (13):
  idCCDefs int NOT NULL identity PK
  PassScore float NOT NULL
  Completeness text NULL
  iPromptOpt int NULL
  CCDefs_iBranchID int NULL
  CCDefs_dCreatedDate datetime NULL
  CCDefs_dModifiedDate datetime NULL
  CCDefs_iCreatedBranchID int NULL
  CCDefs_iModifiedBranchID int NULL
  CCDefs_iCreatedAgentID int NULL
  CCDefs_iModifiedAgentID int NULL
  CCDefs_iChangeSetID int NULL
  CCDefs_Checksum binary(20) NULL

## CCDetail - Credit Control Detail (CreditControlDetail)
Alias: Credit Control Detail | Freedom Name: CreditControlDetail | Record Identifier: 
Notes: Credit Control Detail
PK: DebtorLink
Columns (23):
  DebtorLink int NOT NULL PK
  TradeName varchar(35) NULL
  TypeofBus varchar(20) NULL
  MonthlyPur float NULL
  Granted bit NULL default (0)
  BankCode smallint NULL default (8)
  BankContact varchar(30) NULL
  BankDate smalldatetime NULL
  BankAmount float NULL
  BankRD bit NULL default (0)
  DateBusStart smalldatetime NULL
  LastCredGrant smalldatetime NULL
  LastCredDate smalldatetime NULL
  AuditorName varchar(30) NULL
  CCDetail_iBranchID int NULL
  CCDetail_dCreatedDate datetime NULL
  CCDetail_dModifiedDate datetime NULL
  CCDetail_iCreatedBranchID int NULL
  CCDetail_iModifiedBranchID int NULL
  CCDetail_iCreatedAgentID int NULL
  CCDetail_iModifiedAgentID int NULL
  CCDetail_iChangeSetID int NULL
  CCDetail_Checksum binary(20) NULL

## CliClass - Customer Group (CustomerGroup)
Alias: Customer Group | Freedom Name: CustomerGroup | Record Identifier: Code
Notes: Customer Group
PK: IdCliClass
Columns (25):
  IdCliClass int NOT NULL identity PK
  Code varchar(20) NULL
  Description varchar(100) NULL
  DiscMtrxRow int NULL
  dGroupTimeStamp datetime NULL
  iAccountsIDControlAcc int NULL
  iAccountsIDProfitAcc int NULL
  iAccountsIDLossAcc int NULL
  iTaxControlAccID int NULL
  iRevProfitAcc int NULL
  iRevLossAcc int NULL
  iProvForRevAcc int NULL
  iInvoiceDocProfileID int NULL
  iSOInvoiceDocProfileID int NULL
  iCreditNoteDocProfileID int NULL
  iJCInvoiceDocProfileID int NULL
  CliClass_iBranchID int NULL
  CliClass_dCreatedDate datetime NULL
  CliClass_dModifiedDate datetime NULL
  CliClass_iCreatedBranchID int NULL
  CliClass_iModifiedBranchID int NULL
  CliClass_iCreatedAgentID int NULL
  CliClass_iModifiedAgentID int NULL
  CliClass_iChangeSetID int NULL
  CliClass_Checksum binary(20) NULL

## CliDef - Customer Default (CustomerDefaults)
Alias: Customer Default | Freedom Name: CustomerDefaults | Record Identifier: 
Notes: Customer Default
PK: idCliDef
Columns (60):
  idCliDef int NOT NULL identity PK
  AutoYN varchar(1) NULL
  AutoLength int NULL
  AutoAlphaLength int NULL
  UpperAccNo varchar(1) NULL
  ForceProject bit NOT NULL default (0)
  DefaultTxDesc bit NOT NULL default (0)
  LatestVDPrice bit NOT NULL default (0)
  FilterStartLength int NULL default (0)
  iPDAgentID int NULL
  iPDPromptOpt int NULL
  dPDLastPrompt datetime NULL
  iTaxRateIdNoCharge int NULL
  iPEXTrCodeID int NULL
  iLEXTrCodeID int NULL
  fTaxPromptAmount float NULL
  iDelAddressCodeID1 int NULL
  iDelAddressCodeID2 int NULL
  bUseAllocStoredProc bit NOT NULL default (1)
  bInvTxCheckAccAfterChange bit NOT NULL default (0)
  bUseRounding bit NOT NULL default (0)
  bRoundPOSOnly bit NOT NULL default (0)
  fMinRoundDenom float NOT NULL
  iRoundToOpt int NULL
  iRoundingGLAccountID int NULL
  bForceRep bit NOT NULL default (0)
  iEFTSLayoutID int NOT NULL default (0)
  cEFTSPathOutFile varchar(100) NULL
  iDefaultTermID int NULL
  bUseInsurance bit NULL default (0)
  bForceAuthorisedBy bit NULL default (0)
  bForceClaimNumber bit NULL default (0)
  bForcePolicyNumber bit NULL default (0)
  bForceIncidentDate bit NULL default (0)
  bForceExcessAccName bit NULL default (0)
  bForceExcessAccCont1 bit NULL default (0)
  bForceExcessAccCont2 bit NULL default (0)
  iExcessCustomerId int NULL
  iExcessInvoiceTaxTypeId int NULL
  iRevProfitAcc int NULL
  iRevLossAcc int NULL
  iProvForRevAcc int NULL
  bApplyDiscountToACs bit NOT NULL default (0)
  bStatementRun bit NOT NULL default (0)
  bStatementsAutoNumbers bit NOT NULL default (0)
  iStatementPadLength int NULL
  bStatementUniqueNumber bit NOT NULL default (0)
  bForceStatementReference bit NOT NULL default (0)
  bMBIgnoreServiceonAllocs bit NOT NULL default (0)
  CliDef_iBranchID int NULL
  CliDef_dCreatedDate datetime NULL
  CliDef_dModifiedDate datetime NULL
  CliDef_iCreatedBranchID int NULL
  CliDef_iModifiedBranchID int NULL
  CliDef_iCreatedAgentID int NULL
  CliDef_iModifiedAgentID int NULL
  CliDef_iChangeSetID int NULL
  CliDef_Checksum binary(20) NULL
  cStatementPrefix varchar(20) NULL
  bUseQuickEntry bit NOT NULL default (0)

## Client
PK: DCLink
Columns (103):
  DCLink int NOT NULL identity PK
  Account varchar(20) NULL
  Name varchar(150) NULL
  Title varchar(5) NULL
  Init varchar(6) NULL
  Contact_Person varchar(30) NULL
  Physical1 varchar(40) NULL
  Physical2 varchar(40) NULL
  Physical3 varchar(40) NULL
  Physical4 varchar(40) NULL
  Physical5 varchar(40) NULL
  PhysicalPC varchar(15) NULL
  Addressee varchar(30) NULL
  Post1 varchar(40) NULL
  Post2 varchar(40) NULL
  Post3 varchar(40) NULL
  Post4 varchar(40) NULL
  Post5 varchar(40) NULL
  PostPC varchar(15) NULL
  Delivered_To varchar(30) NULL
  Telephone varchar(25) NULL
  Telephone2 varchar(25) NULL
  Fax1 varchar(25) NULL
  Fax2 varchar(25) NULL
  AccountTerms int NULL
  CT bit NOT NULL default (1)
  Tax_Number varchar(50) NULL
  Registration varchar(20) NULL
  Credit_Limit float NULL
  RepID int NULL
  Interest_Rate float NULL
  Discount float NULL
  On_Hold bit NOT NULL default (0)
  BFOpenType int NULL
  EMail varchar(200) NULL
  BankLink int NULL
  BranchCode varchar(30) NULL
  BankAccNum varchar(30) NULL
  BankAccType varchar(30) NULL
  AutoDisc float NULL
  DiscMtrxRow int NULL
  MainAccLink int NULL
  CashDebtor bit NOT NULL default (0)
  DCBalance float NULL
  CheckTerms bit NOT NULL default (0)
  UseEmail bit NOT NULL default (0)
  iIncidentTypeID int NULL
  iBusTypeID int NULL
  iBusClassID int NULL
  iCountryID int NULL
  iAgentID int NULL
  dTimeStamp datetime NULL
  cAccDescription varchar(80) NULL
  cWebPage varchar(50) NULL
  iClassID int NULL
  iAreasID int NULL
  cBankRefNr varchar(30) NULL
  iCurrencyID int NULL
  bStatPrint bit NOT NULL default (0)
  bStatEmail bit NOT NULL default (0)
  cStatEmailPass varchar(160) NULL
  bForCurAcc bit NOT NULL default (0)
  fForeignBalance float NULL
  bTaxPrompt bit NOT NULL default (1)
  iARPriceListNameID int NULL
  iSettlementTermsID int NOT NULL default (0)
  bSourceDocPrint bit NOT NULL default (1)
  bSourceDocEmail bit NOT NULL default (0)
  iEUCountryID int NOT NULL default (0)
  iDefTaxTypeID int NOT NULL default (0)
  bCODAccount bit NOT NULL default (0)
  iAgeingTermID int NULL
  bElecDocAcceptance bit NOT NULL default (0)
  iBankDetailType tinyint NULL
  cBankAccHolder varchar(30) NULL
  cIDNumber varchar(20) NULL
  cPassportNumber varchar(20) NULL
  bInsuranceCustomer bit NULL default (0)
  cBankCode varchar(15) NULL
  cSwiftCode varchar(11) NULL
  Client_iBranchID int NULL
  Client_dCreatedDate datetime NULL
  Client_dModifiedDate datetime NULL
  Client_iCreatedBranchID int NULL
  Client_iModifiedBranchID int NULL
  Client_iCreatedAgentID int NULL
  Client_iModifiedAgentID int NULL
  Client_iChangeSetID int NULL
  Client_Checksum binary(20) NULL
  iSPQueueID int NULL
  bCustomerZoneEnabled bit NOT NULL default (0)
  iTaxState int NOT NULL default (0)
  bOnlineToolsEnabled bit NOT NULL default (0)
  bTaxVerified bit NOT NULL default (0)
  dDateTaxVerified datetime NULL
  bBadDebtRelief bit NOT NULL default (0)
  bObjectToProcess bit NOT NULL default (0)
  bStatEmailPeople bit NOT NULL default (0)
  bSourceDocEmailPeople bit NOT NULL default (0)
  iTaxCountryID int NOT NULL default (0)
  ubARIsOrderNumRequired bit NULL default (0)
  ulARDepositRequired nvarchar(100) NULL
  ulARDormantActive nvarchar(100) NULL

## Contact - Customer Contact (CustomerContacts)
Alias: Customer Contact | Freedom Name: CustomerContacts | Record Identifier: 
Notes: Customer Contact
PK: AutoIdx
Columns (18):
  AutoIdx int NOT NULL identity PK
  DebtorLink int NULL
  Username varchar(50) NULL
  Person varchar(30) NULL
  Relationship varchar(25) NULL
  TextField text NULL
  Dated smalldatetime NULL
  Time timestamp NULL
  TypeOfCont varchar(25) NULL
  Contact_iBranchID int NULL
  Contact_dCreatedDate datetime NULL
  Contact_dModifiedDate datetime NULL
  Contact_iCreatedBranchID int NULL
  Contact_iModifiedBranchID int NULL
  Contact_iCreatedAgentID int NULL
  Contact_iModifiedAgentID int NULL
  Contact_iChangeSetID int NULL
  Contact_Checksum binary(20) NULL

## Cost - Cost (Cost)
Alias: Cost | Freedom Name: Cost | Record Identifier: 
PK: Autoidx
Columns (16):
  Autoidx int NOT NULL identity PK
  DebtorAccNo varchar(20) NULL
  UserName varchar(50) NULL
  Description varchar(25) NULL
  Dated smalldatetime NULL
  TypeofCost varchar(25) NULL
  Amount float NULL
  Cost_iBranchID int NULL
  Cost_dCreatedDate datetime NULL
  Cost_dModifiedDate datetime NULL
  Cost_iCreatedBranchID int NULL
  Cost_iModifiedBranchID int NULL
  Cost_iCreatedAgentID int NULL
  Cost_iModifiedAgentID int NULL
  Cost_iChangeSetID int NULL
  Cost_Checksum binary(20) NULL

## CostCntr - Asset Cost Centre (CostCentre)
Alias: Asset Cost Centre | Freedom Name: CostCentre | Record Identifier: 
Notes: Cost Centre
PK: Counter
Columns (15):
  Counter int NOT NULL identity PK
  CostCode varchar(20) NULL
  CostName varchar(40) NULL
  ActiveCenter varchar(1) NULL
  iDepartmentID int NULL
  iGLAccountID int NULL
  CostCntr_iBranchID int NULL
  CostCntr_dCreatedDate datetime NULL
  CostCntr_dModifiedDate datetime NULL
  CostCntr_iCreatedBranchID int NULL
  CostCntr_iModifiedBranchID int NULL
  CostCntr_iCreatedAgentID int NULL
  CostCntr_iModifiedAgentID int NULL
  CostCntr_iChangeSetID int NULL
  CostCntr_Checksum binary(20) NULL

## COSTMNT - Costmnt
Alias: Costmnt | Freedom Name:  | Record Identifier: 
Columns: none recorded yet (table seen in another Evolution database, not in the scripted one)

## CrDiscHd - Payables Discount Header (SupplierDiscountMatrixHeader)
Alias: Payables Discount Header | Freedom Name: SupplierDiscountMatrixHeader | Record Identifier: 
Notes: Payables Discount Header
PK: idCrDiscHd
Columns (13):
  idCrDiscHd int NOT NULL identity PK
  Place varchar(1) NOT NULL
  Position int NOT NULL
  Description varchar(30) NULL
  CrDiscHd_iBranchID int NULL
  CrDiscHd_dCreatedDate datetime NULL
  CrDiscHd_dModifiedDate datetime NULL
  CrDiscHd_iCreatedBranchID int NULL
  CrDiscHd_iModifiedBranchID int NULL
  CrDiscHd_iCreatedAgentID int NULL
  CrDiscHd_iModifiedAgentID int NULL
  CrDiscHd_iChangeSetID int NULL
  CrDiscHd_Checksum binary(20) NULL

## CrDiscMx - Payables Discount Matrix Detail (SupplierDiscountMatrix)
Alias: Payables Discount Matrix Detail | Freedom Name: SupplierDiscountMatrix | Record Identifier: 
Notes: Payables Discount Matrix Detail. The row and column positions indicate the matrix coordinates eg (1:2)
PK: idCrDiscMx
Columns (13):
  idCrDiscMx int NOT NULL identity PK
  XPos int NOT NULL
  YPos int NOT NULL
  Percentage float NULL
  CrDiscMx_iBranchID int NULL
  CrDiscMx_dCreatedDate datetime NULL
  CrDiscMx_dModifiedDate datetime NULL
  CrDiscMx_iCreatedBranchID int NULL
  CrDiscMx_iModifiedBranchID int NULL
  CrDiscMx_iCreatedAgentID int NULL
  CrDiscMx_iModifiedAgentID int NULL
  CrDiscMx_iChangeSetID int NULL
  CrDiscMx_Checksum binary(20) NULL

## CredApp - Credit Application (CreditControlApplication)
Alias: Credit Application | Freedom Name: CreditControlApplication | Record Identifier: 
Notes: Credit Application
PK: Autoidx
Columns (69):
  Autoidx int NOT NULL identity PK
  TypeofBus varchar(20) NULL
  AccountNo varchar(20) NULL
  CompanyName varchar(35) NULL
  RegistrationNo varchar(20) NULL
  TradeName varchar(35) NULL
  RegAdd1 varchar(30) NULL
  RegAdd2 varchar(30) NULL
  RegAdd3 varchar(30) NULL
  RegAdd4 varchar(30) NULL
  RegAdd5 varchar(30) NULL
  RegAddPC varchar(30) NULL
  DateBusStart smalldatetime NULL
  Physical1 varchar(30) NULL
  Physical2 varchar(30) NULL
  Physical3 varchar(30) NULL
  Physical4 varchar(30) NULL
  Physical5 varchar(30) NULL
  PhysicalPC varchar(30) NULL
  Postal1 varchar(30) NULL
  Postal2 varchar(30) NULL
  Postal3 varchar(30) NULL
  Postal4 varchar(30) NULL
  Postal5 varchar(30) NULL
  PostalPC varchar(30) NULL
  Telephone varchar(15) NULL
  Fax varchar(15) NULL
  ContactPerson varchar(30) NULL
  TaxNumber varchar(15) NULL
  BankLink int NULL
  BranchCode varchar(30) NULL
  BankAccNum varchar(30) NULL
  Terms smallint NULL default (0)
  CreditLimit float NULL
  MonthlyPur float NULL
  Score float NULL
  ScoreDesc varchar(50) NULL
  ScoreOutOf float NULL
  Granted smallint NULL default (0)
  DateGranted smalldatetime NULL default getdate()
  ApplicationDate smalldatetime NULL default getdate()
  AuditorName varchar(30) NULL
  LatestFinan bit NULL default (0)
  Telephone2 varchar(15) NULL
  BankContact varchar(30) NULL
  BankDate smalldatetime NULL
  BankAmount float NULL
  BankRD bit NULL default (0)
  BankCode smallint NULL
  OwnerList text NULL default '8'
  TradeList text NULL
  ScoreCard text NULL
  ScoreSummary text NULL
  Judgement bit NULL default (0)
  JudgementDet1 varchar(100) NULL
  JudgementDet2 varchar(100) NULL
  International bit NULL default (0)
  TypeofBus2 varchar(20) NULL
  JSEListDate smalldatetime NULL
  SameOwner bit NULL default (0)
  CredApp_iBranchID int NULL
  CredApp_dCreatedDate datetime NULL
  CredApp_dModifiedDate datetime NULL
  CredApp_iCreatedBranchID int NULL
  CredApp_iModifiedBranchID int NULL
  CredApp_iCreatedAgentID int NULL
  CredApp_iModifiedAgentID int NULL
  CredApp_iChangeSetID int NULL
  CredApp_Checksum binary(20) NULL

## CredMnt - Credit Control Reminder Type (CreditControlMaintenance)
Alias: Credit Control Reminder Type | Freedom Name: CreditControlMaintenance | Record Identifier: 
Notes: Credit Control Reminder Type
PK: Autoidx
Columns (12):
  Autoidx int NOT NULL identity PK
  Category varchar(1) NULL
  Description varchar(25) NULL
  CredMnt_iBranchID int NULL
  CredMnt_dCreatedDate datetime NULL
  CredMnt_dModifiedDate datetime NULL
  CredMnt_iCreatedBranchID int NULL
  CredMnt_iModifiedBranchID int NULL
  CredMnt_iCreatedAgentID int NULL
  CredMnt_iModifiedAgentID int NULL
  CredMnt_iChangeSetID int NULL
  CredMnt_Checksum binary(20) NULL

## Currency - Currency (Currency)
Alias: Currency | Freedom Name: Currency | Record Identifier: CurrencyCode
Notes: Currency
PK: CurrencyLink
Columns (18):
  CurrencyLink int NOT NULL identity PK
  CurrencyCode varchar(4) NULL
  Description varchar(30) NULL
  cCurrencySymbol varchar(4) NULL
  iOptions int NULL
  iPromptAgentID int NULL
  Currency_iBranchID int NULL
  Currency_dCreatedDate datetime NULL
  Currency_dModifiedDate datetime NULL
  Currency_iCreatedBranchID int NULL
  Currency_iModifiedBranchID int NULL
  Currency_iCreatedAgentID int NULL
  Currency_iModifiedAgentID int NULL
  Currency_iChangeSetID int NULL
  Currency_Checksum binary(20) NULL
  bAllowedOnRPOS bit NOT NULL default (0)
  fDefaultFloatAmount float NULL
  fDefaultCashPickupAmount float NULL

## CurrencyHist - Currency History (CurrencyHistory)
Alias: Currency History | Freedom Name: CurrencyHistory | Record Identifier: 
Notes: Currency History
PK: idCurrencyHist
Columns (14):
  idCurrencyHist int NOT NULL identity PK
  iCurrencyID int NULL
  dRateDate datetime NULL
  fBuyRate float NULL
  fSellRate float NULL
  CurrencyHist_iBranchID int NULL
  CurrencyHist_dCreatedDate datetime NULL
  CurrencyHist_dModifiedDate datetime NULL
  CurrencyHist_iCreatedBranchID int NULL
  CurrencyHist_iModifiedBranchID int NULL
  CurrencyHist_iCreatedAgentID int NULL
  CurrencyHist_iModifiedAgentID int NULL
  CurrencyHist_iChangeSetID int NULL
  CurrencyHist_Checksum binary(20) NULL

## CWRatio - Case Ware Setup (CaseWareRatio)
Alias: Case Ware Setup | Freedom Name: CaseWareRatio | Record Identifier: 
Notes: Case Ware Setup for General Ledger Accounts.
PK: idCwRatio
Columns (12):
  idCwRatio int NOT NULL identity PK
  CWNextMstAccount int NULL
  iCWRatioAccountType int NOT NULL default (0)
  CWRatio_iBranchID int NULL
  CWRatio_dCreatedDate datetime NULL
  CWRatio_dModifiedDate datetime NULL
  CWRatio_iCreatedBranchID int NULL
  CWRatio_iModifiedBranchID int NULL
  CWRatio_iCreatedAgentID int NULL
  CWRatio_iModifiedAgentID int NULL
  CWRatio_iChangeSetID int NULL
  CWRatio_Checksum binary(20) NULL

## DelTbl - Delivery Method (DeliveryMethod)
Alias: Delivery Method | Freedom Name: DeliveryMethod | Record Identifier: Method
Notes: Delivery Method
PK: Counter
Columns (14):
  Counter int NOT NULL identity PK
  Method varchar(35) NOT NULL
  Comment varchar(80) NULL
  bForDelivery bit NOT NULL default (1)
  dEffectiveDate datetime NULL
  DelTbl_iBranchID int NULL
  DelTbl_dCreatedDate datetime NULL
  DelTbl_dModifiedDate datetime NULL
  DelTbl_iCreatedBranchID int NULL
  DelTbl_iModifiedBranchID int NULL
  DelTbl_iCreatedAgentID int NULL
  DelTbl_iModifiedAgentID int NULL
  DelTbl_iChangeSetID int NULL
  DelTbl_Checksum binary(20) NULL

## Dept
PK: idDept
Columns (14):
  idDept int NOT NULL identity PK
  Name varchar(10) NULL
  Description varchar(40) NULL
  Info varchar(30) NULL
  dBrDeptTimeStamp datetime NULL
  Dept_iBranchID int NULL
  Dept_dCreatedDate datetime NULL
  Dept_dModifiedDate datetime NULL
  Dept_iCreatedBranchID int NULL
  Dept_iModifiedBranchID int NULL
  Dept_iCreatedAgentID int NULL
  Dept_iModifiedAgentID int NULL
  Dept_iChangeSetID int NULL
  Dept_Checksum binary(20) NULL

## DrDiscHd - Receivables Discount Header (CustomerDiscountMatrixHeader)
Alias: Receivables Discount Header | Freedom Name: CustomerDiscountMatrixHeader | Record Identifier: 
Notes: Receivables Discount Header
PK: idDrDiscHd
Columns (13):
  idDrDiscHd int NOT NULL identity PK
  Place varchar(1) NOT NULL
  Position int NOT NULL
  Description varchar(30) NULL
  DrDiscHd_iBranchID int NULL
  DrDiscHd_dCreatedDate datetime NULL
  DrDiscHd_dModifiedDate datetime NULL
  DrDiscHd_iCreatedBranchID int NULL
  DrDiscHd_iModifiedBranchID int NULL
  DrDiscHd_iCreatedAgentID int NULL
  DrDiscHd_iModifiedAgentID int NULL
  DrDiscHd_iChangeSetID int NULL
  DrDiscHd_Checksum binary(20) NULL

## DrDiscMx - Receivables Discount Matrix Detail (CustomerDiscountMatrix)
Alias: Receivables Discount Matrix Detail | Freedom Name: CustomerDiscountMatrix | Record Identifier: 
Notes: Receivables Discount Matrix Detail. The row and column positions indicate the matrix coordinates eg (1:2)
PK: idDrDiscMx
Columns (13):
  idDrDiscMx int NOT NULL identity PK
  XPos int NOT NULL
  YPos int NOT NULL
  Percentage float NULL
  DrDiscMx_iBranchID int NULL
  DrDiscMx_dCreatedDate datetime NULL
  DrDiscMx_dModifiedDate datetime NULL
  DrDiscMx_iCreatedBranchID int NULL
  DrDiscMx_iModifiedBranchID int NULL
  DrDiscMx_iCreatedAgentID int NULL
  DrDiscMx_iModifiedAgentID int NULL
  DrDiscMx_iChangeSetID int NULL
  DrDiscMx_Checksum binary(20) NULL

## Entities - ENTITIES (Entity)
Alias: ENTITIES | Freedom Name: Entity | Record Identifier: 
Notes: ENTITIES. Company Details. GL Defaults
PK: idEntities
Columns (82):
  idEntities int NOT NULL identity PK
  Name varchar(120) NULL
  PhAddress1 varchar(50) NULL
  PhAddress2 varchar(50) NULL
  PhAddress3 varchar(50) NULL
  POAddress1 varchar(50) NULL
  POAddress2 varchar(50) NULL
  POAddress3 varchar(50) NULL
  Telephone1 varchar(15) NULL
  Telephone2 varchar(15) NULL
  Fax varchar(15) NULL
  Version_Dont_Change float NULL
  StrSpare1 varchar(60) NULL
  ShrStrSpare1 varchar(4) NULL
  iNextAuditNumber int NULL
  BankName varchar(40) NULL
  BankAccount varchar(40) NULL
  BranchCode varchar(30) NULL
  EFTSCode varchar(4) NULL
  EFTSName varchar(40) NULL
  EFTSReference varchar(15) NULL
  TranLogActive varchar(1) NULL
  RegisterName varchar(50) NULL
  TradingName varchar(50) NULL
  Town varchar(40) NULL
  CompanyInfo text NULL
  IncorpForm varchar(25) NULL
  TypeofBus varchar(30) NULL
  ShowInactiveGL bit NOT NULL default (1)
  ShowInactiveProjects bit NOT NULL default (1)
  PhPostalCode varchar(15) NULL
  POPostalCode varchar(15) NULL
  PhState int NULL
  POState int NULL
  PhCountry int NULL
  POCountry int NULL
  ContactPerson varchar(50) NULL
  cWebSiteAddress varchar(100) NULL
  cGLSegmentSeparator varchar(10) NULL
  cBankRefNr varchar(30) NULL
  cAccountName varchar(50) NULL
  cBranchName varchar(30) NULL
  fAccountLimit float NULL
  iEUCountryID int NOT NULL default (0)
  bAPDocBudgetCheck bit NOT NULL default (0)
  bAPDocBudgetAnnual bit NOT NULL default (0)
  cHomeCurrency varchar(4) NULL
  bSingleEntityReporting bit NOT NULL default (1)
  iFilterStartLength int NOT NULL default (0)
  bUseIntegreatedEFT bit NULL
  cMerchantType varchar(4) NULL
  cMerchantID varchar(20) NULL
  cIPAddress varchar(20) NULL
  iPort int NULL
  dCommencementDate datetime NULL
  GatewayID int NULL
  bUseBins bit NOT NULL default (0)
  cBinIPAddress nvarchar(20) NULL
  iBinPort int NOT NULL default (12000)
  cBankCode varchar(15) NULL
  bAllowDCProcessing bit NOT NULL default (0)
  iDCBranchLoanAccountID int NULL
  Entities_iBranchID int NULL
  Entities_dCreatedDate datetime NULL
  Entities_dModifiedDate datetime NULL
  Entities_iCreatedBranchID int NULL
  Entities_iModifiedBranchID int NULL
  Entities_iCreatedAgentID int NULL
  Entities_iModifiedAgentID int NULL
  Entities_iChangeSetID int NULL
  Entities_Checksum binary(20) NULL
  bUsemSCOA bit NOT NULL default (0)
  iDefaultTaxState int NOT NULL default (0)
  cAGTCertNo varchar(10) NULL
  cSBFOrganisationID varchar(100) NULL
  cSBFAdminUser varchar(100) NULL
  cSBFSigningKey varchar(100) NULL
  cSBFCompanyID varchar(100) NULL
  cSBFCompanyName varchar(50) NULL
  bSBFKeyRequested bit NULL
  dSBFKeyRequestedValidUntil datetime NULL
  iExchangeRateDecimal smallint NOT NULL default (6)

## GLBranch - General Ledger Branch (GeneralLedgerBranch)
Alias: General Ledger Branch | Freedom Name: GeneralLedgerBranch | Record Identifier: 
PK: idGLBranch
Columns (14):
  idGLBranch int NOT NULL identity PK
  Name varchar(10) NULL
  Description varchar(40) NULL
  Info varchar(30) NULL
  dBrDeptTimeStamp datetime NULL
  GLBranch_iBranchID int NULL
  GLBranch_dCreatedDate datetime NULL
  GLBranch_dModifiedDate datetime NULL
  GLBranch_iCreatedBranchID int NULL
  GLBranch_iModifiedBranchID int NULL
  GLBranch_iCreatedAgentID int NULL
  GLBranch_iModifiedAgentID int NULL
  GLBranch_iChangeSetID int NULL
  GLBranch_Checksum binary(20) NULL

## GrpTbl - Inventory Group (StockGroup)
Alias: Inventory Group | Freedom Name: StockGroup | Record Identifier: StGroup
Notes: Inventory Group
PK: idGrpTbl
Columns (32):
  idGrpTbl int NOT NULL identity PK
  StGroup varchar(20) NOT NULL
  Description varchar(30) NULL
  SalesAccLink int NULL
  COSAccLink int NULL
  StockAccLink int NULL
  PurchasesAccLink int NULL
  SMtrxCol int NULL
  PMtrxCol int NULL
  dGrpTblTimeStamp datetime NULL
  bPromptSales bit NOT NULL default (0)
  bPromptCOS bit NOT NULL default (0)
  bPromptStock bit NOT NULL default (0)
  bPromptPurchases bit NOT NULL default (0)
  CostVarianceAccLink int NULL
  bPromptCostVariance bit NOT NULL default (0)
  StockAdjustAccLink int NULL
  bPromptStockAdjust bit NOT NULL default (0)
  iStockCostVarianceAccID int NOT NULL default (0)
  bPromptStockCostVariance bit NOT NULL default (0)
  iWIPAccID int NOT NULL default (0)
  bPromptWIP bit NOT NULL default (0)
  fGroupGPPercent real NULL
  GrpTbl_iBranchID int NULL
  GrpTbl_dCreatedDate datetime NULL
  GrpTbl_dModifiedDate datetime NULL
  GrpTbl_iCreatedBranchID int NULL
  GrpTbl_iModifiedBranchID int NULL
  GrpTbl_iCreatedAgentID int NULL
  GrpTbl_iModifiedAgentID int NULL
  GrpTbl_iChangeSetID int NULL
  GrpTbl_Checksum binary(20) NULL

## InvNum - Invoice (DocumentHeader)
Alias: Invoice | Freedom Name: DocumentHeader | Record Identifier: OrderNum
Notes: Invoice
PK: AutoIndex
Columns (178):
  AutoIndex bigint NOT NULL identity PK
  DocType int NULL
  DocVersion int NULL
  DocState int NULL
  DocFlag int NULL
  OrigDocID bigint NULL
  InvNumber varchar(50) NULL
  GrvNumber varchar(50) NULL
  GrvID bigint NULL
  AccountID int NULL
  Description varchar(40) NULL
  InvDate smalldatetime NULL
  OrderDate smalldatetime NULL
  DueDate smalldatetime NULL
  DeliveryDate smalldatetime NULL
  TaxInclusive bit NULL
  Email_Sent int NULL
  Address1 varchar(40) NULL
  Address2 varchar(40) NULL
  Address3 varchar(40) NULL
  Address4 varchar(40) NULL
  Address5 varchar(40) NULL
  Address6 varchar(40) NULL
  PAddress1 varchar(40) NULL
  PAddress2 varchar(40) NULL
  PAddress3 varchar(40) NULL
  PAddress4 varchar(40) NULL
  PAddress5 varchar(40) NULL
  PAddress6 varchar(40) NULL
  DelMethodID int NULL
  DocRepID int NULL
  OrderNum varchar(50) NULL
  DeliveryNote varchar(50) NULL
  InvDisc float NULL
  InvDiscReasonID int NULL
  Message1 varchar(255) NULL
  Message2 varchar(255) NULL
  Message3 varchar(255) NULL
  ProjectID int NULL
  TillID int NULL
  POSAmntTendered float NULL
  POSChange float NULL
  GrvSplitFixedCost bit NOT NULL default (0)
  GrvSplitFixedAmnt float NULL
  OrderStatusID int NULL
  OrderPriorityID int NULL
  ExtOrderNum varchar(50) NULL
  ForeignCurrencyID int NULL
  InvDiscAmnt float NULL
  InvDiscAmntEx float NULL
  InvTotExclDEx float NULL
  InvTotTaxDEx float NULL
  InvTotInclDEx float NULL
  InvTotExcl float NULL
  InvTotTax float NULL
  InvTotIncl float NULL
  OrdDiscAmnt float NULL
  OrdDiscAmntEx float NULL
  OrdTotExclDEx float NULL
  OrdTotTaxDEx float NULL
  OrdTotInclDEx float NULL
  OrdTotExcl float NULL
  OrdTotTax float NULL
  OrdTotIncl float NULL
  bUseFixedPrices bit NOT NULL default (0)
  iDocPrinted int NULL
  iINVNUMAgentID int NULL
  fExchangeRate float NULL
  fGrvSplitFixedAmntForeign float NULL
  fInvDiscAmntForeign float NULL
  fInvDiscAmntExForeign float NULL
  fInvTotExclDExForeign float NULL
  fInvTotTaxDExForeign float NULL
  fInvTotInclDExForeign float NULL
  fInvTotExclForeign float NULL
  fInvTotTaxForeign float NULL
  fInvTotInclForeign float NULL
  fOrdDiscAmntForeign float NULL
  fOrdDiscAmntExForeign float NULL
  fOrdTotExclDExForeign float NULL
  fOrdTotTaxDExForeign float NULL
  fOrdTotInclDExForeign float NULL
  fOrdTotExclForeign float NULL
  fOrdTotTaxForeign float NULL
  fOrdTotInclForeign float NULL
  cTaxNumber varchar(50) NULL
  cAccountName varchar(150) NULL
  iProspectID int NOT NULL default (0)
  iOpportunityID int NOT NULL default (0)
  InvTotRounding float NOT NULL default (0)
  OrdTotRounding float NOT NULL default (0)
  fInvTotForeignRounding float NOT NULL default (0)
  fOrdTotForeignRounding float NOT NULL default (0)
  bInvRounding bit NOT NULL default (0)
  iInvSettlementTermsID int NOT NULL default (0)
  cSettlementTermInvMsg varchar(255) NULL
  iOrderCancelReasonID int NOT NULL default (0)
  iLinkedDocID bigint NOT NULL default (0)
  bLinkedTemplate bit NOT NULL default (0)
  InvTotInclExRounding float NOT NULL default (0)
  OrdTotInclExRounding float NOT NULL default (0)
  fInvTotInclForeignExRounding float NOT NULL default (0)
  fOrdTotInclForeignExRounding float NOT NULL default (0)
  iEUNoTCID int NOT NULL default (0)
  iPOAuthStatus int NOT NULL default (0)
  iPOIncidentID int NOT NULL default (0)
  iSupervisorID int NULL
  iMergedDocID bigint NOT NULL default (0)
  iDocEmailed int NOT NULL default (0)
  fDepositAmountForeign float NULL
  fRefundAmount float NULL
  bTaxPerLine bit NOT NULL default (1)
  fDepositAmountTotal float NULL
  fDepositAmountUnallocated float NULL
  fDepositAmountNew float NULL
  fDepositAmountTotalForeign float NULL
  fDepositAmountUnallocatedForeign float NULL
  fRefundAmountForeign float NULL
  KeepAsideCollectionDate smalldatetime NULL
  KeepAsideExpiryDate smalldatetime NULL
  cContact varchar(50) NULL
  cTelephone varchar(25) NULL
  cFax varchar(25) NULL
  cEmail varchar(60) NULL
  cCellular varchar(25) NULL
  imgOrderSignature varbinary(max) NULL
  iInsuranceState int NOT NULL default (0)
  cAuthorisedBy varchar(50) NULL
  cClaimNumber varchar(40) NULL
  cPolicyNumber varchar(40) NULL
  dIncidentDate datetime NULL
  cExcessAccName varchar(150) NULL
  cExcessAccCont1 varchar(50) NULL
  cExcessAccCont2 varchar(50) NULL
  fExcessAmt float NULL
  fExcessPct float NULL
  fExcessExclusive float NOT NULL default (0)
  fExcessInclusive float NOT NULL default (0)
  fExcessTax float NOT NULL default (0)
  fAddChargeExclusive float NOT NULL default (0)
  fAddChargeTax float NOT NULL default (0)
  fAddChargeInclusive float NOT NULL default (0)
  fAddChargeExclusiveForeign float NOT NULL default (0)
  fAddChargeTaxForeign float NOT NULL default (0)
  fAddChargeInclusiveForeign float NOT NULL default (0)
  fOrdAddChargeExclusive float NOT NULL default (0)
  fOrdAddChargeTax float NOT NULL default (0)
  fOrdAddChargeInclusive float NOT NULL default (0)
  fOrdAddChargeExclusiveForeign float NOT NULL default (0)
  fOrdAddChargeTaxForeign float NOT NULL default (0)
  fOrdAddChargeInclusiveForeign float NOT NULL default (0)
  iInvoiceSplitDocID bigint NOT NULL default (0)
  cGIVNumber varchar(50) NULL
  bIsDCOrder bit NOT NULL default (0)
  iDCBranchID int NULL
  iSalesBranchID int NULL
  InvNum_iBranchID int NULL
  InvNum_dCreatedDate datetime NULL
  InvNum_dModifiedDate datetime NULL
  InvNum_iCreatedBranchID int NULL
  InvNum_iModifiedBranchID int NULL
  InvNum_iCreatedAgentID int NULL
  InvNum_iModifiedAgentID int NULL
  InvNum_iChangeSetID int NULL
  InvNum_Checksum binary(20) NULL
  bIDFProccessed bit NOT NULL default (0)
  iImportDeclarationID int NULL default (0)
  bSBSI bit NOT NULL default (0)
  cPermitNumber varchar(20) NOT NULL default ''
  iStateID int NULL
  iCancellationReasonID int NULL
  cDPOrdServiceTaskNo varchar(50) NULL
  cDSOrdServiceTaskNo varchar(50) NULL
  cDCrnServiceTaskNo varchar(50) NULL
  cDSMExtOrderNum varchar(50) NULL
  cHash varchar(200) NULL
  cRevenueIntegration varchar(200) NULL
  cQuoteNum varchar(50) NULL

## JobDef - Job Costing Default (JobCostingDefaults)
Alias: Job Costing Default | Freedom Name: JobCostingDefaults | Record Identifier: 
Notes: Job Costing Default
PK: idJobDef
Columns (64):
  AutoNumber bit NOT NULL default (0)
  CurrentNumber varchar(15) NULL
  WIPM1Link int NULL
  RecoveryM1Link int NULL
  TaxM1Link int NULL
  StockM1Link int NULL
  CreditorM1Link int NULL
  SalesM1Link int NULL
  COSM1Link int NULL
  DebtorM1Link int NULL
  WIPM2Link int NULL
  RecoveryM2Link int NULL
  TaxM2Link int NULL
  StockM2Link int NULL
  CreditorM2Link int NULL
  SalesM2Link int NULL
  COSM2Link int NULL
  DebtorM2Link int NULL
  POSTINGM int NULL
  AutoTemplate bit NOT NULL default (0)
  NextTemplate varchar(15) NULL
  iCCDebitAccount int NULL
  iCCCreditAccount int NULL
  iJobPadTo int NULL
  cJobPrefix varchar(25) NULL
  iTemplatePadTo int NULL
  cTemplatePrefix varchar(25) NULL
  iJobTxTpIDGRV int NULL
  iJobTxTpIDGLOC int NULL
  bAutoJCQuote bit NULL
  cNextJCQuote varchar(15) NULL
  iJCQuotePadTo int NULL
  cJCQuotePrefix varchar(25) NULL
  bAutoJCDelNote bit NULL
  cNextJCDelNote varchar(15) NULL
  iJCDelNotePadTo int NULL
  cJCDelNotePrefix varchar(25) NULL
  bPrintAllLines bit NOT NULL default (1)
  iJobTxTpIDGrvGL int NULL
  bPostGRVCost bit NOT NULL default (0)
  bAPAllowSettlementTerms bit NOT NULL default (0)
  bForceProject bit NOT NULL default (0)
  bForceRep bit NOT NULL default (0)
  bForceExtOrderNum bit NOT NULL default (0)
  bUniqueJobNum bit NULL
  bUniqueQuoteNum bit NULL
  bUniqueTemplateNum bit NULL
  bUniqueDeliveryNoteNum bit NULL
  idJobDef int NOT NULL identity PK
  bStrictWIP bit NOT NULL default (1)
  iFilterStartLength int NULL
  JobDef_iBranchID int NULL
  JobDef_dCreatedDate datetime NULL
  JobDef_dModifiedDate datetime NULL
  JobDef_iCreatedBranchID int NULL
  JobDef_iModifiedBranchID int NULL
  JobDef_iCreatedAgentID int NULL
  JobDef_iModifiedAgentID int NULL
  JobDef_iChangeSetID int NULL
  JobDef_Checksum binary(20) NULL
  bUpdateBudgets bit NOT NULL default (1)
  iWIPVarianceAccount int NULL default (0)
  bPostWIPVarAmount bit NOT NULL default (1)
  bShowWIPMessage bit NOT NULL default (1)

## JobNum - Job Invoice (JobCostingHeader)
Alias: Job Invoice | Freedom Name: JobCostingHeader | Record Identifier: 
Notes: Job Invoice. Master file for Invoices and Quotes processed
PK: AutoIndex
Columns (63):
  AutoIndex int NOT NULL identity PK
  InvNumber varchar(50) NULL
  Description varchar(40) NULL
  InvDate smalldatetime NULL
  Email_Sent int NULL
  AccountID int NULL
  iJCMasterID int NULL
  TaxInclusive bit NULL
  Address1 varchar(40) NULL
  Address2 varchar(40) NULL
  Address3 varchar(40) NULL
  Address4 varchar(40) NULL
  Address5 varchar(40) NULL
  Address6 varchar(40) NULL
  PAddress1 varchar(40) NULL
  PAddress2 varchar(40) NULL
  PAddress3 varchar(40) NULL
  PAddress4 varchar(40) NULL
  PAddress5 varchar(40) NULL
  PAddress6 varchar(40) NULL
  iDelMethodID int NULL
  iRepID int NULL
  OrderNumber varchar(50) NULL
  DeliveryNote varchar(50) NULL
  InvDisc float NULL
  Message1 varchar(255) NULL
  Message2 varchar(255) NULL
  Message3 varchar(255) NULL
  Narration text NULL
  iProjectID int NULL
  InvDiscAmnt float NULL
  InvTotExclDEx float NULL
  InvTotTaxDEx float NULL
  InvTotInclDEx float NULL
  InvTotExcl float NULL
  InvTotTax float NULL
  InvTotIncl float NULL
  DocType int NULL
  bSummaryInv bit NOT NULL default (0)
  cExtOrderNumber varchar(50) NULL
  iDocPrinted int NULL
  InvDiscAmntForeign float NULL
  InvTotExclDExForeign float NULL
  InvTotTaxDExForeign float NULL
  InvTotInclDExForeign float NULL
  InvTotExclForeign float NULL
  InvTotTaxForeign float NULL
  InvTotInclForeign float NULL
  cTaxNumber varchar(15) NULL
  cAccountName varchar(150) NULL
  iInvSettlementTermsID int NOT NULL default (0)
  bTaxPerLine bit NOT NULL default (1)
  JobNum_iBranchID int NULL
  JobNum_dCreatedDate datetime NULL
  JobNum_dModifiedDate datetime NULL
  JobNum_iCreatedBranchID int NULL
  JobNum_iModifiedBranchID int NULL
  JobNum_iCreatedAgentID int NULL
  JobNum_iModifiedAgentID int NULL
  JobNum_iChangeSetID int NULL
  JobNum_Checksum binary(20) NULL
  cHash varchar(200) NULL
  cRevenueIntegration varchar(200) NULL

## JobStock (JobCostingStock)
Alias:  | Freedom Name: JobCostingStock | Record Identifier: 
Notes: Job Stock Issue
PK: none
Columns (47):
  JobStock int NOT NULL identity
  iJobStockGroupID int NULL
  StockItemLink int NULL
  UOM varchar(10) NULL
  QtyIssued float NULL
  QtyIssuedInvoiced float NULL
  QtyIssuedToInvoice float NULL
  QtyIssuedAvailable float NULL
  QtyIssuedAdjusted float NOT NULL default (0)
  iUnitsOfMeasureStockingID int NULL
  iUnitsOfMeasureCategoryID int NULL
  iUnitsOfMeasureID int NULL
  CostPrice float NULL
  Discount float NULL
  SellPriceExcl float NULL
  SellPriceIncl float NULL
  TaxRate float NULL
  LineTotExcl float NULL
  LineTotIncl float NULL
  LineTotTax float NULL
  LineTotExclToInvoice float NULL
  LineTotInclToInvoice float NULL
  LineTotTaxToInvoice float NULL
  LineTotCost float NULL
  WarehouseID int NULL
  iSerialNumberGroupID int NULL
  ExchangeRate float NULL
  SellPriceExclForeign float NULL
  SellPriceInclForeign float NULL
  LineTotExclForeign float NULL
  LineTotInclForeign float NULL
  LineTotTaxForeign float NULL
  LineTotExclForeignToInvoice float NULL
  LineTotInclForeignToInvoice float NULL
  LineTotTaxForeignToInvoice float NULL
  cDescription varchar(100) NULL
  JobStock_iBranchID int NULL
  JobStock_dCreatedDate datetime NULL
  JobStock_dModifiedDate datetime NULL
  JobStock_iCreatedBranchID int NULL
  JobStock_iModifiedBranchID int NULL
  JobStock_iCreatedAgentID int NULL
  JobStock_iModifiedAgentID int NULL
  JobStock_iChangeSetID int NULL
  JobStock_Checksum binary(20) NULL
  iStockBinLocationID int NOT NULL default (0)
  iLotID int NULL default (0)

## JobTxTp - Job Costing Transaction Type (JobCostingTransactionCodes)
Alias: Job Costing Transaction Type | Freedom Name: JobCostingTransactionCodes | Record Identifier: 
Notes: Job Costing Transaction Type
PK: idJobTxTp
Columns (36):
  idJobTxTp int NOT NULL identity PK
  TxType varchar(20) NOT NULL
  Description varchar(40) NULL
  Source int NULL
  OverheadPercent float NULL
  M1WIPLink int NULL
  M1RecoveryLink int NULL
  M1StockLink int NULL
  M1CreditorLink int NULL
  M1TaxLink int NULL
  M1SalesLink int NULL
  M1COSLink int NULL
  M1DebtorLink int NULL
  M2WIPLink int NULL
  M2RecoveryLink int NULL
  M2StockLink int NULL
  M2CreditorLink int NULL
  M2TaxLink int NULL
  M2SalesLink int NULL
  M2COSLink int NULL
  M2DebtorLink int NULL
  iTaxTypeIDInv int NULL
  iTaxTypeIDGrv int NULL
  bSalesFilter bit NOT NULL default (1)
  iSellingTaxGroupID int NULL
  iCostTaxGroupID int NULL
  JobTxTp_iBranchID int NULL
  JobTxTp_dCreatedDate datetime NULL
  JobTxTp_dModifiedDate datetime NULL
  JobTxTp_iCreatedBranchID int NULL
  JobTxTp_iModifiedBranchID int NULL
  JobTxTp_iCreatedAgentID int NULL
  JobTxTp_iModifiedAgentID int NULL
  JobTxTp_iChangeSetID int NULL
  JobTxTp_Checksum binary(20) NULL
  bPromptCosAcc bit NOT NULL default (0)

## MastOffs - Master Office (MasterOffice)
Alias: Master Office | Freedom Name: MasterOffice | Record Identifier: 
Notes: Master Offices Listing
PK: idMastOffs
Columns (12):
  idMastOffs int NOT NULL identity PK
  Description varchar(30) NOT NULL
  Address text NULL
  MastOffs_iBranchID int NULL
  MastOffs_dCreatedDate datetime NULL
  MastOffs_dModifiedDate datetime NULL
  MastOffs_iCreatedBranchID int NULL
  MastOffs_iModifiedBranchID int NULL
  MastOffs_iCreatedAgentID int NULL
  MastOffs_iModifiedAgentID int NULL
  MastOffs_iChangeSetID int NULL
  MastOffs_Checksum binary(20) NULL

## OrdersDf
PK: DefaultCounter
Columns (59):
  DefaultCounter int NOT NULL identity PK
  iModule int NOT NULL default (0)
  OrderPrefix varchar(25) NULL
  DN_POPrefix varchar(25) NULL
  AutoDNNo bit NOT NULL default (0)
  NextDNNo int NULL
  DNoPadLgth int NULL
  AutoCustNo bit NOT NULL default (0)
  NextCustNo int NULL
  CNoPadLgth int NULL
  ReserveStock bit NOT NULL default (0)
  TrCodeID int NULL
  PrintAllLines bit NOT NULL default (0)
  TemplatePrefix varchar(25) NULL
  NextTemplateNo int NULL
  PadTemplateLngth int NULL
  AutoTemplate bit NULL
  AutoQuote bit NULL
  QuotePrefix varchar(25) NULL
  NextQuoteNo int NULL
  PadQuoteLngth int NULL
  bInvGrvSplit bit NULL
  iGrvTrCodeID int NULL
  iSInvGLVarAccID int NULL
  bUseNewCurrencyRate bit NOT NULL default (0)
  iPOAuthType int NOT NULL default (0)
  iPOIncidentTypeID int NULL
  bPOExclusive bit NOT NULL default (1)
  fPOLimit float NULL
  bForceProject bit NOT NULL default (0)
  bForceRep bit NOT NULL default (0)
  bArchiveQuotes bit NOT NULL default (0)
  bForceExtOrderNum bit NOT NULL default (0)
  bForceSupplierInvNumber bit NOT NULL default (0)
  bUniqueOrderNum bit NULL
  bUniqueQuoteNum bit NULL
  bUniqueTemplateNum bit NULL
  bUniqueDeliveryNoteNum bit NULL
  bAllowPOSTender bit NOT NULL default (0)
  bUseDeposits bit NOT NULL default (0)
  bForceDeposits bit NOT NULL default (0)
  iDepTrCodeID int NULL
  fMinDepositPerc float NULL
  bPrintUnprocessedSOPS bit NOT NULL default (0)
  bPrintProcessedSOPS bit NOT NULL default (1)
  bForceDelivery bit NOT NULL default (0)
  bReserveSOLinkedPO bit NOT NULL default (0)
  bSOInvIssueSplit bit NOT NULL default (0)
  iSOInvIssueSplitAccrualAccID int NOT NULL default (0)
  OrdersDf_iBranchID int NULL
  OrdersDf_dCreatedDate datetime NULL
  OrdersDf_dModifiedDate datetime NULL
  OrdersDf_iCreatedBranchID int NULL
  OrdersDf_iModifiedBranchID int NULL
  OrdersDf_iCreatedAgentID int NULL
  OrdersDf_iModifiedAgentID int NULL
  OrdersDf_iChangeSetID int NULL
  OrdersDf_Checksum binary(20) NULL
  bUseDeliveryManagement bit NOT NULL default (0)

## OrdersSt - Order Status (OrdersStatus)
Alias: Order Status | Freedom Name: OrdersStatus | Record Identifier: StatusDescrip
Notes: Order Status
PK: StatusCounter
Columns (11):
  StatusCounter int NOT NULL identity PK
  StatusDescrip varchar(35) NULL
  OrdersSt_iBranchID int NULL
  OrdersSt_dCreatedDate datetime NULL
  OrdersSt_dModifiedDate datetime NULL
  OrdersSt_iCreatedBranchID int NULL
  OrdersSt_iModifiedBranchID int NULL
  OrdersSt_iCreatedAgentID int NULL
  OrdersSt_iModifiedAgentID int NULL
  OrdersSt_iChangeSetID int NULL
  OrdersSt_Checksum binary(20) NULL

## PckTbl - Inventory Pack (PackCodes)
Alias: Inventory Pack | Freedom Name: PackCodes | Record Identifier: Code
Notes: Inventory Pack
PK: idPckTbl
Columns (13):
  idPckTbl int NOT NULL identity PK
  Code varchar(5) NOT NULL
  PackSize float NULL
  Description varchar(30) NULL
  PckTbl_iBranchID int NULL
  PckTbl_dCreatedDate datetime NULL
  PckTbl_dModifiedDate datetime NULL
  PckTbl_iCreatedBranchID int NULL
  PckTbl_iModifiedBranchID int NULL
  PckTbl_iCreatedAgentID int NULL
  PckTbl_iModifiedAgentID int NULL
  PckTbl_iChangeSetID int NULL
  PckTbl_Checksum binary(20) NULL

## PeriodPermissions - Period Permissions
Alias: Period Permissions | Freedom Name:  | Record Identifier: 
PK: idPeriodPermissions
Columns (14):
  idPeriodPermissions int NOT NULL identity PK
  Period int NULL
  AgentType int NULL
  AgentID int NULL
  Allow bit NOT NULL default (0)
  PeriodPermissions_iBranchID int NULL
  PeriodPermissions_dCreatedDate datetime NULL
  PeriodPermissions_dModifiedDate datetime NULL
  PeriodPermissions_iCreatedBranchID int NULL
  PeriodPermissions_iModifiedBranchID int NULL
  PeriodPermissions_iCreatedAgentID int NULL
  PeriodPermissions_iModifiedAgentID int NULL
  PeriodPermissions_iChangeSetID int NULL
  PeriodPermissions_Checksum binary(20) NULL

## PinnedItems (PinnedItem)
Alias:  | Freedom Name: PinnedItem | Record Identifier: 
Notes: Central Search. Pin Items to reuse / saved searches
PK: PinnedItemID
Columns (8):
  PinnedItemID int NOT NULL identity PK
  Name nvarchar(50) NOT NULL
  Description nvarchar(160) NULL
  BackGround nvarchar(50) NULL
  Created datetime NOT NULL
  Modified datetime NOT NULL
  AgentID int NOT NULL
  ApplicationName nvarchar(50) NOT NULL

## PosDefs - POS Default (PointOfSaleDefaults)
Alias: POS Default | Freedom Name: PointOfSaleDefaults | Record Identifier: 
Notes: POS Default
PK: IDPOSDefs
Columns (43):
  IDPOSDefs int NOT NULL identity PK
  AllowLineDisc varchar(1) NULL
  Max_LDisc float NULL
  Max_Disc float NULL
  RecPref varchar(25) NULL
  RecNum varchar(15) NULL
  iRecPad int NULL
  bAutoRecNum bit NULL
  PoleLine1 varchar(20) NULL
  PoleLine2 varchar(20) NULL
  AllocatePM bit NOT NULL default (0)
  iTrCodesIDSTSale int NULL
  iTrCodesIDSTReturn int NULL
  iTrCodesIDPOSFloat int NULL
  iTrCodesIDPOSBanking int NULL
  iTrCodesIDPOSPettyCash int NULL
  iTrCodesIDPOSShortage int NULL
  iTrCodesIDPOSExcess int NULL
  iTrCodesIDARReceipt int NULL
  iTrCodesIDAPPayment int NULL
  iTenderIDDefFloat int NULL
  iTenderIDDefBanking int NULL
  iTenderIDDefPettyCash int NULL
  iTenderIDDefShortage int NULL
  iTenderIDDefExcess int NULL
  iTenderIDDefReceipt int NULL
  iTenderIDDefPayment int NULL
  iTenderIDDefCash int NULL default (1)
  bAutoAllocCashPM bit NOT NULL default (0)
  iTrCodesIDARDepositRefund int NULL
  iTenderIDDefDepositRefund int NULL
  iTrCodesIDARRefund int NULL
  iTenderIDDefRefund int NULL
  bUseDocumentRoundingOnTender bit NULL default (0)
  PosDefs_iBranchID int NULL
  PosDefs_dCreatedDate datetime NULL
  PosDefs_dModifiedDate datetime NULL
  PosDefs_iCreatedBranchID int NULL
  PosDefs_iModifiedBranchID int NULL
  PosDefs_iCreatedAgentID int NULL
  PosDefs_iModifiedAgentID int NULL
  PosDefs_iChangeSetID int NULL
  PosDefs_Checksum binary(20) NULL

## PostAP - Supplier Transaction (PostAccountsPayable)
Alias: Supplier Transaction | Freedom Name: PostAccountsPayable | Record Identifier: 
Notes: Supplier Transaction Listing. Records in this table should always have a link to the POSTGL table.
PK: AutoIdx
Columns (54):
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
  Outstanding float NULL
  fForeignOutstanding float NULL
  cAllocs text NULL
  InvNumKey bigint NULL
  CRCCheck float NULL
  DTStamp datetime NULL
  UserName varchar(50) NULL
  iTaxPeriodID int NULL
  cReference2 varchar(50) NULL
  iAge int NULL
  dDateAged datetime NULL
  iPostSettlementTermsID int NOT NULL default (0)
  iTxBranchID int NULL
  bPBTPaid bit NOT NULL default (0)
  iGLTaxAccountID int NULL
  bTxOnHold bit NOT NULL default (0)
  PostAP_iBranchID int NULL
  PostAP_dCreatedDate datetime NULL
  PostAP_dModifiedDate datetime NULL
  PostAP_iCreatedBranchID int NULL
  PostAP_iModifiedBranchID int NULL
  PostAP_iCreatedAgentID int NULL
  PostAP_iModifiedAgentID int NULL
  PostAP_iChangeSetID int NULL
  PostAP_Checksum binary(20) NULL
  SagePayExtra1 varchar(max) NULL
  SagePayExtra2 varchar(max) NULL
  SagePayExtra3 varchar(max) NULL
  iTaxBadDebtState int NOT NULL default (0)
  bReverseChargeApplied bit NOT NULL default (0)
  bReverseChargeCustoms bit NOT NULL default (0)
  cReverseChargeAuditNr varchar(50) NULL
  cHash varchar(200) NULL
  iKeyVersion int NULL

## PostAR - Customer Transaction (PostAccountsReceivable)
Alias: Customer Transaction | Freedom Name: PostAccountsReceivable | Record Identifier: 
Notes: Customer Transaction. Records in this table should always have a link to the POSTGL table.
PK: AutoIdx
Columns (61):
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
  Outstanding float NULL
  fForeignOutstanding float NULL
  cAllocs text NULL
  InvNumKey bigint NULL
  RepID int NULL
  LinkAccCode int NULL
  TillID int NULL
  CRCCheck float NULL
  DTStamp datetime NULL
  UserName varchar(50) NULL
  iTaxPeriodID int NULL
  cReference2 varchar(50) NULL
  fJCRepCost float NULL
  iAge int NULL
  dDateAged datetime NULL
  iPostSettlementTermsID int NOT NULL default (0)
  iTxBranchID int NULL
  iMBPropertyID int NOT NULL default (0)
  iMBPortionID int NOT NULL default (0)
  iMBServiceID int NOT NULL default (0)
  iMBMeterID int NOT NULL default (0)
  iMBPropertyPortionServiceID int NOT NULL default (0)
  bPBTPaid bit NOT NULL default (0)
  iGLTaxAccountID int NULL
  iTransactionType int NOT NULL default (0)
  PostAR_iBranchID int NULL
  PostAR_dCreatedDate datetime NULL
  PostAR_dModifiedDate datetime NULL
  PostAR_iCreatedBranchID int NULL
  PostAR_iModifiedBranchID int NULL
  PostAR_iCreatedAgentID int NULL
  PostAR_iModifiedAgentID int NULL
  PostAR_iChangeSetID int NULL
  PostAR_Checksum binary(20) NULL
  SagePayExtra1 varchar(max) NULL
  SagePayExtra2 varchar(max) NULL
  SagePayExtra3 varchar(max) NULL
  iTaxBadDebtState int NOT NULL default (0)
  iMajorIndustryCodeID int NULL default (0)
  cHash varchar(200) NULL
  iKeyVersion int NULL

## PostGL - General Ledger Transaction (PostGeneralLedger)
Alias: General Ledger Transaction | Freedom Name: PostGeneralLedger | Record Identifier: 
Notes: General Ledger Transaction. NOTE: The amount of records written to this table, per transaction, will equal the amount of accounts that make up the transaction code. As an example, INV uses three accounts, is linked to IS, which uses two accounts, thus, the records representing this transaction in the POSTGL table will be a total of 5 - the transaction debit and credit entries for these 5 records will also balance.
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
  bPrintCheque bit NOT NULL default (0)
  cReference2 varchar(50) NULL
  RepID int NULL
  fJCRepCost float NULL
  iMFPID int NULL
  bIsJCDocLine bit NOT NULL default (0)
  bIsSTGLDocLine bit NOT NULL default (0)
  iInvLineID bigint NOT NULL default (0)
  iTxBranchID int NULL
  cBankRef varchar(20) NULL
  bPBTPaid bit NOT NULL default (0)
  iGLTaxAccountID int NULL
  bReconciled bit NOT NULL default (0)
  PostGL_iBranchID int NULL
  PostGL_dCreatedDate datetime NULL
  PostGL_dModifiedDate datetime NULL
  PostGL_iCreatedBranchID int NULL
  PostGL_iModifiedBranchID int NULL
  PostGL_iCreatedAgentID int NULL
  PostGL_iModifiedAgentID int NULL
  PostGL_iChangeSetID int NULL
  PostGL_Checksum binary(20) NULL
  iImportDeclarationID int NULL default (0)
  ucIDSOrdTxCMTransporter varchar(30) NULL
  xAttribute xml NULL
  iMajorIndustryCodeID int NULL default (0)
  cHash varchar(200) NULL
  iKeyVersion int NULL
  uiIDSOrdTxCMQTP int NULL
  ufIDSOrdTxCMQTP float NULL

## PostST
PK: AutoIdx
Columns (75):
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
  Quantity float NULL
  Cost float NULL
  WarehouseID int NULL
  JobCodeLink int NULL
  iJobLineID bigint NOT NULL default (0)
  TillID int NULL
  DrCrAccount int NULL
  CRCCheck float NULL
  DTStamp datetime NULL
  UserName varchar(50) NULL
  iTaxPeriodID int NULL
  InvNumKey bigint NULL
  cReference2 varchar(50) NULL
  RepID int NULL
  bChargeCom bit NOT NULL default (1)
  iMFPID int NULL
  iLotID int NULL
  iMFPLineID bigint NOT NULL default (0)
  fUnManufactured float NOT NULL default (0)
  fAdditionalCost float NOT NULL default (0)
  iPostEUNoTCID int NOT NULL default (0)
  iGLAccountID int NOT NULL default (0)
  iTxBranchID int NULL
  fJCWIPQuantity float NOT NULL default (0)
  fMFPWIPQuantity float NOT NULL default (0)
  QuantityR float NULL
  fQuantityInvoiced float NOT NULL default (0)
  PostST_iBranchID int NULL
  PostST_dCreatedDate datetime NULL
  PostST_dModifiedDate datetime NULL
  PostST_iCreatedBranchID int NULL
  PostST_iModifiedBranchID int NULL
  PostST_iCreatedAgentID int NULL
  PostST_iModifiedAgentID int NULL
  PostST_iChangeSetID int NULL
  PostST_Checksum binary(20) NULL
  SagePayExtra1 varchar(max) NULL
  SagePayExtra2 varchar(max) NULL
  SagePayExtra3 varchar(max) NULL
  iMajorIndustryCodeID int NULL default (0)
  ucIDCrnTxSTRollNumber varchar(30) NULL
  ucIDInvTxSTRollNumber varchar(30) NULL
  ucIDRtsTxSTRollNumber varchar(30) NULL
  ucIDSOrdTxSTRollNumber varchar(30) NULL
  ucIDSOrdTxSTSCF varchar(30) NULL
  ucIDSOrdTxSTNoofitems varchar(30) NULL
  ucIDGrvTxSTscfno varchar(30) NULL
  ucIDPOrdTxSTscfno varchar(30) NULL
  ucIDSOrdTxCMTransporter varchar(30) NULL
  iBinLocationID int NOT NULL default (0)
  xAttribute xml NULL
  uiIDSOrdTxCMQTP int NULL
  ufIDSOrdTxCMQTP float NULL
  ubIDSOrdTxSTDateChanged bit NULL
  udIDSOrdTxSTRequiredDate datetime NULL

## PrintGrp - Inventory Document Print Group (PrintGroup)
Alias: Inventory Document Print Group | Freedom Name: PrintGroup | Record Identifier: 
Notes: Inventory Document Print Group
PK: AutoIdx
Columns (13):
  AutoIdx int NOT NULL identity PK
  Descrip varchar(100) NULL
  GrpList text NULL
  DocType int NULL
  PrintGrp_iBranchID int NULL
  PrintGrp_dCreatedDate datetime NULL
  PrintGrp_dModifiedDate datetime NULL
  PrintGrp_iCreatedBranchID int NULL
  PrintGrp_iModifiedBranchID int NULL
  PrintGrp_iCreatedAgentID int NULL
  PrintGrp_iModifiedAgentID int NULL
  PrintGrp_iChangeSetID int NULL
  PrintGrp_Checksum binary(20) NULL

## Project
PK: ProjectLink
Columns (17):
  ProjectLink int NOT NULL identity PK
  ProjectCode varchar(21) NULL
  ProjectName varchar(50) NULL
  ActiveProject bit NOT NULL default (0)
  ProjectDescription varchar(60) NULL
  MasterSubProject varchar(41) NULL
  ProjectLevel int NULL
  SubProjectOfLink int NULL
  Project_iBranchID int NULL
  Project_dCreatedDate datetime NULL
  Project_dModifiedDate datetime NULL
  Project_iCreatedBranchID int NULL
  Project_iModifiedBranchID int NULL
  Project_iCreatedAgentID int NULL
  Project_iModifiedAgentID int NULL
  Project_iChangeSetID int NULL
  Project_Checksum binary(20) NULL

## RecentItems - Recent Items (RecentItem)
Alias: Recent Items | Freedom Name: RecentItem | Record Identifier: 
Notes: Central Search. Stores the last few searches per Agent
PK: RecentItemID
Columns (5):
  RecentItemID int NOT NULL identity PK
  Name nvarchar(50) NOT NULL
  Created datetime NOT NULL
  AgentID int NOT NULL
  ApplicationName nvarchar(50) NOT NULL

## RecurRC
PK: AutoIdx
Columns (19):
  AutoIdx int NOT NULL identity PK
  Description varchar(40) NULL
  Active bit NOT NULL default (0)
  IntType int NULL
  IntData1 int NULL
  IntData2 int NULL
  Occur int NULL
  ActDate smalldatetime NULL
  TermDate smalldatetime NULL
  ChgNow bit NOT NULL default (0)
  RecurRC_iBranchID int NULL
  RecurRC_dCreatedDate datetime NULL
  RecurRC_dModifiedDate datetime NULL
  RecurRC_iCreatedBranchID int NULL
  RecurRC_iModifiedBranchID int NULL
  RecurRC_iCreatedAgentID int NULL
  RecurRC_iModifiedAgentID int NULL
  RecurRC_iChangeSetID int NULL
  RecurRC_Checksum binary(20) NULL

## RecurRDef - Annuity Billing Default (AnnuityBillingDefaults)
Alias: Annuity Billing Default | Freedom Name: AnnuityBillingDefaults | Record Identifier: 
Notes: Annuity Billing Default Listing. PLEASE NOTE - This table has no defined primary key
PK: none
Columns (20):
  idRecurrDef int NOT NULL identity
  iRRAgentID int NULL
  iDCModule int NULL
  iPromptOpt int NULL
  dLastPrompt datetime NULL
  bAlwaysLoad bit NOT NULL default (1)
  bAutoReference bit NOT NULL default (0)
  vReferencePrefix varchar(20) NULL
  iReferenceNext int NULL
  iReferencePadLength int NULL
  iPMTrCodesID int NULL
  RecurRDef_iBranchID int NULL
  RecurRDef_dCreatedDate datetime NULL
  RecurRDef_dModifiedDate datetime NULL
  RecurRDef_iCreatedBranchID int NULL
  RecurRDef_iModifiedBranchID int NULL
  RecurRDef_iCreatedAgentID int NULL
  RecurRDef_iModifiedAgentID int NULL
  RecurRDef_iChangeSetID int NULL
  RecurRDef_Checksum binary(20) NULL

## RecurRF
PK: AutoIdx
Columns (19):
  AutoIdx int NOT NULL identity PK
  Module int NULL
  Descrip varchar(30) NULL
  Amount float NULL
  Incl bit NOT NULL default (0)
  TrCodeID int NULL
  TaxTypeID int NULL
  CurrencyID int NULL
  BaseHome bit NULL default (1)
  iTmplSettlementTermsID int NOT NULL default (0)
  RecurRF_iBranchID int NULL
  RecurRF_dCreatedDate datetime NULL
  RecurRF_dModifiedDate datetime NULL
  RecurRF_iCreatedBranchID int NULL
  RecurRF_iModifiedBranchID int NULL
  RecurRF_iCreatedAgentID int NULL
  RecurRF_iModifiedAgentID int NULL
  RecurRF_iChangeSetID int NULL
  RecurRF_Checksum binary(20) NULL

## RecurRL
PK: AutoIdx
Columns (26):
  AutoIdx int NOT NULL identity PK
  Suspend bit NOT NULL default (0)
  LastUpd smalldatetime NULL
  State int NULL
  Module int NULL
  Account int NULL
  ChgType int NULL
  Template bigint NULL
  Config int NULL
  ActDate smalldatetime NULL
  TermDate smalldatetime NULL
  OccurCnt int NULL
  iContractID int NULL
  bCreateAsOrder bit NOT NULL default (0)
  bDebitOrder bit NOT NULL default (0)
  bCreatePayment bit NOT NULL default (0)
  bAllowSettlementTerms bit NOT NULL default (1)
  RecurRL_iBranchID int NULL
  RecurRL_dCreatedDate datetime NULL
  RecurRL_dModifiedDate datetime NULL
  RecurRL_iCreatedBranchID int NULL
  RecurRL_iModifiedBranchID int NULL
  RecurRL_iCreatedAgentID int NULL
  RecurRL_iModifiedAgentID int NULL
  RecurRL_iChangeSetID int NULL
  RecurRL_Checksum binary(20) NULL

## RecurRTX
PK: AutoIdx
Columns (20):
  AutoIdx int NOT NULL identity PK
  ListIdx int NULL
  TxDate smalldatetime NULL
  TxAmount float NULL
  cTxAuditNumber varchar(50) NULL
  iInvNumID bigint NULL
  bDebitOrderPosted bit NOT NULL default (0)
  bPaymentCreated bit NOT NULL default (0)
  CurrencyID int NULL
  ExchangeRate float NULL
  TxAmountForeign float NULL
  RecurRTX_iBranchID int NULL
  RecurRTX_dCreatedDate datetime NULL
  RecurRTX_dModifiedDate datetime NULL
  RecurRTX_iCreatedBranchID int NULL
  RecurRTX_iModifiedBranchID int NULL
  RecurRTX_iCreatedAgentID int NULL
  RecurRTX_iModifiedAgentID int NULL
  RecurRTX_iChangeSetID int NULL
  RecurRTX_Checksum binary(20) NULL

## Refer
PK: AutoIdx
Columns (25):
  AutoIdx int NOT NULL identity PK
  DebtorAccNo varchar(20) NULL
  NameOfRef varchar(30) NULL
  IDNumber varchar(16) NULL
  DateOfBirth smalldatetime NULL
  Address1 varchar(30) NULL
  Address2 varchar(30) NULL
  Address3 varchar(30) NULL
  Telephone varchar(20) NULL
  PerShare float NULL
  ContactPerson varchar(30) NULL
  CreditLimit float NULL
  Rating varchar(15) NULL
  Category varchar(1) NULL
  CreditGranted varchar(1) NULL
  PunctPayment int NULL
  Refer_iBranchID int NULL
  Refer_dCreatedDate datetime NULL
  Refer_dModifiedDate datetime NULL
  Refer_iCreatedBranchID int NULL
  Refer_iModifiedBranchID int NULL
  Refer_iCreatedAgentID int NULL
  Refer_iModifiedAgentID int NULL
  Refer_iChangeSetID int NULL
  Refer_Checksum binary(20) NULL

## Reminder
PK: Autoidx
Columns (20):
  Autoidx int NOT NULL identity PK
  UserName varchar(50) NULL
  Dated smalldatetime NULL
  TypeofRemind varchar(25) NULL
  TextMemo text NULL
  Status varchar(1) NULL
  CompanyName varchar(35) NULL
  ContactPerson varchar(30) NULL
  Telephone varchar(15) NULL
  Fax varchar(15) NULL
  RemindDate smalldatetime NULL
  Reminder_iBranchID int NULL
  Reminder_dCreatedDate datetime NULL
  Reminder_dModifiedDate datetime NULL
  Reminder_iCreatedBranchID int NULL
  Reminder_iModifiedBranchID int NULL
  Reminder_iCreatedAgentID int NULL
  Reminder_iModifiedAgentID int NULL
  Reminder_iChangeSetID int NULL
  Reminder_Checksum binary(20) NULL

## SalesRep
PK: idSalesRep
Columns (31):
  idSalesRep int NOT NULL identity PK
  Code varchar(20) NOT NULL
  Name varchar(30) NULL
  Method smallint NULL
  Target1 float NULL
  Commission1 float NULL
  Target2 float NULL
  Commission2 float NULL
  Target3 float NULL
  Commission3 float NULL
  Target4 float NULL
  Commission4 float NULL
  Target5 float NULL
  Commission5 float NULL
  Address1 varchar(40) NULL
  Address2 varchar(40) NULL
  Address3 varchar(40) NULL
  Entity varchar(40) NULL
  Rep_On_Hold varchar(1) NULL
  Bank_Account varchar(40) NULL
  Comment1 varchar(80) NULL
  Comment2 varchar(80) NULL
  SalesRep_iBranchID int NULL
  SalesRep_dCreatedDate datetime NULL
  SalesRep_dModifiedDate datetime NULL
  SalesRep_iCreatedBranchID int NULL
  SalesRep_iModifiedBranchID int NULL
  SalesRep_iCreatedAgentID int NULL
  SalesRep_iModifiedAgentID int NULL
  SalesRep_iChangeSetID int NULL
  SalesRep_Checksum binary(20) NULL

## SerialMF
PK: SerialCounter
Columns (19):
  SerialCounter int NOT NULL identity PK
  SerialNumber varchar(30) NULL
  SNStockLink int NULL
  SNDateLMove smalldatetime NULL
  CurrentLoc int NULL
  CurrentAccLink int NULL
  iSNLotID int NULL
  iSNMFPID int NULL
  iSNMFPLineID bigint NOT NULL default (0)
  SerialMF_iBranchID int NULL
  SerialMF_dCreatedDate datetime NULL
  SerialMF_dModifiedDate datetime NULL
  SerialMF_iCreatedBranchID int NULL
  SerialMF_iModifiedBranchID int NULL
  SerialMF_iCreatedAgentID int NULL
  SerialMF_iModifiedAgentID int NULL
  SerialMF_iChangeSetID int NULL
  SerialMF_Checksum binary(20) NULL
  iSNBinLocationID int NOT NULL default (0)

## SerialTX
PK: SNTxCounter
Columns (23):
  SNTxCounter bigint NOT NULL identity PK
  SNLink int NULL
  SNTxDate smalldatetime NULL
  SNTxAccLink int NULL
  SNTxReference varchar(50) NULL
  SNTrCodeID int NULL
  SNAccModule varchar(5) NULL
  SNTransType int NULL
  SNProjectLink int NULL
  SNWarehouseID int NULL
  SNAuditNumber varchar(50) NULL
  cSNTXReference2 varchar(20) NULL
  iTxBranchID int NULL
  SerialTX_iBranchID int NULL
  SerialTX_dCreatedDate datetime NULL
  SerialTX_dModifiedDate datetime NULL
  SerialTX_iCreatedBranchID int NULL
  SerialTX_iModifiedBranchID int NULL
  SerialTX_iCreatedAgentID int NULL
  SerialTX_iModifiedAgentID int NULL
  SerialTX_iChangeSetID int NULL
  SerialTX_Checksum binary(20) NULL
  SNBinLocationID int NOT NULL default (0)

## SimpleSettings
PK: SimpleSettingID
Columns (7):
  SimpleSettingID int NOT NULL identity PK
  Name nvarchar(50) NOT NULL
  Value nvarchar(100) NOT NULL
  AgentID int NOT NULL
  ApplicationName nvarchar(50) NOT NULL
  Created datetime NOT NULL
  Modified datetime NOT NULL

## SlipLay
PK: IDSlipLay
Columns (17):
  IDSlipLay int NOT NULL identity PK
  LayIdentifier varchar(6) NOT NULL
  LayDefHeader text NULL
  LayDefBody text NULL
  LayDefFooter text NULL
  LayHeader text NULL
  LayBody text NULL
  LayFooter text NULL
  SlipLay_iBranchID int NULL
  SlipLay_dCreatedDate datetime NULL
  SlipLay_dModifiedDate datetime NULL
  SlipLay_iCreatedBranchID int NULL
  SlipLay_iModifiedBranchID int NULL
  SlipLay_iCreatedAgentID int NULL
  SlipLay_iModifiedAgentID int NULL
  SlipLay_iChangeSetID int NULL
  SlipLay_Checksum binary(20) NULL

## StDfTbl
PK: idStDfTbl
Columns (177):
  idStDfTbl int NOT NULL identity PK
  AutoInvNum bit NULL default (0)
  InvPref varchar(25) NULL
  InvNum varchar(15) NULL
  InvTrCodeID int NULL
  AutoRtsNum bit NULL
  RtsPref varchar(25) NULL
  RtsNum varchar(15) NULL
  RtsTrCodeID int NULL
  AutoCrnNum bit NULL
  CrnPref varchar(25) NULL
  CrnNum varchar(15) NULL
  CrnTrCodeID int NULL
  AutoGrvNum bit NULL
  GrvPref varchar(25) NULL
  GrvNum varchar(15) NULL
  bInvGrvSplit bit NULL default (0)
  SInvTrCodeID int NULL
  GrvTrCodeID int NULL
  SInvGLVarAccID int NULL
  AdjTrCodeID int NULL
  Neg_Qty varchar(1) NULL
  Decimals smallint NULL
  QuantDec smallint NULL
  GRVNumOpt varchar(1) NULL
  ShowInactive varchar(1) NULL
  InvAutoDisc varchar(1) NULL
  CrnAutoDisc varchar(1) NULL
  GrvAutoDisc varchar(1) NULL
  RtsAutoDisc varchar(1) NULL
  SerialPerLine smallint NULL
  GrvSplitTaxTypeID int NULL
  RTSNumOpt varchar(1) NULL
  AutoCode bit NOT NULL default (0)
  AutoCodeLength int NULL
  AutoCodeAlphaLength int NULL
  FilterStartLength int NULL default (0)
  DefaultAdjDesc bit NULL default (0)
  InvCountAuto bit NULL
  InvCountPrefix varchar(25) NULL
  InvCountNum varchar(15) NULL
  InvPad int NULL
  RTSPad int NULL
  CRNPad int NULL
  GRVPad int NULL
  AutoCodeNum int NULL
  AutoCodePref varchar(3) NULL
  InvCountPad int NULL
  AutoQuoteNum bit NULL
  QuotePref varchar(25) NULL
  QuoteNum int NULL
  QuotePad int NULL
  AutoTemplateNum bit NULL
  TemplatePref varchar(25) NULL
  TemplateNum int NULL
  TemplatePad int NULL
  iINVTaxTypeID int NULL
  iCRNTaxTypeID int NULL
  iGRVTaxTypeID int NULL
  iRTSTaxTypeID int NOT NULL
  iPaymentTrCodesID int NULL
  iSerialFilterStLength int NULL
  bSerialFilterStart bit NULL
  bSerialFilterProcessing bit NULL
  bGrvSplitUseExemptTax bit NOT NULL default (1)
  iInvSeg1TypeID int NULL
  iInvSeg2TypeID int NULL
  iInvSeg3TypeID int NULL
  iInvSeg4TypeID int NULL
  iInvSeg5TypeID int NULL
  iInvSeg6TypeID int NULL
  iInvSeg7TypeID int NULL
  bUseInvSeg bit NOT NULL default (0)
  bPostRepPerLine bit NOT NULL default (0)
  iCostDecimals smallint NULL
  bPostProjectPerLine bit NOT NULL default (0)
  iDefaultLotStatus int NULL
  bUseUpperItemCode bit NOT NULL default (0)
  iPriceListNameID1 int NULL
  iPriceListNameID2 int NULL
  iPriceListNameID3 int NULL
  bNegQtyWarn bit NOT NULL default (0)
  bIsPerpetual bit NOT NULL default (1)
  bIsInclusive bit NOT NULL default (1)
  iCostingMethod int NOT NULL default (0)
  iDefStockCostVarianceAccID int NOT NULL default (0)
  bCostPerWarehouse bit NOT NULL default (0)
  bInvJrBatchAutoNum bit NOT NULL default (1)
  cInvJrBatchPrefix varchar(25) NULL
  iInvJrBatchPadLength int NULL
  bInvJrRefAutoNum bit NOT NULL default (1)
  cInvJrRefPrefix varchar(25) NULL
  iInvJrRefPadLength int NULL
  iInvJrTrCodeID int NULL
  bForceProject bit NOT NULL default (0)
  bForceRep bit NOT NULL default (0)
  bArchiveQuotes bit NOT NULL default (0)
  bSerialProcessActLookup bit NOT NULL default (0)
  bInvLinePostDocDesc bit NOT NULL default (1)
  bFinLinePostDocDesc bit NOT NULL default (1)
  bForceExtOrderNum bit NOT NULL default (0)
  bForceSupplierInvNumber bit NOT NULL default (0)
  bUniqueInvNum bit NULL
  bUniqueRtsNum bit NULL
  bUniqueCrnNum bit NULL
  bUniqueGrvNum bit NULL
  bUniqueQuoteNum bit NULL
  bUniqueTemplateNum bit NULL
  bUniqueInvCountNum bit NULL
  bUniqueExtOrderNum bit NULL
  bUniqueSupplierInvNum bit NULL
  cCostPriceEncodingKey varchar(11) NOT NULL default 'ABCDFGHJKL.'
  fDefaultGPPercent real NULL
  bAllowPOSTender bit NOT NULL default (0)
  bAllowNegStockDef bit NOT NULL default (0)
  bCalculateTaxPerLine bit NOT NULL default (1)
  iInvCountAgentID int NULL
  iInvCountPromptOpt int NULL
  dInvCountLastPrompt datetime NULL
  bInvPrcUpdBatchAutoNum bit NOT NULL default (1)
  cInvPrcUpdBatchPrefix varchar(25) NULL
  iInvPrcUpdBatchPadLength int NULL
  bAutoLotAlloc bit NOT NULL default (0)
  iAutoLotAllocType int NULL
  bInvPrcUpdRefAutoNum bit NOT NULL default (1)
  cInvPrcUpdRefPrefix varchar(25) NULL
  iInvPrcUpdRefPadLength int NULL
  bPostDeliveryPerLine bit NOT NULL default (0)
  bAddToDeliveryDate bit NOT NULL default (0)
  iAddToDeliveryType int NULL
  iAddDeliveryDays int NULL
  bForceDeliveryINV bit NOT NULL default (0)
  bForceDeliveryCRN bit NOT NULL default (0)
  bForceDeliveryGRV bit NOT NULL default (0)
  bForceDeliveryRTS bit NOT NULL default (0)
  bPostCostVarianceGLLine bit NOT NULL default (1)
  bUseDimensions bit NULL default (0)
  bSellUsingDimensions bit NULL default (0)
  bBuyUsingDimensions bit NULL default (0)
  cDefMeasurement varchar(5) NULL default (0)
  cMeasurementRounding varchar(5) NULL default (0)
  cRoundingOption varchar(20) NULL default (0)
  bUseSalesOrders bit NOT NULL default (0)
  bUseUOM bit NOT NULL default (1)
  bInvIssueSplit bit NOT NULL default (0)
  iInvIssueSplitAccrualAccID int NULL
  bAutoGIVNumber bit NOT NULL default (1)
  bUniqueGIVNum bit NOT NULL default (0)
  cGIVPrefix varchar(25) NULL
  cGIVNumber varchar(15) NULL
  iGIVPad int NULL
  bAutoCGRNumber bit NOT NULL default (1)
  bUniqueCGRNum bit NOT NULL default (0)
  cCGRPrefix varchar(25) NULL
  cCGRNumber varchar(15) NULL
  iCGRPad int NULL
  bRTSAverageCostVariance bit NOT NULL default (0)
  StDfTbl_iBranchID int NULL
  StDfTbl_dCreatedDate datetime NULL
  StDfTbl_dModifiedDate datetime NULL
  StDfTbl_iCreatedBranchID int NULL
  StDfTbl_iModifiedBranchID int NULL
  StDfTbl_iCreatedAgentID int NULL
  StDfTbl_iModifiedAgentID int NULL
  StDfTbl_iChangeSetID int NULL
  StDfTbl_Checksum binary(20) NULL
  bAutoSBSINumber bit NOT NULL default (1)
  bUniqueSBSINumber bit NOT NULL default (0)
  cSBSIPrefix varchar(20) NULL
  cSBSINumber varchar(15) NULL
  iSBSIPad int NULL
  bCostPerLot bit NOT NULL default (0)
  bUseDefServiceGroup bit NOT NULL default (0)
  iDefServiceGroupID int NOT NULL default (0)
  bForceCancellationReason bit NOT NULL default (0)
  bPostCancellationReasonPerLine bit NOT NULL default (0)
  bSaveLoadBarcodeID bit NOT NULL default (0)

## StkItem
PK: StockLink
Columns (80):
  StockLink int NOT NULL identity PK
  Code varchar(400) NULL
  Description_1 varchar(50) NULL
  Description_2 varchar(50) NULL
  Description_3 varchar(50) NULL
  ServiceItem bit NOT NULL default (0)
  ItemActive bit NOT NULL default (1)
  WhseItem bit NOT NULL default (0)
  SerialItem bit NOT NULL default (0)
  DuplicateSN bit NOT NULL default (0)
  StrictSN bit NOT NULL default (0)
  BomCode varchar(1) NULL
  SMtrxCol int NULL
  PMtrxCol int NULL
  cModel varchar(50) NULL
  cRevision varchar(50) NULL
  cComponent varchar(50) NULL
  dDateReleased smalldatetime NULL
  dStkitemTimeStamp datetime NULL
  iInvSegValue1ID int NULL
  iInvSegValue2ID int NULL
  iInvSegValue3ID int NULL
  iInvSegValue4ID int NULL
  iInvSegValue5ID int NULL
  iInvSegValue6ID int NULL
  iInvSegValue7ID int NULL
  cExtDescription varchar(255) NULL
  cSimpleCode varchar(20) NULL
  bCommissionItem bit NOT NULL default (1)
  bLotItem bit NOT NULL default (0)
  iLotStatus int NULL
  bLotMustExpire bit NOT NULL default (1)
  iItemCostingMethod int NOT NULL default (0)
  iEUCommodityID int NOT NULL default (0)
  iEUSupplementaryUnitID int NOT NULL default (0)
  fNetMass float NOT NULL default (0)
  iUOMStockingUnitID int NULL
  iUOMDefPurchaseUnitID int NULL
  iUOMDefSellUnitID int NULL
  fStockGPPercent real NULL
  cEachDescription varchar(30) NULL default (0)
  cMeasurement varchar(5) NULL default (0)
  fBuyLength float NULL default (0)
  fBuyWidth float NULL default (0)
  fBuyHeight float NULL default (0)
  fBuyArea float NULL default (0)
  fBuyVolume float NULL default (0)
  cBuyWeight float NULL default (0)
  cBuyUnit varchar(5) NULL default (0)
  fSellLength float NULL default (0)
  fSellWidth float NULL default (0)
  fSellHeight float NULL default (0)
  fSellArea float NULL default (0)
  fSellVolume float NULL default (0)
  cSellWeight float NULL default (0)
  cSellUnit varchar(5) NULL default (0)
  bOverrideSell bit NULL default (0)
  bUOMItem bit NOT NULL default (0)
  bDimensionItem bit NOT NULL default (0)
  bVASItem bit NOT NULL default (0)
  bAirtimeItem bit NOT NULL default (0)
  StkItem_iBranchID int NULL
  StkItem_dCreatedDate datetime NULL
  StkItem_dModifiedDate datetime NULL
  StkItem_iCreatedBranchID int NULL
  StkItem_iModifiedBranchID int NULL
  StkItem_iCreatedAgentID int NULL
  StkItem_iModifiedAgentID int NULL
  StkItem_iChangeSetID int NULL
  StkItem_Checksum binary(20) NULL
  bSyncToSOT bit NOT NULL default (0)
  bImportedServices bit NOT NULL default (0)
  ucIIAIC varchar(30) NULL
  ucIISUPPLIER varchar(50) NULL
  ucIIWEIGHT varchar(30) NULL
  ucIIWIDTH varchar(30) NULL
  ucIIMONTHFOR varchar(30) NULL
  iAttributeGroupID int NOT NULL default (0)
  xAttribute xml NULL
  iMajorIndustryCodeID int NULL default (0)

## TaxRate
PK: idTaxRate
Columns (19):
  idTaxRate int NOT NULL identity PK
  Code varchar(10) NULL
  Description varchar(100) NULL
  TaxRate float NULL
  TaxRate_iBranchID int NULL
  TaxRate_dCreatedDate datetime NULL
  TaxRate_dModifiedDate datetime NULL
  TaxRate_iCreatedBranchID int NULL
  TaxRate_iModifiedBranchID int NULL
  TaxRate_iCreatedAgentID int NULL
  TaxRate_iModifiedAgentID int NULL
  TaxRate_iChangeSetID int NULL
  TaxRate_Checksum binary(20) NULL
  bActiveTaxType bit NOT NULL default (1)
  iTransSource int NOT NULL default (0)
  bAllowImportDeclaration bit NOT NULL default (0)
  cFiscalTaxLabel nvarchar(2) NULL
  bRequireRRP bit NULL default (0)
  cTaxCat varchar(10) NULL

## Tender
PK: IdTender
Columns (24):
  IdTender int NOT NULL identity PK
  TenderNo varchar(10) NOT NULL
  Description varchar(30) NULL
  Force_Narrative varchar(1) NULL
  House_Limit float NULL
  iTrCodesIDInvPM int NULL
  iTrCodesIDCRNRF int NULL
  bUsePinPad bit NULL
  iCardDisplayFirst int NULL
  iCardDisplayLast int NULL
  bForceCardNumber bit NULL
  bForceCardHolder bit NULL
  cExpiryFormat varchar(10) NULL
  bForceExpiry bit NULL
  bApplyDocumentRounding bit NULL default (0)
  Tender_iBranchID int NULL
  Tender_dCreatedDate datetime NULL
  Tender_dModifiedDate datetime NULL
  Tender_iCreatedBranchID int NULL
  Tender_iModifiedBranchID int NULL
  Tender_iCreatedAgentID int NULL
  Tender_iModifiedAgentID int NULL
  Tender_iChangeSetID int NULL
  Tender_Checksum binary(20) NULL

## Tills
PK: IdTills
Columns (18):
  IdTills int NOT NULL identity PK
  TillNo varchar(4) NOT NULL
  iWarehouseID int NULL
  iDeviceIDDisplay int NULL
  iDeviceIDDrawer int NULL
  iDeviceIDPrinter int NULL
  iDeviceIDFiscalPrinter int NULL
  iDeviceIDPinPad int NULL
  cTerminalID varchar(20) NULL
  Tills_iBranchID int NULL
  Tills_dCreatedDate datetime NULL
  Tills_dModifiedDate datetime NULL
  Tills_iCreatedBranchID int NULL
  Tills_iModifiedBranchID int NULL
  Tills_iCreatedAgentID int NULL
  Tills_iModifiedAgentID int NULL
  Tills_iChangeSetID int NULL
  Tills_Checksum binary(20) NULL

## TrCodes
PK: idTrCodes
Columns (32):
  idTrCodes int NOT NULL identity PK
  iModule int NOT NULL
  Code varchar(20) NOT NULL
  LinkID int NULL
  Description varchar(100) NULL
  DebitTrans bit NOT NULL default (1)
  Tax bit NOT NULL default (0)
  Rep bit NOT NULL default (0)
  Account1Link int NULL
  Account2Link int NULL
  TaxAccountLink int NULL
  GLPrompt bit NOT NULL default (0)
  TaxTypeID int NULL
  SplitTr bit NOT NULL default (0)
  bSalesFilter bit NOT NULL default (0)
  bAllowSubAccTrans bit NOT NULL default (0)
  bSettlementDisc bit NOT NULL default (0)
  iDtTaxGroupID int NULL
  iCtTaxGroupID int NULL
  iTaxGroupID int NULL
  iMBServiceID int NOT NULL default (0)
  TrCodes_iBranchID int NULL
  TrCodes_dCreatedDate datetime NULL
  TrCodes_dModifiedDate datetime NULL
  TrCodes_iCreatedBranchID int NULL
  TrCodes_iModifiedBranchID int NULL
  TrCodes_iCreatedAgentID int NULL
  TrCodes_iModifiedAgentID int NULL
  TrCodes_iChangeSetID int NULL
  TrCodes_Checksum binary(20) NULL
  bPrepayment bit NOT NULL default (0)
  bPurchasesFilter bit NOT NULL default (0)

## VenClass
PK: idVenClass
Columns (25):
  idVenClass int NOT NULL identity PK
  Code varchar(20) NULL
  Description varchar(100) NULL
  DiscMtrxRow int NULL
  dGroupTimeStamp datetime NULL
  iAccountsIDControlAcc int NULL
  iAccountsIDProfitAcc int NULL
  iAccountsIDLossAcc int NULL
  iTaxControlAccID int NULL
  iRevProfitAcc int NULL
  iRevLossAcc int NULL
  iProvForRevAcc int NULL
  iInvoiceDocProfileID int NULL
  iSOInvoiceDocProfileID int NULL
  iCreditNoteDocProfileID int NULL
  iJCInvoiceDocProfileID int NULL
  VenClass_iBranchID int NULL
  VenClass_dCreatedDate datetime NULL
  VenClass_dModifiedDate datetime NULL
  VenClass_iCreatedBranchID int NULL
  VenClass_iModifiedBranchID int NULL
  VenClass_iCreatedAgentID int NULL
  VenClass_iModifiedAgentID int NULL
  VenClass_iChangeSetID int NULL
  VenClass_Checksum binary(20) NULL

## VenDef
PK: idVenDef
Columns (40):
  idVenDef int NOT NULL identity PK
  AutoYN varchar(1) NULL
  AutoLength int NULL
  AutoAlphaLength int NULL
  UpperAccNo varchar(1) NULL
  ForceProject bit NOT NULL default (0)
  DefaultTxDesc bit NOT NULL default (0)
  LatestVDPrice bit NOT NULL default (0)
  FilterStartLength int NULL
  iTaxRateIdNoCharge int NULL
  iPEXTrCodeID int NULL
  iLEXTrCodeID int NULL
  fTaxPromptAmount float NULL
  iDelAddressCodeID1 int NULL
  iDelAddressCodeID2 int NULL
  bUseAllocStoredProc bit NOT NULL default (1)
  bInvTxCheckAccAfterChange bit NOT NULL default (0)
  iEFTSLayoutID int NOT NULL default (0)
  cEFTSPathOutFile varchar(100) NULL
  iDefaultTermID int NULL
  iRevProfitAcc int NULL
  iRevLossAcc int NULL
  iProvForRevAcc int NULL
  iRemitBatchManageOpt int NOT NULL default (0)
  VenDef_iBranchID int NULL
  VenDef_dCreatedDate datetime NULL
  VenDef_dModifiedDate datetime NULL
  VenDef_iCreatedBranchID int NULL
  VenDef_iModifiedBranchID int NULL
  VenDef_iCreatedAgentID int NULL
  VenDef_iModifiedAgentID int NULL
  VenDef_iChangeSetID int NULL
  VenDef_Checksum binary(20) NULL
  iPDAgentID int NOT NULL default (0)
  iPDPromptOpt int NOT NULL default (0)
  dPDLastPrompt datetime NULL
  cEFTSFileName varchar(100) NULL
  bEFTSAutoNumbers bit NOT NULL default (0)
  iEFTSPadLength int NULL
  cEFTSPrefix varchar(20) NULL

## Vendor
PK: DCLink
Columns (117):
  DCLink int NOT NULL identity PK
  Account varchar(20) NULL
  Name varchar(150) NULL
  Title varchar(5) NULL
  Init varchar(6) NULL
  Contact_Person varchar(30) NULL
  Physical1 varchar(40) NULL
  Physical2 varchar(40) NULL
  Physical3 varchar(40) NULL
  Physical4 varchar(40) NULL
  Physical5 varchar(40) NULL
  PhysicalPC varchar(15) NULL
  Addressee varchar(30) NULL
  Post1 varchar(40) NULL
  Post2 varchar(40) NULL
  Post3 varchar(40) NULL
  Post4 varchar(40) NULL
  Post5 varchar(40) NULL
  PostPC varchar(15) NULL
  Delivered_To varchar(30) NULL
  Telephone varchar(25) NULL
  Telephone2 varchar(25) NULL
  Fax1 varchar(25) NULL
  Fax2 varchar(25) NULL
  AccountTerms int NULL
  CT bit NOT NULL default (0)
  Tax_Number varchar(50) NULL
  Registration varchar(20) NULL
  Credit_Limit float NULL
  Interest_Rate float NULL
  Discount float NULL
  On_Hold bit NOT NULL default (0)
  BFOpenType int NULL
  EMail varchar(200) NULL
  BankLink int NULL
  BranchCode varchar(30) NULL
  BankAccNum varchar(30) NULL
  BankAccType varchar(30) NULL
  AutoDisc float NULL
  DiscMtrxRow int NULL
  DCBalance float NULL
  CheckTerms bit NOT NULL default (0)
  UseEmail bit NOT NULL default (0)
  iBusTypeID int NULL
  iBusClassID int NULL
  iCountryID int NULL
  cAccDescription varchar(80) NULL
  cWebPage varchar(50) NULL
  dTimeStamp datetime NULL
  iClassID int NULL
  iAreasID int NULL
  cBankRefNr varchar(30) NULL
  iCurrencyID int NULL
  bStatPrint bit NOT NULL default (0)
  bStatEmail bit NOT NULL default (0)
  cStatEmailPass varchar(160) NULL
  bForCurAcc bit NOT NULL default (0)
  bRemittanceChequeEFTS bit NOT NULL default (1)
  fForeignBalance float NULL
  iSettlementTermsID int NOT NULL default (0)
  bSourceDocPrint bit NOT NULL default (1)
  bSourceDocEmail bit NOT NULL default (0)
  iEUCountryID int NOT NULL default (0)
  iDefTaxTypeID int NOT NULL default (0)
  iAgeingTermID int NULL
  iBankDetailType tinyint NULL
  cBankAccHolder varchar(30) NULL
  cIDNumber varchar(20) NULL
  cPassportNumber varchar(20) NULL
  cBankCode varchar(15) NULL
  cSwiftCode varchar(11) NULL
  iBankDetailID int NULL
  Vendor_iBranchID int NULL
  Vendor_dCreatedDate datetime NULL
  Vendor_dModifiedDate datetime NULL
  Vendor_iCreatedBranchID int NULL
  Vendor_iModifiedBranchID int NULL
  Vendor_iCreatedAgentID int NULL
  Vendor_iModifiedAgentID int NULL
  Vendor_iChangeSetID int NULL
  Vendor_Checksum binary(20) NULL
  iSPQueueID int NULL
  iTaxState int NOT NULL default (0)
  ulAPSector1 varchar(100) NULL
  ulAPSector2 varchar(100) NULL
  ulAPSector3 varchar(100) NULL
  ulAPSector4 varchar(100) NULL
  ulAPSector5 varchar(100) NULL
  ulAPSector6 varchar(100) NULL
  ulAPSector7 varchar(100) NULL
  ulAPSector8 varchar(100) NULL
  ulAPSector9 varchar(100) NULL
  ulAPSector10 varchar(100) NULL
  ulAPSupplierLocation varchar(100) NULL
  udAPRegistrationDate datetime NULL
  ubAPBEECompliant bit NULL default (1)
  ulAPStatus varchar(100) NULL
  ulAPDeliveryGoods varchar(100) NULL
  ubAPFailToDeliver bit NULL default (1)
  ubAPWorkforGovt bit NULL default (1)
  ubAPBlacklistedbyGovt bit NULL default (1)
  ubAPConfirmCompany bit NULL default (1)
  ufAPHDI float NULL
  ufAPFunctionality float NULL
  ufAPExperience float NULL
  ufAPWomen float NULL
  ufAPWhite float NULL
  ufAPMiscellaneous float NULL
  ufAPPrice float NULL
  bTaxVerified bit NOT NULL default (0)
  dDateTaxVerified datetime NULL
  cRMCDApprovalNumber varchar(50) NULL
  dRMCDApprovalDate datetime NULL
  bObjectToProcess bit NOT NULL default (0)
  bStatEmailPeople bit NOT NULL default (0)
  bSourceDocEmailPeople bit NOT NULL default (0)
  iTaxCountryID int NOT NULL default (0)

## WhseMst
PK: WhseLink
Columns (37):
  WhseLink int NOT NULL identity PK
  Code varchar(20) NOT NULL
  Name varchar(50) NOT NULL
  KnownAs varchar(50) NULL
  Address1 varchar(40) NULL
  Address2 varchar(40) NULL
  Address3 varchar(40) NULL
  PostCode varchar(15) NULL
  Tel varchar(15) NULL
  Manager varchar(30) NULL
  BankLink int NULL
  BranchCode varchar(30) NULL
  BankAccNum varchar(30) NULL
  BankAccType varchar(30) NULL
  EMail varchar(60) NULL
  ModemTel varchar(15) NULL
  DefaultWhse bit NOT NULL default (0)
  AddNewStock bit NOT NULL default (0)
  dWarehouseTimeStamp datetime NULL
  iWhseTypeID int NOT NULL default (0)
  bAllowToBuyInto bit NOT NULL default (1)
  bAllowToSellFrom bit NOT NULL default (1)
  bAllowNegStock bit NOT NULL default (0)
  WhseMst_iBranchID int NULL
  WhseMst_dCreatedDate datetime NULL
  WhseMst_dModifiedDate datetime NULL
  WhseMst_iCreatedBranchID int NULL
  WhseMst_iModifiedBranchID int NULL
  WhseMst_iCreatedAgentID int NULL
  WhseMst_iModifiedAgentID int NULL
  WhseMst_iChangeSetID int NULL
  WhseMst_Checksum binary(20) NULL
  iDefaultItemGroupID int NULL
  bAllowMultiBinLocations bit NOT NULL default (0)
  bUseDefaultBinLevels bit NOT NULL default (1)
  iDefaultWhseSalesBinID int NULL
  iDefaultWhsePurchaseBinID int NULL

## WhseStk
PK: IdWhseStk
Columns (48):
  IdWhseStk bigint NOT NULL identity PK
  WHWhseID int NULL
  WHStockLink int NOT NULL
  WHStockGroup varchar(20) NULL
  WHQtyOnHand float NOT NULL default (0)
  WHQtyOnSO float NOT NULL default (0)
  WHQtyOnPO float NOT NULL default (0)
  WHQtyReserved float NOT NULL default (0)
  WHTTInv varchar(10) NULL
  WHTTCrn varchar(10) NULL
  WHTTGrv varchar(10) NULL
  WHTTRts varchar(10) NULL
  WHBarCode varchar(400) NULL
  WHRe_Ord_Lvl float NULL
  WHRe_Ord_Qty float NULL
  WHMin_Lvl float NULL
  WHMax_Lvl float NULL
  WHUsePriceDefs bit NOT NULL default (1)
  WHUseInfoDefs bit NOT NULL default (1)
  WHUseOrderDefs bit NOT NULL default (1)
  WHUseDefaultDefs bit NOT NULL default (1)
  WHPackCode varchar(5) NULL
  WHJobQty float NOT NULL default (0)
  iBinLocationID int NULL
  fLGRVCount float NULL
  WHMFPQty float NOT NULL default (0)
  WHUseSupplierDefs bit NOT NULL default (1)
  fAverageCost float NOT NULL default (0)
  fLatestCost float NOT NULL default (0)
  fLowestCost float NOT NULL default (0)
  fHighestCost float NOT NULL default (0)
  fManualCost float NOT NULL default (0)
  fWhseLastGRVCost float NOT NULL default (0)
  bWHAllowNegStock bit NOT NULL default (0)
  fWHQtyToDeliver float NULL
  WhseStk_fLeadDays float NULL
  WHBuyingAgentID int NULL
  fIBTQtyToIssue float NOT NULL default (0)
  fIBTQtyToReceive float NOT NULL default (0)
  WhseStk_iBranchID int NULL
  WhseStk_dCreatedDate datetime NULL
  WhseStk_dModifiedDate datetime NULL
  WhseStk_iCreatedBranchID int NULL
  WhseStk_iModifiedBranchID int NULL
  WhseStk_iCreatedAgentID int NULL
  WhseStk_iModifiedAgentID int NULL
  WhseStk_iChangeSetID int NULL
  WhseStk_Checksum binary(20) NULL
