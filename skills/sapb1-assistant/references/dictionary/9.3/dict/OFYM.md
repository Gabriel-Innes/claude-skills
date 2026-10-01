<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFYM - Financial Year Master
Module: Finance | 6 columns | ObjType: 10000073
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
  ASSESSYEAR U: AssessYear
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(6) Code
  Descr nVarChar(30) Description
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  AssessYear nVarChar(6) Assessment Year
