<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIT1 - Item - Prices - History
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, PriceList, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Number ->OITM
  PriceList Int(6) Price List No. ->OPLN
  Price Num(19,6) Price List
  Currency nVarChar(3) Price List Currency
  Ovrwritten VarChar(1) Manual Price Update default=N [Y=Yes, N=No]
  Factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object ->ADP1
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  Ovrwrite1 VarChar(1) Manual Price Entry (1) default=N [Y=Yes, N=No]
  Ovrwrite2 VarChar(1) Manual Price Entry (2) default=N [Y=Yes, N=No]
  BasePLNum Int(6) Base Price List No. ->OPLN
  UomEntry Int(11) UoM Entry
  PriceType VarChar(1) Price Type default=M [I=Inventory UoM Price, P=Pricing Unit Price, M=Both I and P, O=Other UoM Price]
