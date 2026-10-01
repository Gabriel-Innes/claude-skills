<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ITM8 - Asset Item Balances
Module: Inventory and Production | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  PeriodCat nVarChar(10) Period Category
  DprArea nVarChar(15) Depreciation Area ->ODPA
  APC Num(19,6) APC
  APCHist Num(19,6) Historical APC
  Quantity Num(19,6) Asset Quantity
  OrDpAcc Num(19,6) Accumulated Ordinary Depr.
  UnDpAcc Num(19,6) Accumulated Unplanned Depr.
  SpDpKey1 nVarChar(2) Special Depreciation 01 ->ODPP
  SpDpAcc1 Num(19,6) Accumulated Special Depr. 01
  SpDpKey2 nVarChar(2) Special Depreciation 02 ->ODPP
  SpDpAcc2 Num(19,6) Accumulated Special Depr. 02
  SpDpKey3 nVarChar(2) Special Depreciation 03 ->ODPP
  SpDpAcc3 Num(19,6) Accumulated Special Depr. 03
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object default=4 ->ADP1
  SalvageVal Num(19,6) Salvage Value
  OrDpAcc1 Num(19,6) Ordinary Depr. Accumulation 01
  WriteUpAcc Num(19,6) Accumulated Write-Up
  IsMaSalVal VarChar(1) Manually Changed Salvage Value default=N [Y=Yes, N=No]
  AppreAcc Num(19,6) Accumulated Appreciation
