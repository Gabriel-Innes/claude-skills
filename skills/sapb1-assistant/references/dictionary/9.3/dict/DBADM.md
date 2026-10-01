<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DBADM - Read-Only DB User
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ROUser
Fields (name type(len) description [values] ->parent table):
  ROUser nVarChar(254) Read-Only User
  ROPass nVarChar(254) Read-Only Password
