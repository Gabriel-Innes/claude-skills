<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OERT - Excise Register Numbering Type
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NumTypeId
  TYPE_NAME U: NumTypeNam
Fields (name type(len) description [values] ->parent table):
  NumTypeId Int(11) Numbering Type ID
  NumTypeNam nVarChar(30) Numbering Type Name
  FirstNum Int(11) First Number
  NextNum Int(11) Next Number
  LastNum Int(11) Last Number
