<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TRN2 - Subtable of OTRN
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SubLineNum, LineNum, TrnAbsEntr
  UniqueIdx U: LangCode, LineNum, TrnAbsEntr
Fields (name type(len) description [values] ->parent table):
  TrnAbsEntr Int(11) OTRN Abs Entry
  LineNum Int(11) Line Number of TRN1
  SubLineNum Int(11) Subline Number
  LangCode Int(11) Language Code
  Text Text(16) Translated Text
