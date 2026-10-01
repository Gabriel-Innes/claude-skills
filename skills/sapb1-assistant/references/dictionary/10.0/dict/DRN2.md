<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# DRN2 - Depreciation Run - Posting - Asset
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, AssetClass, ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRN
  AcctDtn nVarChar(15) Account Determination ->OADT
  ItemCode nVarChar(50) Item Code ->OITM
  OrdDprAmt Num(19,6) Ordinary Depreciation Amount
  SpDprAmt Num(19,6) Special Depreciation Amount
  RevReserve Num(19,6) Revaluation Reserve Amount
  AssetClass nVarChar(20) Asset Class ->OACS
