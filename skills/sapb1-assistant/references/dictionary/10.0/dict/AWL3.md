<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AWL3 - Task Notes
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(11) Line ID
  Note Text(16) Note
  Creator nVarChar(25) Creator
  NoteDate Date(8) Note Date
  Access VarChar(1) Accessibility default=W [W=Workflow, T=Task]
  LogIns Int(11) Log Instance
