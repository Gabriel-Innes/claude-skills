<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWVT - List View Variants
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
  GROUP: UserId, ViewType, ViewId, ObjName
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  Order Int(11) Order
  UserId Int(11) User Id
  ViewType nVarChar(50) View Type
  SubVType nVarChar(50) Sub View Type
  ViewId nVarChar(50) View Id default=-1
  ObjName nVarChar(50) Object Name
  FltBarLout Text(16) FilterBarLayout
  SysFilter Text(16) System Filter
  UserFilter Text(16) User Filter
  CdtFilter Text(16) Condition Filter
  IsPublic VarChar(1) Is Public default=N [Y=Yes, N=No]
  IsSys VarChar(1) Is System default=N [Y=Yes, N=No]
  Name nVarChar(100) Variant Name
  Version Int(11) Version
  OvpCus Text(16) Overview Customization
  ChartCus Text(16) Chart Customization
