<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GPA5 - Product Cost Adjustment - Recalculation of Product Cost
Module: Marketing Documents | 31 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  LineId Int(11) Row No.
  Selected VarChar(1) Choose default=Y [Y=Yes, N=No]
  LnType VarChar(1) Choose default=O [P=Product Serial/Batch Line, O=Production Order Line]
  ProdCode nVarChar(50) Product Code
  ProdDescr nVarChar(200) Product Description
  PODocAbs Int(11) PO Document Abs. Entry
  PODocNum Int(11) PO Document Number
  DocType VarChar(1) Choose default=I [I=Issue for Production, R=Receipt from Production]
  DocAbs Int(11) Document Abs. Entry
  DocNum Int(11) Document Number
  DocLineNum Int(11) Document Line Number
  PostDate Date(8) Posting Date
  ItemCode nVarChar(50) Item No.
  ItemDescr nVarChar(200) Item Description
  DistNumber nVarChar(36) Batch Number
  SnBAbs Int(11) SnB Abs. Entry
  ManagedBy Int(11) Managed By default=-1 [10000044=Batch Numbers, 10000045=Serial Numbers, -1=]
  LnQty Num(19,6) Line Quantity
  SnBQty Num(19,6) Serial/Batch Quantity
  LnCost Num(19,6) Line Cost
  DebCred VarChar(1) Debited or Credited default=D [D=Debited, C=Credited]
  LnTotal Num(19,6) Line Total
  SnBTotal Num(19,6) SnB Total
  SBAccTotal Num(19,6) Serial/Batch Accumulated Total
  SBAccQty Num(19,6) Serial/Batch Accumulated Quantity
  ACAccTotal Num(19,6) Actual Cost Accumulated Total
  ACAccQty Num(19,6) Actual Cost Accumulated Quantity
  Applied Num(19,6) Applied Adjustment
  Variance Num(19,6) Variance to Apply
  MRVAdjust Num(19,6) MRV Adjustment
