<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OVMC - Value Mapping Communication Object
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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
