<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->

# ACEM - Cost Element
Module: Sales Opportunities | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CemCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CemCode nVarChar(20) Cost Element Code
  CemDescr nVarChar(50) Cost Element Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=256000005 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]

# AOC1 - Distribution Rule - Rows
Module: Sales Opportunities | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode, PrcCode, ValidFrom, logInstanc
  PROF_ID: PrcCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code ->OOCR
  PrcCode nVarChar(8) Cost Center Code ->OPRC
  PrcAmount Num(19,6) Total in Cost Center
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Effective from
  ValidTo Date(8) Effective to
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update

# AOCR - Distribution Rule
Module: Sales Opportunities | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode, logInstanc
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code
  OcrName nVarChar(30) Factor Description
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(6) In Which Dimension default=1 ->ODIM
  AbsEntry Int(11) Numerator
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  IsFixedAmt VarChar(1) Distribute by Fixed Amount default=N [Y=Yes, N=No]

# AOPR - Opportunity
Module: Sales Opportunities | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OpprId, LogInstanc
Fields (name type(len) description [values] ->parent table):
  OpprId Int(11) Sequence No.
  CardCode nVarChar(15) BP Code ->OCRD
  SlpCode Int(11) Main Sales Emp. ->OSLP
  CprCode Int(11) Contact Person ->OCPR
  Source Int(11) Source ->OOSR
  IntCat1 Int(11) Interest - Field 1 ->OOIN
  IntCat2 Int(11) Interest - Field 2 ->OOIN
  IntCat3 Int(11) Interest - Field 3 ->OOIN
  IntRate Int(11) Interest Level ->OOIR
  OpenDate Date(8) Start Date
  DifType VarChar(1) Closing Type default=D [M=Months, W=Weeks, D=Days]
  PredDate Date(8) Predicted Closing Date
  MaxSumLoc Num(19,6) Local Potential Amount
  MaxSumSys Num(19,6) System Potential Amount
  WtSumLoc Num(19,6) Weighted Amount (LC) - Document
  WtSumSys Num(19,6) Weighted Amount (SC)
  PrcnProf Num(19,6) Gross Profit %
  SumProfL Num(19,6) Gross Profit Total - Local
  SumProfS Num(19,6) Gross Profit Total - System
  Memo Text(16) Remarks
  Status VarChar(1) Status default=O [O=Open, L=Lost, W=Won]
  StatusRem nVarChar(30) Status Remarks
  Reason Int(11) Reason for Closing ->OOFR
  RealSumLoc Num(19,6) Total Amount - Local
  RealSumSys Num(19,6) Total Amount - System
  RealProfL Num(19,6) Closing Gross Profit - Local
  RealProfS Num(19,6) Closing Gross Profit - System
  CloPrcnt Num(19,6) Closing Percentage
  StepLast Int(6) Current Stage No. ->OOST
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred to Next Year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  CardName nVarChar(100) BP Name
  CloseDate Date(8) Closing Date
  LastSlp Int(11) Last Sales Emp. ->OSLP
  Name nVarChar(100) Opportunity Name
  Territory Int(11) Territory ->OTER
  Industry Int(11) Industry ->OOND
  ChnCrdCode nVarChar(15) BP Channel Code ->OCRD
  ChnCrdName nVarChar(100) BP Channel Name
  PrjCode nVarChar(20) Project Code ->OPRJ
  CardGroup Int(6) BP Group ->OCRD
  ChnCrdCon Int(11) BP Channel Contact ->OCPR
  Owner Int(11) Data Ownership field ->OHEM
  attachment Text(16) Attachments
  DocType nVarChar(9) Linked Document Type default=-1 [-1=, 23=Quotations, 17=Sales Orders, 15=Delivery Notes, 13=Sales Invoices, 540000006=Purchase Quotations, 22=Purchase Orders, 20=Goods Receipt POs, 18=Purchase Invoices]
  DocNum Int(11) Linked Document Number
  DocEntry Int(11) Linked Document Entry
  DocChkbox VarChar(1) Document Checkbox
  AtcEntry Int(11) Attachment Entry
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  OpprType VarChar(1) Opportunity Type default=R [R=Sales, P=Purchasing]
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  CreateDate Date(8) Creation Date
  EncryptIV nVarChar(100) Encrypt IV
  DataVers Int(11) Data Version default=1

# APRC - Cost Center
Module: Sales Opportunities | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrcCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  PrcCode nVarChar(8) Center Code
  PrcName nVarChar(30) Center Name
  GrpCode nVarChar(4) Group Code
  Balance Num(19,6) Balance
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(6) In Which Dimension default=1 ->ODIM
  CCTypeCode nVarChar(8) Cost Center Type Code ->OCCT
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CCOwner Int(11) Cost Center Owner ->OHEM

# OCEM - Cost Element
Module: Sales Opportunities | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CemCode
Fields (name type(len) description [values] ->parent table):
  CemCode nVarChar(20) Cost Element Code
  CemDescr nVarChar(50) Cost Element Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=256000005 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]

# OCMT - Competitors
Module: Sales Opportunities | 6 columns | ObjType: 109
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompetId
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  CompetId Int(11) Sequence No.
  Name nVarChar(15) Name
  ThreatLevl Int(6) Threat Level default=1 [1=Low, 2=Medium, 3=High]
  Memo nVarChar(50) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OCR1 - Distribution Rule - Rows
Module: Sales Opportunities | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode, PrcCode, ValidFrom
  PROF_ID: PrcCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code ->OOCR
  PrcCode nVarChar(8) Center Code ->OPRC
  PrcAmount Num(19,6) Total in Center
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Effective From default=19000101
  ValidTo Date(8) Effective To
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update

# ODOR - Doubtful Debts
Module: Sales Opportunities | 3 columns | ObjType: 185
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NUMOFDAYS U: NumOfDays
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  NumOfDays Int(11) No. of Days
  Percentage Num(19,6) Doubtful Debt %

# OOCR - Distribution Rule
Module: Sales Opportunities | 14 columns | ObjType: 62
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code
  OcrName nVarChar(30) Factor Description
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(6) In Which Dimension default=1 ->ODIM
  AbsEntry Int(11) Numerator
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  IsFixedAmt VarChar(1) Distribute by Fixed Amount default=N [Y=Yes, N=No]

# OOND - Industries
Module: Sales Opportunities | 3 columns | ObjType: 201
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IndCode
  IND_NAME U: IndName
Fields (name type(len) description [values] ->parent table):
  IndCode Int(11) Industry Code
  IndName nVarChar(40) Industry Name
  IndDesc nVarChar(120) Industry Description

# OOPR - Opportunity
Module: Sales Opportunities | 59 columns | ObjType: 97
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OpprId
Fields (name type(len) description [values] ->parent table):
  OpprId Int(11) Sequence No.
  CardCode nVarChar(15) BP Code ->OCRD
  SlpCode Int(11) Main Sales Emp. ->OSLP
  CprCode Int(11) Contact Person ->OCPR
  Source Int(11) Source ->OOSR
  IntCat1 Int(11) Interest - Field 1 ->OOIN
  IntCat2 Int(11) Interest - Field 2 ->OOIN
  IntCat3 Int(11) Interest - Field 3 ->OOIN
  IntRate Int(11) Interest Level ->OOIR
  OpenDate Date(8) Start Date
  DifType VarChar(1) Closing Type default=D [M=Months, W=Weeks, D=Days]
  PredDate Date(8) Predicted Closing Date
  MaxSumLoc Num(19,6) Local Potential Amount
  MaxSumSys Num(19,6) System Potential Amount
  WtSumLoc Num(19,6) Weighted Amount (LC) - Document
  WtSumSys Num(19,6) Weighted Amount (SC)
  PrcnProf Num(19,6) Gross Profit %
  SumProfL Num(19,6) Gross Profit Total - Local
  SumProfS Num(19,6) Gross Profit Total - System
  Memo Text(16) Remarks
  Status VarChar(1) Status default=O [O=Open, L=Lost, W=Won]
  StatusRem nVarChar(30) Status Remarks
  Reason Int(11) Reason for Closing ->OOFR
  RealSumLoc Num(19,6) Total Amount - Local
  RealSumSys Num(19,6) Total Amount - System
  RealProfL Num(19,6) Closing Gross Profit - Local
  RealProfS Num(19,6) Closing Gross Profit - System
  CloPrcnt Num(19,6) Closing Percentage
  StepLast Int(6) Current Stage No. ->OOST
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred to next year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  CardName nVarChar(100) BP Name
  CloseDate Date(8) Closing Date
  LastSlp Int(11) Last Sales Emp. ->OSLP
  Name nVarChar(100) Opportunity Name
  Territory Int(11) Territory ->OTER
  Industry Int(11) Industry ->OOND
  ChnCrdCode nVarChar(15) BP Channel Code ->OCRD
  ChnCrdName nVarChar(100) BP Channel Name
  PrjCode nVarChar(20) Project Code ->OPRJ
  CardGroup Int(6) BP Group ->OCRD
  ChnCrdCon Int(11) BP Channel Contact ->OCPR
  Owner Int(11) Data Ownership field ->OHEM
  attachment Text(16) Attachments
  DocType nVarChar(9) Linked Document Type default=-1 [-1=, 23=Quotations, 17=Sales Orders, 15=Delivery Notes, 13=Sales Invoices, 540000006=Purchase Quotations, 22=Purchase Orders, 20=Goods Receipt POs, 18=Purchase Invoices]
  DocNum Int(11) Linked Document Number
  DocEntry Int(11) Linked Document Entry
  DocChkbox VarChar(1) Document Checkbox default=N [N=No, Y=Yes]
  AtcEntry Int(11) Attachment Entry
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  OpprType VarChar(1) Opportunity Type default=R [R=Sales, P=Purchasing]
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  CreateDate Date(8) Creation Date
  EncryptIV nVarChar(100) Encrypt IV
  DataVers Int(11) Data Version default=1

# OORL - Relationships
Module: Sales Opportunities | 2 columns | ObjType: 212
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OrlCode
  NAME U: OrlDesc
Fields (name type(len) description [values] ->parent table):
  OrlCode Int(11) Relationship Code
  OrlDesc nVarChar(100) Relationship Description

# OOST - Opportunity Stage
Module: Sales Opportunities | 8 columns | ObjType: 101
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num
  STEP U: StepId
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Name
  StepId Int(6) Stage No.
  CloPrcnt Num(19,6) Closing Percentage
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  SalesStage VarChar(1) Sales default=Y [Y=Yes, N=No]
  PurStage VarChar(1) Purchasing default=Y [Y=Yes, N=No]

# OPR1 - Opportunity - Rows
Module: Sales Opportunities | 25 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OpprId, Line
Fields (name type(len) description [values] ->parent table):
  OpprId Int(11) Sequence No. ->OOPR
  Line Int(6) Row No.
  SlpCode Int(11) Sales Employee ->OSLP
  CntctCode Int(11) Contact Person ->OCPR
  OpenDate Date(8) Start Date
  CloseDate Date(8) Closing Date
  Step_Id Int(11) Stage Key ->OOST
  ClosePrcnt Num(19,6) Percentage Rate
  MaxSumLoc Num(19,6) Max. Local Total
  MaxSumSys Num(19,6) Max. System Total
  Memo Text(16) Remarks
  DocId Int(11) Object Code
  ObjType nVarChar(9) Object Type default=-1 [-1=, 0=, 23=Sales Quotations, 17=Sales Orders, 15=Delivery Notes, 13=Sales Invoices, 540000006=Purchase Quotations, 22=Purchase Orders, 20=Goods Receipt POs, 18=Purchase Invoices]
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Linked VarChar(1) Activity default=N [Y=Yes, N=No]
  WtSumLoc Num(19,6) Weighted Amount (LC) - Rows
  WtSumSys Num(19,6) Weighted Amount (SC)
  UserSign Int(6) User Signature ->OUSR
  ChnCrdCode nVarChar(15) BP Channel Code ->OCRD
  ChnCrdName nVarChar(100) BP Channel Name
  ChnCrdCon Int(11) BP Channel Contact ->OCPR
  DocChkbox VarChar(1) Document Checkbox [Y=Yes, N=No]
  Owner Int(11) Data Ownership Field ->OHEM
  DocNumber Int(11) Document Number
  EncryptIV nVarChar(100) Encrypt IV

# OPR2 - Opportunity - Partners
Module: Sales Opportunities | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OpportId, Line
Fields (name type(len) description [values] ->parent table):
  OpportId Int(11) Sequence No.
  Line Int(6) Row No.
  ParterId Int(11) Partners ->OPRT
  Memo nVarChar(50) Details
  OrlCode Int(11) Relationship Code ->OORL
  RelatCard nVarChar(15) Related BP ->OCRD
  EncryptIV nVarChar(100) Encrypt IV

# OPR3 - Opportunity - Competitors
Module: Sales Opportunities | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OpportId, Line
Fields (name type(len) description [values] ->parent table):
  OpportId Int(11) Sequence No.
  Line Int(6) Row No.
  CompetId Int(11) Competitors ->OCMT
  Memo nVarChar(50) Details
  Won VarChar(1) Won or Lost default=N [Y=Yes, N=No]
  ThreatLevl Int(6) Threat Level [1=Low, 2=Medium, 3=High]
  EncryptIV nVarChar(100) Encrypt IV

# OPR4 - Opportunity - Interests
Module: Sales Opportunities | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OprId, Line
Fields (name type(len) description [values] ->parent table):
  OprId Int(11) Sequence No.
  Line Int(6) Row No.
  IntId Int(11) Interest ID ->OOIN
  Prmry VarChar(1) Primary Interest default=N [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV

# OPR5 - Opportunity - Reasons
Module: Sales Opportunities | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OpportId, Line
Fields (name type(len) description [values] ->parent table):
  OpportId Int(11) Sequence No.
  Line Int(6) Row No.
  ReasondId Int(11) Reason ->OOFR
  EncryptIV nVarChar(100) Encrypt IV

# OPRC - Cost Center
Module: Sales Opportunities | 16 columns | ObjType: 61
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrcCode
Fields (name type(len) description [values] ->parent table):
  PrcCode nVarChar(8) Center Code
  PrcName nVarChar(30) Center Name
  GrpCode nVarChar(4) Group Code
  Balance Num(19,6) Balance
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(6) In Which Dimension default=1 ->ODIM
  CCTypeCode nVarChar(8) Cost Center Type Code ->OCCT
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CCOwner Int(11) Cost Center Owner ->OHEM
