<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# USR3 - User Authorization
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PermId, UserLink
Fields (name type(len) description [values] ->parent table):
  UserLink Int(6) User Link ->OUSR
  PermId nVarChar(20) Authorization ID ->OUPT
  Permission VarChar(1) Authorization default=N [V=Various, F=Full, R=Read Only, N=None, U=Undefined Type]
