<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# REQ3 - External System Call Request - Message Argument List
Module: Service | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ArgName, LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Request ID ->OREQ
  LineId Int(11) Message Line ID ->REQ1
  ArgName nVarChar(20) Argument Name
  ArgValue nVarChar(254) Argument Value
