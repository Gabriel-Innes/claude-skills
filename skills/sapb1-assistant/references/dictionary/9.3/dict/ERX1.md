<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ERX1 - Excise Registering Number-Rows
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NumTypeId, ErnId
Fields (name type(len) description [values] ->parent table):
  ErnId Int(11) Excise Register Numbering ID ->OERX
  NumTypeId Int(11) Numbering Type ID
  NumTypeNam nVarChar(30) Numbering Type Name
  FirstNum Int(11) First Number
  NextNum Int(11) Next Number
  LastNum Int(11) Last Number
  ResetDate Date(8) Date of last reset
