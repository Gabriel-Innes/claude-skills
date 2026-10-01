<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MIN2 - Item Imformation of MI
Module: Marketing Documents | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Entry, DocType, AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  MinvNum Int(11) Monthly Invoice Number
  DocNum Int(11) Document Number
  DocType nVarChar(20) Document Type [13=A/R Invoice, 14=A/R Credit Memo]
  DocDate Date(8) Document Date
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item No.
  ItemName nVarChar(200) Item Name
  ItemPrice Num(19,6) Item Price
  ItemCurr nVarChar(3) Item Currency
  itemRate Num(19,6) Currency Exchange Rate
  ItemQuan Num(19,6) Item Quantity
  ItemType VarChar(1) Item Type default=I [I=, E=, D=, R=, T=, S=, P=, W=]
  ItemTotal Num(19,6) Item Total
  TaxAmount Num(19,6) Tax Amount
  LineTotal Num(19,6) Row Total
  Entry Int(11) Monthly Invoice Entry ->OMIN
  AbsEntry Int(11) Document Entry
