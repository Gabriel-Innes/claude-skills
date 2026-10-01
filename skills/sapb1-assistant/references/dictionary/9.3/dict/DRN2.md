<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DRN2 - Depreciation Run - Posting - Asset
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, AssetClass, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRN
  AcctDtn nVarChar(15) Account Determination ->OADT
  ItemCode nVarChar(50) Item Code ->OITM
  OrdDprAmt Num(19,6) Ordinary Depreciation Amount
  SpDprAmt Num(19,6) Special Depreciation Amount
  RevReserve Num(19,6) Revaluation Reserve Amount
  AssetClass nVarChar(20) Asset Class ->OACS
