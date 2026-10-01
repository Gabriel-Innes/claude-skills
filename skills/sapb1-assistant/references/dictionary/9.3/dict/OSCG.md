<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSCG - Service Category
Module: Inventory and Production | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: ServiceCtg
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  ServiceCtg nVarChar(60) Service Category
  Descrip nVarChar(120) Description
