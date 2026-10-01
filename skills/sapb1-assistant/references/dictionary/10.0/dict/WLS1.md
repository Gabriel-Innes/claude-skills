<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WLS1 - Potential Processor of Tasks
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(6) Line ID
  Candidate nVarChar(254) Candidate
  LogIns Int(11) Log Instance
  WasRead VarChar(1) Was Read default=N [Y=Yes, N=No]
  CandExpr nVarChar(254) Candidate Expression
