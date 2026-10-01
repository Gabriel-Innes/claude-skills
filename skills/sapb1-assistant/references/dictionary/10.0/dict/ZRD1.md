<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ZRD1 - POS Daily Summary - Totals
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  CODE U: Code, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Internal ID ->OZRD
  LineNum Int(11) Row Number
  Code nVarChar(8) Totalizer Code
  Number Int(11) Totalizer Number
  TotalSum Num(19,6) Total Sum
  Descriptn nVarChar(254) Description
