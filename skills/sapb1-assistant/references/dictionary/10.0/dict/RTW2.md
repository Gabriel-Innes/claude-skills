<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RTW2 - Boleto Retorno Wizard: Import Archive
Module: Banking | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry
  SequenceNo Int(11) Sequence No.
  StampDate Date(8) Time Stamp Date
  RetFile nVarChar(254) Retorno File
  Format nVarChar(100) File Format Name
  BankCode nVarChar(30) Bank Code
  Account nVarChar(50) Acct No.
  RunType VarChar(1) Run Type default=D [D=Draft, X=Executed]
  RunRecords Int(11) Run Records
  ImCardName VarChar(1) Import Card Name default=N
  PostDate Date(8) Posting Date
