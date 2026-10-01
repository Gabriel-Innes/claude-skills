<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->

# AAAR - Substitute Authorizer
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  AuthrID Int(11) Authorizer ID ->OUSR
  SubsttID Int(11) Substitute Authorizer ID ->OUSR
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  WtmCode Int(11) Approval Template Code ->OWTM
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  CreateDate Date(8) Date Created
  CreateTS Int(11) Creatn Time - Incl. Secs
  UserSign Int(11) User Signature ->OUSR
  UserSign2 Int(6) User Signature 2
  Applied VarChar(1) Substitute Action Performed default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Update Date

# ACPA1 - Periods Category - WIP Mapping - Log
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OACP
  LineNum Int(11) Line Number
  LogInstanc Int(11) Log Instance
  AcctFrom nVarChar(15) Consolidate from Account ->OACT
  AcctTo nVarChar(15) Consolidate to Account ->OACT

# ADRC - G/L Account Determination Criteria - Resources - History
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DmcId, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DmcId Int(11) Determination ID
  DmcAlias nVarChar(100) Determination Alias
  Active VarChar(1) Determination Status default=N [Y=Yes, N=No]
  Priority Int(6) Determination Priority
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  AdvRulCol Int(6) Advanced Rules Column

# AEBK - E-Books - History
Module: General | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  MARK U: MARK, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) E-Books Abs. Entry
  MARK nVarChar(40) MARK
  CancelMARK nVarChar(40) Cancel MARK
  UID nVarChar(50) UID
  IssueVATID nVarChar(64) Issuer VAT Number
  CPVATID nVarChar(64) Counterpart VAT Number
  Series nVarChar(16) Series
  AA nVarChar(200) AA
  IssueDate Date(8) Issue Date
  InvoiceTyp nVarChar(100) Invoice Type
  Currency nVarChar(200) Currency
  TlNetVal Num(19,6) Total Net Value
  TlVatAmn Num(19,6) Total VAT Amount
  TlWheldAmn Num(19,6) Total Withheld Amount
  TlGrossVal Num(19,6) Total Gross Value
  LinkDocTyp Int(11) Linked Doc. Type [18=A/P Invoices, 19=A/P Credit Memos, 30=Journal Entries, 0=, -1=]
  LinkDocEnt Int(11) Linked Doc. Entry
  IsNegMark VarChar(1) Is Negative MARK default=N [N=No, Y=Yes]
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  SourceECM8 Int(11) LogNum of Source ECM8
  ObjType nVarChar(20) Object Type default=234003013 [234003013=E-Books Expense] ->ADP1
  UserSign2 Int(6) Updating User ->OUSR

# AEK1 - E-Books (Rows) - History
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) E-Books Abs. Entry ->AEBK
  LineNum Int(11) Line Number
  NetValue Num(19,6) Net Value
  VatCatgory Int(11) VAT Category
  VatAmount Num(19,6) VAT Amount
  WithheldAm Num(19,6) Withheld Amount
  WhPrctCat Int(11) Withheld Percent Category
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  LogInstanc Int(11) Log Instance default=0

# AGRS - G/L Account Advanced Rules for Resources - History
Module: General | 55 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PeriodCat nVarChar(10) Period Category
  FinancYear Date(8) Beginning of Financial Year
  Year Int(6) Financial Year
  PeriodName nVarChar(20) Period Name
  SubType VarChar(1) Sub-Period Type default=Y [Y=Year, Q=Quarters, M=Months, D=Days]
  PeriodNum Int(11) Number of Periods
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  ResCode nVarChar(50) Resource No. ->ORSC
  ResGrpCod Int(6) Resource Group ->ORSB
  WhsCode nVarChar(8) Warehouse Code
  BPGrpCod Int(6) BP Group
  LicTradNum nVarChar(32) Federal Tax ID default=!^| [!^|=All, !^|E=Empty, !^|F=Filled, Enter Tax ID=Enter Tax ID]
  ShipCountr nVarChar(3) Ship-to Country/Region
  ShipState nVarChar(3) Ship-To State
  Comments nVarChar(254) Remarks
  CreateDate Date(8) Creation Date
  RuleCode nVarChar(20) Advanced Rule Code
  GLMethod VarChar(1) Get G/L Account By default=A [A=General, W=Warehouse, C=Item Group]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  ResRevAct nVarChar(15) Resource Revenue Account ->OACT
  ResExpAct nVarChar(15) Resource Expense Account ->OACT
  ResSaleAct nVarChar(15) Resource Sales Credit Account ->OACT
  ResPurAct nVarChar(15) Resource Purchase Credit Acct ->OACT
  ResNInvAct nVarChar(15) Resource Received Not Inv. ->OACT
  ResStdExp1 nVarChar(15) Resource Std. Cost Expense 1 ->OACT
  ResStdExp2 nVarChar(15) Resource Std. Cost Expense 2 ->OACT
  ResStdExp3 nVarChar(15) Resource Std. Cost Expense 3 ->OACT
  ResStdExp4 nVarChar(15) Resource Std. Cost Expense 4 ->OACT
  ResStdExp5 nVarChar(15) Resource Std. Cost Expense 5 ->OACT
  ResStdExp6 nVarChar(15) Resource Std. Cost Expense 6 ->OACT
  ResStdExp7 nVarChar(15) Resource Std. Cost Expense 7 ->OACT
  ResStdExp8 nVarChar(15) Resource Std. Cost Expense 8 ->OACT
  ResStdExp9 nVarChar(15) Resource Std. Cost Expense 9 ->OACT
  ResStdEx10 nVarChar(15) Resource Std. Cost Expense 10 ->OACT
  ResWipAct nVarChar(15) Resource WIP Account ->OACT
  ResScrapAc nVarChar(15) Scrap Account ->OACT
  WipOffPlAc nVarChar(15) WIP Offset P&L Account ->OACT
  ResOffPlAc nVarChar(15) Resource Offset P&L Account ->OACT
  Active VarChar(1) Is Rule Active default=Y [Y=Yes, N=No]
  CmpPrivate VarChar(1) Company/Private default=A [A=All, C=Company, I=Private]
  VatGroup nVarChar(8) Tax Definition ->OVTG
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  Usage Int(11) Usage Code for Document ->OUSG

# AHF1 - Hide Functions Configuration - Rows History
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FuncID Int(11) Function ID ->OHFC
  formNum nVarChar(128) Form Number
  ItemUID nVarChar(128) Item UID
  ColUID nVarChar(128) Column UID
  HideVal nVarChar(20) Hide Valid Value
  AltVal nVarChar(20) Alternative Valid Value
  PanelID Int(6) Hide Item by Panel
  ActionType Int(6) Hide Item Action Type default=0 [0=Hide Item, 1=Hide Column, 2=Hide Item's Valid Value, 3=Hide Panel, 4=Hide Column's Valid Value]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# AHF2 - Hide Function Configuration - Rows History
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FuncID Int(11) Function ID ->OHFC
  MainMenu Int(11) Main Menu ID
  MovMenuTo Int(11) Target Postion Menu Move
  ActionType Int(6) Action Type default=0 [0=Hide Menu, 1=Move Menu, 2=Hide Pop-Up Menu]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# AHFC - Hide Functions Configuration - History
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FuncName nVarChar(100) Function Name
  Hidden VarChar(1) Enabled [Y/N] default=Y [Y=Yes, N=No]
  Type nVarChar(6) Type default=0 [0=System, 1=User]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# AIRI - Input Service Distribution - Recipient Invoice
Module: General | 30 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
  INDEX U: DocNum, PIndicator, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  RefNo nVarChar(100) Reference No.
  RefEntry Int(11) Reference Entry
  RefDocDate Date(8) Reference Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(254) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# AIRR - Input Service Distribution - Recipient Credit Memo
Module: General | 30 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
  INDEX U: DocNum, PIndicator, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  RefNo nVarChar(100) Reference No.
  RefEntry Int(11) Reference Entry
  RefDocDate Date(8) Reference Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(254) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# AISC - Input Service Distribution - Credit Memo
Module: General | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
  INDEX U: DocNum, PIndicator, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  Revised VarChar(1) Revised default=N [Y=Yes, N=No]
  OrgRefNo nVarChar(100) Original Reference No.
  OrgRefEty Int(11) Original Reference Entry
  OrgDocDate Date(8) Original Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code default=0
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  ISDEntry Int(11) ISD Entry
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(254) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# AISD - Input Service Distribution
Module: General | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
  INDEX U: DocNum, PIndicator, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  SrcLctCode Int(11) Source Location Code
  SrcLctName nVarChar(100) Source Location Name
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  Revised VarChar(1) Revised default=N [Y=Yes, N=No]
  OrgRefNo nVarChar(100) Original Reference No.
  OrgRefEty Int(11) Original Reference Entry
  OrgDocDate Date(8) Original Document Date
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  DstPercent Num(19,6) Percent to Distribute
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# AISI - Input Service Distribution - Invoice
Module: General | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
  INDEX U: DocNum, PIndicator, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  Revised VarChar(1) Revised default=N [Y=Yes, N=No]
  OrgRefNo nVarChar(100) Original Reference No.
  OrgRefEty Int(11) Original Reference Entry
  OrgDocDate Date(8) Original Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code default=0
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  ISDEntry Int(11) ISD Entry
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(254) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# ALT2 - Alerts - Groups
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, GroupId
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  GroupId Int(6) Group Id ->OUGR
  SendIntrnl VarChar(1) Send Internally default=N [Y=Yes, N=No]
  SendEMail VarChar(1) Send E-Mail default=N [Y=Yes, N=No]
  SendSMS VarChar(1) Send SMS default=N [Y=Yes, N=No]
  SendFax VarChar(1) Send Fax default=N [Y=Yes, N=No]

# AMR3 - Inventory Revaluation SNB
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BaseLine, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  BaseLine Int(11) Base Row Number
  LineNum Int(11) Row Number
  SNBNum nVarChar(36) Serial and Batch Number
  AdmisDate Date(8) Admission Date
  ExpiryDate Date(8) Expiration Date
  CurrCost Num(19,6) Current Cost
  NewCost Num(19,6) New Cost
  DebCred Num(19,6) Debit Credit Value
  SNBOpenQty Num(19,6) SNB Open Quantity
  RToStock Num(19,6) Reval. Amount Posted to Stock
  SnbSysNum Int(11) SNB System Number
  SnbAbsEnt Int(11) SNB Abs. Entry
  SnbQty Num(19,6) SNB Quantity
  SnbCostT Num(19,6) SNB Cost Total
  SnbLotNum nVarChar(36) SNB Lot Number
  SnbMfn nVarChar(36) SNB Manufacture Attribute

# APH1 - Project Management - Stages - History
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OPHA
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMC2
  POS Int(11) Position
  START Date(8) Start Date
  CLOSE Date(8) Closing Date
  FINISHDATE Date(8) Finished Date
  Task Int(11) Task Type
  DSCRIPTION Text(16) Description
  EXPCOSTS Num(19,6) Planned Cost
  InvAmtAR Num(19,6) Invoiced Amount (A/R)
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvAmtAP Num(19,6) Invoiced Amount (A/P)
  OpenAmtAP Num(19,6) Open Amount (A/P)
  PERCENT Num(19,6) Contribution Rate - Percentage
  FINISH VarChar(1) Finished default=N [Y=Yes, N=No]
  OWNER Int(11) Owner ->OHEM
  StageDep1 Int(11) Stage Dependence (1)
  StageDep2 Int(11) Stage Dependence (2)
  StageDep3 Int(11) Stage Dependence (3)
  StageDep4 Int(11) Stage Dependence (4)
  StDp1Type VarChar(1) Stage Dependence (1) project type default=P [P=Project, S=Subproject]
  StDp2Type VarChar(1) Stage Dependence (2) project type default=P [P=Project, S=Subproject]
  StDp3Type VarChar(1) Stage Dependence (3) project type default=P [P=Project, S=Subproject]
  StDp4Type VarChar(1) Stage Dependence (4) project type default=P [P=Project, S=Subproject]
  StDp1Abs Int(11) Stage Dependence (1) project key
  StDp2Abs Int(11) Stage Dependence (2) project key
  StDp3Abs Int(11) Stage Dependence (3) project key
  StDp4Abs Int(11) Stage Dependence (4) project key
  LogInstanc Int(11) Log Instance default=0
  AtcEntry Int(11) Attachment Entry ->OATC
  UniqueID nVarChar(50) Unique ID
  EncryptIV nVarChar(100) Encrypt IV

# APH2 - Project Management - Stages - Open Issues - History
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  AREA Int(11) Area ->PMC3
  PRIORITY Int(11) Priority
  REMARKS Text(16) Remarks
  CLOSED VarChar(1) Closed default=N [Y=Yes, N=No]
  SOLUTIONID Int(11) Solution Code ->OSLT
  SOLUTION nVarChar(254) Solution Description
  RESPNSIBLE Int(11) Responsible ->OHEM
  ENTERED Int(11) Entered By ->OHEM
  DATE Date(8) Date Entered
  EFFORT Num(19,6) Effort Costs
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# APH3 - Project Management - Stages - Attachments - History
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  PATH Text(16) Document Path
  FILE nVarChar(100) File Name
  DATE Date(8) Date
  LogInstanc Int(11) Log Instance default=0

# APH4 - Project Management - Stages - Documents - History
Module: General | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  TYP Int(11) Document Type default=-1 [-1=Please select, 30=Manual Journal Entry, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 16=Return, 203002=A/R Down Payment Request, 203=A/R Down Payment Invoice, 13=A/R Invoice, 14=A/R Credit Memo, 13002=A/R Reserve Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 204002=A/P Down Payment Request, 204=A/P Down Payment Invoice, 18=A/P Invoice, 19=A/P Credit Memo, 18002=A/P Reserve Invoice, 191=Service Call, 59=Goods Receipt, 60=Goods Issue, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 1470000113=Purchase Request, 234000032=Goods Return Request, 234000031=Return Request]
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry
  DocDate Date(8) Document Date
  Total Num(19,6) Total
  LineNum Int(11) Line Number
  Status VarChar(1) Line status default=O [O=Open, C=Closed]
  LogInstanc Int(11) Log Instance default=0
  AmountCat VarChar(1) Category to which we will apply the amount from Total [I=Invoiced, O=Open]
  Categorize nVarChar(2) Category Open Amount/Invoiced A/R, A/P to which we will apply the amount from journal entry [=Ignore, OP=Open Amount (A/P), OR=Open Amount (A/R), IP=Invoiced (A/P), IR=Invoiced (A/R)]
  Operation VarChar(1) Operation which we will apply to the amount from the total [=Ignore, A=Add, S=Subtract]
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  ChargedQty Num(19,6) Charged Quantity
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  EncryptIV nVarChar(100) Encrypt IV
  PartTotal Num(19,6) Partially Invoiced Total

# APH5 - Project Management - Stages - Resources - History
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  LogInstanc Int(11) Log Instance default=0

# APH6 - Project Management - Stages - Activities - History
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  ACTIVITYID Int(11) Activity Number ->OCLG
  LogInstanc Int(11) Log Instance default=0
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV

# APH7 - Project Management - Workorders - History
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry ->OWOR
  LogInstanc Int(11) Log Instance default=0
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  EncryptIV nVarChar(100) Encrypt IV

# APH8 - Project Management - Summary - History
Module: General | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  PhBudget Num(19,6) Subproject Budget
  OpenAmtAP Num(19,6) Open Amount (A/P)
  InvoicedAP Num(19,6) Invoiced (A/P)
  TotalAP Num(19,6) Total (A/P)
  TotVarAP Num(19,6) Total Variance (A/P)
  VarPercAP Num(19,6) Variance Percentage (A/P)
  AccPhBudg Num(19,6) Accumulated Subproject Budget
  AccOpAmAP Num(19,6) Accumulated Open Amount (A/P)
  AccInvAP Num(19,6) Accumulated Invoiced (A/P)
  AccTotAP Num(19,6) Accumulated Total (A/P)
  AccTVarAP Num(19,6) Accumulated Total Variance (A/P)
  AccVPercAP Num(19,6) Accumulated Variance Percentage (A/P)
  PoPhAmt Num(19,6) Potential Subproject Amount
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvoicedAR Num(19,6) Invoiced (A/R)
  TotalAR Num(19,6) Total (A/R)
  TotVarAR Num(19,6) Total Variance (A/R)
  VarPercAR Num(19,6) Variance Percentage (A/R)
  AccPoPhAmt Num(19,6) Accumulated Potential Subproject Amount
  AccOpAmAR Num(19,6) Accumulated Open Amount (A/R)
  AccInvAR Num(19,6) Accumulated Invoiced (A/R)
  AccTotAR Num(19,6) Accumulated Total (A/R)
  AccTVarAR Num(19,6) Accumulated Total Variance (A/R)
  AccVPercAR Num(19,6) Accumulated Variance Percentage (A/R)
  ActICCost Num(19,6) Actual Item Component Cost
  ActRCCost Num(19,6) Actual Resource Component Cost
  ActAddCost Num(19,6) Actual Additional Cost
  ActPrCost Num(19,6) Actual Product Cost
  ActBPrCost Num(19,6) Actual By-Product Cost
  TotalVar Num(19,6) Total Variance
  DueDate Date(8) Due Date
  CloseDate Date(8) Actual Closing Date
  Overdue Int(11) Overdue default=0
  Valid VarChar(1) If the calculated data is valid default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0

# APHA - Project Management Subproject - History
Module: General | 22 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  OWNER Int(11) Owner ->OHEM
  NAME nVarChar(254) Name
  START Date(8) Subproject Start Date
  FINISHED Num(19,6) Deduction - Percentage
  ParentID Int(11) Parent Subproject
  ProjectID Int(11) Project No. ->OPMG
  Code Int(11) Subproject No.
  TYP Int(11) Subproject Type ->PMC1
  CONTRIB Num(19,6) Subproject Contribution - Percentage
  STATUS VarChar(1) Status default=O [O=Open, C=Closed]
  END Date(8) Subproject End Date
  COST Num(19,6) Actual Cost
  PLANNED Num(19,6) Planned Cost
  Level Int(11) Depth of Subproject within the project
  DUEDATE Date(8) Due Date
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time

# APM1 - Project Management - Stages - History
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OPMG
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMC2
  POS Int(11) Position
  START Date(8) Start Date
  CLOSE Date(8) Closing Date
  FINISHDATE Date(8) Finished Date
  Task Int(11) Task Type
  DSCRIPTION Text(16) Description
  EXPCOSTS Num(19,6) Planned Cost
  InvAmtAR Num(19,6) Invoiced Amount (A/R)
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvAmtAP Num(19,6) Invoiced Amount (A/P)
  OpenAmtAP Num(19,6) Open Amount (A/P)
  PERCENT Num(19,6) Contribution Rate - Percentage
  FINISH VarChar(1) Finished default=N [Y=Yes, N=No]
  OWNER Int(11) Owner ->OHEM
  StageDep1 Int(11) Stage Dependence (1)
  StageDep2 Int(11) Stage Dependence (2)
  StageDep3 Int(11) Stage Dependence (3)
  StageDep4 Int(11) Stage Dependence (4)
  StDp1Type VarChar(1) Stage Dependence (1) project type default=P [P=Project, S=Subproject]
  StDp2Type VarChar(1) Stage Dependence (2) project type default=P [P=Project, S=Subproject]
  StDp3Type VarChar(1) Stage Dependence (3) project type default=P [P=Project, S=Subproject]
  StDp4Type VarChar(1) Stage Dependence (4) project type default=P [P=Project, S=Subproject]
  StDp1Abs Int(11) Stage Dependence (1) project key
  StDp2Abs Int(11) Stage Dependence (2) project key
  StDp3Abs Int(11) Stage Dependence (3) project key
  StDp4Abs Int(11) Stage Dependence (4) project key
  LogInstanc Int(11) Log Instance default=0
  AtcEntry Int(11) Attachment Entry ->OATC
  UniqueID nVarChar(50) Unique ID
  EncryptIV nVarChar(100) Encrypt IV

# APM2 - Project Management - Stages - Open Issues - History
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  AREA Int(11) Area ->PMC3
  PRIORITY Int(11) Priority
  REMARKS Text(16) Remarks
  CLOSED VarChar(1) Closed default=N [Y=Yes, N=No]
  SOLUTIONID Int(11) Solution Code ->OSLT
  SOLUTION nVarChar(254) Solution Description
  RESPNSIBLE Int(11) Responsible ->OHEM
  ENTERED Int(11) Entered By ->OHEM
  DATE Date(8) Date Entered
  EFFORT Num(19,6) Effort Costs
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# APM3 - Project Management - Stages - Attachments - History
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMG1
  PATH Text(16) Document Path
  FILE nVarChar(100) File Name
  DATE Date(8) Date
  LogInstanc Int(11) Log Instance default=0

# APM4 - Project Management - Stages - Documents - History
Module: General | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  TYP Int(11) Document Type default=-1 [-1=Please select, 112=Document Draft, 30=Manual Journal Entry, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 16=Return, 203002=A/R Down Payment Request, 203=A/R Down Payment Invoice, 13=A/R Invoice, 14=A/R Credit Memo, 13002=A/R Reserve Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 204002=A/P Down Payment Request, 204=A/P Down Payment Invoice, 18=A/P Invoice, 19=A/P Credit Memo, 18002=A/P Reserve Invoice, 191=Service Call, 59=Goods Receipt, 60=Goods Issue, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 1470000113=Purchase Request, 234000032=Goods Return Request, 234000031=Return Request]
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry
  DocDate Date(8) Document Date
  Total Num(19,6) Total
  LineNum Int(11) Line Number
  Status VarChar(1) Line status default=O [O=Open, C=Closed]
  LogInstanc Int(11) Log Instance default=0
  AmountCat VarChar(1) Category to which we will apply the amount from Total [I=Invoiced, O=Open]
  Categorize nVarChar(2) Category Open Amount/Invoiced A/R, A/P to which we will apply the amount from journal entry [=Ignore, OP=Open Amount (A/P), OR=Open Amount (A/R), IP=Invoiced (A/P), IR=Invoiced (A/R)]
  Operation VarChar(1) Operation which we will apply to the amount from the total [=Ignore, A=Add, S=Subtract]
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  ChargedQty Num(19,6) Charged Quantity
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  EncryptIV nVarChar(100) Encrypt IV
  PartTotal Num(19,6) Partially Invoiced Total

# APM5 - Project Management - Stages - Resources - History
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMG1
  LogInstanc Int(11) Log Instance default=0

# APM6 - Project Management - Stages - Activities - History
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  ACTIVITYID Int(11) Activity Number ->OCLG
  LogInstanc Int(11) Log Instance default=0
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV

# APM7 - Project Management - Workorders - History
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry ->OWOR
  LogInstanc Int(11) Log Instance default=0
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  EncryptIV nVarChar(100) Encrypt IV

# APM8 - Project Management - Summary - History
Module: General | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  PhBudget Num(19,6) Subproject Budget
  OpenAmtAP Num(19,6) Open Amount (A/P)
  InvoicedAP Num(19,6) Invoiced (A/P)
  TotalAP Num(19,6) Total (A/P)
  TotVarAP Num(19,6) Total Variance (A/P)
  VarPercAP Num(19,6) Variance Percentage (A/P)
  AccPhBudg Num(19,6) Accumulated Subproject Budget
  AccOpAmAP Num(19,6) Accumulated Open Amount (A/P)
  AccInvAP Num(19,6) Accumulated Invoiced (A/P)
  AccTotAP Num(19,6) Accumulated Total (A/P)
  AccTVarAP Num(19,6) Accumulated Total Variance (A/P)
  AccVPercAP Num(19,6) Accumulated Variance Percentage (A/P)
  PoPhAmt Num(19,6) Potential Subproject Amount
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvoicedAR Num(19,6) Invoiced (A/R)
  TotalAR Num(19,6) Total (A/R)
  TotVarAR Num(19,6) Total Variance (A/R)
  VarPercAR Num(19,6) Variance Percentage (A/R)
  AccPoPhAmt Num(19,6) Accumulated Potential Subproject Amount
  AccOpAmAR Num(19,6) Accumulated Open Amount (A/R)
  AccInvAR Num(19,6) Accumulated Invoiced (A/R)
  AccTotAR Num(19,6) Accumulated Total (A/R)
  AccTVarAR Num(19,6) Accumulated Total Variance (A/R)
  AccVPercAR Num(19,6) Accumulated Variance Percentage (A/R)
  ActICCost Num(19,6) Actual Item Component Cost
  ActRCCost Num(19,6) Actual Resource Component Cost
  ActAddCost Num(19,6) Actual Additional Cost
  ActPrCost Num(19,6) Actual Product Cost
  ActBPrCost Num(19,6) Actual By-Product Cost
  TotalVar Num(19,6) Total Variance
  DueDate Date(8) Due Date
  CloseDate Date(8) Actual Closing Date
  Overdue Int(11) Overdue default=0
  Valid VarChar(1) If the calculated data is valid default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0

# APMG - Project Management Document - History
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  OWNER Int(11) Owner ->OHEM
  NAME nVarChar(254) Project Name
  START Date(8) Project Start Date
  FINISHED Num(19,6) Deduction - Percentage
  DocNum Int(11) Document Number
  Series Int(11) Series
  TYP VarChar(1) Project Type default=E [E=External, I=Internal]
  CARDCODE nVarChar(15) BP Code ->OCRD
  CARDNAME nVarChar(100) BP Name
  CONTACT Int(11) Contact Person ->OCPR
  TERRITORY Int(11) Business Partner Territory ->OTER
  EMPLOYEE Int(11) Sales Employee default=-1 ->OSLP
  WithPhases VarChar(1) Project with Phases default=N [Y=Yes, N=No]
  STATUS VarChar(1) Status default=S [S=Started, P=Paused, T=Stopped, F=Finished, N=Canceled]
  DUEDATE Date(8) Due Date
  CLOSING Date(8) Closing Date
  FIPROJECT nVarChar(20) Financial Project ->OPRJ
  RISK VarChar(1) Risk Level default=L [L=Low, M=Medium, H=High]
  INDUSTRY Int(11) Industry Code ->OOND
  REASON Text(16) Comments
  Free_Text Text(16) Free Text
  BPLid Int(11) Business Place ID ->OBPL
  AtcEntry Int(11) Attachment Entry
  Attachment Text(16) Attachments
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV

# ARSB - Resource Groups - History
Module: General | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResGrpCod, logInstanc
  GROUP_NAME U: ResGrpNam, logInstanc
Fields (name type(len) description [values] ->parent table):
  ResGrpCod Int(6) Number
  ResGrpNam nVarChar(20) Group Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Object nVarChar(20) Object Type - History default=292
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History
  updateDate Date(8) Date of Update - History
  ResType VarChar(1) Resource Type default=M [M=Machine, L=Labor, O=Other]
  CostName1 nVarChar(254) Resource Std Cost 1
  CostVal1 Num(19,6) Resource Std Cost 1
  CostName2 nVarChar(254) Resource Std Cost 2
  CostVal2 Num(19,6) Resource Std Cost 2
  CostName3 nVarChar(254) Resource Std Cost 3
  CostVal3 Num(19,6) Resource Std Cost 3
  CostName4 nVarChar(254) Resource Std Cost 4
  CostVal4 Num(19,6) Resource Std Cost 4
  CostName5 nVarChar(254) Resource Std Cost 5
  CostVal5 Num(19,6) Resource Std Cost 5
  CostName6 nVarChar(254) Resource Std Cost 2
  CostVal6 Num(19,6) Resource Std Cost 6
  CostName7 nVarChar(254) Resource Std Cost 7
  CostVal7 Num(19,6) Resource Std Cost 7
  CostName8 nVarChar(254) Resource Std Cost 8
  CostVal8 Num(19,6) Resource Std Cost 8
  CostName9 nVarChar(254) Resource Std Cost 9
  CostVal9 Num(19,6) Resource Std Cost 9
  CostName10 nVarChar(254) Resource Std Cost 10
  CostVal10 Num(19,6) Resource Std Cost 10
  ResUoM nVarChar(20) Resource Unit of Measurement

# ARSC - Resource Master Data - Log
Module: General | 125 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, LogInstanc
  ITEM_NAME: ResName
  SALE: PrchseRes
  PURCHASE: SellRes
  PRODUCTION: ProdRes
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Code
  VisResCode nVarChar(50) Resource No.
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  CodeBars nVarChar(254) Bar Code
  ResName nVarChar(200) Resource Description
  FrgnName nVarChar(200) Description in Foreign Lang.
  ResType VarChar(1) Resource Type default=M [M=Machine, L=Labor, O=Other]
  ResGrpCod Int(6) Resource Group default=1 ->ORSB
  UnitOfMsr nVarChar(100) Unit of Measure
  PrchseRes VarChar(1) Purchase Resource [Yes/No] default=Y [Y=Yes, N=No]
  SellRes VarChar(1) Sales Resource [Yes/No] default=Y [Y=Yes, N=No]
  ProdRes VarChar(1) Production Resource [Yes/No] default=Y [Y=Yes, N=No]
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  IssueMthd VarChar(1) Issue Method default=B [B=Backflush, M=Manual]
  StdCost1 Num(19,6) Resource Cost 1
  StdCost2 Num(19,6) Resource Cost 2
  StdCost3 Num(19,6) Resource Cost 3
  StdCost4 Num(19,6) Resource Cost 4
  StdCost5 Num(19,6) Resource Cost 5
  StdCost6 Num(19,6) Resource Cost 6
  StdCost7 Num(19,6) Resource Cost 7
  StdCost8 Num(19,6) Resource Cost 8
  StdCost9 Num(19,6) Resource Cost 9
  StdCost10 Num(19,6) Resource Cost 10
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  DfltWH nVarChar(8) Default Warehouse
  QueryGroup Int(11) Properties default=0
  PicturName nVarChar(200) Picture
  UserText Text(16) Item Remarks
  QryGroup1 VarChar(1) Property 1 default=N [Y=Yes, N=No]
  QryGroup2 VarChar(1) Property 2 default=N [Y=Yes, N=No]
  QryGroup3 VarChar(1) Property 3 default=N [Y=Yes, N=No]
  QryGroup4 VarChar(1) Property 4 default=N [Y=Yes, N=No]
  QryGroup5 VarChar(1) Property 5 default=N [Y=Yes, N=No]
  QryGroup6 VarChar(1) Property 6 default=N [Y=Yes, N=No]
  QryGroup7 VarChar(1) Property 7 default=N [Y=Yes, N=No]
  QryGroup8 VarChar(1) Property 8 default=N [Y=Yes, N=No]
  QryGroup9 VarChar(1) Property 9 default=N [Y=Yes, N=No]
  QryGroup10 VarChar(1) Property 10 default=N [Y=Yes, N=No]
  QryGroup11 VarChar(1) Property 11 default=N [Y=Yes, N=No]
  QryGroup12 VarChar(1) Property 12 default=N [Y=Yes, N=No]
  QryGroup13 VarChar(1) Property 13 default=N [Y=Yes, N=No]
  QryGroup14 VarChar(1) Property 14 default=N [Y=Yes, N=No]
  QryGroup15 VarChar(1) Property 15 default=N [Y=Yes, N=No]
  QryGroup16 VarChar(1) Property 16 default=N [Y=Yes, N=No]
  QryGroup17 VarChar(1) Property 17 default=N [Y=Yes, N=No]
  QryGroup18 VarChar(1) Property 18 default=N [Y=Yes, N=No]
  QryGroup19 VarChar(1) Property 19 default=N [Y=Yes, N=No]
  QryGroup20 VarChar(1) Property 20 default=N [Y=Yes, N=No]
  QryGroup21 VarChar(1) Property 21 default=N [Y=Yes, N=No]
  QryGroup22 VarChar(1) Property 22 default=N [Y=Yes, N=No]
  QryGroup23 VarChar(1) Property 23 default=N [Y=Yes, N=No]
  QryGroup24 VarChar(1) Property 24 default=N [Y=Yes, N=No]
  QryGroup25 VarChar(1) Property 25 default=N [Y=Yes, N=No]
  QryGroup26 VarChar(1) Property 26 default=N [Y=Yes, N=No]
  QryGroup27 VarChar(1) Property 27 default=N [Y=Yes, N=No]
  QryGroup28 VarChar(1) Property 28 default=N [Y=Yes, N=No]
  QryGroup29 VarChar(1) Property 29 default=N [Y=Yes, N=No]
  QryGroup30 VarChar(1) Property 30 default=N [Y=Yes, N=No]
  QryGroup31 VarChar(1) Property 31 default=N [Y=Yes, N=No]
  QryGroup32 VarChar(1) Property 32 default=N [Y=Yes, N=No]
  QryGroup33 VarChar(1) Property 33 default=N [Y=Yes, N=No]
  QryGroup34 VarChar(1) Property 34 default=N [Y=Yes, N=No]
  QryGroup35 VarChar(1) Property 35 default=N [Y=Yes, N=No]
  QryGroup36 VarChar(1) Property 36 default=N [Y=Yes, N=No]
  QryGroup37 VarChar(1) Property 37 default=N [Y=Yes, N=No]
  QryGroup38 VarChar(1) Property 38 default=N [Y=Yes, N=No]
  QryGroup39 VarChar(1) Property 39 default=N [Y=Yes, N=No]
  QryGroup40 VarChar(1) Property 40 default=N [Y=Yes, N=No]
  QryGroup41 VarChar(1) Property 41 default=N [Y=Yes, N=No]
  QryGroup42 VarChar(1) Property 42 default=N [Y=Yes, N=No]
  QryGroup43 VarChar(1) Property 43 default=N [Y=Yes, N=No]
  QryGroup44 VarChar(1) Property 44 default=N [Y=Yes, N=No]
  QryGroup45 VarChar(1) Property 45 default=N [Y=Yes, N=No]
  QryGroup46 VarChar(1) Property 46 default=N [Y=Yes, N=No]
  QryGroup47 VarChar(1) Property 47 default=N [Y=Yes, N=No]
  QryGroup48 VarChar(1) Property 48 default=N [Y=Yes, N=No]
  QryGroup49 VarChar(1) Property 49 default=N [Y=Yes, N=No]
  QryGroup50 VarChar(1) Property 50 default=N [Y=Yes, N=No]
  QryGroup51 VarChar(1) Property 51 default=N [Y=Yes, N=No]
  QryGroup52 VarChar(1) Property 52 default=N [Y=Yes, N=No]
  QryGroup53 VarChar(1) Property 53 default=N [Y=Yes, N=No]
  QryGroup54 VarChar(1) Property 54 default=N [Y=Yes, N=No]
  QryGroup55 VarChar(1) Property 55 default=N [Y=Yes, N=No]
  QryGroup56 VarChar(1) Property 56 default=N [Y=Yes, N=No]
  QryGroup57 VarChar(1) Property 57 default=N [Y=Yes, N=No]
  QryGroup58 VarChar(1) Property 58 default=N [Y=Yes, N=No]
  QryGroup59 VarChar(1) Property 59 default=N [Y=Yes, N=No]
  QryGroup60 VarChar(1) Property 60 default=N [Y=Yes, N=No]
  QryGroup61 VarChar(1) Property 61 default=N [Y=Yes, N=No]
  QryGroup62 VarChar(1) Property 62 default=N [Y=Yes, N=No]
  QryGroup63 VarChar(1) Property 63 default=N [Y=Yes, N=No]
  QryGroup64 VarChar(1) Property 64 default=N [Y=Yes, N=No]
  CreateDate Date(8) Date of Creation
  UpdateDate Date(8) Date of Update
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=290
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  UserSign2 Int(6) Updating User
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  LastPurPrc Num(19,6) Last Purchase Price
  LastPurCur nVarChar(3) Last Purchase Currency
  LastPurDat Date(8) Last Purchase Date
  LstEvlPric Num(19,6) Last Evaluated Price
  LstEvlDate Date(8) Date of Last Reval. Price
  NumResUnit Int(11) No. of Resource Units default=1
  TimeResUn Int(11) Time per Resource Units
  ResAlloc VarChar(1) Resource Allocation default=S [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  LinkItm nVarChar(50) Linked Item ->OITM
  RelCap1 VarChar(1) Relevant to single run capacity 1 default=Y [Y=Yes, N=No]
  RelCap2 VarChar(1) Relevant to single run capacity 2 default=Y [Y=Yes, N=No]
  RelCap3 VarChar(1) Relevant to single run capacity 3 default=Y [Y=Yes, N=No]
  RelCap4 VarChar(1) Relevant to single run capacity 4 default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature

# ARSC1 - Resources - Warehouses - Log
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, WhsCode, LogInstanc
  WHS: WhsCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Locked VarChar(1) Locked default=N [N=No, Y=Yes]
  ObjType nVarChar(20) Object default=290
  LogInstanc Int(11) Log Instance default=0

# ARSC2 - Resources - Prices - Log
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, PriceList, LogInstanc
  CURRENCY: Currency
  PRICE_LIST: PriceList
  MANUAL: Ovrwritten
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  PriceList Int(11) Price List No. ->OPLN
  Price Num(19,6) List Price
  Currency nVarChar(3) Currency for List Price ->OCRN
  Ovrwritten VarChar(1) Manual Price Entry default=N [Y=Yes, N=No]
  Factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=290 ->ADP1
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  Ovrwrite1 VarChar(1) Manual Price Entry (1) default=N [Y=Yes, N=No]
  Ovrwrite2 VarChar(1) Manual Price Entry (2) default=N [Y=Yes, N=No]

# ARSC3 - Resouces - Fixed Assets - Log
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, ItemCode, LogInstanc
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  ItemCode nVarChar(50) Item Code ->OITM
  LogInstanc Int(11) Log Instance default=0

# ARSC4 - Resources - Employees - Log
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, EmpID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  EmpID nVarChar(11) Employee No. ->OHEM
  LogInstanc Int(11) Log Instance default=0

# ARSC5 - Resources - Preferred Vendors - Log
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, VendorCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  VendorCode nVarChar(15) Vendor Code ->OCRD
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=290 ->ADP1

# ARSC6 - Resources - Daily Capacities - Log
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, WeekDay, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  WeekDay Int(11) Weekday No. [1=First Day of Week, 2=Second Day of Week, 3=Third Day of Week, 4=Fourth Day of Week, 5=Fifth Day of Week, 6=Sixth Day of Week, 7=Seventh Day of Week]
  CapFactor1 Num(19,6) Day 1 Capacity Factor 1
  CapFactor2 Num(19,6) Day 1 Capacity Factor 2
  CapFactor3 Num(19,6) Day 1 Capacity Factor 3
  CapFactor4 Num(19,6) Day 1 Capacity Factor 4
  CapTotal Num(19,6) Total Daily Capacity
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  SngRunCap Num(19,6) Single Run Capacity

# ASC7 - Service Call BP Address
Module: General | 67 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSCL
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) NF Reference
  Carrier nVarChar(15) Carrier Code ->OCRD
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=191 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  EncryptIV nVarChar(100) Encrypt IV

# ASH1 - Time Sheet - Rows - History
Module: General | 31 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  Date Date(8) Date
  ActType Int(11) Activity Type ->PMC5
  LaborItem nVarChar(50) Labor Item No.
  StartTime Int(11) Start Time
  EndTime Int(11) End Time
  Workorder Int(11) Workorder Doc. Entry ->OWOR
  WorAbs Int(11) Workorder Abs. Entry
  ServCall Int(11) Service Call ID ->OSCL
  CostCenter nVarChar(8) Cost Center
  FiProject nVarChar(20) Financial Project
  Location Int(11) Location
  GPSData nVarChar(50) GPS Data
  Branch Int(11) Branch ID ->OBPL
  Break Int(11) Break
  NonBillTm Int(11) Nonbillable Time
  EffectTm Int(11) Effective Time
  BillableTm Int(11) Billable Time
  FullDay VarChar(1) Full Day default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ProjectID Int(11) Project or Subproject ID
  Subproject Int(11) Subproject ID
  StageID Int(11) Stage ID
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV
  BreakHr Num(19,6) Break Hours
  NonBillHr Num(19,6) Non-Billable Hours
  EffectHr Num(19,6) Effective Hours
  BillableHr Num(19,6) Billable Hours

# ASQL - SQL query
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SqlCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  SqlCode nVarChar(254) SQL query code
  SqlName nVarChar(254) SQL query name
  SqlText Text(16) SQL text
  ParamList nVarChar(254) List of bound parameter names
  ParamDetai nVarChar(254) Parameter details
  InternalS Text(16) Internal SQL text
  LogInstanc Int(11) Log instance default=0
  ObjType nVarChar(20) Object Type default=2
  CreateDate Date(8) Created On
  UpdateDate Date(8) Updated On
  DataVers Int(11) Data version default=1

# ATSH - Time Sheet - Header - History
Module: General | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  ProjectID Int(11) Project No. ->OPMG
  DocNum Int(11) Document Number
  Type VarChar(1) Type default=E [E=Employee, U=User, O=External]
  UserID Int(11) Employee/User ID ->OHEM
  LastName nVarChar(50) Last Name
  FirstName nVarChar(50) First Name
  Department Int(6) Department
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  SAPPassprt Text(16) Extended SAP Passport
  EncryptIV nVarChar(100) Encrypt IV
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachment
  UserCode nVarChar(50) Employee/User Code
  DataVers Int(11) Data Version default=1

# BSJ1 - Backend Scheduling Sub Tasks
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID, TaskID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Job ID ->OBSJ
  TaskID Int(11) Sub Task ID
  Type nVarChar(50) Task Type
  Params Text(16) Parameters
  RunAs Int(6) Run As User ->OUSR
  Status VarChar(1) Status default=S [S=Scheduled, R=Running, E=Error, F=Finished, P=Pending, C=Creating]
  PostTask Int(11) Post-Task
  PreTask Int(11) Pre-Task
  LastDate Date(8) Last Running Date
  LastTime Int(6) Last Running Time
  Retry Int(11) Retry Times default=0
  TimeOut Int(11) Time out default=20
  Message nVarChar(200) Status Message

# CCFG - Company Configuration
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ConfigEntr
Fields (name type(len) description [values] ->parent table):
  ConfigEntr Int(11) Internal Configuration ID
  ConfigName nVarChar(250) Configuration File Name
  ConfigDate Date(8) Configuration File Create Date
  ConfigTime Int(6) Configuration File Create Time
  UserCode Int(11) Configuration Created By
  CreateBy Int(11) Created from Menu: [0=Express Configuration Wizard, 1=Configuration Management]
  ServerName nVarChar(250) Configuration Saved on Server:
  CompanyDB nVarChar(250) Company Database
  Internal VarChar(1) Internal default=N [N=No, Y=Yes]

# CDIC - Dictionary
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Namespace, _Key
Fields (name type(len) description [values] ->parent table):
  Namespace nVarChar(50) Namespace
  _Key nVarChar(50) Key
  _Value Text(16) Value

# CFN1 - Default Common Functions
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ItemIndex
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OCFN
  ItemIndex Int(11) Common Function Item Index
  UserMenu VarChar(1) User Menu Flag default=N [Y=, N=]
  MenuUID nVarChar(50) Menu UID
  Name nVarChar(100) Name

# CFUS - Functionality Usage Statistics
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FuncName, UserCode
Fields (name type(len) description [values] ->parent table):
  FuncName nVarChar(100) Function Name
  UserCode nVarChar(25) User Code
  Count Int(11) Total No. of Records
  Since Date(8) Since Date
  LastUse Date(8) Last Use Date

# CIFV - Inventory-FIFO Revaluation
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, LayerNum
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  LayerNum Int(11) Layer Number
  OinmNum Int(11) OINM Transaction Number ->OINM
  Instance Int(11) Instance in OINM
  Quantity Num(19,6) Quantity in Layer
  Price Num(19,6) Price in Layer
  OutQty Num(19,6) Out Quantity

# CIGR - Approval Process Ignore List
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, FieldName
Fields (name type(len) description [values] ->parent table):
  Category VarChar(1) Category [D=Document, O=Inventory Opening Balance, P=Inventory Posting, C=Inventory Counting, V=Payment]
  TableName nVarChar(20) Table Name
  FieldName nVarChar(50) Field Name

# CIN11 - Correction Invoice - Drawn Dpm Detail
Module: General | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OCIN
  LineNum Int(11) Row Number
  LineSeq Int(11) Sequence Number
  BaseAbs Int(11) Base Document Internal ID
  BaseType Int(11) Base Object Type default=-1 [-1=]
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  VatPrcnt Num(19,6) VAT Percent
  LineTotal Num(19,6) Net LC
  TotalFrgn Num(19,6) Net FC
  TotalSumSy Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFrgn Num(19,6) Tax FC
  VatSumSys Num(19,6) Tax SC
  ObjType nVarChar(20) Object Type default=132 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Liable for Acquisition Tax default=N [N=No, Y=Yes]
  IsAllDrawn VarChar(1) Remaining Amount Drawn default=N [Y=Yes, N=No]
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  BaseNet Num(19,6) Base Net LC
  BaseNetFc Num(19,6) Base Net FC
  BaseNetSc Num(19,6) Base Net SC
  BaseVat Num(19,6) Base Tax LC
  BaseVatFc Num(19,6) Base Tax FC
  BaseVatSc Num(19,6) Base Tax SC
  BaseGross Num(19,6) Base Gross LC
  BaseGrossF Num(19,6) Base Gross FC
  BaseGrossS Num(19,6) Base Gross SC
  LineType VarChar(1) Line Type default=D [D=Document Row, R=Currency Rounding, H=Down Payment Document Rounding]
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum LC
  BaseDctFc Num(19,6) Base Deductible Sum FC
  BaseDctSc Num(19,6) Base Deductible Sum SC
  BaseEq Num(19,6) Base Equalization Sum LC
  BaseEqFc Num(19,6) Base Equalization Sum FC
  BaseEqSc Num(19,6) Base Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  ApplGross Num(19,6) Applied Gross LC
  ApplGrossF Num(19,6) Applied Gross FC
  ApplGrossS Num(19,6) Applied Gross SC
  TaxAdjust VarChar(1) Manual Tax Adjustment default=N [Y=Yes, N=No]
  RvsChrgSum Num(19,6) Reverse Charge Sum LC
  RvsChrgFc Num(19,6) Reverse Charge Sum FC
  RvsChrgSc Num(19,6) Reverse Charge Sum SC
  BasRvsChrg Num(19,6) Base Reverse Charge LC
  BasRvsFc Num(19,6) Base Reverse Charge FC
  BasRvsSc Num(19,6) Base Reverse Charge SC
  ApplRvs Num(19,6) Applied Reverse Charge LC
  ApplRvsFc Num(19,6) Applied Reverse Charge FC
  ApplRvsSc Num(19,6) Applied Reverse Charge SC
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# CLC1 - Change Logs Cleanup Line
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ModObjKey
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ModObjKey nVarChar(8) Module or Object Key
  CurSize Num(19,6) Current Size (MB)
  Status Int(11) Status

# COLM - COLM resource
Module: General | 64 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, Num, ResCode, RevCode
  UNIQUE_ID U: Name, UniqueID
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation Date
  Updated Date(8) Update Date
  Name nVarChar(64) Table Name
  Num Int(11) Column Number
  ItemType Int(11) Item Type default=0 [0=None, 16=Edit text, 105=Bar, 113=Select popup, 116=Link button, 121=Check box, 117=Picture]
  Enabled VarChar(1) Enabled default=1 [0=No, 1=Yes]
  CellType Int(11) Cell Type default=16 [0=None, 16=Edit text, 105=Bar, 113=Select popup, 116=Link button, 121=Check box, 117=Picture]
  Font Int(11) Font Number
  FontSize Int(11) Font Size
  Attributes Int(11) Attributes
  Style Int(11) Style
  Mode Int(11) Mode
  TitleType Int(11) Title Type default=0 [0=None, 117=Picture]
  TitleEnabl VarChar(1) Title Enabled
  TitleFont Int(11) Title Font Number
  TFontSize Int(11) Title Font Size
  TitleAtt Int(11) Title Attributes
  TitleStyle Int(11) Title Style
  TitleMode Int(11) Title Mode
  VarNum Int(11) Variable Number
  LinkVar Int(11) Link Variable
  DragVar Int(11) Drag Variable
  FileCode nVarChar(20) Table Code
  FieldNum nVarChar(10) Field Alias
  Editable VarChar(1) Editable default=1 [0=No, 1=Yes]
  SuppressZe VarChar(1) Suppress Zeros default=0 [0=No, 1=Yes]
  DataRequir VarChar(1) Data Required default=0 [0=No, 1=Yes]
  ForceUpper VarChar(1) Force Upper default=0 [0=No, 1=Yes]
  RightJust VarChar(1) Right Justified default=1 [0=No, 1=Yes, 2=Language dependant]
  UserType VarChar(1) Binding Type default=0 [0=Data, 1=User Variable]
  Sentence VarChar(1) Sentencing default=0 [0=No, 1=Yes]
  ShowType VarChar(1) Show Type default=0 [0=Value + Description, 1=Value only, 2=Description only]
  DispDecr VarChar(1) Display Description default=0 [0=No, 1=Yes]
  LinkTo Int(11) Link To Item
  DragEntity Int(11) Drag Entity
  Class Int(11) Class
  TitleIndex Int(11) Title Index default=0
  DescIndex Int(11) Description Index default=0
  TxtFgRed Int(11) Text Foreground Red
  TxtFgGreen Int(11) Text Foreground Green
  TxtFgBlue Int(11) Text Foreground Blue
  TxtBgRed Int(11) Text Background Red
  TxtBgGreen Int(11) Text Background Green
  TxtBgBlue Int(11) Text Background Blue
  TtlFgRed Int(11) Title Foreground Red
  TtlFgGreen Int(11) Title Foreground Green
  TtlFgBlue Int(11) Title Foreground Blue
  TtlBgRed Int(11) Title Background Red
  TtlBgGreen Int(11) Title Background Green
  TtlBgBlue Int(11) Title Background Blue
  Width Int(11) Width
  SuppRepeat VarChar(1) Suppress Repeating default=0 [0=No, 1=Yes]
  AutoGraph VarChar(1) Auto Graph default=0 [0=No, 1=Yes]
  AutoCumm VarChar(1) Auto Cummulative default=0 [0=No, 1=Yes]
  UniqueID nVarChar(10) Unique ID
  TitleStr nVarChar(254) Title String
  ColDesc nVarChar(254) Column Description
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  TtlFntName nVarChar(32) Title Font Name
  CllFntName nVarChar(32) Cell Font Name
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  BindObjId Int(11) Bind Object Id default=-1

# CPA1 - Periods Category - WIP Mapping
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OACP
  LineNum Int(11) Line Number
  LogInstanc Int(11) Log Instance
  AcctFrom nVarChar(15) Consolidate from Account ->OACT
  AcctTo nVarChar(15) Consolidate to Account ->OACT

# CPRC - Contact Persons - Communication Mean
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CntctCode, CommMeanID
Fields (name type(len) description [values] ->parent table):
  CntctCode Int(11) Internal Number ->OCPR
  CommMeanID Int(11) Communication Mean ID ->OCMM
  Select VarChar(1) Select [Y=Yes, N=No]
  CardCode nVarChar(15) BP Code ->OCRD
  CntctName nVarChar(50) Contact Person Name ->OCPR

# CPT1 - Cockpit Subtable
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, SubEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OCPT
  SubEntry Int(11) Subnumber
  _Title nVarChar(20) Show Title
  WdtEntry Int(11) Widget Entry ->OWDT
  _Left Int(6) Left
  _Right Int(6) Right
  _Top Int(6) Top
  _Bottom Int(6) Bottom

# CRDC - BP - Communication Means
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, CommMeanId
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  CommMeanId Int(11) Communication Mean ID ->OCMM
  Select VarChar(1) Select [Y=Yes, N=No]

# CTNS - Transaction Notification Setting
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  OBJECT_ID U: ObjectId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal No.
  ObjectId nVarChar(30) Business Object ID
  EnableAsyN VarChar(1) Enable async notification default=N [Y=Yes, N=No]
  EnableTn VarChar(1) Transaction Notification default=Y [Y=Yes, N=No]
  EnablePTn VarChar(1) Post Transaction Notification default=Y [Y=Yes, N=No]

# CUL1 - Customer Usage Statistics Log
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParrentDoc, LineNum
Fields (name type(len) description [values] ->parent table):
  ParrentDoc Int(11) Parent Document
  LineNum Int(11) Line Number
  Param Text(16) Parameter

# DAB1 - Dashboard Queries
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DsbEntry, QryCtgry, QryName
Fields (name type(len) description [values] ->parent table):
  DsbEntry Int(11) Dashboard Entry ->ODAB
  QryCtgry Int(11) Query Category ->OQCN
  QryName nVarChar(100) Query Name

# DAL1 - Mapping between form item and dashboard column
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LinkEntry Int(11) Internal Key
  ItemID nVarChar(250) Item ID
  ObjName nVarChar(250) Object Name
  PropName nVarChar(250) Property Name
  QueryCol nVarChar(250) Query Column
  MobDesc nVarChar(250) Mobile Description
  IsUDF VarChar(1) Is UDF or Not default=N [Y=Yes, N=No]

# DOCR - 
Module: General | 60 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TypeCode, Local, Numerator, Language, ResCode, RevCode
  TYP_LOC_NM: TypeCode, Local, Numerator
  TYPE_LOC: TypeCode, Local
  TYPE: TypeCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Code
  DocName nVarChar(64) Report Name
  Author nVarChar(32) Author
  Notes nVarChar(254) Remarks
  Width Int(6) Width default=595
  Height Int(6) Height default=842
  LMargin Int(6) Left Margin default=10
  RMargin Int(6) Right Margin default=30
  TMargin Int(6) Top Margin default=10
  BMargin Int(6) Bottom Margin default=10
  CanChange Int(6) Changable default=1 [1=TRUE, 0=FALSE]
  PaperSize nVarChar(100) Paper Size default=A4 210 x 297 mm
  Oreint VarChar(1) Orientation default=P [P=Vertical, L=Horizontal]
  GridSize Int(6) Grid Size default=10
  GridType VarChar(1) Grid Type default=1 [1=Compbination, 2=Continuous line, 3=Broken line, 4=Dots]
  ShowGrid VarChar(1) Display Grid default=1 [1=TRUE, 0=FALSE]
  SnapGrid VarChar(1) Next to Grid default=1 [1=TRUE, 0=FALSE]
  Picture Text(16) Picture
  TypeCode nVarChar(4) Type Code
  FrgnReport VarChar(1) Foreign Language Report default=0 [1=TRUE, 0=FALSE]
  CanSort Int(6) Sortable default=1 [1=TRUE, 0=FALSE]
  LeaderCode nVarChar(8) Leader Report
  FollowCode nVarChar(8) Follow-Up Report
  SwapOnScrn Int(6) Convert Font in Print Preview default=0 [1=Yes, 0=FALSE]
  ScreenFont nVarChar(50) Preview Printing Font default=Arial
  ScrFOffset Int(6) Change Font Size in Preview Pr default=-1
  SwpInEmail Int(6) Convert Font for E-mail default=0 [1=Yes, 0=FALSE]
  EmailFont nVarChar(50) E-Mail Font default=Arial
  EmFOffset Int(6) Change Font Size for E-Mail default=-1
  QString Text(16) Query
  QType VarChar(1) Query Type default=R [R=Regular, W=Wizard]
  Language Int(6) Language
  RobjCode Int(11) Imp Exp Obj Code default=0
  ExtName Text(16) Extension Name
  ExtOnErr VarChar(1) Action Taken On Ext Error default=S [S=Stop, I=Ignore, P=Promt]
  NumRepArs Int(6) Number of Repetitive Areas default=1
  AlgnFooter VarChar(1) Allign Footer to Buttom default=N [Y=Yes, N=No]
  Local nVarChar(2) Localization
  Numerator Int(6) Numerator
  NextAppId Int(6) Next Item AppId default=1
  Created Date(8) Creation Date
  Updated Date(8) Updated Date
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  TimeFormat VarChar(1) Time Template default=0 [0=Default, 1=24H, 2=12H]
  DateFormat VarChar(1) Date Template default=0 [0=Default, 1=DD/MM/YY, 2=DD/MM/CCYY, 3=MM/DD/YY, 4=MM/DD/CCYY, 5=CCYY/MM/DD, 6=DD/Month/YYYY]
  DateSep VarChar(1) Date Separator
  DecSep VarChar(1) Decimal Separator
  ThousSep VarChar(1) Thousands Separator
  Printer nVarChar(100) Printer
  NumLayPage Int(11) Number of Layout Pages
  NumCopy Int(11) Number of Copies default=1
  GbiSupport VarChar(1) GBI settings supported default=N [Y=Yes, N=No]
  Use1stPrtr VarChar(1) Use 1st page printer default=N [Y=Yes, N=No]
  Prtr1st nVarChar(100) Printer for First Page
  Shading VarChar(1) Print item backgrounds default=Y [Y=Yes, N=No]
  ForceExpXX VarChar(1) Force Export XX Report default=N [Y=Yes, N=No]
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  UseSysPref VarChar(1) Use System Preference default=Y [Y=Yes, N=No]

# EBCFG - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(50)
  LnscpId nVarChar(50)
  Company nVarChar(254)
  DefltRecvr Int(11)

# EBK1 - E-Books - Rows
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) E-Books Abs. Entry ->OEBK
  LineNum Int(11) Line Number
  NetValue Num(19,6) Net Value
  VatCatgory Int(11) VAT Category
  VatAmount Num(19,6) VAT Amount
  WithheldAm Num(19,6) Withheld Amount
  WhPrctCat Int(11) Withheld Percent Category
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  LogInstanc Int(11) Log Instance default=0

# EBUSR - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: B1Company
Fields (name type(len) description [values] ->parent table):
  B1Company nVarChar(100) B1 Company DB name
  B1User nVarChar(30) B1 user name (from OUSR)
  Pwd Text(16) encrypted password
  Pwd2 nVarChar(254) encrypted password (backup)

# ECLGF - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id, FileName
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(100) Transaction Id
  FileName nVarChar(254) The configuration file name
  FileHash nVarChar(100) The file hash code
  XmlFile Text(16) The file saved as Xml

# ECLGT - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id, TableName, TableId, CfgCol
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(100) transaction id
  TableName nVarChar(50) db table name
  TableId nVarChar(100) id field within db table
  CfgCol nVarChar(50) column within db table
  OldValue nVarChar(254)
  NewValue nVarChar(254)

# ECLOG - 
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(100)
  TimeStamp Date(8)

# EESUB - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EventType, Processor, ReturnAddr, ReceiverId, SenderId
Fields (name type(len) description [values] ->parent table):
  EventType nVarChar(30)
  Processor nVarChar(60)
  ReceiverId nVarChar(50)
  ReturnAddr nVarChar(254)
  SenderId nVarChar(50)
  FilterName nVarChar(60)
  FilterVal nVarChar(60)

# ELCFG - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id nVarChar(50)
  Name nVarChar(100)
  Type nVarChar(10)
  FaultAddr nVarChar(254)

# EMERR - 
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Identity(11) Error ID
  QueueType nVarChar(30) Queue type
  IDInQueue nVarChar(60) Message ID in the queue
  ErrCode nVarChar(60) Error code
  Severity nVarChar(10) Error severity
  ErrMessage nVarChar(254) Error message
  Member nVarChar(60) Error accessed member
  ExcType nVarChar(160) Exception type
  ExcString Text(16) Exception string

# EMIDS - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SequenceID, DispatchID
Fields (name type(len) description [values] ->parent table):
  SequenceID nVarChar(60) Event Sequence ID
  ProcessID nVarChar(60) Processed message ID
  DispatchID nVarChar(60) Dispached message ID

# EMMSG - 
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(60) Message ID
  Service nVarChar(160) Service
  Operation nVarChar(60) Operation
  Sender nVarChar(50) Sender ID
  Receiver nVarChar(50) Receiver ID
  InOut nVarChar(10) Incoming outgoing indicator
  BOType nVarChar(100) Business object type
  BOID nVarChar(30) Business object ID
  SboBoType nVarChar(100) Business one object type
  SboBoID nVarChar(30) Business one object ID

# EMSTT - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MessageID, Timestamp, Status
Fields (name type(len) description [values] ->parent table):
  MessageID nVarChar(60) Message ID
  Timestamp Date(8) Timestamp
  Status nVarChar(30) Status
  ErrorID Int(11) Error ID

# EPASM - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AsmName
Fields (name type(len) description [values] ->parent table):
  AsmName nVarChar(100) plugin assembly name
  PkgName nVarChar(50) FK to the EPPKG table
  AsmType nVarChar(20) Ttypes contained in assembly default=All [Messages=Only IMessage contained in the assembly, Processors=Only IMessageProcessor contained in the assembly, All=All types are in the assembly]

# EPOPR - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrvId, OprName
Fields (name type(len) description [values] ->parent table):
  SrvId Int(11) FK to EPSRV table
  OprName nVarChar(60) name of service operation
  SyncMode nVarChar(20) synch or a-sync mode of opr
  PrmMsgType nVarChar(60) operation parameter type
  PrcId nVarChar(60) FK to EPPRC table
  RetMsgType nVarChar(60) operation returned type
  ParamName nVarChar(60) Parameter name

# EPPKG - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PkgName
Fields (name type(len) description [values] ->parent table):
  PkgName nVarChar(50) Name of the plugin package
  PartnerId nVarChar(50) Id of the plugin's partner
  PkgVersion nVarChar(30) version of package installed

# EPPRC - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrcId
Fields (name type(len) description [values] ->parent table):
  PrcId nVarChar(60) Plugin processor id
  AsmName nVarChar(100) FK to EPASM table
  PrcType nVarChar(160) the type name of the processor
  OutSerName nVarChar(160) default service
  OutOprName nVarChar(60) default service operation

# EPSRV - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
  IX_SERVICE U: SrvName, Namespace
  IX_ADDRESS U: SrvAddress
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) auto generated id
  PkgName nVarChar(50) FK to EPPKG table
  SrvName nVarChar(60) thee name of the service
  Namespace nVarChar(100) namespace of service in code
  SrvAddress nVarChar(254) the prefix url of the service
  InOut nVarChar(10) Service direction

# FLR1 - Filter Lines
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, ColName
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Foreign Key
  LineNum Int(11) Line Number
  ColName nVarChar(10) Column Name
  CompValue nVarChar(254) Compare Value
  CompOper nVarChar(2) Compare Operator default== [===, >=>, <</td>=<</td>, >==>=, <==<=, !==!=]

# FND1 - Folio Numbering - Document Series
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, Series
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFND
  Series Int(11) Series ID ->OFNS

# FNS1 - Folio Numbering - Voided Series
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Series, FolNumFrom
  To U: Series, FolNumTo
Fields (name type(len) description [values] ->parent table):
  Series Int(11) Series ID ->OFNS
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  Reason nVarChar(100) Reason For Number Skipping

# FORM - FORM resource
Module: General | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, ResCode, RevCode
  NUM U: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Name nVarChar(64) Form name
  Num Int(11) Form number
  Type Int(11) Form type default=0 [0=Resize Document, 1=Dialog Box, 3=No Title Document, 4=Fixed Document, 5=Resize No Title Document, 6=Toolbar, 7=Fixed No Minimize]
  CloseBox VarChar(1) Close box default=1 [0=No, 1=Yes]
  DfltButton Int(11) Default button default=0
  _Top Int(11) Top
  _Bottom Int(11) Bottom
  _Left Int(11) Left
  _Right Int(11) Right
  MaxUnique Int(11) Max Unique
  RobjCode Int(11) ImpExp Obj Code default=0
  HelpCntxt nVarChar(32) Help Context
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  UseBoBind VarChar(1) Use BO Binding default=N [Y=Yes, N=No]

# HFC1 - Hide Function Configuration - Rows
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FuncID Int(11) Function ID ->OHFC
  formNum nVarChar(128) Form Number
  ItemUID nVarChar(128) Item UID
  ColUID nVarChar(128) Column UID
  HideVal nVarChar(20) Hide Valid Value
  AltVal nVarChar(20) Alternative Valid Value
  PanelID Int(6) Hide Item by Panel
  ActionType Int(6) Hide Item Action Type default=0 [0=Hide Item, 1=Hide Column, 2=Hide Item's Valid Value, 3=Hide Panel, 4=Hide Column's Valid Value]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# HFC2 - Hide Function Configuration - Rows
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FuncID Int(11) Function ID ->OHFC
  MainMenu Int(11) Main Menu ID
  MovMenuTo Int(11) Target Postion Menu Move
  ActionType Int(6) Action Type default=0 [0=Hide Menu, 1=Move Menu, 2=Hide Pop-Up Menu]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# HMM1 - Child Table of OHMM
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  UNIQUEVIEW U: ViewName
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OHMM
  LineNum Int(11) Child No.
  ViewType VarChar(1) View Type [A=Attribute View, C=Calculation View, Y=Analytic View, P=Procedure]
  ViewName nVarChar(100) View Name
  MenuDesc nVarChar(254) Menu Description
  MenuEnable VarChar(1) Menu Enable [Y=Yes, N=No]
  IAEnable VarChar(1) Interactive Analysis Enable default=Y [Y=Yes, N=No]
  SLEnable VarChar(1) Enable Service Layer [Y=Yes, N=No]
  SLExpose VarChar(1) Expose Service Layer [Y=Yes, N=No]

# HMM2 - Child Table of OHHM
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OHMM
  LineNum Int(11) Child No.
  VerType VarChar(1) Version Type [H=SAP HANA Version, A=SAP Business One Analytics Powered by HANA Version, B=SAP Business One Version]
  Ver nVarChar(100) Version

# HMM3 - OHMM Child Table
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OHMM
  LineNum Int(11) Line Number
  LangCode nVarChar(8) Language Code
  LangDesc nVarChar(50) Language Description

# IDX1 - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  COLUMN U: fatherId, columnId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36)
  fatherId nVarChar(36)
  columnId nVarChar(36)
  lineNum Int(11)

# IER1 - India E-Billing Report - Lines
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEbtry, EDocEntry
Fields (name type(len) description [values] ->parent table):
  AbsEbtry Int(11) Internal Number ->OIER
  EDocEntry Int(11) Internal Number of ECM2

# IMGDT - User Delete Group Log Time
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  Owner nVarChar(25) Message Owner
  GrpId Int(11) Group Id
  Time Date(8) Time

# IMGLG - Group Message Log
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  From nVarChar(25) Message Sender
  GrpId Int(11) Group Id
  Msg Text(16) Message Content
  Time Date(8) Time
  Nty VarChar(1) Is Notification default=N [Y=Yes, N=No]

# IMGP1 - Group User
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  GrpId Int(11) Group Id
  UsrCode nVarChar(25) User Code

# IMGRP - Group Master Data
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Group Id
  GrpName nVarChar(254) Group Name
  CrtTime Date(8) Create Time

# IMLTM - Departure Time
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  UsrCode nVarChar(25) User Code
  Peer nVarChar(25) Peer
  GrpId Int(11) Group Id
  DptTime Date(8) Departure Time

# IMPLG - Private Message Log
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  Owner nVarChar(25) Message Owner
  From nVarChar(25) Message Sender
  To nVarChar(25) Message Receiver
  Msg Text(16) Message Content
  Time Date(8) Time

# IMQSG - Question Suggestions
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) Internal Number
  Content nVarChar(254) Suggestion Content
  Weight Int(11) Suggestion Weight
  Time Date(8) Time
  Owner nVarChar(25) Owner of Suggestion
  Language Int(11) Language of Suggestion default=3

# ITEM - Item Resource
Module: General | 71 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, Num, ResCode, RevCode
  STRING: StrIndex
  UNIQUE_ID U: Name, UniqueID
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation Date
  Updated Date(8) Update Date
  Name nVarChar(64) Form Name
  Num Int(11) Item Number
  ItemType Int(11) Item Type [4=Button, 121=Check box, 114=Edit popup, 16=Edit text, 118=Extended edit, 99=Folder, 101=FwdBck button, 123=Graph, 124=Icon, 116=Link button, 127=Grid, 120=Media, 103=Multi page, 115=Pane button, 104=Pane popup, 117=Picture, 98=Pipe, 125=Popup, 119=Preview, 112=Progress, 122=Radio button, 100=Rectangle, 113=Select popup, 8=Static text, 102=ActiveX, 0=User item, 129=Button Combo]
  Enabled VarChar(1) Enabled default=1 [0=No, 1=Yes]
  _Top Int(11) Top
  _Bottom Int(11) Bottom
  _Left Int(11) Left
  _Right Int(11) Right
  Font Int(11) Font Number
  FontSize Int(11) Font Size
  Attributes Int(11) Attributes
  Style Int(11) Style
  Mode Int(11) Mode
  VarNum Int(11) Variable Number
  AttrVar Int(11) Attribute Variable
  NewLineVar Int(11) New Line Variable
  ProcVar Int(11) Proc Variable
  LinkVar Int(11) Link Variable
  DragVar Int(11) Drag Variable
  FileCode nVarChar(20) Table Name
  FieldNum nVarChar(10) Field Alias
  Editable VarChar(1) Editable default=1 [0=No, 1=Yes]
  Invisible VarChar(1) Invisible default=0 [0=No, 1=Yes]
  SuppressZe VarChar(1) Suppress Zeros default=0 [0=No, 1=Yes]
  DfltButton VarChar(1) Default Button default=0 [0=No, 1=Yes]
  DataRequir VarChar(1) Data Required default=0 [0=No, 1=Yes]
  ForceUpper VarChar(1) Force Upper default=0 [0=No, 1=Yes]
  RightJust VarChar(1) Right Justified default=1 [0=No, 1=Yes, 2=Language dependant, 3=Oppos Language]
  UserType VarChar(1) Data Binding Type default=0 [0=Data, 1=User Variable, 2=Multiple Data Type]
  ShowType VarChar(1) Show type default=0 [0=Value + Description, 1=Value only, 2=Description only]
  DispDecr VarChar(1) Display Description default=0 [0=No, 1=Yes]
  TabOrder Int(11) TAB Order
  LinkTo Int(11) Link to Item
  DragEntity Int(11) Drag Entity
  FromPane Int(11) From Pane
  ToPane Int(11) To Pane
  Class Int(11) Class
  StrIndex Int(11) String Index default=0
  HkeyIndex Int(11) Hotkey Index
  DescIndex Int(11) Description Index default=0
  FrameRed Int(11) Frame Red
  FrameGreen Int(11) Frame Green
  FrameBlue Int(11) Frame Blue
  BodyRed Int(11) Body Red
  BodyGreen Int(11) Body Green
  BodyBlue Int(11) Body Blue
  TextRed Int(11) Text Red
  TextGreen Int(11) Text Green
  TextBlue Int(11) Text Blue
  ThumbRed Int(11) Thumb Red
  ThumbGreen Int(11) Thumb Green
  ThumbBlue Int(11) Thumb Blue
  TxtFgRed Int(11) Text Foreground Red
  TxtFgGreen Int(11) Text Foreground Green
  TxtFgBlue Int(11) Text Foreground blue
  TxtBgRed Int(11) Text Background Red
  TxtBgGreen Int(11) Text Background Green
  TxtBgBlue Int(11) Text Background Blue
  UniqueID nVarChar(10) Unique ID
  ItemString nVarChar(254) Item String
  ItemDesc nVarChar(254) Item Description
  HotkeyPos Int(11) Hotkey Position
  WrapText VarChar(1) Wrap Text default=0 [0=No, 1=Yes]
  UsrSgnStr Int(11) User Sign For String Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  FontName nVarChar(32) Font Name
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  BindObjId Int(11) Bind Object Id default=-1

# ITMR - 
Module: General | 102 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocType, Local, Numerator, Language, ApplID, ResCode, RevCode
  TP_LC_NM_L: DocType, Local, Numerator, Language
  TYP_LOC_NM: DocType, Local, Numerator
  TYPE_LOC: DocType, Local
  TYPE: DocType
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Report
  ItemId Int(6) Item ID
  Container Int(6) Parent Type
  Type Int(6) Type [1=Page header, 2=Start of report, 3=Repetitive area header, 4=Repetitive area, 5=Repetitive area footer, 6=End of report, 7=Page footer, 10=Text field, 11=Picture field, 12=User field]
  VISIBLE VarChar(1) Visible default=1 [1=Yes, 0=No]
  SupZeros VarChar(1) Suppress Zeros default=0 [1=Yes, 0=No]
  ItemLeft Int(6) Left Item
  ItemTop Int(6) Top
  Width Int(6) Width
  Height Int(6) Height
  LMargin Int(6) Left Margin default=0
  RMargin Int(6) Right Margin default=0
  TMargin Int(6) Top Margin default=0
  BMargin Int(6) Bottom Margin default=0
  LeftLine Int(6) Left Border Line Thickness default=0
  RightLine Int(6) Right Border Line Thickness default=0
  TopLine Int(6) Top Border Line Thickness default=0
  BottomLine Int(6) Bottom Border Line Thickness default=0
  Shadow Int(6) Shadow Thickness default=0
  BGRed Int(11) Background - Red default=65535
  BGGreen Int(11) Background - Green default=65535
  BGBlue Int(11) Background - Blue default=65535
  FGRed Int(11) Text - Red default=0
  FGGreen Int(11) Text - Green default=0
  FGBlue Int(11) Text - Blue default=0
  MrkrRed Int(11) Bold - Red default=65535
  MrkrGreen Int(11) Bold - Green default=65535
  MrkrBlue Int(11) Bold - Blue default=65535
  BrdrRed Int(11) Border - Red default=0
  BrdrGreen Int(11) Border - Green default=0
  BrdrBlue Int(11) Border - Blue default=0
  FromPane Int(6) From Area default=0
  ToPane Int(6) To Area default=0
  ItemGroup Int(6) Group No. default=0
  FontName nVarChar(50) Font Name default=Arial
  FontSize Int(6) Font Size default=12
  TextStyle Int(11) Text Style
  Justific VarChar(1) Horizontal Justification default=2 [1=Right, 2=Left, 3=Center, 4=Language Dependent]
  WRAP VarChar(1) Segment default=1 [0=Allow overflow, 1=Fit to cell, 2=Devide to lines]
  PictSize VarChar(1) Picture Size default=1 [0=Original size, 1=Size of box, 2=Adjust to box, 3=Adjust to box height, 4=Adjust to box width]
  DataSource VarChar(1) Data Source default=1 [1=Static, 2=Var, 3=Data, 4=Calculation]
  ItemStr Text(16) String
  VarNum Int(6) Variable No.
  FileName nVarChar(20) File Name
  FieldNum nVarChar(10) Field No.
  ShowDescr VarChar(1) Display Description default=0 [1=Yes, 0=No]
  CalcType nVarChar(2) Calculation Type default=1 [0=Formula, 1=Page number, 17=Total Pages, 2=Date, 3=Time, 4=Column total, 5=Column average, 6=General row no., 7=Group row no., 8=Sort field name, 9=Sort field content, 10=Continue, 11=Continued on next page, 12=Generation message, 13=Column summary for page, 14=Column average for page, 15=Column summary for report, 16=Column average for report, -1=[new formula String]]
  ChangFlags Int(11) Changeable
  ApplID Int(6) Item No.
  CalcCol Int(6) Calculation Column
  YJustific VarChar(1) Vertical Alignment default=3 [1=Top, 2=Bottom, 3=Center]
  SortLevel Int(6) Sort Level default=0
  RevOrder VarChar(1) Reverse Sort default=0 [1=Descending, 0=Ascending]
  SortType VarChar(1) Sort Type default=0 [0=Alpha, 1=Numeric, 2=Money, 3=Date]
  IsUnique VarChar(1) Unique default=0 [1=Yes, 0=No]
  IsGroup VarChar(1) Set as Group default=0 [1=Yes, 0=No]
  NewPage VarChar(1) New Page default=0 [1=Yes, 0=No]
  BarCode VarChar(1) Print as Barcode default=0 [1=Yes, 0=No]
  Condition Text(16) Condition
  LinkTo Int(6) Link to Item default=0
  Operator1 Int(6) Operator 1
  Operator2 Int(6) Operator 2
  Operation Int(6) Operation default=0 [0=, 1=+, 2=-, 3=x, 4=/, 5=%, 17=Left, 18=Right, 19=Round, 6=$Concat, 7=$Right, 8=$Left, 9=$Sentence, 16=$Len, 20=$Currency, 21=$Number, 10=Less, 11=LessEq, 12=Equally, 13=Not eq, 14=GrEq, 15=Greater]
  BCStandard Int(6) Barcode Standard default=0 [0=EAN-13, 1=Code 39, 2=Code 128]
  SumInWords VarChar(1) Display Total as a Word default=0 [1=Yes, 0=No]
  ExcFonting VarChar(1) Block Font Change default=0 [1=Yes, 0=No]
  StrIndex Int(11) String Index default=0
  ContIndex Int(6) Container Index default=0
  ItemIndex Int(6) Item Index default=0
  StrLength Int(6) String Length
  StrFiller VarChar(1) String Filler
  RelatedTo Int(6) Related to Item default=0
  NextSeg Int(6) Next Segment Item Num default=0
  HightAdjst VarChar(1) Height Adjustments default=N [Y=Yes, N=No]
  DupRpttAre VarChar(1) Duplicate Repeatative Area default=N [Y=Yes, N=No]
  LnsRpttAre Int(11) Num Lines In Repeatative Area default=0
  RptDupDist Int(11) Distanse To Rptt Dup (pixels) default=0
  ItemDesc nVarChar(50) Item Description
  ExportXml VarChar(1) Export to xml default=Y [Y=Yes, N=No]
  DocType nVarChar(4) Document Type
  Local nVarChar(2) Localization
  Numerator Int(6) Numerator
  Language Int(6) Language
  Created Date(8) Creation Date
  Updated Date(8) Updated Date
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  IsRef VarChar(1) Is the item refered by another default=N [Y=Yes, N=No]
  FieldId nVarChar(20) Field Identifier
  FGEnabled VarChar(1) Grid Enabled default=Y [Y=Yes, N=No]
  BGEnabled VarChar(1) Background Enabled default=Y [Y=Yes, N=No]
  MKEnabled VarChar(1) Highlight Enabled default=Y [Y=Yes, N=No]
  BDEnabled VarChar(1) Frame Enabled default=Y [Y=Yes, N=No]
  HidEmpRptt VarChar(1) Hide Empty Area default=N [Y=Yes, N=No]
  RpttFtrAll VarChar(1) Display Rep. Footer on All default=N [Y=Yes, N=No]
  GbiDataTyp Int(6) Data Type default=0 [0=, 1=C n, 2=C.. n, 3=I.. n, 4=D w.d]
  GbiDataLen nVarChar(6) Data Length
  PageBreak Int(6) Page Break default=0 [0=None, 1=Before Area, 2=After Area]
  IsLogo VarChar(1) Is Logo default=N [Y=Yes, N=No]
  VarDefName nVarChar(50) Variable Definition Name
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# IWR1 - India E-Way Bill Report - Lines
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEbtry, EDocEntry
Fields (name type(len) description [values] ->parent table):
  AbsEbtry Int(11) Internal Number ->OIWR
  EDocEntry Int(11) Internal Number of ECM2

# KPI1 - Key Performance Indicator Field
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  KPIEntry Int(11) KPI Number
  Type Int(11) KPI Field Type
  FieldName nVarChar(250) KPI Field Name
  Method nVarChar(250) Aggregation Method
  DbType nVarChar(250) Database Type
  DefValue nVarChar(250) Default Value

# KPI2 - Key Performance Indicator Scope
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  KPIEntry Int(11) KPI Number
  Type nVarChar(250) KPI Scope Type
  From Num(19,6) From Value
  To Num(19,6) To Value
  Color nVarChar(250) Color

# KPI3 - Key Performance Indicator Parameter or Filter
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  KPIEntry Int(11) KPI Number
  Type nVarChar(20) Type
  FldName nVarChar(250) Field Name
  FldMethod nVarChar(250) Field Method
  Operator nVarChar(250) Operator
  DbType nVarChar(250) Database Type
  SqlType Int(11) SQL Type
  FromValue nVarChar(250) From Value
  ToValue nVarChar(250) To Value
  DftValue nVarChar(250) Default Value
  ParamType nVarChar(20) Parameter Type
  UdqPh nVarChar(50) UDQ Parameter's Placeholder
  UdqOp nVarChar(20) UDQ Parameter's Operator

# KPI4 - Key Performance Indicator Discrete Value
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FltEntry Int(11) Parameter Or Filter Number
  Value nVarChar(50) Discrete Value
  Desc nVarChar(250) Discrete Value Description

# KPI5 - Key Performance Indicator Formula's Variable
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  KPIEntry Int(11) KPI Number
  CalcEntry Int(11) Calculation KPI Number
  VarName nVarChar(250) Variable Name

# KPS1 - KPI Set Array 1
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: KpsCode, LineNum
  NAME U: KpsCode, KpiName
Fields (name type(len) description [values] ->parent table):
  KpsCode nVarChar(15) KPI Set Code
  LineNum Int(11) KPI Line Number
  KpiName nVarChar(100) KPI Name
  KpiValue1 Num(19,6) KPI Value 1
  KpiValue2 Num(19,6) KPI Value 2
  KpiValue3 Num(19,6) KPI Value 3
  KpiValue4 Num(19,6) KPI Value 4
  KpiValue5 Num(19,6) KPI Value 5
  KpiValue6 Num(19,6) KPI Value 6
  KpiValue7 Num(19,6) KPI Value 7
  KpiValue8 Num(19,6) KPI Value 8
  KpiValue9 Num(19,6) KPI Value 9
  KpiValue10 Num(19,6) KPI Value 10
  KpiValue11 Num(19,6) KPI Value 11
  KpiValue12 Num(19,6) KPI Value 12
  KpiValue13 Num(19,6) KPI Value 13
  KpiValue14 Num(19,6) KPI Value 14
  KpiValue15 Num(19,6) KPI Value 15
  KpiValue16 Num(19,6) KPI Value 16
  KpiValue17 Num(19,6) KPI Value 17
  KpiValue18 Num(19,6) KPI Value 18
  KpiValue19 Num(19,6) KPI Value 19
  KpiValue20 Num(19,6) KPI Value 20
  KpiValue21 Num(19,6) KPI Value 21
  KpiValue22 Num(19,6) KPI Value 22
  KpiValue23 Num(19,6) KPI Value 23
  KpiValue24 Num(19,6) KPI Value 24
  KpiValue25 Num(19,6) KPI Value 25
  KpiValue26 Num(19,6) KPI Value 26
  KpiValue27 Num(19,6) KPI Value 27
  KpiValue28 Num(19,6) KPI Value 28
  KpiValue29 Num(19,6) KPI Value 29
  KpiValue30 Num(19,6) KPI Value 30

# LCL1 - Localization languages
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LoclKey, Language
Fields (name type(len) description [values] ->parent table):
  LoclKey Int(11) Locl Key
  Language Int(11) Language

# LGL1 - Legal Data - Rows
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineSeq
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OLGL
  LineSeq Int(11) Line Sequence
  LineType VarChar(1) Line Type default=R [T=Document Total, R=Tax Per Line, V=Total Tax]
  TaxCode nVarChar(8) Tax Code
  TaxRate Num(19,6) Tax Rate
  Amount Num(19,6) Amount

# LOCL - Localizations Table
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LocCode
  ABS_KEY U: AbsKey
Fields (name type(len) description [values] ->parent table):
  AbsKey Int(11) Abs Key
  LocCode nVarChar(2) Localization Code
  Name nVarChar(32) Name
  DfltLang Int(11) Default Language
  B5IColctn nVarChar(20) B5I Collection Name
  IncldInExp VarChar(1) Include In export default=N [Y=Yes, N=No]
  IncEnInExp VarChar(1) Include English In Export default=Y [Y=Yes, N=No]

# LOG1 - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: absId, fldName
Fields (name type(len) description [values] ->parent table):
  absId Int(11)
  fldName nVarChar(10)
  valFrom nVarChar(254)
  valTo nVarChar(254)

# LTF1 - Legal Text Format Lines
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Format ID ->OLTF
  LineNum Int(11) Line No.
  LineCode nVarChar(30) Format Code ->OLTI

# MACT - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  ACTION U: fatherId, actName
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Unique Id
  fatherId nVarChar(36) MOBJ id
  lineNum Int(11) Line Number
  actName nVarChar(50) Action Name
  noteSid Int(11) Action Name String Index
  note nVarChar(254) Note
  actType VarChar(1) Action Type

# MCFL - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  COLUMN U: fatherId, columnId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36)
  fatherId nVarChar(36)
  lineNum Int(11)
  columnId nVarChar(36)

# MCOL - 
Module: General | 25 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  COL_NAME: fatherId, colName
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Object Id
  lineNum Int(11) Line Number
  colName nVarChar(50) Column Name
  colType VarChar(1) Column Type
  colSize Int(11) Column Size
  linkObjId nVarChar(36) Link to Object Id
  note nVarChar(254) Note
  defaultVal nVarChar(254) Default Value
  editSize Int(11) Edit Size
  mandatory VarChar(1) Mandatory default=N [Y=Yes, N=No]
  editType VarChar(1) Edit Type
  rdOnlyAdd VarChar(1) Read Only for Add Mode
  rdOnlyUpd VarChar(1) Read Only for Update Mode
  supresZero VarChar(1) Supress Zero
  locale nVarChar(254) Localization
  onListEvt VarChar(1) On List Event
  onChgEvt VarChar(1) On Change Event
  noteSid Int(11) String Id
  width Int(11) Width
  noteList nVarChar(254) Listview Note
  noteLstSid Int(11) String id of list view note
  fieldType Int(11) Field Type
  diType VarChar(1) DI API Fields
  diBatType VarChar(1) DI Batch Mode Type

# MDKY - MetaData Tables DKeys
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, HKeyIndex, DKeyIndex, ResCode, RevCode
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(5) Table Name
  HKeyIndex Int(6) HKey Index
  DKeyIndex Int(6) DKey Index
  FieldName nVarChar(20) Field in Key
  Upper VarChar(1) Upper default=Y [Y=Yes, N=No]
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# MFLD - MetaData Tables Fields
Module: General | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, FieldIndex, ResCode, RevCode
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(5) Table Name
  FieldIndex Int(6) Field Index
  Name nVarChar(20) Field Name
  Alias nVarChar(10) Alias
  Descr nVarChar(250) Description
  Type VarChar(1) Type default=A [A=DB Alpha, M=DB Memo, N=DB Numeric, D=DB Date, B=DB Binary, I=DB Auto Key]
  Size Int(6) Size
  FieldType Int(6) Field Type Num
  Visible VarChar(1) Visible default=Y [Y=Yes, N=No]
  EditType VarChar(1) Edit Type
  EditSize Int(6) Edit Size
  RFile nVarChar(4) Related Table
  ColHeading nVarChar(30) Column Heading
  FrmHeading nVarChar(30) Form Heading
  GroupNum Int(6) Group Number default=0 [0=User, -1=System]
  DefaultVal nVarChar(254) Default Value
  DIStatus VarChar(1) DI Status default=E [N=Not added to DI, Y=Added as Read/Write, R=Added as Read Only, E=NOT DEFINED]
  Dirty VarChar(1) Dirty default=Y [Y=Yes, N=No]
  Flag1 VarChar(1) Flag1 default=N [Y=Yes, N=No]
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1
  AssGrp nVarChar(16) Association Group
  AssType nVarChar(2) Association Type default=-1 [-1=, OT=Object Type, O1=Object Key Seg. 1, O2=Object Key Seg. 2, O3=Object Key Seg. 3, O4=Object Key Seg. 4, O5=Object Key Seg. 5, O6=Object Key Seg. 6, AO=Array Offset, A1=Array Key 1, A2=Array Key 2, A3=Array Key 3]
  IsPersist VarChar(1) Is Field Persistant default=Y [Y=Yes, N=No]

# MHKY - MetaData Tables HKeys
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, HKeyIndex, ResCode, RevCode
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(5) Table Name
  HKeyIndex Int(6) HKey Index
  Name nVarChar(10) Key Name
  ViewOrder Int(6) View Order
  UniqueKey VarChar(1) Unique Key default=Y [Y=Yes, N=No]
  Ascend VarChar(1) Ascending default=Y [Y=Yes, N=No]
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# MIDX - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, idxName
  GUID U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36)
  fatherId nVarChar(36)
  idxName nVarChar(36)
  isUnique VarChar(1)

# MKEY - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  COLUMN U: fatherId, columnId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Unique Id
  fatherId nVarChar(36) Meta Object Guid
  columnId nVarChar(36) Column Id
  lineNum Int(11) Line Number
  fatheColId nVarChar(36) Father Column Id

# MLOG - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: absId
Fields (name type(len) description [values] ->parent table):
  absId Int(11)
  userCode nVarChar(20)
  ipAddress nVarChar(20)
  updateDate Date(8)
  tableName nVarChar(10)
  operation VarChar(1) [C=Create, U=Update, D=Remove]
  objGuid nVarChar(36)

# MLST - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
  COLUMN U: fatherId, columnId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36)
  fatherId nVarChar(36)
  lineNum Int(11)
  columnId nVarChar(36)

# MOBJ - 
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: guid
  TABLE_NAME U: tableName
  FA_OBJ_ID: fatheObjId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  tableName nVarChar(50) Table Name
  fatheObjId nVarChar(36) Father Object Id
  note nVarChar(254) Note
  popCol1 nVarChar(36) Popup Column 1
  objId Int(11) Internal Object Id
  objArrayId Int(11) Internal Object Array Number
  allowAdd VarChar(1) Allow Create
  allowUpd VarChar(1) Allow Update
  allowDel VarChar(1) Allow Remove
  noteSid Int(11)
  modeList VarChar(1) Listview Mode
  modeGet VarChar(1) Get by Key Mode
  isSystem VarChar(1) Is System Table

# MRV3 - Inventory Revaluation SNB
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BaseLine, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  BaseLine Int(11) Base Row Number
  LineNum Int(11) Row Number
  SNBNum nVarChar(36) Serial and Batch Number
  AdmisDate Date(8) Admission Date
  ExpiryDate Date(8) Expiration Date
  CurrCost Num(19,6) Current Cost
  NewCost Num(19,6) New Cost
  DebCred Num(19,6) Debit Credit Value
  SNBOpenQty Num(19,6) SNB Open Quantity
  RToStock Num(19,6) Reval. Amount Posted to Stock
  SnbSysNum Int(11) SNB System Number
  SnbAbsEnt Int(11) SNB Abs. Entry
  SnbQty Num(19,6) SNB Quantity
  SnbCostT Num(19,6) SNB Cost Total
  SnbLotNum nVarChar(36) SNB Lot Number
  SnbMfn nVarChar(36) SNB Manufacture Attribute

# MSG1 - [MSG1]
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogNum, UserCode
Fields (name type(len) description [values] ->parent table):
  LogNum Int(11) ??' ?????
  UserCode nVarChar(50) �?? ?????

# MTBL - MetaData Tables
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, ResCode, RevCode
Fields (name type(len) description [values] ->parent table):
  Name nVarChar(5) Table Name
  ViewOrder Int(6) View Order default=30 [-1=Invisible, 10=Administration, 20=Administration Plus, 30=Master Data, 40=Document Line, 50=Document, 60=Log File, 70=Payment Line, 80=Payments]
  Type Int(6) Table Type default=1 [1=User OM, 2=User, 3=System OM, 4=System]
  Descr nVarChar(254) Description
  Category Int(6) Category default=0
  SubCateg Int(6) Sub Category default=0
  Dirty VarChar(1) Dirty default=Y [Y=Yes, N=No]
  Created Date(8) Creation Date
  Updated Date(8) Update Date
  InfoCtgory Int(6) Information Category default=0
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# MUSR - 
Module: General | 1 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: userCode
Fields (name type(len) description [values] ->parent table):
  userCode nVarChar(20)

# MVAL - MetaData Tables Fields Vals
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, FieldIndex, ValIndex, ResCode, RevCode
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(5) Table Name
  FieldIndex Int(6) Field Index
  ValIndex Int(6) Val Index
  Value nVarChar(254) Value
  Descr nVarChar(254) Description
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  DiEnumCode Int(11) DI Enum Code
  DiEnItCode Int(11) DI Enum Item Code
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# NCP1 - New Cockpit Tile
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PageEntry Int(11) Page Number
  Type nVarChar(20) Type
  WidgetId Int(11) Widget ID
  Size nVarChar(10) Size default=1x1
  Index Int(11) Index default=0
  Settings Text(16) Settings

# NCP2 - New Cockpit Tile
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PageEntry, ObjectType, ObjectKey
Fields (name type(len) description [values] ->parent table):
  PageEntry Int(11) Page Number ->ONCP
  Type nVarChar(20) Type ->NCP1
  ObjectType Int(11) Object Type ->CDPM
  ObjectKey nVarChar(50) Object ID ->CDPM

# NFN5 - NF Skipped Numbers
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SeqCode, VisOrder
Fields (name type(len) description [values] ->parent table):
  SeqCode Int(6) Sequence Code
  NFeNoFrom Int(11) NF-e No. From default=0
  NFeNoTo Int(11) NF-e No. To default=0
  Year Int(6) Year
  Reason nVarChar(254) Reason for Number Skipping
  Reply nVarChar(50) Reply from the Authority
  Status VarChar(1) Status default=N [N=New, S=Sent, A=Approved, E=Error]
  VisOrder Int(6) Visual Order
  CreateDate Date(8) Creation Date
  CreateTime Int(11) Creation Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(11) Update Time
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

# OAGM - Arguments for Integration Framework
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number of Document
  ObjType nVarChar(20) Object Type
  XmlGen Text(16) XML File Generated
  XmlRet Text(16) XML File Returned
  Message nVarChar(254) Message

# OBBI - Brazil Beverage Indexer
Module: General | 5 columns | ObjType: 540000068
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  TBL_TM_GRP U: TableCode, BrandCode, GroupCode
Fields (name type(len) description [values] ->parent table):
  TableCode nVarChar(2) Beverage Table Code ->OBSI
  BrandCode Int(11) Beverage Commercial Brand Code ->OBNI
  GroupCode nVarChar(2) Beverage Group Code ->OBSI
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) ID

# OBFI - Brazil Fuel Indexer
Module: General | 5 columns | ObjType: 540000067
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(10) Fuel Code
  FGroupCode Int(11) Fuel Group Code
  Descr nVarChar(254) Description
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) ID

# OBNI - Brazil Numeric Indexer
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  IND_CODE_K U: IndexType, Code
Fields (name type(len) description [values] ->parent table):
  IndexType Int(11) Indexer Type
  Code Int(11) Code
  Descr nVarChar(254) Beverage Brand
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) ID

# OBOB - Business Object Brief
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId Int(11) Object ID
  TableName nVarChar(30) Table Name
  PrimaryKey nVarChar(30) Primary Key
  TitleField nVarChar(100) Title Field
  DescField nVarChar(100) Description Field
  DeviceType VarChar(1) Device Type default=D [D=Desktop, M=Mobile]
  UsedBy VarChar(1) The record is used by BO list/Quick Access/Both default=A [A=All, B=BO List, R=Recent Updates]

# OBOD - BIOD Master Data
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BIOD_ENTRY
  USERID: BIOD_UID
Fields (name type(len) description [values] ->parent table):
  BIOD_ENTRY Int(11) BIOD Key
  BIOD_UID Int(6) User ID
  BIOD_QID Int(11) Query Internal Key
  BIOD_QN nVarChar(100) Query Name
  BIOD_QLD Date(8) Last Upload Date
  BIOD_QLT Int(6) Last Upload Time

# OBOL - Business Object Link
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, ColumnName
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(30) Table Name
  ColumnName nVarChar(30) Column Name
  ItemUid Int(11) Form Item UID

# OBSJ - Backend scheduling job
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Job ID
  Type nVarChar(100) Job Type
  Desc nVarChar(100) Description
  Status VarChar(1) Status default=S [S=Scheduled, R=Running, E=Error, F=Finished, P=Pending, C=Creating]
  Schedule VarChar(1) Schedule Type default=O [O=Once]
  NextDate Date(8) Next Running Date
  NextTime Int(6) Next Running Time
  BFParams Text(16) Begin Function Parameters
  EFParams Text(16) End Function Parameters
  BFRetry Int(11) Begin Function Retry Times default=0
  EFRetry Int(11) End Function Retry Times default=0
  RunAs Int(6) Callback Run as User ->OUSR
  Message nVarChar(200) Status Message
  RunType VarChar(1) Run Type default=M [M=Manual, A=Automatic]

# OBTA - Brazil - Tax Adjustment
Module: General | 48 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NUM U: DocNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID
  Status VarChar(1) Status default=O [O=Open, C=Canceled]
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DocNum Int(11) Document Number
  DocRate Num(19,6) Document Rate
  TaxCat Int(11) Tax Category
  Type Int(6) Type default=1 [1=Referred Collection Document, 2=Other Obligations, Adjustments, and Information Originating from Fiscal Documents, 3=Adjustment of ICMS Appraisal, 4=Adjustment and Additional Information of ICMS Appraisal, 5=Adjustment of ICMS and Identification of Fiscal Documents, 6=ICMS Obligations to Pay or Paid - Own Operations, 7=Adjustment of ICMS-ST Appraisal, 8=Adjustment and Additional Information of ICMS-ST Appraisal, 9=Adjustment of ICMS-ST and Identification of Fiscal Documents, 10=ICMS-ST Obligations to Pay or Paid - Own Operations, 11=Adjustment of IPI Appraisal, 12=Adjustment of PIS Appraisal, 13=Adjustment of COFINS appraisal]
  Oper Int(6) Operation default=1 [1=Other Debits, 2=Chargeback of Debits, 3=Other Credits, 4=Credit Chargeback, 5=Tax Deductions Calculated]
  RefVisType Int(11) Referenced Document ID default=1 [1=A/R Invoices, 2=A/P Invoices, 3=A/R Credit Memos, 4=A/P Credit Memos, 5=Deliveries, 6=Goods Receipt PO, 7=A/R Reserve Invoices, 8=A/P Reserve Invoices, 9=External Document]
  RefObjType Int(11) Referenced Document Type [13=A/R Invoices, 18=A/P Invoices, 14=A/R Credit Memos, 19=A/P Credit Memos, 15=Deliveries, 20=Goods Receipt PO, -1=External Document]
  RefDocEnt Int(11) Referenced Document Entry
  RefDocNum Int(11) Referenced Document Number
  StateUf nVarChar(2) State - UF
  PostDate Date(8) Posting Date
  CodDa VarChar(1) Collection Document default=1 [1=GNRE, 2=Other Document]
  NumDa nVarChar(20) Document Number
  CodAut nVarChar(30) Bank Authentication
  VlDa Num(19,6) Total Value
  VlDaSc Num(19,6) Total Value SC
  DtVcto Date(8) Due Date
  DtPgto Date(8) Payment Date
  CodAj nVarChar(10) ICMS Code
  DescCompAj nVarChar(120) Remarks
  BcIcms Num(19,6) ICMS Base Amount
  BcIcmsSc Num(19,6) ICMS Base Amount SC
  AliqIcms Num(19,6) ICMS Rate
  VlIcms Num(19,6) ICMS Value
  VlIcmsSc Num(19,6) ICMS Value SC
  VlOutros Num(19,6) Other Values
  CodAjApur nVarChar(10) Adjustment Code
  NumProc nVarChar(10) Procedure Docket Number
  IndProc VarChar(1) Procedure Docket Indicator
  Ser nVarChar(3) Fiscal Document Serial
  Sub nVarChar(3) Fiscal Document Subserial
  NumDoc Int(11) Fiscal Document Number
  DtDoc Date(8) Fiscal Document Issue Date
  CodMod nVarChar(6) Model Document Number
  CodPart nVarChar(15) BP Code ->OCRD
  CodRec nVarChar(15) Revenue Code
  GLAcct nVarChar(15) G/L Account Code ->OACT
  ItemCode nVarChar(50) Item Code ->OITM
  BPLId Int(11) Branch ID ->OBPL
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Generation Time
  UpdateDate Date(8) Date of Update
  TransId Int(11) Transaction Number ->OJDT

# OBVL - Serial Numbers and Batch Valuation Log
Module: General | 36 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  ILM_ENT: ILMEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocEntry Int(11) Doc Abs. Entry
  DocLineNum Int(11) Doc Line Number
  DocType Int(11) Transact. Type default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 13=A/R Invoice, 15=Delivery, 16=Returns, 17=Sales Order, 18=A/P Invoice, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase Order, 23=Sales Quotation, 59=Goods Receipt, 67=Inventory Transfer, 69=Landed Costs, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment]
  ActionType Int(11) Action Type default=5 [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]
  AccumType Int(11) Accumulator Type default=0 [0=ACCUM_EMPTY, 1=ACCUM_ON_HAND, 2=ACCUM_COMMITTED, 3=ACCUM_ON_ORDER, 4=ACCUM_CONSIGNATION, 5=ACCUM_COUNTED]
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  CreateDate Date(8) Generation Date
  CreateTime Int(6) Generation Time
  ItemCode nVarChar(50) Item No.
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Batch Number
  MdAbsEntry Int(11) MD Abs. Entry
  TrValApply VarChar(1) Apply Transaction Value default=Y [Y=Yes, N=No]
  TransValue Num(19,6) Transaction Value
  InvValue Num(19,6) Inventory Value
  CogsValue Num(19,6) Cogs Value
  Quantity Num(19,6) Quantity
  OverlapQty Num(19,6) Overlap Quantity
  CogsQty Num(19,6) Cogs Quantity
  CalcPrice Num(19,6) Calculated Price
  PriceDiff Num(19,6) Price Difference
  InvDiff Num(19,6) Inventory Difference
  Balance Num(19,6) Batch Balance
  AccTotal Num(19,6) Total Accumulator
  AccQty Num(19,6) Quantity-In Accumulator
  AccNegQ Num(19,6) Quantity-Out Accumulator
  ILMEntry Int(11) ILM Entry
  ITLEntry Int(11) ITL Entry
  CostQty Num(19,6) Cost Quantity
  Cost Num(19,6) Cost
  BaseDocEn Int(11) Base Doc. Abs. Entry
  BaseLnNum Int(11) Base Doc. Line Number
  DeltaAccT Num(19,6) Delta Total Accumulator
  RowAction Int(11) Row Action Type [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]

# OCFN - Common Functions Widget
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  CockpitID Int(6) Cockpit ID

# OCIP - Configuration of Integration Packages
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(10) Package Code
  Name nVarChar(254) Package Name
  DsplID Int(11) Display Description ID
  IsEnable VarChar(1) Is Enabled

# OCLC - Change Logs Cleanup
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ClnpScn nVarChar(100) Cleanup Scenario Name
  ClnpDate Date(8) Cleanup Date
  UpTo Date(8) Clean Up Logs Until
  Rmrks nVarChar(254) Remarks
  CreateTS Int(11) Create Time - Incl. Secs
  UserSign Int(6) User Signature ->OUSR

# OCMF - Common Functions of Fiori-Style Cockpit
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserID, ItemIndex
  INDEX: ItemIndex
Fields (name type(len) description [values] ->parent table):
  UserID Int(6) User ID ->OUSR
  ItemIndex Int(11) Common Function Item Index
  MenuUID nVarChar(50) Menu UID
  GroupID Int(6) Authorization Group ID ->OUGR
  MenuType VarChar(1) Menu Type default=S [S=System Menu, O=Menu of User Defined Object, Q=Menu of User Defined Query, A=Menu added by UI API, N=Menu added by Unknown Source]
  CmfMenuId nVarChar(50) Common Function Menu ID

# OCMM - Communication Media
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: CommCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CommCode nVarChar(50) Communication Media Code
  CommDesc nVarChar(100) Communication Media Desc.

# OCPT - Cockpit Main Table
Module: General | 18 columns | ObjType: 1210000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code, UserSign
  NAME U: Name, UserSign
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code Int(6) Cockpit Code
  Name nVarChar(20) Name
  Descr nVarChar(100) Description
  IsDefault VarChar(1) Is Default default=N [Y=, N=]
  UserSign Int(6) User ID ->OUSR
  IsPublic VarChar(1) Public default=N [Y=, N=]
  Strategy nVarChar(20) Layout Strategy
  _Top Int(11) Client Top
  _Left Int(11) Client Left
  _Width Int(11) Client Width
  _Height Int(11) Client Height
  Date Date(8) Publication Date
  Time Int(6) Publication Time
  Mnfacturer nVarChar(50) Provider
  Pubby nVarChar(30) Published By
  Disabled VarChar(1) Disabled default=N [Y=, N=]
  Type VarChar(1) Type default=U [U=User, T=Template]

# OCUC - CUS Configuration
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) Abs. Entry
  Type Int(11) Type
  Param nVarChar(254) Parameter
  Value Text(16) Value

# OCUL - Customer Usage Statistics Log
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Identity(11) Internal Number
  StartRef Int(11) Session Start Reference
  EventType Int(11) Event Type
  DateTime nVarChar(20) Date Time

# ODAB - Dashboard
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: PackEntry, DashbdCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  PackEntry Int(11) Package Entry ->OWPK
  DashbdCode nVarChar(32) Dashboard Code
  DashbdName nVarChar(100) Dashboard Name
  DashbdPath nVarChar(254) Dashboard Path
  Note Text(16) Dashboard Description
  Status VarChar(1) Dashboard Status default=A [I=Inactive, A=Active]
  JobFlag VarChar(1) Use Schedule Job Flag default=N [Y=Yes, N=No]
  JobType VarChar(1) Schedule Job Type default=R [R=Real Time, P=Periodic]
  JobSetting nVarChar(100) Schedule Job Time Setting
  RenewDate Date(8) Latest Renew Date
  RenewTime Int(6) Latest Renew Time
  ProcName nVarChar(100) Procedure Name
  JobName nVarChar(100) Schedule Job Name

# ODAL - Link between dashboard and form
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  DashEntry Int(11) Dashboard Entry
  FormID nVarChar(250) Form ID
  MobDesc nVarChar(250) Mobile Description

# ODCC - Dashboard Cache Configuration
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs Entry
  Enable VarChar(1) Enable default=N [Y=, N=]
  Start Int(11) Start
  CronString nVarChar(254) Cron String
  UserSign Int(6) User Signature ->OUSR

# ODRC - G/L Account Determination Criteria - Resources
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DmcId
Fields (name type(len) description [values] ->parent table):
  DmcId Int(11) Determination ID
  DmcAlias nVarChar(100) Determination Alias
  Active VarChar(1) Determination Status default=N [Y=Yes, N=No]
  Priority Int(6) Determination Priority
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  AdvRulCol Int(6) Advanced Rules Column

# ODSL - Schedule Row Detail
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SCHD_LINE U: ObjType, DocEntry, DocLineNum, SchdLine
  DOCLINESLD: ObjType, DocEntry, DocLineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjType nVarChar(20) Object Type default=-1 [-1=, 13=A/R Reserve Invoice, 17=Sales Order, 18=A/P Reserve Invoice, 22=Purchase Order, 163=A/P Correction Reserve Invoice, 165=A/R Correction Reserve Invoice, 202=Production Order, 1250000001=Warehouse Transfer Request]
  DocEntry Int(11) Associated Doc. Entry
  DocLineNum Int(11) Associated Doc Row No.
  SchdLine Int(11) Schedule Row No.
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  CfmDate Date(8) Confirmation Date
  CfmQty Num(19,6) Confirmation Quantity
  FixedCfm VarChar(1) Fixed Confirmation Data default=N [Y=Yes, N=No]
  ReqQty Num(19,6) Required Quantity

# ODW1 - Default Open Documents
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, DocType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OODW
  DocType Int(11) Open Document Type

# OEBK - E-Books
Module: General | 27 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  UID U: UID
  MARK U: MARK
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) E-Books Abs. Entry
  MARK nVarChar(40) MARK
  CancelMARK nVarChar(40) Cancel MARK
  UID nVarChar(50) UID
  IssueVATID nVarChar(64) Issuer VAT Number
  CPVATID nVarChar(64) Counterpart VAT Number
  Series nVarChar(16) Series
  AA nVarChar(200) AA
  IssueDate Date(8) Issue Date
  InvoiceTyp nVarChar(100) Invoice Type
  Currency nVarChar(200) Currency
  TlNetVal Num(19,6) Total Net Value
  TlVatAmn Num(19,6) Total VAT Amount
  TlWheldAmn Num(19,6) Total Withheld Amount
  TlGrossVal Num(19,6) Total Gross Value
  LinkDocTyp Int(11) Linked Doc. Type [18=A/P Invoices, 19=A/P Credit Memos, 30=Journal Entries, 0=, -1=]
  LinkDocEnt Int(11) Linked Doc. Entry
  IsNegMark VarChar(1) Is Negative MARK default=N [N=No, Y=Yes]
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  SourceECM8 Int(11) LogNum of Source ECM8
  ObjType nVarChar(20) Object Type default=234003013 [234003013=E-Books Expense] ->ADP1
  UserSign2 Int(6) Updating User ->OUSR

# OEDT - EWB Document Type
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  DOC_TYPE U: TypeCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TypeCode nVarChar(3) EWB Document Type Code
  TypeName nVarChar(50) EWB Document Type Description

# OEST - EWB Sub-Type
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SUB_TYPE U: SubID
  SUPLY_TYPE: SuplyType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SubID Int(11) EWB Sub-Type Code
  SubType nVarChar(50) Sub supply type of e-way bill
  SuplyType VarChar(1) EWB Supply Type default=B [B=Both, I=Inward, O=Outward]

# OETM - EWB Transportation Mode
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  MODE_CODE U: ModeCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ModeCode Int(11) EWB Transportation Mode Code
  ModeName nVarChar(50) EWB Transportation Mode Name

# OEUT - EWB Unit
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  UNIT_CODE U: UnitCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  UnitCode nVarChar(3) EWB Unit Code
  UnitName nVarChar(30) EWB Unit Name

# OEVT - EWB Vehicle Type
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  VEHIC_TYPE U: TypeCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TypeCode VarChar(1) EWB Vehicle Type Code
  TypeName nVarChar(50) EWB Vehicle Type Description

# OFAI - Office 365 App Identity
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(254) ID
  APP_ID nVarChar(254) Office 365 App ID
  APP_PASS nVarChar(254) Office 365 App Password

# OFAT - Office 365 Authorization Token
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(254) ID
  USER_ID nVarChar(254) User ID
  OFUSERNAME nVarChar(254) Office User Name
  AUTH_TOKEN Text(16) Authorization Token
  ID_TOKEN Text(16) ID Token

# OFBT - Office 365 SAP Business One Template
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(254) ID
  NAME nVarChar(254) Name
  CONTENT Text(16) Content
  ISDEFAULT Int(6) Is Default
  BOTYPE nVarChar(254) BO Type
  DOCTYPE nVarChar(254) Doc Type
  TEMPFORMAT nVarChar(254) Template Format

# OFLR - Object Filter
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Key
  FilterName nVarChar(64) Filter Name
  UserSign Int(6) User Signature ->OUSR
  TableName nVarChar(5) Table Name
  VisOrder Int(6) Visible Order
  StatCol nVarChar(10) Statistics Column
  UnitCol nVarChar(10) Unit Column

# OFND - Folio Numbering Documents
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  OBJECT U: ObjectCode, DocSubtype
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(20) Document
  DocSubtype nVarChar(2) Subdocument default=-- [--=, DM=A/P Debit Memo, DN=A/R Debit Memo, IB=A/R Bill]

# OFNS - Folio Numbering - Series
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Series
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Series Int(11) Series ID
  Name nVarChar(100) Name
  PTICode nVarChar(5) POI Code ->OPTI
  FirstNum Int(11) First Number
  NextNum Int(11) Next Number
  LastNum Int(11) Last Number
  Letter VarChar(1) Letter [A=A, B=B, C=C, E=E, M=M, R=R, T=T, X=X, -=-]
  CAI nVarChar(14) CAI
  CAIDueDate Date(8) CAI Due Date
  Remarks nVarChar(100) Remarks
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]

# OFTA - Office 365 Template Action
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(254) ID
  BOTYPE nVarChar(254) BO Type
  DOCTYPE nVarChar(254) Doc Type
  TEMPFORMAT nVarChar(254) Template Format
  USER_ID nVarChar(254) User ID
  ACTIONTIME Date(8) Action Time
  ACTIONTYPE nVarChar(254) Action Type

# OFTP - Office 365 Doc Export Task Progress
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TASKID
Fields (name type(len) description [values] ->parent table):
  TASKID nVarChar(254) Task ID
  USER_ID nVarChar(254) User ID
  CURR Int(11) Current
  TOTAL Int(11) Total
  ERROR_CODE nVarChar(254) Error Code
  STATE nVarChar(254) State
  STARTTIME Date(8) Start Time
  FILE_NAME nVarChar(254) File Name
  RESULT nVarChar(254) Result
  ONETTOKEN Text(16) One Time Token
  TASKTYPE nVarChar(254) Task Type

# OFUS - Office 365 User Settings
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(254) ID
  USER_ID nVarChar(254) User ID
  FOLDERNAME Text(16) Office Folder Name Map
  LOCALE nVarChar(254) Locale
  PROFPHOTO Text(16) Profile Photo

# OGPA - Gross Profit Adjustment
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Name nVarChar(100) Gross Profit Adjustment Name
  CreateDate Date(8) Create Date
  UserSign Int(6) User Signature
  Status VarChar(1) Status [R=Saved Recommendations, S=Simulation, E=Executed, P=Saved Parameters]
  Remarks nVarChar(254) Description
  WizType VarChar(1) Wizard Type default=A [A=Gross Profit Adjustment Wizard, R=Production Cost Recalculation Wizard]
  nGPAdj Int(11) Number of Gross Profits Recalculated
  nPCAdj Int(11) Number of Product Costs Recalculated
  nGPFail Int(11) Number of Gross Profit Recalculations Failed
  nPCFail Int(11) Number of Failed Product Cost Recalculations
  nJECreate Int(11) Number of Journal Entries Created
  nMRVCreate Int(11) Number of MRV Created

# OGRS - G/L Account Advanced Rules for Resources
Module: General | 55 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PeriodCat nVarChar(10) Period Category
  FinancYear Date(8) Beginning of Financial Year
  Year Int(6) Financial Year
  PeriodName nVarChar(20) Period Name
  SubType VarChar(1) Sub-Period Type default=Y [Y=Year, Q=Quarters, M=Months, D=Days]
  PeriodNum Int(11) Number of Periods
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  ResCode nVarChar(50) Resource No. ->ORSC
  ResGrpCod Int(6) Resource Group ->ORSB
  WhsCode nVarChar(8) Warehouse Code
  BPGrpCod Int(6) BP Group
  LicTradNum nVarChar(32) Federal Tax ID default=!^| [!^|=All, !^|E=Empty, !^|F=Filled, Enter Tax ID=Enter Tax ID]
  ShipCountr nVarChar(3) Ship-to Country/Region
  ShipState nVarChar(3) Ship-To State
  Comments nVarChar(254) Remarks
  CreateDate Date(8) Creation Date
  RuleCode nVarChar(20) Advanced Rule Code
  GLMethod VarChar(1) Get G/L Account By default=A [A=General, W=Warehouse, C=Resource Group]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  ResRevAct nVarChar(15) Resource Revenue Account ->OACT
  ResExpAct nVarChar(15) Resource Expense Account ->OACT
  ResSaleAct nVarChar(15) Resource Sales Credit Account ->OACT
  ResPurAct nVarChar(15) Resource Purchase Credit Acct ->OACT
  ResNInvAct nVarChar(15) Resource Received Not Inv. Acct ->OACT
  ResStdExp1 nVarChar(15) Resource Std. Cost Expense 1 ->OACT
  ResStdExp2 nVarChar(15) Resource Std. Cost Expense 2 ->OACT
  ResStdExp3 nVarChar(15) Resource Std. Cost Expense 3 ->OACT
  ResStdExp4 nVarChar(15) Resource Std. Cost Expense 4 ->OACT
  ResStdExp5 nVarChar(15) Resource Std. Cost Expense 5 ->OACT
  ResStdExp6 nVarChar(15) Resource Std. Cost Expense 6 ->OACT
  ResStdExp7 nVarChar(15) Resource Std. Cost Expense 7 ->OACT
  ResStdExp8 nVarChar(15) Resource Std. Cost Expense 8 ->OACT
  ResStdExp9 nVarChar(15) Resource Std. Cost Expense 9 ->OACT
  ResStdEx10 nVarChar(15) Resource Std. Cost Expense 10 ->OACT
  ResWipAct nVarChar(15) Resource WIP Account ->OACT
  ResScrapAc nVarChar(15) Scrap Account ->OACT
  WipOffPlAc nVarChar(15) WIP Offset P&L Account ->OACT
  ResOffPlAc nVarChar(15) Resource Offset P&L Account ->OACT
  Active VarChar(1) Is Rule Active default=Y [Y=Yes, N=No]
  CmpPrivate VarChar(1) Company/Private default=A [A=All, C=Company, I=Private]
  VatGroup nVarChar(8) Tax Definition ->OVTG
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  Usage Int(11) Usage Code for Document ->OUSG

# OHFC - Hide Functions Configuration
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FuncName nVarChar(100) Function Name
  Hidden VarChar(1) Enabled [Y/N] default=Y [Y=Yes, N=No]
  Type nVarChar(6) Type default=0 [0=System, 1=User]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# OHMM - SAP HANA Model Management
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ModelAuth nVarChar(100) Model Author
  ModelName nVarChar(100) Model Name
  ModelVer nVarChar(100) Model Version
  Desc Text(16) Description
  Status VarChar(1) Status [I=Imported, D=Deployed, T=In Task]
  InfoFile Text(16) Info File
  UpdateBy Int(11) Last Updated User's Code
  ChangeBy nVarChar(100) Last Changed SAP HANA User
  CreateDate nVarChar(100) Created at Date
  CreateTime Int(11) Created at Time
  ChangeDate nVarChar(100) Changed at Date
  ChangeTime Int(11) Changed at Time
  TaskId Int(11) Task ID
  DeployDate Date(8) Deployment Date
  DeployTime Int(11) Deployment Time
  Language nVarChar(8) Deployment Language

# OIER - India E-Billing Report - Header
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEbtry
Fields (name type(len) description [values] ->parent table):
  AbsEbtry Int(11) Internal Number
  RootEcm2 Int(11) Internal Number of ECM2
  Status VarChar(1) Status of Report

# OIMD - Live Collaboration Data
Module: General | 1 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry

# OIRI - Input Service Distribution - Recipient Invoice
Module: General | 30 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  RefNo nVarChar(100) Reference No.
  RefEntry Int(11) Reference Entry
  RefDocDate Date(8) Reference Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(254) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# OIRR - Input Service Distribution - Recipient Credit Memo
Module: General | 30 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  RefNo nVarChar(100) Reference No.
  RefEntry Int(11) Reference Entry
  RefDocDate Date(8) Reference Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(254) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# OISC - Input Service Distribution - Credit Memo
Module: General | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  Revised VarChar(1) Revised default=N [Y=Yes, N=No]
  OrgRefNo nVarChar(100) Original Reference No.
  OrgRefEty Int(11) Original Reference Entry
  OrgDocDate Date(8) Original Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code default=0
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  ISDEntry Int(11) ISD Entry
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(254) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# OISD - Input Service Distribution
Module: General | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  SrcLctCode Int(11) Source Location Code
  SrcLctName nVarChar(100) Source Location Name
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  Revised VarChar(1) Revised default=N [Y=Yes, N=No]
  OrgRefNo nVarChar(100) Original Reference No.
  OrgRefEty Int(11) Original Reference Entry
  OrgDocDate Date(8) Original Document Date
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  DstPercent Num(19,6) Percent to Distribute
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# OISI - Input Service Distribution - Invoice
Module: General | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  Revised VarChar(1) Revised default=N [Y=Yes, N=No]
  OrgRefNo nVarChar(100) Original Reference No.
  OrgRefEty Int(11) Original Reference Entry
  OrgDocDate Date(8) Original Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code default=0
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  ISDEntry Int(11) ISD Entry
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(254) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number

# OIWR - India E-Way Bill Report - Header
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEbtry
Fields (name type(len) description [values] ->parent table):
  AbsEbtry Int(11) Internal Number
  RootEcm2 Int(11) Internal Number of ECM2
  Status VarChar(1) Status of Report

# OJSON - JSON Content Repository
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
  INDEX1 U: Type, Index1
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  Type VarChar(1) Type [F=Form Preference]
  Index1 nVarChar(254) User-Defined Indexes
  Content Text(16) JSON Content
  UserSign Int(6) User Signature ->OUSR

# OKPI - Key Performance Indicator Package
Module: General | 25 columns | ObjType: 1320000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(250) KPI Code
  Name nVarChar(250) KPI Name
  Desc nVarChar(254) Description
  ValueType nVarChar(200) Value Type
  ValueQid Int(11) Value Query Number
  ViewName nVarChar(250) Value View Name
  ViewCtg nVarChar(250) View Catalog
  ViewSyn nVarChar(250) View Synonym
  TrendType nVarChar(250) Trend Type
  TrendQid Int(11) Trend Query Number
  GoalValue Num(19,6) Goal Value
  GoalQid nVarChar(11) Goal Query Number
  GoalDesc nVarChar(250) Goal Description
  CalcFrml nVarChar(250) Calculation Formula
  Visible VarChar(1) Visible For Front End default=Y
  SBetter VarChar(1) Smaller Value is Better default=Y
  Author nVarChar(32) Creator
  Version nVarChar(13) Version
  CreateDate Date(8) Create Date
  CreateTime Int(6) Create Time
  IsSystem VarChar(1) Is System default=N
  MeasUnit nVarChar(50) Measuring Unit default=0
  RevSign VarChar(1) Reverse Sign default=N
  Unit nVarChar(250) Unit

# OKPS - KPI Set
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: KpsCode
Fields (name type(len) description [values] ->parent table):
  KpsCode nVarChar(15) KPI Set Code
  KpsName nVarChar(100) KPI Set Name
  KpsType VarChar(1) KPI Set Type default=S [S=Single, Q=Quarterly, M=Monthly, P=Multiple]
  FieldsNum Int(11) KPI Set Fields Number
  CreateDate Date(8) Create Date - History
  UserSign Int(6) Updating User - History ->OUSR

# OLCD - Live Collaboration Deletion Log
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DateUntil Date(8) Send Date
  UserSign Int(6) User Signature ->OUSR

# OLNK - Help Links
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LnkAddr Text(16) Link Address
  Descr nVarChar(100) Description
  Provider nVarChar(50) Provider

# OLTI - Legal Text Items
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineCode
Fields (name type(len) description [values] ->parent table):
  LineCode nVarChar(30) Format Code
  XMLPath nVarChar(150) XML Path

# ONCP - New Cockpit Table
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name, Owner
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) Name
  Owner Int(11) Owner ->OUSR
  GroupId Int(11) Group ID
  CreateDate Date(8) Create Date
  UpdateDate Date(8) Update Date
  IsPublic VarChar(1) Public default=N [Y=, N=]
  Pubby nVarChar(30) Published By
  PubDate Date(8) Publication Date
  Type VarChar(1) Type default=T [U=User, T=Template]
  Descr nVarChar(100) Description
  Date Date(8) Publication Date
  Time Int(6) Publication Time
  Mnfacturer nVarChar(50) Provider

# OODW - Open Documents Widget
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  CockpitID Int(6) Cockpit ID

# OPAC - PAC Companies
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PACCode
Fields (name type(len) description [values] ->parent table):
  PACCode nVarChar(16) PAC Code
  PACName nVarChar(100) PAC Name
  PublicKey Text(16) PAC Public Key
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  EDFCode Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI, 4=FPA, 5=MTD, 6=EWB, 7=PEPPOL, 8=HOI, 9=MYF, 10=EIS, 11=IIS, 12=IIS_ANNUAL]

# OPCM - POS/Cash Register
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  ID_CODE U: IdCode
  POC_CR U: PosCode, CrCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  IdCode nVarChar(50) Identification Code
  PosCode nVarChar(6) Point of Service Code
  PosDesc nVarChar(100) Point of Service Description
  CrCode nVarChar(20) Cash Register Code
  CrDesc nVarChar(100) Cash Register Description
  Remarks nVarChar(250) Remarks

# OPHA - Project Management Subproject
Module: General | 22 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  OWNER Int(11) Owner ->OHEM
  NAME nVarChar(254) Name
  START Date(8) Subproject Start Date
  FINISHED Num(19,6) Deduction - Percentage
  ParentID Int(11) Parent Subproject
  ProjectID Int(11) Project No. ->OPMG
  Code Int(11) Subproject No.
  TYP Int(11) Subproject Type ->PMC1
  CONTRIB Num(19,6) Subproject Contribution - Percentage
  STATUS VarChar(1) Status default=O [O=Open, C=Closed]
  END Date(8) Subproject End Date
  COST Num(19,6) Actual Cost
  PLANNED Num(19,6) Planned Cost
  Level Int(11) Depth of Subproject within the project
  DUEDATE Date(8) Due Date
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time

# OPMC - Project Management Configuration
Module: General | 1 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key

# OPMG - Project Management Document
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  OWNER Int(11) Owner ->OHEM
  NAME nVarChar(254) Project Name
  START Date(8) Project Start Date
  FINISHED Num(19,6) Deduction - Percentage
  DocNum Int(11) Document Number
  Series Int(11) Series
  TYP VarChar(1) Project Type default=E [E=External, I=Internal]
  CARDCODE nVarChar(15) BP Code ->OCRD
  CARDNAME nVarChar(100) BP Name
  CONTACT Int(11) Contact Person ->OCPR
  TERRITORY Int(11) Business Partner Territory ->OTER
  EMPLOYEE Int(11) Sales Employee default=-1 ->OSLP
  WithPhases VarChar(1) Project with Phases default=N [Y=Yes, N=No]
  STATUS VarChar(1) Status default=S [S=Started, P=Paused, T=Stopped, F=Finished, N=Canceled]
  DUEDATE Date(8) Due Date
  CLOSING Date(8) Closing Date
  FIPROJECT nVarChar(20) Financial Project ->OPRJ
  RISK VarChar(1) Risk Level default=L [L=Low, M=Medium, H=High]
  INDUSTRY Int(11) Industry Code ->OOND
  REASON Text(16) Comments
  Free_Text Text(16) Free Text
  BPLid Int(11) Business Place ID ->OBPL
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachments
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV

# OPMX - Payroll
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  UID U: Uid
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Total Num(19,6) Total
  Currency nVarChar(3) Currency ->OCRN
  Rate Num(19,6) Exchange Rate
  Uid nVarChar(100) UUID of payroll
  RFC nVarChar(20) RFC
  CreateDate Date(8) Creation Date
  FileDate Date(8) File Date
  FileName nVarChar(254) Imported File Name
  JVBatchNum Int(11) Journal Voucher Batch Number ->OBTF
  JVTransId Int(11) Journal Voucher Trans Number ->OBTF
  JETransId Int(11) Journal Entry Trans Number ->OJDT
  Type VarChar(1) Type default=P [P=Payroll, E=Expenses]

# OPRA - Payroll G/L accounts Setup
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CATE_CODE U: CateType, CateCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CateType VarChar(1) Category Type [P=Perception, D=Deduction, N=Payroll Payable, R=Rounding, O=Other Payments]
  CateCode nVarChar(8) Category Code
  Category nVarChar(254) Category of Payroll
  Account nVarChar(15) G/L Account ->OACT

# OPRI - Browser Access Printers
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(250) Printer Name
  UserID Int(6) User ID
  Desc nVarChar(254) Description
  Server nVarChar(254) Server
  Selected VarChar(1) Select Printer default=N
  DPrinter VarChar(1) Default Printer default=N

# OPST - Service Call Problem Subtype
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ProSubTyId
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  ProSubTyId Int(6) Problem Subtype ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# OPTI - Point of Issue
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(5) Code
  Desc nVarChar(100) Description
  Type VarChar(1) Type default=P [P=Domestic Printing, E=Domestic Electronic, F=Fiscal, X=Export Printing, T=Export Electronic]
  SOpDate Date(8) Start Operating Date
  EndOpDate Date(8) End Operating Date
  Remarks nVarChar(100) Remarks
  EDocExpFrm Int(11) Electronic Doc. Export Format
  BPLId Int(11) Branch ->OBPL
  EDocGenTyp VarChar(1) Electronic Doc. Generation Type [N=Not Relevant, G=Generate]

# ORCJ - Resource Capacity Log
Module: General | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
  RWDT: ResCode, WhsCode, CapDate, CapType
  BASE_DOC: BaseObjTyp, BaseAbsEnt, BaseLine
  OWNING_DOC: OwnObjTyp, OwnAbsEnt, OwnLine
Fields (name type(len) description [values] ->parent table):
  Id Int(11) Primary Key
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  CapDate Date(8) Capacity Date
  CapType VarChar(1) Type of Capacity Entry default=I [I=Internal, O=Ordered, C=Committed, U=Consumed]
  Capacity Num(19,6) Capacity
  SrcObjType Int(11) Source Object Type default=-1 [-1=, 202=Production Order, 60=Issue for Production, 59=Receipt from Production, 17=Sales Order, 15=Delivery, 13=A/R Invoice, -13=A/R Reserve Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 16=Returns, 22=Purchase Order, 20=Goods Receipt PO, 18=A/P Invoice, -18=A/P Reserve Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 21=Goods Return]
  SrcAbsEnt Int(11) Source Absolute Entry
  SrcLine Int(11) Source Line Number
  BaseObjTyp Int(11) Base Object Type default=-1 [-1=, 202=Production Order]
  BaseAbsEnt Int(11) Base Absolute Entry
  BaseLine Int(11) Base Line Number
  ActionType Int(6) Action Type default=-1 [-1=, 1=Production Order - Create, 2=Production Order - Close, 3=Production Order - Reschedule, 4=Production Order - Add Line, 5=Production Order - Delete Line, 6=Production Order - Update Line, 7=Issue for Production - Create, 8=Receipt from Production - Create, 9=Sales Order - Create, 10=Sales Order - Close, 11=Sales Order - Cancel, 12=Sales Order - Add Line, 13=Sales Order - Delete Line, 14=Sales Order - Update Line, 15=Delivery - Create, 16=Delivery - Close, 17=Delivery - Cancel, 18=A/R Invoice - Create, 19=A/R Invoice - Cancel, 20=A/R Credit Memo - Create, 21=A/R Credit Memo - Cancel, 22=Correction A/R Invoice - Create, 23=Correction A/R Invoice Reversal - Create, 24=Returns - Create, 25=Returns - Cancel, 26=Returns - Close, 27=Purchase Order - Create, 28=Purchase Order - Close, 29=Purchase Order - Cancel, 30=Purchase Order - Add Line, 31=Purchase Order - Delete Line, 32=Purchase Order - Update Line, 33=Goods Receipt PO - Create, 34=Goods Receipt PO - Close, 35=Goods Receipt PO - Cancel, 36=A/P Invoice - Create, 37=A/P Invoice - Cancel, 38=A/P Credit Memo - Create, 39=A/P Credit Memo - Cancel, 40=Correction A/P Invoice - Create, 41=Correction A/P Invoice Reversal - Create, 42=Goods Return - Create, 43=Goods Return - Cancel, 44=Goods Return - Close, 45=A/R Invoice - Update, 46=A/P Invoice - Update, 47=A/R Reserve Invoice - Create, 48=A/R Reserve Invoice - Update, 49=A/R Reserve Invoice - Cancel, 50=A/P Reserve Invoice - Create, 51=A/P Reserve Invoice - Update, 52=A/P Reserve Invoice - Cancel]
  OwnObjTyp Int(11) Owning Doc. Object Type default=-1 [-1=, 202=Production Order, 60=Issue for Production, 59=Receipt from Production, 17=Sales Order, 15=Delivery, 13=A/R Invoice, -13=A/R Reserve Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 16=Returns, 22=Purchase Order, 20=Goods Receipt PO, 18=A/P Invoice, -18=A/P Reserve Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 21=Goods Return]
  OwnAbsEnt Int(11) Owning Doc. Absolute Entry
  OwnLine Int(11) Owning Doc. Line Number
  RevdObjTyp Int(11) Reverted Object Type default=-1 [-1=, 60=Issue for Production]
  RevdAbsEnt Int(11) Reverted Absolute Entry
  RevdLine Int(11) Reverted Line Number
  MemoSrc VarChar(1) Memo Source default=- [-=, C=Resource Capacity Form, S=Set Daily Internal Capacities Form]
  Memo Text(16) Memo
  SngRunCap Num(19,6) Single Run Capacity
  MemoSrcSng VarChar(1) Memo Source of Single Run Capacity default=- [-=, C=Resource Capacity Form, S=Set Daily Internal Capacities Form]
  MemoSng Text(16) Memo of Single Run Capacity

# OREA - Return Action
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  ACTION U: Action
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Action nVarChar(228) Return Action

# ORER - Return Reason
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  REASON U: Reason
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Reason nVarChar(228) Return Reason

# ORSB - Resource Groups
Module: General | 32 columns | ObjType: 292
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResGrpCod
  GROUP_NAME U: ResGrpNam
Fields (name type(len) description [values] ->parent table):
  ResGrpCod Int(6) Number
  ResGrpNam nVarChar(20) Group Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Object nVarChar(20) Object Type - History default=292
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History
  updateDate Date(8) Date of Update - History
  ResType VarChar(1) Resource Type default=M [M=Machine, L=Labor, O=Other]
  CostName1 nVarChar(254) Resource Std Cost 1
  CostVal1 Num(19,6) Resource Std Cost 1
  CostName2 nVarChar(254) Resource Std Cost 2
  CostVal2 Num(19,6) Resource Std Cost 2
  CostName3 nVarChar(254) Resource Std Cost 3
  CostVal3 Num(19,6) Resource Std Cost 3
  CostName4 nVarChar(254) Resource Std Cost 4
  CostVal4 Num(19,6) Resource Std Cost 4
  CostName5 nVarChar(254) Resource Std Cost 5
  CostVal5 Num(19,6) Resource Std Cost 5
  CostName6 nVarChar(254) Resource Std Cost 6
  CostVal6 Num(19,6) Resource Std Cost 6
  CostName7 nVarChar(254) Resource Std Cost 7
  CostVal7 Num(19,6) Resource Std Cost 7
  CostName8 nVarChar(254) Resource Std Cost 8
  CostVal8 Num(19,6) Resource Std Cost 8
  CostName9 nVarChar(254) Resource Std Cost 9
  CostVal9 Num(19,6) Resource Std Cost 9
  CostName10 nVarChar(254) Resource Std Cost 10
  CostVal10 Num(19,6) Resource Std Cost 10
  ResUoM nVarChar(20) Resource Unit of Measurement

# ORSC - Resources
Module: General | 125 columns | ObjType: 290
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode
  RES_CODE U: VisResCode
  ITEM_NAME: ResName
  SALE: PrchseRes
  PURCHASE: SellRes
  PRODUCTION: ProdRes
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Code
  VisResCode nVarChar(50) Resource No.
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  CodeBars nVarChar(254) Bar Code
  ResName nVarChar(200) Resource Description
  FrgnName nVarChar(200) Description in Foreign Lang.
  ResType VarChar(1) Resource Type default=M [M=Machine, L=Labor, O=Other]
  ResGrpCod Int(6) Resource Group default=1 ->ORSB
  UnitOfMsr nVarChar(100) Unit of Measure
  PrchseRes VarChar(1) Purchase Resource [Yes/No] default=Y [Y=Yes, N=No]
  SellRes VarChar(1) Sales Resource [Yes/No] default=Y [Y=Yes, N=No]
  ProdRes VarChar(1) Production Resource [Yes/No] default=Y [Y=Yes, N=No]
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  IssueMthd VarChar(1) Issue Method default=B [B=Backflush, M=Manual]
  StdCost1 Num(19,6) Resource Cost 1
  StdCost2 Num(19,6) Resource Cost 2
  StdCost3 Num(19,6) Resource Cost 3
  StdCost4 Num(19,6) Resource Cost 4
  StdCost5 Num(19,6) Resource Cost 5
  StdCost6 Num(19,6) Resource Cost 6
  StdCost7 Num(19,6) Resource Cost 7
  StdCost8 Num(19,6) Resource Cost 8
  StdCost9 Num(19,6) Resource Cost 9
  StdCost10 Num(19,6) Resource Cost 10
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  DfltWH nVarChar(8) Default Warehouse
  QueryGroup Int(11) Properties default=0
  PicturName nVarChar(200) Picture
  UserText Text(16) Item Remarks
  QryGroup1 VarChar(1) Property 1 default=N [Y=Yes, N=No]
  QryGroup2 VarChar(1) Property 2 default=N [Y=Yes, N=No]
  QryGroup3 VarChar(1) Property 3 default=N [Y=Yes, N=No]
  QryGroup4 VarChar(1) Property 4 default=N [Y=Yes, N=No]
  QryGroup5 VarChar(1) Property 5 default=N [Y=Yes, N=No]
  QryGroup6 VarChar(1) Property 6 default=N [Y=Yes, N=No]
  QryGroup7 VarChar(1) Property 7 default=N [Y=Yes, N=No]
  QryGroup8 VarChar(1) Property 8 default=N [Y=Yes, N=No]
  QryGroup9 VarChar(1) Property 9 default=N [Y=Yes, N=No]
  QryGroup10 VarChar(1) Property 10 default=N [Y=Yes, N=No]
  QryGroup11 VarChar(1) Property 11 default=N [Y=Yes, N=No]
  QryGroup12 VarChar(1) Property 12 default=N [Y=Yes, N=No]
  QryGroup13 VarChar(1) Property 13 default=N [Y=Yes, N=No]
  QryGroup14 VarChar(1) Property 14 default=N [Y=Yes, N=No]
  QryGroup15 VarChar(1) Property 15 default=N [Y=Yes, N=No]
  QryGroup16 VarChar(1) Property 16 default=N [Y=Yes, N=No]
  QryGroup17 VarChar(1) Property 17 default=N [Y=Yes, N=No]
  QryGroup18 VarChar(1) Property 18 default=N [Y=Yes, N=No]
  QryGroup19 VarChar(1) Property 19 default=N [Y=Yes, N=No]
  QryGroup20 VarChar(1) Property 20 default=N [Y=Yes, N=No]
  QryGroup21 VarChar(1) Property 21 default=N [Y=Yes, N=No]
  QryGroup22 VarChar(1) Property 22 default=N [Y=Yes, N=No]
  QryGroup23 VarChar(1) Property 23 default=N [Y=Yes, N=No]
  QryGroup24 VarChar(1) Property 24 default=N [Y=Yes, N=No]
  QryGroup25 VarChar(1) Property 25 default=N [Y=Yes, N=No]
  QryGroup26 VarChar(1) Property 26 default=N [Y=Yes, N=No]
  QryGroup27 VarChar(1) Property 27 default=N [Y=Yes, N=No]
  QryGroup28 VarChar(1) Property 28 default=N [Y=Yes, N=No]
  QryGroup29 VarChar(1) Property 29 default=N [Y=Yes, N=No]
  QryGroup30 VarChar(1) Property 30 default=N [Y=Yes, N=No]
  QryGroup31 VarChar(1) Property 31 default=N [Y=Yes, N=No]
  QryGroup32 VarChar(1) Property 32 default=N [Y=Yes, N=No]
  QryGroup33 VarChar(1) Property 33 default=N [Y=Yes, N=No]
  QryGroup34 VarChar(1) Property 34 default=N [Y=Yes, N=No]
  QryGroup35 VarChar(1) Property 35 default=N [Y=Yes, N=No]
  QryGroup36 VarChar(1) Property 36 default=N [Y=Yes, N=No]
  QryGroup37 VarChar(1) Property 37 default=N [Y=Yes, N=No]
  QryGroup38 VarChar(1) Property 38 default=N [Y=Yes, N=No]
  QryGroup39 VarChar(1) Property 39 default=N [Y=Yes, N=No]
  QryGroup40 VarChar(1) Property 40 default=N [Y=Yes, N=No]
  QryGroup41 VarChar(1) Property 41 default=N [Y=Yes, N=No]
  QryGroup42 VarChar(1) Property 42 default=N [Y=Yes, N=No]
  QryGroup43 VarChar(1) Property 43 default=N [Y=Yes, N=No]
  QryGroup44 VarChar(1) Property 44 default=N [Y=Yes, N=No]
  QryGroup45 VarChar(1) Property 45 default=N [Y=Yes, N=No]
  QryGroup46 VarChar(1) Property 46 default=N [Y=Yes, N=No]
  QryGroup47 VarChar(1) Property 47 default=N [Y=Yes, N=No]
  QryGroup48 VarChar(1) Property 48 default=N [Y=Yes, N=No]
  QryGroup49 VarChar(1) Property 49 default=N [Y=Yes, N=No]
  QryGroup50 VarChar(1) Property 50 default=N [Y=Yes, N=No]
  QryGroup51 VarChar(1) Property 51 default=N [Y=Yes, N=No]
  QryGroup52 VarChar(1) Property 52 default=N [Y=Yes, N=No]
  QryGroup53 VarChar(1) Property 53 default=N [Y=Yes, N=No]
  QryGroup54 VarChar(1) Property 54 default=N [Y=Yes, N=No]
  QryGroup55 VarChar(1) Property 55 default=N [Y=Yes, N=No]
  QryGroup56 VarChar(1) Property 56 default=N [Y=Yes, N=No]
  QryGroup57 VarChar(1) Property 57 default=N [Y=Yes, N=No]
  QryGroup58 VarChar(1) Property 58 default=N [Y=Yes, N=No]
  QryGroup59 VarChar(1) Property 59 default=N [Y=Yes, N=No]
  QryGroup60 VarChar(1) Property 60 default=N [Y=Yes, N=No]
  QryGroup61 VarChar(1) Property 61 default=N [Y=Yes, N=No]
  QryGroup62 VarChar(1) Property 62 default=N [Y=Yes, N=No]
  QryGroup63 VarChar(1) Property 63 default=N [Y=Yes, N=No]
  QryGroup64 VarChar(1) Property 64 default=N [Y=Yes, N=No]
  CreateDate Date(8) Date of Creation
  UpdateDate Date(8) Date of Update
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=290
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  UserSign2 Int(6) Updating User
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  LastPurPrc Num(19,6) Last Purchase Price
  LastPurCur nVarChar(3) Last Purchase Currency
  LastPurDat Date(8) Last Purchase Date
  LstEvlPric Num(19,6) Last Evaluated Price
  LstEvlDate Date(8) Date of Last Reval. Price
  NumResUnit Int(11) No. of Resource Units default=1
  TimeResUn Int(11) Time per Resource Units
  ResAlloc VarChar(1) Resource Allocation default=S [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  LinkItm nVarChar(50) Linked Item ->OITM
  RelCap1 VarChar(1) Relevant to single run capacity 1 default=Y [Y=Yes, N=No]
  RelCap2 VarChar(1) Relevant to single run capacity 2 default=Y [Y=Yes, N=No]
  RelCap3 VarChar(1) Relevant to single run capacity 3 default=Y [Y=Yes, N=No]
  RelCap4 VarChar(1) Relevant to single run capacity 4 default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR

# ORSG - Resource Properties
Module: General | 3 columns | ObjType: 291
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResTypCod
  GROUP_NAME U: ResGrpNam
Fields (name type(len) description [values] ->parent table):
  ResTypCod Int(6) Number
  ResGrpNam nVarChar(50) Property Name
  UserSign nVarChar(6) User Signature ->OUSR

# ORVC - Business Partner VAT No. Verification Response
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  RSP_COD U: ResponCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ResponCode Int(11) Response Code
  ResponName Text(16) Response Description

# OSAB - Social
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  SocialName nVarChar(32) Social Name
  SocialUrl nVarChar(100) Social URL

# OSAS - Sales App Setting
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(100) Name
  AdBoardId Int(11) Advanced Dashboard ID ->OXAP
  CAdBoardId Int(11) Customer Advanced Dashboard ID ->OXAP

# OSDL - Sensitive Personal Data Access Log
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DataSubjct VarChar(1) Data Subject Type [1=OHEM, 2=OCRD, 3=OUSR, 4=OCPR]
  SubjctKey nVarChar(100) Data Subject Key
  DataTable nVarChar(5) Data Table
  TblKeyCnt Int(11) Data Table Key Count
  KeyVal1 nVarChar(100) Key Value 1
  KeyVal2 nVarChar(100) Key Value 2
  KeyVal3 nVarChar(100) Key Value 3
  KeyVal4 nVarChar(100) Key Value 4
  Property nVarChar(50) Property Name
  UserSign Int(11) Access User Signature ->OUSR
  AccessDate Int(11) Access Date
  AccessTime Int(11) Access Time
  AccessChnl VarChar(1) Access Channel [U=UI, D=DI, B=Browser Access, W=Personal Data Management Wizard, A=Bank File]
  Version nVarChar(13) Version

# OSES - 
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PK_CODE U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) SEFAZ Country Code
  Descr nVarChar(100) SEFAZ Country Description

# OSLD - Schedule Row Detail
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SCHD_LINE U: ObjType, DocEntry, DocLineNum, SchdLine
  DOCLINESLD: ObjType, DocEntry, DocLineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjType nVarChar(20) Object Type default=-1 [-1=, 13=A/R Reserve Invoice, 17=Sales Order, 18=A/P Reserve Invoice, 22=Purchase Order, 163=A/P Correction Reserve Invoice, 165=A/R Correction Reserve Invoice, 202=Production Order, 1250000001=Warehouse Transfer Request]
  DocEntry Int(11) Associated Doc Entry
  DocLineNum Int(11) Associated Doc Row No.
  SchdLine Int(11) Schedule Row No.
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  CfmDate Date(8) Confirmation Date
  CfmQty Num(19,6) Confirmation Quantity
  FixedCfm VarChar(1) Fixed Confirmation Data default=N [Y=Yes, N=No]
  ReqQty Num(19,6) Required Quantity

# OSLS - Short Link Mapping
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) GUID for short link
  Origin nVarChar(128) The origin of source link
  SrcLink Text(16) The source link URL
  OwnerCode nVarChar(50) The creator user code
  CreateDate Date(8) Date
  CreateTime Int(11) Time default=0

# OSQL - SQL query
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SqlCode
Fields (name type(len) description [values] ->parent table):
  SqlCode nVarChar(254) SQL query code
  SqlName nVarChar(254) SQL query name
  SqlText Text(16) SQL text
  ParamList nVarChar(254) List of bound parameter names
  ParamDetai nVarChar(254) Parameter details
  InternalS Text(16) Internal SQL text
  LogInstanc Int(11) Log instance default=0
  ObjType nVarChar(20) Object Type default=2
  CreateDate Date(8) Created On
  UpdateDate Date(8) Updated On
  DataVers Int(11) Data version default=1

# OSRC - Service App Report Configuration
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  SysRptName nVarChar(120) System Report Name
  SysRptTemp Text(16) System Report Template
  CusRptName nVarChar(120) Customized Report Name
  CusRptTemp Text(16) Customized Report Template
  RptChoice VarChar(1) Report Choice [S=System, C=Customized]

# OSSG - Service App Setting groups
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(100) Name
  CustGroup VarChar(1) Customized Group default=N [Y=Yes, N=No]
  EnEditTime VarChar(1) Enable Edit Time default=N [Y=Yes, N=No]
  EnReject VarChar(1) Enable Reject default=N [Y=Yes, N=No]
  EnResign VarChar(1) Enable Resign default=N [Y=Yes, N=No]
  EnFollowup VarChar(1) Enable Follow-up default=N [Y=Yes, N=No]
  EnSign VarChar(1) Enable Signature default=N [Y=Yes, N=No]
  EnStarRat VarChar(1) Enable Star Rating default=N [Y=Yes, N=No]
  EnActDura VarChar(1) Enable Actual Duration default=N [Y=Yes, N=No]
  AdBoardId Int(11) Advanced Dashboard ID ->OXAP

# OSTB - Template
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Template nVarChar(32) Template
  TemplateId nVarChar(100) Template ID

# OSTS - Service App Technician settings
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Technician Int(11) Technician ->OHEM
  Choice VarChar(1) Choice default=C [G=Group, C=Customize]
  GroupCode Int(11) Group Code ->OSSG

# OSWA - Specific Withholding Amounts
Module: General | 72 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PymntRsnCd, CardCode, CUSplit
Fields (name type(len) description [values] ->parent table):
  PymntRsnCd nVarChar(3) Payment Reason Code ->OPTR
  CardCode nVarChar(15) BP Code ->OCRD
  FllTxInAdv Num(19,6) Full WTax Taxation in Advance
  AmntsOnhld Num(19,6) WTax Amount on Hold
  RTAsWth Num(19,6) Regional IRPEF Held as WTax
  RTAsAdv Num(19,6) Regional IRPEF - In Advance
  SspndRegTx Num(19,6) Regional Suspended Tax - IRPEF
  MTAsWth Num(19,6) Municipal Tax as WTax - IRPEF
  MTAsAdv Num(19,6) Municipal Tax Held as Advance
  SspndMTTx Num(19,6) Suspended Municipal Tax
  TxblPrYr Num(19,6) Taxable Amt - Previous Year
  WTHPrYr Num(19,6) WTax Amount - Previous Year
  ScrtyCntrP Num(19,6) Social Security Tax Payer
  ScrtyCntrS Num(19,6) Social Security Supplier
  ExpsRmbrsd Num(19,6) Expenses Reimbursed
  WTHRmbrsd Num(19,6) WTax Reimbursed
  DlvryIdNo nVarChar(100) Delivery Identification No.
  SnglCrtfNo nVarChar(17) Single Certification No.
  ErnYr Int(6) Earning Year
  Advanced VarChar(1) Advanced default=N [Y=Yes, N=No]
  WTHTypCd nVarChar(2) WTax Type Code ->OWXT
  GrssAmount Num(19,6) Gross Amount Due to Supplier
  NtSbjctFrg Num(19,6) Amount Not Subject to WT
  TxblAmnt Num(19,6) Taxable Amount
  WTHAmnt Num(19,6) Withholding Tax Amount
  SSFiscalCd nVarChar(16) Social Security Fiscal C..(29)
  SSIName nVarChar(100) Social Security Institut..(30)
  SSICode VarChar(1) Social Security Institut..(31) [2=ENPAM, 4=ENPAPI]
  CompanyCd nVarChar(16) Company Code(32)
  Category VarChar(1) Category(33) [O=Medico di assistenze primaria, P=Pediatra di libera scelta, Q=Medico specialista esterno, R=Medico della Medicina dei Servize a tempo determinato, S=Medico dell'Emergenza territoriale a tempo determinato, T=Medico della Continuit� assistenziale a tempo determinato, U=Infermieri prestatori d'opera occasionali]
  EmpeSSCntr Num(19,6) Employee social security..(34)
  EmprSSCntr Num(19,6) Employer social security..(35)
  OthCntrbts VarChar(1) Other Contributions(36) default=N [Y=Yes, N=No]
  VOthCntrbt Num(19,6) Value of Other Contribut..(37)
  OthAmntDue Num(19,6) Other amounts due(38)
  OthAmntPd Num(19,6) Other amounts paid(39)
  AmntPdBfBr Num(19,6) Amount Paid before Bankr..(41)
  AmntPdByTr Num(19,6) Amount Paid by Trustee(42)
  FiscalCode nVarChar(16) Fiscal Code(52)
  TxblAmntE Num(19,6) Taxable Amount(53)
  TaxAmount Num(19,6) Tax Amount(54)
  TxAmntInAd Num(19,6) Tax Amount in Advance(55)
  SspndWTHTx Num(19,6) Suspended WTH Tax(56)
  AdRgTxIRPH Num(19,6) Additional Regional tax..(57)
  AdRgTxIRPA Num(19,6) Additional Regional tax..(58)
  SspdRgnlTx Num(19,6) Suspended Regional Tax(59)
  AdCtTxIRWT Num(19,6) Additional City tax to I..(60)
  AdCtTxIWTA Num(19,6) Additional City Tax to I..(61)
  SspndCtTx Num(19,6) Suspended City Tax(62)
  FsCdTrdPty nVarChar(16) Fiscal Code Third Party(71)
  FCdTrdPtyS nVarChar(16) Fiscal Code Third Party..(72)
  FscCdExpr nVarChar(16) Fiscal Code Expropriation(73)
  FsCdMnDbS nVarChar(16) Fiscal Code of Main Deb..(101)
  AmntPdS Num(19,6) Amount Paid(102)
  WHTApdS Num(19,6) WHT Applied(103)
  WHTNApdS VarChar(1) WHT not Applied(104) default=N [Y=Yes, N=No]
  FsCdMnDbR nVarChar(16) Fiscal Code of Main Deb..(105)
  AmntPdR Num(19,6) Amount Paid(106)
  WHTApdR Num(19,6) WHT Applied(107)
  WHTNApdR VarChar(1) WHT not Applied(108) default=N [Y=Yes, N=No]
  AmntPdA Num(19,6) Amount Paid(131)
  TxAppldA Num(19,6) Tax Applied(132)
  AmntPdB Num(19,6) Amount Paid(133)
  TxAppldB Num(19,6) Tax Applied(134)
  AmntPdC Num(19,6) Amount Paid(135)
  TxAppldC Num(19,6) Tax Applied(136)
  AmntPdD Num(19,6) Amount Paid(137)
  TxAppldD Num(19,6) Tax Applied(138)
  AmtPvdNTxS Num(19,6) Amounts provided and no..(104)
  AmtPvdNTxR Num(19,6) Amounts provided and no..(108)
  CUSplit VarChar(1) CU Split default=N [N=No, Y=Yes]
  SmRnNtWTx Num(19,6) Returned Amount After Deduction of WTax

# OTCN - Tracking Note
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CCD U: CCDNum, DirectImp
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry
  CCDNum nVarChar(40) CCD Number
  Date Date(8) Date
  CustTerm nVarChar(15) Customs Terminal
  CntrOrigin nVarChar(3) Country/Region of Origin
  DirectImp VarChar(1) Direct Import default=N [Y=Yes, N=No]
  CardCode nVarChar(15) BP Code

# OTOF - Tax Offices
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TOFCode
Fields (name type(len) description [values] ->parent table):
  TOFCode Int(11) Tax Office Code
  TOFName nVarChar(100) Tax Office Name

# OTSH - Time Sheet - Header
Module: General | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  ProjectID Int(11) Project No. ->OPMG
  DocNum Int(11) Document Number
  Type VarChar(1) Type default=E [E=Employee, U=User, O=External]
  UserID Int(11) Employee/User ID ->OHEM
  LastName nVarChar(50) Last Name
  FirstName nVarChar(50) First Name
  Department Int(6) Department
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Production Date
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  SAPPassprt Text(16) Extended SAP Passport
  EncryptIV nVarChar(100) Encrypt IV
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachment
  UserCode nVarChar(50) Employee/User Code
  DataVers Int(11) Data Version default=1

# OTTP - ToolTip Preview
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, ObjectId
Fields (name type(len) description [values] ->parent table):
  UserSign Int(6) User Signature ->OUSR
  ObjectId Int(11) Object ID
  IsEnabled VarChar(1) Enabled default=Y [Y=Yes, N=No]

# OUAL - User Action Log
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
  TIME: ActionDate, ActionTime
  ID_KEY: ObjectId, ObjectKey
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  UserId Int(6) User Id ->OUSR
  ActionDate Date(8) Action Date
  ActionTime Int(11) Action Time
  ActionType VarChar(1) Action Type
  ObjectId Int(11) Object Id
  ObjectKey nVarChar(64) Object Key

# OUDV - User-Defined Views for Service Layer
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name
Fields (name type(len) description [values] ->parent table):
  Name nVarChar(100) View Name
  DBType nVarChar(20) Database Type [MSSQL=Microsoft SQL Server, HANA=SAP HANA]
  SchemaName nVarChar(64) Schema Name
  CreateDate Date(8) Create Date

# OVEC - E-Books VAT Exemption Cause
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EBCausCode
Fields (name type(len) description [values] ->parent table):
  EBCausCode Int(11) Code
  EBCausDesc nVarChar(150) Description

# OWDBD - Dashboard Overview
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  Content Text(16) Content
  Sys VarChar(1) Sys default=Y [Y=Yes, N=No]

# OWDT - Widget Table
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(20) Widget Name
  UserSign nVarChar(6) User ID ->OUSR
  Prototype nVarChar(100) Prototype

# OWFLT - List View Filters
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  TableName nVarChar(50) Table Name
  FilterName nVarChar(50) Filter Name

# OWFST - Web Client Form Settings
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  FormId nVarChar(40) Form Id
  UserId Int(11) User Id
  ObjType nVarChar(20) Object Type default=17

# OWHL - Register of VAT Payers
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ImportDate
Fields (name type(len) description [values] ->parent table):
  ImportDate Date(8) Import Date
  HashCount Int(11) Hash Count
  Comment nVarChar(254) Comments
  NextDate Date(8) Next Date

# OWLBT - Fiori Launchpad Bookmark Tiles
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  Title Text(16) Title
  SubTitle Text(16) Sub Title
  Info Text(16) Icon
  Bind nVarChar(16) Bind Type
  Target Text(16) Url Target

# OWLPD - Launchpad
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  ThemeId nVarChar(254) Theme Id
  DisQikView VarChar(1) Display Quick View or not default=N [Y=Yes, N=No]
  NtfShowDay Int(11) Notification Show Days Setting

# OWNOT - Notifications
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  Date Date(8) Activity Date
  Read VarChar(1) Read/Unread status
  Dismissed VarChar(1) Dismissed or not
  NotiType Int(11) Notification Type

# OWPK - Dashboard Packages
Module: General | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: PackagCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  PackagCode nVarChar(32) Package Code
  PackagName nVarChar(100) Package Name
  Note Text(16) Package Description
  Content Text(16) Package Content
  Author nVarChar(32) Creator
  Version nVarChar(13) Version
  CreateDate Date(8) Create Date
  CreateTime Int(6) Create Time
  IsSystem VarChar(1) Is System default=N [N=No, Y=Yes]
  PackagType VarChar(1) Package Type default=D [D=Dashboard, M=Mobile, P=Pervasive]
  ISIMDB VarChar(1) IS IMDB default=N [N=No, Y=Yes]
  StraType nVarChar(254) Strategy Type default=none
  StraPara nVarChar(254) Strategy Parameters
  SourceType nVarChar(20) Query Source Type default=normal
  ViewName nVarChar(250) View's Name
  ViewCtg nVarChar(250) View's Catalog
  ViewSyn nVarChar(250) View's Synonym
  Viewid Int(11) Query Number

# OWSV - Web Client Smart View
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) GUID
  Name nVarChar(254) Name
  TgtObject nVarChar(32) Target Object
  VariantId nVarChar(40) Variant ID
  ApplyToDoc nVarChar(254) Apply To Docs

# OWUAC - Recent user activities
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  AppId Text(16) App Id
  AppType nVarChar(20) App Type
  Count Int(11) Count
  Timestamp nVarChar(20) Timestamp
  Title nVarChar(100) Title
  Url Text(16) Url
  UsageArray nVarChar(100) Usage Array
  UserId Int(11) User Id
  RecentDay nVarChar(20) Recent Day

# OWUPR - User Preference
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  TableName nVarChar(10) Table Name
  ColName nVarChar(10) Column Name
  DefaultVal nVarChar(254) Default Value

# OWVG - Variant Groups
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
  GROUP U: UserId, ViewType, ViewId, ObjName
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  ViewType nVarChar(50) View Type
  ViewId nVarChar(50) View Id default=-1
  ObjName nVarChar(50) Object Name
  DftVrnt nVarChar(40) Default Variant

# OWVT - List View Variants
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
  GROUP: UserId, ViewType, ViewId, ObjName
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  Order Int(11) Order
  UserId Int(11) User Id
  ViewType nVarChar(50) View Type
  SubVType nVarChar(50) Sub View Type
  ViewId nVarChar(50) View Id default=-1
  ObjName nVarChar(50) Object Name
  FltBarLout Text(16) FilterBarLayout
  SysFilter Text(16) System Filter
  UserFilter Text(16) User Filter
  CdtFilter Text(16) Condition Filter
  IsPublic VarChar(1) Is Public default=N [Y=Yes, N=No]
  IsSys VarChar(1) Is System default=N [Y=Yes, N=No]
  Name nVarChar(100) Variant Name
  Version Int(11) Version
  OvpCus Text(16) Overview Customization
  ChartCus Text(16) Chart Customization

# OWWT - Workbench
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  CATEGORY U: Category
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Workbench Template ID
  Category nVarChar(40) Workbench Category
  Layout Text(16) Workbench Layout
  Action Text(16) Workbench Actions

# OXAP - XAPP Master Data
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of XAPP
  Name nVarChar(250) Name of XAPP
  Default VarChar(1) Is default default=N

# PACT - Pervasive's Insight to Action
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(250) Insight to Action Name
  Type nVarChar(50) Insight to Action Type
  TgtObjId nVarChar(250) Target Object Number
  SrcObjId nVarChar(250) Source Object Number
  SrcType nVarChar(50) Source Object Type

# PACT1 - Pervasive's Insight to Actions' Subitem
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjId nVarChar(250) Source Object Number
  SrcType nVarChar(50) Source Object Type
  TgtObjId nVarChar(250) Target Object Number
  TgtType nVarChar(50) Target Object Type
  ActEntry nVarChar(11) Action Number

# PACT3 - Pervasive's Insight to Action's Table Field
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ActItemEnt Int(11) Action Item Number
  TableName nVarChar(50) Table Name
  FieldName nVarChar(50) Field Name
  IsUDF VarChar(1) Is UDF or Not default=N [Y=Yes, N=No]

# PHA1 - Project Management - Stages
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OPHA
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMC2
  POS Int(11) Position
  START Date(8) Start Date
  CLOSE Date(8) Closing Date
  FINISHDATE Date(8) Finished Date
  Task Int(11) Task Type
  DSCRIPTION Text(16) Description
  EXPCOSTS Num(19,6) Planned Cost
  InvAmtAR Num(19,6) Invoiced Amount (A/R)
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvAmtAP Num(19,6) Invoiced Amount (A/P)
  OpenAmtAP Num(19,6) Open Amount (A/P)
  PERCENT Num(19,6) Contribution Rate - Percentage
  FINISH VarChar(1) Finished default=N [Y=Yes, N=No]
  OWNER Int(11) Owner ->OHEM
  StageDep1 Int(11) Stage Dependence (1)
  StageDep2 Int(11) Stage Dependence (2)
  StageDep3 Int(11) Stage Dependence (3)
  StageDep4 Int(11) Stage Dependence (4)
  StDp1Type VarChar(1) Stage Dependence (1) project type default=P [P=Project, S=Subproject]
  StDp2Type VarChar(1) Stage Dependence (2) project type default=P [P=Project, S=Subproject]
  StDp3Type VarChar(1) Stage Dependence (3) project type default=P [P=Project, S=Subproject]
  StDp4Type VarChar(1) Stage Dependence (4) project type default=P [P=Project, S=Subproject]
  StDp1Abs Int(11) Stage Dependence (1) project key
  StDp2Abs Int(11) Stage Dependence (2) project key
  StDp3Abs Int(11) Stage Dependence (3) project key
  StDp4Abs Int(11) Stage Dependence (4) project key
  LogInstanc Int(11) Log Instance default=0
  AtcEntry Int(11) Attachment Entry ->OATC
  UniqueID nVarChar(50) Unique ID
  EncryptIV nVarChar(100) Encrypt IV

# PHA2 - Project Management - Stages - Open Issues
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  AREA Int(11) Area ->PMC3
  PRIORITY Int(11) Priority
  REMARKS Text(16) Remarks
  CLOSED VarChar(1) Closed default=N [Y=Yes, N=No]
  SOLUTIONID Int(11) Solution Code ->OSLT
  SOLUTION nVarChar(254) Solution Description
  RESPNSIBLE Int(11) Responsible ->OHEM
  ENTERED Int(11) Entered By ->OHEM
  DATE Date(8) Date Entered
  EFFORT Num(19,6) Effort Costs
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# PHA3 - Project Management - Stages - Attachments
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  PATH Text(16) Document Path
  FILE nVarChar(100) File Name
  DATE Date(8) Date
  LogInstanc Int(11) Log Instance default=0

# PHA4 - Project Management - Stages - Documents
Module: General | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  TYP Int(11) Document Type default=-1 [-1=Please select, 112=Document Draft, 30=Manual Journal Entry, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 16=Return, 203002=A/R Down Payment Request, 203=A/R Down Payment Invoice, 13=A/R Invoice, 14=A/R Credit Memo, 13002=A/R Reserve Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 204002=A/P Down Payment Request, 204=A/P Down Payment Invoice, 18=A/P Invoice, 19=A/P Credit Memo, 18002=A/P Reserve Invoice, 191=Service Call, 59=Goods Receipt, 60=Goods Issue, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 1470000113=Purchase Request, 234000032=Goods Return Request, 234000031=Return Request]
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry
  DocDate Date(8) Document Date
  Total Num(19,6) Total
  LineNum Int(11) Line Number
  Status VarChar(1) Line status default=O [O=Open, C=Closed]
  LogInstanc Int(11) Log Instance default=0
  AmountCat VarChar(1) Category to which we will apply the amount from Total [I=Invoiced, O=Open]
  Categorize nVarChar(2) Category Open Amount/Invoiced A/R, A/P to which we will apply the amount from journal entry [=Ignore, OP=Open Amount (A/P), OR=Open Amount (A/R), IP=Invoiced (A/P), IR=Invoiced (A/R)]
  Operation VarChar(1) Operation which we will apply to the amount from the total [=Ignore, A=Add, S=Subtract]
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  ChargedQty Num(19,6) Charged Quantity
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  EncryptIV nVarChar(100) Encrypt IV
  PartTotal Num(19,6) Partially Invoiced Total

# PHA5 - Project Management - Stages - Resources
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PHA1
  LogInstanc Int(11) Log Instance default=0

# PHA6 - Project Management - Stages - Activities
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  ACTIVITYID Int(11) Activity Number ->OCLG
  LogInstanc Int(11) Log Instance default=0
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV

# PHA7 - Project Management - Workorders
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PHA1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry ->OWOR
  LogInstanc Int(11) Log Instance default=0
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  EncryptIV nVarChar(100) Encrypt IV

# PHA8 - Project Management - Summary
Module: General | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  PhBudget Num(19,6) Subproject Budget
  OpenAmtAP Num(19,6) Open Amount (A/P)
  InvoicedAP Num(19,6) Invoiced (A/P)
  TotalAP Num(19,6) Total (A/P)
  TotVarAP Num(19,6) Total Variance (A/P)
  VarPercAP Num(19,6) Variance Percentage (A/P)
  AccPhBudg Num(19,6) Accumulated Subproject Budget
  AccOpAmAP Num(19,6) Accumulated Open Amount (A/P)
  AccInvAP Num(19,6) Accumulated Invoiced (A/P)
  AccTotAP Num(19,6) Accumulated Total (A/P)
  AccTVarAP Num(19,6) Accumulated Total Variance (A/P)
  AccVPercAP Num(19,6) Accumulated Variance Percentage (A/P)
  PoPhAmt Num(19,6) Potential Subproject Amount
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvoicedAR Num(19,6) Invoiced (A/R)
  TotalAR Num(19,6) Total (A/R)
  TotVarAR Num(19,6) Total Variance (A/R)
  VarPercAR Num(19,6) Variance Percentage (A/R)
  AccPoPhAmt Num(19,6) Accumulated Potential Subproject Amount
  AccOpAmAR Num(19,6) Accumulated Open Amount (A/R)
  AccInvAR Num(19,6) Accumulated Invoiced (A/R)
  AccTotAR Num(19,6) Accumulated Total (A/R)
  AccTVarAR Num(19,6) Accumulated Total Variance (A/R)
  AccVPercAR Num(19,6) Accumulated Variance Percentage (A/R)
  ActICCost Num(19,6) Actual Item Component Cost
  ActRCCost Num(19,6) Actual Resource Component Cost
  ActAddCost Num(19,6) Actual Additional Cost
  ActPrCost Num(19,6) Actual Product Cost
  ActBPrCost Num(19,6) Actual By-Product Cost
  TotalVar Num(19,6) Total Variance
  DueDate Date(8) Due Date
  CloseDate Date(8) Actual Closing Date
  Overdue Int(11) Overdue default=0
  Valid VarChar(1) If the calculated data is valid default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0

# PMC1 - Project Management Configuration - Phase Types
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PhaseID
Fields (name type(len) description [values] ->parent table):
  PhaseID Int(11) Phase No.
  Name nVarChar(100) Phase Name

# PMC2 - Project Management Configuration - Stages Setup
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: StageID
Fields (name type(len) description [values] ->parent table):
  StageID Int(11) Stage No.
  Name nVarChar(100) Stage Name
  Dscription nVarChar(254) Stage Description

# PMC3 - Project Management Configuration - Area
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AreaID
Fields (name type(len) description [values] ->parent table):
  AreaID Int(11) Area No.
  Name nVarChar(100) Area Name

# PMC4 - Project Management Configuration - Priority
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PriorityID
Fields (name type(len) description [values] ->parent table):
  PriorityID Int(11) Priority No.
  Name nVarChar(100) Priority Name

# PMC5 - Project Management Configuration - Activity Type
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ActTypeID
Fields (name type(len) description [values] ->parent table):
  ActTypeID Int(11) Activity Type No.
  ActType nVarChar(100) Activity Type
  LaborItem nVarChar(50) Labor Item No. ->OITM
  Chargeable VarChar(1) Chargeable default=Y [Y=Yes, N=No]
  Absence VarChar(1) Absence default=Y [Y=Yes, N=No]
  AbsenceID Int(11) Absence No.

# PMC6 - Project Management Configuration - Tasks
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID
Fields (name type(len) description [values] ->parent table):
  TaskID Int(11) Task No.
  Name nVarChar(100) Task Name

# PMG1 - Project Management - Stages
Module: General | 33 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OPMG
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMC2
  POS Int(11) Position
  START Date(8) Start Date
  CLOSE Date(8) Closing Date
  FINISHDATE Date(8) Finished Date
  Task Int(11) Task Type
  DSCRIPTION Text(16) Description
  EXPCOSTS Num(19,6) Planned Cost
  InvAmtAR Num(19,6) Invoiced Amount (A/R)
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvAmtAP Num(19,6) Invoiced Amount (A/P)
  OpenAmtAP Num(19,6) Open Amount (A/P)
  PERCENT Num(19,6) Contribution Rate - Percentage
  FINISH VarChar(1) Finished default=N [Y=Yes, N=No]
  OWNER Int(11) Owner ->OHEM
  StageDep1 Int(11) Stage Dependence (1)
  StageDep2 Int(11) Stage Dependence (2)
  StageDep3 Int(11) Stage Dependence (3)
  StageDep4 Int(11) Stage Dependence (4)
  StDp1Type VarChar(1) Stage Dependence (1) project type default=P [P=Project, S=Subproject]
  StDp2Type VarChar(1) Stage Dependence (2) project type default=P [P=Project, S=Subproject]
  StDp3Type VarChar(1) Stage Dependence (3) project type default=P [P=Project, S=Subproject]
  StDp4Type VarChar(1) Stage Dependence (4) project type default=P [P=Project, S=Subproject]
  StDp1Abs Int(11) Stage Dependence (1) project key
  StDp2Abs Int(11) Stage Dependence (2) project key
  StDp3Abs Int(11) Stage Dependence (3) project key
  StDp4Abs Int(11) Stage Dependence (4) project key
  LogInstanc Int(11) Log Instance default=0
  AtcEntry Int(11) Attachment Entry ->OATC
  UniqueID nVarChar(50) Unique ID
  EncryptIV nVarChar(100) Encrypt IV

# PMG2 - Project Management - Stages - Open Issues
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  AREA Int(11) Area ->PMC3
  PRIORITY Int(11) Priority
  REMARKS Text(16) Remarks
  CLOSED VarChar(1) Closed default=N [Y=Yes, N=No]
  SOLUTIONID Int(11) Solution Code ->OSLT
  SOLUTION nVarChar(254) Solution Description
  RESPNSIBLE Int(11) Responsible ->OHEM
  ENTERED Int(11) Entered By ->OHEM
  DATE Date(8) Date Entered
  EFFORT Num(19,6) Effort Costs
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV

# PMG3 - Project Management - Stages - Attachments
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMG1
  PATH Text(16) Document Path
  FILE nVarChar(100) File Name
  DATE Date(8) Date
  LogInstanc Int(11) Log Instance default=0

# PMG4 - Project Management - Stages - Documents
Module: General | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  TYP Int(11) Document Type default=-1 [-1=Please select, 112=Document Draft, 30=Manual Journal Entry, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 16=Return, 203002=A/R Down Payment Request, 203=A/R Down Payment Invoice, 13=A/R Invoice, 14=A/R Credit Memo, 13002=A/R Reserve Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 21=Goods Return, 204002=A/P Down Payment Request, 204=A/P Down Payment Invoice, 18=A/P Invoice, 19=A/P Credit Memo, 18002=A/P Reserve Invoice, 191=Service Call, 59=Goods Receipt, 60=Goods Issue, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 1470000113=Purchase Request, 234000032=Goods Return Request, 234000031=Return Request]
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry
  DocDate Date(8) Document Date
  Total Num(19,6) Total
  LineNum Int(11) Line Number
  Status VarChar(1) Line status default=O [O=Open, C=Closed]
  LogInstanc Int(11) Log Instance default=0
  AmountCat VarChar(1) Category to which we will apply the amount from Total [I=Invoiced, O=Open]
  Categorize nVarChar(2) Category Open Amount/Invoiced A/R, A/P to which we will apply the amount from journal entry [=Ignore, OP=Open Amount (A/P), OR=Open Amount (A/R), IP=Invoiced (A/P), IR=Invoiced (A/R)]
  Operation VarChar(1) Operation which we will apply to the amount from the total [=Ignore, A=Add, S=Subtract]
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  ChargedQty Num(19,6) Charged Quantity
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  EncryptIV nVarChar(100) Encrypt IV
  PartTotal Num(19,6) Partially Invoiced Total

# PMG5 - Project Management - Stages - Resources
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID ->PMG1
  LogInstanc Int(11) Log Instance default=0

# PMG6 - Project Management - Stages - Activities
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  ACTIVITYID Int(11) Activity Number ->OCLG
  LogInstanc Int(11) Log Instance default=0
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV

# PMG7 - Project Management - Workorders
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->PMG1
  LineID Int(11) Row No.
  StageID Int(11) Stage ID
  DOCNUM Int(11) Document Number
  DocEntry Int(11) Document Abs. Entry ->OWOR
  LogInstanc Int(11) Log Instance default=0
  Chargeable VarChar(1) Chargeable [Yes/No] default=N [Y=Yes, N=No]
  Charged Num(19,6) Charged
  EncryptIV nVarChar(100) Encrypt IV

# PMG8 - Project Management - Summary
Module: General | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  PhBudget Num(19,6) Subproject Budget
  OpenAmtAP Num(19,6) Open Amount (A/P)
  InvoicedAP Num(19,6) Invoiced (A/P)
  TotalAP Num(19,6) Total (A/P)
  TotVarAP Num(19,6) Total Variance (A/P)
  VarPercAP Num(19,6) Variance Percentage (A/P)
  AccPhBudg Num(19,6) Accumulated Subproject Budget
  AccOpAmAP Num(19,6) Accumulated Open Amount (A/P)
  AccInvAP Num(19,6) Accumulated Invoiced (A/P)
  AccTotAP Num(19,6) Accumulated Total (A/P)
  AccTVarAP Num(19,6) Accumulated Total Variance (A/P)
  AccVPercAP Num(19,6) Accumulated Variance Percentage (A/P)
  PoPhAmt Num(19,6) Potential Subproject Amount
  OpenAmtAR Num(19,6) Open Amount (A/R)
  InvoicedAR Num(19,6) Invoiced (A/R)
  TotalAR Num(19,6) Total (A/R)
  TotVarAR Num(19,6) Total Variance (A/R)
  VarPercAR Num(19,6) Variance Percentage (A/R)
  AccPoPhAmt Num(19,6) Accumulated Potential Subproject Amount
  AccOpAmAR Num(19,6) Accumulated Open Amount (A/R)
  AccInvAR Num(19,6) Accumulated Invoiced (A/R)
  AccTotAR Num(19,6) Accumulated Total (A/R)
  AccTVarAR Num(19,6) Accumulated Total Variance (A/R)
  AccVPercAR Num(19,6) Accumulated Variance Percentage (A/R)
  ActICCost Num(19,6) Actual Item Component Cost
  ActRCCost Num(19,6) Actual Resource Component Cost
  ActAddCost Num(19,6) Actual Additional Cost
  ActPrCost Num(19,6) Actual Product Cost
  ActBPrCost Num(19,6) Actual By-Product Cost
  TotalVar Num(19,6) Total Variance
  DueDate Date(8) Due Date
  CloseDate Date(8) Actual Closing Date
  Overdue Int(11) Overdue default=0
  Valid VarChar(1) If the calculated data is valid default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0

# PMG9 - Project Management - Charged Document Lines Log - Used by Billing Wizard
Module: General | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, BWRefID, TargetType, TargetAbs, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  BWRefID Int(11) Billing Wizard Reference ID
  TargetType Int(11) Target Document Type default=-1 [-1=, 15=Delivery, 13=A/R Invoice]
  TargetAbs Int(11) Target Document Abs. Entry
  TargetNum Int(11) Target Document Number
  TargetLine Int(11) Target Document Line Number
  SubProjID Int(11) Subproject ID default=-1
  StageID Int(11) Stage ID
  SourceType Int(11) Source Document Type default=-1 [-1=, 18=A/P Invoice, 23=Sales Quotation, 17=Sales Order, 13002=A/R Reserve Invoice, 15=Delivery, 33=Activity, 202=Work Order, 234000024=Timesheet]
  SourceAbs Int(11) Source Document Abs. Entry
  SourceNum Int(11) Source Document Number
  SourceLine Int(11) Source Document Line Number
  Charged Num(19,6) Charged
  ChargedQty Num(19,6) Charged Quantity
  DestType Int(11) Destination Table Type default=-1 [-1=, 234000021=Project Management Document, 234000022=Project Management Subproject, 234000024=Time Sheet Document]
  DestArr Int(11) Destination Table Array default=-1 [-1=, 1=Time Sheet Lines, 4=Stage Documents, 6=Stage Activities, 7=Stage Workorders]
  DestAbs Int(11) Destination Table Abs. Entry
  DestLine Int(11) Destination Table Line Number

# PMX1 - Payroll Line
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPMX
  LineNum Int(11) Row Number
  CateType VarChar(1) Category Type
  CateCode nVarChar(3) Category Code
  Keyword nVarChar(10) Keyword
  Category nVarChar(100) Category
  Debit nVarChar(20) Debit Amount
  Credit nVarChar(20) Credit Amout
  FCDebit nVarChar(20) FC Debit Amount
  FCCredit nVarChar(20) FC Credit Amount

# PUTR - Pre-Upgrade Test Result
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SerialNum
Fields (name type(len) description [values] ->parent table):
  SerialNum Int(11) Serial Number
  CompanyVer nVarChar(40) Company Version
  TargetVer nVarChar(40) Target Version
  BeginTime nVarChar(20) Start Time
  EndTime nVarChar(20) End Time

# PUTR1 - Pre-Upgrade Test Result Line
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SerialNum, TestID
Fields (name type(len) description [values] ->parent table):
  SerialNum Int(11) Serial Number
  TestID Int(11) Test ID
  TestDesc nVarChar(254) Test Description
  Result VarChar(1) Result [S=Success, E=Error, W=Warning, K=Skipped]
  BeginTime nVarChar(20) Start Time
  EndTime nVarChar(20) End Time
  SAPNote nVarChar(100) SAP Note Link

# QAG1 - Query Authorization Group Assignment
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AUTHGRPID, CATEGORYID
Fields (name type(len) description [values] ->parent table):
  AUTHGRPID Int(11) Query Authorization Group ID ->OQAG
  CATEGORYID Int(11) Category ID ->OQCN

# RADM - Resource Administration
Module: General | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResVersion
Fields (name type(len) description [values] ->parent table):
  DevGroup nVarChar(3) Development Group
  ResVersion nVarChar(5) Resource Version
  ReleaseDte Date(8) Rsleade Date
  RelFrzDate Date(8) GUI Freeze Date for Release
  Sp1Date Date(8) SP1 Date
  Sp1FrzDate Date(8) GUI Freeze Date for SP1
  Sp2Date Date(8) SP2 Date
  Sp2FrzDate Date(8) GUI Freeze Date for SP2
  DbLocked Int(11) Is DB Locked for Edit [0=Not Locked, 1=GUI Freeze (Translations), 2=Read Only, 3=Full Lock]
  DbVersion nVarChar(10) Resource DB Version
  CreateDate Date(8) Creation Date of DB
  CreateTime Int(11) Creation Time of DB default=0
  CanLogin VarChar(1) Can Users Login
  ValidPath nVarChar(100) Valid Path For Running
  P4Path nVarChar(100) P4 Version Path
  MDVersion Int(11) Metadata Version default=-1
  VerScpDate Date(8) Version Scope Date
  VerScpTime Int(11) Version Scope Time default=0
  TransVer nVarChar(10) Translation Version
  Flags nVarChar(100) Resource flags
  WpFileName nVarChar(100) Wallpaper File Name default=NotSet

# RAMI - 
Module: General | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ErrUID
  GUID: GuidStr
  CodeDefine U: MsgDef
  String U: StrlNum, StrIdx
  ObjectId: ObjName, SonTable, Alias
Fields (name type(len) description [values] ->parent table):
  ErrUID nVarChar(11) Error Message Unique ID
  StrlNum Int(11) String List Number
  StrIdx Int(11) String Index
  GuidStr nVarChar(32) GUID String default=3A51AF1A405C41479530D05FF95A3FBA
  MsgDef nVarChar(100) Message Define
  MsgType VarChar(1) Message Type default=E [E=Error, W=Warning, N=Info, S=Success, O=None]
  MsgArea nVarChar(20) Message Area default=-1 [-1=, AP_AR=Sales and Purchurse orders, RPT=Reports, PROD=Production, LGST=ItemMasterData, INVT=Inventory, FIN=Financial, BANK=Banking, CARD=BP Master Data, AUTH=Authorization, ADMIN=Administration, SDK=SDK UI, LCNS=License, ADDON=Add-On manager, FORM=Form Infrastructure, DB=DB Infrastructure, CORE=Core Layer, INST=Installation and Upgrade]
  ScnExp Text(16) Scenarion Explanation
  ObjName nVarChar(20) Object Name
  SonTable nVarChar(20) Son Table
  Alias nVarChar(10) Alias
  FormID Int(11) Form ID
  PaneID Int(6) Pane Id default=0
  ItemID Int(11) Item ID default=-1
  CreateDate Date(8) Creation date
  CreateTime Int(6) Creation Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time
  UserSign Int(11) User Sign
  SolExp Text(16) Solution Explanation
  CsnId nVarChar(30) CSN Note Id
  DispType nVarChar(30) Display Type default=SBAR [SBAR=Sbar, NOTE=Note, DIALOG_OKCancelType=Dialog OK Cancel, DIALOG_YesNoCancelType=Dialog Yes No Cancel, DIALOG_YesNoType=Dialog Yes No, DIALOG_YesAllNoAllCancelType=Dialog Yes All No All Cancel, DIALOG_ErrorOkType=Dialog Error Ok, DIALOG_ContinueSaveType=Dialog Continue Save, DIALOG_RemoveCancelType=Dialog Remove Cancel, DIALOG_ContinueCancelType=Dialog Continue Cancel, DIALOG_ContinueCancelNoType=Dialog Continue Cancel No, DIALOG_AddCancelType=Dialog Add Cancel, DIALOG_ContinueStopType=Dialog Continue Stop, DIALOG_YesCancelType=Dialog Yes Cancel, DIALOG_ContinueOpenType=Dialog Continue Open, DIALOG_OpenContinueCancelType=Dialog Open Continue Cancel, DIALOG_YesYesAllNoType=Dialog Yes Yes All No, DIALOG_YesYesAllNoAllType=Dialog Yes Yes All No All]
  ColmID Int(11) Column ID default=-1
  IsDeleted VarChar(1) Is Deleted default=N [N=No, Y=Yes]

# RCOD - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocCode
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Base Doc Code
  TrnsDocCod nVarChar(8) Translation Doc Code
  ClntDocCod nVarChar(8) Client Doc Code
  LocMask nVarChar(100) Localization Mask
  LangMask nVarChar(100) Language Mask
  TranRequir VarChar(1) Translation Required

# RCON - Connection Map for CR Templates
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocCode, ConnID
Fields (name type(len) description [values] ->parent table):
  DocCode nVarChar(8) Internal Template Key
  ConnID Int(11) Connection ID
  OldServer nVarChar(64) Old Server Name
  OldDbName nVarChar(64) Old Database Name
  NewServer nVarChar(64) Mapped Server Name
  NewDbName nVarChar(64) Mapped Database Name
  UserCode nVarChar(32) User Code
  SubIndex Int(6) Subreport Index
  SubName nVarChar(64) Subreport Name

# RCR2 - Recurring Postings - Document Reference Information
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RcurCode, Instance, LineNum
  CODE: RcurCode
Fields (name type(len) description [values] ->parent table):
  RcurCode nVarChar(8) Recurring Postings Code ->ORCR
  ObjType Int(11) Object Type
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document N
  RefObjType nVarChar(20) Referenced Object Type [23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 46=Outgoing Payments, 57=Checks for Payment, 321=Internal Reconciliation, 34=Recurring Posting, 30=Journal Entry, 59=Goods Receipt, 60=Goods Issue, 162=Inventory Revaluation, 1470000065=Inventory Counting, 10000071=Inventory Posting, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 202=Production Order, 13001=Original Invoice, -1=External Document]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks
  CardCode nVarChar(15) Business Partner
  Instance Int(6) Instance default=0

# RCTR - Update Counters
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Resource
Fields (name type(len) description [values] ->parent table):
  Resource Int(11) Resource
  Counter Int(11) Counter

# RDCT - Dictionary
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Num
  STRING: Language, String
  NUM: Num
Fields (name type(len) description [values] ->parent table):
  Language Int(11) Language code
  Num Int(11) String number
  String nVarChar(250) String
  Updated Date(8) Update date
  UpdateTime Int(6) Update Time default=0

# RDGP - Development Groups
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  NUM U: Num
  ID_START U: IdtRngStrt
  ID_END U: IdRngEnd
  FORM_START U: FrmRngStrt
  FORM_END U: FrmRngEnd
  MTX_START U: MtxRngStrt
  MTX_END U: MtxRngEnd
  STRL_START U: StrRngStrt
  STRL_END U: StrRngEnd
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Group Number
  GroupCode nVarChar(3) Development Group Code
  GroupName nVarChar(20) Development Group Name
  Lcaliztion nVarChar(2) Localization of Dev Group
  IdtRngStrt Int(11) Unique Id Range - Start
  IdRngEnd Int(11) Unique Id Range - End
  FrmRngStrt Int(11) Forms Editing Range - Start
  FrmRngEnd Int(11) Forms Editing Range - End
  MtxRngStrt Int(11) Matrixes Editing Range - Start
  MtxRngEnd Int(11) Matrixes Editing Range - End
  StrRngStrt Int(11) String Lists Range - Start
  StrRngEnd Int(11) String Lists Range - End

# RDMS - Dictionary Master
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num
  SBO_CODE U: SBOCode
Fields (name type(len) description [values] ->parent table):
  Num Int(11) String number
  Internal VarChar(1) Internal default=0 [1=Yes, 0=No]
  Created Date(8) Creation date
  Remarks nVarChar(250) Remarks
  SBOCode nVarChar(30) SBO Code
  StringType nVarChar(4) String Type
  MaxLen Int(11) Maximum Length

# RFRM - FORM resource
Module: General | 40 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Name
  NUM U: Language, Num
  M_NAME: Name
  M_NUM: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) Form name
  Num Int(11) Form number
  Title nVarChar(64) Title
  TitleUpd Date(8) Title update
  TitleLen Int(11) Title length
  Type Int(11) Form type default=0 [0=Resize Document, 1=Dialog Box, 3=No Title Document, 4=Fixed Document, 5=Resize No Title Document, 6=Toolbar]
  CloseBox VarChar(1) Close box default=1 [0=Yes, 1=No]
  DfltButton Int(11) Default button default=0
  _Top Int(11) Top default=1
  _Bottom Int(11) Bottom
  _Left Int(11) Left
  _Right Int(11) Right
  DoColor VarChar(1) Use color table default=1 [0=Yes, 1=No]
  CT_SEED Int(11) CT_SEED
  CT_RESERVE Int(11) CT_RESERVE
  CT_SIZE Int(11) CT_SIZE
  CT_S0_VAL Int(11) CT_S0_VALUE
  CT_S0_RED Int(11) CT_S0_RED
  CT_S0_GRN Int(11) CT_S0_GREEN
  CT_S0_BLUE Int(11) CT_S0_BLUE
  CT_S1_VAL Int(11) CT_S1_VALUE
  CT_S1_RED Int(11) CT_S1_RED
  CT_S1_GRN Int(11) CT_S1_GREEN
  CT_S1_BLUE Int(11) CT_S1_BLUE
  CT_S2_VAL Int(11) CT_S2_VALUE
  CT_S2_RED Int(11) CT_S2_RED
  CT_S2_GRN Int(11) CT_S2_GREEN
  CT_S2_BLUE Int(11) CT_S2_BLUE
  CT_S3_VAL Int(11) CT_S3_VALUE
  CT_S3_RED Int(11) CT_S3_RED
  CT_S3_GRN Int(11) CT_S3_GREEN
  CT_S3_BLUE Int(11) CT_S3_BLUE
  CT_S4_VAL Int(11) CT_S4_VALUE
  CT_S4_RED Int(11) CT_S4_RED
  CT_S4_GRN Int(11) CT_S4_GREEN
  CT_S4_BLUE Int(11) CT_S4_BLUE
  MaxUnique Int(11) Max Unique

# RFTL - FITL resource
Module: General | 72 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Name, Num
  M_NAME: Name, Num
  STRING: ItemString
  UNIQUE_ID U: Language, Name, UniqueID
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update dateS
  Language Int(11) Language code
  Name nVarChar(64) FITL name
  Num Int(11) Item number
  ItemType Int(11) Item type [4=Button, 121=Check box, 114=Edit popup, 16=Edit text, 118=Extended edit, 99=Folder, 101=FwdBck button, 123=Graph, 124=Icon, 116=Link button, 127=Matrix, 120=Media, 103=Multi page, 115=Pane button, 104=Pane popup, 117=Picture, 98=Pipe, 125=Popup, 119=Preview, 112=Progress, 122=Radio button, 100=Rectangle, 113=Select popup, 8=Static text, 102=User group, 0=User item]
  Enabled VarChar(1) Enabled default=1 [0=No, 1=Yes]
  _Top Int(11) Top
  _Bottom Int(11) Bottom
  _Left Int(11) Left
  _Right Int(11) Right
  ItemRes Int(11) Item resource
  Font Int(11) Font number
  FontSize Int(11) Font size
  Attributes Int(11) Attributes
  Style Int(11) Style
  Mode Int(11) Mode
  VarNum Int(11) Variable number
  AttrVar Int(11) Attribute variable
  NewLineVar Int(11) New line variable
  ProcVar Int(11) Proc variable
  LinkVar Int(11) Link variable
  DragVar Int(11) Drag variable
  FileCode nVarChar(8) File code
  FieldNum Int(11) Field number
  IndexType VarChar(1) Index type default=0 [0=Variable, 1=Static]
  IndexVal Int(11) Index value
  FatIdxType VarChar(1) Father index type default=0 [0=Variable, 1=Static]
  FatIdxVal Int(11) Father index value
  Editable VarChar(1) Editable default=1 [0=No, 1=Yes]
  Invisible VarChar(1) Invisible default=0 [0=No, 1=Yes]
  SuppressZe VarChar(1) Suppress zeros default=0 [0=No, 1=Yes]
  DfltButton VarChar(1) Default button default=0 [0=No, 1=Yes]
  DataRequir VarChar(1) Data required default=0 [0=No, 1=Yes]
  ForceUpper VarChar(1) Force upper default=0 [0=No, 1=Yes]
  RightJust VarChar(1) Right justified default=1 [0=No, 1=Yes]
  UserType VarChar(1) User type default=0 [0=No, 1=Yes]
  Override VarChar(1) Override validation default=0 [0=No, 1=Yes]
  Sentence VarChar(1) Sentencing default=0 [0=No, 1=Yes]
  ShowType VarChar(1) Show type default=0 [0=Value + Description, 1=Value only, 2=Description only]
  DispDecr VarChar(1) Display description default=0 [0=No, 1=Yes]
  TabOrder Int(11) TAB order
  LinkTo Int(11) Link to item
  DragEntity Int(11) Drag entity
  FromPane Int(11) From pane
  ToPane Int(11) To pane
  Class Int(11) Class
  ItemString nVarChar(64) Item string
  StringUpd Date(8) String update date
  StringLen Int(11) String length
  ItemDesc nVarChar(30) Item description
  DescUpd Date(8) Description update date
  DescLen Int(11) Description length
  FrameRed Int(11) Frame red
  FrameGreen Int(11) Frame green
  FrameBlue Int(11) Frame blue
  BodyRed Int(11) Body red
  BodyGreen Int(11) Body green
  BodyBlue Int(11) Body blue
  TextRed Int(11) Text red
  TextGreen Int(11) Text green
  TextBlue Int(11) Text blue
  ThumbRed Int(11) Thumb red
  ThumbGreen Int(11) Thumb green
  ThumbBlue Int(11) Thumb blue
  TxtFgRed Int(11) Text foreground red
  TxtFgGreen Int(11) Text foreground green
  TxtFgBlue Int(11) Text foreground blue
  TxtBgRed Int(11) Text background red
  TxtBgGreen Int(11) Text background green
  TxtBgBlue Int(11) Text background green
  UniqueID nVarChar(10) Unique ID

# RGRP - users groups
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(11) Group Code
  GroupName nVarChar(20) Group Name
  Perms nVarChar(250) Permissions

# RHKY - Hotkeys
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Num
  ITEM U: Language, FormName, ItemNum
Fields (name type(len) description [values] ->parent table):
  Language Int(11) Language code
  Num Int(11) Hotkey Number
  FormName nVarChar(64) Form name
  ItemNum Int(11) Item number
  HkeyIndex Int(11) Hotkey Index in String

# RINF - Resource Info
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResKey
Fields (name type(len) description [values] ->parent table):
  ResKey nVarChar(15) Resource Key
  Remarks nVarChar(254) Remarks

# RLCK - resource locks table
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: resType, masterKey
Fields (name type(len) description [values] ->parent table):
  resType Int(11) Resource Type default=1 [1=form resource, 3=Grid resource, 5=String list resource, 18=Report]
  masterKey nVarChar(64) Master Key
  wrkstation nVarChar(250) Work Station
  userSign Int(11) User Sign
  date Date(8) Date
  time Int(11) Time
  count Int(11) Locks Count default=1

# RLNG - ????
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  BASE: IsBase
  SHORT_NAME U: ShortName
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Code Int(11) Language code
  Name nVarChar(50) Language name
  ShortName nVarChar(4) Short name
  Direction VarChar(1) Direction default=1 [0=Right to left, 1=Left to right]
  IsBase VarChar(1) Is base default=0 [0=No, 1=Yes]
  Charset Int(11) Charset
  CodePage Int(11) Codepage
  KBLayout Int(11) Keyboard layout
  LangStr nVarChar(50) Language String
  TransInB5I VarChar(1) Translated In B5I System default=0
  HelpLang nVarChar(4) Online Help Language Code
  hasHotKey VarChar(1) The language has hot key default=Y [Y=Has HotKey, N=Does not have HotKey]

# RLOG - Resource Edit Log
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsKey, ResCode
  RESOURCE: ResType, MasterKey, SlaveNum
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  AbsKey Int(11) Abs Key
  UserSign Int(11) User Sign
  ResType Int(11) Resource Type
  MasterKey nVarChar(64) Master Key
  SlaveNum nVarChar(20) Slave Num
  Date Date(8) Date
  Time Int(6) Time
  FldName nVarChar(10) Field Name
  NewVal nVarChar(64) New Value
  BatchNum Int(11) Batch Change Number
  ResCode Int(11) Resource Code default=-1

# RMSG - EditMode Messages
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: abs
  TO_WHO: toWho
  WHO_READ: toWho, msgRead
Fields (name type(len) description [values] ->parent table):
  abs Int(11) abs
  fromWho Int(11) from Who
  toWho Int(11) to Who
  date Date(8) date
  time Int(11) time
  loggedOnly VarChar(1) msg valid only f logged default=Y
  message nVarChar(250) message
  msgRead VarChar(1) was message read default=N

# RMTL - MITL resource
Module: General | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Name, Num
  M_NAME: Name, Num
  UNIQUE_ID U: Language, Name, UniqueID
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) MITL name
  Num Int(11) Column number
  ItemType Int(11) Item type default=0 [0=None, 16=Edit text, 105=Bar, 113=Select popup, 116=Link button, 121=Check box, 117=Picture]
  Enabled VarChar(1) Enabled default=1 [0=No, 1=Yes]
  CellType Int(11) CellType default=16 [0=None, 16=Edit text, 105=Bar, 113=Select popup, 116=Link button, 121=Check box]
  CellRes Int(11) Cell resource
  Font Int(11) Font number
  FontSize Int(11) Font size
  Attributes Int(11) Attributes
  Style Int(11) Style
  Mode Int(11) Mode
  TitleType Int(11) Title type default=0 [0=None, 117=Picture]
  TitleEnabl VarChar(1) Title enabled
  TitleRes Int(11) Title resource
  TitleFont Int(11) Title font number
  TFontSize Int(11) Title font size
  TitleAttr Int(11) Title attributes
  TitleStyle Int(11) Title style
  TitleMode Int(11) Title mode
  VarNum Int(11) Variable number
  LinkVar Int(11) Link variable
  DragVar Int(11) Drag variable
  FileCode nVarChar(8) File code
  FieldNum Int(11) Field number
  IndexType VarChar(1) Index type default=0 [0=Variable, 1=Static]
  IndexVal Int(11) Index value
  FatIdxType VarChar(1) Father index type default=0 [0=Variable, 1=Static]
  FatIdxVal Int(11) Father index value
  Editable VarChar(1) Editable default=1 [0=No, 1=Yes]
  SuppressZe VarChar(1) Suppress zeros default=0 [0=No, 1=Yes]
  DataRequir VarChar(1) Data required default=0 [0=No, 1=Yes]
  ForceUpper VarChar(1) Force upper default=0 [0=No, 1=Yes]
  RightJust VarChar(1) Right justified default=1 [0=No, 1=Yes]
  UserType VarChar(1) User type default=0 [0=No, 1=Yes]
  Sentence VarChar(1) Sentencing default=0 [0=No, 1=Yes]
  ShowType VarChar(1) Show type default=0 [0=Value + Description, 1=Value only, 2=Description only]
  DispDecr VarChar(1) Display description default=0 [0=No, 1=Yes]
  LinkTo Int(11) Link to item
  DragEntity Int(11) Drag entity
  Class Int(11) Class
  ItemString nVarChar(64) Item string
  StringUpd Date(8) String update date
  StringLen Int(11) String length
  Title nVarChar(64) Title string
  TitleUpd Date(8) Title updated
  TitleLen Int(11) Title length
  ItemDesc nVarChar(30) Item description
  DescUpd Date(8) Description update date
  DescLen Int(11) Description length
  TxtFgRed Int(11) Text foreground red
  TxtFgGreen Int(11) Text foreground green
  TxtFgBlue Int(11) Text foreground blue
  TxtBgRed Int(11) Text background red
  TxtBgGreen Int(11) Text background green
  TxtBgBlue Int(11) Text background green
  TtlFgRed Int(11) Title foreground red
  TtlFgGreen Int(11) Title foreground green
  TtlFgBlue Int(11) Title foreground blue
  TtlBgRed Int(11) Title background red
  TtlBgGreen Int(11) Title background green
  TtlBgBlue Int(11) Title background blue
  Width Int(11) Width
  UserLen Int(11) User length
  SuppRepeat VarChar(1) Suppress repeating default=0 [0=No, 1=Yes]
  AutoGraph VarChar(1) Auto graph default=0 [0=No, 1=Yes]
  AutoCumm VarChar(1) Auto cummulative default=0 [0=No, 1=Yes]
  UniqueID nVarChar(10) Unique ID

# RMTX - MATX resource
Module: General | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Name
  NUM U: Language, Num
  M_NAME: Name
  M_NUM: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) MATX name
  Num Int(11) MATX number
  DoColor VarChar(1) Use color table default=0 [0=No, 1=Yes]
  BorderRed Int(11) Border red
  BorderGrn Int(11) Border green
  BorderBlue Int(11) Border blue
  BgRed Int(11) Background red
  BgGreen Int(6) Background green
  BgBlue Int(11) Background blue
  CellHeight Int(11) Cell height
  TitleHeigt Int(11) Title height
  Width Int(11) Width
  MaxUnique Int(11) Max Unique

# ROBJ - TM Import/Export Obj
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsKey
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsKey Int(11) Absolute Key
  Name nVarChar(100) Name
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time default=0
  SentDate Date(8) Date Sent For Trans
  SentTime Int(6) Time Sent For Trans default=0
  Localztion nVarChar(2) Localization relevance of obj default=XX
  SntStrCont Int(11) Send Strings Count

# ROBL - Resource Object I/E Log
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RobjKey, Language
Fields (name type(len) description [values] ->parent table):
  RobjKey Int(11) Resource Object Key
  Language Int(11) Language
  ImportDate Date(8) Date Object Imported In Lang
  ImportTime Int(6) Time Imported default=0

# RSC1 - Resources - Warehouses
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, WhsCode
  WHS: WhsCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Locked VarChar(1) Locked default=N [N=No, Y=Yes]
  ObjType nVarChar(20) Object default=290
  LogInstanc Int(11) Log Instance default=0

# RSC2 - Resources - Prices
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, PriceList
  CURRENCY: Currency
  PRICE_LIST: PriceList
  MANUAL: Ovrwritten
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  PriceList Int(11) Price List No. ->OPLN
  Price Num(19,6) List Price
  Currency nVarChar(3) Currency for List Price ->OCRN
  Ovrwritten VarChar(1) Manual Price Entry default=N [Y=Yes, N=No]
  Factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=290 ->ADP1
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  Ovrwrite1 VarChar(1) Manual Price Entry (1) default=N [Y=Yes, N=No]
  Ovrwrite2 VarChar(1) Manual Price Entry (2) default=N [Y=Yes, N=No]

# RSC3 - Resouces - Fixed Assets
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, ItemCode
  ITEM_CODE U: ItemCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  ItemCode nVarChar(50) Item Code ->OITM
  LogInstanc Int(11) Log Instance default=0

# RSC4 - Resources - Employees
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, EmpID
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  EmpID nVarChar(11) Employee No. ->OHEM
  LogInstanc Int(11) Log Instance default=0

# RSC5 - Resources - Preferred Vendors
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, VendorCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  VendorCode nVarChar(15) Vendor Code ->OCRD
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=290 ->ADP1

# RSC6 - Resources - Daily Capacities
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, WeekDay
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  WeekDay Int(11) Weekday No. default=1 [1=First Day of Week, 2=Second Day of Week, 3=Third Day of Week, 4=Fourth Day of Week, 5=Fifth Day of Week, 6=Sixth Day of Week, 7=Seventh Day of Week]
  CapFactor1 Num(19,6) Day 1 Capacity Factor 1
  CapFactor2 Num(19,6) Day 1 Capacity Factor 2
  CapFactor3 Num(19,6) Day 1 Capacity Factor 3
  CapFactor4 Num(19,6) Day 1 Capacity Factor 4
  CapTotal Num(19,6) Total Daily Capacity
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  SngRunCap Num(19,6) Single Run Capacity

# RSDB - Resource DB List
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsKey
  SERVER_DB U: ServerName, DbName
Fields (name type(len) description [values] ->parent table):
  AbsKey Int(11) Abs Key
  ServerName nVarChar(254) Server Name
  DbName nVarChar(64) Resource DB Name
  Date Date(8) Creation date
  Time Date(8) Creation Time
  OrigDB Int(11) Original DB
  MBServer nVarChar(254) Master Base Server Name
  MBDbName nVarChar(64) Master Base DB Name

# RSLG - Resource Merge Log
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SourceDB, TargetDB, RSName, RSType
Fields (name type(len) description [values] ->parent table):
  SourceDB Int(11) Source DB
  TargetDB Int(11) Target DB
  RSName nVarChar(64) Resource Name
  RSType Int(11) Resource Type
  RSStatus VarChar(1) Resourc Status default=N [D=Difference, C=Conflict, M=Merged, N=No Differences]

# RSLM - SLIM
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SBOCode
Fields (name type(len) description [values] ->parent table):
  SBOCode nVarChar(15) SBO Code
  SlimCode nVarChar(100) Slim Code

# RSMS - Resource Merged Snapshots List
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SourceDB, TargetDB
  BASE_DB U: BaseServer, BaseDB
Fields (name type(len) description [values] ->parent table):
  SourceDB Int(11) Source DB
  TargetDB Int(11) Target DB
  BaseServer nVarChar(254) Base Server Name
  BaseDB nVarChar(254) Base DB Name

# RSTI - STRI resource
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Name, Num
  M_NUM: Name, Num
  UNIQUE_ID U: Language, Name, UniqueID
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) STRL name ->STRL
  Num Int(11) String number
  String nVarChar(250) String
  StringLen Int(11) String length
  UniqueID nVarChar(10) Unique ID

# RSTR - STRL resource
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Name
  NUM U: Language, Num
  M_NUM: Num
  M_NAME: Name
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) STRL name
  Num Int(11) STRL number
  MaxUnique Int(11) Max Unique

# RSYS - System Strings
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num
  STRING U: String
Fields (name type(len) description [values] ->parent table):
  Num Int(11) String number
  String nVarChar(250) String
  StringType Int(6) String Type default=0 [0=Free Text, 1=Form, 2=Table, 3=Resource]
  RefCounter Int(11) Reference Counter

# RTPL - Translation Problems Log
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, ResKey
Fields (name type(len) description [values] ->parent table):
  Language Int(11) Language Code
  ResKey nVarChar(15) Resource Key
  Created Date(8) Creation Date
  CreateTime Int(6) Generation Time
  Updated Date(8) Update Date
  UpdateTime Int(6) Update Time
  UserText Text(16) Memo
  Attachment Text(16) Attached File
  UserName nVarChar(254) User Name
  E_Mail nVarChar(100) E-Mail

# RUSR - Resource Users
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign
  I_USER U: IUserCode
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  IUserCode nVarChar(15) I User Code
  Name nVarChar(30) User Name
  UserGroup Int(11) Authorization Group
  Password nVarChar(20) Password
  UserSign Int(11) User Signature

# SALOG - add-ons change log table
Module: General | 37 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) Log ID default=-1
  Operation nVarChar(20) DB Operation
  AddOnId Int(11) AddOn ID
  NameSpace nVarChar(20) Partner Name Space
  PName nVarChar(40) Partner Name
  AName nVarChar(40) AddOn Name
  EName nVarChar(128) AddOn Exe name
  CData nVarChar(80) Partner Contact Data
  AddOnChk nVarChar(32) AddOn Exe Check Sum
  InstName nVarChar(128) AddOn Installer Name
  InstChkSum nVarChar(32) AddOn Installer Check Sum
  InstTime Int(11) Installation estimation time
  AddOnVer nVarChar(20) AddOn Version
  ForceFlag VarChar(1) AddOn Install force flag default=Y [Y=Yes, N=No]
  UnInstName nVarChar(128) AddOn Uninstaller Name
  UnInstChk nVarChar(32) AddOn UnInstaller Check Sum
  UnInstPar nVarChar(200) UnInstaller params
  InstIsUn VarChar(1) Is Installer is UnInstaller
  AGroup VarChar(1) AddOn Group
  IParams nVarChar(200) Installer Params
  UnInstTime Int(11) Uninstallation estimation time default=0
  AutoAssign VarChar(1) Automatic Company Assignment default=N
  Visible VarChar(1) AddOn is visible in AddOnAdmin default=Y [Y=Yes, visible, N=]
  SelfUpgrd VarChar(1) Don`t install/uninstal default=N [Y=Yes, don`t install/uninstall, N=No, perform install/uninstall]
  InstSil VarChar(1) Use silent mode in install default=N [Y=Silent mode supported, N=Silent mode not supported]
  UnInstSil VarChar(1) Use silent mode in uninstall default=N [Y=Silent mode supported, N=Silent mode not supported]
  UpgSil VarChar(1) Use silent mode in upgrade default=N [Y=Silent mode supported, N=Silent mode not supported]
  InstPFChk nVarChar(32) Checksum of install param file
  UnInstPFCh nVarChar(32) Checksum of uninstall par file
  UpgPFChk nVarChar(32) Checksum of upgrade param file
  UpgName nVarChar(128) Addon upgrader name
  UpgTime Int(11) Estimated upgrade time default=0
  UpgParams nVarChar(200) Upgrader params
  UpgChkSum nVarChar(32) Addon upgrader checksum
  IsAdd64 VarChar(1) Is Addon Installer 64bit default=N
  AddPlat VarChar(1) Platform of addon installer default=N [N=x86, X=x64]
  ClientType VarChar(1) Client type supported by the addon default=W [W=Windows desktop, B=Browser access, A=All]

# SARI - add-ons table
Module: General | 41 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NameSpace, AName, AddOnId, AddPlat
Fields (name type(len) description [values] ->parent table):
  AddOnId Int(11) AddOn ID default=-1
  NameSpace nVarChar(20) Partner Name Space
  PName nVarChar(40) Partner Name
  AName nVarChar(40) AddOn Name
  EName nVarChar(128) AddOn Exe name
  CData nVarChar(80) Partner Contact Data
  AddOnChk nVarChar(32) AddOn Exe Check Sum
  InstName nVarChar(128) AddOn Installer Name
  InstChkSum nVarChar(32) AddOn Installer Check Sum
  ABinary Text(16) AddOn Installer Binary
  InstTime Int(11) Installation estimation time
  AddOnVer nVarChar(20) AddOn Version
  ForceFlag VarChar(1) AddOn Install force flag default=Y [Y=Yes, N=No]
  UnInstName nVarChar(128) AddOn Uninstaller Name
  UnInstChk nVarChar(32) AddOn UnInstaller Check Sum
  UnInstPar nVarChar(200) UnInstaller params
  InstIsUn VarChar(1) Is Installer is UnInstaller
  AGroup VarChar(1) AddOn Group
  IParams nVarChar(200) Installer Params
  UnInstTime Int(11) Uninstallation estimation time default=0
  AutoAssign VarChar(1) Automatic Company Assignment default=N
  Visible VarChar(1) AddOn is visible in AddOnAdmin default=Y [Y=Yes, visible, N=]
  SelfUpgrd VarChar(1) Don`t install/uninstal default=N [Y=Yes, don`t install/uninstall, N=No, perform install/uninstall]
  InstSil VarChar(1) Use silent mode in install default=N [Y=Silent mode supported, N=Silent mode not supported]
  UnInstSil VarChar(1) Use silent mode in uninstall default=N [Y=Silent mode supported, N=Silent mode not supported]
  UpgSil VarChar(1) Use silent mode in upgrade default=N [Y=Silent mode supported, N=Silent mode not supported]
  InstParF Text(16) Parameter files in install
  UnInstParF Text(16) Parameter files in uninstall
  UpgParF Text(16) Parameter files in upgrade
  InstPFChk nVarChar(32) Checksum of install param file
  UnInstPFCh nVarChar(32) Checksum of uninstall par file
  UpgPFChk nVarChar(32) Checksum of upgrade param file
  UpgName nVarChar(128) Addon upgrader name
  UpgTime Int(11) Estimated upgrade time default=0
  UpgParams nVarChar(200) Upgrader params
  AUpgrader Text(16) Addon upgrader binary
  UpgChkSum nVarChar(32) Addon upgrader checksum
  ABinary64 Text(16) AddOn Installer Binary (64bit)
  IsAdd64 VarChar(1) Is Addon Installer 64bit default=N
  AddPlat VarChar(1) Platform of addon installer default=N [N=x86, X=x64]
  ClientType VarChar(1) Client type supported by the addon default=W [W=Windows desktop, B=Browser access, A=All]

# SCAB - Appl CABs
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  Flags nVarChar(50) Flags default=NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  ApplCab Text(16) Appl. CAB
  DbCab Text(16) Metadata CAB
  ComOBSCab Text(16) Com OBS CAB
  ComUICab Text(16) Com UI CAB
  ApplCab64 Text(16) Appl. CAB (64bit)
  DbCab64 Text(16) Metadata CAB (64bit)

# SCFG - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: B1iEnabled
Fields (name type(len) description [values] ->parent table):
  PFlags Text(16) Protect settings flags
  B1iEnabled VarChar(1) Is B1i enabled? default=Y [Y=Yes, N=No]
  LstBckupTo Int(11) Last backup Timeout default=60
  SkinStyle VarChar(1) Skin Style default=H
  IsPALInit VarChar(1) Is PAL Initialize or Not default=N
  PANAVer Int(11) Pervasive Version default=0

# SCLC - 
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LangCode
Fields (name type(len) description [values] ->parent table):
  LangCode Int(11) Language Code
  BaseID Int(11) Base language ID
  HotKeyID Int(11) Hotkey language ID
  Updated Date(8) Date of update
  File Text(16) Localization Resource File
  FileName nVarChar(64) Localization file name
  UpdTime Int(11) Time of update
  Version nVarChar(32) B1 version
  PatchLevel nVarChar(16) Special build string

# SCPT - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: guid
  NAME U: scriptName
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  scriptName nVarChar(50) Script Name
  script Text(16) Script Details

# SCSP - Stored Procs (Company)
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SpName, ServerType
Fields (name type(len) description [values] ->parent table):
  SpName nVarChar(50) SP Name
  SpString Text(16) SP String
  doBefore VarChar(1) Do before [Y=, N=]
  ForceCreat VarChar(1) Force Create [Y=Yes, N=No]
  ServerType Int(11) Server Type default=0

# SCUC - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) AbsEntry
  Type Int(11) Type
  Param nVarChar(254) Parameter
  Value Text(16) Value

# SDRC - Drag&Relate - Categories
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) ObjectId
  DescStr nVarChar(30) Description
  VisOrder Int(6) Visual order
  PartOf VarChar(1) PartOf default=D [D=Docs, R=Reports, T=Tools]

# SDRF - Drag&Relate - Files
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) ObjectId
  DescStr nVarChar(30) Description
  FatherId nVarChar(4) FatherId
  VisLevel Int(6) Visual level [1=, 2=]
  VisOrder Int(6) Visual order

# SDRO - Drag&Relate - Output fields
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId, FieldId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) Object Id
  FieldId Int(6) Field Id
  DescStr nVarChar(30) Description
  VisOrder Int(6) Visual order

# SDRQ - Drag&Relate - Queries
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjTo, ObjFrom, ServerType
Fields (name type(len) description [values] ->parent table):
  ObjTo nVarChar(4) ObjectTo
  ObjFrom nVarChar(4) ObjectFrom
  JoinStr nVarChar(254) Join String
  FilterStr nVarChar(128) Filter String
  ServerType Int(11) Server Type default=0

# SDRR - Drag&Relate - Reports
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjId, ServerType
Fields (name type(len) description [values] ->parent table):
  ObjId nVarChar(4) Object ID
  ReportStr Text(16) Report String
  ServerType Int(11) Server Type default=0

# SEULA - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Locale, EULAType
Fields (name type(len) description [values] ->parent table):
  Locale nVarChar(100) Localization
  EULAType VarChar(1) EULA type default=P [P=Productive, E=Evaluation]
  EULADoc Text(16) EULA doc
  Format nVarChar(50) format default=TXT [TXT=Text Format, PDF=PDF Format]
  CheckSum nVarChar(50) checksum

# SEVT - 
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SequenceID
  SOURCE_DB: SourceDB, ObjectType, FieldValue
Fields (name type(len) description [values] ->parent table):
  SequenceID Identity(11) Sequence ID
  SourceDB nVarChar(100) Event source database
  Timestamp nVarChar(20) Event timestamp
  Status nVarChar(50) Event status
  Retry Int(11) Sending event retries
  ObjectType nVarChar(30) Object type
  TransType VarChar(1) Transaction type
  FieldsInKe Int(11) Number of fields in key
  FieldNames nVarChar(254) Names of key fields
  FieldValue nVarChar(254) Values of key fields
  UserID nVarChar(155) Modified by user
  USER_CODE nVarChar(25) User code
  SAPPassprt Text(16) Extended SAP Passport

# SEWAD - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  DBNAME: DbName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry
  DbName nVarChar(100) DB Name (common/company)
  AddonId Int(11) Addon ID
  AddonName nVarChar(128) Addon Name
  AddonVer nVarChar(12) Addon Version
  NameSpace nVarChar(20) Partner Name Space
  PartName nVarChar(40) Partner Name

# SEWBU - 
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) AbsEntry
  CompanyNam nVarChar(100) CompanyName
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  CustNumber VarChar(1) Customer Number
  CompDbName nVarChar(100) Company DB Name
  DateFrom nVarChar(10) Bck Date From
  StartDate nVarChar(10) Bck start date
  FinishDate nVarChar(10) Bck finish date
  Size Int(11) Bck size
  LogSize Int(11) Bck Log Size
  DbVersion nVarChar(32) Db Version
  CodePage Int(11) Code Page

# SEWCS - 
Module: General | 42 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  SmpTableId nVarChar(3) Smp Table ID
  COAtemplat VarChar(1) COA Template
  LocalCurr nVarChar(3) Local Currency
  SystemCurr nVarChar(3) System Currenct
  UseSegAcc VarChar(1) Use Segment Accounts
  StkValuat VarChar(1) Stock Valuation
  PricSysPWh VarChar(1) Price System Per Warehouse
  AllowRelSt VarChar(1) Stock Release w/o Cost Price
  CostPrcLst VarChar(1) Gross profit Base Price Origi
  GrossBySal VarChar(1) Calculate % GP as
  BlkNegQuan VarChar(1) Block Negative Quantity
  RoundMeth VarChar(1) Rounding Method
  RoundVAT VarChar(1) Round Tax Amount in Rows
  EnblExpns VarChar(1) Manage Expenses in Documents
  DirectRate VarChar(1) Exchange Rate Posting
  SumDec Int(11) Decimal - Amounts
  PriceDec Int(11) Decimal - Prices
  RateDec Int(11) Decimal - Rates
  QtyDec Int(11) Decimal - Quantities
  PercentDec Int(11) Decimal - Percent
  MeasureDec Int(11) Decimal - Units
  DecSep VarChar(1) Decimal - Separator
  DpmSalAct nVarChar(15) Sal-DownPayment Clearing Acct
  DfltIncom nVarChar(15) Sales -Revenues Account
  ForgnIncm nVarChar(15) Sales -Revenues Foreign
  ECIncome nVarChar(15) Sales -Revenue EU
  SHandleWT VarChar(1) Sales -enable WT
  SDfltWT nVarChar(4) Sales -Default WT Code
  NINum nVarChar(20) Ni No
  ExpireDate Date(8) Sales - Expiration Date
  CrtfcateNO nVarChar(20) Sales - Certificate Number
  SaleVatOff nVarChar(15) Sales - Tax Offsetting account
  DfltExpn nVarChar(15) Purchase - Expense Account
  ForgnExpn nVarChar(15) Purchase-Foreign Expense Acct
  ECExepnses nVarChar(15) Purchase - EU Expense account
  DpmPurAct nVarChar(15) Pur-DownPayment Clearing Acct
  ExpVarAct nVarChar(15) Purchase - Variance accont
  PHandleWT VarChar(1) Purchase - WT enabled
  PDfltWT nVarChar(4) Purchase - Default WT code
  PurcVatOff nVarChar(15) Pur - Tax Offsetting account
  ComissAct nVarChar(15) Gen - Credit Card Deposit fee

# SEWDB - 
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry nVarChar(8) Absolute Entry
  SmpTableId nVarChar(3) Smp Table ID
  CollectDat nVarChar(10) DB Size Collect Date
  CompDbName nVarChar(100) Company DB Name
  DbPath nVarChar(254) Db Path
  PrevDbSize nVarChar(32) Prev Db Size
  DbSize nVarChar(32) Db Size
  TranLogSiz nVarChar(32) Transaction Log Size
  TranLogPat nVarChar(254) Transaction Log Path
  TotalDbSiz nVarChar(16) Total Db Size
  FreDskSpac nVarChar(16) Free Disk Space
  MaxDbSize nVarChar(16) Max Db Size
  MaxLogSize nVarChar(16) Max Log Size

# SEWDQ - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CompDbNam
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry
  CompDbNam nVarChar(100) Company Db Name
  QueryStr Text(16) The query processed string
  NumCol Int(11) Number of column in answer
  NumRow Int(11) Number of rows in answer
  ResStr Text(16) The format restult string

# SEWDV - 
Module: General | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  CustNumber VarChar(1) Customer Number
  DocPeriod nVarChar(32) Doc Period
  SalesOrdrs Int(11) Sales Orders
  SalDlvDocs Int(11) Sales Delivery Docs
  SalesInvs Int(11) Sales Invoices
  PurcOrders Int(11) Purchase Orders
  GoodRecpts Int(11) Good Receipts
  PurchAPInv Int(11) Purchase AP Invoices
  ServicCall Int(11) Service Calls
  MaterBills Int(11) Meterial Bills
  WorkOrders Int(11) Work Orders
  SalesOppor Int(11) Opportunities
  ItmMasterD Int(11) Item Master Data
  CustBPMasD Int(11) Customer Bp Master Data
  SuppBPMasD Int(11) Supplier Bp Master Data
  SalOrdMinR Int(11) Min Rows Of Sales Orders
  SlDlvrMinR Int(11) Min rows Of Sales DElivery
  SlsInvMinR Int(11) Min rows Of Invoices
  PrcOrdMinR Int(11) Min rows Of Purchase Orders
  GodRcpMinR Int(11) Min rows Of Good Receipts
  WrkOrdMinR Int(11) Min rows Of work orders
  QuotMinR Int(11) Min rows Of QUOT
  RetMinR Int(11) Min rows Of RETURN
  DownMinR Int(11) Min rows Of DOWN
  ARCrdMinR Int(11) Min rows Of ARCREDIT
  GodRecMinR Int(11) Min rows Of GOODREC
  APRetMinR Int(11) Min rows Of APRETURN
  APDwnMinR Int(11) Min rows Of APDOWN
  APInvMinR Int(11) Min rows Of APINVOICE
  APCrdMinR Int(11) Min rows Of APCREDIT
  SalOrdMaxR Int(11) Max Rows Of Sales Orders
  SlDlvrMaxR Int(11) Max rows Of Sales DElivery
  SlsInvMaxR Int(11) Max rows Of Invoices
  PrcOrdMaxR Int(11) Max rows Of Purchase Orders
  GodRcpMaxR Int(11) Max rows Of Good Receipts
  WrkOrdMaxR Int(11) Max rows Of work orders
  QuotMaxR Int(11) Max rows Of QUOT
  RetMaxR Int(11) Max rows Of RETURN
  DownMaxR Int(11) Max rows Of DOWN
  ARCrdMaxR Int(11) Max rows Of ARCREDIT
  GodRecMaxR Int(11) Max rows Of GOODREC
  APRetMaxR Int(11) Max rows Of APRETURN
  APDwnMaxR Int(11) Max rows Of APDOWN
  APInvMaxR Int(11) Max rows Of APINVOICE
  APCrdMaxR Int(11) Min rows Of APCREDIT
  NoPickLst Int(11) No of Picklists in system
  MaxLnPkLst Int(11) Maximum Lines in Pick List
  MinLnPkLst Int(11) Minimum Lines in Pick List
  MaxChldBm Int(11) Maximum children per BOM
  NoProdOrd Int(11) Number of Production order
  NoSrlNum Int(11) No of Serial number items
  NoBatchNum Int(11) No of Batch number items
  StockTras Int(11) Number of Stock Transfers
  MaxRStTrs Int(11) Max num of rows per stock tran
  MinRStTrs Int(11) Min num of rows per stock tran
  NoPriceLst Int(11) 'Number of Price Lists

# SEWH1 - 
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MachineNam, CompDbNam, ID
Fields (name type(len) description [values] ->parent table):
  MachineNam nVarChar(254) Machine Name
  CompDbNam nVarChar(100) Company Db Name
  ID Int(11) AddOn ID
  Name nVarChar(40) AddOn Name
  Version nVarChar(13) AddOn Version
  Status nVarChar(50) AddOn Status
  InstStatus VarChar(1) AddOn Installation Status default=P [I=Installed, P=Pending]
  EwaSentDat nVarChar(10) EWA Sent Date

# SEWHW - 
Module: General | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MachineNam, CompDbNam
Fields (name type(len) description [values] ->parent table):
  MachineNam nVarChar(254) Machine Name
  CompDbNam nVarChar(100) Company Db Name
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  CustNumber nVarChar(100) Customer Number
  OsType nVarChar(64) OS Type
  OsVersion nVarChar(32) OS Version
  VendorIden nVarChar(254) Vendor Identity
  CpuType nVarChar(32) CPU TYPE
  NumOfCPUs Int(11) Number Of CPUs
  PhysMemory Int(11) Physical Memory
  ServerFlag VarChar(1) Server Flag (Is Server?) [0=No, 1=Yes]
  TotDskSpac nVarChar(16) Total Disk Space
  FreDskSpac nVarChar(16) Free Disk Space
  UseDskSpac nVarChar(16) Used Disk Space
  CRRntmVer nVarChar(100) CR Runtime Version
  BOBIPltVer nVarChar(100) BO BI Platform Version
  CRDsgnrVer nVarChar(100) CR Designer Version
  CRIntPgVer nVarChar(100) CR Integration Package Version
  NETFrmVer nVarChar(254) .NET Framework Version
  NETFrmSDKV nVarChar(254) .NET Framework SDK Version
  MmrMngSett nVarChar(254) Memory Management Settings
  B1ClntPltf nVarChar(10) BusinessOne Client Platform

# SEWIC - 
Module: General | 41 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbName
Fields (name type(len) description [values] ->parent table):
  CompanyNam nVarChar(100) CompanyName
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  EwaSentTim nVarChar(8) EWA Sent Time
  CustNumber VarChar(1) Customer Number
  CustName VarChar(1) Customer Name
  CustConPer VarChar(1) Customer contact person
  CustEmail nVarChar(100) Customer Email
  PartnerNam nVarChar(100) Partner Name
  PartConPer VarChar(1) Partnercontact person
  PartEmail nVarChar(100) Partner Email
  PartEmail2 VarChar(1) Partner Email 2
  CompDbName nVarChar(100) Company DB Name
  CompDbVer nVarChar(32) Compnay DB Version
  SentUser nVarChar(30) Sent User
  B1Version nVarChar(32) B1 Version
  B1Suppack nVarChar(128) B1 Support Pack
  B1Patch nVarChar(128) B1 Patch
  UiApiVer nVarChar(32) UI API Version
  InstallNum nVarChar(128) Installation Number
  SystemNum nVarChar(128) System Number
  LicenseNum nVarChar(128) License Number
  SystemStat VarChar(1) System Status
  DbType nVarChar(64) DB Type
  DbVersion nVarChar(32) DB Version
  CommLogPat nVarChar(254) SBo-Common Log Path
  CommLogSiz Int(11) SBO-Common Log Size
  CommRecovM nVarChar(32) SBO-Common Recovery Model
  AOFramewor VarChar(1) Addon Framwork
  AODtw VarChar(1) Addon DTW
  AOSupTools nVarChar(12) Addon Support Tools
  AODateV nVarChar(12) Addon Date V
  AOAld nVarChar(12) Addon Ald
  AOBcSets nVarChar(12) Addon BC Sets
  AOElster nVarChar(12) Addon Elster
  AOFixAsset nVarChar(12) Addon Fixed Assets
  AOIntrStat nVarChar(12) Addon Intra Stat
  AOOutlookI nVarChar(12) Addon Outlook integration
  AOPayEngin nVarChar(12) Addon Payment Engine
  AOStampIt nVarChar(12) Addon Stamp it
  CompRecovM nVarChar(32) Company Recover Model

# SEWLA - 
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MachineNam
Fields (name type(len) description [values] ->parent table):
  MachineNam nVarChar(254) Machine Name
  IsErr nVarChar(4) Is Error InLog

# SEWSN - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MachineNam, CompDbNam
Fields (name type(len) description [values] ->parent table):
  MachineNam nVarChar(64) Machine Name
  CompDbNam nVarChar(100) Company Db Name
  CollecStat Int(11) Collection Status default=0 [0=No Collection, 1=In Process, 2=Completed]
  SentUser nVarChar(30) Sent User
  CompleDate nVarChar(10) Completion Date

# SEWST - 
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(30) Name
  U_SentDate nVarChar(10) Sent Date
  U_SentTime nVarChar(8) Sent Time
  U_UserID nVarChar(8) User ID
  U_RCode nVarChar(3) Return Code
  U_RInfo nVarChar(254) Return info
  U_AutoSent VarChar(1) Is schedule sent or manual

# SEWSY - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: S_USER
Fields (name type(len) description [values] ->parent table):
  S_USER nVarChar(16) Absolute Key
  SmpSendAdd nVarChar(254) Smp Server URL
  SmpInboAdd nVarChar(254) Smp user Inbox URL
  CollecData VarChar(1) Communication and trigger flag default=N [Y=CollectData, N=DontCollectData]
  FindSolAdd nVarChar(254) Find Solution URL
  FeedOptAdd nVarChar(254) Feedback Option URL

# SEWU - 
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: S_USER
Fields (name type(len) description [values] ->parent table):
  S_USER nVarChar(16) S-Username
  S_PASS Text(16) S-Password

# SEWU1 - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam, TblId
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  TblId nVarChar(20) Table Id
  UDFNum Int(11) number of UDFs
  TotUdfSz Int(11) Total UDFs size per table

# SEWU2 - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam, FMSFormId
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  FMSFormId nVarChar(20) FMS FORM ID
  NoFMS Int(11) Number Of FMS

# SEWUA - 
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  NoUdfDb Int(11) number of UDFs
  NoTblUdf Int(11) UDFs per table
  NoAutoFMS Int(11) Auto Refresh in use
  NoRegFMS Int(11) No FMS with Refresh Regular
  NoCustTmpl Int(11) No of customised Document

# SEWUS - 
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry
  CompanyNam nVarChar(100) CompanyName
  SmpTableId nVarChar(3) Smp Table ID
  EwaSentDat nVarChar(10) EWA Sent Date
  CustNumber VarChar(1) Customer Number
  CompDbName nVarChar(100) Company DB Name
  EwaUserCod nVarChar(16) Ewa User Code
  EwaUserNam nVarChar(16) Ewa User Name
  EwaUserSup VarChar(1) Ewa Is super user default=0 [1=Yes, 0=No]

# SEWUT - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam, transid
Fields (name type(len) description [values] ->parent table):
  CompDbNam nVarChar(100) Company Db Name
  transid nVarChar(10) transid
  transtype nVarChar(3) transtype
  installmen nVarChar(10) installments

# SFDK - 
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Feedback DI
  WindowID nVarChar(254) Window ID
  DBName nVarChar(100) Company DB Name
  UserSign Int(11) User Sign
  Date Date(8) Feedback Date
  Time Int(6) Feedback Time
  Version nVarChar(254) Version including patch number
  LOC nVarChar(3) Localization
  UILang nVarChar(3) UI Language
  Feedback Int(6) Feedback
  GUID nVarChar(32) GUID
  StrLID nVarChar(11) String List ID
  StrIID nVarChar(11) String Index ID
  MsgText nVarChar(254) Message text

# SFMD - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  Metadefs Text(16) Metadefs.bin
  ClusterID nVarChar(3) Cluster Identification
  PatchLevel nVarChar(50) Application Patch Level

# SHLP - Server Help
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LangCode
Fields (name type(len) description [values] ->parent table):
  LangCode nVarChar(5) Language Code
  HelpImage Text(16) Help Image
  Version Int(11) Help Version
  helpPath Text(16) Help Path

# SHQR - Upgrade queries history
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version, TableId, Instance, DoBefore, ServerType
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  TableId nVarChar(4) Metadata CAB
  Instance Int(6) Query instance
  DoBefore VarChar(1) Do Before default=Y [Y=Yes, N=No]
  QurString Text(16) Query String
  ServerType Int(11) Server Type default=0

# SINF - Server Info
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  Flags nVarChar(100) Flags
  UpgCab Text(16) Upg CAB
  AppDate Date(8) Application Date
  ClusterID nVarChar(3) Cluster Identification
  AppTime Int(6) Application Time
  ShrPath Text(16) Shared folder path
  Algo Int(6) Encryption Algorithm.
  PatchLevel nVarChar(50) Application Patch Level
  BuildDesc nVarChar(50) Build Descriptor
  IsPALInit VarChar(1) Is PAL Initialize or Not default=N
  FP nVarChar(50) Application Feature Pack

# SINP - [SINP]
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SupplCode
Fields (name type(len) description [values] ->parent table):
  SupplCode nVarChar(128) Supplier code
  SubDate Date(8) Submission date
  SubTime Int(6) Submission time
  LogNum Int(11) ??' ?????

# SLIC - 
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LSRV
Fields (name type(len) description [values] ->parent table):
  LSRV nVarChar(254) license server path default=-1
  AliasUpd nVarChar(254) Installation Date

# SLOG - 
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsKey
Fields (name type(len) description [values] ->parent table):
  LogConfig Text(16) Log configuration
  UseDBConf VarChar(1) Use DB configuration
  ActLog VarChar(1) Activate Log
  ModDate Date(8) DB log modification date
  LogDefConf Text(16) Log Default configuration
  ReposConf Text(16) Log Repository Configuration
  AbsKey Identity(11) Primary Key
  ModTime Int(6) DB log modification time

# SLOGR - 
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogKey
Fields (name type(len) description [values] ->parent table):
  LogKey Identity(11) Table key
  CompName nVarChar(100) Computer Name
  LoginName nVarChar(100) Login Name
  ProcessID Int(11) Process ID
  LogDate Date(8) Log file date
  LogFile Text(16) Log file blob
  Archive Int(11) Archive type default=0 [1=AuditArchive, 0=NotArchive]
  CrashTime nVarChar(14) Time of the crash

# SLSC - Local Settings Components CABs
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LocCode, Code
Fields (name type(len) description [values] ->parent table):
  LocCode nVarChar(3) LocalCode
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  Type VarChar(1) Type [C=Chart of accounts, R=Reports, O=Objects, P=CR Report, L=CR Layout, H=HANA Content]
  DataCab Text(16) Data CAB
  System VarChar(1) System package default=N [Y=Yes, N=No]

# SLSD - Local Settings
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(3) Code
  Name nVarChar(100) Name
  DefLang Int(11) default language

# SLSP - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompID
Fields (name type(len) description [values] ->parent table):
  CompID nVarChar(36) Component ID
  CompType nVarChar(50) Component Type
  CompIdent nVarChar(254) Component Identity
  TimeStamp nVarChar(20) Time Stamp

# SLSPP - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParamID, CompID
Fields (name type(len) description [values] ->parent table):
  ParamID nVarChar(36) Parameter ID
  CompID nVarChar(36) Component ID
  ParamKey nVarChar(50) Parameter Key
  ParamValue Text(16) Parameter Value

# SOUT - [SOUT]
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogNum
  STATUS: Status
Fields (name type(len) description [values] ->parent table):
  LogNum Int(11) ??' ?????
  Company nVarChar(128) Company
  USER_CODE nVarChar(8) User code
  Object Int(11) Object
  ObjectAbs Int(11) ObjectAbs
  SubDate Date(8) Submission date
  SubTime Int(6) Submission time
  ActDate Date(8) Action date
  ActTime Int(6) Action time
  Status VarChar(1) Status default=C [C=Check in, P=In process, E=Error, S=Success, I=Success with info]
  ErrCode Int(11) Error code
  ErrMessage Text(16) Error message

# SPAR - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Owner, Name
Fields (name type(len) description [values] ->parent table):
  Owner nVarChar(40) Owner
  Name nVarChar(254) Name
  Value Text(16) Value

# SPRM - [SPRM]
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs entry
  SaCoName nVarChar(128) SAP company name
  MySAPCard nVarChar(128) My SAP card
  MeInSAP nVarChar(128) Me in SAP
  AttUser nVarChar(128) Attending user

# SRGC - Registred companies
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: dbName, dbUser
Fields (name type(len) description [values] ->parent table):
  dbName nVarChar(100) DB Name
  cmpName nVarChar(100) Comp. Name
  versStr nVarChar(13) Version
  dbUser nVarChar(50) SQL User
  LOC nVarChar(100) localization
  cmpStatus VarChar(1) Comp. Status

# SSEN - 
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID nVarChar(254) Session ID
  ServerName nVarChar(254) Server Name
  Port Int(11) Port Number
  ReqEnter Int(11) Request Enter Time
  ReqLeave Int(11) Request Leave Time
  DBServer nVarChar(254) DB Server Name
  DBName nVarChar(254) Company DB Name
  UserCode nVarChar(64) Company User Code
  UserPwd nVarChar(254) Company User
  Language Int(11) Language Code

# STNG - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: lang, num
Fields (name type(len) description [values] ->parent table):
  lang Int(11) Language
  num Int(11) Number
  string nVarChar(254) String

# STRI - String list item resource
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, Num, ResCode, RevCode
  UNIQUE_ID U: Name, UniqueID
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Name nVarChar(64) STRL name
  Num Int(11) String number
  StrIndex Int(11) String Index default=0
  ItemString nVarChar(254) Item string
  UniqueID nVarChar(10) Unique ID
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# STRL - String List resource
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, ResCode, RevCode
  NUM U: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Name nVarChar(64) STRL name
  Num Int(11) STRL number
  MaxUnique Int(11) Max Unique
  RobjCode Int(11) Imp Exp Obj Code default=0
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# SWDP - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DeploymtID
Fields (name type(len) description [values] ->parent table):
  DeploymtID Identity(11) Workflow Deployment ID
  Name nVarChar(254) Deployment Name
  DeploymtDt Date(8) Deployment Date

# SWEI - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EngineAddr
Fields (name type(len) description [values] ->parent table):
  EngineAddr nVarChar(200) Workflow Engine Address
  EngineVer nVarChar(30) Workflow Engine Version
  HashCode Int(11) Random Generated Hash Code
  StartTime nVarChar(50) Start Date of Workflow Engine
  LastUpdate nVarChar(50) Last Update Date and Time
  NextUpdate nVarChar(50) Expected next update date
  EngCmpnys Text(16) Company dbs that support workf

# SWFQ - 
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SequenceID
Fields (name type(len) description [values] ->parent table):
  SequenceID Int(11) Sequence ID
  SourceDB nVarChar(100) Source DB
  Timestamp nVarChar(20) Timestamp
  ObjectType nVarChar(30) Object Type
  TransType VarChar(1) Transaction Type [A=Add, U=Update, C=Cancel, D=Delete]
  FieldsInKe Int(11) Number of fields in key
  FieldNames nVarChar(254) Key Field Names
  FieldValue nVarChar(254) Key Field Values
  UserID nVarChar(25) UserID
  TaskID nVarChar(64) TaskID
  TrigEvntID nVarChar(64) Trigger Event ID
  TrigParams Text(16) Trigger parameters

# SWID - 
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name
Fields (name type(len) description [values] ->parent table):
  Name nVarChar(200) Name
  Value Int(11) Value
  Rev Int(11) Revision
  LastUpdate nVarChar(50) Last update date and time

# SWPD - 
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ProcDefID
Fields (name type(len) description [values] ->parent table):
  ProcDefID Identity(11) WF process definition ID
  DeploymtID Int(11) Deployment ID ->SWDP
  ResourceID Int(11) Resource ID ->SWRS
  Key nVarChar(254) WF process definition key
  Name nVarChar(254) WF process definition name
  Desc Text(16) WF process definition
  Category nVarChar(50) WF category uri
  Version nVarChar(13) WF process definition version
  ProcType nVarChar(20) Process definition type
  Status VarChar(1) Status during import default=M [M=Importing, P=Imported, F=Import failed, I=Inactive, A=Active, E=Activate failed, D=Deleted]
  StartType VarChar(1) Start Type default=M [M=Manual Start, T=Timer Start, C=Conditional Start]

# SWRS - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResourceID
Fields (name type(len) description [values] ->parent table):
  ResourceID Identity(11) Workflow Resource ID
  Name nVarChar(254) Workflow Resouce Name
  Version nVarChar(13) Resource Version
  DeploymtID Int(11) Deployment ID ->SWDP
  Bytes Text(16) Resource Library

# SXRCD - XLR Class Definitions
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: classid
Fields (name type(len) description [values] ->parent table):
  classid Int(11) classid
  name nVarChar(50) name
  descriptio nVarChar(254) description
  created Date(8) created
  lastmodifi Date(8) lastmodified

# SXRCO - XLR Context
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContextId
Fields (name type(len) description [values] ->parent table):
  ContextId Int(11) ContextId
  B1User nVarChar(50) B1User
  Password nVarChar(50) Password
  Language Int(11) Language
  Applicatio Int(11) ApplicationId
  LogonDate Date(8) LogonDate
  ExpiryDate Date(8) ExpiryDate
  Constrain nVarChar(250) Constraint
  DB nVarChar(250) DB
  ForceCust Int(11) ForceCustomConnect default=0
  Roles nVarChar(250) Roles
  InvalidTer Text(16) InvalidTerms

# SXRDB - XLR Databases
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DatabaseId
Fields (name type(len) description [values] ->parent table):
  Name nVarChar(50) Name
  ConnectStr nVarChar(250) ConnectString
  Constrain nVarChar(250) Constraint
  DatabaseId nVarChar(250) DatabaseId

# SXRDF - XLR Definition
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DimFilterI
  second U: RoleId, DimId
Fields (name type(len) description [values] ->parent table):
  DimFilterI Identity(11) DimFilterId
  RoleId nVarChar(16) RoleId
  DimId nVarChar(20) DimId
  ModuleId nVarChar(20) ModuleId
  AccessType Int(11) AccessType default=0
  ReadInclud Text(16) ReadIncludeExpr

# SXREL - XLR Event Log
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EventId
Fields (name type(len) description [values] ->parent table):
  EventId Int(11) EventId
  Type Int(11) Type
  Text Text(16) Text
  Date Date(8) Date

# SXRET - XLR Enum Types
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: enumid
Fields (name type(len) description [values] ->parent table):
  enumid Int(11) enumid
  name nVarChar(50) name
  type Int(11) type

# SXREV - XLR Enum Values
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: enumid, name
Fields (name type(len) description [values] ->parent table):
  enumid Int(11) enumid
  name nVarChar(50) name
  ivalue Int(11) ivalue
  cvalue nVarChar(50) cvalue

# SXRFU - XLR Functions
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FunctionID
Fields (name type(len) description [values] ->parent table):
  FunctionID nVarChar(254) FunctionID
  FunctionTe Text(16) FunctionText

# SXRIN - XLR Instances
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: InstId
Fields (name type(len) description [values] ->parent table):
  InstId Identity(11) InstId
  ContextId Int(11) ContextId
  Text Text(16) Text

# SXRME - XLR Members
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MemberId
  second U: RoleId, DomainType, Name, Domain
Fields (name type(len) description [values] ->parent table):
  MemberId Identity(11) MemberId
  RoleId nVarChar(16) RoleId
  DomainType Int(11) DomainType default=0
  MemberType Int(11) MemberType default=0
  Name nVarChar(244) Name
  Domain nVarChar(244) Domain
  Descriptio nVarChar(254) Description

# SXRNO - XLR Notes
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: noteid
Fields (name type(len) description [values] ->parent table):
  noteid nVarChar(32) noteid
  notetext Text(16) notetext
  modified Date(8) modified
  access nVarChar(50) access

# SXROA - XLR Object Access
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectAcce
Fields (name type(len) description [values] ->parent table):
  ObjectAcce Identity(11) ObjectAccessId
  RoleId nVarChar(16) RoleId
  ObjId nVarChar(254) ObjId
  SubId nVarChar(50) SubId
  AccessLeve Int(11) AccessLevel

# SXROB - XLR Objects
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: objid
Fields (name type(len) description [values] ->parent table):
  objid Int(11) objid
  classid Int(11) classid default=0
  name nVarChar(50) name
  descriptio nVarChar(254) description
  created Date(8) created
  lastmodifi Date(8) lastmodified
  access nVarChar(50) access
  searchstri nVarChar(200) searchstring

# SXRPD - XLR Property Definitions
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: propdefid
Fields (name type(len) description [values] ->parent table):
  propdefid Int(11) propdefid
  classid Int(11) classid
  seqno Int(11) seqno default=0
  name nVarChar(50) name
  category nVarChar(50) category default='General'
  descriptio nVarChar(254) description
  type Int(11) type default=0
  minoccurs Int(11) minoccurs default=0
  maxoccurs Int(11) maxoccurs default=999999
  classrefid Int(11) classrefid default=0
  enumid Int(11) enumid default=0 [0=]

# SXRPR - XLR Properties
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: propid
Fields (name type(len) description [values] ->parent table):
  propid Identity(11) propid
  objid Int(11) objid
  propdefid Int(11) propdefid
  ivalue Int(11) ivalue
  fvalue Num(19,6) fvalue
  cvalue Text(16) cvalue

# SXRRE - XLR Relations
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: relid
  second U: objidfrom, propdefid, seqno
Fields (name type(len) description [values] ->parent table):
  relid Identity(11) relid
  objidfrom Int(11) objidfrom default=0
  propdefid Int(11) propdefid default=0
  seqno Int(11) seqno default=0
  objidto Int(11) objidto default=0

# SXRRO - XLR Relations
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RoleId
  second U: AppId, DatabaseId, Name
Fields (name type(len) description [values] ->parent table):
  RoleId nVarChar(16) RoleId
  AppId nVarChar(225) AppId
  DatabaseId nVarChar(225) DatabaseId
  Name nVarChar(50) Name
  Descriptio nVarChar(254) Description

# SXRSS - XLR Security Settings
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SecuritySe
  second U: AppId, DatabaseId, ModuleId, Label
Fields (name type(len) description [values] ->parent table):
  SecuritySe Identity(11) SecuritySettingId
  AppId nVarChar(218) AppId
  DatabaseId nVarChar(218) DatabaseId
  ModuleId nVarChar(20) ModuleId default='' [''=]
  Label nVarChar(50) Label
  Value Text(16) Value

# SXRTE - XLR Terms
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TermId, Language
Fields (name type(len) description [values] ->parent table):
  TermId nVarChar(50) TermId
  Language Int(11) Language
  Type Int(11) Type
  Term Text(16) Term

# TABL - Table resource
Module: General | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name, ResCode, RevCode
  NUM U: Num
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Name nVarChar(64) Table name
  Num Int(11) Table number
  DoColor VarChar(1) Use color table default=0 [0=No, 1=Yes]
  BorderRed Int(11) Border red
  BorderGrn Int(11) Border green
  BorderBlue Int(11) Border blue
  BgRed Int(11) Background red default=65535
  BgGreen Int(11) Background green default=65535
  BgBlue Int(11) Background blue default=65535
  CellHeight Int(11) Cell height
  TitleHeigt Int(11) Title height
  Width Int(11) Width
  MaxUnique Int(11) Max Unique
  UsrSgnAttr Int(11) User Sign For Attribs Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# TCN1 - Tracking Note - Line Data
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OTCN
  LineNum Int(11) Row Number
  ItemCCDNum nVarChar(20) Item CCD Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  CntrOrigin nVarChar(3) Country/Region of Origin
  AccQtyAP Num(19,6) Accumulated A/P Quantity
  AccQtyAR Num(19,6) Accumulated A/R Quantity
  AccRelQty Num(19,6) Accumulated Relocated Quantity
  CstGrpCode Int(6) Customs Group ->OARG

# TCN2 - Tracking Note - Brokers
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OTCN
  LineNum Int(11) Row Number
  CardCode nVarChar(15) BP Code ->OCRD
  AgrNo Int(11) Blanket Agreement Number ->OOAT

# TCN3 - Tracking Note - Warehouse Qty
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, WhsCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OTCN
  LineNum Int(11) Row Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  QtyOnHand Num(19,6) On Hand Quantity

# TSCD - Schedules
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrvcName
  NAME_SCHED U: SrvcName, LastExDate
Fields (name type(len) description [values] ->parent table):
  SrvcName nVarChar(20) Service application name
  SchedType VarChar(1) Type of schedule default=P [P=Suspended / Paused, O=Once, S=Every X seconds, M=Every X minutes, D=Daily, W=Weekly, T=Monthly]
  SchedDate Date(8) Scheduled date
  SchedDay nVarChar(2) Scheduled day default=1
  Interval Int(11) Interval
  LastExDate Date(8) Last execution date
  AutoStart VarChar(1) Auto run when OS starts default=Y [Y=Yes, N=NO]

# TSH1 - Time Sheet - Rows
Module: General | 31 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LineID Int(11) Row No.
  Date Date(8) Date
  ActType Int(11) Activity Type ->PMC5
  LaborItem nVarChar(50) Labor Item No.
  StartTime Int(11) Start Time
  EndTime Int(11) End Time
  Workorder Int(11) Workorder Doc. Entry ->OWOR
  WorAbs Int(11) Workorder Abs. Entry
  ServCall Int(11) Service Call ID ->OSCL
  CostCenter nVarChar(8) Cost Center
  FiProject nVarChar(20) Financial Project
  Location Int(11) Location
  GPSData nVarChar(50) GPS Data
  Branch Int(11) Branch ID ->OBPL
  Break Int(11) Break
  NonBillTm Int(11) Nonbillable Time
  EffectTm Int(11) Effective Time
  BillableTm Int(11) Billable Time
  FullDay VarChar(1) Full Day default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ProjectID Int(11) Project or Subproject ID
  Subproject Int(11) Subproject ID
  StageID Int(11) Stage ID
  Charged Num(19,6) Charged
  Chargeable VarChar(1) Chargeable [Yes/No] default=Y [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV
  BreakHr Num(19,6) Break Hours
  NonBillHr Num(19,6) Non-Billable Hours
  EffectHr Num(19,6) Effective Hours
  BillableHr Num(19,6) Billable Hours

# TTP1 - ToolTip Preview - Rows
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, ObjectId, DataKey
Fields (name type(len) description [values] ->parent table):
  UserSign Int(6) User Signature ->OUSR
  ObjectId Int(11) Object ID
  DataKey nVarChar(50) Data Key
  VisOrder Int(11) Visual Order
  IsVisible VarChar(1) Visible default=Y [Y=Yes, N=No]

# TYPR - 
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CODE, Local, ResCode, RevCode
  TYPE: CODE
Fields (name type(len) description [values] ->parent table):
  CODE nVarChar(4) Report Type
  NAME nVarChar(250) Type Name
  DEFLT_REP nVarChar(8) Standard Report
  Local nVarChar(2) Localization
  Created Date(8) Creation Date
  Updated Date(8) Updated Date
  UsrSgnStr Int(11) User Sign For Strings Change default=-1
  ResCode Int(11) Resource Code from RSBD default=-1
  RevCode Int(11) Revision Code default=-1

# TZLI - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) id
  TimeZone nVarChar(100) time zone default=1 [1=(GMT-12:00) International Date Line West, 2=(GMT-11:00) Midway Island, Samoa, 3=(GMT-10:00) Hawaii, 4=(GMT-09:00) Alaska, 5=(GMT-08:00) Tijuana, Baja California, 6=(GMT-08:00) Pacific Time (US & Canada), 7=(GMT-07:00) Mountain Time (US & Canada), 8=(GMT-07:00) Chihuahua, La Paz, Mazatlan - Old, 9=(GMT-07:00) Chihuahua, La Paz, Mazatlan - New, 10=(GMT-07:00) Arizona, 11=(GMT-06:00) Saskatchewan, 12=(GMT-06:00) Guadalajara, Mexico City, Monterrey - Old, 13=(GMT-06:00) Guadalajara, Mexico City, Monterrey - New, 14=(GMT-06:00) Central Time (US & Canada), 15=(GMT-06:00) Central America, 16=(GMT-05:00) Indiana (East), 17=(GMT-05:00) Eastern Time (US & Canada), 18=(GMT-05:00) Bogota, Lima, Quito, Rio Branco, 19=(GMT-04:30) Caracas, 20=(GMT-04:00) Santiago, 21=(GMT-04:00) Manaus, 22=(GMT-04:00) La Paz, 23=(GMT-04:00) Atlantic Time (Canada), 24=(GMT-03:30) Newfoundland, 25=(GMT-03:00) Montevideo, 26=(GMT-03:00) Greenland, 27=(GMT-03:00) Georgetown, 28=(GMT-03:00) Buenos Aires, 29=(GMT-03:00) Brasilia, 30=(GMT-02:00) Mid-Atlantic, 31=(GMT-01:00) Cape Verde Is., 32=(GMT-01:00) Azores, 33=(GMT) Casablanca, 34=(GMT) Greenwich Mean Time : Dublin, Edinburgh, Lisbon, London, 35=(GMT) Monrovia, Reykjavik, 36=(GMT+01:00) Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna, 37=(GMT+01:00) Belgrade, Bratislava, Budapest, Ljubljana, Prague, 38=(GMT+01:00) Brussels, Copenhagen, Madrid, Paris, 39=(GMT+01:00) Sarajevo, Skopje, Warsaw, Zagreb, 40=(GMT+01:00) West Central Africa, 41=(GMT+02:00) Amman, 42=(GMT+02:00) Athens, Bucharest, Istanbul, 43=(GMT+02:00) Beirut, 44=(GMT+02:00) Cairo, 45=(GMT+02:00) Harare, Pretoria, 46=(GMT+02:00) Helsinki, Kyiv, Riga, Sofia, Tallinn, Vilnius, 47=(GMT+02:00) Jerusalem, 48=(GMT+02:00) Minsk, 49=(GMT+02:00) Windhoek, 50=(GMT+03:00) Baghdad, 51=(GMT+03:00) Kuwait, Riyadh, 52=(GMT+03:00) Moscow, St. Petersburg, Volgograd, 53=(GMT+03:00) Nairobi, 54=(GMT+03:00) Tbilisi, 55=(GMT+03:30) Tehran, 56=(GMT+04:00) Abu Dhabi, Muscat, 57=(GMT+04:00) Baku, 58=(GMT+04:00) Caucasus Standard Time, 59=(GMT+04:00) Port Louis, 60=(GMT+04:00) Yerevan, 61=(GMT+04:30) Kabul, 62=(GMT+05:00) Ekaterinburg, 63=(GMT+05:00) Islamabad, Karachi, 64=(GMT+05:00) Tashkent, 65=(GMT+05:30) Chennai, Kolkata, Mumbai, New Delhi, 66=(GMT+05:30) Sri Jayawardenepura, 67=(GMT+05:45) Kathmandu, 68=(GMT+06:00) Almaty, Novosibirsk, 69=(GMT+06:00) Astana, Dhaka, 70=(GMT+06:30) Yangon (Rangoon), 71=(GMT+07:00) Bangkok, Hanoi, Jakarta, 72=(GMT+07:00) Krasnoyarsk, 73=(GMT+08:00) Beijing, Chongqing, Hong Kong, Urumqi, 74=(GMT+08:00) Irkutsk, Ulaan Bataar, 75=(GMT+08:00) Kuala Lumpur, Singapore, 76=(GMT+08:00) Perth, 77=(GMT+08:00) Taipei, 78=(GMT+09:00) Osaka, Sapporo, Tokyo, 79=(GMT+09:00) Seoul, 80=(GMT+09:00) Yakutsk, 81=(GMT+09:30) Adelaide, 82=(GMT+09:30) Darwin, 83=(GMT+10:00) Brisbane, 84=(GMT+10:00) Canberra, Melbourne, Sydney, 85=(GMT+10:00) Guam, Port Moresby, 86=(GMT+10:00) Hobart, 87=(GMT+10:00) Vladivostok, 88=(GMT+11:00) Magadan, Solomon Is., New Caledonia, 89=(GMT+12:00) Auckland, Wellington, 90=(GMT+12:00) Fiji, Kamchatka, Marshall Is., 91=(GMT+13:00) Nuku'alofa]
  Offset Int(11) offset from GMT/UTC time default=1 [1=-720, 2=-660, 3=-600, 4=-540, 5=-480, 6=-480, 7=-420, 8=-420, 9=-420, 10=-420, 11=-360, 12=-360, 13=-360, 14=-360, 15=-360, 16=-300, 17=-300, 18=-300, 19=-270, 20=-240, 21=-240, 22=-240, 23=-240, 24=-210, 25=-180, 26=-180, 27=-180, 28=-180, 29=-180, 30=-120, 31=-60, 32=-60, 33=0, 34=0, 35=0, 36=60, 37=60, 38=60, 39=60, 40=60, 41=120, 42=120, 43=120, 44=120, 45=120, 46=120, 47=120, 48=120, 49=120, 50=180, 51=180, 52=180, 53=180, 54=180, 55=210, 56=240, 57=240, 58=240, 59=240, 60=240, 61=270, 62=300, 63=300, 64=300, 65=330, 66=330, 67=345, 68=360, 69=360, 70=390, 71=420, 72=420, 73=480, 74=480, 75=480, 76=480, 77=480, 78=540, 79=540, 80=540, 81=570, 82=570, 83=600, 84=600, 85=600, 86=600, 87=600, 88=660, 89=720, 90=720, 91=780]

# UBVL - Serial Numbers and Batch Valuation Log
Module: General | 36 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocEntry Int(11) Doc. Abs. Entry
  DocLineNum Int(11) Doc. Line Number
  DocType Int(11) Transact. Type default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 13=A/R Invoice, 15=Delivery, 16=Returns, 17=Sales Order, 18=A/P Invoice, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase Order, 23=Sales Quotation, 59=Goods Receipt, 67=Inventory Transfer, 69=Landed Costs, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment]
  ActionType Int(11) Action Type default=5 [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]
  AccumType Int(11) Accumulator Type default=0 [0=ACCUM_EMPTY, 1=ACCUM_ON_HAND, 2=ACCUM_COMMITTED, 3=ACCUM_ON_ORDER, 4=ACCUM_CONSIGNATION, 5=ACCUM_COUNTED]
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers]
  CreateDate Date(8) Generation Date
  CreateTime Int(6) Generation Time
  ItemCode nVarChar(50) Item No.
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Batch Number
  MdAbsEntry Int(11) MD Abs. Entry
  TrValApply VarChar(1) Apply Transaction Value default=Y [Y=Yes, N=No]
  TransValue Num(19,6) Transaction Value
  InvValue Num(19,6) Inventory Value
  CogsValue Num(19,6) Cogs Value
  Quantity Num(19,6) Quantity
  OverlapQty Num(19,6) Overlap Quantity
  CogsQty Num(19,6) Cogs Quantity
  CalcPrice Num(19,6) Calculated Price
  PriceDiff Num(19,6) Price Difference
  InvDiff Num(19,6) Inventory Difference
  Balance Num(19,6) Batch Balance
  AccTotal Num(19,6) Total Accumulator
  AccQty Num(19,6) Quantity-Out Accumulator
  AccNegQ Num(19,6) Quantity-In Accumulator
  ILMEntry Int(11) ILM Entry
  ITLEntry Int(11) ITL Entry
  CostQty Num(19,6) Cost Quantity
  Cost Num(19,6) Cost
  BaseDocEn Int(11) Base Doc. Abs. Entry
  BaseLnNum Int(11) Base Doc. Line Number
  DeltaAccT Num(19,6) Delta Total Accumulator
  RowAction Int(11) Row Action Type [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]

# UDAB - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  name nVarChar(50) Dashboard Name
  type VarChar(1) Dashboard Type
  scriptId nVarChar(36) Script Id

# UFRM - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: guid
  FATHER_ID: fatherId
  OBJECT_ID U: objId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  formName nVarChar(254) Form Name
  objId nVarChar(36) Object Id
  frmNameSid Int(11) Form Name String Index

# UIC1 - Customized Forms in Templates
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId, FormId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  Width Int(6) Form Width
  Height Int(6) Form Height
  MenuId nVarChar(20) Menu ID

# UIC2 - Customized Forms in Template
Module: General | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId, FormId, ItemId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  ItemId nVarChar(70) Item ID
  Visible VarChar(1) Visible
  VisibleCtl VarChar(1) Visible Control
  Editable VarChar(1) Editable
  EditbleCtl VarChar(1) Editable Control
  Left Int(6) Left
  Top Int(6) Top
  Right Int(6) Right
  Bottom Int(6) Bottom
  FromPane Int(6) From Pane
  ToPane Int(6) To Pane
  UDF VarChar(1) UDF default=N
  TableName nVarChar(20) TableName

# UIC3 - Template User Customization
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId, UserID
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  UserID Int(6) User ID ->OUSR
  IsTemplate VarChar(1) Is Template

# UIC4 - Forms in Assigned Templates
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserID, FormId, TPLId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  UserID Int(6) User ID ->OUSR

# UIC5 - Customized Folders in Template
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId, FormId, ItemId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  ItemId nVarChar(20) Item ID
  Left Int(6) Left
  Right Int(6) Right
  Top Int(6) Top
  Bottom Int(6) Bottom
  CurPan Int(6) Current Pane
  Caption nVarChar(50) Caption
  GroupItem nVarChar(20) Group Item

# UIC6 - Template Group Customization
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId, GroupID
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  GroupID Int(6) Group ID ->OUGR
  IsTemplate VarChar(1) Is Template

# UICU - Customized Template
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId
  NAME_KEY U: TPLName
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID
  TPLName nVarChar(155) Template Name
  TPLDesc nVarChar(155) Template Description
  UserID Int(6) User ID
  Parent Int(6) Parent Template ID
  IsTemplate VarChar(1) Is Template

# UITE - 
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, itemOrder
  GUID U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  itemOrder Int(11) Item Order
  itemLabel nVarChar(254) Item Label
  itemType VarChar(1) Item Type
  columnId nVarChar(36) Column Id
  sonFormId nVarChar(36) Son Form Id
  note nVarChar(254) Note
  groupId nVarChar(36) Group Id
  locale nVarChar(254) Localization Flag
  locVisible nVarChar(254) Visible Settings
  labelSid Int(11) Item Name String Id
  groupIcon Int(11) Group Icon Index
  groupType VarChar(1) Group Type
  actionId nVarChar(36) ->MACT
  linkButton VarChar(1) Show Link Button default=N
  mVisible VarChar(1) Mobile Visibility

# ULNG - 
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: lang, lineNum
Fields (name type(len) description [values] ->parent table):
  lang Int(11) Language Id
  lineNum Int(11) Line Number
  string nVarChar(254) String

# UMNU - 
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: guid
  FATHER_ID: fatherId
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Fathter Id
  lineNum Int(11) Line Num
  menuName nVarChar(254) Menu Name
  linkType VarChar(1) Link Type
  linkTo nVarChar(36) LinkTo
  icon Int(11) Icon
  locale nVarChar(254) Localization Flag
  mnuNameSid Int(11) Menu String Id
  linkChart nVarChar(36) Linked Chart Id

# USR7 - Group User Association
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserId, GroupId
Fields (name type(len) description [values] ->parent table):
  UserId Int(6) User ID ->OUSR
  GroupId Int(6) Group ID ->OUGR
  Category nVarChar(155) Group Category
  StartDate Date(8) Start Date
  DueDate Date(8) Due Date

# USR8 - Point of Issue User Association
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserId, PTICode
Fields (name type(len) description [values] ->parent table):
  UserId Int(6) User ID ->OUSR
  PTICode nVarChar(5) POI Code ->OPTI

# UXILM - IVI Irrelevant Message IDs
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID
  MinMsgID Int(11) MINMessage ID
  MaxMsgID Int(11) MaxMessage ID
  DocEntry Int(11) Doc Number
  DocLineNum Int(11) Doc Row Number
  TransType Int(11) Transaction Type default=-1

# WDBD1 - Dashboard Cards
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  Content Text(16) Content
  Sys VarChar(1) Sys default=Y [Y=Yes, N=No]
  Version nVarChar(40) Version

# WFLT1 - List View Filters Conditions
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name
  CompExpr nVarChar(50) Compare Expression
  Value nVarChar(50) Value

# WFST1 - Web Client Form Setting Items
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  ItemId nVarChar(40) Item Id
  Order Int(11) Order
  Visible VarChar(1) Visible
  Editable VarChar(1) Editable
  VisInGrid VarChar(1) VisInGrid
  EditInGrid VarChar(1) EditInGrid

# WHL1 - Register of VAT Payers - List of Hashed Data
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HashData
Fields (name type(len) description [values] ->parent table):
  HashData nVarChar(128) Hash Data
  Type nVarChar(20) Type

# WHL2 - Register of VAT Payers - List of Masks
Module: General | 1 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Mask
Fields (name type(len) description [values] ->parent table):
  Mask nVarChar(50) Mask

# WHL3 - Register of VAT Payers - BPs Compared with OWHL
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, NIP, BankAcc
Fields (name type(len) description [values] ->parent table):
  LastDate Date(8) Last Date
  CardCode nVarChar(15) BP Code
  NIP nVarChar(32) Federal Tax ID
  BankAcc nVarChar(50) Bank Account

# WLPD1 - Fiori Launchpad Groups
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  GroupId nVarChar(40) Group Id
  GroupName nVarChar(100) Group Name
  Visible VarChar(1) Visible default=Y [Y=Yes, N=No]

# WLPD2 - Fiori Launchpad Tiles
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RootId, ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  RootId nVarChar(40) Root Guid
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  TileId nVarChar(40) Tile Id

# WMNU - 
Module: General | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjCode
Fields (name type(len) description [values] ->parent table):
  ObjCode Int(11) Object Code
  ObjName nVarChar(20) Object Name
  FatherID Int(11) Father Menu ID
  BrothetID Int(11) Older Brother Menu ID
  KeyNum nVarChar(100) m_KeyNum
  ExCommand nVarChar(100) m_exCommand
  Params nVarChar(100) m_params
  ParamsEx nVarChar(100) m_paramsEx
  MatchFlag nVarChar(100) m_matchFlag
  Dag nVarChar(100) m_dag
  Form nVarChar(100) m_form
  RetProc nVarChar(100) m_paRetProc
  InitMode nVarChar(100) m_initialMode
  Message nVarChar(100) m_message
  KeyStr nVarChar(100) m_keyStr
  SubType nVarChar(100) m_subType
  Condition nVarChar(254) local setting condition
  FormProc nVarChar(100) Draw Form Proc
  StrList Int(11) StrList Num

# WOBJ - Object Wizard
Module: General | 44 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjCode
  NAME U: ObjName
Fields (name type(len) description [values] ->parent table):
  ObjCode Int(11) Object Code
  ObjName nVarChar(20) Object Name
  Category VarChar(1) Category default=2 [2=Noun, 3=Operation, 4=History, 1=Abstract, 0=Not Exists]
  TableName nVarChar(20) TableName
  NOE VarChar(1) NOE or form default=N [Y=Yes, F=Form, N=None]
  ObjDesc nVarChar(254) Object Description
  FileName nVarChar(254) File Name
  Status VarChar(1) Execution Status default=D [R=Ready, P=Postponed, D=Done]
  ClassName nVarChar(100) Class Name
  AutoComp VarChar(1) OnAutoComplete default=Y [Y=Yes, N=No]
  Cancel VarChar(1) OnCancel default=N [Y=Yes, N=No]
  CanUpdate VarChar(1) OnCanUpdate default=N [Y=Yes, N=No]
  ChckDelet VarChar(1) OnCheckDelete default=N [Y=Yes, N=No]
  Close1 VarChar(1) OnClose default=N [Y=Yes, N=No]
  Create1 VarChar(1) OnCreate default=Y [Y=Yes, N=No]
  CreateDef VarChar(1) OnCreateDefaults default=N [Y=Yes, N=No]
  Delete1 VarChar(1) OnDelete default=Y [Y=Yes, N=No]
  GetByKey VarChar(1) OnGetByKey default=N [Y=Yes, N=No]
  GetNextSer VarChar(1) OnGetNextSerial default=N [Y=Yes, N=No]
  InitData VarChar(1) OnInitData default=N [Y=Yes, N=No]
  InitFlow VarChar(1) OnInitFlow default=N [Y=Yes, N=No]
  EndSucFlow VarChar(1) OnEndSuccessfulFlow default=N [Y=Yes, N=No]
  IsValid VarChar(1) OnIsValid default=Y [Y=Yes, N=No]
  PutSignate VarChar(1) OnPutSignature default=N [Y=Yes, N=No]
  UndoCancel VarChar(1) OnUndoCancel default=N [Y=Yes, N=No]
  Update1 VarChar(1) OnUpdate default=Y [Y=Yes, N=No]
  Upgrade VarChar(1) OnUpgrade default=N [Y=Yes, N=No]
  YearTransf VarChar(1) OnYearTransfer default=N [Y=Yes, N=No]
  AddLogEnt VarChar(1) OnAddLogEntry default=N [Y=Yes, N=No]
  LogTable nVarChar(20) Log Table
  CanDisplay VarChar(1) Can Display default=Y [Y=Yes, N=No]
  UserSign Int(11) User Signature default=-1
  IsSeries VarChar(1) Is Series default=N [Y=Yes, N=No]
  AddInVer Int(11) Added in version
  AbbrevIdx Int(11) Index in abbreviation strl
  DfaultForm Int(11) Default form for DI permission
  IsService VarChar(1) Is Service default=N [Y=Yes, N=No]
  ExtraPerm Int(11) Extra Permission for DI
  StrlIndex nVarChar(254) String list index
  CanArchive VarChar(1) Can Archive default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation date
  CreateTime Int(6) Creation Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time

# WOFL - Object Wizard Fields
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjCode, FldIndex
Fields (name type(len) description [values] ->parent table):
  ObjCode Int(11) Object Code
  FldIndex Int(6) Field Index
  FldNum Int(6) Field Number
  Editable VarChar(1) Editable default=N [Y=Yes, N=No]
  Find VarChar(1) Find default=N [Y=Yes, N=No]
  DispDescr VarChar(1) Display Description default=N [Y=Yes, N=No]

# WORF - Object Wizard Related Files
Module: General | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjName, SonNum
  UNIQUE_ID U: UniqueId
  TABLE U: ObjName, ObjTable
Fields (name type(len) description [values] ->parent table):
  ObjName Int(11) Parent Object Code
  SonNum Int(11) Son Number
  ObjTable nVarChar(20) Son Table
  RelObj nVarChar(20) Object
  RelType VarChar(1) Relationship Type default=L [L=Line, O=Odd, A=Another object contained]
  LogSon nVarChar(20) Son's Log table
  FthrLineId Int(11) Father's Line Id default=0
  UniqueId Int(11) Son Unique Id
  LnObjCode nVarChar(20) Line object code
  SonDesc nVarChar(30) Son Description
  CreateDate Date(8) Creation date
  CreateTime Int(6) Creation Time
  UpdateDate Date(8) Update Date
  UpdateTime Int(6) Update Time
  UserSign Int(11) User Sign
  FieldIndex Int(6) Field Index

# WPK1 - Dashboard Packages' Parameter or Filter
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DsbrdEntry Int(11) Dashboard Entry
  Type nVarChar(20) Type
  FldName nVarChar(250) Field Name
  FldMethod nVarChar(250) Field Method
  Operator nVarChar(250) Operator
  DbType nVarChar(250) Database Type
  SqlType Int(11) SQL Type
  FromValue nVarChar(250) From Value
  ToValue nVarChar(250) To Value
  DftValue nVarChar(250) Default Value
  ParamType nVarChar(20) Parameter Type
  UdqPh nVarChar(50) UDQ Parameter's Placeholder
  UdqOp nVarChar(20) UDQ Parameter's Operator

# WPK2 - Dashboard Packages' Discrete Value
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FltEntry Int(11) Parameter or Filter Number
  Value nVarChar(50) Discrete Value
  Desc nVarChar(250) Discrete Value Description

# WPK3 - Dashboard Legend Color
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DsbrdEntry Int(11) Dashboard Entry
  FldName nVarChar(250) Field Name
  FldMethod nVarChar(250) Field Method
  DbType nVarChar(250) Database Type
  SqlType Int(11) SQL Type

# WPK4 - Dashboard Legend Color Value
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldEntry Int(11) Field Entry
  Value nVarChar(250) Legend Color Value

# WSV1 - Web Client Smart View Filter
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) GUID
  ParentId nVarChar(40) Parent Id ->OWSV
  FlterFld nVarChar(254) Filter Name
  BindField nVarChar(254) Bind Field
  CardId nVarChar(40) Card Id

# WVT1 - Variant -- selected columns
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent ID
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name

# WVT10 - Variant -- Mchart value axis 2
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RootId, ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  RootId nVarChar(40) Root Guid
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name

# WVT11 - Variant -- Mchart size
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RootId, ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  RootId nVarChar(40) Root Guid
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name

# WVT2 - Variant -- group by
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name

# WVT3 - Variant -- sort by
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) ParentId
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name
  Direction nVarChar(50) Direction

# WVT4 - Variant -- embedded chart
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  ChartType nVarChar(50) Chart Type
  ShowLegend VarChar(1) Show Legend default=N [Y=Yes, N=No]
  CtgrAxis1 nVarChar(254) Category Axis 1
  CtgrAxis2 nVarChar(254) Category Axis 2
  TimeAxis nVarChar(254) Time Axis
  Color nVarChar(254) Color
  Shape nVarChar(254) Shape
  BblWidth nVarChar(254) Bubble width

# WVT5 - Variant -- embedded chart value 1
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RootId, ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  RootId nVarChar(40) Root Guid
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name

# WVT6 - Variant -- embedded chart value 2
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RootId, ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  RootId nVarChar(40) Root Guid
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name

# WVT7 - Variant -- embedded chart size
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RootId, ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  RootId nVarChar(40) Root Guid
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name

# WVT8 - Variant -- Mchart
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  ChartType nVarChar(50) Chart Type
  ShowLegend VarChar(1) Show Legend default=N [Y=Yes, N=No]
  CtgrAxis1 nVarChar(254) Category axis 1
  CtgrAxis2 nVarChar(254) Category axis 2
  TimeAxis nVarChar(254) Time Axis
  Color nVarChar(254) Color
  Shape nVarChar(254) Shape
  BblWidth nVarChar(254) Bubble Width

# WVT9 - Variant -- Mchart value axis 1
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RootId, ParentId, Guid
Fields (name type(len) description [values] ->parent table):
  RootId nVarChar(40) Root Guid
  ParentId nVarChar(40) Parent Id
  Guid nVarChar(40) Guid
  Order Int(11) Order
  ColName nVarChar(50) Column Name

# XAP1 - Page of XAPP
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of page
  XAPEntry Int(11) Foreign key of XAPP
  Name nVarChar(250) Page name
  Default VarChar(1) Is default or not default=N

# XAP2 - XAPP Widget
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of widget
  PageEntry Int(11) Foreign of XAPP page
  Type nVarChar(250) Widget Type
  ObjEntry Int(11) Foeign key of widget content
  Width Int(11) Width of widget
  Height Int(11) Height of widget
  Index Int(11) Order of widget

# XAP3 - XAP Filter
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of XAPP filter
  XAPEntry Int(11) Foreign key of XAPP
  Name nVarChar(250) Name of filter
  Type nVarChar(250) Type of filter
  Method nVarChar(250) Filter method
  MultiValue VarChar(1) Allow multiple value

# XAP4 - Widget Item
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of filter item
  FilEntry Int(11) Foreign key of filter
  TarEntry Int(11) Target content Entry
  TarType nVarChar(250) Target content type
  TarField nVarChar(250) Target field
  IsBase VarChar(1) Is base or not

# XSCMP - XApp Company Assignment
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: XID, COMPANY
Fields (name type(len) description [values] ->parent table):
  XID nVarChar(64) XID
  COMPANY nVarChar(128) COMPANY
  ACTIVATE Int(6) ACTIVATE

# XSSE - XS Session
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SID, XKEY
Fields (name type(len) description [values] ->parent table):
  SID nVarChar(32) SID
  XKEY nVarChar(50) XKEY
  VALUE Text(16) VALUE
  UPDATETIME Date(8) UPDATETIME

# XSUSR - XApp User Authorization
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: COMPANY, USER_CODE
Fields (name type(len) description [values] ->parent table):
  XID nVarChar(64) XID
  COMPANY nVarChar(128) COMPANY
  USER_CODE nVarChar(128) USER_CODE

# XSXA - XS XApp Registration Info
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: XID
  XS_NAME U: NAME
  XS_PACKAGE U: PACKAGE
Fields (name type(len) description [values] ->parent table):
  XID nVarChar(64) XID
  NAME nVarChar(254) NAME
  VERSION nVarChar(64) VERSION
  PACKAGE nVarChar(254) PACKAGE
