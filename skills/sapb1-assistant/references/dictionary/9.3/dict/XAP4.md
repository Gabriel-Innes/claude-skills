<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XAP4 - Widget Item
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of filter item
  FilEntry Int(11) Foreign key of filter
  TarEntry Int(11) Target content Entry
  TarType nVarChar(250) Target content type
  TarField nVarChar(250) Target field
  IsBase VarChar(1) Is base or not
