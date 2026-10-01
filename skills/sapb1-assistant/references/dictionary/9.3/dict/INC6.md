<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# INC6 - Inventory Counting - Team Counter - Row UoM
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CounterNum, ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  CounterNum Int(11) Counter Number
  UomQty Num(19,6) UoM Counted Qty
  InvtQty Num(19,6) Counted Qty of Inventory UoM
  LogIns Int(11) Log Instance - History
