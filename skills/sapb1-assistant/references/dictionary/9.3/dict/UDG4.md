<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UDG4 - User Defaults - Default POI for Folio Numbering Documents
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FNDAbs, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) POI Code
  FNDAbs Int(11) Folio Numbering Document Abs Entry ->OFND
  ObjectCode nVarChar(20) Document
  DocSubtype nVarChar(2) Subdocument default=-- [--=, DM=A/P Debit Memo, DN=A/R Debit Memo, IB=A/R Bill]
  DflPTICode nVarChar(5) Default POI Code ->OPTI
