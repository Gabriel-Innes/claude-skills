<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SXRDB - XLR Databases
Module: General | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DatabaseId
Fields (name type(len) description [values] ->parent table):
  Name nVarChar(50) Name
  ConnectStr nVarChar(250) ConnectString
  Constrain nVarChar(250) Constraint
  DatabaseId nVarChar(250) DatabaseId
