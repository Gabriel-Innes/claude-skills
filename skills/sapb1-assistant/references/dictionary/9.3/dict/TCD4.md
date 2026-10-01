<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TCD4 - Withholding Tax Code Determination
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Tcd2Id Int(11) Determination Key Field ID
  WTCode nVarChar(8) WTax Code
  Type VarChar(1) WTax Code Type default=L [R=AR Default WT Code, P=AP Default WT Code, L=Line Item WT Code]
