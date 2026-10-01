<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OIRD - Report Definition
Module: Reports | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ReportId
Fields (name type(len) description [values] ->parent table):
  ReportId nVarChar(254) Report Id
  Type Int(11) Type default=1
  CategoryId Int(11) Category Id
  Revision nVarChar(10) Revision
  Title nVarChar(254) Title
  Definition Text(16) Report Definition
  System VarChar(1) System
  CreateBy nVarChar(25) Created By
  CreateDate Date(8) Creation Timestamp
  ModifyBy nVarChar(25) Modified By
  ModifyDate Date(8) Modification Timestamp
