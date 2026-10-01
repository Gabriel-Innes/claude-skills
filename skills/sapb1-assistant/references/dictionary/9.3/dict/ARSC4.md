<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ARSC4 - Resources - Employees - Log
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, EmpID, ResCode
Fields (name type(len) description [values] ->parent table):
  ResCode nVarChar(50) Internal Resource ID ->ORSC
  EmpID nVarChar(11) Employee No. ->OHEM
  LogInstanc Int(11) Log Instance default=0
