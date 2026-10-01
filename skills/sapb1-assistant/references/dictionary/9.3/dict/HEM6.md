<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# HEM6 - Employee Roles
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Employee Role Row
  roleID Int(11) Role ID ->OHTY
  LogInstanc Int(11) Log Instance default=0
