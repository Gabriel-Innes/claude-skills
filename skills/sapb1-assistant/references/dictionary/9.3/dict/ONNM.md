<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ONNM - Document Numbering
Module: Administration | 8 columns | ObjType: 35
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocSubType, ObjectCode
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  AutoKey Int(11) Automatic Key default=0
  DfltSeries Int(11) Default Series default=0
  UpdCounter Int(6) Update Counter default=0
  UserSign Int(6) User Signature ->OUSR
  DocSubType nVarChar(2) Document Sub-Type default=-- [--=, IE=Invoice Exempt, DN=Debit Memo, IB=Bill, EB=Exempt Bill, RI=Reserve Invoice, IR=Invoice & Receipt, DM=A/P Debit Memo, IX=Export Invoice, RP=A/P Reserve Invoice, OV=Outgoing VAT - Withholding Tax, OG=Outgoing Gross Income - Withholding Tax, ON=Outgoing Income - Withholding Tax, OS=Outgoing Social Security - Withholding Tax, OI=Outgoing Industry Specific - Withholding Tax, OD=Outgoing District Specific - Withholding Tax, IC=Incoming WTax Certificate, GA=GST Tax Invoice, GD=GST Debit Memo, RV=Refund Voucher]
  DocAlias nVarChar(20) Alternative Document Name
  PeriodTyp VarChar(1) Seq. Period Type of Supply Code
