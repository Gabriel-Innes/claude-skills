<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OACS - Asset Classes
Module: Finance | 14 columns | ObjType: 1470000032
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  AssetType VarChar(1) Asset Type default=G [G=General, L=Low Value Asset]
  LimitFrom Num(19,6) Value Limit From
  LimitTo Num(19,6) Value Limit To
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  BPLId Int(11) Branch ->OBPL
  AttrGrp Int(11) Attribute Group default=-1 ->OFAA
  SnapshotId Int(11) Snapshot ID default=0
