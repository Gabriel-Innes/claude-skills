<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# FAC2 - Fixed Asset Parameter Change - Period Control Change
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
  PERCONTROL U: VisOrder, PeriodCat, DprArea, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFAC
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  PeriodCat nVarChar(10) Period Category
  VisOrder Int(11) Visual Order
  OldDprSt VarChar(1) Old Depreciation Status default=Y [Y=Yes, N=No]
  NewDprSt VarChar(1) New Depreciation Status default=Y [Y=Yes, N=No]
  OldFactor Num(19,6) Old Factor
  NewFactor Num(19,6) New Factor
