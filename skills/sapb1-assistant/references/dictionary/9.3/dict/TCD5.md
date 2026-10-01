<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TCD5 - Tax Code by Usage
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  Tcd3Id Int(11) Valid Period ID
  UsageCode Int(11) Usage
  TaxCode nVarChar(8) Tax Code
  Type VarChar(1) Tax Code Type default=L [R=A/R Default Tax Code, P=A/P Default Tax Code, L=Line Item Tax Code]
  ExpTaxCode nVarChar(8) Freight Tax Code
  PurTaxCode nVarChar(8) Purchase Tax Code
