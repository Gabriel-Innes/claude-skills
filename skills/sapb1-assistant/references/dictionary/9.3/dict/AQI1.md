<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AQI1 - Inventory Opening Balance - Rows
Module: Inventory and Production | 39 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, DocLineNum, DocEntry
  ITEM_CODE: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID
  DocLineNum Int(11) Row Number in Document
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  InvntryUom nVarChar(100) Inventory UoM
  OnHandBef Num(19,6) Quantity Stored in Warehouse
  Price Num(19,6) Price
  Quantity Num(19,6) Quantity - Delta
  Currency nVarChar(3) Price Currency
  Rate Num(19,6) Currency Price
  IOffIncAcc nVarChar(15) Inventory Offset Increase Acct ->OACT
  DOffDecAcc nVarChar(15) Inventory Offset Decrease Acct ->OACT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  ObjType nVarChar(20) Object Type default=310000001
  Project nVarChar(20) Project Code ->OPRJ
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM [Y=Yes, N=No]
  InvUoMQty Num(19,6) Inventory UoM Qty
  BinEntry Int(11) Bin Location Entry ->OBIN
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  Remark nVarChar(254) Remarks
  Location Int(11) Location
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  LogInstanc Int(11) Log Instance - History
  BinNegQty VarChar(1) Allow Bin Negative Quantity default=N [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  ActPrice Num(19,6) Actual Price
  PostValueL Num(19,6) Posted Value LC
  PostValueS Num(19,6) Posted Value SC
