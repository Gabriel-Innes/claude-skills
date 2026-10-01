<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# PUTR - Pre-Upgrade Test Result
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SerialNum
Fields (name type(len) description [values] ->parent table):
  SerialNum Int(11) Serial Number
  CompanyVer nVarChar(40) Company Version
  TargetVer nVarChar(40) Target Version
  BeginTime nVarChar(20) Start Time
  EndTime nVarChar(20) End Time
