<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OBTF - Journal Voucher Entry
Module: Finance | 113 columns | ObjType: 28
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BatchNum, TransId
  TRANS_TYPE: TransType, CreatedBy
  JDT_NUM: TransId
  BTF_STATUS: BtfStatus
Fields (name type(len) description [values] ->parent table):
  BatchNum Int(11) Journal Voucher No. ->OBTD
  TransId Int(11) Transaction Number
  BtfStatus VarChar(1) Status default=O [O=Open, C=Closed]
  TransType nVarChar(20) Origin default=-1 [16=Returns, 203=A/R Down Payment, 15=Delivery, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt PO, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 281=A/P Tax Invoice, 69=Landed Costs, 140000009=Outgoing Excise Invoice, 140000010=Incoming Excise Invoice, 254000065=Self Invoice, 254000066=Self Credit Memo, 10000079=TDS Adjustment, 24=Incoming Payment, 25=Deposit, 46=Vendor Payment, 57=Checks for Payment, 76=Postdated Deposit, 182=BoE Transaction, -2=Opening Balance, -3=Closing Balance, 321=Internal Reconciliation, 10000046=Data Archive, 30=Journal Entry, 58=Inventory List, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, 68=Work Instructions, 162=Inventory Valuation, 202=Production Order, 1470000049=Fixed Asset Capitalization, 1470000060=Fixed Asset Capitalization Credit Memo, 1470000094=Fixed Asset Retirement, 1470000075=Fixed Asset Manual Depreciation, 1470000090=Fixed Asset Transfer, 1470000085=Fixed Asset Revaluation, -1=All Transactions, 310000001=Inventory Opening Balance, 10000071=Inventory Posting, 254000061=Input Service Distribution Invoice, 254000062=Input Service Distribution Recipient Invoice, 254000063=Input Service Distribution Credit Memo, 254000064=Input Service Distribution Recipient Credit Memo, -4=Adj. for Manual Ext. Reconciliation]
  BaseRef nVarChar(11) Origin No.
  RefDate Date(8) Posting Date
  Memo nVarChar(254) Remarks
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  CreatedBy Int(11) Origin
  LocTotal Num(19,6) Total in Local Currency
  FcTotal Num(19,6) Total in Foreign Currency
  SysTotal Num(19,6) Total in System Currency
  TransCode nVarChar(4) Transaction Code ->OTRC
  OrignCurr nVarChar(3) Original Currency ->OCRN
  TransRate Num(19,6) Transaction Rate
  BtfLine Int(11) Row in Voucher
  TransCurr nVarChar(3) Transaction Currency
  Project nVarChar(20) Project Code ->OPRJ
  DueDate Date(8) Value Date
  TaxDate Date(8) Tax Date
  PCAddition VarChar(1) PC Addition default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UpdateDate Date(8) Update Date
  CreateDate Date(8) Recording Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  RefndRprt VarChar(1) Repayment Report default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  Indicator nVarChar(2) Indicator Code ->OIDC
  AdjTran VarChar(1) Adjusting Transaction default=N [Y=Yes, N=No]
  RevSource VarChar(1) Revaluation Source default=N [F=FC, S=System, N=No]
  StornoDate Date(8) Reversal Date
  StornoToTr Int(11) Reverse Transaction
  AutoStorno VarChar(1) Use Auto-Reverse default=N [Y=Yes, N=No]
  Corisptivi VarChar(1) Transaction Values default=N [Y=Yes, N=No]
  VatDate Date(8) VAT Date
  StampTax VarChar(1) Stamp Tax default=N [Y=Yes, N=No]
  Series Int(11) Series default=0
  Number Int(11) Number
  AutoVAT VarChar(1) Automatic Tax default=N [Y=Yes, N=No]
  DocSeries Int(11) Document Series
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  CreateTime Int(6) Generation Time
  BlockDunn VarChar(1) Block Dunning Letter default=N [N=No, Y=Yes]
  ReportEU VarChar(1) Include in EU Report default=N [Y=VAT, N=No]
  Report347 VarChar(1) Include in 347 Report default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  DocType nVarChar(60) Transact. Type ->OJET
  AttNum Int(11) Number of Attachments default=0
  GenRegNo VarChar(1) Generate Reg. No. or Not default=N [Y=Yes, N=No]
  RG23APart2 Int(11) RG23A Part2 No
  RG23CPart2 Int(11) RG23C Part2 No
  MatType Int(11) Material Type
  Creator nVarChar(155) Creator Name
  Approver nVarChar(155) Approver Name
  Location Int(11) Loc. ->OLCT
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  AutoWT VarChar(1) Automatic WTax default=N [Y=Yes, N=No]
  WTSum Num(19,6) WTax Amount
  WTSumSC Num(19,6) WTax Amount (SC)
  WTSumFC Num(19,6) WTax Amount (FC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedS Num(19,6) Applied WTax (SC)
  WTAppliedF Num(19,6) Applied WTax (FC)
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseVtAt Num(19,6) WTax Base VAT Amount
  BaseVtAtSC Num(19,6) WTax Base VAT Amount (SC)
  BaseVtAtFC Num(19,6) WTax Base VAT Amount (FC)
  VersionNum nVarChar(13) Version Number
  BaseTrans Int(11) Base Transaction Number
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Country/Region of Residence, 5=Certificate of Fiscal Residence, 6=Other Document]
  OperatCode VarChar(1) Operation Code [A=Summary Invoices Entry, B=Summary Receipts Entry, C=Invoice with Several VAT Rates, D=Correction Invoice, E=Due VAT Pending Invoice Issuance, F=Expenses Incurred by Travel Agent for Customers, G=Special Regulation for VAT Group, H=Special Regulation for Gold Investment, I=Reverse Charge Procedure, J=Unsummarized Receipts, K=Identification of Error Transactions, X=Transactions with Entrepreneurs Issuing Receipts for Agricultural Compensation, N=Service Invoicing by Travel Agencies on Behalf of Third Parties, R=Business Office Rental, S=Subsidies, T=Incoming Payments for Industrial and Intellectual Property Rights, U=Insurance Transactions, V=Purchases from Travel Agencies, W=Transactions Subject to Production, Service, and Import Taxes in Ceuta and Melilla]
  Ref3 nVarChar(100) Reference 3
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  SupplCode nVarChar(254) Supplementary Code
  SPSrcType Int(11) Service Posting Source Type
  SPSrcID Int(11) Service Posting Source ID
  SPSrcDLN Int(11) Service Post. Source Delivery
  DeferedTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  AgrNo Int(11) Blanket Agreement Number ->OOAT
  SeqNum Int(11) Sequence Number
  ECDPosTyp VarChar(1) ECD Posting Type default=N [N=Normal, E=Statement]
  RptPeriod nVarChar(5) Reporting Period
  RptMonth Date(8) Reporting Month
  ExTransId Int(11) Exposed Transaction ID
  PrlLinked VarChar(1) Is JE linked by MX Payroll default=N [Y=Yes, N=No]
  PTICode nVarChar(5) POI Code
  Letter VarChar(1) Letter
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  IsCoEntry VarChar(1) Cost Center Transfer form default=N [Y=Yes, N=No]
  SAPPassprt Text(16) Extended SAP Passport
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachment
  EBookable VarChar(1) E-Books Enabled default=N [N=No, Y=Yes]
  DataVers Int(11) Data Version default=1
