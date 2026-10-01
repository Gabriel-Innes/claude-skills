<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HMM3 - OHMM Child Table
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OHMM
  LineNum Int(11) Line Number
  LangCode nVarChar(8) Language Code
  LangDesc nVarChar(50) Language Description
