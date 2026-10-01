<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIDT - Employee ID Type
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IDType
Fields (name type(len) description [values] ->parent table):
  IDType nVarChar(30) ID Type
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
