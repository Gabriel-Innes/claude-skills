<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OASC - Account Segmentation Categories
Module: Finance | 5 columns | ObjType: 143
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code, SegmentId
Fields (name type(len) description [values] ->parent table):
  SegmentId Int(6) Segment ID ->OASG
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  ShortName nVarChar(10) Short Name
  UserSign Int(6) User Signature ->OUSR
