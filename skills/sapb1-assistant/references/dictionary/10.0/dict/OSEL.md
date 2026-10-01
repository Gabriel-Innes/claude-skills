<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSEL - Selection Lists
Module: Reports | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  UserID Int(6) User Signature ->OUSR
  FilterName nVarChar(30) Filter Name default=_
  FormNum nVarChar(20) Form Number
  AbsEntry Int(11) Internal ID
