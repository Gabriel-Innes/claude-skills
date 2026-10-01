<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# STNG - STNG
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: num, lang
Fields (name type(len) description [values] ->parent table):
  lang Int(11) Language
  num Int(11) Number
  string nVarChar(254) String
