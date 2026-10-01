<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWFQ - SWFQ History Table
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SequenceID, LogInst
Fields (name type(len) description [values] ->parent table):
  SequenceID Int(11) Sequence ID
  SourceDB nVarChar(100) Source Database
  Timestamp nVarChar(20) Time Stamp
  ObjectType nVarChar(30) Object Type
  TransType VarChar(1) Transaction Type [A=Add, U=Update, C=Cancel, D=Delete]
  FieldsInKe Int(11) Number of Fields in Key
  FieldNames nVarChar(254) Key Field Names
  FieldValue nVarChar(254) Key Field Values
  UserID nVarChar(25) UserID
  TaskID nVarChar(64) Task ID
  TrigEvntID nVarChar(64) Trigger Event ID
  TrigParams Text(16) Trigger Parameters
  LogInst Int(11) Log Instance
  IsSuccess VarChar(1) Is Message Handled Successfully
  ResultMemo nVarChar(250) Memo of the Result
