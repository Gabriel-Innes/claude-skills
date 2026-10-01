<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ASPP - Special Prices
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ItemCode, CardCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  Price Num(19,6) Special Price
  Currency nVarChar(3) Price Currency
  Discount Num(19,6) Discount in %
  ListNum Int(6) Price List No. default=0 ->OPLN
  AutoUpdt VarChar(1) Auto Update default=Y [Y=Yes, N=No]
  EXPAND VarChar(1) Item Details default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  SrcPrice Int(6) Source Price default=0 [0=Unit Price - Pri. Crcy, 1=Unit Price - Add. Crcy 1, 2=Unit Price - Add. Crcy 2]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Update Date
  Valid VarChar(1) Active default=Y [Y=Yes, N=No]
  ValidFrom Date(8) Active From
  ValidTo Date(8) Active To
