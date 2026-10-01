<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCQG - Card Properties
Module: Business Partners | 4 columns | ObjType: 44
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Property Group Code
  GroupName nVarChar(50) Property Name
  UserSign Int(6) User Signature ->OUSR
  Filler nVarChar(10) Filler
