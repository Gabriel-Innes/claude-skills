<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BGT3 - Budget - Cost Accounting Rows
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BudgId, OcrCode, DimCode, Line_ID
Fields (name type(len) description [values] ->parent table):
  BudgId Int(11) Budget Key ->OBGT
  OcrCode nVarChar(8) Factor Code ->OOCR
  DimCode Int(6) In Which Dimension ->ODIM
  Instance Int(11) Instance default=1 ->OBGS
  Line_ID Int(11) Row Number
  DebLTotal Num(19,6) Monthly Budget - Deb.
  CredLTotal Num(19,6) Monthly Budget - Cr.
  DebSTotal Num(19,6) Monthly Budget - SC Deb.
  CredSTotal Num(19,6) Monthly Budget - SC Cr.
  UserSign Int(6) User Signature ->OUSR
