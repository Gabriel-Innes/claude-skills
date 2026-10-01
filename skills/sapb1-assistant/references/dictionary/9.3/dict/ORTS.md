<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORTS - CPI and FC Rates for Reports
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ReportType, Currency, RateDate
  DATE: RateDate
Fields (name type(len) description [values] ->parent table):
  RateDate Date(8) Exchange Rate Date
  Currency nVarChar(3) Currency Code
  Rate Num(19,6) Currency Rate
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ReportType VarChar(1) Report Rate Type default=S [S=Standard Report Rate, I=Intrastat Exchange Rate]
