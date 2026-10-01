<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUGP - UoM Group
Module: Inventory and Production | 11 columns | ObjType: 10000197
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UgpEntry
  CODE U: UgpCode
  NAME: UgpName
Fields (name type(len) description [values] ->parent table):
  UgpEntry Int(11) UoM Group Abs. Entry
  UgpCode nVarChar(20) UoM Group Code
  UgpName nVarChar(100) UoM Group Name
  BaseUom Int(11) Base UoM Abs. Entry ->OUOM
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
