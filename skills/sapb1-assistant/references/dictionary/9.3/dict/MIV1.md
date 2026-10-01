<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MIV1 - A/P Monthly Invoice - Document
Module: Marketing Documents | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry, DocType, Entry
Fields (name type(len) description [values] ->parent table):
  MinvNum Int(11) Monthly Invoice Number
  AbsEntry Int(11) Internal Key
  DocNum Int(11) Document Number
  DocType nVarChar(20) Document Object ID [18=A/P Invoice, 19=A/P Credit Memo]
  DocDate Date(8) Document Posting Date
  DocDueDate Date(8) Document Due Date
  DocClsDate Date(8) Document Closing Date
  DocAmount Num(19,6) Total Amount
  DocExpense Num(19,6) Document Expense
  DocDiscSum Num(19,6) Document Discount Sum
  DocRound Num(19,6) Document Rounding
  DocTax Num(19,6) Document Tax Amount
  Closed VarChar(1) Is Document closed in MI default=N [Y=Closed, N=Not Closed]
  MINumWnCls Int(11) absEntry when doc closed
  Entry Int(11) Monthly Invoice Entry ->OMIV
