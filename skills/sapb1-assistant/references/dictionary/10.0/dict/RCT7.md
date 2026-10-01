<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RCT7 - Incoming Pmt - Tax Amount per Document
Module: Banking | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocNum, LineSeq
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineSeq Int(11) Row Sequence
  InvoiceSeq Int(11) Invoice Sequence Number
  ValueDate Date(8) Due Date
  Inv4Seq Int(11) INV4 Sequence Number
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV
