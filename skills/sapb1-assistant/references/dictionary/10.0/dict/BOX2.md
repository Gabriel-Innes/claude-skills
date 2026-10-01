<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BOX2 - Box Definition - Accounts
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, Account, BosCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Group Code
  ReportType VarChar(1) Report Type default=B [B=, S=]
  Account nVarChar(15) Account ->OACT
  SeqNum Int(11) Sequence Number
  EffecDate Date(8) Effective From
  BosCode Int(11) Box Set Code ->OBOS
