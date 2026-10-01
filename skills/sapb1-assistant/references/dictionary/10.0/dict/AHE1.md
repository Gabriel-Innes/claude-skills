<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AHE1 - Absence Information
Module: Human Resources | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: empID, line, LogInstanc
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee ID ->OHEM
  line Int(6) Absence Information Row
  fromDate Date(8) Absence From
  toDate Date(8) Absence To
  reason nVarChar(20) Reason
  approvedBy nVarChar(20) Approved By
  cnfrmrNum Int(11) Confirmer Number ->OHEM
  LogInstanc Int(11) Log Instance default=0
  type Int(11) Absence Type ->PMC5
  EncryptIV nVarChar(100) Encrypt IV
