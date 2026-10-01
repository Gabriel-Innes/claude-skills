<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# RSLG - Resource Merge Log
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SourceDB, TargetDB, RSName, RSType
Fields (name type(len) description [values] ->parent table):
  SourceDB Int(11) Source DB
  TargetDB Int(11) Target DB
  RSName nVarChar(64) Resource Name
  RSType Int(11) Resource Type
  RSStatus VarChar(1) Resourc Status default=N [D=Difference, C=Conflict, M=Merged, N=No Differences]
