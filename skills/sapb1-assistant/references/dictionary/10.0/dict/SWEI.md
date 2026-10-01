<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SWEI - 
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EngineAddr
Fields (name type(len) description [values] ->parent table):
  EngineAddr nVarChar(200) Workflow Engine Address
  EngineVer nVarChar(30) Workflow Engine Version
  HashCode Int(11) Random Generated Hash Code
  StartTime nVarChar(50) Start Date of Workflow Engine
  LastUpdate nVarChar(50) Last Update Date and Time
  NextUpdate nVarChar(50) Expected next update date
  EngCmpnys Text(16) Company dbs that support workf
