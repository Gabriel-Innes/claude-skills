<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IVM1 - Invoice Mapping Object Details
Module: Marketing Documents | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OIVM
  LineNum Int(11) Line Number
  DocType nVarChar(20) Document Type
  DocEntry Int(11) Document Entry
  GtsStatus VarChar(1) GTS Status
