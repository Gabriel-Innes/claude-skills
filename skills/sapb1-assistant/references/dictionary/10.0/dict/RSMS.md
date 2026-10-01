<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RSMS - Resource Merged Snapshots List
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SourceDB, TargetDB
  BASE_DB U: BaseServer, BaseDB
Fields (name type(len) description [values] ->parent table):
  SourceDB Int(11) Source DB
  TargetDB Int(11) Target DB
  BaseServer nVarChar(254) Base Server Name
  BaseDB nVarChar(254) Base DB Name
