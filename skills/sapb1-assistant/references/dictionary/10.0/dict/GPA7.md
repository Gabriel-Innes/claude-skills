<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GPA7 - Product Cost Adjustment - Journal Entry Details
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  Series Int(11) Series default=0
  Ref2 nVarChar(100) Reference 2
  JERemarks nVarChar(254) Journal Remarks
  MRVRef nVarChar(11) MRV Entry Reference
