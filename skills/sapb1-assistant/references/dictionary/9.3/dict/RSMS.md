<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RSMS - Resource Merged Snapshots List
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TargetDB, SourceDB
  BASE_DB U: BaseDB, BaseServer
Fields (name type(len) description [values] ->parent table):
  SourceDB Int(11) Source DB
  TargetDB Int(11) Target DB
  BaseServer nVarChar(254) Base Server Name
  BaseDB nVarChar(254) Base DB Name
