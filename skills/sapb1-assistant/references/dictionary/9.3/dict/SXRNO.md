<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRNO - XLR Notes
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: noteid
Fields (name type(len) description [values] ->parent table):
  noteid nVarChar(32) noteid
  notetext Text(16) notetext
  modified Date(8) modified
  access nVarChar(50) access
