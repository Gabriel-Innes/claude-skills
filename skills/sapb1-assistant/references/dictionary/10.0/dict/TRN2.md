<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TRN2 - Subtable of OTRN
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrnAbsEntr, LineNum, SubLineNum
  UniqueIdx U: TrnAbsEntr, LineNum, LangCode
Fields (name type(len) description [values] ->parent table):
  TrnAbsEntr Int(11) OTRN Abs Entry
  LineNum Int(11) Line Number of TRN1
  SubLineNum Int(11) Subline Number
  LangCode Int(11) Language Code
  Text Text(16) Translated Text
