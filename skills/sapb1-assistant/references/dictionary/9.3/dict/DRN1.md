<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DRN1 - Depreciation Run - Posting
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AssetClass, DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRN
  AcctDtn nVarChar(15) Account Determination ->OADT
  TransId Int(11) Transaction Number ->OJDT
  OrdDprAct nVarChar(15) Ordinary Depreciation Account ->OACT
  SpDprAct nVarChar(15) Special Depreciation Account ->OACT
  SpBalAct nVarChar(15) Special Balance Account ->OACT
  OrdBalAct nVarChar(15) Ordinary Balance Account ->OACT
  OrdDprAmt Num(19,6) Ordinary Depreciation Amount
  SpDprAmt Num(19,6) Special Depreciation Amount
  RevResAct nVarChar(15) Revaluation Reserve Account ->OACT
  RevResClr nVarChar(15) Revaluation Reserve Clearing ->OACT
  RevReserve Num(19,6) Revaluation Reserve Amount
  AssetClass nVarChar(20) Asset Class ->OACS
  CancelId Int(11) Cancelation Transaction No.
