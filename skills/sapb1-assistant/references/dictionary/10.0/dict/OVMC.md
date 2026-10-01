<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OVMC - Value Mapping Communication Object
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SYS_ID Int(11) Third Party System ID
  ObjectId Int(11) Object ID
  Type nVarChar(2) Type default=MD [MD=Master Data, TR=Transaction]
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  EndDate Date(8) End Date
  EndTime Int(11) End Time
  Message Text(16) Message
  Status VarChar(1) Communication Status default=P [P=Pending, E=Error, N=New, S=Successful, R=Rejected]
