<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCFH - Cash Flow Statement History
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CFHId
Fields (name type(len) description [values] ->parent table):
  CFHId Int(11) Cash Flow History Identity
  CFHName nVarChar(100) Saved Cash Flow Name
  UserSign Int(6) User Signature ->OUSR
  UserName nVarChar(30) User Name
  CreateDate Date(8) Recording Date
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
