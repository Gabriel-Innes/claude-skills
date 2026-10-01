<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPRA - Payroll G/L accounts Setup
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CATE_CODE U: CateType, CateCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CateType VarChar(1) Category Type [P=Perception, D=Deduction, N=Payroll Payable, R=Rounding, O=Other Payments]
  CateCode nVarChar(8) Category Code
  Category nVarChar(254) Category of Payroll
  Account nVarChar(15) G/L Account ->OACT
