<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITM9 - Item - UoM Prices
Module: Inventory and Production | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UomEntry, PriceList, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PriceList Int(6) Price List No. ->OPLN
  UomEntry Int(11) UoM Entry ->OUOM
  Factor Num(19,6) Reduced By %
  Price Num(19,6) UoM Price
  Currency nVarChar(3) Currency for UoM Price ->OCRN
  AutoUpdate VarChar(1) Automatic Update default=Y [Y=Yes, N=No]
  AddPrice1 Num(19,6) Additional Price (1)
  Currency1 nVarChar(3) Currency for Add. Price 1 ->OCRN
  AddPrice2 Num(19,6) Additional Price (2)
  Currency2 nVarChar(3) Currency for Add. Price 2 ->OCRN
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  Factor1 Num(19,6) Reduced By %
  Factor2 Num(19,6) Reduced By %
  UpdateDate Date(8) Date of Update
  PriceType VarChar(1) Price Type default=O [I=Inventory UoM Price, P=Pricing Unit Price, M=Both I and P, O=Other UoM Price]
