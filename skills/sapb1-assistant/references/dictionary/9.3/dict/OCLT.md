<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCLT - Activity Types
Module: Business Partners | 5 columns | ObjType: 103
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(20) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, p=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
