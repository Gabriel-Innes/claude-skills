<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OERN - Excise Register Numbering
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NumTypeID
Fields (name type(len) description [values] ->parent table):
  NumTypeID Int(11) ID for numbering type
  NumTypeNam nVarChar(30) Name for numbering type
  FirstNum Int(11) First number default=1
  NextNum Int(11) Next Number default=1
  LastNum Int(11) Last Number
  UserSign Int(6) User Signature ->OUSR
  ResetDate Date(8) Date of last reset
