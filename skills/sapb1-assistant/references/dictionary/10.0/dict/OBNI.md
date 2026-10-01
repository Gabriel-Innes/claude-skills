<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBNI - Brazil Numeric Indexer
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  IND_CODE_K U: IndexType, Code
Fields (name type(len) description [values] ->parent table):
  IndexType Int(11) Indexer Type
  Code Int(11) Code
  Descr nVarChar(254) Beverage Brand
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) ID
