<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DPI22 - A/R Down Payment - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: StdCostNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->DPI1
  LineNum Int(11) Row Number ->DPI1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=203
  LogInstanc Int(11) Log Instance default=0
