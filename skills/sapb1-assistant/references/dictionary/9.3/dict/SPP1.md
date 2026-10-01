<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SPP1 - Special Prices - Data Areas
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LINENUM, ItemCode, CardCode
  CARD: CardCode
  ITEM: ItemCode
  CURRENCY: Currency
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OSPP
  CardCode nVarChar(15) BP Code ->OSPP
  LINENUM Int(6) Row Number
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount %
  ListNum Int(6) Price List No. default=0 ->OPLN
  FromDate Date(8) Date From
  ToDate Date(8) Date To
  AutoUpdt VarChar(1) Auto Update default=Y [Y=Yes, N=No]
  Expand VarChar(1) Item Details default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
