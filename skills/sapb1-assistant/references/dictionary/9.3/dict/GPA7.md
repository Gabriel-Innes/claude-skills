<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GPA7 - Product Cost Adjustment - Journal Entry Details
Module: Marketing Documents | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OGPA
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  Series Int(11) Series default=0
  Ref2 nVarChar(100) Reference 2
  JERemarks nVarChar(50) Journal Remarks
  MRVRef nVarChar(11) MRV Entry Reference
