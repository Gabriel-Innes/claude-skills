<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# SDIS - Dynamic Interface (Strings)
Module: Administration | 8 columns | ObjType: 229
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormId, ItemId, ColumnId, Language
Fields (name type(len) description [values] ->parent table):
  FormId nVarChar(40) Form ID
  ItemId nVarChar(40) Item ID
  ColumnId nVarChar(20) Column ID
  Language Int(11) Language Code default=0
  ItemString nVarChar(254) Item String
  IsBold VarChar(1) Is Bold default=N [Y=Yes, N=No]
  IsItalic VarChar(1) Is Italics default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature default=-1 ->OUSR
