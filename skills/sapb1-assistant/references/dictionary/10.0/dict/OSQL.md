<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSQL - SQL query
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SqlCode
Fields (name type(len) description [values] ->parent table):
  SqlCode nVarChar(254) SQL query code
  SqlName nVarChar(254) SQL query name
  SqlText Text(16) SQL text
  ParamList nVarChar(254) List of bound parameter names
  ParamDetai nVarChar(254) Parameter details
  InternalS Text(16) Internal SQL text
  LogInstanc Int(11) Log instance default=0
  ObjType nVarChar(20) Object Type default=2
  CreateDate Date(8) Created On
  UpdateDate Date(8) Updated On
  DataVers Int(11) Data version default=1
