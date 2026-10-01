<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AUG1 - UoM Group Detail
Module: Inventory and Production | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UgpEntry, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  UomEntry Int(11) UoM Abs. Entry ->OUOM
  AltQty Num(19,6) Alternative Quantity
  BaseQty Num(19,6) Base Quantity
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  WghtFactor Int(6) Weight Factor default=0 ->OWGT
  UdfFactor Int(11) UDF Factor default=-1
  IsActive VarChar(1) Is Active or Not default=Y [Y=Yes, N=No]
