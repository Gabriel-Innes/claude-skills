<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OADF - Address Formats
Module: Administration | 5 columns | ObjType: 131
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  ADF_NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(50) Name
  Format nVarChar(100) Format
  UserSign Int(6) User Signature ->OUSR
  SuppBkLine VarChar(1) Suppress Blank Lines default=N [N=No, Y=Yes]
