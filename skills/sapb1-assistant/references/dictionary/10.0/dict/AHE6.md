<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AHE6 - Employee Roles
Module: Human Resources | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: empID, line, LogInstanc
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Employee Role Row
  roleID Int(11) Role ID ->OHTY
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV
