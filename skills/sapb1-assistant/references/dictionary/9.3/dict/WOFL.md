<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# WOFL - Object Wizard Fields
Module: General | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: FldIndex, ObjCode
Fields (name type(len) description [values] ->parent table):
  ObjCode Int(11) Object Code
  FldIndex Int(6) Field Index
  FldNum Int(6) Field Number
  Editable VarChar(1) Editable default=N [Y=Yes, N=No]
  Find VarChar(1) Find default=N [Y=Yes, N=No]
  DispDescr VarChar(1) Display Description default=N [Y=Yes, N=No]
