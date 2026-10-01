<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VTR1 - Tax Groups
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Adtnl_Key, ObjectCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs Entry (Numerator)
  ObjectCode nVarChar(30) Object Code
  Sum VarChar(1) Sum default=N [Y=Yes, N=No]
  DispOrder Int(11) Display Order
  ObjectType VarChar(1) Object Type
  Selected VarChar(1) Selected Object [Y=Yes, N=No]
  FromObject nVarChar(20) From Object
  ToObject nVarChar(20) To Object
  Adtnl_Key VarChar(1) Additional Key
  Amount Num(19,6) Amount
