<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# NCP1 - New Cockpit Tile
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PageEntry Int(11) Page Number
  Type nVarChar(20) Type
  WidgetId Int(11) Widget ID
  Size nVarChar(10) Size default=1x1
  Index Int(11) Index default=0
  Settings Text(16) Settings
