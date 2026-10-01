<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWL2 - Input data for tasks
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, LineID, TaskID
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
