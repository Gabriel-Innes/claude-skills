<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OMSG - Messaging Service Settings
Module: Administration | 4 columns | ObjType: 10000105
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USERID
Fields (name type(len) description [values] ->parent table):
  USERID Int(6) User Signature default=-1
  Signature Text(16) E-Mail signature
  UseCompSig VarChar(1) Use Company Signature default=N [Y=Yes, N=No]
  DummySig Text(16) Dummy Signature
