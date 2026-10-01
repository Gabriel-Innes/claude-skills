<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUKD - User Key Description
Module: Administration | 5 columns | ObjType: 193
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: KeyId, TableName
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(20) Table Name
  KeyId Int(6) Key Index
  KeyName nVarChar(10) Key Name
  UniqueKey VarChar(1) Unique Key default=N [Y=Yes, N=No]
  Action VarChar(1) Action default=N [A=Add, U=Update, D=Delete, N=None]
