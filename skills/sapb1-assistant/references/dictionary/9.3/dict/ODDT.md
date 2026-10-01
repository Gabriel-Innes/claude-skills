<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODDT - Withholding Tax Deduction Hierarchy
Module: Business Partners | 12 columns | ObjType: 116
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Numerator
  CARD U: TrcCode, WHShaamGrp, CardCode
Fields (name type(len) description [values] ->parent table):
  Numerator Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  TrcCode nVarChar(10) Hierarchy Code
  TrcName nVarChar(30) Hierarchy Name
  DateFrom Date(8) Valid From
  DateTo Date(8) Valid Until
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LastUpdate Date(8) Last Update Date
  WHShaamGrp VarChar(1) Withholding Shaam Group default=1 [1=Services and Asset, 2=Agricultural Products, 3=Insurance Commissions, 4=Withholding Tax Instructions, 5=Interest, Exchange Rate Differences]
  DdctPrcnt Num(19,6) Deduction %
  MaxSum Num(19,6) Maximum Total
