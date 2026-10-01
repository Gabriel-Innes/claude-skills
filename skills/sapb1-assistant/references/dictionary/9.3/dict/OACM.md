<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OACM - Accumulation
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  ACCUM: PeriodCat, WTCode, CardCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  WTCode nVarChar(4) WTax Code ->OWHT
  PeriodCat nVarChar(20) Period Category
  AcmAmt Num(19,6) Accumulation Amount
