<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UGR1 - Group Authorization
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PermId, GroupLink
Fields (name type(len) description [values] ->parent table):
  GroupLink Int(6) Group Link ->OUGR
  PermId nVarChar(20) Authorization ID ->OUPT
  Permission VarChar(1) Authorization default=N [V=Various, F=Full, R=Read Only, N=None, U=Undefined Type]
