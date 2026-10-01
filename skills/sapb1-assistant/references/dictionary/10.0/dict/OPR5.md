<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPR5 - Opportunity - Reasons
Module: Sales Opportunities | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OpportId, Line
Fields (name type(len) description [values] ->parent table):
  OpportId Int(11) Sequence No.
  Line Int(6) Row No.
  ReasondId Int(11) Reason ->OOFR
  EncryptIV nVarChar(100) Encrypt IV
