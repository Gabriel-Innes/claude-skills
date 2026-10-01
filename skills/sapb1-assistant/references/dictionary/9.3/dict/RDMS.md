<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# RDMS - Dictionary Master
Module: General | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Num
  SBO_CODE U: SBOCode
Fields (name type(len) description [values] ->parent table):
  Num Int(11) String number
  Internal VarChar(1) Internal default=0 [1=Yes, 0=No]
  Created Date(8) Creation date
  Remarks nVarChar(250) Remarks
  SBOCode nVarChar(30) SBO Code
  StringType nVarChar(4) String Type
  MaxLen Int(11) Maximum Length
