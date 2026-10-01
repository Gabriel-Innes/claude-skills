<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# EMERR - EMERR
Module: General | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Identity(11) Error ID
  QueueType nVarChar(30) Queue type
  IDInQueue nVarChar(60) Message ID in the queue
  ErrCode nVarChar(60) Error code
  Severity nVarChar(10) Error severity
  ErrMessage nVarChar(254) Error message
  Member nVarChar(60) Error accessed member
  ExcType nVarChar(160) Exception type
  ExcString Text(16) Exception string
