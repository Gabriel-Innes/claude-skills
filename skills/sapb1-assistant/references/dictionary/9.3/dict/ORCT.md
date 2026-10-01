<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ORCT - Incoming Payment
Module: Banking | 183 columns | ObjType: 24
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  NUM U: PIndicator, DocNum
  CARD: CardCode
  HANDWRITEN: Handwrtten
  CANCELED: Canceled
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=C [C=Customer, A=Account, S=Vendor, P=P.L.A, T=Tax, D=TDS]
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) Customer/Vendor Code
  CardName nVarChar(100) Customer/Vendor Name
  Address nVarChar(254) Address
  DdctPrcnt Num(19,6) Deduction Percent
  DdctSum Num(19,6) Total Deductions
  DdctSumFC Num(19,6) Total Deductions (FC)
  CashAcct nVarChar(15) Cash Account ->OACT
  CashSum Num(19,6) Cash Amount
  CashSumFC Num(19,6) Cash Amount (FC)
  CreditSum Num(19,6) Credit Amount
  CredSumFC Num(19,6) Credit Amount (FC)
  CheckAcct nVarChar(15) Current Account ->OACT
  CheckSum Num(19,6) Check Amount
  CheckSumFC Num(19,6) Check Amount (FC)
  TrsfrAcct nVarChar(15) Transfer Account ->OACT
  TrsfrSum Num(19,6) Transfer Amount
  TrsfrSumFC Num(19,6) Transfer Amount (FC)
  TrsfrDate Date(8) Transfer Date
  TrsfrRef nVarChar(27) Intended Purpose
  PayNoDoc VarChar(1) Non-Calculated Payment default=N [Y=Yes, N=No]
  NoDocSum Num(19,6) Non-Calculated Amount
  NoDocSumFC Num(19,6) Non-Calculated Amount (FC)
  DocCurr nVarChar(3) Document Currency ->OCRN
  DiffCurr VarChar(1) Enter in local currency default=N [N=No, Y=Yes]
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Price
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(8) Reference 2
  CounterRef nVarChar(8) Counter Reference
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  DocTime Int(6) Generation Time
  ShowAtCard VarChar(1) Display Customer Ref. No. default=N [Y=Yes, N=No]
  SpiltTrans VarChar(1) Split Transaction Journal default=N [Y=Yes, N=No]
  CreateTran VarChar(1) Create Journal Entry default=Y [Y=Yes, N=No]
  Flags Int(11) Flags default=0
  CntctCode Int(11) Contact Person ->OCPR
  DdctSumSy Num(19,6) System Deduction Amount
  CashSumSy Num(19,6) Cash Amount (SC)
  CredSumSy Num(19,6) System Credit Amount
  CheckSumSy Num(19,6) Check Amount (SC)
  TrsfrSumSy Num(19,6) Transfer Amount (SC)
  NoDocSumSy Num(19,6) Non-Invoiced System Amount
  DocTotalSy Num(19,6) Document Total (SC)
  ObjType nVarChar(20) Object Type default=24 [24=Incoming Payment] ->ADP1
  StornoRate Num(19,6) Cancellation Rate
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  ApplyVAT VarChar(1) Tax Definition default=N [Y=Yes, N=No]
  TaxDate Date(8) Document Date
  Series Int(11) Series ->NNM1
  confirmed VarChar(1) Approved default=N [Y=Yes, N=No]
  ShowJDT VarChar(1) Display Journal Entries default=N [Y=Yes, N=No]
  BankCode nVarChar(30) Bank Code for Bank Transfer
  BankAcct nVarChar(50) Account for Bank Transfer
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer, B=BSP]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatSum Num(19,6) Tax Amount
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  VatPrcnt Num(19,6) Tax %
  Dcount Num(19,6) Discount %
  DcntSum Num(19,6) Discount Amount
  DcntSumFC Num(19,6) Discount Amount (FC)
  DcntSumSy Num(19,6) Discount Amount (SC)
  SpltCredLn VarChar(1) Split Vendor Credit Row default=N [Y=Yes, N=No]
  PrjCode nVarChar(20) Project ->OPRJ
  PaymentRef nVarChar(27) Payment Reference No.
  Submitted VarChar(1) Submitted default=N [Y=Yes, N=No]
  Status VarChar(1) Created by Payment Run default=N [Y=Yes, N=No, C=BoE Canceled]
  PayMth nVarChar(15) Payment Method ->OPYM
  BankCountr nVarChar(3) Bank Country ->OCRY
  FreightSum Num(19,6) Freight Sum
  FreigtFC Num(19,6) Freight Sum (FC)
  FreigtSC Num(19,6) Freight Sum (SC)
  BoeAcc nVarChar(15) Boe Account ->OACT
  BoeNum Int(11) Bill of Exchange No.
  BoeSum Num(19,6) Bill of Exchange Amount
  BoeSumFc Num(19,6) Bill of Exchange Amount (FC)
  BoeSumSc Num(19,6) Bill of Exchange Amount (SC)
  BoeAgent nVarChar(32) Bill of Exchange Agent ->OAGP
  BoeStatus VarChar(1) Bill of Exchange Status
  WtCode nVarChar(4) WTax Code ->OWHT
  WtSum Num(19,6) WTax Amount
  WtSumFrgn Num(19,6) WTax Amount (FC)
  WtSumSys Num(19,6) WTax Amount (SC)
  WtAccount nVarChar(15) WTax Account ->OACT
  WtBaseAmnt Num(19,6) WTax Taxable Amount
  Proforma VarChar(1) Proforma default=N [Y=Yes, N=No]
  BoeAbs Int(11) Boe Key ->OBOE
  BpAct nVarChar(15) BP Account ->OACT
  BcgSum Num(19,6) Bank Charges Amount
  BcgSumFC Num(19,6) Bank Charges Amount (FC)
  BcgSumSy Num(19,6) Bank Charges Amount (SC)
  PIndicator nVarChar(10) Period Indicator ->OPID
  PaPriority VarChar(1) Payment Priority default=6 [1=, 2=, 3=, 4=, 5=, 6=]
  PayToCode nVarChar(50) Pay to
  IsPaytoBnk VarChar(1) Is Pay to Bank default=N [N=No, Y=Yes]
  PBnkCnt nVarChar(3) Pay to Bank Country ->OCRY
  PBnkCode nVarChar(30) Pay to Bank Code
  PBnkAccnt nVarChar(50) Pay to Bank Account No.
  PBnkBranch nVarChar(50) Pay to Bank Branch
  WizDunBlck VarChar(1) Wizard Dunning Block default=N [N=No, Y=Yes]
  WtBaseSum Num(19,6) WTax Base Sum
  WtBaseSumF Num(19,6) WTax Base Sum (FC)
  WtBaseSumS Num(19,6) WTax Base Sum (SC)
  UndOvDiff Num(19,6) Under/Overpayment Difference
  UndOvDiffS Num(19,6) Under/Overpayment Diff. (SC)
  BankActKey Int(11) Bank Account Internal ID ->DSC1
  VersionNum nVarChar(11) Version Number
  VatDate Date(8) VAT Date
  TransCode nVarChar(4) Transaction Code ->OTRC
  PaymType VarChar(1) Payment Type default=N [N=, E=Electronic, P=Mail, T=Telegraph, X=Express]
  TfrRealAmt Num(19,6) Transfer Real Amount
  CancelDate Date(8) Cancelation Date
  OpenBal Num(19,6) Open Balance Amount
  OpenBalFc Num(19,6) Open Balance Amount (FC)
  OpenBalSc Num(19,6) Open Balance Amount (SC)
  BcgTaxSum Num(19,6) Bank Charge Tax Amount
  BcgTaxSumF Num(19,6) Bank Charge Tax Amount(FC)
  BcgTaxSumS Num(19,6) Bank Charge Tax Amount(SC)
  TpwID Int(11) Tax Payment Wizard ID default=0
  ChallanNo nVarChar(32) Challan No.
  ChallanBak nVarChar(60) Challan Bank Name
  ChallanDat Date(8) Challan Received Date
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  BcgVatGrp nVarChar(8) Bank Charge Tax Group ->OVTG
  BcgVatPcnt Num(19,6) Bank Charge Tax %
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  BSRCode nVarChar(25) BSR Code
  LocCode Int(11) Location Code ->OLCT
  WTOnhldPst Num(19,6) WTax On Hold, Posted
  UserSign2 Int(6) Updating User ->OUSR
  BuildDesc nVarChar(50) Build Descriptor
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Residence Country, 5=Certificate of Fiscal Residence, 6=Other Document]
  OperatCode VarChar(1) Operation Code [A=Summary Invoices Entry, B=Summary Receipts Entry, C=Invoice with Several VAT Rates, D=Correction Invoice, E=Due VAT Pending Invoice Issuance, F=Expenses Incurred by Travel Agent for Customers, G=Special Regulation for VAT Group, H=Special Regulation for Gold Investment, I=Reverse Charge Procedure, J=Unsummarized Receipts, K=Identification of Error Transactions, N=Service Invoicing by Travel Agencies on Behalf of Third Parties, R=Business Office Rental, S=Subsidies, T=Incoming Payments for Industrial and Intellectual Property Rights, U=Insurance Transactions, V=Purchases from Travel Agencies, W=Transactions Subject to Production, Service and Import Taxes in Ceuta and Melilla, X=Transactions with Entrepreneurs Issuing Receipts for Agricultural Compensation]
  UndOvDiffF Num(19,6) Under/Overpayment Diff. (FC)
  MIEntry Int(11) MI Entry Include this Payment default=0
  FreeText1 nVarChar(100) Free Text 1
  FreeText2 nVarChar(100) Free Text 2
  FreeText3 nVarChar(100) Free Text 3
  ShowDocNo VarChar(1) Display Document No. default=Y [Y=Yes, N=No]
  TDSInterst Num(19,6) TDS Interest default=0
  TDSCharges Num(19,6) TDS Other Charges default=0
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  MIType nVarChar(20) MI Type Include this Payment [270=A/R Monthly Invoice, 140000014=A/P Monthly Invoice]
  SupplCode nVarChar(254) Supplementary Code
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number
  BPLCentPmt VarChar(1) Centralized Payment default=N [N=No, Y=Yes]
  DraftKey Int(11) Payment Draft Internal ID ->OPDF
  TDSFee Num(19,6) TDS Fee
  MinHeadCL Int(11) Minor Head of Challan [200=TDS Payable by Taxpayer, 400=TDS Regular Assessment (Raised by IT Dept)]
  SEPADate Date(8) Requested SEPA Pmt Date
  OwnerCode Int(11) Payment Owner ->OHEM
  AgrNo Int(11) Agreement No. ->OOAT
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS]
  DrNo nVarChar(32) Dr. No.
  PmntWTCert VarChar(1) Payment by WT Certificate Only default=N [Y=Yes, N=No]
  EnPBnkAcct Text(16) Encryption of Pay to Bank Acct
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
