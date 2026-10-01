<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WTQ7 - Inventory Transfer Request - Delivery Packages
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID ->OWTQ
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=1250000001 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV
