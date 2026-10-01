<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EMIDS - EMIDS
Module: General | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DispatchID, SequenceID
Fields (name type(len) description [values] ->parent table):
  SequenceID nVarChar(60) Event Sequence ID
  ProcessID nVarChar(60) Processed message ID
  DispatchID nVarChar(60) Dispached message ID
