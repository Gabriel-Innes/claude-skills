<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AWL3 - Task Notes
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, LineID, TaskID
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(11) Line ID
  Note Text(16) Note
  Creator nVarChar(25) Creator
  NoteDate Date(8) Note Date
  Access VarChar(1) Accessibility default=W [W=Workflow, T=Task]
  LogIns Int(11) Log Instance
