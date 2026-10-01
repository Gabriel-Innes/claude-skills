<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIDC - Indicator
Module: Finance | 3 columns | ObjType: 138
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Indicator Code
  Name nVarChar(50) Indicator Name
  UserSign Int(6) User Signature ->OUSR
