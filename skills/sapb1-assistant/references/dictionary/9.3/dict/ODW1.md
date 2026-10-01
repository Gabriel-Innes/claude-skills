<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODW1 - Default Open Documents
Module: General | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OODW
  DocType Int(11) Open Document Type
