<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DGP4 - Business Place List
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  LineNum Int(11) Line Number
  BPLId Int(11) Business Place ID ->OBPL
  BPLName nVarChar(100) Business Place Name
  Checked VarChar(1) Checked default=Y [Y=, N=]
