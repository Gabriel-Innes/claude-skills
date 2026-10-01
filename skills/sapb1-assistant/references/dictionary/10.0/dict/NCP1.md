<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# NCP1 - New Cockpit Tile
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PageEntry Int(11) Page Number
  Type nVarChar(20) Type
  WidgetId Int(11) Widget ID
  Size nVarChar(10) Size default=1x1
  Index Int(11) Index default=0
  Settings Text(16) Settings
