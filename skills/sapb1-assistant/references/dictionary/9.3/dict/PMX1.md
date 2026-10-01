<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PMX1 - Payroll Line
Module: General | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPMX
  LineNum Int(11) Row Number
  CateType VarChar(1) Category Type
  CateCode nVarChar(3) Category Code
  Keyword nVarChar(10) Keyword
  Category nVarChar(100) Category
  Debit nVarChar(20) Debit Amount
  Credit nVarChar(20) Credit Amout
  FCDebit nVarChar(20) FC Debit Amount
  FCCredit nVarChar(20) FC Credit Amount
