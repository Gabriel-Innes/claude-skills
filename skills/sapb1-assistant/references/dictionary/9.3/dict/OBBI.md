<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBBI - Brazil Beverage Indexer
Module: General | 5 columns | ObjType: 540000068
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ID
  TBL_TM_GRP U: GroupCode, BrandCode, TableCode
Fields (name type(len) description [values] ->parent table):
  TableCode nVarChar(2) Beverage Table Code ->OBSI
  BrandCode Int(11) Beverage Commercial Brand Code ->OBNI
  GroupCode nVarChar(2) Beverage Group Code ->OBSI
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) ID
