<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RDCT - Dictionary
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num, Language
  STRING: String, Language
  NUM: Num
Fields (name type(len) description [values] ->parent table):
  Language Int(11) Language code
  Num Int(11) String number
  String nVarChar(250) String
  Updated Date(8) Update date
  UpdateTime Int(6) Update Time default=0
