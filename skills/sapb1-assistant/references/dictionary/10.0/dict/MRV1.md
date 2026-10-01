<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MRV1 - Inventory Revaluation Information Array
Module: Inventory and Production | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
  ITEM_WHS: ItemCode, WhsCode
  ITEM: ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OMRV
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  Dscription nVarChar(200) Item/Service Description
  Quantity Num(19,6) Quantity
  Price Num(19,6) Price
  LineTotal Num(19,6) Row Total
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  RIncmAcct nVarChar(15) Inv. Reval. Increment Account
  RDcrmAcct nVarChar(15) Inv. Reval. Decrement Account
  RToStock Num(19,6) Reval. Amount Posted to Stock
  RActPrice Num(19,6) Inv. Reval. Actual Price
  ROnHand Num(19,6) In Stock at Time of Revaluation
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=162
  EvalSystem VarChar(1) Cost Accounting Method [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch] ->OITM
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  UnitMsr nVarChar(100) Unit of Measure
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
