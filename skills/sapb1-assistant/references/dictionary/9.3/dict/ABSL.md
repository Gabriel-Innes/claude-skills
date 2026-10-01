<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ABSL - Warehouse Sublevel - History
Module: Inventory and Production | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldAbs Int(11) Bin Field Conf. Internal Number ->OBFC
  SLCode nVarChar(50) Code
  Descr nVarChar(50) Description
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N
