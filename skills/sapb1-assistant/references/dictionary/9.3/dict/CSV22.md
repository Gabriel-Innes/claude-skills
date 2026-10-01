<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CSV22 - A/R Correction Invoice Reversal - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: StdCostNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->CSV1
  LineNum Int(11) Row Number ->CSV1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=166
  LogInstanc Int(11) Log Instance default=0
