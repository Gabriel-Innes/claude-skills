<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ROBL - Resource Object I/E Log
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Language, RobjKey
Fields (name type(len) description [values] ->parent table):
  RobjKey Int(11) Resource Object Key
  Language Int(11) Language
  ImportDate Date(8) Date Object Imported In Lang
  ImportTime Int(6) Time Imported default=0
