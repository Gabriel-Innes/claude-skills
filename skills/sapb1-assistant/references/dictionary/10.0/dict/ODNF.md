<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODNF - DNF Code
Module: Inventory and Production | 8 columns | ObjType: 140000041
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NCM_DNF U: NCMEntry, DNFCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  NCMEntry Int(11) NCM Code ->ONCM
  DNFCode nVarChar(5) DNF Code
  DNFUoM nVarChar(10) DNF UoM
  DNFFactor Num(19,6) DNF Factor
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
