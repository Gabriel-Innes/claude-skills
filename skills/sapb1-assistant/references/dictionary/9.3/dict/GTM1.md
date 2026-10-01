<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GTM1 - GTS Mapping Object Details
Module: Marketing Documents | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OGTM
  LineNum Int(11) Line Number
  ItemCode nVarChar(50) Item Code ->OITM
  ItemName nVarChar(100) Item Name
  ItemUoM nVarChar(100) Item UoM
  ItemSpec nVarChar(30) Item Spec.
  ItemTaxCat nVarChar(4) Item Tax Category
  Quantity Num(19,6) Quantity
  Amount Num(19,6) Amount
  VatPercent Num(19,6) VAT Percent
  DiscRate Num(19,6) Discount Rate
  DiscAmount Num(19,6) Discount Amount
  VatAmount Num(19,6) VAT Amount
  DiscVatAmt Num(19,6) Discount VAT Amount
  UnitPrice Num(19,6) Unit Price
  UPirceType VarChar(1) Unit Price Type default=0 [0=Net, 1=Gross]
