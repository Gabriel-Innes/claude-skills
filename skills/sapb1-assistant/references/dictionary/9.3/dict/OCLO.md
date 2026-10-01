<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCLO - Meetings Location
Module: Business Partners | 5 columns | ObjType: 104
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(50) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
