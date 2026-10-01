<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MPO1 - Value Mapping Data
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineId Int(11) Line Id
  ThirdPID Int(11) Third party internal number
  ThirdPVal nVarChar(100) Third Party Value
