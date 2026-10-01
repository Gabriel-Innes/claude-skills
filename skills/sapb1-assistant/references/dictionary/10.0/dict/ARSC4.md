<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ARSC4 - Resources - Employees - Log
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ResCode, EmpID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  EmpID nVarChar(11) Employee No. ->OHEM
  LogInstanc Int(11) Log Instance default=0
