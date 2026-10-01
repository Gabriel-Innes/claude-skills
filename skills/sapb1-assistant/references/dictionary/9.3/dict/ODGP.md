<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODGP - Document Generation Parameter Sets
Module: Administration | 57 columns | ObjType: 233
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SET_NAME U: SetName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SetName nVarChar(20) Set Name
  SetDesc nVarChar(100) Set Description
  CreateDate Date(8) Creation Date
  ModifyDate Date(8) Last Modified
  UserSign Int(6) User Signature ->OUSR
  Target nVarChar(20) Target Document Type default=-1 [-1=, 17=Sales Order, 15=Delivery, 16=Returns, 13=A/R Invoice]
  PostDate Date(8) Posting Date
  TaxDate Date(8) Document Date
  Series Int(11) Series
  Items VarChar(1) Items Documents Summary default=Y [Y=Yes, N=No]
  ItemSmmry VarChar(1) Items Summary Method default=N [N=No Summary, I=Summary by Items, D=Summary by Documents]
  Service VarChar(1) Service Documents Summary default=N [Y=Yes, N=No]
  ServSmmry VarChar(1) Service Summary Method default=N [N=No Summary, D=Summary by Documents]
  ExchgRate VarChar(1) Exchange Rate default=C [D=Use Base Doc. and Row Rate, B=Use Base Row Rate, C=Use Current Rate]
  CreatDraft VarChar(1) Create Drafts default=N [Y=Yes, N=No]
  BaseQUT VarChar(1) Sales Quotation Summary default=N [Y=Yes, N=No]
  BaseRDR VarChar(1) Order Summary default=N [Y=Yes, N=No]
  BaseDLN VarChar(1) Delivery Summary default=N [Y=Yes, N=No]
  BaseRDN VarChar(1) Returns Summary default=N [Y=Yes, N=No]
  BaseResINV VarChar(1) A/R Reserve Invoice Summary default=N [Y=Yes, N=No]
  ExpndSel VarChar(1) Expanded Selection Criteria default=N [Y=Yes, N=No]
  SortField nVarChar(100) Sort Field default=DocNum [DocNum=Document Number, DocDate=Posting Date, DocDueDate=Due Date, NumAtCard=BP Reference No., DocTotal=Document Amount, SlpCode=Sales Employee]
  Consolidat VarChar(1) Consolidate default=Y [Y=Yes, N=No]
  ExpandCons VarChar(1) Expanded Consolidation Options default=N [Y=Yes, N=No]
  RCNSummary VarChar(1) Reference Document default=N [Y=Yes, N=No]
  ChainCode Int(11) Retail Chain
  OredrNum1 Int(11) Order No. From
  OredrNum2 Int(11) To
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  Indirect VarChar(1) Indirect default=N [Y=Yes, N=No]
  DoReport VarChar(1) Overview of Invoice Deliveries default=N [Y=Yes, N=No]
  FileExport VarChar(1) File Export default=N [Y=Yes, N=No]
  SavePath Text(16) File Path
  DealNum nVarChar(12) Closing No.
  UseDirect VarChar(1) Direct/Indirect default=N [Y=Yes, N=No]
  NoItmCode VarChar(1) Drop Item No. Where Cat. No. E default=N [Y=Yes, N=No]
  OnData VarChar(1) Missing Data default=N [N=Skip to Next Document, B=Skip to Next Customer, W=Ask for User Confirmation]
  OnLedger VarChar(1) Bookkeeping Alert default=N [N=Skip to Next Document, B=Skip to Next Customer, W=Ask for User Confirmation]
  OnInvnt VarChar(1) Warehouse Alert default=N [N=Skip to Next Document, B=Skip to Next Customer, W=Ask for User Confirmation]
  Summary nVarChar(250) Summary
  AltItmDocs VarChar(1) Process docsc with alt. items default=Y [Y=Yes, N=No]
  PartDelivr VarChar(1) Partial Delivery default=N [Y=Yes, N=No]
  ConsiderBP VarChar(1) Consider BP default=Y [Y=Yes, N=No]
  ConsiderTy VarChar(1) Consider Type default=Y [Y=Yes, N=No]
  EDocGenTyp VarChar(1) Electr. Doc. Generation Type default=D [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later, D=Use Defaults]
  ESeries Int(6) Electronic Series ->NNM4
  EDocNum nVarChar(20) Electronic Document Number
  ReopOriRdr VarChar(1) Reopen Origin. Order by Return default=N [Y=Yes, N=No]
  ReopManCls VarChar(1) Reop. Man. Closed/Canc. Orders default=N [Y=Yes, N=No]
  SeqCode Int(6) Target Doc. NF Sequence Code
  UseBaseSeq VarChar(1) Use Base Document NF Sequence default=N [Y=Yes, N=No]
  OnSeqCode VarChar(1) Missing NF Sequence default=N [N=Skip to Next Document, T=Use NF Sequence from Step 2]
  BPLId Int(11) Branch ->OBPL
  BlckFrOnly VarChar(1) Block Docs. with Zero Items default=N [Y=Yes, N=No]
  DocSubType nVarChar(2) Document Sub-Type default=-- [--=Bill of Supply, GA=GST Tax Invoice]
  EDocDflt VarChar(1) Apply El. Doc. Defaults default=Y [Y=Yes, N=No]
