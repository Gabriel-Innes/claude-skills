<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# LGL1 - Legal Data - Rows
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OLGL
  LineSeq Int(11) Line Sequence
  LineType VarChar(1) Line Type default=R [T=Document Total, R=Tax Per Line, V=Total Tax]
  TaxCode nVarChar(8) Tax Code
  TaxRate Num(19,6) Tax Rate
  Amount Num(19,6) Amount
