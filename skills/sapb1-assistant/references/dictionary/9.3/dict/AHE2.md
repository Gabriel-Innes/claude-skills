<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AHE2 - Education
Module: Human Resources | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Education: Information Row
  fromDate Date(8) Education from
  toDate Date(8) Education to
  type Int(11) Education Type ->OHED
  institute nVarChar(100) Institute
  major nVarChar(50) Major
  diploma nVarChar(50) Diploma
  LogInstanc Int(11) Log Instance default=0
