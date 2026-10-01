<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DAR4 - Data Archive - Candidate
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ArcEntry, Line_ID
  ABS_TYPE: DocAbs, DocType
Fields (name type(len) description [values] ->parent table):
  ArcEntry Int(11) Data Archive Entry
  Series Int(11) Series
  Line_ID Int(11) Row Number
  DocType nVarChar(20) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Internal ID
  Total Num(19,6) Total
  RefDate Date(8) Posting Date
  Type VarChar(1) Type default=R [R=Recommendation, M=Marked]
  Remarks nVarChar(100) Remarks
