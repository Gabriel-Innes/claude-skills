<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMLT - Multi-Language Translation
Module: Administration | 6 columns | ObjType: 224
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TranEntry
  Second U: PK, FieldAlias, TableName
Fields (name type(len) description [values] ->parent table):
  TranEntry Int(11) Internal Number
  TableName nVarChar(20) Table Name
  FieldAlias nVarChar(50) Field Alias
  PK nVarChar(254) Primary Key of Object
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
