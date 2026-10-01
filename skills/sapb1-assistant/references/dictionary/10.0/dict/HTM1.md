<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# HTM1 - Team Members
Module: Human Resources | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: teamID, empID
Fields (name type(len) description [values] ->parent table):
  teamID Int(11) Team ID ->OHTM
  line Int(6) Row
  empID Int(11) Employee ID ->OHEM
  role VarChar(1) Role in Team default=M [L=Leader, M=Member]
  LogInstanc Int(11) Log Instance default=0
