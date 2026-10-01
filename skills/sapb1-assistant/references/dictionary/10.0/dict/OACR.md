<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OACR - Accrual Type
Module: Finance | 8 columns | ObjType: 540000048
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Accrual Type Code
  Name nVarChar(30) Accrual Type Name
  PostingAct nVarChar(15) Posting Account ->OACT
  CalcAcct nVarChar(15) Calculation Account ->OACT
  InterimAct nVarChar(15) Interim Account ->OACT
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
