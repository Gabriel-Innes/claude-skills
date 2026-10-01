<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMLS - Distribution List
Module: Administration | 4 columns | ObjType: 87
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(30) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
