<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RSLG - Resource Merge Log
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RSType, RSName, TargetDB, SourceDB
Fields (name type(len) description [values] ->parent table):
  SourceDB Int(11) Source DB
  TargetDB Int(11) Target DB
  RSName nVarChar(64) Resource Name
  RSType Int(11) Resource Type
  RSStatus VarChar(1) Resourc Status default=N [D=Difference, C=Conflict, M=Merged, N=No Differences]
