<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWTM - Approval Templates
Module: Administration | 8 columns | ObjType: 121
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WtmCode
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  Name nVarChar(20) Name
  Remarks nVarChar(100) Description
  Conds VarChar(1) Conditions default=N [Y=Yes, N=No]
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  PmptChg VarChar(1) Prompt Change default=Y [Y=Yes, N=No]
  AppOnUpd VarChar(1) Apply on Update default=Y [Y=Yes, N=No]
