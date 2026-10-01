<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCRC - Credit Cards
Module: Administration | 13 columns | ObjType: 36
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CreditCard
  CARD_NAME U: CardName
Fields (name type(len) description [values] ->parent table):
  CreditCard Int(6) Credit Card Code
  CardName nVarChar(30) Credit Card Name
  AcctCode nVarChar(15) G/L Account ->OACT
  Phone nVarChar(50) Telephone
  CompanyId nVarChar(20) Company ID
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  IntTaxCode nVarChar(2) Internal Tax Code [1=Isracard, 2=CAL, 3=Diners, 4=American Express, 6=Leumi Card]
  UserSign2 Int(6) Updating User ->OUSR
  Country nVarChar(3) Country/Region Code ->OCRY
