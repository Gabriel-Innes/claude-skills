<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# USR6 - User Branch Assignment
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserCode, BPLId
Fields (name type(len) description [values] ->parent table):
  UserCode nVarChar(25) User Code ->OUSR
  BPLId Int(11) Assigned Branch ->OBPL
  DigCrtPath Text(16) Digital Certificate Path
  AcsDsbldBP VarChar(1) Access Disabled BP default=N [Y=Yes, N=No]
  UserID Int(6) User ID
