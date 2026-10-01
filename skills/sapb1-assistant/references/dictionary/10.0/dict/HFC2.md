<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# HFC2 - Hide Function Configuration - Rows
Module: General | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FuncID Int(11) Function ID ->OHFC
  MainMenu Int(11) Main Menu ID
  MovMenuTo Int(11) Target Postion Menu Move
  ActionType Int(6) Action Type default=0 [0=Hide Menu, 1=Move Menu, 2=Hide Pop-Up Menu]
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
