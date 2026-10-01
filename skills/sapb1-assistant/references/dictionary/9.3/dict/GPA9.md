<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GPA9 - Applied Gross Profit Adjustments
Module: Marketing Documents | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  DocAbs Int(11) Document Abs. Entry
  DocType nVarChar(20) Document Type
  DocLineNum Int(11) Document Line Number
  SnBAbs Int(11) SnB Abs. Entry
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  Applied Num(19,6) Applied Adjustment
