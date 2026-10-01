<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OMLT - Multi-Language Translation
Module: Administration | 6 columns | ObjType: 224
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TranEntry
  Second U: TableName, FieldAlias, PK
Fields (name type(len) description [values] ->parent table):
  TranEntry Int(11) Internal Number
  TableName nVarChar(20) Table Name
  FieldAlias nVarChar(50) Field Alias
  PK nVarChar(254) Primary Key of Object
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
