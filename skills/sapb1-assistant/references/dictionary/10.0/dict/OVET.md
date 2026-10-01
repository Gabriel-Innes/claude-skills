<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OVET - VAT Exemption Types
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: typeID
Fields (name type(len) description [values] ->parent table):
  typeID Int(6) Type ID
  TypeCode nVarChar(2) Type Code
  TypeName nVarChar(100) Type Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
