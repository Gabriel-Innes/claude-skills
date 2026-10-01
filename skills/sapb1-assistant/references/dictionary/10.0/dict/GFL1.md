<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# GFL1 - Grid Filter Rules
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormID, GridID, UserCode, FilterID, GridColumn
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  GridID nVarChar(11) Grid ID
  UserCode Int(6) User Code
  FilterID Int(11) Filter ID
  GridColumn Int(6) Grid Column
  FilterRule Int(6) FilterRule
  Value nVarChar(254) Value
  ValueTo nVarChar(254) ValueTo
