<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWGT - Weight Units
Module: Inventory and Production | 7 columns | ObjType: 51
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UnitCode
  DISPLAY U: UnitDisply
  UNIT_NAME U: UnitName
Fields (name type(len) description [values] ->parent table):
  UnitCode Int(6) Unit Code
  UnitDisply nVarChar(2) Unit Display
  UnitName nVarChar(20) Unit Name
  WightInMG Num(19,6) Unit Weight in mg
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
