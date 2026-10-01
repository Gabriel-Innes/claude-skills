<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OAIM - Archive Inventory Message
Module: Inventory and Production | 49 columns
Indexes (name: columns; first = primary key; U = unique):
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
