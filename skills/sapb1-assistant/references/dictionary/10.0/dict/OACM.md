<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OACM - Accumulation
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  ACCUM: CardCode, WTCode, PeriodCat
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  WTCode nVarChar(4) WTax Code ->OWHT
  PeriodCat nVarChar(20) Period Category
  AcmAmt Num(19,6) Accumulation Amount
  ExcdTransc VarChar(1) Exceed Transaction Threshold default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
