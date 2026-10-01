<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OACG - Account Category
Module: Finance | 6 columns | ObjType: 238
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  SECOND U: Name, Source
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Name nVarChar(40) Name
  Source VarChar(1) Source default=B [B=Balance Sheet, P=Profit and Loss, C=Trial Balance, O=Other]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DateSource VarChar(1) Date Source [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Document Date, P=Partner Implementation, T=Year Transfer]
  UserSign nVarChar(6) User Signature ->OUSR
