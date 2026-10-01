<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ARSC2 - Resources - Prices - Log
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, PriceList, LogInstanc
  CURRENCY: Currency
  PRICE_LIST: PriceList
  MANUAL: Ovrwritten
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  PriceList Int(11) Price List No. ->OPLN
  Price Num(19,6) List Price
  Currency nVarChar(3) Currency for List Price ->OCRN
  Ovrwritten VarChar(1) Manual Price Entry default=N [Y=Yes, N=No]
  Factor Num(19,6) Factor
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=290 ->ADP1
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  Ovrwrite1 VarChar(1) Manual Price Entry (1) default=N [Y=Yes, N=No]
  Ovrwrite2 VarChar(1) Manual Price Entry (2) default=N [Y=Yes, N=No]
