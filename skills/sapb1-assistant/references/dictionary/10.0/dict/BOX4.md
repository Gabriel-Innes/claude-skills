<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BOX4 - Box Definition - Contra Accounts of Accounts
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, Account, BosCode, ContraAct
Fields (name type(len) description [values] ->parent table):
  ReportType VarChar(1) Report Type default=B [B=, S=]
  EffecDate Date(8) Effective From
  BoxCode nVarChar(30) Group Code
  Account nVarChar(15) Account
  ContraAct nVarChar(15) Offset Account
  SeqNum Int(11) Sequence Number
  BosCode Int(11) Box Set Code ->OBOS
