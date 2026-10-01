<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPR4 - Opportunity - Interests
Module: Sales Opportunities | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OprId, Line
Fields (name type(len) description [values] ->parent table):
  OprId Int(11) Sequence No.
  Line Int(6) Row No.
  IntId Int(11) Interest ID ->OOIN
  Prmry VarChar(1) Primary Interest default=N [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV
