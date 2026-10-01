<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CRD8 - BP Branch Assignment
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, BPLId
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  BPLId Int(11) Assigned Branch ->OBPL
  DisabledBP VarChar(1) Disabled for BP default=N [Y=Yes, N=No]
