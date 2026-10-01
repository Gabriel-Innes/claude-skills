<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# HMM3 - OHMM Child Table
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OHMM
  LineNum Int(11) Line Number
  LangCode nVarChar(8) Language Code
  LangDesc nVarChar(50) Language Description
