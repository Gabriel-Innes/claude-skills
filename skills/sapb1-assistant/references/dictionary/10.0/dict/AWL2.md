<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWL2 - Input data for tasks
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(11) Line ID
  ObjectType nVarChar(20) Object Type
  ObjKey nVarChar(100) Object Key
  Command VarChar(1) Command default=B [B=Based On, M=Field Mapping]
  LogIns Int(11) Log Instance
  ObjSubType nVarChar(64) Object Subtype
  ObjDetail Text(16) Object Detail
