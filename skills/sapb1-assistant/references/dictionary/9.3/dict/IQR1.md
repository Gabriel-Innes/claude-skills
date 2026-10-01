<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# IQR1 - Inventory Posting - Rows
Module: Inventory and Production | 50 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocLineNum, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  DocLineNum Int(11) Row Number in Document
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  InvntryUom nVarChar(100) Inventory UoM
  OnHandBef Num(19,6) Quantity Stored in Warehouse
  Price Num(19,6) Price
  Quantity Num(19,6) Variance
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  ObjType nVarChar(20) Object Type default=10000071
  Project nVarChar(20) Project Code ->OPRJ
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  BinEntry Int(11) Bin Location Entry ->OBIN
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  CountDate Date(8) Count Date
  CountTime Int(11) Count Time
  DiffPercnt Num(19,6) Percentage Difference
  BaseRef nVarChar(16) Base Document Reference
  BaseType Int(11) Base Document Type default=1470000065 [-1=, 1470000065=Inventory Counting]
  BaseEntry Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  CountQty Num(19,6) Counted Quantity
  Remark nVarChar(254) Remarks
  LogInstanc Int(11) Log Instance - History
  CpyCount Int(11) Copied Count default=0 [0=, 1=Inventory Taker One, 2=Two Takers - Taker 1, 3=Two Takers - Taker 2, 4=Two Takers - Items with Zero Difference]
  BinNegQty VarChar(1) Allow Bin Negative Quantity default=N [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  UgpEntry Int(11) UoM Group Entry ->OUGP
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
  UomCode nVarChar(20) UoM Code for DI ->OUOM
  ItmsPerUnt Num(19,6) Items per Unit for DI
  UomQty Num(19,6) UoM Counted Qty for DI
  ActPrice Num(19,6) Actual Price
  PostValueL Num(19,6) Posted Value LC
  PostValueS Num(19,6) Posted Value SC
