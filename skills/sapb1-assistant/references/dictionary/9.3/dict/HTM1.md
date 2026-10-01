<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HTM1 - Team Members
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: empID, teamID
Fields (name type(len) description [values] ->parent table):
  teamID Int(11) Team ID ->OHTM
  line Int(6) Row
  empID Int(11) Employee ID ->OHEM
  role VarChar(1) Role in Team default=M [L=Leader, M=Member]
