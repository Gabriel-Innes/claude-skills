<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OFTP - Office 365 Doc Export Task Progress
Module: General | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TASKID
Fields (name type(len) description [values] ->parent table):
  TASKID nVarChar(254) Task ID
  USER_ID nVarChar(254) User ID
  CURR Int(11) Current
  TOTAL Int(11) Total
  ERROR_CODE nVarChar(254) Error Code
  STATE nVarChar(254) State
  STARTTIME Date(8) Start Time
  FILE_NAME nVarChar(254) File Name
  RESULT nVarChar(254) Result
  ONETTOKEN Text(16) One Time Token
  TASKTYPE nVarChar(254) Task Type
