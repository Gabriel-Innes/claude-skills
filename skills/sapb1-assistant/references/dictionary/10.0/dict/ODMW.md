<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ODMW - Data Migration
Module: Administration | 11 columns | ObjType: 136
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Package Code
  Name nVarChar(20) Package Name
  CategoryId Int(11) Category ID ->OQCN
  DestPath Text(16) Dest. Path
  Extantion nVarChar(5) Exported
  UserSign Int(6) User Signature ->OUSR
  Delim nVarChar(10) Include Title default=T [T=Tab, K=,, D=;, S=Space]
  InclTitle VarChar(1) Set to Exported default=N [Y=Yes, N=No]
  SetExp VarChar(1) New Records default=N [Y=Yes, N=No]
  NewRecs VarChar(1) Save default=N [Y=Yes, N=No]
  Summary Text(16) Summary
