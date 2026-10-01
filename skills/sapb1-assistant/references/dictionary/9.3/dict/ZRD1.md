<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ZRD1 - POS Daily Summary - Totals
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  CODE U: AbsEntry, Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Internal ID ->OZRD
  LineNum Int(11) Row Number
  Code nVarChar(8) Totalizer Code
  Number Int(11) Totalizer Number
  TotalSum Num(19,6) Total Sum
  Descriptn nVarChar(254) Description
