<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MDC2 - Master Data Cleanup - MD Log
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectType, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OMDC
  ObjectType nVarChar(20) Object Type
  UserAction VarChar(1) User Action [O=Original Recommendation, D=Deactivate]
  DelContent nVarChar(100) Delete Content List
