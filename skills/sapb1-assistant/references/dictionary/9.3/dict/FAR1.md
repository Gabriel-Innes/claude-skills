<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FAR1 - Fixed Asset Revaluation - Rows
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OFAR
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  NBV Num(19,6) NBV
  New_NBV Num(19,6) New NBV
  Remarks nVarChar(100) Remarks
  RevalPerc Num(19,6) Revaluation Percentage %
