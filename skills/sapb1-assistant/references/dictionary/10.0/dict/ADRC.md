<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ADRC - G/L Account Determination Criteria - Resources - History
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DmcId, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DmcId Int(11) Determination ID
  DmcAlias nVarChar(100) Determination Alias
  Active VarChar(1) Determination Status default=N [Y=Yes, N=No]
  Priority Int(6) Determination Priority
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  AdvRulCol Int(6) Advanced Rules Column
