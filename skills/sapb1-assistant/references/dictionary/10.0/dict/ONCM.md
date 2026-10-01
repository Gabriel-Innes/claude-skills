<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ONCM - NCM Code
Module: Administration | 8 columns | ObjType: 257
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: NcmCode, GroupCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  NcmCode nVarChar(15) NCM Code
  Descrip nVarChar(254) Description
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  GroupCode VarChar(1) Group Code default=L
  Group Int(6) NCM Group ->ONCG
