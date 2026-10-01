<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ORLD - Reference Links Definition
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  OBJ_FIELD U: ObjectCode, DocSubType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(20) Document
  DocSubType nVarChar(2) Document Subtype default=-- [--=, IE=Invoice Exempt, DN=Debit Memo, IB=Bill, EB=Exempt Bill, DM=A/P Debit Memo, IX=Export Invoice, GA=GST Tax Invoice, GD=GST Debit Memo]
  Status VarChar(1) Status default=O [O=Original, C=Customized]
