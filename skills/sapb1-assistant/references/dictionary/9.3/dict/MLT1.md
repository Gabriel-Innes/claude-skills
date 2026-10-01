<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MLT1 - Translations in user language
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LangCode, TranEntry
Fields (name type(len) description [values] ->parent table):
  TranEntry Int(11) Key From Header Table
  LangCode Int(11) Language Code of User Language
  Trans Text(16) Translation Content
