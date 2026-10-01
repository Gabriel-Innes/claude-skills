<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AMR2 - Inventory Revaluation FIFO Rows (Archive)
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, BaseLine, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->MRV1
  BaseLine Int(11) Base Row Number
  LineNum Int(11) Row Number
  Quantity Num(19,6) Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RActPrice Num(19,6) Inventory Reval. Current Cost
  INMTransNm Int(11) INM Transaction Number
  INMInst Int(11) INM Instance
  INMTransTy Int(11) INM Transaction Type default=-1
  INMCreatBy Int(11) INM Document Key Created
  INMBaseRef nVarChar(11) INM Base Reference
  INMDocDate Date(8) INM Posting Date
  INMOpenQty Num(19,6) INM Open Quantity
  ObjType nVarChar(20) Object Type default=162
  LogInstanc Int(11) Log Instance default=0
  IVLTransSe Int(11) IVL Transaction Sequence No. default=-1
  IVLLayerID Int(11) IVL Layer ID default=-1
  INMLineNum Int(11) INM Row Number in Document
  INMSubLine Int(11) INM Subrow Number
