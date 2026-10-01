<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ULNG - ULNG
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: lineNum, lang
Fields (name type(len) description [values] ->parent table):
  lang Int(11) Language Id
  lineNum Int(11) Line Number
  string nVarChar(254) String
