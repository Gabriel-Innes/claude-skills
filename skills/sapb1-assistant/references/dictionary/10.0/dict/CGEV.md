<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CGEV - Event Log
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EventID
Fields (name type(len) description [values] ->parent table):
  EventID Identity(11) Event ID
  EventDate Date(8) Date of Event
  EventTime Int(11) Timestamp of Event
  UserCode nVarChar(25) Current User ID
  SourceIP nVarChar(64) Network Address of SAP Business One Client
  EventType nVarChar(32) Event Type
  EventDetls Text(16) Event Description
