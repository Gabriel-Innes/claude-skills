<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXREL - XLR Event Log
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: EventId
Fields (name type(len) description [values] ->parent table):
  EventId Int(11) EventId
  Type Int(11) Type
  Text Text(16) Text
  Date Date(8) Date
