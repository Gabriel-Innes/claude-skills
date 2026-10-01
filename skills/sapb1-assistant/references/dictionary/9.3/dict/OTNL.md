<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
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
