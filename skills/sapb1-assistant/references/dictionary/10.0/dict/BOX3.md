<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BOX3 - Box Definition - Choice
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, Value, BosCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Group Code
  ReportType VarChar(1) Report Type default=B [B=, S=]
  Value nVarChar(8) Value
  Descr nVarChar(250) Description
  EffecDate Date(8) Effective From
  BosCode Int(11) Box Set Code ->OBOS
  IsDefault VarChar(1) Is Default default=N [Y=Yes, N=No]
