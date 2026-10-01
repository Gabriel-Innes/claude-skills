<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# MDC2 - Master Data Cleanup - MD Log
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ObjectType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OMDC
  ObjectType nVarChar(20) Object Type
  UserAction VarChar(1) User Action [O=Original Recommendation, D=Deactivate]
  DelContent nVarChar(100) Delete Content List
