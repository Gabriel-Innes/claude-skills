<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SDIS - Dynamic Interface (Strings)
Module: Administration | 8 columns | ObjType: 229
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Language, ColumnId, ItemId, FormId
Fields (name type(len) description [values] ->parent table):
  FormId nVarChar(40) Form ID
  ItemId nVarChar(40) Item ID
  ColumnId nVarChar(20) Column ID
  Language Int(11) Language Code default=0
  ItemString nVarChar(254) Item String
  IsBold VarChar(1) Is Bold default=N [Y=Yes, N=No]
  IsItalic VarChar(1) Is Italics default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature default=-1 ->OUSR
