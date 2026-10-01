<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SIVL - Whse Journal
Module: Inventory and Production | 78 columns
Indexes (name: columns; first = primary key; U = unique):
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
