<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AHE1 - Absence Information
Module: Human Resources | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee ID ->OHEM
  line Int(6) Absence Information Row
  fromDate Date(8) Absence from
  toDate Date(8) Absence to
  reason nVarChar(20) Reason
  approvedBy nVarChar(20) Approved By
  cnfrmrNum Int(11) Confirmer Number ->OHEM
  LogInstanc Int(11) Log Instance default=0
  type Int(11) Absence Type
