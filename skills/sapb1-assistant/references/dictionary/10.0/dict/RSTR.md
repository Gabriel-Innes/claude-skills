<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RSTR - STRL resource
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Name
  NUM U: Language, Num
  M_NUM: Num
  M_NAME: Name
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) STRL name
  Num Int(11) STRL number
  MaxUnique Int(11) Max Unique
