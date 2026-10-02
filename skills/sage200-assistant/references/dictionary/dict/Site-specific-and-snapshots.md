# Sage 200 Evolution table dictionary - Site specific and snapshots

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _as_FM_ManufactureCostLine
PK: ID
Columns (47):
  ID bigint NOT NULL identity PK
  CreationDate datetime NULL
  LastUpdateDate datetime NULL
  ManufactureID bigint NULL
  Description varchar(max) NULL
  WarehouseID int NULL
  TransactionDate datetime NULL
  Reference varchar(max) NULL
  Quantity decimal(18,2) NULL
  QuantityAvailable decimal(18,2) NULL
  UnitOfMeasureID int NULL
  UnitCost decimal(18,2) NULL
  Processed bit NULL
  Lot int NULL
  CostingItemID int NULL
  TotalCost decimal(18,2) NULL
  Implement int NULL
  Line int NULL
  CanChangeLineType bit NULL
  Action int NULL
  Type int NULL
  AccountID bigint NULL
  IsLotTracked bit NULL
  IsWarehouseTracked bit NULL
  IsServiceItem bit NULL
  NeedsUnitOfMeasure bit NULL
  ActivityID bigint NULL
  SyncedFJCId uniqueidentifier NULL
  ItemDescription varchar(max) NULL
  IsNutrientItem bit NULL
  Natrium decimal(18,2) NULL
  PhosporOxide decimal(18,2) NULL
  PotassiumOxide decimal(18,2) NULL
  Sulphur decimal(18,2) NULL
  Magnesium decimal(18,2) NULL
  CalciumOxide decimal(18,2) NULL
  CalculationType varchar(max) NULL
  CostType int NULL
  State int NULL
  AuditNumber varchar(max) NULL
  CostingItem int NULL
  Transfered bit NULL
  TransferedToManufactureId bigint NULL
  CreatedOnDate datetimeoffset(7) NULL
  LastModificationDate datetimeoffset(7) NULL
  UOMQuantity decimal(18,2) NULL
  LotCode varchar(255) NULL

## _as_FM_ManufactureHarvestLine
PK: ID
Columns (17):
  ID bigint NOT NULL identity PK
  CreationDate datetime NULL
  LastUpdateDate datetime NULL
  CreatedOnDate datetimeoffset(7) NULL
  LastModificationDate datetimeoffset(7) NULL
  LineNumber int NULL
  ItemID int NULL
  Description varchar(max) NULL
  Quantity decimal(18,2) NULL
  WarehouseID int NULL
  LotID int NULL
  UnitOfMeasureID int NULL
  Reference varchar(max) NULL
  HarvestDate datetime NULL
  ManufactureID bigint NULL
  Hectare decimal(18,2) NULL
  UOMDefaultQuantity decimal(18,2) NULL

## _as_FM_ManufactureHeader
PK: ID
Columns (42):
  ID bigint NOT NULL identity PK
  CreationDate datetime NULL
  LastUpdateDate datetime NULL
  NrOfHa decimal(18,2) NULL
  EstimatedQuantityToProduce decimal(18,2) NULL
  ManufactureTypeID bigint NULL
  EstimatedTotalCost decimal(18,2) NULL
  PlantingDate datetime NULL
  ActualQuantityProduced decimal(18,2) NULL
  TotalIncurredCosts decimal(18,2) NULL
  TotalOUMQuantity decimal(18,2) NULL
  BillOfMaterialID int NULL
  WiPAccountID int NULL
  Description varchar(max) NULL
  ProcessReference varchar(max) NULL
  ExternalReference varchar(max) NULL
  WarehouseID int NULL
  Closed bit NULL
  CreateAsset bit NULL
  GLAccountID int NULL
  ProjectID int NULL
  EndItemID bigint NULL
  Field varchar(max) NULL
  StartDate datetime NULL
  ManufactureLeadTime decimal(18,2) NULL
  ProjectedCompletionDate datetime NULL
  ActualCompletionDate datetime NULL
  ResourceAllocationMode int NULL
  TotalIncurredCostsLastHarvest decimal(18,2) NULL
  LotId int NULL
  TotalFairValue decimal(18,2) NULL
  Writeoff bit NULL
  WriteoffDate datetime NULL
  WriteoffPerformedOn datetime NULL
  WriteoffReason varchar(2000) NULL
  WriteoffAgentId int NULL
  WriteoffAudit varchar(25) NULL
  Contract varchar(255) NULL
  Longitude varchar(max) NULL
  Latitude varchar(max) NULL
  CreatedOnDate datetimeoffset(7) NULL
  LastModificationDate datetimeoffset(7) NULL

## _as_FM_ManufactureType
PK: ID
Columns (9):
  ID bigint NOT NULL identity PK
  CreationDate datetime NULL
  LastUpdateDate datetime NULL
  Code varchar(max) NULL
  Name varchar(max) NULL
  ProcessMethod uniqueidentifier NULL
  ResourceAllocationMode int NULL
  CreatedOnDate datetimeoffset(7) NULL
  LastModificationDate datetimeoffset(7) NULL

## _as_IntegrationLog_Granite
PK: none
Columns (13):
  Id bigint NOT NULL identity
  CycleLineID varchar(100) NULL
  CycleID bigint NULL
  LinePostSTId bigint NULL
  LinePostGLId bigint NULL
  ManufactureLineId bigint NULL
  UnitCost float NULL
  AuditNumber varchar(100) NULL
  ManufactureId bigint NULL
  ProductionPostSTId bigint NULL
  IntegrationStatusId smallint NULL
  Created_Date datetime NOT NULL default getdate()
  Finalized_Date datetime NULL

## _as_IntegrationLog_Granite_Reversal
PK: none
Columns (13):
  Id bigint NOT NULL identity
  CycleLineID varchar(100) NULL
  CycleID bigint NULL
  LinePostSTId bigint NULL
  LinePostGLId bigint NULL
  ManufactureLineId bigint NULL
  UnitCost float NULL
  AuditNumber varchar(100) NULL
  ManufactureId bigint NULL
  ProductionPostSTId bigint NULL
  IntegrationStatusId smallint NULL
  Created_Date datetime NOT NULL default getdate()
  Finalized_Date datetime NULL

## _as_IntegrationLog_MFClosing
PK: Id
Columns (6):
  Id bigint NOT NULL identity PK
  _etblManufProcessID bigint NULL
  DateClosed datetime NULL default getdate()
  MFP_dLastUpdated datetime NULL
  MFP_fManufQuantity float NULL
  MFP_fQtyManufactured float NULL

## _etblManufProcess20250314
PK: none
Columns (32):
  idManufProcess int NOT NULL identity
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
  bOverrideCompWhse bit NOT NULL
  iInvoiceLineID bigint NOT NULL
  bIsLinkedToOrder bit NOT NULL
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
  iBOMAttributeGroupID int NOT NULL
  xBOMAttribute xml NULL

## _etblManufProcessLine20250528
PK: none
Columns (35):
  idManufProcessLine bigint NOT NULL identity
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
  bProcessed bit NOT NULL
  dTransactionDate datetime NULL
  dLastUpdateDate datetime NULL
  fQtyAvailable float NULL
  cDescription varchar(255) NULL
  iLotID int NULL
  iPickingSlipPrinted int NOT NULL
  iUnmanufactureLineNo int NOT NULL
  iDocVersion int NOT NULL
  fLineCost float NOT NULL
  _etblManufProcessLine_iBranchID int NULL
  _etblManufProcessLine_dCreatedDate datetime NULL
  _etblManufProcessLine_dModifiedDate datetime NULL
  _etblManufProcessLine_iCreatedBranchID int NULL
  _etblManufProcessLine_iModifiedBranchID int NULL
  _etblManufProcessLine_iCreatedAgentID int NULL
  _etblManufProcessLine_iModifiedAgentID int NULL
  _etblManufProcessLine_iChangeSetID int NULL
  _etblManufProcessLine_Checksum binary(20) NULL
  iStockBinLocationID int NULL
  iNewStockBinLocationID int NULL
  iAttributeGroupID int NOT NULL
  xAttribute xml NULL

## _etblPriceListPrices20260619
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

## _rtblAgents20241111
PK: none
Columns (132):
  idAgents int NOT NULL identity
  bSysAccount bit NOT NULL
  cAgentName varchar(50) NULL
  cPassword varchar(160) NULL
  cFirstName varchar(20) NULL
  cInitials varchar(5) NULL
  cLastName varchar(30) NULL
  cTitle varchar(6) NULL
  cDisplayName varchar(60) NULL
  cDescription varchar(50) NULL
  cTelWork varchar(20) NULL
  cTelFax varchar(20) NULL
  cTelMobile varchar(20) NULL
  cTelHome varchar(20) NULL
  cEmail varchar(60) NULL
  cWebPage varchar(50) NULL
  cComments varchar(1024) NULL
  cAddressStreet varchar(512) NULL
  cAddressPOBox varchar(30) NULL
  cAddressCity varchar(30) NULL
  cAddressState varchar(30) NULL
  cAddressZip varchar(15) NULL
  cAddressCountry varchar(30) NULL
  bCanAssign bit NOT NULL
  bPwdCanChange bit NOT NULL
  bPwdMustChange bit NOT NULL
  bPwdChangeEvery bit NOT NULL
  iPwdChangeDays int NULL
  dPwdLastChange smalldatetime NULL
  cPwdRemind varchar(160) NULL
  bAgentOutOffice bit NOT NULL
  bExitWarning bit NOT NULL
  bCanSetOutOfOffice bit NOT NULL
  bKnowledgeBaseWarning bit NOT NULL
  bNewIncidentNotification bit NOT NULL
  bUseDefaultTree bit NOT NULL
  bAutoSpellCheck bit NOT NULL
  iDefIncidentTypeGroupID int NULL
  iDefTillId int NULL
  iDefCashAccount int NULL
  iDefWhseId int NULL
  iNotifyEscalateMinutes int NULL
  iNotifyDueMinutes int NULL
  bForceThisWarehouse bit NOT NULL
  bAgentActive bit NOT NULL
  bCBAgNoneVisible bit NOT NULL
  bCBAgAllVisible bit NOT NULL
  bJRAgNoneVisible bit NOT NULL
  bJRAgAllVisible bit NOT NULL
  bCBUseGrpDefaults bit NOT NULL
  bJRUseGrpDefaults bit NOT NULL
  bCBAgOwnVisible bit NOT NULL
  bJRAgOwnVisible bit NOT NULL
  iPOAuthType int NOT NULL
  iPOIncidentTypeID int NULL
  bPOExclusive bit NOT NULL
  fPOLimit float NULL
  bPOUseGrpDefaults bit NOT NULL
  cAccessPurchaseWhIDLst varchar(1024) NULL
  cAccessSalesWhIDLst varchar(1024) NULL
  cAccessOtherTxWhIDList varchar(1024) NULL
  cAccessPurchaseWhChkLstInd char(1) NOT NULL
  cAccessSalesWhChkLstInd char(1) NOT NULL
  cAccessOtherTxWhChkLstInd char(1) NOT NULL
  iDefProjectID int NULL
  cAccessProjectIDLst varchar(1024) NULL
  cAccessProjectChkLstInd char(1) NULL
  iDefRepID int NULL
  cAccessRepIDLst varchar(1024) NULL
  cAccessRepChkLstInd char(1) NULL
  Max_LDisc float NOT NULL
  Max_Disc float NOT NULL
  cOperatorCode varchar(50) NULL
  cOperatorPassword varchar(50) NULL
  cOperatorNewPassword varchar(50) NULL
  cAccessBranchIDLst varchar(1024) NULL
  cAccessBranchChkLstInd char(1) NULL
  iDocketInputMode int NOT NULL
  cOperatorCodePOS varchar(50) NULL
  cOperatorPasswordPOS varchar(50) NULL
  cOperatorNewPasswordPOS varchar(50) NULL
  bCanChangeSessionDate bit NOT NULL
  cEFTOperatorCode varchar(6) NULL
  bSupervisorAgent bit NULL
  bLockedOut bit NOT NULL
  cAccessARGroupIDLst varchar(1024) NULL
  cAccessARGroupChkLstInd char(1) NOT NULL
  bIncludeARNoGroups bit NOT NULL
  bApplyARGroupsToEnqRep bit NULL
  cAccessAPGroupIDLst varchar(1024) NULL
  cAccessAPGroupChkLstInd char(1) NOT NULL
  bIncludeAPNoGroups bit NOT NULL
  bApplyAPGroupsToEnqRep bit NULL
  vbBiometric varchar(max) NULL
  fDefMax_LDisc float NULL
  fDefMax_Disc float NULL
  bApplyAccessRepsToReports bit NULL
  bApplyAccessProjectsToReports bit NULL
  idPOSMenuSetup int NULL
  bAgentIsBuyer bit NOT NULL
  bUseBiometric bit NOT NULL
  FiscalPrinterId int NOT NULL
  FiscalDeviceId int NOT NULL
  _rtblAgents_iBranchID int NULL
  _rtblAgents_dCreatedDate datetime NULL
  _rtblAgents_dModifiedDate datetime NULL
  _rtblAgents_iCreatedBranchID int NULL
  _rtblAgents_iModifiedBranchID int NULL
  _rtblAgents_iCreatedAgentID int NULL
  _rtblAgents_iModifiedAgentID int NULL
  _rtblAgents_iChangeSetID int NULL
  _rtblAgents_Checksum binary(20) NULL
  cAccessDocCatGroupIDLst varchar(1024) NULL
  cAccessDocCatGroupChkLstInd char(1) NOT NULL
  iDefDocCatID int NULL
  cAccessDocCatIDLst varchar(1024) NULL
  cAccessDocCatChkLstInd char(1) NOT NULL
  cAccessIncidentTypeGroupIDLst varchar(1024) NULL
  cAccessIncidentTypeGroupChkLstInd char(1) NOT NULL
  cAccessIncidentTypeIDLst varchar(1024) NULL
  cAccessIncidentTypeChkLstInd char(1) NOT NULL
  cSagePayUserName varchar(50) NULL
  cSagePayPassword varchar(160) NULL
  cSagePayPIN varchar(30) NULL
  iAgentLoginScreen int NOT NULL
  cVisibleBranchesLst nvarchar(1024) NULL
  cVisibleBranchesLstInd nvarchar(1024) NULL
  cVisibleWarehousesLst nvarchar(1024) NULL
  cVisibleWarehousesLstInd nvarchar(1024) NULL
  cAccessProcessFlowIDLst varchar(1024) NULL
  cAccessProcessFlowChkLstInd char(1) NOT NULL
  cEmailSignature varchar(max) NULL

## _rtblAgents_20240812
PK: none
Columns (132):
  idAgents int NOT NULL identity
  bSysAccount bit NOT NULL
  cAgentName varchar(50) NULL
  cPassword varchar(160) NULL
  cFirstName varchar(20) NULL
  cInitials varchar(5) NULL
  cLastName varchar(30) NULL
  cTitle varchar(6) NULL
  cDisplayName varchar(60) NULL
  cDescription varchar(50) NULL
  cTelWork varchar(20) NULL
  cTelFax varchar(20) NULL
  cTelMobile varchar(20) NULL
  cTelHome varchar(20) NULL
  cEmail varchar(60) NULL
  cWebPage varchar(50) NULL
  cComments varchar(1024) NULL
  cAddressStreet varchar(512) NULL
  cAddressPOBox varchar(30) NULL
  cAddressCity varchar(30) NULL
  cAddressState varchar(30) NULL
  cAddressZip varchar(15) NULL
  cAddressCountry varchar(30) NULL
  bCanAssign bit NOT NULL
  bPwdCanChange bit NOT NULL
  bPwdMustChange bit NOT NULL
  bPwdChangeEvery bit NOT NULL
  iPwdChangeDays int NULL
  dPwdLastChange smalldatetime NULL
  cPwdRemind varchar(160) NULL
  bAgentOutOffice bit NOT NULL
  bExitWarning bit NOT NULL
  bCanSetOutOfOffice bit NOT NULL
  bKnowledgeBaseWarning bit NOT NULL
  bNewIncidentNotification bit NOT NULL
  bUseDefaultTree bit NOT NULL
  bAutoSpellCheck bit NOT NULL
  iDefIncidentTypeGroupID int NULL
  iDefTillId int NULL
  iDefCashAccount int NULL
  iDefWhseId int NULL
  iNotifyEscalateMinutes int NULL
  iNotifyDueMinutes int NULL
  bForceThisWarehouse bit NOT NULL
  bAgentActive bit NOT NULL
  bCBAgNoneVisible bit NOT NULL
  bCBAgAllVisible bit NOT NULL
  bJRAgNoneVisible bit NOT NULL
  bJRAgAllVisible bit NOT NULL
  bCBUseGrpDefaults bit NOT NULL
  bJRUseGrpDefaults bit NOT NULL
  bCBAgOwnVisible bit NOT NULL
  bJRAgOwnVisible bit NOT NULL
  iPOAuthType int NOT NULL
  iPOIncidentTypeID int NULL
  bPOExclusive bit NOT NULL
  fPOLimit float NULL
  bPOUseGrpDefaults bit NOT NULL
  cAccessPurchaseWhIDLst varchar(1024) NULL
  cAccessSalesWhIDLst varchar(1024) NULL
  cAccessOtherTxWhIDList varchar(1024) NULL
  cAccessPurchaseWhChkLstInd char(1) NOT NULL
  cAccessSalesWhChkLstInd char(1) NOT NULL
  cAccessOtherTxWhChkLstInd char(1) NOT NULL
  iDefProjectID int NULL
  cAccessProjectIDLst varchar(1024) NULL
  cAccessProjectChkLstInd char(1) NULL
  iDefRepID int NULL
  cAccessRepIDLst varchar(1024) NULL
  cAccessRepChkLstInd char(1) NULL
  Max_LDisc float NOT NULL
  Max_Disc float NOT NULL
  cOperatorCode varchar(50) NULL
  cOperatorPassword varchar(50) NULL
  cOperatorNewPassword varchar(50) NULL
  cAccessBranchIDLst varchar(1024) NULL
  cAccessBranchChkLstInd char(1) NULL
  iDocketInputMode int NOT NULL
  cOperatorCodePOS varchar(50) NULL
  cOperatorPasswordPOS varchar(50) NULL
  cOperatorNewPasswordPOS varchar(50) NULL
  bCanChangeSessionDate bit NOT NULL
  cEFTOperatorCode varchar(6) NULL
  bSupervisorAgent bit NULL
  bLockedOut bit NOT NULL
  cAccessARGroupIDLst varchar(1024) NULL
  cAccessARGroupChkLstInd char(1) NOT NULL
  bIncludeARNoGroups bit NOT NULL
  bApplyARGroupsToEnqRep bit NULL
  cAccessAPGroupIDLst varchar(1024) NULL
  cAccessAPGroupChkLstInd char(1) NOT NULL
  bIncludeAPNoGroups bit NOT NULL
  bApplyAPGroupsToEnqRep bit NULL
  vbBiometric varchar(max) NULL
  fDefMax_LDisc float NULL
  fDefMax_Disc float NULL
  bApplyAccessRepsToReports bit NULL
  bApplyAccessProjectsToReports bit NULL
  idPOSMenuSetup int NULL
  bAgentIsBuyer bit NOT NULL
  bUseBiometric bit NOT NULL
  FiscalPrinterId int NOT NULL
  FiscalDeviceId int NOT NULL
  _rtblAgents_iBranchID int NULL
  _rtblAgents_dCreatedDate datetime NULL
  _rtblAgents_dModifiedDate datetime NULL
  _rtblAgents_iCreatedBranchID int NULL
  _rtblAgents_iModifiedBranchID int NULL
  _rtblAgents_iCreatedAgentID int NULL
  _rtblAgents_iModifiedAgentID int NULL
  _rtblAgents_iChangeSetID int NULL
  _rtblAgents_Checksum binary(20) NULL
  cAccessDocCatGroupIDLst varchar(1024) NULL
  cAccessDocCatGroupChkLstInd char(1) NOT NULL
  iDefDocCatID int NULL
  cAccessDocCatIDLst varchar(1024) NULL
  cAccessDocCatChkLstInd char(1) NOT NULL
  cAccessIncidentTypeGroupIDLst varchar(1024) NULL
  cAccessIncidentTypeGroupChkLstInd char(1) NOT NULL
  cAccessIncidentTypeIDLst varchar(1024) NULL
  cAccessIncidentTypeChkLstInd char(1) NOT NULL
  cSagePayUserName varchar(50) NULL
  cSagePayPassword varchar(160) NULL
  cSagePayPIN varchar(30) NULL
  iAgentLoginScreen int NOT NULL
  cVisibleBranchesLst nvarchar(1024) NULL
  cVisibleBranchesLstInd nvarchar(1024) NULL
  cVisibleWarehousesLst nvarchar(1024) NULL
  cVisibleWarehousesLstInd nvarchar(1024) NULL
  cAccessProcessFlowIDLst varchar(1024) NULL
  cAccessProcessFlowChkLstInd char(1) NOT NULL
  cEmailSignature varchar(max) NULL

## _wtblIPadDetails
PK: idIPadNumber
Columns (12):
  idIPadNumber bigint NOT NULL identity PK
  cCode nvarchar(18) NULL
  cDescription nvarchar(50) NULL
  cUDID nvarchar(50) NULL
  cAutoNumber nvarchar(50) NULL
  dtTimeStamp datetime NULL
  dtCreatedDt datetime NULL
  dtModifiedDt datetime NULL
  iCreatedAgentId int NULL
  iModifiedAgentId int NULL
  iDeviceType int NOT NULL default (0)
  bIsActive bit NOT NULL default (1)

## _wtblIPadUser
PK: idIPadUser
Columns (16):
  idIPadUser bigint NOT NULL identity PK
  iAgentId bigint NOT NULL
  bIsUserRoleMgmt bit NOT NULL
  bIsActive bit NOT NULL
  dtCreatedDt datetime NULL
  dtModifiedDt datetime NULL
  iCreatedAgentId int NULL
  iModifiedAgentId int NULL
  iModuleType int NOT NULL
  iDefSalesRepID int NULL
  iDefWarehouseID int NULL
  iAssignedIPadID bigint NULL
  bAllCustomers bit NULL
  iSalesWarehouseID int NULL
  iTrCodeID int NULL
  bUseInvoice bit NULL default (0)

## _wtblMapIPadUserToInvCount
PK: idIPadInvCount
Columns (13):
  idIPadInvCount int NOT NULL identity PK
  iIPadUserId bigint NOT NULL
  iInvCountID int NOT NULL
  iStatusId int NULL
  _wtblMapIPadUserToInvCount_iBranchID int NULL
  _wtblMapIPadUserToInvCount_dCreatedDate datetime NULL
  _wtblMapIPadUserToInvCount_dModifiedDate datetime NULL
  _wtblMapIPadUserToInvCount_iCreatedBranchID int NULL
  _wtblMapIPadUserToInvCount_iModifiedBranchID int NULL
  _wtblMapIPadUserToInvCount_iCreatedAgentID int NULL
  _wtblMapIPadUserToInvCount_iModifiedAgentID int NULL
  _wtblMapIPadUserToInvCount_iChangeSetID int NULL
  _wtblMapIPadUserToInvCount_Checksum binary(20) NULL

## _wtblPEMMobilityModules
PK: idMobilityModule
Columns (10):
  idMobilityModule int NOT NULL identity PK
  cCode nvarchar(50) NOT NULL
  cName nvarchar(50) NOT NULL
  cDescription nvarchar(max) NOT NULL
  iModuleTypeId int NOT NULL
  gIdentifier uniqueidentifier NULL
  bIsWinjitModule bit NOT NULL
  bIsOneAgentPerDevice bit NOT NULL
  bIsMultipleDevicePerAgent bit NOT NULL
  bIsActive bit NOT NULL

## _wtblSystem
PK: idSystem
Columns (3):
  idSystem int NOT NULL identity PK
  cIdentity varchar(35) NULL
  cValue varchar(1024) NULL

## Accounts20250825
PK: none
Columns (80):
  AccountLink int NOT NULL identity
  Master_Sub_Account varchar(91) NULL
  AccountLevel int NULL
  Account varchar(91) NULL
  iAccountType int NOT NULL
  SubAccOfLink int NULL
  Dept varchar(10) NULL
  Brch varchar(10) NULL
  Jr bit NOT NULL
  Description varchar(255) NULL
  CaseAcc varchar(10) NULL
  ActiveAccount bit NOT NULL
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
  iAllowICSales bit NOT NULL
  iAllowICPurchases bit NOT NULL
  iMBReportingCategoryID int NULL
  iMBCashFlowCategoryID int NULL
  bMBIsAsset bit NOT NULL
  bMBIsGrant bit NOT NULL
  iMBAssetClassificationID int NULL
  iMBAssetCategoryID int NULL
  iMBAssetTypeID int NULL
  iMBGrantLevel1TypeID int NULL
  iMBGrantLevel2TypeID int NULL
  iMBGrantLevel3TypeID int NULL
  bIsBranchLoanAccount bit NOT NULL
  bForeignBankAcc bit NOT NULL
  iForeignBankCurrencyID int NULL
  iForeignBankPEXAccID int NULL
  iForeignBankLEXAccID int NULL
  bRevalueWithSellingRate bit NOT NULL
  bPaymentsBasedTax bit NOT NULL
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
  iAttributeGroupID int NOT NULL
  xAttribute xml NULL
  cSBFBankAccountID varchar(100) NULL

## StkItem_20260417
PK: none
Columns (80):
  StockLink int NOT NULL identity
  Code varchar(400) NULL
  Description_1 varchar(50) NULL
  Description_2 varchar(50) NULL
  Description_3 varchar(50) NULL
  ServiceItem bit NOT NULL
  ItemActive bit NOT NULL
  WhseItem bit NOT NULL
  SerialItem bit NOT NULL
  DuplicateSN bit NOT NULL
  StrictSN bit NOT NULL
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
  bCommissionItem bit NOT NULL
  bLotItem bit NOT NULL
  iLotStatus int NULL
  bLotMustExpire bit NOT NULL
  iItemCostingMethod int NOT NULL
  iEUCommodityID int NOT NULL
  iEUSupplementaryUnitID int NOT NULL
  fNetMass float NOT NULL
  iUOMStockingUnitID int NULL
  iUOMDefPurchaseUnitID int NULL
  iUOMDefSellUnitID int NULL
  fStockGPPercent real NULL
  cEachDescription varchar(30) NULL
  cMeasurement varchar(5) NULL
  fBuyLength float NULL
  fBuyWidth float NULL
  fBuyHeight float NULL
  fBuyArea float NULL
  fBuyVolume float NULL
  cBuyWeight float NULL
  cBuyUnit varchar(5) NULL
  fSellLength float NULL
  fSellWidth float NULL
  fSellHeight float NULL
  fSellArea float NULL
  fSellVolume float NULL
  cSellWeight float NULL
  cSellUnit varchar(5) NULL
  bOverrideSell bit NULL
  bUOMItem bit NOT NULL
  bDimensionItem bit NOT NULL
  bVASItem bit NOT NULL
  bAirtimeItem bit NOT NULL
  StkItem_iBranchID int NULL
  StkItem_dCreatedDate datetime NULL
  StkItem_dModifiedDate datetime NULL
  StkItem_iCreatedBranchID int NULL
  StkItem_iModifiedBranchID int NULL
  StkItem_iCreatedAgentID int NULL
  StkItem_iModifiedAgentID int NULL
  StkItem_iChangeSetID int NULL
  StkItem_Checksum binary(20) NULL
  bSyncToSOT bit NOT NULL
  bImportedServices bit NOT NULL
  ucIIAIC varchar(30) NULL
  ucIISUPPLIER varchar(50) NULL
  ucIIWEIGHT varchar(30) NULL
  ucIIWIDTH varchar(30) NULL
  ucIIMONTHFOR varchar(30) NULL
  iAttributeGroupID int NOT NULL
  xAttribute xml NULL
  iMajorIndustryCodeID int NULL

## syncChecksums
PK: none
Columns (3):
  idSyncDefinition int NOT NULL identity
  cTableName varchar(80) NULL
  cChecksumFields varchar(200) NULL

## tbltrackid
PK: none
Columns (3):
  ID int NOT NULL
  Qty float NULL
  AutoIDx int NOT NULL identity

## Thyme_StkItemBackup
PK: none
Columns (80):
  StockLink int NOT NULL identity
  Code varchar(400) NULL
  Description_1 varchar(50) NULL
  Description_2 varchar(50) NULL
  Description_3 varchar(50) NULL
  ServiceItem bit NOT NULL
  ItemActive bit NOT NULL
  WhseItem bit NOT NULL
  SerialItem bit NOT NULL
  DuplicateSN bit NOT NULL
  StrictSN bit NOT NULL
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
  bCommissionItem bit NOT NULL
  bLotItem bit NOT NULL
  iLotStatus int NULL
  bLotMustExpire bit NOT NULL
  iItemCostingMethod int NOT NULL
  iEUCommodityID int NOT NULL
  iEUSupplementaryUnitID int NOT NULL
  fNetMass float NOT NULL
  iUOMStockingUnitID int NULL
  iUOMDefPurchaseUnitID int NULL
  iUOMDefSellUnitID int NULL
  fStockGPPercent real NULL
  cEachDescription varchar(30) NULL
  cMeasurement varchar(5) NULL
  fBuyLength float NULL
  fBuyWidth float NULL
  fBuyHeight float NULL
  fBuyArea float NULL
  fBuyVolume float NULL
  cBuyWeight float NULL
  cBuyUnit varchar(5) NULL
  fSellLength float NULL
  fSellWidth float NULL
  fSellHeight float NULL
  fSellArea float NULL
  fSellVolume float NULL
  cSellWeight float NULL
  cSellUnit varchar(5) NULL
  bOverrideSell bit NULL
  bUOMItem bit NOT NULL
  bDimensionItem bit NOT NULL
  bVASItem bit NOT NULL
  bAirtimeItem bit NOT NULL
  StkItem_iBranchID int NULL
  StkItem_dCreatedDate datetime NULL
  StkItem_dModifiedDate datetime NULL
  StkItem_iCreatedBranchID int NULL
  StkItem_iModifiedBranchID int NULL
  StkItem_iCreatedAgentID int NULL
  StkItem_iModifiedAgentID int NULL
  StkItem_iChangeSetID int NULL
  StkItem_Checksum binary(20) NULL
  bSyncToSOT bit NOT NULL
  bImportedServices bit NOT NULL
  ucIIAIC varchar(30) NULL
  ucIISUPPLIER varchar(50) NULL
  ucIIWEIGHT varchar(30) NULL
  ucIIWIDTH varchar(30) NULL
  ucIIMONTHFOR varchar(30) NULL
  iAttributeGroupID int NOT NULL
  xAttribute xml NULL
  iMajorIndustryCodeID int NULL
