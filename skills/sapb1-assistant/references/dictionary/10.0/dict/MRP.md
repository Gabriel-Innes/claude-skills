<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->

# FCT1 - Sales Forecast - Rows
Module: MRP | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsID, ItemCode, Date, WhsCode
Fields (name type(len) description [values] ->parent table):
  AbsID Int(11) Internal Number ->OFCT
  LineID Int(11) Row Number
  ItemCode nVarChar(50) Item No. ->OITM
  Date Date(8) Day Forecasted
  Quantity Num(19,6) Quantity
  WhsCode nVarChar(8) Warehouse default=-1 ->OWHS

# MSN1 - MRP Scenarios - Warehouses Array
Module: MRP | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, WhsCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OMSN
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  ReqSel VarChar(1) Requirement Selection default=Y [Y=Yes, N=No]
  InvtSel VarChar(1) Inventory Selection default=Y [Y=Yes, N=No]
  ExtIvntSel VarChar(1) Existing Inventory Selection default=Y [Y=Yes, N=No]

# MSN2 - MRP Run Results
Module: MRP | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, PeriodID, ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodID Int(11) Period ID
  Initial Num(19,6) Initial Quantity
  InitialOrg Num(19,6) Original Initial Quantity
  InStock Num(19,6) Incoming Stock
  OutStock Num(19,6) Outgoing Stock
  Final Num(19,6) Final Quantity
  FinalOrg Num(19,6) Original Final Quantity
  Requests Num(19,6) Requests

# MSN3 - MRP Pegging Information
Module: MRP | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodID Int(11) Period ID
  Quantity Num(19,6) Quantity
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  BaseObj nVarChar(20) Base Object Type
  BaseDocNum nVarChar(16) Base Document Number
  BaseDue Date(8) Base Due Date
  StockType VarChar(1) Stock Operation Type default=I [I=Stock Issue, R=Stock Receipt]
  LineID Int(11) Row Number
  ParentCode nVarChar(50) Parent Item No. ->OITM
  StartDate Date(8) Period Start Date
  EndDate Date(8) Period End Date
  WhsCode nVarChar(8) Warehouse Code ->OWHS

# MSN4 - MRP Scenarios - Items Array
Module: MRP | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ItemCode
  ItemCode: ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OMSN
  ItemCode nVarChar(50) Item Code
  Selected VarChar(1) Selected default=Y [Y=Yes, N=No]
  TmpForMrp VarChar(1) Is Temporary for MRP default=N
  WorDueDate Date(8) Production Order Due Date
  DsmDueDate Date(8) Disassembly Order Due Date
  NorDueDate Date(8) Non Prd Order Doc. Due Date
  Interval Int(6) Order Intervals
  Multiple Num(19,6) Order Multiple
  MinORdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  prcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  ToleranDay Int(11) Tolerance Day
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]

# MSN5 - MRP-Specific Document
Module: MRP | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, DocType, DocEntry, DocSubType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocType nVarChar(20) Document Type
  DocEntry Int(11) Document Entry
  Selected VarChar(1) Selected default=Y [Y=Yes, N=No]
  DocSubType nVarChar(2) Document Sub-Type default=--

# ODPH - Template for Demand Planning
Module: MRP | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Template Internal Number
  UserSign nVarChar(50) User Signature
  TmpltName nVarChar(100) Template Name
  TmpltCnt Text(16) Template Content
  CrtDate Date(8) Create Date

# OFCT - Sales Forecast
Module: MRP | 7 columns | ObjType: 198
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsID
  FCT_CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsID Int(11) Internal Number
  Code nVarChar(16) Forecast Code
  Name nVarChar(100) Forecast Name
  UserSign Int(6) User Signature ->OUSR
  StartDate Date(8) Forecast Start Date
  EndDate Date(8) Forecast End Date
  FormView VarChar(1) Forecast Form View default=D [D=Daily, W=Weekly, M=Monthly]

# OMSN - MRP Scenarios
Module: MRP | 57 columns | ObjType: 199
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  MSN_CODE U: MsnCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  MsnCode nVarChar(30) MRP Scenario Code
  Descr nVarChar(100) Description
  GrpPeriods VarChar(1) Group Data into Periods of default=D [D=Days, W=Weeks, M=Months]
  PeriodsLen Int(11) Group Data into Periods of default=1
  StartDate Date(8) Report Start Date
  EndDate Date(8) Report End Date
  MaxLdTime Int(11) Maximum Cumulative Lead Time
  HldaysProd VarChar(1) Holidays for Production default=Y [Y=Yes, N=No]
  HldaysPurc VarChar(1) Holidays for Purchase default=Y [Y=Yes, N=No]
  ItmFrom nVarChar(50) Items Codes From ->OITM
  ItmTo nVarChar(50) Items Codes To ->OITM
  ItmGrp Int(11) Items Groups ->OITB
  ItmQryGrp nVarChar(250) Item Summary Report Group
  ExistStock VarChar(1) Consider Existing Inventory default=Y [Y=Yes, N=No]
  PurchOrder VarChar(1) Consider Purchase Orders default=Y [Y=Yes, N=No]
  SalesOrder VarChar(1) Consider Sales Orders default=Y [Y=Yes, N=No]
  WorkOrder VarChar(1) Consider Work Orders default=Y [Y=Yes, N=No]
  MinStckLvl VarChar(1) Minimum Inventory Level default=N [Y=Yes, N=No]
  FCTAbs Int(11) Forecast Absolute Entry ->OFCT
  SortBy VarChar(1) Sort By default=L [L=Assembly Sequence, C=Item Number, N=Item Description, G=Item Group]
  ItmReq VarChar(1) Items Without Requirement default=N [Y=Yes, N=No]
  Simulation VarChar(1) Is Scenario a Simulation default=N [Y=Yes, N=No]
  UpdateDate Date(8) Update Date
  UpdateBy nVarChar(20) Update By
  LastExecDa Date(8) Last Execute Date
  AllItems VarChar(1) All Items default=Y
  ByCompany VarChar(1) By Company default=Y
  IncHisData VarChar(1) Include Historical Data default=N [Y=Yes, N=No]
  ResInv VarChar(1) Reserve Invoice default=N [Y=Yes, N=No]
  Wtrq VarChar(1) Inventory Transfer Request default=N [Y=Yes, N=No]
  InvtLevel VarChar(1) Inventory Level default=D [D=, R=Required, I=Minimum, A=Maximum, M=Minimum - Maximum]
  RcmPO VarChar(1) Recommend Purchase Order default=N [Y=Yes, N=No]
  RcmWO VarChar(1) Recommend Production Order default=Y [Y=Yes, N=No]
  RcmWTRQ VarChar(1) Recommend ITRQ default=N [Y=Yes, N=No]
  RCMDefWhs VarChar(1) Recommend to Default Warehouse default=Y [Y=Yes, N=No]
  OnlyNettbl VarChar(1) Only Nettable default=Y [Y=Yes, N=No]
  ExpandedPO VarChar(1) Expanded Purchase Order default=N
  ExpandedSO VarChar(1) Expanded Sales Order default=N [Y=Yes, N=No]
  RcmCalDate Date(8) Recommendation Calculated Date
  RcmCalTime Int(11) Recommendation Calculated Time
  PurchOAT VarChar(1) Blanket Purchase Agreement default=Y [Y=Yes, N=No]
  SalesOAT VarChar(1) Blanket Sales Agreement default=Y
  Rots VarChar(1) Recurring Order Transactions default=N [Y=Yes, N=No]
  ExpdResINV VarChar(1) Expanded Reserve Invoice default=N
  ExpdWOR VarChar(1) Expanded Production Order default=N [Y=Yes, N=No]
  IgnoreCLT VarChar(1) Ignore Cumulative Lead Time default=N [Y=Yes, N=No]
  PurchReq VarChar(1) Consider Purchase Request default=N [Y=Yes, N=No]
  PurchQuota VarChar(1) Consider Purchase Quotations default=N [Y=Yes, N=No]
  SalesQuota VarChar(1) Consider Sales Quotations default=N [Y=Yes, N=No]
  ExpdPurReq VarChar(1) Expanded Purchase Request default=N [Y=Yes, N=No]
  ExpdPQuota VarChar(1) Expanded Purchase Quotations default=N [Y=Yes, N=No]
  ExpdSQuota VarChar(1) Expanded Sales Quotations default=N [Y=Yes, N=No]
  ExpdPAgree VarChar(1) Expanded Purchase Agreements default=N [Y=Yes, N=No]
  ExpdSAgree VarChar(1) Expanded Sales Agreements default=N [Y=Yes, N=No]
  ExpdTraReq VarChar(1) Expanded Transfer Request default=N [Y=Yes, N=No]
  DisSelItem VarChar(1) Display Selected Item Only default=N [Y=Yes, N=No]

# ORCM - Recommendation Data
Module: MRP | 31 columns | ObjType: 213
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjAbs Int(11) Document Internal Number
  ObjType Int(11) Document Number
  ItemCode nVarChar(50) Item No. ->OITM
  DueDate Date(8) Order Due Date
  OrderType VarChar(1) Order Type default=P [P=Purchase Order, W=Production Order, T=Inventory Transfer Request, Q=Purchase Quotation, R=Purchase Request]
  Quantity Num(19,6) Quantity
  UOM nVarChar(100) Buy or Inventory UoM
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  Warehouse nVarChar(8) Warehouse ->OWHS
  Price Num(19,6) Price After Discount
  Currency nVarChar(3) Price Currency
  Origin VarChar(1) Order Origin default=M [M=MRP]
  Status VarChar(1) Order Status default=O [O=Opened, A=Accepted, P=Processed, D=Deleted]
  UserSign Int(6) User Signature ->OUSR
  DocDate Date(8) Generation Date
  DocTime Int(6) Generation Time
  BPLid Int(11) Business Place ID default=-1
  PriceBefDi Num(19,6) Unit Price
  DiscPrcnt Num(19,6) Discount % Per Row
  ReleasDate Date(8) Release Date
  PriceAftV Num(19,6) Price after VAT
  FromWhse nVarChar(8) From Warehouse
  FstReqDate Date(8) First Request Date
  UomEntry Int(11) UoM Entry
  NumPerMsr Num(19,6) UoM Value
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  UseDiscnt VarChar(1) Use BP Special Price default=Y [Y=Yes, N=No]
  PriceMode VarChar(1) Price Mode [N=Net, G=Gross]
  RouDatCalc VarChar(1) Routing Date Calculation [S=On Start Date, D=On End Date, F=Start Date Onwards, B=End Date Backwards]
