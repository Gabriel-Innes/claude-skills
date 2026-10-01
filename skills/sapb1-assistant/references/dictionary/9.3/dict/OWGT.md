<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OWGT - Weight Units
Module: Inventory and Production | 7 columns | ObjType: 51
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UnitCode
  DISPLAY U: UnitDisply
  UNIT_NAME U: UnitName
Fields (name type(len) description [values] ->parent table):
  UnitCode Int(6) Unit Code
  UnitDisply nVarChar(2) Unit Display
  UnitName nVarChar(20) Unit Name
  WightInMG Num(19,6) Unit Weight in mg
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
