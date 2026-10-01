<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPTF - BoE Portfolio
Module: Banking | 5 columns | ObjType: 268
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  ID U: PtfId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PtfId nVarChar(3) Internal Portfolio ID
  PtfCode nVarChar(2) Portfolio Code
  PtfNum nVarChar(4) Portfolio Number
  PtfDespt nVarChar(20) Description
