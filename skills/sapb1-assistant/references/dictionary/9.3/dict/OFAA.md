<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OFAA - Asset Attributes
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  Name U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(100) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  SnapshotId Int(11) Snapshot ID default=0
