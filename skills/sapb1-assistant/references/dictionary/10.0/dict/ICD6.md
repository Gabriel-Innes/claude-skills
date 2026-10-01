<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ICD6 - Inventory Counting Draft - Team Counter - Row UoM
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum, CounterNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ChildNum Int(11) Child Number
  CounterNum Int(11) Counter Number
  UomQty Num(19,6) UoM Counted Qty
  InvtQty Num(19,6) Counted Qty of Inventory UoM
  LogIns Int(11) Log Instance - History
