<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OEXD - Freight Setup
Module: Administration | 40 columns | ObjType: 125
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ExpnsCode
  NAME U: ExpnsName
Fields (name type(len) description [values] ->parent table):
  ExpnsCode Int(11) Internal Number
  ExpnsName nVarChar(20) Name
  RevAcct nVarChar(15) Revenue Account ->OACT
  ExpnsAcct nVarChar(15) Expense Account ->OACT
  TaxLiable VarChar(1) Tax Liable default=N [Y=Yes, N=No]
  RevFixSum Num(19,6) Fixed Amount - Revenues
  ExpFixSum Num(19,6) Fixed Amount - Expenses
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  VatGroupI nVarChar(8) Output Tax Group ->OVTG
  VatGroupO nVarChar(8) Input Tax Group ->OVTG
  DistrbMthd VarChar(1) Distribution Method default=N [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  In1099 VarChar(1) Include in 1099 default=N [Y=Yes, N=No]
  ExpOfstAct nVarChar(15) Freight Clearing Account ->OACT
  WTLiable VarChar(1) WTax Liable default=N [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method default=T [N=None, Q=Quantity, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price default=N [Y=Yes, N=No]
  SalseRpt VarChar(1) Sales Analysis Report default=N [Y=Yes, N=No]
  PchRpt VarChar(1) Purchase Analysis Report default=N [Y=Yes, N=No]
  RevExmAcct nVarChar(15) Revenues Exempted Account ->OACT
  ExpnsExAct nVarChar(15) Expense Exempted Account ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account
  ExpnsType VarChar(1) Freight Type default=1 [1=Shipping, 2=Insurance, 3=Other, 4=Special]
  OcrCode nVarChar(8) Distr. Rule ->OOCR
  TaxDisMthd VarChar(1) Tax Distribution Method default=N [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distr. Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distr. Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distr. Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distr. Rule5 ->OOCR
  OcrCodeX nVarChar(100) Distr. Rule ->OOCR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User ->OUSR
  Project nVarChar(20) Project ->OPRJ
  Intrastat VarChar(1) Intrastat Relevant default=N [Y=Yes, N=No]
  GrsFreight VarChar(1) Gross Freight default=N [Y=Yes, N=No]
  SacCode nVarChar(8) SAC Code
  FreighType VarChar(1) Freight Type default=S [S=Standard, B=Bollo]
  DataVers Int(11) Data Version default=1
