<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AMDR1 - Manual Distribution Rule - Rows
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode, PrcCode, ValidFrom, logInstanc
  PROF_ID: PrcCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code ->OMDR
  PrcCode nVarChar(8) Cost Center Code ->OPRC
  PrcAmount Num(19,6) Total in Cost Center
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Effective from default=19000101 [19000101=]
  ValidTo Date(8) Effective to
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
