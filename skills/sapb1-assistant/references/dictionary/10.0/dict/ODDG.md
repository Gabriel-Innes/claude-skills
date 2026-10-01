<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODDG - Withholding Tax Deduction Groups
Module: Finance | 6 columns | ObjType: 117
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Numerator
  NAME U: DdgCode, DdgName
Fields (name type(len) description [values] ->parent table):
  Numerator Int(11) Group Key
  DdgCode nVarChar(2) Group Code ->ODGL
  DdgName nVarChar(30) Group Name
  DdctPrcnt Num(19,6) Max. Red. in %
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
