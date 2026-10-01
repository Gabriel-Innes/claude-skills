<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBSJ - Backend scheduling job
Module: General | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Job ID
  Type nVarChar(100) Job Type
  Desc nVarChar(100) Description
  Status VarChar(1) Status default=S [S=Scheduled, R=Running, E=Error, F=Finished, P=Pending, C=Creating]
  Schedule VarChar(1) Schedule Type default=O [O=Once]
  NextDate Date(8) Next Running Date
  NextTime Int(6) Next Running Time
  BFParams Text(16) Begin Function Parameters
  EFParams Text(16) End Function Parameters
  BFRetry Int(11) Begin Function Retry Times default=0
  EFRetry Int(11) End Function Retry Times default=0
  RunAs Int(6) Callback Run as User ->OUSR
  Message nVarChar(200) Status Message
  RunType VarChar(1) Run Type default=M [M=Manual, A=Automatic]
