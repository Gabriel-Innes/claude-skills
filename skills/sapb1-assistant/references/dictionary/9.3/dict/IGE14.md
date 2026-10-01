<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IGE14 - Goods Issue - Assembly - Rows
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ChildNum, LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  LineNum Int(11) Row Number default=-1
  ChildNum Int(11) Child Number default=-1
  ItemCode nVarChar(50) Item no. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  Quantity Num(19,6) Quantity
  TotalQty Num(19,6) Total Quantity
  OpenQty Num(19,6) Remaining Open Quantity
  ObjectType nVarChar(20) object type default=60 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  BaseChildN Int(11) Base Child Number default=-1
