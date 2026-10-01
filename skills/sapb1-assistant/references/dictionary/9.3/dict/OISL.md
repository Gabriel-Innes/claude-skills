<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OISL - Simulation Log File
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogEntry
Fields (name type(len) description [values] ->parent table):
  LogEntry Int(11) Internal Number
  TaskType nVarChar(20) Type of Task
  RunID Int(11) Simulation Run
  Version Int(11) B1 Main Release Version
  PatchLevel nVarChar(50) B1 Patch Level Version
  LastMsgID Int(11) Last OILM Message ID
  FinishDate Date(8) Finish Date
  FinishTime Int(6) Finish Time
  UserCode nVarChar(25) User Code
  Status VarChar(1) Status [R=In Progress, F=Failed, S=Successful]
  InitMap VarChar(1) Initialize MAP Items
  InitStd VarChar(1) Initialize STD Items
