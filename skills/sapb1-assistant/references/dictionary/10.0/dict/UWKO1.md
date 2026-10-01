<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UWKO1 - Production Instructions - Rows
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OrderNum, LineID
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  OrderNum Int(11) Instruction Key ->OWKO
  LineID Int(11) Row Number default=0
  ItemCode nVarChar(50) Item No. ->OITT
  Descript nVarChar(200) Item Description
  Quantity Num(19,6) Item Quantity
  Price Num(19,6) Item Price
  Currency nVarChar(3) Price Currency ->OCRN
  WhsCode nVarChar(8) Item Warehouse ->OWHS
  FinncPriod Int(11) Posting Period ->OFPR
  ActWorkCod nVarChar(15) Active Account Code ->OACT
  ActWorkSum Num(19,6) Total Work
  ProdUpgNum Int(11) Production Upgrade No. ->OWOR
