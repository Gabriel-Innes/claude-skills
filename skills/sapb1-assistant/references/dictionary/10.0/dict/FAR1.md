<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# FAR1 - Fixed Asset Revaluation - Rows
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OFAR
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  NBV Num(19,6) NBV
  New_NBV Num(19,6) New NBV
  Remarks nVarChar(100) Remarks
  RevalPerc Num(19,6) Revaluation Percentage %
  OrdDprDur Num(19,6) Ordinary Depr. During Period
  UnDpDur Num(19,6) Unplanned Depr. During Period
  SpDprDur Num(19,6) Special Depr. During Period
  WriteUpDur Num(19,6) Write-Up During Period
