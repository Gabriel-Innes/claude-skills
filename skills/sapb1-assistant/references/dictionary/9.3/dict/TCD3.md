<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# TCD3 - Tax Code Determination
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD3_UNI U: EfctFrom, Tcd2Id
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Tcd2Id Int(11) Determination Key Field ID ->TCD2
  EfctFrom Date(8) Effective From
  EfctTo Date(8) Effective To
  TaxCode nVarChar(8) Tax Code
