<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OALC - Loading Expenses
Module: Administration | 8 columns | ObjType: 48
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AlcCode
  GROUP_NAME: AlcName
Fields (name type(len) description [values] ->parent table):
  AlcCode nVarChar(2) Code
  AlcName nVarChar(30) Name
  OhType VarChar(1) Allocation By default=F [F=Cash Value Before Customs, C=Cash Value After Customs, Q=Quantity, W=Weight, V=Volume, A=Equal, L=Legal Cost]
  AcctCode nVarChar(15) Account Code ->OACT
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LaCAllcAcc nVarChar(15) Landed Costs Alloc. Account
  CostCateg VarChar(1) Cost Category [V=Customs VAT, E=Excise Cost, D=Customs Duty]
