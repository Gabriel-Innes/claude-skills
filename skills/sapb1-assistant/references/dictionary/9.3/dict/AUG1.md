<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AUG1 - UoM Group Detail
Module: Inventory and Production | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, UgpEntry
Fields (name type(len) description [values] ->parent table):
  UgpEntry Int(11) UoM Group Abs. Entry ->OUGP
  UomEntry Int(11) UoM Abs. Entry ->OUOM
  AltQty Num(19,6) Alternative Quantity
  BaseQty Num(19,6) Base Quantity
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  WghtFactor Int(6) Weight Factor default=0 ->OWGT
  UdfFactor Int(11) UDF Factor default=-1
