<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CPT1 - Cockpit Subtable
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SubEntry, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OCPT
  SubEntry Int(11) Subnumber
  _Title nVarChar(20) Show Title
  WdtEntry Int(11) Widget Entry ->OWDT
  _Left Int(6) Left
  _Right Int(6) Right
  _Top Int(6) Top
  _Bottom Int(6) Bottom
