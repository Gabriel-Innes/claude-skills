<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ABAT - Attribute - History
Module: Inventory and Production | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FldAbs Int(11) Bin Field Conf. Internal Number ->OBFC
  AttrValue nVarChar(20) Code
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Year Transfer [Y/N] default=N
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Deleted VarChar(1) Deleted default=N
