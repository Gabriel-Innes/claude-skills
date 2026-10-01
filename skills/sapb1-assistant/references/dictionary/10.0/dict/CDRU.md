<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CDRU - Drag & Relate User Settings
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserID, ObjectId, PartOf
Fields (name type(len) description [values] ->parent table):
  UserID Int(11) User ID default=-1
  ObjectId nVarChar(4) ObjectId
  PartOf VarChar(1) PartOf default=C [C=Category, R=Report, F=Table]
  Disabled VarChar(1) Disabled default=N [Y=Yes, N=No]
