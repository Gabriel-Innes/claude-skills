<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OCEST - CEST Codes
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CEST_CODE U: CEST
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CEST nVarChar(32) CEST Code
  Descr Text(16) Description
  LogInstanc Int(11) Log Instance default=0
