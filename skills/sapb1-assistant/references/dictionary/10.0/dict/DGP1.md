<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DGP1 - Customer List
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CardCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  CardCode nVarChar(15) Customer Code ->OCRD
  CardName nVarChar(100) Customer Name
  Checked VarChar(1) Checked default=Y [Y=Yes, N=No]
  CtrlAcct nVarChar(15) Control Account
