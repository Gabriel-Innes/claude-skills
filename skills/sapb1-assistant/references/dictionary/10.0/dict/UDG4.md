<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UDG4 - User Defaults - Default POI for Folio Numbering Documents
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, FNDAbs
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) POI Code
  FNDAbs Int(11) Folio Numbering Document Abs Entry ->OFND
  ObjectCode nVarChar(20) Document
  DocSubtype nVarChar(2) Subdocument default=-- [--=, DM=A/P Debit Memo, DN=A/R Debit Memo, IB=A/R Bill]
  DflPTICode nVarChar(5) Default POI Code ->OPTI
  DflPtiFCE nVarChar(5) Default POI Code for FCE
