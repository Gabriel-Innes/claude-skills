<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AHF1 - Hide Functions Configuration - Rows History
Module: General | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FuncID Int(11) Function ID ->OHFC
  formNum nVarChar(128) Form Number
  ItemUID nVarChar(128) Item UID
  ColUID nVarChar(128) Column UID
  HideVal nVarChar(20) Hide Valid Value
  AltVal nVarChar(20) Alternative Valid Value
  PanelID Int(6) Hide Item by Panel
  ActionType Int(6) Hide Item Action Type default=0 [0=Hide Item, 1=Hide Column, 2=Hide Item's Valid Value, 3=Hide Panel, 4=Hide Column's Valid Value]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
