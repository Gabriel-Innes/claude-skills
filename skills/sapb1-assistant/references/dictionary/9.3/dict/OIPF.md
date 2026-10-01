<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIPF - Landed Costs
Module: Inventory and Production | 64 columns | ObjType: 69
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM U: Series, Instance, DocNum
  SUPPLIER: CardCode
  AGENT: AgentNum, AgentCode
  CURRENCY: DocCur
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) Vendor Code ->OCRD
  SuppName nVarChar(100) Vendor Name
  AgentCode nVarChar(15) Subst. Code ->OCRD
  AgentName nVarChar(100) Subst. Name
  DocStatus VarChar(1) Document Status default=O [C=Closed, O=Open]
  AgentNum nVarChar(16) File Number
  Descr nVarChar(250) Remarks
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  DocCur nVarChar(3) Document Currency
  DocRate Num(19,6) Document Rate
  ExpCustom Num(19,6) Projected Customs
  ActCustom Num(19,6) Act. Import Duty
  Vat1 Num(19,6) Tax 2
  Vat2 Num(19,6) Tax 2
  BeforeVat Num(19,6) Total Before Tax
  DocTotal Num(19,6) Document Total
  CostSum Num(19,6) Total Costs
  DocTime Int(6) Generation Time
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  ExCustomFC Num(19,6) Projected Customs (FC)
  AcCustomFC Num(19,6) Act. Import Duty in FC
  Vat1FC Num(19,6) Tax 1 (FC)
  Vat2FC Num(19,6) Tax 2 (FC)
  BeforVatFC Num(19,6) Total Before Tax (FC)
  DocTotalFC Num(19,6) Document Total (FC)
  CostSumFC Num(19,6) Total Costs (FC)
  CloseDate Date(8) Closing Date
  Cost_Match Num(19,6) Expenses Diff. for Reconciliation
  C_Match_FC Num(19,6) Expenses Diff. for Recon. (FC)
  BillOfLad nVarChar(20) Bill of Lading No.
  TrnspCode Int(6) Delivery Category ->OSHP
  CostFactor Num(19,6) Expenses Factor
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  TaxDate Date(8) Document Date
  Series Int(11) Series
  JdtNum Int(11) Journal Number ->OJDT
  JdtMemo nVarChar(50) Transaction Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ObjType nVarChar(20) Object Type default=69 ->ADP1
  ExCustomSC Num(19,6) Projected Customs (SC)
  ActCustSC Num(19,6) Actual Customs (SC)
  TtlCostSC Num(19,6) Total Expenditure (SC)
  VersionNum nVarChar(11) Version Number
  OpenForLaC VarChar(1) Open For Landed Costs default=Y [Y=Yes, N=No]
  incCustom VarChar(1) Include Customs Expenses default=Y
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  BuildDesc nVarChar(50) Build Descriptor
  SupplCode nVarChar(254) Supplementary Code
  AtcEntry Int(11) Attachment Entry
  CustDate Date(8) Customs Date
  BPLId Int(11) Branch ->OBPL
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
