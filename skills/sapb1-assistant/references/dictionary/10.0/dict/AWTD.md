<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWTD - Withholding Tax Definition
Module: Finance | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WTCode nVarChar(4) WTax Code
  WTName nVarChar(50) WTax Name
  Rate Num(19,6) Rate
  EffecDate Date(8) Effective From
  Inactive VarChar(1) Inactive default=N [Y=, N=]
  OffclCode nVarChar(15) Official Code
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  BaseType VarChar(1) Base Type default=N [N=Net, V=VAT, G=Gross, H=Gross - VAT]
  WTTypeId Int(11) Type ->OWTT
  BaseMin Num(19,6) Min. Amount
  PrctBsAmnt Num(19,6) % Base Amount
  FmlId Int(11) Formula ID ->OFML
  Account nVarChar(15) Account ->OACT
  SlScProgr VarChar(1) Sliding Scale Progressive Tax default=N [Y=, N=]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CalcWHTCrM VarChar(1) Calculate Withholding Tax in Automatic Credit Memo default=Y [Y=Yes, N=No]
