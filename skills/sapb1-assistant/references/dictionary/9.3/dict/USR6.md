<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# USR6 - User Branch Assignment
Module: Business Partners | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, UserCode
Fields (name type(len) description [values] ->parent table):
  UserCode nVarChar(25) User Code ->OUSR
  BPLId Int(11) Assigned Branch ->OBPL
  DigCrtPath Text(16) Digital Certificate Path
  AcsDsbldBP VarChar(1) Access Disabled BP default=N [Y=Yes, N=No]
