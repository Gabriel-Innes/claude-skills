<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RTL1 - Resource Transaction Log
Module: Inventory and Production | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BaseLogEnt, StdCostNum, LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Log Entry ID
  StdCostNum Int(11) Resource Standard Cost Number
  BaseLogEnt Int(11) Base Log Entry ID default=-1 ->ORTL
  DocQty Num(19,6) Doc. Quantity
  Price Num(19,6) Price
  Total Num(19,6) Total
  OpenTotal Num(19,6) Open Total
