<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# HEM3 - Employee Reviews
Module: Human Resources | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: empID, line
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Employee Review Row
  date Date(8) Employee Review Date
  reviewDesc nVarChar(100) Review Description
  manager Int(11) Manager ->OHEM
  grade nVarChar(50) Grade
  remarks Text(16) Reviews
  LogInstanc Int(11) Log Instance default=0
  EncryptIV nVarChar(100) Encrypt IV
