<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UWOR - Production Order
Module: Inventory and Production | 63 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  NUM U: DocNum, PIndicator
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
  OriginType VarChar(1) Production Order Origin default=M [M=Manual, R=MRP, S=Sales Order, U=Upgrade, P=Production Order]
  UserSign Int(6) User Signature ->OUSR
  Comments nVarChar(254) Remarks
  CloseDate Date(8) Closing Date
  RlsDate Date(8) Release Date
  CardCode nVarChar(15) Customer Code ->OCRD
  Warehouse nVarChar(8) Warehouse ->OWHS
  Uom nVarChar(100) Inv. UoM in Production Order
  LineDirty Int(11) Line Modified
  JrnlMemo nVarChar(254) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  CreateDate Date(8) Creation Date
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  PIndicator nVarChar(10) Period Indicator default=' ' ->OPID
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
  CloseVerNm nVarChar(13) Closing Version Number
  StartDate Date(8) Start Date
  ObjType nVarChar(20) Object Type default=202
  ProdName nVarChar(200) Product Description
  Priority Int(6) Priority default=100
  RouDatCalc VarChar(1) Routing Date Calculation default=S [S=On Start Date, D=On End Date, F=Start Date Forwards, B=End Date Backwards]
  UpdAlloc VarChar(1) Update Allocation default=M [M=Manual, A=Auto]
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VersionNum nVarChar(13) Version Number
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SAPPassprt Text(16) Extended SAP Passport
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachment
  AsChild VarChar(1) Parent set as component default=N [Y=Parent set as component, N=Parent not set as component]
  LinkToObj nVarChar(20) Linked To default=17 [202=Production Order, 17=Sales Order]
  ProcItms VarChar(1) Procure Items default=N [Y=Yes, N=No]
  ReopOriDoc VarChar(1) Reopen Origin. Doc Cancel [Y=Yes, N=No]
