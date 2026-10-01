<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSVT - Define Summary VAT Report Type
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) VAT Report Type ID
  Name nVarChar(254) Summary VAT Report Type
  Descript nVarChar(254) Description
  NameDesc nVarChar(254) Name & Desc
