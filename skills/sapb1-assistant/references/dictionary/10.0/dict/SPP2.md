<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SPP2 - Special Prices - Quantity Areas
Module: Inventory and Production | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, ItemCode, SPP1LNum, SPP2LNum
  CARD: CardCode
  ITEM: ItemCode
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  SPP1LNum Int(6) Dates Row Number
  SPP2LNum Int(6) Row Number
  Amount Num(19,6) Quantity
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount in %
  UomEntry Int(6) UoM Entry ->OUOM
  LogInstanc Int(11) Log Instance default=0
