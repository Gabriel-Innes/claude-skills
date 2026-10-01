<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SIVL1 - IVL Layer Level
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TransSeq, LayerID
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No. ->OIVL
  LayerID Int(11) Layer ID
  CalcPrice Num(19,6) Calculated Price
  Balance Num(19,6) Stock Balance
  TransValue Num(19,6) Transaction Value
  LayerInQty Num(19,6) Receipt Quantity
  LayerOutQ Num(19,6) Issue Quantity
  RevalTotal Num(19,6) Inventory Revaluation Total
