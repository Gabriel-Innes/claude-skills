<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RSTI - STRI resource
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, Name, Num
  M_NUM: Name, Num
  UNIQUE_ID U: Language, Name, UniqueID
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) STRL name ->STRL
  Num Int(11) String number
  String nVarChar(250) String
  StringLen Int(11) String length
  UniqueID nVarChar(10) Unique ID
