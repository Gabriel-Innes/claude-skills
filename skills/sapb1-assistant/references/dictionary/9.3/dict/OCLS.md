<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCLS - Activity Subjects
Module: Business Partners | 6 columns | ObjType: 84
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  type U: Name, Type
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(20) Name
  Type Int(6) Related Type default=-1 ->OCLT
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
