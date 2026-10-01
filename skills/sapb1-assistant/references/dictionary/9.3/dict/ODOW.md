<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODOW - Data Ownership - Objects
Module: Administration | 11 columns | ObjType: 207
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SubObject, Object
Fields (name type(len) description [values] ->parent table):
  Object nVarChar(20) The Object Number
  SubObject Int(6) Array Offset default=0
  OwnerField Int(6) Column Number of Owner
  Active VarChar(1) Indication: Does it Work default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  UpdateUser Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AC Int(11) Cache Access Counter default=0
  OwnerCtrl Int(6) The way owner is controlled default=7
