<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UICU - Customized Template
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TPLId
  NAME_KEY U: TPLName
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID
  TPLName nVarChar(155) Template Name
  TPLDesc nVarChar(155) Template Description
  UserID Int(6) User ID
  Parent Int(6) Parent Template ID
  IsTemplate VarChar(1) Is Template
