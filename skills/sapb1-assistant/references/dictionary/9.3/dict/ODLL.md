<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODLL - Bar Code Algorithm File
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DllEntry
  NAME U: DllName
Fields (name type(len) description [values] ->parent table):
  DllEntry Int(11) Internal Number
  DllName nVarChar(254) DLL Name
  DllDesp nVarChar(50) DLL Description
