<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UILM - IVI Inventory Log Message
Module: Inventory and Production | 89 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MessageID
  CARD: BPCardCode
  DocLine: TransType, DocEntry, DocLineNum, SubLineNum
  APPOBJ: ApplObj, AppObjAbs, AppObjType, AppObjLine
  BASEOBJ: BaseType, BaseAbsEnt, BaseLine, BSubLineNo
  EntryType: DocEntry, TransType, MessageID
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
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  CreateDate Date(8) Creation Date
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  DocPrice Num(19,6) Doc Price
  CardName nVarChar(100) BP Name
  Dscription nVarChar(200) Item Description
  TreeType VarChar(1) BOM Type default=N [N=Not a BOM, A=Assembly, S=Sales, I=BOM Component Item, P=Production, T=Template]
  ApplObj Int(11) Applied Object default=-1
  AppObjAbs Int(11) Applied Object Internal ID default=-1
  AppObjType VarChar(1) Applied Object Type
  AppObjLine Int(11) Applied Object Row default=-1
  BASE_REF nVarChar(11) Base Reference
  TransSeqRf Int(11) Transaction Sequence Ref default=-1
  LayerIDRef Int(11) Layer ID Reference default=-1
  VersionNum nVarChar(13) Version Number
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
  Ref3 nVarChar(100) Reference 3
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
