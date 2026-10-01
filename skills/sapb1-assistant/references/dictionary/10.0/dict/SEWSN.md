<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SEWSN - 
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MachineNam, CompDbNam
Fields (name type(len) description [values] ->parent table):
  MachineNam nVarChar(64) Machine Name
  CompDbNam nVarChar(100) Company Db Name
  CollecStat Int(11) Collection Status default=0 [0=No Collection, 1=In Process, 2=Completed]
  SentUser nVarChar(30) Sent User
  CompleDate nVarChar(10) Completion Date
