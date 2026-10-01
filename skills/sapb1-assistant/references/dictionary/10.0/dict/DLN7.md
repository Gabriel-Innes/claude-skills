<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DLN7 - Delivery Packages
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, PackageNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODLN
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=15 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV
