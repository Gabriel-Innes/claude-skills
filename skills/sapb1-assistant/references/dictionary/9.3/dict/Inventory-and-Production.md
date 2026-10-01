<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->

# ABAT - Attribute - History
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldAbs Int(11) Bin Field Conf. Internal Number ->OBFC
  AttrValue nVarChar(20) Code
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N

# ABFC - Bin Field Configuration - History
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldType VarChar(1) Field Type [S=Warehouse Sublevel, A=Bin Location Attribute]
  FldNum Int(6) Field Number
  DispName nVarChar(20) Display Name
  Activated VarChar(1) Active [Y/N] default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  DftName nVarChar(20) Default Field Name

# ABIN - Bin Location - History
Module: Inventory and Production | 64 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BinCode nVarChar(228) Bin Location Code
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SysBin VarChar(1) System Bin default=N [Y=Yes, N=No]
  SL1Abs Int(11) Sublevel-1 Internal Number ->OBSL
  SL1Code nVarChar(50) Sublevel-1 Code
  SL2Abs Int(11) Sublevel-2 Internal Number ->OBSL
  SL2Code nVarChar(50) Sublevel-2 Code
  SL3Abs Int(11) Sublevel-3 Internal Number ->OBSL
  SL3Code nVarChar(50) Sublevel-3 Code
  SL4Abs Int(11) Sublevel-4 Internal Number ->OBSL
  SL4Code nVarChar(50) Sublevel-4 Code
  Attr1Abs Int(11) Attribute-1 Internal Number ->OBAT
  Attr1Val nVarChar(20) Attribute-1 Value
  Attr2Abs Int(11) Attribute-2 Internal Number ->OBAT
  Attr2Val nVarChar(20) Attribute-2 Value
  Attr3Abs Int(11) Attribute-3 Internal Number ->OBAT
  Attr3Val nVarChar(20) Attribute-3 Value
  Attr4Abs Int(11) Attribute-4 Internal Number ->OBAT
  Attr4Val nVarChar(20) Attribute-4 Value
  Attr5Abs Int(11) Attribute-5 Internal Number ->OBAT
  Attr5Val nVarChar(20) Attribute-5 Value
  Attr6Abs Int(11) Attribute-6 Internal Number ->OBAT
  Attr6Val nVarChar(20) Attribute-6 Value
  Attr7Abs Int(11) Attribute-7 Internal Number ->OBAT
  Attr7Val nVarChar(20) Attribute-7 Value
  Attr8Abs Int(11) Attribute-8 Internal Number ->OBAT
  Attr8Val nVarChar(20) Attribute-8 Value
  Attr9Abs Int(11) Attribute-9 Internal Number ->OBAT
  Attr9Val nVarChar(20) Attribute-9 Value
  Attr10Abs Int(11) Attribute-10 Internal Number ->OBAT
  Attr10Val nVarChar(20) Attribute-10 Value
  Disabled VarChar(1) Inactive default=N [Y=Yes, N=No]
  Descr nVarChar(50) Description
  BarCode nVarChar(100) Bar Code
  AltSortCod nVarChar(50) Alternative Sort Code
  ItmRtrictT Int(6) Item Restriction Type default=0 [0=None, 1=Specific Item, 2=Single Item Only, 3=Specific Item Group, 4=Single Item Group Only]
  SpcItmCode nVarChar(50) Specific Item Code ->OITM
  SpcItmGrpC Int(6) Specific Item Group Code ->OITB
  SngBatch VarChar(1) Batch Restriction default=N [N=None, Y=Single Batch]
  RtrictType Int(6) Restricted Transactions Type default=0 [0=None, 1=All Transactions, 2=Inbound Transactions, 3=Outbound Transactions, 4=All Except Inventory Transfer and Counting Transactions]
  RtrictResn nVarChar(254) Reason for Restriction
  RtrictDate Date(8) Last Updated On
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N
  MinLevel Num(19,6) Minimum Qty
  MaxLevel Num(19,6) Maximum Qty
  ReceiveBin VarChar(1) Receiving Bin Location default=N [Y=Yes, N=No]
  NoAutoAllc VarChar(1) Excl. fr. Auto Alloc. on Issue default=N [Y=Yes, N=No]
  MaxWeight1 Num(19,6) Maximum Weight 1
  Wght1Unit Int(6) Unit of Maximum Weight 1 ->OWGT
  MaxWeight2 Num(19,6) Maximum Weight 2
  Wght2Unit Int(6) Unit of Maximum Weight 2 ->OWGT
  UoMRtrict Int(6) UoM Restriction default=0 [0=None, 1=Specific UoM, 2=Single UoM Only, 3=Specific UoM Group, 4=Single UoM Group Only]
  SpcUoMCode Int(11) Specified UoM Code ->OUOM
  SpcUGPCode Int(11) Specified UoM Group Code ->OUGP
  SngUoMCode Int(11) Single UoM Code ->OUOM

# ABSL - Warehouse Sublevel - History
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldAbs Int(11) Bin Field Conf. Internal Number ->OBFC
  SLCode nVarChar(50) Code
  Descr nVarChar(50) Description
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N

# ABTN - Batch Numbers Master Data
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  SYSTEM_KEY U: LogInstanc, SysNumber, ItemCode
  DIST_KEY: DistNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Batch Number
  MnfSerial nVarChar(36) Batch Attribute 1
  LotNumber nVarChar(36) Batch Attribute 2
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Warranty Start Date
  GrntExp Date(8) Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Location
  Status VarChar(1) Status default=0 [0=Released, 1=Not Accessible, 2=Locked]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) Abs Entry
  ObjType nVarChar(20) Object Type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

# ABTW - Batch Attributes in Location
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  SYSTEM_KEY U: LogInstanc, WhsCode, SysNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number ->OBTN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Location nVarChar(100) Location
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) Abs Entry
  MdAbsEntry Int(11) MD Abs. Entry ->OBTN
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# ADG1 - Discount Groups Rows
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjKey, ObjType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry ->OEDG
  ObjType nVarChar(20) Object Type [52=Item Groups, 8=Item Properties, 43=Manufacturer, 4=Items]
  ObjKey nVarChar(50) Object Key
  DiscType VarChar(1) Discount Type default=D [D=Discount, P=Pay for/Get for Free]
  Discount Num(19,6) Discount
  PayFor Num(19,6) Paid Qty
  ForFree Num(19,6) Free Qty
  UpTo Num(19,6) Max. Free Qty
  LogInstanc Int(11) Log Instance default=0

# ADNF - DNF Code
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  NCM_DNF U: LogInstanc, DNFCode, NCMEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  NCMEntry Int(11) NCM Code ->ONCM
  DNFCode nVarChar(5) DNF Code
  DNFUoM nVarChar(10) DNF UoM
  DNFFactor Num(19,6) DNF Factor
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# AEDG - Discount Groups
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Type VarChar(1) Type [A=All BPs, C=Customer Group, V=Vendor Group, S=Specific BP]
  ObjType nVarChar(20) Object Type default=-1 [-1=, 10=Card Payment Groups, 2=Cards]
  ObjCode nVarChar(15) Object Code
  DiscRel VarChar(1) Disc. Relations default=L [L=Lowest Discount, H=Highest Discount, A=Average, S=Total, M=Discount Multiples]
  ValidFor VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidForm Date(8) Active From
  ValidTo Date(8) Active To
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Form ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Update Date

# AIGW - Item Group - Warehouse - History
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItmsGrpCod Int(6) Item Group Code ->OITB
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# AIN1 - Inventory Counting - Rows
Module: Inventory and Production | 41 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  ItemDesc nVarChar(100) Item Description
  Freeze VarChar(1) Item Freeze Status default=N [Y=Yes, N=No]
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  InWhsQty Num(19,6) In-Whse Qty on Count Date
  Counted VarChar(1) Counted default=N [Y=Yes, N=No]
  CountQty Num(19,6) Counted Quantity
  CountQtyT1 Num(19,6) Counter 1 - Counted Quantity
  CountQtyT2 Num(19,6) -
  Remark nVarChar(254) Remarks
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  Difference Num(19,6) Difference
  DiffPercen Num(19,6) Difference %
  CountDate Date(8) Count Date
  CountTime Int(11) Count Time
  TargetRef nVarChar(16) Target Document Reference
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 10000071=Inventory Posting]
  TargetEntr Int(11) Target Document Internal ID
  TargetLine Int(11) Target Document Row
  ProjCode nVarChar(20) Project Code ->OPRJ
  OcrCode nVarChar(8) Distribution Rule Code ->OOCR
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  BinEntry Int(11) Bin Location Entry ->OBIN
  VisOrder Int(11) Visual Order
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  PrefVendor nVarChar(15) Preferred Vendor ->OCRD
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Entry ->OUGP
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
  CountDiff Num(19,6) Counters' Diff.
  CountDiffP Num(19,6) Counters' Diff. (%)
  UomCode nVarChar(20) UoM Code for DI
  UomQty Num(19,6) UoM Counted Qty for DI

# AIN10 - Inventory Counting - Individual Counters - Row UoM
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CounterNum, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  CounterNum Int(11) Counter Number
  UomQty Num(19,6) UoM Counted Qty
  InvtQty Num(19,6) Counted Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# AIN11 - Inventory Counting - Individual Counters - Row SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, CounterNum, SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  CounterNum Int(11) Counter Number

# AIN2 - Inventory Counting - UoM
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, ChildNum, LineNum, DocEntry
  BUSINESS U: LogIns, UomCode, BarCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  BarCode nVarChar(254) Bar Code
  UomCode nVarChar(20) UoM Code ->OUOM
  UomQty Num(19,6) UoM Counted Qty
  CountQty Num(19,6) Counted Qty of Inventory UoM
  Tk1UomQty Num(19,6) Counter 1 UoM Counted Qty
  Tk2UomQty Num(19,6) -
  Tk1CntQty Num(19,6) Counter 1 Counted Qty of Inv.
  Tk2CntQty Num(19,6) -
  ItmsPerUnt Num(19,6) Items per Unit
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  TeamUomQty Num(19,6) Team UoM Counted Qty
  TeamCntQty Num(19,6) Team Counted Qty
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM

# AIN3 - Inventory Count - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# AIN4 - Inventory Counting - Team Counters
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CounterNum, DocEntry
  BUSINESS U: LogIns, CounterId, CounteType, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  CounterNum Int(11) Counter Number
  CounteType Int(11) Type of Counter default=12 [12=User, 171=Employee]
  CounterId Int(11) Counter ID
  CounteName nVarChar(155) Counter Name
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# AIN5 - Inventory Counting - Team Counters - Row Counted Qty
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CounterNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  CounterNum Int(11) Counter Number
  TotalQty Num(19,6) Total Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# AIN6 - Inventory Counting - Team Counter - Row UoM
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CounterNum, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  CounterNum Int(11) Counter Number
  UomQty Num(19,6) UoM Counted Qty
  InvtQty Num(19,6) Counted Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# AIN7 - Inventory Counting - Team Counter - Row SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  CounterNum Int(11) Counter Number

# AIN8 - Inventory Counting - Individual Counters
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CounterNum, DocEntry
  BUSINESS U: LogIns, CounterId, CounteType, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  CounterNum Int(11) Counter Number
  CounteType Int(11) Type of Counter default=12 [12=User, 171=Employee]
  CounterId Int(11) Counter ID
  CounteName nVarChar(155) Counter Name
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# AIN9 - Inventory Counting - Individual Counter - Row Counted Qty
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CounterNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  CounterNum Int(11) Counter Number
  TotalQty Num(19,6) Total Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# AINC - Inventory Counting
Module: Inventory and Production | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, DocEntry
  SERIES U: LogIns, DocNum, Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  CountDate Date(8) Date of Counting
  Time Int(11) Time of Counting
  CountType VarChar(1) Counting Type default=1 [1=Single Counter, 2=Multiple Counters]
  Taker1Type Int(11) Type of Counter default=12 [12=User, 171=Employee]
  Taker1Id Int(11) Counter ID
  Taker2Type Int(11) - default=12
  Taker2Id Int(11) -
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Ref2 nVarChar(11) Reference 2
  Remarks Text(16) Remarks
  LogIns Int(11) Log Instance - History
  UserSign Int(6) User Creating - History ->OUSR
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  CreateDate Date(8) Create Date - History
  ObjType nVarChar(20) Object Type default=1470000065
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Approved, A=Generated by Authorizer, C=Canceled]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OICD
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  TeamCount Int(11) Count of Team Counters default=0
  IndvCount Int(11) Count of Individual Counters default=0
  DiffQty Num(19,6) Total Difference
  DiffPercen Num(19,6) Total Difference (%)
  UpdateTS Int(11) Update Full Time
  CreateTime Int(6) Generation Time
  PIndicator nVarChar(10) Period Indicator
  FinncPriod Int(11) Posting Period
  PostDate Date(8) Posting Date
  VersionNum nVarChar(11) Version Number
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]

# AIQI - Inventory Opening Balance
Module: Inventory and Production | 34 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, DocEntry
  DOC_DATE: DocDate
  CREATEDATE: DocTime, CreateDate
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  CreateDate Date(8) Creation Date
  DocTime Int(6) Generation Time
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DocDate Date(8) Posting Date
  Reference nVarChar(11) Reference
  Comments nVarChar(254) Remarks
  DocDueDate Date(8) Due Date
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  VersionNum nVarChar(11) Version Number
  JdtNum Int(11) Journal Number
  Reference2 nVarChar(11) Reference 2
  ObjType nVarChar(20) Object Type default=310000001
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PriceSrc VarChar(1) Price Source default=3 [1=By Price List, 2=Last Evaluated Price, 3=Item Cost]
  PriceList Int(11) Price List
  JrnlMemo nVarChar(50) Journal Remarks
  TaxDate Date(8) Document Date
  Status VarChar(1) Status default=O [O=Open, C=Close]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Update User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OIOD
  Printed VarChar(1) Printed default=N
  DocTotal Num(19,6) Document Total
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  UpdateTS Int(11) Update Full Time
  PIndicator nVarChar(10) Period Indicator
  FinncPriod Int(11) Posting Period

# AIQR - Inventory Posting
Module: Inventory and Production | 37 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, DocEntry
  DOC_DATE: DocDate
  CREATEDATE: DocTime, CreateDate
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  CreateDate Date(8) Creation Date
  DocTime Int(6) Generation Time
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DocDate Date(8) Posting Date
  Reference nVarChar(11) Reference
  Comments nVarChar(254) Remarks
  DocDueDate Date(8) Due Date
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  VersionNum nVarChar(11) Version Number
  JdtNum Int(11) Journal Number ->OJDT
  Reference2 nVarChar(11) Reference 2
  ObjType nVarChar(20) Object Type default=10000071
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PriceSrc Int(11) Price Source default=3 [1=By Price List, 2=Last Evaluated Price, 3=Item Cost]
  PriceList Int(11) Price List
  JrnlMemo nVarChar(50) Journal Remarks
  Status VarChar(1) Status default=O [O=Open, C=Close]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  CountDate Date(8) Date of Counting
  CountTime Int(11) Time of Counting
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OIPD
  Printed VarChar(1) Printed default=N
  DocTotal Num(19,6) Document Total
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  UpdateTS Int(11) Update Full Time
  CopyOption VarChar(1) DI Copy from Option default=0 [0=No Counters Diff., 1=Individual 1, 2=Individual 2, 3=Individual 3, 4=Individual 4, 5=Individual 5, 6=Team Counted Quantity]
  BaseEntry Int(11) Base Counting Doc. Entry
  PIndicator nVarChar(10) Period Indicator
  FinncPriod Int(11) Posting Period

# AIT1 - Item - Prices - History
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, PriceList, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Number ->OITM
  PriceList Int(6) Price List No. ->OPLN
  Price Num(19,6) Price List
  Currency nVarChar(3) Price List Currency
  Ovrwritten VarChar(1) Manual Price Update default=N [Y=Yes, N=No]
  Factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object ->ADP1
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  Ovrwrite1 VarChar(1) Manual Price Entry (1) default=N [Y=Yes, N=No]
  Ovrwrite2 VarChar(1) Manual Price Entry (2) default=N [Y=Yes, N=No]
  BasePLNum Int(6) Base Price List No. ->OPLN
  UomEntry Int(11) UoM Entry
  PriceType VarChar(1) Price Type default=M [I=Inventory UoM Price, P=Pricing Unit Price, M=Both I and P, O=Other UoM Price]

# AIT11 - Asset Item Period Control
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, VisOrder, DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  VisOrder Int(11) Visual Order
  DprSt VarChar(1) Depreciation Status default=Y [Y=Yes, N=No]
  factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ActualUnit Int(11) Actual Units

# AIT13 - Asset Attributes
Module: Inventory and Production | 67 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  AttriTxt1 nVarChar(100) Attribute 1
  AttriTxt2 nVarChar(100) Attribute 2
  AttriTxt3 nVarChar(100) Attribute 3
  AttriTxt4 nVarChar(100) Attribute 4
  AttriTxt5 nVarChar(100) Attribute 5
  AttriTxt6 nVarChar(100) Attribute 6
  AttriTxt7 nVarChar(100) Attribute 7
  AttriTxt8 nVarChar(100) Attribute 8
  AttriTxt9 nVarChar(100) Attribute 9
  AttriTxt10 nVarChar(100) Attribute 10
  AttriTxt11 nVarChar(100) Attribute 11
  AttriTxt12 nVarChar(100) Attribute 12
  AttriTxt13 nVarChar(100) Attribute 13
  AttriTxt14 nVarChar(100) Attribute 14
  AttriTxt15 nVarChar(100) Attribute 15
  AttriTxt16 nVarChar(100) Attribute 16
  AttriTxt17 nVarChar(100) Attribute 17
  AttriTxt18 nVarChar(100) Attribute 18
  AttriTxt19 nVarChar(100) Attribute 19
  AttriTxt20 nVarChar(100) Attribute 20
  AttriTxt21 nVarChar(100) Attribute 21
  AttriTxt22 nVarChar(100) Attribute 22
  AttriTxt23 nVarChar(100) Attribute 23
  AttriTxt24 nVarChar(100) Attribute 24
  AttriTxt25 nVarChar(100) Attribute 25
  AttriTxt26 nVarChar(100) Attribute 26
  AttriTxt27 nVarChar(100) Attribute 27
  AttriTxt28 nVarChar(100) Attribute 28
  AttriTxt29 nVarChar(100) Attribute 29
  AttriTxt30 nVarChar(100) Attribute 30
  AttriTxt31 nVarChar(100) Attribute 31
  AttriTxt32 nVarChar(100) Attribute 32
  AttriInt33 Int(11) Attribute 33
  AttriInt34 Int(11) Attribute 34
  AttriInt35 Int(11) Attribute 35
  AttriInt36 Int(11) Attribute 36
  AttriInt37 Int(11) Attribute 37
  AttriInt38 Int(11) Attribute 38
  AttriInt39 Int(11) Attribute 39
  AttriInt40 Int(11) Attribute 40
  AttriInt41 Int(11) Attribute 41
  AttriInt42 Int(11) Attribute 42
  AttriDt43 Date(8) Attribute 43
  AttriDt44 Date(8) Attribute 44
  AttriDt45 Date(8) Attribute 45
  AttriDt46 Date(8) Attribute 46
  AttriDt47 Date(8) Attribute 47
  AttriAm48 Num(19,6) Attribute 48
  AttriAm49 Num(19,6) Attribute 49
  AttriAm50 Num(19,6) Attribute 50
  AttriAm51 Num(19,6) Attribute 51
  AttriAm52 Num(19,6) Attribute 52
  AttriAm53 Num(19,6) Attribute 53
  AttriAm54 Num(19,6) Attribute 54
  AttriPr55 Num(19,6) Attribute 55
  AttriPr56 Num(19,6) Attribute 56
  AttriPr57 Num(19,6) Attribute 57
  AttriPr58 Num(19,6) Attribute 58
  AttriPr59 Num(19,6) Attribute 59
  AttriQTY60 Num(19,6) Attribute 60
  AttriQTY61 Num(19,6) Attribute 61
  AttriQTY62 Num(19,6) Attribute 62
  AttriQTY63 Num(19,6) Attribute 63
  AttriQTY64 Num(19,6) Attribute 64
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

# AIT2 - Items - Multiple Preferred Vendors - History
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, VendorCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  VendorCode nVarChar(15) Vendor Code ->OCRD
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object ->ADP1

# AIT3 - Items - Localization Fields - History
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  IncNature nVarChar(10) Income Nature ->OBMI
  LogInstanc Int(11) IPI Class Code
  ObjType nVarChar(20) Log Instance default=0

# AIT5 - Asset Item Projects - History
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  LineNum Int(11) Line Number
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Project nVarChar(20) Project ->OPRJ
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

# AIT6 - Asset Item Distribution Rules
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  LineNum Int(11) Line Number
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

# AIT7 - Asset Item Depreciation Params - History
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  VisOrder Int(11) Visual Order
  DprStart Date(8) Depreciation Start Date
  DprEnd Date(8) Depreciation End Date
  UsefulLife Int(11) Useful Life
  RemainLife Num(19,6) Remaining Life
  DprType nVarChar(15) Depreciation Type ->ODTP
  DprTypeC nVarChar(15) Depr. Type Calculation ->ODTP
  UsefulLfeC Int(11) Useful Life Calculation
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  RemainDays Num(19,6) Remaining Life in Days
  TotalUnits Int(11) Total Units in Life
  RemainUnit Int(11) Remaining Units
  StanUnit Int(11) Standard Units

# AIT8 - Asset Item Balances - History
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  APC Num(19,6) APC
  APCHist Num(19,6) Historical APC
  Quantity Num(19,6) Asset Quantity
  OrDpAcc Num(19,6) Accumulated Ordinary Depr.
  UnDpAcc Num(19,6) Accumulated Unplanned Depr.
  SpDpKey1 nVarChar(2) Special Depreciation 01 ->ODPP
  SpDpAcc1 Num(19,6) Accumulated Special Depr. 01
  SpDpKey2 nVarChar(2) Special Depreciation 02 ->ODPP
  SpDpAcc2 Num(19,6) Accumulated Special Depr. 02
  SpDpKey3 nVarChar(2) Special Depreciation 03 ->ODPP
  SpDpAcc3 Num(19,6) Accumulated Special Depr. 03
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  SalvageVal Num(19,6) Salvage Value
  OrDpAcc1 Num(19,6) Ordinary Depr. Accumulation 01
  WriteUpAcc Num(19,6) Accumulated Write-Up
  IsMaSalVal VarChar(1) Manually Changed Salvage Value default=N [Y=Yes, N=No]
  AppreAcc Num(19,6) Accumulated Appreciation

# AIT9 - Item - UoM Prices
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, UomEntry, PriceList, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PriceList Int(6) Price List No. ->OPLN
  UomEntry Int(11) UoM Entry ->OUOM
  Factor Num(19,6) Reduced By %
  Price Num(19,6) UoM Price
  Currency nVarChar(3) Currency for UoM Price ->OCRN
  AutoUpdate VarChar(1) Automatic Update default=Y [Y=Yes, N=No]
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  Factor1 Num(19,6) Reduced By %
  Factor2 Num(19,6) Reduced By %
  UpdateDate Date(8) Date of Update
  PriceType VarChar(1) Price Type default=O [I=Inventory UoM Price, P=Pricing Unit Price, M=Both I and P, O=Other UoM Price]

# AITB - Item Groups - History
Module: Inventory and Production | 82 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: logInstanc, ItmsGrpCod
  GROUP_NAME U: logInstanc, ItmsGrpNam
Fields (name type(len) description [values] ->parent table):
  ItmsGrpCod Int(6) Number
  ItmsGrpNam nVarChar(20) Group Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost Of Goods Sold ->OACT
  TransferAc nVarChar(15) Allocation Acct ->OACT
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Acct ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase ->OACT
  ReturnAc nVarChar(15) Sales Returns ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Sales Revenue - EU ->OACT
  EUExpensAc nVarChar(15) EU Expense Acct ->OACT
  FrRevenuAc nVarChar(15) Sales Revenue - Foreign ->OACT
  FrExpensAc nVarChar(15) Foreign Expense Acct ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  CycleCode Int(6) Cycle Code ->OCYC
  Alert VarChar(1) Alert default=N [N=No, Y=Yes]
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  ExchangeAc nVarChar(15) Exchange Rate Differences Account ->OACT
  BalanceAcc nVarChar(15) Goods Clearing Acct ->OACT
  PurchaseAc nVarChar(15) Purchase Acct ->OACT
  PAReturnAc nVarChar(15) PA Return Acct ->OACT
  PurchOfsAc nVarChar(15) Purchase Offset Acct ->OACT
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Acct ->OACT
  IncresGlAc nVarChar(15) G/L Increase Acct ->OACT
  InvntSys VarChar(1) Inventory System [A=Moving Average, S=Standard, F=FIFO]
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  StokRvlAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkOffsAct nVarChar(15) Inventory Revaluation Offset Account ->OACT
  WipAcct nVarChar(15) WIP Material Account ->OACT
  WipVarAcct nVarChar(15) WIP Material Variance Account ->OACT
  CostRvlAct nVarChar(15) Cost of Sale Revaluation Acct ->OACT
  CstOffsAct nVarChar(15) Cost of Sales Reval. Offs. Acct ->OACT
  ExpClrAct nVarChar(15) Expenses Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  Object nVarChar(20) Object Type - History default=52
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Update Date - History
  ARCMAct nVarChar(15) Sales Credit Acct ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Foreign Acct ->OACT
  ARCMEUAct nVarChar(15) Sales Credit EU Acct ->OACT
  ARCMExpAct nVarChar(15) Exempted Credits ->OACT
  APCMAct nVarChar(15) Purchase Credit Acct ->OACT
  APCMFrnAct nVarChar(15) Foreign Purchase Credit Acct ->OACT
  APCMEUAct nVarChar(15) EU Purchase Credit Acct ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account ->OACT
  ItemClass VarChar(1) Service or Material default=2 [1=Service, 2=Material]
  OSvcCode Int(11) Outgoing Service Code default=-1 ->OSCD
  ISvcCode Int(11) Incoming Service Code default=-1 ->OSCD
  ServiceGrp Int(11) Service Group default=-1 ->OSGP
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  NegStckAct nVarChar(15) Negative Inventory Adjustment ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Acct ->OACT
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  UgpEntry Int(11) Default UoM Group Entry ->OUGP
  IUoMEntry Int(11) Default Inventory UoM ->OUOM
  ToleranDay Int(11) Tolerance Days
  RuleCode nVarChar(2) Checking Rule Code ->ODCR
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account
  RawMtrl VarChar(1) Raw Material default=N [N=No, Y=Yes]

# AITM - Items - History
Module: Inventory and Production | 322 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ItemCode
  ITEM_NAME: ItemName
  TREE_TYPE: TreeType
  COM_GROUP: CommisGrp
  SALE: SellItem
  PURCHASE: PrchseItem
  INVENTORY: InvntItem
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Number
  ItemName nVarChar(100) Item Description
  FrgnName nVarChar(100) Foreign Name
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  CstGrpCode Int(6) Customs Group default=-1 ->OARG
  VatGourpSa nVarChar(8) Tax Definition ->OVTG
  CodeBars nVarChar(254) Bar Code
  VATLiable VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  PrchseItem VarChar(1) Purchase Item default=Y [Y=Yes, N=No]
  SellItem VarChar(1) Sales Item default=Y [Y=Yes, N=No]
  InvntItem VarChar(1) Inventory Item default=Y [Y=Yes, N=No]
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Qty Ordered by Customers
  OnOrder Num(19,6) Qty Ordered from Vendors
  IncomeAcct nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  MaxLevel Num(19,6) Free1
  DfltWH nVarChar(8) Default Whse
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  SuppCatNum nVarChar(50) Mfr Catalog No.
  BuyUnitMsr nVarChar(100) Purchasing UoM default=Unit
  NumInBuy Num(19,6) No. of Items per Purchase Unit
  ReorderQty Num(19,6) Required (Purchasing UoM)
  MinLevel Num(19,6) Minimum Inventory Level
  LstEvlPric Num(19,6) Last Evaluated Price
  LstEvlDate Date(8) Date of Last Revaluation Price
  CustomPer Num(19,6) Customs Rate
  Canceled VarChar(1) Canceled Item [Yes/No] default=N [Y=Yes, N=No]
  MnufctTime Int(11) Production Date
  WholSlsTax VarChar(1) Tax Rate for Wholesaler
  RetilrTax VarChar(1) Sales Tax %
  SpcialDisc Num(19,6) Special Discount %
  DscountCod Int(6) Discount Code
  TrackSales VarChar(1) Follow-Up [Yes/No] default=N [Y=Yes, N=No]
  SalUnitMsr nVarChar(100) Sales UoM default=Unit
  NumInSale Num(19,6) No. of Items per Sales Unit
  Consig Num(19,6) Consignment Goods Whse
  QueryGroup Int(11) Properties default=0
  Counted Num(19,6) Counted Qty
  OpenBlnc Num(19,6) Opening Stock
  EvalSystem VarChar(1) Valuation Method [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch]
  UserSign Int(6) User Signature ->OUSR
  FREE VarChar(1) Free Item [Y/N] default=N [Y=Yes, N=No]
  PicturName nVarChar(200) Picture
  Transfered VarChar(1) Year Transferred [Y/N] default=N [Y=Yes, N=No]
  BlncTrnsfr VarChar(1) Balances Transferred [Y/N] default=N [Y=Yes, N=No]
  UserText Text(16) Item Remarks
  SerialNum nVarChar(17) Serial Number
  CommisPcnt Num(19,6) Commission % for Item
  CommisSum Num(19,6) Total Commission for Item
  CommisGrp Int(6) Commission Group default=0 ->OCOG
  TreeType VarChar(1) Bill of Materials Type default=N [N=Not a BOM, A=Assembly, S=Sales, P=Production, T=Template]
  TreeQty Num(19,6) No. of Units
  LastPurPrc Num(19,6) Last Purchase Price
  LastPurCur nVarChar(3) Last Purchase Currency
  LastPurDat Date(8) Last Purchase Date
  ExitCur nVarChar(3) Release Currency
  ExitPrice Num(19,6) Release Price
  ExitWH nVarChar(8) Release Warehouse
  AssetItem VarChar(1) Fixed Asset Indicator default=N [Y=Yes, N=No]
  WasCounted VarChar(1) Counted default=N [Y=Yes, N=No]
  ManSerNum VarChar(1) Serial No. Management default=N [Y=Yes, N=No]
  SHeight1 Num(19,6) Height 1 - Sales Unit
  SHght1Unit Int(6) Height 1 - UoM for Sales
  SHeight2 Num(19,6) Height 2 - Sales Unit
  SHght2Unit Int(6) Height 2 - UoM for Sales
  SWidth1 Num(19,6) Width 1 - Sales Unit
  SWdth1Unit Int(6) Width 1 - UoM for Sales
  SWidth2 Num(19,6) Width 2 - Sales Unit
  SWdth2Unit Int(6) Width 2 - UoM for Sales
  SLength1 Num(19,6) Length 1 - Sales Unit
  SLen1Unit Int(6) Length 1 - UoM for Sales
  Slength2 Num(19,6) Length 2 - Sales Unit
  SLen2Unit Int(6) Length 2 - UoM for Sales
  SVolume Num(19,6) Volume - Sales Unit
  SVolUnit Int(6) Volume - UoM for Sales
  SWeight1 Num(19,6) Weight 1 - Sales Unit
  SWght1Unit Int(6) Weight 1 - UoM for Sales
  SWeight2 Num(19,6) Weight 2 - Sales Unit
  SWght2Unit Int(6) Weight 2 - UoM for Sales
  BHeight1 Num(19,6) Height 1 - Purchasing Unit
  BHght1Unit Int(6) Height 1 - UoM for Purchasing
  BHeight2 Num(19,6) Height 2 - Purchasing Unit
  BHght2Unit Int(6) Height 2 - UoM for Purchasing
  BWidth1 Num(19,6) Width 1 - Purchasing Unit
  BWdth1Unit Int(6) Width 1 - UoM for Purchasing
  BWidth2 Num(19,6) Width 2 - Purchasing Unit
  BWdth2Unit Int(6) Width 2 - UoM for Purchasing
  BLength1 Num(19,6) Length 1 - Purchase Unit
  BLen1Unit Int(6) Length 1 - UoM for Purchasing
  Blength2 Num(19,6) Length 2 - Purchase Unit
  BLen2Unit Int(6) Length 2 - UoM for Purchasing
  BVolume Num(19,6) Volume - Purchasing Unit
  BVolUnit Int(6) Volume - UoM for Purchasing
  BWeight1 Num(19,6) Weight 1 - Purchasing Unit
  BWght1Unit Int(6) Weight 1 - UoM for Purchasing
  BWeight2 Num(19,6) Weight 2 - Purchasing Unit
  BWght2Unit Int(6) Weight 2 - UoM for Purchasing
  FixCurrCms nVarChar(3) Currency of Fixed Commission
  FirmCode Int(6) Manufacturer default=-1 ->OMRC
  LstSalDate Date(8) Last Sale Date
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
  CreateDate Date(8) Production Date
  UpdateDate Date(8) Date of Update
  ExportCode nVarChar(20) Data Export Code
  SalFactor1 Num(19,6) Sales Factor 1
  SalFactor2 Num(19,6) Sales Factor 2
  SalFactor3 Num(19,6) Sales Factor 3
  SalFactor4 Num(19,6) Sales Factor 4
  PurFactor1 Num(19,6) Purchasing Factor 1
  PurFactor2 Num(19,6) Purchasing Factor 2
  PurFactor3 Num(19,6) Purchasing Factor 3
  PurFactor4 Num(19,6) Purchasing Factor 4
  SalFormula nVarChar(40) Sales Formula
  PurFormula nVarChar(40) Purchasing Formula
  VatGroupPu nVarChar(8) Tax Definition ->OVTG
  AvgPrice Num(19,6) Item Cost
  PurPackMsr nVarChar(30) Packaging UoM (Purchasing) default=Box
  PurPackUn Num(19,6) Quantity per Package (Purchasing)
  SalPackMsr nVarChar(30) Packaging UoM (Sales) default=Box
  SalPackUn Num(19,6) Quantity per Package (Sales)
  SCNCounter Int(6) SCN Counter
  ManBtchNum VarChar(1) Manage Batch No. [Yes/No] default=N [Y=Yes, N=No]
  ManOutOnly VarChar(1) Manage SN on Release Only default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer, G=Fixed Assets Migration]
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  BlockOut VarChar(1) Force Selection of Serial No. or Batch No. default=Y [Y=Yes, N=No]
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type ->ADP1
  SWW nVarChar(16) Additional Identifier
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  DocEntry Int(11) Numerator
  ExpensAcct nVarChar(15) Expense Account ->OACT
  FrgnInAcct nVarChar(15) Revenue Account - Foreign ->OACT
  ShipType Int(6) Shipping Type ->OSHP
  GLMethod VarChar(1) Set G/L Accounts By default=W [W=Warehouse, C=Item Group, L=Item Level]
  ECInAcct nVarChar(15) Revenue Account - EU
  FrgnExpAcc nVarChar(15) Expense Account - Foreign
  ECExpAcc nVarChar(15) Expense Account - EU
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, U=Use Tax, N=No Tax]
  ByWh VarChar(1) Manage Inventory by Warehouse
  WTLiable VarChar(1) Withholding Tax Liable default=Y [Y=Yes, N=No]
  ItemType VarChar(1) Item Type default=I [I=Items, L=Labor, T=Travel, F=Fixed Assets]
  WarrntTmpl nVarChar(20) Warranty Template ->OCTT
  BaseUnit nVarChar(20) Base Unit Name
  CountryOrg nVarChar(3) Country of Origin
  StockValue Num(19,6) Inventory Value
  Phantom VarChar(1) Phantom Item default=N [Y=Yes, N=No]
  IssueMthd VarChar(1) Issue Method default=B [B=Backflush, M=Manual]
  FREE1 VarChar(1) Yield in %
  PricingPrc Num(19,6) Pricing Percentage
  MngMethod VarChar(1) Management Method default=R [A=On Every Transaction, R=On Release Only]
  ReorderPnt Num(19,6) Reorder Point
  InvntryUom nVarChar(100) Inventory UoM
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  IndirctTax VarChar(1) Indirect Tax default=N [Y=Yes, N=No]
  TaxCodeAR nVarChar(8) Sales Tax Code ->OSTC
  TaxCodeAP nVarChar(8) Purchasing Tax Code ->OSTC
  OSvcCode Int(11) Outgoing Service Code ->OSCD
  ISvcCode Int(11) Incoming Service Code ->OSCD
  ServiceGrp Int(11) Service Group ->OSGP
  NCMCode Int(11) NCM Code ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  ServiceCtg Int(11) Service Category default=-1 [-1=] ->OSCG
  ItemClass VarChar(1) Service or Material default=2 [2=Material, 1=Service]
  Excisable VarChar(1) Excisable [Yes/No] default=N [Y=Yes, N=No]
  ChapterID Int(11) Chapter ID default=-1 ->OCHP
  NotifyASN nVarChar(40) Notification Availed SN.
  ProAssNum nVarChar(20) Provisional Assessment No.
  AssblValue Num(19,6) Assessable Value
  DNFEntry Int(11) DNF Code Entry default=-1 ->ODNF
  UserSign2 Int(6) Updating User ->OUSR
  Spec nVarChar(30) Item Specification
  TaxCtg nVarChar(4) Tax Category
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  FuelCode Int(11) Fuel default=-1 ->OBFI
  BeverTblC nVarChar(2) Beverage Table ->OBSI
  BeverGrpC nVarChar(2) Beverage Group ->OBSI
  BeverTM Int(11) Beverage Brand default=-1 ->OBNI
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  ToleranDay Int(11) Tolerance Days
  UgpEntry Int(11) UoM Group ->OUGP
  PUoMEntry Int(11) Default Purchase UoM ->OUOM
  SUoMEntry Int(11) Default Sales UoM ->OUOM
  IUoMEntry Int(11) Inventory UoM ->OUOM
  IssuePriBy Int(6) Issue Primarily By SnB or Bin [0=Issue Primarily by Serial/Batch Number, 1=Issue Primarily by Bin Location]
  AssetClass nVarChar(20) Asset Class ->OACS
  AssetGroup nVarChar(15) Asset Group ->OAGS
  InventryNo nVarChar(12) Inventory Number of Asset
  Technician Int(11) Technician of Fixed Asset ->OHEM
  Employee Int(11) Employee of Fixed Asset ->OHEM
  Location Int(11) Location ->OLCT
  StatAsset VarChar(1) Owned by Company default=N [Y=Yes, N=No]
  Cession VarChar(1) Cession default=N [Y=Yes, N=No]
  DeacAftUL VarChar(1) Deactivate After Useful Life default=N [Y=Yes, N=No]
  AsstStatus VarChar(1) Asset Status default=N [N=New, A=Active, I=Inactive]
  CapDate Date(8) Capitalization Date
  AcqDate Date(8) Acquisition Date
  RetDate Date(8) Retirement Date
  GLPickMeth VarChar(1) G/L Account Pick Method default=A [A=General, W=Warehouse, C=Item Group]
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  MgrByQty VarChar(1) Manage Asset by Quantity default=N [Y=Yes, N=No]
  AssetRmk1 nVarChar(100) Asset Remark 1
  AssetRmk2 nVarChar(100) Asset Remark 2
  AssetAmnt1 Num(19,6) Asset Amount 1
  AssetAmnt2 Num(19,6) Asset Amount 2
  DeprGroup nVarChar(15) Depreciation Group ->OADG
  AssetSerNo nVarChar(32) Asset Serial Number
  CntUnitMsr nVarChar(100) Inventory Counting UoM Name
  NumInCnt Num(19,6) No. of Items per Counting Unit
  INUoMEntry Int(11) Inventory Counting UoM Entry ->OUOM
  OneBOneRec VarChar(1) One Batch One Receipt default=N [Y=Yes, N=No]
  RuleCode nVarChar(2) Checking Rule Code ->ODCR
  ScsCode nVarChar(10) Scs Code
  SpProdType nVarChar(2) Special Product Type [MT=Cellular Phones, IO=Integrated Circuits]
  IWeight1 Num(19,6) Weight 1 - Inventory
  IWght1Unit Int(6) Weight 1 - Inventory Unit
  IWeight2 Num(19,6) Weight 2 - Inventory
  IWght2Unit Int(6) Weight 2 - Inventory Unit
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VirtAstItm VarChar(1) Virtual Asset Item default=N [N=No, Y=Yes]
  SouVirAsst nVarChar(50) Source Virtual Asset Item ->OITM
  InCostRoll VarChar(1) Include in Prod. Cost Rollup default=Y [Y=Yes, N=No]
  PrdStdCst Num(19,6) Production Std Cost
  EnAstSeri VarChar(1) Enforce Asset Serial Numbers default=N [Y=Yes, N=No]
  LinkRsc nVarChar(50) Linked Resource ->ORSC
  OnHldPert Num(19,6) Capital Goods On Hold Percent
  onHldLimt Num(19,6) Capital Goods on Hold Limit
  PriceUnit Int(11) Pricing Unit ->OUOM
  GSTRelevnt VarChar(1) GST Relevant default=N [Y=Yes, N=No]
  SACEntry Int(11) SAC Entry default=-1 ->OSAC
  GstTaxCtg VarChar(1) GST Tax Category default=R [R=Regular, N=Nil Rated, E=Exempt]
  AssVal4WTR Num(19,6) Assessable Value for WTR
  ExcImpQUoM Int(11) Default Excise Imported Quantity UoM [112=Liters, m3, 168=Tonne, metric ton (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcFixAmnt Num(19,6) Default Excise Fixed Amount
  ExcRate Num(19,6) Default Excise Rate
  SOIExc VarChar(1) SOI Excisable default=4 [1=Excisable, 2=Exemption of excises, 3=Excises are paid to another authority, 4=Not Excisable]
  TNVED nVarChar(10) TNVED Code
  Imported VarChar(1) Imported Item default=N [Y=Yes, N=No]
  AutoBatch VarChar(1) Automatic Batch Creation default=N [Y=Yes, N=No]
  CstmActing VarChar(1) Customer Accounting default=N [N=No, Y=Yes]

# AITT - Product Tree - History
Module: Inventory and Production | 27 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstac, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(50) Parent Item ->OITM
  TreeType VarChar(1) BOM Type default=P [A=Assembly, S=Sales, P=Production, T=Template]
  PriceList Int(6) Price List default=0 ->OPLN
  Qauntity Num(19,6) No. of Units
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SCNCounter Int(6) SCN Counter
  DispCurr nVarChar(3) Display Currency
  ToWH nVarChar(8) Whse for Finished Product
  Object nVarChar(20) Object Type default=66
  LogInstac Int(11) Log Instance - History
  UserSign2 Int(11) Updating User ->OUSR
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  HideComp VarChar(1) Hide Components in Printing default=N [Y=Yes, N=No]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  UpdateTime Int(11) Time of Update
  Project nVarChar(20) Project Code ->OPRJ
  PlAvgSize Num(19,6) Planned Average Production Size default=1
  Name nVarChar(100) Product Description
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateTS Int(11) Update Full Time

# AITW - Items - Warehouse - History
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: logInstanc, WhsCode, ItemCode
  ITEM: ItemCode
  WHS: WhsCode
  COUNTED: WasCounted
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Defined
  OnOrder Num(19,6) Ordered
  Consig Num(19,6) Consignment Goods WH
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  MinStock Num(19,6) Min. Stock
  MaxStock Num(19,6) Max. Stock
  MinOrder Num(19,6) Min. Order
  AvgPrice Num(19,6) Average Price
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  BalInvntAc nVarChar(15) Inventory Acc. ->OACT
  SaleCostAc nVarChar(15) Cost Acc. ->OACT
  TransferAc nVarChar(15) Transfers Acc. ->OACT
  RevenuesAc nVarChar(15) Revenues Acct ->OACT
  VarianceAc nVarChar(15) Variance Acc. ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns ->OACT
  ExpensesAc nVarChar(15) Expenses Acct. ->OACT
  EURevenuAc nVarChar(15) Sales Revenue - EU ->OACT
  EUExpensAc nVarChar(15) EU Expenses Acc. ->OACT
  FrRevenuAc nVarChar(15) Sales Revenue - Foreign ->OACT
  FrExpensAc nVarChar(15) Foreign Expenses Acc. ->OACT
  ExmptIncom nVarChar(15) Exempt Revenues Account ->OACT
  PriceDifAc nVarChar(15) Price Differences Acc.
  ExchangeAc nVarChar(15) Exchange Rate Differences Acc.
  BalanceAcc nVarChar(15) Goods Clearing Acc.
  PurchaseAc nVarChar(15) Purchase Acc.
  PAReturnAc nVarChar(15) PA Return Acc.
  PurchOfsAc nVarChar(15) Purchase Offset Acc.
  ShpdGdsAct nVarChar(15) Shipped Goods Account
  VatRevAct nVarChar(15) VAT in Revenue Account
  StockValue Num(19,6) Stock Value
  DecresGlAc nVarChar(15) Decrease GL Acc.
  IncresGlAc nVarChar(15) Increase GL Acc.
  StokRvlAct nVarChar(15) Stock Inflation Adjust Account
  StkOffsAct nVarChar(15) Stock Inflation Offset Account
  WipAcct nVarChar(15) WIP Material Account
  WipVarAcct nVarChar(15) WIP Material Variance Account
  CostRvlAct nVarChar(15) Cost Inflation Account
  CstOffsAct nVarChar(15) Cost Inflation Offset Account
  ExpClrAct nVarChar(15) Expenses Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offsetting Account ->OACT
  Object nVarChar(20) Object Type - History default=31
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Update Date - History
  ARCMAct nVarChar(15) Sales Credit Acct
  ARCMFrnAct nVarChar(15) Sales Credit Foreign Acct
  ARCMEUAct nVarChar(15) Sales Credit EU Acct
  ARCMExpAct nVarChar(15) Exempted Credits
  APCMAct nVarChar(15) Purchase Credit Acct
  APCMFrnAct nVarChar(15) Foreign Purchase Credit Acct
  APCMEUAct nVarChar(15) EU Purchase Credit Acct
  RevRetAct nVarChar(15) Revenue Returns Account
  NegStckAct nVarChar(15) Negative Stock Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Acct
  PurBalAct nVarChar(15) Purchase Balance Account
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  Freezed VarChar(1) Item Frozen in Warehouse default=N [Y=Yes, N=No]
  FreezeDoc Int(11) INC Document Frozen By ->OINC
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account

# AKL1 - Pick List - Rows - History
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInsac, PickEntry, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPKL
  PickEntry Int(11) Row Number
  OrderEntry Int(11) Order Entry
  OrderLine Int(11) Order Row ID
  PickQtty Num(19,6) Picked Quantity
  PickStatus VarChar(1) Pick Status default=R [R=Released for Picking, Y=Picked, P=Picked, D=Partially Delivered, C=Closed]
  RelQtty Num(19,6) Released Quantity
  LogInsac Int(11) Log Instance - History
  PrevReleas Num(19,6) Previously Released Quantity
  BaseObject Int(11) Base Object Type [17=Order, 13=Reserve Invoice, 0=]

# AKL2 - Pick List for SnB and Bin Details
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, Pkl2LinNum, PickEntry, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPKL
  PickEntry Int(11) Row Number
  Pkl2LinNum Int(11) PKL2 Line Number
  ItemCode nVarChar(50) Item No. ->OITM
  ManagedBy Int(11) Management Method default=-1 [10000044=BTN, 10000045=SRN, -1=NOB]
  SnBEntry Int(11) SnB Abs. Entry
  BinAbs Int(11) Bin Internal Number ->OBIN
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  RelQtty Num(19,6) Released Quantity
  PickQtty Num(19,6) Picked Quantity
  ObjType nVarChar(20) Object Type default=156 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# AMGP - Material Group
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  CODE U: LogInstanc, MatGrp
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  MatGrp nVarChar(3) Material Group
  Descrip nVarChar(70) Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# AMR1 - Inventory Revaluation - History - Rows
Module: Inventory and Production | 23 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, LineNum, DocEntry
  ITEM_WHS: WhsCode, ItemCode
  ITEM: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OMRV
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  Dscription nVarChar(100) Item/Service Description
  Quantity Num(19,6) Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  RIncmAcct nVarChar(15) Inv. Reval. Increment Account
  RDcrmAcct nVarChar(15) Inv. Reval. Decrement Account
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RActPrice Num(19,6) Inv. Reval. Actual Price
  ROnHand Num(19,6) In Stock at Reval.
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=162
  EvalSystem VarChar(1) Cost Accounting Method [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch] ->OITM
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  UnitMsr nVarChar(100) Unit of Measure
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# AMR2 - Inventory Revaluation FIFO Rows (Archive)
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, BaseLine, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->MRV1
  BaseLine Int(11) Base Row Number
  LineNum Int(11) Row Number
  Quantity Num(19,6) Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RActPrice Num(19,6) Inventory Reval. Current Cost
  INMTransNm Int(11) INM Transaction Number
  INMInst Int(11) INM Instance
  INMTransTy Int(11) INM Transaction Type default=-1
  INMCreatBy Int(11) INM Document Key Created
  INMBaseRef nVarChar(11) INM Base Reference
  INMDocDate Date(8) INM Posting Date
  INMOpenQty Num(19,6) INM Open Quantity
  ObjType nVarChar(20) Object Type default=162
  LogInstanc Int(11) Log Instance default=0
  IVLTransSe Int(11) IVL Transaction Sequence No. default=-1
  IVLLayerID Int(11) IVL Layer ID default=-1
  INMLineNum Int(11) INM Row Number in Document
  INMSubLine Int(11) INM Subrow Number

# AMRV - Inventory Revaluation - History
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, DocEntry
  NUM: ObjType, LogInstanc, DocNum
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocDate Date(8) Posting Date
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  DocTime Int(6) Generation Time
  RevalType VarChar(1) Inventory Revaluation Type default=P [P=Price Change, M=Material Debit/Credit]
  UpdateDate Date(8) Update Date
  CreateDate Date(8) Creation Date
  Series Int(11) Series default=0 ->NNM1
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto. Incr., D=Data Document, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  StationID Int(11) Workstation ID ->CSTN
  RIncmAcct nVarChar(15) Invent. Reval. Expense Account
  RExpnAcct nVarChar(15) Invent. Reval. Expense Account
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=162
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  VersionNum nVarChar(11) Version Number
  InflaReval VarChar(1) Inflation-Based Revaluation default=N
  SupplCode nVarChar(254) Supplementary Code
  CardCode nVarChar(15) Customer/Vendor Code
  CardName nVarChar(100) Customer/Vendor Name
  CreatedBy VarChar(1) Entry Creation Origin default=M [M=Created Manually by User, W=Created by Production Cost Recalculation Wizard]

# APKL - Pick List - History
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstac, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry
  Name nVarChar(155) Name
  OwnerCode Int(6) Owner Code ->OUSR
  OwnerName nVarChar(155) Owner Name
  PickDate Date(8) Pick Date
  Remarks Text(16) Remarks
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  ShipType Int(6) Shipping Type
  Status VarChar(1) Status default=R [R=Released, Y=Picked, P=Partially Picked, D=Partially Delivered, C=Closed]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original, =]
  LogInstac Int(11) Log Instance - History
  ObjType nVarChar(20) Object Type default=156 ->ADP1
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]

# APLN - Price Lists
Module: Inventory and Production | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ListNum
  LIST_NAME U: LogInstanc, ListName
Fields (name type(len) description [values] ->parent table):
  ListNum Int(6) Price List No.
  ListName nVarChar(32) Price List Name
  BASE_NUM Int(6) Base Price List ->OPLN
  Factor Num(19,6) Factor
  RoundSys Int(6) Rounding Method default=0 [0=No Rounding, 1=Round to Full Decimal Amount, 2=Round to Full Amount, 3=Round to Full Tens Amount, 4=Fixed Ending, 5=Fixed Interval]
  GroupCode Int(6) Group No. default=1 [1=Group 1, 2=Group 2, 3=Group 3, 4=Group 4]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SPPCounter Int(11) SPP Counter
  UserSign Int(6) User Signature ->OUSR
  IsGrossPrc VarChar(1) Gross Price? default=N [Y=Gross, N=Net]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  ValidFor VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidFrom Date(8) Active From
  ValidTo Date(8) Active To
  CreateDate Date(8) Creation Date
  PrimCurr nVarChar(3) Primary Default Curreny
  AddCurr1 nVarChar(3) Additional Default Currency 1
  AddCurr2 nVarChar(3) Additional Default Currency 2
  RoundRule VarChar(1) Rounding Rule default=R [R=Round to Closest, C=Round Up, F=Round Down]
  ExtAmount Num(19,6) Fixed Amount (Ending/Interval)
  RndFrmtInt nVarChar(10) Ending/Interval - Integer Part
  RndFrmtDec nVarChar(10) Ending/Interval - Decimal Part

# AQI1 - Inventory Opening Balance - Rows
Module: Inventory and Production | 39 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, DocLineNum, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  DocLineNum Int(11) Row Number in Document
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  InvntryUom nVarChar(100) Inventory UoM
  OnHandBef Num(19,6) Quantity Stored in Warehouse
  Price Num(19,6) Price
  Quantity Num(19,6) Quantity - Delta
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  ObjType nVarChar(20) Object Type default=310000001
  Project nVarChar(20) Project Code ->OPRJ
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM [Y=Yes, N=No]
  InvUoMQty Num(19,6) Inventory UoM Qty
  BinEntry Int(11) Bin Location Entry ->OBIN
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  Remark nVarChar(254) Remarks
  Location Int(11) Location
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  LogInstanc Int(11) Log Instance - History
  BinNegQty VarChar(1) Allow Bin Negative Quantity default=N [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  ActPrice Num(19,6) Actual Price
  PostValueL Num(19,6) Posted Value LC
  PostValueS Num(19,6) Posted Value SC

# AQI2 - Inventory Opening Balance - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# AQI3 - Inventory Opening Balance - Tracking Note Assignment - History
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(20) Item CCD Number
  CntrOrigin nVarChar(3) Country of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=0
  SubLineNum Int(11) BOM Line No.

# AQR1 - Inventory Posting - Rows
Module: Inventory and Production | 50 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, DocLineNum, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  DocLineNum Int(11) Row Number in Document
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  InvntryUom nVarChar(100) Inventory UoM
  OnHandBef Num(19,6) Quantity Stored in Warehouse
  Price Num(19,6) Price
  Quantity Num(19,6) Quantity - Delta
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  ObjType nVarChar(20) Object Type default=10000071
  Project nVarChar(20) Project Code ->OPRJ
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  BinEntry Int(11) Bin Location Entry ->OBIN
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  CountDate Date(8) Count Date
  CountTime Int(11) Count Time
  DiffPercnt Num(19,6) Percentage Difference
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=1470000065 [-1=, 1470000065=Inventory Counting]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  CountQty Num(19,6) Counted Quantity
  Remark nVarChar(254) Remarks
  LogInstanc Int(11) Log Instance - History
  CpyCount Int(11) Copied Count default=0 [0=, 1=Inventory Taker One, 2=Two Takers - Taker 1, 3=Two Takers - Taker 2, 4=Two Takers - Items with Zero Difference]
  BinNegQty VarChar(1) Allow Bin Negative Quantity default=N [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  UgpEntry Int(11) UoM Group Entry ->OUGP
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
  UomCode nVarChar(20) UoM Code for DI
  ItmsPerUnt Num(19,6) Items per Unit for DI
  UomQty Num(19,6) UoM Counted Qty for DI
  ActPrice Num(19,6) Actual Price
  PostValueL Num(19,6) Posted Value LC
  PostValueS Num(19,6) Posted Value SC

# AQR2 - Inventory Counting - UoM
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, ChildNum, LineNum, DocEntry
  BUSINESS U: LogIns, UomCode, BarCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  BarCode nVarChar(254) Bar Code
  UomCode nVarChar(20) UoM Code ->OUOM
  UomQty Num(19,6) UoM Counted Qty
  CountQty Num(19,6) Counted Qty - Inventory UoM
  Tk1UomQty Num(19,6) Counter 1 UoM Counted Qty
  Tk2UomQty Num(19,6) -
  Tk1CntQty Num(19,6) Counter 1 Counted Qty of Inv.
  Tk2CntQty Num(19,6) -
  ItmsPerUnt Num(19,6) Items per Unit
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  TeamUomQty Num(19,6) Team UoM Counted Qty
  TeamCntQty Num(19,6) Team Counted Qty
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM

# AQR3 - Inventory Count - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# AQR4 - Inventory Opening Balance - Tracking Note Assignment - History
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(20) Item CCD Number
  CntrOrigin nVarChar(3) Country of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=0
  SubLineNum Int(11) BOM Line No.

# ASP1 - Special Prices - Data Areas
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LINENUM, ItemCode, CardCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OSPP
  CardCode nVarChar(15) BP Code ->OSPP
  LINENUM Int(6) Row Number
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount %
  ListNum Int(6) Price List No. default=0 ->OPLN
  FromDate Date(8) Date From
  ToDate Date(8) Date To
  AutoUpdt VarChar(1) Auto Update default=Y [Y=Yes, N=No]
  Expand VarChar(1) Item Details default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0

# ASP2 - Special Prices - Quantity Areas
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, SPP2LNum, SPP1LNum, ItemCode, CardCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  SPP1LNum Int(6) Dates Row Number
  SPP2LNum Int(6) Row Number
  Amount Num(19,6) Quantity
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount in %
  UomEntry Int(6) UoM Entry ->OUOM
  LogInstanc Int(11) Log Instance default=0

# ASPP - Special Prices
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ItemCode, CardCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount in %
  ListNum Int(6) Price List No. default=0 ->OPLN
  AutoUpdt VarChar(1) Auto Update default=Y [Y=Yes, N=No]
  EXPAND VarChar(1) Item Details default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  SrcPrice Int(6) Source Price default=0 [0=Unit Price - Pri. Crcy, 1=Unit Price - Add. Crcy 1, 2=Unit Price - Add. Crcy 2]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Update Date
  Valid VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidFrom Date(8) Active From
  ValidTo Date(8) Active To

# ASRN - Serial Numbers Master Data
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  SYSTEM_KEY U: LogInstanc, SysNumber, ItemCode
  DIST_KEY: DistNumber, ItemCode
  LOT_KEY: LotNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Serial Number
  MnfSerial nVarChar(36) Manufacturer Serial No.
  LotNumber nVarChar(36) Lot Number
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Mfr Warranty Start Date
  GrntExp Date(8) Mfr Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Location
  Status VarChar(1) Status [0=Available, 1=Unavailable]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) Abs Entry
  ObjType nVarChar(20) Object Type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

# ATS1 - Transporter - Transportations
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transporter Abs. Entry
  LineNum Int(11) Line Number
  TransMode Int(11) Mode ->OETM
  VehicleTyp nVarChar(2) Vehicle Type ->OEVT
  VehicleNo nVarChar(15) Vehicle Number
  LogInstanc Int(11) Log Instance default=0

# ATSP - Transporters
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transporter Abs. Entry
  TransCode nVarChar(20) Transporter Code
  TransName nVarChar(25) Transporter Name
  TransID nVarChar(15) Transporter ID
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]

# ATT1 - Bill of Materials - Components - History
Module: Inventory and Production | 28 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LogInstanc, Father
  VISORDER U: VisOrder, LogInstanc, Father
Fields (name type(len) description [values] ->parent table):
  Father nVarChar(50) Parent Item ->OITT
  ChildNum Int(11) Child Element No.
  VisOrder Int(11) Visual Order
  Code nVarChar(50) Child Code
  Quantity Num(19,6) Quantity
  Warehouse nVarChar(8) Warehouse ->OWHS
  Price Num(19,6) Price
  Currency nVarChar(3) Currency
  PriceList Int(6) Price List default=0 ->OPLN
  OrigPrice Num(19,6) Original Price
  OrigCurr nVarChar(3) Original Currency
  IssueMthd VarChar(1) Issue Method [B=Backflush, M=Manual]
  Uom nVarChar(100) Inventory UOM
  Comment nVarChar(254) Comment
  LogInstanc Int(11) Log Instance
  Object nVarChar(20) Object default=66
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  PrncpInput VarChar(1) Principal Input default=N [Y=Yes, N=No]
  Project nVarChar(20) Project Code ->OPRJ
  Type Int(11) Component Type default=4 [4=Item, 290=Resource, -18=Text]
  WipActCode nVarChar(15) WIP Account Code ->OACT
  AddQuantit Num(19,6) Additional Quantity
  LineText Text(16) Row Text
  StageId Int(11) Stage ID

# ATT2 - BOM - Route Stages - History
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, StageId, Father
  SEQUENCE U: LogInstanc, SeqNum, Father
Fields (name type(len) description [values] ->parent table):
  Father nVarChar(50) Parent Item ->OITT
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  WaitDays Num(19,6) Waiting Days default=0

# AUG1 - UoM Group Detail
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, UgpEntry
Fields (name type(len) description [values] ->parent table):
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  UomEntry Int(11) UoM Abs. Entry ->OUOM
  AltQty Num(19,6) Alternative Quantity
  BaseQty Num(19,6) Base Quantity
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  WghtFactor Int(6) Weight Factor default=0 ->OWGT
  UdfFactor Int(11) UDF Factor default=-1

# AUGP - UoM Group
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, UgpEntry
Fields (name type(len) description [values] ->parent table):
  UgpEntry Int(11) UoM Group Abs. Entry
  UgpCode nVarChar(20) UoM Group Code
  UgpName nVarChar(100) UoM Group Name
  BaseUom Int(11) Base UoM Abs. Entry ->OUOM
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]

# AUOM - UoM Master Data
Module: Inventory and Production | 30 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, UomEntry
Fields (name type(len) description [values] ->parent table):
  UomEntry Int(11) UoM Abs. Entry
  UomCode nVarChar(20) UoM Code
  UomName nVarChar(100) UoM Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(6) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  WghtUnit Int(6) Weight UoM
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  IntSymbol nVarChar(20) International Symbol
  EwbUnit Int(11) EWB Unit ->OEUT

# AWHS - Warehouses - History
Module: Inventory and Production | 102 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: logInstanc, WhsCode
Fields (name type(len) description [values] ->parent table):
  WhsCode nVarChar(8) Warehouse Code
  WhsName nVarChar(100) Warehouse Name
  IntrnalKey Int(11) Internal Key
  Grp_Code nVarChar(4) Group Code
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Allocation Account ->OACT
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns Account ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Revenue Account - EU ->OACT
  EUExpensAc nVarChar(15) Expense Account - EU ->OACT
  FrRevenuAc nVarChar(15) Revenue Account - Foreign ->OACT
  FrExpensAc nVarChar(15) Expense Account - Foreign ->OACT
  VatGroup nVarChar(8) Tax Group ->OSTC
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County ->OCNT
  Country nVarChar(3) Country ->OCRY
  State nVarChar(3) Status ->OCST
  Location Int(11) Location ->OLCT
  DropShip VarChar(1) Drop-Ship default=N [N=No, Y=Yes]
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  UseTax VarChar(1) Allow Use Tax default=N [Y=Yes, N=No]
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  ExchangeAc nVarChar(15) Exchange Rate Differences Account ->OACT
  BalanceAcc nVarChar(15) Goods Clearing Account ->OACT
  PurchaseAc nVarChar(15) Purchase Account ->OACT
  PAReturnAc nVarChar(15) Purchase Return Account ->OACT
  PurchOfsAc nVarChar(15) Purchase Offset Account ->OACT
  FedTaxID nVarChar(32) Federal Tax ID
  Building Text(16) Building/Floor/Room
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  Nettable VarChar(1) Nettable default=Y [Y=Yes, N=No]
  StokRvlAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkOffsAct nVarChar(15) Inventory Revaluation Offset Account ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  CostRvlAct nVarChar(15) COGS Revaluation Account ->OACT
  CstOffsAct nVarChar(15) COGS Revaluation Offset Acct ->OACT
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  objType nVarChar(20) Object Type - History default=64
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  ARCMAct nVarChar(15) Sales Credit Acct ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Foreign Acct ->OACT
  ARCMEUAct nVarChar(15) Sales Credit EU Acct ->OACT
  ARCMExpAct nVarChar(15) Exempted Credits ->OACT
  APCMAct nVarChar(15) Purchase Credit Acct ->OACT
  APCMFrnAct nVarChar(15) Foreign Purchase Credit Acct ->OACT
  APCMEUAct nVarChar(15) EU Purchase Credit Acct ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account ->OACT
  BPLid Int(11) Business Place ID ->OBPL
  OwnerCode VarChar(1) Owner Code default=1 [1=Company Item Property, 2=Third-Party Warehouse, 3=Third-Party Warehouse]
  NegStckAct nVarChar(15) Negative Stock Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Acct ->OACT
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  Excisable VarChar(1) Excisable [Yes/No] default=N [Y=Yes, N=No]
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WhShipTo nVarChar(100) Ship-to Name (WH)
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  StorKeeper Int(11) Storekeeper ->OHEM
  Shipper nVarChar(15) Shipper ->OCRD
  BinActivat VarChar(1) Bin Activated [Y/N] default=N [Y=Yes, N=No]
  BinSeptor nVarChar(5) Bin Separator default=-
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  AutoIssMtd Int(6) Auto. Issue Method default=0 [0=Single Choice, 1=Bin Location Code Order, 2=Alternative Sort Code Order, 3=Descending Quantity, 4=Ascending Quantity, 7=Ascending Quantity - Single Bin Preferred, 5=FIFO, 6=LIFO]
  ManageSnB VarChar(1) Drop-Ship Manage SnB default=N [N=No, Y=Yes]
  RecItemsBy Int(6) Receiving Bin Locations Method default=0 [0=Bin Location Code Order, 1=Alternative Sort Code Order]
  RecBinEnab VarChar(1) Enable Receiving Bin Locations default=N [Y=Yes, N=No]
  GlblLocNum nVarChar(50) Global Location Number
  RecvEmpBin VarChar(1) Restrict Receipts to Empty Bin default=Y [Y=Yes, N=No]
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  RecvMaxQty VarChar(1) Recv. up to Max. Qty default=N [Y=Yes, N=No]
  AutoRecvMd Int(6) Auto. Receipt Method default=0 [0=Default Bin Location, 1=Last Bin Location That Received Item, 2=Item's Current Bin Locations, 3=Item's Current and Historical Bin Locations]
  RecvMaxWT VarChar(1) Recv. up to Max. Weight default=N [Y=Yes, N=No]
  RecvUpTo nVarChar(6) Receive up to default=0 [0=Maximum Qty, 1=Maximum Weight, 2=Max. Qty and Weight]
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account
  TaxOffice nVarChar(50) Tax Office
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  External VarChar(1) External default=N [N=No, Y=Yes]

# AWO1 - Production Order (Rows) - History
Module: Inventory and Production | 37 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, DocEntry
  VISORDER U: LogInstanc, VisOrder, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item No.
  BaseQty Num(19,6) Base Quantity
  PlannedQty Num(19,6) Planned Quantity - Rows
  IssuedQty Num(19,6) Issued Quantity
  IssueType VarChar(1) Production Order Issue Type [M=Manual, B=Backflush]
  wareHouse nVarChar(8) Warehouse ->OWHS
  VisOrder Int(11) Visual Order
  WipActCode nVarChar(15) WIP Account Code ->OACT
  CompTotal Num(19,6) Total Completed Sum
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  LocCode Int(11) Location Code ->OLCT
  LogInstanc Int(11) Log Instance default=0
  Project nVarChar(20) Project Code ->OPRJ
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  ItemType Int(11) Item Type default=4 [4=Item, 290=Resource, -18=Text]
  AdditQty Num(19,6) Additional Quantity
  LineText Text(16) Row Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Release for Picking, P=Partially Picked]
  PickQty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick List ID Number
  ReleaseQty Num(19,6) Released Quantity
  ResAlloc VarChar(1) Resource Allocation [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  StageId Int(11) Stage ID
  BaseQtyNum Num(19,6) Base Quantity Numerator
  BaseQtyDen Num(19,6) Base Quantity Denominator
  ReqDays Num(19,6) Required Days default=0
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  Status VarChar(1) Stage Status default=P [P=Planned, I=In Progress, C=Complete]

# AWO2 - Production Order - Base
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, BaseLine, BaseEntry, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  BaseEntry Int(11) Production Order Base Entry ->RDR1
  BaseNum Int(11) Production Order Base Number
  BaseLine Int(11) Production Order Base Line
  LogInstanc Int(11) Log Instance default=0

# AWO3 - Production Order - (Closure) - History
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LayerID, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number
  LineNum Int(11) Row Number
  LayerID Int(11) Layer ID
  Quantity Num(19,6) Quantity
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RToStockSc Num(19,6) Reval. Amt Posted to Stock (SC)
  WhsCode nVarChar(8) Warehouse Code
  IVLTransSe Int(11) IVL Transaction Sequence No.
  IVLLayerID Int(11) IVL Layer ID
  SnbSysNum Int(11) SNB System Number
  SnbAbsEnt Int(11) SNB Abs. Entry
  LogInstanc Int(11) Log Instance default=0
  INMSubLine Int(11) INM Subrow Number default=-1

# AWO4 - Production Order - Route Stages - History
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, StageId, DocEntry
  SEQUENCE U: LogInstanc, SeqNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->AWOR
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  Status VarChar(1) Stage Status default=O [O=Open, C=Closed]
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  ReqDays Num(19,6) Required Days default=0
  WaitDays Num(19,6) Waiting Days default=0

# AWO5 - Production Order - Document Reference Information - History
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number
  ObjType nVarChar(20) Object Type default=202
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks

# AWOR - Production Order - History
Module: Inventory and Production | 57 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, DocEntry
  NUM U: LogInstanc, PIndicator, DocNum
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series default=0 ->NNM1
  ItemCode nVarChar(50) Product No. ->OITT
  Status VarChar(1) Production Order Status default=P [P=Planned, R=Released, L=Closed, C=Canceled]
  Type VarChar(1) Production Order Type default=S [S=Standard, P=Special, D=Disassembly]
  PlannedQty Num(19,6) Planned Quantity - Header
  CmpltQty Num(19,6) Completed Quantity
  RjctQty Num(19,6) Rejected Quantity
  PostDate Date(8) Order Date
  DueDate Date(8) Due Date
  OriginAbs Int(11) Production Order Origin Entry
  OriginNum Int(11) Production Order Origin Number
  OriginType VarChar(1) Production Order Origin default=M [M=Manual, R=MRP, S=Sales Order, U=Upgrade]
  UserSign Int(6) User Signature ->OUSR
  Comments nVarChar(254) Remarks
  CloseDate Date(8) Closing Date
  RlsDate Date(8) Release Date
  CardCode nVarChar(15) Customer Code ->OCRD
  Warehouse nVarChar(8) Warehouse ->OWHS
  Uom nVarChar(100) Inv. UoM in Production Order
  LineDirty Int(11) Line Modified
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  CreateDate Date(8) Creation Date
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  PIndicator nVarChar(10) Period Indicator ->OPID
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  Project nVarChar(20) Project Code ->OPRJ
  SupplCode nVarChar(254) Supplementary Code
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  PickRmrk nVarChar(254) Pick Remarks
  SysCloseDt Date(8) System Closing Date
  SysCloseTm Int(6) System Closing Time
  CloseVerNm nVarChar(11) Closing Version Number
  StartDate Date(8) Start Date
  ObjType nVarChar(20) Object Type default=202
  ProdName nVarChar(100) Product Description
  Priority Int(6) Priority default=100
  RouDatCalc VarChar(1) Routing Date Calculation default=S [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  UpdAlloc VarChar(1) Update Allocation default=M [M=Manual, A=Auto]
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VersionNum nVarChar(11) Version Number
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SAPPassprt Text(16) Extended SAP Passport

# CCS1 - Cycle Count Determination- Subtable
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Entry, WhsCode
Fields (name type(len) description [values] ->parent table):
  WhsCode nVarChar(8) Warehouse Code
  Entry Int(11) Entry
  CycleCode Int(6) Cycle Code
  Alert VarChar(1) Alert default=N [Y=Yes, N=No]
  DestUser Int(6) Destination User
  NextDate Date(8) Next Counting Date
  Time Int(6) Time
  ExcldZrQty VarChar(1) Exclude Zero Quantity default=Y [Y=Yes, N=No]
  Alerted VarChar(1) Alerted default=N [N=No, Y=Yes]
  ChangExist VarChar(1) Change Existing Items in DI default=N [N=No, Y=Yes]

# CIVI - IVI Config File
Module: Inventory and Production | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  EnableRun VarChar(1) Enable Run default=N [Y=Yes, N=No]
  EnblRunDt Date(8) Enable Run Date
  MsgSource Int(11) Object ID of Message Source
  IsOILMUpd VarChar(1) Is OILM Updated default=N [N=No, Y=Yes]
  EnblDays Int(11) Enable Valid In Days default=30
  LstChkMsg Int(11) Last Checked OILM Message
  LstMsgDate Date(8) Last Build Message Date
  LstHndlMsg Int(11) Last Handled OILM Message
  EnableUpd VarChar(1) Enable Update default=Y [Y=Yes, N=No]
  IgnPreUpd VarChar(1) Ignore Previous Update default=N [Y=Yes, N=No]
  ForceRSP VarChar(1) Force RSP Precheck default=N [Y=Yes, N=No]
  ReorderFrm Date(8) Reorder 8.8 Messages: From Date
  ReorderTo Date(8) Reorder 8.8 Messages: To Date
  InitMap VarChar(1) Initialize MAP Items
  InitStd VarChar(1) Initialize STD Items

# EDG1 - Discount Groups Rows
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjKey, ObjType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry ->OEDG
  ObjType nVarChar(20) Object Type [52=Item Groups, 8=Item Properties, 43=Manufacturer, 4=Items]
  ObjKey nVarChar(50) Object Key
  DiscType VarChar(1) Discount Type default=D [D=Discount, P=Pay for/Get for Free]
  Discount Num(19,6) Discount
  PayFor Num(19,6) Paid Qty
  ForFree Num(19,6) Free Qty
  UpTo Num(19,6) Max. Free Qty
  LogInstanc Int(11) Log Instance default=0

# ENT1 - Entry - Rows
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Entry ->OINV
  LineNum Int(11) Row Number
  BaseEntry Int(11) Base Document Internal ID
  PackQty Num(19,6) Packing Quantity
  PurPackMsr nVarChar(8) Packaging UoM Name default=Pack
  ArsnalName nVarChar(20) Storage Group Name
  ArsnalCode nVarChar(20) Storage Group Code
  UnitMsr nVarChar(20) Ref. UoM (Type) default=Unit
  Quantity Num(19,6) Quantity
  Fraction Num(19,6) Remainder
  Weight1 Num(19,6) Weight
  LineTotal Num(19,6) Row Total
  ItemCode nVarChar(50) Item No. ->OITM

# ICD1 - Inventory Counting Draft - Rows
Module: Inventory and Production | 41 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OICD
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  ItemDesc nVarChar(100) Item Description
  Freeze VarChar(1) Item Freeze Status default=N [Y=Yes, N=No]
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  InWhsQty Num(19,6) In-Whse Qty on Count Date
  Counted VarChar(1) Counted default=N [Y=Yes, N=No]
  CountQty Num(19,6) Counted Quantity
  CountQtyT1 Num(19,6) Counter 1 - Counted Quantity
  CountQtyT2 Num(19,6) -
  Remark nVarChar(254) Remarks
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  Difference Num(19,6) Difference
  DiffPercen Num(19,6) Difference %
  CountDate Date(8) Count Date
  CountTime Int(11) Count Time
  TargetRef nVarChar(16) Target Document Reference
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 10000071=Inventory Posting]
  TargetEntr Int(11) Target Document Internal ID
  TargetLine Int(11) Target Document Row
  ProjCode nVarChar(20) Project Code ->OPRJ
  OcrCode nVarChar(8) Distribution Rule Code ->OOCR
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  BinEntry Int(11) Bin Location Entry ->OBIN
  VisOrder Int(11) Visual Order
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  PrefVendor nVarChar(15) Preferred Vendor ->OCRD
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Entry ->OUGP
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
  CountDiff Num(19,6) Counters' Diff.
  CountDiffP Num(19,6) Counters' Diff. (%)
  UomCode nVarChar(20) UoM Code for DI
  UomQty Num(19,6) UoM Counted Qty for DI

# ICD10 - Inventory Counting Draft - Individual Counter - Row UoM
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  CounterNum Int(11) Counter Number
  UomQty Num(19,6) UoM Counted Qty
  InvtQty Num(19,6) Counted Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# ICD11 - Inventory Counting Draft - Individual Counter - Row SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  CounterNum Int(11) Counter Number

# ICD2 - Inventory Counting Draft - UoM
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
  BUSINESS U: UomCode, BarCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OICD
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  BarCode nVarChar(254) Bar Code
  UomCode nVarChar(20) UoM Code ->OUOM
  UomQty Num(19,6) UoM Counted Qty
  CountQty Num(19,6) Counted Qty of Inventory UoM
  Tk1UomQty Num(19,6) Counter 1 UoM Counted Qty
  Tk2UomQty Num(19,6) -
  Tk1CntQty Num(19,6) Counter 1 Counted Qty of Inv.
  Tk2CntQty Num(19,6) -
  ItmsPerUnt Num(19,6) Items per Unit
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  TeamUomQty Num(19,6) Team UoM Counted Qty
  TeamCntQty Num(19,6) Team Counted Qty
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM

# ICD3 - Inventory Count Draft - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OICD
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# ICD4 - Inventory Counting Draft - Team Counters
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, DocEntry
  BUSINESS U: CounterId, CounteType, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  CounterNum Int(11) Counter Number
  CounteType Int(11) Type of Counter default=12 [12=User, 171=Employee]
  CounterId Int(11) Counter ID
  CounteName nVarChar(155) Counter Name
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# ICD5 - Inventory Counting Draft - Team Counter - Row Counted Qty
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  CounterNum Int(11) Counter Number
  TotalQty Num(19,6) Total Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# ICD6 - Inventory Counting Draft - Team Counter - Row UoM
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  CounterNum Int(11) Counter Number
  UomQty Num(19,6) UoM Counted Qty
  InvtQty Num(19,6) Counted Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# ICD7 - Inventory Counting Draft - Team Counter - Row SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  CounterNum Int(11) Counter Number

# ICD8 - Inventory Counting Draft - Individual Counters
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, DocEntry
  BUSINESS U: CounterId, CounteType, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  CounterNum Int(11) Counter Number
  CounteType Int(11) Type of Counter default=12 [12=User, 171=Employee]
  CounterId Int(11) Counter ID
  CounteName nVarChar(155) Counter Name
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# ICD9 - Inventory Counting Draft - Individual Counter - Row Counted Qty
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  CounterNum Int(11) Counter Number
  TotalQty Num(19,6) Total Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# IGE1 - Goods Issue - Rows
Module: Inventory and Production | 287 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseLine, BaseType, BaseEntry
  VIS_ORDER: VisOrder, DocEntry
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: OpenQty, WhsCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 59=Goods Receipt]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 202=Production Order]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No.
  Dscription nVarChar(100) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Base Price for Gross Profit
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  SubCatNum nVarChar(50) Customer/Vendor Cat. No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (FC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick List ID Number
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) Withholding Tax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Item, M=Resource]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Inventory Price
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight [Y=Yes, N=No]
  DescOW VarChar(1) Description Overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Details Overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No.
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item, 290=Resource]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others, =]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# IGE10 - Goods Issue - Row Structure
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocEntry
  SECONDARY U: OrderNum, AftLineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=60 ->ADP1

# IGE11 - Goods Issue - Drawn Dpm Detail
Module: Inventory and Production | 70 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
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
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
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

# IGE12 - Goods Issue - Tax Extension
Module: Inventory and Production | 81 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
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
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=60 ->ADP1
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
  CountryS nVarChar(3) Country ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country ->OCRY
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
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code

# IGE13 - Goods Issue Rows - Distributed Expenses
Module: Inventory and Production | 59 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum, LineNum, DocEntry
  LINE: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# IGE14 - Goods Issue - Assembly - Rows
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1

# IGE15 - Gds Issue - Drawn Dpm Applied
Module: Inventory and Production | 84 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# IGE16 - Goods Issue - SnB properties
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnBIndex, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OIGE
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=60
  LogInstanc Int(11) Log Instance

# IGE19 - Goods Issue - Bin Allocation Data
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BinAllocSe, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OIGE
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# IGE2 - Goods Issue - Freight - Rows
Module: Inventory and Production | 58 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum, LineNum, DocEntry
  LINE: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)

# IGE21 - Goods Issue - Document Reference Information
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RefType, LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=60
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order, 321=Internal Reconciliation]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de crédito de los documentos relacionados, 02=Nota de débito de los documentos relacionados, 03=Devolución de mercancía sobre facturas o traslados previos, 04=Sustitución de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicación de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, MX_09=Factura generada por pagos diferidos]

# IGE26 - Goods Issue - E-Way Bill Information
Module: Inventory and Production | 36 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line

# IGE3 - Goods Issue - Freight
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  DOCUMENT: BaseAbsEnt, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 202=Production Order]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)

# IGE4 - Goods Issue - Tax Amount per Document
Module: Inventory and Production | 55 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocEntry
  SCONDARY: staType, StaCode, StcCode, ExpnsCode, GroupNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]

# IGE5 - Goods Issue - Withholding Tax
Module: Inventory and Production | 148 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  SECONDERY U: Doc1LineNo, BaseAbsEnt, WTCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OIGE
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 202=Production Order]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)

# IGE6 - Goods Issue - Installments
Module: Inventory and Production | 64 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InstlmntID, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)

# IGE7 - Delivery Packages - Goods Issue
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# IGE8 - Items in Package - Goods Issue
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: NumPerMsr, UomEntry, ItemCode, PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# IGE9 - Goods Issue - Drawn Dpm
Module: Inventory and Production | 27 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=60 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# IGN1 - Goods Receipt - Rows
Module: Inventory and Production | 287 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseLine, BaseType, BaseEntry
  VIS_ORDER: VisOrder, DocEntry
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: OpenQty, WhsCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [67=Warehouses Transfer, 0=, -1=]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 202=Production Order, 60=Goods Issue]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(100) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Base Price for Gross Profit
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  SubCatNum nVarChar(50) Customer/Vendor Cat. No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (FC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Warehouse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick List ID Number
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) Withholding Tax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount
  LineVatS Num(19,6) Net Tax Amount
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Inventory Price
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight [Y=Yes, N=No]
  DescOW VarChar(1) Description Overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Details Overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No.
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item, 290=Resource]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others, =]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# IGN10 - Goods Receipt - Row Structure
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocEntry
  SECONDARY U: OrderNum, AftLineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=59 ->ADP1

# IGN11 - Goods Receipt - Drawn Dpm Det
Module: Inventory and Production | 70 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
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
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
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

# IGN12 - Goods Receipt - Tax Extension
Module: Inventory and Production | 81 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
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
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=59 ->ADP1
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
  CountryS nVarChar(3) Country ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country ->OCRY
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
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code

# IGN13 - Goods Receipt Rows - Distributed Expenses
Module: Inventory and Production | 59 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum, LineNum, DocEntry
  LINE: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# IGN14 - Goods Receipt - Assembly - Rows
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1

# IGN15 - Gds Rcpt - Drawn Dpm Applied
Module: Inventory and Production | 84 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# IGN16 - Goods Receipt - SnB properties
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnBIndex, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OIGN
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=59
  LogInstanc Int(11) Log Instance

# IGN19 - Goods Receipt - Bin Allocation Data
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BinAllocSe, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OIGN
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# IGN2 - Goods Receipt - Freight - Rows
Module: Inventory and Production | 58 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum, LineNum, DocEntry
  LINE: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)

# IGN21 - Goods Receipt - Document Reference Information
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RefType, LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=59
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order, 321=Internal Reconciliation]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de crédito de los documentos relacionados, 02=Nota de débito de los documentos relacionados, 03=Devolución de mercancía sobre facturas o traslados previos, 04=Sustitución de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicación de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, MX_09=Factura generada por pagos diferidos]

# IGN26 - Goods Receipt - E-Way Bill Information
Module: Inventory and Production | 36 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line

# IGN3 - Goods Receipt - Freight
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  DOCUMENT: BaseAbsEnt, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 202=Production Order]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)

# IGN4 - Goods Receipt - Tax Amount per Document
Module: Inventory and Production | 55 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocEntry
  SCONDARY: staType, StaCode, StcCode, ExpnsCode, GroupNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]

# IGN5 - Goods Receipt - Withholding Tax
Module: Inventory and Production | 148 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  SECONDERY U: Doc1LineNo, BaseAbsEnt, WTCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OIGN
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 202=Production Order]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)

# IGN6 - Goods Receipt- Installments
Module: Inventory and Production | 64 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InstlmntID, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)

# IGN7 - Goods Receipt - Delivery Packages
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# IGN8 - Goods Receipt - Items in Package
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: NumPerMsr, UomEntry, ItemCode, PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=59 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# IGN9 - Goods Receipt - Drawn Dpm
Module: Inventory and Production | 27 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGN
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=59 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# ILM1 - Srl & Batch Det of Inv Log Msg
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SysNumber, ItemCode, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number
  Quantity Num(19,6) Quantity
  MdAbsEntry Int(11) MD Abs Entry

# ILM2 - Inventory Account Substitute
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DebitCredi, AccountId, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  AccountId Int(6) Account ID default=-1
  AcctCode nVarChar(15) Account Code ->OACT
  DebitCredi VarChar(1) Debit or Credit default=U [U=Unknown, D=Debit, C=Credit]

# ILM3 - Non-Inventory and Resource Components Log Msg
Module: Inventory and Production | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  LineID Int(11) Line ID
  POLine Int(11) Line in Production Order
  ItemType Int(11) Item Type
  ItemCode nVarChar(50) Item No. ->OITM
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  Quantity Num(19,6) Quantity
  TotalLC Num(19,6) Inventory Total LC
  BaseAbsEnt Int(11) Abs. Entry of Base Doc. default=-1
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 60=Goods Issue]
  BaseLine Int(11) Base Line Number default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry
  StgDesc nVarChar(100) Stage Description

# IMT1 - Acct data in selected template
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AccountId, TemplateId
Fields (name type(len) description [values] ->parent table):
  TemplateId Int(6) Template ID default=-1 ->OIMT
  AccountId Int(6) Account ID default=-1
  DebitCredi VarChar(1) Debit or Credit default=U [U=Unknown, D=DEBIT, C=CREDIT, B=Both, T=Total]
  OrderCalc Int(6) Order Calc default=-1

# IMT11 - Calculated expression's constituent with sign for specifying account in specific template
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PoSt_ID, AccountId, TemplateId
Fields (name type(len) description [values] ->parent table):
  TemplateId Int(6) Template ID default=-1 ->IMT1
  AccountId Int(6) Account ID default=-1 ->IMT1
  Sign VarChar(1) Sing of the constituent default=A [A=Add, S=Sub]
  PoSt_ID Int(6) Id into Post Structure default=-1

# INC1 - Inventory Counting - Rows
Module: Inventory and Production | 41 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  ItemDesc nVarChar(100) Item Description
  Freeze VarChar(1) Item Freeze Status default=N [Y=Yes, N=No]
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  InWhsQty Num(19,6) In-Whse Qty on Count Date
  Counted VarChar(1) Counted default=N [Y=Yes, N=No]
  CountQty Num(19,6) Counted Quantity
  CountQtyT1 Num(19,6) Counter 1 - Counted Quantity
  CountQtyT2 Num(19,6) -
  Remark nVarChar(254) Remarks
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  Difference Num(19,6) Difference
  DiffPercen Num(19,6) Difference %
  CountDate Date(8) Count Date
  CountTime Int(11) Count Time
  TargetRef nVarChar(16) Target Document Reference
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 10000071=Inventory Posting]
  TargetEntr Int(11) Target Document Internal ID
  TargetLine Int(11) Target Document Row
  ProjCode nVarChar(20) Project Code ->OPRJ
  OcrCode nVarChar(8) Distribution Rule Code ->OOCR
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  BinEntry Int(11) Bin Location Entry ->OBIN
  VisOrder Int(11) Visual Order
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  PrefVendor nVarChar(15) Preferred Vendor ->OCRD
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Entry ->OUGP
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
  CountDiff Num(19,6) Counters' Diff.
  CountDiffP Num(19,6) Counters' Diff. (%)
  UomCode nVarChar(20) UoM Code for DI ->OUOM
  UomQty Num(19,6) UoM Counted Qty for DI

# INC10 - Inventory Counting - Individual Counters - Row UoM
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  CounterNum Int(11) Counter Number
  UomQty Num(19,6) UoM Counted Qty
  InvtQty Num(19,6) Counted Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# INC11 - Inventory Counting - Individual Counter - Row SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  CounterNum Int(11) Counter Number

# INC2 - Inventory Counting - UoM
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
  BUSINESS U: UomCode, BarCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  BarCode nVarChar(254) Bar Code
  UomCode nVarChar(20) UoM Code ->OUOM
  UomQty Num(19,6) UoM Counted Qty
  CountQty Num(19,6) Counted Qty of Inventory UoM
  Tk1UomQty Num(19,6) Counter 1 UoM Counted Qty
  Tk2UomQty Num(19,6) -
  Tk1CntQty Num(19,6) Counter 1 Counted Qty of Inv.
  Tk2CntQty Num(19,6) -
  ItmsPerUnt Num(19,6) Items per Unit
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  TeamUomQty Num(19,6) Team UoM Counted Qty
  TeamCntQty Num(19,6) Team Counted Qty
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM

# INC3 - Inventory Count - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# INC4 - Inventory Counting - Team Counters
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, DocEntry
  BUSINESS U: CounterId, CounteType, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  CounterNum Int(11) Counter Number
  CounteType Int(11) Type of Counter default=12 [12=User, 171=Employee]
  CounterId Int(11) Counter ID
  CounteName nVarChar(155) Counter Name
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# INC5 - Inventory Counting - Team Counter - Row Counted Qty
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  CounterNum Int(11) Counter Number
  TotalQty Num(19,6) Total Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# INC6 - Inventory Counting - Team Counter - Row UoM
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  CounterNum Int(11) Counter Number
  UomQty Num(19,6) UoM Counted Qty
  InvtQty Num(19,6) Counted Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# INC7 - Inventory Counting - Team Counter - Row SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  CounterNum Int(11) Counter Number

# INC8 - Inventory Counting - Individual Counters
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, DocEntry
  BUSINESS U: CounterId, CounteType, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  CounterNum Int(11) Counter Number
  CounteType Int(11) Type of Counter default=12 [12=User, 171=Employee]
  CounterId Int(11) Counter ID
  CounteName nVarChar(155) Counter Name
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# INC9 - Inventory Counting - Individual Counters - Row Counted Qty
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  CounterNum Int(11) Counter Number
  TotalQty Num(19,6) Total Qty of Inventory UoM
  LogIns Int(11) Log Instance - History

# IOD1 - Inventory Opening Balance Draft - Rows
Module: Inventory and Production | 39 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocLineNum, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIOD
  DocLineNum Int(11) Row Number in Document
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  InvntryUom nVarChar(100) Inventory UoM
  OnHandBef Num(19,6) Quantity Stored in Warehouse
  Price Num(19,6) Price
  Quantity Num(19,6) Quantity - Delta
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  ObjType nVarChar(20) Object Type default=310000001
  Project nVarChar(20) Project Code ->OPRJ
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM [Y=Yes, N=No]
  InvUoMQty Num(19,6) Inventory UoM Qty
  BinEntry Int(11) Bin Location Entry ->OBIN
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  Remark nVarChar(254) Remarks
  Location Int(11) Location
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  LogInstanc Int(11) Log Instance - History
  BinNegQty VarChar(1) Allow Bin Negative Quantity default=N [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  ActPrice Num(19,6) Actual Price
  PostValueL Num(19,6) Posted Value LC
  PostValueS Num(19,6) Posted Value SC

# IOD2 - Inventory Opening Balance Draft - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OIOD
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# IPD1 - Inventory Posting Draft - Rows
Module: Inventory and Production | 50 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocLineNum, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIPD
  DocLineNum Int(11) Row Number in Document
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  InvntryUom nVarChar(100) Inventory UoM
  OnHandBef Num(19,6) Quantity Stored in Warehouse
  Price Num(19,6) Price
  Quantity Num(19,6) Quantity - Delta
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  ObjType nVarChar(20) Object Type default=10000071
  Project nVarChar(20) Project Code ->OPRJ
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  BinEntry Int(11) Bin Location Entry ->OBIN
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  CountDate Date(8) Count Date
  CountTime Int(11) Count Time
  DiffPercnt Num(19,6) Percentage Difference
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=1470000065 [-1=, 1470000065=Inventory Counting]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  CountQty Num(19,6) Counted Quantity
  Remark nVarChar(254) Remarks
  LogInstanc Int(11) Log Instance - History
  CpyCount Int(11) Copied Count default=0 [0=, 1=Inventory Taker One, 2=Two Takers - Taker 1, 3=Two Takers - Taker 2, 4=Two Takers - Items with Zero Difference]
  BinNegQty VarChar(1) Allow Bin Negative Quantity default=N [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  UgpEntry Int(11) UoM Group Entry ->OUGP
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
  UomCode nVarChar(20) UoM Code for DI
  ItmsPerUnt Num(19,6) Items per Unit for DI
  UomQty Num(19,6) UoM Counted Qty for DI
  ActPrice Num(19,6) Actual Price
  PostValueL Num(19,6) Posted Value LC
  PostValueS Num(19,6) Posted Value SC

# IPD2 - Inventory Posting Draft - UoM
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
  BUSINESS U: UomCode, BarCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OIPD
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  BarCode nVarChar(254) Bar Code
  UomCode nVarChar(20) UoM Code ->OUOM
  UomQty Num(19,6) UoM Counted Qty
  CountQty Num(19,6) Counted Qty - Inventory UoM
  Tk1UomQty Num(19,6) Counter 1 UoM Counted Qty
  Tk2UomQty Num(19,6) -
  Tk1CntQty Num(19,6) Counter 1 Counted Qty of Inv.
  Tk2CntQty Num(19,6) -
  ItmsPerUnt Num(19,6) Items per Unit
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  TeamUomQty Num(19,6) Team UoM Counted Qty
  TeamCntQty Num(19,6) Team Counted Qty
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM

# IPD3 - Inventory Posting Draft - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OIPD
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# IPF1 - Landed Costs - Rows
Module: Inventory and Production | 113 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  BASE: OrigLine, BaseEntry
  ITEM: ItemCode, BaseEntry
  CURRENCY: Currency
  BASE_LINE: OrigLine, BaseEntry, BaseType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Landed Costs Internal ID ->OIPF
  LineNum Int(11) Row Number
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Goods Receipt PO, 69=Landed Costs, 18=A/P Invoice]
  BaseEntry Int(11) Base Document Internal ID
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(100) Item Description
  Quantity Num(19,6) Quantity
  PriceFOB Num(19,6) Base Doc. Price
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  Custom Num(19,6) Projected Customs
  CustomFC Num(19,6) Projected Customs (FC)
  Cost Num(19,6) Expenditure
  CostFC Num(19,6) Freight (FC)
  PriceAtWH Num(19,6) Whse Price
  PricAtWHFC Num(19,6) Whse Price (FC)
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  Volume Num(19,6) Volume
  UnitCode Int(6) Volume UoM ->OLGT
  Weight1 Num(19,6) Weight 1
  UnitCode1 Int(6) Unit of Weight 1 ->OWGT
  Weight2 Num(19,6) Weight 2
  UnitCode2 Int(6) Unit of Weight 2 ->OWGT
  CardCode nVarChar(15) Vendor Code ->OCRD
  Reference nVarChar(16) Reference
  OrigLine Int(11) Base Line Number
  FactNoCust Num(19,6) Factor Without Customs
  FacWthCust Num(19,6) Factor with Customs
  PriceList Int(6) Price List No. ->OPLN
  CostOH VarChar(1) Cost Surcharge default=Y [Y=Yes, N=No]
  StockEval VarChar(1) Use for Inventory Valuation default=Y [Y=Yes, N=No]
  UseBaseUn VarChar(1) Inventory UoM [Y=Yes, N=No]
  BlockNum nVarChar(100) Block No.
  ImportLog nVarChar(20) Import Log
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  OrigRow Int(11) Original Row
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  OrigWhs nVarChar(8) Original Warehouse ->OWHS
  ReleaseNum Int(11) Release Number
  VarCosts Num(19,6) Variant Costs
  ConstCosts Num(19,6) Fixed Costs
  VarCostsFR Num(19,6) Variant Costs (FC)
  CnstCostFR Num(19,6) Fixed Costs (FC)
  UserCustom Num(19,6) User Expected Custom
  UsrCusomFC Num(19,6) User Expected Foreign Custom
  FobValue Num(19,6) Base Doc. Value Row Total (LC)
  FobValueFC Num(19,6) Base Doc. Value Row Total (FC)
  TtlExpndLC Num(19,6) Allocated Unit Costs Row Total
  TtlExpndFC Num(19,6) Allocated Unit Costs Row Total
  TtlCustLC Num(19,6) Allocated Unit Costs Row Total
  TtlCustFC Num(19,6) Allocated Unit Costs Row Total
  TtlCostLC Num(19,6) Row Ttl Cust + Alloc Costs LC
  TtlCostFC Num(19,6) Row Ttl Cust + Alloc Costs FC
  TtlVolume Num(19,6) Volume Row Total
  TtlWeight Num(19,6) Weight Row Total
  BaseRowNum Int(11) use IPF1_BASE_LINE_NUM instead
  TtlCustSC Num(19,6) Ttl Row Projected Customs (SC)
  TtlExpndSC Num(19,6) Allocated Costs Row Total (SC)
  OriBAbsEnt Int(11) Original Base Doc. Internal ID default=-1
  OriBLinNum Int(11) Original Base Doc. Row No. default=-1
  TargetDoc Int(11) Target Document Internal No.
  FobValCurr nVarChar(3) Base Doc. Value Currency
  FobnLaC Num(19,6) FOB and Included Costs (LC)
  FobnLaCFC Num(19,6) FOB and Included Costs (FC)
  NumPerMsr Num(19,6) UoM Value
  Project nVarChar(20) Project Code ->OPRJ
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  OriBDocTyp nVarChar(11) Original Base Document Type default=-1 [-1=, 18=A/P Invoice, 20=Goods Receipt PO]
  CustRate Num(19,6) Custom Group Rate
  LFixCost Num(19,6) Locked Fixed Cost
  LFixCostFC Num(19,6) Locked Fixed Cost (FC)
  LVarCost Num(19,6) Locked Variable Cost
  LVarCostFC Num(19,6) Locked Variable Cost (FC)
  CstmsRate Num(19,6) Customs Rate
  VatGroup nVarChar(8) VAT Code
  VatPrcnt Num(19,6) VAT Rate per Row
  VatSum Num(19,6) Total of VAT
  SnbType nVarChar(20) Batch or Serial Type default=-1 [-1=, 10000045=Serial, 10000044=Batch]
  SnbAbsEnt Int(11) SnB Abs. Entry default=-1
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Distinct Number
  ExciseSum Num(19,6) Sum of Excise
  ExcisSumFC Num(19,6) Sum of Excise - FC
  ExcInStk VarChar(1) Is Excise in Stock default=N [Y=Yes, N=No]
  CustomSum Num(19,6) Sum of Customs Cost
  CustSumFC Num(19,6) Sum of Customs Cost in FC
  CstmInStk VarChar(1) Is Customs in Stock default=Y [Y=Yes, N=No]
  CstmVatSum Num(19,6) Sum of Customs Cost VAT
  CstmVatFC Num(19,6) Sum of Customs Cost VAT in FC
  CstmVatStk VarChar(1) Is Customs VAT in Stock default=Y [Y=Yes, N=No]
  CCDEntry Int(11) CCD Abs. Entry
  CCDNumber nVarChar(20) Number of CCD
  ExcisSumSC Num(19,6) Sum of Excise - SC
  CustSumSC Num(19,6) Sum of Customs Cost in SC
  CstmVatSC Num(19,6) Sum of Customs Cost VAT in SC
  InvQty Num(19,6) Inventory Quantity
  CCDLineNum Int(11) CCD Row Number
  TtlVolCCM Num(19,6) Volume Row Total per CCM
  ExcImpQty Num(19,6) Excise Imported Quantity
  ExcFixAmnt Num(19,6) Excise Fixed Amount
  ExcRate Num(19,6) Excise Rate
  ExcAmntUoM Num(19,6) Excise Amount UoM
  ExcAmntAdV Num(19,6) Excise Amount Ad Valorem
  ExcImpQUoM Int(11) Excise Imported Quantity UoM [112=Liters, m3, 168=Tonne, metric ton (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcBasAmnt Num(19,6) Excise Base Amount
  LineNumV3 Int(11) Target VAT Row Number in IPF3 ->IPF3
  FobVal2 Num(19,6) Corrected Base Doc. Value Row Total (LC) default=0
  FobVal2FC Num(19,6) Corrected Base Doc. Value Row Total (FC) default=0

# IPF2 - Landed Costs - Costs
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CostType, AlcCode, DocEntry
  NUM: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Landed Costs Internal ID ->OIPF
  LineNum Int(11) Row Number
  AlcCode nVarChar(2) Cost Code ->OALC
  OhType VarChar(1) Load by [F=Cash Value Before Customs, C=Cash Value After Customs, Q=Quantity, W=Weight, V=Volume, A=Equal, L=Legal Cost]
  CostSum Num(19,6) Total Costs
  CostSumFC Num(19,6) Total Costs (FC)
  Factor Num(19,6) Factor
  CostType VarChar(1) Cost Type default=F [F=Fixed Costs, V=Variable Costs, L=Legal Costs]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  LaCAllcAcc nVarChar(15) Landed Costs Alloc. Account
  CostSumSC Num(19,6) Total Costs (SC)
  InCustCalc VarChar(1) Included in Customs Calc default=N [Y=Yes, N=No]
  OpenCost Num(19,6) Open Costs
  OpenCostFC Num(19,6) Open Costs (FC)
  OpenCostSC Num(19,6) Open Costs (SC)
  AgentCode nVarChar(15) Subst. Code
  AgentName nVarChar(100) Subst. Name
  CostCateg VarChar(1) Cost Category [V=Customs VAT, E=Excise Cost, D=Customs Duty]

# IPF3 - Landed Costs - Customs Summary
Module: Inventory and Production | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Landed Costs Internal ID ->OIPF
  LineNum Int(11) Row Number
  Dscription nVarChar(100) Summary Description
  LaCAllcAcc nVarChar(15) Landed Costs Alloc. Account
  CustSum Num(19,6) Customs Summary
  CustSumFC Num(19,6) Customs Summary FC
  CustSumSC Num(19,6) Customs Summary SC
  OpenSum Num(19,6) Open Customs Summary
  OpenSumFC Num(19,6) Open Customs Summary (FC)
  OpenSumSC Num(19,6) Open Customs Summary (SC)
  AccType Int(11) Type of Account of Summarized
  VatGroup nVarChar(8) VAT Code ->OVTG
  CstmVatStk VarChar(1) Is Customs VAT in Stock default=Y [Y=Yes, N=No]
  CCDEntry Int(11) CCD Abs. Entry
  LineNum2 Int(11) Row Number in IPF2 ->IPF2

# IQI1 - Inventory Opening Balance - Rows
Module: Inventory and Production | 39 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocLineNum, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  DocLineNum Int(11) Row Number in Document
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  InvntryUom nVarChar(100) Inventory UoM
  OnHandBef Num(19,6) Quantity Stored in Warehouse
  Price Num(19,6) Price
  Quantity Num(19,6) Opening Balance
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  ObjType nVarChar(20) Object Type default=310000001
  Project nVarChar(20) Project Code ->OPRJ
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM [Y=Yes, N=No]
  InvUoMQty Num(19,6) Inventory UoM Qty
  BinEntry Int(11) Bin Location Entry ->OBIN
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  Remark nVarChar(254) Remarks
  Location Int(11) Location
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  LogInstanc Int(11) Log Instance - History
  BinNegQty VarChar(1) Allow Bin Negative Quantity default=N [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  ActPrice Num(19,6) Actual Price
  PostValueL Num(19,6) Posted Value LC
  PostValueS Num(19,6) Posted Value SC

# IQI2 - Inventory Opening Balance - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# IQI3 - Inventory Opening Balance - Tracking Note Assignment
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(20) Item CCD Number
  CntrOrigin nVarChar(3) Country of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=310000001
  SubLineNum Int(11) BOM Line No.

# IQR1 - Inventory Posting - Rows
Module: Inventory and Production | 50 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocLineNum, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  DocLineNum Int(11) Row Number in Document
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  InvntryUom nVarChar(100) Inventory UoM
  OnHandBef Num(19,6) Quantity Stored in Warehouse
  Price Num(19,6) Price
  Quantity Num(19,6) Variance
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  ObjType nVarChar(20) Object Type default=10000071
  Project nVarChar(20) Project Code ->OPRJ
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  BinEntry Int(11) Bin Location Entry ->OBIN
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  CountDate Date(8) Count Date
  CountTime Int(11) Count Time
  DiffPercnt Num(19,6) Percentage Difference
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=1470000065 [-1=, 1470000065=Inventory Counting]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  CountQty Num(19,6) Counted Quantity
  Remark nVarChar(254) Remarks
  LogInstanc Int(11) Log Instance - History
  CpyCount Int(11) Copied Count default=0 [0=, 1=Inventory Taker One, 2=Two Takers - Taker 1, 3=Two Takers - Taker 2, 4=Two Takers - Items with Zero Difference]
  BinNegQty VarChar(1) Allow Bin Negative Quantity default=N [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  UgpEntry Int(11) UoM Group Entry ->OUGP
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
  UomCode nVarChar(20) UoM Code for DI ->OUOM
  ItmsPerUnt Num(19,6) Items per Unit for DI
  UomQty Num(19,6) UoM Counted Qty for DI
  ActPrice Num(19,6) Actual Price
  PostValueL Num(19,6) Posted Value LC
  PostValueS Num(19,6) Posted Value SC

# IQR2 - Inventory Posting - UoM
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
  BUSINESS U: UomCode, BarCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  BarCode nVarChar(254) Bar Code
  UomCode nVarChar(20) UoM Code ->OUOM
  UomQty Num(19,6) UoM Counted Qty
  CountQty Num(19,6) Counted Qty - Inventory UoM
  Tk1UomQty Num(19,6) Counter 1 UoM Counted Qty
  Tk2UomQty Num(19,6) -
  Tk1CntQty Num(19,6) Counter 1 Counted Qty of Inv.
  Tk2CntQty Num(19,6) -
  ItmsPerUnt Num(19,6) Items per Unit
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  TeamUomQty Num(19,6) Team UoM Counted Qty
  TeamCntQty Num(19,6) Team Counted Qty
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM

# IQR3 - Inventory Posting - SnB
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnbIndex, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  SnbIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) Object Abs.
  DrfWObjAbs Int(11) Draft Whse Obj. Abs. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance - History
  TakerType Int(11) Counter Type [0=One Counter, 1=Two Counters - Counter 1, 2=Two Counters - Counter 2]

# IQR4 - Inventory Posting - Tracking Note Assignment
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  LineNum Int(11) Row Number
  ChildNum Int(11) Assignment Line
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line
  Quantity Num(19,6) Quantity
  ItemCCDNum nVarChar(20) Item CCD Number
  CntrOrigin nVarChar(3) Country of Origin
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=10000071
  SubLineNum Int(11) BOM Line No.

# ITL1 - Srl & Batch Details in Transac
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SysNumber, ItemCode, LogEntry
  SNB_SYSID: SysNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Internal ID ->OITL
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number
  Quantity Num(19,6) Quantity
  AllocQty Num(19,6) Allocated Quantity
  MdAbsEntry Int(11) MD Abs Entry
  ReleaseQty Num(19,6) Release Quantity
  PickedQty Num(19,6) Picked Quantity
  OrderedQty Num(19,6) Ordered Quantity

# ITM1 - Items - Prices
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PriceList, ItemCode
  CURRENCY: Currency
  PRICE_LIST: PriceList
  MANUAL: Ovrwritten
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PriceList Int(6) Price List No. ->OPLN
  Price Num(19,6) List Price
  Currency nVarChar(3) Currency for List Price ->OCRN
  Ovrwritten VarChar(1) Manual Price Entry default=N [Y=Yes, N=No]
  Factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  Ovrwrite1 VarChar(1) Manual Price Entry (1) default=N [Y=Yes, N=No]
  Ovrwrite2 VarChar(1) Manual Price Entry (2) default=N [Y=Yes, N=No]
  BasePLNum Int(6) Base Price List No. ->OPLN
  UomEntry Int(11) UoM Entry ->OUOM
  PriceType VarChar(1) Price Type default=M [I=Inventory UoM Price, P=Pricing Unit Price, M=Both I and P, O=Other UoM Price]

# ITM10 - OITM Extension
Module: Inventory and Production | 20 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  ISCommCode Int(11) Commodity Code ->ODCI
  ISSubMasUn Int(11) Intrastat Additional Measure ->ODCI
  ISFactor Num(19,6) IS Factor Additional Measure
  ISOrCSTImp Int(11) IS Destination State for Impor. ->ODCI
  ISOrCSTExp Int(11) IS State of Origin for Export ->ODCI
  ISNaTraImp Int(11) IS Nature of Trans. Import ->ODCI
  ISNaTraExp Int(11) IS Nature of Trans. Export ->ODCI
  ISStProImp Int(11) IS Statistical Procedure Imp. ->ODCI
  ISStProExp Int(11) IS Statistical Procedure Exp. ->ODCI
  ISOriCntry nVarChar(3) Intrastat Country of Origin ->OCRY
  ISSerCode Int(11) Intrastat Service Code ->ODCI
  ISItemType VarChar(1) Intrastat Item Type default=I [I=Item, S=Service]
  ISSerSupMt nVarChar(12) IS Service Supply Method default=I [I=Immediate, R=To More Resumptions]
  ISSerPayMt nVarChar(12) IS Service Payment Method default=X [A=Accredited to Bank Account, B=Bank Transfer, X=Other]
  ISOrCRYImp nVarChar(3) IS Destination Country for Imp. ->OCRY
  ISOrCRYExp nVarChar(3) IS Origin Country for Export ->OCRY
  ISUseWeigh VarChar(1) Use Wt in Add. Measure Calc. default=Y [Y=Yes, N=No]
  ISRelevant VarChar(1) Intrastat Relevant default=N [Y=Yes, N=No]
  ISStatCode nVarChar(2) Statistical Code

# ITM11 - Asset Item Period Control
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: VisOrder, DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  VisOrder Int(11) Visual Order
  DprSt VarChar(1) Depreciation Status default=Y [Y=Yes, N=No]
  factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ActualUnit Int(11) Actual Units

# ITM12 - UoM in Item
Module: Inventory and Production | 23 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UomEntry, UomType, ItemCode
  UOM_ENTRY: UomEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  UomType VarChar(1) UoM Type default=P [P=Purchasing, S=Sales, I=Inventory]
  UomEntry Int(11) UoM Entry ->OUOM
  BcdEntDft Int(11) Default Bar Code Entry ->OBCD
  PkgCodeDft Int(11) Default Package Code ->OPKG
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Height 1 UoM
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Height 2 UoM
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Width 1 UoM
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Width 2 UoM
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Length 1 UoM
  Length2 Num(19,6) Length 2
  Len2Unit Int(6) Length 2 UoM
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Weight 1 UoM
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Weight 2 UoM

# ITM13 - Asset Attributes
Module: Inventory and Production | 67 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  AttriTxt1 nVarChar(100) Attribute 1
  AttriTxt2 nVarChar(100) Attribute 2
  AttriTxt3 nVarChar(100) Attribute 3
  AttriTxt4 nVarChar(100) Attribute 4
  AttriTxt5 nVarChar(100) Attribute 5
  AttriTxt6 nVarChar(100) Attribute 6
  AttriTxt7 nVarChar(100) Attribute 7
  AttriTxt8 nVarChar(100) Attribute 8
  AttriTxt9 nVarChar(100) Attribute 9
  AttriTxt10 nVarChar(100) Attribute 10
  AttriTxt11 nVarChar(100) Attribute 11
  AttriTxt12 nVarChar(100) Attribute 12
  AttriTxt13 nVarChar(100) Attribute 13
  AttriTxt14 nVarChar(100) Attribute 14
  AttriTxt15 nVarChar(100) Attribute 15
  AttriTxt16 nVarChar(100) Attribute 16
  AttriTxt17 nVarChar(100) Attribute 17
  AttriTxt18 nVarChar(100) Attribute 18
  AttriTxt19 nVarChar(100) Attribute 19
  AttriTxt20 nVarChar(100) Attribute 20
  AttriTxt21 nVarChar(100) Attribute 21
  AttriTxt22 nVarChar(100) Attribute 22
  AttriTxt23 nVarChar(100) Attribute 23
  AttriTxt24 nVarChar(100) Attribute 24
  AttriTxt25 nVarChar(100) Attribute 25
  AttriTxt26 nVarChar(100) Attribute 26
  AttriTxt27 nVarChar(100) Attribute 27
  AttriTxt28 nVarChar(100) Attribute 28
  AttriTxt29 nVarChar(100) Attribute 29
  AttriTxt30 nVarChar(100) Attribute 30
  AttriTxt31 nVarChar(100) Attribute 31
  AttriTxt32 nVarChar(100) Attribute 32
  AttriInt33 Int(11) Attribute 33
  AttriInt34 Int(11) Attribute 34
  AttriInt35 Int(11) Attribute 35
  AttriInt36 Int(11) Attribute 36
  AttriInt37 Int(11) Attribute 37
  AttriInt38 Int(11) Attribute 38
  AttriInt39 Int(11) Attribute 39
  AttriInt40 Int(11) Attribute 40
  AttriInt41 Int(11) Attribute 41
  AttriInt42 Int(11) Attribute 42
  AttriDt43 Date(8) Attribute 43
  AttriDt44 Date(8) Attribute 44
  AttriDt45 Date(8) Attribute 45
  AttriDt46 Date(8) Attribute 46
  AttriDt47 Date(8) Attribute 47
  AttriAm48 Num(19,6) Attribute 48
  AttriAm49 Num(19,6) Attribute 49
  AttriAm50 Num(19,6) Attribute 50
  AttriAm51 Num(19,6) Attribute 51
  AttriAm52 Num(19,6) Attribute 52
  AttriAm53 Num(19,6) Attribute 53
  AttriAm54 Num(19,6) Attribute 54
  AttriPr55 Num(19,6) Attribute 55
  AttriPr56 Num(19,6) Attribute 56
  AttriPr57 Num(19,6) Attribute 57
  AttriPr58 Num(19,6) Attribute 58
  AttriPr59 Num(19,6) Attribute 59
  AttriQTY60 Num(19,6) Attribute 60
  AttriQTY61 Num(19,6) Attribute 61
  AttriQTY62 Num(19,6) Attribute 62
  AttriQTY63 Num(19,6) Attribute 63
  AttriQTY64 Num(19,6) Attribute 64
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

# ITM2 - Items - Multiple Preferred Vendors
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: VendorCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  VendorCode nVarChar(15) Vendor Code ->OCRD
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

# ITM3 - Items - Localization Fields
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  IncNature nVarChar(10) Income Nature ->OBMI
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

# ITM4 - Package in Items
Module: Inventory and Production | 23 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PkgCode, UomEntry, UomType, ItemCode
  PKG_CODE: PkgCode
  UOM_ENTRY: UomEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  UomType VarChar(1) UoM Type default=P [P=Purchasing, S=Sales]
  UomEntry Int(11) UoM Entry ->OUOM
  PkgCode Int(11) Package Code ->OPKG
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Height 1 UoM
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Height 2 UoM
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Width 1 UoM
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Width 2 UoM
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Length 1 UoM
  Length2 Num(19,6) Length 2
  Len2Unit Int(6) Length 2 UoM
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Weight 1 UoM
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Weight 2 UoM
  QtyPerPack Num(19,6) Quantity per Packaging UoM

# ITM5 - Asset Item Projects
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  LineNum Int(11) Line Number
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Project nVarChar(20) Project ->OPRJ
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

# ITM6 - Asset Item Distribution Rules
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  LineNum Int(11) Line Number
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1

# ITM7 - Asset Item Depreciation Params
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  VisOrder Int(11) Visual Order
  DprStart Date(8) Depreciation Start Date
  DprEnd Date(8) Depreciation End Date
  UsefulLife Int(11) Useful Life
  RemainLife Num(19,6) Remaining Life
  DprType nVarChar(15) Depreciation Type ->ODTP
  DprTypeC nVarChar(15) Depr. Type Calculation ->ODTP
  UsefulLfeC Int(11) Useful Life Calculation
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  RemainDays Num(19,6) Remaining Life in Days
  TotalUnits Int(11) Total Units in Life
  RemainUnit Int(11) Remaining Units
  StanUnit Int(11) Standard Units

# ITM8 - Asset Item Balances
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  APC Num(19,6) APC
  APCHist Num(19,6) Historical APC
  Quantity Num(19,6) Asset Quantity
  OrDpAcc Num(19,6) Accumulated Ordinary Depr.
  UnDpAcc Num(19,6) Accumulated Unplanned Depr.
  SpDpKey1 nVarChar(2) Special Depreciation 01 ->ODPP
  SpDpAcc1 Num(19,6) Accumulated Special Depr. 01
  SpDpKey2 nVarChar(2) Special Depreciation 02 ->ODPP
  SpDpAcc2 Num(19,6) Accumulated Special Depr. 02
  SpDpKey3 nVarChar(2) Special Depreciation 03 ->ODPP
  SpDpAcc3 Num(19,6) Accumulated Special Depr. 03
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  SalvageVal Num(19,6) Salvage Value
  OrDpAcc1 Num(19,6) Ordinary Depr. Accumulation 01
  WriteUpAcc Num(19,6) Accumulated Write-Up
  IsMaSalVal VarChar(1) Manually Changed Salvage Value default=N [Y=Yes, N=No]
  AppreAcc Num(19,6) Accumulated Appreciation

# ITM9 - Item - UoM Prices
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UomEntry, PriceList, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PriceList Int(6) Price List No. ->OPLN
  UomEntry Int(11) UoM Entry ->OUOM
  Factor Num(19,6) Reduced By %
  Price Num(19,6) UoM Price
  Currency nVarChar(3) Currency for UoM Price ->OCRN
  AutoUpdate VarChar(1) Automatic Update default=Y [Y=Yes, N=No]
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  Factor1 Num(19,6) Reduced By %
  Factor2 Num(19,6) Reduced By %
  UpdateDate Date(8) Date of Update
  PriceType VarChar(1) Price Type default=O [I=Inventory UoM Price, P=Pricing Unit Price, M=Both I and P, O=Other UoM Price]

# ITT1 - Bill of Materials - Components
Module: Inventory and Production | 28 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, Father
  VISORDER U: VisOrder, Father
  FATHER: Father
  CHILD: Code
  PRICE_LIST: PriceList
Fields (name type(len) description [values] ->parent table):
  Father nVarChar(50) Parent Item ->OITT
  ChildNum Int(11) Component Element Number
  VisOrder Int(11) Visual Order
  Code nVarChar(50) Component Code
  Quantity Num(19,6) Quantity
  Warehouse nVarChar(8) Warehouse ->OWHS
  Price Num(19,6) Price
  Currency nVarChar(3) Currency ->OCRN
  PriceList Int(6) Price List default=0 ->OPLN
  OrigPrice Num(19,6) Original Price
  OrigCurr nVarChar(3) Original Currency
  IssueMthd VarChar(1) Issue Method [B=Backflush, M=Manual]
  Uom nVarChar(100) Inventory UoM
  Comment nVarChar(254) Comment
  LogInstanc Int(11) Log Instance
  Object nVarChar(20) Object default=66
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  PrncpInput VarChar(1) Principal Input default=N [Y=Yes, N=No]
  Project nVarChar(20) Project Code ->OPRJ
  Type Int(11) Component Type default=4 [4=Item, 290=Resource, -18=Text]
  WipActCode nVarChar(15) WIP Account Code ->OACT
  AddQuantit Num(19,6) Additional Quantity
  LineText Text(16) Row Text
  StageId Int(11) Stage ID

# ITT2 - BOM - Route Stages
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StageId, Father
  SEQUENCE U: SeqNum, Father
Fields (name type(len) description [values] ->parent table):
  Father nVarChar(50) Parent Item ->OITT
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  WaitDays Num(19,6) Waiting Days default=0

# ITW1 - Item Count Alert
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BinAbs, WhsCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  UserSign Int(6) User Signature ->OUSR
  CycleCode Int(6) Cycle Code ->OCYC
  Alert VarChar(1) Alert default=N [N=No, Y=Yes]
  NextDate Date(8) Next Counting Date
  Time Int(6) Alert Time
  DestUser Int(6) Destination User ->OUSR
  Alerted VarChar(1) Alerted default=N [Y=Yes, N=No]
  BinAbs Int(11) Bin Internal Number default=-1 ->OBIN

# IVL1 - IVL Layer Level
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LayerID, TransSeq
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No. ->OIVL
  LayerID Int(11) Layer ID
  CalcPrice Num(19,6) Calculated Price
  Balance Num(19,6) Stock Balance
  TransValue Num(19,6) Transaction Value
  LayerInQty Num(19,6) Receipt Quantity
  LayerOutQ Num(19,6) Issue Quantity
  RevalTotal Num(19,6) Inventory Revaluation Total

# IVL2 - Inventory Components for Production
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, MessageID
Fields (name type(len) description [values] ->parent table):
  Transseq Int(11) Transaction sequence
  MessageID Int(11) Message ID ->OILM
  LineID Int(11) Line ID
  POLine Int(11) Line in Production Order
  ItemType Int(11) Item Type
  ItemCode nVarChar(50) Item No. ->OITM
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  LayerTSeq Int(11) FIFO Layer Transaction Sequence default=-1
  LayerId Int(11) Layer ID default=-1
  Quantity Num(19,6) Quantity
  TotalLC Num(19,6) Inventory Total LC
  BaseAbsEnt Int(11) Abs. Entry of Base Doc. default=-1
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 60=Goods Issue]
  BaseLine Int(11) Base Line Number default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description

# IVLG - Inventory Revaluation Log File
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Unique Key
  UtilVer Int(11) Inventory Revaluation Utility
  B1Ver Int(11) B1 Version
  SrcDBVer Int(11) Source Database Version
  DestDBName nVarChar(128) Destination Database Name
  DestDBPath Text(16) Destination Database Path
  FromDoc Int(11) Document From
  FromSysDat Date(8) System Date From
  ToDoc Int(11) Last calculated document
  ToSysDate Date(8) To System Date
  CustDbUpd VarChar(1) Customer DB was updated default=N [Y=, N=]
  HistTblCrt VarChar(1) History tables created default=N [Y=, N=]
  SuccRecalc VarChar(1) Successful recalculation default=N [Y=, N=]
  Comment nVarChar(100) Recalculation Comment
  EnblFromTo VarChar(1) Enabling From-To Function default=N
  StrFld nVarChar(50) General String Field
  NumFld Int(11) Include Custom from OIPF
  LoadCust VarChar(1) Load Customs on Item Value default=Y [Y="Load Customs on Item Value" is selected, N="Load Customs on Item Value" is not selected]

# IVRU - Inventory Valuation Utility
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Successive No.
  SourceDB nVarChar(128) Source Database
  UtilityDB nVarChar(128) Utility DB
  IVLGEntry Int(11) IVLG Entry ->IVLG
  UpdDate Date(8) Update Date and Time
  TblHINM nVarChar(30) HINM Name
  TblHITM nVarChar(30) HITM Name
  TblHITW nVarChar(30) HITW Name
  TblFINM nVarChar(30) FINM Name
  TblFITM nVarChar(30) FITM Name
  TblFITW nVarChar(30) FITW Name
  TrSeqHINM Int(11) Last HINM Trans. Seq. No.
  TrSeqOINM Int(11) Last OINM Trans. Seq. No.
  TrIdUtil Int(11) Last OJDT Trans. No. Utility
  TrIdProd Int(11) Last OJDT Trans. No. Productiv
  Comment nVarChar(100) Comment
  StrFld nVarChar(50) General String Field
  NumFld Int(11) General Number Field

# IWB1 - Batch No. Quantities Backup
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNumber, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OIWB
  LineNumber Int(11) Line Number
  BtqAbs Int(11) Btq Abs. Entry ->OBTQ
  MdAbsEntry Int(11) MD Abs. Entry ->OBTN
  CountedQty Num(19,6) Counted Quantity

# IWB2 - Serial No. Quantities Backup
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNumber, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry ->OIWB
  LineNumber Int(11) Line Number
  SrqAbs Int(11) SRQ Abs. Entry ->OSRQ
  MdAbsEntry Int(11) MD Abs. Entry ->OSRN
  CountedQty Num(19,6) Counted Quantity

# LIVI - IVI Log File
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Internal Number
  Version Int(11) B1 Main Version
  PatchLevel nVarChar(50) B1 PL Version
  Comment nVarChar(100) Recalculation Comment
  LoadCustom VarChar(1) Load customs from OIPF default=Y [N=No, Y=Yes]
  LastMsgID Int(11) Last OILM Message ID
  UpdateDate Date(8) Date of Update
  InitMap VarChar(1) Initialize MAP Items
  InitStd VarChar(1) Initialize STD Items

# LIVI1 - IVI Log Array File
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CalcNum, LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Internal Number ->LIVI
  CalcNum Int(11) Partial Sequence Number
  CreateDate Date(8) Create Date
  UserToDate Date(8) User To Date
  ActuToDate Date(8) Actual To Date
  LastMsgID Int(11) Last Calculated OILM Message
  Result VarChar(1) Result of Calculation default=F [F=Failure, S=Success, A=Archived]
  ResultStr nVarChar(254) Result String of Calculation
  UserSign Int(6) User Signature ->OUSR
  IgnFail VarChar(1) Ignore Previous Failure default=N [Y=Yes, N=No]
  ReorderFrm Date(8) Reorder 8.8 Messages: From Date
  ReorderTo Date(8) Reorder 8.8 Messages: To Date
  StopDate Date(8) Stop Date
  StopTime Int(6) Stop Time

# MRV1 - Inventory Revaluation Information Array
Module: Inventory and Production | 23 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  ITEM_WHS: WhsCode, ItemCode
  ITEM: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OMRV
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  Dscription nVarChar(100) Item/Service Description
  Quantity Num(19,6) Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  RIncmAcct nVarChar(15) Inv. Reval. Increment Account
  RDcrmAcct nVarChar(15) Inv. Reval. Decrement Account
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RActPrice Num(19,6) Inv. Reval. Actual Price
  ROnHand Num(19,6) In Stock at Time of Revaluation
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=162
  EvalSystem VarChar(1) Cost Accounting Method [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch] ->OITM
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  UnitMsr nVarChar(100) Unit of Measure
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# MRV2 - Inventory Revaluation FIFO Rows
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, BaseLine, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->MRV1
  BaseLine Int(11) Base Row Number
  LineNum Int(11) Row Number
  Quantity Num(19,6) Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RActPrice Num(19,6) Inventory Reval. Current Cost
  INMTransNm Int(11) INM Transaction Number
  INMInst Int(11) INM Instance
  INMTransTy Int(11) INM Transaction Type default=-1
  INMCreatBy Int(11) INM Document Key Created
  INMBaseRef nVarChar(11) INM Base Reference
  INMDocDate Date(8) INM Posting Date
  INMOpenQty Num(19,6) INM Open Quantity
  ObjType nVarChar(20) Object Type default=162
  LogInstanc Int(11) Log Instance default=0
  IVLTransSe Int(11) IVL Transaction Sequence No. default=-1
  IVLLayerID Int(11) IVL Layer ID default=-1
  INMLineNum Int(11) INM Row Number in Document
  INMSubLine Int(11) INM Subrow Number default=-1

# OAIM - Archive Inventory Message
Module: Inventory and Production | 49 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID
  DocEntry Int(11) Document Number
  TransType Int(11) Transaction Type default=-1
  DocLineNum Int(11) Document Row Number
  Quantity Num(19,6) Quantity in Document
  EffectQty Num(19,6) Effective Inventory Quantity
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TotalLC Num(19,6) Inventory Total LC
  TotalFC Num(19,6) Inventory Total FC
  BaseAbsEnt Int(11) Internal No. of Base Doc
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 13=A/R Invoice, 15=Delivery, 16=Returns, 17=Sales Order, 18=A/P Invoice, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase Order, 23=Sales Quotation, 59=Goods Receipt, 67=Inventory Transfer, 69=Landed Costs, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment]
  Currency nVarChar(3) Document Currency ->OCRN
  AccumType Int(11) Accumulator Type default=0 [0=ACCUM_EMPTY, 1=ACCUM_ON_HAND, 2=ACCUM_COMMITTED, 3=ACCUM_ON_ORDER, 4=ACCUM_CONSIGNATION, 5=ACCUM_COUNTED]
  ActionType Int(11) Action Type default=5 [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]
  ExpensesLC Num(19,6) Expenses (LC)
  ExpensesFC Num(19,6) Expenses (FC)
  ItemCode nVarChar(50) Item Code ->OITM
  DocDate Date(8) Document Date
  DocRate Num(19,6) Document Rate
  JrnlMemo nVarChar(50) Journal Remarks
  BaseLine Int(11) Base Row Number default=-1
  CreateTime Int(6) Generation Time
  CreateDate Date(8) Creation Date
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  DocPrice Num(19,6) Document Price
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=BOM Component Item]
  ApplObj Int(11) Applied Object default=-1
  AppObjAbs Int(11) Applied Object Internal ID default=-1
  AppObjType VarChar(1) Applied Object Type
  AppObjLine Int(11) Applied Object Row default=-1
  TransSeqRf Int(11) Transaction Sequence Ref default=-1
  LayerIDRef Int(11) Layer ID Reference default=-1
  VersionNum nVarChar(11) Version Number
  PriceRate Num(19,6) Price Rate
  PriceCurr nVarChar(3) Price Currency ->OCRN
  Price Num(19,6) Price
  CIShbQty Num(19,6) Corr. Inv. Doc. Should Be Qty
  SubLineNum Int(11) Subrow Number default=-1
  PrjCode nVarChar(20) Project Code ->OPRJ
  UseDocPric VarChar(1) Use Document Price default=N [Y=Yes, N=No]
  Location Int(11) Location ->OLCT
  BSubLineNo Int(11) Base Subrow Number default=-1
  AppSubLine Int(11) Applied Subrow Number default=-1
  DocAction Int(11) Document Action Type

# OALI - Alternative Items 2
Module: Inventory and Production | 4 columns | ObjType: 107
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AltItem, OrigItem
Fields (name type(len) description [values] ->parent table):
  OrigItem nVarChar(50) Original Item No. ->OITM
  AltItem nVarChar(50) Alternative Item No. ->OITM
  Match Num(19,6) Match Factor
  Remarks nVarChar(50) Item Remarks

# OARG - Customs Groups
Module: Inventory and Production | 16 columns | ObjType: 56
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CstGrpCode
  GROUP_NAME U: CstGrpName
Fields (name type(len) description [values] ->parent table):
  CstGrpCode Int(6) Code
  CstGrpName nVarChar(20) Name
  GroupNum nVarChar(20) Number
  Custom Num(19,6) Customs
  BuyTax Num(19,6) Purchase
  OtherTax Num(19,6) Other
  TotalTax Num(19,6) Total
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  cstAllcAcc nVarChar(15) Customs Allocation Account ->OACT
  cstExpAcc nVarChar(15) Customs Expense Account ->OACT
  PortAddr nVarChar(50) Local Clearance - Port Address
  PortState nVarChar(3) Port State
  ExciExpAcc nVarChar(15) Excise Expense Account ->OACT
  ExciAlcAcc nVarChar(15) Excise Allocation Account ->OACT

# OBAT - Bin Location Attribute
Module: Inventory and Production | 12 columns | ObjType: 10000204
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: AttrValue, FldAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldAbs Int(11) Bin Field Conf. Internal Number ->OBFC
  AttrValue nVarChar(20) Code
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N

# OBBQ - Item - Serial/Batch - Bin Accumulator
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: BinAbs, SnBMDAbs
  BIN_ABS: BinAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item Code ->OITM
  SnBMDAbs Int(11) Batch MD Internal Number ->OBTN
  BinAbs Int(11) Bin Internal Number ->OBIN
  OnHandQty Num(19,6) On-Hand Quantity
  WhsCode nVarChar(8) Warehouse Code ->OWHS

# OBCD - Bar Code Master Data
Module: Inventory and Production | 11 columns | ObjType: 1470000062
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BcdEntry
  ITEM U: BcdCode, UomEntry, ItemCode
  BCD_CODE: BcdCode
Fields (name type(len) description [values] ->parent table):
  BcdEntry Int(11) Bar Code Abs. Entry
  BcdCode nVarChar(254) Bar Code - Code
  BcdName nVarChar(100) Bar Code Name
  ItemCode nVarChar(50) Item No. ->OITM
  UomEntry Int(11) UoM Abs. Entry ->OUOM
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date

# OBFC - Bin Field Configuration
Module: Inventory and Production | 14 columns | ObjType: 10000203
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: FldNum, FldType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldType VarChar(1) Field Type [S=Warehouse Sublevel, A=Bin Location Attribute]
  FldNum Int(6) Field Number
  DispName nVarChar(20) Display Name
  Activated VarChar(1) Active [Y/N] default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  DftName nVarChar(20) Default Field Name

# OBIN - Bin Location
Module: Inventory and Production | 64 columns | ObjType: 10000206
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BIN_CODE U: BinCode
  WHS_CODE: SysBin, WhsCode
  BUSINESS_K: SL4Code, SL3Code, SL2Code, SL1Code, WhsCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BinCode nVarChar(228) Bin Location Code
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SysBin VarChar(1) System Bin default=N [Y=Yes, N=No]
  SL1Abs Int(11) Sublevel-1 Internal Number ->OBSL
  SL1Code nVarChar(50) Sublevel-1 Code
  SL2Abs Int(11) Sublevel-2 Internal Number ->OBSL
  SL2Code nVarChar(50) Sublevel-2 Code
  SL3Abs Int(11) Sublevel-3 Internal Number ->OBSL
  SL3Code nVarChar(50) Sublevel-3 Code
  SL4Abs Int(11) Sublevel-4 Internal Number ->OBSL
  SL4Code nVarChar(50) Sublevel-4 Code
  Attr1Abs Int(11) Attribute-1 Internal Number ->OBAT
  Attr1Val nVarChar(20) Attribute-1 Value
  Attr2Abs Int(11) Attribute-2 Internal Number ->OBAT
  Attr2Val nVarChar(20) Attribute-2 Value
  Attr3Abs Int(11) Attribute-3 Internal Number ->OBAT
  Attr3Val nVarChar(20) Attribute-3 Value
  Attr4Abs Int(11) Attribute-4 Internal Number ->OBAT
  Attr4Val nVarChar(20) Attribute-4 Value
  Attr5Abs Int(11) Attribute-5 Internal Number ->OBAT
  Attr5Val nVarChar(20) Attribute-5 Value
  Attr6Abs Int(11) Attribute-6 Internal Number ->OBAT
  Attr6Val nVarChar(20) Attribute-6 Value
  Attr7Abs Int(11) Attribute-7 Internal Number ->OBAT
  Attr7Val nVarChar(20) Attribute-7 Value
  Attr8Abs Int(11) Attribute-8 Internal Number ->OBAT
  Attr8Val nVarChar(20) Attribute-8 Value
  Attr9Abs Int(11) Attribute-9 Internal Number ->OBAT
  Attr9Val nVarChar(20) Attribute-9 Value
  Attr10Abs Int(11) Attribute-10 Internal Number ->OBAT
  Attr10Val nVarChar(20) Attribute-10 Value
  Disabled VarChar(1) Inactive default=N [Y=Yes, N=No]
  Descr nVarChar(50) Description
  BarCode nVarChar(100) Bar Code
  AltSortCod nVarChar(50) Alternative Sort Code
  ItmRtrictT Int(6) Item Restriction Type default=0 [0=None, 1=Specific Item, 2=Single Item Only, 3=Specific Item Group, 4=Single Item Group Only]
  SpcItmCode nVarChar(50) Specific Item Code ->OITM
  SpcItmGrpC Int(6) Specific Item Group Code ->OITB
  SngBatch VarChar(1) Batch Restriction default=N [N=None, Y=Single Batch]
  RtrictType Int(6) Restricted Transactions Type default=0 [0=None, 1=All Transactions, 2=Inbound Transactions, 3=Outbound Transactions, 4=All Except Inventory Transfer and Counting Transactions]
  RtrictResn nVarChar(254) Reason for Restriction
  RtrictDate Date(8) Last Updated On
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N
  MinLevel Num(19,6) Minimum Qty
  MaxLevel Num(19,6) Maximum Qty
  ReceiveBin VarChar(1) Receiving Bin Location default=N [Y=Yes, N=No]
  NoAutoAllc VarChar(1) Excl. fr. Auto Alloc. on Issue default=N [Y=Yes, N=No]
  MaxWeight1 Num(19,6) Maximum Weight 1
  Wght1Unit Int(6) Unit of Maximum Weight 1 ->OWGT
  MaxWeight2 Num(19,6) Maximum Weight 2
  Wght2Unit Int(6) Unit of Maximum Weight 2 ->OWGT
  UoMRtrict Int(6) UoM Restriction default=0 [0=None, 1=Specific UoM, 2=Single UoM Only, 3=Specific UoM Group, 4=Single UoM Group Only]
  SpcUoMCode Int(11) Specified UoM Code ->OUOM
  SpcUGPCode Int(11) Specified UoM Group Code ->OUGP
  SngUoMCode Int(11) Single UoM Code ->OUOM

# OBSL - Warehouse Sublevel
Module: Inventory and Production | 13 columns | ObjType: 10000205
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: SLCode, FldAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldAbs Int(11) Bin Field Conf. Internal Number ->OBFC
  SLCode nVarChar(50) Code
  Descr nVarChar(50) Description
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N

# OBTL - Bin Transaction Log
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  MESSAGE_ID: MessageID
  BIN_ABS: BinAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  MessageID Int(11) ILM Message ID ->OILM
  BinAbs Int(11) Bin Internal Number ->OBIN
  SnBMDAbs Int(11) SnB Master Data Internal Number default=-1
  Quantity Num(19,6) Quantity
  ITLEntry Int(11) ITL Log Internal ID default=-1 ->OITL

# OBTN - Batch Numbers Master Data
Module: Inventory and Production | 32 columns | ObjType: 10000044
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: SysNumber, ItemCode
  DIST_KEY: DistNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Batch Number
  MnfSerial nVarChar(36) Batch Attribute 1
  LotNumber nVarChar(36) Batch Attribute 2
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Warranty Start Date
  GrntExp Date(8) Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Location
  Status VarChar(1) Status default=0 [0=Released, 1=Not Accessible, 2=Locked]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  ObjType nVarChar(20) object type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

# OBTQ - Batch No. Quantities
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: WhsCode, SysNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number ->OBTN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  CommitQty Num(19,6) Committed Quantity
  CountQty Num(19,6) Counted Quantity
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry ->OBTN
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  CCDQuant Num(19,6) CCD Quantity

# OBTW - Batch Attributes in Location
Module: Inventory and Production | 14 columns | ObjType: 310000008
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: WhsCode, SysNumber, ItemCode
  ABS_WHS U: WhsCode, MdAbsEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number ->OBTN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Location nVarChar(100) Location
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry ->OBTN
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OCCS - Cycle Count Determination
Module: Inventory and Production | 3 columns | ObjType: 1470000092
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WhsCode
Fields (name type(len) description [values] ->parent table):
  WhsCode nVarChar(8) Warehouse Code
  CycleType VarChar(1) Cycle Type default=G [G=Item Group, S=Sublevel]
  CycleBy Int(6) Cycle By default=0 [0=Item Group, 1=Warehouse Sublevel 1, 2=Warehouse Sublevel 2, 3=Warehouse Sublevel 3, 4=Warehouse Sublevel 4]

# OCHP - India Chapter ID
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CHAPTERID U: ChapterID
  CHAPTER: SubHeading, Heading, Chapter
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Chapter nVarChar(20) Chapter
  Heading nVarChar(20) Tariff Heading
  SubHeading nVarChar(20) Tariff Subheading
  Dscription nVarChar(120) Description for Tariff Heading
  ChapterID nVarChar(64) Chapter ID

# OCYC - Cycle
Module: Inventory and Production | 24 columns | ObjType: 146
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Cycle Code
  Name nVarChar(20) Cycle Name
  Frequency VarChar(1) Frequency [0=Daily, 1=Weekly, 2=Every Four Weeks, 3=Monthly, 4=Quarterly, 5=Semiannually, 6=Annually, 7=None, 8=Every "X" Days:]
  Day Int(11) Day
  Hour Int(11) Hour
  UserSign Int(6) User Signature ->OUSR
  NextDate Date(8) Next Counting Date
  Type VarChar(1) Cycle Type default=C [C=Cycle, M=MRP]
  SubOption VarChar(1) Suboption default=1 [1=Option 1, 2=Option 2]
  Interval Int(11) Interval default=1
  EndType VarChar(1) Recurrence End Type default=N [N=No End Date, C=By Counter, D=By Date]
  MaxOccur Int(11) Max. Occurrences
  SeEndDat Date(8) Series End Date
  Sunday VarChar(1) Sunday default=N [N=No, Y=Yes]
  Monday VarChar(1) Monday default=N [N=No, Y=Yes]
  Tuesday VarChar(1) Tuesday default=N [N=No, Y=Yes]
  Wednesday VarChar(1) Wednesday default=N [N=No, Y=Yes]
  Thursday VarChar(1) Thursday default=N [N=No, Y=Yes]
  Friday VarChar(1) Friday default=N [N=No, Y=Yes]
  Saturday VarChar(1) Saturday default=N [N=No, Y=Yes]
  DayInMonth Int(11) Repeat Day in Month
  Week Int(11) Repeat Week in Month [1=First, 2=Second, 3=Third, 4=Fourth, 5=Last]
  DayOfWeek Int(11) Repeat Day of Week [8=Day, 9=Weekday, 0=Weekend Day, 1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday]
  Month Int(11) Repeat Month

# ODBN - Bat. Nos - Draft - Master Data
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  DIST_KEY: DistNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System No.
  DistNumber nVarChar(36) Distinct Number
  MnfSerial nVarChar(36) Manufacturer Serial No.
  LotNumber nVarChar(36) Lot Number
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Warranty Start Date
  GrntExp Date(8) Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Loc.
  Status VarChar(1) Status default=0 [0=Released, 1=Not Accessible, 2=Locked]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  ObjType nVarChar(20) object type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

# ODBW - Batch Draft Attribs in Locat.
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System No. ->OBTN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Location nVarChar(100) Loc.
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# ODNF - DNF Code
Module: Inventory and Production | 8 columns | ObjType: 140000041
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  NCM_DNF U: DNFCode, NCMEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  NCMEntry Int(11) NCM Code ->ONCM
  DNFCode nVarChar(5) DNF Code
  DNFUoM nVarChar(10) DNF UoM
  DNFFactor Num(19,6) DNF Factor
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# ODSN - SNs - Draft - Master Data
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  DIST_KEY: DistNumber, ItemCode
  LOT_KEY: LotNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System No.
  DistNumber nVarChar(36) Distinct Number
  MnfSerial nVarChar(36) Manufacturer Serial No.
  LotNumber nVarChar(36) Lot Number
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Warranty Start Date
  GrntExp Date(8) Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Loc.
  Status VarChar(1) Status [0=Available, 1=Unavailable]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  ObjType nVarChar(20) object type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

# ODSW - SN Draft Attribs in Location
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System No. ->OSRN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Location nVarChar(100) Loc.
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OEDG - Discount Groups
Module: Inventory and Production | 14 columns | ObjType: 1470000077
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE_TYPE U: Type, ObjCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Type VarChar(1) Type [A=All BPs, C=Customer Group, V=Vendor Group, S=Specific BP]
  ObjType nVarChar(20) Object Type default=-1 [-1=, 10=Card Payment Groups, 2=Cards]
  ObjCode nVarChar(15) Object Code
  DiscRel VarChar(1) Disc. Relations default=L [L=Lowest Discount, H=Highest Discount, A=Average, S=Total, M=Discount Multiples]
  ValidFor VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidForm Date(8) Active From
  ValidTo Date(8) Active To
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Form ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Update Date

# OENT - Shipping Types
Module: Inventory and Production | 40 columns | ObjType: 88
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM: DocNum
  BASE_DOC: BaseDocObj, BaseDocNum
  OBJECT: ObjType
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number ->OUSR
  BaseDocNum Int(11) Base Document Number ->OUSR
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  ObjType nVarChar(20) Object Type ->ADP1
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  FreZoneNum nVarChar(8) ID Number
  Shiper nVarChar(100) Sender
  Address nVarChar(254) Address
  FromCntry nVarChar(100) Country - Origin
  ToCntry nVarChar(100) Country - Destination
  FromPort nVarChar(100) Origin Port
  ToPort nVarChar(100) Destination Port
  AirPlane nVarChar(50) Ship/Aircraft
  AirPlanNum nVarChar(40) No. of Ships/Aircraft
  TotalFob Num(19,6) Total
  Taxes Num(19,6) Taxes
  Insurance Num(19,6) Insurance
  Others Num(19,6) Other
  TotalCif Num(19,6) Document Total
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  GroupNum Int(6) Payment Terms Code ->OCTG
  DocTime Int(6) Document Time
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TrnspCode Int(6) Delivery Code default=-1 ->OSHP
  PartSupply VarChar(1) Delivery of Goods default=Y [Y=Yes, N=No]
  ImportEnt Int(11) Landed Costs ->OIPF
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  NumForPrn nVarChar(100) Base Doc. No. for Printing ->OUSR
  PurPackMsr nVarChar(8) Packaging UoM Name
  Series Int(11) Series
  BaseDocObj Int(6) Base Document Object Type
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OGTY - GST Regn Type
Module: Inventory and Production | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  GSTType nVarChar(50) GST Regn. type
  descrip nVarChar(100) Description

# OIBQ - Item - Bin Accumulator
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: BinAbs, ItemCode
  BIN_ABS: BinAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item Code ->OITM
  BinAbs Int(11) Bin Internal Number ->OBIN
  OnHandQty Num(19,6) On-Hand Quantity
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Freezed VarChar(1) Item Frozen in Bin Location default=N [Y=Yes, N=No]
  FreezeDoc Int(11) Inventory Count Doc. Frozen By ->OINC

# OICD - Inventory Counting Draft
Module: Inventory and Production | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  CountDate Date(8) Date of Counting
  Time Int(11) Time of Counting
  CountType VarChar(1) Counting Type default=1 [1=Single Counter, 2=Multiple Counters]
  Taker1Type Int(11) Type of Counter default=12 [12=User, 171=Employee]
  Taker1Id Int(11) Counter ID
  Taker2Type Int(11) - default=12
  Taker2Id Int(11) -
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Ref2 nVarChar(11) Reference 2
  Remarks Text(16) Remarks
  LogIns Int(11) Log Instance - History
  UserSign Int(6) User Creating - History ->OUSR
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  CreateDate Date(8) Create Date - History
  ObjType nVarChar(20) Object Type default=1470000065
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Approved, A=Generated by Authorizer, C=Canceled]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OICD
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  TeamCount Int(11) Count of Team Counters default=0
  IndvCount Int(11) Count of Individual Counters default=0
  DiffQty Num(19,6) Total Difference
  DiffPercen Num(19,6) Total Difference (%)
  UpdateTS Int(11) Update Full Time
  CreateTime Int(6) Generation Time
  PIndicator nVarChar(10) Period Indicator
  FinncPriod Int(11) Posting Period
  PostDate Date(8) Posting Date
  VersionNum nVarChar(11) Version Number
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]

# OIGE - Goods Issue
Module: Inventory and Production | 424 columns | ObjType: 60
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  AT_CARD: CardCode, NumAtCard
  CUSTOMER: CardCode
  NUM U: PIndicator, DocSubType, Segment, Instance, DocNum
  DOC_STATUS: CANCELED, DocStatus
  FTHR_CARD: FatherType, FatherCard
  SERIES: Series
  OWNER_CODE: OwnerCode
  DATE_PIND: PIndicator, DocDate
  ESERIES: EDocNum, ESeries
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Numerator
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No]
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original, A=Amended]
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Closed]
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=60 [60=Goods Issue] ->ADP1
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) Expense Account ->OCRD
  CardName nVarChar(100) Customer/Vendor Name
  Address nVarChar(254) Bill to
  NumAtCard nVarChar(100) Customer/Vendor Ref. No.
  VatPercent Num(19,6) Tax Rate
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  DiscPrcnt Num(19,6) Discount % for Document
  DiscSum Num(19,6) Total Discount
  DiscSumFC Num(19,6) Total Discount in FC
  DocCur nVarChar(3) Document Currency ->OCRN
  DocRate Num(19,6) Document Rate
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total in FC
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  GrosProfit Num(19,6) Gross Profit
  GrosProfFC Num(19,6) Gross Profit in FC
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  ReceiptNum Int(11) Receipt Number
  GroupNum Int(6) Price List ->OCTG
  DocTime Int(6) Generation Time
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TrnspCode Int(6) Delivery Method default=-1 ->OSHP
  PartSupply VarChar(1) Partial Delivery default=Y [Y=Yes, N=No]
  Confirmed VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  GrossBase Int(6) Price List for Gross Profit default=0
  ImportEnt Int(11) Landed Costs Internal ID
  CreateTran VarChar(1) Create Journal Entry default=N [Y=Yes, N=No]
  SummryType VarChar(1) Summary Method default=N [N=No Summary, I=By Items, D=By Documents]
  UpdInvnt VarChar(1) Warehouse Update default=N [N=No, O=Orders from Vendors, C=Customer Orders, G=Consignment, I=Stock]
  UpdCardBal VarChar(1) Update Balances default=N [N=No, O=Orders, D=Delivery Notes, B=Bookkeeping]
  Instance Int(6) Instance default=0
  Flags Int(11) Flags default=0
  InvntDirec VarChar(1) Warehouse Direction default=X [X=Release, E=Receipt]
  CntctCode Int(11) Contact Person ->OCPR
  ShowSCN VarChar(1) Display BP Catalog Number default=N [Y=Yes, N=No]
  FatherCard nVarChar(15) BP Consolidation
  SysRate Num(19,6) System Price
  CurSource VarChar(1) Base Currency default=C [L=Local Currency, S=System Currency, C=BP Currency]
  VatSumSy Num(19,6) Tax Amount (SC)
  DiscSumSy Num(19,6) Total Discount in SC
  DocTotalSy Num(19,6) Document Total in SC
  PaidSys Num(19,6) Paid in SC
  FatherType VarChar(1) Parent Summary Type default=P [P=Payment Consolidation, D=Delivery Consolidation]
  GrosProfSy Num(19,6) Gross Profit in SC
  UpdateDate Date(8) Date of Update
  IsICT VarChar(1) A/R Invoice + Payment default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight Num(19,6) Weight
  WeightUnit Int(6) Weight UoM
  Series Int(11) Series ->NNM1
  TaxDate Date(8) Document Date
  Filler nVarChar(8) Filter ->OWHS
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  StampNum nVarChar(16) Stamp No.
  isCrin VarChar(1) Corrected Invoice default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  UserSign Int(6) User Signature ->OUSR
  selfInv VarChar(1) Autom. Invoice default=N [N=No, Y=Yes]
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid in FC
  VatPaidSys Num(19,6) Tax Paid in SC
  UserSign2 Int(6) Updating User ->OUSR
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  draftKey Int(11) Document Draft Internal ID default=-1 ->ODRF
  TotalExpns Num(19,6) Total Expenses
  TotalExpFC Num(19,6) Total Expenses (FC)
  TotalExpSC Num(19,6) Total Expenses (SC)
  DunnLevel Int(11) Dunning Level
  Address2 nVarChar(254) Ship-To Address
  LogInstanc Int(11) Log Instance default=0
  Exported VarChar(1) Exported default=N [Y=Yes, N=No]
  StationID Int(11) Workstation ID ->CSTN
  Indicator nVarChar(2) Indicator ->OIDC
  NetProc VarChar(1) Net Procedure default=N [Y=Yes, N=No]
  AqcsTax Num(19,6) Acquisition Tax
  AqcsTaxFC Num(19,6) Acquisition Tax (FC)
  AqcsTaxSC Num(19,6) Acquisition Tax (SC)
  CashDiscPr Num(19,6) Cash Discount Percentage
  CashDiscnt Num(19,6) Cash Discount
  CashDiscFC Num(19,6) Cash Discount (FC)
  CashDiscSC Num(19,6) Cash Discount (SC)
  ShipToCode nVarChar(50) Ship-to Code
  LicTradNum nVarChar(32) Licensed Dealer No.
  PaymentRef nVarChar(27) Payment Reference No.
  WTSum Num(19,6) Withholding Tax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  RoundDif Num(19,6) Rounding Diff. Amount
  RoundDifFC Num(19,6) Rounding Diff. Amount (FC)
  RoundDifSy Num(19,6) Rounding Diff. Amount (SC)
  CheckDigit VarChar(1) Control Digit
  Form1099 Int(11) 1099 Form ->OTNN
  Box1099 nVarChar(20) 1099 Box
  submitted VarChar(1) Submitted default=N [Y=Yes, N=No]
  PoPrss VarChar(1) PO Process default=N [Y=Yes, N=No]
  Rounding VarChar(1) Rounding default=N [Y=Yes, N=No]
  RevisionPo VarChar(1) Split PO default=N [Y=Yes, N=No]
  Segment Int(6) Segment default=0
  ReqDate Date(8) Required Date
  CancelDate Date(8) Cancelation Date
  PickStatus VarChar(1) Pick Status default=N [Y=Yes, N=No]
  Pick VarChar(1) Pick default=N [Y=Yes, N=No]
  BlockDunn VarChar(1) Block Dunning default=N [Y=Yes, N=No]
  PeyMethod nVarChar(15) Payment Method ->OPYM
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  MaxDscn VarChar(1) Maximum Discount default=N [Y=Yes, N=No]
  Reserve VarChar(1) Reserve default=N [Y=Yes, N=No]
  Max1099 Num(19,6) Max. 1099 Amount
  CntrlBnk nVarChar(15) Central Bank Indicator ->OCBI
  PickRmrk nVarChar(254) Pick Remarks
  ISRCodLine nVarChar(53) ISR Coding Line
  ExpAppl Num(19,6) Exp applied
  ExpApplFC Num(19,6) Exp applied FC
  ExpApplSC Num(19,6) Exp applied DC
  Project nVarChar(20) Project Code ->OPRJ
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  LetterNum nVarChar(20) Tax Exemption Letter No.
  FromDate Date(8) Exemption Validity Date From
  ToDate Date(8) Exemption Validity Date To
  WTApplied Num(19,6) Applied Withholding Tax
  WTAppliedF Num(19,6) Applied WTax (FC)
  BoeReserev VarChar(1) Bill of Exchange Reserved default=N [Y=Yes, N=No]
  AgentCode nVarChar(32) Agent Code ->OAGP
  WTAppliedS Num(19,6) Applied WTax (SC)
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  Installmnt Int(6) No. of Installments default=1
  VATFirst VarChar(1) Apply Tax on 1st Installment [Y=Yes, N=No]
  NnSbAmnt Num(19,6) WTax Non-Subject Amount
  NnSbAmntSC Num(19,6) WTax Non-Subject Amount (SC)
  NbSbAmntFC Num(19,6) WTax Non-Subject Amount (FC)
  ExepAmnt Num(19,6) Withholding Tax Exempt Amount
  ExepAmntSC Num(19,6) WTax Exempt Amount (FC)
  ExepAmntFC Num(19,6) WTax Exempt Amount (FC)
  VatDate Date(8) VAT Date
  CorrExt nVarChar(25) External Corrected Document No.
  CorrInv Int(11) Internal Corrected Document No.
  NCorrInv Int(11) Next Correcting Document
  CEECFlag VarChar(1) Block Creation Target Corr Inv default=N [N=No, Y=Yes]
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  CtlAccount nVarChar(15) Control Account ->OACT
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Registration Number
  TxInvRptNo nVarChar(10) Tax Invoice Rpt Number
  TxInvRptDt Date(8) Tax Invoice Rpt Date
  KVVATCode Text(16) VAT Code for Tax Invoice Rpt
  WTDetails nVarChar(100) Withholding Tax Details
  SumAbsId Int(11) Summary VAT Abstract ID default=-1
  SumRptDate Date(8) Summary VAT Report Date
  PIndicator nVarChar(10) Period Indicator ->OPID
  ManualNum nVarChar(20) Manual Number
  UseShpdGd VarChar(1) Use Shipped Goods Account default=N [N=No, Y=Yes]
  BaseVtAt Num(19,6) BPL ID Assigned to Invoice
  BaseVtAtSC Num(19,6) BPL Name
  BaseVtAtFC Num(19,6) Tax Reg. Number
  NnSbVAt Num(19,6) Tax Invoice Rpt Number
  NnSbVAtSC Num(19,6) Tax Invoice Rpt Date
  NbSbVAtFC Num(19,6) WTax Amount - VAT-exempt
  ExptVAt Num(19,6) WTax Exempted VAT Amount
  ExptVAtSC Num(19,6) WTax Exempted VAT Amount (SC)
  ExptVAtFC Num(19,6) Withholding Tax Details
  LYPmtAt Num(19,6) Last Year's Payments
  LYPmtAtSC Num(19,6) Last Years Payments (SC)
  LYPmtAtFC Num(19,6) Summary Tax Report Date
  ExpAnSum Num(19,6) Period Indicator
  ExpAnSys Num(19,6) Manual Number
  ExpAnFrgn Num(19,6) Use Shipped Goods Account
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=-- [--=Goods Issue]
  DpmStatus VarChar(1) Summary VAT Abstract ID default=O [O=Open, C=Closed]
  DpmAmnt Num(19,6) Down Payment Amount LC
  DpmAmntSC Num(19,6) Down Payment Amount SC
  DpmAmntFC Num(19,6) Down Payment Amount FC
  DpmDrawn VarChar(1) Drawn to Down Payment default=N [N=No, Y=Yes]
  DpmPrcnt Num(19,6) Down Payment Percent
  PaidSum Num(19,6) Total Paid Sum
  PaidSumFc Num(19,6) Total Paid Sum (FC)
  PaidSumSc Num(19,6) Total Paid Sum (SC)
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  DpmAppl Num(19,6) Down Payment Applied LC
  DpmApplFc Num(19,6) Down Payment Applied FC
  DpmApplSc Num(19,6) Down Payment Applied SC
  LPgFolioN Int(11) Folio No. for Last Page in Doc.
  Header Text(16) Header
  Footer Text(16) Footer
  Posted VarChar(1) Down Payment Was Posted default=Y [Y=Yes, N=No]
  OwnerCode Int(11) Document Owner ->OHEM
  BPChCode nVarChar(15) BP Channel Code ->OCRD
  BPChCntc Int(11) BP Channel Contact Person ->OCPR
  PayToCode nVarChar(50) Pay to
  IsPaytoBnk VarChar(1) Is Pay to Bank [N=No, Y=Yes]
  BnkCntry nVarChar(3) Pay to Bank Country ->OCRY
  BankCode nVarChar(30) Pay to Bank Code
  BnkAccount nVarChar(50) Pay to Bank Account No.
  BnkBranch nVarChar(50) Pay to Bank Branch
  isIns VarChar(1) Reserve Invoice default=N [Y=Yes, N=No]
  TrackNo nVarChar(30) Tracking Number
  VersionNum nVarChar(11) Version Number
  LangCode Int(11) Language Code ->OLNG
  BPNameOW VarChar(1) BP_NAME_OVERWRITTEN default=N [Y=Yes, N=No]
  BillToOW VarChar(1) BILL_TO_OVERWRITTEN default=N [Y=Yes, N=No]
  ShipToOW VarChar(1) SHIP_TO_OVERWRITTEN default=N [Y=Yes, N=No]
  RetInvoice VarChar(1) Credit Memo default=N [Y=Yes, N=No]
  ClsDate Date(8) Document Closing Date
  MInvNum Int(11) Monthly Invoice No.
  MInvDate Date(8) Monthly Invoice Date
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  Model nVarChar(6) Nota Fiscal Model default=0 ->ONFM
  TaxOnExp Num(19,6) Tax On Expenses Sum
  TaxOnExpFc Num(19,6) Tax On Expenses Sum (FC)
  TaxOnExpSc Num(19,6) Tax On Expenses Sum (SC)
  TaxOnExAp Num(19,6) Tax On Expenses Applied
  TaxOnExApF Num(19,6) Tax on Freight Applied (FC)
  TaxOnExApS Num(19,6) Tax on Freight Applied (SC)
  LastPmnTyp VarChar(1) Last Payment Type [R=Receipt, V=Vendor Payment]
  LndCstNum Int(11) Landed Cost Number
  UseCorrVat VarChar(1) Use Correction VAT Group default=N [N=No, Y=Yes]
  BlkCredMmo VarChar(1) Block Creating Credit Memo Tgt default=N [N=No, Y=Yes]
  OpenForLaC VarChar(1) Open For Landed Costs default=Y [Y=Open for Landed Costs, N=Closed for Landed Costs]
  Excised VarChar(1) Excised default=O [O=Open, C=Close]
  ExcRefDate Date(8) Excise Ref. Date
  ExcRmvTime nVarChar(8) Excise Removal Time
  SrvGpPrcnt Num(19,6) Gross Profit Prcnt of Service
  DepositNum Int(11) Deposit Number
  CertNum nVarChar(31) Certificate Number
  DutyStatus VarChar(1) Duty Status default=Y [Y=With Payment of Duty, N=Without Payment of Duty]
  AutoCrtFlw VarChar(1) Auto Create Follow-up Document default=N [N=No, Y=Yes]
  FlwRefDate Date(8) Follow-up Document Ref. Date
  FlwRefNum nVarChar(100) Follow-up Document Ref. Number
  VatJENum Int(11) VAT Journal Entry Number default=-1
  DpmVat Num(19,6) Down Payment Tax LC
  DpmVatFc Num(19,6) Down Payment Tax FC
  DpmVatSc Num(19,6) Down Payment Tax SC
  DpmAppVat Num(19,6) Down Payment Applied Tax LC
  DpmAppVatF Num(19,6) Down Payment Applied Tax FC
  DpmAppVatS Num(19,6) Down Payment Applied Tax SC
  InsurOp347 VarChar(1) 347 Insurance Operation default=N [N=No, Y=Yes]
  IgnRelDoc VarChar(1) Ignore Relevant Doc on Archive default=N [N=No, Y=Yes]
  BuildDesc nVarChar(50) Build Descriptor
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Residence Country, 5=Certificate of Fiscal Residence, 6=Other Document, 7=Not Registered]
  Checker Int(11) Checker ->OHEM
  Payee Int(11) Payee ->OHEM
  CopyNumber Int(11) Copy Number default=0
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  PQTGrpSer Int(11) Pur Quotation Group Series
  PQTGrpNum Int(11) Pur Quotation Group Number
  PQTGrpHW VarChar(1) Pur Quotation Group Manual default=N [Y=Yes, N=No]
  ReopOriDoc VarChar(1) Reopen Origin. Order by Return [Y=Yes, N=No]
  ReopManCls VarChar(1) Reop. Man. Closed/Canc. Orders [Y=Yes, N=No]
  DocManClsd VarChar(1) Document Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  ClosingOpt Int(6) Closing Option default=1
  SpecDate Date(8) Posting Date Specified by User
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  NTSApprov VarChar(1) NTS Approved default=N [N=No, Y=Yes]
  NTSWebSite Int(6) E-Tax Web Site ->OTWS
  NTSeTaxNo nVarChar(50) E-Tax Number
  NTSApprNo nVarChar(50) NTS Approval Number
  PayDuMonth VarChar(1) Start From [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Number of Additional Months
  ExtraDays Int(6) Number of Additional Days
  CdcOffset Int(6) Cash Discount Offset default=0
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  EDocGenTyp VarChar(1) Electr. Doc. Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  ESeries Int(6) Electronic Series ->NNM4
  EDocNum nVarChar(50) Electronic Document Number
  EDocExpFrm Int(11) Electronic Doc. Export Format
  OnlineQuo VarChar(1) Create Online Quotation default=N [Y=Yes, N=No]
  POSEqNum nVarChar(20) POS Equipment Number
  POSManufSN nVarChar(20) POS Manufacturer Serial Number
  POSCashN Int(11) POS Cashier Number
  EDocStatus VarChar(1) Electronic Document Status default=C [N=New, P=Pending, S=Sent, E=Error, C=OK]
  EDocCntnt Text(16) Electronic Document Content
  EDocProces VarChar(1) Electronic Document Process default=C [C=CFD, I=CFDI]
  EDocErrCod nVarChar(50) Electronic Document Error Code
  EDocErrMsg Text(16) Electronic Document Error Msg
  EDocCancel VarChar(1) Electronic Document - Canceled default=N [N=No, Y=Yes]
  EDocTest VarChar(1) Electronic Document - Testing default=N [N=No, Y=Yes]
  EDocPrefix nVarChar(10) Electronic Document - Prefix
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  DpmAsDscnt VarChar(1) Discount Document with Dpm default=N [N=No, Y=Yes]
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  SupplCode nVarChar(254) Supplementary Code
  GTSRlvnt VarChar(1) Relevant To GTS default=N [N=No, Y=Yes]
  BaseDisc Num(19,6) Base Discount LC
  BaseDiscSc Num(19,6) Base Discount SC
  BaseDiscFc Num(19,6) Base Discount FC
  BaseDiscPr Num(19,6) Base Discount Percentage
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  SrvTaxRule VarChar(1) Apply Service Tax Rule default=N [Y=Yes, N=No]
  AnnInvDecR Int(11) Annual Inv. Declaration Ref.
  Supplier nVarChar(15) Supplier ->OCRD
  Releaser Int(11) Goods Distribution Approver ->OHEM
  Receiver Int(11) Goods Release Approver ->OHEM
  ToWhsCode nVarChar(8) To Warehouse Code ->OWHS
  AssetDate Date(8) Fixed Asset Value Date
  Requester nVarChar(25) User Requesting Goods
  ReqName nVarChar(155) User Name
  Branch Int(6) Branch ->OUBR
  Department Int(6) Department ->OUDP
  Email nVarChar(100) E-Mail
  Notify VarChar(1) Send Notification Needed [Y=Yes, N=No]
  ReqType Int(11) Requester Type User/Employee default=12 [12=User, 171=Employee]
  OriginType VarChar(1) Document Origin default=M [M=Manual, R=MRP, S=Sales Order, D=Document Generation Wizard]
  IsReuseNum VarChar(1) Is Reusing Document Number default=N [Y=Yes, N=No]
  IsReuseNFN VarChar(1) Is Reusing Nota Fiscal Number default=N [Y=Yes, N=No]
  DocDlvry VarChar(1) Document Delivery [0=None, 1=Create Online Document, 2=Post to Ariba Network]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmF Num(19,6) Paid by Down Payment (FC)
  PaidDpmS Num(19,6) Paid by Down Payment (SC)
  EnvTypeNFe Int(11) Environment Type NF-e default=-1 ->OBNI
  AgrNo Int(11) Agreement No.
  IsAlt VarChar(1) Is Alteration default=N [Y=Yes, N=No]
  AltBaseTyp Int(11) Alteration Base Type default=-1 [-1=, 13=, 18=, 163=, 165=]
  AltBaseEnt Int(11) Alteration Base Entry
  AuthCode nVarChar(250) Authorization Code
  StDlvDate Date(8) Start Delivery Date
  StDlvTime Int(11) Start Delivery Time
  EndDlvDate Date(8) End Delivery Date
  EndDlvTime Int(11) End Delivery Time
  VclPlate nVarChar(20) Vehicle Plate
  ElCoStatus nVarChar(10) Elec. Comm. Status [0=Approved, 1=Pending Approval, 2=Rejected]
  AtDocType nVarChar(2) AT Document Type [GT=GT, GA=GA, GD=GD, GR=GR, GC=GC, FT=FT, FS=FS, NC=NC, ND=ND, FR=FR]
  ElCoMsg nVarChar(254) Elec. Comm. Message
  PrintSEPA VarChar(1) Print SEPA Direct Debit Prenotification default=N [Y=Yes, N=No]
  FreeChrg Num(19,6) Free of Charge BP
  FreeChrgFC Num(19,6) Free of Charge BP FC
  FreeChrgSC Num(19,6) Free of Charge BP SC
  NfeValue Num(19,6) NF-e Value
  FiscDocNum nVarChar(100) Fiscal Document Number
  RelatedTyp Int(11) Related Type default=-1 [-1=, 0=, 59=Goods Receipt, 60=Goods Issue]
  RelatedEnt Int(11) Related Entry
  CCDEntry Int(11) CCD Abs. Entry
  NfePrntFo Int(11) NF-e Printing Format default=0 [0=No DANFE, 1=Portrait, 2=Landscape, 3=Simplified, 4=DANFE NFC-e, 5=Mail]
  ZrdAbs Int(11) POS Daily Summary Number ->OZRD
  POSRcptNo Int(11) POS Receipt Number
  FoCTax Num(19,6) Free of Charge BP Tax
  FoCTaxFC Num(19,6) Free of Charge BP Tax FC
  FoCTaxSC Num(19,6) Free of Charge BP Tax SC
  TpCusPres Int(11) Type of End-User Presence ->OBNI
  ExcDocDate Date(8) Excise Doc. Date
  FoCFrght Num(19,6) Free of Charge Freight
  FoCFrghtFC Num(19,6) Free of Charge Freight FC
  FoCFrghtSC Num(19,6) Free of Charge Freight SC
  InterimTyp Int(6) Interim Type default=0 [0=None]
  PTICode nVarChar(5) POI Code ->OPTI
  Letter VarChar(1) Letter
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  FolSeries Int(11) Folio Series ->OFNS
  SplitTax Num(19,6) Split Payment Tax
  SplitTaxFC Num(19,6) Split Payment Tax FC
  SplitTaxSC Num(19,6) Split Payment Tax SC
  ToBinCode nVarChar(228) To Bin Location
  PriceMode VarChar(1) Price Mode [N=Net, G=Gross, M=Net and Gross]
  PoDropPrss VarChar(1) PO Drop-Ship Process default=N [Y=Yes, N=No]
  PermitNo nVarChar(20) Permit Number
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  DocTaxID nVarChar(32) Document Tax ID
  DateReport Date(8) Date of Reporting
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  PosCashReg Int(11) POS/Cash Register
  DmpTransID nVarChar(20) Trans ID for Down Payment
  ECommerBP nVarChar(15) E-Commerce Operator ->OCRD
  EComerGSTN nVarChar(15) GST Regn No of E-Commerce
  Revision VarChar(1) Revision default=N [Y=Yes, N=No]
  RevRefNo nVarChar(100) Original Ref. No.
  RevRefDate Date(8) Original Ref. Date
  RevCreRefN nVarChar(100) Original Credit/Debit Ref. No.
  RevCreRefD Date(8) Orign Credit/Debit Ref. Date
  TaxInvNo nVarChar(100) Tax Invoice No.
  FrmBpDate Date(8) From Vendor Date
  GSTTranTyp nVarChar(2) GST Transaction Type [--=Bill of Supply, GA=GST Tax Invoice, GD=GST Debit Memo]
  BaseType Int(11) Base Document Type default=-1 [-1=]
  BaseEntry Int(11) Base Document Internal Key
  ComTrade VarChar(1) Commission Trade default=E [E=, S=Sales Agent, P=Purchase Agent, C=Consignor]
  UseBilAddr VarChar(1) Determine GST by Using Bill to [Y=Yes, N=No]
  IssReason Int(6) Reason for issuing note default=1 [1=Sales Return, 2=Post sale discount, 3=Deficiency in service, 4=Correction in invoice, 5=Change in POS, 6=Finalization of Provisional Assessment, 7=Others]
  ComTradeRt VarChar(1) Commission Trade Return default=N [Y=Yes, N=No]
  SplitPmnt VarChar(1) A/P Split Payment default=N [Y=Yes, N=No]
  SOIWizId Int(11) SOI Wizard ID ->OSOI
  SelfPosted VarChar(1) Self Invoice Created [Yes/No] default=N [Y=Yes, N=No]
  EnBnkAcct Text(16) Encryption of Pay to Bank Acct
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EWBGenType VarChar(1) E-Way Bill Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  SAPPassprt Text(16) Extended SAP Passport
  CtActTax Num(19,6) Customer Accounting Tax
  CtActTaxFC Num(19,6) Customer Accounting Tax (FC)
  CtActTaxSC Num(19,6) Customer Accounting Tax (SC)

# OIGN - Goods Receipt
Module: Inventory and Production | 424 columns | ObjType: 59
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  AT_CARD: CardCode, NumAtCard
  CUSTOMER: CardCode
  NUM U: PIndicator, DocSubType, Segment, Instance, DocNum
  DOC_STATUS: CANCELED, DocStatus
  FTHR_CARD: FatherType, FatherCard
  SERIES: Series
  OWNER_CODE: OwnerCode
  DATE_PIND: PIndicator, DocDate
  ESERIES: EDocNum, ESeries
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Numerator
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No]
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original, A=Amended]
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Closed]
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=59 [59=Goods Receipt] ->ADP1
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) Revenue Account ->OCRD
  CardName nVarChar(100) Customer/Vendor Name
  Address nVarChar(254) Bill to
  NumAtCard nVarChar(100) Customer/Vendor Ref. No.
  VatPercent Num(19,6) Tax Rate
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  DiscPrcnt Num(19,6) Discount % for Document
  DiscSum Num(19,6) Total Discount
  DiscSumFC Num(19,6) Total Discount in FC
  DocCur nVarChar(3) Document Currency ->OCRN
  DocRate Num(19,6) Document Rate
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total in FC
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid in FC
  GrosProfit Num(19,6) Gross Profit
  GrosProfFC Num(19,6) Gross Profit in FC
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  ReceiptNum Int(11) Receipt Number
  GroupNum Int(6) Price List ->OCTG
  DocTime Int(6) Generation Time
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TrnspCode Int(6) Delivery Method default=-1 ->OSHP
  PartSupply VarChar(1) Partial Delivery default=Y [Y=Yes, N=No]
  Confirmed VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  GrossBase Int(6) Price List for Gross Profit default=0
  ImportEnt Int(11) Landed Costs Internal ID
  CreateTran VarChar(1) Create Journal Entry default=N [Y=Yes, N=No]
  SummryType VarChar(1) Summary Method default=N [N=No Summary, I=By Items, D=By Documents]
  UpdInvnt VarChar(1) Warehouse Update default=N [N=No, O=Orders from Vendors, C=Customer Orders, G=Consignment, I=Stock]
  UpdCardBal VarChar(1) Update Balances default=N [N=No, O=Orders, D=Delivery Notes, B=Bookkeeping]
  Instance Int(6) Instance default=0
  Flags Int(11) Flags default=0
  InvntDirec VarChar(1) Warehouse Direction default=X [X=Release, E=Receipt]
  CntctCode Int(11) Contact Person ->OCPR
  ShowSCN VarChar(1) Display BP Catalog Number default=N [Y=Yes, N=No]
  FatherCard nVarChar(15) BP Consolidation
  SysRate Num(19,6) System Price
  CurSource VarChar(1) Base Currency default=C [L=Local Currency, S=System Currency, C=BP Currency]
  VatSumSy Num(19,6) Tax Amount (SC)
  DiscSumSy Num(19,6) Total Discount in SC
  DocTotalSy Num(19,6) Document Total in SC
  PaidSys Num(19,6) Paid in SC
  FatherType VarChar(1) Parent Summary Type default=P [P=Payment Consolidation, D=Delivery Consolidation]
  GrosProfSy Num(19,6) Gross Profit in SC
  UpdateDate Date(8) Date of Update
  IsICT VarChar(1) A/R Invoice + Payment default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight Num(19,6) Weight
  WeightUnit Int(6) Weight UoM
  Series Int(11) Series ->NNM1
  TaxDate Date(8) Document Date
  Filler nVarChar(8) Filter ->OWHS
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  StampNum nVarChar(16) Stamp No.
  isCrin VarChar(1) Corrected Invoice default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  UserSign Int(6) User Signature ->OUSR
  selfInv VarChar(1) Autom. Invoice default=N [N=No, Y=Yes]
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid in FC
  VatPaidSys Num(19,6) Tax Paid in SC
  UserSign2 Int(6) Updating User ->OUSR
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  draftKey Int(11) Document Draft Internal ID default=-1 ->ODRF
  TotalExpns Num(19,6) Total Expenses
  TotalExpFC Num(19,6) Total Expenses (FC)
  TotalExpSC Num(19,6) Total Expenses (SC)
  DunnLevel Int(11) Dunning Level
  Address2 nVarChar(254) Ship-To Address
  LogInstanc Int(11) Log Instance default=0
  Exported VarChar(1) Exported default=N [Y=Yes, N=No]
  StationID Int(11) Workstation ID ->CSTN
  Indicator nVarChar(2) Indicator ->OIDC
  NetProc VarChar(1) Net Procedure default=N [Y=Yes, N=No]
  AqcsTax Num(19,6) Acquisition Tax
  AqcsTaxFC Num(19,6) Acquisition Tax (FC)
  AqcsTaxSC Num(19,6) Acquisition Tax (SC)
  CashDiscPr Num(19,6) Cash Discount Percentage
  CashDiscnt Num(19,6) Cash Discount
  CashDiscFC Num(19,6) Cash Discount (FC)
  CashDiscSC Num(19,6) Cash Discount (SC)
  ShipToCode nVarChar(50) Ship-to Code
  LicTradNum nVarChar(32) Licensed Dealer No.
  PaymentRef nVarChar(27) Payment Reference No.
  WTSum Num(19,6) Withholding Tax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  RoundDif Num(19,6) Rounding Diff. Amount
  RoundDifFC Num(19,6) Rounding Diff. Amount (FC)
  RoundDifSy Num(19,6) Rounding Diff. Amount (SC)
  CheckDigit VarChar(1) Control Digit
  Form1099 Int(11) 1099 Form ->OTNN
  Box1099 nVarChar(20) 1099 Box
  submitted VarChar(1) Submitted default=N [Y=Yes, N=No]
  PoPrss VarChar(1) PO Process default=N [Y=Yes, N=No]
  Rounding VarChar(1) Rounding default=N [Y=Yes, N=No]
  RevisionPo VarChar(1) Split PO default=N [Y=Yes, N=No]
  Segment Int(6) Segment default=0
  ReqDate Date(8) Required Date
  CancelDate Date(8) Cancelation Date
  PickStatus VarChar(1) Pick Status default=N [Y=Yes, N=No]
  Pick VarChar(1) Pick default=N [Y=Yes, N=No]
  BlockDunn VarChar(1) Block Dunning default=N [Y=Yes, N=No]
  PeyMethod nVarChar(15) Payment Method ->OPYM
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  MaxDscn VarChar(1) Maximum Discount default=N [Y=Yes, N=No]
  Reserve VarChar(1) Reserve default=N [Y=Yes, N=No]
  Max1099 Num(19,6) Max. 1099 Amount
  CntrlBnk nVarChar(15) Central Bank Indicator ->OCBI
  PickRmrk nVarChar(254) Pick Remarks
  ISRCodLine nVarChar(53) ISR Coding Line
  ExpAppl Num(19,6) Exp applied
  ExpApplFC Num(19,6) Exp applied FC
  ExpApplSC Num(19,6) Exp applied DC
  Project nVarChar(20) Project Code ->OPRJ
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  LetterNum nVarChar(20) Tax Exemption Letter No.
  FromDate Date(8) Exemption Validity Date From
  ToDate Date(8) Exemption Validity Date To
  WTApplied Num(19,6) Applied Withholding Tax
  WTAppliedF Num(19,6) Applied WTax (FC)
  BoeReserev VarChar(1) Bill of Exchange Reserved default=N [Y=Yes, N=No]
  AgentCode nVarChar(32) Agent Code ->OAGP
  WTAppliedS Num(19,6) Applied WTax (SC)
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  Installmnt Int(6) No. of Installments default=1
  VATFirst VarChar(1) Apply Tax on 1st Installment [Y=Yes, N=No]
  NnSbAmnt Num(19,6) WTax Non-Subject Amount
  NnSbAmntSC Num(19,6) WTax Non-Subject Amount (SC)
  NbSbAmntFC Num(19,6) WTax Non-Subject Amount (FC)
  ExepAmnt Num(19,6) Withholding Tax Exempt Amount
  ExepAmntSC Num(19,6) WTax Exempt Amount (FC)
  ExepAmntFC Num(19,6) WTax Exempt Amount (FC)
  VatDate Date(8) VAT Date
  CorrExt nVarChar(25) External Corrected Document No.
  CorrInv Int(11) Internal Corrected Document No.
  NCorrInv Int(11) Next Correcting Document
  CEECFlag VarChar(1) Block Creation Target Corr Inv default=N [N=No, Y=Yes]
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  CtlAccount nVarChar(15) Control Account ->OACT
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Registration Number
  TxInvRptNo nVarChar(10) Tax Invoice Rpt Number
  TxInvRptDt Date(8) Tax Invoice Rpt Date
  KVVATCode Text(16) VAT Code for Tax Invoice Rpt
  WTDetails nVarChar(100) Withholding Tax Details
  SumAbsId Int(11) Summary VAT Abstract ID default=-1
  SumRptDate Date(8) Summary VAT Report Date
  PIndicator nVarChar(10) Period Indicator ->OPID
  ManualNum nVarChar(20) Manual Number
  UseShpdGd VarChar(1) Use Shipped Goods Account default=N [N=No, Y=Yes]
  BaseVtAt Num(19,6) BPL ID Assigned to Invoice
  BaseVtAtSC Num(19,6) BPL Name
  BaseVtAtFC Num(19,6) Tax Reg. Number
  NnSbVAt Num(19,6) Tax Invoice Rpt Number
  NnSbVAtSC Num(19,6) Tax Invoice Rpt Date
  NbSbVAtFC Num(19,6) WTax Amount - VAT-exempt
  ExptVAt Num(19,6) WTax Exempted VAT Amount
  ExptVAtSC Num(19,6) WTax Exempted VAT Amount (SC)
  ExptVAtFC Num(19,6) Withholding Tax Details
  LYPmtAt Num(19,6) Last Year's Payments
  LYPmtAtSC Num(19,6) Last Years Payments (SC)
  LYPmtAtFC Num(19,6) Summary Tax Report Date
  ExpAnSum Num(19,6) Period Indicator
  ExpAnSys Num(19,6) Manual Number
  ExpAnFrgn Num(19,6) Use Shipped Goods Account
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=-- [--=Goods Receipt]
  DpmStatus VarChar(1) Summary VAT Abstract ID default=O [O=Open, C=Closed]
  DpmAmnt Num(19,6) Down Payment Amount LC
  DpmAmntSC Num(19,6) Down Payment Amount SC
  DpmAmntFC Num(19,6) Down Payment Amount FC
  DpmDrawn VarChar(1) Drawn to Down Payment default=N [N=No, Y=Yes]
  DpmPrcnt Num(19,6) Down Payment Percent
  PaidSum Num(19,6) Total Paid Sum
  PaidSumFc Num(19,6) Total Paid Sum (FC)
  PaidSumSc Num(19,6) Total Paid Sum (SC)
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  DpmAppl Num(19,6) Down Payment Applied LC
  DpmApplFc Num(19,6) Down Payment Applied FC
  DpmApplSc Num(19,6) Down Payment Applied SC
  LPgFolioN Int(11) Folio No. for Last Page in Doc.
  Header Text(16) Header
  Footer Text(16) Footer
  Posted VarChar(1) Down Payment Was Posted default=Y [Y=Yes, N=No]
  OwnerCode Int(11) Document Owner ->OHEM
  BPChCode nVarChar(15) BP Channel Code ->OCRD
  BPChCntc Int(11) BP Channel Contact Person ->OCPR
  PayToCode nVarChar(50) Pay to
  IsPaytoBnk VarChar(1) Is Pay to Bank [N=No, Y=Yes]
  BnkCntry nVarChar(3) Pay to Bank Country ->OCRY
  BankCode nVarChar(30) Pay to Bank Code
  BnkAccount nVarChar(50) Pay to Bank Account No.
  BnkBranch nVarChar(50) Pay to Bank Branch
  isIns VarChar(1) Reserve Invoice default=N [Y=Yes, N=No]
  TrackNo nVarChar(30) Tracking Number
  VersionNum nVarChar(11) Version Number
  LangCode Int(11) Language Code ->OLNG
  BPNameOW VarChar(1) BP_NAME_OVERWRITTEN default=N [Y=Yes, N=No]
  BillToOW VarChar(1) BILL_TO_OVERWRITTEN default=N [Y=Yes, N=No]
  ShipToOW VarChar(1) SHIP_TO_OVERWRITTEN default=N [Y=Yes, N=No]
  RetInvoice VarChar(1) Credit Memo default=N [Y=Yes, N=No]
  ClsDate Date(8) Document Closing Date
  MInvNum Int(11) Monthly Invoice No.
  MInvDate Date(8) Monthly Invoice Date
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  Model nVarChar(6) Nota Fiscal Model default=0 ->ONFM
  TaxOnExp Num(19,6) Tax On Expenses Sum
  TaxOnExpFc Num(19,6) Tax On Expenses Sum (FC)
  TaxOnExpSc Num(19,6) Tax On Expenses Sum (SC)
  TaxOnExAp Num(19,6) Tax On Expenses Applied
  TaxOnExApF Num(19,6) Tax on Freight Applied (FC)
  TaxOnExApS Num(19,6) Tax on Freight Applied (SC)
  LastPmnTyp VarChar(1) Last Payment Type [R=Receipt, V=Vendor Payment]
  LndCstNum Int(11) Landed Cost Number
  UseCorrVat VarChar(1) Use Correction VAT Group default=N [N=No, Y=Yes]
  BlkCredMmo VarChar(1) Block Creating Credit Memo Tgt default=N [N=No, Y=Yes]
  OpenForLaC VarChar(1) Open For Landed Costs default=Y [Y=Open for Landed Costs, N=Closed for Landed Costs]
  Excised VarChar(1) Excised default=O [O=Open, C=Close]
  ExcRefDate Date(8) Excise Ref. Date
  ExcRmvTime nVarChar(8) Excise Removal Time
  SrvGpPrcnt Num(19,6) Gross Profit Prcnt of Service
  DepositNum Int(11) Deposit Number
  CertNum nVarChar(31) Certificate Number
  DutyStatus VarChar(1) Duty Status default=Y [Y=With Payment of Duty, N=Without Payment of Duty]
  AutoCrtFlw VarChar(1) Auto Create Follow-up Document default=N [N=No, Y=Yes]
  FlwRefDate Date(8) Follow-up Document Ref. Date
  FlwRefNum nVarChar(100) Follow-up Document Ref. Number
  VatJENum Int(11) VAT Journal Entry Number default=-1
  DpmVat Num(19,6) Down Payment Tax LC
  DpmVatFc Num(19,6) Down Payment Tax FC
  DpmVatSc Num(19,6) Down Payment Tax SC
  DpmAppVat Num(19,6) Down Payment Applied Tax LC
  DpmAppVatF Num(19,6) Down Payment Applied Tax FC
  DpmAppVatS Num(19,6) Down Payment Applied Tax SC
  InsurOp347 VarChar(1) 347 Insurance Operation default=N [N=No, Y=Yes]
  IgnRelDoc VarChar(1) Ignore Relevant Doc on Archive default=N [N=No, Y=Yes]
  BuildDesc nVarChar(50) Build Descriptor
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Residence Country, 5=Certificate of Fiscal Residence, 6=Other Document, 7=Not Registered]
  Checker Int(11) Checker ->OHEM
  Payee Int(11) Payee ->OHEM
  CopyNumber Int(11) Copy Number default=0
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  PQTGrpSer Int(11) Pur Quotation Group Series
  PQTGrpNum Int(11) Pur Quotation Group Number
  PQTGrpHW VarChar(1) Pur Quotation Group Manual default=N [Y=Yes, N=No]
  ReopOriDoc VarChar(1) Reopen Origin. Order by Return [Y=Yes, N=No]
  ReopManCls VarChar(1) Reop. Man. Closed/Canc. Orders [Y=Yes, N=No]
  DocManClsd VarChar(1) Document Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  ClosingOpt Int(6) Closing Option default=1
  SpecDate Date(8) Posting Date Specified by User
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  NTSApprov VarChar(1) NTS Approved default=N [N=No, Y=Yes]
  NTSWebSite Int(6) E-Tax Web Site ->OTWS
  NTSeTaxNo nVarChar(50) E-Tax Number
  NTSApprNo nVarChar(50) NTS Approval Number
  PayDuMonth VarChar(1) Start From [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Number of Additional Months
  ExtraDays Int(6) Number of Additional Days
  CdcOffset Int(6) Cash Discount Offset default=0
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  EDocGenTyp VarChar(1) Electr. Doc. Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  ESeries Int(6) Electronic Series ->NNM4
  EDocNum nVarChar(50) Electronic Document Number
  EDocExpFrm Int(11) Electronic Doc. Export Format
  OnlineQuo VarChar(1) Create Online Quotation default=N [Y=Yes, N=No]
  POSEqNum nVarChar(20) POS Equipment Number
  POSManufSN nVarChar(20) POS Manufacturer Serial Number
  POSCashN Int(11) POS Cashier Number
  EDocStatus VarChar(1) Electronic Document Status default=C [N=New, P=Pending, S=Sent, E=Error, C=OK]
  EDocCntnt Text(16) Electronic Document Content
  EDocProces VarChar(1) Electronic Document Process default=C [C=CFD, I=CFDI]
  EDocErrCod nVarChar(50) Electronic Document Error Code
  EDocErrMsg Text(16) Electronic Document Error Msg
  EDocCancel VarChar(1) Electronic Document - Canceled default=N [N=No, Y=Yes]
  EDocTest VarChar(1) Electronic Document - Testing default=N [N=No, Y=Yes]
  EDocPrefix nVarChar(10) Electronic Document - Prefix
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  DpmAsDscnt VarChar(1) Discount Document with Dpm default=N [N=No, Y=Yes]
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  SupplCode nVarChar(254) Supplementary Code
  GTSRlvnt VarChar(1) Relevant To GTS default=N [N=No, Y=Yes]
  BaseDisc Num(19,6) Base Discount LC
  BaseDiscSc Num(19,6) Base Discount SC
  BaseDiscFc Num(19,6) Base Discount FC
  BaseDiscPr Num(19,6) Base Discount Percentage
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  SrvTaxRule VarChar(1) Apply Service Tax Rule default=N [Y=Yes, N=No]
  AnnInvDecR Int(11) Annual Inv. Declaration Ref.
  Supplier nVarChar(15) Supplier ->OCRD
  Releaser Int(11) Goods Distribution Approver ->OHEM
  Receiver Int(11) Goods Release Approver ->OHEM
  ToWhsCode nVarChar(8) To Warehouse Code ->OWHS
  AssetDate Date(8) Fixed Asset Value Date
  Requester nVarChar(25) User Requesting Goods
  ReqName nVarChar(155) User Name
  Branch Int(6) Branch ->OUBR
  Department Int(6) Department ->OUDP
  Email nVarChar(100) E-Mail
  Notify VarChar(1) Send Notification Needed [Y=Yes, N=No]
  ReqType Int(11) Requester Type User/Employee default=12 [12=User, 171=Employee]
  OriginType VarChar(1) Document Origin default=M [M=Manual, R=MRP, S=Sales Order, D=Document Generation Wizard]
  IsReuseNum VarChar(1) Is Reusing Document Number default=N [Y=Yes, N=No]
  IsReuseNFN VarChar(1) Is Reusing Nota Fiscal Number default=N [Y=Yes, N=No]
  DocDlvry VarChar(1) Document Delivery [0=None, 1=Create Online Document, 2=Post to Ariba Network]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmF Num(19,6) Paid by Down Payment (FC)
  PaidDpmS Num(19,6) Paid by Down Payment (SC)
  EnvTypeNFe Int(11) Environment Type NF-e default=-1 ->OBNI
  AgrNo Int(11) Agreement No.
  IsAlt VarChar(1) Is Alteration default=N [Y=Yes, N=No]
  AltBaseTyp Int(11) Alteration Base Type default=-1 [-1=, 13=, 18=, 163=, 165=]
  AltBaseEnt Int(11) Alteration Base Entry
  AuthCode nVarChar(250) Authorization Code
  StDlvDate Date(8) Start Delivery Date
  StDlvTime Int(11) Start Delivery Time
  EndDlvDate Date(8) End Delivery Date
  EndDlvTime Int(11) End Delivery Time
  VclPlate nVarChar(20) Vehicle Plate
  ElCoStatus nVarChar(10) Elec. Comm. Status [0=Approved, 1=Pending Approval, 2=Rejected]
  AtDocType nVarChar(2) AT Document Type [GT=GT, GA=GA, GD=GD, GR=GR, GC=GC, FT=FT, FS=FS, NC=NC, ND=ND, FR=FR]
  ElCoMsg nVarChar(254) Elec. Comm. Message
  PrintSEPA VarChar(1) Print SEPA Direct Debit Prenotification default=N [Y=Yes, N=No]
  FreeChrg Num(19,6) Free of Charge BP
  FreeChrgFC Num(19,6) Free of Charge BP FC
  FreeChrgSC Num(19,6) Free of Charge BP SC
  NfeValue Num(19,6) NF-e Value
  FiscDocNum nVarChar(100) Fiscal Document Number
  RelatedTyp Int(11) Related Type default=-1 [-1=, 0=, 59=Goods Receipt, 60=Goods Issue]
  RelatedEnt Int(11) Related Entry
  CCDEntry Int(11) CCD Abs. Entry
  NfePrntFo Int(11) NF-e Printing Format default=0 [0=No DANFE, 1=Portrait, 2=Landscape, 3=Simplified, 4=DANFE NFC-e, 5=Mail]
  ZrdAbs Int(11) POS Daily Summary Number ->OZRD
  POSRcptNo Int(11) POS Receipt Number
  FoCTax Num(19,6) Free of Charge BP Tax
  FoCTaxFC Num(19,6) Free of Charge BP Tax FC
  FoCTaxSC Num(19,6) Free of Charge BP Tax SC
  TpCusPres Int(11) Type of End-User Presence ->OBNI
  ExcDocDate Date(8) Excise Doc. Date
  FoCFrght Num(19,6) Free of Charge Freight
  FoCFrghtFC Num(19,6) Free of Charge Freight FC
  FoCFrghtSC Num(19,6) Free of Charge Freight SC
  InterimTyp Int(6) Interim Type default=0 [0=None]
  PTICode nVarChar(5) POI Code ->OPTI
  Letter VarChar(1) Letter
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  FolSeries Int(11) Folio Series ->OFNS
  SplitTax Num(19,6) Split Payment Tax
  SplitTaxFC Num(19,6) Split Payment Tax FC
  SplitTaxSC Num(19,6) Split Payment Tax SC
  ToBinCode nVarChar(228) To Bin Location
  PriceMode VarChar(1) Price Mode [N=Net, G=Gross, M=Net and Gross]
  PoDropPrss VarChar(1) PO Drop-Ship Process default=N [Y=Yes, N=No]
  PermitNo nVarChar(20) Permit Number
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  DocTaxID nVarChar(32) Document Tax ID
  DateReport Date(8) Date of Reporting
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  PosCashReg Int(11) POS/Cash Register
  DmpTransID nVarChar(20) Trans ID for Down Payment
  ECommerBP nVarChar(15) E-Commerce Operator ->OCRD
  EComerGSTN nVarChar(15) GST Regn No of E-Commerce
  Revision VarChar(1) Revision default=N [Y=Yes, N=No]
  RevRefNo nVarChar(100) Original Ref. No.
  RevRefDate Date(8) Original Ref. Date
  RevCreRefN nVarChar(100) Original Credit/Debit Ref. No.
  RevCreRefD Date(8) Orign Credit/Debit Ref. Date
  TaxInvNo nVarChar(100) Tax Invoice No.
  FrmBpDate Date(8) From Vendor Date
  GSTTranTyp nVarChar(2) GST Transaction Type [--=Bill of Supply, GA=GST Tax Invoice, GD=GST Debit Memo]
  BaseType Int(11) Base Document Type default=-1 [-1=]
  BaseEntry Int(11) Base Document Internal Key
  ComTrade VarChar(1) Commission Trade default=E [E=, S=Sales Agent, P=Purchase Agent, C=Consignor]
  UseBilAddr VarChar(1) Determine GST by Using Bill to [Y=Yes, N=No]
  IssReason Int(6) Reason for issuing note default=1 [1=Sales Return, 2=Post sale discount, 3=Deficiency in service, 4=Correction in invoice, 5=Change in POS, 6=Finalization of Provisional Assessment, 7=Others]
  ComTradeRt VarChar(1) Commission Trade Return default=N [Y=Yes, N=No]
  SplitPmnt VarChar(1) A/P Split Payment default=N [Y=Yes, N=No]
  SOIWizId Int(11) SOI Wizard ID ->OSOI
  SelfPosted VarChar(1) Self Invoice Created [Yes/No] default=N [Y=Yes, N=No]
  EnBnkAcct Text(16) Encryption of Pay to Bank Acct
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EWBGenType VarChar(1) E-Way Bill Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  SAPPassprt Text(16) Extended SAP Passport
  CtActTax Num(19,6) Customer Accounting Tax
  CtActTaxFC Num(19,6) Customer Accounting Tax (FC)
  CtActTaxSC Num(19,6) Customer Accounting Tax (SC)

# OIGW - Item Group - Warehouse
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: WhsCode, ItmsGrpCod
  WHS_CODE: WhsCode
  DFT_BIN: DftBinAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItmsGrpCod Int(6) Item Group Code ->OITB
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# OILM - Inventory Log Message
Module: Inventory and Production | 89 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: MessageID
  CARD: BPCardCode
  DocLine: SubLineNum, DocLineNum, DocEntry, TransType
  APPOBJ: AppObjLine, AppObjType, AppObjAbs, ApplObj
  BASEOBJ: BSubLineNo, BaseLine, BaseAbsEnt, BaseType
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID
  DocEntry Int(11) Doc Abs Entry
  TransType Int(11) Transaction Type default=-1
  DocLineNum Int(11) Doc Line Number
  Quantity Num(19,6) Quantity in Doc
  EffectQty Num(19,6) Stock Effect Qty
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TotalLC Num(19,6) Inventory Total LC
  TotalFC Num(19,6) Inventory Total FC
  TotalSC Num(19,6) Inventory Total SC
  BaseAbsEnt Int(11) Abs Entry of Base Doc
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 13=A/R Invoice, 15=Delivery, 16=Returns, 17=Sales Order, 18=A/P Invoice, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase Order, 23=Sales Quotation, 59=Goods Receipt, 67=Inventory Transfer, 69=Landed Costs, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment]
  BaseCurr nVarChar(3) Base Currency
  Currency nVarChar(3) Doc Currency ->OCRN
  AccumType Int(11) Accumulator Type default=0 [0=ACCUM_EMPTY, 1=ACCUM_ON_HAND, 2=ACCUM_COMMITTED, 3=ACCUM_ON_ORDER, 4=ACCUM_CONSIGNATION, 5=ACCUM_COUNTED]
  ActionType Int(11) Action Type default=5 [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]
  ExpensesLC Num(19,6) Expenses (LC)
  ExpensesFC Num(19,6) Expenses (FC)
  ExpensesSC Num(19,6) Expenses (SC)
  DocDueDate Date(8) Doc. Due Date
  ItemCode nVarChar(50) Item Code ->OITM
  BPCardCode nVarChar(15) Business Partner Code ->OCRD
  DocDate Date(8) Doc Date
  DocRate Num(19,6) Doc. Rate
  Comment nVarChar(254) Comment
  JrnlMemo nVarChar(50) Journal Remarks
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(100) Reference 2
  BaseLine Int(11) Base Line Number default=-1
  SnBType Int(11) Serials and Batches Type default=-1 [0=Batch Numbers Management, 1=Serial Numbers Management]
  CreateTime Int(6) Generation Time
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  CreateDate Date(8) Creation Date
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  DocPrice Num(19,6) Doc Price
  CardName nVarChar(100) BP Name
  Dscription nVarChar(100) Item Description
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=BOM Component Item, P=Production, T=Template]
  ApplObj Int(11) Applied Object default=-1
  AppObjAbs Int(11) Applied Object Abs Entry default=-1
  AppObjType VarChar(1) Applied Object Type
  AppObjLine Int(11) Applied Object Line default=-1
  BASE_REF nVarChar(11) Base Reference
  TransSeqRf Int(11) Transaction Sequence Ref default=-1
  LayerIDRef Int(11) Layer ID Reference default=-1
  VersionNum nVarChar(11) Version Number
  PriceRate Num(19,6) Price Rate
  PriceCurr nVarChar(3) Price Currency ->OCRN
  DocTotal Num(19,6) Document Total
  Price Num(19,6) Price
  CIShbQty Num(19,6) Corr. Inv. Doc. Should Be Qty
  SubLineNum Int(11) Sub Line Number default=-1
  PrjCode nVarChar(20) Project code ->OPRJ
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TaxDate Date(8) Document Date
  UseDocPric VarChar(1) Use Document Price default=N [Y=Yes, N=No]
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  Location Int(11) Location ->OLCT
  DocPrcRate Num(19,6) Document Price Rate
  DocPrcCurr nVarChar(3) Document Price Currency ->OCRN
  CgsOcrCod nVarChar(8) COGS Distribution Rule ->OOCR
  CgsOcrCod2 nVarChar(8) COGS Distribution Rule 2 ->OOCR
  CgsOcrCod3 nVarChar(8) COGS Distribution Rule 3 ->OOCR
  CgsOcrCod4 nVarChar(8) COGS Distribution Rule 4 ->OOCR
  CgsOcrCod5 nVarChar(8) COGS Distribution Rule 5 ->OOCR
  BSubLineNo Int(11) Base Subrow Number default=-1
  AppSubLine Int(11) Applied Subrow Number default=-1
  UserSign Int(6) User Signature ->OUSR
  SysRate Num(19,6) System Rate
  ExFromRpt VarChar(1) Exclude from Report default=N [Y=Yes, N=No]
  Ref3 nVarChar(11) Reference 3
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  DocAction Int(11) Document Action Type
  UseShpdGd VarChar(1) Use Shipped Goods Account default=N [N=No, Y=Yes]
  AddTotalLC Num(19,6) Additional Total LC
  AddExpLC Num(19,6) Additional Expenses LC
  IsNegLnQty VarChar(1) Negative Line Quantity default=N
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry
  StgDesc nVarChar(100) Stage Description

# OIMT - Templates for Inventory JE
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TemplateId
  SECONDARY U: TmpType, Action, LocalizId, ValuatType, BaseType, TransType
Fields (name type(len) description [values] ->parent table):
  ValuatType VarChar(1) Document Valuation Type default=N [A=, F=, S=, N=unDefined]
  TransType Int(11) Transaction type default=-1
  BaseType Int(6) Base Transaction Type default=-1
  TemplateId Int(6) Template ID default=-1
  LocalizId nVarChar(2) Localization Identifier default=XX [XX=All Localizations]
  Action Int(6) Action Type default=0
  JEPosting VarChar(1) Posting Status default=N [N=None, C=Complete, P=Partial]
  LineActTyp Int(6) Line Account Type default=2 [2=LINE_ACCT_TYPE]
  TmpType Int(6) Template Type default=0
  Total VarChar(1) Total Type default=M [M=Total from Message, C=Total from Calculator, F=Total from Formula]

# OINC - Inventory Counting
Module: Inventory and Production | 35 columns | ObjType: 1470000065
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  SERIES U: DocNum, Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  CountDate Date(8) Date of Counting
  Time Int(11) Time of Counting
  CountType VarChar(1) Counting Type default=1 [1=Single Counter, 2=Multiple Counters]
  Taker1Type Int(11) Type of Counter default=12 [12=User, 171=Employee]
  Taker1Id Int(11) Counter ID
  Taker2Type Int(11) - default=12 [12=User, 171=Employee]
  Taker2Id Int(11) -
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  Ref2 nVarChar(11) Reference 2
  Remarks Text(16) Remarks
  LogIns Int(11) Log Instance - History
  UserSign Int(6) User Creating - History ->OUSR
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  CreateDate Date(8) Create Date - History
  ObjType nVarChar(20) Object Type default=1470000065
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Approved]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OICD
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  TeamCount Int(11) Count of Team Counters default=0
  IndvCount Int(11) Count of Individual Counters default=0
  DiffQty Num(19,6) Total Difference
  DiffPercen Num(19,6) Total Difference (%)
  UpdateTS Int(11) Update Full Time
  CreateTime Int(6) Generation Time
  PIndicator nVarChar(10) Period Indicator ->OPID
  FinncPriod Int(11) Posting Period ->OFPR
  PostDate Date(8) Posting Date
  VersionNum nVarChar(11) Version Number
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]

# OIOD - Inventory Opening Balance Draft
Module: Inventory and Production | 34 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  DOC_DATE: DocDate
  CREATEDATE: DocTime, CreateDate
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  CreateDate Date(8) Creation Date
  DocTime Int(6) Generation Time
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DocDate Date(8) Posting Date
  Reference nVarChar(11) Reference
  Comments nVarChar(254) Remarks
  DocDueDate Date(8) Due Date
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  VersionNum nVarChar(11) Version Number
  JdtNum Int(11) Journal Number
  Reference2 nVarChar(11) Reference 2
  ObjType nVarChar(20) Object Type default=310000001
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PriceSrc VarChar(1) Price Source default=3 [1=By Price List, 2=Last Evaluated Price, 3=Item Cost]
  PriceList Int(11) Price List
  JrnlMemo nVarChar(50) Journal Remarks
  TaxDate Date(8) Document Date
  Status VarChar(1) Status default=O [O=Open, C=Close]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Update User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OIOD
  Printed VarChar(1) Printed default=N
  DocTotal Num(19,6) Document Total
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  UpdateTS Int(11) Update Full Time
  PIndicator nVarChar(10) Period Indicator
  FinncPriod Int(11) Posting Period

# OIPD - Inventory Posting Draft
Module: Inventory and Production | 37 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  DOC_DATE: DocDate
  CREATEDATE: DocTime, CreateDate
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  CreateDate Date(8) Creation Date
  DocTime Int(6) Generation Time
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DocDate Date(8) Posting Date
  Reference nVarChar(11) Reference
  Comments nVarChar(254) Remarks
  DocDueDate Date(8) Due Date
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  VersionNum nVarChar(11) Version Number
  JdtNum Int(11) Journal Number ->OJDT
  Reference2 nVarChar(11) Reference 2
  ObjType nVarChar(20) Object Type default=10000071
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PriceSrc Int(11) Price Source default=3 [1=By Price List, 2=Last Evaluated Price, 3=Item Cost]
  PriceList Int(11) Price List
  JrnlMemo nVarChar(50) Journal Remarks
  Status VarChar(1) Status default=O [O=Open, C=Close]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  CountDate Date(8) Date of Counting
  CountTime Int(11) Time of Counting
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OIPD
  Printed VarChar(1) Printed default=N
  DocTotal Num(19,6) Document Total
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  UpdateTS Int(11) Update Full Time
  CopyOption VarChar(1) DI Copy from Option default=0 [0=No Counters Diff., 1=Individual 1, 2=Individual 2, 3=Individual 3, 4=Individual 4, 5=Individual 5, 6=Team Counted Quantity]
  BaseEntry Int(11) Base Counting Doc. Entry
  PIndicator nVarChar(10) Period Indicator
  FinncPriod Int(11) Posting Period

# OIPF - Landed Costs
Module: Inventory and Production | 64 columns | ObjType: 69
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM U: Series, Instance, DocNum
  SUPPLIER: CardCode
  AGENT: AgentNum, AgentCode
  CURRENCY: DocCur
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) Vendor Code ->OCRD
  SuppName nVarChar(100) Vendor Name
  AgentCode nVarChar(15) Subst. Code ->OCRD
  AgentName nVarChar(100) Subst. Name
  DocStatus VarChar(1) Document Status default=O [C=Closed, O=Open]
  AgentNum nVarChar(16) File Number
  Descr nVarChar(250) Remarks
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  DocCur nVarChar(3) Document Currency
  DocRate Num(19,6) Document Rate
  ExpCustom Num(19,6) Projected Customs
  ActCustom Num(19,6) Act. Import Duty
  Vat1 Num(19,6) Tax 2
  Vat2 Num(19,6) Tax 2
  BeforeVat Num(19,6) Total Before Tax
  DocTotal Num(19,6) Document Total
  CostSum Num(19,6) Total Costs
  DocTime Int(6) Generation Time
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  ExCustomFC Num(19,6) Projected Customs (FC)
  AcCustomFC Num(19,6) Act. Import Duty in FC
  Vat1FC Num(19,6) Tax 1 (FC)
  Vat2FC Num(19,6) Tax 2 (FC)
  BeforVatFC Num(19,6) Total Before Tax (FC)
  DocTotalFC Num(19,6) Document Total (FC)
  CostSumFC Num(19,6) Total Costs (FC)
  CloseDate Date(8) Closing Date
  Cost_Match Num(19,6) Expenses Diff. for Reconciliation
  C_Match_FC Num(19,6) Expenses Diff. for Recon. (FC)
  BillOfLad nVarChar(20) Bill of Lading No.
  TrnspCode Int(6) Delivery Category ->OSHP
  CostFactor Num(19,6) Expenses Factor
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  TaxDate Date(8) Document Date
  Series Int(11) Series
  JdtNum Int(11) Journal Number ->OJDT
  JdtMemo nVarChar(50) Transaction Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ObjType nVarChar(20) Object Type default=69 ->ADP1
  ExCustomSC Num(19,6) Projected Customs (SC)
  ActCustSC Num(19,6) Actual Customs (SC)
  TtlCostSC Num(19,6) Total Expenditure (SC)
  VersionNum nVarChar(11) Version Number
  OpenForLaC VarChar(1) Open For Landed Costs default=Y [Y=Yes, N=No]
  incCustom VarChar(1) Include Customs Expenses default=Y
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  BuildDesc nVarChar(50) Build Descriptor
  SupplCode nVarChar(254) Supplementary Code
  AtcEntry Int(11) Attachment Entry
  CustDate Date(8) Customs Date
  BPLId Int(11) Branch ->OBPL
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# OIQI - Inventory Opening Balance
Module: Inventory and Production | 34 columns | ObjType: 310000001
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  DOC_DATE: DocDate
  CREATEDATE: DocTime, CreateDate
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  CreateDate Date(8) Creation Date
  DocTime Int(6) Generation Time
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DocDate Date(8) Posting Date
  Reference nVarChar(11) Reference
  Comments nVarChar(254) Remarks
  DocDueDate Date(8) Due Date
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  VersionNum nVarChar(11) Version Number
  JdtNum Int(11) Journal Number
  Reference2 nVarChar(11) Reference 2
  ObjType nVarChar(20) Object Type default=310000001
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PriceSrc VarChar(1) Price Source default=3 [1=By Price List, 2=Last Evaluated Price, 3=Item Cost]
  PriceList Int(11) Price List
  JrnlMemo nVarChar(50) Journal Remarks
  TaxDate Date(8) Document Date
  Status VarChar(1) Status default=O [O=Open, C=Close]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Update User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OIOD
  Printed VarChar(1) Printed default=N
  DocTotal Num(19,6) Document Total
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  UpdateTS Int(11) Update Full Time
  PIndicator nVarChar(10) Period Indicator ->OPID
  FinncPriod Int(11) Posting Period ->OFPR

# OIQR - Inventory Posting
Module: Inventory and Production | 37 columns | ObjType: 10000071
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  DOC_DATE: DocDate
  CREATEDATE: DocTime, CreateDate
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  CreateDate Date(8) Creation Date
  DocTime Int(6) Generation Time
  IOffIncAcc nVarChar(15) Inventory Offset - Increase Ac ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DocDate Date(8) Posting Date
  Reference nVarChar(11) Reference
  Comments nVarChar(254) Remarks
  DocDueDate Date(8) Due Date
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  VersionNum nVarChar(11) Version Number
  JdtNum Int(11) Journal Number ->OJDT
  Reference2 nVarChar(11) Reference 2
  ObjType nVarChar(20) Object Type default=10000071
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PriceSrc Int(11) Price Source default=3 [1=By Price List, 2=Last Evaluated Price, 3=Item Cost]
  PriceList Int(11) Price List
  JrnlMemo nVarChar(50) Journal Remarks
  Status VarChar(1) Status default=O [O=Open, C=Close]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  CountDate Date(8) Date of Counting
  CountTime Int(11) Time of Counting
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  DraftKey Int(11) Draft Document Internal ID default=-1 ->OIPD
  Printed VarChar(1) Printed default=N
  DocTotal Num(19,6) Document Total
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  UpdateTS Int(11) Update Full Time
  CopyOption VarChar(1) DI Copy from Option default=0 [0=No Counters Diff., 1=Individual 1, 2=Individual 2, 3=Individual 3, 4=Individual 4, 5=Individual 5, 6=Team Counted Quantity]
  BaseEntry Int(11) Base Counting Doc. Entry
  PIndicator nVarChar(10) Period Indicator ->OPID
  FinncPriod Int(11) Posting Period ->OFPR

# OIRT - Interest Prices
Module: Inventory and Production | 5 columns | ObjType: 92
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Numerator
Fields (name type(len) description [values] ->parent table):
  Numerator Int(11) Internal Number
  EffectDate Date(8) Expiration Date
  AnlIntrst Num(19,6) Annual Interest Rate
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OISL - Simulation Log File
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Internal Number
  TaskType nVarChar(20) Type of Task
  RunID Int(11) Simulation Run
  Version Int(11) B1 Main Release Version
  PatchLevel nVarChar(50) B1 Patch Level Version
  LastMsgID Int(11) Last OILM Message ID
  FinishDate Date(8) Finish Date
  FinishTime Int(6) Finish Time
  UserCode nVarChar(25) User Code
  Status VarChar(1) Status [R=In Progress, F=Failed, S=Successful]
  InitMap VarChar(1) Initialize MAP Items
  InitStd VarChar(1) Initialize STD Items

# OITB - Item Groups
Module: Inventory and Production | 82 columns | ObjType: 52
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItmsGrpCod
  GROUP_NAME U: ItmsGrpNam
Fields (name type(len) description [values] ->parent table):
  ItmsGrpCod Int(6) Number
  ItmsGrpNam nVarChar(20) Group Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Allocation Account ->OACT
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns Account ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Revenue Account - EU ->OACT
  EUExpensAc nVarChar(15) Expense Account - EU ->OACT
  FrRevenuAc nVarChar(15) Revenue Account - Foreign ->OACT
  FrExpensAc nVarChar(15) Expense Account - Foreign ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  CycleCode Int(6) Cycle Code ->OCYC
  Alert VarChar(1) Alert default=N [N=No, Y=Yes]
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  ExchangeAc nVarChar(15) Exchange Rate Differences Account ->OACT
  BalanceAcc nVarChar(15) Goods Clearing Account ->OACT
  PurchaseAc nVarChar(15) Purchase Account ->OACT
  PAReturnAc nVarChar(15) Purchase Return Account ->OACT
  PurchOfsAc nVarChar(15) Purchase Offset Account ->OACT
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  InvntSys VarChar(1) Inventory System [A=Moving Average, S=Standard, F=FIFO]
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  StokRvlAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkOffsAct nVarChar(15) Inventory Revaluation Offset Account ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  CostRvlAct nVarChar(15) COGS Revaluation Account ->OACT
  CstOffsAct nVarChar(15) COGS Revaluation Offset Acct ->OACT
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  Object nVarChar(20) Object Type - History default=52
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  ARCMAct nVarChar(15) Sales Credit Account ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign ->OACT
  ARCMEUAct nVarChar(15) Sales Credit Account - EU ->OACT
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account ->OACT
  APCMAct nVarChar(15) Purchase Credit Account ->OACT
  APCMFrnAct nVarChar(15) Purchase Credit Account - Foreign ->OACT
  APCMEUAct nVarChar(15) Purchase Credit Account - EU ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account ->OACT
  ItemClass VarChar(1) Service or Material default=2 [1=Service, 2=Material]
  OSvcCode Int(11) Outgoing Service Code default=-1 ->OSCD
  ISvcCode Int(11) Incoming Service Code default=-1 ->OSCD
  ServiceGrp Int(11) Service Group default=-1 ->OSGP
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  NegStckAct nVarChar(15) Negative Inventory Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account ->OACT
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  UgpEntry Int(11) Default UoM Group Entry ->OUGP
  IUoMEntry Int(11) Default Inventory UoM ->OUOM
  ToleranDay Int(11) Tolerance Days
  RuleCode nVarChar(2) Checking Rule Code ->ODCR
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]
  FreeChrgSA nVarChar(15) Free of Charge Sales Account ->OACT
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account ->OACT
  RawMtrl VarChar(1) Raw Material default=N [N=No, Y=Yes]

# OITG - Item Properties
Module: Inventory and Production | 3 columns | ObjType: 8
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItmsTypCod
  GROUP_NAME U: ItmsGrpNam
Fields (name type(len) description [values] ->parent table):
  ItmsTypCod Int(6) Number
  ItmsGrpNam nVarChar(50) Property Name
  UserSign Int(6) User Signature ->OUSR

# OITL - Inventory Transactions Log
Module: Inventory and Production | 40 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogEntry
  DOC_INFO: DocEntry, SubLineNum, DocLine, ManagedBy, DocType
  BASEREF: BSubLineNo, BaseLine, BaseEntry, BaseType
  APPLYREF: AppSubLine, ApplyLine, ApplyEntry, ApplyType
  TRANSID: TransId
  ACTUAL_INF: ManagedBy, ActBaseTp, ActBaseEnt, ActBaseLn, ActBasSubL
  ALLOC_REF: AllocateLn, AllocatEnt, AllocateTp
  DOC_REF: LogEntry, DocLine, DocEntry, DocType
  ITEM_CODE: ApplyType, LogEntry, ItemCode, LocCode, ManagedBy, Instance, ApplyEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Internal ID
  TransId Int(11) Transaction ID
  ItemCode nVarChar(50) Item Code ->OITM
  ItemName nVarChar(100) Item Description
  ManagedBy Int(11) Management Method default=4 [10000044=BTN, 10000045=SRN, 4=ITM]
  DocEntry Int(11) Document Internal ID
  DocLine Int(11) Doc. Row Number
  DocType Int(11) Transact. Type default=-1
  DocNum Int(11) Doc. Number
  BaseEntry Int(11) Base Document Internal ID default=-1
  BaseLine Int(11) Base Document Row Number default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 13=A/R Invoice, 15=Delivery, 16=Returns, 17=Sales Order, 18=A/P Invoice, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase Order, 23=Sales Quotation, 59=Goods Receipt, 67=Inventory Transfer, 69=Landed Costs, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment]
  ApplyEntry Int(11) Applied Document Internal ID
  ApplyLine Int(11) Applied Document Line Number
  ApplyType Int(11) Applied Document Type default=-1
  DocDate Date(8) Doc. Posting Date
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  DocQty Num(19,6) Doc. Quantity
  StockQty Num(19,6) Stock Affecting Quantity
  DefinedQty Num(19,6) SnB Defined Quantity
  StockEff Int(11) Stock Effect default=0 [0=ACCUM_EMPTY, 1=ACCUM_ON_HAND, 2=ACCUM_COMMITTED, 3=ACCUM_ON_ORDER]
  CreateDate Date(8) Creation Date
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  AppDocNum Int(11) Applied Document Number
  VersionNum nVarChar(11) Version Number
  Transfered VarChar(1) Year Tranfer default=N
  Instance Int(6) INSTANCE default=0
  SubLineNum Int(11) Subrow Number default=-1
  BSubLineNo Int(11) Base Subrow Number default=-1
  AppSubLine Int(11) Applied Subrow Number default=-1
  ActBaseTp Int(11) Actual Base Type default=-1
  ActBaseEnt Int(11) Actual Base Entry
  ActBaseLn Int(11) Actual Base Line default=-1
  ActBasSubL Int(11) Actual Base Subline default=-1
  AllocateTp Int(11) Allocate Document Type default=-1
  AllocatEnt Int(11) Allocate Document Entry default=-1
  AllocateLn Int(11) Allocate Document Line default=-1
  CreateTime Int(6) Creation Time default=0

# OITM - Items
Module: Inventory and Production | 322 columns | ObjType: 4
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItemCode
  ITEM_NAME: ItemName
  TREE_TYPE: TreeType
  COM_GROUP: CommisGrp
  SALE: SellItem
  PURCHASE: PrchseItem
  INVENTORY: InvntItem
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No.
  ItemName nVarChar(100) Item Description
  FrgnName nVarChar(100) Foreign Name
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  CstGrpCode Int(6) Customs Group default=-1 ->OARG
  VatGourpSa nVarChar(8) Sales Tax Definition ->OVTG
  CodeBars nVarChar(254) Bar Code
  VATLiable VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  PrchseItem VarChar(1) Purchase Item default=Y [Y=Yes, N=No]
  SellItem VarChar(1) Sales Item default=Y [Y=Yes, N=No]
  InvntItem VarChar(1) Inventory Item default=Y [Y=Yes, N=No]
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Qty Ordered by Customers
  OnOrder Num(19,6) Qty Ordered from Vendors
  IncomeAcct nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  MaxLevel Num(19,6) Maximum Inventory Level
  DfltWH nVarChar(8) Default Warehouse
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  SuppCatNum nVarChar(50) Mfr Catalog No.
  BuyUnitMsr nVarChar(100) Purchasing UoM
  NumInBuy Num(19,6) No. of Items per Purchase Unit
  ReorderQty Num(19,6) Required (Purchasing UoM)
  MinLevel Num(19,6) Minimum Inventory Level
  LstEvlPric Num(19,6) Last Evaluated Price
  LstEvlDate Date(8) Date of Last Reval. Price
  CustomPer Num(19,6) Customs Rate
  Canceled VarChar(1) Canceled Item [Yes/No] default=N [Y=Yes, N=No]
  MnufctTime Int(11) Production Date in Days
  WholSlsTax VarChar(1) Tax Rate for Wholesaler
  RetilrTax VarChar(1) Sales Tax in %
  SpcialDisc Num(19,6) Special Discount %
  DscountCod Int(6) Discount Code
  TrackSales VarChar(1) Follow-Up [Yes/No] default=N [Y=Yes, N=No]
  SalUnitMsr nVarChar(100) Sales UoM
  NumInSale Num(19,6) No. of Items per Sales Unit
  Consig Num(19,6) Consignment Goods Whse
  QueryGroup Int(11) Properties default=0
  Counted Num(19,6) Quantity Counted in Inventory
  OpenBlnc Num(19,6) Initial Stock
  EvalSystem VarChar(1) Valuation Method [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch]
  UserSign Int(6) User Signature ->OUSR
  FREE VarChar(1) Free [Yes/No] default=N [Y=Yes, N=No]
  PicturName nVarChar(200) Picture
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  BlncTrnsfr VarChar(1) Balances transferred [Yes/No] default=N [Y=Yes, N=No]
  UserText Text(16) Item Remarks
  SerialNum nVarChar(17) Serial Number
  CommisPcnt Num(19,6) % Commission for Item
  CommisSum Num(19,6) Total Commission for Item
  CommisGrp Int(6) Commission Group default=0 ->OCOG
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, P=Production, T=Template]
  TreeQty Num(19,6) No. of Units
  LastPurPrc Num(19,6) Last Purchase Price
  LastPurCur nVarChar(3) Last Purchase Currency
  LastPurDat Date(8) Last Purchase Date
  ExitCur nVarChar(3) Issue Currency
  ExitPrice Num(19,6) Issue Price
  ExitWH nVarChar(8) Release Warehouse
  AssetItem VarChar(1) Fixed Asset Indicator default=N [Y=Yes, N=No]
  WasCounted VarChar(1) Counted default=N [Y=Yes, N=No]
  ManSerNum VarChar(1) Serial No. Management default=N [Y=Yes, N=No]
  SHeight1 Num(19,6) Height 1 - Sales Unit
  SHght1Unit Int(6) Height 1 - UoM for Sales
  SHeight2 Num(19,6) Height 2 - Sales Unit
  SHght2Unit Int(6) Height 2 - UoM for Sales
  SWidth1 Num(19,6) Width 1 - Sales Unit
  SWdth1Unit Int(6) Width 1 - UoM for Sales
  SWidth2 Num(19,6) Width 2 - Sales Unit
  SWdth2Unit Int(6) Width 2 - UoM for Sales
  SLength1 Num(19,6) Length 1 - Sales Unit
  SLen1Unit Int(6) Length 1 - UoM for Sales
  Slength2 Num(19,6) Length 2 - Sales Unit
  SLen2Unit Int(6) Length 2 - UoM for Sales
  SVolume Num(19,6) Volume - Sales Unit
  SVolUnit Int(6) Volume - UoM for Sales
  SWeight1 Num(19,6) Weight 1 - Sales Unit
  SWght1Unit Int(6) Weight 1 - UoM for Sales
  SWeight2 Num(19,6) Weight 2 - Sales Unit
  SWght2Unit Int(6) Weight 2 - UoM for Sales
  BHeight1 Num(19,6) Height 1 - Purchasing Unit
  BHght1Unit Int(6) Height 1 - UoM for Purchasing
  BHeight2 Num(19,6) Height 2 - Purchasing Unit
  BHght2Unit Int(6) Height 2 - UoM for Purchasing
  BWidth1 Num(19,6) Width 1 - Purchasing Unit
  BWdth1Unit Int(6) Width 1 - UoM for Purchasing
  BWidth2 Num(19,6) Width 2 - Purchasing Unit
  BWdth2Unit Int(6) Width 2 - UoM for Purchasing
  BLength1 Num(19,6) Length 1 - Purchase Unit
  BLen1Unit Int(6) Length 1 - UoM for Purchasing
  Blength2 Num(19,6) Length 2 - Purchase Unit
  BLen2Unit Int(6) Length 2 - UoM for Purchasing
  BVolume Num(19,6) Volume - Purchasing Unit
  BVolUnit Int(6) Volume - UoM for Purchasing
  BWeight1 Num(19,6) Weight 1 - Purchasing Unit
  BWght1Unit Int(6) Weight 1 - UoM for Purchasing
  BWeight2 Num(19,6) Weight 2 - Purchasing Unit
  BWght2Unit Int(6) Weight 2 - UoM for Purchasing
  FixCurrCms nVarChar(3) Currency of Fixed Commission
  FirmCode Int(6) Manufacturer default=-1 ->OMRC
  LstSalDate Date(8) Last Sale Date
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
  CreateDate Date(8) Production Date
  UpdateDate Date(8) Date of Update
  ExportCode nVarChar(20) Data Export Code
  SalFactor1 Num(19,6) Sales Factor 1
  SalFactor2 Num(19,6) Sales Factor 2
  SalFactor3 Num(19,6) Sales Factor 3
  SalFactor4 Num(19,6) Sales Factor 4
  PurFactor1 Num(19,6) Purchasing Factor 1
  PurFactor2 Num(19,6) Purchasing Factor 2
  PurFactor3 Num(19,6) Purchasing Factor 3
  PurFactor4 Num(19,6) Purchasing Factor 4
  SalFormula nVarChar(40) Sales Formula
  PurFormula nVarChar(40) Purchasing Formula
  VatGroupPu nVarChar(8) Purchase Tax Definition ->OVTG
  AvgPrice Num(19,6) Item Cost
  PurPackMsr nVarChar(30) Packaging UoM (Purchasing)
  PurPackUn Num(19,6) Quantity per Package (Purchasing)
  SalPackMsr nVarChar(30) Packaging UoM (Sales)
  SalPackUn Num(19,6) Quantity per Package (Sales)
  SCNCounter Int(6) SCN Counter
  ManBtchNum VarChar(1) Manage Batch No. [Yes/No] default=N [Y=Yes, N=No]
  ManOutOnly VarChar(1) Manage SN Only on Exit default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer, G=Fixed Assets Migration]
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  BlockOut VarChar(1) Force selection of serial no. default=Y [Y=Yes, N=No]
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=4 ->ADP1
  SWW nVarChar(16) Additional Identifier
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  DocEntry Int(11) Internal Number
  ExpensAcct nVarChar(15) Expense Account ->OACT
  FrgnInAcct nVarChar(15) Revenue Account - Foreign ->OACT
  ShipType Int(6) Shipping Type ->OSHP
  GLMethod VarChar(1) Set G/L Accounts By default=W [W=Warehouse, C=Item Group, L=Item Level]
  ECInAcct nVarChar(15) Revenue Account - EU
  FrgnExpAcc nVarChar(15) Expense Account - Foreign
  ECExpAcc nVarChar(15) Expense Account - EU
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, U=Use Tax, N=No Tax]
  ByWh VarChar(1) Manage Inventory by Warehouse [Y=Yes, N=No]
  WTLiable VarChar(1) WTax Liable default=Y [Y=Yes, N=No]
  ItemType VarChar(1) Item Type default=I [I=Items, L=Labor, T=Travel, F=Fixed Assets]
  WarrntTmpl nVarChar(20) Warranty Template ->OCTT
  BaseUnit nVarChar(20) Base Unit Name
  CountryOrg nVarChar(3) Country of Origin
  StockValue Num(19,6) Inventory Value
  Phantom VarChar(1) Phantom Item default=N [Y=Yes, N=No]
  IssueMthd VarChar(1) Issue Method [B=Backflush, M=Manual]
  FREE1 VarChar(1) Yield in %
  PricingPrc Num(19,6) Pricing Percentage
  MngMethod VarChar(1) Management Method default=R [A=On Every Transaction, R=On Release Only]
  ReorderPnt Num(19,6) Reorder Point
  InvntryUom nVarChar(100) Inventory UoM
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  IndirctTax VarChar(1) Indirect Tax default=N [Y=Yes, N=No]
  TaxCodeAR nVarChar(8) Tax Code (A/R) ->OSTC
  TaxCodeAP nVarChar(8) Tax Code (A/P) ->OSTC
  OSvcCode Int(11) Outgoing Service Code default=-1 ->OSCD
  ISvcCode Int(11) Incoming Service Code default=-1 ->OSCD
  ServiceGrp Int(11) Service Group default=-1 ->OSGP
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  ServiceCtg Int(11) Service Category default=-1 ->OSCG
  ItemClass VarChar(1) Service or Material default=2 [2=Material, 1=Service]
  Excisable VarChar(1) Excisable [Yes/No] default=N [Y=Yes, N=No]
  ChapterID Int(11) Chapter ID default=-1 ->OCHP
  NotifyASN nVarChar(40) Notification Availed SN.
  ProAssNum nVarChar(20) Provisional Assessment No.
  AssblValue Num(19,6) Assessable Value
  DNFEntry Int(11) DNF Code Entry default=-1 ->ODNF
  UserSign2 Int(6) Updating User ->OUSR
  Spec nVarChar(30) Item Specification
  TaxCtg nVarChar(4) Tax Category
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  FuelCode Int(11) Fuel default=-1 ->OBFI
  BeverTblC nVarChar(2) Beverage Table ->OBSI
  BeverGrpC nVarChar(2) Beverage Group ->OBSI
  BeverTM Int(11) Beverage Brand default=-1 ->OBNI
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  ToleranDay Int(11) Tolerance Days
  UgpEntry Int(11) UoM Group ->OUGP
  PUoMEntry Int(11) Default Purchase UoM ->OUOM
  SUoMEntry Int(11) Default Sales UoM ->OUOM
  IUoMEntry Int(11) Inventory UoM ->OUOM
  IssuePriBy Int(6) Issue Primarily By SnB or Bin [0=Issue Primarily by Serial/Batch Number, 1=Issue Primarily by Bin Location]
  AssetClass nVarChar(20) Asset Class ->OACS
  AssetGroup nVarChar(15) Asset Group ->OAGS
  InventryNo nVarChar(12) Inventory Number of Asset
  Technician Int(11) Technician of Fixed Asset ->OHEM
  Employee Int(11) Employee of Fixed Asset ->OHEM
  Location Int(11) Location ->OLCT
  StatAsset VarChar(1) Owned by Company default=N [Y=Yes, N=No]
  Cession VarChar(1) Cession default=N [Y=Yes, N=No]
  DeacAftUL VarChar(1) Deactivate After Useful Life default=N [Y=Yes, N=No]
  AsstStatus VarChar(1) Asset Status default=N [N=New, A=Active, I=Inactive]
  CapDate Date(8) Capitalization Date
  AcqDate Date(8) Acquisition Date
  RetDate Date(8) Retirement Date
  GLPickMeth VarChar(1) G/L Account Pick Method default=A [A=General, W=Warehouse, C=Item Group]
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  MgrByQty VarChar(1) Manage Asset by Quantity default=N [Y=Yes, N=No]
  AssetRmk1 nVarChar(100) Asset Remark 1
  AssetRmk2 nVarChar(100) Asset Remark 2
  AssetAmnt1 Num(19,6) Asset Amount 1
  AssetAmnt2 Num(19,6) Asset Amount 2
  DeprGroup nVarChar(15) Depreciation Group ->OADG
  AssetSerNo nVarChar(32) Asset Serial Number
  CntUnitMsr nVarChar(100) Inventory Counting UoM Name
  NumInCnt Num(19,6) No. of Items per Counting Unit
  INUoMEntry Int(11) Inventory Counting UoM Entry ->OUOM
  OneBOneRec VarChar(1) One Batch One Receipt default=N [Y=Yes, N=No]
  RuleCode nVarChar(2) Checking Rule Code ->ODCR
  ScsCode nVarChar(10) SCS Code
  SpProdType nVarChar(2) Special Product Type [MT=Cellular Phones, IO=Integrated Circuits]
  IWeight1 Num(19,6) Weight 1 - Inventory
  IWght1Unit Int(6) Weight 1 - Inventory Unit
  IWeight2 Num(19,6) Weight 2 - Inventory
  IWght2Unit Int(6) Weight 2 - Inventory Unit
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VirtAstItm VarChar(1) Virtual Asset Item default=N [Y=Yes, N=No]
  SouVirAsst nVarChar(50) Source Virtual Asset Item ->OITM
  InCostRoll VarChar(1) Include in Prod. Cost Rollup default=Y [Y=Yes, N=No]
  PrdStdCst Num(19,6) Production Std Cost
  EnAstSeri VarChar(1) Enforce Asset Serial Numbers default=N [Y=Yes, N=No]
  LinkRsc nVarChar(50) Linked Resource ->ORSC
  OnHldPert Num(19,6) Capital Goods On Hold Percent
  onHldLimt Num(19,6) Capital Goods on Hold Limit
  PriceUnit Int(11) Pricing Unit ->OUOM
  GSTRelevnt VarChar(1) GST Relevant default=N [Y=Yes, N=No]
  SACEntry Int(11) SAC Entry default=-1 ->OSAC
  GstTaxCtg VarChar(1) GST Tax Category default=R [R=Regular, N=Nil Rated, E=Exempt]
  AssVal4WTR Num(19,6) Assessable Value for WTR
  ExcImpQUoM Int(11) Default Excise Imported Quantity UoM [112=Liters, m3, 168=Tonne, metric ton (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcFixAmnt Num(19,6) Default Excise Fixed Amount
  ExcRate Num(19,6) Default Excise Rate
  SOIExc VarChar(1) SOI Excisable default=4 [1=Excisable, 2=Exemption of excises, 3=Excises are paid to another authority, 4=Not Excisable]
  TNVED nVarChar(10) TNVED Code
  Imported VarChar(1) Imported Item default=N [Y=Yes, N=No]
  AutoBatch VarChar(1) Automatic Batches [Yes/No] default=N [Y=Yes, N=No]
  CstmActing VarChar(1) Customer Accounting default=N [N=No, Y=Yes]

# OITT - Product Tree
Module: Inventory and Production | 27 columns | ObjType: 66
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  PRICE_LIST: PriceList
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(50) Parent Item ->OITM
  TreeType VarChar(1) BOM Type default=P [A=Assembly, S=Sales, P=Production, T=Template]
  PriceList Int(6) Price List default=0 ->OPLN
  Qauntity Num(19,6) No. of Units
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SCNCounter Int(6) SCN Counter
  DispCurr nVarChar(3) Display Currency
  ToWH nVarChar(8) Whse for Finished Product
  Object nVarChar(20) Object Type default=66
  LogInstac Int(11) Log Instance - History
  UserSign2 Int(11) Updating User ->OUSR
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  HideComp VarChar(1) Hide Components in Printing default=N [Y=Yes, N=No]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  UpdateTime Int(11) Time of Update
  Project nVarChar(20) Project Code ->OPRJ
  PlAvgSize Num(19,6) Planned Average Production Size default=1
  Name nVarChar(100) Product Description
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateTS Int(11) Update Full Time

# OITW - Items - Warehouse
Module: Inventory and Production | 73 columns | ObjType: 31
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WhsCode, ItemCode
  WHS: WhsCode
  DFT_BIN: DftBinAbs
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Defined
  OnOrder Num(19,6) Ordered
  Consig Num(19,6) Consignment Goods Whse
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  MinStock Num(19,6) Minimum Inventory
  MaxStock Num(19,6) Maximum Inventory
  MinOrder Num(19,6) Min. Order
  AvgPrice Num(19,6) Average Price
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Transfer Acct ->OACT
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns Account ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Revenue Account - EU ->OACT
  EUExpensAc nVarChar(15) Expense Account - EU ->OACT
  FrRevenuAc nVarChar(15) Revenue Account - Foreign ->OACT
  FrExpensAc nVarChar(15) Expense Account - Foreign ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  PriceDifAc nVarChar(15) Price Differences Account
  ExchangeAc nVarChar(15) Exchange Rate Differences Account
  BalanceAcc nVarChar(15) Goods Clearing Account
  PurchaseAc nVarChar(15) Purchase Account
  PAReturnAc nVarChar(15) Purchase Return Account
  PurchOfsAc nVarChar(15) Purchase Offset Account
  ShpdGdsAct nVarChar(15) Shipped Goods Account
  VatRevAct nVarChar(15) VAT in Revenue Account
  StockValue Num(19,6) Inventory Value
  DecresGlAc nVarChar(15) G/L Decrease Account
  IncresGlAc nVarChar(15) G/L Increase Account
  StokRvlAct nVarChar(15) Stock Inflation Adjust Account
  StkOffsAct nVarChar(15) Stock Inflation Offset Account
  WipAcct nVarChar(15) WIP Inventory Account
  WipVarAcct nVarChar(15) WIP Inventory Variance Account
  CostRvlAct nVarChar(15) Cost Inflation Account
  CstOffsAct nVarChar(15) Cost Inflation Offset Account
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  Object nVarChar(20) Object Type - History default=31
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  ARCMAct nVarChar(15) Sales Credit Account
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign
  ARCMEUAct nVarChar(15) Sales Credit Account - EU
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account
  APCMAct nVarChar(15) Purchase Credit Account
  APCMFrnAct nVarChar(15) Purchase Credit Account - Foreign
  APCMEUAct nVarChar(15) Purchase Credit Account - EU
  RevRetAct nVarChar(15) Revenue Returns Account
  NegStckAct nVarChar(15) Negative Inventory Adj. Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account
  PurBalAct nVarChar(15) Purchase Balance Account
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  Freezed VarChar(1) Item Frozen in Warehouse default=N [Y=Yes, N=No]
  FreezeDoc Int(11) INC Document Frozen By ->OINC
  FreeChrgSA nVarChar(15) Free of Charge Sales Account ->OACT
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account ->OACT

# OIVE - FIFO Based Sales Return
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TRANS_SEQ: LayerID, TransSeq
  TreeID: TreeID
Fields (name type(len) description [values] ->parent table):
  TreeID Int(11) Tree ID default=0
  ParentID Int(11) Parent ID default=-1
  AbsEntry Int(11) Internal Number
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TransSeq Int(11) Transaction Sequence No. ->OIVL
  LayerID Int(11) Layer ID
  LayerInQty Num(19,6) Layer In Quantity
  LayerOutQ Num(19,6) Layer Out Quantity
  LayerVal Num(19,6) Layer Value
  ItemCode nVarChar(50) Item Code ->OITM
  EntryTreeI Int(11) Entry Tree ID
  LayerCogs Num(19,6) Layer - Cost of Goods Sold

# OIVK - IVL Vs OINM Keys
Module: Inventory and Production | 6 columns | ObjType: 10000062
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: INMTransSe
  TRANSSEQ U: LayerID, TransSeq
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No.
  LayerID Int(11) Layer ID
  RootID Int(11) Root ID
  TransNum Int(11) Transaction Number
  Instance Int(11) Instance default=0
  INMTransSe Int(11) INM_Transaction Sequence No.

# OIVL - Whse Journal
Module: Inventory and Production | 78 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TransSeq
  ITEM: ItemCode
  CURRENCY: Currency
  DOCDATE: DocDate
  DOCENTRY: DocLineNum, TransType, CreatedBy
  MESSAGEID: MessageID
  TREEID: TreeID
Fields (name type(len) description [values] ->parent table):
  TransType Int(11) Transaction Type default=-1 [15=Delivery, 16=Returns, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 18=A/P Invoice, 19=A/P Credit Memo, -2=Opening Balance, 58=Inventory Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfer, 68=Work Instructions, -1=All Transactions, 162=Inventory Revaluation, 69=Landed Costs, 310000001=Initial Quantity, 10000071=Inventory Posting]
  CreatedBy Int(11) Document Key Created
  BASE_REF nVarChar(11) Base Reference
  DocLineNum Int(11) Row Number in Document
  DocDate Date(8) Posting Date
  CreateTime Int(6) Generation Time
  ItemCode nVarChar(50) Item No. ->OITM
  InQty Num(19,6) Receipt Quantity
  OutQty Num(19,6) Issue Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  TrnsfrAct nVarChar(15) Transfer Account ->OACT
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  ReturnAct nVarChar(15) Returning Account ->OACT
  ExcRateAct nVarChar(15) Exchange Rate Differences Acct ->OACT
  ClearAct nVarChar(15) Goods Clearing Account ->OACT
  CostAct nVarChar(15) COGS Account ->OACT
  WipAct nVarChar(15) WIP Inventory Account ->OACT
  OpenStock Num(19,6) Open Sum Inventory Value
  CreateDate Date(8) Creation Date
  PriceDiff Num(19,6) Price Difference Value
  TransSeq Int(11) Transaction Sequence No. default=0
  InvntAct nVarChar(15) Inventory Account ->OACT
  SubLineNum Int(11) Subrow Number default=-1
  AppObjLine Int(11) Applied Object Line default=-1
  Expenses Num(19,6) Inventory Expenses
  OpenExp Num(19,6) Open Expenses Value
  Allocation Num(19,6) Allocation Amount
  OpenAlloc Num(19,6) Open Allocation Value
  ExpAlloc Num(19,6) Expenses Allocation Value
  OExpAlloc Num(19,6) Open Expenses Allocation Value
  OpenPDiff Num(19,6) Open Price Diff. Value
  ExchDiff Num(19,6) Exchange Rate Difference Value
  OpenEDiff Num(19,6) Open Exchange Rate Diff. Value
  NegInvAdjs Num(19,6) Negative Inventory Adjustment Value
  OpenNegInv Num(19,6) Open Negative Adjustment
  NegStckAct nVarChar(15) Negative Inventory Adj. Acct ->OACT
  BTransVal Num(19,6) Base Transaction Value
  VarVal Num(19,6) Variance Value
  BExpVal Num(19,6) Base Freight Value
  CogsVal Num(19,6) COGS Value
  BNegAVal Num(19,6) Base Negative Adjustment Amt
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  IOffIncVal Num(19,6) Inv. Offset Increase Value
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DOffDecVal Num(19,6) Inv. Offset Decrease Value
  DecAcc nVarChar(15) G/L Decrease Account ->OACT
  DecVal Num(19,6) G/L Decrease Value
  WipVal Num(19,6) WIP Inventory Value
  WipVarAcc nVarChar(15) WIP Variance Account ->OACT
  WipVarVal Num(19,6) WIP Variance Value
  IncAct nVarChar(15) G/L Increase Account
  IncVal Num(19,6) G/L Increase Value
  ExpCAcc nVarChar(15) Expense Clearing Account ->OACT
  CostMethod VarChar(1) Costing Method default=N [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch, N=None]
  MessageID Int(11) Message ID ->OILM
  LocType Int(11) Location Type
  LocCode nVarChar(8) Warehouse Code
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, Y=Year Transfer]
  PostStatus VarChar(1) Posting Status default=N [N=None, P=Partial, C=Complete]
  SumStock Num(19,6) Sum Stock Value
  OpenCogs Num(19,6) Open COGS Value
  OpenQty Num(19,6) Open Quantity
  TreeID Int(11) Tree ID default=-1
  ParentID Int(11) Parent ID default=-1
  PAOffAcc nVarChar(15) Purchase Offset Account ->OACT
  PAOffVal Num(19,6) Purchase Offset Value
  OpenPAOff Num(19,6) Open Purchase Offset Value
  PAAcc nVarChar(15) Purchase Account ->OACT
  PAVal Num(19,6) Purchase Account Value
  OpenPA Num(19,6) Open Purchase Value
  LinkArc VarChar(1) Linked To Archived Doc default=N [N=No, Y=Yes]
  VersionNum nVarChar(11) Version Number
  BSubLineNo Int(11) Base Subrow Number default=-1
  WipDebCred VarChar(1) WIP Account: Debit/Credit Side

# OIVQ - FIFO Queue Working Table
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TRANS_SEQ U: LayerID, TransSeq
  TreeOpenQt: OpenQty, TreeID
Fields (name type(len) description [values] ->parent table):
  TreeID Int(11) Tree ID default=0
  ParentID Int(11) Parent ID default=-1
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TransSeq Int(11) Transaction Sequence No. ->OIVL
  LayerID Int(11) Layer ID
  OpenQty Num(19,6) Open Quantity
  OpenValue Num(19,6) Open Value
  ItemCode nVarChar(50) Item Code ->OITM
  AbsEntry Int(11) Internal ID
  StockActio Int(11) Stock Action Type default=-1 [15=Delivery, 16=Returns, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 18=A/P Invoice, 19=A/P Credit Memo, -2=Opening Balance, 58=Inventory Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfer, 68=Work Instructions, -1=All Transactions, 162=Inventory Revaluation, 69=Landed Costs]
  RemMethod VarChar(1) Quantity Removal Method default=U [U=Unspecified, I=Issue, R=Revaluation]

# OIWB - Items - Warehouse Counting Data Backup
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: WhsCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs. Entry
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]

# OLCT - Location
Module: Inventory and Production | 51 columns | ObjType: 144
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  LOCATION U: Location
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Location Code
  Location nVarChar(100) Name
  UserSign Int(6) User Signature ->OUSR
  PanCirNo nVarChar(32) PAN Circle No.
  PanWardNo nVarChar(32) PAN Ward No.
  PanOfficer nVarChar(32) PAN Assessing Officer
  TanCirNo nVarChar(32) TAN Circle No.
  TanWardNo nVarChar(32) TAN Ward No.
  TanOfficer nVarChar(32) TAN Assessing Officer
  LstVatNo nVarChar(100) LST/VAT Number
  CstNo nVarChar(100) CST Number
  ExemptNo nVarChar(100) Exemption Number
  TanNo nVarChar(100) TAN Number
  ServTaxNo nVarChar(100) Service Tax Number
  AsseType nVarChar(100) Assessee Type
  CompType nVarChar(100) Company Type
  NatOfBiz nVarChar(100) Nature of Business
  TinNo nVarChar(100) TIN Number
  PanNo nVarChar(10) PAN Number
  RegType nVarChar(2) Registration Type [XM=XM, XD=XD, EM=EM, ED=ED, SD=SD]
  EccNo nVarChar(40) ECC Number
  CeRegNo nVarChar(40) CE Register Number
  CeRange nVarChar(60) CE Range
  CeDivision nVarChar(60) CE Division
  CeComRate nVarChar(60) CE Commissionerate
  ManuCode nVarChar(60) Manufaturer Code
  Jurisd nVarChar(60) Jurisdiction
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  Country nVarChar(3) Country ->OCRY
  State nVarChar(3) State
  Building Text(16) Building/Floor/Room
  SSIExmpt VarChar(1) SSI Exemption default=N [Y=Yes, N=No]
  SSIExmptSt VarChar(1) SSI Exemption Status default=E [E=New Location, N=Upgrade Not Changed, C=Upgrade Changed]
  CitAddress nVarChar(254) CIT Address
  CitCity nVarChar(100) CIT City
  CitPinCode nVarChar(10) CIT Pin Code
  OnHoldAct nVarChar(15) Capital Goods On Hold Account ->OACT
  GSTRegnNo nVarChar(15) GSTIN
  GSTRelevt nVarChar(2) GST Location Relevant default=N
  GSTTDS nVarChar(30) GSTIN TDS
  GSTISD nVarChar(30) GSTIN ISD
  GSTType Int(11) GST Type [-1=, 1=Regular/TDS/ISD, 2=Casual Taxable Person, 3=Composition Levy, 4=Government Department or PSU, 5=Non-Resident Taxable Person, 6=UN Agency or Embassy] ->OGTY
  VendorCode nVarChar(15) Vendor Code ->OCRD
  CstmerCode nVarChar(15) Customer Code ->OCRD
  DropShip nVarChar(8) Drop Ship Warehouse ->OWHS
  IngClrAc nVarChar(15) Ineligible ITC Clearing A/C
  IntBrClrAc nVarChar(15) Inter-branch ITC Clearing A/C

# OLGT - Length Units
Module: Inventory and Production | 8 columns | ObjType: 50
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UnitCode
  DISPLAY U: UnitDisply
  UNIT_NAME U: UnitName
  VOLUME: VolDisply
Fields (name type(len) description [values] ->parent table):
  UnitCode Int(6) Unit Code
  UnitDisply nVarChar(2) Unit Display
  UnitName nVarChar(20) Unit Name
  VolDisply nVarChar(3) Unit Code for Quantity Display
  SizeInMM Num(19,6) Unit Length in mm
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OMGP - Material Group
Module: Inventory and Production | 6 columns | ObjType: 256
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: MatGrp
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  MatGrp nVarChar(3) Material Group
  Descrip nVarChar(70) Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OMRC - Manufacturers
Module: Inventory and Production | 4 columns | ObjType: 43
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FirmCode
  GROUP_NAME U: FirmName
Fields (name type(len) description [values] ->parent table):
  FirmCode Int(6) Code
  FirmName nVarChar(30) Manufacturer Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OMRL - Advanced Inventory Revaluation
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM U: Segment, Instance, DocNum
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series default=0
  DocDate Date(8) Posting Date
  RevalType VarChar(1) Inventory Valuation Type default=P [P=Price Change, M=Inventory Debit/Credit]
  Handwrtten VarChar(1) Manual Numbering default=N
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  DocCur nVarChar(3) Document Currency
  DocRate Num(19,6) Document Rate
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  DocTime Int(6) Generation Time
  Confirmed VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  StampNum nVarChar(16) Stamp No.
  FinncPriod Int(11) Posting Period ->OFPR
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  LogInstanc Int(11) Log Instance default=0
  StationID Int(11) Workstation ID ->CSTN
  Rounding VarChar(1) Rounding default=N [Y=Yes, N=No]
  Segment Int(6) Segment default=0
  ReqDate Date(8) Required Date
  CancelDate Date(8) Cancelation Date
  Project nVarChar(20) Project Code ->OPRJ

# OMRV - Inventory Revaluation
Module: Inventory and Production | 32 columns | ObjType: 162
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM: DocNum
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocDate Date(8) Posting Date
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  DocTime Int(6) Generation Time
  RevalType VarChar(1) Inventory Valuation Type default=P [P=Price Change, M=Inventory Debit/Credit]
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Series Int(11) Series ->NNM1
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  StationID Int(11) Workstation ID ->CSTN
  RIncmAcct nVarChar(15) Invent. Reval. Expense Account
  RExpnAcct nVarChar(15) Invent. Reval. Expense Account
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=162
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  VersionNum nVarChar(11) Version Number
  InflaReval VarChar(1) Inflation-Based Revaluation default=N [Y=Yes, N=No]
  SupplCode nVarChar(254) Supplementary Code
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  CardName nVarChar(100) Customer/Vendor Name
  CreatedBy VarChar(1) Entry Creation Origin default=M [M=Created Manually by User, W=Created by Production Cost Recalculation Wizard]

# OOFR - Defect Cause
Module: Inventory and Production | 4 columns | ObjType: 102
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Num
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Description
  SortOrder Int(6) Sort default=100
  UserSign Int(6) User Signature ->OUSR

# OOIN - Interest
Module: Inventory and Production | 4 columns | ObjType: 98
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Num
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Description
  SortOrder Int(6) Sort default=100
  UserSign Int(6) User Signature ->OUSR

# OOIR - Interest Level
Module: Inventory and Production | 4 columns | ObjType: 99
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Num
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Description
  SortOrder Int(6) Sort default=100
  UserSign Int(6) User Signature ->OUSR

# OOSR - Information Source
Module: Inventory and Production | 4 columns | ObjType: 100
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Num
Fields (name type(len) description [values] ->parent table):
  Num Int(11) Sequence No.
  Descript nVarChar(30) Description
  SortOrder Int(6) Sort
  UserSign Int(6) User Signature ->OUSR

# OPKG - Package Types
Module: Inventory and Production | 20 columns | ObjType: 205
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PkgCode
  TYPE U: PkgType
Fields (name type(len) description [values] ->parent table):
  PkgCode Int(11) Code
  PkgType nVarChar(30) Type
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  WghtUnit Int(6) Weight UoM
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2

# OPKL - Pick List
Module: Inventory and Production | 17 columns | ObjType: 156
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry
  Name nVarChar(155) Name
  OwnerCode Int(6) Owner Code ->OUSR
  OwnerName nVarChar(155) Owner Name
  PickDate Date(8) Pick Date
  Remarks Text(16) Remarks
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  ShipType Int(6) Shipping Type
  Status VarChar(1) Status default=R [R=Released, Y=Picked, P=Partially Picked, D=Partially Delivered, C=Closed]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original, =]
  LogInstac Int(11) Log Instance - History
  ObjType nVarChar(20) Object Type default=156 ->ADP1
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  UseBaseUn VarChar(1) Inventory UoM default=N [Y=Yes, N=No]

# OPLN - Price Lists
Module: Inventory and Production | 24 columns | ObjType: 6
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ListNum
  LIST_NAME U: ListName
Fields (name type(len) description [values] ->parent table):
  ListNum Int(6) Price List No.
  ListName nVarChar(32) Price List Name
  BASE_NUM Int(6) Base Price List ->OPLN
  Factor Num(19,6) Factor
  RoundSys Int(6) Rounding Method default=0 [0=No Rounding, 1=Round to Full Decimal Amount, 2=Round to Full Amount, 3=Round to Full Tens Amount, 4=Fixed Ending, 5=Fixed Interval]
  GroupCode Int(6) Group No. default=1 [1=Group 1, 2=Group 2, 3=Group 3, 4=Group 4]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SPPCounter Int(11) SPP Counter
  UserSign Int(6) User Signature ->OUSR
  IsGrossPrc VarChar(1) Gross Price? default=N [Y=Gross, N=Net]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  ValidFor VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidFrom Date(8) Active From
  ValidTo Date(8) Active To
  CreateDate Date(8) Creation Date
  PrimCurr nVarChar(3) Primary Default Currency
  AddCurr1 nVarChar(3) Additional Default Currency 1
  AddCurr2 nVarChar(3) Additional Default Currency 2
  RoundRule VarChar(1) Rounding Rule default=R [R=Round to Closest, C=Round Up, F=Round Down]
  ExtAmount Num(19,6) Fixed Amount (Ending/Interval)
  RndFrmtInt nVarChar(10) Ending/Interval - Integer Part
  RndFrmtDec nVarChar(10) Ending/Interval - Decimal Part

# OPSC - Product Source Code
Module: Inventory and Production | 3 columns | ObjType: 1320000039
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Source Code
  Desc nVarChar(100) Description
  GroupCode Int(6) Group Code ->OPSG

# ORCN - Retail Chains
Module: Inventory and Production | 11 columns | ObjType: 79
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChainCode
  NAME U: ChainName
Fields (name type(len) description [values] ->parent table):
  ChainCode Int(11) Internal Number
  ChainName nVarChar(20) Chain Name
  SuppNum nVarChar(20) Vendor Code
  SuppName nVarChar(20) Vendor Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  SavePath Text(16) File Path
  UsePartSup VarChar(1) Use Goods Del. default=N [Y=Yes, N=No]
  BaseCode Int(11) Basic Grid Template default=-1
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ExportNum Int(11) Export Counter default=0
  UserSign Int(6) User Signature ->OUSR

# ORTL - Resource Transaction Log
Module: Inventory and Production | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Entry ID
  ResCode nVarChar(50) Resource Code ->ORSC
  DocType Int(11) Transact. Type
  DocEntry Int(11) Document Internal ID
  DocLine Int(11) Doc. Row Number
  BaseType Int(11) Base Document Type
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row Number
  ActionType Int(11) Action Type default=0 [0=RESOURCE_TRANSACTION_UNKNOWN, 1=RESOURCE_TRANSACTION_IN, 2=RESOURCE_TRANSACTION_OUT]
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  VersionNum nVarChar(11) Version Number
  PostDate Date(8) Posting Date
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  DocQty Num(19,6) Doc. Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  OpenQty Num(19,6) Open Quantity
  DocNum nVarChar(11) Document Number
  BaseDocNum nVarChar(11) Base Document Number
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry
  StgDesc nVarChar(100) Stage Description

# OSAC - India SAC Code
Module: Inventory and Production | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SERVCODE U: ServCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  ServName nVarChar(254) Service Name
  ServCode nVarChar(8) Service Code

# OSBQ - Item - Serial/Batch - Bin Accumulator
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: BinAbs, SnBMDAbs
  BIN_ABS: BinAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item Code ->OITM
  SnBMDAbs Int(11) Serial MD Internal Number ->OSRN
  BinAbs Int(11) Bin Internal Number ->OBIN
  OnHandQty Num(19,6) On-Hand Quantity
  WhsCode nVarChar(8) Warehouse Code ->OWHS

# OSCG - Service Category
Module: Inventory and Production | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: ServiceCtg
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  ServiceCtg nVarChar(60) Service Category
  Descrip nVarChar(120) Description

# OSPG - Special Prices for Groups
Module: Inventory and Production | 6 columns | ObjType: 85
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjKey, ObjType, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  ObjType nVarChar(20) Object Type [52=Item Group, 8=Item Properties, 43=Companies]
  ObjKey nVarChar(50) Object Key
  Discount Num(19,6) Discount
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Form ->OUSR

# OSPP - Special Prices
Module: Inventory and Production | 17 columns | ObjType: 7
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItemCode, CardCode
  CARD: CardCode
  ITEM: ItemCode
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount in %
  ListNum Int(6) Price List No. default=0 ->OPLN
  AutoUpdt VarChar(1) Auto Update default=Y [Y=Yes, N=No]
  EXPAND VarChar(1) Item Details default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  SrcPrice Int(6) Source Price default=0 [0=Price - Pri. Curr., 1=Price - Add. Curr. 1, 2=Price - Add. Curr. 2]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Update Date
  Valid VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidFrom Date(8) Active From
  ValidTo Date(8) Active To

# OSRN - Serial Numbers Master Data
Module: Inventory and Production | 32 columns | ObjType: 10000045
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: SysNumber, ItemCode
  DIST_KEY: DistNumber, ItemCode
  LOT_KEY: LotNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Serial Number
  MnfSerial nVarChar(36) Manufacturer Serial No.
  LotNumber nVarChar(36) Lot Number
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Mfr Warranty Start Date
  GrntExp Date(8) Mfr Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Location
  Status VarChar(1) Status [0=Available, 1=Unavailable, 2=Allocated]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  ObjType nVarChar(20) object type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

# OSRQ - Serial No. Quantities
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: WhsCode, SysNumber, ItemCode
  MDABS_KEY: MdAbsEntry
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number ->OSRN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  CommitQty Num(19,6) Committed Quantity
  CountQty Num(19,6) Counted Quantity
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry ->OSRN
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  CCDQuant Num(19,6) CCD Quantity

# OSRW - Serial No. Attribs in Location
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: WhsCode, SysNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number ->OSRN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Location nVarChar(100) Location
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) abs entry
  MdAbsEntry Int(11) MD Abs Entry ->OSRN
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OSTQ - Inventory Valuation Utility Queries
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  QueryNAme nVarChar(100) Query Name
  QueryStr Text(16) Query String
  Severity VarChar(1) Inventory Valuation Query Seve default=E [W=Warning if fails, E=Error if fails]
  QueryGroup VarChar(1) Query Group default=B [B=Before Recalculation, A=After Recalculation, T=Year Transfer]

# OTNL - CCD Log
Module: Inventory and Production | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TrNtAbsEnt Int(11) Tracking Note Internal Number ->OTCN
  TrNtLineNo Int(11) Tracking Note Row Number ->TCN1
  Quantity Num(19,6) Quantity
  WhsCode nVarChar(8) Warehouse Code
  DocEntry Int(11) Doc Abs Entry
  DocNum Int(11) Doc Number
  DocType Int(11) Transaction Type default=-1
  DocLineNum Int(11) Doc Line Number
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseLnNum Int(11) Base Document Line No.
  ActionType Int(11) Action Type default=5 [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]
  CCDNum nVarChar(40) CCD Number
  ItemCode nVarChar(50) Item Code
  DirectImp VarChar(1) Direct Import default=N [Y=Yes, N=No]
  CntrOrigin nVarChar(3) Country of Origin
  AccQty Num(19,6) Quantity-In Accumulator
  AccNegQ Num(19,6) Quantity-Out Accumulator
  AccRelQty Num(19,6) Reallocation Quantity Accumulator
  CCDQty Num(19,6) CCD Quantity
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Generation Time
  OnHandQty Num(19,6) Warehouse On Hand Quantity
  OILMEntry Int(11) OILM Abs Entry ->OILM

# OTSP - Transporters
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TRANS_CODE U: TransCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transporter Abs. Entry
  TransCode nVarChar(20) Transporter Code
  TransName nVarChar(25) Transporter Name
  TransID nVarChar(15) Transporter ID
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]

# OUGP - UoM Group
Module: Inventory and Production | 11 columns | ObjType: 10000197
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UgpEntry
  CODE U: UgpCode
  NAME: UgpName
Fields (name type(len) description [values] ->parent table):
  UgpEntry Int(11) UoM Group Abs. Entry
  UgpCode nVarChar(20) UoM Group Code
  UgpName nVarChar(100) UoM Group Name
  BaseUom Int(11) Base UoM Abs. Entry ->OUOM
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]

# OUOM - UoM Master Data
Module: Inventory and Production | 30 columns | ObjType: 10000199
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UomEntry
  CODE U: UomCode
  NAME: UomName
Fields (name type(len) description [values] ->parent table):
  UomEntry Int(11) UoM Abs. Entry
  UomCode nVarChar(20) UoM Code
  UomName nVarChar(100) UoM Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(6) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  WghtUnit Int(6) Weight UoM
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  IntSymbol nVarChar(20) International Symbol
  EwbUnit Int(11) EWB Unit ->OEUT

# OWGT - Weight Units
Module: Inventory and Production | 7 columns | ObjType: 51
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UnitCode
  DISPLAY U: UnitDisply
  UNIT_NAME U: UnitName
Fields (name type(len) description [values] ->parent table):
  UnitCode Int(6) Unit Code
  UnitDisply nVarChar(2) Unit Display
  UnitName nVarChar(20) Unit Name
  WightInMG Num(19,6) Unit Weight in mg
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OWHS - Warehouses
Module: Inventory and Production | 102 columns | ObjType: 64
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WhsCode
  DFT_BIN: DftBinAbs
Fields (name type(len) description [values] ->parent table):
  WhsCode nVarChar(8) Warehouse Code
  WhsName nVarChar(100) Warehouse Name
  IntrnalKey Int(11) Internal Key
  Grp_Code nVarChar(4) Group Code
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Allocation Account ->OACT
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns Account ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Revenue Account - EU ->OACT
  EUExpensAc nVarChar(15) Expense Account - EU ->OACT
  FrRevenuAc nVarChar(15) Revenue Account - Foreign ->OACT
  FrExpensAc nVarChar(15) Expense Account - Foreign ->OACT
  VatGroup nVarChar(8) Tax Group ->OSTC
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County ->OCNT
  Country nVarChar(3) Country ->OCRY
  State nVarChar(3) State ->OCST
  Location Int(11) Location ->OLCT
  DropShip VarChar(1) Drop-Ship default=N [N=No, Y=Yes]
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  UseTax VarChar(1) Allow Use Tax default=N [Y=Yes, N=No]
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  ExchangeAc nVarChar(15) Exchange Rate Differences Account ->OACT
  BalanceAcc nVarChar(15) Goods Clearing Account ->OACT
  PurchaseAc nVarChar(15) Purchase Account ->OACT
  PAReturnAc nVarChar(15) Purchase Return Account ->OACT
  PurchOfsAc nVarChar(15) Purchase Offset Account ->OACT
  FedTaxID nVarChar(32) Federal Tax ID
  Building Text(16) Building/Floor/Room
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  Nettable VarChar(1) Nettable default=Y [Y=Yes, N=No]
  StokRvlAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkOffsAct nVarChar(15) Inventory Revaluation Offset Account ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  CostRvlAct nVarChar(15) COGS Revaluation Account ->OACT
  CstOffsAct nVarChar(15) COGS Revaluation Offset Acct ->OACT
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  objType nVarChar(20) Object Type - History default=64
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  ARCMAct nVarChar(15) Sales Credit Account ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign ->OACT
  ARCMEUAct nVarChar(15) Sales Credit Account - EU ->OACT
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account ->OACT
  APCMAct nVarChar(15) Purchase Credit Account ->OACT
  APCMFrnAct nVarChar(15) Purchase Credit Account - Foreign ->OACT
  APCMEUAct nVarChar(15) Purchase Credit Account - EU ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account ->OACT
  BPLid Int(11) Business Place ID ->OBPL
  OwnerCode VarChar(1) Owner Code default=1 [1=Company Item Property, 2=Third-Party Warehouse, 3=Third-Party Item in my Property]
  NegStckAct nVarChar(15) Negative Inventory Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account ->OACT
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  Excisable VarChar(1) Excisable [Yes/No] default=N [Y=Yes, N=No]
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WhShipTo nVarChar(100) Ship-to Name (WH)
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  StorKeeper Int(11) Storekeeper ->OHEM
  Shipper nVarChar(15) Shipper ->OCRD
  BinActivat VarChar(1) Bin Activated [Y/N] default=N [Y=Yes, N=No]
  BinSeptor nVarChar(5) Bin Separator default=-
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  AutoIssMtd Int(6) Auto. Issue Method default=0 [0=Single Choice, 1=Bin Location Code Order, 2=Alternative Sort Code Order, 3=Descending Quantity, 4=Ascending Quantity, 7=Ascending Quantity - Single Bin Preferred, 5=FIFO, 6=LIFO]
  ManageSnB VarChar(1) Drop-Ship Manage SnB default=N [N=No, Y=Yes]
  RecItemsBy Int(6) Receiving Bin Locations Method default=0 [0=Bin Location Code Order, 1=Alternative Sort Code Order]
  RecBinEnab VarChar(1) Enable Receiving Bin Locations default=N [Y=Yes, N=No]
  GlblLocNum nVarChar(50) Global Location Number
  RecvEmpBin VarChar(1) Restrict Receipts to Empty Bin default=Y [Y=Yes, N=No]
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  RecvMaxQty VarChar(1) Recv. up to Max. Qty default=N [Y=Yes, N=No]
  AutoRecvMd Int(6) Auto. Receipt Method default=0 [0=Default Bin Location, 1=Last Bin Location That Received Item, 2=Item's Current Bin Locations, 3=Item's Current and Historical Bin Locations]
  RecvMaxWT VarChar(1) Recv. up to Max. Weight default=N [Y=Yes, N=No]
  RecvUpTo nVarChar(6) Receive up to default=0 [0=Maximum Qty, 1=Maximum Weight, 2=Max. Qty and Weight]
  FreeChrgSA nVarChar(15) Free of Charge Sales Account ->OACT
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account ->OACT
  TaxOffice nVarChar(50) Tax Office
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  External VarChar(1) External default=N [N=No, Y=Yes]

# OWKO - Production Instructions
Module: Inventory and Production | 31 columns | ObjType: 68
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: OrderNum
  SERIAL U: Instance, SerialNum
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  OrderNum Int(11) Instruction Key default=0
  Status VarChar(1) Processing Status default=O [O=Work Instructions, I=Work Instructions, E=Production Completed]
  Canceled VarChar(1) Order Canceled Yes/No default=N [Y=Canceled, N=Not Canceled]
  OrderDate Date(8) Order Date
  ProdctDate Date(8) Work Start Date
  ExpFinishD Date(8) Expected Completion Date
  FinishDate Date(8) Work Finish Date
  FinishUser nVarChar(8) Name of Person Receiving Instructions ->OUSR
  CardCode nVarChar(15) Sold-to Party Code ->OCRD
  CustomName nVarChar(100) Sold-to Party Name
  NumInCustm nVarChar(16) Customer Ref. No.
  TotalOrder Num(19,6) Order Total
  TotalCurr nVarChar(3) Total Currency
  DocTime Int(6) Generation Time
  Memo nVarChar(254) Remarks
  SerialNum Int(11) Instruction Number
  CntctCode Int(11) Contact Person default=0 ->OCPR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  Series Int(11) Series ->NNM1
  ActWorkCod nVarChar(15) Active Account Code ->OACT
  ActWorkSum Num(19,6) Work Total
  JrnlMemo nVarChar(50) Journal Remarks
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ObjType nVarChar(20) Object Type default=68 ->ADP1
  UserSign Int(6) User Signature ->OUSR
  PriceList Int(6) Price List default=1 ->OPLN
  FinncPriod Int(11) Posting Period ->OFPR
  SysRate Num(19,6) System Rate

# OWOR - Production Order
Module: Inventory and Production | 57 columns | ObjType: 202
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM U: PIndicator, DocNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series default=0 ->NNM1
  ItemCode nVarChar(50) Product No. ->OITT
  Status VarChar(1) Production Order Status default=P [P=Planned, R=Released, L=Closed, C=Canceled]
  Type VarChar(1) Production Order Type default=S [S=Standard, P=Special, D=Disassembly]
  PlannedQty Num(19,6) Planned Quantity - Header
  CmpltQty Num(19,6) Completed Quantity
  RjctQty Num(19,6) Rejected Quantity
  PostDate Date(8) Order Date
  DueDate Date(8) Due Date
  OriginAbs Int(11) Production Order Origin Entry
  OriginNum Int(11) Production Order Origin Number
  OriginType VarChar(1) Production Order Origin default=M [M=Manual, R=MRP, S=Sales Order, U=Upgrade]
  UserSign Int(6) User Signature ->OUSR
  Comments nVarChar(254) Remarks
  CloseDate Date(8) Closing Date
  RlsDate Date(8) Release Date
  CardCode nVarChar(15) Customer Code ->OCRD
  Warehouse nVarChar(8) Warehouse ->OWHS
  Uom nVarChar(100) Inv. UoM in Production Order
  LineDirty Int(11) Line Modified
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  CreateDate Date(8) Creation Date
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  PIndicator nVarChar(10) Period Indicator ->OPID
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  Project nVarChar(20) Project Code ->OPRJ
  SupplCode nVarChar(254) Supplementary Code
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  PickRmrk nVarChar(254) Pick Remarks
  SysCloseDt Date(8) System Closing Date
  SysCloseTm Int(6) System Closing Time
  CloseVerNm nVarChar(11) Closing Version Number
  StartDate Date(8) Start Date
  ObjType nVarChar(20) Object Type default=202
  ProdName nVarChar(100) Product Description
  Priority Int(6) Priority default=100
  RouDatCalc VarChar(1) Routing Date Calculation default=S [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  UpdAlloc VarChar(1) Update Allocation default=M [M=Manual, C=Calculated, R=Run Calculation]
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VersionNum nVarChar(11) Version Number
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SAPPassprt Text(16) Extended SAP Passport

# OWTC - WTax Certificates
Module: Inventory and Production | 19 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RctType nVarChar(20) Object Type [24=Incoming Payment, 46=Outgoing Payment]
  RctAbs Int(11) Receipt No.
  Jurisdict nVarChar(2) Jurisdiction
  WtaxType nVarChar(2) WTax Type [--=WTax Certificate, OV=Outgoing VAT - Withholding Tax, OG=Outgoing Gross Income - Withholding Tax, ON=Outgoing Income - Withholding Tax, OS=Outgoing Social Security - Withholding Tax, OI=Outgoing Industry Specific - Withholding Tax, OD=Outgoing District Specific - Withholding Tax, IC=Incoming WTax Certificate]
  WtAbsEntry Int(11) Internal Number
  DueDate Date(8) Due Date
  CerSeries Int(11) WTax Certificate Series
  Number Int(11) Number
  RefNumber nVarChar(20) Reference Number
  SumVatAmnt Num(19,6) Sum of VAT Amount
  SumDocTot Num(19,6) Sum of Doc. Total Amount
  SumBaseAmn Num(19,6) Sum of Base Amount
  SumAccumAm Num(19,6) Sum of Accumulated Amount
  SumPercpAm Num(19,6) Sum of Perception Amount
  PTICode nVarChar(5) POI Code
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator
  PTICodeRef nVarChar(20) POI Code Reference

# OWTQ - Inventory Transfer Request
Module: Inventory and Production | 424 columns | ObjType: 1250000001
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  AT_CARD: CardCode, NumAtCard
  CUSTOMER: CardCode
  NUM U: PIndicator, DocSubType, Segment, Instance, DocNum
  DOC_STATUS: CANCELED, DocStatus
  FTHR_CARD: FatherType, FatherCard
  SERIES: Series
  OWNER_CODE: OwnerCode
  DATE_PIND: PIndicator, DocDate
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No]
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original, A=Amended]
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Closed]
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=1250000001 [1250000001=Inventory Transfer Request] ->ADP1
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  CardName nVarChar(100) Customer/Vendor Name
  Address nVarChar(254) Bill to
  NumAtCard nVarChar(100) BP Reference No.
  VatPercent Num(19,6) Tax Rate
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  DiscPrcnt Num(19,6) Discount % for Document
  DiscSum Num(19,6) Total Discount
  DiscSumFC Num(19,6) Total Discount (FC)
  DocCur nVarChar(3) Document Currency ->OCRN
  DocRate Num(19,6) Document Rate
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  GrosProfit Num(19,6) Gross Profit
  GrosProfFC Num(19,6) Gross Profit (FC)
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number
  ReceiptNum Int(11) Receipt Number
  GroupNum Int(6) Payment Terms Code ->OCTG
  DocTime Int(6) Generation Time
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TrnspCode Int(6) Shipping Type default=-1 ->OSHP
  PartSupply VarChar(1) Partial Delivery default=Y [Y=Yes, N=No]
  Confirmed VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  GrossBase Int(6) Price List for Gross Profit default=0
  ImportEnt Int(11) Order Number
  CreateTran VarChar(1) Create Journal Entry default=N [Y=Yes, N=No]
  SummryType VarChar(1) Summary Method default=N [N=No Summary, I=By Items, D=By Documents]
  UpdInvnt VarChar(1) Whse Update default=N [N=No, O=Orders from Vendors, C=Customer Orders, G=Consignment, I=Stock]
  UpdCardBal VarChar(1) Update Balances default=N [N=No, O=Orders, D=Delivery Notes, B=Bookkeeping]
  Instance Int(6) Instance default=0
  Flags Int(11) Flags default=0
  InvntDirec VarChar(1) Warehouse Direction default=X [X=Release, E=Receipt]
  CntctCode Int(11) Contact Person ->OCPR
  ShowSCN VarChar(1) Display BP Catalog Number default=N [Y=Yes, N=No]
  FatherCard nVarChar(15) BP Consolidation ->OCRD
  SysRate Num(19,6) System Price
  CurSource VarChar(1) Base Currency default=C [L=Local Currency, S=System Currency, C=BP Currency]
  VatSumSy Num(19,6) Tax Amount (SC)
  DiscSumSy Num(19,6) Total Discount (SC)
  DocTotalSy Num(19,6) Document Total (SC)
  PaidSys Num(19,6) Paid (SC)
  FatherType VarChar(1) Parent Summary Type default=P [P=Payment Consolidation, D=Delivery Consolidation]
  GrosProfSy Num(19,6) Gross Profit (SC)
  UpdateDate Date(8) Date of Update
  IsICT VarChar(1) A/R Invoice + Payment default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight Num(19,6) Weight
  WeightUnit Int(6) Weight UoM
  Series Int(11) Series ->NNM1
  TaxDate Date(8) Document Date
  Filler nVarChar(8) Filter ->OWHS
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  StampNum nVarChar(16) Stamp No.
  isCrin VarChar(1) Correction Invoice default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  UserSign Int(6) User Signature ->OUSR
  selfInv VarChar(1) Autom. Invoice default=N [N=No, Y=Yes]
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  UserSign2 Int(6) Updating User ->OUSR
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  draftKey Int(11) Document Draft Internal ID default=-1 ->ODRF
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  DunnLevel Int(11) Dunning Level ->ODUN
  Address2 nVarChar(254) Ship To
  LogInstanc Int(11) Log Instance default=0
  Exported VarChar(1) Exported default=N [Y=Yes, N=No]
  StationID Int(11) Workstation ID ->CSTN
  Indicator nVarChar(2) Indicator ->OIDC
  NetProc VarChar(1) Net Procedure default=N [Y=Yes, N=No]
  AqcsTax Num(19,6) Acquisition Tax
  AqcsTaxFC Num(19,6) Acquisition Tax (FC)
  AqcsTaxSC Num(19,6) Acquisition Tax (SC)
  CashDiscPr Num(19,6) Cash Discount Percentage
  CashDiscnt Num(19,6) Cash Discount
  CashDiscFC Num(19,6) Cash Discount (FC)
  CashDiscSC Num(19,6) Cash Discount (SC)
  ShipToCode nVarChar(50) Ship-to Code
  LicTradNum nVarChar(32) Licensed Dealer No.
  PaymentRef nVarChar(27) Payment Reference No.
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  RoundDif Num(19,6) Rounding Diff. Amount
  RoundDifFC Num(19,6) Rounding Diff. Amount (FC)
  RoundDifSy Num(19,6) Rounding Diff. Amount (SC)
  CheckDigit VarChar(1) Control Digit
  Form1099 Int(11) 1099 Form ->OTNN
  Box1099 nVarChar(20) 1099 Box
  submitted VarChar(1) Submitted default=N [Y=Yes, N=No]
  PoPrss VarChar(1) PO Process default=N [Y=Yes, N=No]
  Rounding VarChar(1) Rounding default=N [Y=Yes, N=No]
  RevisionPo VarChar(1) Split Purchase Order default=N [Y=Yes, N=No]
  Segment Int(6) Segment default=0
  ReqDate Date(8) Required Date
  CancelDate Date(8) Cancelation Date
  PickStatus VarChar(1) Pick Status default=N [Y=Yes, N=No]
  Pick VarChar(1) Pick default=N [Y=Yes, N=No]
  BlockDunn VarChar(1) Block Dunning default=N [Y=Yes, N=No]
  PeyMethod nVarChar(15) Payment Method ->OPYM
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  MaxDscn VarChar(1) Maximum Discount default=N [Y=Yes, N=No]
  Reserve VarChar(1) Reserve default=N [Y=Yes, N=No]
  Max1099 Num(19,6) Max. 1099 Amount
  CntrlBnk nVarChar(15) Central Bank Indicator ->OCBI
  PickRmrk nVarChar(254) Pick Remarks
  ISRCodLine nVarChar(53) ISR Coding Line
  ExpAppl Num(19,6) Expenses Applied
  ExpApplFC Num(19,6) Expenses Applied (FC)
  ExpApplSC Num(19,6) Expenses Applied (SC)
  Project nVarChar(20) Project Code ->OPRJ
  DeferrTax VarChar(1) Deferred Tax [Y=Yes, N=No]
  LetterNum nVarChar(20) Tax Exemption Letter No.
  FromDate Date(8) Exemption Validity Date From
  ToDate Date(8) Exemption Validity Date To
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  BoeReserev VarChar(1) Bill of Exchange Reserved default=N [Y=Yes, N=No]
  AgentCode nVarChar(32) Agent Code ->OAGP
  WTAppliedS Num(19,6) Applied WTax (SC)
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  Installmnt Int(6) No. of Installments default=1
  VATFirst VarChar(1) Apply Tax on 1st Installment [Y=Yes, N=No]
  NnSbAmnt Num(19,6) WTax Non-Subject Amount
  NnSbAmntSC Num(19,6) WTax Non-Subject Amount (SC)
  NbSbAmntFC Num(19,6) WTax Non-Subject Amount (FC)
  ExepAmnt Num(19,6) Withholding Tax Exempt Amount
  ExepAmntSC Num(19,6) WTax Exempt Amount (SC)
  ExepAmntFC Num(19,6) WTax Exempt Amount (FC)
  VatDate Date(8) Document Date
  CorrExt nVarChar(25) External Corrected Document No.
  CorrInv Int(11) Internal Corrected Document No.
  NCorrInv Int(11) Next Correcting Document
  CEECFlag VarChar(1) Block Creation of Tgt Corr Doc default=N [N=No, Y=Yes]
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  CtlAccount nVarChar(15) Control Account ->OACT
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number
  TxInvRptNo nVarChar(10) Tax Invoice Rpt Number
  TxInvRptDt Date(8) Tax Invoice Rpt Date
  KVVATCode Text(16) VAT Code for Tax Invoice Rpt
  WTDetails nVarChar(100) Withholding Tax Details
  SumAbsId Int(11) Summary VAT Abstract ID default=-1
  SumRptDate Date(8) Summary VAT Report Date
  PIndicator nVarChar(10) Period Indicator ->OPID
  ManualNum nVarChar(20) Manual Number
  UseShpdGd VarChar(1) Use Shipped Goods Account default=N [N=No, Y=Yes]
  BaseVtAt Num(19,6) BPL ID Assigned to Invoice
  BaseVtAtSC Num(19,6) BPL Name
  BaseVtAtFC Num(19,6) Tax Reg. Number
  NnSbVAt Num(19,6) Tax Invoice Rpt Number
  NnSbVAtSC Num(19,6) Tax Invoice Rpt Date
  NbSbVAtFC Num(19,6) WTax Non-Subject VAT Amt (FC)
  ExptVAt Num(19,6) WTax Exempt VAT Amount
  ExptVAtSC Num(19,6) WTax Exempt VAT Amount (SC)
  ExptVAtFC Num(19,6) WTax Exempt VAT Amount (FC)
  LYPmtAt Num(19,6) Last Year's Payments
  LYPmtAtSC Num(19,6) Last Years Payments (SC)
  LYPmtAtFC Num(19,6) Summary Tax Report Date
  ExpAnSum Num(19,6) Period Indicator
  ExpAnSys Num(19,6) Manual Number
  ExpAnFrgn Num(19,6) Use Shipped Goods Account
  DocSubType nVarChar(2) Document Subtype default=-- [--=Inventory Transfer Request]
  DpmStatus VarChar(1) Summary VAT Abstract ID default=O [O=Open, C=Closed]
  DpmAmnt Num(19,6) Down Payment Amount LC
  DpmAmntSC Num(19,6) Down Payment Amount SC
  DpmAmntFC Num(19,6) Down Payment Amount FC
  DpmDrawn VarChar(1) Drawn to Down Payment default=N [N=No, Y=Yes]
  DpmPrcnt Num(19,6) Down Payment Percent
  PaidSum Num(19,6) Total Paid Sum
  PaidSumFc Num(19,6) Total Paid Sum (FC)
  PaidSumSc Num(19,6) Total Paid Sum (SC)
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  DpmAppl Num(19,6) Down Payment Applied LC
  DpmApplFc Num(19,6) Down Payment Applied FC
  DpmApplSc Num(19,6) Down Payment Applied SC
  LPgFolioN Int(11) Folio No. for Last Page in Doc.
  Header Text(16) Header
  Footer Text(16) Footer
  Posted VarChar(1) Down Payment Was Posted default=Y [Y=Yes, N=No]
  OwnerCode Int(11) Document Owner ->OHEM
  BPChCode nVarChar(15) BP Channel Code ->OCRD
  BPChCntc Int(11) BP Channel Contact Person ->OCPR
  PayToCode nVarChar(50) Pay To
  IsPaytoBnk VarChar(1) Is Pay-To Bank [N=No, Y=Yes]
  BnkCntry nVarChar(3) Pay-To Bank Country ->OCRY
  BankCode nVarChar(30) Pay-To Bank Code
  BnkAccount nVarChar(50) Pay-To Bank Account No.
  BnkBranch nVarChar(50) Pay-To Bank Branch
  isIns VarChar(1) Reserve Invoice default=N [Y=Yes, N=No]
  TrackNo nVarChar(30) Tracking Number
  VersionNum nVarChar(11) Version Number
  LangCode Int(11) Language Code ->OLNG
  BPNameOW VarChar(1) BP Name Overwritten default=N [Y=Yes, N=No]
  BillToOW VarChar(1) Bill-To Overwritten default=N [Y=Yes, N=No]
  ShipToOW VarChar(1) Ship-To Overwritten default=N [Y=Yes, N=No]
  RetInvoice VarChar(1) Credit Memo default=N [Y=Yes, N=No]
  ClsDate Date(8) Document Closing Date
  MInvNum Int(11) Monthly Invoice No.
  MInvDate Date(8) Monthly Invoice Date
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  Model nVarChar(6) Nota Fiscal Model default=0 ->ONFM
  TaxOnExp Num(19,6) Tax on Freight Sum
  TaxOnExpFc Num(19,6) Tax on Freight Sum (FC)
  TaxOnExpSc Num(19,6) Tax on Freight Sum (SC)
  TaxOnExAp Num(19,6) Tax on Freight Applied
  TaxOnExApF Num(19,6) Tax on Freight Applied (FC)
  TaxOnExApS Num(19,6) Tax on Freight Applied (SC)
  LastPmnTyp VarChar(1) Last Payment Type [R=Receipt, V=Vendor Payment]
  LndCstNum Int(11) Landed Cost Number
  UseCorrVat VarChar(1) Use Correction VAT Group default=N [N=No, Y=Yes]
  BlkCredMmo VarChar(1) Block Creation of Target Credit Memo default=N [N=No, Y=Yes]
  OpenForLaC VarChar(1) Open for Landed Costs default=Y [N=Closed for Landed Costs, Y=Open for Landed Costs]
  Excised VarChar(1) Excised default=O [C=Close, O=Open]
  ExcRefDate Date(8) Excise Ref. Date
  ExcRmvTime nVarChar(8) Excise Removal Time
  SrvGpPrcnt Num(19,6) Gross Profit Prcnt of Service default=100
  DepositNum Int(11) Deposit Number
  CertNum nVarChar(31) Certificate Number
  DutyStatus VarChar(1) Duty Status default=Y [Y=With Payment of Duty, N=Without Payment of Duty]
  AutoCrtFlw VarChar(1) Auto Create Follow-up Document default=N [N=No, Y=Yes]
  FlwRefDate Date(8) Follow-up Document Ref. Date
  FlwRefNum nVarChar(100) Follow-up Document Ref. Number
  VatJENum Int(11) VAT Journal Entry Number default=-1
  DpmVat Num(19,6) Down Payment Tax LC
  DpmVatFc Num(19,6) Down Payment Tax FC
  DpmVatSc Num(19,6) Down Payment Tax SC
  DpmAppVat Num(19,6) Down Payment Applied Tax LC
  DpmAppVatF Num(19,6) Down Payment Applied Tax FC
  DpmAppVatS Num(19,6) Down Payment Applied Tax SC
  InsurOp347 VarChar(1) 347 Insurance Operation default=N [N=No, Y=Yes]
  IgnRelDoc VarChar(1) Ignore Relevant Doc on Archive default=N [N=No, Y=Yes]
  BuildDesc nVarChar(50) Build Descriptor
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Residence Country, 5=Certificate of Fiscal Residence, 6=Other Document, 7=Not Registered]
  Checker Int(11) Checker ->OHEM
  Payee Int(11) Payee ->OHEM
  CopyNumber Int(11) Copy Number default=0
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  PQTGrpSer Int(11) Pur Quotation Group Series
  PQTGrpNum Int(11) Pur Quotation Group Number
  PQTGrpHW VarChar(1) Pur Quotation Group Manual default=N [Y=Yes, N=No]
  ReopOriDoc VarChar(1) Reopen Origin. Order by Return [Y=Yes, N=No]
  ReopManCls VarChar(1) Reop. Man. Closed/Canc. Orders [Y=Yes, N=No]
  DocManClsd VarChar(1) Document Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  ClosingOpt Int(6) Closing Option default=1
  SpecDate Date(8) Posting Date Specified by User
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  NTSApprov VarChar(1) NTS Approved default=N [N=No, Y=Yes]
  NTSWebSite Int(6) E-Tax Web Site ->OTWS
  NTSeTaxNo nVarChar(50) E-Tax Number
  NTSApprNo nVarChar(50) NTS Approval Number
  PayDuMonth VarChar(1) Start From [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Number of Additional Months
  ExtraDays Int(6) Number of Additional Days
  CdcOffset Int(6) Cash Discount Offset default=0
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  EDocGenTyp VarChar(1) Electr. Doc. Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  ESeries Int(6) Electronic Series ->NNM4
  EDocNum nVarChar(50) Electronic Document Number
  EDocExpFrm Int(11) Electronic Doc. Export Format
  OnlineQuo VarChar(1) Create Online Quotation default=N [Y=Yes, N=No]
  POSEqNum nVarChar(20) POS Equipment Number
  POSManufSN nVarChar(20) POS Manufacturer Serial Number
  POSCashN Int(11) POS Cashier Number
  EDocStatus VarChar(1) Electronic Document Status default=C [N=New, P=Pending, S=Sent, E=Error, C=OK]
  EDocCntnt Text(16) Electronic Document Content
  EDocProces VarChar(1) Electronic Document Process default=C [C=CFD, I=CFDI]
  EDocErrCod nVarChar(50) Electronic Document Error Code
  EDocErrMsg Text(16) Electronic Document Error Msg
  EDocCancel VarChar(1) Electronic Document - Canceled default=N [N=No, Y=Yes]
  EDocTest VarChar(1) Electronic Document - Testing default=N [N=No, Y=Yes]
  EDocPrefix nVarChar(10) Electronic Document - Prefix
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  DpmAsDscnt VarChar(1) Discount Document with Dpm default=N [N=No, Y=Yes]
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  SupplCode nVarChar(254) Supplementary Code
  GTSRlvnt VarChar(1) Relevant To GTS default=N [N=No, Y=Yes]
  BaseDisc Num(19,6) Base Discount LC
  BaseDiscSc Num(19,6) Base Discount SC
  BaseDiscFc Num(19,6) Base Discount FC
  BaseDiscPr Num(19,6) Base Discount Percentage
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  SrvTaxRule VarChar(1) Apply Service Tax Rule default=N [Y=Yes, N=No]
  AnnInvDecR Int(11) Annual Inv. Declaration Ref.
  Supplier nVarChar(15) Supplier ->OCRD
  Releaser Int(11) Goods Distribution Approver ->OHEM
  Receiver Int(11) Goods Release Approver ->OHEM
  ToWhsCode nVarChar(8) To Warehouse Code ->OWHS
  AssetDate Date(8) Fixed Asset Value Date
  Requester nVarChar(25) User Requesting Goods
  ReqName nVarChar(155) User Name
  Branch Int(6) Branch ->OUBR
  Department Int(6) Department ->OUDP
  Email nVarChar(100) E-Mail
  Notify VarChar(1) Send Notification Needed [Y=Yes, N=No]
  ReqType Int(11) Requester Type User/Employee default=12 [12=User, 171=Employee]
  OriginType VarChar(1) Document Origin default=M [M=Manual, R=MRP, S=Sales Order, D=Document Generation Wizard]
  IsReuseNum VarChar(1) Is Reusing Document Number default=N [Y=Yes, N=No]
  IsReuseNFN VarChar(1) Is Reusing Nota Fiscal Number default=N [Y=Yes, N=No]
  DocDlvry VarChar(1) Document Delivery [0=None, 1=Create Online Document, 2=Post to Ariba Network]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmF Num(19,6) Paid by Down Payment (FC)
  PaidDpmS Num(19,6) Paid by Down Payment (SC)
  EnvTypeNFe Int(11) Environment Type NF-e default=-1 ->OBNI
  AgrNo Int(11) Agreement No.
  IsAlt VarChar(1) Is Alteration default=N [Y=Yes, N=No]
  AltBaseTyp Int(11) Alteration Base Type default=-1 [-1=, 13=, 18=, 163=, 165=]
  AltBaseEnt Int(11) Alteration Base Entry
  AuthCode nVarChar(250) Authorization Code
  StDlvDate Date(8) Start Delivery Date
  StDlvTime Int(11) Start Delivery Time
  EndDlvDate Date(8) End Delivery Date
  EndDlvTime Int(11) End Delivery Time
  VclPlate nVarChar(20) Vehicle Plate
  ElCoStatus nVarChar(10) Elec. Comm. Status [0=Approved, 1=Pending Approval, 2=Rejected]
  AtDocType nVarChar(2) AT Document Type [GT=GT, GA=GA, GD=GD, GR=GR, GC=GC, FT=FT, FS=FS, NC=NC, ND=ND, FR=FR]
  ElCoMsg nVarChar(254) Elec. Comm. Message
  PrintSEPA VarChar(1) Print SEPA Direct Debit Prenotification default=N [Y=Yes, N=No]
  FreeChrg Num(19,6) Free of Charge BP
  FreeChrgFC Num(19,6) Free of Charge BP FC
  FreeChrgSC Num(19,6) Free of Charge BP SC
  NfeValue Num(19,6) NF-e Value
  FiscDocNum nVarChar(100) Fiscal Document Number
  RelatedTyp Int(11) Related Type default=-1 [-1=]
  RelatedEnt Int(11) Related Entry
  CCDEntry Int(11) CCD Abs. Entry
  NfePrntFo Int(11) NF-e Printing Format default=0 [0=No DANFE, 1=Portrait, 2=Landscape, 3=Simplified, 4=DANFE NFC-e, 5=Mail]
  ZrdAbs Int(11) POS Daily Summary Number ->OZRD
  POSRcptNo Int(11) POS Receipt Number
  FoCTax Num(19,6) Free of Charge BP Tax
  FoCTaxFC Num(19,6) Free of Charge BP Tax FC
  FoCTaxSC Num(19,6) Free of Charge BP Tax SC
  TpCusPres Int(11) Type of End-User Presence ->OBNI
  ExcDocDate Date(8) Excise Doc. Date
  FoCFrght Num(19,6) Free of Charge Freight
  FoCFrghtFC Num(19,6) Free of Charge Freight FC
  FoCFrghtSC Num(19,6) Free of Charge Freight SC
  InterimTyp Int(6) Interim Type default=0 [0=None]
  PTICode nVarChar(5) POI Code ->OPTI
  Letter VarChar(1) Letter
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  FolSeries Int(11) Folio Series ->OFNS
  SplitTax Num(19,6) Split Payment Tax
  SplitTaxFC Num(19,6) Split Payment Tax FC
  SplitTaxSC Num(19,6) Split Payment Tax SC
  ToBinCode nVarChar(228) To Bin Location
  PriceMode VarChar(1) Price Mode [N=Net, G=Gross, M=Net and Gross]
  PoDropPrss VarChar(1) PO Drop-Ship Process default=N [Y=Yes, N=No]
  PermitNo nVarChar(20) Permit Number
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  DocTaxID nVarChar(32) Document Tax ID
  DateReport Date(8) Date of Reporting
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  PosCashReg Int(11) POS/Cash Register
  DmpTransID nVarChar(20) Trans ID for Down Payment
  ECommerBP nVarChar(15) E-Commerce Operator ->OCRD
  EComerGSTN nVarChar(15) GST Regn No of E-Commerce
  Revision VarChar(1) Revision default=N [Y=Yes, N=No]
  RevRefNo nVarChar(100) Original Ref. No.
  RevRefDate Date(8) Original Ref. Date
  RevCreRefN nVarChar(100) Original Credit/Debit Ref. No.
  RevCreRefD Date(8) Orign Credit/Debit Ref. Date
  TaxInvNo nVarChar(100) Tax Invoice No.
  FrmBpDate Date(8) From Vendor Date
  GSTTranTyp nVarChar(2) GST Transaction Type [--=Bill of Supply, GA=GST Tax Invoice, GD=GST Debit Memo]
  BaseType Int(11) Base Document Type default=-1 [-1=]
  BaseEntry Int(11) Base Document Internal Key
  ComTrade VarChar(1) Commission Trade default=E [E=, S=Sales Agent, P=Purchase Agent, C=Consignor]
  UseBilAddr VarChar(1) Determine GST by Using Bill to [Y=Yes, N=No]
  IssReason Int(6) Reason for issuing note default=1 [1=Sales Return, 2=Post sale discount, 3=Deficiency in service, 4=Correction in invoice, 5=Change in POS, 6=Finalization of Provisional Assessment, 7=Others]
  ComTradeRt VarChar(1) Commission Trade Return default=N [Y=Yes, N=No]
  SplitPmnt VarChar(1) A/P Split Payment default=N [Y=Yes, N=No]
  SOIWizId Int(11) SOI Wizard ID ->OSOI
  SelfPosted VarChar(1) Self Invoice Created [Yes/No] default=N [Y=Yes, N=No]
  EnBnkAcct Text(16) Encryption of Pay to Bank Acct
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EWBGenType VarChar(1) E-Way Bill Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  SAPPassprt Text(16) Extended SAP Passport
  CtActTax Num(19,6) Customer Accounting Tax
  CtActTaxFC Num(19,6) Customer Accounting Tax (FC)
  CtActTaxSC Num(19,6) Customer Accounting Tax (SC)

# OWTR - Inventory Transfer
Module: Inventory and Production | 424 columns | ObjType: 67
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  AT_CARD: CardCode, NumAtCard
  CUSTOMER: CardCode
  NUM U: PIndicator, DocSubType, Segment, Instance, DocNum
  DOC_STATUS: CANCELED, DocStatus
  FTHR_CARD: FatherType, FatherCard
  SERIES: Series
  OWNER_CODE: OwnerCode
  DATE_PIND: PIndicator, DocDate
  ESERIES: EDocNum, ESeries
  FOL_SERIES: FolSeries
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=I [I=Item, S=Service]
  CANCELED VarChar(1) Canceled default=N [Y=Yes, N=No]
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original, A=Amended]
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Closed]
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  ObjType nVarChar(20) Object Type default=67 [67=Inventory Transfer] ->ADP1
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  CardName nVarChar(100) Customer/Vendor Name
  Address nVarChar(254) Bill to
  NumAtCard nVarChar(100) BP Reference No.
  VatPercent Num(19,6) Tax Rate
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  DiscPrcnt Num(19,6) Discount % for Document
  DiscSum Num(19,6) Total Discount
  DiscSumFC Num(19,6) Total Discount (FC)
  DocCur nVarChar(3) Document Currency ->OCRN
  DocRate Num(19,6) Document Rate
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  GrosProfit Num(19,6) Gross Profit
  GrosProfFC Num(19,6) Gross Profit (FC)
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  ReceiptNum Int(11) Receipt Number
  GroupNum Int(6) Price Lists ->OPLN
  DocTime Int(6) Generation Time
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TrnspCode Int(6) Shipping Type default=-1 ->OSHP
  PartSupply VarChar(1) Partial Delivery default=Y [Y=Yes, N=No]
  Confirmed VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  GrossBase Int(6) Price List for Gross Profit default=0
  ImportEnt Int(11) Landed Costs Internal ID ->OIPF
  CreateTran VarChar(1) Create Journal Entry default=N [Y=Yes, N=No]
  SummryType VarChar(1) Summary Method default=N [N=No Summary, I=By Items, D=By Documents]
  UpdInvnt VarChar(1) Whse Update default=N [N=No, O=Orders from Vendors, C=Sales Orders, G=Consignment, I=Stock]
  UpdCardBal VarChar(1) Update Balances default=N [N=No, O=Orders, D=Delivery Notes, B=Bookkeeping]
  Instance Int(6) Instance default=0
  Flags Int(11) Flags default=0
  InvntDirec VarChar(1) Warehouse Direction default=X [X=Release, E=Receipt]
  CntctCode Int(11) Contact Person ->OCPR
  ShowSCN VarChar(1) Display BP Catalog Number default=N [Y=Yes, N=No]
  FatherCard nVarChar(15) BP Consolidation
  SysRate Num(19,6) System Price
  CurSource VarChar(1) Base Currency default=C [L=Local Currency, S=System Currency, C=BP Currency]
  VatSumSy Num(19,6) Tax Amount (SC)
  DiscSumSy Num(19,6) Total Discount (SC)
  DocTotalSy Num(19,6) Document Total (SC)
  PaidSys Num(19,6) Paid (SC)
  FatherType VarChar(1) Parent Summary Type default=P [P=Payment Consolidation, D=Delivery Consolidation]
  GrosProfSy Num(19,6) Gross Profit (SC)
  UpdateDate Date(8) Date of Update
  IsICT VarChar(1) A/R Invoice + Payment default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight Num(19,6) Weight
  WeightUnit Int(6) Weight UoM
  Series Int(11) Series ->NNM1
  TaxDate Date(8) Document Date
  Filler nVarChar(8) Filter ->OWHS
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  StampNum nVarChar(16) Stamp No.
  isCrin VarChar(1) Corrected Invoice default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  UserSign Int(6) User Signature ->OUSR
  selfInv VarChar(1) Autom. Invoice default=N [N=No, Y=Yes]
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  UserSign2 Int(6) Updating User ->OUSR
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  draftKey Int(11) Document Draft Internal ID default=-1 ->ODRF
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  DunnLevel Int(11) Dunning Level
  Address2 nVarChar(254) Ship To
  LogInstanc Int(11) Log Instance default=0
  Exported VarChar(1) Exported default=N [Y=Yes, N=No]
  StationID Int(11) Workstation ID ->CSTN
  Indicator nVarChar(2) Indicator ->OIDC
  NetProc VarChar(1) Net Procedure default=N [Y=Yes, N=No]
  AqcsTax Num(19,6) Acquisition Tax
  AqcsTaxFC Num(19,6) Acquisition Tax (FC)
  AqcsTaxSC Num(19,6) Acquisition Tax (SC)
  CashDiscPr Num(19,6) Cash Discount Percentage
  CashDiscnt Num(19,6) Cash Discount
  CashDiscFC Num(19,6) Cash Discount (FC)
  CashDiscSC Num(19,6) Cash Discount (SC)
  ShipToCode nVarChar(50) Ship-to Code
  LicTradNum nVarChar(32) Licensed Dealer No.
  PaymentRef nVarChar(27) Payment Reference No.
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  RoundDif Num(19,6) Rounding Diff. Amount
  RoundDifFC Num(19,6) Rounding Diff. Amount (FC)
  RoundDifSy Num(19,6) Rounding Diff. Amount (SC)
  CheckDigit VarChar(1) Control Digit
  Form1099 Int(11) 1099 Form ->OTNN
  Box1099 nVarChar(20) 1099 Box
  submitted VarChar(1) Submitted default=N [Y=Yes, N=No]
  PoPrss VarChar(1) PO Process default=N [Y=Yes, N=No]
  Rounding VarChar(1) Rounding default=N [Y=Yes, N=No]
  RevisionPo VarChar(1) Split Purchase Order default=N [Y=Yes, N=No]
  Segment Int(6) Segment default=0
  ReqDate Date(8) Required Date
  CancelDate Date(8) Cancelation Date
  PickStatus VarChar(1) Pick Status default=N [Y=Yes, N=No]
  Pick VarChar(1) Pick default=N [Y=Yes, N=No]
  BlockDunn VarChar(1) Block Dunning default=N [Y=Yes, N=No]
  PeyMethod nVarChar(15) Payment Method ->OPYM
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  MaxDscn VarChar(1) Maximum Discount default=N [Y=Yes, N=No]
  Reserve VarChar(1) Reserve default=N [Y=Yes, N=No]
  Max1099 Num(19,6) Max. 1099 Amount
  CntrlBnk nVarChar(15) Central Bank Indicator ->OCBI
  PickRmrk nVarChar(254) Pick Remarks
  ISRCodLine nVarChar(53) ISR Coding Line
  ExpAppl Num(19,6) Exp applied
  ExpApplFC Num(19,6) Exp applied FC
  ExpApplSC Num(19,6) Exp applied DC
  Project nVarChar(20) Project Code ->OPRJ
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  LetterNum nVarChar(20) Tax Exemption Letter No.
  FromDate Date(8) Exemption Validity Date From
  ToDate Date(8) Exemption Validity Date To
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  BoeReserev VarChar(1) Bill of Exchange Reserved default=N [Y=Yes, N=No]
  AgentCode nVarChar(32) Agent Code ->OAGP
  WTAppliedS Num(19,6) Applied WTax (SC)
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  Installmnt Int(6) No. of Installments default=1
  VATFirst VarChar(1) Apply Tax on 1st Installment [Y=Yes, N=No]
  NnSbAmnt Num(19,6) WTax Non-Subject Amount
  NnSbAmntSC Num(19,6) WTax Non-Subject Amount (SC)
  NbSbAmntFC Num(19,6) WTax Non-Subject Amount (FC)
  ExepAmnt Num(19,6) Withholding Tax Exempt Amount
  ExepAmntSC Num(19,6) WTax Exempt Amount (SC)
  ExepAmntFC Num(19,6) WTax Exempt Amount (FC)
  VatDate Date(8) Document Date
  CorrExt nVarChar(25) External Corrected Document No.
  CorrInv Int(11) Internal Corrected Document No.
  NCorrInv Int(11) Next Correcting Document
  CEECFlag VarChar(1) Block Creation Target Corr Inv default=N [N=No, Y=Yes]
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  CtlAccount nVarChar(15) Control Account ->OACT
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number
  TxInvRptNo nVarChar(10) Tax Invoice Rpt Number
  TxInvRptDt Date(8) Tax Invoice Rpt Date
  KVVATCode Text(16) VAT Code for Tax Invoice Rpt
  WTDetails nVarChar(100) WTax Details
  SumAbsId Int(11) Summary VAT Abstract ID default=-1
  SumRptDate Date(8) Summary VAT Report Date
  PIndicator nVarChar(10) Period Indicator ->OPID
  ManualNum nVarChar(20) Manual Number
  UseShpdGd VarChar(1) Use Shipped Goods Account default=N [N=No, Y=Yes]
  BaseVtAt Num(19,6) BPL ID Assigned to Invoice
  BaseVtAtSC Num(19,6) BPL Name
  BaseVtAtFC Num(19,6) Tax Reg. Number
  NnSbVAt Num(19,6) Tax Invoice Rpt Number
  NnSbVAtSC Num(19,6) Tax Invoice Rpt Date
  NbSbVAtFC Num(19,6) WTax Amount - VAT-exempt (FC)
  ExptVAt Num(19,6) WTax Exempt VAT Amount
  ExptVAtSC Num(19,6) WTax Exempt VAT Amount (SC)
  ExptVAtFC Num(19,6) WTax Details
  LYPmtAt Num(19,6) Last Year's Payments
  LYPmtAtSC Num(19,6) Last Years Payments (SC)
  LYPmtAtFC Num(19,6) Summary Tax Report Date
  ExpAnSum Num(19,6) Period Indicator
  ExpAnSys Num(19,6) Manual Number
  ExpAnFrgn Num(19,6) Use Shipped Goods Account
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=-- [--=Inventory Transfers]
  DpmStatus VarChar(1) Summary VAT Abstract ID default=O [O=Open, C=Closed]
  DpmAmnt Num(19,6) Down Payment Amount LC
  DpmAmntSC Num(19,6) Down Payment Amount SC
  DpmAmntFC Num(19,6) Down Payment Amount FC
  DpmDrawn VarChar(1) Drawn to Down Payment default=N [N=No, Y=Yes]
  DpmPrcnt Num(19,6) Down Payment Percent
  PaidSum Num(19,6) Total Paid Sum
  PaidSumFc Num(19,6) Total Paid Sum (FC)
  PaidSumSc Num(19,6) Total Paid Sum (SC)
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  DpmAppl Num(19,6) Down Payment Applied LC
  DpmApplFc Num(19,6) Down Payment Applied FC
  DpmApplSc Num(19,6) Down Payment Applied SC
  LPgFolioN Int(11) Folio No. for Last Page in Doc.
  Header Text(16) Header
  Footer Text(16) Footer
  Posted VarChar(1) Down Payment Was Posted default=Y [Y=Yes, N=No]
  OwnerCode Int(11) Document Owner ->OHEM
  BPChCode nVarChar(15) BP Channel Code ->OCRD
  BPChCntc Int(11) BP Channel Contact Person ->OCPR
  PayToCode nVarChar(50) Pay to
  IsPaytoBnk VarChar(1) Is Pay to Bank [N=No, Y=Yes]
  BnkCntry nVarChar(3) Pay to Bank Country ->OCRY
  BankCode nVarChar(30) Pay to Bank Code
  BnkAccount nVarChar(50) Pay to Bank Account No.
  BnkBranch nVarChar(50) Pay to Bank Branch
  isIns VarChar(1) Reserve Invoice default=N [Y=Yes, N=No]
  TrackNo nVarChar(30) Tracking Number
  VersionNum nVarChar(11) Version Number
  LangCode Int(11) Language Code ->OLNG
  BPNameOW VarChar(1) BP Name Overwritten default=N [Y=Yes, N=No]
  BillToOW VarChar(1) Bill-To Overwritten default=N [Y=Yes, N=No]
  ShipToOW VarChar(1) Ship-to Overwritten default=N [Y=Yes, N=No]
  RetInvoice VarChar(1) Returning Invoice default=N [Y=Yes, N=No]
  ClsDate Date(8) Document Closing Date
  MInvNum Int(11) Monthly Invoice No.
  MInvDate Date(8) Monthly Invoice Date
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Numbers
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Sub-Series String
  Model nVarChar(6) Nota Fiscal Model default=0 ->ONFM
  TaxOnExp Num(19,6) Tax on Freight Sum
  TaxOnExpFc Num(19,6) Tax on Freight Sum (FC)
  TaxOnExpSc Num(19,6) Tax on Freight Sum (SC)
  TaxOnExAp Num(19,6) Tax on Freight Applied
  TaxOnExApF Num(19,6) Tax on Freight Applied (FC)
  TaxOnExApS Num(19,6) Tax on Freight Applied (SC)
  LastPmnTyp VarChar(1) Last Payment Type [R=Receipt, V=Vendor Payment]
  LndCstNum Int(11) Landed Cost Number
  UseCorrVat VarChar(1) Use Correction VAT Group default=N [N=No, Y=Yes]
  BlkCredMmo VarChar(1) Block Creation of Target Credit Memo default=N [N=No, Y=Yes]
  OpenForLaC VarChar(1) Open For Landed Costs default=Y [Y=Open for Landed Costs, N=Closed for Landed Costs]
  Excised VarChar(1) Excised default=O [O=Open, C=Close]
  ExcRefDate Date(8) Excise Ref. Date
  ExcRmvTime nVarChar(8) Excise Removal Time
  SrvGpPrcnt Num(19,6) Gross Profit Prcnt of Service
  DepositNum Int(11) Deposit Number
  CertNum nVarChar(31) Certificate Number
  DutyStatus VarChar(1) Duty Status default=Y [Y=With Payment of Duty, N=Without Payment of Duty]
  AutoCrtFlw VarChar(1) Auto Create Follow-up Document default=N [N=No, Y=Yes]
  FlwRefDate Date(8) Follow-up Document Ref. Date
  FlwRefNum nVarChar(100) Follow-up Document Ref. Number
  VatJENum Int(11) VAT Journal Entry Number default=-1 ->OJDT
  DpmVat Num(19,6) Down Payment Tax LC
  DpmVatFc Num(19,6) Down Payment Tax FC
  DpmVatSc Num(19,6) Down Payment Tax SC
  DpmAppVat Num(19,6) Down Payment Applied Tax LC
  DpmAppVatF Num(19,6) Down Payment Applied Tax FC
  DpmAppVatS Num(19,6) Down Payment Applied Tax SC
  InsurOp347 VarChar(1) 347 Insurance Operation default=N [N=No, Y=Yes]
  IgnRelDoc VarChar(1) Ignore Relevant Doc on Archive default=N [N=No, Y=Yes]
  BuildDesc nVarChar(50) Build Descriptor
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Residence Country, 5=Certificate of Fiscal Residence, 6=Other Document, 7=Not Registered]
  Checker Int(11) Checker ->OHEM
  Payee Int(11) Payee ->OHEM
  CopyNumber Int(11) Copy Number default=0
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  PQTGrpSer Int(11) Pur Quotation Group Series
  PQTGrpNum Int(11) Pur Quotation Group Number
  PQTGrpHW VarChar(1) Pur Quotation Group Manual default=N [Y=Yes, N=No]
  ReopOriDoc VarChar(1) Reopen Origin. Order by Return [Y=Yes, N=No]
  ReopManCls VarChar(1) Reop. Man. Closed/Canc. Orders [Y=Yes, N=No]
  DocManClsd VarChar(1) Document Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  ClosingOpt Int(6) Closing Option default=1
  SpecDate Date(8) Posting Date Specified by User
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  NTSApprov VarChar(1) NTS Approved default=N [N=No, Y=Yes]
  NTSWebSite Int(6) E-Tax Web Site ->OTWS
  NTSeTaxNo nVarChar(50) E-Tax Number
  NTSApprNo nVarChar(50) NTS Approval Number
  PayDuMonth VarChar(1) Start From [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Number of Additional Months
  ExtraDays Int(6) Number of Additional Days
  CdcOffset Int(6) Cash Discount Offset default=0
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  EDocGenTyp VarChar(1) Electr. Doc. Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  ESeries Int(6) Electronic Series ->NNM4
  EDocNum nVarChar(50) Electronic Document Number
  EDocExpFrm Int(11) Electronic Doc. Export Format
  OnlineQuo VarChar(1) Create Online Quotation default=N [Y=Yes, N=No]
  POSEqNum nVarChar(20) POS Equipment Number
  POSManufSN nVarChar(20) POS Manufacturer Serial Number
  POSCashN Int(11) POS Cashier Number
  EDocStatus VarChar(1) Electronic Document Status default=C [N=New, P=Pending, S=Sent, E=Error, C=OK]
  EDocCntnt Text(16) Electronic Document Content
  EDocProces VarChar(1) Electronic Document Process default=C [C=CFD, I=CFDI]
  EDocErrCod nVarChar(50) Electronic Document Error Code
  EDocErrMsg Text(16) Electronic Document Error Msg
  EDocCancel VarChar(1) Electronic Document - Canceled default=N [N=No, Y=Yes]
  EDocTest VarChar(1) Electronic Document - Testing default=N [N=No, Y=Yes]
  EDocPrefix nVarChar(10) Electronic Document - Prefix
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  DpmAsDscnt VarChar(1) Discount Document with Dpm default=N [N=No, Y=Yes]
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  SupplCode nVarChar(254) Supplementary Code
  GTSRlvnt VarChar(1) Relevant To GTS default=N [N=No, Y=Yes]
  BaseDisc Num(19,6) Base Discount LC
  BaseDiscSc Num(19,6) Base Discount SC
  BaseDiscFc Num(19,6) Base Discount FC
  BaseDiscPr Num(19,6) Base Discount Percentage
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  SrvTaxRule VarChar(1) Apply Service Tax Rule default=N [Y=Yes, N=No]
  AnnInvDecR Int(11) Annual Inv. Declaration Ref.
  Supplier nVarChar(15) Supplier ->OCRD
  Releaser Int(11) Goods Distribution Approver ->OHEM
  Receiver Int(11) Goods Release Approver ->OHEM
  ToWhsCode nVarChar(8) To Warehouse Code ->OWHS
  AssetDate Date(8) Fixed Asset Value Date
  Requester nVarChar(25) User Requesting Goods
  ReqName nVarChar(155) User Name
  Branch Int(6) Branch ->OUBR
  Department Int(6) Department ->OUDP
  Email nVarChar(100) E-Mail
  Notify VarChar(1) Send Notification Needed [Y=Yes, N=No]
  ReqType Int(11) Requester Type User/Employee default=12 [12=User, 171=Employee]
  OriginType VarChar(1) Document Origin default=M [M=Manual, R=MRP, S=Sales Order, D=Document Generation Wizard]
  IsReuseNum VarChar(1) Is Reusing Document Number default=N [Y=Yes, N=No]
  IsReuseNFN VarChar(1) Is Reusing Nota Fiscal Number default=N [Y=Yes, N=No]
  DocDlvry VarChar(1) Document Delivery [0=None, 1=Create Online Document, 2=Post to Ariba Network]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmF Num(19,6) Paid by Down Payment (FC)
  PaidDpmS Num(19,6) Paid by Down Payment (SC)
  EnvTypeNFe Int(11) Environment Type NF-e default=-1 ->OBNI
  AgrNo Int(11) Agreement No.
  IsAlt VarChar(1) Is Alteration default=N [Y=Yes, N=No]
  AltBaseTyp Int(11) Alteration Base Type default=-1 [-1=, 13=, 18=, 163=, 165=]
  AltBaseEnt Int(11) Alteration Base Entry
  AuthCode nVarChar(250) Authorization Code
  StDlvDate Date(8) Start Delivery Date
  StDlvTime Int(11) Start Delivery Time
  EndDlvDate Date(8) End Delivery Date
  EndDlvTime Int(11) End Delivery Time
  VclPlate nVarChar(20) Vehicle Plate
  ElCoStatus nVarChar(10) Elec. Comm. Status [0=Approved, 1=Pending Approval, 2=Rejected]
  AtDocType nVarChar(2) AT Document Type [GT=GT, GA=GA, GD=GD, GR=GR, GC=GC, FT=FT, FS=FS, NC=NC, ND=ND, FR=FR]
  ElCoMsg nVarChar(254) Elec. Comm. Message
  PrintSEPA VarChar(1) Print SEPA Direct Debit Prenotification default=N [Y=Yes, N=No]
  FreeChrg Num(19,6) Free of Charge BP
  FreeChrgFC Num(19,6) Free of Charge BP FC
  FreeChrgSC Num(19,6) Free of Charge BP SC
  NfeValue Num(19,6) NF-e Value
  FiscDocNum nVarChar(100) Fiscal Document Number
  RelatedTyp Int(11) Related Type default=-1 [-1=]
  RelatedEnt Int(11) Related Entry
  CCDEntry Int(11) CCD Abs. Entry
  NfePrntFo Int(11) NF-e Printing Format default=0 [0=No DANFE, 1=Portrait, 2=Landscape, 3=Simplified, 4=DANFE NFC-e, 5=Mail]
  ZrdAbs Int(11) POS Daily Summary Number ->OZRD
  POSRcptNo Int(11) POS Receipt Number
  FoCTax Num(19,6) Free of Charge BP Tax
  FoCTaxFC Num(19,6) Free of Charge BP Tax FC
  FoCTaxSC Num(19,6) Free of Charge BP Tax SC
  TpCusPres Int(11) Type of End-User Presence ->OBNI
  ExcDocDate Date(8) Excise Doc. Date
  FoCFrght Num(19,6) Free of Charge Freight
  FoCFrghtFC Num(19,6) Free of Charge Freight FC
  FoCFrghtSC Num(19,6) Free of Charge Freight SC
  InterimTyp Int(6) Interim Type default=0 [0=None]
  PTICode nVarChar(5) POI Code ->OPTI
  Letter VarChar(1) Letter [A=A, B=B, C=C, E=E, M=M, R=R]
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  FolSeries Int(11) Folio Series ->OFNS
  SplitTax Num(19,6) Split Payment Tax
  SplitTaxFC Num(19,6) Split Payment Tax FC
  SplitTaxSC Num(19,6) Split Payment Tax SC
  ToBinCode nVarChar(228) To Bin Location
  PriceMode VarChar(1) Price Mode [N=Net, G=Gross, M=Net and Gross]
  PoDropPrss VarChar(1) PO Drop-Ship Process default=N [Y=Yes, N=No]
  PermitNo nVarChar(20) Permit Number
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  DocTaxID nVarChar(32) Document Tax ID
  DateReport Date(8) Date of Reporting
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  PosCashReg Int(11) POS/Cash Register
  DmpTransID nVarChar(20) Trans ID for Down Payment
  ECommerBP nVarChar(15) E-Commerce Operator ->OCRD
  EComerGSTN nVarChar(15) GST Regn No of E-Commerce
  Revision VarChar(1) Revision default=N [Y=Yes, N=No]
  RevRefNo nVarChar(100) Original Ref. No.
  RevRefDate Date(8) Original Ref. Date
  RevCreRefN nVarChar(100) Original Credit/Debit Ref. No.
  RevCreRefD Date(8) Orign Credit/Debit Ref. Date
  TaxInvNo nVarChar(100) Tax Invoice No.
  FrmBpDate Date(8) From Vendor Date
  GSTTranTyp nVarChar(2) GST Transaction Type [--=Bill of Supply, GA=GST Tax Invoice, GD=GST Debit Memo]
  BaseType Int(11) Base Document Type default=-1 [-1=]
  BaseEntry Int(11) Base Document Internal Key
  ComTrade VarChar(1) Commission Trade default=E [E=, S=Sales Agent, P=Purchase Agent, C=Consignor]
  UseBilAddr VarChar(1) Determine GST by Using Bill to [Y=Yes, N=No]
  IssReason Int(6) Reason for issuing note default=1 [1=Sales Return, 2=Post sale discount, 3=Deficiency in service, 4=Correction in invoice, 5=Change in POS, 6=Finalization of Provisional Assessment, 7=Others]
  ComTradeRt VarChar(1) Commission Trade Return default=N [Y=Yes, N=No]
  SplitPmnt VarChar(1) A/P Split Payment default=N [Y=Yes, N=No]
  SOIWizId Int(11) SOI Wizard ID ->OSOI
  SelfPosted VarChar(1) Self Invoice Created [Yes/No] default=N [Y=Yes, N=No]
  EnBnkAcct Text(16) Encryption of Pay to Bank Acct
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EWBGenType VarChar(1) E-Way Bill Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  SAPPassprt Text(16) Extended SAP Passport
  CtActTax Num(19,6) Customer Accounting Tax
  CtActTaxFC Num(19,6) Customer Accounting Tax (FC)
  CtActTaxSC Num(19,6) Customer Accounting Tax (SC)

# PKL1 - Pick List - Rows
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PickEntry, AbsEntry
  ORDER: OrderLine, OrderEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPKL
  PickEntry Int(11) Row Number
  OrderEntry Int(11) Order Entry
  OrderLine Int(11) Order Row ID
  PickQtty Num(19,6) Picked Quantity
  PickStatus VarChar(1) Pick Status default=R [R=Released for Picking, Y=Picked, P=Partially Picked, D=Partially Delivered, C=Closed]
  RelQtty Num(19,6) Released Quantity
  LogInsac Int(11) Log Instance - History
  PrevReleas Num(19,6) Previously Released Quantity
  BaseObject Int(11) Base Object Type [17=Order, 13=Reserve Invoice, 202=Production Order, 1250000001=Inventory Transfer Request, 0=]

# PKL2 - Pick List for SnB and Bin Details
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Pkl2LinNum, PickEntry, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPKL
  PickEntry Int(11) Row Number
  Pkl2LinNum Int(11) PKl2 Line Number
  ItemCode nVarChar(50) Item No. ->OITM
  ManagedBy Int(11) Management Method default=-1 [10000044=BTN, 10000045=SRN, -1=NOB]
  SnBEntry Int(11) SnB Abs. Entry
  BinAbs Int(11) Bin Internal Number ->OBIN
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  RelQtty Num(19,6) Released Quantity
  PickQtty Num(19,6) Picked Quantity
  ObjType nVarChar(20) Object Type default=156 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# RTL1 - Resource Transaction Log
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BaseLogEnt, StdCostNum, LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Entry ID
  StdCostNum Int(11) Resource Standard Cost Number
  BaseLogEnt Int(11) Base Log Entry ID default=-1 ->ORTL
  DocQty Num(19,6) Doc. Quantity
  Price Num(19,6) Price
  Total Num(19,6) Total
  OpenTotal Num(19,6) Open Total

# SITM - Items
Module: Inventory and Production | 322 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItemCode
  ITEM_NAME: ItemName
  TREE_TYPE: TreeType
  COM_GROUP: CommisGrp
  SALE: SellItem
  PURCHASE: PrchseItem
  INVENTORY: InvntItem
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No.
  ItemName nVarChar(100) Item Description
  FrgnName nVarChar(100) Foreign Name
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  CstGrpCode Int(6) Customs Group default=-1 ->OARG
  VatGourpSa nVarChar(8) Sales Tax Definition ->OVTG
  CodeBars nVarChar(254) Bar Code
  VATLiable VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  PrchseItem VarChar(1) Purchase Item default=Y [Y=Yes, N=No]
  SellItem VarChar(1) Sales Item default=Y [Y=Yes, N=No]
  InvntItem VarChar(1) Inventory Item default=Y [Y=Yes, N=No]
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Qty Ordered by Customers
  OnOrder Num(19,6) Qty Ordered from Vendors
  IncomeAcct nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  MaxLevel Num(19,6) Maximum Inventory Level
  DfltWH nVarChar(8) Default Warehouse
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  SuppCatNum nVarChar(50) Mfr Catalog No.
  BuyUnitMsr nVarChar(100) Purchasing UoM
  NumInBuy Num(19,6) No. of Items per Purchase Unit
  ReorderQty Num(19,6) Required (Purchasing UoM)
  MinLevel Num(19,6) Minimum Inventory Level
  LstEvlPric Num(19,6) Last Evaluated Price
  LstEvlDate Date(8) Date of Last Reval. Price
  CustomPer Num(19,6) Customs Rate
  Canceled VarChar(1) Canceled Item [Yes/No] default=N [Y=Yes, N=No]
  MnufctTime Int(11) Production Date in Days
  WholSlsTax VarChar(1) Tax Rate for Wholesaler
  RetilrTax VarChar(1) Sales Tax in %
  SpcialDisc Num(19,6) Special Discount %
  DscountCod Int(6) Discount Code
  TrackSales VarChar(1) Follow-Up [Yes/No] default=N [Y=Yes, N=No]
  SalUnitMsr nVarChar(100) Sales UoM
  NumInSale Num(19,6) No. of Items per Sales Unit
  Consig Num(19,6) Consignment Goods Whse
  QueryGroup Int(11) Properties default=0
  Counted Num(19,6) Quantity Counted in Inventory
  OpenBlnc Num(19,6) Initial Stock
  EvalSystem VarChar(1) Valuation Method [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch]
  UserSign Int(6) User Signature ->OUSR
  FREE VarChar(1) Free [Yes/No] default=N [Y=Yes, N=No]
  PicturName nVarChar(200) Picture
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  BlncTrnsfr VarChar(1) Balances transferred [Yes/No] default=N [Y=Yes, N=No]
  UserText Text(16) Item Remarks
  SerialNum nVarChar(17) Serial Number
  CommisPcnt Num(19,6) % Commission for Item
  CommisSum Num(19,6) Total Commission for Item
  CommisGrp Int(6) Commission Group default=0 ->OCOG
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, P=Production, T=Template]
  TreeQty Num(19,6) No. of Units
  LastPurPrc Num(19,6) Last Purchase Price
  LastPurCur nVarChar(3) Last Purchase Currency
  LastPurDat Date(8) Last Purchase Date
  ExitCur nVarChar(3) Issue Currency
  ExitPrice Num(19,6) Issue Price
  ExitWH nVarChar(8) Release Warehouse
  AssetItem VarChar(1) Fixed Asset Indicator default=N [Y=Yes, N=No]
  WasCounted VarChar(1) Counted default=N [Y=Yes, N=No]
  ManSerNum VarChar(1) Serial No. Management default=N [Y=Yes, N=No]
  SHeight1 Num(19,6) Height 1 - Sales Unit
  SHght1Unit Int(6) Height 1 - UoM for Sales
  SHeight2 Num(19,6) Height 2 - Sales Unit
  SHght2Unit Int(6) Height 2 - UoM for Sales
  SWidth1 Num(19,6) Width 1 - Sales Unit
  SWdth1Unit Int(6) Width 1 - UoM for Sales
  SWidth2 Num(19,6) Width 2 - Sales Unit
  SWdth2Unit Int(6) Width 2 - UoM for Sales
  SLength1 Num(19,6) Length 1 - Sales Unit
  SLen1Unit Int(6) Length 1 - UoM for Sales
  Slength2 Num(19,6) Length 2 - Sales Unit
  SLen2Unit Int(6) Length 2 - UoM for Sales
  SVolume Num(19,6) Volume - Sales Unit
  SVolUnit Int(6) Volume - UoM for Sales
  SWeight1 Num(19,6) Weight 1 - Sales Unit
  SWght1Unit Int(6) Weight 1 - UoM for Sales
  SWeight2 Num(19,6) Weight 2 - Sales Unit
  SWght2Unit Int(6) Weight 2 - UoM for Sales
  BHeight1 Num(19,6) Height 1 - Purchasing Unit
  BHght1Unit Int(6) Height 1 - UoM for Purchasing
  BHeight2 Num(19,6) Height 2 - Purchasing Unit
  BHght2Unit Int(6) Height 2 - UoM for Purchasing
  BWidth1 Num(19,6) Width 1 - Purchasing Unit
  BWdth1Unit Int(6) Width 1 - UoM for Purchasing
  BWidth2 Num(19,6) Width 2 - Purchasing Unit
  BWdth2Unit Int(6) Width 2 - UoM for Purchasing
  BLength1 Num(19,6) Length 1 - Purchase Unit
  BLen1Unit Int(6) Length 1 - UoM for Purchasing
  Blength2 Num(19,6) Length 2 - Purchase Unit
  BLen2Unit Int(6) Length 2 - UoM for Purchasing
  BVolume Num(19,6) Volume - Purchasing Unit
  BVolUnit Int(6) Volume - UoM for Purchasing
  BWeight1 Num(19,6) Weight 1 - Purchasing Unit
  BWght1Unit Int(6) Weight 1 - UoM for Purchasing
  BWeight2 Num(19,6) Weight 2 - Purchasing Unit
  BWght2Unit Int(6) Weight 2 - UoM for Purchasing
  FixCurrCms nVarChar(3) Currency of Fixed Commission
  FirmCode Int(6) Manufacturer default=-1 ->OMRC
  LstSalDate Date(8) Last Sale Date
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
  CreateDate Date(8) Production Date
  UpdateDate Date(8) Date of Update
  ExportCode nVarChar(20) Data Export Code
  SalFactor1 Num(19,6) Sales Factor 1
  SalFactor2 Num(19,6) Sales Factor 2
  SalFactor3 Num(19,6) Sales Factor 3
  SalFactor4 Num(19,6) Sales Factor 4
  PurFactor1 Num(19,6) Purchasing Factor 1
  PurFactor2 Num(19,6) Purchasing Factor 2
  PurFactor3 Num(19,6) Purchasing Factor 3
  PurFactor4 Num(19,6) Purchasing Factor 4
  SalFormula nVarChar(40) Sales Formula
  PurFormula nVarChar(40) Purchasing Formula
  VatGroupPu nVarChar(8) Purchase Tax Definition ->OVTG
  AvgPrice Num(19,6) Item Cost
  PurPackMsr nVarChar(30) Packaging UoM (Purchasing)
  PurPackUn Num(19,6) Quantity per Package (Purchasing)
  SalPackMsr nVarChar(30) Packaging UoM (Sales)
  SalPackUn Num(19,6) Quantity per Package (Sales)
  SCNCounter Int(6) SCN Counter
  ManBtchNum VarChar(1) Manage Batch No. [Yes/No] default=N [Y=Yes, N=No]
  ManOutOnly VarChar(1) Manage SN Only on Exit default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer, G=Fixed Assets Migration]
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  BlockOut VarChar(1) Force selection of serial no. default=Y [Y=Yes, N=No]
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=4 ->ADP1
  SWW nVarChar(16) Additional Identifier
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  DocEntry Int(11) Internal Number
  ExpensAcct nVarChar(15) Expense Account ->OACT
  FrgnInAcct nVarChar(15) Revenue Account - Foreign ->OACT
  ShipType Int(6) Shipping Type ->OSHP
  GLMethod VarChar(1) Set G/L Accounts By default=W [W=Warehouse, C=Item Group, L=Item Level]
  ECInAcct nVarChar(15) Revenue Account - EU
  FrgnExpAcc nVarChar(15) Expense Account - Foreign
  ECExpAcc nVarChar(15) Expense Account - EU
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, U=Use Tax, N=No Tax]
  ByWh VarChar(1) Manage Inventory by Warehouse
  WTLiable VarChar(1) WTax Liable default=Y [Y=Yes, N=No]
  ItemType VarChar(1) Item Type default=I [I=Items, L=Labor, T=Travel, F=Fixed Assets]
  WarrntTmpl nVarChar(20) Warranty Template ->OCTT
  BaseUnit nVarChar(20) Base Unit Name
  CountryOrg nVarChar(3) Country of Origin
  StockValue Num(19,6) Inventory Value
  Phantom VarChar(1) Phantom Item default=N [Y=Yes, N=No]
  IssueMthd VarChar(1) Issue Method [B=Backflush, M=Manual]
  FREE1 VarChar(1) Yield in %
  PricingPrc Num(19,6) Pricing Percentage
  MngMethod VarChar(1) Management Method default=R [A=On Every Transaction, R=On Release Only]
  ReorderPnt Num(19,6) Reorder Point
  InvntryUom nVarChar(100) Inventory UoM
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  IndirctTax VarChar(1) Indirect Tax default=N [Y=Yes, N=No]
  TaxCodeAR nVarChar(8) Tax Code (A/R) ->OSTC
  TaxCodeAP nVarChar(8) Tax Code (A/P) ->OSTC
  OSvcCode Int(11) Outgoing Service Code default=-1 ->OSCD
  ISvcCode Int(11) Incoming Service Code default=-1 ->OSCD
  ServiceGrp Int(11) Service Group default=-1 ->OSGP
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  ServiceCtg Int(11) Service Category default=-1 [-1=] ->OSCG
  ItemClass VarChar(1) Service or Material default=2 [2=Material, 1=Service]
  Excisable VarChar(1) Excisable [Yes/No] default=N [Y=Yes, N=No]
  ChapterID Int(11) Chapter ID default=-1 ->OCHP
  NotifyASN nVarChar(40) Notification Availed SN.
  ProAssNum nVarChar(20) Provisional Assessment No.
  AssblValue Num(19,6) Assessable Value
  DNFEntry Int(11) DNF Code Entry default=-1 ->ODNF
  UserSign2 Int(6) Updating User ->OUSR
  Spec nVarChar(30) Item Specification
  TaxCtg nVarChar(4) Tax Category
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  FuelCode Int(11) Fuel default=-1 ->OBFI
  BeverTblC nVarChar(2) Beverage Table ->OBSI
  BeverGrpC nVarChar(2) Beverage Group ->OBSI
  BeverTM Int(11) Beverage Brand default=-1 ->OBNI
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  ToleranDay Int(11) Tolerance Days
  UgpEntry Int(11) UoM Group ->OUGP
  PUoMEntry Int(11) Default Purchase UoM ->OUOM
  SUoMEntry Int(11) Default Sales UoM ->OUOM
  IUoMEntry Int(11) Inventory UoM ->OUOM
  IssuePriBy Int(6) Issue Primarily By SnB or Bin [0=Issue Primarily by Serial/Batch Number, 1=Issue Primarily by Bin Location]
  AssetClass nVarChar(20) Asset Class ->OACS
  AssetGroup nVarChar(15) Asset Group ->OAGS
  InventryNo nVarChar(12) Inventory Number of Asset
  Technician Int(11) Technician of Fixed Asset ->OHEM
  Employee Int(11) Employee of Fixed Asset ->OHEM
  Location Int(11) Location ->OLCT
  StatAsset VarChar(1) Owned by Company default=N [Y=Yes, N=No]
  Cession VarChar(1) Cession default=N [Y=Yes, N=No]
  DeacAftUL VarChar(1) Deactivate After Useful Life default=N [Y=Yes, N=No]
  AsstStatus VarChar(1) Asset Status default=N [N=New, A=Active, I=Inactive]
  CapDate Date(8) Capitalization Date
  AcqDate Date(8) Acquisition Date
  RetDate Date(8) Retirement Date
  GLPickMeth VarChar(1) G/L Account Pick Method default=A [A=General, W=Warehouse, C=Item Group]
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  MgrByQty VarChar(1) Manage Asset by Quantity default=N [Y=Yes, N=No]
  AssetRmk1 nVarChar(100) Asset Remark 1
  AssetRmk2 nVarChar(100) Asset Remark 2
  AssetAmnt1 Num(19,6) Asset Amount 1
  AssetAmnt2 Num(19,6) Asset Amount 2
  DeprGroup nVarChar(15) Depreciation Group ->OADG
  AssetSerNo nVarChar(32) Asset Serial Number
  CntUnitMsr nVarChar(100) Inventory Counting UoM Name
  NumInCnt Num(19,6) No. of Items per Counting Unit
  INUoMEntry Int(11) Inventory Counting UoM Entry ->OUOM
  OneBOneRec VarChar(1) One Batch One Receipt default=N [Y=Yes, N=No]
  RuleCode nVarChar(2) Checking Rule Code ->ODCR
  ScsCode nVarChar(10) Scs Code
  SpProdType nVarChar(2) Special Product Type [MT=Cellular Phones, IO=Integrated Circuits]
  IWeight1 Num(19,6) Weight 1 - Inventory
  IWght1Unit Int(6) Weight 1 - Inventory Unit
  IWeight2 Num(19,6) Weight 2 - Inventory
  IWght2Unit Int(6) Weight 2 - Inventory Unit
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VirtAstItm VarChar(1) Virtual Asset Item default=N [N=No, Y=Yes]
  SouVirAsst nVarChar(50) Source Virtual Asset Item ->OITM
  InCostRoll VarChar(1) Include in Prod. Cost Rollup default=Y [Y=Yes, N=No]
  PrdStdCst Num(19,6) Production Std Cost
  EnAstSeri VarChar(1) Enforce Asset Serial Numbers default=N [Y=Yes, N=No]
  LinkRsc nVarChar(50) Linked Resource ->ORSC
  OnHldPert Num(19,6) Capital Goods On Hold Percent
  onHldLimt Num(19,6) Capital Goods on Hold Limit
  PriceUnit Int(11) Pricing Unit ->OUOM
  GSTRelevnt VarChar(1) GST Relevant default=N [Y=Yes, N=No]
  SACEntry Int(11) SAC Entry default=-1 ->OSAC
  GstTaxCtg VarChar(1) GST Tax Category default=R [R=Regular, N=Nil Rated, E=Exempt]
  AssVal4WTR Num(19,6) Assessable Value for WTR
  ExcImpQUoM Int(11) Default Excise Imported Quantity UoM [112=Liters, m3, 168=Tonne, metric ton (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcFixAmnt Num(19,6) Default Excise Fixed Amount
  ExcRate Num(19,6) Default Excise Rate
  SOIExc VarChar(1) SOI Excisable default=4 [1=Excisable, 2=Exemption of excises, 3=Excises are paid to another authority, 4=Not Excisable]
  TNVED nVarChar(10) TNVED Code
  Imported VarChar(1) Imported Item default=N [Y=Yes, N=No]
  AutoBatch VarChar(1) Automatic Batch Creation default=N [Y=Yes, N=No]
  CstmActing VarChar(1) Customer Accounting default=N [N=No, Y=Yes]

# SITW - Items - Warehouse
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WhsCode, ItemCode
  WHS: WhsCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Defined
  OnOrder Num(19,6) Ordered
  Consig Num(19,6) Consignment Goods Whse
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  MinStock Num(19,6) Minimum Inventory
  MaxStock Num(19,6) Maximum Inventory
  MinOrder Num(19,6) Min. Order
  AvgPrice Num(19,6) Average Price
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Transfer Acct ->OACT
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns Account ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Revenue Account - EU ->OACT
  EUExpensAc nVarChar(15) Expense Account - EU ->OACT
  FrRevenuAc nVarChar(15) Revenue Account - Foreign ->OACT
  FrExpensAc nVarChar(15) Expense Account - Foreign ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  PriceDifAc nVarChar(15) Price Differences Account
  ExchangeAc nVarChar(15) Exchange Rate Differences Account
  BalanceAcc nVarChar(15) Goods Clearing Account
  PurchaseAc nVarChar(15) Purchase Account
  PAReturnAc nVarChar(15) Purchase Return Account
  PurchOfsAc nVarChar(15) Purchase Offset Account
  ShpdGdsAct nVarChar(15) Shipped Goods Account
  VatRevAct nVarChar(15) VAT in Revenue Account
  StockValue Num(19,6) Inventory Value
  DecresGlAc nVarChar(15) G/L Decrease Account
  IncresGlAc nVarChar(15) G/L Increase Account
  StokRvlAct nVarChar(15) Stock Inflation Adjust Account
  StkOffsAct nVarChar(15) Stock Inflation Offset Account
  WipAcct nVarChar(15) WIP Inventory Account
  WipVarAcct nVarChar(15) WIP Inventory Variance Account
  CostRvlAct nVarChar(15) Cost Inflation Account
  CstOffsAct nVarChar(15) Cost Inflation Offset Account
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  Object nVarChar(20) Object Type - History default=31
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  ARCMAct nVarChar(15) Sales Credit Account
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign
  ARCMEUAct nVarChar(15) Sales Credit Account - EU
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account
  APCMAct nVarChar(15) Purchase Credit Account
  APCMFrnAct nVarChar(15) Purchase Credit Account - Foreign
  APCMEUAct nVarChar(15) Purchase Credit Account - EU
  RevRetAct nVarChar(15) Revenue Returns Account
  NegStckAct nVarChar(15) Negative Inventory Adj. Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account
  PurBalAct nVarChar(15) Purchase Balance Account
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  Freezed VarChar(1) Item Frozen in Warehouse default=N [Y=Yes, N=No]
  FreezeDoc Int(11) INC Document Frozen By ->OINC
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account

# SIVE - FIFO Based Sales Return
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TRANS_SEQ: LayerID, TransSeq
  TreeID: TreeID
Fields (name type(len) description [values] ->parent table):
  TreeID Int(11) Tree ID default=0
  ParentID Int(11) Parent ID default=-1
  AbsEntry Int(11) Internal Number
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TransSeq Int(11) Transaction Sequence No. ->SIVL
  LayerID Int(11) Layer ID
  LayerInQty Num(19,6) Layer In Quantity
  LayerOutQ Num(19,6) Layer Out Quantity
  LayerVal Num(19,6) Layer Value
  ItemCode nVarChar(50) Item Code ->SITM
  EntryTreeI Int(11) Entry Tree ID
  LayerCogs Num(19,6) Layer - Cost of Goods Sold

# SIVK - IVL Vs OINM Keys
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: INMTransSe
  TRANSSEQ U: LayerID, TransSeq
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No.
  LayerID Int(11) Layer ID
  RootID Int(11) Root ID
  TransNum Int(11) Transaction Number
  Instance Int(11) Instance default=0
  INMTransSe Int(11) INM_Transaction Sequence No.

# SIVL - Whse Journal
Module: Inventory and Production | 78 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TransSeq
  ITEM: ItemCode
  CURRENCY: Currency
  DOCDATE: DocDate
  DOCENTRY: DocLineNum, TransType, CreatedBy
  MESSAGEID: MessageID
Fields (name type(len) description [values] ->parent table):
  TransType Int(11) Transaction Type default=-1 [15=Delivery, 16=Returns, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 18=A/P Invoice, 19=A/P Credit Memo, -2=Opening Balance, 58=Inventory Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfer, 68=Work Instructions, -1=All Transactions, 162=Inventory Revaluation, 69=Landed Costs]
  CreatedBy Int(11) Document Key Created
  BASE_REF nVarChar(11) Base Reference
  DocLineNum Int(11) Row Number in Document
  DocDate Date(8) Posting Date
  CreateTime Int(6) Generation Time
  ItemCode nVarChar(50) Item No. ->SITM
  InQty Num(19,6) Receipt Quantity
  OutQty Num(19,6) Issue Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  TrnsfrAct nVarChar(15) Transfer Account ->OACT
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  ReturnAct nVarChar(15) Returning Account ->OACT
  ExcRateAct nVarChar(15) Exchange Rate Differences Acct ->OACT
  ClearAct nVarChar(15) Goods Clearing Account ->OACT
  CostAct nVarChar(15) COGS Account ->OACT
  WipAct nVarChar(15) WIP Inventory Account ->OACT
  OpenStock Num(19,6) Open Sum Inventory Value
  CreateDate Date(8) Creation Date
  PriceDiff Num(19,6) Price Difference Value
  TransSeq Int(11) Transaction Sequence No. default=0
  InvntAct nVarChar(15) Inventory Account ->OACT
  SubLineNum Int(11) Subrow Number default=-1
  AppObjLine Int(11) Applied Object Line default=-1
  Expenses Num(19,6) Inventory Expenses
  OpenExp Num(19,6) Open Expenses Value
  Allocation Num(19,6) Allocation Amount
  OpenAlloc Num(19,6) Open Allocation Value
  ExpAlloc Num(19,6) Expenses Allocation Value
  OExpAlloc Num(19,6) Open Expenses Allocation Value
  OpenPDiff Num(19,6) Open Price Diff. Value
  ExchDiff Num(19,6) Exchange Rate Difference Value
  OpenEDiff Num(19,6) Open Exchange Rate Diff. Value
  NegInvAdjs Num(19,6) Negative Inventory Adjustment Value
  OpenNegInv Num(19,6) Open Negative Adjustment
  NegStckAct nVarChar(15) Negative Inventory Adj. Acct ->OACT
  BTransVal Num(19,6) Base Transaction Value
  VarVal Num(19,6) Variance Value
  BExpVal Num(19,6) Base Freight Value
  CogsVal Num(19,6) COGS Value
  BNegAVal Num(19,6) Base Negative Adjustment Amt
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  IOffIncVal Num(19,6) Inv. Offset Increase Value
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DOffDecVal Num(19,6) Inv. Offset Decrease Value
  DecAcc nVarChar(15) G/L Decrease Account ->OACT
  DecVal Num(19,6) G/L Decrease Value
  WipVal Num(19,6) WIP Inventory Value
  WipVarAcc nVarChar(15) WIP Variance Account ->OACT
  WipVarVal Num(19,6) WIP Variance Value
  IncAct nVarChar(15) G/L Increase Account
  IncVal Num(19,6) G/L Increase Value
  ExpCAcc nVarChar(15) Expense Clearing Account ->OACT
  CostMethod VarChar(1) Costing Method default=N [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch, N=None]
  MessageID Int(11) Message ID ->OILM
  LocType Int(11) Location Type
  LocCode nVarChar(8) Warehouse Code
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, Y=Year Transfer]
  PostStatus VarChar(1) Posting Status default=N [N=None, P=Partial, C=Complete]
  SumStock Num(19,6) Sum Stock Value
  OpenCogs Num(19,6) Open COGS Value
  OpenQty Num(19,6) Open Quantity
  TreeID Int(11) Tree ID default=-1
  ParentID Int(11) Parent ID default=-1
  PAOffAcc nVarChar(15) Purchase Offset Account ->OACT
  PAOffVal Num(19,6) Purchase Offset Value
  OpenPAOff Num(19,6) Open Purchase Offset Value
  PAAcc nVarChar(15) Purchase Account ->OACT
  PAVal Num(19,6) Purchase Account Value
  OpenPA Num(19,6) Open Purchase Value
  LinkArc VarChar(1) Linked To Archived Doc default=N [N=No, Y=Yes]
  VersionNum nVarChar(11) Version Number
  BSubLineNo Int(11) Base Subrow Number default=-1
  WipDebCred VarChar(1) WIP Account: Debit/Credit Side

# SIVL1 - IVL Layer Level
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LayerID, TransSeq
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No. ->OIVL
  LayerID Int(11) Layer ID
  CalcPrice Num(19,6) Calculated Price
  Balance Num(19,6) Stock Balance
  TransValue Num(19,6) Transaction Value
  LayerInQty Num(19,6) Receipt Quantity
  LayerOutQ Num(19,6) Issue Quantity
  RevalTotal Num(19,6) Inventory Revaluation Total

# SIVL2 - Inventory Components for Production
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, MessageID
Fields (name type(len) description [values] ->parent table):
  Transseq Int(11) Transaction sequence
  MessageID Int(11) Message ID ->OILM
  LineID Int(11) Line ID
  POLine Int(11) Line in Production Order
  ItemType Int(11) Item Type
  ItemCode nVarChar(50) Item No. ->OITM
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  LayerTSeq Int(11) FIFO Layer Transaction Sequence default=-1
  LayerId Int(11) Layer ID default=-1
  Quantity Num(19,6) Quantity
  TotalLC Num(19,6) Inventory Total LC
  BaseAbsEnt Int(11) Abs. Entry of Base Doc. default=-1
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 60=Goods Issue]
  BaseLine Int(11) Base Line Number default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description

# SIVQ - FIFO Queue Working Table
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TRANS_SEQ U: LayerID, TransSeq
  TreeOpenQt: OpenQty, TreeID
Fields (name type(len) description [values] ->parent table):
  TreeID Int(11) Tree ID default=0
  ParentID Int(11) Parent ID default=-1
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TransSeq Int(11) Transaction Sequence No. ->SIVL
  LayerID Int(11) Layer ID
  OpenQty Num(19,6) Open Quantity
  OpenValue Num(19,6) Open Value
  ItemCode nVarChar(50) Item Code ->SITM
  AbsEntry Int(11) Internal ID
  StockActio Int(11) Stock Action Type default=-1 [15=Delivery, 16=Returns, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 18=A/P Invoice, 19=A/P Credit Memo, -2=Opening Balance, 58=Inventory Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfer, 68=Work Instructions, -1=All Transactions, 162=Inventory Revaluation, 69=Landed Costs]
  RemMethod VarChar(1) Quantity Removal Method default=U [U=Unspecified, I=Issue, R=Revaluation]

# SPP1 - Special Prices - Data Areas
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LINENUM, ItemCode, CardCode
  CARD: CardCode
  ITEM: ItemCode
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OSPP
  CardCode nVarChar(15) BP Code ->OSPP
  LINENUM Int(6) Row Number
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount %
  ListNum Int(6) Price List No. default=0 ->OPLN
  FromDate Date(8) Date From
  ToDate Date(8) Date To
  AutoUpdt VarChar(1) Auto Update default=Y [Y=Yes, N=No]
  Expand VarChar(1) Item Details default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0

# SPP2 - Special Prices - Quantity Areas
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SPP2LNum, SPP1LNum, ItemCode, CardCode
  CARD: CardCode
  ITEM: ItemCode
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  SPP1LNum Int(6) Dates Row Number
  SPP2LNum Int(6) Row Number
  Amount Num(19,6) Quantity
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount in %
  UomEntry Int(6) UoM Entry ->OUOM
  LogInstanc Int(11) Log Instance default=0

# TSP1 - Transporter - Transportations
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transporter Abs. Entry
  LineNum Int(11) Line Number
  TransMode Int(11) Mode ->OETM
  VehicleTyp nVarChar(2) Vehicle Type ->OEVT
  VehicleNo nVarChar(15) Vehicle Number
  LogInstanc Int(11) Log Instance default=0

# UBTN - Batch Numbers Master Data
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: SysNumber, ItemCode
  DIST_KEY: DistNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Batch Number
  MnfSerial nVarChar(36) Batch Attribute 1
  LotNumber nVarChar(36) Batch Attribute 2
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Warranty Start Date
  GrntExp Date(8) Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Location
  Status VarChar(1) Status default=0 [0=Released, 1=Not Accessible, 2=Locked]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) Abs. Entry
  ObjType nVarChar(20) Object Type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

# UGP1 - UoM Group Detail
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, UgpEntry
  GROUP U: UomEntry, UgpEntry
Fields (name type(len) description [values] ->parent table):
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  UomEntry Int(11) UoM Abs. Entry ->OUOM
  AltQty Num(19,6) Alternative Quantity
  BaseQty Num(19,6) Base Quantity
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  WghtFactor Int(6) Weight Factor default=0 ->OWGT
  UdfFactor Int(11) UDF Factor default=-1

# UILM - IVI Inventory Log Message
Module: Inventory and Production | 89 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: MessageID
  CARD: BPCardCode
  DocLine: SubLineNum, DocLineNum, DocEntry, TransType
  APPOBJ: AppObjLine, AppObjType, AppObjAbs, ApplObj
  BASEOBJ: BSubLineNo, BaseLine, BaseAbsEnt, BaseType
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID
  DocEntry Int(11) Doc Number
  TransType Int(11) Transaction Type default=-1
  DocLineNum Int(11) Doc Row Number
  Quantity Num(19,6) Quantity in Doc
  EffectQty Num(19,6) Stock Effective Qty
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TotalLC Num(19,6) Inventory Total LC
  TotalFC Num(19,6) Inventory Total FC
  TotalSC Num(19,6) Inventory Total SC
  BaseAbsEnt Int(11) Internal ID of Base Document
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 13=A/R Invoice, 15=Delivery, 16=Returns, 17=Sales Order, 18=A/P Invoice, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase Order, 23=Sales Quotation, 59=Goods Receipt, 67=Inventory Transfer, 69=Landed Costs, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment]
  BaseCurr nVarChar(3) Base Currency
  Currency nVarChar(3) Doc Currency ->OCRN
  AccumType Int(11) Accumulator Type default=0 [0=ACCUM_EMPTY, 1=ACCUM_ON_HAND, 2=ACCUM_COMMITTED, 3=ACCUM_ON_ORDER, 4=ACCUM_CONSIGNATION, 5=ACCUM_COUNTED]
  ActionType Int(11) Action Type default=5 [0=TRANSACTION_UNKNOWN, 1=TRANSACTION_IN, 2=TRANSACTION_OUT, 3=TRANSACTION_SET, 4=TRANSACTION_COMPLETE, 5=EMPTY_TRANSACTION, 6=TRANSACTION_REVALUATION, 7=TRANSACTION_REVALUATION_INCREASE, 8=TRANSACTION_REVALUATION_DECREASE, 9=TRANSACTION_CLOSE_IN, 10=TRANSACTION_CLOSE_OUT, 11=TRANSACTION_NEGATIVE_REVALUATION, 12=TRANSACTION_NULLIFY, 13=TRANSACTION_RESERVE_CI_IN, 14=TRANSACTION_RESERVE_CI_OUT, 15=TRANSACTION_RESERVE_CI_REVAL_INC, 16=TRANSACTION_RESERVE_CI_REVAL_DEC, 17=TRANSACTION_REVAL_PRICE_CHANGE_INCREASE, 18=TRANSACTION_REVAL_PRICE_CHANGE_DECREASE]
  ExpensesLC Num(19,6) Expenses (LC)
  ExpensesFC Num(19,6) Expenses (FC)
  ExpensesSC Num(19,6) Expenses (SC)
  DocDueDate Date(8) Doc. Due Date
  ItemCode nVarChar(50) Item Code ->OITM
  BPCardCode nVarChar(15) Business Partner Code ->OCRD
  DocDate Date(8) Doc Date
  DocRate Num(19,6) Doc. Rate
  Comment nVarChar(254) Comment
  JrnlMemo nVarChar(50) Journal Remarks
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(100) Reference 2
  BaseLine Int(11) Base Row Number default=-1
  SnBType Int(11) Serials and Batches Type default=-1 [0=Batch Numbers Management, 1=Serial Number Management]
  CreateTime Int(6) Generation Time
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  CreateDate Date(8) Creation Date
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  DocPrice Num(19,6) Doc Price
  CardName nVarChar(100) BP Name
  Dscription nVarChar(100) Item Description
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=BOM Component Item, P=Production, T=Template]
  ApplObj Int(11) Applied Object default=-1
  AppObjAbs Int(11) Applied Object Internal ID default=-1
  AppObjType VarChar(1) Applied Object Type
  AppObjLine Int(11) Applied Object Row default=-1
  BASE_REF nVarChar(11) Base Reference
  TransSeqRf Int(11) Transaction Sequence Ref default=-1
  LayerIDRef Int(11) Layer ID Reference default=-1
  VersionNum nVarChar(11) Version Number
  PriceRate Num(19,6) Price Rate
  PriceCurr nVarChar(3) Price Currency ->OCRN
  DocTotal Num(19,6) Document Total
  Price Num(19,6) Price
  CIShbQty Num(19,6) Corr. Inv. Doc. Should Be Qty
  SubLineNum Int(11) Sub Line Number default=-1
  PrjCode nVarChar(20) Project code ->OPRJ
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  TaxDate Date(8) Document Date
  UseDocPric VarChar(1) Use Document Price default=N [Y=Yes, N=No]
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  Location Int(11) Location ->OLCT
  DocPrcRate Num(19,6) Document Price Rate
  DocPrcCurr nVarChar(3) Document Price Currency ->OCRN
  CgsOcrCod nVarChar(8) COGS Distribution Rule ->OOCR
  CgsOcrCod2 nVarChar(8) COGS Distribution Rule 2 ->OOCR
  CgsOcrCod3 nVarChar(8) COGS Distribution Rule 3 ->OOCR
  CgsOcrCod4 nVarChar(8) COGS Distribution Rule 4 ->OOCR
  CgsOcrCod5 nVarChar(8) COGS Distribution Rule 5 ->OOCR
  BSubLineNo Int(11) Base Subrow Number default=-1
  AppSubLine Int(11) Applied Subrow Number default=-1
  UserSign Int(6) User Signature ->OUSR
  SysRate Num(19,6) System Rate
  ExFromRpt VarChar(1) Exclude from Report default=N [Y=Yes, N=No]
  Ref3 nVarChar(11) Reference 3
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  DocAction Int(11) Document Action Type
  UseShpdGd VarChar(1) Use Shipped Goods Account default=N [N=No, Y=Yes]
  AddTotalLC Num(19,6) Additional Total LC
  AddExpLC Num(19,6) Additional Expenses LC
  IsNegLnQty VarChar(1) Negative Line Quantity default=N
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry
  StgDesc nVarChar(100) Stage Description

# UILM1 - Srl & Batch Det of Inv Log Msg
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SysNumber, ItemCode, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  ItemCode nVarChar(50) Item Code ->OITM
  SysNumber Int(11) System Number
  Quantity Num(19,6) Quantity
  MdAbsEntry Int(11) MD Abs Entry

# UILM2 - Inventory Account Substitute
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DebitCredi, AccountId, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  AccountId Int(6) Account ID default=-1
  AcctCode nVarChar(15) Account Code ->OACT
  DebitCredi VarChar(1) Debit or Credit default=U [U=Unknown, D=Debit, C=Credit]

# UILM3 - Non-Inventory and Resource Components Log Msg
Module: Inventory and Production | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, ItemCode, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID Int(11) Message ID ->OILM
  LineID Int(11) Line ID
  POLine Int(11) Line in Production Order
  ItemType Int(11) Item Type
  ItemCode nVarChar(50) Item No. ->OITM
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  Quantity Num(19,6) Quantity
  TotalLC Num(19,6) Inventory Total LC
  BaseAbsEnt Int(11) Abs. Entry of Base Doc. default=-1
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 60=Goods Issue]
  BaseLine Int(11) Base Line Number default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry
  StgDesc nVarChar(100) Stage Description

# UITM - Items
Module: Inventory and Production | 322 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItemCode
  ITEM_NAME: ItemName
  TREE_TYPE: TreeType
  COM_GROUP: CommisGrp
  SALE: SellItem
  PURCHASE: PrchseItem
  INVENTORY: InvntItem
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No.
  ItemName nVarChar(100) Item Description
  FrgnName nVarChar(100) Foreign Name
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  CstGrpCode Int(6) Customs Group default=-1 ->OARG
  VatGourpSa nVarChar(8) Sales Tax Definition ->OVTG
  CodeBars nVarChar(254) Bar Code
  VATLiable VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  PrchseItem VarChar(1) Purchase Item default=Y [Y=Yes, N=No]
  SellItem VarChar(1) Sales Item default=Y [Y=Yes, N=No]
  InvntItem VarChar(1) Inventory Item default=Y [Y=Yes, N=No]
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Qty Ordered by Customers
  OnOrder Num(19,6) Qty Ordered from Vendors
  IncomeAcct nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  MaxLevel Num(19,6) Maximum Inventory Level
  DfltWH nVarChar(8) Default Warehouse
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  SuppCatNum nVarChar(50) Mfr Catalog No.
  BuyUnitMsr nVarChar(100) Purchasing UoM
  NumInBuy Num(19,6) No. of Items per Purchase Unit
  ReorderQty Num(19,6) Required (Purchasing UoM)
  MinLevel Num(19,6) Minimum Inventory Level
  LstEvlPric Num(19,6) Last Evaluated Price
  LstEvlDate Date(8) Date of Last Reval. Price
  CustomPer Num(19,6) Customs Rate
  Canceled VarChar(1) Canceled Item [Yes/No] default=N [Y=Yes, N=No]
  MnufctTime Int(11) Production Date in Days
  WholSlsTax VarChar(1) Tax Rate for Wholesaler
  RetilrTax VarChar(1) Sales Tax in %
  SpcialDisc Num(19,6) Special Discount %
  DscountCod Int(6) Discount Code
  TrackSales VarChar(1) Follow-Up [Yes/No] default=N [Y=Yes, N=No]
  SalUnitMsr nVarChar(100) Sales UoM
  NumInSale Num(19,6) No. of Items per Sales Unit
  Consig Num(19,6) Consignment Goods Whse
  QueryGroup Int(11) Properties default=0
  Counted Num(19,6) Quantity Counted in Inventory
  OpenBlnc Num(19,6) Initial Inventory
  EvalSystem VarChar(1) Valuation Method [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch]
  UserSign Int(6) User Signature ->OUSR
  FREE VarChar(1) Free [Yes/No] default=N [Y=Yes, N=No]
  PicturName nVarChar(200) Picture
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  BlncTrnsfr VarChar(1) Balances Transferred [Yes/No] default=N [Y=Yes, N=No]
  UserText Text(16) Item Remarks
  SerialNum nVarChar(17) Serial Number
  CommisPcnt Num(19,6) % Commission for Item
  CommisSum Num(19,6) Total Commission for Item
  CommisGrp Int(6) Commission Group default=0 ->OCOG
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, P=Production, T=Template]
  TreeQty Num(19,6) No. of Units
  LastPurPrc Num(19,6) Last Purchase Price
  LastPurCur nVarChar(3) Last Purchase Currency
  LastPurDat Date(8) Last Purchase Date
  ExitCur nVarChar(3) Issue Currency
  ExitPrice Num(19,6) Issue Price
  ExitWH nVarChar(8) Release Warehouse
  AssetItem VarChar(1) Fixed Asset Indicator default=N [Y=Yes, N=No]
  WasCounted VarChar(1) Counted default=N [Y=Yes, N=No]
  ManSerNum VarChar(1) Serial No. Management default=N [Y=Yes, N=No]
  SHeight1 Num(19,6) Height 1 - Sales Unit
  SHght1Unit Int(6) Height 1 - UoM for Sales
  SHeight2 Num(19,6) Height 2 - Sales Unit
  SHght2Unit Int(6) Height 2 - UoM for Sales
  SWidth1 Num(19,6) Width 1 - Sales Unit
  SWdth1Unit Int(6) Width 1 - UoM for Sales
  SWidth2 Num(19,6) Width 2 - Sales Unit
  SWdth2Unit Int(6) Width 2 - UoM for Sales
  SLength1 Num(19,6) Length 1 - Sales Unit
  SLen1Unit Int(6) Length 1 - UoM for Sales
  Slength2 Num(19,6) Length 2 - Sales Unit
  SLen2Unit Int(6) Length 2 - UoM for Sales
  SVolume Num(19,6) Volume - Sales Unit
  SVolUnit Int(6) Volume - UoM for Sales
  SWeight1 Num(19,6) Weight 1 - Sales Unit
  SWght1Unit Int(6) Weight 1 - UoM for Sales
  SWeight2 Num(19,6) Weight 2 - Sales Unit
  SWght2Unit Int(6) Weight 2 - UoM for Sales
  BHeight1 Num(19,6) Height 1 - Purchasing Unit
  BHght1Unit Int(6) Height 1 - UoM for Purchasing
  BHeight2 Num(19,6) Height 2 - Purchasing Unit
  BHght2Unit Int(6) Height 2 - UoM for Purchasing
  BWidth1 Num(19,6) Width 1 - Purchasing Unit
  BWdth1Unit Int(6) Width 1 - UoM for Purchasing
  BWidth2 Num(19,6) Width 2 - Purchasing Unit
  BWdth2Unit Int(6) Width 2 - UoM for Purchasing
  BLength1 Num(19,6) Length 1 - Purchase Unit
  BLen1Unit Int(6) Length 1 - UoM for Purchasing
  Blength2 Num(19,6) Length 2 - Purchase Unit
  BLen2Unit Int(6) Length 2 - UoM for Purchasing
  BVolume Num(19,6) Volume - Purchasing Unit
  BVolUnit Int(6) Volume - UoM for Purchasing
  BWeight1 Num(19,6) Weight 1 - Purchasing Unit
  BWght1Unit Int(6) Weight 1 - UoM for Purchasing
  BWeight2 Num(19,6) Weight 2 - Purchasing Unit
  BWght2Unit Int(6) Weight 2 - UoM for Purchasing
  FixCurrCms nVarChar(3) Currency of Fixed Commission
  FirmCode Int(6) Manufacturer default=-1 ->OMRC
  LstSalDate Date(8) Last Sale Date
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
  CreateDate Date(8) Production Date
  UpdateDate Date(8) Date of Update
  ExportCode nVarChar(20) Data Export Code
  SalFactor1 Num(19,6) Sales Factor 1
  SalFactor2 Num(19,6) Sales Factor 2
  SalFactor3 Num(19,6) Sales Factor 3
  SalFactor4 Num(19,6) Sales Factor 4
  PurFactor1 Num(19,6) Purchasing Factor 1
  PurFactor2 Num(19,6) Purchasing Factor 2
  PurFactor3 Num(19,6) Purchasing Factor 3
  PurFactor4 Num(19,6) Purchasing Factor 4
  SalFormula nVarChar(40) Sales Formula
  PurFormula nVarChar(40) Purchasing Formula
  VatGroupPu nVarChar(8) Purchase Tax Definition ->OVTG
  AvgPrice Num(19,6) Item Cost
  PurPackMsr nVarChar(30) Packaging UoM (Purchasing)
  PurPackUn Num(19,6) Quantity per Package (Purchasing)
  SalPackMsr nVarChar(30) Packaging UoM (Sales)
  SalPackUn Num(19,6) Quantity per Package (Sales)
  SCNCounter Int(6) SCN Counter
  ManBtchNum VarChar(1) Manage Batch No. [Yes/No] default=N [Y=Yes, N=No]
  ManOutOnly VarChar(1) Manage SNs Only on Exit default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer, G=Fixed Assets Migration]
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  BlockOut VarChar(1) Force Selection of Serial No. default=Y [Y=Yes, N=No]
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=4 ->ADP1
  SWW nVarChar(16) Additional Identifier
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  DocEntry Int(11) Internal Number
  ExpensAcct nVarChar(15) Expense Account ->OACT
  FrgnInAcct nVarChar(15) Revenue Account - Foreign ->OACT
  ShipType Int(6) Shipping Type ->OSHP
  GLMethod VarChar(1) Set G/L Accounts By default=W [W=Warehouse, C=Item Group, L=Item Level]
  ECInAcct nVarChar(15) Revenue Account - EU
  FrgnExpAcc nVarChar(15) Expense Account - Foreign
  ECExpAcc nVarChar(15) Expense Account - EU
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, U=Use Tax, N=No Tax]
  ByWh VarChar(1) Manage Inventory by Warehouse
  WTLiable VarChar(1) WTax Liable default=Y [Y=Yes, N=No]
  ItemType VarChar(1) Item Type default=I [I=Items, L=Labor, T=Travel, F=Fixed Assets]
  WarrntTmpl nVarChar(20) Warranty Template ->OCTT
  BaseUnit nVarChar(20) Base Unit Name
  CountryOrg nVarChar(3) Country of Origin
  StockValue Num(19,6) Inventory Value
  Phantom VarChar(1) Phantom Item default=N [Y=Yes, N=No]
  IssueMthd VarChar(1) Issue Method [B=Backflush, M=Manual]
  FREE1 VarChar(1) Yield in %
  PricingPrc Num(19,6) Pricing Percentage
  MngMethod VarChar(1) Management Method default=R [A=On Every Transaction, R=On Release Only]
  ReorderPnt Num(19,6) Reorder Point
  InvntryUom nVarChar(100) Inventory UoM
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  IndirctTax VarChar(1) Indirect Tax default=N [Y=Yes, N=No]
  TaxCodeAR nVarChar(8) Tax Code (A/R) ->OSTC
  TaxCodeAP nVarChar(8) Tax Code (A/P) ->OSTC
  OSvcCode Int(11) Outgoing Service Code default=-1 ->OSCD
  ISvcCode Int(11) Incoming Service Code default=-1 ->OSCD
  ServiceGrp Int(11) Service Group default=-1 ->OSGP
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  ServiceCtg Int(11) Service Category default=-1 [-1=] ->OSCG
  ItemClass VarChar(1) Service or Material default=2 [2=Material, 1=Service]
  Excisable VarChar(1) Excisable [Yes/No] default=N [Y=Yes, N=No]
  ChapterID Int(11) Chapter ID default=-1 ->OCHP
  NotifyASN nVarChar(40) Notification Available SNs
  ProAssNum nVarChar(20) Provisional Assessment No.
  AssblValue Num(19,6) Assessable Value
  DNFEntry Int(11) DNF Code Entry default=-1 ->ODNF
  UserSign2 Int(6) Updating User ->OUSR
  Spec nVarChar(30) Item Specification
  TaxCtg nVarChar(4) Tax Category
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  FuelCode Int(11) Fuel default=-1 ->OBFI
  BeverTblC nVarChar(2) Beverage Table ->OBSI
  BeverGrpC nVarChar(2) Beverage Group ->OBSI
  BeverTM Int(11) Beverage Brand default=-1 ->OBNI
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  ToleranDay Int(11) Tolerance Days
  UgpEntry Int(11) UoM Group ->OUGP
  PUoMEntry Int(11) Default Purchase UoM ->OUOM
  SUoMEntry Int(11) Default Sales UoM ->OUOM
  IUoMEntry Int(11) Inventory UoM ->OUOM
  IssuePriBy Int(6) Issue Primarily By SnB or Bin [0=Issue Primarily by Serial/Batch Number, 1=Issue Primarily by Bin Location]
  AssetClass nVarChar(20) Asset Class ->OACS
  AssetGroup nVarChar(15) Asset Group ->OAGS
  InventryNo nVarChar(12) Inventory Number of Asset
  Technician Int(11) Technician of Fixed Asset ->OHEM
  Employee Int(11) Employee of Fixed Asset ->OHEM
  Location Int(11) Location ->OLCT
  StatAsset VarChar(1) Owned by Company default=N [Y=Yes, N=No]
  Cession VarChar(1) Cession default=N [Y=Yes, N=No]
  DeacAftUL VarChar(1) Deactivate After Useful Life default=N [Y=Yes, N=No]
  AsstStatus VarChar(1) Asset Status default=N [N=New, A=Active, I=Inactive]
  CapDate Date(8) Capitalization Date
  AcqDate Date(8) Acquisition Date
  RetDate Date(8) Retirement Date
  GLPickMeth VarChar(1) G/L Account Pick Method default=A [A=General, W=Warehouse, C=Item Group]
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  MgrByQty VarChar(1) Manage Asset by Quantity default=N [Y=Yes, N=No]
  AssetRmk1 nVarChar(100) Asset Remark 1
  AssetRmk2 nVarChar(100) Asset Remark 2
  AssetAmnt1 Num(19,6) Asset Amount 1
  AssetAmnt2 Num(19,6) Asset Amount 2
  DeprGroup nVarChar(15) Depreciation Group ->OADG
  AssetSerNo nVarChar(32) Asset Serial Number
  CntUnitMsr nVarChar(100) Inventory Counting UoM Name
  NumInCnt Num(19,6) No. of Items per Counting Unit
  INUoMEntry Int(11) Inventory Counting UoM Entry ->OUOM
  OneBOneRec VarChar(1) One Batch One Receipt default=N [Y=Yes, N=No]
  RuleCode nVarChar(2) Checking Rule Code ->ODCR
  ScsCode nVarChar(10) Scs Code
  SpProdType nVarChar(2) Special Product Type [MT=Cellular Phones, IO=Integrated Circuits]
  IWeight1 Num(19,6) Weight 1 - Inventory
  IWght1Unit Int(6) Weight 1 - Inventory Unit
  IWeight2 Num(19,6) Weight 2 - Inventory
  IWght2Unit Int(6) Weight 2 - Inventory Unit
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VirtAstItm VarChar(1) Virtual Asset Item default=N [N=No, Y=Yes]
  SouVirAsst nVarChar(50) Source Virtual Asset Item ->OITM
  InCostRoll VarChar(1) Include in Prod. Cost Rollup default=Y [Y=Yes, N=No]
  PrdStdCst Num(19,6) Production Std Cost
  EnAstSeri VarChar(1) Enforce Asset Serial Numbers default=N [Y=Yes, N=No]
  LinkRsc nVarChar(50) Linked Resource ->ORSC
  OnHldPert Num(19,6) Capital Goods On Hold Percent
  onHldLimt Num(19,6) Capital Goods on Hold Limit
  PriceUnit Int(11) Pricing Unit ->OUOM
  GSTRelevnt VarChar(1) GST Relevant default=N [Y=Yes, N=No]
  SACEntry Int(11) SAC Entry default=-1 ->OSAC
  GstTaxCtg VarChar(1) GST Tax Category default=R [R=Regular, N=Nil Rated, E=Exempt]
  AssVal4WTR Num(19,6) Assessable Value for WTR
  ExcImpQUoM Int(11) Default Excise Imported Quantity UoM [112=Liters, m3, 168=Tonne, metric ton (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcFixAmnt Num(19,6) Default Excise Fixed Amount
  ExcRate Num(19,6) Default Excise Rate
  SOIExc VarChar(1) SOI Excisable default=4 [1=Excisable, 2=Exemption of excises, 3=Excises are paid to another authority, 4=Not Excisable]
  TNVED nVarChar(10) TNVED Code
  Imported VarChar(1) Imported Item default=N [Y=Yes, N=No]
  AutoBatch VarChar(1) Automatic Batch Creation default=N [Y=Yes, N=No]
  CstmActing VarChar(1) Customer Accounting default=N [N=No, Y=Yes]

# UITW - Items - Warehouse
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WhsCode, ItemCode
  WHS: WhsCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->UITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Defined
  OnOrder Num(19,6) Ordered
  Consig Num(19,6) Consignment Goods Whse
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  MinStock Num(19,6) Minimum Inventory
  MaxStock Num(19,6) Maximum Inventory
  MinOrder Num(19,6) Min. Order
  AvgPrice Num(19,6) Average Price
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Transfer Acct ->OACT
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns Account ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Revenue Account - EU ->OACT
  EUExpensAc nVarChar(15) Expense Account - EU ->OACT
  FrRevenuAc nVarChar(15) Revenue Account - Foreign ->OACT
  FrExpensAc nVarChar(15) Expense Account - Foreign ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  PriceDifAc nVarChar(15) Price Differences Account
  ExchangeAc nVarChar(15) Exchange Rate Differences Account
  BalanceAcc nVarChar(15) Goods Clearing Account
  PurchaseAc nVarChar(15) Purchase Account
  PAReturnAc nVarChar(15) Purchase Return Account
  PurchOfsAc nVarChar(15) Purchase Offset Account
  ShpdGdsAct nVarChar(15) Shipped Goods Account
  VatRevAct nVarChar(15) VAT in Revenue Account
  StockValue Num(19,6) Inventory Value
  DecresGlAc nVarChar(15) G/L Decrease Account
  IncresGlAc nVarChar(15) G/L Increase Account
  StokRvlAct nVarChar(15) Stock Inflation Adjust Account
  StkOffsAct nVarChar(15) Stock Inflation Offset Account
  WipAcct nVarChar(15) WIP Inventory Account
  WipVarAcct nVarChar(15) WIP Inventory Variance Account
  CostRvlAct nVarChar(15) Cost Inflation Account
  CstOffsAct nVarChar(15) Cost Inflation Offset Account
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  Object nVarChar(20) Object Type - History default=31
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  ARCMAct nVarChar(15) Sales Credit Account
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign
  ARCMEUAct nVarChar(15) Sales Credit Account - EU
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account
  APCMAct nVarChar(15) Purchase Credit Account
  APCMFrnAct nVarChar(15) Purchase Credit Account - Foreign
  APCMEUAct nVarChar(15) Purchase Credit Account - EU
  RevRetAct nVarChar(15) Revenue Returns Account
  NegStckAct nVarChar(15) Neg. Inventory Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account
  PurBalAct nVarChar(15) Purchase Balance Account
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  Freezed VarChar(1) Item Frozen in Warehouse default=N [Y=Yes, N=No]
  FreezeDoc Int(11) INC Document Frozen By ->OINC
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account

# UIVE - FIFO Based Sales Return
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TRANS_SEQ: LayerID, TransSeq
  TreeID: TreeID
Fields (name type(len) description [values] ->parent table):
  TreeID Int(11) Tree ID default=0
  ParentID Int(11) Parent ID default=-1
  AbsEntry Int(11) Internal Number
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TransSeq Int(11) Transaction Sequence No. ->UIVL
  LayerID Int(11) Layer ID
  LayerInQty Num(19,6) Layer In Quantity
  LayerOutQ Num(19,6) Layer Out Quantity
  LayerVal Num(19,6) Layer Value
  ItemCode nVarChar(50) Item Code ->UITM
  EntryTreeI Int(11) Entry Tree ID
  LayerCogs Num(19,6) Layer - Cost of Goods Sold

# UIVK - IVL Vs OINM Keys
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: INMTransSe
  TRANSSEQ U: LayerID, TransSeq
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No.
  LayerID Int(11) Layer ID
  RootID Int(11) Root ID
  TransNum Int(11) Transaction Number
  Instance Int(11) Instance default=0
  INMTransSe Int(11) INM_Transaction Sequence No.

# UIVL - Whse Journal
Module: Inventory and Production | 78 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TransSeq
  ITEM: ItemCode
  CURRENCY: Currency
  DOCDATE: DocDate
  DOCENTRY: DocLineNum, TransType, CreatedBy
  MESSAGEID: MessageID
  TREEID: TreeID
Fields (name type(len) description [values] ->parent table):
  TransType Int(11) Transaction Type default=-1 [15=Delivery, 16=Returns, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 18=A/P Invoice, 19=A/P Credit Memo, -2=Opening Balance, 58=Inventory Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfer, 68=Work Instructions, -1=All Transactions, 162=Inventory Revaluation, 69=Landed Costs]
  CreatedBy Int(11) Document No. Created
  BASE_REF nVarChar(11) Base Reference
  DocLineNum Int(11) Row Number in Document
  DocDate Date(8) Posting Date
  CreateTime Int(6) Generation Time
  ItemCode nVarChar(50) Item No. ->UITM
  InQty Num(19,6) Receipt Quantity
  OutQty Num(19,6) Issue Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  TrnsfrAct nVarChar(15) Transfer Account ->OACT
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  ReturnAct nVarChar(15) Returning Account ->OACT
  ExcRateAct nVarChar(15) Exchange Rate Differences Acct ->OACT
  ClearAct nVarChar(15) Goods Clearing Account ->OACT
  CostAct nVarChar(15) COGS Account ->OACT
  WipAct nVarChar(15) WIP Inventory Account ->OACT
  OpenStock Num(19,6) Open Sum Inventory Value
  CreateDate Date(8) Creation Date
  PriceDiff Num(19,6) Price Difference Value
  TransSeq Int(11) Transaction Sequence No. default=0
  InvntAct nVarChar(15) Inventory Account ->OACT
  SubLineNum Int(11) Subrow Number default=-1
  AppObjLine Int(11) Applied Object Row default=-1
  Expenses Num(19,6) Inventory Expenses
  OpenExp Num(19,6) Open Expenses Value
  Allocation Num(19,6) Allocation Amount
  OpenAlloc Num(19,6) Open Allocation Value
  ExpAlloc Num(19,6) Expenses Allocation Value
  OExpAlloc Num(19,6) Open Expenses Allocation Value
  OpenPDiff Num(19,6) Open Price Diff. Value
  ExchDiff Num(19,6) Exchange Rate Difference Value
  OpenEDiff Num(19,6) Open Exchange Rate Diff. Value
  NegInvAdjs Num(19,6) Negative Inventory Adjustment Value
  OpenNegInv Num(19,6) Open Negative Adjustment
  NegStckAct nVarChar(15) Neg. Inventory Adjustment Acct ->OACT
  BTransVal Num(19,6) Base Transaction Value
  VarVal Num(19,6) Variance Value
  BExpVal Num(19,6) Base Freight Value
  CogsVal Num(19,6) COGS Value
  BNegAVal Num(19,6) Base Negative Adjustment Amt
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  IOffIncVal Num(19,6) Inv. Offset Increase Value
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  DOffDecVal Num(19,6) Inv. Offset Decrease Value
  DecAcc nVarChar(15) G/L Decrease Account ->OACT
  DecVal Num(19,6) G/L Decrease Value
  WipVal Num(19,6) WIP Inventory Value
  WipVarAcc nVarChar(15) WIP Variance Account ->OACT
  WipVarVal Num(19,6) WIP Variance Value
  IncAct nVarChar(15) G/L Increase Account
  IncVal Num(19,6) G/L Increase Value
  ExpCAcc nVarChar(15) Expense Clearing Account ->OACT
  CostMethod VarChar(1) Costing Method default=N [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch, N=None]
  MessageID Int(11) Message ID ->UILM
  LocType Int(11) Location Type
  LocCode nVarChar(8) Warehouse Code
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, Y=Year Transfer]
  PostStatus VarChar(1) Posting Status default=N [N=None, P=Partial, C=Complete]
  SumStock Num(19,6) Sum Inventory Value
  OpenCogs Num(19,6) Open COGS Value
  OpenQty Num(19,6) Open Quantity
  TreeID Int(11) Tree ID default=-1
  ParentID Int(11) Parent ID default=-1
  PAOffAcc nVarChar(15) Purchase Offset Account ->OACT
  PAOffVal Num(19,6) Purchase Offset Value
  OpenPAOff Num(19,6) Open Purchase Offset Value
  PAAcc nVarChar(15) Purchase Account ->OACT
  PAVal Num(19,6) Purchase Account Value
  OpenPA Num(19,6) Open Purchase Value
  LinkArc VarChar(1) Linked To Archived Doc default=N [N=No, Y=Yes]
  VersionNum nVarChar(11) Version Number
  BSubLineNo Int(11) Base Subrow Number default=-1
  WipDebCred VarChar(1) WIP Account: Debit/Credit Side

# UIVL1 - IVL Layer Level
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LayerID, TransSeq
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No.
  LayerID Int(11) Layer ID
  CalcPrice Num(19,6) Calculated Price
  Balance Num(19,6) Stock Balance
  TransValue Num(19,6) Transaction Value
  LayerInQty Num(19,6) Receipt Quantity
  LayerOutQ Num(19,6) Issue Quantity
  RevalTotal Num(19,6) Inventory Revaluation Total

# UIVL2 - Inventory Components for Production
Module: Inventory and Production | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, MessageID
Fields (name type(len) description [values] ->parent table):
  Transseq Int(11) Transaction sequence
  MessageID Int(11) Message ID ->OILM
  LineID Int(11) Line ID
  POLine Int(11) Line in Production Order
  ItemType Int(11) Item Type
  ItemCode nVarChar(50) Item No. ->OITM
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  LayerTSeq Int(11) FIFO Layer Transaction Sequence default=-1
  LayerId Int(11) Layer ID default=-1
  Quantity Num(19,6) Quantity
  TotalLC Num(19,6) Inventory Total LC
  BaseAbsEnt Int(11) Abs. Entry of Base Doc. default=-1
  BaseType Int(11) Base Transaction Type default=-1 [-1=, 0=, 60=Goods Issue]
  BaseLine Int(11) Base Line Number default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description

# UIVQ - FIFO Queue Working Table
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TRANS_SEQ U: LayerID, TransSeq
  TreeOpenQt: OpenQty, TreeID
Fields (name type(len) description [values] ->parent table):
  TreeID Int(11) Tree ID default=0
  ParentID Int(11) Parent ID default=-1
  LocType Int(6) Location Type
  LocCode nVarChar(8) Location Code
  TransSeq Int(11) Transaction Sequence No. ->UIVL
  LayerID Int(11) Layer ID
  OpenQty Num(19,6) Open Quantity
  OpenValue Num(19,6) Open Value
  ItemCode nVarChar(50) Item Code ->UITM
  AbsEntry Int(11) Internal Number
  StockActio Int(11) Stock Action Type default=-1 [15=Delivery, 16=Returns, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 18=A/P Invoice, 19=A/P Credit Memo, -2=Opening Balance, 58=Inventory Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfer, 68=Work Instructions, -1=All Transactions, 162=Inventory Revaluation, 69=Landed Costs]
  RemMethod VarChar(1) Quantity Removal Method default=U [U=Unspecified, I=Issue, R=Revaluation]

# USRN - Serial Numbers Master Data
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SYSTEM_KEY U: SysNumber, ItemCode
  DIST_KEY: DistNumber, ItemCode
  LOT_KEY: LotNumber, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SysNumber Int(11) System Number
  DistNumber nVarChar(36) Serial Number
  MnfSerial nVarChar(36) Manufacturer Serial No.
  LotNumber nVarChar(36) Lot Number
  ExpDate Date(8) Expiration Date
  MnfDate Date(8) Manufacturing Date
  InDate Date(8) Admission Date
  GrntStart Date(8) Mfr Warranty Start Date
  GrntExp Date(8) Mfr Warranty End Date
  CreateDate Date(8) Creation Date
  Location nVarChar(100) Location
  Status VarChar(1) Status [0=Available, 1=Unavailable, 2=Allocated]
  Notes Text(16) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  AbsEntry Int(11) Abs. Entry
  ObjType nVarChar(20) Object Type
  itemName nVarChar(100) Item Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CostTotal Num(19,6) Total Cost of Batches
  Quantity Num(19,6) Quantity
  QuantOut Num(19,6) Output Quantity
  PriceDiff Num(19,6) Price Difference
  Balance Num(19,6) Batch Balance
  TrackingNt Int(11) CCD Tracking Note ->OTCN
  TrackiNtLn Int(11) CCD Tracking Note Line ->TCN1
  SumDec Int(6) Totals Accuracy for SnB

# UWKO - Production Instructions
Module: Inventory and Production | 31 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: OrderNum
  SERIAL U: Instance, SerialNum
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  OrderNum Int(11) Instruction Key default=0
  Status VarChar(1) Processing Status default=O [O=Work Instructions, I=Work Instructions, E=Production Completed]
  Canceled VarChar(1) Order Canceled Yes/No default=N [Y=Canceled, N=Not Canceled]
  OrderDate Date(8) Order Date
  ProdctDate Date(8) Work Start Date
  ExpFinishD Date(8) Expected Completion Date
  FinishDate Date(8) Work Finish Date
  FinishUser nVarChar(8) Name of Person Receiving Instructions ->OUSR
  CardCode nVarChar(15) Sold-To-Party Code ->OCRD
  CustomName nVarChar(100) Sold-To-Party Name
  NumInCustm nVarChar(16) Customer Ref. No.
  TotalOrder Num(19,6) Order Total
  TotalCurr nVarChar(3) Total Currency
  DocTime Int(6) Generation Time
  Memo nVarChar(254) Remarks
  SerialNum Int(11) Instruction Number
  CntctCode Int(11) Contact Person default=0 ->OCPR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  Series Int(11) Series ->NNM1
  ActWorkCod nVarChar(15) Active Account Code ->OACT
  ActWorkSum Num(19,6) Work Total
  JrnlMemo nVarChar(50) Journal Remarks
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ObjType nVarChar(20) Object Type default=68 ->ADP1
  UserSign Int(6) User Signature ->OUSR
  PriceList Int(6) Price List default=1 ->OPLN
  FinncPriod Int(11) Posting Period ->OFPR
  SysRate Num(19,6) System Rate

# UWKO1 - Production Instructions - Rows
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, OrderNum
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  OrderNum Int(11) Instruction Key ->OWKO
  LineID Int(11) Row Number default=0
  ItemCode nVarChar(50) Item No. ->OITT
  Descript nVarChar(100) Item Description
  Quantity Num(19,6) Item Quantity
  Price Num(19,6) Item Price
  Currency nVarChar(3) Price Currency ->OCRN
  WhsCode nVarChar(8) Item Warehouse ->OWHS
  FinncPriod Int(11) Posting Period ->OFPR
  ActWorkCod nVarChar(15) Active Account Code ->OACT
  ActWorkSum Num(19,6) Total Work
  ProdUpgNum Int(11) Production Upgrade No. ->OWOR

# UWO2 - Production Order - Base
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BaseLine, BaseEntry, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  BaseEntry Int(11) Production Order Base Entry ->RDR1
  BaseNum Int(11) Production Order Base Number
  BaseLine Int(11) Production Order Base Line
  LogInstanc Int(11) Log Instance default=0

# UWOR - Production Order
Module: Inventory and Production | 57 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM U: PIndicator, DocNum
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series default=0 ->NNM1
  ItemCode nVarChar(50) Product No. ->OITT
  Status VarChar(1) Production Order Status default=P [P=Planned, R=Released, L=Closed, C=Canceled]
  Type VarChar(1) Production Order Type default=S [S=Standard, P=Special, D=Disassembly]
  PlannedQty Num(19,6) Planned Quantity - Header
  CmpltQty Num(19,6) Completed Quantity
  RjctQty Num(19,6) Rejected Quantity
  PostDate Date(8) Order Date
  DueDate Date(8) Due Date
  OriginAbs Int(11) Production Order Origin Entry
  OriginNum Int(11) Production Order Origin Number
  OriginType VarChar(1) Production Order Origin default=M [M=Manual, R=MRP, S=Sales Order, U=Upgrade]
  UserSign Int(6) User Signature ->OUSR
  Comments nVarChar(254) Remarks
  CloseDate Date(8) Closing Date
  RlsDate Date(8) Release Date
  CardCode nVarChar(15) Customer Code ->OCRD
  Warehouse nVarChar(8) Warehouse ->OWHS
  Uom nVarChar(100) Inv. UoM in Production Order
  LineDirty Int(11) Line Modified
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  CreateDate Date(8) Creation Date
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  PIndicator nVarChar(10) Period Indicator ->OPID
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  Project nVarChar(20) Project Code ->OPRJ
  SupplCode nVarChar(254) Supplementary Code
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  PickRmrk nVarChar(254) Pick Remarks
  SysCloseDt Date(8) System Closing Date
  SysCloseTm Int(6) System Closing Time
  CloseVerNm nVarChar(11) Closing Version Number
  StartDate Date(8) Start Date
  ObjType nVarChar(20) Object Type default=202
  ProdName nVarChar(100) Product Description
  Priority Int(6) Priority default=100
  RouDatCalc VarChar(1) Routing Date Calculation default=S [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  UpdAlloc VarChar(1) Update Allocation default=M [M=Manual, A=Auto]
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VersionNum nVarChar(11) Version Number
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SAPPassprt Text(16) Extended SAP Passport

# UWOR1 - Production Order - Rows
Module: Inventory and Production | 37 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  VISORDER U: VisOrder, DocEntry
  ITEM_WHS: wareHouse, ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item No.
  BaseQty Num(19,6) Base Quantity
  PlannedQty Num(19,6) Planned Quantity - Rows
  IssuedQty Num(19,6) Issued Quantity
  IssueType VarChar(1) Production Order Issue Type [M=Manual, B=Backflush]
  wareHouse nVarChar(8) Warehouse ->OWHS
  VisOrder Int(11) Visual Order
  WipActCode nVarChar(15) WIP Account Code ->OACT
  CompTotal Num(19,6) Total Completed Sum
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  LocCode Int(11) Location Code ->OLCT
  LogInstanc Int(11) Log Instance default=0
  Project nVarChar(20) Project Code ->OPRJ
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  ItemType Int(11) Item Type default=4 [4=Item, 290=Resource, -18=Text]
  AdditQty Num(19,6) Additional Quantity
  LineText Text(16) Row Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Release for Picking, P=Partially Picked]
  PickQty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick List ID Number
  ReleaseQty Num(19,6) Released Quantity
  ResAlloc VarChar(1) Resource Allocation [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  StageId Int(11) Stage ID
  BaseQtyNum Num(19,6) Base Quantity Numerator
  BaseQtyDen Num(19,6) Base Quantity Denominator
  ReqDays Num(19,6) Required Days default=0
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  Status VarChar(1) Stage Status default=P [P=Planned, I=In Progress, C=Complete]

# UWOR3 - Production Order - Closure
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LayerID, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number
  LineNum Int(11) Row Number
  LayerID Int(11) Layer ID
  Quantity Num(19,6) Quantity
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RToStockSc Num(19,6) Reval. Amt Posted to Stock SC
  WhsCode nVarChar(8) Warehouse Code
  IVLTransSe Int(11) IVL Transaction Sequence No.
  IVLLayerID Int(11) IVL Layer ID
  SnbSysNum Int(11) SNB System Number
  SnbAbsEnt Int(11) SNB Abs. Entry
  LogInstanc Int(11) Log Instance default=0
  INMSubLine Int(11) INM Subrow Number default=-1

# UWOR4 - Production Order - Route Stages
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StageId, DocEntry
  SEQUENCE U: SeqNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  Status VarChar(1) Stage Status default=P [P=Planned, I=In Progress, C=Complete]
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  ReqDays Num(19,6) Required Days default=0
  WaitDays Num(19,6) Waiting Days default=0

# UWOR5 - Production Order - Document Reference Information
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number
  ObjType nVarChar(20) Object Type default=202
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks

# VLG1 - Validation of Recalc. From To
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RecNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Unique Key ->IVLG
  RecNum Int(11) Record Number
  FromSysDat Date(8) From System Date
  FromDocNum Int(11) From Document Number
  FromDocTyp Int(6) From Document Type
  ToSysDate Date(8) To System Date
  ToDocNum Int(11) To Document Number
  ToDocType Int(6) To Document Type
  CalRecOINM Int(11) Calculated Record in OINM
  LastCalcTS Int(11) Last Calculated Trans. Seq.
  SumTranVal Num(19,6) Sum of Transaction Value
  StrFld nVarChar(50) General String Field
  NumFld Int(11) General Number Field

# WKO1 - Production Instructions - Rows
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, OrderNum
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  OrderNum Int(11) Instruction Key ->OWKO
  LineID Int(11) Row Number default=0
  ItemCode nVarChar(50) Item No. ->OITT
  Descript nVarChar(100) Item Description
  Quantity Num(19,6) Item Quantity
  Price Num(19,6) Item Price
  Currency nVarChar(3) Price Currency ->OCRN
  WhsCode nVarChar(8) Item Warehouse ->OWHS
  FinncPriod Int(11) Posting Period ->OFPR
  ActWorkCod nVarChar(15) Active Account Code ->OACT
  ActWorkSum Num(19,6) Total Work
  ProdUpgNum Int(11) Production Upgrade No. ->OWOR

# WOR1 - Production Order - Rows
Module: Inventory and Production | 37 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  VISORDER U: VisOrder, DocEntry
  ITEM_WHS: wareHouse, ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item No.
  BaseQty Num(19,6) Base Quantity
  PlannedQty Num(19,6) Planned Quantity - Rows
  IssuedQty Num(19,6) Issued Quantity
  IssueType VarChar(1) Production Order Issue Type [M=Manual, B=Backflush]
  wareHouse nVarChar(8) Warehouse ->OWHS
  VisOrder Int(11) Visual Order
  WipActCode nVarChar(15) WIP Account Code ->OACT
  CompTotal Num(19,6) Total Completed Sum
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  LocCode Int(11) Location Code ->OLCT
  LogInstanc Int(11) Log Instance default=0
  Project nVarChar(20) Project Code ->OPRJ
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  ItemType Int(11) Item Type default=4 [4=Item, 290=Resource, -18=Text]
  AdditQty Num(19,6) Additional Quantity
  LineText Text(16) Row Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Release for Picking, P=Partially Picked]
  PickQty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick List ID Number
  ReleaseQty Num(19,6) Released Quantity
  ResAlloc VarChar(1) Resource Allocation [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  StageId Int(11) Stage ID
  BaseQtyNum Num(19,6) Base Quantity Numerator
  BaseQtyDen Num(19,6) Base Quantity Denominator
  ReqDays Num(19,6) Required Days default=0
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  Status VarChar(1) Stage Status default=P [P=Planned, I=In Progress, C=Complete]

# WOR2 - Production Order - Base
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BaseLine, BaseEntry, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  BaseEntry Int(11) Production Order Base Entry ->ORDR
  BaseNum Int(11) Production Order Base Number
  BaseLine Int(11) Production Order Base Line
  LogInstanc Int(11) Log Instance default=0

# WOR2V - Production Order - Base
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BaseEntry, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  BaseEntry Int(11) Production Order Base Entry ->ORDR
  BaseNum Int(11) Production Order Base Number
  CardCode nVarChar(15) Customer Code
  PostDate nVarChar(8) Posting Date
  DueDate nVarChar(8) Due Date
  DocTotal Num(19,6) Document Total
  Remark nVarChar(254) Document Remarks
  DocCur nVarChar(3) Document Currency

# WOR3 - Production Order - Closure
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LayerID, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  LineNum Int(11) Row Number
  LayerID Int(11) Layer ID
  Quantity Num(19,6) Quantity
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RToStockSc Num(19,6) Reval. Amt Posted to Stock SC
  WhsCode nVarChar(8) Warehouse Code
  IVLTransSe Int(11) IVL Transaction Sequence No.
  IVLLayerID Int(11) IVL Layer ID
  SnbSysNum Int(11) SNB System Number
  SnbAbsEnt Int(11) SNB Abs. Entry
  LogInstanc Int(11) Log Instance default=0
  INMSubLine Int(11) INM Subrow Number default=-1

# WOR4 - Production Order - Route Stages
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StageId, DocEntry
  SEQUENCE U: SeqNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  StageId Int(11) Stage ID
  SeqNum Int(11) Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  Name nVarChar(100) Stage Name
  LogInstanc Int(11) Log Instance default=0
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  Status VarChar(1) Stage Status default=P [P=Planned, I=In Progress, C=Complete]
  RtCalcProp Num(19,6) Routing Calculation Proportion default=100
  ReqDays Num(19,6) Required Days default=0
  WaitDays Num(19,6) Waiting Days default=0

# WOR5 - Production Order - Document Reference Information
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number
  ObjType nVarChar(20) Object Type default=202
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order]
  IssueDate Date(8) Date of Issue
  Remark nVarChar(254) Remarks

# WTC1 - WTax Certificates - WT Groups in Certificates
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineId Int(11) Row Number
  WtAbsEntry Int(11) Internal Number
  WTPercent Num(19,6) WTax Rate
  SumVatAmnt Num(19,6) Sum of VAT Amount
  SumDocTot Num(19,6) Sum of Doc. Total Amount
  SumBaseAmn Num(19,6) Sum of Base Amount
  SumAccumAm Num(19,6) Sum of Accumulated Amount
  SumPercpAm Num(19,6) Sum of Perception Amount

# WTC2 - WTax Certificates - Docs in WT Groups
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, BaseLineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BaseLineId Int(11) Base Line Number
  LineId Int(11) Line Number
  DocEntry Int(11) Internal Number
  DocObjType nVarChar(20) Doc. Object Type
  VatAmnt Num(19,6) VAT Amount
  DocTot Num(19,6) Doc. Total Amount
  WTBaseAmnt Num(19,6) WTax Base Amount
  WTAccAmnt Num(19,6) Accumulated Amount
  WTPercpAm Num(19,6) WTax Perception Amount
  WTPercent Num(19,6) WTax Rate

# WTQ1 - Inventory Transfer Request - Rows
Module: Inventory and Production | 287 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseLine, BaseType, BaseEntry
  VIS_ORDER: VisOrder, DocEntry
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: OpenQty, WhsCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 67=Warehouse Transfers]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Purchase Delivery Notes, 59=Inventory General Entry, 67=Warehouse Transfers]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(100) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price after Discount
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total (FC)
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount (FC)
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Base Price for Gross Profit
  PriceBefDi Num(19,6) Unit Price
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  SubCatNum nVarChar(50) Customer/Vendor Cat. No. ->OSCN
  BaseCard nVarChar(15) Base BP Code ->OCRD
  TotalSumSy Num(19,6) Row Total (SC)
  OpenSumSys Num(19,6) Open Amount (SC)
  InvntSttus VarChar(1) Warehouse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Profit Center ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Rate per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Volume
  VolUnit Int(6) Volume UoM
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) Additional Identifier
  VatSum Num(19,6) Total Tax
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Internal ID
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Backorder [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick List ID Number
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) Applied Tax
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) Tax Discount %
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatlF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Was/Should Be default=S [W=Was, S=Should Be]
  ToStock Num(19,6) Corr. Invoice Amt to Inventory
  ToDiff Num(19,6) Corr. Invoice Amount to Diff.
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total Including Tax
  CountryOrg nVarChar(3) Country of Origin
  StckDstSum Num(19,6) Stock Distribution Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Row Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Item Cost
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inventory Journal Pr.
  StckDstFc Num(19,6) Stock Distribution Sum (FC)
  StckDstSc Num(19,6) Stock Distribution Sum (SC)
  LstByDsFc Num(19,6) Last Buy Distribute Sum (FC)
  LstByDsSc Num(19,6) Last Buy Distribute Sum (SC)
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-To Description
  StckAppD Num(19,6) Stock Distrib. - Applied Sum
  StckAppDFC Num(19,6) Stock Dist. - Applied Sum (FC)
  StckAppDSC Num(19,6) Stock Dist. - Applied Sum (SC)
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total (FC)
  GTotalSC Num(19,6) Gross Total (SC)
  DistribExp VarChar(1) Distribute Freight Charges [Y=Yes, N=No]
  DescOW VarChar(1) Description Overwritten default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) Remarks overwritten default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied (FC)
  VatWoDpmSc Num(19,6) Tax Before DPM Applied (SC)
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) Withholding Tax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Profit Center Code ->OOCR
  CiOppLineN Int(11) Row Number of Associated Row default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Profit Center Code 2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Profit Center Code 3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Profit Center Code 4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Profit Center Code 5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sale UoM if Base Unit
  NumPerMsr2 Num(19,6) Pur/Sale UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List - Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts - Discount Groups, V=Inactive Price List - Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts - Discount Groups, 2=Active Price List, 7=Active Price List - Discount Groups, 5=Inactive Price List, 6=Inactive Price List - Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No.
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others, =]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# WTQ10 - Inventory Transfer Request - Row Structure
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocEntry
  SECONDARY U: OrderNum, AftLineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1

# WTQ11 - Inv. Transfer Request - Drawn Dpm Det.
Module: Inventory and Production | 70 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
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
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax Liable default=N [N=No, Y=Yes]
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
  DctSum Num(19,6) Deductible Sum (LC)
  DctSumFc Num(19,6) Deductible Sum (FC)
  DctSumSc Num(19,6) Deductible Sum (SC)
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplDct Num(19,6) Applied Deductible Sum (LC)
  ApplDctFc Num(19,6) Applied Deductible Sum (FC)
  ApplDctSc Num(19,6) Applied Deductible Sum (SC)
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  BaseDct Num(19,6) Base Deductible Sum (LC)
  BaseDctFc Num(19,6) Base Deductible Sum (FC)
  BaseDctSc Num(19,6) Base Deductible Sum (SC)
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

# WTQ12 - Inventory Transfer Request - Tax Extension
Module: Inventory and Production | 81 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectType, LogInstanc, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
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
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=1250000001 ->ADP1
  TaxId10 nVarChar(100) Assessee Type
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
  CountryS nVarChar(3) Country ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=, Y=]
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
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code

# WTQ13 - Inventory Transfer Request Rows - Distributed Freights
Module: Inventory and Production | 59 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, GroupNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# WTQ14 - Inventory Transfer Request - Assembly - Rows
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectType, LogInstanc, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1

# WTQ15 - Inv. Transfer Request - Drawn Dpm Appl
Module: Inventory and Production | 84 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjType, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Number ->OWTQ
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum (LC)
  DctSumFc Num(19,6) Deductible Sum (FC)
  DctSumSc Num(19,6) Deductible Sum (SC)
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum (LC)
  ApplDctFc Num(19,6) Applied Deductible Sum (FC)
  ApplDctSc Num(19,6) Applied Deductible Sum (SC)
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum (LC)
  PaidDctFc Num(19,6) Paid Deductible Sum (FC)
  PaidDctSc Num(19,6) Paid Deductible Sum (SC)
  PaidEq Num(19,6) Paid Equalization Sum (LC)
  PaidEqFc Num(19,6) Paid Equalization Sum (FC)
  PaidEqSc Num(19,6) Paid Equalization Sum (SC)
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum (LC)
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum (FC)
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum (SC)
  DpApplEq Num(19,6) Dpm Appl Equalization Sum (LC)
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum (FC)
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum (SC)
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# WTQ16 - Inventory Transfer Request - SnB Properties
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, SnBIndex, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Number ->OWTQ
  LineNum Int(11) Row Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjId Int(11) Object ID
  ObjAbs Int(11) SnB Object No.
  DrfWObjAbs Int(11) SnBW Draft Object No. default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance

# WTQ19 - Inventory Transfer Request - Bin Allocation Data
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BinAllocSe, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OWTQ
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# WTQ2 - Inventory Transfer Request - Freight - Rows
Module: Inventory and Production | 58 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, GroupNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  LineNum Int(11) Row Number
  GroupNum Int(11) Group No.
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total (SC)
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)

# WTQ21 - Inventory Transfer Request - Document Reference Information
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RefType, LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=1250000001
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order, 321=Internal Reconciliation]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de crédito de los documentos relacionados, 02=Nota de débito de los documentos relacionados, 03=Devolución de mercancía sobre facturas o traslados previos, 04=Sustitución de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicación de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, MX_09=Factura generada por pagos diferidos]

# WTQ26 - Inventory Transfer Request - E-Way Bill Information
Module: Inventory and Production | 36 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTQ
  SuplyType nVarChar(20) EWB Transaction Type [O=Outward, I=Inward]
  SubSplyTyp Int(11) EWB Sub-Type ->OEST
  DocType nVarChar(3) EWB Doc. Type ->OEDT
  TransMode Int(11) EWB Transportation Mode ->OETM
  Distance Num(19,6) EWB Transport Distance
  TransDocNo nVarChar(16) EWB Transporter Doc. No.
  TransDate Date(8) EWB Transportation Date
  VehicleTyp nVarChar(2) EWB Vehicle Type ->OEVT
  VehicleNo nVarChar(15) EWB Vehicle Number
  EWayBillNo nVarChar(20) EWB No.
  EwbDate Date(8) E-Way Bill Date
  FrmTraName nVarChar(100) EWB Consignor Name
  FrmAddres1 nVarChar(120) EWB Consignor Address 1
  FrmAddres2 nVarChar(120) EWB Consignor Address 2
  FrmZipCode nVarChar(20) EWB Consignor Zip Code
  ActFrmStat nVarChar(2) Dispatch State of EWB Consignor
  ToTraName nVarChar(100) EWB Consignee Name
  ToAddres1 nVarChar(120) EWB Consignee Address 1
  ToAddres2 nVarChar(120) EWB Consignee Address 2
  ToZipCode nVarChar(20) EWB Consignee Zip Code
  ActToState nVarChar(2) Ship-To State of EWB Consignee
  FrmGSTN nVarChar(15) EWB Consignor GSTN
  FrmState nVarChar(2) Bill-To State of EWB Consignor
  ToGSTN nVarChar(15) EWB Consignee GSTN
  ToState nVarChar(2) Bill-To State of EWB Consignee
  MainHsnEnt Int(11) EWB Main HSN Entry ->OCHP
  FrmPlace nVarChar(50) EWB Consignor Place
  ToPlace nVarChar(50) EWB Consignee Place
  TransID nVarChar(15) EWB Transporter ID
  TransName nVarChar(25) EWB Transporter Name
  ExpireDate Date(8) EWB Expiration Date
  ObjectType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TspEntry Int(11) Transporter Abs. Entry ->OTSP
  TspLine Int(11) Transportation Line

# WTQ3 - Inventory Transfer Request - Freight
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, LineNum, DocEntry
  DOCUMENT: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  ExpnsCode Int(11) Expense Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Goods Receipt PO, 59=Goods Receipt]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  LineNum Int(11) Line Number default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Drawn Total
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)

# WTQ4 - Inventory Transfer Request - Tax Amount per Document
Module: Inventory and Production | 55 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjectType, LineSeq, DocEntry
  SCONDARY: staType, StaCode, StcCode, ExpnsCode, GroupNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group No. default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Tax Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Authority Type ->OSTT
  TaxAcct nVarChar(15) Authority Code
  TaxSum Num(19,6) Tax % ->OACT
  TaxSumFrgn Num(19,6) Tax Account
  TaxSumSys Num(19,6) Tax Amount
  BaseSum Num(19,6) Tax Amount (FC)
  BaseSumFrg Num(19,6) Base Amount
  BaseSumSys Num(19,6) Base Amount (FC)
  ObjectType nVarChar(20) Base Amount (SC)
  LogInstanc Int(11) Tax Amount (SC) default=0 ->ADP1
  TaxStatus VarChar(1) Base Amount default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]

# WTQ5 - Inventory Transfer Request - Withholding Tax
Module: Inventory and Production | 148 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OWTQ
  WTCode nVarChar(4) WTax Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  ApplAmnt Num(19,6) Applied WTax Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) WTax Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 20=Goods Receipt PO, 59=Goods Receipt]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency From Doc. Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)

# WTQ6 - Inventory Transfer Request - Installments
Module: Inventory and Production | 64 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InstlmntID, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax Amount
  VATBlckFC Num(19,6) Reserved Tax Amount (FC)
  VATBlckSC Num(19,6) Reserved Tax Amount (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard Dunning Block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Freight
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)

# WTQ7 - Inventory Transfer Request - Delivery Packages
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# WTQ8 - Inventory Transfer Request - Items in Package
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: NumPerMsr, UomEntry, ItemCode, PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# WTQ9 - Inventory Transfer Request - Drawn DPM
Module: Inventory and Production | 27 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=1250000001 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]

# WTR1 - Inventory Transfer - Rows
Module: Inventory and Production | 287 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  STATUS: LineStatus
  CURRENCY: Currency
  ACCOUNT: AcctCode
  BASE_ENTRY: BaseLine, BaseType, BaseEntry
  VIS_ORDER: VisOrder, DocEntry
  OWNER_CODE: OwnerCode
  ITM_WHS_OQ: OpenQty, WhsCode, ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 20=Goods Receipt, 18=A/P Invoice, 204=A/P Down Payment]
  TrgetEntry Int(11) Target Document Internal ID
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Purchase Delivery Notes, 59=Inventory General Entry, 67=Warehouses Transfers, 1250000001=Inventory Transfer Request]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  ItemCode nVarChar(50) Item Code ->OITM
  Dscription nVarChar(100) Item/Service Description
  Quantity Num(19,6) Quantity
  ShipDate Date(8) Row Delivery Date
  OpenQty Num(19,6) Remaining Open Quantity
  Price Num(19,6) Price
  Currency nVarChar(3) Price Currency ->OCRN
  Rate Num(19,6) Currency Rate
  DiscPrcnt Num(19,6) Discount % per Row
  LineTotal Num(19,6) Row Total
  TotalFrgn Num(19,6) Row Total in FC
  OpenSum Num(19,6) Open Amount
  OpenSumFC Num(19,6) Open Amount in FC
  VendorNum nVarChar(50) Vendor Catalog No.
  SerialNum nVarChar(17) Serial Number
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  Commission Num(19,6) Commission Percentage
  TreeType VarChar(1) Tree Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=Sales BOM Component, P=Production, T=Template]
  AcctCode nVarChar(15) Account Code ->OACT
  TaxStatus VarChar(1) Tax Definition [Y=Yes, N=No]
  GrossBuyPr Num(19,6) Base Price for Gross Profit
  PriceBefDi Num(19,6) Price Before Discount
  DocDate Date(8) Posting Date
  Flags Int(11) Flags default=0
  OpenCreQty Num(19,6) Credit Memo Amount
  UseBaseUn VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  SubCatNum nVarChar(50) Customer/Vendor Cat. No. ->OSCN
  BaseCard nVarChar(15) Base Card Code ->OCRD
  TotalSumSy Num(19,6) Row Total in FC
  OpenSumSys Num(19,6) Open Amount in System Currency
  InvntSttus VarChar(1) Whse Status default=O [O=Open, C=Closed]
  OcrCode nVarChar(8) Costing Code ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  CodeBars nVarChar(254) Bar Code
  VatPrcnt Num(19,6) Tax Percentage per Row
  VatGroup nVarChar(8) Tax Definition ->OVTG
  PriceAfVAT Num(19,6) Gross Price after Discount
  Height1 Num(19,6) Height 1
  Hght1Unit Int(6) Unit of Height 1
  Height2 Num(19,6) Height 2
  Hght2Unit Int(6) Unit of Height 2
  Width1 Num(19,6) Width 1
  Wdth1Unit Int(6) Unit of Width 1
  Width2 Num(19,6) Width 2
  Wdth2Unit Int(6) Unit of Width 2
  Length1 Num(19,6) Length 1
  Len1Unit Int(6) Unit of Length 1
  length2 Num(19,6) Length 2
  Len2Unit Int(6) Unit of Length 2
  Volume Num(19,6) Quantity
  VolUnit Int(6) Unit of Measure
  Weight1 Num(19,6) Weight 1
  Wght1Unit Int(6) Unit of Weight 1
  Weight2 Num(19,6) Weight 2
  Wght2Unit Int(6) Unit of Weight 2
  Factor1 Num(19,6) Factor 1
  Factor2 Num(19,6) Factor 2
  Factor3 Num(19,6) Factor 3
  Factor4 Num(19,6) Factor 4
  PackQty Num(19,6) Packing Quantity
  UpdInvntry VarChar(1) Whse Update default=Y [Y=Yes, N=No]
  BaseDocNum Int(11) Base Document No.
  BaseAtCard nVarChar(100) Customer/Vendor Base Document
  SWW nVarChar(16) SWW
  VatSum Num(19,6) Tax Total
  VatSumFrgn Num(19,6) Tax Sum (FC)
  VatSumSy Num(19,6) Tax Sum (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BlockNum nVarChar(100) Block Number
  ImportLog nVarChar(20) Import Log
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAqcuistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  DistribSum Num(19,6) Distributed Amount
  DstrbSumFC Num(19,6) Distributed Amount (FC)
  DstrbSumSC Num(19,6) Distributed Amount (SC)
  GrssProfit Num(19,6) Row Gross Profit
  GrssProfSC Num(19,6) Row Gross Profit (SC)
  GrssProfFC Num(19,6) Row Gross Profit (FC)
  VisOrder Int(11) Visual Order
  INMPrice Num(19,6) Item's Last Sales Price (OINM)
  PoTrgNum Int(11) PO Target No.
  PoTrgEntry nVarChar(11) PO Target Entry
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  PoLineNum Int(11) PO Target Row No.
  Address nVarChar(254) Address
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type [Y=Regular Tax, N=No Tax, U=Use Tax]
  OrigItem nVarChar(50) Original Item ->OITM
  BackOrdr VarChar(1) Allow Back Order [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  PickStatus VarChar(1) Pick Status default=N [Y=Picked, N=Not Picked, R=Released for Picking, P=Partially Picked]
  PickOty Num(19,6) Pick Quantity
  PickIdNo Int(11) Pick List ID Number
  TrnsCode Int(6) Shipping Method default=-1 ->OSHP
  VatAppld Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied FC
  VatAppldSC Num(19,6) VAT Applied SC
  BaseQty Num(19,6) Base Quantity
  BaseOpnQty Num(19,6) Base Open Quantity
  VatDscntPr Num(19,6) VAT Discount Percent
  WtLiable VarChar(1) WT Liable [Y=Yes, N=No]
  DeferrTax VarChar(1) DeferredTax default=N [Y=Yes, N=No]
  EquVatPer Num(19,6) Equalization Tax Percentage
  EquVatSum Num(19,6) Equalization Tax Total
  EquVatSumF Num(19,6) Equalization Tax Total FC
  EquVatSumS Num(19,6) Equalization Tax Total SC
  LineVat Num(19,6) Net Tax Sum
  LineVatlF Num(19,6) Net Tax Sum
  LineVatS Num(19,6) Net Tax Sum
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value
  CEECFlag VarChar(1) Correction Invoice Item W/S default=S [W=Was, S=Should be]
  ToStock Num(19,6) Corr Inv. Amount to Stock
  ToDiff Num(19,6) Corr Inv. Amount to Diff. Acct
  ExciseAmt Num(19,6) Excise Amount
  TaxPerUnit Num(19,6) Tax per Unit
  TotInclTax Num(19,6) Total (incl. Tax)
  CountryOrg nVarChar(3) Country of Origin
  StckDstSum Num(19,6) Stock Distribute Sum
  ReleasQtty Num(19,6) Released Quantity
  LineType VarChar(1) Line Type default=R [R=Regular]
  TranType VarChar(1) Transaction Type [C=Complete, R=Reject]
  Text Text(16) Text
  OwnerCode Int(11) Document Owner
  StockPrice Num(19,6) Stock Price
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  LstByDsSum Num(19,6) Last Buy Distribute Sum
  StckINMPr Num(19,6) Stock Inm Price
  LstBINMPr Num(19,6) Last Buy Inm Price
  StckDstFc Num(19,6) Stock Distribute Sum Foreign
  StckDstSc Num(19,6) Stock Distribute Sum System
  LstByDsFc Num(19,6) Last Buy Distribute Sum FC
  LstByDsSc Num(19,6) Last Buy Distribute Sum SC
  StockSum Num(19,6) Stock Sum
  StockSumFc Num(19,6) Stock Sum FC
  StockSumSc Num(19,6) Stock Sum SC
  StckSumApp Num(19,6) Stock Sum Applied
  StckAppFc Num(19,6) Stock Sum Applied FC
  StckAppSc Num(19,6) Stock Sum Applied SC
  ShipToCode nVarChar(50) Ship-to Code
  ShipToDesc nVarChar(254) Ship-to Description
  StckAppD Num(19,6) Stock Distribution Applied Sum
  StckAppDFC Num(19,6) Stock Distrib. Applied Sum FC
  StckAppDSC Num(19,6) Stock Distrib. Applied Sum SC
  BasePrice VarChar(1) Price for Total Calculation default=E [E=Exclude Tax, I=Include Tax]
  GTotal Num(19,6) Gross Total
  GTotalFC Num(19,6) Gross Total FC
  GTotalSC Num(19,6) Gross Total SC
  DistribExp VarChar(1) Distribute Expense [Y=Yes, N=No]
  DescOW VarChar(1) DESC_OVERWRITTEN default=N [Y=Yes, N=No]
  DetailsOW VarChar(1) DETAILS_OVERWRITTEN default=N [Y=Yes, N=No]
  GrossBase Int(6) Base Method for Gross Profit
  VatWoDpm Num(19,6) Tax Before DPM Applied
  VatWoDpmFc Num(19,6) Tax Before DPM Applied FC
  VatWoDpmSc Num(19,6) Tax Before DPM Applied SC
  CFOPCode nVarChar(6) CFOP Code for Document ->OCFP
  CSTCode nVarChar(6) CST Code for ICMS
  Usage Int(11) Usage Code for Document ->OUSG
  TaxOnly VarChar(1) Tax Only [Y=Yes, N=No]
  WtCalced VarChar(1) WTax Calculated default=N [N=No, Y=Yes]
  QtyToShip Num(19,6) Quantity to Ship
  DelivrdQty Num(19,6) Delivered Quantity
  OrderedQty Num(19,6) Ordered Quantity
  CogsOcrCod nVarChar(8) COGS Distribution Rule Code ->OOCR
  CiOppLineN Int(11) Line Number of Opposite Line default=-1
  CogsAcct nVarChar(15) COGS Account Code ->OACT
  ChgAsmBoMW VarChar(1) Change Whs for Asm BoM Child [Y=Yes, N=No]
  ActDelDate Date(8) Actual Delivery Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  TaxDistSum Num(19,6) Tax Distributed Amount
  TaxDistSFC Num(19,6) Tax Distributed Amount (FC)
  TaxDistSSC Num(19,6) Tax Distributed Amount (SC)
  PostTax VarChar(1) Post Tax in Price to Stock default=Y [Y=Yes, N=No]
  Excisable VarChar(1) Excisable [Yes/No] [Y=Yes, N=No]
  AssblValue Num(19,6) Assessable Value
  RG23APart1 Int(11) RG23A Part1 Number
  RG23APart2 Int(11) RG23A Part2 Number
  RG23CPart1 Int(11) RG23C Part1 Number
  RG23CPart2 Int(11) RG23C Part2 Number
  CogsOcrCo2 nVarChar(8) COGS Distribution Rule Code2 ->OOCR
  CogsOcrCo3 nVarChar(8) COGS Distribution Rule Code3 ->OOCR
  CogsOcrCo4 nVarChar(8) COGS Distribution Rule Code4 ->OOCR
  CogsOcrCo5 nVarChar(8) COGS Distribution Rule Code5 ->OOCR
  LnExcised VarChar(1) Line Excised [O=Open, C=Closed, P=Copied to OEI]
  LocCode Int(11) Location Code ->OLCT
  StockValue Num(19,6) Total COGS Value
  GPTtlBasPr Num(19,6) Total Base Price for Profit
  unitMsr2 nVarChar(100) Pur/Sal UoM if BaseUnit
  NumPerMsr2 Num(19,6) Pur/Sal UoM Value if Base Unit
  SpecPrice VarChar(1) Price Source Type default=N [Y=Special Prices for Business Partner, N=Manual, W=Active Price List, Discount Groups, R=Active Price List, U=Inactive Price List, A=Blanket Agreement, P=Period and Volume Discounts, Q=Period and Volume Discounts, Discount Groups, V=Inactive Price List, Discount Groups, 9=Special Prices for Business Partner, !=Blanket Agreement, 0=Period and Volume Discounts, 1=Period and Volume Discounts, Discount Groups, 2=Active Price List, 7=Active Price List, Discount Groups, 5=Inactive Price List, 6=Inactive Price List, Discount Groups]
  CSTfIPI nVarChar(2) CST for IPI Code
  CSTfPIS nVarChar(2) CST for PIS Code
  CSTfCOFINS nVarChar(2) CST for COFINS Code
  ExLineNo nVarChar(10) ExLineNo
  isSrvCall VarChar(1) Created from Service Call default=N [Y=Yes, N=No]
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  PQTReqDate Date(8) Pur Quotation: Required Date
  PcDocType Int(11) Purchase Confirmation Doc Type default=-1 [-1=No Type, 22=Purchase Order, 540000006=Purchase Quotation]
  PcQuantity Num(19,6) Purchase Confirmation Quantity
  LinManClsd VarChar(1) Line Was Closed Manually default=N [Y=Yes, N=No, U=Unknown]
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  NoInvtryMv VarChar(1) Without Inventory Movement default=N [Y=Yes, N=No]
  ActBaseEnt Int(11) Actual Base Document Entry
  ActBaseLn Int(11) Actual Base Line Number
  ActBaseNum Int(11) Actual Base Document No.
  OpenRtnQty Num(19,6) Quantity Open for Return
  AgrNo Int(11) Agreement No.
  AgrLnNum Int(11) Agreement Row Number
  CredOrigin VarChar(1) Credit Origin ->OBSI
  Surpluses Num(19,6) Surpluses
  DefBreak Num(19,6) Defect and Breakup
  Shortages Num(19,6) Shortages
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  UomEntry2 Int(11) UoM Entry if Base Unit default=0 ->OUOM
  UomCode nVarChar(20) UoM Code
  UomCode2 nVarChar(20) UoM Code if Base Unit
  FromWhsCod nVarChar(8) From Warehouse Code ->OWHS
  NeedQty VarChar(1) Consider Quantity of Items default=N [Y=Yes, N=No]
  PartRetire VarChar(1) Partial Retirement default=N [Y=Yes, N=No]
  RetireQty Num(19,6) Retirement Quantity
  RetireAPC Num(19,6) Retirement APC
  RetirAPCFC Num(19,6) Retirement APC FC
  RetirAPCSC Num(19,6) Retirement APC SC
  InvQty Num(19,6) Quantity - Inventory UoM
  OpenInvQty Num(19,6) Open Quantity (Inventory UoM)
  EnSetCost VarChar(1) Enable Set Item Cost in Return default=N [Y=Yes, N=No]
  RetCost Num(19,6) Return Cost in A/R Return
  Incoterms Int(11) Incoterms default=0 ->ODCI
  TransMod Int(11) Transport Mode default=0 ->ODCI
  LineVendor nVarChar(15) Line Vendor Code ->OCRD
  DistribIS VarChar(1) Distribute Intrastat Freight default=N [Y=Yes, N=No]
  ISDistrb Num(19,6) Intrastat Distrib. Amount
  ISDistrbFC Num(19,6) Intrastat Distrib. Amount (FC)
  ISDistrbSC Num(19,6) Intrastat Distrib. Amount (SC)
  IsByPrdct VarChar(1) Item Is By-Product default=N [N=No, Y=Yes]
  ItemType Int(11) Item Type default=4 [4=Item]
  PriceEdit VarChar(1) Price Was Edited by User default=N [N=No, Y=Yes]
  PrntLnNum Int(11) Parent Line Number
  LinePoPrss VarChar(1) Line PO Process default=N [Y=Yes, N=No]
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  TaxRelev VarChar(1) Tax Relevant Row default=Y [Y=Yes, N=No]
  LegalText nVarChar(254) Legal Text
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  LicTradNum nVarChar(32) Federal Tax ID
  InvQtyOnly VarChar(1) Change Qty (Inv. UoM) Only default=N [Y=Yes, N=No]
  UnencReasn Int(11) Reason for Unencumbered ICMS
  ShipFromCo nVarChar(50) Ship-From Code
  ShipFromDe nVarChar(254) Ship-From Description
  FisrtBin nVarChar(228) First Bin Location
  AllocBinC nVarChar(11) Allocated Bin Location Count
  ExpType nVarChar(4) Expense Type ->OEXD
  ExpUUID nVarChar(50) Expense UUID
  ExpOpType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others, =]
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  MYFtype nVarChar(2) MYF type [S1=MYF sales, S2=Retail sales, P1=MYF purchase, P3=Other expense]
  GPBefDisc Num(19,6) Gross Price
  ReturnRsn Int(6) Return Reason default=-1
  ReturnAct Int(6) Return Action default=-1
  StgSeqNum Int(11) Stage Sequence Number
  StgEntry Int(11) Stage Entry ->ORST
  StgDesc nVarChar(100) Stage Description
  ItmTaxType nVarChar(2) Item GST Tax Category [GR=GST Regular, GN=GST Nil Rated, GE=GST Exempt, NE=Excisable, NN=Non-GST Non-Excisable]
  SacEntry Int(11) SAC Entry ->OSAC
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  HsnEntry Int(11) HSN Entry
  OriBAbsEnt Int(11) Original Base Document Internal ID
  OriBLinNum Int(11) Original Base Document Line Number
  OriBDocTyp Int(11) Original Base Document Type
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# WTR10 - Inventory Transfer - Row Structure
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocEntry
  SECONDARY U: OrderNum, AftLineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineSeq Int(11) Row Sequence
  AftLineNum Int(11) After Row Number
  OrderNum Int(11) Order Number
  LineType VarChar(1) Row Type [T=Text, S=Subtotal]
  LineText Text(16) Row Text
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=67 ->ADP1

# WTR11 - Inv. Transfer - Drawn Dpm Det.
Module: Inventory and Production | 70 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
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
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance
  IsAcq VarChar(1) Acquisition Tax-Liable default=N [N=No, Y=Yes]
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

# WTR12 - Inventory Transfer - Tax Extension
Module: Inventory and Production | 81 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
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
  NfRef nVarChar(254) Nota Fiscal Reference
  Carrier nVarChar(15) Carrier Code
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=67 ->ADP1
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
  CountryS nVarChar(3) Country ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country ->OCRY
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
  ImpExpNo nVarChar(100) Import/Export Bill No.
  ImpExpDate Date(8) Import/Export Date
  BpGSTType Int(11) GST Regn Type of BP
  BpGSTN nVarChar(15) GST Regn No of BP
  BpStateCod nVarChar(3) State Code of Business Partner ->OCST
  BPStatGSTN nVarChar(2) GST State Code of BP
  LocGSTType Int(11) GST Regn Type of Location
  LocGSTN nVarChar(15) GST Regn No of Location
  LocStatCod nVarChar(3) State Code of Location ->OCST
  LocStaGSTN nVarChar(2) GST State Code of Location
  BpCountry nVarChar(3) Country Code of BP ->OCRY
  OrigImpNo nVarChar(100) Original Bill of Entry No.
  OrigImpDat Date(8) Original Bill of Entry Date
  ExportType VarChar(1) Exporting Type default=E [E=Imports/Exports, S=SEZ Developer, U=SEZ Unit, D=Deemed Imports/Exports]
  PortCode nVarChar(100) Port Code

# WTR13 - Inventory Transfer Rows - Distributed Freights
Module: Inventory and Production | 59 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum, LineNum, DocEntry
  LINE: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Aquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Normal Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) VAT Applied Frgn
  VatAppldSC Num(19,6) VAT Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Base Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Line No.
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Abs. Entry default=-1
  BaseGroup Int(11) Base Document Group default=-1
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1
  VisOrder Int(11) Visual Order
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  DistribExp VarChar(1) Distribute Freights [Y=Yes, N=No]
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# WTR14 - Inventory Transfer - Assembly - Rows
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1

# WTR15 - Inv. Transfer - Drawn Dpm Appl
Module: Inventory and Production | 84 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  ObjType nVarChar(20) object type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  StaCode nVarChar(8) Tax Authority Code
  StaType Int(11) Tax Authority Type
  StaIndex Int(11) Tax Authority Seq Index
  BaseNet Num(19,6) Net LC
  BaseNetFc Num(19,6) Net FC
  BaseNetSc Num(19,6) Net SC
  VatSum Num(19,6) Tax LC
  VatSumFc Num(19,6) Tax FC
  VatSumSc Num(19,6) Tax SC
  DctSum Num(19,6) Deductible Sum LC
  DctSumFc Num(19,6) Deductible Sum FC
  DctSumSc Num(19,6) Deductible Sum SC
  EqSum Num(19,6) Equalization Sum LC
  EqSumFc Num(19,6) Equalization Sum FC
  EqSumSc Num(19,6) Equalization Sum SC
  ApplNet Num(19,6) Applied Net LC
  ApplNetFc Num(19,6) Applied Net FC
  ApplNetSc Num(19,6) Applied Net SC
  ApplVat Num(19,6) Applied Tax LC
  ApplVatFc Num(19,6) Applied Tax FC
  ApplVatSc Num(19,6) Applied Tax SC
  ApplDct Num(19,6) Applied Deductible Sum LC
  ApplDctFc Num(19,6) Applied Deductible Sum FC
  ApplDctSc Num(19,6) Applied Deductible Sum SC
  ApplEq Num(19,6) Applied Equalization Sum LC
  ApplEqFc Num(19,6) Applied Equalization Sum FC
  ApplEqSc Num(19,6) Applied Equalization Sum SC
  PaidNet Num(19,6) Paid Net LC
  PaidNetFc Num(19,6) Paid Net FC
  PaidNetSc Num(19,6) Paid Net SC
  PaidVat Num(19,6) Paid Tax LC
  PaidVatFc Num(19,6) Paid Tax FC
  PaidVatSc Num(19,6) Paid Tax SC
  PaidDct Num(19,6) Paid Deductible Sum LC
  PaidDctFc Num(19,6) Paid Deductible Sum FC
  PaidDctSc Num(19,6) Paid Deductible Sum SC
  PaidEq Num(19,6) Paid Equalization Sum LC
  PaidEqFc Num(19,6) Paid Equalization Sum FC
  PaidEqSc Num(19,6) Paid Equalization Sum SC
  DpApplNet Num(19,6) Dpm Appl Net LC
  DpApplNetF Num(19,6) Dpm Appl Net FC
  DpApplNetS Num(19,6) Dpm Appl Net SC
  DpApplVat Num(19,6) Dpm Appl Tax LC
  DpApplVatF Num(19,6) Dpm Appl Tax FC
  DpApplVatS Num(19,6) Dpm Appl Tax SC
  DpApplDct Num(19,6) Dpm Appl Deductible Sum LC
  DpApplDctF Num(19,6) Dpm Appl Deductible Sum FC
  DpApplDctS Num(19,6) Dpm Appl Deductible Sum SC
  DpApplEq Num(19,6) Dpm Appl Equalization Sum LC
  DpApplEqFc Num(19,6) Dpm Appl Equalization Sum FC
  DpApplEqSc Num(19,6) Dpm Appl Equalization Sum SC
  TaxCode nVarChar(8) Tax Code ->OSTC
  LineType VarChar(1) Row Type default=D [D=Document, R=Exchange Rate Rounding, H=Document Header Rounding]
  BaseGrs Num(19,6) Gross LC
  BaseGrsFc Num(19,6) Gross FC
  BaseGrsSc Num(19,6) Gross SC
  ApplGrs Num(19,6) Applied Gross LC
  ApplGrsFc Num(19,6) Applied Gross FC
  ApplGrsSc Num(19,6) Applied Gross SC
  PaidGrs Num(19,6) Paid Gross LC
  PaidGrsFc Num(19,6) Paid Gross FC
  PaidGrsSc Num(19,6) Paid Gross SC
  DpApplGrs Num(19,6) Dpm Appl Gross LC
  DpApplGrsF Num(19,6) Dpm Appl Gross FC
  DpApplGrsS Num(19,6) Dpm Appl Gross SC
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSc Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFc Num(19,6) Reverse Charge Sum (FC)
  ApplRvs Num(19,6) Applied Reverse Charge Sum LC
  ApplRvsSc Num(19,6) Applied Reverse Charge Sum SC
  ApplRvsFc Num(19,6) Applied Reverse Charge Sum FC
  PaidRvs Num(19,6) Paid Reverse Charge Sum LC
  PaidRvsSc Num(19,6) Paid Reverse Charge Sum SC
  PaidRvsFc Num(19,6) Paid Reverse Charge Sum FC
  DpApplRvs Num(19,6) Dpm Applied Reverse Charge LC
  DpApplRvsS Num(19,6) Dpm Applied Reverse Charge SC
  DpApplRvsF Num(19,6) Dpm Applied Reverse Charge FC
  IsPrscGood VarChar(1) Is Prescribed Goods default=N [Y=Yes, N=No]
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [Y=Yes, N=No]

# WTR16 - Inventory Transfer - SnB properties
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SnBIndex, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) abs entry ->OWTR
  LineNum Int(11) Line Number
  SnBIndex Int(11) SnB Index
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse ->OWHS
  ObjId Int(11) Object id
  ObjAbs Int(11) Object Abs
  DrfWObjAbs Int(11) draft Wobj Abs default=-1
  Quantity Num(19,6) Quantity
  SubLineNum Int(11) Subrow Number default=-1
  ObjType nVarChar(20) Object Type default=67
  LogInstanc Int(11) Log Instance

# WTR19 - Inventory Transfer - Bin Allocation Data
Module: Inventory and Production | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BinAllocSe, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OWTR
  BinAllocSe Int(11) Bin Allocation Sequence
  LineNum Int(11) Line Number
  SubLineNum Int(11) Subline Number default=-1
  SnBType Int(11) SnB Type default=-1
  SnBMDAbs Int(11) SnB Master Data Internal No. default=-1
  BinAbs Int(11) Bin Internal Number ->OBIN
  Quantity Num(19,6) Quantity
  ItemCode nVarChar(50) Item Code ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  AllowNeg VarChar(1) Allow Negative Entry [Y/N] default=N [Y=Yes, N=No]
  BinActTyp Int(6) Bin Action Type [1=Transaction In, 2=Transaction Out, 4=SnB Complete, 8=Bin First Then SnB]

# WTR2 - Inventory Transfer - Freight - Rows
Module: Inventory and Production | 58 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum, LineNum, DocEntry
  LINE: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  GroupNum Int(11) Group Number
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Vat Applied Frgn
  VatAppldSC Num(19,6) Vat Applied Sys
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  lineVat Num(19,6) Net Tax Amount
  lineVatlF Num(19,6) Net Tax Amount (FC)
  lineVatS Num(19,6) Net Tax Amount (SC)
  WtLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report [Y=Yes, N=No]
  BaseGroup Int(11) Base Document Group default=-1 [-1=, 0=, 1=, 2=]
  Status VarChar(1) Status default=O [O=Open, C=Close]
  TrgGroup Int(11) Target Group default=-1 [-1=, 0=, 1=, 2=]
  VisOrder Int(11) Visual Order
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)

# WTR21 - Inventory Transfer - Document Reference Information
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RefType, LineNum, DocEntry
  DOC_ENTRY: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjectType nVarChar(20) Object Type default=67
  LogInstanc Int(11) Log Instance default=0
  RefType VarChar(1) Reference Types default=S [S=System Document, E=External Document]
  LineNum Int(11) Line Number
  RefDocEntr Int(11) Referenced Internal Number
  RefDocNum Int(11) Referenced Document Number
  ExtDocNum nVarChar(100) External Referenced Document Number
  RefObjType nVarChar(20) Referenced Object Type [-1=External Document, 23=Sales Quotation, 17=Sales Order, 15=Delivery Notes, 234000031=Return Request, 16=Return, 203=Down Payment Incoming, 13=A/R Invoice, 14=A/R Credit Memo, 165=A/R Correction Invoice, 280=A/R Tax Invoice, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=Down Payment Outgoing, 18=A/P Invoice, 19=A/P Credit Memo, 163=A/P Correction Invoice, 281=A/P Tax Invoice, 69=Landed Costs, 24=Incoming Payments, 30=Journal Entry, 202=Production Order, 321=Internal Reconciliation]
  AccessKey nVarChar(100) Access Key
  IssueDate Date(8) Date of Issue
  IssuerCNPJ nVarChar(100) Issuer CNPJ
  IssuerCode nVarChar(10) Fiscal Document Issuer UF Code
  Model nVarChar(6) Fiscal Document Model
  Series nVarChar(3) Fiscal Document Series
  Number Int(11) Fiscal Document Number
  RefAccKey nVarChar(100) Referenced CT-e Access Key
  RefAmount Num(19,6) Referenced Amount
  SubSeries nVarChar(3) Fiscal Document Subseries
  Remark nVarChar(254) Remarks
  LinkRefTyp nVarChar(20) Link Reference Type default=00 [00=, 01=Nota de crédito de los documentos relacionados, 02=Nota de débito de los documentos relacionados, 03=Devolución de mercancía sobre facturas o traslados previos, 04=Sustitución de los CFDI previos, 05=Traslados de mercancias facturados previamente, 06=Factura generada por los traslados previos, 07=CFDI por aplicación de anticipo, 08=Customs, MX_08=Factura generada por pagos en parcialidades, MX_09=Factura generada por pagos diferidos]

# WTR3 - Inventory Transfer - Freight
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
  DOCUMENT: BaseAbsEnt, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  ExpnsCode Int(11) Freight Code ->OEXD
  LineTotal Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSumSy Num(19,6) Total (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  Comments nVarChar(100) Remarks
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DistrbMthd VarChar(1) Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  TaxStatus VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Row Tax %
  VatSum Num(19,6) Tax Amount
  VatSumFrgn Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  DedVatSum Num(19,6) Deductible Tax Amount
  DedVatSumF Num(19,6) Deductible Tax Amount (FC)
  DedVatSumS Num(19,6) Deductible Tax Amount (SC)
  IsAcquistn VarChar(1) Acquisition Tax default=N [Y=Yes, N=No]
  TaxCode nVarChar(8) Tax Code ->OSTC
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  WTLiable VarChar(1) WTax Liable [Y=Yes, N=No]
  VatApplied Num(19,6) Vat Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)
  LineVat Num(19,6) Net Tax Amount
  LineVatF Num(19,6) Net Tax Amount (FC)
  LineVatS Num(19,6) Net Tax Amount (SC)
  BaseMethod VarChar(1) Drawing Method [N=None, Q=Quantity, V=Volume, W=Weight, T=Total, A=All]
  Stock VarChar(1) Stock [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price [Y=Yes, N=No]
  AnalysRpt VarChar(1) Analysis Report default=N [Y=Yes, N=No]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseType Int(11) Base Document Type default=-1 [-1=, 0=, 20=Goods Receipt PO, 59=Goods Receipt, 67=Inventory Transfer, 1250000001=Inventory Transfer Request]
  BaseRef Int(11) Base Document Reference
  BaseLnNum Int(11) Base Document Row No.
  LineNum Int(11) line num default=-1
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Type
  TrgAbsEnt Int(11) Target Doc. Internal No. default=-1
  StDstr Num(19,6) Stock Distributed Sum
  StDstrSC Num(19,6) Stock Distributed Sum (SC)
  StDstrFC Num(19,6) Stock Distributed Sum (FC)
  FixCurr nVarChar(3) Fixation Currency ->OCRN
  VatDscntPr Num(19,6) Tax Discount %
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDistMtd VarChar(1) Tax Distribution Method [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  VatGrpSrc VarChar(1) VAT Group Source default=N [N=Not Defined, M=Manually Entered, D=Determined]
  DrawnTotal Num(19,6) Drawn Total
  DrawnFC Num(19,6) Drawn Total (FC)
  DrawnSC Num(19,6) Drawn Total (SC)
  GrsAmount Num(19,6) Gross Amount
  GrsFC Num(19,6) Gross Amount (FC)
  GrsSC Num(19,6) Gross Amount (SC)
  BaseTotal VarChar(1) Base Total for Calculation default=N [N=Net Total, G=Gross Total]
  RetReqLC Num(19,6) Return Request Amount
  RetReqFC Num(19,6) Return Request Amount (FC)
  RetReqSC Num(19,6) Return Request Amount (SC)
  RRVatLC Num(19,6) Return Request VAT Amount
  RRVatFC Num(19,6) Return Request VAT Amount (FC)
  RRVatSC Num(19,6) Return Request VAT Amount (SC)

# WTR4 - Inventory Transfer - Tax Amount per Document
Module: Inventory and Production | 55 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocEntry
  SCONDARY: staType, StaCode, StcCode, ExpnsCode, GroupNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number default=-1
  GroupNum Int(11) Group Number default=-1
  ExpnsCode Int(11) Expense Code default=-1 ->OEXD
  RelateType Int(11) Relation Type default=1 [1=Row, 2=Row Freight Charges, 3=Document Expenses, 13=Distributed Freights]
  StcCode nVarChar(8) Tax Code ->OSTC
  StaCode nVarChar(8) Authority Code ->OSTA
  staType Int(11) Authority Type ->OSTT
  TaxRate Num(19,6) Tax Rate
  TaxAcct nVarChar(15) Tax Account ->OACT
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=13 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  TaxStatus VarChar(1) Tax Status default=Y [Y=Regular Tax, N=No Tax, U=Use Tax]
  VatApplied Num(19,6) VAT Applied
  VatAppldFC Num(19,6) Applied Tax (FC)
  VatAppldSC Num(19,6) Applied Tax (SC)
  LineSeq Int(11) Line Sequence
  DeferrAcct nVarChar(15) Deferred Tax Account ->OACT
  BaseType Int(11) Base Document Type default=-1
  BaseAbs Int(11) Base Doc Abs Entry default=-1
  BaseSeq Int(11) Base Doc. Line Sequence
  DeductTax Num(19,6) Deductible Tax Amount
  DdctTaxFrg Num(19,6) Deductible Tax Amount (FC)
  DdctTaxSys Num(19,6) Deductible Tax Amount (SC)
  BaseAppld Num(19,6) Applied Base Amount
  BaseApldFC Num(19,6) Applied Base Amount (FC)
  BaseApldSC Num(19,6) Applied Base Amount (SC)
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Tax Included in Price? default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt? default=N [Y=Yes, N=No]
  TaxExpAct nVarChar(15) Expense Account for Tax ->OACT
  OnHoldTax Num(19,6) On Hold Tax Amount
  OnHoldTaxF Num(19,6) On Hold Tax Amount (FC)
  OnHoldTaxS Num(19,6) On Hold Tax Amount (SC)
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  TaxSumOrg Num(19,6) Tax Amount Original
  TaxSumOrgF Num(19,6) Tax Amount Original (FC)
  TaxSumOrgS Num(19,6) Tax Amount Original (SC)
  OpenTax Num(19,6) Open Service Tax
  OpenTaxFC Num(19,6) Open Service Tax (FC)
  OpenTaxSC Num(19,6) Open Service Tax (SC)
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgTax Num(19,6) Reverse Charge Tax Amount
  RvsChrgSC Num(19,6) Reverse Charge Tax Amount (SC)
  RvsChrgFC Num(19,6) Reverse Charge Tax Amount (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]

# WTR5 - Inventory Transfer - Withholding Tax
Module: Inventory and Production | 148 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  SECONDERY U: Doc1LineNo, BaseAbsEnt, WTCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OWTR
  WTCode nVarChar(4) WT Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount in SC
  TxblAmntFC Num(19,6) Taxable Amount in FC
  WTAmnt Num(19,6) WT Amount
  WTAmntSC Num(19,6) WT Amount (SC)
  WTAmntFC Num(19,6) WT Amount (FC)
  ApplAmnt Num(19,6) Applied WT Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT]
  BaseAbsEnt Int(11) Base Abs Entry default=-1
  BaseLine Int(11) Base Line
  BaseNum Int(11) Base Document Type default=-1 [-1=, 0=, 20=Goods Receipt PO, 59=Goods Receipt, 67=Inventory Transfer, 1250000001=Inventory Transfer Request]
  LineNum Int(11) Line Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Abs. Entry default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WT Line Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Line
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No.
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)

# WTR6 - Inventory Transfer - Installments
Module: Inventory and Production | 64 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InstlmntID, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  InstlmntID Int(6) Installment ID default=1
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  DueDate Date(8) Due Date
  Status VarChar(1) Installment Status default=O [O=Open, C=Closed]
  DunnLevel Int(11) Dunning Level default=0
  InsTotal Num(19,6) Total Installment
  InsTotalFC Num(19,6) Total Installment (FC)
  InsTotalSy Num(19,6) Total Installment (SC)
  PaidToDate Num(19,6) Paid to Date
  PaidFC Num(19,6) Paid (FC)
  PaidSys Num(19,6) Paid (SC)
  VatSum Num(19,6) Total Tax
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  VatPaid Num(19,6) Tax Paid to Date
  VatPaidFC Num(19,6) Tax Paid (FC)
  VatPaidSys Num(19,6) Tax Paid (SC)
  TotalExpns Num(19,6) Total Freight Charges
  TotalExpFC Num(19,6) Total Freight Charges (FC)
  TotalExpSC Num(19,6) Total Freight Charges (SC)
  ExpAppl Num(19,6) Applied Freight Charges
  ExpApplFC Num(19,6) Applied Freight Charges (FC)
  ExpApplSC Num(19,6) Applied Freight Charges (SC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTAppliedS Num(19,6) Applied WTax (SC)
  TotalBlck Num(19,6) Total Reserved Amount
  TotalBlckF Num(19,6) Total Reserved Amount (FC)
  TotalBlckS Num(19,6) Total Reserved Amount (SC)
  VATBlck Num(19,6) Reserved Tax
  VATBlckFC Num(19,6) Reserved Tax (FC)
  VATBlckSC Num(19,6) Reserved Tax (SC)
  ExpnsBlck Num(19,6) Reserved Freight Charges
  ExpnsBlckF Num(19,6) Reserved Freight Charges (FC)
  ExpnsBlckS Num(19,6) Reserved Freight Charges (SC)
  WTBlocked Num(19,6) Reserved WTax Amount
  WTBlockedF Num(19,6) Reserved WTax Amount (FC)
  WTBlockedS Num(19,6) Reserved WTax Amount (SC)
  InstPrcnt Num(19,6) Installment %
  DunWizBlck VarChar(1) Wizard dunning block default=N [N=No, Y=Yes]
  DunDate Date(8) Last Dunning Date
  Paid Num(19,6) Paid
  PaidFrgn Num(19,6) Paid (FC)
  PaidSc Num(19,6) Paid (SC)
  reserved VarChar(1) Reserved default=N [N=No, Y=Yes]
  TaxOnExp Num(19,6) Tax on Expenses
  TaxOnExpFc Num(19,6) Tax on Expenses (FC)
  TaxOnExpSc Num(19,6) Tax on Expenses (SC)
  TaxOnExpAp Num(19,6) Applied Tax on Expenses
  TaxOnExApF Num(19,6) Applied Tax on Expenses (FC)
  TaxOnExApS Num(19,6) Applied Tax on Expenses (SC)
  TaxOnExBlo Num(19,6) Reserved Tax on Freight Amount
  TaxOnExBlF Num(19,6) Reserved Tax on Freight Amt FC
  TaxOnExBlS Num(19,6) Reserved Tax on Freight Amt SC
  LvlUpdDate Date(8) Dunning Level Update Date
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  PaidDpm Num(19,6) Paid by Down Payment
  PaidDpmFc Num(19,6) Paid by Down Payment (FC)
  PaidDpmSc Num(19,6) Paid by Down Payment (SC)

# WTR7 - Inventory Transfer - Delivery Packages
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# WTR8 - Inventory Transfer - Items in Package
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: NumPerMsr, UomEntry, ItemCode, PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=67 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0

# WTR9 - Inventory Transfer - Drawn Dpm
Module: Inventory and Production | 27 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OWTR
  LineNum Int(11) Row Number
  BaseAbs Int(11) Base Document Internal ID
  BaseLine Int(11) Base Document Row
  TargetBase VarChar(1) Target or Base Document default=B [B=Base, T=Target]
  ObjType nVarChar(20) Base Object Type
  DrawnSum Num(19,6) Net LC
  DrawnSumFc Num(19,6) Net FC
  DrawnSumSc Num(19,6) Net SC
  LogInstanc Int(11) Log Instance default=0
  ObjCode nVarChar(20) Object Type default=67 ->ADP1
  ApplDrawn Num(19,6) Applied Net LC
  ApplDrawnF Num(19,6) Applied Net FC
  ApplDrawnS Num(19,6) Applied Net SC
  BaseDocNum Int(11) Base Document Number
  BsDocDate Date(8) Base Posting Date
  BsDueDate Date(8) Base Due Date
  BsCardName nVarChar(100) Base BP Name
  BsComments nVarChar(254) Base Remarks
  Posted VarChar(1) Base Document Posted default=Y [Y=Yes, N=No]
  Vat Num(19,6) Tax LC
  VatFc Num(19,6) Tax FC
  VatSc Num(19,6) Tax SC
  Gross Num(19,6) Gross LC
  GrossFc Num(19,6) Gross FC
  GrossSc Num(19,6) Gross SC
  IsGross VarChar(1) Is Gross Line default=N [N=Net Line, Y=Gross Line]
