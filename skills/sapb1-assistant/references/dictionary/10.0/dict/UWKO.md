<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UWKO - Production Instructions
Module: Inventory and Production | 31 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OrderNum
  SERIAL U: SerialNum, Instance
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
  JrnlMemo nVarChar(254) Journal Remarks
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ObjType nVarChar(20) Object Type default=68 ->ADP1
  UserSign Int(6) User Signature ->OUSR
  PriceList Int(6) Price List default=1 ->OPLN
  FinncPriod Int(11) Posting Period ->OFPR
  SysRate Num(19,6) System Rate
