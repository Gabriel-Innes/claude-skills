<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PRR7 - A/P Return Request - Delivery Packages
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PackageNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OINV
  PackageNum Int(11) Package Number
  PackageTyp nVarChar(30) Package Type
  Weight Num(19,6) Weight
  WeightUnit Int(6) UoM ->OWGT
  ObjType nVarChar(20) Object Type default=234000032 ->ADP1
  LogInstanc Int(11) Log Instance default=0
