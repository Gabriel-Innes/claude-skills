<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AMR2 - Inventory Revaluation FIFO Rows (Archive)
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BaseLine, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->MRV1
  BaseLine Int(11) Base Row Number
  LineNum Int(11) Row Number
  Quantity Num(19,6) Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RActPrice Num(19,6) Inventory Reval. Current Cost
  INMTransNm Int(11) INM Transaction Number ->OINM
  INMInst Int(11) INM Instance ->OINM
  INMTransTy Int(11) INM Transaction Type default=-1 ->OINM
  INMCreatBy Int(11) INM Document Key Created ->OINM
  INMBaseRef nVarChar(11) INM Base Reference ->OINM
  INMDocDate Date(8) INM Posting Date ->OINM
  INMOpenQty Num(19,6) INM Open Quantity ->OINM
  ObjType nVarChar(20) Object Type default=162
  LogInstanc Int(11) Log Instance default=0
  IVLTransSe Int(11) IVL Transaction Sequence No. default=-1
  IVLLayerID Int(11) IVL Layer ID default=-1
  INMLineNum Int(11) INM Row Number in Document ->OINM
  INMSubLine Int(11) INM Subrow Number ->OINM
