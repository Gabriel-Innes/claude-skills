<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTRB - Tax Report Wizard for Brazil
Module: Reports | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: RunName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BPLId Int(11) Branch ID ->OBPL
  GPCId Int(11) Government Payment Code ->OGPC
  GPCCode nVarChar(6) Government Payment Code
  Year Int(6) Reporting Year
  PrdType VarChar(1) Period Type [Q=Quarter, M=Month, H=Half Month, T=Ten Days]
  PrdNum Int(11) Period Number
  PrdDate Date(8) Period Date To
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  Status VarChar(1) Wizard Run Status [S=Saved, E=Executed, C=Canceled]
  StateTax VarChar(1) State Tax default=N [Y=Yes, N=No]
  DueDate Date(8) Due Date
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Generation Time
  UpdateDate Date(8) Date of Update
