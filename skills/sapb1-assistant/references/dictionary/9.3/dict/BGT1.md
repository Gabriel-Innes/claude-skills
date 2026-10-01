<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# BGT1 - Budget - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line_ID, BudgId
Fields (name type(len) description [values] ->parent table):
  BudgId Int(11) Budget Key ->OBGT
  Line_ID Int(11) Row Number default=0
  DebLTotal Num(19,6) Monthly Budget - Deb.
  CredLTotal Num(19,6) Monthly Budget - Cr.
  DebSTotal Num(19,6) Monthly Budget - SC Deb.
  CredSTotal Num(19,6) Monthly Budget - SC Cr.
  DebRLTotal Num(19,6) Monthly Bal. - Deb.
  CrdRLTotal Num(19,6) Monthly Bal. - Cr.
  DebRSTotal Num(19,6) Monthly Bal. - SC Deb.
  CrdRSTotal Num(19,6) Monthly Bal. - SC Cred.
  FtrIDRLSum Num(19,6) Fut. Monthly Incomes SC Cr.
  FtrIDRSSum Num(19,6) Fut. Monthly Incomes SC Deb.
  FtrICRLSum Num(19,6) Fut. Incomes - Cr.
  FtrICRSSum Num(19,6) Fut. Incomes - Sys. Cr.
  FtrODRLSum Num(19,6) Fut. Expen - Local Deb.
  FtrODRSSum Num(19,6) Fut.Expen - SC Deb.
  FtrOCRLSum Num(19,6) Fut.Expen - Local Cr.
  FtrOCRSSum Num(19,6) Fut.Expen - Sys. Cr.
  MonthPrcnt Num(19,6) % of annual budget amount
  LineMemo nVarChar(50) Row Details
  Instance Int(11) Instance default=1 ->OBGS
  AcctCode nVarChar(15) Account Code
  UserSign Int(6) User Signature ->OUSR
