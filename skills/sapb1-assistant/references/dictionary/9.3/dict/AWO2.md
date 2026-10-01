<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWO2 - Production Order - Base
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, BaseLine, BaseEntry, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  BaseEntry Int(11) Production Order Base Entry ->RDR1
  BaseNum Int(11) Production Order Base Number
  BaseLine Int(11) Production Order Base Line
  LogInstanc Int(11) Log Instance default=0
