<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTRC - Journal Entry Codes
Module: Finance | 6 columns | ObjType: 45
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrnsCode
  DESCRIP: TrnsCodDsc
Fields (name type(len) description [values] ->parent table):
  TrnsCode nVarChar(4) Code
  TrnsCodDsc nVarChar(20) Description
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Pcn874Ctg VarChar(1) Trans. Category for PCN874 default=N [N=None, I=Import Log, E=Export Log, O=Other, R=A/R Invoice - Palestinian Territory, P=A/P Invoice - Palestinian Territory, M=Self-Employed - Sales, C=Self-Employed - Purchase]
