<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DGP3 - Expanded Consolidation Options
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CondNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  CondNum Int(11) Condition Number
  ConFldID nVarChar(100) Consolidation Field ID
  Checked VarChar(1) Checked default=N [Y=Yes, N=No]
