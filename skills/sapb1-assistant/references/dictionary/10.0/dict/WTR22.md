<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WTR22 - Inventory Transfer - Resource Costs
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->WTR1
  LineNum Int(11) Row Number ->WTR1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=67
  LogInstanc Int(11) Log Instance default=0
