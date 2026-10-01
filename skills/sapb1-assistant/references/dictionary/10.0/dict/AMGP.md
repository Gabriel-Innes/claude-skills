<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AMGP - Material Group
Module: Inventory and Production | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  CODE U: MatGrp, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  MatGrp nVarChar(3) Material Group
  Descrip nVarChar(70) Description
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
