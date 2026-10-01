<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUGR - Authorization Group
Module: General | 9 columns | ObjType: 231000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupId
  NAME_KEY U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupId Int(6) Authorization Group ID
  GroupName nVarChar(155) Group Name
  GroupDec nVarChar(155) Group Description
  Allowences Text(16) Allowances
  TPLId Int(6) Template ID ->UICU
  StartDate Date(8) Start Date
  DueDate Date(8) Due Date
  GroupType VarChar(1) Group Type default=A [A=Authorization, F=Form Settings, T=Alerts, U=UI Configuration Templates, L=All]
  CockpitId Int(6) Cockpit Template ID
