<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ADMC - G/L Account Determination Criteria - Inventory - History
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, DmcId
Fields (name type(len) description [values] ->parent table):
  DmcId Int(6) Determination ID
  DmcAlias nVarChar(100) Determination Alias
  Active VarChar(1) Determination Status default=N [Y=Yes, N=No]
  Priority Int(6) Determination Priority
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  AdvRulCol Int(6) Advanced Rules Column
  IsUDF VarChar(1) Is User Defined Field default=N [Y=Yes, N=No]
