<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# QWZ3 - Query Condition Fields
Module: Reports | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Numerator
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Query Code
  Numerator Int(11) Internal Number
  OpenBrackt Int(11) Open Brackets Counter
  FileCode nVarChar(20) Table Name
  FieldAlias nVarChar(30) Field Alias
  Operation Int(11) Operation
  CondVal nVarChar(254) Cond. Val.
  CondEndVal nVarChar(254) Cond. and Val.
  CompareFld VarChar(1) Compare Fields default=N [Y=Yes, N=No]
  UseRes VarChar(1) Use Res. default=N [Y=Yes, N=No]
  CompTblIdx nVarChar(20) Compare Table Index
  CompFldNum nVarChar(254) Compare Field Number
  Relatship Int(11) Relationship
  ClosBrackt Int(11) Close Brackets Counter
  Free_Text Text(16) Free Text
