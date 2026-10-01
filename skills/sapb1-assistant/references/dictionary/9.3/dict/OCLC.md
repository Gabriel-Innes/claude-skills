<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCLC - Change Logs Cleanup
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ClnpScn nVarChar(100) Cleanup Scenario Name
  ClnpDate Date(8) Cleanup Date
  UpTo Date(8) Clean Up Logs Until
  Rmrks nVarChar(254) Remarks
  CreateTS Int(11) Create Time - Incl. Secs
  UserSign Int(6) User Signature ->OUSR
