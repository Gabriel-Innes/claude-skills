<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EDG1 - Discount Groups Rows
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ObjType, ObjKey
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry ->OEDG
  ObjType nVarChar(20) Object Type [52=Item Groups, 8=Item Properties, 43=Manufacturer, 4=Items]
  ObjKey nVarChar(50) Object Key
  DiscType VarChar(1) Discount Type default=D [D=Discount, P=Pay for/Get for Free]
  Discount Num(19,6) Discount
  PayFor Num(19,6) Paid Qty
  ForFree Num(19,6) Free Qty
  UpTo Num(19,6) Max. Free Qty
  LogInstanc Int(11) Log Instance default=0
