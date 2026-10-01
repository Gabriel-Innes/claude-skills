<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# QWZ1 - Query Tables
Module: Reports | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Numerator, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Query Code
  Numerator Int(11) Internal Number
  FileCode nVarChar(20) Table Name
  IsTemp VarChar(1) Is Temp default=N [Y=Yes, N=No]
  DoJoin VarChar(1) Do Join default=N [Y=Yes, N=No]
  JoinToTbl Int(11) Joined to Table
  NumOfConds Int(11) No. of Conds.
  OuterJoin VarChar(1) Outer Join default=N [Y=Yes, N=No]
  RightJoin VarChar(1) Right Join default=N [Y=Yes, N=No]
