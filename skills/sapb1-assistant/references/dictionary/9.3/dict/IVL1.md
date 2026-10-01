<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IVL1 - IVL Layer Level
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LayerID, TransSeq
Fields (name type(len) description [values] ->parent table):
  TransSeq Int(11) Transaction Sequence No. ->OIVL
  LayerID Int(11) Layer ID
  CalcPrice Num(19,6) Calculated Price
  Balance Num(19,6) Stock Balance
  TransValue Num(19,6) Transaction Value
  LayerInQty Num(19,6) Receipt Quantity
  LayerOutQ Num(19,6) Issue Quantity
  RevalTotal Num(19,6) Inventory Revaluation Total
