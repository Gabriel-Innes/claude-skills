<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFAR - Fixed Asset Revaluation
Module: Finance | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: PIndicator, DocNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  AssetDate Date(8) Asset Value Date
  Ref nVarChar(32) Reference
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  DprArea nVarChar(15) Depreciation Area ->ODPA
  TransId Int(11) Transaction Number ->OJDT
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocDate Date(8) Document Date
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  RevalPerc Num(19,6) Revaluation Percentage %
