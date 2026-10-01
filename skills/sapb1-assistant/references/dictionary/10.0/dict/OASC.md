<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OASC - Account Segmentation Categories
Module: Finance | 5 columns | ObjType: 143
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SegmentId, Code
Fields (name type(len) description [values] ->parent table):
  SegmentId Int(6) Segment ID ->OASG
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  ShortName nVarChar(10) Short Name
  UserSign Int(6) User Signature ->OUSR
