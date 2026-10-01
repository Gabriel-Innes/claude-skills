<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SEWSN - SEWSN
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompDbNam, MachineNam
Fields (name type(len) description [values] ->parent table):
  MachineNam nVarChar(64) Machine Name
  CompDbNam nVarChar(100) Company Db Name
  CollecStat Int(11) Collection Status default=0 [0=No Collection, 1=In Process, 2=Completed]
  SentUser nVarChar(30) Sent User
  CompleDate nVarChar(10) Completion Date
