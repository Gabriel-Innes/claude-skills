<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OMRL - Advanced Inventory Revaluation
Module: Inventory and Production | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM U: Segment, Instance, DocNum
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series default=0
  DocDate Date(8) Posting Date
  RevalType VarChar(1) Inventory Valuation Type default=P [P=Price Change, M=Inventory Debit/Credit]
  Handwrtten VarChar(1) Manual Numbering default=N
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  DocCur nVarChar(3) Document Currency
  DocRate Num(19,6) Document Rate
  Ref2 nVarChar(11) Reference 2
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  DocTime Int(6) Generation Time
  Confirmed VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  StampNum nVarChar(16) Stamp No.
  FinncPriod Int(11) Posting Period ->OFPR
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  LogInstanc Int(11) Log Instance default=0
  StationID Int(11) Workstation ID ->CSTN
  Rounding VarChar(1) Rounding default=N [Y=Yes, N=No]
  Segment Int(6) Segment default=0
  ReqDate Date(8) Required Date
  CancelDate Date(8) Cancelation Date
  Project nVarChar(20) Project Code ->OPRJ
