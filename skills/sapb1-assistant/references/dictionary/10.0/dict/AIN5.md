<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AIN5 - Inventory Counting - Team Counters - Row Counted Qty - History
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, CounterNum, LogIns
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  CounterNum Int(11) Counter Number
  TotalQty Num(19,6) Total Qty of Inventory UoM
  LogIns Int(11) Log Instance - History
