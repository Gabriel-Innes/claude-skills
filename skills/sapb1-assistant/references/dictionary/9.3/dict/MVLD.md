<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MVLD - MVLD
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: lineNum, fatherId
  GUID U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  lineNum Int(11) Line Number
  value nVarChar(254) Value
  note nVarChar(254) Note
  noteSid Int(11) Note String Id
