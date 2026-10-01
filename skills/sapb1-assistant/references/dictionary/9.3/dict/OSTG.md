<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OSTG - State Groups
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Group No.
  GroupName nVarChar(20) Group Name
  UserSign Int(6) User Signature ->OUSR
