<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GPA6 - Product Cost Adjustment - Applied Material Revaluations
Module: Marketing Documents | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  PODocAbs Int(11) PO Document Abs. Entry
  Applied Num(19,6) Applied Adjustment
