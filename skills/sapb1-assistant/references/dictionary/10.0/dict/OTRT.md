<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OTRT - Posting Templates
Module: Finance | 11 columns | ObjType: 55
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrtCode
Fields (name type(len) description [values] ->parent table):
  TrtCode nVarChar(8) Template Code
  Dscription nVarChar(60) Template Description
  FrgnMode VarChar(1) FC Template default=Y [Y=Yes, N=No]
  Memo nVarChar(50) Details
  TransCode nVarChar(4) Transaction Code
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  StampTax VarChar(1) Stamp Tax default=N [Y=Yes, N=No]
  AutoVat VarChar(1) Automatic VAT default=N [Y=Yes, N=No]
  ManageWTax VarChar(1) Manage WTax default=N [Y=Yes, N=No]
  DeferedTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
