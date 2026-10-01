<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# FIX1 - Fixed Asset Transaction - Rows
Module: Finance | 34 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDARY: DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFIX
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ID ->ODPA
  PeriodCat nVarChar(10) Period Category ID
  PostPeriod Int(11) Posting Subperiod
  RefDate Date(8) Posting Date
  APC Num(19,6) APC
  OrdDpr Num(19,6) Ordinary Depreciation
  UnpDpr Num(19,6) Unplanned Depreciation
  SpDprKey1 nVarChar(2) Special Depreciation Key 01 ->ODPP
  SpDpr1 Num(19,6) Special Depreciation 01
  Qty Num(19,6) Quantity
  DprType nVarChar(15) New Depreciation Type ->ODTP
  DprDate Date(8) New Depreciation Start Date
  RemLife Int(11) New Remaining Life
  SalvageVal Num(19,6) New Salvage Value
  RecvAsst nVarChar(50) Receiving Item Code ->OITM
  RetirDate Date(8) Retirement Date
  SpDprKey2 nVarChar(2) Special Depreciation Key 02 ->ODPP
  SpDpr2 Num(19,6) Special Depreciation 02
  SpDprKey3 nVarChar(2) Special Depreciation Key 03 ->ODPP
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 260=Low Value Asset Full Retirement, 270=Low Value Asset Full Scrapping, 310=Full Transfer, 320=Partial Transfer, 330=Asset Class Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 550=Revaluation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value, 560=Change of Period Control, 570=Change of Total Units]
  UsefulLife Int(11) New Useful Life
  Appr Num(19,6) Appreciation
  WriteUp Num(19,6) Write-Up
  DeltaDays Int(11) Delta Remaining Life in Days
  NewAstCls nVarChar(20) New Asset Class ->OACS
  HistOrdDpr Num(19,6) Historical Ordinary Depr.
  SpDpr3 Num(19,6) Special Depreciation 03
  TransAmnt Num(19,6) Transaction Amount
  Remark nVarChar(254) Remarks
  ReTranType nVarChar(4) Receiving Transaction Type default=0 [0=Unknown, 110=Acquisition, 115=Subacquisition]
  NewTtlUnit Int(11) New Total Unit
