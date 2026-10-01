<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AIRI - Input Service Distribution - Recipient Invoice
Module: General | 27 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, DocEntry
  INDEX U: LogInstanc, PIndicator, DocNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=O [O=Open, C=Canceled]
  RefNo nVarChar(100) Reference No.
  RefEntry Int(11) Reference Entry
  RefDocDate Date(8) Reference Document Date
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  ObjType nVarChar(20) Object Type
  SrcLoc Int(11) Source Location Code
  SrcLocName nVarChar(100) Source Location Name
  SrcGSTIN nVarChar(15) Source Location GSTIN
  TarLoc Int(11) Target Location Code
  TarLocName nVarChar(100) Target Location Name
  TarGSTIN nVarChar(15) Target Location GSTIN
  DataSource VarChar(1) Data Source
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  JrnlMemo nVarChar(50) Journal Remarks
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
