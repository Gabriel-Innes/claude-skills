<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWL5 - Task Field Mapping Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, LineID, TaskID
Fields (name type(len) description [values] ->parent table):
  WFInstID nVarChar(64) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID nVarChar(6) Line ID
  InputID Int(11) Input ID
  SrcFld nVarChar(50) Source Field
  TgtFld nVarChar(50) Target Field
  LogIns Int(11) Log Instance
