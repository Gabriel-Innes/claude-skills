<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OLGT - Length Units
Module: Inventory and Production | 8 columns | ObjType: 50
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: UnitCode
  DISPLAY U: UnitDisply
  UNIT_NAME U: UnitName
  VOLUME: VolDisply
Fields (name type(len) description [values] ->parent table):
  UnitCode Int(6) Unit Code
  UnitDisply nVarChar(2) Unit Display
  UnitName nVarChar(20) Unit Name
  VolDisply nVarChar(3) Unit Code for Quantity Display
  SizeInMM Num(19,6) Unit Length in mm
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
