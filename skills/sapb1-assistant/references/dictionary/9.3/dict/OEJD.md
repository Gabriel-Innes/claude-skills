<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OEJD - Company Details for ERV-JAb
Module: Reports | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CRegNum nVarChar(7) Commercial Register Number
  LFBSheet nVarChar(3) Legal Form on Actl Bal Sht Dte [AG=Public Limited Company (AG), SC=European Cooperative Society (SCE), SE=Company under European Law (SE, Societa Europaea), GEN=Industrial Cooperative Society, GES=Limited Liability Company (GmbH), KG=Limited Partnership, OG=Open Company]
  LFBSheetPr nVarChar(3) Lgl Form on Bal Sht Dte Prv Yr [AG=Public Limited Company (AG), SC=European Cooperative Society (SCE), SE=Company under European Law (SE, Societa Europaea), GEN=Industrial Cooperative Society, GES=Limited Liability Company (GmbH), KG=Limited Partnership, OG=Open Company, CNE=Company does not exist]
  RegNum nVarChar(7) Reg. No. of Partner Company
  CmpanyName Text(16) Company Name
