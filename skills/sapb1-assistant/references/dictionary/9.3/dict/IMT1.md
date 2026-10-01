<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IMT1 - Acct data in selected template
Module: Inventory and Production | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AccountId, TemplateId
Fields (name type(len) description [values] ->parent table):
  TemplateId Int(6) Template ID default=-1 ->OIMT
  AccountId Int(6) Account ID default=-1
  DebitCredi VarChar(1) Debit or Credit default=U [U=Unknown, D=DEBIT, C=CREDIT, B=Both, T=Total]
  OrderCalc Int(6) Order Calc default=-1
