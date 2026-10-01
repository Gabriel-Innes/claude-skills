<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFND - Folio Numbering Documents
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  OBJECT U: DocSubtype, ObjectCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(20) Document
  DocSubtype nVarChar(2) Subdocument default=-- [--=, DM=A/P Debit Memo, DN=A/R Debit Memo, IB=A/R Bill]
