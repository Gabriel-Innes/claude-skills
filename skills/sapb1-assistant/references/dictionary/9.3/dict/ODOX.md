<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODOX - Data Ownership - Exceptions
Module: Administration | 10 columns | ObjType: 208
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: OwnerShpBy, SubObject, Object, QueryId
Fields (name type(len) description [values] ->parent table):
  QueryId nVarChar(20) Query ID
  Object nVarChar(20) The Object Number
  SubObject Int(6) Array Offset default=0
  UserSign Int(6) User Signature ->OUSR
  UpdateUser Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AC Int(11) Cache Access Counter default=0
  OwnerShpBy VarChar(1) Defined by Ownership Method default=N [N=Not Specified, R=Ownership By Branch]
