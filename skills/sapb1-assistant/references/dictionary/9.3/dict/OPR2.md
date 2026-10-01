<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPR2 - Opportunity - Partners
Module: Sales Opportunities | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line, OpportId
Fields (name type(len) description [values] ->parent table):
  OpportId Int(11) Sequence No.
  Line Int(6) Row No.
  ParterId Int(11) Partners ->OPRT
  Memo nVarChar(50) Details
  OrlCode Int(11) Relationship Code ->OORL
  RelatCard nVarChar(15) Related BP ->OCRD
