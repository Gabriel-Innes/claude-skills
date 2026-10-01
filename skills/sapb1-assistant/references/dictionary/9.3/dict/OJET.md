<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OJET - JE Document Type
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: JEType
Fields (name type(len) description [values] ->parent table):
  JEType nVarChar(60) JE Document Type
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DocTypDesc nVarChar(254) Document Type Description
  ShortName nVarChar(254) Short Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
