<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WOR2 - Production Order - Base
Module: Inventory and Production | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, BaseEntry, BaseLine
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal Number ->OWOR
  BaseEntry Int(11) Production Order Base Entry ->ORDR
  BaseNum Int(11) Production Order Base Number
  BaseLine Int(11) Production Order Base Line
  LogInstanc Int(11) Log Instance default=0
