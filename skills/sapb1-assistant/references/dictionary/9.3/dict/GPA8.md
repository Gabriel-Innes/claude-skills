<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GPA8 - Product Cost Adjustment - MRV Document Lines
Module: Marketing Documents | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  ProdCode nVarChar(20) Product Code
  ProdDescr nVarChar(100) Product Description
  DistNumber nVarChar(36) Batch Number
  SnBAbs Int(11) SnB Abs. Entry
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  IncrAcct nVarChar(15) G/L Increase Account
  DecrAcct nVarChar(15) G/L Decrease Account
  DebCredAmt Num(19,6) Debit/Credit Amount
