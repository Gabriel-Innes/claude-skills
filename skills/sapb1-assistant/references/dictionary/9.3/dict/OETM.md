<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OETM - EWB Transportation Mode
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  MODE_CODE U: ModeCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ModeCode Int(11) EWB Transportation Mode Code
  ModeName nVarChar(50) EWB Transportation Mode Name
