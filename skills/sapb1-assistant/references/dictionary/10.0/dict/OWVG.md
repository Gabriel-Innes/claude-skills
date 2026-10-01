<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWVG - Variant Groups
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Guid
  GROUP U: UserId, ViewType, ViewId, ObjName
Fields (name type(len) description [values] ->parent table):
  Guid nVarChar(40) Guid
  UserId Int(11) User Id
  ViewType nVarChar(50) View Type
  ViewId nVarChar(50) View Id default=-1
  ObjName nVarChar(50) Object Name
  DftVrnt nVarChar(40) Default Variant
