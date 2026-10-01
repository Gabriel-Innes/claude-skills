<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWL4 - Task Output Data
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, LineID, TaskID
Fields (name type(len) description [values] ->parent table):
  WFInstID nVarChar(64) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID nVarChar(6) Line ID
  ObjectType nVarChar(20) Object Type
  ObjKey nVarChar(100) Object Key
  LogIns Int(11) Log Instance
  OutParamID nVarChar(64) Object ID in WF Engine
  ObjSubType nVarChar(64) Object Subtype
