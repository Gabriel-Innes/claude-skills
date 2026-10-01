<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AHTM - Employee Teams - Log
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: teamID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  teamID Int(11) Team ID
  name nVarChar(20) Team Name
  descriptio Text(16) Description
  LogInstanc Int(11) Log Instance default=0
