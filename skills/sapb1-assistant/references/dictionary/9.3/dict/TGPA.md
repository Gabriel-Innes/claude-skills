<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TGPA - Gross Profit Adjustment - Log
Module: Marketing Documents | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) Internal Key
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  LineID Int(11) Line ID
  Selected VarChar(1) Selected default=N
  DocType nVarChar(20) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Abs. Entry
  DocLineNum Int(11) Document Line Number
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers]
  SysNumber Int(11) System Number
