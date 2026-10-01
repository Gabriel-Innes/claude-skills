<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WLS5 - Task Field Mapping Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID
Fields (name type(len) description [values] ->parent table):
  WFInstID nVarChar(64) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID nVarChar(6) Line ID
  InputID Int(11) Input ID
  SrcFld nVarChar(50) Source Field
  TgtFld nVarChar(50) Target Field
  LogIns Int(11) Log Instance
