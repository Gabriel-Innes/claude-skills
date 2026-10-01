<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GFL2 - Grid Filter Name
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FilterID, UserCode, GridID, FormID
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  GridID nVarChar(11) Grid ID
  UserCode Int(6) User Code
  FilterID Int(11) Filter ID default=-1
  Name nVarChar(100) Name
