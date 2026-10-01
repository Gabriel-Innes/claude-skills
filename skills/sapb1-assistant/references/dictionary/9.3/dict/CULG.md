<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CULG - Company Upgrade Log
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogId
Fields (name type(len) description [values] ->parent table):
  LogId Int(11) LogId
  VersFrom Int(11) Version from
  VersTo Int(11) Version to
  TableId nVarChar(4) Table ID
  OnCreate VarChar(1) Err. on creation default=C [C=Create, Q=Query]
  ErrLevel nVarChar(30) Error Level
  InQuery nVarChar(254) -
  ErrMessage nVarChar(254) -
  UpgStart nVarChar(30) Start upgrade
  UserID Int(11) User Signature
