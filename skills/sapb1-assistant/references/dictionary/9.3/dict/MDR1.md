<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# MDR1 - Manual Distribution Rule - Rows
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ValidFrom, PrcCode, OcrCode
  PROF_ID: PrcCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code ->OMDR
  PrcCode nVarChar(8) Center Code ->OPRC
  PrcAmount Num(19,6) Total in Center
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=, N=]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Effective From default=19000101 [19000101=]
  ValidTo Date(8) Effective To
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
