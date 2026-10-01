<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OADF - Address Formats
Module: Administration | 4 columns | ObjType: 131
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  ADF_NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(50) Name
  Format nVarChar(100) Format
  UserSign Int(6) User Signature ->OUSR
