<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACL2 - Activity Multiple Recipients - History
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ClgCode, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ClgCode Int(11) Activity Number ->OCLG
  LineNum Int(11) Line Number
  ObjType nVarChar(20) Object Type default=12 [12=User, 171=Employee]
  ObjCode nVarChar(50) Object Code
  LogInstanc Int(11) Log Instance default=0
