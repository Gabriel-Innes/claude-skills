<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OPR2 - Opportunity - Partners
Module: Sales Opportunities | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OpportId, Line
Fields (name type(len) description [values] ->parent table):
  OpportId Int(11) Sequence No.
  Line Int(6) Row No.
  ParterId Int(11) Partners ->OPRT
  Memo nVarChar(50) Details
  OrlCode Int(11) Relationship Code ->OORL
  RelatCard nVarChar(15) Related BP ->OCRD
  EncryptIV nVarChar(100) Encrypt IV
