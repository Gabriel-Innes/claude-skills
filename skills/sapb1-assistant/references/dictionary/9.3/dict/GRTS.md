<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# GRTS - GRTS
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ScopeID
Fields (name type(len) description [values] ->parent table):
  ScopeID Int(11) Scope ID
  Descript nVarChar(50) Description
  Granted VarChar(1) Granted default=N [Y=Yes, N=No]
  AccssT nVarChar(100) Access Token
  RfrshT nVarChar(100) Refresh Token
