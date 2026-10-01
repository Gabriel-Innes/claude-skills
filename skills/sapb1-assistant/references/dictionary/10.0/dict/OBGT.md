<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBGT - Budget
Module: Finance | 25 columns | ObjType: 77
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  ACCNT_CODE U: AcctCode, FinancYear, Instance
  INTER_KEY: FatherCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  AcctCode nVarChar(15) Account Code
  BgdCode Int(11) Division Code ->OBGD
  FatherCode nVarChar(15) Parent Account Key
  FthrPrcnt Num(19,6) Parent Acct %
  DebLTotal Num(19,6) Total Annual Budget - Debit (LC)
  CredLTotal Num(19,6) Total Annual Budget - Credit (LC)
  DebSTotal Num(19,6) Total Annual Budget - Debit (SC)
  CredSTotal Num(19,6) Total Annual Budget - Credit (SC)
  DebRLTotal Num(19,6) Budget Balance - Debit (LC)
  CrdRLTotal Num(19,6) Budget Balance - Credit (LC)
  DebRSTotal Num(19,6) Budget Balance - Debit (SC)
  CrdRSTotal Num(19,6) Budget Balance - Credit (SC)
  FtrIDRLSum Num(19,6) Future Annual Revenues - Debit (LC)
  FtrIDRSSum Num(19,6) Future Annual Revenues - Credit (SC)
  FtrICRLSum Num(19,6) Future Revenues - Debit (LC)
  FtrICRSSum Num(19,6) Future Revenues - Debit (SC)
  FtrODRLSum Num(19,6) Future Annual Expenses - Credit (LC)
  FtrOCRLSum Num(19,6) Future Annual Expenses - Debit (LC)
  FtrODRSSum Num(19,6) Future Annual Expenses - Credit (SC)
  FtrOCRSSum Num(19,6) Future Annual Expenses - Debit (SC)
  FinancYear Date(8) Start of Fiscal Year
  Instance Int(11) Instance default=1 ->OBGS
  UserSign Int(6) User Signature ->OUSR
  SCNCounter Int(6) SCN Counter
