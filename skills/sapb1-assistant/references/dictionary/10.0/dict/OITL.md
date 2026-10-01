<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OITL - Inventory Transactions Log
Module: Inventory and Production | 40 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogEntry
  DOC_INFO: ManagedBy, DocType, DocEntry, DocLine, SubLineNum
  BASEREF: BaseType, BaseEntry, BaseLine, BSubLineNo
  APPLYREF: ApplyType, ApplyEntry, ApplyLine, AppSubLine
  TRANSID: TransId
  ACTUAL_INF: ManagedBy, ActBaseTp, ActBaseEnt, ActBaseLn, ActBasSubL
  ALLOC_REF: AllocateTp, AllocatEnt, AllocateLn
  DOC_REF: DocType, DocEntry, DocLine, LogEntry
  ITEM_CODE: ItemCode, LocCode, ManagedBy, Instance, ApplyEntry, ApplyType, LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Internal ID
  TransId Int(11) Transaction ID
  ItemCode nVarChar(50) Item Code ->OITM
  ItemName nVarChar(200) Item Description
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
  VersionNum nVarChar(13) Version Number
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
