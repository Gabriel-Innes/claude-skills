<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OEI14 - Outgoing Excise Invoice - Assembly - Rows
Module: Marketing Documents | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ChildNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OOEI
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=140000009 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
  EncryptIV nVarChar(100) Encrypt IV
