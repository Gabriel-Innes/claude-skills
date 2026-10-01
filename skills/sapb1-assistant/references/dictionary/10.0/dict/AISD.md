<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AISD - Input Service Distribution
Module: General | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
  INDEX U: DocNum, PIndicator, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  SrcLctCode Int(11) Source Location Code
  SrcLctName nVarChar(100) Source Location Name
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  Revised VarChar(1) Revised default=N [Y=Yes, N=No]
  OrgRefNo nVarChar(100) Original Reference No.
  OrgRefEty Int(11) Original Reference Entry
  OrgDocDate Date(8) Original Document Date
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  DstPercent Num(19,6) Percent to Distribute
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number
