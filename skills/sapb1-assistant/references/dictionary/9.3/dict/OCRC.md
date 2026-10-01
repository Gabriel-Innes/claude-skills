<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCRC - Credit Cards
Module: Administration | 13 columns | ObjType: 36
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CreditCard
  CARD_NAME U: CardName
Fields (name type(len) description [values] ->parent table):
  CreditCard Int(6) Credit Card Code
  CardName nVarChar(30) Credit Card Name
  AcctCode nVarChar(15) G/L Account ->OACT
  Phone nVarChar(20) Telephone
  CompanyId nVarChar(20) Company ID
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  IntTaxCode nVarChar(2) Internal Tax Code [1=Isracard, 2=CAL, 3=Diners, 4=American Express, 6=Leumi Card]
  UserSign2 Int(6) Updating User ->OUSR
  Country nVarChar(3) Country Code ->OCRY
