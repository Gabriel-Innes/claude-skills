<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBNI - Brazil Numeric Indexer
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ID
  IND_CODE_K U: Code, IndexType
Fields (name type(len) description [values] ->parent table):
  IndexType Int(11) Indexer Type
  Code Int(11) Code
  Descr nVarChar(254) Beverage Brand
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) ID
