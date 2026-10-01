<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPRA - Payroll G/L accounts Setup
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CATE_CODE U: CateCode, CateType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CateType VarChar(1) Category Type [P=Perception, D=Deduction, N=Payroll Payable, R=Rounding, O=Other Payments]
  CateCode nVarChar(8) Category Code
  Category nVarChar(254) Category of Payroll
  Account nVarChar(15) G/L Account ->OACT
