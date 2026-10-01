<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODRC - G/L Account Determination Criteria - Resources
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DmcId
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
