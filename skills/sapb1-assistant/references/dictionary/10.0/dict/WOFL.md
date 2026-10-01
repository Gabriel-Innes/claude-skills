<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# WOFL - Object Wizard Fields
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjCode, FldIndex
Fields (name type(len) description [values] ->parent table):
  ObjCode Int(11) Object Code
  FldIndex Int(6) Field Index
  FldNum Int(6) Field Number
  Editable VarChar(1) Editable default=N [Y=Yes, N=No]
  Find VarChar(1) Find default=N [Y=Yes, N=No]
  DispDescr VarChar(1) Display Description default=N [Y=Yes, N=No]
