<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ABP1 - Business Place Tax IDs
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, DstState, BPLId
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) BPL ID ->OBPL
  DstState nVarChar(3) Destination State ->OCST
  IENumber nVarChar(32) I.E. Number
  LogInstanc Int(11) Log Instance default=0
