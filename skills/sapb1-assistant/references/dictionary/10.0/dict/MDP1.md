<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MDP1 - Manual Depreciation - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OMDP
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  AcctCode nVarChar(15) Account Code ->OACT
  Quantity Num(19,6) Quantity
  LineTotal Num(19,6) Line Total
  TotalFrgn Num(19,6) Line Total (FC)
  TotalSys Num(19,6) Line Total (SC)
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  NewItemCod nVarChar(50) New Item Code ->OITM
  Partial VarChar(1) Partial default=N [Y=Yes, N=No]
  APC Num(19,6) APC
  NewAstCls nVarChar(20) New Asset Class ->OACS
  ObjType nVarChar(20) Object Type
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 130=APC Write-Up, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 310=Full Transfer, 320=Partial Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
