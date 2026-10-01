<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OEXT - Expense Types
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ExpType
Fields (name type(len) description [values] ->parent table):
  ExpType nVarChar(4) Expense Type
  ExpName nVarChar(30) Expense Name
  ExpAcct nVarChar(15) G/L Account ->OACT
  PaidByComp VarChar(1) Paid By Company default=N [Y=Yes, N=No]
  VatGroup nVarChar(8) VAT Group ->OSTC
  VatGrpEU nVarChar(8) VAT Group ->OVTG
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
