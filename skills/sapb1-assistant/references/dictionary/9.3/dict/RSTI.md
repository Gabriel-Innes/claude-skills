<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RSTI - STRI resource
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num, Name, Language
  M_NUM: Num, Name
  UNIQUE_ID U: UniqueID, Name, Language
Fields (name type(len) description [values] ->parent table):
  Created Date(8) Creation date
  Updated Date(8) Update date
  Language Int(11) Language code
  Name nVarChar(64) STRL name ->STRL
  Num Int(11) String number
  String nVarChar(250) String
  StringLen Int(11) String length
  UniqueID nVarChar(10) Unique ID
