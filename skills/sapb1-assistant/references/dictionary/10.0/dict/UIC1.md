<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UIC1 - Customized Forms in Templates
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId, FormId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  Width Int(6) Form Width
  Height Int(6) Form Height
  MenuId nVarChar(20) Menu ID
