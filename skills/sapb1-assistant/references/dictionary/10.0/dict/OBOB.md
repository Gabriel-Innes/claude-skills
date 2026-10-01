<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBOB - Business Object Brief
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId Int(11) Object ID
  TableName nVarChar(30) Table Name
  PrimaryKey nVarChar(30) Primary Key
  TitleField nVarChar(100) Title Field
  DescField nVarChar(100) Description Field
  DeviceType VarChar(1) Device Type default=D [D=Desktop, M=Mobile]
  UsedBy VarChar(1) The record is used by BO list/Quick Access/Both default=A [A=All, B=BO List, R=Recent Updates]
