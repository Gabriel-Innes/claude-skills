<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OIDX - CPI Codes
Module: Administration | 5 columns | ObjType: 38
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IdexCode
Fields (name type(len) description [values] ->parent table):
  IdexCode nVarChar(3) Code
  IndexName nVarChar(50) Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
