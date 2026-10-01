<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# INC1 - Inventory Counting - Rows
Module: Inventory and Production | 41 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number ->OINC
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  ItemDesc nVarChar(100) Item Description
  Freeze VarChar(1) Item Freeze Status default=N [Y=Yes, N=No]
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  InWhsQty Num(19,6) In-Whse Qty on Count Date
  Counted VarChar(1) Counted default=N [Y=Yes, N=No]
  CountQty Num(19,6) Counted Quantity
  CountQtyT1 Num(19,6) Counter 1 - Counted Quantity
  CountQtyT2 Num(19,6) -
  Remark nVarChar(254) Remarks
  BarCode nVarChar(254) Bar Code
  InvUoM VarChar(1) Inventory UoM default=Y [Y=Yes, N=No]
  Difference Num(19,6) Difference
  DiffPercen Num(19,6) Difference %
  CountDate Date(8) Count Date
  CountTime Int(11) Count Time
  TargetRef nVarChar(16) Target Document Reference
  TargetType Int(11) Target Document Type default=-1 [-1=, 0=, 10000071=Inventory Posting]
  TargetEntr Int(11) Target Document Internal ID
  TargetLine Int(11) Target Document Row
  ProjCode nVarChar(20) Project Code ->OPRJ
  OcrCode nVarChar(8) Distribution Rule Code ->OOCR
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  BinEntry Int(11) Bin Location Entry ->OBIN
  VisOrder Int(11) Visual Order
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  FirmCode Int(6) Manufacturer ->OMRC
  SuppCatNum nVarChar(50) Mfr Catalog No.
  PrefVendor nVarChar(15) Preferred Vendor ->OCRD
  LogIns Int(11) Log Instance - History
  UgpEntry Int(11) UoM Group Entry ->OUGP
  IUomEntry nVarChar(20) Inventory UoM Entry ->OUOM
  CountDiff Num(19,6) Counters' Diff.
  CountDiffP Num(19,6) Counters' Diff. (%)
  UomCode nVarChar(20) UoM Code for DI ->OUOM
  UomQty Num(19,6) UoM Counted Qty for DI
