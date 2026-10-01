<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# XAP2 - XAPP Widget
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Key of widget
  PageEntry Int(11) Foreign of XAPP page
  Type nVarChar(250) Widget Type
  ObjEntry Int(11) Foeign key of widget content
  Width Int(11) Width of widget
  Height Int(11) Height of widget
  Index Int(11) Order of widget
