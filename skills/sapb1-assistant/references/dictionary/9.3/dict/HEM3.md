<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HEM3 - Employee Reviews
Module: Human Resources | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Employee Review Row
  date Date(8) Employee Review Date
  reviewDesc nVarChar(100) Review Description
  manager Int(11) Manager ->OHEM
  grade nVarChar(50) Grade
  remarks Text(16) Reviews
  LogInstanc Int(11) Log Instance default=0
