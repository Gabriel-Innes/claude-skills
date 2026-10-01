<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIGW - Item Group - Warehouse - History
Module: Inventory and Production | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItmsGrpCod Int(6) Item Group Code ->OITB
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
