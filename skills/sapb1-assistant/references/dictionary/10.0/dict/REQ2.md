<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# REQ2 - External System Call Request - Argument List
Module: Service | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId, ArgName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Request ID ->OREQ
  LineId Int(11) Message Line ID default=1
  ArgName nVarChar(20) Argument Name
  ArgValue nVarChar(254) Argument Value
