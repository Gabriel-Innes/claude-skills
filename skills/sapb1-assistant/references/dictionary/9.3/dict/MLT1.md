<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MLT1 - Translations in user language
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LangCode, TranEntry
Fields (name type(len) description [values] ->parent table):
  TranEntry Int(11) Key From Header Table
  LangCode Int(11) Language Code of User Language
  Trans Text(16) Translation Content
