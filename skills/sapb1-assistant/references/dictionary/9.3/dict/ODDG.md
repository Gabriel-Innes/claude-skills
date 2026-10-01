<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODDG - Withholding Tax Deduction Groups
Module: Finance | 6 columns | ObjType: 117
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Numerator
  NAME U: DdgName, DdgCode
Fields (name type(len) description [values] ->parent table):
  Numerator Int(11) Group Key
  DdgCode nVarChar(2) Group Code ->ODGL
  DdgName nVarChar(30) Group Name
  DdctPrcnt Num(19,6) Max. Red. in %
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
