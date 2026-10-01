<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MDC1 - Master Data Cleanup - Log
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OMDC
  LineID Int(11) Line ID
  ObjectType nVarChar(20) Object Type
  ObjectKey nVarChar(20) Object Key
  Name nVarChar(100) Name
  LastDate Date(8) Last Transaction Date
  Action VarChar(1) Action [R=Remove, D=Deactivate]
  ObjectCode nVarChar(100) Object Code
  ActFailed VarChar(1) Action Failed default=N [Y=Yes, N=No]
  OrigAction VarChar(1) Original Action [R=Remove, D=Deactivate]
  SubObjType nVarChar(20) Subobject Type
  SubObjKey nVarChar(50) Subobject Key
  SubObjNam1 nVarChar(50) Subobject Name 1
  SubObjNam2 nVarChar(50) Subobject Name 2
  SubObjNam3 nVarChar(50) Subobject Name 3
