<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCQG - Card Properties
Module: Business Partners | 4 columns | ObjType: 44
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Property Group Code
  GroupName nVarChar(50) Property Name
  UserSign Int(6) User Signature ->OUSR
  Filler nVarChar(10) Filler
