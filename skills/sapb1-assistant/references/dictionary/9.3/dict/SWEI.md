<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SWEI - SWEI
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: EngineAddr
Fields (name type(len) description [values] ->parent table):
  EngineAddr nVarChar(200) Workflow Engine Address
  EngineVer nVarChar(30) Workflow Engine Version
  HashCode Int(11) Random Generated Hash Code
  StartTime nVarChar(50) Start Date of Workflow Engine
  LastUpdate nVarChar(50) Last Update Date and Time
  NextUpdate nVarChar(50) Expected next update date
  EngCmpnys Text(16) Company dbs that support workf
