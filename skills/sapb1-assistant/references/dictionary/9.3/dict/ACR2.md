<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACR2 - Bussiness Partners - Payment Methods-History
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, LineNum, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  LineNum Int(11) Row Number
  PymCode nVarChar(15) Payment Method Code ->OPYM
  LogInstanc Int(11) Log Instance default=0
  ObjType Int(6) Object Type default=2 ->ADP1
