<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# INC9 - Inventory Counting - Individual Counters - Row Counted Qty
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CounterNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  CounterNum Int(11) Counter Number
  TotalQty Num(19,6) Total Qty of Inventory UoM
  LogIns Int(11) Log Instance - History
