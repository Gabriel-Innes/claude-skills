<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORLD - Reference Links Definition
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  OBJ_FIELD U: DocSubType, ObjectCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(20) Document
  DocSubType nVarChar(2) Document Subtype default=-- [--=, IE=Invoice Exempt, DN=Debit Memo, IB=Bill, EB=Exempt Bill, DM=A/P Debit Memo, IX=Export Invoice, GA=GST Tax Invoice, GD=GST Debit Memo]
  Status VarChar(1) Status default=O [O=Original, C=Customized]
