<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OTER - Territories
Module: Business Partners | 5 columns | ObjType: 200
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: territryID
  LOCATION U: lindex, parent
  DESCRIPT: descript
Fields (name type(len) description [values] ->parent table):
  territryID Int(11) Territory ID
  descript nVarChar(200) Description
  parent Int(11) Superordinate Object default=-1 ->OTER
  lindex Int(11) Location Index
  inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
