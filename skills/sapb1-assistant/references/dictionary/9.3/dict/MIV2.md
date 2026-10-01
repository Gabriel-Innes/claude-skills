<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MIV2 - A/P Monthly Invoice - Item
Module: Marketing Documents | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry, DocType, Entry
Fields (name type(len) description [values] ->parent table):
  MinvNum Int(11) Monthly Invoice Number
  DocNum Int(11) Document Number
  DocType nVarChar(20) Document Type [18=A/P Invoice, 19=A/P Credit Memo]
  DocDate Date(8) Document Date
  LineNum Int(11) Line number
  ItemCode nVarChar(50) Item No.
  ItemName nVarChar(100) Item Name
  ItemPrice Num(19,6) Item Price
  ItemCurr nVarChar(3) Item Currency
  ItemRate Num(19,6) Currency Exchange Rate
  ItemQuan Num(19,6) Item Quantity
  ItemType VarChar(1) Item Type default=I [I=Item, E=Expense, R=Rounding, T=Tax Amount, S=Service, D=Down Payment Paid, W=WTax Amount]
  ItemTotal Num(19,6) Net Total
  TaxAmount Num(19,6) Tax Amount of Line Level
  LineTotal Num(19,6) Gross Total
  Entry Int(11) Monthly Invoice Entry ->OMIV
  AbsEntry Int(11) Document Entry
