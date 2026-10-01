<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ADO22 - Marketing Document (Resource Costs) - History
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, StdCostNum, LogInstanc, ObjectType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADO1
  LineNum Int(11) Row Number ->ADO1
  StdCostNum Int(11) Resource Standard Cost Number
  Price Num(19,6) Price
  Total Num(19,6) Total
  ObjectType nVarChar(20) Object Type default=13
  LogInstanc Int(11) Log Instance default=0
