<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OSUS - Support Usage Statistics
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Identity(11) Internal Number
  SessionID Int(11) Session ID
  Type Int(11) Type
  ID nVarChar(254) ID
  Param nVarChar(254) Param.
  TimeStamp Date(8) Time Stamp
