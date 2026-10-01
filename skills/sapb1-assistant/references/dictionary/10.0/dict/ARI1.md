<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ARI1 - Add-On
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USER_CODE, AddOnID
Fields (name type(len) description [values] ->parent table):
  USER_CODE nVarChar(25) User Code ->OUSR
  AddOnID Int(11) Add-On ID
  AddOnType VarChar(1) Add-On Type [M=Manual, C=Critical, A=Automatic, D=Disabled]
  EnableFlag VarChar(1) Add-On Enable Flag default=Y [Y=Yes, N=No]
