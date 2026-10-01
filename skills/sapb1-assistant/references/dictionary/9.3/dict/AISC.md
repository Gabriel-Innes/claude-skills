<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AISC - Input Service Distribution - Credit Memo
Module: General | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, DocEntry
  INDEX U: LogInstanc, PIndicator, DocNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  Revised VarChar(1) Revised default=N [Y=Yes, N=No]
  OrgRefNo nVarChar(100) Original Reference No.
  OrgRefEty Int(11) Original Reference Entry
  OrgDocDate Date(8) Original Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code default=0
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  ISDEntry Int(11) ISD Entry
  DataSource VarChar(1) Data Source
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(50) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
