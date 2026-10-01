<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPMX - Payroll
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  UID U: Uid
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Total Num(19,6) Total
  Currency nVarChar(3) Currency ->OCRN
  Rate Num(19,6) Exchange Rate
  Uid nVarChar(100) UUID of payroll
  RFC nVarChar(20) RFC
  CreateDate Date(8) Creation Date
  FileDate Date(8) File Date
  FileName nVarChar(254) Imported File Name
  JVBatchNum Int(11) Journal Voucher Batch Number ->OBTF
  JVTransId Int(11) Journal Voucher Trans Number ->OBTF
  JETransId Int(11) Journal Entry Trans Number ->OJDT
  Type VarChar(1) Type default=P [P=Payroll, E=Expenses]
