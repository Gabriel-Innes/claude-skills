<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# CFUS - Functionality Usage Statistics
Module: General | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UserCode, FuncName
Fields (name type(len) description [values] ->parent table):
  FuncName nVarChar(100) Function Name
  UserCode nVarChar(25) User Code
  Count Int(11) Total No. of Records
  Since Date(8) Since Date
  LastUse Date(8) Last Use Date
