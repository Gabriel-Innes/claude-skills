<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AEXT - Expense Types
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, ExpType
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
