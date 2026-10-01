<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ATT1 - Bill of Materials - Components - History
Module: Inventory and Production | 28 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ChildNum, LogInstanc, Father
  VISORDER U: VisOrder, LogInstanc, Father
Fields (name type(len) description [values] ->parent table):
  Father nVarChar(50) Parent Item ->OITT
  ChildNum Int(11) Child Element No.
  VisOrder Int(11) Visual Order
  Code nVarChar(50) Child Code
  Quantity Num(19,6) Quantity
  Warehouse nVarChar(8) Warehouse ->OWHS
  Price Num(19,6) Price
  Currency nVarChar(3) Currency
  PriceList Int(6) Price List default=0 ->OPLN
  OrigPrice Num(19,6) Original Price
  OrigCurr nVarChar(3) Original Currency
  IssueMthd VarChar(1) Issue Method [B=Backflush, M=Manual]
  Uom nVarChar(100) Inventory UOM
  Comment nVarChar(254) Comment
  LogInstanc Int(11) Log Instance
  Object nVarChar(20) Object default=66
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  PrncpInput VarChar(1) Principal Input default=N [Y=Yes, N=No]
  Project nVarChar(20) Project Code ->OPRJ
  Type Int(11) Component Type default=4 [4=Item, 290=Resource, -18=Text]
  WipActCode nVarChar(15) WIP Account Code ->OACT
  AddQuantit Num(19,6) Additional Quantity
  LineText Text(16) Row Text
  StageId Int(11) Stage ID
