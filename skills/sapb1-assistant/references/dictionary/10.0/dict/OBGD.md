<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBGD - Budget Cost Assess. Mthd
Module: Finance | 17 columns | ObjType: 78
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BgdCode
  NAME U: BgdName
Fields (name type(len) description [values] ->parent table):
  BgdCode Int(11) Division Code
  BgdName nVarChar(30) Description
  BgdTotal Num(19,6) Budget Amount
  Month1 Num(19,6) January
  Month2 Num(19,6) February
  Month3 Num(19,6) March
  Month4 Num(19,6) April
  Month5 Num(19,6) May
  Month6 Num(19,6) June
  Month7 Num(19,6) July
  Month8 Num(19,6) August
  Month9 Num(19,6) September
  Month10 Num(19,6) October
  Month11 Num(19,6) November
  Month12 Num(19,6) December
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
