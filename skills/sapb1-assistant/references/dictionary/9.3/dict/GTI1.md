<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GTI1 - GTS Invoice Details
Module: Marketing Documents | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGTI
  LineNum Int(11) Line Number
  DisctLine VarChar(1) Discount Flag default=0 [0=Normal, 1=Discount Line]
  ItemName nVarChar(60) Item Name
  ItemSpec nVarChar(30) Item Specification
  Uom nVarChar(16) Unit of Measurement
  Quantity Num(19,6) Quantity
  NetAmount Num(19,6) Net Amount
  VatPercent Num(19,6) VAT Percent
  VatAmount Num(19,6) VAT Amount
  UnitPrice Num(19,6) Unit Price
  UnitPricTp VarChar(1) Unit Price Type default=0 [0=Net, 1=Gross]
  ItemTaxCat nVarChar(4) Item Tax Category
