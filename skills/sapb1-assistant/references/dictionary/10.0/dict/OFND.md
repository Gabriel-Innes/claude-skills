<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFND - Folio Numbering Documents
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  OBJECT U: ObjectCode, DocSubtype
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(20) Document
  DocSubtype nVarChar(2) Subdocument default=-- [--=, DM=A/P Debit Memo, DN=A/R Debit Memo, IB=A/R Bill]
