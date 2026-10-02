# Sage 200 Evolution table dictionary - Contact Management

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _rtblActiveDirectoryUsers
PK: iADProfileID
Columns (13):
  iADProfileID int NOT NULL identity PK
  iAgentsID int NOT NULL
  cADProfileUserName varchar(160) NULL
  cADProfileDomainName varchar(160) NULL
  _rtblActiveDirectoryUsers_iBranchID int NULL
  _rtblActiveDirectoryUsers_dCreatedDate datetime NULL
  _rtblActiveDirectoryUsers_dModifiedDate datetime NULL
  _rtblActiveDirectoryUsers_iCreatedBranchID int NULL
  _rtblActiveDirectoryUsers_iModifiedBranchID int NULL
  _rtblActiveDirectoryUsers_iCreatedAgentID int NULL
  _rtblActiveDirectoryUsers_iModifiedAgentID int NULL
  _rtblActiveDirectoryUsers_iChangeSetID int NULL
  _rtblActiveDirectoryUsers_Checksum binary(20) NULL

## _rtblAgentGroupMembers - Agent Group Member (AgentGroupMember)
Alias: Agent Group Member | Freedom Name: AgentGroupMember | Record Identifier: 
Notes: Agent Group Member
PK: iGroupID+iAgentID
Columns (12):
  iGroupID int NOT NULL PK
  iAgentID int NOT NULL PK
  bSysGroupMember bit NOT NULL default (0)
  _rtblAgentGroupMembers_iBranchID int NULL
  _rtblAgentGroupMembers_dCreatedDate datetime NULL
  _rtblAgentGroupMembers_dModifiedDate datetime NULL
  _rtblAgentGroupMembers_iCreatedBranchID int NULL
  _rtblAgentGroupMembers_iModifiedBranchID int NULL
  _rtblAgentGroupMembers_iCreatedAgentID int NULL
  _rtblAgentGroupMembers_iModifiedAgentID int NULL
  _rtblAgentGroupMembers_iChangeSetID int NULL
  _rtblAgentGroupMembers_Checksum binary(20) NULL

## _rtblAgentGroups - Agent Groups (AgentGroup)
Alias: Agent Groups | Freedom Name: AgentGroup | Record Identifier: 
Notes: Agent Groups
PK: idAgentGroups
Columns (32):
  idAgentGroups int NOT NULL identity PK
  bSysGroup bit NOT NULL default (0)
  cGroupName varchar(30) NULL
  cDescription varchar(50) NULL
  cComments varchar(1024) NULL
  bCanAssign bit NOT NULL default (1)
  iAssignRule int NOT NULL default (0)
  iAssignAgent int NULL
  bUseDefaultTree bit NOT NULL default (1)
  bCBGrpAllVisible bit NOT NULL default (0)
  bCBGrpNoneVisible bit NOT NULL default (0)
  bJRGrpAllVisible bit NOT NULL default (0)
  bJRGrpNoneVisible bit NOT NULL default (0)
  bCBGrpAgentVisible bit NOT NULL default (1)
  bJRGrpAgentVisible bit NOT NULL default (1)
  iPOAuthType int NOT NULL default (0)
  iPOIncidentTypeID int NULL
  bPOExclusive bit NOT NULL default (1)
  fPOLimit float NULL
  bPOUseDefaults bit NOT NULL default (1)
  idPOSMenuSetup int NULL
  _rtblAgentGroups_iBranchID int NULL
  _rtblAgentGroups_dCreatedDate datetime NULL
  _rtblAgentGroups_dModifiedDate datetime NULL
  _rtblAgentGroups_iCreatedBranchID int NULL
  _rtblAgentGroups_iModifiedBranchID int NULL
  _rtblAgentGroups_iCreatedAgentID int NULL
  _rtblAgentGroups_iModifiedAgentID int NULL
  _rtblAgentGroups_iChangeSetID int NULL
  _rtblAgentGroups_Checksum binary(20) NULL
  cAccessProcessFlowIDLst varchar(1024) NULL
  cAccessProcessFlowChkLstInd char(1) NOT NULL default (2)

## _rtblAgentLockedOut
PK: IDAgentLockedOut
Columns (14):
  IDAgentLockedOut int NOT NULL identity PK
  iAgentID int NOT NULL
  dLockedOutDate datetime NOT NULL
  dUnlockedOutDate datetime NULL
  iUnlockOutAgentID int NULL
  _rtblAgentLockedOut_iBranchID int NULL
  _rtblAgentLockedOut_dCreatedDate datetime NULL
  _rtblAgentLockedOut_dModifiedDate datetime NULL
  _rtblAgentLockedOut_iCreatedBranchID int NULL
  _rtblAgentLockedOut_iModifiedBranchID int NULL
  _rtblAgentLockedOut_iCreatedAgentID int NULL
  _rtblAgentLockedOut_iModifiedAgentID int NULL
  _rtblAgentLockedOut_iChangeSetID int NULL
  _rtblAgentLockedOut_Checksum binary(20) NULL

## _rtblAgents - Agent (Agent)
Alias: Agent | Freedom Name: Agent | Record Identifier: cAgentName
Notes: Agent
PK: idAgents
Columns (132):
  idAgents int NOT NULL identity PK
  bSysAccount bit NOT NULL default (0)
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
  bCanAssign bit NOT NULL default (1)
  bPwdCanChange bit NOT NULL default (1)
  bPwdMustChange bit NOT NULL default (1)
  bPwdChangeEvery bit NOT NULL default (0)
  iPwdChangeDays int NULL
  dPwdLastChange smalldatetime NULL
  cPwdRemind varchar(160) NULL
  bAgentOutOffice bit NOT NULL default (0)
  bExitWarning bit NOT NULL default (1)
  bCanSetOutOfOffice bit NOT NULL default (1)
  bKnowledgeBaseWarning bit NOT NULL default (1)
  bNewIncidentNotification bit NOT NULL default (0)
  bUseDefaultTree bit NOT NULL default (1)
  bAutoSpellCheck bit NOT NULL default (0)
  iDefIncidentTypeGroupID int NULL
  iDefTillId int NULL
  iDefCashAccount int NULL
  iDefWhseId int NULL
  iNotifyEscalateMinutes int NULL
  iNotifyDueMinutes int NULL
  bForceThisWarehouse bit NOT NULL default (0)
  bAgentActive bit NOT NULL default (1)
  bCBAgNoneVisible bit NOT NULL default (0)
  bCBAgAllVisible bit NOT NULL default (0)
  bJRAgNoneVisible bit NOT NULL default (0)
  bJRAgAllVisible bit NOT NULL default (0)
  bCBUseGrpDefaults bit NOT NULL default (0)
  bJRUseGrpDefaults bit NOT NULL default (0)
  bCBAgOwnVisible bit NOT NULL default (1)
  bJRAgOwnVisible bit NOT NULL default (1)
  iPOAuthType int NOT NULL default (0)
  iPOIncidentTypeID int NULL
  bPOExclusive bit NOT NULL default (1)
  fPOLimit float NULL
  bPOUseGrpDefaults bit NOT NULL default (1)
  cAccessPurchaseWhIDLst varchar(1024) NULL
  cAccessSalesWhIDLst varchar(1024) NULL
  cAccessOtherTxWhIDList varchar(1024) NULL
  cAccessPurchaseWhChkLstInd char(1) NOT NULL default '2'
  cAccessSalesWhChkLstInd char(1) NOT NULL default '2'
  cAccessOtherTxWhChkLstInd char(1) NOT NULL default '2'
  iDefProjectID int NULL
  cAccessProjectIDLst varchar(1024) NULL
  cAccessProjectChkLstInd char(1) NULL
  iDefRepID int NULL
  cAccessRepIDLst varchar(1024) NULL
  cAccessRepChkLstInd char(1) NULL
  Max_LDisc float NOT NULL default (100)
  Max_Disc float NOT NULL default (100)
  cOperatorCode varchar(50) NULL
  cOperatorPassword varchar(50) NULL
  cOperatorNewPassword varchar(50) NULL
  cAccessBranchIDLst varchar(1024) NULL
  cAccessBranchChkLstInd char(1) NULL
  iDocketInputMode int NOT NULL default (0)
  cOperatorCodePOS varchar(50) NULL
  cOperatorPasswordPOS varchar(50) NULL
  cOperatorNewPasswordPOS varchar(50) NULL
  bCanChangeSessionDate bit NOT NULL default (0)
  cEFTOperatorCode varchar(6) NULL
  bSupervisorAgent bit NULL default (0)
  bLockedOut bit NOT NULL default (0)
  cAccessARGroupIDLst varchar(1024) NULL
  cAccessARGroupChkLstInd char(1) NOT NULL default (2)
  bIncludeARNoGroups bit NOT NULL default (1)
  bApplyARGroupsToEnqRep bit NULL
  cAccessAPGroupIDLst varchar(1024) NULL
  cAccessAPGroupChkLstInd char(1) NOT NULL default (2)
  bIncludeAPNoGroups bit NOT NULL default (1)
  bApplyAPGroupsToEnqRep bit NULL
  vbBiometric varchar(max) NULL
  fDefMax_LDisc float NULL
  fDefMax_Disc float NULL
  bApplyAccessRepsToReports bit NULL
  bApplyAccessProjectsToReports bit NULL
  idPOSMenuSetup int NULL
  bAgentIsBuyer bit NOT NULL default (0)
  bUseBiometric bit NOT NULL default (0)
  FiscalPrinterId int NOT NULL default (0)
  FiscalDeviceId int NOT NULL default (0)
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
  cAccessDocCatGroupChkLstInd char(1) NOT NULL default (2)
  iDefDocCatID int NULL
  cAccessDocCatIDLst varchar(1024) NULL
  cAccessDocCatChkLstInd char(1) NOT NULL default (2)
  cAccessIncidentTypeGroupIDLst varchar(1024) NULL
  cAccessIncidentTypeGroupChkLstInd char(1) NOT NULL default (2)
  cAccessIncidentTypeIDLst varchar(1024) NULL
  cAccessIncidentTypeChkLstInd char(1) NOT NULL default (2)
  cSagePayUserName varchar(50) NULL
  cSagePayPassword varchar(160) NULL
  cSagePayPIN varchar(30) NULL
  iAgentLoginScreen int NOT NULL default (0)
  cVisibleBranchesLst nvarchar(1024) NULL
  cVisibleBranchesLstInd nvarchar(1024) NULL
  cVisibleWarehousesLst nvarchar(1024) NULL
  cVisibleWarehousesLstInd nvarchar(1024) NULL
  cAccessProcessFlowIDLst varchar(1024) NULL
  cAccessProcessFlowChkLstInd char(1) NOT NULL default (2)
  cEmailSignature varchar(max) NULL

## _rtblBusClass - Business Classification (Business)
Alias: Business Classification | Freedom Name: Business | Record Identifier: cBusClass
Notes: Business Classification
PK: idBusClass
Columns (11):
  idBusClass int NOT NULL identity PK
  cBusClass varchar(50) NULL
  _rtblBusClass_iBranchID int NULL
  _rtblBusClass_dCreatedDate datetime NULL
  _rtblBusClass_dModifiedDate datetime NULL
  _rtblBusClass_iCreatedBranchID int NULL
  _rtblBusClass_iModifiedBranchID int NULL
  _rtblBusClass_iCreatedAgentID int NULL
  _rtblBusClass_iModifiedAgentID int NULL
  _rtblBusClass_iChangeSetID int NULL
  _rtblBusClass_Checksum binary(20) NULL

## _rtblBusDept - Business Department (BusinessDepartment)
Alias: Business Department | Freedom Name: BusinessDepartment | Record Identifier: 
Notes: Business Department. Contact people can be linked to a specific department.
PK: idBusDept
Columns (11):
  idBusDept int NOT NULL identity PK
  cBusDept varchar(50) NULL
  _rtblBusDept_iBranchID int NULL
  _rtblBusDept_dCreatedDate datetime NULL
  _rtblBusDept_dModifiedDate datetime NULL
  _rtblBusDept_iCreatedBranchID int NULL
  _rtblBusDept_iModifiedBranchID int NULL
  _rtblBusDept_iCreatedAgentID int NULL
  _rtblBusDept_iModifiedAgentID int NULL
  _rtblBusDept_iChangeSetID int NULL
  _rtblBusDept_Checksum binary(20) NULL

## _rtblBusDesig - Business Designation (BusinessDesignation)
Alias: Business Designation | Freedom Name: BusinessDesignation | Record Identifier: 
Notes: Business Designation. Various work titles / designations can be created.
PK: idBusDesig
Columns (11):
  idBusDesig int NOT NULL identity PK
  cBusDesig varchar(50) NULL
  _rtblBusDesig_iBranchID int NULL
  _rtblBusDesig_dCreatedDate datetime NULL
  _rtblBusDesig_dModifiedDate datetime NULL
  _rtblBusDesig_iCreatedBranchID int NULL
  _rtblBusDesig_iModifiedBranchID int NULL
  _rtblBusDesig_iCreatedAgentID int NULL
  _rtblBusDesig_iModifiedAgentID int NULL
  _rtblBusDesig_iChangeSetID int NULL
  _rtblBusDesig_Checksum binary(20) NULL

## _rtblBusType - Business Type (BusinessType)
Alias: Business Type | Freedom Name: BusinessType | Record Identifier: cBusType
Notes: Business Type
PK: idBusType
Columns (11):
  idBusType int NOT NULL identity PK
  cBusType varchar(50) NULL
  _rtblBusType_iBranchID int NULL
  _rtblBusType_dCreatedDate datetime NULL
  _rtblBusType_dModifiedDate datetime NULL
  _rtblBusType_iCreatedBranchID int NULL
  _rtblBusType_iModifiedBranchID int NULL
  _rtblBusType_iCreatedAgentID int NULL
  _rtblBusType_iModifiedAgentID int NULL
  _rtblBusType_iChangeSetID int NULL
  _rtblBusType_Checksum binary(20) NULL

## _rtblClass
PK: idClass
Columns (12):
  idClass int NOT NULL PK
  cDescription varchar(32) NULL
  bAvailable bit NOT NULL default (0)
  _rtblClass_iBranchID int NULL
  _rtblClass_dCreatedDate datetime NULL
  _rtblClass_dModifiedDate datetime NULL
  _rtblClass_iCreatedBranchID int NULL
  _rtblClass_iModifiedBranchID int NULL
  _rtblClass_iCreatedAgentID int NULL
  _rtblClass_iModifiedAgentID int NULL
  _rtblClass_iChangeSetID int NULL
  _rtblClass_Checksum binary(20) NULL

## _rtblCMDefaults - Contact Management Default (ContactManagementDefaults)
Alias: Contact Management Default | Freedom Name: ContactManagementDefaults | Record Identifier: 
Notes: Contact Management Default
PK: idCMDefaults
Columns (47):
  idCMDefaults int NOT NULL identity PK
  iPeopleFilterStLength int NULL
  bAutoContracts bit NOT NULL default (0)
  vContractPrefix varchar(25) NULL
  iContractPadLength int NULL
  iContractFilterStLength int NULL
  vKBPrefix varchar(25) NULL
  iKBPadLength int NULL
  vIncidentPrefix varchar(25) NULL
  iIncidentPadLength int NULL
  bIncDefAgentName bit NOT NULL default (0)
  bIncDispCustNotes bit NOT NULL default (0)
  vDocStorePath varchar(256) NULL
  bRestrictAgents bit NULL default (1)
  bRestrictInActiveAgents bit NULL default (0)
  bColorCodeOverDueDate bit NULL default (0)
  iOverDueColor int NULL
  bSpellCheck bit NOT NULL default (0)
  bAutoIncidents bit NOT NULL default (0)
  bAutoKB bit NOT NULL default (0)
  iDueDateIncrement int NULL
  iDueTimeIncrement int NULL
  bUseExpContracts bit NOT NULL default (0)
  bUseBlockedContracts bit NOT NULL default (0)
  bPostIncidentOnHoldCust bit NOT NULL default (1)
  bSFAOpportunityAutoNum bit NOT NULL default (1)
  cSFAOpportunityNextNum varchar(15) NULL
  iSFAOpportunityPadTo int NULL
  cSFAOpportunityPrefix varchar(25) NULL
  iDeftOpportunityIncidentTypeID int NULL
  bSFAApplyAgentFilter bit NOT NULL default (0)
  bSFAUseSalesOrders bit NOT NULL default (0)
  iSFAReopenOppStatusID int NOT NULL default (0)
  iSFAFilterStLength int NOT NULL default (0)
  bAutoEmailAssignedAgent bit NOT NULL default (0)
  iDocumentFilterStLength int NOT NULL default (0)
  bSourceDocLinked bit NOT NULL default (0)
  iSourceDocLinkDisplay int NOT NULL default (0)
  _rtblCMDefaults_iBranchID int NULL
  _rtblCMDefaults_dCreatedDate datetime NULL
  _rtblCMDefaults_dModifiedDate datetime NULL
  _rtblCMDefaults_iCreatedBranchID int NULL
  _rtblCMDefaults_iModifiedBranchID int NULL
  _rtblCMDefaults_iCreatedAgentID int NULL
  _rtblCMDefaults_iModifiedAgentID int NULL
  _rtblCMDefaults_iChangeSetID int NULL
  _rtblCMDefaults_Checksum binary(20) NULL

## _rtblCompetitor - Competitor (Competitor)
Alias: Competitor | Freedom Name: Competitor | Record Identifier: 
Notes: Competitor
PK: idCompetitor
Columns (12):
  idCompetitor int NOT NULL identity PK
  cCompanyName varchar(50) NULL
  cDescription varchar(100) NULL
  _rtblCompetitor_iBranchID int NULL
  _rtblCompetitor_dCreatedDate datetime NULL
  _rtblCompetitor_dModifiedDate datetime NULL
  _rtblCompetitor_iCreatedBranchID int NULL
  _rtblCompetitor_iModifiedBranchID int NULL
  _rtblCompetitor_iCreatedAgentID int NULL
  _rtblCompetitor_iModifiedAgentID int NULL
  _rtblCompetitor_iChangeSetID int NULL
  _rtblCompetitor_Checksum binary(20) NULL

## _rtblCompetitorProduct - Competitor Product (CompetitorProduct)
Alias: Competitor Product | Freedom Name: CompetitorProduct | Record Identifier: 
Notes: Competitor Product
PK: IDCompetitorProduct
Columns (13):
  IDCompetitorProduct int NOT NULL identity PK
  cProductName varchar(50) NULL
  cDescription varchar(100) NULL
  cDetailedDescription varchar(1024) NULL
  _rtblCompetitorProduct_iBranchID int NULL
  _rtblCompetitorProduct_dCreatedDate datetime NULL
  _rtblCompetitorProduct_dModifiedDate datetime NULL
  _rtblCompetitorProduct_iCreatedBranchID int NULL
  _rtblCompetitorProduct_iModifiedBranchID int NULL
  _rtblCompetitorProduct_iCreatedAgentID int NULL
  _rtblCompetitorProduct_iModifiedAgentID int NULL
  _rtblCompetitorProduct_iChangeSetID int NULL
  _rtblCompetitorProduct_Checksum binary(20) NULL

## _rtblCompetitorProductLink - Competitor Product Link (CompetitorProductLink)
Alias: Competitor Product Link | Freedom Name: CompetitorProductLink | Record Identifier: 
Notes: Competitor Product Link
PK: idCompetitorProductLink
Columns (14):
  idCompetitorProductLink int NOT NULL identity PK
  iCompetitorID int NOT NULL default (0)
  iCompetitorProductID int NOT NULL default (0)
  fProductPrice float NULL
  dDtPriceUpdated datetime NULL
  _rtblCompetitorProductLink_iBranchID int NULL
  _rtblCompetitorProductLink_dCreatedDate datetime NULL
  _rtblCompetitorProductLink_dModifiedDate datetime NULL
  _rtblCompetitorProductLink_iCreatedBranchID int NULL
  _rtblCompetitorProductLink_iModifiedBranchID int NULL
  _rtblCompetitorProductLink_iCreatedAgentID int NULL
  _rtblCompetitorProductLink_iModifiedAgentID int NULL
  _rtblCompetitorProductLink_iChangeSetID int NULL
  _rtblCompetitorProductLink_Checksum binary(20) NULL

## _rtblContractDocLinks - Contract Document Link
Alias: Contract Document Link | Freedom Name:  | Record Identifier: 
Notes: Contract Document Link
PK: idDocLinks
Columns (13):
  idDocLinks int NOT NULL identity PK
  iDocStoreID int NULL
  iLinkSource int NULL default (0)
  iLinkID int NULL
  _rtblContractDocLinks_iBranchID int NULL
  _rtblContractDocLinks_dCreatedDate datetime NULL
  _rtblContractDocLinks_dModifiedDate datetime NULL
  _rtblContractDocLinks_iCreatedBranchID int NULL
  _rtblContractDocLinks_iModifiedBranchID int NULL
  _rtblContractDocLinks_iCreatedAgentID int NULL
  _rtblContractDocLinks_iModifiedAgentID int NULL
  _rtblContractDocLinks_iChangeSetID int NULL
  _rtblContractDocLinks_Checksum binary(20) NULL

## _rtblContracts - Contract (IncidentContracts)
Alias: Contract | Freedom Name: IncidentContracts | Record Identifier: 
Notes: Contract
PK: idContracts
Columns (27):
  idContracts int NOT NULL identity PK
  cContractNumber varchar(50) NULL
  iDebtorID int NOT NULL default (0)
  cContractName varchar(50) NOT NULL
  cContractReference varchar(50) NULL
  dCreated datetime NULL
  dStartDate smalldatetime NOT NULL
  dEndDate smalldatetime NOT NULL
  iBillType int NOT NULL
  iTimeUnit int NOT NULL default (0)
  fAmount float NOT NULL default (0)
  bBlock bit NOT NULL default (0)
  iIncidentTypeID int NULL
  bAllowOverride bit NOT NULL default (1)
  cInvoice varchar(30) NULL
  iUnitsUsed int NOT NULL default (0)
  iRecurrTransID int NULL
  bExtendEndDate bit NOT NULL default (0)
  _rtblContracts_iBranchID int NULL
  _rtblContracts_dCreatedDate datetime NULL
  _rtblContracts_dModifiedDate datetime NULL
  _rtblContracts_iCreatedBranchID int NULL
  _rtblContracts_iModifiedBranchID int NULL
  _rtblContracts_iCreatedAgentID int NULL
  _rtblContracts_iModifiedAgentID int NULL
  _rtblContracts_iChangeSetID int NULL
  _rtblContracts_Checksum binary(20) NULL

## _rtblContractTemplates
PK: idContractTemplates | UNIQUE: idContractTemplates
Columns (21):
  idContractTemplates int NOT NULL identity PK
  cTemplateName varchar(50) NOT NULL
  iDefYears int NOT NULL default (0)
  iDefMonths int NOT NULL default (0)
  iDefDays int NOT NULL default (0)
  iBillType int NOT NULL default (0)
  iTimeUnit int NOT NULL default (0)
  fAmount float NOT NULL default (0)
  iIncidentTypeID int NULL
  bAllowOverride bit NOT NULL default (1)
  iCInvTemplateID int NULL
  iRRConfigurationID int NULL
  _rtblContractTemplates_iBranchID int NULL
  _rtblContractTemplates_dCreatedDate datetime NULL
  _rtblContractTemplates_dModifiedDate datetime NULL
  _rtblContractTemplates_iCreatedBranchID int NULL
  _rtblContractTemplates_iModifiedBranchID int NULL
  _rtblContractTemplates_iCreatedAgentID int NULL
  _rtblContractTemplates_iModifiedAgentID int NULL
  _rtblContractTemplates_iChangeSetID int NULL
  _rtblContractTemplates_Checksum binary(20) NULL

## _rtblContractTx - Contract Transactions (ContractTransaction)
Alias: Contract Transactions | Freedom Name: ContractTransaction | Record Identifier: 
Notes: Contract Transactions
PK: idContractTx
Columns (17):
  idContractTx int NOT NULL identity PK
  dDate smalldatetime NOT NULL
  iContractID int NOT NULL
  iIncidentID int NOT NULL
  fAmount float NOT NULL default (0)
  iDurationMins int NOT NULL default (0)
  dTimeStamp datetime NULL
  cTxInvoice varchar(30) NULL
  _rtblContractTx_iBranchID int NULL
  _rtblContractTx_dCreatedDate datetime NULL
  _rtblContractTx_dModifiedDate datetime NULL
  _rtblContractTx_iCreatedBranchID int NULL
  _rtblContractTx_iModifiedBranchID int NULL
  _rtblContractTx_iCreatedAgentID int NULL
  _rtblContractTx_iModifiedAgentID int NULL
  _rtblContractTx_iChangeSetID int NULL
  _rtblContractTx_Checksum binary(20) NULL

## _rtblCountry - Country (Country)
Alias: Country | Freedom Name: Country | Record Identifier: cCountryName
Notes: Country
PK: idCountry
Columns (11):
  idCountry int NOT NULL identity PK
  cCountryName varchar(30) NOT NULL
  _rtblCountry_iBranchID int NULL
  _rtblCountry_dCreatedDate datetime NULL
  _rtblCountry_dModifiedDate datetime NULL
  _rtblCountry_iCreatedBranchID int NULL
  _rtblCountry_iModifiedBranchID int NULL
  _rtblCountry_iCreatedAgentID int NULL
  _rtblCountry_iModifiedAgentID int NULL
  _rtblCountry_iChangeSetID int NULL
  _rtblCountry_Checksum binary(20) NULL

## _rtblDocCat - Document Category (DocumentCategory)
Alias: Document Category | Freedom Name: DocumentCategory | Record Identifier: 
Notes: Document Category
PK: idDocCat
Columns (11):
  idDocCat int NOT NULL identity PK
  cDescription varchar(64) NOT NULL
  _rtblDocCat_iBranchID int NULL
  _rtblDocCat_dCreatedDate datetime NULL
  _rtblDocCat_dModifiedDate datetime NULL
  _rtblDocCat_iCreatedBranchID int NULL
  _rtblDocCat_iModifiedBranchID int NULL
  _rtblDocCat_iCreatedAgentID int NULL
  _rtblDocCat_iModifiedAgentID int NULL
  _rtblDocCat_iChangeSetID int NULL
  _rtblDocCat_Checksum binary(20) NULL

## _rtblDocLinks - Document Link (DocumentLinks)
Alias: Document Link | Freedom Name: DocumentLinks | Record Identifier: 
Notes: Document Link
PK: idDocLinks
Columns (13):
  idDocLinks int NOT NULL identity PK
  iDocStoreID int NOT NULL
  iLinkSource int NOT NULL default (0)
  iLinkID int NOT NULL
  _rtblDocLinks_iBranchID int NULL
  _rtblDocLinks_dCreatedDate datetime NULL
  _rtblDocLinks_dModifiedDate datetime NULL
  _rtblDocLinks_iCreatedBranchID int NULL
  _rtblDocLinks_iModifiedBranchID int NULL
  _rtblDocLinks_iCreatedAgentID int NULL
  _rtblDocLinks_iModifiedAgentID int NULL
  _rtblDocLinks_iChangeSetID int NULL
  _rtblDocLinks_Checksum binary(20) NULL

## _rtblDocStore
PK: idDocStore
Columns (18):
  idDocStore int NOT NULL identity PK
  cDocStoreName varchar(20) NOT NULL
  cDocName varchar(255) NOT NULL
  iDocCatID int NULL
  cDocDescription varchar(255) NOT NULL
  dModified smalldatetime NOT NULL
  iAgentID int NOT NULL
  nIcon image NULL
  bIsActive bit NOT NULL default (1)
  _rtblDocStore_iBranchID int NULL
  _rtblDocStore_dCreatedDate datetime NULL
  _rtblDocStore_dModifiedDate datetime NULL
  _rtblDocStore_iCreatedBranchID int NULL
  _rtblDocStore_iModifiedBranchID int NULL
  _rtblDocStore_iCreatedAgentID int NULL
  _rtblDocStore_iModifiedAgentID int NULL
  _rtblDocStore_iChangeSetID int NULL
  _rtblDocStore_Checksum binary(20) NULL

## _rtblEscalateGrp - Escalation Group (EscalationGroup)
Alias: Escalation Group | Freedom Name: EscalationGroup | Record Identifier: 
Notes: Escalation Groups can be created for various groups of agents. This table contains a list of all the escalation groups created on the database.
PK: idEscalateGrp
Columns (11):
  idEscalateGrp int NOT NULL identity PK
  cDescription varchar(30) NOT NULL
  _rtblEscalateGrp_iBranchID int NULL
  _rtblEscalateGrp_dCreatedDate datetime NULL
  _rtblEscalateGrp_dModifiedDate datetime NULL
  _rtblEscalateGrp_iCreatedBranchID int NULL
  _rtblEscalateGrp_iModifiedBranchID int NULL
  _rtblEscalateGrp_iCreatedAgentID int NULL
  _rtblEscalateGrp_iModifiedAgentID int NULL
  _rtblEscalateGrp_iChangeSetID int NULL
  _rtblEscalateGrp_Checksum binary(20) NULL

## _rtblEscalateGrpMembers - Escalation Group Member (EscalationGroupMembers)
Alias: Escalation Group Member | Freedom Name: EscalationGroupMembers | Record Identifier: 
Notes: Escalation Group Member
PK: idEscalateGrpMembers | UNIQUE: idEscalateGrpMembers
Columns (14):
  idEscalateGrpMembers int NOT NULL identity PK
  iEscalateGrpID int NOT NULL
  iAgentGroupID int NOT NULL
  iSequence int NOT NULL
  iEscalateMins int NOT NULL default (0)
  _rtblEscalateGrpMembers_iBranchID int NULL
  _rtblEscalateGrpMembers_dCreatedDate datetime NULL
  _rtblEscalateGrpMembers_dModifiedDate datetime NULL
  _rtblEscalateGrpMembers_iCreatedBranchID int NULL
  _rtblEscalateGrpMembers_iModifiedBranchID int NULL
  _rtblEscalateGrpMembers_iCreatedAgentID int NULL
  _rtblEscalateGrpMembers_iModifiedAgentID int NULL
  _rtblEscalateGrpMembers_iChangeSetID int NULL
  _rtblEscalateGrpMembers_Checksum binary(20) NULL

## _rtblIncidentAction - Incident Action (IncidentAction)
Alias: Incident Action | Freedom Name: IncidentAction | Record Identifier: 
Notes: Incident Action
PK: idIncidentAction
Columns (12):
  idIncidentAction int NOT NULL PK
  cDescription varchar(32) NULL
  cPDescription varchar(32) NULL
  _rtblIncidentAction_iBranchID int NULL
  _rtblIncidentAction_dCreatedDate datetime NULL
  _rtblIncidentAction_dModifiedDate datetime NULL
  _rtblIncidentAction_iCreatedBranchID int NULL
  _rtblIncidentAction_iModifiedBranchID int NULL
  _rtblIncidentAction_iCreatedAgentID int NULL
  _rtblIncidentAction_iModifiedAgentID int NULL
  _rtblIncidentAction_iChangeSetID int NULL
  _rtblIncidentAction_Checksum binary(20) NULL

## _rtblIncidentCat - Incident Category (IncidentCategory)
Alias: Incident Category | Freedom Name: IncidentCategory | Record Identifier: 
Notes: Incident Category
PK: idIncidentCat
Columns (11):
  idIncidentCat int NOT NULL identity PK
  cDescription varchar(32) NULL
  _rtblIncidentCat_iBranchID int NULL
  _rtblIncidentCat_dCreatedDate datetime NULL
  _rtblIncidentCat_dModifiedDate datetime NULL
  _rtblIncidentCat_iCreatedBranchID int NULL
  _rtblIncidentCat_iModifiedBranchID int NULL
  _rtblIncidentCat_iCreatedAgentID int NULL
  _rtblIncidentCat_iModifiedAgentID int NULL
  _rtblIncidentCat_iChangeSetID int NULL
  _rtblIncidentCat_Checksum binary(20) NULL

## _rtblIncidentLog - Incident Log (IncidentLines)
Alias: Incident Log | Freedom Name: IncidentLines | Record Identifier: 
Notes: Incident Log
PK: idIncidentLog
Columns (20):
  idIncidentLog int NOT NULL identity PK
  iIncidentID int NOT NULL
  dActionDate datetime NOT NULL
  iIncidentActionID int NOT NULL
  cResolution text NULL
  iAgentID int NULL
  bProxy bit NOT NULL default (0)
  iNewAgentID int NULL
  cSourceContent text NULL
  cSourceID varchar(128) NULL default ''
  iRejectReasonID int NULL
  _rtblIncidentLog_iBranchID int NULL
  _rtblIncidentLog_dCreatedDate datetime NULL
  _rtblIncidentLog_dModifiedDate datetime NULL
  _rtblIncidentLog_iCreatedBranchID int NULL
  _rtblIncidentLog_iModifiedBranchID int NULL
  _rtblIncidentLog_iCreatedAgentID int NULL
  _rtblIncidentLog_iModifiedAgentID int NULL
  _rtblIncidentLog_iChangeSetID int NULL
  _rtblIncidentLog_Checksum binary(20) NULL

## _rtblIncidentLog_Archive - Incident Log Archive
Alias: Incident Log Archive | Freedom Name:  | Record Identifier: 
Notes: Incident Log Archive
PK: idIncidentLog
Columns (20):
  idIncidentLog int NOT NULL PK
  iIncidentID int NOT NULL
  dActionDate datetime NOT NULL
  iIncidentActionID int NOT NULL
  cResolution text NULL
  iAgentID int NULL
  bProxy bit NOT NULL default (0)
  iNewAgentID int NULL
  cSourceContent text NULL
  cSourceID varchar(128) NOT NULL default ''
  iRejectReasonID int NULL
  _rtblIncidentLog_Archive_iBranchID int NULL
  _rtblIncidentLog_Archive_dCreatedDate datetime NULL
  _rtblIncidentLog_Archive_dModifiedDate datetime NULL
  _rtblIncidentLog_Archive_iCreatedBranchID int NULL
  _rtblIncidentLog_Archive_iModifiedBranchID int NULL
  _rtblIncidentLog_Archive_iCreatedAgentID int NULL
  _rtblIncidentLog_Archive_iModifiedAgentID int NULL
  _rtblIncidentLog_Archive_iChangeSetID int NULL
  _rtblIncidentLog_Archive_Checksum binary(20) NULL

## _rtblIncidentPriority - Incident Priority (ContactManagementIncidentPriority)
Alias: Incident Priority | Freedom Name: ContactManagementIncidentPriority | Record Identifier: cDescription
Notes: Incident Prioriy
PK: idIncidentPriority
Columns (13):
  idIncidentPriority int NOT NULL PK
  cDescription varchar(32) NULL
  iColor int NULL
  bDefault bit NULL default (0)
  _rtblIncidentPriority_iBranchID int NULL
  _rtblIncidentPriority_dCreatedDate datetime NULL
  _rtblIncidentPriority_dModifiedDate datetime NULL
  _rtblIncidentPriority_iCreatedBranchID int NULL
  _rtblIncidentPriority_iModifiedBranchID int NULL
  _rtblIncidentPriority_iCreatedAgentID int NULL
  _rtblIncidentPriority_iModifiedAgentID int NULL
  _rtblIncidentPriority_iChangeSetID int NULL
  _rtblIncidentPriority_Checksum binary(20) NULL

## _rtblIncidents
PK: idIncidents
Columns (58):
  idIncidents int NOT NULL identity PK
  dCreated datetime NOT NULL
  dLastModified datetime NOT NULL
  iClassID int NOT NULL
  iIncidentStatusID int NOT NULL
  bRequireAck bit NOT NULL default (0)
  iDebtorID int NOT NULL default (0)
  iPersonID int NOT NULL default (0)
  iIncidentCatID int NULL default (0)
  cOurRef varchar(50) NULL
  cYourRef varchar(50) NULL
  cOutline varchar(1024) NULL
  iPriorityID int NOT NULL
  iEscalateGrpID int NOT NULL default (0)
  iAgentGroupID int NOT NULL default (0)
  iCurrentAgentID int NOT NULL
  iContractTxID int NOT NULL default (0)
  iStockID int NOT NULL default (0)
  iPrivNode int NULL
  iIncidentTypeID int NOT NULL default (0)
  dDueBy datetime NULL
  iDuration int NULL
  iContractID int NULL
  cChangeLog text NULL
  iIncidentTypeGroupID int NULL
  iWorkflowID int NULL
  iWorkflowStatusID int NULL
  bHasBeenRejected bit NOT NULL default (0)
  iSupplierID int NULL
  iFixedAssetID int NULL
  iEmployeeID int NULL
  iProjectID int NULL
  iJobCostingID int NULL
  iProspectID int NOT NULL default (0)
  iOpportunityID int NOT NULL default (0)
  iPOInvoiceID bigint NOT NULL default (0)
  bPOViewed bit NOT NULL default (0)
  iRequisitionID int NOT NULL default (0)
  iLinkID int NULL
  iRfqID int NULL
  iSIMReqID int NULL
  _rtblIncidents_iBranchID int NULL
  _rtblIncidents_dCreatedDate datetime NULL
  _rtblIncidents_dModifiedDate datetime NULL
  _rtblIncidents_iCreatedBranchID int NULL
  _rtblIncidents_iModifiedBranchID int NULL
  _rtblIncidents_iCreatedAgentID int NULL
  _rtblIncidents_iModifiedAgentID int NULL
  _rtblIncidents_iChangeSetID int NULL
  _rtblIncidents_Checksum binary(20) NULL
  iPmtRecId int NOT NULL default (0)
  iJrBatchId int NOT NULL default (0)
  ufINCValueSalesLead float NULL
  ulINCLeadStatus nvarchar(100) NULL
  ulINCLeadQuality nvarchar(100) NULL
  ucINCICARnumber nvarchar(30) NULL
  ulINCLeadSource nvarchar(100) NULL
  uiINCCostofComplaint int NULL

## _rtblIncidents_Archive
PK: idIncidents
Columns (58):
  idIncidents int NOT NULL identity PK
  dCreated datetime NOT NULL
  dLastModified datetime NOT NULL
  iClassID int NOT NULL
  iIncidentStatusID int NOT NULL
  bRequireAck bit NOT NULL
  iDebtorID int NOT NULL
  iPersonID int NOT NULL
  iIncidentCatID int NULL
  cOurRef varchar(50) NULL
  cYourRef varchar(50) NULL
  cOutline varchar(1024) NULL
  iPriorityID int NOT NULL
  iEscalateGrpID int NOT NULL
  iAgentGroupID int NOT NULL
  iCurrentAgentID int NOT NULL
  iContractTxID int NOT NULL
  iStockID int NOT NULL
  iPrivNode int NULL
  iIncidentTypeID int NOT NULL
  dDueBy datetime NULL
  iDuration int NULL
  iContractID int NULL
  cChangeLog text NULL
  iIncidentTypeGroupID int NULL
  iWorkflowID int NULL
  iWorkflowStatusID int NULL
  bHasBeenRejected bit NOT NULL
  iSupplierID int NULL
  iFixedAssetID int NULL
  iEmployeeID int NULL
  iProjectID int NULL
  iJobCostingID int NULL
  iProspectID int NOT NULL default (0)
  iOpportunityID int NOT NULL default (0)
  iRequisitionID int NOT NULL default (0)
  bPOViewed bit NULL
  iPOInvoiceID bigint NOT NULL default (0)
  iLinkID int NULL
  iRfqID int NULL
  iSIMReqID int NULL
  _rtblIncidents_Archive_iBranchID int NULL
  _rtblIncidents_Archive_dCreatedDate datetime NULL
  _rtblIncidents_Archive_dModifiedDate datetime NULL
  _rtblIncidents_Archive_iCreatedBranchID int NULL
  _rtblIncidents_Archive_iModifiedBranchID int NULL
  _rtblIncidents_Archive_iCreatedAgentID int NULL
  _rtblIncidents_Archive_iModifiedAgentID int NULL
  _rtblIncidents_Archive_iChangeSetID int NULL
  _rtblIncidents_Archive_Checksum binary(20) NULL
  iPmtRecId int NOT NULL default (0)
  iJrBatchId int NOT NULL default (0)
  ufINCValueSalesLead float NULL
  ulINCLeadStatus nvarchar(100) NULL
  ulINCLeadQuality nvarchar(100) NULL
  ucINCICARnumber nvarchar(30) NULL
  ulINCLeadSource nvarchar(100) NULL
  uiINCCostofComplaint int NULL

## _rtblIncidentStatus - Incident Status (IncidentStatus)
Alias: Incident Status | Freedom Name: IncidentStatus | Record Identifier: 
Notes: Incident Status
PK: idIncidentStatus
Columns (11):
  idIncidentStatus int NOT NULL PK
  cDescription varchar(32) NULL
  _rtblIncidentStatus_iBranchID int NULL
  _rtblIncidentStatus_dCreatedDate datetime NULL
  _rtblIncidentStatus_dModifiedDate datetime NULL
  _rtblIncidentStatus_iCreatedBranchID int NULL
  _rtblIncidentStatus_iModifiedBranchID int NULL
  _rtblIncidentStatus_iCreatedAgentID int NULL
  _rtblIncidentStatus_iModifiedAgentID int NULL
  _rtblIncidentStatus_iChangeSetID int NULL
  _rtblIncidentStatus_Checksum binary(20) NULL

## _rtblIncidentTemplates - Incident Template
Alias: Incident Template | Freedom Name:  | Record Identifier: 
Notes: Incident Template
PK: idIncidentTemplates
Columns (13):
  idIncidentTemplates int NOT NULL identity PK
  cTemplateName varchar(32) NOT NULL
  iIncidentID int NOT NULL
  iAgentID int NOT NULL default (0)
  _rtblIncidentTemplates_iBranchID int NULL
  _rtblIncidentTemplates_dCreatedDate datetime NULL
  _rtblIncidentTemplates_dModifiedDate datetime NULL
  _rtblIncidentTemplates_iCreatedBranchID int NULL
  _rtblIncidentTemplates_iModifiedBranchID int NULL
  _rtblIncidentTemplates_iCreatedAgentID int NULL
  _rtblIncidentTemplates_iModifiedAgentID int NULL
  _rtblIncidentTemplates_iChangeSetID int NULL
  _rtblIncidentTemplates_Checksum binary(20) NULL

## _rtblIncidentType - Incident Type (IncidentType)
Alias: Incident Type | Freedom Name: IncidentType | Record Identifier: cDescription
Notes: Incident types classifies incidents based on their content and on which agents have to deal with the incident. 1. When you create an incident you specify an incident type. 2. The incident type links to an escalation group.
PK: idIncidentType
Columns (20):
  idIncidentType int NOT NULL identity PK
  cDescription varchar(50) NOT NULL
  iEscGroupID int NULL
  bAllowOverride bit NOT NULL default (1)
  bRequireContract bit NOT NULL default (0)
  iIncidentTypeGroupID int NULL
  iWorkflowID int NULL
  bAllowOverrideIncidentType bit NOT NULL default (1)
  bPOIncidentType bit NOT NULL default (0)
  cDefaultOutline varchar(1024) NULL
  bActive bit NOT NULL default (1)
  _rtblIncidentType_iBranchID int NULL
  _rtblIncidentType_dCreatedDate datetime NULL
  _rtblIncidentType_dModifiedDate datetime NULL
  _rtblIncidentType_iCreatedBranchID int NULL
  _rtblIncidentType_iModifiedBranchID int NULL
  _rtblIncidentType_iCreatedAgentID int NULL
  _rtblIncidentType_iModifiedAgentID int NULL
  _rtblIncidentType_iChangeSetID int NULL
  _rtblIncidentType_Checksum binary(20) NULL

## _rtblKBADocLinks - KBA Document Link
Alias: KBA Document Link | Freedom Name:  | Record Identifier: 
Notes: KBA Document Link
PK: idDocLinks
Columns (13):
  idDocLinks int NOT NULL identity PK
  iDocStoreID int NULL
  iLinkSource int NULL default (0)
  iLinkID int NULL
  _rtblKBADocLinks_iBranchID int NULL
  _rtblKBADocLinks_dCreatedDate datetime NULL
  _rtblKBADocLinks_dModifiedDate datetime NULL
  _rtblKBADocLinks_iCreatedBranchID int NULL
  _rtblKBADocLinks_iModifiedBranchID int NULL
  _rtblKBADocLinks_iCreatedAgentID int NULL
  _rtblKBADocLinks_iModifiedAgentID int NULL
  _rtblKBADocLinks_iChangeSetID int NULL
  _rtblKBADocLinks_Checksum binary(20) NULL

## _rtblKBCategoryLinks - KB Category Link
Alias: KB Category Link | Freedom Name:  | Record Identifier: 
Notes: KB Category Link
PK: idCategoryLinks
Columns (13):
  idCategoryLinks int NOT NULL identity PK
  iKnowledgeBaseID int NOT NULL default (0)
  iKnowledgeBaseCatValueID int NOT NULL
  bSelected bit NOT NULL
  _rtblKBCategoryLinks_iBranchID int NULL
  _rtblKBCategoryLinks_dCreatedDate datetime NULL
  _rtblKBCategoryLinks_dModifiedDate datetime NULL
  _rtblKBCategoryLinks_iCreatedBranchID int NULL
  _rtblKBCategoryLinks_iModifiedBranchID int NULL
  _rtblKBCategoryLinks_iCreatedAgentID int NULL
  _rtblKBCategoryLinks_iModifiedAgentID int NULL
  _rtblKBCategoryLinks_iChangeSetID int NULL
  _rtblKBCategoryLinks_Checksum binary(20) NULL

## _rtblKBDescriptionLinks - KB Description Links
Alias: KB Description Links | Freedom Name:  | Record Identifier: 
Notes: KB Description Links
PK: idDescriptionLinks
Columns (13):
  idDescriptionLinks int NOT NULL identity PK
  iKnowledgeBaseID int NOT NULL
  iDescriptionID int NOT NULL
  cDescription text NULL
  _rtblKBDescriptionLinks_iBranchID int NULL
  _rtblKBDescriptionLinks_dCreatedDate datetime NULL
  _rtblKBDescriptionLinks_dModifiedDate datetime NULL
  _rtblKBDescriptionLinks_iCreatedBranchID int NULL
  _rtblKBDescriptionLinks_iModifiedBranchID int NULL
  _rtblKBDescriptionLinks_iCreatedAgentID int NULL
  _rtblKBDescriptionLinks_iModifiedAgentID int NULL
  _rtblKBDescriptionLinks_iChangeSetID int NULL
  _rtblKBDescriptionLinks_Checksum binary(20) NULL

## _rtblKBDescriptionSetup - KB Description Setup
Alias: KB Description Setup | Freedom Name:  | Record Identifier: 
Notes: KB Description Setup
PK: idKBDescriptionSetup
Columns (13):
  idKBDescriptionSetup int NOT NULL identity PK
  idDescription int NOT NULL
  cDescriptionLabel varchar(35) NOT NULL
  bInUse bit NOT NULL default (0)
  _rtblKBDescriptionSetup_iBranchID int NULL
  _rtblKBDescriptionSetup_dCreatedDate datetime NULL
  _rtblKBDescriptionSetup_dModifiedDate datetime NULL
  _rtblKBDescriptionSetup_iCreatedBranchID int NULL
  _rtblKBDescriptionSetup_iModifiedBranchID int NULL
  _rtblKBDescriptionSetup_iCreatedAgentID int NULL
  _rtblKBDescriptionSetup_iModifiedAgentID int NULL
  _rtblKBDescriptionSetup_iChangeSetID int NULL
  _rtblKBDescriptionSetup_Checksum binary(20) NULL

## _rtblKnowledgeBase - Knowledge Base
Alias: Knowledge Base | Freedom Name:  | Record Identifier: 
Notes: Knowledge Base
PK: idKnowledgeBase
Columns (20):
  idKnowledgeBase int NOT NULL identity PK
  cArticleNumber varchar(50) NULL default (0)
  cSummary varchar(1024) NULL
  iStockID int NULL default (0)
  iStatus int NOT NULL default (0)
  bPublic bit NOT NULL default (0)
  dCreatedDate smalldatetime NOT NULL
  iCreatedAgentID int NOT NULL default (0)
  dDateEdited smalldatetime NULL
  iEditedAgentID int NOT NULL default (0)
  bIsActive bit NOT NULL default (1)
  _rtblKnowledgeBase_iBranchID int NULL
  _rtblKnowledgeBase_dCreatedDate datetime NULL
  _rtblKnowledgeBase_dModifiedDate datetime NULL
  _rtblKnowledgeBase_iCreatedBranchID int NULL
  _rtblKnowledgeBase_iModifiedBranchID int NULL
  _rtblKnowledgeBase_iCreatedAgentID int NULL
  _rtblKnowledgeBase_iModifiedAgentID int NULL
  _rtblKnowledgeBase_iChangeSetID int NULL
  _rtblKnowledgeBase_Checksum binary(20) NULL

## _rtblKnowledgeBaseCat - Knowledge Base Category
Alias: Knowledge Base Category | Freedom Name:  | Record Identifier: 
Notes: Knowledge Base Category
PK: idKnowledgeBaseCat
Columns (13):
  idKnowledgeBaseCat int NOT NULL PK
  cName varchar(30) NOT NULL
  cDescription varchar(50) NULL
  bInUse bit NOT NULL default (0)
  _rtblKnowledgeBaseCat_iBranchID int NULL
  _rtblKnowledgeBaseCat_dCreatedDate datetime NULL
  _rtblKnowledgeBaseCat_dModifiedDate datetime NULL
  _rtblKnowledgeBaseCat_iCreatedBranchID int NULL
  _rtblKnowledgeBaseCat_iModifiedBranchID int NULL
  _rtblKnowledgeBaseCat_iCreatedAgentID int NULL
  _rtblKnowledgeBaseCat_iModifiedAgentID int NULL
  _rtblKnowledgeBaseCat_iChangeSetID int NULL
  _rtblKnowledgeBaseCat_Checksum binary(20) NULL

## _rtblKnowledgeBaseCatValue - Knowledge Base Category Value
Alias: Knowledge Base Category Value | Freedom Name:  | Record Identifier: 
Notes: Knowledge Base Category Value
PK: idKnowledgeBaseCatValue
Columns (12):
  idKnowledgeBaseCatValue int NOT NULL identity PK
  cDescription varchar(50) NOT NULL
  iKnowledgeBaseCatID int NULL
  _rtblKnowledgeBaseCatValue_iBranchID int NULL
  _rtblKnowledgeBaseCatValue_dCreatedDate datetime NULL
  _rtblKnowledgeBaseCatValue_dModifiedDate datetime NULL
  _rtblKnowledgeBaseCatValue_iCreatedBranchID int NULL
  _rtblKnowledgeBaseCatValue_iModifiedBranchID int NULL
  _rtblKnowledgeBaseCatValue_iCreatedAgentID int NULL
  _rtblKnowledgeBaseCatValue_iModifiedAgentID int NULL
  _rtblKnowledgeBaseCatValue_iChangeSetID int NULL
  _rtblKnowledgeBaseCatValue_Checksum binary(20) NULL

## _rtblKnowledgeBaseLinks - Knowledge Base Link
Alias: Knowledge Base Link | Freedom Name:  | Record Identifier: 
Notes: Knowledge Base Link
PK: idKnowledgeBaseLinks
Columns (12):
  idKnowledgeBaseLinks int NOT NULL identity PK
  iKnowledgeBaseID int NOT NULL
  iIncidentID int NOT NULL
  _rtblKnowledgeBaseLinks_iBranchID int NULL
  _rtblKnowledgeBaseLinks_dCreatedDate datetime NULL
  _rtblKnowledgeBaseLinks_dModifiedDate datetime NULL
  _rtblKnowledgeBaseLinks_iCreatedBranchID int NULL
  _rtblKnowledgeBaseLinks_iModifiedBranchID int NULL
  _rtblKnowledgeBaseLinks_iCreatedAgentID int NULL
  _rtblKnowledgeBaseLinks_iModifiedAgentID int NULL
  _rtblKnowledgeBaseLinks_iChangeSetID int NULL
  _rtblKnowledgeBaseLinks_Checksum binary(20) NULL

## _rtblNotify
PK: idNotify
Columns (16):
  idNotify int NOT NULL identity PK
  dNotifyDate datetime NULL
  iForAgentID int NOT NULL
  iIncidentID int NULL
  iIncidentLogID int NULL
  bRead bit NOT NULL default (0)
  iWhseIBTID int NULL
  _rtblNotify_iBranchID int NULL
  _rtblNotify_dCreatedDate datetime NULL
  _rtblNotify_dModifiedDate datetime NULL
  _rtblNotify_iCreatedBranchID int NULL
  _rtblNotify_iModifiedBranchID int NULL
  _rtblNotify_iCreatedAgentID int NULL
  _rtblNotify_iModifiedAgentID int NULL
  _rtblNotify_iChangeSetID int NULL
  _rtblNotify_Checksum binary(20) NULL

## _rtblOpportunity - Sales Opportunity (SalesOpportunity)
Alias: Sales Opportunity | Freedom Name: SalesOpportunity | Record Identifier: cOpportunityNumber
Notes: Sales Opportunity
PK: IDOpportunity
Columns (32):
  IDOpportunity int NOT NULL identity PK
  cOpportunityNumber varchar(50) NULL
  iClientID int NOT NULL default (0)
  iProspectID int NOT NULL default (0)
  iPeopleID int NOT NULL default (0)
  iAgentID int NOT NULL default (0)
  iOpportunityStageID int NOT NULL default (0)
  iOpportunityStatusID int NOT NULL default (0)
  iOpportunitySourceID int NOT NULL default (0)
  iOppSourceClientID int NOT NULL default (0)
  iOppSourceSupplierID int NOT NULL default (0)
  iOppSourceAgentID int NOT NULL default (0)
  dDateStart datetime NULL
  dDateClose datetime NULL
  dDateActualClose datetime NULL
  fClosedAmount float NULL
  fProbabilityPerc float NULL
  bPublic bit NOT NULL default (0)
  iActiveInvNumID bigint NOT NULL default (0)
  fForecastAmount float NULL
  fBudgetedAmount float NULL
  cOpportunityDescription varchar(100) NULL
  iProjectID int NOT NULL default (0)
  _rtblOpportunity_iBranchID int NULL
  _rtblOpportunity_dCreatedDate datetime NULL
  _rtblOpportunity_dModifiedDate datetime NULL
  _rtblOpportunity_iCreatedBranchID int NULL
  _rtblOpportunity_iModifiedBranchID int NULL
  _rtblOpportunity_iCreatedAgentID int NULL
  _rtblOpportunity_iModifiedAgentID int NULL
  _rtblOpportunity_iChangeSetID int NULL
  _rtblOpportunity_Checksum binary(20) NULL

## _rtblOpportunityCompetitor - Sales Opportunity Competitor (CompetitorLinktoOpportunity)
Alias: Sales Opportunity Competitor | Freedom Name: CompetitorLinktoOpportunity | Record Identifier: 
Notes: Sales Opportunity Competitor
PK: idOpportunityCompetitor
Columns (15):
  idOpportunityCompetitor int NOT NULL identity PK
  iOpportunityID int NOT NULL
  iCompetitorID int NOT NULL
  iCompetitorProductID int NOT NULL default (0)
  fPrice float NULL
  bWonDeal bit NOT NULL default (0)
  _rtblOpportunityCompetitor_iBranchID int NULL
  _rtblOpportunityCompetitor_dCreatedDate datetime NULL
  _rtblOpportunityCompetitor_dModifiedDate datetime NULL
  _rtblOpportunityCompetitor_iCreatedBranchID int NULL
  _rtblOpportunityCompetitor_iModifiedBranchID int NULL
  _rtblOpportunityCompetitor_iCreatedAgentID int NULL
  _rtblOpportunityCompetitor_iModifiedAgentID int NULL
  _rtblOpportunityCompetitor_iChangeSetID int NULL
  _rtblOpportunityCompetitor_Checksum binary(20) NULL

## _rtblOpportunityDocLinks - Sales Opportunity Document Link (OpportunityDocumentLinks)
Alias: Sales Opportunity Document Link | Freedom Name: OpportunityDocumentLinks | Record Identifier: 
Notes: Sales Opportunity Document Link
PK: IDDocLinks
Columns (13):
  IDDocLinks int NOT NULL identity PK
  iDocStoreID int NULL
  iLinkSource int NULL
  iLinkID int NULL
  _rtblOpportunityDocLinks_iBranchID int NULL
  _rtblOpportunityDocLinks_dCreatedDate datetime NULL
  _rtblOpportunityDocLinks_dModifiedDate datetime NULL
  _rtblOpportunityDocLinks_iCreatedBranchID int NULL
  _rtblOpportunityDocLinks_iModifiedBranchID int NULL
  _rtblOpportunityDocLinks_iCreatedAgentID int NULL
  _rtblOpportunityDocLinks_iModifiedAgentID int NULL
  _rtblOpportunityDocLinks_iChangeSetID int NULL
  _rtblOpportunityDocLinks_Checksum binary(20) NULL

## _rtblOpportunitySource - Sales Opportunity Source
Alias: Sales Opportunity Source | Freedom Name:  | Record Identifier: 
Notes: Sales Opportunity Source
PK: IDOpportunitySource
Columns (11):
  IDOpportunitySource int NOT NULL identity PK
  cSourceDesc varchar(50) NULL
  _rtblOpportunitySource_iBranchID int NULL
  _rtblOpportunitySource_dCreatedDate datetime NULL
  _rtblOpportunitySource_dModifiedDate datetime NULL
  _rtblOpportunitySource_iCreatedBranchID int NULL
  _rtblOpportunitySource_iModifiedBranchID int NULL
  _rtblOpportunitySource_iCreatedAgentID int NULL
  _rtblOpportunitySource_iModifiedAgentID int NULL
  _rtblOpportunitySource_iChangeSetID int NULL
  _rtblOpportunitySource_Checksum binary(20) NULL

## _rtblOpportunityStage - Sales Opportunity Stage (OpportuntiyStage)
Alias: Sales Opportunity Stage | Freedom Name: OpportuntiyStage | Record Identifier: 
Notes: Sales Opportunity Stage
PK: IDOpportunityStage
Columns (15):
  IDOpportunityStage int NOT NULL identity PK
  cStageName varchar(50) NULL
  cStageDescription varchar(100) NULL
  iOpportunityStatusID int NULL
  iStageSequence int NULL
  fDefProbabilityPerc float NULL
  _rtblOpportunityStage_iBranchID int NULL
  _rtblOpportunityStage_dCreatedDate datetime NULL
  _rtblOpportunityStage_dModifiedDate datetime NULL
  _rtblOpportunityStage_iCreatedBranchID int NULL
  _rtblOpportunityStage_iModifiedBranchID int NULL
  _rtblOpportunityStage_iCreatedAgentID int NULL
  _rtblOpportunityStage_iModifiedAgentID int NULL
  _rtblOpportunityStage_iChangeSetID int NULL
  _rtblOpportunityStage_Checksum binary(20) NULL

## _rtblOpportunityStatus - Sales Opportunity Status (OpportuntiyStatus)
Alias: Sales Opportunity Status | Freedom Name: OpportuntiyStatus | Record Identifier: 
Notes: Sales Opportunity Status
PK: IDOpportunityStatus
Columns (12):
  IDOpportunityStatus int NOT NULL identity PK
  cStatusName varchar(50) NULL
  bFinal bit NOT NULL default (0)
  _rtblOpportunityStatus_iBranchID int NULL
  _rtblOpportunityStatus_dCreatedDate datetime NULL
  _rtblOpportunityStatus_dModifiedDate datetime NULL
  _rtblOpportunityStatus_iCreatedBranchID int NULL
  _rtblOpportunityStatus_iModifiedBranchID int NULL
  _rtblOpportunityStatus_iCreatedAgentID int NULL
  _rtblOpportunityStatus_iModifiedAgentID int NULL
  _rtblOpportunityStatus_iChangeSetID int NULL
  _rtblOpportunityStatus_Checksum binary(20) NULL

## _rtblPeople - People (People)
Alias: People | Freedom Name: People | Record Identifier: 
Notes: People
PK: idPeople
Columns (32):
  idPeople int NOT NULL identity PK
  cFirstName varchar(20) NULL
  cInitials varchar(5) NULL
  cLastName varchar(30) NULL
  cDisplayName varchar(60) NULL
  cTitle varchar(6) NULL
  cDescription varchar(50) NULL
  cTelWork varchar(20) NULL
  cTelFax varchar(20) NULL
  cTelMobile varchar(20) NULL
  cTelHome varchar(20) NULL
  cEmail varchar(60) NULL
  cWebPage varchar(50) NULL
  cComments varchar(1024) NULL
  cAddress varchar(240) NULL
  cPostalAddress varchar(240) NULL
  iBusDeptID int NULL
  iBusDesigID int NULL
  dBirthDate smalldatetime NULL
  dPeopleTimeStamp datetime NULL
  _rtblPeople_iBranchID int NULL
  _rtblPeople_dCreatedDate datetime NULL
  _rtblPeople_dModifiedDate datetime NULL
  _rtblPeople_iCreatedBranchID int NULL
  _rtblPeople_iModifiedBranchID int NULL
  _rtblPeople_iCreatedAgentID int NULL
  _rtblPeople_iModifiedAgentID int NULL
  _rtblPeople_iChangeSetID int NULL
  _rtblPeople_Checksum binary(20) NULL
  bObjectToProcess bit NOT NULL default (0)
  bStatEmail bit NOT NULL default (0)
  bSourceDocEmail bit NOT NULL default (0)

## _rtblPeopleLinks - People Link (PeopleLinks)
Alias: People Link | Freedom Name: PeopleLinks | Record Identifier: 
Notes: People Link
PK: idPeopleLinks
Columns (13):
  idPeopleLinks int NOT NULL identity PK
  iPeopleID int NULL
  iDebtorID int NULL
  cModule varchar(2) NULL
  _rtblPeopleLinks_iBranchID int NULL
  _rtblPeopleLinks_dCreatedDate datetime NULL
  _rtblPeopleLinks_dModifiedDate datetime NULL
  _rtblPeopleLinks_iCreatedBranchID int NULL
  _rtblPeopleLinks_iModifiedBranchID int NULL
  _rtblPeopleLinks_iCreatedAgentID int NULL
  _rtblPeopleLinks_iModifiedAgentID int NULL
  _rtblPeopleLinks_iChangeSetID int NULL
  _rtblPeopleLinks_Checksum binary(20) NULL

## _rtblProspect - Prospective Customer (ProspectiveCustomer)
Alias: Prospective Customer | Freedom Name: ProspectiveCustomer | Record Identifier: cCompanyName
Notes: Prospective Customer
PK: IDProspect
Columns (31):
  IDProspect int NOT NULL identity PK
  cCompanyName varchar(50) NULL
  cTelephone varchar(25) NULL
  cFax varchar(25) NULL
  cPhysicalAddress1 varchar(40) NULL
  cPhysicalAddress2 varchar(40) NULL
  cPhysicalAddress3 varchar(40) NULL
  cPhysicalAddress4 varchar(40) NULL
  cPhysicalAddress5 varchar(40) NULL
  cPhysicalAddressPC varchar(15) NULL
  cPostalAddress1 varchar(40) NULL
  cPostalAddress2 varchar(40) NULL
  cPostalAddress3 varchar(40) NULL
  cPostalAddress4 varchar(40) NULL
  cPostalAddress5 varchar(40) NULL
  cPostalAddressPC varchar(15) NULL
  cWebsite varchar(60) NULL
  cEmail varchar(60) NULL
  bChargeTax bit NOT NULL default (1)
  iAgentID int NOT NULL default (0)
  bPublic bit NOT NULL default (0)
  iRepID int NOT NULL default (0)
  _rtblProspect_iBranchID int NULL
  _rtblProspect_dCreatedDate datetime NULL
  _rtblProspect_dModifiedDate datetime NULL
  _rtblProspect_iCreatedBranchID int NULL
  _rtblProspect_iModifiedBranchID int NULL
  _rtblProspect_iCreatedAgentID int NULL
  _rtblProspect_iModifiedAgentID int NULL
  _rtblProspect_iChangeSetID int NULL
  _rtblProspect_Checksum binary(20) NULL

## _rtblRefBase
PK: idRefBase
Columns (12):
  idRefBase int NOT NULL identity PK
  cRefType varchar(30) NULL
  iNextNo int NULL default (100000)
  _rtblRefBase_iBranchID int NULL
  _rtblRefBase_dCreatedDate datetime NULL
  _rtblRefBase_dModifiedDate datetime NULL
  _rtblRefBase_iCreatedBranchID int NULL
  _rtblRefBase_iModifiedBranchID int NULL
  _rtblRefBase_iCreatedAgentID int NULL
  _rtblRefBase_iModifiedAgentID int NULL
  _rtblRefBase_iChangeSetID int NULL
  _rtblRefBase_Checksum binary(20) NULL

## _rtblRefBook - Reference Book
Alias: Reference Book | Freedom Name:  | Record Identifier: 
Notes: Reference Book
PK: idRefBook
Columns (13):
  idRefBook int NOT NULL identity PK
  iRefBaseID int NULL
  iBookedNo int NULL
  bAvailable bit NOT NULL default (0)
  _rtblRefBook_iBranchID int NULL
  _rtblRefBook_dCreatedDate datetime NULL
  _rtblRefBook_dModifiedDate datetime NULL
  _rtblRefBook_iCreatedBranchID int NULL
  _rtblRefBook_iModifiedBranchID int NULL
  _rtblRefBook_iCreatedAgentID int NULL
  _rtblRefBook_iModifiedAgentID int NULL
  _rtblRefBook_iChangeSetID int NULL
  _rtblRefBook_Checksum binary(20) NULL

## _rtblStockLinks - Inventory Link (StockLink)
Alias: Inventory Link | Freedom Name: StockLink | Record Identifier: 
Notes: Inventory Link
PK: idStockLinks
Columns (26):
  idStockLinks int NOT NULL identity PK
  iStockID int NOT NULL
  iDCLink int NOT NULL
  bItemActive bit NOT NULL default (1)
  cProductReference varchar(30) NULL
  cModule varchar(2) NOT NULL
  cSupInvCode varchar(20) NULL
  iWhseID int NULL
  bDefaultSupplier bit NOT NULL default (0)
  bDCOnHold bit NOT NULL default (0)
  dTimeStamp datetime NULL
  fLastGRVCost float NOT NULL default (0)
  dLastGRVCostDate datetime NULL
  fManualCost float NOT NULL default (0)
  _rtblStockLinks_fLeadDays float NULL
  fMinOrderQuantity float NULL
  _rtblStockLinks_iBranchID int NULL
  _rtblStockLinks_dCreatedDate datetime NULL
  _rtblStockLinks_dModifiedDate datetime NULL
  _rtblStockLinks_iCreatedBranchID int NULL
  _rtblStockLinks_iModifiedBranchID int NULL
  _rtblStockLinks_iCreatedAgentID int NULL
  _rtblStockLinks_iModifiedAgentID int NULL
  _rtblStockLinks_iChangeSetID int NULL
  _rtblStockLinks_Checksum binary(20) NULL
  iTaxTypeID int NULL default (0)

## _rtblUserDict - User Dictionary (UserDefinedFieldsCollection)
Alias: User Dictionary | Freedom Name: UserDefinedFieldsCollection | Record Identifier: 
Notes: This table contains a list of all user defined fields created in the database. Values: Contracts : _rtblContracts; Customers : CLIENT; Employees : EmplMain; Fixed Assets : _btblFAAssets; General Ledger : Accounts; Incidents : _rtblIncidents; Inventory Document : InvNum; Inventory items : STKITEM; Job Cards : _btblJCMaster; People : _rtblPeople; Suppliers : VENDOR
PK: idUserDict
Columns (24):
  idUserDict int NOT NULL identity PK
  cFieldName varchar(50) NOT NULL
  cFieldDescription varchar(50) NOT NULL
  iFieldType int NOT NULL
  iFieldSize int NULL
  iFieldIndex int NOT NULL
  cTableName varchar(50) NOT NULL
  cLookupOptions varchar(max) NULL
  bForceValue bit NOT NULL default (0)
  cDefaultValue varchar(250) NULL
  iPageIndex int NULL
  cPageName varchar(50) NULL
  iFieldDecimals int NULL
  iModuleOptions int NULL
  _rtblUserDict_iBranchID int NULL
  _rtblUserDict_dCreatedDate datetime NULL
  _rtblUserDict_dModifiedDate datetime NULL
  _rtblUserDict_iCreatedBranchID int NULL
  _rtblUserDict_iModifiedBranchID int NULL
  _rtblUserDict_iCreatedAgentID int NULL
  _rtblUserDict_iModifiedAgentID int NULL
  _rtblUserDict_iChangeSetID int NULL
  _rtblUserDict_Checksum binary(20) NULL
  bIsUserHist bit NOT NULL default (0)

## _rtblWorkCal - Working Calendar
Alias: Working Calendar | Freedom Name:  | Record Identifier: 
Notes: Working Calendar
PK: idWorkCal
Columns (20):
  idWorkCal int NOT NULL identity PK
  iStartTime int NOT NULL
  iEndTime int NOT NULL
  cDescription varchar(20) NULL
  bSunday bit NOT NULL default (0)
  bMonday bit NOT NULL default (0)
  bTuesday bit NOT NULL default (0)
  bWednesday bit NOT NULL default (0)
  bThursday bit NOT NULL default (0)
  bFriday bit NOT NULL default (0)
  bSaturday bit NOT NULL default (0)
  _rtblWorkCal_iBranchID int NULL
  _rtblWorkCal_dCreatedDate datetime NULL
  _rtblWorkCal_dModifiedDate datetime NULL
  _rtblWorkCal_iCreatedBranchID int NULL
  _rtblWorkCal_iModifiedBranchID int NULL
  _rtblWorkCal_iCreatedAgentID int NULL
  _rtblWorkCal_iModifiedAgentID int NULL
  _rtblWorkCal_iChangeSetID int NULL
  _rtblWorkCal_Checksum binary(20) NULL

## _rtblWorkCalExDates - Working Calendar Exlcude Date
Alias: Working Calendar Exlcude Date | Freedom Name:  | Record Identifier: 
Notes: Working Calendar Exlcude Date
PK: idWorkCalExDates
Columns (12):
  idWorkCalExDates int NOT NULL identity PK
  dExDate smalldatetime NOT NULL
  bRepeat bit NOT NULL default (0)
  _rtblWorkCalExDates_iBranchID int NULL
  _rtblWorkCalExDates_dCreatedDate datetime NULL
  _rtblWorkCalExDates_dModifiedDate datetime NULL
  _rtblWorkCalExDates_iCreatedBranchID int NULL
  _rtblWorkCalExDates_iModifiedBranchID int NULL
  _rtblWorkCalExDates_iCreatedAgentID int NULL
  _rtblWorkCalExDates_iModifiedAgentID int NULL
  _rtblWorkCalExDates_iChangeSetID int NULL
  _rtblWorkCalExDates_Checksum binary(20) NULL
