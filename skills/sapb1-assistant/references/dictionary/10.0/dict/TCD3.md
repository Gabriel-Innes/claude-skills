<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TCD3 - Tax Code Determination
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD3_UNI U: Tcd2Id, EfctFrom
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Tcd2Id Int(11) Determination Key Field ID ->TCD2
  EfctFrom Date(8) Effective From
  EfctTo Date(8) Effective To
  TaxCode nVarChar(8) Tax Code
