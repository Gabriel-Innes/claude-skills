<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBFC - Bin Field Configuration
Module: Inventory and Production | 14 columns | ObjType: 10000203
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  BUSINESS_K U: FldType, FldNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldType VarChar(1) Field Type [S=Warehouse Sublevel, A=Bin Location Attribute]
  FldNum Int(6) Field Number
  DispName nVarChar(20) Display Name
  Activated VarChar(1) Active [Y/N] default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  DftName nVarChar(20) Default Field Name
