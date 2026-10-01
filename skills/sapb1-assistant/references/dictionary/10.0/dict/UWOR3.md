<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UWOR3 - Production Order - Closure
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LayerID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number
  LineNum Int(11) Row Number
  LayerID Int(11) Layer ID
  Quantity Num(19,6) Quantity
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RToStockSc Num(19,6) Reval. Amt Posted to Stock SC
  WhsCode nVarChar(8) Warehouse Code
  IVLTransSe Int(11) IVL Transaction Sequence No.
  IVLLayerID Int(11) IVL Layer ID
  SnbSysNum Int(11) SNB System Number
  SnbAbsEnt Int(11) SNB Abs. Entry
  LogInstanc Int(11) Log Instance default=0
  INMSubLine Int(11) INM Subrow Number default=-1
