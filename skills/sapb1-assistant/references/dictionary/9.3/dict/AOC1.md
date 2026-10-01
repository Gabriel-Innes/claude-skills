<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AOC1 - Distribution Rule - Rows
Module: Sales Opportunities | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: logInstanc, ValidFrom, PrcCode, OcrCode
  PROF_ID: PrcCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code ->OOCR
  PrcCode nVarChar(8) Cost Center Code ->OPRC
  PrcAmount Num(19,6) Total in Cost Center
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Effective from
  ValidTo Date(8) Effective to
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
