<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIN2 - Inventory Counting - UoM
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, ChildNum, LineNum, DocEntry
  BUSINESS U: LogIns, UomCode, BarCode, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  BarCode nVarChar(254) Bar Code
  UomCode nVarChar(20) UoM Code ->OUOM
  UomQty Num(19,6) UoM Counted Qty
  CountQty Num(19,6) Counted Qty of Inventory UoM
  Tk1UomQty Num(19,6) Counter 1 UoM Counted Qty
  Tk2UomQty Num(19,6) -
  Tk1CntQty Num(19,6) Counter 1 Counted Qty of Inv.
  Tk2CntQty Num(19,6) -
  ItmsPerUnt Num(19,6) Items per Unit
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  TeamUomQty Num(19,6) Team UoM Counted Qty
  TeamCntQty Num(19,6) Team Counted Qty
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
