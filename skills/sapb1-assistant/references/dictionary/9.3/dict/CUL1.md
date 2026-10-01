<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CUL1 - Customer Usage Statistics Log
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, ParrentDoc
Fields (name type(len) description [values] ->parent table):
  ParrentDoc Int(11) Parent Document
  LineNum Int(11) Line Number
  Param Text(16) Parameter
