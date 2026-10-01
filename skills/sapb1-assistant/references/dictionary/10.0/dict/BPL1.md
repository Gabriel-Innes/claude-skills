<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# BPL1 - Branch I.E. Numbers
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, DstState
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) BPL ID ->OBPL
  DstState nVarChar(3) Destination State ->OCST
  IENumber nVarChar(32) I.E. Number
  LogInstanc Int(11) Log Instance default=0
