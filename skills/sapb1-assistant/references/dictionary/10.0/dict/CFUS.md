<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# CFUS - Functionality Usage Statistics
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FuncName, UserCode
Fields (name type(len) description [values] ->parent table):
  FuncName nVarChar(100) Function Name
  UserCode nVarChar(25) User Code
  Count Int(11) Total No. of Records
  Since Date(8) Since Date
  LastUse Date(8) Last Use Date
