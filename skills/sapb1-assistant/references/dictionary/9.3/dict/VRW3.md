<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VRW3 - VAT Reposting Wizard - Rows 3
Module: Finance | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
