<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OACM - Accumulation
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
  ACCUM: PeriodCat, WTCode, CardCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  WTCode nVarChar(4) WTax Code ->OWHT
  PeriodCat nVarChar(20) Period Category
  AcmAmt Num(19,6) Accumulation Amount
