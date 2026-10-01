<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPYB - Payment Block
Module: Banking | 2 columns | ObjType: 159
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  PAYBLOCK U: PayBlock
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PayBlock nVarChar(50) Payment Block
