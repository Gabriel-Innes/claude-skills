<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WLS1 - Potential Processor of Tasks
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, TaskID
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(6) Line ID
  Candidate nVarChar(254) Candidate
  LogIns Int(11) Log Instance
  WasRead VarChar(1) Was Read default=N [Y=Yes, N=No]
  CandExpr nVarChar(254) Candidate Expression
