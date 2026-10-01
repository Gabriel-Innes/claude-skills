<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ONFN - Nota Fiscal Numbering
Module: Administration | 6 columns | ObjType: 263
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  AutoKey Int(11) Automatic Key default=0
  DfltSeq Int(6) Default Sequence default=0
  UpdCounter Int(6) Update Counter default=0
  UserSign Int(6) User Signature ->OUSR
  DocSubType nVarChar(2) Document Sub-Type default=-- [--=, GA=GST Tax Invoice, GD=GST Debit Memo, RV=Refund Voucher]
