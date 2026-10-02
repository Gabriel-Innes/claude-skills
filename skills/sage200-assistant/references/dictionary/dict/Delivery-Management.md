# Sage 200 Evolution table dictionary - Delivery Management

One entry per table: `## TABLE - alias (FreedomName)`; `Alias | Freedom Name | Record Identifier` and `Notes` as Evolution's Database Object browser shows them (Freedom Name = the SDK class the table backs); `PK` (plus UNIQUE / FK when declared - Evolution declares almost none, joins follow naming, see ../conventions.md); then one column per line: `Name type(size) NULL|NOT NULL [identity] [PK] [default X] - description`. Add a column description after ` - `; leave it off until one is known.

## _dReportLayout - Report Layout
Alias: Report Layout | Freedom Name:  | Record Identifier: 
Notes: Delivery Management. Report Layout
PK: idReportLayout
Columns (15):
  idReportLayout int NOT NULL identity PK
  cRptDescription nvarchar(80) NOT NULL
  iVersion int NULL
  nLayout varbinary(max) NOT NULL
  bReadOnly bit NOT NULL
  bIsDefaultLayout bit NULL
  _dReportLayout_iBranchID int NULL
  _dReportLayout_dCreatedDate datetime NULL
  _dReportLayout_dModifiedDate datetime NULL
  _dReportLayout_iCreatedBranchID int NULL
  _dReportLayout_iModifiedBranchID int NULL
  _dReportLayout_iCreatedAgentID int NULL
  _dReportLayout_iModifiedAgentID int NULL
  _dReportLayout_iChangeSetID int NULL
  _dReportLayout_Checksum binary(20) NULL

## _dtblDefaults - Defaults
Alias: Defaults | Freedom Name:  | Record Identifier: 
Notes: Delivery Management. Default Setting
PK: IdDefaults
Columns (15):
  IdDefaults int NOT NULL identity PK
  iNextAutoNum int NOT NULL
  iPadTo int NOT NULL
  cPrefix nvarchar(25) NULL
  bAutoNum bit NOT NULL default (1)
  bUniqueNum bit NOT NULL default (0)
  _dtblDefaults_iBranchID int NULL
  _dtblDefaults_dCreatedDate datetime NULL
  _dtblDefaults_dModifiedDate datetime NULL
  _dtblDefaults_iCreatedBranchID int NULL
  _dtblDefaults_iModifiedBranchID int NULL
  _dtblDefaults_iCreatedAgentID int NULL
  _dtblDefaults_iModifiedAgentID int NULL
  _dtblDefaults_iChangeSetID int NULL
  _dtblDefaults_Checksum binary(20) NULL

## _dtblDeliveryMethod - Delivery Method
Alias: Delivery Method | Freedom Name:  | Record Identifier: 
Notes: Delivery Management. Delivery Methods
PK: IdDeliveryMethod
Columns (6):
  IdDeliveryMethod int NOT NULL identity PK
  iDelMethodID int NULL
  cMethod nvarchar(35) NULL
  cComment nvarchar(80) NULL
  bSelect bit NULL
  dEffectiveDate datetime NULL

## _dtblDeliveryNote
PK: IdDeliveryNote
Columns (32):
  IdDeliveryNote int NOT NULL identity PK
  iAccountID bigint NULL
  iInvoiceID bigint NULL
  iInventoryID bigint NULL
  ibtblInvoiceLineID bigint NULL
  iWarehouseID bigint NULL
  cInvoiceNumber nvarchar(50) NULL
  cDelNoteNum nvarchar(50) NULL
  fTotalQty float NULL
  fQtyDelivered float NULL
  fConfirmDeliveryQty float NULL
  dDeliveryDate datetime NULL
  iStatus int NULL
  bIsPrinted bit NULL
  cOrderNum nvarchar(50) NULL
  bPerInvoice bit NULL
  bIsLotItem bit NULL
  iLotID int NULL
  cLotNumber nvarchar(50) NULL
  bIsSerialItem bit NULL
  iAttributeGroupID int NULL
  xAttribute xml NULL
  _dtblDeliveryNote_iBranchID int NULL
  _dtblDeliveryNote_dCreatedDate datetime NULL
  _dtblDeliveryNote_dModifiedDate datetime NULL
  _dtblDeliveryNote_iCreatedBranchID int NULL
  _dtblDeliveryNote_iModifiedBranchID int NULL
  _dtblDeliveryNote_iCreatedAgentID int NULL
  _dtblDeliveryNote_iModifiedAgentID int NULL
  _dtblDeliveryNote_iChangeSetID int NULL
  _dtblDeliveryNote_Checksum binary(20) NULL
  iStockBinLocationID int NOT NULL default (0)

## _dtblDeliverySerials - Delivery Serials
Alias: Delivery Serials | Freedom Name:  | Record Identifier: 
Notes: Delivery Management
PK: IdDeliverySerials
Columns (16):
  IdDeliverySerials int NOT NULL identity PK
  iInvoiceID int NULL
  iInvoiceLineID bigint NULL
  iInvoiceLineSN int NULL
  iDeliveryNoteID int NULL
  iStatus int NULL
  cSerialNumber nvarchar(50) NULL
  _dtblDeliverySerials_iBranchID int NULL
  _dtblDeliverySerials_dCreatedDate datetime NULL
  _dtblDeliverySerials_dModifiedDate datetime NULL
  _dtblDeliverySerials_iCreatedBranchID int NULL
  _dtblDeliverySerials_iModifiedBranchID int NULL
  _dtblDeliverySerials_iCreatedAgentID int NULL
  _dtblDeliverySerials_iModifiedAgentID int NULL
  _dtblDeliverySerials_iChangeSetID int NULL
  _dtblDeliverySerials_Checksum binary(20) NULL
