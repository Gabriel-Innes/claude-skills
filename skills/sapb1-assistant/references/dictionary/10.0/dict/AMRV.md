<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AMRV - Inventory Revaluation - History
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc, ObjType
  NUM: DocNum, LogInstanc, ObjType
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocDate Date(8) Posting Date
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(254) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  DocTime Int(6) Generation Time
  RevalType VarChar(1) Inventory Revaluation Type default=P [P=Price Change, M=Material Debit/Credit]
  UpdateDate Date(8) Update Date
  CreateDate Date(8) Creation Date
  Series Int(11) Series default=0 ->NNM1
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto. Incr., D=Data Document, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  StationID Int(11) Workstation ID ->CSTN
  RIncmAcct nVarChar(15) Invent. Reval. Expense Account
  RExpnAcct nVarChar(15) Invent. Reval. Expense Account
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=162
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  VersionNum nVarChar(13) Version Number
  InflaReval VarChar(1) Inflation-Based Revaluation default=N
  SupplCode nVarChar(254) Supplementary Code
  CardCode nVarChar(15) Customer/Vendor Code
  CardName nVarChar(100) Customer/Vendor Name
  CreatedBy VarChar(1) Entry Creation Origin default=M [M=Created Manually by User, W=Created by Production Cost Recalculation Wizard]
