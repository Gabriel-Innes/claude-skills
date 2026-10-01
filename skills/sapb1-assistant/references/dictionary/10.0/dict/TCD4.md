<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TCD4 - Withholding Tax Code Determination
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Tcd2Id Int(11) Determination Key Field ID
  WTCode nVarChar(8) WTax Code
  Type VarChar(1) WTax Code Type default=L [R=AR Default WT Code, P=AP Default WT Code, L=Line Item WT Code]
