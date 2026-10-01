<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACS1 - Asset Classes - Depreciation Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum
  UNIQUE U: Code, DprAreaID
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code ->OACS
  LineNum Int(11) Line Number
  DprAreaID nVarChar(15) Depreciation Area ID ->ODPA
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  AcctDtn nVarChar(15) Account Determination ->OADT
  DprTypID nVarChar(15) Depreciation Type ID ->ODTP
  UseLife Int(11) Useful Life
  LogInstanc Int(11) Log Instance default=0
  SnapshotId Int(11) Snapshot ID default=0
