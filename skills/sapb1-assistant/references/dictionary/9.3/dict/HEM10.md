<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HEM10 - Employee Branch Assignment
Module: Human Resources | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BPLId, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No.
  BPLId Int(11) Assigned Branch ->OBPL
