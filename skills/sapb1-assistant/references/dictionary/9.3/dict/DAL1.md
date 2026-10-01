<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DAL1 - Mapping between form item and dashboard column
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  LinkEntry Int(11) Internal Key
  ItemID nVarChar(250) Item ID
  ObjName nVarChar(250) Object Name
  PropName nVarChar(250) Property Name
  QueryCol nVarChar(250) Query Column
  MobDesc nVarChar(250) Mobile Description
  IsUDF VarChar(1) Is UDF or Not default=N [Y=Yes, N=No]
