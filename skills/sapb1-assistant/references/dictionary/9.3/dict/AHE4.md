<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AHE4 - Previous Employment
Module: Human Resources | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Previous Employment Row
  fromDate Date(8) Employment from
  toDate Date(8) Employment to
  employer nVarChar(50) Employer
  position nVarChar(50) Position
  remarks Text(16) Previous Employment
  LogInstanc Int(11) Log Instance default=0
