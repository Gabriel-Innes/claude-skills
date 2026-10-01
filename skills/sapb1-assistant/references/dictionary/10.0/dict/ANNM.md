<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ANNM - Document Numbering - History
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, logInstanc
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  AutoKey Int(11) Automatic Key default=0
  DfltSeries Int(11) Default Series default=0
  UpdCounter Int(11) Update Counter default=0
  UserSign Int(6) User Signature ->OUSR
  DocSubType nVarChar(2) Document Sub-Type default=-- [--=, IE=Invoice Exempt, DN=Debit Memo, IB=Bill, EB=Exempt Bill, RI=Reserve Invoice, IR=Invoice & Receipt, DM=A/P Debit Memo, IX=Export Invoice, RP=A/P Reserve Invoice, OV=Outgoing VAT - Withholding Tax, OG=Outgoing Gross Income - Withholding Tax, ON=Outgoing Income - Withholding Tax, OS=Outgoing Social Security - Withholding Tax, OI=Outgoing Industry Specific - Withholding Tax, OD=Outgoing District Specific - Withholding Tax, IC=Incoming WTax Certificate, GA=GST Tax Invoice, GD=GST Debit Memo, RV=Refund Voucher]
  DocAlias nVarChar(20) Alternative Document Name
  PeriodTyp VarChar(1) Seq. Period Type of Supply Code
  logInstanc Int(11) Log Instance - History
