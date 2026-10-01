<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SPRM - [SPRM]
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs entry
  SaCoName nVarChar(128) SAP company name
  MySAPCard nVarChar(128) My SAP card
  MeInSAP nVarChar(128) Me in SAP
  AttUser nVarChar(128) Attending user
