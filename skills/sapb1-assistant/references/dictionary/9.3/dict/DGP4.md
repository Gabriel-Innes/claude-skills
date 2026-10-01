<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DGP4 - Business Place List
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  LineNum Int(11) Line Number
  BPLId Int(11) Business Place ID ->OBPL
  BPLName nVarChar(100) Business Place Name
  Checked VarChar(1) Checked default=Y [Y=, N=]
