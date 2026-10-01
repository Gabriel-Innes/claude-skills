<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# QWZ2 - Query Result Fields
Module: Reports | 19 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Numerator, Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Query Code
  Numerator Int(11) Internal Number
  FileCode nVarChar(20) Table Name
  FieldAlias nVarChar(10) Field Alias
  Title nVarChar(30) Field Title
  SortOrder Int(11) Sort Order
  SortType VarChar(1) Sort Type default=N [Y=Yes, N=No]
  GroupBy VarChar(1) Group By default=N [Y=Yes, N=No]
  AgregType Int(11) Agreggate Function
  CalcField nVarChar(254) Calculation Field
  IsCalc VarChar(1) Is Calculation default=N [Y=Yes, N=No]
  TmpAlias nVarChar(11) New Alias in Res. Table
  TmpDescr nVarChar(30) New Description in Res. Table
  Fld2Alias nVarChar(10) Field 2 Number
  FileCode2 nVarChar(20) Field 2 Table Name
  Agreg2Type Int(11) Field 2 Aggregate Function
  FldOp Int(11) Formula Operation
  FldCnstVal nVarChar(254) Field Const. Val.
  Fld2CnsVal nVarChar(254) Field 2 Const. Val.
