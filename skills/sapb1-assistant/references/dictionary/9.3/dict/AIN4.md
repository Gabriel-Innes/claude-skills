<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIN4 - Inventory Counting - Team Counters
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogIns, CounterNum, DocEntry
  BUSINESS U: LogIns, CounterId, CounteType, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  CounterNum Int(11) Counter Number
  CounteType Int(11) Type of Counter default=12 [12=User, 171=Employee]
  CounterId Int(11) Counter ID
  CounteName nVarChar(155) Counter Name
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order
