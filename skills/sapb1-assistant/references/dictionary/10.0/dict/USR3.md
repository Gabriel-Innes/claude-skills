<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# USR3 - User Authorization
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserLink, PermId
Fields (name type(len) description [values] ->parent table):
  UserLink Int(6) User Link ->OUSR
  PermId nVarChar(20) Authorization ID ->OUPT
  Permission VarChar(1) Authorization default=N [V=Various, F=Full, R=Read Only, N=None, U=Undefined Type]
