<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OKPS - KPI Set
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: KpsCode
Fields (name type(len) description [values] ->parent table):
  KpsCode nVarChar(15) KPI Set Code
  KpsName nVarChar(100) KPI Set Name
  KpsType VarChar(1) KPI Set Type default=S [S=Single, Q=Quarterly, M=Monthly, P=Multiple]
  FieldsNum Int(11) KPI Set Fields Number
  CreateDate Date(8) Create Date - History
  UserSign Int(6) Updating User - History ->OUSR
