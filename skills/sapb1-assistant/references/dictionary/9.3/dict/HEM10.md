<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HEM10 - Employee Branch Assignment
Module: Human Resources | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No.
  BPLId Int(11) Assigned Branch ->OBPL
