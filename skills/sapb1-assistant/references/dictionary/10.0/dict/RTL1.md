<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RTL1 - Resource Transaction Log
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogEntry, StdCostNum, BaseLogEnt
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Entry ID
  StdCostNum Int(11) Resource Standard Cost Number
  BaseLogEnt Int(11) Base Log Entry ID default=-1 ->ORTL
  DocQty Num(19,6) Doc. Quantity
  Price Num(19,6) Price
  Total Num(19,6) Total
  OpenTotal Num(19,6) Open Total
