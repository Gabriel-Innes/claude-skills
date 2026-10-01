<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OACG - Account Category
Module: Finance | 6 columns | ObjType: 238
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  SECOND U: Source, Name
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Name nVarChar(40) Name
  Source VarChar(1) Source default=B [B=Balance Sheet, P=Profit and Loss, C=Trial Balance, O=Other]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DateSource VarChar(1) Date Source [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Document Date, P=Partner Implementation, T=Year Transfer]
  UserSign nVarChar(6) User Signature ->OUSR
