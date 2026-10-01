<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EMSTT - EMSTT
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Status, Timestamp, MessageID
Fields (name type(len) description [values] ->parent table):
  MessageID nVarChar(60) Message ID
  Timestamp Date(8) Timestamp
  Status nVarChar(30) Status
  ErrorID Int(11) Error ID
