<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OOPR - Opportunity
Module: Sales Opportunities | 57 columns | ObjType: 97
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: OpprId
Fields (name type(len) description [values] ->parent table):
  OpprId Int(11) Sequence No.
  CardCode nVarChar(15) BP Code ->OCRD
  SlpCode Int(11) Main Sales Emp. ->OSLP
  CprCode Int(11) Contact Person ->OCPR
  Source Int(11) Source ->OOSR
  IntCat1 Int(11) Interest - Field 1 ->OOIN
  IntCat2 Int(11) Interest - Field 2 ->OOIN
  IntCat3 Int(11) Interest - Field 3 ->OOIN
  IntRate Int(11) Interest Level ->OOIR
  OpenDate Date(8) Start Date
  DifType VarChar(1) Closing Type default=D [M=Months, W=Weeks, D=Days]
  PredDate Date(8) Predicted Closing Date
  MaxSumLoc Num(19,6) Local Potential Amount
  MaxSumSys Num(19,6) System Potential Amount
  WtSumLoc Num(19,6) Weighted Amount (LC) - Document
  WtSumSys Num(19,6) Weighted Amount (SC)
  PrcnProf Num(19,6) Gross Profit %
  SumProfL Num(19,6) Gross Profit Total - Local
  SumProfS Num(19,6) Gross Profit Total - System
  Memo Text(16) Remarks
  Status VarChar(1) Status default=O [O=Open, L=Lost, W=Won]
  StatusRem nVarChar(30) Status Remarks
  Reason Int(11) Reason for Closing ->OOFR
  RealSumLoc Num(19,6) Total Amount - Local
  RealSumSys Num(19,6) Total Amount - System
  RealProfL Num(19,6) Closing Gross Profit - Local
  RealProfS Num(19,6) Closing Gross Profit - System
  CloPrcnt Num(19,6) Closing Percentage
  StepLast Int(6) Current Stage No. ->OOST
  UserSign Int(6) User Signature ->OUSR
  Transfered VarChar(1) Transferred to next year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  CardName nVarChar(100) BP Name
  CloseDate Date(8) Closing Date
  LastSlp Int(11) Last Sales Emp. ->OSLP
  Name nVarChar(100) Opportunity Name
  Territory Int(11) Territory ->OTER
  Industry Int(11) Industry ->OOND
  ChnCrdCode nVarChar(15) BP Channel Code ->OCRD
  ChnCrdName nVarChar(100) BP Channel Name
  PrjCode nVarChar(20) Project Code ->OPRJ
  CardGroup Int(6) BP Group ->OCRD
  ChnCrdCon Int(11) BP Channel Contact ->OCPR
  Owner Int(11) Data Ownership field ->OHEM
  attachment Text(16) Attachments
  DocType nVarChar(9) Linked Document Type default=-1 [-1=, 23=Quotations, 17=Sales Orders, 15=Delivery Notes, 13=Sales Invoices, 540000006=Purchase Quotations, 22=Purchase Orders, 20=Goods Receipt POs, 18=Purchase Invoices]
  DocNum Int(11) Linked Document Number
  DocEntry Int(11) Linked Document Entry
  DocChkbox VarChar(1) Document Checkbox
  AtcEntry Int(11) Attachment Entry
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  OpprType VarChar(1) Opportunity Type default=R [R=Sales, P=Purchasing]
  UpdateTS Int(11) Update Full Time
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  CreateDate Date(8) Creation Date
