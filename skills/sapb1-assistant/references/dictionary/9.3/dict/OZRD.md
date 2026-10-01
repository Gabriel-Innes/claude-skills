<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OZRD - POS Daily Summary
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocDate Date(8) Document Date
  POSEquipNo nVarChar(20) POS Equipment No. ->OPOS
  ResetCntr Int(11) Reset Counter
  SummaryCnt Int(11) Summary Counter
  OperCntr Int(11) Operation Counter
  TotalSum Num(19,6) Total Sum
  GrossSale Num(19,6) Gross Sale Sum
  PISSum Num(19,6) PIS Sum
  COFINSSum Num(19,6) COFINS Sum
