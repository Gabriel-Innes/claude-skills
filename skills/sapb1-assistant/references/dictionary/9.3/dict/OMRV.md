<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMRV - Inventory Revaluation
Module: Inventory and Production | 32 columns | ObjType: 162
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM: DocNum
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocDate Date(8) Posting Date
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  DocTime Int(6) Generation Time
  RevalType VarChar(1) Inventory Valuation Type default=P [P=Price Change, M=Inventory Debit/Credit]
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Series Int(11) Series ->NNM1
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
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
  VersionNum nVarChar(11) Version Number
  InflaReval VarChar(1) Inflation-Based Revaluation default=N [Y=Yes, N=No]
  SupplCode nVarChar(254) Supplementary Code
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  CardName nVarChar(100) Customer/Vendor Name
  CreatedBy VarChar(1) Entry Creation Origin default=M [M=Created Manually by User, W=Created by Production Cost Recalculation Wizard]
