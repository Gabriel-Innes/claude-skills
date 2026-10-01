<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCOG - Commission Groups
Module: Business Partners | 7 columns | ObjType: 65
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Commission Group Code
  GroupName nVarChar(30) Commission Group Name
  Commission Num(19,6) Commission Percentage
  PrvComsnPr Num(19,6) Prev. Commission in %
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
