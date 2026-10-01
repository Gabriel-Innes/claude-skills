<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBFC - Bin Field Configuration
Module: Inventory and Production | 14 columns | ObjType: 10000203
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BUSINESS_K U: FldNum, FldType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldType VarChar(1) Field Type [S=Warehouse Sublevel, A=Bin Location Attribute]
  FldNum Int(6) Field Number
  DispName nVarChar(20) Display Name
  Activated VarChar(1) Active [Y/N] default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  DftName nVarChar(20) Default Field Name
