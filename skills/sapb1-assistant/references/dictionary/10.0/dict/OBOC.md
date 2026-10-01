<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBOC - External Bank Operation Code Category
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CATEGORY U: OpCodeCat
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  OpCodeCat nVarChar(30) Operation Code Category
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
