<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# UIC4 - Forms in Assigned Templates
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserID, FormId, TPLId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  FormId nVarChar(20) Form ID
  UserID Int(6) User ID ->OUSR
