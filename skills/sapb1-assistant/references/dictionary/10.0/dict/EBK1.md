<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# EBK1 - E-Books - Rows
Module: General | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) E-Books Abs. Entry ->OEBK
  LineNum Int(11) Line Number
  NetValue Num(19,6) Net Value
  VatCatgory Int(11) VAT Category
  VatAmount Num(19,6) VAT Amount
  WithheldAm Num(19,6) Withheld Amount
  WhPrctCat Int(11) Withheld Percent Category
  ExClassTyp Int(11) Expense Classification Type ->OECP
  ExClassCat Int(11) Expense Classification Cat. ->OECC
  VATClassTy Int(11) VAT Classification Type ->OECP
  VATClassCa Int(11) VAT Classification Category ->OECC
  LogInstanc Int(11) Log Instance default=0
