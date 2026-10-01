<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ARTT - CPI and FC Rates - History
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RateDate, Currency, LogInstanc
  DATE: RateDate, LogInstanc
Fields (name type(len) description [values] ->parent table):
  RateDate Date(8) Exchange Rate Date
  Currency nVarChar(3) Currency Code
  Rate Num(19,6) Currency Rate
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(11) Updating User ->OUSR
