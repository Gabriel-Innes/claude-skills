# Sage 200 Evolution table dictionary - Add on modules

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _iotblDefaults
PK: IdDefaults
Columns (78):
  IdDefaults int NOT NULL identity PK
  iNextAutoNumIB int NOT NULL
  iPadToIB int NOT NULL
  cPrefixIB nvarchar(3) NULL
  bAutoNumIB bit NOT NULL
  bUniqueNumIB bit NOT NULL
  iNextAutoNumIBR int NOT NULL
  iPadToIBR int NOT NULL
  cPrefixIBR nvarchar(3) NULL
  bAutoNumIBR bit NOT NULL
  bUniqueNumIBR bit NOT NULL
  bAutoPO bit NOT NULL
  cCategory1 nvarchar(30) NULL default (0)
  cCategory2 nvarchar(30) NULL default (0)
  cCategory3 nvarchar(30) NULL default (0)
  cCategory4 nvarchar(30) NULL default (0)
  cCategory5 nvarchar(30) NULL default (0)
  bInUseCat1 bit NULL default (0)
  bInUseCat2 bit NULL default (0)
  bInUseCat3 bit NULL default (0)
  bInUseCat4 bit NULL default (0)
  bInUseCat5 bit NULL default (0)
  iCat1From int NULL default (0)
  iCat1To int NULL default (0)
  iCat2From int NULL default (0)
  iCat2To int NULL default (0)
  iCat3From int NULL default (0)
  iCat3To int NULL default (0)
  iCat4From int NULL default (0)
  iCat4To int NULL default (0)
  iCat5From int NULL default (0)
  iCat5To int NULL default (0)
  fNewReOrdLvlCat1 float NULL default (0)
  fNewReOrdLvlCat2 float NULL default (0)
  fNewReOrdLvlCat3 float NULL default (0)
  fNewReOrdLvlCat4 float NULL default (0)
  fNewReOrdLvlCat5 float NULL default (0)
  fNewReOrdQtyCat1 float NULL default (0)
  fNewReOrdQtyCat2 float NULL default (0)
  fNewReOrdQtyCat3 float NULL default (0)
  fNewReOrdQtyCat4 float NULL default (0)
  fNewReOrdQtyCat5 float NULL default (0)
  fNewMinLvlCat1 float NULL default (0)
  fNewMinLvlCat2 float NULL default (0)
  fNewMinLvlCat3 float NULL default (0)
  fNewMinLvlCat4 float NULL default (0)
  fNewMinLvlCat5 float NULL default (0)
  fNewMaxLvlCat1 float NULL default (0)
  fNewMaxLvlCat2 float NULL default (0)
  fNewMaxLvlCat3 float NULL default (0)
  fNewMaxLvlCat4 float NULL default (0)
  fNewMaxLvlCat5 float NULL default (0)
  iUsageCalcRnd int NULL default (0)
  fUsageCalcPercentage float NULL default (0)
  iLevelUpdateRnd int NULL default (0)
  fLevelUpdatePercentage float NULL default (0)
  bUsagePerDay bit NULL default (0)
  fSpikePer float NULL default (0)
  cSpikeColour nvarchar(100) NULL
  iUsageInterval int NULL default (0)
  iLastTransDays int NULL default (0)
  iNextAutoNumTemp int NOT NULL default (0)
  iPadToTemp int NOT NULL default (0)
  cPrefixTemp nvarchar(3) NULL
  bAutoNumTemp bit NOT NULL default (0)
  bUniqueNumTemp bit NOT NULL default (0)
  iDecSellPrice int NULL default (0)
  iDecCostPrice int NULL default (0)
  iDecQuantities int NULL default (0)
  _iotblDefaults_iBranchID int NULL
  _iotblDefaults_dCreatedDate datetime NULL
  _iotblDefaults_dModifiedDate datetime NULL
  _iotblDefaults_iCreatedBranchID int NULL
  _iotblDefaults_iModifiedBranchID int NULL
  _iotblDefaults_iCreatedAgentID int NULL
  _iotblDefaults_iModifiedAgentID int NULL
  _iotblDefaults_iChangeSetID int NULL
  _iotblDefaults_Checksum binary(20) NULL

## _iotblReorderBatch
PK: idReorderBatch
Columns (14):
  idReorderBatch int NOT NULL identity PK
  cBatchNumber nvarchar(50) NULL
  dBatchDate smalldatetime NULL
  iTemplateId int NOT NULL
  bArchived bit NULL
  _iotblReorderBatch_iBranchID int NULL
  _iotblReorderBatch_dCreatedDate datetime NULL
  _iotblReorderBatch_dModifiedDate datetime NULL
  _iotblReorderBatch_iCreatedBranchID int NULL
  _iotblReorderBatch_iModifiedBranchID int NULL
  _iotblReorderBatch_iCreatedAgentID int NULL
  _iotblReorderBatch_iModifiedAgentID int NULL
  _iotblReorderBatch_iChangeSetID int NULL
  _iotblReorderBatch_Checksum binary(20) NULL

## _iotblReorderBatchLines
PK: iReorderBatchLineId
Columns (75):
  iReorderBatchLineId int NOT NULL identity PK
  iReorderBatchId int NOT NULL
  bInclude bit NULL
  cItemCode nvarchar(400) NULL
  cItemDescription nvarchar(50) NULL
  cDescription nvarchar(50) NULL
  cSalesOrder nvarchar(50) NULL
  dSalesOrderDate smalldatetime NULL
  fSalesOrderQty float NULL
  iUsageWarehouseId int NULL
  iPOWarehouseId int NULL
  fUsage float NULL
  fUsagePerDay float NULL
  fQtyOnHand float NULL
  fQtyOnStock float NULL
  fQtyAvailable float NULL
  fQtyOnPO float NULL
  fQtyOnSO float NULL
  fQtyReserved float NULL
  fQtyOnJob float NULL
  fQtyMF float NULL
  fReorderLevel float NULL
  fReorderQty float NULL
  fMinLevel float NULL
  fMaxLevel float NULL
  cCostingMethod nvarchar(50) NULL
  fAverageCost float NULL
  fLatestCost float NULL
  fHighestCost float NULL
  fLowestCost float NULL
  fManualCost float NULL
  fLastGRVCost float NULL
  iPreferredSupplier int NULL
  iPOSupplier int NULL
  fLeadTimeItem float NULL
  fLeadTimeDemandItem float NULL
  fSupplierLeadeTime float NULL
  fLeadTimeDemandSupplier float NULL
  fWarehouseLeadTime float NULL
  fLeadTimeDemandWarehouse float NULL
  iProject int NULL
  fSuggestedPOQty float NULL
  fPrice float NULL
  fExchangeRate float NULL
  fForeignPrice float NULL
  fLineTotal float NULL
  cUnit nvarchar(50) NULL
  iDeliveryMethodId int NULL
  iPriorityId int NULL
  iStatusId int NULL
  cOrderDescription nvarchar(100) NULL
  iStockLink int NULL
  iWhseLink int NULL
  bProcessed bit NULL
  cItemGroup nvarchar(20) NULL
  cBinLocationName nvarchar(20) NULL
  cBarCode nvarchar(30) NULL
  cDescription_3 nvarchar(50) NULL
  cPack nvarchar(20) NULL
  cPackDescription nvarchar(50) NULL
  fPackSize float NULL default (0)
  fNewReorderLevel float NULL default (0)
  fNewReorderQty float NULL default (0)
  fNewMinLevel float NULL default (0)
  fNewMaxLevel float NULL default (0)
  cCategory nvarchar(20) NULL
  _iotblReorderBatchLines_iBranchID int NULL
  _iotblReorderBatchLines_dCreatedDate datetime NULL
  _iotblReorderBatchLines_dModifiedDate datetime NULL
  _iotblReorderBatchLines_iCreatedBranchID int NULL
  _iotblReorderBatchLines_iModifiedBranchID int NULL
  _iotblReorderBatchLines_iCreatedAgentID int NULL
  _iotblReorderBatchLines_iModifiedAgentID int NULL
  _iotblReorderBatchLines_iChangeSetID int NULL
  _iotblReorderBatchLines_Checksum binary(20) NULL

## _iotblSystemStructure
PK: AutoIdx
Columns (6):
  AutoIdx int NOT NULL PK
  iParentId int NULL
  iImageIndex int NULL
  cDisplayText nvarchar(50) NULL
  cModuleName nvarchar(50) NULL
  iOrder int NULL

## _iotblTemplateMaster
PK: idReorderTemplate
Columns (107):
  idReorderTemplate int NOT NULL identity PK
  cTempName nvarchar(50) NOT NULL
  cTempDescription nvarchar(200) NULL
  dTempDate date NULL
  iTransFromDays int NULL
  cTransCodes nvarchar(max) NULL
  cTransSource nvarchar(max) NULL
  iInvItemFromId int NULL
  iInvItemToId int NULL
  bIgnoreInactiveItem bit NULL
  cInvGroups nvarchar(max) NULL
  cInvPacks nvarchar(max) NULL
  cInvBinLocations nvarchar(max) NULL
  cInvWarehouses nvarchar(max) NULL
  cInvFilterCriteria nvarchar(max) NULL
  iSoNoFromId int NULL
  iSoNoToId int NULL
  cSoStatus nvarchar(50) NULL
  bSoIgnoreInactiveProject bit NULL
  cSoProjects nvarchar(max) NULL
  cSoForeignCurr nvarchar(max) NULL
  bSoUnconfirmed bit NULL
  bSoPartConfirmed bit NULL
  bSoMerged bit NULL
  iSoFromDays int NULL
  iSoFilterBy int NULL
  iBomItemFromId int NULL
  iBomItemToId int NULL
  cBomReference nvarchar(max) NULL
  cBomExtReference nvarchar(max) NULL
  iBomFromDays int NULL
  cBomProjects nvarchar(max) NULL
  cInvForecastFormula nvarchar(max) NULL
  dPoDate date NULL
  cPoDescription nvarchar(100) NULL
  iPoDeliveryMethodId int NULL
  iPoStatusId int NULL
  iPoPriorityId int NULL
  iPoProjectId int NULL
  iPoWarehouseId int NULL
  bIncludePOQty bit NULL default (0)
  bSkipSO bit NULL default (1)
  iSupplierFromId int NULL default (0)
  iSupplierToId int NULL default (0)
  bIgnoreOnHoldSuppAcc bit NULL default (1)
  cSuppGroups nvarchar(max) NULL default (0)
  cSuppAreas nvarchar(max) NULL default (0)
  bIgnoreBOMCompItem bit NULL default (1)
  bIncludeZeroUsageItem bit NOT NULL default (1)
  cInvItemFrom nvarchar(400) NULL default (0)
  cInvItemTo nvarchar(400) NULL default (0)
  cBomItemFrom nvarchar(400) NULL default (0)
  cBomItemTo nvarchar(400) NULL default (0)
  cSupplierFrom nvarchar(400) NULL default (0)
  cSupplierTo nvarchar(400) NULL default (0)
  bUsedForReorder bit NULL default (1)
  cCategory1 nvarchar(30) NULL default (0)
  cCategory2 nvarchar(30) NULL default (0)
  cCategory3 nvarchar(30) NULL default (0)
  cCategory4 nvarchar(30) NULL default (0)
  cCategory5 nvarchar(30) NULL default (0)
  iCat1From int NULL default (0)
  iCat1To int NULL default (0)
  iCat2From int NULL default (0)
  iCat2To int NULL default (0)
  iCat3From int NULL default (0)
  iCat3To int NULL default (0)
  iCat4From int NULL default (0)
  iCat4To int NULL default (0)
  iCat5From int NULL default (0)
  iCat5To int NULL default (0)
  fNewReOrdLvlCat1 float NULL default (1)
  fNewReOrdLvlCat2 float NULL default (1)
  fNewReOrdLvlCat3 float NULL default (1)
  fNewReOrdLvlCat4 float NULL default (1)
  fNewReOrdLvlCat5 float NULL default (1)
  fNewReOrdQtyCat1 float NULL default (1)
  fNewReOrdQtyCat2 float NULL default (1)
  fNewReOrdQtyCat3 float NULL default (1)
  fNewReOrdQtyCat4 float NULL default (1)
  fNewReOrdQtyCat5 float NULL default (1)
  fNewMinLvlCat1 float NULL default (1)
  fNewMinLvlCat2 float NULL default (1)
  fNewMinLvlCat3 float NULL default (1)
  fNewMinLvlCat4 float NULL default (1)
  fNewMinLvlCat5 float NULL default (1)
  fNewMaxLvlCat1 float NULL default (1)
  fNewMaxLvlCat2 float NULL default (1)
  fNewMaxLvlCat3 float NULL default (1)
  fNewMaxLvlCat4 float NULL default (1)
  fNewMaxLvlCat5 float NULL default (1)
  dTransDateFrom datetime NULL
  dTransDateTo datetime NULL
  bUsagePerDay bit NULL default (0)
  dCreatedDate datetime NULL default (0)
  dModifiedDate datetime NULL default (0)
  iCreatedAgentID int NULL default (0)
  iModifiedAgentID int NULL default (0)
  _iotblTemplateMaster_iBranchID int NULL
  _iotblTemplateMaster_dCreatedDate datetime NULL
  _iotblTemplateMaster_dModifiedDate datetime NULL
  _iotblTemplateMaster_iCreatedBranchID int NULL
  _iotblTemplateMaster_iModifiedBranchID int NULL
  _iotblTemplateMaster_iCreatedAgentID int NULL
  _iotblTemplateMaster_iModifiedAgentID int NULL
  _iotblTemplateMaster_iChangeSetID int NULL
  _iotblTemplateMaster_Checksum binary(20) NULL

## _iotblWorkGrp
PK: iWorkGrpId
Columns (13):
  iWorkGrpId int NOT NULL identity PK
  Descrip nvarchar(100) NULL
  GrpList text NULL
  iRecordType int NULL default (0)
  _iotblWorkGrp_iBranchID int NULL
  _iotblWorkGrp_dCreatedDate datetime NULL
  _iotblWorkGrp_dModifiedDate datetime NULL
  _iotblWorkGrp_iCreatedBranchID int NULL
  _iotblWorkGrp_iModifiedBranchID int NULL
  _iotblWorkGrp_iCreatedAgentID int NULL
  _iotblWorkGrp_iModifiedAgentID int NULL
  _iotblWorkGrp_iChangeSetID int NULL
  _iotblWorkGrp_Checksum binary(20) NULL

## _simtblDefaults
PK: none
Columns (33):
  bGeneralLedger bit NULL
  bJobCards bit NULL
  bProject bit NULL
  cStockIssue_Trans varchar(50) NULL
  cStockCredit_Trans varchar(50) NULL
  cIncidentType varchar(50) NULL
  bAllowStock_requistion bit NULL
  bStockAuto_Numbering bit NULL
  cStockPrefix nvarchar(25) NULL
  iStock_PadtoNumber int NULL
  iStockNextNumber int NULL
  bStockUniqueNumber bit NULL
  bIssueAuto_Numbering bit NULL
  cIssuePrefix nvarchar(25) NULL
  iIssue_PadtoNumber int NULL
  iIssueNextNumber int NULL
  bIssueUniqueNumber bit NULL
  bTemplateAutoNumbering bit NULL
  cTemplatePrefix nvarchar(25) NULL
  iTemplate_PadtoNumber int NULL
  iTemplateNextNumber int NULL
  bTemplateUniqueNumber bit NULL
  iTrcode int NULL
  bUseWorkFlow bit NULL
  _simtblDefaults_iBranchID int NULL
  _simtblDefaults_dCreatedDate datetime NULL
  _simtblDefaults_dModifiedDate datetime NULL
  _simtblDefaults_iCreatedBranchID int NULL
  _simtblDefaults_iModifiedBranchID int NULL
  _simtblDefaults_iCreatedAgentID int NULL
  _simtblDefaults_iModifiedAgentID int NULL
  _simtblDefaults_iChangeSetID int NULL
  _simtblDefaults_Checksum binary(20) NULL

## _simtblReportLayout
PK: none
Columns (18):
  idReportLayout int NOT NULL identity
  cRptDescription varchar(80) NOT NULL
  iModuleId int NULL
  iVersion int NULL
  nLayout varbinary(max) NOT NULL
  bReadOnly bit NOT NULL
  bIsDefaultLayout bit NULL
  bIsStandard int NULL
  cRptTypeDescription varchar(80) NULL
  _simtblReportLayout_iBranchID int NULL
  _simtblReportLayout_dCreatedDate datetime NULL
  _simtblReportLayout_dModifiedDate datetime NULL
  _simtblReportLayout_iCreatedBranchID int NULL
  _simtblReportLayout_iModifiedBranchID int NULL
  _simtblReportLayout_iCreatedAgentID int NULL
  _simtblReportLayout_iModifiedAgentID int NULL
  _simtblReportLayout_iChangeSetID int NULL
  _simtblReportLayout_Checksum binary(20) NULL

## _simtblReqHeader
PK: idReqHeader
Columns (17):
  idReqHeader int NOT NULL identity PK
  cRequisitionNo nvarchar(50) NULL
  dRequisitionDate datetime NULL
  iProjectDefaultID int NULL
  cRequestedBy nvarchar(50) NULL
  iIncidentTypeDefaultID int NULL
  iStatus int NULL
  iAgentID int NULL
  _simtblReqHeader_iBranchID int NULL
  _simtblReqHeader_dCreatedDate datetime NULL
  _simtblReqHeader_dModifiedDate datetime NULL
  _simtblReqHeader_iCreatedBranchID int NULL
  _simtblReqHeader_iModifiedBranchID int NULL
  _simtblReqHeader_iCreatedAgentID int NULL
  _simtblReqHeader_iModifiedAgentID int NULL
  _simtblReqHeader_iChangeSetID int NULL
  _simtblReqHeader_Checksum binary(20) NULL

## _simtblReqLines
PK: idReqLines
Columns (40):
  idReqLines int NOT NULL identity PK
  fk_idReqHeader int NULL
  iStockId int NULL
  cDescription nvarchar(max) NULL
  iReqStatus int NULL
  dSartDate datetime NULL
  dEndDate datetime NULL
  fUnitCost float NULL
  iUnitOfMeasure int NULL
  iWarehouseId int NULL
  fLineTotalCost float NULL
  bIsprocessed bit NULL
  fConfirmQty float NULL
  bIswarehouse bit NULL
  cType nchar(50) NULL
  cTypeDetails int NULL
  iTrcodeId int NULL
  iIncidentTypeID int NULL
  iProjectID int NULL
  iAgentID int NULL
  iLineNo int NULL
  iTaxType int NULL
  fk_iIncidentId int NULL
  iStockingUnitID int NULL default (0)
  iUnitCategoryID int NULL default (0)
  iStockingUnitCategoryID int NULL default (0)
  bIsLot bit NULL default (0)
  bIsSerialItem bit NULL default (0)
  iAttributeGroupID int NULL
  xAttribute xml NULL
  iStockBinLocationID int NOT NULL default (0)
  _simtblReqLines_iBranchID int NULL
  _simtblReqLines_dCreatedDate datetime NULL
  _simtblReqLines_dModifiedDate datetime NULL
  _simtblReqLines_iCreatedBranchID int NULL
  _simtblReqLines_iModifiedBranchID int NULL
  _simtblReqLines_iCreatedAgentID int NULL
  _simtblReqLines_iModifiedAgentID int NULL
  _simtblReqLines_iChangeSetID int NULL
  _simtblReqLines_Checksum binary(20) NULL

## _simtblStkIssueLines
PK: iAutoIdx
Columns (37):
  iAutoIdx int NOT NULL identity PK
  iStkIssueId int NULL
  iStkIssueTaxTpId int NULL
  iStockId int NULL
  cDescription nvarchar(max) NULL
  iStatus int NULL
  fUnitCost float NULL
  iUnitOfMeasure int NULL
  iWarehouseId int NULL
  fLineTotalCost float NULL
  bIsprocessed bit NULL
  fConfirmQty float NULL
  bIswarehouse bit NULL
  cType nchar(50) NULL
  cTypeDetails nchar(50) NULL
  cProject nchar(50) NULL
  iTrcodeId int NULL
  bIsLot bit NULL
  iLotNumber int NULL
  iProjectId int NULL
  iStockingUnitID int NULL default (0)
  iUnitCategoryID int NULL default (0)
  iStockingUnitCategoryID int NULL default (0)
  bIsSerialItem bit NULL default (0)
  dLotExpiryDate datetime NULL
  iAttributeGroupID int NULL
  xAttribute xml NULL
  iStockBinLocationID int NOT NULL default (0)
  _simtblStkIssueLines_iBranchID int NULL
  _simtblStkIssueLines_dCreatedDate datetime NULL
  _simtblStkIssueLines_dModifiedDate datetime NULL
  _simtblStkIssueLines_iCreatedBranchID int NULL
  _simtblStkIssueLines_iModifiedBranchID int NULL
  _simtblStkIssueLines_iCreatedAgentID int NULL
  _simtblStkIssueLines_iModifiedAgentID int NULL
  _simtblStkIssueLines_iChangeSetID int NULL
  _simtblStkIssueLines_Checksum binary(20) NULL

## _simtblStockIssueLineSN
PK: idStockIssueLineSN
Columns (14):
  idStockIssueLineSN int NOT NULL identity PK
  iSerialStockIssueID int NOT NULL
  iSerialStockIssueLineID bigint NOT NULL
  cSerialNumber nvarchar(50) NULL
  iSerialMFID int NOT NULL
  _simtblStockIssueLineSN_iBranchID int NULL
  _simtblStockIssueLineSN_dCreatedDate datetime NULL
  _simtblStockIssueLineSN_dModifiedDate datetime NULL
  _simtblStockIssueLineSN_iCreatedBranchID int NULL
  _simtblStockIssueLineSN_iModifiedBranchID int NULL
  _simtblStockIssueLineSN_iCreatedAgentID int NULL
  _simtblStockIssueLineSN_iModifiedAgentID int NULL
  _simtblStockIssueLineSN_iChangeSetID int NULL
  _simtblStockIssueLineSN_Checksum binary(20) NULL

## _simtblStockIssueMaster
PK: iStkIssueId
Columns (21):
  iStkIssueId int NOT NULL identity PK
  cStkIssueNumber nvarchar(50) NULL
  cDescripton nvarchar(max) NULL
  cType nchar(10) NULL
  iStatus int NULL
  dIssueDate datetime NULL
  iProjectId int NULL
  bIsTemplate bit NULL
  cTemplateId nvarchar(20) NULL
  cTemplateDescription nvarchar(20) NULL
  iRequisitionId int NOT NULL default (0)
  cRequestedBy nvarchar(50) NULL
  _simtblStockIssueMaster_iBranchID int NULL
  _simtblStockIssueMaster_dCreatedDate datetime NULL
  _simtblStockIssueMaster_dModifiedDate datetime NULL
  _simtblStockIssueMaster_iCreatedBranchID int NULL
  _simtblStockIssueMaster_iModifiedBranchID int NULL
  _simtblStockIssueMaster_iCreatedAgentID int NULL
  _simtblStockIssueMaster_iModifiedAgentID int NULL
  _simtblStockIssueMaster_iChangeSetID int NULL
  _simtblStockIssueMaster_Checksum binary(20) NULL

## _smtblAgentRights
PK: none
Columns (13):
  AutoIdx int NULL
  iModuleId int NULL
  iAgentId int NULL
  bAdd bit NULL
  bDelete bit NULL
  bEdit bit NULL
  bView bit NULL
  _smtblAgentRights_iBranchID int NOT NULL default '0'
  _smtblAgentRights_iCreatedBranchID int NOT NULL default '0'
  _smtblAgentRights_iCreatedAgentID int NOT NULL default '0'
  _smtblAgentRights_iModifiedAgentID int NOT NULL default '0'
  _smtblAgentRights_iModifiedBranchID int NOT NULL default '0'
  _smtblAgentRights_dModifiedDate datetime NULL

## _smtblBullDocNotes
PK: AutoIdx | UNIQUE: cTitle+cType+iModuleId+cModuleName
Columns (17):
  AutoIdx bigint NOT NULL identity PK
  cTitle varchar(50) NULL
  cDescription varchar(max) NULL
  cAddInfo varchar(500) NULL
  cModuleName varchar(20) NOT NULL
  iModuleId bigint NOT NULL
  dtStamp datetime NOT NULL default getdate()
  iUserId int NOT NULL
  bDeleted bit NOT NULL
  cType varchar(10) NOT NULL
  bActive bit NULL
  _smtblBullDocNotes_iBranchID int NOT NULL default '0'
  _smtblBullDocNotes_iCreatedBranchID int NOT NULL default '0'
  _smtblBullDocNotes_iCreatedAgentID int NOT NULL default '0'
  _smtblBullDocNotes_iModifiedAgentID int NOT NULL default '0'
  _smtblBullDocNotes_iModifiedBranchID int NOT NULL default '0'
  _smtblBullDocNotes_dModifiedDate datetime NULL

## _smtblCodeMaster
PK: AutoIdx | UNIQUE: cCode+cType
Columns (18):
  AutoIdx int NOT NULL identity PK
  cCode varchar(50) NULL
  cDescription varchar(max) NULL
  cType varchar(50) NOT NULL
  bDeleted bit NOT NULL
  dtStamp datetime NOT NULL default getdate()
  iUserId bigint NULL
  cColor varchar(50) NULL
  iParentId int NULL
  bStatus bit NULL
  fCost float NULL
  _smtblCodeMaster_iBranchID int NOT NULL default '0'
  _smtblCodeMaster_iCreatedBranchID int NOT NULL default '0'
  _smtblCodeMaster_iCreatedAgentID int NOT NULL default '0'
  _smtblCodeMaster_iModifiedAgentID int NOT NULL default '0'
  _smtblCodeMaster_iModifiedBranchID int NOT NULL default '0'
  _smtblCodeMaster_dModifiedDate datetime NULL
  iServiceItemID numeric(10,0) NULL

## _smtblContractMatrix
PK: AutoIdx
Columns (26):
  AutoIdx int NOT NULL identity PK
  cCode varchar(50) NULL
  cDescription varchar(500) NULL
  dCreationDate datetime NULL
  dReviewDate datetime NULL
  dStartDate datetime NULL
  dEndDate datetime NULL
  cContractDetails varchar(max) NULL
  cAlerts varchar(max) NULL
  bDeleted bit NULL
  iUserId int NULL
  dtStamp datetime NULL default getdate()
  iContractTemplateId int NULL
  iCustomerId int NULL
  bContract bit NULL
  iContractLenType int NULL
  iContractLen int NULL
  iReviewPeriodType int NULL
  iReviewPeriod int NULL
  cServiceAssetId varchar(max) NULL
  _smtblContractMatrix_iBranchID int NOT NULL default '0'
  _smtblContractMatrix_iCreatedBranchID int NOT NULL default '0'
  _smtblContractMatrix_iCreatedAgentID int NOT NULL default '0'
  _smtblContractMatrix_iModifiedAgentID int NOT NULL default '0'
  _smtblContractMatrix_iModifiedBranchID int NOT NULL default '0'
  _smtblContractMatrix_dModifiedDate datetime NULL

## _smtblContractMatrixChargeRates
PK: AutoIdx | UNIQUE: iContractMatrixId+iWorkTypeId
Columns (14):
  AutoIdx int NOT NULL identity PK
  iContractMatrixId int NULL
  iWorkTypeId int NULL
  fRateIncl float NULL
  fRateExcl float NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  iUserId int NULL
  _smtblContractMatrixChargeRates_iBranchID int NOT NULL default '0'
  _smtblContractMatrixChargeRates_iCreatedBranchID int NOT NULL default '0'
  _smtblContractMatrixChargeRates_iCreatedAgentID int NOT NULL default '0'
  _smtblContractMatrixChargeRates_iModifiedAgentID int NOT NULL default '0'
  _smtblContractMatrixChargeRates_iModifiedBranchID int NOT NULL default '0'
  _smtblContractMatrixChargeRates_dModifiedDate datetime NULL

## _smtblContractMatrixCounterElapsed
PK: AutoIdx | UNIQUE: cCode+cType+iContractMatrixID
Columns (32):
  AutoIdx int NOT NULL identity PK
  iServiceAssetId int NULL
  cCode varchar(50) NULL
  cDescription varchar(200) NULL
  fCurrentReading float NULL
  dCurrentReadingDate datetime NULL
  fPreviousReading float NULL
  dPreviousReadingDate datetime NULL
  fLastBillReading float NULL
  dLastBillReadingDate datetime NULL
  fWarningLevel float NULL
  bWarningActive bit NULL
  cMessage varchar(500) NULL
  cType varchar(10) NULL
  fTotalUnits float NULL
  fUnitsRemaining float NULL
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  iContractMatrixID int NULL
  cMeterType varchar(300) NULL
  cMeterDesc varchar(500) NULL
  cNotes varchar(max) NULL
  cMeterNo varchar(100) NULL
  _smtblContractMatrixCounterElapsed_iBranchID int NOT NULL default '0'
  _smtblContractMatrixCounterElapsed_iCreatedBranchID int NOT NULL default '0'
  _smtblContractMatrixCounterElapsed_iCreatedAgentID int NOT NULL default '0'
  _smtblContractMatrixCounterElapsed_iModifiedAgentID int NOT NULL default '0'
  _smtblContractMatrixCounterElapsed_iModifiedBranchID int NOT NULL default '0'
  _smtblContractMatrixCounterElapsed_dModifiedDate datetime NULL
  iProjectId int NULL
  cExternalRef varchar(max) NULL

## _smtblContractMatrixPeriodService
PK: AutoIdx | UNIQUE: cCode+cType+iServiceAssetId+iContractMatrixID
Columns (50):
  AutoIdx int NOT NULL identity PK
  iServiceAssetId int NULL
  cCode varchar(20) NULL
  cDescription varchar(200) NULL
  fAmount float NULL
  cExternalRef varchar(max) NULL
  bInvoiceWithoutConfirmation bit NULL
  bBillInAdvance bit NULL
  cBillingSchedule varchar(10) NULL
  dNextDate datetime NULL
  iFrequency int NULL
  iJan int NULL
  iFeb int NULL
  iMar int NULL
  iApr int NULL
  iMay int NULL
  iJun int NULL
  iJul int NULL
  iAug int NULL
  iSep int NULL
  iOct int NULL
  iNov int NULL
  iDec int NULL
  dLastActionDate datetime NULL
  cNotes varchar(500) NULL
  fUsage float NULL
  ifk_UsageUnits int NULL
  cType varchar(10) NULL
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  iRequestTypeId int NULL
  iAccountId int NULL
  iContractMatrixID int NULL
  _smtblContractMatrixPeriodService_iBranchID int NOT NULL default '0'
  _smtblContractMatrixPeriodService_iCreatedBranchID int NOT NULL default '0'
  _smtblContractMatrixPeriodService_iCreatedAgentID int NOT NULL default '0'
  _smtblContractMatrixPeriodService_iModifiedAgentID int NOT NULL default '0'
  _smtblContractMatrixPeriodService_iModifiedBranchID int NOT NULL default '0'
  _smtblContractMatrixPeriodService_dModifiedDate datetime NULL
  bIsEscalation bit NULL default (0)
  fEscalationPer float NULL
  fEscalationAmt float NULL
  fEscFrequency float NULL
  fEscalationDays float NULL
  iRepeatEscType int NULL
  dStartEscalationDate datetime NULL
  bIsPercentage bit NULL
  fOriginalAmount float NULL
  iProjectId int NULL

## _smtblContractMatrixStockRates
PK: AutoIdx | UNIQUE: iContractMatrixId+iStkItemId
Columns (14):
  AutoIdx int NOT NULL identity PK
  iContractMatrixId int NULL
  iStkItemId int NULL
  fRateIncl float NULL
  fRateExcl float NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  iUserId int NULL
  _smtblContractMatrixStockRates_iBranchID int NOT NULL default '0'
  _smtblContractMatrixStockRates_iCreatedBranchID int NOT NULL default '0'
  _smtblContractMatrixStockRates_iCreatedAgentID int NOT NULL default '0'
  _smtblContractMatrixStockRates_iModifiedAgentID int NOT NULL default '0'
  _smtblContractMatrixStockRates_iModifiedBranchID int NOT NULL default '0'
  _smtblContractMatrixStockRates_dModifiedDate datetime NULL

## _smtblCounterElapsed
PK: AutoIdx | UNIQUE: cCode+cType+iServiceAssetId+iContractMatrixId
Columns (36):
  AutoIdx int NOT NULL identity PK
  iServiceAssetId int NULL
  cCode varchar(50) NULL
  cDescription varchar(200) NULL
  fCurrentReading float NULL
  dCurrentReadingDate datetime NULL
  fPreviousReading float NULL
  dPreviousReadingDate datetime NULL
  fLastBillReading float NULL
  dLastBillReadingDate datetime NULL
  fWarningLevel float NULL
  bWarningActive bit NULL
  cMessage varchar(500) NULL
  cType varchar(10) NULL - Can either be 'COU' for Counter or 'ELA' for Elapsed
  fTotalUnits float NULL
  fUnitsRemaining float NULL
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  iRefSMBillingAutoIdx int NULL
  iContractMatrixId int NULL
  cMeterType varchar(300) NULL
  cMeterDesc varchar(500) NULL
  cNotes varchar(max) NULL
  cMeterNo varchar(100) NULL
  _smtblCounterElapsed_iBranchID int NOT NULL default '0'
  _smtblCounterElapsed_iCreatedBranchID int NOT NULL default '0'
  _smtblCounterElapsed_iCreatedAgentID int NOT NULL default '0'
  _smtblCounterElapsed_iModifiedAgentID int NOT NULL default '0'
  _smtblCounterElapsed_iModifiedBranchID int NOT NULL default '0'
  _smtblCounterElapsed_dModifiedDate datetime NULL
  iMeterId int NULL
  bResetBilling bit NULL
  iProjectId int NULL
  bDisableBilling bit NOT NULL default (0)
  cExternalRef varchar(max) NULL

## _smtblCreditNoteReferences
PK: none
Columns (9):
  AutoIdx int NOT NULL identity
  iReferenceTaskID int NULL
  iRefCreditNoteId int NULL
  _smtblCreditNoteReferences_iBranchID int NOT NULL default '0'
  _smtblCreditNoteReferences_iCreatedBranchID int NOT NULL default '0'
  _smtblCreditNoteReferences_iCreatedAgentID int NOT NULL default '0'
  _smtblCreditNoteReferences_iModifiedAgentID int NOT NULL default '0'
  _smtblCreditNoteReferences_iModifiedBranchID int NOT NULL default '0'
  _smtblCreditNoteReferences_dModifiedDate datetime NULL

## _smtblDefaults
PK: AutoIdx
Columns (97):
  AutoIdx int NOT NULL identity PK
  ServiceCaption varchar(100) NULL
  RefreshTaskList int NULL
  WIP int NULL
  Recovery int NULL
  Stock int NULL
  AccountsPayable int NULL
  Tax int NULL
  Sales int NULL
  CostofSalesPartsAP int NULL
  AccountsReceivable int NULL
  CostofSalesLabour int NULL
  SalesAccountforAutoBilling int NULL
  Counter int NULL
  Elapsed int NULL
  Period int NULL
  JobCardForm varchar(5000) NULL
  SalesInvoiceForm varchar(5000) NULL
  AutoBillingInvoice varchar(5000) NULL
  DefaultStatusforNewServiceRequest int NULL
  DefaultStatusforNewServiceAsset int NULL
  DefaultServiceTaskPriority int NULL
  DefaultRequestType int NULL
  DefaultContractMatrix int NULL
  DefaultPriorityforNewServiceRequest int NULL
  DefaultServiceItemStatus int NULL
  DefaultTravelTime int NULL
  DefaultTechnicianHours datetime NULL
  DefaultSalesRep int NULL
  NextServiceReqNo float NULL
  NextServiceReqChar varchar(50) NULL
  NextServiceReqInvNo float NULL
  NextServiceReqInvChar varchar(10) NULL
  DefaultGLItem int NULL
  DefaultAPItem int NULL
  DefaultTechItem int NULL
  SalesLabour int NULL
  iTimeUnits int NULL
  iServiceRequestNoPad int NULL
  iServiceInvoiceNoPad int NULL
  iGSTAccount int NULL
  cPartsReportHeading nvarchar(100) NULL
  cLabourReportHeading nvarchar(100) NULL
  cOtherItemsReportHeading nvarchar(100) NULL
  DefaultTechnicianUntil datetime NULL
  bToggleCodeDesc bit NULL
  bAutoServAssetNumber bit NULL
  cServAssetPrefix nvarchar(50) NULL
  iServiceAssetPad int NULL
  iServiceAssetNextNo int NULL
  iTransactionCodeId int NULL
  iAutoBillTransactionCodeId int NULL
  sDefaultPath varchar(400) NULL
  iTaskTempNextNo int NULL
  iTaskTempPad int NULL
  cTaskTempPrefix nvarchar(50) NULL
  iContractNextNo int NULL
  iContractPad int NULL
  cContractPrefix nvarchar(50) NULL
  bAutoContractNo bit NULL
  bShowReminder bit NOT NULL default (0)
  iGenRemNextNo int NULL
  iGenRemPad int NULL
  cGenRemPrefix nvarchar(50) NULL
  bAutoGenRemNo bit NULL
  iAutoCrnTransactionCodeId int NULL
  bAllowLowerChrgRateTech bit NULL
  bGroupByCust bit NULL
  iAutoRequestPeriod int NULL
  iINVTransCode int NULL
  iCRNTransCode int NULL
  DefaultSchSpan numeric(10,0) NULL
  DefaultServiceItemId numeric(10,0) NULL
  DefaultAPServiceItemId numeric(10,0) NULL
  iAPTransCode int NULL
  iAPCreditAccounts int NULL
  iAPDebitAccounts int NULL
  iAPCRTransCode int NULL
  iAPCRCRCode int NULL
  iAPCRDRCode int NULL
  _smtblDefaults_iBranchID int NOT NULL default '0'
  _smtblDefaults_iCreatedBranchID int NOT NULL default '0'
  _smtblDefaults_iCreatedAgentID int NOT NULL default '0'
  _smtblDefaults_iModifiedAgentID int NOT NULL default '0'
  _smtblDefaults_iModifiedBranchID int NOT NULL default '0'
  _smtblDefaults_dModifiedDate datetime NULL
  iMeterBatchNextNo int NULL
  iMeterBatchPad int NULL
  cMeterBatchPrefix nvarchar(50) NULL
  bIsAutoMeterBatch bit NULL
  bUniqueOrderNo bit NULL default (0)
  bForceScheduledDateTime bit NOT NULL default (0)
  Consolidate int NULL
  iInternalAssetCust int NULL
  bAssetTracking bit NOT NULL default (0)
  bForceProjectOnAutoInvoice bit NULL
  bAllowZeroValInv bit NOT NULL default (0)

## _smtblDeletedInvoiceHistory
PK: none
Columns (40):
  cType varchar(10) NULL
  cMeterName varchar(50) NULL
  iServiceAssetId int NULL
  fReading float NULL
  dDate datetime NULL
  cMessage varchar(500) NULL
  iClientId int NULL
  iContractId int NULL
  iAreaId int NULL
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  AutoIdx int NOT NULL identity
  iRefAutoIdx int NULL
  iParentId int NULL
  dWarningDate datetime NOT NULL default getdate()
  bSelected bit NULL default 'FALSE'
  bProcessed bit NULL
  dProcessedDate datetime NULL
  iServiceRequestId int NULL
  cBillingSchedule varchar(3) NULL
  cMonthName varchar(3) NULL
  iYear int NULL
  iDay int NULL
  cDescription nvarchar(500) NULL
  fAmount float NULL
  cExtRef nvarchar(max) NULL
  iMeterId int NULL
  iAccountId int NULL
  iServiceTaskId int NULL
  fPreviousReading float NULL
  cInvoiceNumber varchar(50) NULL
  _smtblDeletedInvoiceHistory_iBranchID int NULL
  _smtblDeletedInvoiceHistory_iCreatedBranchID int NULL
  _smtblDeletedInvoiceHistory_iCreatedAgentID int NULL
  _smtblDeletedInvoiceHistory_iModifiedAgentID int NULL
  _smtblDeletedInvoiceHistory_iModifiedBranchID int NULL
  _smtblDeletedInvoiceHistory_dModifiedDate datetime NULL
  iDocEmailed int NULL default (0)
  iDocPrinted int NULL default (0)

## _smtblErrorCodes
PK: AutoIdx | UNIQUE: cCode
Columns (16):
  AutoIdx int NOT NULL identity PK
  cCode varchar(50) NOT NULL
  cDescription varchar(max) NULL
  cCauses varchar(max) NULL
  cSuggestiveAction varchar(max) NULL
  bDeleted bit NOT NULL default (0)
  dtStamp datetime NOT NULL default getdate()
  iUserId int NOT NULL
  cModuleName varchar(10) NOT NULL
  iModuleId bigint NULL
  _smtblErrorCodes_iBranchID int NOT NULL default '0'
  _smtblErrorCodes_iCreatedBranchID int NOT NULL default '0'
  _smtblErrorCodes_iCreatedAgentID int NOT NULL default '0'
  _smtblErrorCodes_iModifiedAgentID int NOT NULL default '0'
  _smtblErrorCodes_iModifiedBranchID int NOT NULL default '0'
  _smtblErrorCodes_dModifiedDate datetime NULL

## _smtblIncidentLog
PK: idIncidentLog
Columns (14):
  idIncidentLog int NOT NULL identity PK
  iIncidentID int NOT NULL
  dActionDate datetime NOT NULL
  iIncidentActionID int NOT NULL
  cResolution text NULL
  iAgentID int NULL
  iNewAgentID int NULL
  _smtblIncidentLog_iBranchID int NULL
  _smtblIncidentLog_dCreatedDate datetime NULL
  _smtblIncidentLog_dModifiedDate datetime NULL
  _smtblIncidentLog_iCreatedBranchID int NULL
  _smtblIncidentLog_iModifiedBranchID int NULL
  _smtblIncidentLog_iCreatedAgentID int NULL
  _smtblIncidentLog_iModifiedAgentID int NULL

## _smtblIncidents
PK: idIncidents
Columns (19):
  idIncidents int NOT NULL identity PK
  dCreated datetime NOT NULL
  dLastModified datetime NOT NULL
  cOutline varchar(1024) NULL
  iCurrentAgentID int NOT NULL
  iCategoryID int NOT NULL
  iLinkedTo int NOT NULL
  iDocumentID int NOT NULL
  iStatusId int NOT NULL
  dDueBy datetime NULL
  cOutRef nvarchar(100) NULL
  cChangeLog text NULL
  _smtblIncidents_iBranchID int NULL
  _smtblIncidents_dCreatedDate datetime NULL
  _smtblIncidents_dModifiedDate datetime NULL
  _smtblIncidents_iCreatedBranchID int NULL
  _smtblIncidents_iModifiedBranchID int NULL
  _smtblIncidents_iCreatedAgentID int NULL
  _smtblIncidents_iModifiedAgentID int NULL

## _smtblMakeClass
PK: AutoIdx | UNIQUE: iClassId+iMakeId
Columns (9):
  AutoIdx int NOT NULL identity PK
  iClassId varchar(20) NULL
  iMakeId int NULL
  _smtblMakeClass_iBranchID int NOT NULL default '0'
  _smtblMakeClass_iCreatedBranchID int NOT NULL default '0'
  _smtblMakeClass_iCreatedAgentID int NOT NULL default '0'
  _smtblMakeClass_iModifiedAgentID int NOT NULL default '0'
  _smtblMakeClass_iModifiedBranchID int NOT NULL default '0'
  _smtblMakeClass_dModifiedDate datetime NULL

## _smtblMeterWarnings
PK: none
Columns (38):
  cType varchar(10) NULL
  cMeterName varchar(50) NULL
  iServiceAssetId int NULL
  fReading float NULL
  dDate datetime NULL
  cMessage varchar(500) NULL
  iClientId int NULL
  iContractId int NULL
  iAreaId int NULL
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  AutoIdx int NOT NULL identity
  iParentId int NULL
  dWarningDate datetime NOT NULL default getdate()
  bSelected bit NULL default 'FALSE'
  bProcessed bit NULL
  dProcessedDate datetime NULL
  iServiceRequestId int NULL
  cBillingSchedule varchar(3) NULL
  cMonthName varchar(3) NULL
  iYear int NULL
  iDay int NULL
  cDescription nvarchar(500) NULL
  fAmount float NULL
  cExtRef nvarchar(max) NULL
  iMeterId int NULL
  iAccountId int NULL
  iServiceTaskId int NULL
  _smtblMeterWarnings_iBranchID int NOT NULL default '0'
  _smtblMeterWarnings_iCreatedBranchID int NOT NULL default '0'
  _smtblMeterWarnings_iCreatedAgentID int NOT NULL default '0'
  _smtblMeterWarnings_iModifiedAgentID int NOT NULL default '0'
  _smtblMeterWarnings_iModifiedBranchID int NOT NULL default '0'
  _smtblMeterWarnings_dModifiedDate datetime NULL
  fPreviousReading float NULL
  iNewMeterIdForCounter int NULL
  iProjectId int NULL

## _smtblModelParts
PK: AutoIdx | UNIQUE: iModelId+iStockId
Columns (13):
  AutoIdx int NOT NULL identity PK
  iModelId bigint NULL
  iStockId int NULL
  bActive bit NULL
  iUserId int NULL
  dtStamp datetime NULL
  bDeleted bit NULL
  _smtblModelParts_iBranchID int NOT NULL default '0'
  _smtblModelParts_iCreatedBranchID int NOT NULL default '0'
  _smtblModelParts_iCreatedAgentID int NOT NULL default '0'
  _smtblModelParts_iModifiedAgentID int NOT NULL default '0'
  _smtblModelParts_iModifiedBranchID int NOT NULL default '0'
  _smtblModelParts_dModifiedDate datetime NULL

## _smtblModels
PK: AutoIdx | UNIQUE: cCode
Columns (18):
  AutoIdx bigint NOT NULL identity PK
  cCode varchar(20) NULL
  cDescription varchar(max) NULL
  iWarranty int NULL
  dtStamp datetime NOT NULL default getdate()
  iUserId int NOT NULL
  bDeleted bit NOT NULL default (0)
  fk_iInvGroupId int NULL
  fk_iSupplierId int NULL
  fk_iClassId int NULL
  fk_iMakeId int NULL
  _smtblModels_iBranchID int NOT NULL default '0'
  _smtblModels_iCreatedBranchID int NOT NULL default '0'
  _smtblModels_iCreatedAgentID int NOT NULL default '0'
  _smtblModels_iModifiedAgentID int NOT NULL default '0'
  _smtblModels_iModifiedBranchID int NOT NULL default '0'
  _smtblModels_dModifiedDate datetime NULL
  bEnableSubComponent bit NOT NULL default (0)

## _smtblMstMeter
PK: AutoIdx | UNIQUE: cMeterCode+iAssetId
Columns (13):
  AutoIdx int NOT NULL identity PK
  cMeterCode nvarchar(100) NULL
  cMeterNumber nvarchar(100) NULL
  cMeterDesc nvarchar(max) NULL
  cMeterNotes text NULL
  iAssetId int NULL
  iCurrentReading decimal(18,2) NULL
  _smtblMstMeter_iBranchID int NOT NULL default '0'
  _smtblMstMeter_iCreatedBranchID int NOT NULL default '0'
  _smtblMstMeter_iCreatedAgentID int NOT NULL default '0'
  _smtblMstMeter_iModifiedAgentID int NOT NULL default '0'
  _smtblMstMeter_iModifiedBranchID int NOT NULL default '0'
  _smtblMstMeter_dModifiedDate datetime NULL

## _smtblMstMeterReading
PK: AutoIdx
Columns (17):
  AutoIdx int NOT NULL identity PK
  iMeterId int NULL
  iAssetId int NULL
  iCurrentReading decimal(18,2) NULL
  iPreviousReading decimal(18,2) NULL
  cMeterNotes text NULL
  cBatchNumber nvarchar(1000) NULL
  dReadingDate datetime NULL
  bIsBatch bit NULL
  _smtblMstMeterReading_iBranchID int NOT NULL default '0'
  _smtblMstMeterReading_iCreatedBranchID int NOT NULL default '0'
  _smtblMstMeterReading_iCreatedAgentID int NOT NULL default '0'
  _smtblMstMeterReading_iModifiedAgentID int NOT NULL default '0'
  _smtblMstMeterReading_iModifiedBranchID int NOT NULL default '0'
  _smtblMstMeterReading_dModifiedDate datetime NULL
  dPreviousReadingDate datetime NULL
  bTakeOn bit NOT NULL default (0)

## _smtblOtherSubComponents
PK: idOtherSubComponents
Columns (11):
  idOtherSubComponents int NOT NULL identity PK
  cCode varchar(400) NULL
  cDescription varchar(250) NULL
  bSerial bit NULL
  _smtblOtherSubComponents_iBranchID int NULL
  _smtblOtherSubComponents_dCreatedDate datetime NULL
  _smtblOtherSubComponents_dModifiedDate datetime NULL
  _smtblOtherSubComponents_iCreatedBranchID int NULL
  _smtblOtherSubComponents_iModifiedBranchID int NULL
  _smtblOtherSubComponents_iCreatedAgentID int NULL
  _smtblOtherSubComponents_iModifiedAgentID int NULL

## _smtblOtherSubComponentsSerial
PK: idOtherSubComponentsSerial
Columns (10):
  idOtherSubComponentsSerial int NOT NULL identity PK
  cSerialNumber varchar(30) NULL
  iOtherSubComponent int NULL
  _smtblOtherSubComponentsSerial_iBranchID int NULL
  _smtblOtherSubComponentsSerial_dCreatedDate datetime NULL
  _smtblOtherSubComponentsSerial_dModifiedDate datetime NULL
  _smtblOtherSubComponentsSerial_iCreatedBranchID int NULL
  _smtblOtherSubComponentsSerial_iModifiedBranchID int NULL
  _smtblOtherSubComponentsSerial_iCreatedAgentID int NULL
  _smtblOtherSubComponentsSerial_iModifiedAgentID nchar(10) NULL

## _smtblPeriodService
PK: AutoIdx | UNIQUE: cCode+cType+iServiceAssetId+iContractMatrixId
Columns (55):
  AutoIdx int NOT NULL identity PK
  iServiceAssetId int NULL
  cCode varchar(20) NULL
  cDescription varchar(200) NULL
  fAmount float NULL
  cExternalRef varchar(max) NULL
  bInvoiceWithoutConfirmation bit NULL
  bBillInAdvance bit NULL
  cBillingSchedule varchar(10) NULL
  dNextDate datetime NULL
  iFrequency int NULL
  iJan int NULL
  iFeb int NULL
  iMar int NULL
  iApr int NULL
  iMay int NULL
  iJun int NULL
  iJul int NULL
  iAug int NULL
  iSep int NULL
  iOct int NULL
  iNov int NULL
  iDec int NULL
  dLastActionDate datetime NULL
  cNotes varchar(500) NULL
  fUsage float NULL
  ifk_UsageUnits int NULL
  cType varchar(10) NULL - Contains 'PER' for period bill and 'SER' for service schedule
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  iRequestTypeId int NULL
  iAccountId int NULL
  iRefSMBillingAutoIdx int NULL
  iContractMatrixId int NULL
  _smtblPeriodService_iBranchID int NOT NULL default '0'
  _smtblPeriodService_iCreatedBranchID int NOT NULL default '0'
  _smtblPeriodService_iCreatedAgentID int NOT NULL default '0'
  _smtblPeriodService_iModifiedAgentID int NOT NULL default '0'
  _smtblPeriodService_iModifiedBranchID int NOT NULL default '0'
  _smtblPeriodService_dModifiedDate datetime NULL
  iMeterId int NULL
  iServiceTaskTemplate int NULL
  bIsEscalation bit NULL default (0)
  fEscalationPer float NULL
  fEscalationAmt float NULL
  fOriginalAmount float NULL
  fEscFrequency float NULL
  fEscalationDays float NULL
  iRepeatEscType int NULL
  dLastEscalationDate datetime NULL
  dStartEscalationDate datetime NULL
  bIsPercentage bit NULL
  iProjectId int NULL
  bDisableBilling bit NOT NULL default (0)

## _smtblProcessedAutoInvoice
PK: none
Columns (11):
  AutoIdx numeric(10,0) NOT NULL identity
  cInvoiceNo varchar(50) NULL
  cAuditNo varchar(50) NULL
  cMeterType varchar(50) NULL
  iMeterWarningID int NULL
  _smtblProcessedAutoInvoice_iBranchID int NOT NULL default '0'
  _smtblProcessedAutoInvoice_iCreatedBranchID int NOT NULL default '0'
  _smtblProcessedAutoInvoice_iCreatedAgentID int NOT NULL default '0'
  _smtblProcessedAutoInvoice_iModifiedAgentID int NOT NULL default '0'
  _smtblProcessedAutoInvoice_iModifiedBranchID int NOT NULL default '0'
  _smtblProcessedAutoInvoice_dModifiedDate datetime NULL

## _smtblPurchaseOrder
PK: none
Columns (29):
  bUpdateTask bit NULL
  bProcessed bit NULL
  iVendorId int NULL
  iStockId int NULL
  cDescription varchar(2000) NULL
  iServiceTaskId int NULL
  fQty float NULL
  fUnitPrice float NULL
  fTax float NULL
  fLineTotal float NULL
  iUserId int NULL
  dtStamp datetime NULL
  fGrossAmount float NULL
  fTaxPerc float NULL
  iTaxId int NULL
  iEvo_POId int NULL
  iEvo_POLineId bigint NULL
  dDate datetime NULL
  AutoIdx int NOT NULL identity
  iWarehouseId int NULL
  iUnitId int NULL
  ConfirmQty float NULL
  cPOId varchar(50) NULL
  _smtblPurchaseOrder_iBranchID int NOT NULL default '0'
  _smtblPurchaseOrder_iCreatedBranchID int NOT NULL default '0'
  _smtblPurchaseOrder_iCreatedAgentID int NOT NULL default '0'
  _smtblPurchaseOrder_iModifiedAgentID int NOT NULL default '0'
  _smtblPurchaseOrder_iModifiedBranchID int NOT NULL default '0'
  _smtblPurchaseOrder_dModifiedDate datetime NULL

## _smtblPurchaseOrderDetails
PK: none
Columns (18):
  idPOLineDetails int NOT NULL identity
  iPurchaseOrderId int NOT NULL
  iServiceTaskId int NOT NULL
  iStockId int NOT NULL
  fQty float NOT NULL
  iStockBinLocationID int NOT NULL
  iUnitsOfMeasureID int NOT NULL
  iAttributeGroupID int NOT NULL
  xAttribute xml NULL
  cPOId varchar(50) NULL
  dDate datetime NULL
  iUserId int NULL
  _smtblPurchaseOrderDetails_iBranchID int NOT NULL
  _smtblPurchaseOrderDetails_iCreatedBranchID int NOT NULL
  _smtblPurchaseOrderDetails_iCreatedAgentID int NOT NULL
  _smtblPurchaseOrderDetails_iModifiedAgentID int NOT NULL
  _smtblPurchaseOrderDetails_iModifiedBranchID int NOT NULL
  _smtblPurchaseOrderDetails_dModifiedDate datetime NULL

## _smtblrateslab
PK: AutoIdx
Columns (15):
  AutoIdx bigint NOT NULL identity PK
  iServiceAssetId numeric(10,0) NULL
  iBillingID bigint NULL
  iFromQty numeric(15,0) NULL
  iToqty numeric(15,0) NULL
  fRate decimal(18,7) NULL
  _smtblrateslab_iBranchID int NOT NULL default '0'
  _smtblrateslab_iCreatedBranchID int NOT NULL default '0'
  _smtblrateslab_iCreatedAgentID int NOT NULL default '0'
  _smtblrateslab_iModifiedAgentID int NOT NULL default '0'
  _smtblrateslab_iModifiedBranchID int NOT NULL default '0'
  _smtblrateslab_dModifiedDate datetime NULL
  bIsThreshold bit NULL
  cName varchar(50) NULL
  cDescription varchar(100) NULL

## _smtblRateSlabHistory
PK: idRateSlabHistory
Columns (19):
  idRateSlabHistory bigint NOT NULL identity PK
  iRateSlabID bigint NOT NULL
  dActionDate datetime NOT NULL
  iActionType int NOT NULL
  iAgentID int NOT NULL
  iServiceAssetId numeric(10,0) NULL
  iBillingID bigint NULL
  iFromQty numeric(15,0) NULL
  iToqty numeric(15,0) NULL
  fRate decimal(18,7) NULL
  bIsThreshold bit NULL
  cName varchar(50) NULL
  cDescription varchar(100) NULL
  _smtblRateSlabHistory_iBranchID int NULL
  _smtblRateSlabHistory_iCreatedBranchID int NULL
  _smtblRateSlabHistory_iCreatedAgentID int NULL
  _smtblRateSlabHistory_iModifiedAgentID int NULL
  _smtblRateSlabHistory_iModifiedBranchID int NULL
  _smtblRateSlabHistory_dModifiedDate datetime NULL

## _smtblReportLayout
PK: none
Columns (26):
  idReportLayout int NOT NULL identity
  cRptDescription varchar(80) NOT NULL
  iModuleId int NULL
  iVersion int NULL
  nLayout varbinary(max) NOT NULL
  bReadOnly bit NOT NULL
  bIsDefaultLayout bit NULL
  bIsEmailAfterPreview bit NULL
  bUseThisLayout bit NULL
  bUseDefaultPrinter bit NULL
  cPrinterName nvarchar(max) NULL
  bUsePrinterPaperSize bit NULL
  iNoCopies int NULL
  bCollate bit NULL
  bSkipPrinterConfirmation bit NULL
  cDuplex nvarchar(50) NULL
  cDefaultAttFormat nvarchar(200) NULL
  cMailSubject nvarchar(max) NULL
  cDefaultMessage nvarchar(max) NULL
  iMainReportLayoutId int NULL
  _smtblReportLayout_iBranchID int NOT NULL default '0'
  _smtblReportLayout_iCreatedBranchID int NOT NULL default '0'
  _smtblReportLayout_iCreatedAgentID int NOT NULL default '0'
  _smtblReportLayout_iModifiedAgentID int NOT NULL default '0'
  _smtblReportLayout_iModifiedBranchID int NOT NULL default '0'
  _smtblReportLayout_dModifiedDate datetime NULL

## _smtblReportQueries
PK: none
Columns (10):
  AutoIdX int NOT NULL identity
  cRptName varchar(100) NOT NULL
  IsStoredProcedure bit NULL
  cQuery varchar(max) NULL
  _smtblReportQueries_iBranchID int NOT NULL default '0'
  _smtblReportQueries_iCreatedBranchID int NOT NULL default '0'
  _smtblReportQueries_iCreatedAgentID int NOT NULL default '0'
  _smtblReportQueries_iModifiedAgentID int NOT NULL default '0'
  _smtblReportQueries_iModifiedBranchID int NOT NULL default '0'
  _smtblReportQueries_dModifiedDate datetime NULL

## _smtblRequestType
PK: AutoIdx | UNIQUE: cCode
Columns (35):
  AutoIdx int NOT NULL identity PK
  cCode varchar(20) NULL
  cDescription varchar(max) NULL
  bIsActive bit NULL
  cJobCard varchar(5000) NULL
  iSalesparts int NULL
  iSalesLabour int NULL
  iCostParts int NULL
  iCostLabour int NULL
  bDeleted bit NULL
  iUserId int NULL
  dtStamp datetime NULL default getdate()
  iWIPParts int NULL
  iWIPLabour int NULL
  bCharge bit NULL
  iTransactionTypeID int NULL
  WorkTimeSchSpan numeric(10,0) NULL
  iInvTransTypeID int NULL
  iCRNTransTypeID int NULL
  iStkID int NULL
  iTaxID int NULL
  iARAcntID int NULL
  bOverrideTransAcnt bit NULL
  iAPTransCode int NULL
  iAPCreditAccounts int NULL
  iAPDebitAccounts int NULL
  iAPCRTransCode int NULL
  iAPCRCRCode int NULL
  iAPCRDRCode int NULL
  _smtblRequestType_iBranchID int NOT NULL default '0'
  _smtblRequestType_iCreatedBranchID int NOT NULL default '0'
  _smtblRequestType_iCreatedAgentID int NOT NULL default '0'
  _smtblRequestType_iModifiedAgentID int NOT NULL default '0'
  _smtblRequestType_iModifiedBranchID int NOT NULL default '0'
  _smtblRequestType_dModifiedDate datetime NULL

## _smtblRequestTypeActivities
PK: AutoIdx
Columns (13):
  AutoIdx int NOT NULL identity PK
  iRequestTypeId int NULL
  iActivityId int NULL
  iOrder int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  iUserId int NULL
  _smtblRequestTypeActivities_iBranchID int NOT NULL default '0'
  _smtblRequestTypeActivities_iCreatedBranchID int NOT NULL default '0'
  _smtblRequestTypeActivities_iCreatedAgentID int NOT NULL default '0'
  _smtblRequestTypeActivities_iModifiedAgentID int NOT NULL default '0'
  _smtblRequestTypeActivities_iModifiedBranchID int NOT NULL default '0'
  _smtblRequestTypeActivities_dModifiedDate datetime NULL

## _smtblResolution
PK: AutoIdx | UNIQUE: cCode
Columns (17):
  AutoIdx int NOT NULL identity PK
  cCode varchar(20) NULL
  cDescription varchar(max) NULL
  cStatus varchar(max) NULL
  bIsActive bit NULL
  cInvoiceForm varchar(5000) NULL
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  bIsNewServiceRequest bit NULL
  bAuto bit NULL
  _smtblResolution_iBranchID int NOT NULL default '0'
  _smtblResolution_iCreatedBranchID int NOT NULL default '0'
  _smtblResolution_iCreatedAgentID int NOT NULL default '0'
  _smtblResolution_iModifiedAgentID int NOT NULL default '0'
  _smtblResolution_iModifiedBranchID int NOT NULL default '0'
  _smtblResolution_dModifiedDate datetime NULL

## _smtblSADeletedBillingEntries
PK: AutoIdx
Columns (12):
  AutoIdx int NOT NULL identity PK
  Fk_SAbillingID int NULL
  iServiceAssetId int NULL
  cType varchar(50) NULL
  iContractMatrixID int NULL
  iRefSMBillingAutoIdx int NULL
  _smtblSADeletedBillingEntries_iBranchID int NOT NULL default '0'
  _smtblSADeletedBillingEntries_iCreatedBranchID int NOT NULL default '0'
  _smtblSADeletedBillingEntries_iCreatedAgentID int NOT NULL default '0'
  _smtblSADeletedBillingEntries_iModifiedAgentID int NOT NULL default '0'
  _smtblSADeletedBillingEntries_iModifiedBranchID int NOT NULL default '0'
  _smtblSADeletedBillingEntries_dModifiedDate datetime NULL

## _smtblSalesPartsEntry
PK: none
Columns (30):
  iStockId int NULL
  cDescription varchar(2000) NULL
  iServiceTaskId int NULL
  fQty float NULL
  fUnitPrice float NULL
  fTax float NULL
  fLineTotal float NULL
  iUserId int NULL
  dtStamp datetime NULL
  fGrossAmount float NULL
  fTaxPerc float NULL
  iTaxId int NULL
  iEvo_POId int NULL
  iEvo_POLineId bigint NULL
  dDate datetime NULL
  AutoIdx int NOT NULL identity
  iWarehouseId int NULL
  iLotId int NULL
  bProcessed bit NULL
  bIsSerial bit NULL
  bIsWareHse bit NULL
  bIsLot bit NULL
  iUnitId int NULL
  iRepID int NULL
  _smtblSalesPartsEntry_iBranchID int NOT NULL default '0'
  _smtblSalesPartsEntry_iCreatedBranchID int NOT NULL default '0'
  _smtblSalesPartsEntry_iCreatedAgentID int NOT NULL default '0'
  _smtblSalesPartsEntry_iModifiedAgentID int NOT NULL default '0'
  _smtblSalesPartsEntry_iModifiedBranchID int NOT NULL default '0'
  _smtblSalesPartsEntry_dModifiedDate datetime NULL

## _smtblScheduler
PK: AutoIdx
Columns (25):
  iWorkerId int NULL
  iServiceTaskId int NULL
  Status int NULL
  Subject varchar(50) NULL
  Description varchar(max) NULL
  Label int NULL
  StartTime datetime NULL
  EndTime datetime NULL
  Location varchar(50) NULL
  AllDay bit NOT NULL
  EventType int NULL
  RecurrenceInfo varchar(max) NULL
  ReminderInfo varchar(max) NULL
  AutoIdx int NOT NULL identity PK
  dtStamp datetime NULL
  bDeleted bit NULL
  iUserId int NULL
  iDepartmentId int NULL
  StatusCode varchar(50) NULL
  _smtblScheduler_iBranchID int NOT NULL default '0'
  _smtblScheduler_iCreatedBranchID int NOT NULL default '0'
  _smtblScheduler_iCreatedAgentID int NOT NULL default '0'
  _smtblScheduler_iModifiedAgentID int NOT NULL default '0'
  _smtblScheduler_iModifiedBranchID int NOT NULL default '0'
  _smtblScheduler_dModifiedDate datetime NULL

## _smtblServiceAsset
PK: AutoIdx | UNIQUE: cCode
Columns (60):
  AutoIdx int NOT NULL identity PK
  cCode varchar(50) NULL
  cDescription varchar(1000) NULL
  iStockId int NULL
  iSerialId int NULL
  iClassId int NULL
  iMakeId int NULL
  iModelId int NULL
  iAreaId int NULL
  fUsageUnits float NULL
  iUsageUnitsId int NULL
  fLifeSpan float NULL
  iLifeSpanId int NULL
  iDefaultWorkerId int NULL
  iStatusId int NULL
  iCustomerId int NULL
  cCustomerAdd varchar(100) NULL
  iContractMatrixId int NULL
  dStartDate datetime NULL
  dFinishDate datetime NULL
  dReviewDate datetime NULL
  iBillingCustomerId int NULL
  cBillingCustomerAdd varchar(100) NULL
  iWorkerId int NULL
  cLocation varchar(100) NULL
  dCreationDate datetime NULL
  dInvoiceDate datetime NULL
  dInstallationDate datetime NULL
  dNextServiceDate datetime NULL
  dWarrantyStartDate datetime NULL
  dWarrantyEndDate datetime NULL
  dWarrantyReviewDate datetime NULL
  dDecomissionDate datetime NULL
  dLastContactDate datetime NULL
  dNextContactDate datetime NULL
  iSupplierId int NULL
  dDateofPurchase datetime NULL
  dPurchaseWarrantyStartDate datetime NULL
  dPurchaseWarrantyEndDate datetime NULL
  dPurchaseWarrantyReviewDate datetime NULL
  bDeleted bit NULL
  iUserId int NULL
  dtStamp datetime NULL
  iParentId int NULL
  cSerialNo varchar(50) NULL
  iCreatedFrom int NULL
  cClassId varchar(max) NULL
  cMakeId varchar(max) NULL
  cModelId varchar(max) NULL
  bInternalAsset bit NOT NULL default (0)
  _smtblServiceAsset_iBranchID int NOT NULL default '0'
  _smtblServiceAsset_iCreatedBranchID int NOT NULL default '0'
  _smtblServiceAsset_iCreatedAgentID int NOT NULL default '0'
  _smtblServiceAsset_iModifiedAgentID int NOT NULL default '0'
  _smtblServiceAsset_iModifiedBranchID int NOT NULL default '0'
  _smtblServiceAsset_dModifiedDate datetime NULL
  bActive bit NOT NULL default (1)
  iWarrantyCustomerId bigint NULL
  cWarrantyCustomerAdd varchar(max) NULL
  cChangeReason varchar(500) NULL

## _smtblServiceAssetTaskImages
PK: idServiceAssetTaskImage
Columns (13):
  idServiceAssetTaskImage int NOT NULL identity PK
  nImage image NULL
  cImageDesc nvarchar(50) NULL
  iServiceTask int NOT NULL
  iServiceAsset int NOT NULL
  _smtblServiceAssetTaskImages_iBranchID int NULL
  _smtblServiceAssetTaskImages_dCreatedDate datetime NULL
  _smtblServiceAssetTaskImages_dModifiedDate datetime NULL
  _smtblServiceAssetTaskImages_iCreatedBranchID int NULL
  _smtblServiceAssetTaskImages_iModifiedBranchID int NULL
  _smtblServiceAssetTaskImages_iCreatedAgentID int NULL
  _smtblServiceAssetTaskImages_iModifiedAgentID int NULL
  _smtblServiceAssetTaskImages_iChangeSetID int NULL

## _smtblServiceRequest
PK: AutoIdx
Columns (46):
  AutoIdx int NOT NULL identity PK
  iClientId int NULL
  iContractId int NULL
  cDescription varchar(max) NULL
  iServiceAssetId int NULL
  iErrorCodeId int NULL
  iModelId int NULL
  cContact varchar(30) NULL
  dLoggedDate datetime NULL
  dScheduledDate datetime NULL
  dArrivalDate datetime NULL
  dCompletedDate datetime NULL
  iResponseTime int NULL
  iActualTime int NULL
  iRequestTypeId int NULL
  iPriorityId int NULL
  iStatusId int NULL
  cOrderNo varchar(max) NULL
  iTechnicianId int NULL
  bDeleted bit NULL
  iUserId int NULL
  dtStamp datetime NULL
  cAddress varchar(100) NULL
  cRequestNo varchar(50) NULL
  dExpectedCompletion datetime NULL
  cGLAuditNo varchar(20) NULL
  iAreaId int NULL
  cRequestedBy varchar(50) NULL
  iDepartmentId int NULL
  dExpectedArrival datetime NULL
  cContactNo varchar(30) NULL
  cContactEmail varchar(60) NULL
  fCost float NULL
  fRevenue float NULL
  fMargin float NULL
  bIsBillingCustomer bit NOT NULL default (0)
  bAutoGenerated bit NULL
  dAutoReqDate datetime NULL
  _smtblServiceRequest_iBranchID int NOT NULL default '0'
  _smtblServiceRequest_iCreatedBranchID int NOT NULL default '0'
  _smtblServiceRequest_iCreatedAgentID int NOT NULL default '0'
  _smtblServiceRequest_iModifiedAgentID int NOT NULL default '0'
  _smtblServiceRequest_iModifiedBranchID int NOT NULL default '0'
  _smtblServiceRequest_dModifiedDate datetime NULL
  iMeterId int NULL
  bIsWarrantyCustomer bit NOT NULL default (0)

## _smtblServiceSchTemplate
PK: iTemplateId | UNIQUE: cTemplateDesc, cTemplateDesc
Columns (43):
  iTemplateId int NOT NULL identity PK
  cTemplateDesc varchar(50) NULL
  iServiceAssetId int NULL
  cCode varchar(50) NULL
  cDescription varchar(200) NULL
  fAmount float NULL
  cExternalRef varchar(max) NULL
  bInvoiceWithOutConfirmation bit NULL
  bBillInAdvance bit NULL
  cBillingSchedule varchar(10) NULL
  dNextDate datetime NULL
  iFrequency int NULL
  iJan int NULL
  iFeb int NULL
  iMar int NULL
  iApr int NULL
  iMay int NULL
  iJun int NULL
  iJul int NULL
  iAug int NULL
  iSep int NULL
  iOct int NULL
  iNov int NULL
  iDec int NULL
  dtLastActionDate datetime NULL
  cNotes varchar(max) NULL
  fUsage float NULL
  ifk_UsageUnits int NULL
  cType varchar(10) NULL
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  iRequestTypeId int NULL
  iAccountId int NULL
  iRepeatAfter int NULL
  iRepeatType int NULL
  _smtblServiceSchTemplate_iBranchID int NOT NULL default '0'
  _smtblServiceSchTemplate_iCreatedBranchID int NOT NULL default '0'
  _smtblServiceSchTemplate_iCreatedAgentID int NOT NULL default '0'
  _smtblServiceSchTemplate_iModifiedAgentID int NOT NULL default '0'
  _smtblServiceSchTemplate_iModifiedBranchID int NOT NULL default '0'
  _smtblServiceSchTemplate_dModifiedDate datetime NULL
  iServiceTaskTemplate int NULL

## _smtblServiceTask
PK: AutoIdx
Columns (79):
  AutoIdx int NOT NULL identity PK
  iServiceRequestId int NULL
  iErrorCodeId int NULL
  iResolutionCode int NULL
  cSummaryofWork varchar(max) NULL
  cInvoiceText varchar(2000) NULL
  cNextCallComments varchar(max) NULL
  iRequestNo int NULL
  iRequestTypeId int NULL
  iPriorityId int NULL
  iStatusId int NULL
  cOrderNo varchar(max) NULL
  iWorkerId int NULL
  dLoggedDate datetime NULL
  dScheduledDate datetime NULL
  dExpectedArrivalDate datetime NULL
  dArrivalDate datetime NULL
  dCompletedDate datetime NULL
  fResponseTime float NULL
  fActualTime float NULL
  iUserId int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  cDescription varchar(max) NULL
  cTaskNo varchar(50) NULL
  iSalesOrderId int NULL
  cInvoiceNo varchar(50) NULL
  dInvoiceDate datetime NULL
  cPaymentTerms varchar(50) NULL
  bAutoInvoice bit NULL
  dExpectedCompletion datetime NULL
  fTotalOrderValue float NULL
  fTotalProcessedValue float NULL
  fTotalOrderTaxAmount float NULL
  fTotalProcessedTaxAmount float NULL
  fWIPAPTransAudit float NULL
  fWIPStockTransAudit float NULL
  fWIPLabourTransAudit float NULL
  fWIPGLTransAudit float NULL
  bProcessed bit NULL
  iDocType int NULL
  iDepartmentId int NULL
  ServiceReqTaskDesc nvarchar(max) NULL
  bTemplate bit NULL
  bRounded bit NULL default (0)
  iPKPrinted int NULL
  iServiceAssetID int NULL
  bIsWarrantyCustomer bit NULL
  bIsBillingCustomer bit NOT NULL default (0)
  _smtblServiceTask_iBranchID int NOT NULL default '0'
  _smtblServiceTask_iCreatedBranchID int NOT NULL default '0'
  _smtblServiceTask_iCreatedAgentID int NOT NULL default '0'
  _smtblServiceTask_iModifiedAgentID int NOT NULL default '0'
  _smtblServiceTask_iModifiedBranchID int NOT NULL default '0'
  _smtblServiceTask_dModifiedDate datetime NULL
  fTotalDiscountPercent float NULL
  fTotalDiscount float NULL
  iClientId int NULL
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
  iDocEmailed int NULL default (0)
  iDocPrinted int NULL default (0)
  iCRlinked int NULL default (0)
  imgCustSign image NULL
  imgTechSign image NULL
  iProjectId int NULL
  iMeterReadingId int NULL
  iPeriodServiceId int NULL
  IsOpen bit NULL

## _smtblServiceTaskActivities
PK: AutoIdx
Columns (12):
  AutoIdx int NOT NULL identity PK
  iServiceTaskId int NULL
  iActivityId int NULL
  cActivityCode varchar(50) NULL
  cComments varchar(2000) NULL
  iOrder int NULL
  _smtblServiceTaskActivities_iBranchID int NOT NULL default '0'
  _smtblServiceTaskActivities_iCreatedBranchID int NOT NULL default '0'
  _smtblServiceTaskActivities_iCreatedAgentID int NOT NULL default '0'
  _smtblServiceTaskActivities_iModifiedAgentID int NOT NULL default '0'
  _smtblServiceTaskActivities_iModifiedBranchID int NOT NULL default '0'
  _smtblServiceTaskActivities_dModifiedDate datetime NULL

## _smtblServiceTaskLineDetails
PK: idTaskLineDetails
Columns (23):
  idTaskLineDetails int NOT NULL identity PK
  iLDTaskId bigint NOT NULL
  iLDTaskLineId bigint NOT NULL
  iLotID int NOT NULL
  cLotNumber varchar(40) NOT NULL
  dLotExpiryDate datetime NULL
  iStockBinLocationID int NOT NULL
  iUnitsOfMeasureID int NOT NULL
  iAttributeGroupID int NOT NULL
  xAttribute xml NULL
  fldQty float NOT NULL
  fldConfirmed float NOT NULL
  fldQtyReserved float NOT NULL
  fldQtyLastProcess float NOT NULL
  fldProcessed float NOT NULL
  dDate datetime NULL
  iUserId int NULL
  _smtblServiceTaskLineDetails_iBranchID int NULL
  _smtblServiceTaskLineDetails_dModifiedDate datetime NULL
  _smtblServiceTaskLineDetails_iCreatedBranchID int NULL
  _smtblServiceTaskLineDetails_iModifiedBranchID int NULL
  _smtblServiceTaskLineDetails_iCreatedAgentID int NULL
  _smtblServiceTaskLineDetails_iModifiedAgentID int NULL

## _smtblServiceTaskLines
PK: AutoIdx
Columns (66):
  AutoIdx int NOT NULL identity PK
  iServiceTaskId int NULL
  dDate datetime NULL
  bAdd bit NULL
  iModule int NULL
  iModuleId int NULL
  fAvailableQty float NULL
  fQty float NULL
  fConfirmed float NULL
  fProcessed float NULL
  iWarehouse int NULL
  iSerialNo int NULL
  iLotNo int NULL
  fCost float NULL
  fCharge float NULL
  fTax float NULL
  fChargeAmount float NULL
  iProject int NULL
  iSalesRep int NULL
  iUserId int NULL
  dtStamp datetime NULL
  TxTypeId int NULL
  iStockId int NULL
  iSupplierId int NULL
  iLedgerId int NULL
  iWorkerId int NULL
  fUnitPriceExcl float NULL
  fUnitPriceIncl float NULL
  fUnitCost float NULL
  fLineDiscount float NULL
  iTaxTypeId int NULL
  fTaxRate float NULL
  iPriceListNameId int NULL
  fLineTotInclDisc float NULL
  fLineTotExclDisc float NULL
  fLineTotTaxAmount float NULL
  fLineTotTaxAmountNoDisc float NULL
  iWorkCodeId int NULL
  iWorkerTimeId int NULL
  iEvo_POId int NULL
  iEvo_POLineId bigint NULL
  iPurchaseOrderId int NULL
  cDescription varchar(2000) NULL
  iEvo_SOId int NULL
  iEvo_SOLineId bigint NULL
  bIsWareHse bit NULL
  bIsSerial bit NULL
  bIsLot bit NULL
  iModuleParentId int NULL
  fOrderTotal float NULL
  fOrderTax float NULL
  iOriginalLineId int NULL
  iUnitId int NULL
  fActualTime float NULL
  cSerialItems varchar(4000) NULL
  iTechWorkCodeId int NULL
  cItemCode varchar(2000) NULL
  _smtblServiceTaskLines_iBranchID int NOT NULL default '0'
  _smtblServiceTaskLines_iCreatedBranchID int NOT NULL default '0'
  _smtblServiceTaskLines_iCreatedAgentID int NOT NULL default '0'
  _smtblServiceTaskLines_iModifiedAgentID int NOT NULL default '0'
  _smtblServiceTaskLines_iModifiedBranchID int NOT NULL default '0'
  _smtblServiceTaskLines_dModifiedDate datetime NULL
  iServiceTaskTemplateId int NULL default (0)
  bIsFromAutogenerated bit NULL default (0)
  bIsFromMobile bit NULL default (0)

## _smtblSubAssets
PK: AutoIdx
Columns (12):
  AutoIdx int NOT NULL identity PK
  iServiceAssetId int NULL
  iSubServiceAssetId int NULL
  dtStamp datetime NULL
  iUserId int NULL
  bDeleted int NULL
  _smtblSubAssets_iBranchID int NOT NULL default '0'
  _smtblSubAssets_iCreatedBranchID int NOT NULL default '0'
  _smtblSubAssets_iCreatedAgentID int NOT NULL default '0'
  _smtblSubAssets_iModifiedAgentID int NOT NULL default '0'
  _smtblSubAssets_iModifiedBranchID int NOT NULL default '0'
  _smtblSubAssets_dModifiedDate datetime NULL

## _smtblSubComponents
PK: idSubComponents
Columns (14):
  idSubComponents int NOT NULL identity PK
  cCode varchar(400) NULL
  cDescription varchar(250) NULL
  fQty float NULL
  iComponentType smallint NULL
  _smtblSubComponents_iBranchID int NULL
  _smtblSubComponents_dCreatedDate datetime NULL
  _smtblSubComponents_dModifiedDate datetime NULL
  _smtblSubComponents_iCreatedBranchID int NULL
  _smtblSubComponents_iModifiedBranchID int NULL
  _smtblSubComponents_iCreatedAgentID int NULL
  _smtblSubComponents_iModifiedAgentID int NULL
  bSerial bit NULL
  iComponent int NULL

## _smtblSubComponentsAssets
PK: idSubComponentsAssets
Columns (11):
  idSubComponentsAssets int NOT NULL identity PK
  iAsset int NULL
  iSubComponent int NULL
  dWarrantyStart date NULL
  dWarrantyEnd date NULL
  _smtblSubComponentsAssets_iBranchID int NULL
  _smtblSubComponentsAssets_iCreatedBranchID int NULL
  _smtblSubComponentsAssets_iCreatedAgentID int NULL
  _smtblSubComponentsAssets_iModifiedAgentID int NULL
  _smtblSubComponentsAssets_iModifiedBranchID int NULL
  _smtblSubComponentsAssets_dModifiedDate datetime NULL

## _smtblSubComponentsModels
PK: idSubComponentsModels
Columns (9):
  idSubComponentsModels int NOT NULL identity PK
  iModel bigint NULL
  iSubComponent int NULL
  _smtblSubComponentsModels_iBranchID int NULL
  _smtblSubComponentsModels_iCreatedBranchID int NULL
  _smtblSubComponentsModels_iCreatedAgentID int NULL
  _smtblSubComponentsModels_iModifiedAgentID int NULL
  _smtblSubComponentsModels_iModifiedBranchID int NULL
  _smtblSubComponentsModels_dModifiedDate datetime NULL

## _smtblSubComponentsSerialTX
PK: idOtherSubComponentsSerialTX
Columns (10):
  idOtherSubComponentsSerialTX int NOT NULL identity PK
  iSerialNumber int NULL
  iSubComponent int NULL
  _smtblSubComponentsSerialTX_iBranchID int NULL
  _smtblSubComponentsSerialTX_dCreatedDate datetime NULL
  _smtblSubComponentsSerialTX_dModifiedDate datetime NULL
  _smtblSubComponentsSerialTX_iCreatedBranchID int NULL
  _smtblSubComponentsSerialTX_iModifiedBranchID int NULL
  _smtblSubComponentsSerialTX_iCreatedAgentID int NULL
  _smtblSubComponentsSerialTX_iModifiedAgentID int NULL

## _smtblSystemServices
PK: AutoIdx
Columns (9):
  AutoIdx int NOT NULL identity PK
  cServiceName varchar(20) NULL
  dLastActionDate datetime NULL
  _smtblSystemServices_iBranchID int NOT NULL default '0'
  _smtblSystemServices_iCreatedBranchID int NOT NULL default '0'
  _smtblSystemServices_iCreatedAgentID int NOT NULL default '0'
  _smtblSystemServices_iModifiedAgentID int NOT NULL default '0'
  _smtblSystemServices_iModifiedBranchID int NOT NULL default '0'
  _smtblSystemServices_dModifiedDate datetime NULL

## _smtblSystemStructure
PK: AutoIdx
Columns (12):
  AutoIdx int NOT NULL PK
  iParentId int NULL
  iImageIndex int NULL
  cDisplayText varchar(50) NULL
  cModuleName varchar(50) NULL
  iOrder int NULL
  _smtblSystemStructure_iBranchID int NOT NULL default '0'
  _smtblSystemStructure_iCreatedBranchID int NOT NULL default '0'
  _smtblSystemStructure_iCreatedAgentID int NOT NULL default '0'
  _smtblSystemStructure_iModifiedAgentID int NOT NULL default '0'
  _smtblSystemStructure_iModifiedBranchID int NOT NULL default '0'
  _smtblSystemStructure_dModifiedDate datetime NULL

## _smtblTableLog
PK: none
Columns (17):
  AutoIdx bigint NOT NULL identity
  cTableName nvarchar(50) NULL
  cFieldName nvarchar(50) NULL
  cOriginal nvarchar(max) NULL
  cNew nvarchar(max) NULL
  iUserId bigint NULL
  dtStamp datetime NOT NULL default getdate()
  cChangedId nvarchar(max) NOT NULL
  iOriginalId int NULL
  iNewId int NULL
  iChangedId int NULL
  _smtblTableLog_iBranchID int NOT NULL default '0'
  _smtblTableLog_iCreatedBranchID int NOT NULL default '0'
  _smtblTableLog_iCreatedAgentID int NOT NULL default '0'
  _smtblTableLog_iModifiedAgentID int NOT NULL default '0'
  _smtblTableLog_iModifiedBranchID int NOT NULL default '0'
  _smtblTableLog_dModifiedDate datetime NULL

## _smtblTechReference
PK: none
Columns (9):
  AutoIdx numeric(38,0) NOT NULL identity
  iServiceTaskId int NULL
  iTechncianId int NULL
  _smtblTechReference_iBranchID int NOT NULL default '0'
  _smtblTechReference_iCreatedBranchID int NOT NULL default '0'
  _smtblTechReference_iCreatedAgentID int NOT NULL default '0'
  _smtblTechReference_iModifiedAgentID int NOT NULL default '0'
  _smtblTechReference_iModifiedBranchID int NOT NULL default '0'
  _smtblTechReference_dModifiedDate datetime NULL

## _smtblUserDict
PK: idUserDict
Columns (22):
  idUserDict int NOT NULL identity PK
  cFieldName varchar(50) NOT NULL
  cFieldDescription varchar(50) NOT NULL
  iFieldType int NOT NULL
  iFieldSize int NULL
  iFieldIndex int NOT NULL
  cTableName varchar(50) NOT NULL
  cLookupOptions varchar(max) NULL
  bForceValue bit NOT NULL
  cDefaultValue varchar(250) NULL
  iPageIndex int NULL
  cPageName varchar(50) NULL
  iFieldDecimals int NULL
  _smtblUserDict_iBranchID int NULL
  _smtblUserDict_dCreatedDate datetime NULL
  _smtblUserDict_dModifiedDate datetime NULL
  _smtblUserDict_iCreatedBranchID int NULL
  _smtblUserDict_iModifiedBranchID int NULL
  _smtblUserDict_iCreatedAgentID int NULL
  _smtblUserDict_iModifiedAgentID int NULL
  iModuleOptions int NULL
  _smtblUserDict_iChangeSetID int NULL

## _smtblUserRights
PK: AutoIdx
Columns (17):
  AutoIdx int NOT NULL identity PK
  iAgentId int NULL
  iMenuId int NULL
  iParentId int NULL
  iImageIndex int NULL
  cDisplayText varchar(50) NULL
  cModuleName varchar(50) NULL
  bAdd bit NULL
  bEdit bit NULL
  bDelete bit NULL
  bAccess bit NULL
  _smtblUserRights_iBranchID int NOT NULL default '0'
  _smtblUserRights_iCreatedBranchID int NOT NULL default '0'
  _smtblUserRights_iCreatedAgentID int NOT NULL default '0'
  _smtblUserRights_iModifiedAgentID int NOT NULL default '0'
  _smtblUserRights_iModifiedBranchID int NOT NULL default '0'
  _smtblUserRights_dModifiedDate datetime NULL

## _smtblWorker
PK: AutoIdx | UNIQUE: cCode
Columns (23):
  AutoIdx int NOT NULL identity PK
  cCode varchar(20) NOT NULL
  cFirstname varchar(50) NULL
  cLastname varchar(50) NULL
  fCost float NULL
  bActive bit NULL
  bIsTechnician bit NULL
  cAdd1 varchar(50) NULL
  cAdd2 varchar(50) NULL
  cAdd3 varchar(50) NULL
  cPostCode varchar(10) NULL
  cTelephone varchar(20) NULL
  cMobile varchar(20) NULL
  cEmail varchar(50) NULL
  bDeleted bit NOT NULL
  dtStamp datetime NOT NULL default getdate()
  iUserId int NOT NULL
  _smtblWorker_iBranchID int NOT NULL default '0'
  _smtblWorker_iCreatedBranchID int NOT NULL default '0'
  _smtblWorker_iCreatedAgentID int NOT NULL default '0'
  _smtblWorker_iModifiedAgentID int NOT NULL default '0'
  _smtblWorker_iModifiedBranchID int NOT NULL default '0'
  _smtblWorker_dModifiedDate datetime NULL

## _smtblWorkerAvailability
PK: AutoIdx
Columns (11):
  AutoIdx int NOT NULL identity PK
  dDate datetime NULL
  iUserid int NULL
  bDeleted bit NULL
  dtStamp datetime NULL
  _smtblWorkerAvailability_iBranchID int NOT NULL default '0'
  _smtblWorkerAvailability_iCreatedBranchID int NOT NULL default '0'
  _smtblWorkerAvailability_iCreatedAgentID int NOT NULL default '0'
  _smtblWorkerAvailability_iModifiedAgentID int NOT NULL default '0'
  _smtblWorkerAvailability_iModifiedBranchID int NOT NULL default '0'
  _smtblWorkerAvailability_dModifiedDate datetime NULL

## _smtblWorkerAvailabilityLines
PK: AutoIdx
Columns (20):
  AutoIdx int NOT NULL identity PK
  iWorkerAvailabilityId int NULL
  iWorkerId int NULL
  bAvailable bit NULL
  iTime int NULL
  bAL bit NULL
  bLSL bit NULL
  bSL bit NULL
  bAdmin bit NULL
  cAdminNotes varchar(500) NULL
  bOther bit NULL
  cOtherNotes varchar(500) NULL
  dFromTime datetime NULL
  dToTime datetime NULL
  _smtblWorkerAvailabilityLines_iBranchID int NOT NULL default '0'
  _smtblWorkerAvailabilityLines_iCreatedBranchID int NOT NULL default '0'
  _smtblWorkerAvailabilityLines_iCreatedAgentID int NOT NULL default '0'
  _smtblWorkerAvailabilityLines_iModifiedAgentID int NOT NULL default '0'
  _smtblWorkerAvailabilityLines_iModifiedBranchID int NOT NULL default '0'
  _smtblWorkerAvailabilityLines_dModifiedDate datetime NULL

## _smtblWorkerCharges
PK: AutoIdx | UNIQUE: FK_WorkerId+FK_WorkTypeId
Columns (15):
  AutoIdx int NOT NULL identity PK
  fCost float NULL
  fRate float NULL
  FK_WorkerId int NOT NULL
  FK_WorkTypeId int NOT NULL
  bDeleted bit NOT NULL
  dtStamp datetime NOT NULL default getdate()
  iUserId int NOT NULL
  bDefault bit NULL
  _smtblWorkerCharges_iBranchID int NOT NULL default '0'
  _smtblWorkerCharges_iCreatedBranchID int NOT NULL default '0'
  _smtblWorkerCharges_iCreatedAgentID int NOT NULL default '0'
  _smtblWorkerCharges_iModifiedAgentID int NOT NULL default '0'
  _smtblWorkerCharges_iModifiedBranchID int NOT NULL default '0'
  _smtblWorkerCharges_dModifiedDate datetime NULL

## _smtblWorkerDepartments
PK: AutoIdx | UNIQUE: iWorkerId+iDepartmentId
Columns (9):
  AutoIdx int NOT NULL identity PK
  iWorkerId int NOT NULL
  iDepartmentId int NOT NULL
  _smtblWorkerDepartments_iBranchID int NOT NULL default '0'
  _smtblWorkerDepartments_iCreatedBranchID int NOT NULL default '0'
  _smtblWorkerDepartments_iCreatedAgentID int NOT NULL default '0'
  _smtblWorkerDepartments_iModifiedAgentID int NOT NULL default '0'
  _smtblWorkerDepartments_iModifiedBranchID int NOT NULL default '0'
  _smtblWorkerDepartments_dModifiedDate datetime NULL

## _smtblWorkerDetails
PK: AutoIdx | UNIQUE: FK_WorkerId+FK_TypeId+cType
Columns (17):
  AutoIdx int NOT NULL identity PK
  dDate datetime NULL
  cType varchar(10) NULL
  FK_WorkerId int NULL
  FK_TypeId bigint NULL
  bDeleted bit NOT NULL
  dtStamp datetime NOT NULL default getdate()
  iUserId int NOT NULL
  dRenewalDate datetime NULL
  cDocuments varchar(400) NULL
  cDocDescription varchar(50) NULL
  _smtblWorkerDetails_iBranchID int NOT NULL default '0'
  _smtblWorkerDetails_iCreatedBranchID int NOT NULL default '0'
  _smtblWorkerDetails_iCreatedAgentID int NOT NULL default '0'
  _smtblWorkerDetails_iModifiedAgentID int NOT NULL default '0'
  _smtblWorkerDetails_iModifiedBranchID int NOT NULL default '0'
  _smtblWorkerDetails_dModifiedDate datetime NULL

## _smtblWorkerDocuments
PK: none
Columns (12):
  iDocId int NOT NULL identity
  cDocName varchar(400) NULL
  cDocRealName varchar(400) NULL
  bActive bit NULL
  cDescription varchar(400) NULL
  iFK_iAutoIdx int NULL
  _smtblWorkerDocuments_iBranchID int NOT NULL default '0'
  _smtblWorkerDocuments_iCreatedBranchID int NOT NULL default '0'
  _smtblWorkerDocuments_iCreatedAgentID int NOT NULL default '0'
  _smtblWorkerDocuments_iModifiedAgentID int NOT NULL default '0'
  _smtblWorkerDocuments_iModifiedBranchID int NOT NULL default '0'
  _smtblWorkerDocuments_dModifiedDate datetime NULL

## _smtblWorkerTimes
PK: AutoIdx
Columns (20):
  AutoIdx int NOT NULL identity PK
  iWorkerId int NULL
  iServiceTaskId int NULL
  iWorkCodeId int NULL
  dDate datetime NULL
  dFromTime datetime NULL
  dToTime datetime NULL
  iMins int NULL
  cComments ntext NULL
  iUserId int NULL
  dtStamp datetime NULL
  bDeleted bit NULL
  SpendTime decimal(15,2) NULL
  iWarehouse int NULL
  _smtblWorkerTimes_iBranchID int NOT NULL default '0'
  _smtblWorkerTimes_iCreatedBranchID int NOT NULL default '0'
  _smtblWorkerTimes_iCreatedAgentID int NOT NULL default '0'
  _smtblWorkerTimes_iModifiedAgentID int NOT NULL default '0'
  _smtblWorkerTimes_iModifiedBranchID int NOT NULL default '0'
  _smtblWorkerTimes_dModifiedDate datetime NULL

## NT_Suppliers
PK: NTSupID
Columns (22):
  NTSupID int NOT NULL identity PK
  num int NULL
  Name_of_Supplier/Person nvarchar(255) NOT NULL
  Registration nvarchar(20) NULL
  id_number nvarchar(20) NULL
  Reason_for_Restriction nvarchar(255) NULL
  Period_From datetime NULL
  Period_To datetime NULL
  Authorised_by nvarchar(100) NULL
  Still_Blocked bit NOT NULL
  Reason_for_Removal nvarchar(100) NULL
  Date_of_entry datetime NULL
  Date_of_removal datetime NULL
  NT_Suppliers_iBranchID int NULL
  NT_Suppliers_dCreatedDate datetime NULL
  NT_Suppliers_dModifiedDate datetime NULL
  NT_Suppliers_iCreatedBranchID int NULL
  NT_Suppliers_iModifiedBranchID int NULL
  NT_Suppliers_iCreatedAgentID int NULL
  NT_Suppliers_iModifiedAgentID int NULL
  NT_Suppliers_iChangeSetID int NULL
  NT_Suppliers_Checksum binary(20) NULL

## NT_Suppliers_Audit
PK: iNTSupAuditID
Columns (7):
  iNTSupAuditID int NOT NULL identity PK
  NTSupID int NOT NULL
  PeriodFrom datetime NULL
  PeriodTo datetime NULL
  StillBlocked bit NULL
  NT_SupplierAudit_dModifiedDate datetime NOT NULL default getdate()
  NT_SupplierAudit_iModifiedby int NULL

## PR_Defaults
PK: none
Columns (25):
  iNextNum_Pmt int NOT NULL default (1)
  iPadTo_Pmt int NOT NULL default (4)
  cPrefix_Pmt nvarchar(3) NULL
  iNextNum_Rec int NOT NULL default (1)
  iPadTo_Rec int NOT NULL default (4)
  cPrefix_Rec nvarchar(3) NULL
  iBankGLAccId int NULL
  iAPGLAccId int NULL
  iARGLAccId int NULL
  iTrCodeId int NULL
  iTenderTypeId int NULL
  isMultiCurrEnable bit NULL
  isPrevVouchReqrd bit NULL
  isSplitAllocationEnable bit NULL
  PR_Defaults_iBranchID int NULL
  PR_Defaults_dCreatedDate datetime NULL
  PR_Defaults_dModifiedDate datetime NULL
  PR_Defaults_iCreatedBranchID int NULL
  PR_Defaults_iModifiedBranchID int NULL
  PR_Defaults_iCreatedAgentID int NULL
  PR_Defaults_iModifiedAgentID int NULL
  PR_Defaults_iChangeSetID int NULL
  PR_Defaults_Checksum binary(20) NULL
  bUseWorkflow bit NOT NULL default (0)
  iIncidentType int NOT NULL default (0)

## PR_JrBatches
PK: idJrBatches
Columns (19):
  idJrBatches int NOT NULL identity PK
  iVoucherTypeID int NOT NULL
  cReference nvarchar(50) NULL
  dBatchDate datetime NULL
  iProjectID int NULL
  cNarrative nvarchar(200) NULL
  bProcessed bit NOT NULL
  iTrCodeId int NOT NULL
  iIncidentTypeId int NOT NULL default (0)
  iIncidentID int NOT NULL default (0)
  PR_JrBatches_iBranchID int NULL
  PR_JrBatches_dCreatedDate datetime NULL
  PR_JrBatches_dModifiedDate datetime NULL
  PR_JrBatches_iCreatedBranchID int NULL
  PR_JrBatches_iModifiedBranchID int NULL
  PR_JrBatches_iCreatedAgentID int NULL
  PR_JrBatches_iModifiedAgentID int NULL
  PR_JrBatches_iChangeSetID int NULL
  PR_JrBatches_Checksum binary(20) NULL

## PR_JrBatchLines
PK: idJrBatchLines
Columns (21):
  idJrBatchLines int NOT NULL identity PK
  iJrBatchesID int NOT NULL
  dLineDate datetime NOT NULL
  iPeriod int NOT NULL
  iAccountID int NOT NULL
  cAccountName nvarchar(50) NULL
  cLineReference nvarchar(50) NULL
  cLineDescription nvarchar(100) NULL
  fDebitAmt float NOT NULL
  fCreditAmt float NOT NULL
  iLineProjectID int NULL
  iLineID int NOT NULL
  PR_JrBatchLines_iBranchID int NULL
  PR_JrBatchLines_dCreatedDate datetime NULL
  PR_JrBatchLines_dModifiedDate datetime NULL
  PR_JrBatchLines_iCreatedBranchID int NULL
  PR_JrBatchLines_iModifiedBranchID int NULL
  PR_JrBatchLines_iCreatedAgentID int NULL
  PR_JrBatchLines_iModifiedAgentID int NULL
  PR_JrBatchLines_iChangeSetID int NULL
  PR_JrBatchLines_Checksum binary(20) NULL

## PR_PmtRec
PK: idPR_PmtRec
Columns (57):
  idPR_PmtRec int NOT NULL identity PK
  Audit_No nvarchar(50) NULL
  bIsReceipt bit NOT NULL default (1)
  iModule int NOT NULL default (0)
  iCustSuppGLAccId int NULL
  iBankAccountID int NULL
  iAPAccId int NULL
  iARAccId int NULL
  iGrpId int NULL
  iTrAccId int NULL
  iARTrAccId int NULL
  fAmount float NOT NULL default (0)
  iTenderTypeId int NOT NULL default (0)
  dExtraDate datetime NULL
  TxDate datetime NULL
  Reference nvarchar(50) NULL
  Description nvarchar(100) NULL
  Username nvarchar(50) NULL
  cChequeNo nvarchar(50) NULL
  iBankLink int NULL
  cBankBranch nvarchar(50) NULL
  cBankRefNo nvarchar(50) NULL
  cEFTAccountNo nvarchar(50) NULL
  cAccountHolder nvarchar(50) NULL
  cCardNo nvarchar(50) NULL
  cCardType nvarchar(50) NULL
  dCardExpiryDate nvarchar(50) NULL
  cCardAuthCode nvarchar(50) NULL
  bProcessUnprocessed nvarchar(50) NULL
  bApproved bit NULL
  cCabNo nvarchar(50) NULL
  cOwnerLessee nvarchar(50) NULL
  cCurrencySymbol nvarchar(50) NULL
  fExchangeRate float NOT NULL default (1)
  fHomeAmount float NOT NULL default (0)
  fForeignAmount float NOT NULL default (0)
  bIsHomeCurrency bit NULL
  iCurrencyLink int NULL
  iVoucherID int NOT NULL default (1)
  cNarrative nvarchar(500) NULL
  fk_iProjectID int NULL
  bSpiltTrans bit NULL
  cAccountPayee nvarchar(50) NULL
  bPostDated bit NOT NULL default (0)
  bPostDatedChqCancelled bit NOT NULL default (0)
  bIsPrinted bit NOT NULL default (0)
  PR_PmtRec_iBranchID int NULL
  PR_PmtRec_dCreatedDate datetime NULL
  PR_PmtRec_dModifiedDate datetime NULL
  PR_PmtRec_iCreatedBranchID int NULL
  PR_PmtRec_iModifiedBranchID int NULL
  PR_PmtRec_iCreatedAgentID int NULL
  PR_PmtRec_iModifiedAgentID int NULL
  PR_PmtRec_iChangeSetID int NULL
  PR_PmtRec_Checksum binary(20) NULL
  iIncidentTypeId int NOT NULL default (0)
  iIncidentID int NOT NULL default (0)

## PR_ReportLayoutNew
PK: idReportLayout
Columns (16):
  idReportLayout int NOT NULL identity PK
  cRptDescription nvarchar(80) NULL
  iModuleId int NULL
  iVersion int NULL
  nLayout varbinary(max) NOT NULL
  bReadOnly bit NOT NULL
  bIsDefaultLayout bit NULL
  PR_ReportLayoutNew_iBranchID int NULL
  PR_ReportLayoutNew_dCreatedDate datetime NULL
  PR_ReportLayoutNew_dModifiedDate datetime NULL
  PR_ReportLayoutNew_iCreatedBranchID int NULL
  PR_ReportLayoutNew_iModifiedBranchID int NULL
  PR_ReportLayoutNew_iCreatedAgentID int NULL
  PR_ReportLayoutNew_iModifiedAgentID int NULL
  PR_ReportLayoutNew_iChangeSetID int NULL
  PR_ReportLayoutNew_Checksum binary(20) NULL

## PR_RoleAuthorisation
PK: iRoleAuthID
Columns (17):
  iRoleAuthID int NOT NULL identity PK
  fk_iUserRoleID int NULL
  fk_iVoucherType int NULL
  cRole nvarchar(50) NULL
  fMaxAmount float NULL
  bSave bit NULL
  bProcess bit NULL
  bReprint bit NULL
  PR_RoleAuthorisation_iBranchID int NULL
  PR_RoleAuthorisation_dCreatedDate datetime NULL
  PR_RoleAuthorisation_dModifiedDate datetime NULL
  PR_RoleAuthorisation_iCreatedBranchID int NULL
  PR_RoleAuthorisation_iModifiedBranchID int NULL
  PR_RoleAuthorisation_iCreatedAgentID int NULL
  PR_RoleAuthorisation_iModifiedAgentID int NULL
  PR_RoleAuthorisation_iChangeSetID int NULL
  PR_RoleAuthorisation_Checksum binary(20) NULL

## PR_RoleVoucherAssociation
PK: iRoleVhcID
Columns (13):
  iRoleVhcID int NOT NULL identity PK
  fk_iRoleAuthorisationId int NULL
  bSelect bit NULL
  fk_iVoucherTypeId int NULL
  PR_RoleVoucherAssociation_iBranchID int NULL
  PR_RoleVoucherAssociation_dCreatedDate datetime NULL
  PR_RoleVoucherAssociation_dModifiedDate datetime NULL
  PR_RoleVoucherAssociation_iCreatedBranchID int NULL
  PR_RoleVoucherAssociation_iModifiedBranchID int NULL
  PR_RoleVoucherAssociation_iCreatedAgentID int NULL
  PR_RoleVoucherAssociation_iModifiedAgentID int NULL
  PR_RoleVoucherAssociation_iChangeSetID int NULL
  PR_RoleVoucherAssociation_Checksum binary(20) NULL

## PR_SplitInfo
PK: idPR_Split
Columns (20):
  idPR_Split int NOT NULL identity PK
  idPR_PmtRec int NULL
  iCustSuppGLAccId int NULL
  iBankAccountID int NULL
  fExchangeRate float NOT NULL default (1)
  fHomeAmount float NOT NULL default (0)
  fForeignAmount float NOT NULL default (0)
  iCurrencyLink int NULL
  cParticulars nvarchar(500) NULL
  iProjectID int NOT NULL default (0)
  cDescription nvarchar(100) NULL
  PR_SplitInfo_iBranchID int NULL
  PR_SplitInfo_dCreatedDate datetime NULL
  PR_SplitInfo_dModifiedDate datetime NULL
  PR_SplitInfo_iCreatedBranchID int NULL
  PR_SplitInfo_iModifiedBranchID int NULL
  PR_SplitInfo_iCreatedAgentID int NULL
  PR_SplitInfo_iModifiedAgentID int NULL
  PR_SplitInfo_iChangeSetID int NULL
  PR_SplitInfo_Checksum binary(20) NULL

## PR_UserRoleAssociation
PK: iUserRoleID
Columns (14):
  iUserRoleID int NOT NULL identity PK
  fk_iRoleAuthorisationId int NULL
  fk_iUserId int NULL
  cUser nvarchar(50) NULL
  cRole nvarchar(50) NULL
  PR_UserRoleAssociation_iBranchID int NULL
  PR_UserRoleAssociation_dCreatedDate datetime NULL
  PR_UserRoleAssociation_dModifiedDate datetime NULL
  PR_UserRoleAssociation_iCreatedBranchID int NULL
  PR_UserRoleAssociation_iModifiedBranchID int NULL
  PR_UserRoleAssociation_iCreatedAgentID int NULL
  PR_UserRoleAssociation_iModifiedAgentID int NULL
  PR_UserRoleAssociation_iChangeSetID int NULL
  PR_UserRoleAssociation_Checksum binary(20) NULL

## PR_VoucherMaster
PK: iVoucherMstID
Columns (12):
  iVoucherMstID int NOT NULL identity PK
  cVoucherType nvarchar(50) NULL
  cVoucherDescription nvarchar(200) NULL
  PR_VoucherMaster_iBranchID int NULL
  PR_VoucherMaster_dCreatedDate datetime NULL
  PR_VoucherMaster_dModifiedDate datetime NULL
  PR_VoucherMaster_iCreatedBranchID int NULL
  PR_VoucherMaster_iModifiedBranchID int NULL
  PR_VoucherMaster_iCreatedAgentID int NULL
  PR_VoucherMaster_iModifiedAgentID int NULL
  PR_VoucherMaster_iChangeSetID int NULL
  PR_VoucherMaster_Checksum binary(20) NULL

## PR_VoucherType
PK: iVoucherTypeID
Columns (29):
  iVoucherTypeID int NOT NULL identity PK
  fk_iTenderTypeID int NULL
  cVoucherName nvarchar(50) NULL
  cVoucherDescr nvarchar(200) NULL
  iDeftStartNo int NULL
  iPad int NULL
  cSuffix nvarchar(10) NULL
  cCreatedBy nvarchar(10) NULL
  dCreatedOn datetime NULL
  dInActiveOn datetime NULL
  cPrefix nvarchar(10) NULL
  bIsActive bit NULL
  iBankGLAccId int NULL
  iAPGLAccId int NULL
  iARGLAccId int NULL
  iTrCodeId int NULL
  fk_iVoucherMaster int NULL
  cReportName nvarchar(50) NULL
  PR_VoucherType_iBranchID int NULL
  PR_VoucherType_dCreatedDate datetime NULL
  PR_VoucherType_dModifiedDate datetime NULL
  PR_VoucherType_iCreatedBranchID int NULL
  PR_VoucherType_iModifiedBranchID int NULL
  PR_VoucherType_iCreatedAgentID int NULL
  PR_VoucherType_iModifiedAgentID int NULL
  PR_VoucherType_iChangeSetID int NULL
  PR_VoucherType_Checksum binary(20) NULL
  bAutoNo bit NOT NULL default (1)
  bUniqueNo bit NOT NULL default (0)

## RFQ
PK: iRFQID
Columns (51):
  iRFQID int NOT NULL identity PK
  iRequisitionLinesID int NOT NULL
  iModuleID int NOT NULL default (0)
  iStockCodeID int NULL
  cDescription nvarchar(50) NULL
  iWareHouseID int NULL
  fQuantity float NOT NULL default (0.0)
  fQtyProcessed float NOT NULL default (0.0)
  fQtyConfirm float NOT NULL default (0.0)
  fUnitPrice float NOT NULL default (0.0)
  iTaxType int NULL
  fTaxRate float NULL
  fLineDiscount float NULL
  fQuantityLineTotExcl float NULL
  fQuantityLineTaxAmount float NULL
  dExpectedDate datetime NULL
  iRequisitionID int NULL
  OrderNum nvarchar(50) NULL
  iState int NOT NULL default (0)
  iSupplierID int NOT NULL
  dOrderDate datetime NULL
  fQuotedPrice float NULL default (0)
  fQuotedQuantity float NULL default (0)
  Archived bit NULL default (0)
  dLastModifiedDate datetime NULL
  dReceivedDate datetime NULL
  cLineNotes nvarchar(1024) NULL
  dEvaluationdate datetime NULL
  cEvaluationComments nvarchar(1024) NULL
  cFileName nvarchar(100) NULL
  cFileContent varbinary(max) NULL
  dQuotationDeadLine datetime NULL
  bApprovePO bit NULL
  bAuthorizePO bit NULL
  iHODAgent1 int NULL default (0)
  iHODAgent2 int NULL
  fQuotedPriceForeign float NULL
  fQuotedPriceIncl float NULL
  iCriteriaID int NULL default (0)
  bRecommend bit NULL default (0)
  RFQ_iBranchID int NULL
  RFQ_dCreatedDate datetime NULL
  RFQ_dModifiedDate datetime NULL
  RFQ_iCreatedBranchID int NULL
  RFQ_iModifiedBranchID int NULL
  RFQ_iCreatedAgentID int NULL
  RFQ_iModifiedAgentID int NULL
  RFQ_iChangeSetID int NULL
  RFQ_Checksum binary(20) NULL
  iAttributeGroupID int NULL
  xAttribute xml NULL

## RFQ_AgentCostCentreMap
PK: idAgentCostCentreMap | FK: idAgent -> _rtblAgents(idAgents)
Columns (4):
  idAgentCostCentreMap int NOT NULL identity PK
  idAgent int NULL
  CostCentreId varchar(max) NULL
  dLastModifiedDate datetime NULL

## RFQ_AgentSectorMapping
PK: idAgentSectorMap | FK: idAgents -> _rtblAgents(idAgents)
Columns (4):
  idAgentSectorMap int NOT NULL identity PK
  idAgents int NULL
  SectorIds varchar(max) NULL
  dLastModifiedDate datetime NULL default getdate()

## RFQ_APShareholderLinks
PK: idAPShareholderLinks
Columns (14):
  idAPShareholderLinks int NOT NULL identity PK
  iAPShareholderID int NOT NULL
  iSupplierID int NOT NULL
  fPercentage float NOT NULL
  cPositionHeld varchar(50) NOT NULL
  bDirector bit NULL default (0)
  iBranchID int NULL
  dCreatedDate datetime NULL
  dModifiedDate datetime NULL
  iCreatedBranchID int NULL
  iModifiedBranchID int NULL
  iCreatedAgentID int NULL
  iModifiedAgentID int NULL
  iChangeSetID int NULL

## RFQ_Audit
PK: none
Columns (10):
  TableName varchar(128) NOT NULL
  TableID varchar(1000) NULL
  FieldName varchar(128) NOT NULL
  OldValue varchar(1000) NULL
  NewValue varchar(1000) NULL
  UpdateDate datetime NULL default getdate()
  UserName varchar(128) NULL default suser_sname()
  WorkStation varchar(128) NULL default host_name()
  Application varchar(128) NULL default app_name()
  Status int NULL

## RFQ_AuditTables
PK: iAuditTableID
Columns (4):
  iAuditTableID int NOT NULL identity PK
  cTableName nvarchar(200) NULL
  bIsAuditing bit NULL default (0)
  bIsAudit bit NULL default (0)

## RFQ_CostCentre
PK: idCostCentre
Columns (13):
  idCostCentre int NOT NULL identity PK
  cCostCentre nvarchar(100) NULL
  cDescription nvarchar(200) NULL
  bAddedToUDF bit NULL
  RFQ_costcentre_iBranchID int NULL
  RFQ_costcentre_dCreatedDate datetime NULL
  RFQ_costcentre_dModifiedDate datetime NULL
  RFQ_costcentre_iCreatedBranchID int NULL
  RFQ_costcentre_iModifiedBranchID int NULL
  RFQ_costcentre_iCreatedAgentID int NULL
  RFQ_costcentre_iModifiedAgentID int NULL
  RFQ_costcentre_iChangeSetID int NULL
  RFQ_costcentre_Checksum binary(20) NULL

## RFQ_DeviationReason
PK: idDeviationReason
Columns (16):
  idDeviationReason int NOT NULL identity PK
  cCode varchar(10) NULL
  cReasonDesc nvarchar(500) NULL
  bActive bit NULL
  bDefault bit NULL default (0)
  dCreatedDate datetime NULL default getdate()
  dModifiedDate datetime NULL
  RFQ_DeviationReason_iBranchID int NULL
  RFQ_DeviationReason_dCreatedDate datetime NULL
  RFQ_DeviationReason_dModifiedDate datetime NULL
  RFQ_DeviationReason_iCreatedBranchID int NULL
  RFQ_DeviationReason_iModifiedBranchID int NULL
  RFQ_DeviationReason_iCreatedAgentID int NULL
  RFQ_DeviationReason_iModifiedAgentID int NULL
  RFQ_DeviationReason_iChangeSetID int NULL
  RFQ_DeviationReason_Checksum binary(20) NULL

## RFQ_Deviations
PK: idDeviation
Columns (10):
  idDeviation int NOT NULL identity PK
  cScreenName nvarchar(100) NOT NULL
  cType nvarchar(100) NOT NULL
  iUserID int NOT NULL
  iRequisitionID int NOT NULL
  iRFQID int NULL
  EntityID int NULL
  dDeviationDate datetime NULL
  iCommentID int NULL
  cAdditionalComment nvarchar(1000) NULL

## RFQ_Event
PK: iEventID
Columns (3):
  iEventID int NOT NULL identity PK
  cEventCode nvarchar(50) NOT NULL
  cDescription nvarchar(100) NULL

## RFQ_FileAttachment
PK: iFileID
Columns (5):
  iFileID int NOT NULL identity PK
  iRFQID int NOT NULL
  cFileName nvarchar(200) NULL
  cFileContent varbinary(max) NULL
  iSupplierID int NULL

## RFQ_NewQuotationParams
PK: PK_NewQuotationParamID
Columns (10):
  PK_NewQuotationParamID int NOT NULL identity PK
  FK_iRequisitionID int NULL
  FK_QuotationParamID int NULL
  cParamName nvarchar(200) NULL
  IsMandatory bit NULL
  iScore int NULL
  cComment nvarchar(500) NULL
  dLastModifiedDate datetime NULL default getdate()
  cNewComment nvarchar(500) NULL
  iCriteriaID int NULL

## RFQ_NewTender
PK: PK_NewTenderID
Columns (26):
  PK_NewTenderID int NOT NULL identity PK
  cTenderNo nvarchar(50) NOT NULL
  cTenderTitle nvarchar(200) NOT NULL
  cTenderRefNo nvarchar(50) NOT NULL
  cDescription nvarchar(500) NOT NULL
  dAnnouncementDate datetime NOT NULL
  dOpeningDate datetime NOT NULL
  dLastSubmissionDate datetime NOT NULL
  dCompletiondate datetime NOT NULL
  fEarnestMoney float NULL
  bIsEMDMandatory bit NOT NULL default (0)
  iProjectID int NULL
  iIncidentTypeID int NULL
  fTenderTotal float NULL
  cTenderTerms nvarchar(max) NULL
  dLastModifiedDate datetime NOT NULL default getdate()
  iLastModifiedBy int NULL
  RFQ_NewTender_iBranchID int NULL
  RFQ_NewTender_dCreatedDate datetime NULL
  RFQ_NewTender_dModifiedDate datetime NULL
  RFQ_NewTender_iCreatedBranchID int NULL
  RFQ_NewTender_iModifiedBranchID int NULL
  RFQ_NewTender_iCreatedAgentID int NULL
  RFQ_NewTender_iModifiedAgentID int NULL
  RFQ_NewTender_iChangeSetID int NULL
  RFQ_NewTender_Checksum binary(20) NULL

## RFQ_NewTenderDetails
PK: PK_NewTenderDetailID | FK: FK_NewTenderID -> RFQ_NewTender(PK_NewTenderID)
Columns (28):
  PK_NewTenderDetailID int NOT NULL identity PK
  FK_NewTenderID int NOT NULL
  iModuleID int NOT NULL
  iAccountID int NOT NULL
  cDescription varchar(50) NULL
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
  iIncidentID int NULL default (0)
  iPOInvoiceID int NULL default (0)
  fActualPrice float NULL default (0)
  fExchangeRate float NULL
  fExpectedPriceForeign float NULL
  fActualPriceForeign float NULL
  dApprovalDate datetime NULL
  bHasParameters bit NULL default (0)
  dLastModifiedDate datetime NOT NULL default getdate()
  iRequisitionLinesID int NULL
  cSector varchar(100) NULL
  iAttributeGroupID int NULL
  xAttribute xml NULL

## RFQ_NewTenderParams
PK: PK_NewTenderParamID | FK: FK_NewTenderDetailID -> RFQ_NewTenderDetails(PK_NewTenderDetailID), FK_TenderParamID -> RFQ_TenderParameters(PK_TenderParamID)
Columns (9):
  PK_NewTenderParamID int NOT NULL identity PK
  FK_NewTenderDetailID int NULL
  FK_NewTenderID int NULL
  FK_TenderParamID int NULL
  cParamName nvarchar(200) NULL
  IsMandatory bit NULL
  iScore int NULL
  cComment nvarchar(500) NULL
  dLastModifiedDate datetime NULL default getdate()

## RFQ_Notes
PK: iNoteID
Columns (7):
  iNoteID int NOT NULL identity PK
  iRequisitionID int NOT NULL
  iAgentID int NOT NULL
  dDate datetime NOT NULL
  cNote nvarchar(500) NOT NULL
  bStickyNote bit NULL
  cFunctionality nvarchar(50) NULL

## RFQ_ParameterCriteria
PK: idRfqParam
Columns (15):
  idRfqParam int NOT NULL identity PK
  cCriteria nvarchar(100) NULL
  cDescription nvarchar(200) NULL
  bRandomSelection bit NULL default (0)
  iRandomSupplier int NULL
  iNoOfQuotes int NULL
  RFQ_ParameterCriteria_iBranchID int NULL
  RFQ_ParameterCriteria_dCreatedDate datetime NULL
  RFQ_ParameterCriteria_dModifiedDate datetime NULL
  RFQ_ParameterCriteria_iCreatedBranchID int NULL
  RFQ_ParameterCriteria_iModifiedBranchID int NULL
  RFQ_ParameterCriteria_iCreatedAgentID int NULL
  RFQ_ParameterCriteria_iModifiedAgentID int NULL
  RFQ_ParameterCriteria_iChangeSetID int NULL
  RFQ_ParameterCriteria_Checksum binary(20) NULL

## RFQ_ParameterUDF
PK: idRfqParamUdf
Columns (6):
  idRfqParamUdf int NOT NULL identity PK
  fkParameterCriteriaId int NULL
  iUserDictId int NULL
  cFieldName nvarchar(50) NULL
  fWeightage float NULL
  bWeightage bit NULL default (0)

## RFQ_PeopleLinks
PK: iPeopleLinks
Columns (5):
  iPeopleLinks int NOT NULL identity PK
  iPeopleID int NULL
  iDebtorID int NULL
  dCreatedDate datetime NULL
  dModifiedDate datetime NULL

## RFQ_QuotationParameters
PK: PK_QuotationParamID
Columns (15):
  PK_QuotationParamID int NOT NULL identity PK
  cParamName nvarchar(100) NOT NULL
  cDescription nvarchar(500) NULL
  bIsMandatory bit NOT NULL default (0)
  bIsActive bit NULL default (1)
  dLastModifiedDate datetime NOT NULL default getdate()
  RFQ_QuotationParameters_iBranchID int NULL
  RFQ_QuotationParameters_dCreatedDate datetime NULL
  RFQ_QuotationParameters_dModifiedDate datetime NULL
  RFQ_QuotationParameters_iCreatedBranchID int NULL
  RFQ_QuotationParameters_iModifiedBranchID int NULL
  RFQ_QuotationParameters_iCreatedAgentID int NULL
  RFQ_QuotationParameters_iModifiedAgentID int NULL
  RFQ_QuotationParameters_iChangeSetID int NULL
  RFQ_QuotationParameters_Checksum binary(20) NULL

## RFQ_RecordQuotationParams
PK: PK_RecordQuotationParamID
Columns (11):
  PK_RecordQuotationParamID int NOT NULL identity PK
  FK_iRequisitionID int NULL
  FK_iSupplierID int NULL
  FK_QuotationParamID int NULL
  cParamName nvarchar(200) NULL
  iScore int NOT NULL
  iUserScore int NULL
  iPercent float NULL
  cComment nvarchar(500) NULL
  IsMandatory bit NULL
  dLastModifiedDate datetime NULL default getdate()

## RFQ_RecordTender
PK: PK_RecordTender
Columns (33):
  PK_RecordTender int NOT NULL identity PK
  FK_NewTenderID int NOT NULL
  cTenderNo nvarchar(50) NOT NULL
  cTenderTitle nvarchar(200) NOT NULL
  cTenderRefNo nvarchar(50) NOT NULL
  cDescription nvarchar(500) NOT NULL
  dAnnouncementDate datetime NOT NULL
  dOpeningDate datetime NOT NULL
  dLastSubmissionDate datetime NOT NULL
  dCompletiondate datetime NOT NULL
  dSubmissiondate datetime NOT NULL
  fEarnestMoney float NULL
  bIsEMDMandatory bit NOT NULL default (0)
  iSupplierID int NOT NULL
  iProjectID int NULL
  iIncidentTypeID int NULL
  fTenderTotal float NULL
  cTenderTerms nvarchar(max) NULL
  dLastModifiedDate datetime NULL default getdate()
  iRecordSavedBy int NULL
  iScoreEnteredBy int NULL
  iRecordEvaluatedBy int NULL
  dEvaluationdate datetime NULL
  cEvaluationComments nvarchar(max) NULL
  RFQ_RecordTender_iBranchID int NULL
  RFQ_RecordTender_dCreatedDate datetime NULL
  RFQ_RecordTender_dModifiedDate datetime NULL
  RFQ_RecordTender_iCreatedBranchID int NULL
  RFQ_RecordTender_iModifiedBranchID int NULL
  RFQ_RecordTender_iCreatedAgentID int NULL
  RFQ_RecordTender_iModifiedAgentID int NULL
  RFQ_RecordTender_iChangeSetID int NULL
  RFQ_RecordTender_Checksum binary(20) NULL

## RFQ_RecordTenderDetails
PK: PK_RecordTenderDetailID | FK: FK_RecordTenderID -> RFQ_RecordTender(PK_RecordTender)
Columns (31):
  PK_RecordTenderDetailID int NOT NULL identity PK
  FK_RecordTenderID int NOT NULL
  iModuleID int NOT NULL
  iAccountID int NOT NULL
  cDescription varchar(50) NULL
  fQuantity float NOT NULL default (0)
  fQuotedQuantity float NULL
  fExpectedPrice float NOT NULL default (0)
  fQuotedPrice float NULL
  dExpectedDate datetime NULL
  dQuoteddate datetime NULL
  iProjectID int NOT NULL
  iJobID int NOT NULL
  iIncidentTypeID int NOT NULL
  iEscalateGroupID int NOT NULL
  iAgentID int NOT NULL
  cLineNotes varchar(1024) NULL
  iLineStatus int NOT NULL default (0)
  iIncidentID int NOT NULL default (0)
  iPOInvoiceID int NULL default (0)
  fActualPrice float NULL default (0)
  fExchangeRate float NULL
  fExpectedPriceForeign float NULL
  fActualPriceForeign float NULL
  dApprovalDate datetime NULL
  dLastModifiedDate datetime NULL default getdate()
  iRequisitionLinesID int NULL
  cEvaluationComments nvarchar(max) NULL
  cSector varchar(100) NULL
  iAttributeGroupID int NULL
  xAttribute xml NULL

## RFQ_RecordTenderParams
PK: PK_RecordTenderParamID | FK: FK_RecordTenderDetailID -> RFQ_RecordTenderDetails(PK_RecordTenderDetailID), FK_TenderParamID -> RFQ_TenderParameters(PK_TenderParamID)
Columns (11):
  PK_RecordTenderParamID int NOT NULL identity PK
  FK_RecordTenderID int NULL
  FK_RecordTenderDetailID int NULL
  FK_TenderParamID int NULL
  cParamName nvarchar(200) NULL
  iScore int NOT NULL
  iUserScore int NULL
  iPercent float NULL
  cComment nvarchar(500) NULL
  IsMandatory bit NULL
  dLastModifiedDate datetime NULL default getdate()

## RFQ_ReportLayout
PK: none
Columns (7):
  idReportLayout int NOT NULL identity
  cRptDescription varchar(80) NOT NULL
  iModuleId int NULL
  iVersion int NULL
  nLayout varbinary(max) NOT NULL
  bReadOnly bit NOT NULL
  bIsDefaultLayout bit NULL

## RFQ_Sector
PK: idSector
Columns (13):
  idSector int NOT NULL identity PK
  cSector nvarchar(100) NULL
  cDescription nvarchar(200) NULL
  bAddedToUDF bit NULL
  RFq_sector_iBranchID int NULL
  RFq_sector_dCreatedDate datetime NULL
  RFq_sector_dModifiedDate datetime NULL
  RFq_sector_iCreatedBranchID int NULL
  RFq_sector_iModifiedBranchID int NULL
  RFq_sector_iCreatedAgentID int NULL
  RFq_sector_iModifiedAgentID int NULL
  RFq_sector_iChangeSetID int NULL
  RFq_sector_Checksum binary(20) NULL

## RFQ_StockLinks
PK: idStockLinks
Columns (18):
  idStockLinks int NOT NULL identity PK
  iStockID int NOT NULL
  iDCLink int NOT NULL
  bItemActive bit NOT NULL default (1)
  dCreatedDate datetime NULL
  dModifiedDate datetime NULL
  cProductReference varchar(30) NULL
  cModule varchar(2) NULL
  cSupInvCode varchar(20) NULL
  iWhseID int NULL
  bDefaultSupplier bit NOT NULL default (0)
  bDCOnHold bit NOT NULL default (0)
  fLastGRVCost float NULL default (0)
  fManualCost float NOT NULL default (0)
  fminOrderQuantity float NULL
  iBranchID int NULL
  fLeadDays float NULL
  dLastGRVCostDate datetime NULL

## RFQ_SupplierFiltering
PK: idSupplierUDF
Columns (5):
  idSupplierUDF int NOT NULL identity PK
  iUserDictID int NOT NULL
  cFieldName nvarchar(50) NULL
  bCriteria bit NULL
  bIsActive bit NULL

## RFQ_SupplierPreference
PK: idSupplierUDF
Columns (5):
  idSupplierUDF int NOT NULL identity PK
  iUserDictID int NOT NULL
  cFieldName nvarchar(50) NULL
  fWeightage float NULL
  bIsActive bit NULL

## RFQ_TenderDF
PK: PK_Default
Columns (18):
  AutoNewTenderNo bit NULL default (1)
  NewTenderPrefix nvarchar(20) NULL
  NextNewTenderNo int NULL
  NewTenderPadLength int NULL
  AutoRecordTenderNo bit NULL default (1)
  RecordTenderPrefix nvarchar(20) NULL
  NextRecordTenderNo int NULL
  RecordTenderPadLength int NULL
  PK_Default int NOT NULL identity PK
  RFQ_TenderDF_iBranchID int NULL
  RFQ_TenderDF_dCreatedDate datetime NULL
  RFQ_TenderDF_dModifiedDate datetime NULL
  RFQ_TenderDF_iCreatedBranchID int NULL
  RFQ_TenderDF_iModifiedBranchID int NULL
  RFQ_TenderDF_iCreatedAgentID int NULL
  RFQ_TenderDF_iModifiedAgentID int NULL
  RFQ_TenderDF_iChangeSetID int NULL
  RFQ_TenderDF_Checksum binary(20) NULL

## RFQ_TenderParameters
PK: PK_TenderParamID
Columns (15):
  PK_TenderParamID int NOT NULL identity PK
  cParamName nvarchar(100) NOT NULL
  cDescription nvarchar(500) NULL
  bIsMandatory bit NOT NULL default (0)
  bIsActive bit NULL default (1)
  dLastModifiedDate datetime NOT NULL default getdate()
  RFQ_TenderParameters_iBranchID int NULL
  RFQ_TenderParameters_dCreatedDate datetime NULL
  RFQ_TenderParameters_dModifiedDate datetime NULL
  RFQ_TenderParameters_iCreatedBranchID int NULL
  RFQ_TenderParameters_iModifiedBranchID int NULL
  RFQ_TenderParameters_iCreatedAgentID int NULL
  RFQ_TenderParameters_iModifiedAgentID int NULL
  RFQ_TenderParameters_iChangeSetID int NULL
  RFQ_TenderParameters_Checksum binary(20) NULL

## RFQ_UDF
PK: idUDF
Columns (5):
  idUDF int NOT NULL identity PK
  iVendorID int NOT NULL
  cFieldName nvarchar(200) NOT NULL
  cValue nvarchar(max) NOT NULL
  dModifiedDate datetime NULL default getdate()

## RFQ_Vendor
PK: idVendor
Columns (73):
  idVendor int NOT NULL identity PK
  cVendorAccount varchar(20) NOT NULL
  cVendorName varchar(50) NULL
  cDescription varchar(80) NULL
  cVendorTitle nvarchar(5) NULL
  cInit varchar(6) NULL
  bApproved bit NULL default (0)
  bRejected bit NULL default (0)
  bExportToEvo bit NULL default (0)
  dLastModifiedDate datetime NULL default getdate()
  iClassID int NULL
  iAreasID int NULL
  BFOpen int NULL
  CheckTerms bit NOT NULL default (0)
  CT bit NOT NULL default (0)
  Tax_Number varchar(50) NULL
  Registration varchar(20) NULL
  iAgeingTermID int NULL
  AccountTerms int NULL
  Credit_Limit float NULL
  Interest_Rate float NULL
  iSettlementTermsID int NULL
  Discount float NULL
  AutoDisc float NULL
  DiscMtrxRow int NULL
  bForCurAcc bit NOT NULL default (0)
  iCurrencyID int NULL
  Contact_Person varchar(30) NULL
  Delivered_To varchar(30) NULL
  Fax1 varchar(25) NULL
  Fax2 varchar(25) NULL
  cWebPage varchar(50) NULL
  Telephone varchar(25) NULL
  Telephone2 varchar(25) NULL
  Addressee varchar(30) NULL
  EMail varchar(60) NULL
  Post1 varchar(40) NULL
  Post2 varchar(40) NULL
  Post3 varchar(40) NULL
  Post4 varchar(40) NULL
  Post5 varchar(40) NULL
  PostPC varchar(15) NULL
  Physical1 varchar(40) NULL
  Physical2 varchar(40) NULL
  Physical3 varchar(40) NULL
  Physical4 varchar(40) NULL
  Physical5 varchar(40) NULL
  PhysicalPC varchar(15) NULL
  RFQ_Vendor_iBranchID int NULL
  RFQ_Vendor_dCreatedDate datetime NULL
  RFQ_Vendor_dModifiedDate datetime NULL
  RFQ_Vendor_iCreatedBranchID int NULL
  RFQ_Vendor_iModifiedBranchID int NULL
  RFQ_Vendor_iCreatedAgentID int NULL
  RFQ_Vendor_iModifiedAgentID int NULL
  RFQ_Vendor_iChangeSetID int NULL
  RFQ_Vendor_Checksum binary(20) NULL
  BankLink int NULL
  BranchCode varchar(30) NULL
  BankAccNum varchar(30) NULL
  BankAccType varchar(30) NULL
  cBankRefNr varchar(30) NULL
  bStatPrint bit NULL
  bStatEmail bit NULL
  bSourceDocPrint bit NULL
  bSourceDocEmail bit NULL
  cStatEmailPass varchar(20) NULL
  bRemittanceChequeEFTS bit NULL
  iDefTaxTypeID int NOT NULL default (0)
  cIDNumber varchar(20) NULL
  cPassportNumber varchar(20) NULL
  cBankAccHolder varchar(30) NULL
  cBankCode varchar(15) NULL

## RFQ_VendorParameter
PK: VendorParameterID
Columns (15):
  VendorParameterID int NOT NULL identity PK
  cParameterName nvarchar(100) NOT NULL
  cDescription nvarchar(200) NULL
  bIsMandatory bit NULL default (0)
  bIsActive bit NULL default (0)
  dLastModifiedDate datetime NULL default getdate()
  RFQ_VendorParameter_iBranchID int NULL
  RFQ_VendorParameter_dCreatedDate datetime NULL
  RFQ_VendorParameter_dModifiedDate datetime NULL
  RFQ_VendorParameter_iCreatedBranchID int NULL
  RFQ_VendorParameter_iModifiedBranchID int NULL
  RFQ_VendorParameter_iCreatedAgentID int NULL
  RFQ_VendorParameter_iModifiedAgentID int NULL
  RFQ_VendorParameter_iChangeSetID int NULL
  RFQ_VendorParameter_Checksum binary(20) NULL

## RFQ_VendorScore
PK: idVendorScore | FK: iVendorID -> RFQ_Vendor(idVendor), iParameterID -> RFQ_VendorParameter(VendorParameterID)
Columns (14):
  idVendorScore int NOT NULL identity PK
  iVendorID int NOT NULL
  iParameterID int NOT NULL
  cScore nvarchar(50) NOT NULL
  dLastModifiedDate datetime NULL default getdate()
  RFQ_VendorScore_iBranchID int NULL
  RFQ_VendorScore_dCreatedDate datetime NULL
  RFQ_VendorScore_dModifiedDate datetime NULL
  RFQ_VendorScore_iCreatedBranchID int NULL
  RFQ_VendorScore_iModifiedBranchID int NULL
  RFQ_VendorScore_iCreatedAgentID int NULL
  RFQ_VendorScore_iModifiedAgentID int NULL
  RFQ_VendorScore_iChangeSetID int NULL
  RFQ_VendorScore_Checksum binary(20) NULL

## RFQ_WorkflowLink
PK: iWorkflowLinkID | FK: iWorkflowMemberID -> _btblCMWorkflowMembers(idWorkflowMembers), iEventID -> RFQ_Event(iEventID)
Columns (3):
  iWorkflowLinkID int NOT NULL identity PK
  iWorkflowMemberID int NOT NULL
  iEventID int NOT NULL

## RFQDf
PK: DefaultCounter
Columns (57):
  DefaultCounter int NOT NULL identity PK
  iWIPLink int NOT NULL default (0)
  iMasterLink int NOT NULL default (0)
  DCLink int NOT NULL default (1)
  bSalesOrder bit NOT NULL default (0)
  bWareHouse bit NOT NULL default (0)
  cSageAppPath nvarchar(max) NULL
  bIsPrefSupplier bit NULL default (1)
  IsGL bit NULL default (1)
  IsOther bit NULL default (1)
  iIncidentType int NULL
  bVolumeContract bit NULL
  cDBVersion nvarchar(50) NULL
  bResZeroStock bit NULL
  bShowReportLogo bit NULL
  iRFQAutorization int NULL default (1)
  IsQuotedPriceEditable bit NULL
  IsCostCentreEditable bit NULL
  IsQuantityEditable bit NULL
  SetRejectionProcess bit NULL
  bIsLinkedSupplier bit NOT NULL default (1)
  bIsCriteriaAside bit NOT NULL default (0)
  iSupplierIncident int NULL
  bProspectiveSupplier bit NULL
  bRFQWorkflow bit NULL
  AutoNewRFQNo bit NULL default (1)
  NewRFQPrefix nvarchar(20) NULL
  NextNewRFQNo int NULL
  NewRFQPadLength int NULL
  fReportingAmount float NULL
  fRestrictedSupOrdAmt float NULL
  bUseInclPrices bit NULL
  bReportToNatTreasury bit NULL
  cReportingEmailID nvarchar(500) NULL
  bForceEmailToNationalTreasury bit NULL
  bBlockRestrictedSup bit NULL
  cMunicipalityName nvarchar(100) NULL
  bBBBEE_Script bit NOT NULL default (0)
  bRotateOnRFQ bit NOT NULL default (0)
  iRandomSupplier int NOT NULL default (5)
  bForceCostCentre bit NULL
  iSTTrCode int NOT NULL default (0)
  bSupplierRotation bit NOT NULL default (1)
  bSupplierPreference bit NOT NULL default (0)
  cSupplierUDFs nvarchar(max) NULL
  bAutomatedCriteria bit NOT NULL default (0)
  IsST bit NULL
  bForceSector bit NULL
  RFQDF_iBranchID int NULL
  RFQDF_dCreatedDate datetime NULL
  RFQDF_dModifiedDate datetime NULL
  RFQDF_iCreatedBranchID int NULL
  RFQDF_iModifiedBranchID int NULL
  RFQDF_iCreatedAgentID int NULL
  RFQDF_iModifiedAgentID int NULL
  RFQDF_iChangeSetID int NULL
  RFQDF_Checksum binary(20) NULL

## WHT_Batch
PK: idBatch
Columns (26):
  idBatch int NOT NULL identity PK
  batchNumber nvarchar(30) NULL
  batchState nvarchar(2) NULL
  fWHTPercentage float NULL
  fWHTAmount float NULL
  idInvNum bigint NULL
  idInvoiceLines bigint NULL
  GrvNumber nvarchar(18) NULL
  AccountId int NULL
  InvDate smalldatetime NULL
  OrderDate smalldatetime NULL
  DueDate smalldatetime NULL
  DeliveryDate smalldatetime NULL
  OrderNum nvarchar(20) NULL
  cAccountName nvarchar(50) NULL
  fExchangeRate float NULL
  cDescription nvarchar(50) NULL
  fQtyProcessed float NULL
  fUnitPriceExcl float NULL
  fUnitPriceIncl float NULL
  fTaxRate float NULL
  iTaxTypeId int NULL
  ForeignCurrencyID int NULL
  fUnitPriceExclForeign float NULL
  fUnitPriceInclForeign float NULL
  WHT_Batch_iBranchID int NULL

## WHT_BatchStatus
PK: idBatchNumber
Columns (6):
  idBatchNumber int NOT NULL identity PK
  batchNumber nvarchar(30) NULL
  batchStatus bit NULL
  creationDate datetime NULL
  processingDate datetime NULL
  WHT_BatchStatus_iBranchID int NULL

## WHT_DefaultSettings
PK: none
Columns (14):
  idAccountLink int NULL
  idVendorGLAccount int NULL
  idTrCodes int NULL
  SubAccount nvarchar(41) NULL
  Account nvarchar(21) NULL
  AccountType nvarchar(50) NULL
  Description nvarchar(255) NULL
  TrCode nvarchar(4) NULL
  TrCodeDescription nvarchar(100) NULL
  CutOffDate datetime NULL
  isGlItemToShow bit NULL default (1)
  isStItemToShow bit NULL default (1)
  isServiceItemToShow bit NULL default (1)
  WHT_DefaultSettings_iBranchID int NULL

## WHT_State
PK: none
Columns (2):
  State nvarchar(2) NULL
  Description nvarchar(30) NULL

## WHT_TaxMaster
PK: idTaxMaster
Columns (8):
  idTaxMaster int NOT NULL identity PK
  idVendor int NULL
  VendorAccount nvarchar(30) NULL
  VendorName nvarchar(50) NULL
  bIsVendorWHT bit NULL
  fWHTPercentage float NULL
  bIsSelect bit NULL
  WHT_TaxMaster_iBranchID int NULL

## WHT_UserDetails
PK: idUser
Columns (5):
  idUser int NOT NULL identity PK
  cUserName nvarchar(24) NULL
  cPassword nvarchar(100) NULL
  bIsAdmin bit NULL
  cRole nvarchar(30) NULL
