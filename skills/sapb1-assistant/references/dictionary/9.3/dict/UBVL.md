<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UBVL - Serial Numbers and Batch Valuation Log
Module: General | 36 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
