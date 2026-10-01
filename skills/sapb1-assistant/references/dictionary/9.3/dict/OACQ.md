<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OACQ - Capitalization
Module: Finance | 44 columns | ObjType: 1470000049
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: PIndicator, DocNum
  TRANS_TYPE: CreatedBy, TransType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PeriodCat nVarChar(10) Period Category
  FinncPriod Int(11) Posting Period ->OFPR
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=P [P=Posted, D=Draft, C=Canceled]
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  Reference nVarChar(32) Reference
  ObjType nVarChar(20) Object Type
  Currency nVarChar(3) Currency ->OCRN
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Rate
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  TransType nVarChar(20) Original Document default=-1 [13=A/R Invoice, 19=A/P Credit Memo, 18=A/P Invoice, 46=Outgoing Payment, 163=A/P Correction Invoice, 1470000049=Capitalization, 1470000060=Fixed Assets Credit Memo, -1=All Transactions, 1470000075=Manual Depreciation, 1470000090=Fixed Assets Transfer, 1470000094=Retirement]
  CreatedBy Int(11) Original
  JrnlMemo nVarChar(50) Journal Remarks
  AssetDate Date(8) Asset Value Date
  CurSource VarChar(1) Base Currency default=L [L=Local Currency, S=System Currency, F=Foreign Currency]
  DocType nVarChar(15) Document Type default=PL [PL=Ordinary Depreciation, UP=Unplanned Depreciation, SD=Special Depreciation, AP=Appreciation, TR=Asset Transfer, NC=Sales, SC=Scrapping, TC=Asset Class Transfer]
  PrjSmarz VarChar(1) Summarize by Project default=N [Y=Yes, N=No]
  DstRlSmarz VarChar(1) Summarize by Distribution Rule default=N [Y=Yes, N=No]
  ManDprType nVarChar(15) Manual Depreciation Type ->ODTP
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  DprArea nVarChar(15) Depreciation Area ->ODPA
  BPLId Int(11) Branch ->OBPL
  BaseRef nVarChar(11) Base Reference
  LVARetire VarChar(1) Low Value Asset Retirement default=N [Y=Yes, N=No]
  CancelOpt Int(6) Cancelation Option default=1
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  GdsMovType nVarChar(2) Goods Movement Type [SI=Opening Balance of Fixed Assets, IM=Initialization of Fixed Assets, IP=FA Use in Progress, CI=End of Fixed Assets Use, MC=Immobilization from Current Assets]
