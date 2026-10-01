<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCCT - Cost Center Type
Module: Finance | 4 columns | ObjType: 540000042
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CctCode
Fields (name type(len) description [values] ->parent table):
  CctCode nVarChar(8) Cost Center Type Code
  CctName nVarChar(30) Cost Center Type Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
