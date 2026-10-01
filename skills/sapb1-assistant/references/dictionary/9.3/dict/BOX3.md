<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BOX3 - Box Definition - Choice
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BosCode, Value, ReportType, BoxCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Group Code
  ReportType VarChar(1) Report Type default=B [B=, S=]
  Value nVarChar(8) Value
  Descr nVarChar(250) Description
  EffecDate Date(8) Effective From
  BosCode Int(11) Box Set Code ->OBOS
  IsDefault VarChar(1) Is Default default=N [Y=Yes, N=No]
