<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AHE2 - Education
Module: Human Resources | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: empID, line, LogInstanc
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
  EncryptIV nVarChar(100) Encrypt IV
