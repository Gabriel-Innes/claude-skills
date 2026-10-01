<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# APRJ - Project Codes
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, PrjCode
Fields (name type(len) description [values] ->parent table):
  PrjCode nVarChar(20) Project Code
  PrjName nVarChar(100) Project Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
