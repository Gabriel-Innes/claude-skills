<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCFH - Cash Flow Statement History
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CFHId
Fields (name type(len) description [values] ->parent table):
  CFHId Int(11) Cash Flow History Identity
  CFHName nVarChar(100) Saved Cash Flow Name
  UserSign Int(6) User Signature ->OUSR
  UserName nVarChar(30) User Name
  CreateDate Date(8) Recording Date
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
