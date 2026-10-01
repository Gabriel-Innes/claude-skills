<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# IGE8 - Items in Package - Goods Issue
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum, ItemCode, UomEntry, NumPerMsr
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OIGE
  PackageNum Int(11) Package Number
  ItemCode nVarChar(50) Item Code ->OITM
  Quantity Num(19,6) Quantity
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=60 ->ADP1
  UomEntry Int(11) UoM Entry default=0 ->OUOM
  unitMsr nVarChar(100) Unit
  NumPerMsr Num(19,6) UoM Value default=0
