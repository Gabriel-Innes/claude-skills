<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CDPM - Dynamic Permission
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PermId
  OBJECT: ObjectType, Name
Fields (name type(len) description [values] ->parent table):
  PermId Int(11) Permission ID
  Name nVarChar(100) Name
  ObjectType Int(11) Object Type
  ObjectKey nVarChar(200) Object ID
  Father Int(11) Parent
  PermOption Int(6) Permission Option default=0 [0=Full/Read/None, 1=Full/None, 2=Full/None/Saved Queries]
  System VarChar(1) System Flag default=N [Y=Yes, N=No]
  Hidden VarChar(1) Hidden default=N [Y=Yes, N=No]
  SortOrder Int(11) Sort Order
