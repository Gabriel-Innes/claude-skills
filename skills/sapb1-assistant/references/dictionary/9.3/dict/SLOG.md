<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SLOG - SLOG
Module: General | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsKey
Fields (name type(len) description [values] ->parent table):
  LogConfig Text(16) Log configuration
  UseDBConf VarChar(1) Use DB configuration
  ActLog VarChar(1) Activate Log
  ModDate Date(8) DB log modification date
  LogDefConf Text(16) Log Default configuration
  ReposConf Text(16) Log Repository Configuration
  AbsKey Identity(11) Primary Key
  ModTime Int(6) DB log modification time
