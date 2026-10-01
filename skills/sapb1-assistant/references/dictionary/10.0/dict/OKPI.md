<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OKPI - Key Performance Indicator Package
Module: General | 25 columns | ObjType: 1320000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(250) KPI Code
  Name nVarChar(250) KPI Name
  Desc nVarChar(254) Description
  ValueType nVarChar(200) Value Type
  ValueQid Int(11) Value Query Number
  ViewName nVarChar(250) Value View Name
  ViewCtg nVarChar(250) View Catalog
  ViewSyn nVarChar(250) View Synonym
  TrendType nVarChar(250) Trend Type
  TrendQid Int(11) Trend Query Number
  GoalValue Num(19,6) Goal Value
  GoalQid nVarChar(11) Goal Query Number
  GoalDesc nVarChar(250) Goal Description
  CalcFrml nVarChar(250) Calculation Formula
  Visible VarChar(1) Visible For Front End default=Y
  SBetter VarChar(1) Smaller Value is Better default=Y
  Author nVarChar(32) Creator
  Version nVarChar(13) Version
  CreateDate Date(8) Create Date
  CreateTime Int(6) Create Time
  IsSystem VarChar(1) Is System default=N
  MeasUnit nVarChar(50) Measuring Unit default=0
  RevSign VarChar(1) Reverse Sign default=N
  Unit nVarChar(250) Unit
