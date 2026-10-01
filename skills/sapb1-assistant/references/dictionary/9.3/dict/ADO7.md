<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ADO7 - Delivery Packages - History
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, ObjType, PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ADOC
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
