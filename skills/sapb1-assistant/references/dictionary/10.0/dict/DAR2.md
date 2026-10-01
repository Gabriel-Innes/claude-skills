<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DAR2 - Data Archive - Transaction Log
Module: Administration | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ArcEntry, Line_ID
Fields (name type(len) description [values] ->parent table):
  ArcEntry Int(11) Data Archive Entry
  Line_ID Int(11) Row Number default=0
  Approve VarChar(1) Approve default=Y [Y=Yes, N=No]
  DocType Int(11) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Abs Entry
  CardCode nVarChar(15) Customer/Vendor Code
  RefDate Date(8) Posting Date
  DueDate Date(8) Due Date
  TaxDate Date(8) Document Date
  Total Num(19,6) Total
  Action VarChar(1) Action default=T [R=Remove, L=Locked, T=Temporary]
  Remarks nVarChar(50) Remarks
  KeySeg1 nVarChar(15) Key Segment 1
  KeySeg2 nVarChar(15) Key Segment 2
  KeySeg3 nVarChar(15) Key Segment 3
  KeySeg4 nVarChar(15) Key Segment 4
  KeySeg5 nVarChar(15) Key Segment 5
  KeySeg6 nVarChar(15) Key Segment 6
  ClusterId Int(11) Cluster ID
