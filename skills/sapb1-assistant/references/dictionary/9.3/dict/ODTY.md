<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODTY - BoE Document Type
Module: Banking | 3 columns | ObjType: 267
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  TYPE U: DocType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocType nVarChar(2) Document Type
  DocDespt nVarChar(20) Description
