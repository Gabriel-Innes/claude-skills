<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UIC6 - Template Group Customization
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupID, TPLId
Fields (name type(len) description [values] ->parent table):
  TPLId Int(6) Template ID ->UICU
  GroupID Int(6) Group ID ->OUGR
  IsTemplate VarChar(1) Is Template
