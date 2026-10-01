<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBSI - Brazil String Indexer
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  IND_CODE_K U: Code, IndexType
Fields (name type(len) description [values] ->parent table):
  IndexType Int(11) Indexer Type
  Code nVarChar(30) Code
  Descr Text(16) Beverage Table
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) Unique ID
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
