<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ORCM - Recommendation Data
Module: MRP | 31 columns | ObjType: 213
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  ObjAbs Int(11) Document Internal Number
  ObjType Int(11) Document Number
  ItemCode nVarChar(50) Item No. ->OITM
  DueDate Date(8) Order Due Date
  OrderType VarChar(1) Order Type default=P [P=Purchase Order, W=Production Order, T=Inventory Transfer Request, Q=Purchase Quotation, R=Purchase Request]
  Quantity Num(19,6) Quantity
  UOM nVarChar(100) Buy or Inventory UoM
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  Warehouse nVarChar(8) Warehouse ->OWHS
  Price Num(19,6) Price After Discount
  Currency nVarChar(3) Price Currency
  Origin VarChar(1) Order Origin default=M [M=MRP]
  Status VarChar(1) Order Status default=O [O=Opened, A=Accepted, P=Processed, D=Deleted]
  UserSign Int(6) User Signature ->OUSR
  DocDate Date(8) Generation Date
  DocTime Int(6) Generation Time
  BPLid Int(11) Business Place ID default=-1
  PriceBefDi Num(19,6) Unit Price
  DiscPrcnt Num(19,6) Discount % Per Row
  ReleasDate Date(8) Release Date
  PriceAftV Num(19,6) Price after VAT
  FromWhse nVarChar(8) From Warehouse
  FstReqDate Date(8) First Request Date
  UomEntry Int(11) UoM Entry
  NumPerMsr Num(19,6) UoM Value
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Row Number
  UseDiscnt VarChar(1) Use BP Special Price default=Y [Y=Yes, N=No]
  PriceMode VarChar(1) Price Mode [N=Net, G=Gross]
  RouDatCalc VarChar(1) Routing Date Calculation [S=On Start Date, D=On End Date, F=Start Date Onwards, B=End Date Backwards]
