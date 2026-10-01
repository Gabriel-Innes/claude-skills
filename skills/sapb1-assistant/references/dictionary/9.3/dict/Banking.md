<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->

# ABO1 - External Bank Operation Code - Rows - Log
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBOC
  ExOpCode nVarChar(40) External Bank Operation Code
  OPDscrpt nVarChar(40) Operation Description
  InOpCode Int(11) Internal Bank Operation Code ->OBTC
  LogInstanc Int(11) Log Instance default=0
  LineId Int(6) Row

# ABOC - External Bank Operation Code - Log
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  OpCodeCat nVarChar(30) Operation Code Category
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

# ABOE - Bill of Exchange for Payment - History
Module: Banking | 92 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, BoeKey
  VPM_NUM: PmntNum
  TRANS_NUM: TransNum
  DPS_NUM: DepositNum
  BOE_NUM U: LogInstanc, BoeType, BoeNum
Fields (name type(len) description [values] ->parent table):
  BoeKey Int(11) Bill of Exchange Key
  BoeNum Int(11) Bill of Exchange No.
  BoeStatus VarChar(1) Bill of Exchange Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, L=Closed, F=Failed, V=BoE to Vendor]
  BoeType VarChar(1) Bill of Exchange Type default=I [I=Incoming, O=Outgoing]
  DpsBankCod nVarChar(30) Deposit Bank Code
  DpsCntrCod nVarChar(3) Deposit Country Code ->OCRY
  DueDate Date(8) Bill of Exchange Due Date
  DpstAcct nVarChar(50) Bank Account No.
  DpstBranch nVarChar(50) Branch for Payments
  Details nVarChar(50) Details
  TransRef nVarChar(8) Journal Entry Reference
  PmntDate Date(8) Payment Date
  PmntNum Int(11) Payment No.
  BoeSum Num(19,6) Bill of Exchange Amount
  BoeSumSC Num(19,6) Bill of Exchange Amount (SC)
  BoeSumFC Num(19,6) Bill of Exchange Amount (FC)
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  BoeAcct nVarChar(15) BP Account Code ->OACT
  Currency nVarChar(3) Bill of Exchange Currency ->OCRN
  Printed VarChar(1) Printed default=N [N=No, Y=Yes]
  TotalWords nVarChar(100) Total in Words
  Signature nVarChar(155) Signature
  TransNum Int(11) Transaction No. default=0
  LinesSum Num(19,6) Row Totals
  DdctPrcnt Num(19,6) % Withholding Tax Ded.
  Address nVarChar(254) Address
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  VatTotal Num(19,6) Total Tax
  VatTotalSC Num(19,6) Total Tax (SC)
  VatTotalFC Num(19,6) Total Tax (FC)
  VatCalcult VarChar(1) Calculate Tax default=N [Y=Yes, N=No]
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SumRfndCln Num(19,6) Deduction Refund Amount
  UserSign Int(6) User Signature ->OUSR
  PrintedBy Int(6) Printed By
  Transfered VarChar(1) Transferred to next year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  BPBankCod nVarChar(30) BP Bank Code
  BPBankNam nVarChar(250) BP Bank Name
  BPBankAct nVarChar(50) BP Bank Account
  BPBankBrnc nVarChar(50) BP Bank Branch
  BPBankCtr nVarChar(3) BP Bank Country ->OCRY
  RefNum nVarChar(254) Reference No.
  IsReconcld VarChar(1) Reconciled default=N [N=No, Y=Yes]
  Comments nVarChar(254) Remarks
  PayMethCod nVarChar(15) Payment Method Code ->OPYM
  DepositNum Int(11) Deposit Number
  PymMethNam nVarChar(100) Payment Method Name
  DeductSum Num(19,6) Deduction Amount
  ControlKey nVarChar(2) Control Key
  AgentCode nVarChar(32) Agent Code ->OAGP
  ReconcilNu Int(11) External Reconciliation No.
  DepositTyp VarChar(1) Deposit Type [C=Collection, D=Discounted]
  CreatStatu VarChar(1) Creation Status [G=Generated, S=Sent]
  Ref2 nVarChar(254) Reference 2
  PayEngSt1 VarChar(1) Payment Engine Status 1
  PayEngSt2 VarChar(1) Payment Engine Status 2
  PayEngSt3 nVarChar(3) Payment Engine Status 3
  StampTax nVarChar(8) Stamp Tax Code ->OVTG
  StmpTxAmnt Num(19,6) Stamp Tax Amount
  DpsActKey Int(11) Bank Account Internal ID ->DSC1
  OutBnkKey Int(11) Outgoing Bank Account Key ->DSC1
  Portfolio nVarChar(8) Portfolio ->OPFT
  VndCodeCEE nVarChar(15) Vendor Code ->OCRD
  VndNameCEE nVarChar(100) Vendor Name
  OurNum Int(11) Our Number
  BarcodeNum nVarChar(120) Bar Code Number
  BarcodeRep nVarChar(100) Bar Code Representation
  OurNumChk VarChar(1) Our Number Check Digit
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  LPgFolioN Int(11) Folio No. for Last Page in Doc.
  UserSign2 Int(6) Updating User ->OUSR
  IntrstAmnt Num(19,6) Interest Amount
  DiscAmnt Num(19,6) Discount Amount
  FineAmnt Num(19,6) Fine Amount
  IntrstDate Date(8) BoE Interest Date
  DiscDate Date(8) BoE Discount Date
  FineDate Date(8) BoE Fine Date
  PostType VarChar(1) Posting Type [D=Default, A=Alternative]
  IOFAmnt Num(19,6) IOF Amount
  ServFeeAm Num(19,6) Service Fee Amount
  OtherExAm Num(19,6) Other Expenses Amount
  OtherInAm Num(19,6) Other Incomes Amount
  BPLId Int(11) Branch ->OBPL
  EnBPBnkAct Text(16) Encryption of BP Bank Account
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# ABT1 - Internal Bank Operation Codes - Accounts - Log
Module: Banking | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number default=0
  LineId Int(6) Row
  GLAct nVarChar(15) G/L Account ->OACT
  Project nVarChar(20) Project ->OPRJ
  PrftCenter nVarChar(8) Distribution Rule ->OOCR
  VatCode nVarChar(8) VAT Code ->OVTG
  LogInstanc Int(11) Log Instance default=0
  PrftCent2 nVarChar(8) Distribution Rule2 ->OOCR
  PrftCent3 nVarChar(8) Distribution Rule3 ->OOCR
  PrftCent4 nVarChar(8) Distribution Rule4 ->OOCR
  PrftCent5 nVarChar(8) Distribution Rule5 ->OOCR

# ABTC - Internal Bank Operation Codes - Log
Module: Banking | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number default=0
  InOpCode nVarChar(15) Internal Bank Operation Code Name
  PstTrans VarChar(1) Posting Transaction default=1 [1=Incoming Bank Transfer, 2=Outgoing Bank Transfer, 3=Incoming Bill of Exchange, 4=Outgoing Bill of Exchange, 5=Outgoing Checks, 6=Deposit]
  BPorAct VarChar(1) BP or Account default=C [C=BP, A=Account]
  PstMethod VarChar(1) BP Posting Method default=1 [0=, 1=Business Partner from/to Bank Account, 2=Bank Interim Account or Bank Account, 3=External Reconciliation]
  ActFee nVarChar(15) Account Fee ->OACT
  ProjFee nVarChar(20) Project Fee ->OPRJ
  PrftCntFee nVarChar(8) Fee Distribution Rule ->OOCR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  Descript nVarChar(40) Operation Description
  PrftCntFe2 nVarChar(8) Fee Distribution Rule2 ->OOCR
  PrftCntFe3 nVarChar(8) Fee Distribution Rule3 ->OOCR
  PrftCntFe4 nVarChar(8) Fee Distribution Rule4 ->OOCR
  PrftCntFe5 nVarChar(8) Fee Distribution Rule5 ->OOCR
  UserSign2 Int(6) Updating User ->OUSR

# ACH1 - Checks for Payment - Rows - History
Module: Banking | 22 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineId, CheckKey
Fields (name type(len) description [values] ->parent table):
  CheckKey Int(11) SBO Internal Key ->OCHO
  LineId Int(11) Row Number
  LineDitail nVarChar(40) Row Details
  LineMoney Num(19,6) Row Total
  LineCurr nVarChar(3) Row Currency
  LineAcct nVarChar(15) Row G/L Acct
  Line_A_C VarChar(1) G/L Acct/BP Code default=0
  Code nVarChar(8) Tax Definition ->OVTG
  CredAcct nVarChar(15) Credited Account ->OACT
  TotalLine Num(19,6) Row Total
  VatPercent Num(19,6) Tax %:
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=57 ->ADP1
  LineMnyLC Num(19,6) Row Total (LC)
  LineMnySC Num(19,6) Row Total (SC)
  LineMnyFC Num(19,6) Row Total (FC)
  TotLineLC Num(19,6) Row Total (LC)
  TotLineSC Num(19,6) Row Total (SC)
  TotLineFC Num(19,6) Row Total (FC)
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History

# ACHO - Checks for Payment - History
Module: Banking | 56 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, CheckKey
  VPM_NUM: PmntNum
  TRANS_NUM: TransNum
Fields (name type(len) description [values] ->parent table):
  CheckKey Int(11) Check Key
  CheckNum Int(11) Check Number
  BankNum nVarChar(30) Bank Code
  Branch nVarChar(50) Branch
  BankName nVarChar(250) Bank Name
  CheckDate Date(8) Check Date
  DpstAcct nVarChar(50) Bank Account Number
  DpstBranch Int(6) Branch for Payments
  AcctNum nVarChar(50) Account Number
  Details nVarChar(50) Details
  TransRef nVarChar(11) Journal Entry Reference
  PmntDate Date(8) Payment Date
  PmntNum Int(11) Payment No. default=0 ->OVPM
  CheckSum Num(19,6) Check Amount
  Trnsfrable VarChar(1) Negotiable default=N [N=No, Y=Yes]
  VendorCode nVarChar(15) Vendor Code
  Currency nVarChar(3) Check Currency
  Canceled VarChar(1) Canceled default=N [N=No, Y=Yes]
  CardOrAcct VarChar(1) G/L Acct/BP Code default=C [C=BP, A=Account]
  Printed VarChar(1) Printed default=N [N=No, Y=Yes]
  VendorName nVarChar(100) Vendor Name
  TotalWords nVarChar(254) Total in Words
  Signature nVarChar(30) Signature
  CheckAcct nVarChar(15) Customer Account Code
  TransNum Int(11) Transaction Number default=0 ->OJDT
  LinesSum Num(19,6) Row Totals
  Deduction Num(19,6) Deduction Amount
  DdctPrcnt Num(19,6) Withholding Tax Ded. %
  Address nVarChar(254) Address
  CreateJdt VarChar(1) Create Journal Entry default=Y [N=No, Y=Yes]
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  VatTotal Num(19,6) Total Tax
  VatCalcult VarChar(1) Calculate Tax default=N [Y=Yes, N=No]
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SumRfndCln Num(19,6) Deduction Refund Amount
  UserSign Int(6) User Signature ->OUSR
  PrintedBy Int(6) Printed By
  Transfered VarChar(1) Transferred to Next Year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=57 ->ADP1
  CountryCod nVarChar(3) Country Code ->OCRY
  AddrName nVarChar(50) Address Name
  PrnConfrm VarChar(1) Confirm Printing default=N [N=No, Y=Yes]
  BnkActKey Int(11) Bank Account Internal ID ->DSC1
  CancelDate Date(8) Cancelation Date
  ManualChk VarChar(1) Manual Check default=N [N=No, Y=Yes]
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) Branch Reg. No.
  Endorse VarChar(1) Endorse default=N [N=No, Y=Yes]
  EndorsChNo Int(11) Endorsable Check No. ->OCHH
  UserSign2 Int(6) Updating User - History ->OUSR
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# ADS1 - House Bank Accounts
Module: Banking | 79 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
Fields (name type(len) description [values] ->parent table):
  BankCode nVarChar(30) Bank Code
  Account nVarChar(50) Acct No.
  Branch nVarChar(50) Branch
  NextCheck Int(11) Next Check No.
  GLAccount nVarChar(15) G/L Account ->OACT
  Free VarChar(1) Free
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  Country nVarChar(3) Country ->OCRY
  State nVarChar(3) State ->OCST
  BISR VarChar(1) BISR default=N [Y=Yes, N=No]
  ControlKey nVarChar(2) Control Key
  UsrNumber1 nVarChar(25) User No. 1
  UsrNumber2 nVarChar(25) User No. 2
  UsrNumber3 nVarChar(25) User No. 3
  UsrNumber4 nVarChar(25) User No. 4
  IBAN nVarChar(50) IBAN
  DscountBOE nVarChar(15) Debt of Discounted BoE ->OACT
  TolrnceDay Int(11) Tolerance Days
  MinAmntBOE Num(19,6) Min. Amount of Bill of Exchange
  MaxAmntBOE Num(19,6) Max. Amount of Bill of Exchange
  DscntLimit Num(19,6) Discount Limit
  DaysInAdva Int(11) Days in Advance
  BankCollec nVarChar(15) Bank on Collection ->OACT
  BankDiscou nVarChar(15) Bank on Discounted ->OACT
  BranchName nVarChar(50) Branch Name
  AliasName nVarChar(50) Alias Name
  CompanyCod nVarChar(10) Company Code
  AcctType VarChar(1) Account Type
  Building Text(16) Building/Floor/Room
  BIK nVarChar(15) BIK
  AcctName nVarChar(250) Bank Account Name
  CorresAcct nVarChar(30) Correspondent Account
  Phone nVarChar(25) Telephone No.
  Fax nVarChar(25) Fax
  GLIntriAct nVarChar(15) G/L Interim Account ->OACT
  ChkPaper VarChar(1) Paper Type default=D [B=Blank Paper, S=Overflow Prenumbered Check Stock, P=Overflow Blank Paper, D=Default]
  MaxChkLine Int(6) Maximum Lines
  TmpltName nVarChar(8) Template Name
  AbsEntry Int(11) Internal Number
  BankKey Int(11) Bank ID ->ODSC
  LockChk VarChar(1) Lock Checks Printing default=N [Y=Yes, N=No]
  OurNum Int(11) Our Number in Next Boleto
  AgreeNum nVarChar(10) Agreement Number
  AccountChk VarChar(1) Account Check Digit
  ISRType Int(6) ISR Type default=2 [1=ISR, 2=BISR, 3=ISR+, 4=BISR+]
  ISRBillerI nVarChar(9) ISR Biller ID
  CustIdNum nVarChar(10) Customer ID Number default=0
  InSeri Int(11) Incoming Payment Series default=-1 ->NNM1
  OutSeri Int(11) Outgoing Payment Series default=-1 ->NNM1
  JDTSeri Int(11) Journal Entry Series default=-1 ->NNM1
  FilePlug nVarChar(50) Import File Name
  ImpStmt VarChar(1) Imported Bank Statement default=N [Y=Create New - From File, N=Create New - Manually]
  PreNumber VarChar(1) Prenumbered Check default=Y [Y=Yes, N=No]
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UsrLogSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  SwiftNum nVarChar(50) BIC/SWIFT Code
  FineAcct nVarChar(15) Fine Account ->OACT
  IntrstAcct nVarChar(15) Interest Account ->OACT
  DscntAcct nVarChar(15) Discount Account ->OACT
  SvcFeeAcct nVarChar(15) Service Fee Account ->OACT
  BranchChk nVarChar(5) Branch Check Digit
  RetFile nVarChar(50) Retorno File Format
  IOFTaxAcct nVarChar(15) IOF Tax Account
  OthExpAcct nVarChar(15) Other Expenses Account ->OACT
  OthIncAcct nVarChar(15) Other Incomes Account ->OACT
  CollCode nVarChar(50) Collection Code
  FileSeqNNo Int(11) File Sequence Next Number
  RefCoLevel VarChar(1) Reference Control Level default=H [S=Soft Control, H=Hard Control, V=Hard Control with variable length, F=Hard Control with fixed length]
  RefFixLen1 Int(6) Reference fixed length 1
  RefFixLen2 Int(6) Reference fixed length 2
  Currency nVarChar(3) Currency ->OCRN

# ARC1 - Incoming Payment - Checks - History
Module: Banking | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjType, LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  LineID Int(11) Row Number
  DueDate Date(8) Check Date
  CheckNum Int(11) Check Number
  BankCode nVarChar(30) Account Number default=-1
  Branch nVarChar(50) Branch Number
  AcctNum nVarChar(50) Account Number
  Details nVarChar(254) Details
  Trnsfrable VarChar(1) Negotiable default=N [Y=Yes, N=No]
  CheckSum Num(19,6) Check Amount
  Currency nVarChar(3) Check Currency
  Flags Int(11) Flags default=0 ->OCRN
  ObjType nVarChar(20) ObjType ->ADP1
  LogInstanc Int(11) Log Instance default=0
  CountryCod nVarChar(3) Country Code ->OCRY
  CheckAct nVarChar(15) Check Account ->OACT
  CheckAbs Int(11) Check ID Entry ->OCHO
  BnkActKey Int(11) Bank Account Internal ID ->DSC1
  ManualChk VarChar(1) Manual Check default=N [N=No, Y=Yes]
  FiscalID nVarChar(100) Fiscal ID
  OrigIssdBy nVarChar(254) Orginally Issued By
  Endorse VarChar(1) Endorse default=N [Y=Yes, N=No]
  EndorsChNo Int(11) Endorsable Check No. ->OCHH
  EnAcctNum Text(16) Encryption of Account Number
  EncryptIV nVarChar(100) Encrypt IV

# ARC2 - Incoming Payment - Invoices - History
Module: Banking | 63 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjType, InvoiceId, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  InvoiceId Int(11) Sequence No.
  DocEntry Int(11) Invoice Key
  SumApplied Num(19,6) Paid (LC)
  AppliedFC Num(19,6) Paid (FC)
  AppliedSys Num(19,6) Paid (SC)
  InvType nVarChar(20) Document Type default=13 [203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 25=Deposit, 46=Payment Advice, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, -1=All Transactions, 163=A/P Correction Invoice, 165=A/R Correction Invoice, 0=]
  DocRate Num(19,6) Document Rate
  Flags Int(11) Flags default=0
  IntrsStat VarChar(1) Interest Letter Status default=U [U=Not Sent, S=Sent, C=Closed]
  DocLine Int(11) Row Key default=0
  vatApplied Num(19,6) Tax Definition
  vatAppldFC Num(19,6) Tax Paid (FC)
  vatAppldSy Num(19,6) Tax Paid (SC)
  selfInv VarChar(1) Auto. Invoice default=N [N=No, Y=Yes]
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  Dcount Num(19,6) Discount
  DcntSum Num(19,6) Discount Amount
  DcntSumFC Num(19,6) Discount Amount (FC)
  DcntSumSy Num(19,6) Discount Amount (SC)
  BfDcntSum Num(19,6) Amount Bef. Discount
  BfDcntSumF Num(19,6) Amount Bef. Discount (FC)
  BfDcntSumS Num(19,6) Amount Bef. Discount (SC)
  BfNetDcnt Num(19,6) Net Amount Bef. Discount
  BfNetDcntF Num(19,6) Net Amount Bef. Discount (FC)
  BfNetDcntS Num(19,6) Net Amount Bef. Discount (SC)
  PaidSum Num(19,6) Amount Paid (LC)
  ExpAppld Num(19,6) Freight applied
  ExpAppldFC Num(19,6) Freight applied FC
  ExpAppldSC Num(19,6) Freight applied SC
  Rounddiff Num(19,6) Rounding Diff.
  RounddifFc Num(19,6) Rounding Diff. (FC)
  RounddifSc Num(19,6) Rounding Diff. (SC)
  InstId Int(6) Installment ID default=1
  WtAppld Num(19,6) Applied WTax
  WtAppldFC Num(19,6) Applied WT (FC)
  WtAppldSC Num(19,6) Applied WTax (SC)
  LinkDate Date(8) Link Date
  AmtDifPst Date(8) Amount Diffs. Posting Date
  PaidDpm VarChar(1) Paid Down Payment default=N [N=No, Y=Yes]
  DpmPosted VarChar(1) Link Date
  ExpVatSum Num(19,6) VAT on Expenses Sum
  ExpVatSumF Num(19,6) VAT on Expenses Sum (FC)
  ExpVatSumS Num(19,6) VAT on Expenses Sum (SC)
  IsRateDiff VarChar(1) Is Exchange Rate default=N
  WtInvCatS Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSF Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSS Num(19,6) Withholding Tax Invoice Categ.
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  DocTransId Int(11) Trans. ID of Paid Document ->OJDT
  MIEntry Int(11) MI Entry Include this Payment default=0
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  IsSelected VarChar(1) Is Record Selected default=N [Y=Yes, N=No]
  WTOnHold Num(19,6) Withholding Tax On Hold
  WTOnhldPst Num(19,6) Withholding Tax Posted
  baseAbs Int(11) Base Document Number
  MIType nVarChar(20) MI Type Include this Payment [270=A/R Monthly Invoice, 140000014=A/P Monthly Invoice]
  DocSubType nVarChar(2) Document Subtype default=--
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]

# ARC3 - Credit Vouchers History
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjType, LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document No. ->OVPM
  LineID Int(11) Row No.
  CreditCard Int(6) Credit Card default=-1 ->OCRC
  CreditAcct nVarChar(15) Credit Amount ->OACT
  CrCardNum nVarChar(64) Credit Card No.
  CardValid Date(8) Credit Card Valid Until
  VoucherNum nVarChar(20) Credit Voucher No.
  OwnerIdNum nVarChar(15) ID Number
  OwnerPhone nVarChar(20) Telephone
  CrTypeCode Int(6) Payment Method Code default=-1 ->OCRP
  NumOfPmnts Int(6) No. of Payments default=1
  FirstDue Date(8) 1st Payment Date
  FirstSum Num(19,6) First Partial Payment
  AddPmntSum Num(19,6) Each Additional Payment
  CreditSum Num(19,6) Credit Amount
  CreditCur nVarChar(3) Credit Voucher Currency ->OCRN
  CreditRate Num(19,6) Credit Voucher Rate
  ConfNum nVarChar(20) Confirmation No.
  CreditType VarChar(1) Credit Transaction Type default=S [U=Telephone Transaction, S=Regular, I=Internet Transaction]
  CredPmnts Int(6) No. of Credit Payments default=1
  PlCrdStat nVarChar(4) Pelecard Debit Status default=-1
  MagnetStr nVarChar(40) Magnetic Stripe Content
  SpiltCred VarChar(1) Split Credit Voucher Payment default=N [Y=Yes, N=No]
  ConsolNum Int(11) Vendor Credit Code default=-1 ->OPVL
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

# ARC4 - Incoming Payment - Account List - History
Module: Banking | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjType, LineId, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineId Int(11) Row Number
  AcctCode nVarChar(15) Account ->OACT
  SumApplied Num(19,6) Paid
  AppliedFC Num(19,6) Paid (FC)
  AppliedSys Num(19,6) Paid (SC)
  Descrip nVarChar(250) Details
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax %
  AcctName nVarChar(100) Account Name
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  GrossAmnt Num(19,6) Gross Amount
  GrssAmntFC Num(19,6) Gross Amount (FC)
  GrssAmntSC Num(19,6) Gross Amount (SC)
  AmntBase VarChar(1) Base Amount [E=Exclude Tax, I=Include Tax]
  VatAmnt Num(19,6) VAT Amount
  VatAmntFC Num(19,6) VAT Amount (FC)
  VatAmntSC Num(19,6) VAT Amount (SC)
  UserChaVat VarChar(1) User Changed VAT default=N [N=No, Y=Yes]
  TaxTypeID Int(11) Tax Type Component ID ->OSTT
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Section Int(11) Section ->OSEC
  AsseType VarChar(1) Assessee Type [C=Company, P=Others]
  LocCode Int(11) Location Code ->OLCT
  MatType Int(11) Material Type default=0
  EquVatPer Num(19,6) Equalization Tax Rate
  EquVatSum Num(19,6) Equalization VAT Amount
  EquVatSumF Num(19,6) Equalization VAT Amount (FC)
  EquVatSumS Num(19,6) Equalization VAT Amount (SC)

# ARC5 - Reciept log vat adjustment-History
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjType, LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document No. - History ->ORCT
  InvEntry Int(11) Invoice Key - History ->OINV
  LineNum Int(11) Row Number - History
  ObjType nVarChar(20) Object Type - History ->ADP1
  LogInstanc Int(11) Log Instance - History default=0
  VatGroup nVarChar(8) Tax Group - History ->OVTG
  VatPrcnt Num(19,6) Tax % - History
  VatSum Num(19,6) Tax Amount - History
  BaseSum Num(19,6) Base Amount - History
  NoDedSum Num(19,6) Non-Deductible Amount
  BaseSumFc Num(19,6) Base Amount (FC)
  VatSumFc Num(19,6) Tax Amount (FC)
  NoDedSumFc Num(19,6) Non-Deductible Amount (FC)
  BaseSumSc Num(19,6) Base Amount (SC)
  NoDedSumSc Num(19,6) Non-Deductible Amount (SC)
  VatSumSc Num(19,6) VAT Amount (SC)
  CashDiscAc nVarChar(15) Cash Discount Account
  BaseObjArr Int(6) Base Object Array Number default=1
  BaseObj Int(11) Base Object default=13
  InstlmntId Int(6) Installment ID default=0
  GroupNum Int(11) Group Number default=0
  LineSeq Int(11) Row Sequence default=-1
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)

# ARC6 - Incoming Payments - WTax Rows - History
Module: Banking | 77 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, Line, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  InvoiceId Int(11) Invoice Key
  WTCode nVarChar(4) WTax Code ->OWHT
  PymMean VarChar(1) Payment Means default=C [C=Cash, K=Checks, R=Credit Card, T=Bank Transfer, B=Bill of Exchange]
  DueDate Date(8) Due Date
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (SC)
  WTSumSC Num(19,6) WTax Amount (FC)
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  PymAmount Num(19,6) Payment Amount
  PymAmounF Num(19,6) Payment Amount (FC)
  PymAmounS Num(19,6) Payment Amount (SC)
  Line Int(11) Internal Number
  LogInstanc Int(11) Log Instance - History default=0
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  WTPosted Num(19,6) WT Posted
  WTPostedFC Num(19,6) WT Posted FC
  WTPostedSC Num(19,6) WT Posted SC
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  DepositNum Int(11) Deposit Number ->OVPM
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtC Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtC Num(19,6) Cess GST Base Amount (FC)
  UtgstAmt Num(19,6) UTGST Amount
  UtgstAmtSC Num(19,6) UTGST Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Amount (FC)
  CsgstAmt Num(19,6) Cess GST Amount
  CsgstAmtSC Num(19,6) Cess GST Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Amount (FC)

# ARC7 - Incoming Payments - Tax Amount per Document - History
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjectType, LogInstanc, LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineSeq Int(11) Row Sequence
  InvoiceSeq Int(11) Invoice Sequence Number
  ValueDate Date(8) Due Date
  Inv4Seq Int(11) INV4 Sequence Number
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# ARC8 - Incoming Payment - TDS Entries - History
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjectType, LineNum, DocNum
  INVOICE: DocLine, DocEntry, InvType
  PAYMENT: PaidLine, PaidEntry
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineNum Int(11) Row Number
  InvType nVarChar(20) Invoice Category
  DocEntry Int(11) Invoice Internal ID
  DocLine Int(11) Invoice Row Number
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  PaidEntry Int(11) Payment Internal ID
  PaidLine Int(11) Payment Row Number

# ARCT - Incoming Payment - History
Module: Banking | 183 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, LogInstanc, DocEntry
  NUM U: PIndicator, ObjType, LogInstanc, DocNum
  CARD: CardCode
  HANDWRITEN: Handwrtten
  CANCELED: Canceled
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=C [C=Customer, A=Account, S=Vendor, P=P.L.A, D=Yes, T=TDS]
  Canceled VarChar(1) Canceled default=N [Y=No, N=Yes]
  Handwrtten VarChar(1) Manual Numbering default=N [Y=No, N=Copy]
  Printed VarChar(1) Printed default=N [Y=Original, N=Yes]
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Due Date
  CardCode nVarChar(15) BP Code
  CardName nVarChar(100) BP Name
  Address nVarChar(254) Address
  DdctPrcnt Num(19,6) Deduction %
  DdctSum Num(19,6) Total Deductions
  DdctSumFC Num(19,6) Total Deductions (FC)
  CashAcct nVarChar(15) Cash Account ->OACT
  CashSum Num(19,6) Cash Amount
  CashSumFC Num(19,6) Cash Amount (FC)
  CreditSum Num(19,6) Credit Amount
  CredSumFC Num(19,6) Credit Amount (FC)
  CheckAcct nVarChar(15) Cash Account ->OACT
  CheckSum Num(19,6) Check Amount
  CheckSumFC Num(19,6) Check Amount (FC)
  TrsfrAcct nVarChar(15) Bank Transfer Account ->OACT
  TrsfrSum Num(19,6) Bank Transfer Amount
  TrsfrSumFC Num(19,6) Bank Transfer Amount (FC)
  TrsfrDate Date(8) Bank Transfer Date
  TrsfrRef nVarChar(27) Intended Purpose
  PayNoDoc VarChar(1) Non-Calculated Payment default=N [Y=No, N=No]
  NoDocSum Num(19,6) Non-Calculated Amount
  NoDocSumFC Num(19,6) Non-Calculated Amount (FC)
  DocCurr nVarChar(3) Document Currency ->OCRN
  DiffCurr VarChar(1) Entered in LC default=N [N=Yes, Y=Yes]
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) Price (SC)
  DocTotal Num(19,6) Total Document
  DocTotalFC Num(19,6) Total Document (FC)
  Ref1 nVarChar(11) Ref. 2
  Ref2 nVarChar(8) Ref. 3
  CounterRef nVarChar(8) Counter Reference
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remark
  TransId Int(11) Transaction Number ->OJDT
  DocTime Int(6) Creation Time
  ShowAtCard VarChar(1) Display Customer Ref. No. default=N [Y=No, N=Yes]
  SpiltTrans VarChar(1) Split Journal Entry default=N [Y=No, N=Yes]
  CreateTran VarChar(1) Create Journal Entry default=Y [Y=No, N=Yes]
  Flags Int(11) Flags default=0
  CntctCode Int(11) Contact Person ->OCPR
  DdctSumSy Num(19,6) Deduction Amount (SC)
  CashSumSy Num(19,6) Cash Amount in (SC)
  CredSumSy Num(19,6) Credit Amount (SC)
  CheckSumSy Num(19,6) Check Amount (SC)
  TrsfrSumSy Num(19,6) Bank Transfer Amount (SC)
  NoDocSumSy Num(19,6) Not Invoiced Amount (SC)
  DocTotalSy Num(19,6) Total Document (SC)
  ObjType nVarChar(20) Object Type ->ADP1
  StornoRate Num(19,6) Cancellation Rate
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  ApplyVAT VarChar(1) Tax Definition default=N [Y=No, N=Yes]
  TaxDate Date(8) Document Date
  Series Int(11) Series ->NNM1
  confirmed VarChar(1) Approved default=N [Y=No, N=Yes]
  ShowJDT VarChar(1) Display Journal Entries default=N [Y=No, N=Unknown]
  BankCode nVarChar(30) Bank Code for Bank Transfer
  BankAcct nVarChar(50) Account for Bank Transfer
  DataSource VarChar(1) Data Source default=N [N=Interface, I=Update, U=Import, M=DI API, O=Doc. Generation Wizard, A=Restore Wizard, D=Partner Implementation, P=Year Transfer, T=Yes, B=BSP]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatSum Num(19,6) Tax Amount
  VatSumFC Num(19,6) Tax Amount (FC)
  VatSumSy Num(19,6) Tax Amount (SC)
  FinncPriod Int(11) Posting Period ->OFPR
  VatPrcnt Num(19,6) Tax %
  Dcount Num(19,6) Discount
  DcntSum Num(19,6) Discount Amount
  DcntSumFC Num(19,6) Discount Amount (FC)
  DcntSumSy Num(19,6) Discount Amount (SC)
  SpltCredLn VarChar(1) Split Credit Voucher default=N [Y=No, N=Yes]
  PrjCode nVarChar(20) Project Code ->OPRJ
  PaymentRef nVarChar(27) Payment Reference No.
  Submitted VarChar(1) Submitted default=N [Y=No, N=Yes]
  Status VarChar(1) Created by Payment Wizard default=N [Y=No, N=BoE Canceled, C=Yes]
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
  WtSumSys Num(19,6) WTax Amount (FC)
  WtAccount nVarChar(15) WTax Account ->OACT
  WtBaseAmnt Num(19,6) WTax Taxable Amount
  Proforma VarChar(1) Proforma default=N [Y=No, N=No]
  BoeAbs Int(11) Boe Key ->OBOE
  BpAct nVarChar(15) BP Account ->OACT
  BcgSum Num(19,6) Bank Charges Amount
  BcgSumFC Num(19,6) Bank Charges Amount (FC)
  BcgSumSy Num(19,6) Bank Charges Amount (SC)
  PIndicator nVarChar(10) Period Indicator ->OPID
  PaPriority VarChar(1) Payment Priority default=6 [1=, 2=, 3=, 4=, 5=, 6=]
  PayToCode nVarChar(50) Pay to
  IsPaytoBnk VarChar(1) Is Pay to Bank default=N [N=Yes, Y=No.]
  PBnkCnt nVarChar(3) Pay to Bank Country ->OCRY
  PBnkCode nVarChar(30) Pay to Bank Code
  PBnkAccnt nVarChar(50) Pay to Bank Account No.
  PBnkBranch nVarChar(50) Pay to Bank Branch
  WizDunBlck VarChar(1) Wizard Dunning Block default=N [N=YES, Y=Yes]
  WtBaseSum Num(19,6) WTax Base Sum
  WtBaseSumF Num(19,6) WTax Base Sum (FC)
  WtBaseSumS Num(19,6) WTax Base Sum (SC)
  UndOvDiff Num(19,6) Under/Overpayment Difference
  UndOvDiffS Num(19,6) Under/Overpayment Diff. (SC)
  BankActKey Int(11) Bank Account Internal ID ->DSC1
  VersionNum nVarChar(11) Version Number
  VatDate Date(8) Tax Date
  TransCode nVarChar(4) Transaction Code ->OTRC
  PaymType VarChar(1) Payment Type default=N [N=, E=Mail, P=Telegraph, T=Express, X=Without]
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
  WddStatus VarChar(1) Authorization Status default=- [-=Pending, W=Approved, Y=Rejected, N=Generated, P=Generated by Authorizer, A=Canceled, C=Canceled]
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
  OperatCode VarChar(1) Operation Code [A=Summary Invoices Entry, B=Summary Receipts Entry, C=Invoice with Several VAT Rates, D=Correction Invoice, E=Due VAT Pending Invoice Issuance, F=Expenses Incurred by Travel Agent for Customers, G=Special Regulation for VAT Group, H=Special Regulation for Gold Investment, I=Reverse Charge Procedure, J=Unsummarized Receipts, K=Identification of Error Transactions, X=Transactions with Entrepreneurs Issuing Receipts for Agricultural Compensation, N=Service Invoicing by Travel Agencies on Behalf of Third Parties, R=Business Office Rental, S=Subsidies, T=Incoming Payments for Industrial and Intellectual Property Rights, U=Insurance Transactions, V=Purchases from Travel Agencies, W=Transactions Subject to Production, Service and Import Taxes in Ceuta and Melilla]
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

# BNK1 - Bank Statement - Documents List
Module: Banking | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ListLineID, BSLine, IdNumber
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) Bank Statement ID
  BSLine Int(11) Bank Statement Line ID
  ListLineID Int(6) List Line ID
  DocID nVarChar(27) Document Identifier
  AmntLC Num(19,6) Amount (LC)
  AmnFC Num(19,6) Amount (FC)
  IsDebit VarChar(1) Debit [Yes/No] default=Y [Y=Yes, N=No]

# BNK2 - Bank Statement - Recommendation List
Module: Banking | 29 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ListLineID, BSLine, IdNumber
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) Bank Statement ID
  BSLine Int(11) Bank Statement Line ID
  ListLineID Int(6) List Line ID
  DocID nVarChar(27) Document Identifier
  DocType Int(6) Document Type [15=Delivery, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt PO, 21=Goods Returns, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 25=Deposit, 46=Payment Advice, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, 58=Whse Reconciliation, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, -1=All transactions]
  AmntLC Num(19,6) Applied Amount (LC)
  AmntFC Num(19,6) Applied Amount (FC)
  IsDebit VarChar(1) Debit [Yes/No] default=Y [Y=Yes, N=No]
  GLAct nVarChar(15) G/L Account or BP Code ->OACT
  PrftCenter nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project ->OPRJ
  VatCode nVarChar(8) VAT Code ->OVTG
  Selected VarChar(1) Selected [Y=Yes, N=No]
  VatLC Num(19,6) VAT or Discount Amount (LC)
  VatFC Num(19,6) VAT or Discount Amount (FC)
  Installmnt Int(11) Installment
  InterimAct nVarChar(15) Interim Account ->OACT
  JdtLine Int(11) Journal Entry ->OJDT
  DocNum Int(11) Document Number
  PrftCent2 nVarChar(8) Distribution Rule2 ->OOCR
  PrftCent3 nVarChar(8) Distribution Rule3 ->OOCR
  PrftCent4 nVarChar(8) Distribution Rule4 ->OOCR
  PrftCent5 nVarChar(8) Distribution Rule5 ->OOCR
  MatchLog nVarChar(254) Matching Criteria Log
  DueBal Num(19,6) Balance Due
  DueBalFC Num(19,6) Balance Due (FC)
  AmntSC Num(19,6) Applied Amount (SC)
  BPLId Int(11) Branch ID ->OBPL
  BPLName nVarChar(100) Branch Name

# BOC1 - External Bank Operation Code - Rows
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ExOpCode, AbsEntry
  BY_LINE U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBOC
  ExOpCode nVarChar(40) External Bank Operation Code
  OPDscrpt nVarChar(40) Operation Description
  InOpCode Int(11) Internal Bank Operation Code ->OBTC
  LogInstanc Int(11) Log Instance default=0
  LineId Int(6) Row

# BOE1 - Bill of Exchange for Payment - Rows
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, BoeKey
Fields (name type(len) description [values] ->parent table):
  BoeKey Int(11) SBO Internal Key ->OBOE
  LineId Int(11) Row No.
  LineDitail nVarChar(40) Row Details
  LineMoney Num(19,6) Row Total
  LineCurr nVarChar(3) Row Currency ->OCRN
  LineAcct nVarChar(15) Row Account
  Line_A_C VarChar(1) BP/Account default=0
  Code nVarChar(8) Tax Definition ->OVTG
  CredAcct nVarChar(15) Credited Account ->OACT
  TotalLine Num(19,6) Row Total
  VatPercent Num(19,6) Tax %:
  UserSign Int(11) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0

# BOT1 - Bill of Exchange Transactions
Module: Banking | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BoeType, BOENumber, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Transaction No. ->OBOT
  BOENumber Int(11) Bill of Exchange No.
  BoeType VarChar(1) Bill of Exchange Type default=I [I=Incoming, O=Outgoing]
  DueDate Date(8) Bill of Exchange Due Date
  BPBankCtr nVarChar(3) BP Bank Country ->OCRY
  BPBankCod nVarChar(30) BP Bank Code
  BPBankAct nVarChar(50) BP Bank Account
  BPBankBrnc nVarChar(50) BP Bank Branch
  ExReconNum Int(11) Extra Reconciliation Number
  BOEAbs Int(11) Bill of Exchange Key ->OBOE
  BPLId Int(11) Branch ->OBPL
  EnBPBnkAct Text(16) Encryption of BP Bank Account
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# BTC1 - Internal Bank Operation Codes - Accounts
Module: Banking | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineId Int(6) Row
  GLAct nVarChar(15) G/L Account ->OACT
  Project nVarChar(20) Project ->OPRJ
  PrftCenter nVarChar(8) Distribution Rule ->OOCR
  VatCode nVarChar(8) VAT Code ->OVTG
  LogInstanc Int(11) Log Instance default=0
  PrftCent2 nVarChar(8) Distribution Rule2 ->OOCR
  PrftCent3 nVarChar(8) Distribution Rule3 ->OOCR
  PrftCent4 nVarChar(8) Distribution Rule4 ->OOCR
  PrftCent5 nVarChar(8) Distribution Rule5 ->OOCR

# CHD1 - Checks for Payment Drafts - Rows
Module: Banking | 22 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, CheckKey
Fields (name type(len) description [values] ->parent table):
  CheckKey Int(11) SAP Business One Internal Key ->OCHD
  LineId Int(11) Row No.
  LineDitail nVarChar(40) Row Details
  LineMoney Num(19,6) Row Total
  LineCurr nVarChar(3) Row Currency
  LineAcct nVarChar(15) Row Account
  Line_A_C VarChar(1) Business Partner or Account default=0
  Code nVarChar(8) Tax Definition ->OVTG
  CredAcct nVarChar(15) Credited Account ->OACT
  TotalLine Num(19,6) Row Total
  VatPercent Num(19,6) Tax %:
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=123 ->ADP1
  LineMnyLC Num(19,6) Row Total (LC)
  LineMnySC Num(19,6) Row Total (SC)
  LineMnyFC Num(19,6) Row Total (FC)
  TotLineLC Num(19,6) Row Total (LC)
  TotLineSC Num(19,6) Row Total (SC)
  TotLineFC Num(19,6) Row Total (FC)
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History

# CHO1 - Checks for Payment - Rows
Module: Banking | 22 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, CheckKey
Fields (name type(len) description [values] ->parent table):
  CheckKey Int(11) SAP Business One Internal Key ->OCHO
  LineId Int(11) Row Number
  LineDitail nVarChar(40) Row Details
  LineMoney Num(19,6) Row Total
  LineCurr nVarChar(3) Row Currency
  LineAcct nVarChar(15) Row Account
  Line_A_C VarChar(1) Business Partner or Account default=0
  Code nVarChar(8) Tax Definition ->OVTG
  CredAcct nVarChar(15) Credited Account ->OACT
  TotalLine Num(19,6) Row Total
  VatPercent Num(19,6) Tax %:
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=57 ->ADP1
  LineMnyLC Num(19,6) Row Total (LC)
  LineMnySC Num(19,6) Row Total (SC)
  LineMnyFC Num(19,6) Row Total (FC)
  TotLineLC Num(19,6) Row Total (LC)
  TotLineSC Num(19,6) Row Total (SC)
  TotLineFC Num(19,6) Row Total (FC)
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History

# CHO2 - Checks for Payment - Print Status
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Index
  ChkNum Int(11) Check Number
  Status VarChar(1) Status default=N [D=Details, V=Void, N=Not Confirmed, T=Not Printed, O=Overflow]
  PrnBy Int(6) Printed By
  LineNum Int(11) Row Number

# CTG1 - Installment Layout
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: IntsNo, CTGCode
  ABS_ENTRY U: InstDays, InstMonth, CTGCode
Fields (name type(len) description [values] ->parent table):
  CTGCode Int(6) Payment Method Code ->OCTG
  IntsNo Int(6) Installment No.
  InstMonth Int(6) Installment Month default=0
  InstDays Int(6) Installment Days default=0
  InstPrcnt Num(19,6) Installment %

# DPS1 - Deposit - Rows
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CheckKey, DepositId
Fields (name type(len) description [values] ->parent table):
  DepositId Int(11) Deposit Key ->ODPS
  CheckKey Int(11) Check Key
  DepCancel VarChar(1) Canceled default=N [Y=Yes, N=No]

# DSC1 - House Bank Accounts
Module: Banking | 79 columns | ObjType: 231
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SECONDARY U: Account, BankCode, Country
Fields (name type(len) description [values] ->parent table):
  BankCode nVarChar(30) Bank Code
  Account nVarChar(50) Acct No.
  Branch nVarChar(50) Branch
  NextCheck Int(11) Next Check No.
  GLAccount nVarChar(15) G/L Account ->OACT
  Free VarChar(1) Free
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  Country nVarChar(3) Country ->OCRY
  State nVarChar(3) State ->OCST
  BISR VarChar(1) BISR default=N [Y=Yes, N=No]
  ControlKey nVarChar(2) Control Key
  UsrNumber1 nVarChar(25) User No. 1
  UsrNumber2 nVarChar(25) User No. 2
  UsrNumber3 nVarChar(25) User No. 3
  UsrNumber4 nVarChar(25) User No. 4
  IBAN nVarChar(50) IBAN
  DscountBOE nVarChar(15) Debt of Discounted BoE ->OACT
  TolrnceDay Int(11) Tolerance Days
  MinAmntBOE Num(19,6) Min. Amount of Bill of Exchange
  MaxAmntBOE Num(19,6) Max. Amount of Bill of Exchange
  DscntLimit Num(19,6) Discount Limit
  DaysInAdva Int(11) Days in Advance
  BankCollec nVarChar(15) Bank on Collection ->OACT
  BankDiscou nVarChar(15) Bank on Discounted ->OACT
  BranchName nVarChar(50) Branch Name
  AliasName nVarChar(50) Alias Name
  CompanyCod nVarChar(10) Company Code
  AcctType VarChar(1) Account Type
  Building Text(16) Building/Floor/Room
  BIK nVarChar(15) BIK
  AcctName nVarChar(250) Bank Account Name
  CorresAcct nVarChar(30) Correspondent Account
  Phone nVarChar(25) Telephone No.
  Fax nVarChar(25) Fax
  GLIntriAct nVarChar(15) G/L Interim Account ->OACT
  ChkPaper VarChar(1) Paper Type default=D [B=Blank Paper, S=Overflow Prenumbered Check Stock, P=Overflow Blank Paper, D=Default]
  MaxChkLine Int(6) Maximum Lines
  TmpltName nVarChar(8) Template Name
  AbsEntry Int(11) Internal Number
  BankKey Int(11) Bank Internal ID ->ODSC
  LockChk VarChar(1) Lock Checks Printing default=N [Y=Yes, N=No]
  OurNum Int(11) Our Number in Next Boleto
  AgreeNum nVarChar(10) Agreement Number
  AccountChk VarChar(1) Account Check Digit
  ISRType Int(6) ISR Type default=2 [1=ISR, 2=BISR, 3=ISR+, 4=BISR+]
  ISRBillerI nVarChar(9) ISR Biller ID
  CustIdNum nVarChar(10) Customer ID Number default=0
  InSeri Int(11) Incoming Payment Series default=-1 ->NNM1
  OutSeri Int(11) Outgoing Payment Series default=-1 ->NNM1
  JDTSeri Int(11) Journal Entry Series default=-1 ->NNM1
  FilePlug nVarChar(50) Import File Name
  ImpStmt VarChar(1) Imported Bank Statement default=N [Y=Create New - From File, N=Create New - Manually]
  PreNumber VarChar(1) Prenumbered Check default=Y [Y=Yes, N=No]
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UsrLogSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  SwiftNum nVarChar(50) BIC/SWIFT Code
  FineAcct nVarChar(15) Fine Account ->OACT
  IntrstAcct nVarChar(15) Interest Account ->OACT
  DscntAcct nVarChar(15) Discount Account ->OACT
  SvcFeeAcct nVarChar(15) Service Fee Account ->OACT
  BranchChk nVarChar(5) Branch Check Digit
  RetFile nVarChar(50) Retorno File Format
  IOFTaxAcct nVarChar(15) IOF Tax Account
  OthExpAcct nVarChar(15) Other Expenses Account ->OACT
  OthIncAcct nVarChar(15) Other Incomes Account ->OACT
  CollCode nVarChar(50) Collection Code
  FileSeqNNo Int(11) File Sequence Next Number
  RefCoLevel VarChar(1) Reference control level default=H [S=Soft Control, H=Hard Control, V=Hard Control with variable length, F=Hard Control with fixed length]
  RefFixLen1 Int(6) Reference fixed length 1
  RefFixLen2 Int(6) Reference fixed length 2
  Currency nVarChar(3) Currency ->OCRN

# ITR1 - Internal Reconciliation - Rows
Module: Banking | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, ReconNum
  Journal: TransRowId, TransId
  Object: SrcObjAbs, SrcObjTyp
Fields (name type(len) description [values] ->parent table):
  ReconNum Int(11) Reconciliation Number ->OITR
  LineSeq Int(11) Row Number
  ShortName nVarChar(15) BP/Account Code
  TransId Int(11) Transaction Internal ID ->OJDT
  TransRowId Int(11) Transaction Row Number
  SrcObjTyp nVarChar(20) Source Object Type [30=Journal Transactions, 13=Invoices, 18=Purchases, 24=Receipts, 46=Outgoing Payments, 14=Revert Invoices, 19=Revert Purchases, 203=Down Payment Incoming, 204=Down Payment Outgoing, 163=Correction A/P Invoice, 164=Correction A/P Invoice Reversals, 165=Correction A/R Invoice, 166=Correction A/R Invoice Reversals]
  SrcObjAbs Int(11) Source Object Internal ID
  ReconSum Num(19,6) Reconciliation Amount
  ReconSumFC Num(19,6) Reconciliation Amount (FC)
  ReconSumSC Num(19,6) Reconciliation Amount (SC)
  FrgnCurr nVarChar(3) Foreign Currency ->OCRN
  SumMthCurr Num(19,6) Amt in Reconciliation Currency
  IsCredit VarChar(1) Credit or Debit [C=Credit, D=Debit]
  Account nVarChar(15) Account Code ->OACT
  CashDisSum Num(19,6) Cash Discount Amount
  WTSum Num(19,6) Withholding Tax Amount
  WTSumFC Num(19,6) Withholding Tax Amount (FC)
  WTSumSC Num(19,6) Withholding Tax Amount (SC)
  ExpSum Num(19,6) Freight Amount
  ExpSumFC Num(19,6) Freight Amount (FC)
  ExpSumSC Num(19,6) Freight Amount (SC)
  netBefDisc Num(19,6) Net Before Discount Sum
  MIEntry Int(11) MI Entry Include this Recon. default=0
  MIType nVarChar(20) MI Type Include this Recon. [270=A/R Monthly Invoice, 140000014=A/P Monthly Invoice]
  InstID Int(11) Installment ID default=0

# MTH1V - Journal Entries of External Reconciliation
Module: Banking | 18 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line_ID, TransID, MatchNum, IsInternal, MthAcctCod
Fields (name type(len) description [values] ->parent table):
  MthAcctCod nVarChar(15) Account Code
  IsInternal VarChar(1) Reconciliation Type default=E [I=Internal, E=External]
  MatchNum Int(11) Reconciliation No.
  TransID Int(11) Transaction No.
  Line_ID Int(11) Row Number
  RefDate Date(8) Posting Date
  DueDate Date(8) Due Date
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  Ref3Line nVarChar(27) Reference 3
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  SYSDeb Num(19,6) System Debit Amount
  SYSCred Num(19,6) System Credit Amount
  FCDebit Num(19,6) Foreign Debit Amount
  FCCredit Num(19,6) Foreign Credit Amount
  Currency nVarChar(3) Currency
  LineMemo nVarChar(254) Row Details

# MTH2V - Bank Statements of External Reconciliation
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Sequence, MatchNum, IsInternal, MthAcctCod
  SECONDARY U: Sequence, BnkAcctCod
Fields (name type(len) description [values] ->parent table):
  MthAcctCod nVarChar(15) Account Code
  IsInternal VarChar(1) Reconciliation Type default=E [I=Internal, E=External]
  MatchNum Int(11) Reconciliation No.
  BnkAcctCod nVarChar(15) Account Code
  Sequence Int(11) Sequence No.
  DueDate Date(8) Due Date
  Ref nVarChar(27) Reference
  DebAmount Num(19,6) Debit Amount
  Memo nVarChar(254) Details

# MTH3V - Filter for Query MTH
Module: Banking | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: MatchNum, IsInternal, MthAcctCod
Fields (name type(len) description [values] ->parent table):
  absEntry Int(11) Internal Number
  AcctCdeFrm nVarChar(15) Account Code From
  AcctCdeTo nVarChar(15) Account Code To
  IsInternal VarChar(1) Reconciliation Type default=E [I=Internal, E=External]
  IsCard VarChar(1) Select BP or Account default=A [A=G/L Account, C=BP]
  MatchNumFr Int(11) Reconciliation No. From
  MatchNumTo Int(11) Reconciliation No. To
  MthDateFrm Date(8) Reconciliation Date From
  MthDateTo Date(8) Reconciliation Date To
  MthAcctCod nVarChar(15) Account Code
  MatchNum Int(11) Reconciliation No.

# OBCA - Bank Charges Allocation Codes
Module: Banking | 2 columns | ObjType: 239
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(3) Code
  Name nVarChar(50) Description

# OBCG - Bank Charge for Bank Transfers
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SerialNo
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  BkChgAmt Num(19,6) Bank Charge
  SerialNo Int(11) Serial No.
  DocCurr nVarChar(3) Document Currency
  BcgTaxAmt Num(19,6) Bank Charge Tax

# OBNH - Bank Statement Header
Module: Banking | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: IdNumber
  ACT_NUM_DT U: BSDate, BSNum, ActKey
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) Internal Number
  ActKey Int(11) Bank Account Internal Number ->DSC1
  BSNum Int(11) Statement Internal Number
  BSDate Date(8) Statement Date
  Status VarChar(1) Status default=D [E=Finalized, D=Draft, O=Old]
  Imported VarChar(1) Imported From File default=Y [Y=Yes, N=No]
  StrtBlncF Num(19,6) Starting Balance (FC)
  EndBlncF Num(19,6) Ending Balance (FC)
  Currency nVarChar(3) Currency ->OCRN
  StrtBlncL Num(19,6) Starting Balance (LC)
  EndBlncL Num(19,6) Ending Balance (LC)
  FileCRC nVarChar(32) Bank Statement File Hash
  StmtGuid nVarChar(32) Bank Statement GUID
  BSFileNum nVarChar(50) Bank Statement Number
  PeriodAbs Int(11) Period Abs Entry
  DfltBPL Int(11) Default Branch

# OBNK - External Bank Statement Received
Module: Banking | 73 columns | ObjType: 42
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Sequence, AcctCode
  MATCH_ID: BankMatch
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) External Bank Statement No. ->OBNH
  AcctCode nVarChar(15) Account Number ->OACT
  Sequence Int(11) Sequence No. default=0
  AcctName nVarChar(100) Account Name
  Ref nVarChar(27) Reference
  DueDate Date(8) Due Date
  Memo nVarChar(254) Details
  DebAmount Num(19,6) Debit Amount (FC)
  DebAmntCur nVarChar(3) Currency for Accounts Payable ->OCRN
  CredAmnt Num(19,6) Credit Amount (FC)
  CredAmntCu nVarChar(3) Credit Currency ->OCRN
  balance Num(19,6) Balance
  BankMatch Int(11) Reconciliation No.
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ExternCode nVarChar(30) External Code
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  StatemNo Int(11) Statement Number
  DocNum nVarChar(27) Invoice Document
  PaymCreat VarChar(1) Payment Created default=N [Y=Yes, N=No]
  LineStatus VarChar(1) Row Status
  VisOrder Int(11) Visual Order
  DocNumType VarChar(1) Doc. No. Source default=D [P=Payment Reference No., I=ISR, D=Doc Num]
  Memo2 nVarChar(254) Details 2
  PaymentRef nVarChar(27) Payment Reference No.
  autoCreate VarChar(1) Manually/Automatically Create default=M [M=Manual, A=Automatic]
  BSLineDate Date(8) Bank Statement Entry Date
  BSValuDate Date(8) Bank Statement Due Date
  InOpCode Int(11) Internal Bank Operation Code ->OBTC
  Cleared VarChar(1) Cleared default=N [Y=Yes, N=No]
  OposAct nVarChar(50) BP Bank Account
  DebAmntLC Num(19,6) Debit Amount (LC)
  CredAmntLC Num(19,6) Credit Amount (LC)
  ExchngRate Num(19,6) Exchange Rate
  BPIBAN nVarChar(50) IBAN of the BP Bank Account
  Fee Num(19,6) Fee on the Line
  PmnPstDate Date(8) Payment Posting Date
  PmnValDate Date(8) Payment Due Date
  LnDocDate Date(8) Line Document Date
  VatAmntLC Num(19,6) VAT Amount (LC)
  VatAmntFC Num(19,6) VAT Amount (FC)
  JDTID Int(11) Journal Entry ID ->OJDT
  PmntID Int(11) Payment ID
  ObjCrtType Int(6) Document Type default=24
  PstMethod VarChar(1) Posting Method default=C [A=G/L Account from/to Bank Account, C=BP from/to Bank Account, J=Interim Account from/to Bank Account, E=External Reconciliation, I=Ignore]
  FeeAct nVarChar(15) G/L Account for Fee ->OACT
  FeeProfitC nVarChar(8) Fee Distribution Rule ->OOCR
  FeeProj nVarChar(20) Project Fee ->OPRJ
  BpBankCode nVarChar(30) BP Bank Code
  FeeProfit2 nVarChar(8) Fee Distribution Rule2 ->OOCR
  FeeProfit3 nVarChar(8) Fee Distribution Rule3 ->OOCR
  FeeProfit4 nVarChar(8) Fee Distribution Rule4 ->OOCR
  FeeProfit5 nVarChar(8) Fee Distribution Rule5 ->OOCR
  ApplWTSum Num(19,6) Applied WTax Sum
  InfoLog nVarChar(254) Information Log
  LineOrigin VarChar(1) Row Origin default=R [R=Regular, A=Archive]
  BPSwift nVarChar(50) BP BIC/SWIFT Code
  Source VarChar(1) Source default=I [I=Imported, A=Imported and Amended, M=Manually Entered]
  PayOrderNo Int(11) Payment Order Number
  TaxIDNum nVarChar(32) Federal Tax ID
  PONumber Int(11) External Payment Order Number
  FormatName nVarChar(254) Format Name for Bank Statement
  FileCRC nVarChar(32) Bank Statement File Hash Code
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  BPLIdPmn Int(11) Branch for Payment ID ->OBPL
  BPAcctName nVarChar(250) BP Bank Account Name
  EnOposAct Text(16) Encryption of BP Bank Account
  EnBPIBAN Text(16) Encryption of BP Bank IBAN
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  CreateDate Date(8) Creation Date

# OBOC - External Bank Operation Code Category
Module: Banking | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CATEGORY U: OpCodeCat
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  OpCodeCat nVarChar(30) Operation Code Category
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

# OBOE - Bill of Exchange for Payment
Module: Banking | 92 columns | ObjType: 181
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BoeKey
  VPM_NUM: PmntNum
  TRANS_NUM: TransNum
  DPS_NUM: DepositNum
  BOE_NUM U: BoeType, BoeNum
Fields (name type(len) description [values] ->parent table):
  BoeKey Int(11) Bill of Exchange Key
  BoeNum Int(11) Bill of Exchange No.
  BoeStatus VarChar(1) Bill of Exchange Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, L=Closed, F=Failed, V=BoE to Vendor]
  BoeType VarChar(1) Bill of Exchange Type default=I [I=Incoming, O=Outgoing]
  DpsBankCod nVarChar(30) Deposit Bank Code
  DpsCntrCod nVarChar(3) Deposit Country Code ->OCRY
  DueDate Date(8) Bill of Exchange Due Date
  DpstAcct nVarChar(50) Bank Account No.
  DpstBranch nVarChar(50) Branch for Payments
  Details nVarChar(50) Details
  TransRef nVarChar(8) Journal Entry Reference
  PmntDate Date(8) Payment Date
  PmntNum Int(11) Payment No.
  BoeSum Num(19,6) Bill of Exchange Amount
  BoeSumSC Num(19,6) Bill of Exchange Amount (SC)
  BoeSumFC Num(19,6) Bill of Exchange Amount (FC)
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  BoeAcct nVarChar(15) BP Account Code ->OACT
  Currency nVarChar(3) Bill of Exchange Currency ->OCRN
  Printed VarChar(1) Printed default=N [N=No, Y=Yes]
  TotalWords nVarChar(100) Total in Words
  Signature nVarChar(155) Signature
  TransNum Int(11) Transaction No. default=0
  LinesSum Num(19,6) Row Totals
  DdctPrcnt Num(19,6) % Withholding Tax Ded.
  Address nVarChar(254) Address
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  VatTotal Num(19,6) Total Tax
  VatTotalSC Num(19,6) Total Tax (SC)
  VatTotalFC Num(19,6) Total Tax (FC)
  VatCalcult VarChar(1) Calculate Tax default=N [Y=Yes, N=No]
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SumRfndCln Num(19,6) Deduction Refund Amount
  UserSign Int(6) User Signature ->OUSR
  PrintedBy Int(6) Printed By
  Transfered VarChar(1) Transferred to next year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  BPBankCod nVarChar(30) BP Bank Code
  BPBankNam nVarChar(250) BP Bank Name
  BPBankAct nVarChar(50) BP Bank Account
  BPBankBrnc nVarChar(50) BP Bank Branch
  BPBankCtr nVarChar(3) BP Bank Country ->OCRY
  RefNum nVarChar(254) Reference No.
  IsReconcld VarChar(1) Reconciled default=N [N=No, Y=Yes]
  Comments nVarChar(254) Remarks
  PayMethCod nVarChar(15) Payment Method Code ->OPYM
  DepositNum Int(11) Deposit Number
  PymMethNam nVarChar(100) Payment Method Name
  DeductSum Num(19,6) Deduction Amount
  ControlKey nVarChar(2) Control Key
  AgentCode nVarChar(32) Agent Code ->OAGP
  ReconcilNu Int(11) External Reconciliation No.
  DepositTyp VarChar(1) Deposit Type [C=Collection, D=Discounted]
  CreatStatu VarChar(1) Creation Status [G=Generated, S=Sent]
  Ref2 nVarChar(254) Reference 2
  PayEngSt1 VarChar(1) Payment Engine Status 1
  PayEngSt2 VarChar(1) Payment Engine Status 2
  PayEngSt3 nVarChar(3) Payment Engine Status 3
  StampTax nVarChar(8) Stamp Tax Code ->OVTG
  StmpTxAmnt Num(19,6) Stamp Tax Amount
  DpsActKey Int(11) Bank Account Internal ID ->DSC1
  OutBnkKey Int(11) Outgoing Bank Account Key ->DSC1
  Portfolio nVarChar(8) Portfolio ->OPFT
  VndCodeCEE nVarChar(15) Vendor Code ->OCRD
  VndNameCEE nVarChar(100) Vendor Name
  OurNum Int(11) Our Number
  BarcodeNum nVarChar(120) Bar Code Number
  BarcodeRep nVarChar(100) Bar Code Representation
  OurNumChk VarChar(1) Our Number Check Digit
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  LPgFolioN Int(11) Folio No. for Last Page in Doc.
  UserSign2 Int(6) Updating User ->OUSR
  IntrstAmnt Num(19,6) Interest Amount
  DiscAmnt Num(19,6) Discount Amount
  FineAmnt Num(19,6) Fine Amount
  IntrstDate Date(8) BoE Interest Date
  DiscDate Date(8) BoE Discount Date
  FineDate Date(8) BoE Fine Date
  PostType VarChar(1) Posting Type [D=Default, A=Alternative]
  IOFAmnt Num(19,6) IOF Amount
  ServFeeAm Num(19,6) Service Fee Amount
  OtherExAm Num(19,6) Other Expenses Amount
  OtherInAm Num(19,6) Other Incomes Amount
  BPLId Int(11) Branch ->OBPL
  EnBPBnkAct Text(16) Encryption of BP Bank Account
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# OBOT - Bill Of Exchang Transaction
Module: Banking | 10 columns | ObjType: 182
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) BOE Transaction key
  UserSign Int(6) User Signature ->OUSR
  StatusFrom VarChar(1) Status from [S=Sent, G=Generated, D=Deposit, P=Paid, F=Failed, V=BoE to Vendor]
  StatusTo VarChar(1) Status To [C=Canceled, G=Generated, D=Deposit, P=Paid, F=Failed, L=Closed, V=BoE to Vendor]
  TranDate Date(8) Transaction Date
  TranTime Int(6) Transaction Time
  Reconciled VarChar(1) was the Boe Reconciled default=N [Y=Yes, N=No]
  TransId Int(11) Transaction Number ->OJDT
  PostDate Date(8) Posting Date
  TaxDate Date(8) Document Date

# OBST - BoE Stamp Tax
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  AMOUNT U: Amount
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Amount Num(19,6) BoE Amount
  StampTax Num(19,6) BoE Stamp Tax

# OBTC - Internal Bank Operation Codes
Module: Banking | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE_NAME U: InOpCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number default=0
  InOpCode nVarChar(15) Internal Bank Operation Code Name
  PstTrans VarChar(1) Posting Transaction default=1 [1=Bank Transfer, 2=Incoming Bill of Exchange, 3=Outgoing Bill of Exchange, 4=Outgoing Checks, 5=Deposit]
  BPorAct VarChar(1) BP or Account default=C [C=BP, A=Account]
  PstMethod VarChar(1) BP Posting Method default=C [A=G/L Account from/to Bank Account, C=Business Partner from/to Bank Account, J=Bank Interim Account from/to Bank Account, E=External Reconciliation, I=Ignore]
  ActFee nVarChar(15) Account Fee ->OACT
  ProjFee nVarChar(20) Project Fee ->OPRJ
  PrftCntFee nVarChar(8) Fee Distribution Rule ->OOCR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  Descript nVarChar(40) Operation Description
  PrftCntFe2 nVarChar(8) Fee Distribution Rule2 ->OOCR
  PrftCntFe3 nVarChar(8) Fee Distribution Rule3 ->OOCR
  PrftCntFe4 nVarChar(8) Fee Distribution Rule4 ->OOCR
  PrftCntFe5 nVarChar(8) Fee Distribution Rule5 ->OOCR
  UserSign2 Int(6) Updating User ->OUSR

# OCBI - Central Bank Ind.
Module: Banking | 2 columns | ObjType: 161
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Indicator
Fields (name type(len) description [values] ->parent table):
  Indicator nVarChar(15) Bank Indicator
  Dsc nVarChar(50) Description

# OCHD - Checks for Payment Drafts
Module: Banking | 56 columns | ObjType: 123
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CheckKey
  VPM_NUM: PmntNum
  TRANS_NUM: TransNum
Fields (name type(len) description [values] ->parent table):
  CheckKey Int(11) Check Key
  CheckNum Int(11) Check Number
  BankNum nVarChar(30) Bank No.
  Branch nVarChar(50) Branch
  BankName nVarChar(250) Bank Name
  CheckDate Date(8) Cashing Date
  DpstAcct nVarChar(50) Bank Account Number
  DpstBranch Int(6) Branch for Payments
  AcctNum nVarChar(50) Account No.
  Details nVarChar(50) Details
  TransRef nVarChar(11) Transaction Reference
  PmntDate Date(8) Payment Date
  PmntNum Int(11) Payment No. ->OVPM
  CheckSum Num(19,6) Check Amount
  Trnsfrable VarChar(1) Freely Negotiable default=N [Y=Yes, N=No]
  VendorCode nVarChar(15) Vendor Code
  Currency nVarChar(3) Check Currency
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CardOrAcct VarChar(1) Business Partner or Account default=C [C=Card, A=Account]
  Printed VarChar(1) Printed default=N [N=No, Y=Yes]
  VendorName nVarChar(100) Vendor Name
  TotalWords nVarChar(254) Total in Words
  Signature nVarChar(30) Signature
  CheckAcct nVarChar(15) Credited Account Code
  TransNum Int(11) Transaction Number default=0 ->OJDT
  LinesSum Num(19,6) Row Totals
  Deduction Num(19,6) WTax Deduction - Amt
  DdctPrcnt Num(19,6) Withholding Tax Deduction %
  Address nVarChar(254) Address
  CreateJdt VarChar(1) Create Journal Entry default=Y [N=No, Y=Yes]
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  VatTotal Num(19,6) Total Tax
  VatCalcult VarChar(1) Calculate Tax default=N [Y=Yes, N=No]
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SumRfndCln Num(19,6) Deduction Refund Amount
  UserSign Int(6) User Signature ->OUSR
  PrintedBy Int(6) Printed By
  Transfered VarChar(1) Transferred to next year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=123 ->ADP1
  CountryCod nVarChar(3) Country Code ->OCRY
  AddrName nVarChar(50) Address Name
  PrnConfrm VarChar(1) Confirm Printing default=N [N=No, Y=Yes]
  BnkActKey Int(11) Bank Account Internal ID ->DSC1
  CancelDate Date(8) Cancelation Date
  ManualChk VarChar(1) Manual Check default=N [N=No, Y=Yes]
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) Branch Reg. No.
  Endorse VarChar(1) Endorse default=N [N=No, Y=Yes]
  EndorsChNo Int(11) Endorsable Check No. ->OCHH
  UserSign2 Int(6) Updating User - History ->OUSR
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# OCHH - Check Register
Module: Banking | 37 columns | ObjType: 27
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CheckKey
  RECEIPT: RcptLineId, RcptNum
  DEP_ABS1: DpstAbs
  CHECK_NUM: CheckNum
  DEP_ABS2: DepNum2
Fields (name type(len) description [values] ->parent table):
  CheckKey Int(11) Check Key
  CheckNum Int(11) Check Number
  BankCode nVarChar(30) Bank Code
  Branch nVarChar(50) Branch Number
  CashCheck nVarChar(15) Check Register Account
  CheckDate Date(8) Check Date
  Details nVarChar(20) Details
  CardCode nVarChar(15) BP/Account Code ->OCRD
  RcptDate Date(8) Receipt Date
  RcptNum Int(11) Receipt Number ->ORCT
  CheckSum Num(19,6) Check Amount
  Trnsfrable VarChar(1) Negotiable default=N [Y=Yes, N=No]
  Deposited VarChar(1) Deposited default=N [C=As Cash, N=No, S=As Postdated]
  Converted VarChar(1) Endorsed default=N [Y=Yes, N=No]
  Vendor nVarChar(15) Endorsed for
  TransNum Int(11) Payment Transaction
  DepNum2 Int(11) Postdated Deposit Key default=0 ->ODPT
  DpstAbs Int(11) Payment Internal ID ->ODPS
  BankAcct nVarChar(15) Deposit Account
  AcctNum nVarChar(50) Account Number
  Currency nVarChar(3) Check Currency
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  RcptLineId Int(11) Row Number in Receipt
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  UserID Int(6) User Signature ->OUSR
  BankCountr nVarChar(3) Bank Country ->OCRY
  Project nVarChar(20) Project Code ->OPRJ
  CanceJEAbs Int(11) Cancellation Journal Entry ->OJDT
  TempJEAbs Int(11) Temp. Journal Entry
  CardName nVarChar(100) BP/Account Name
  FiscalID nVarChar(100) Fiscal ID
  OrigIssdBy nVarChar(254) Orginally Issued By
  RejeByBank VarChar(1) Rejected by Bank default=N [Y=Yes, N=No]
  EnAcctNum Text(16) Encryption of Account Number
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# OCHO - Checks for Payment
Module: Banking | 56 columns | ObjType: 57
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CheckKey
  VPM_NUM: PmntNum
  TRANS_NUM: TransNum
Fields (name type(len) description [values] ->parent table):
  CheckKey Int(11) Check Key
  CheckNum Int(11) Check No.
  BankNum nVarChar(30) Bank Code
  Branch nVarChar(50) Branch
  BankName nVarChar(250) Bank Name
  CheckDate Date(8) Check Date
  DpstAcct nVarChar(50) Bank Account No.
  DpstBranch Int(6) Branch for Payments
  AcctNum nVarChar(50) Account No.
  Details nVarChar(50) Details
  TransRef nVarChar(11) Journal Entry Reference
  PmntDate Date(8) Payment Date
  PmntNum Int(11) Payment No. default=0 ->OVPM
  CheckSum Num(19,6) Check Amount
  Trnsfrable VarChar(1) Negotiable default=N [N=No, Y=Yes]
  VendorCode nVarChar(15) Vendor Code
  Currency nVarChar(3) Check Currency
  Canceled VarChar(1) Canceled default=N [N=No, Y=Yes]
  CardOrAcct VarChar(1) Business Partner or Account default=C [C=BP, A=Account]
  Printed VarChar(1) Printed default=N [N=No, Y=Yes]
  VendorName nVarChar(100) Vendor Name
  TotalWords nVarChar(254) Total in Words
  Signature nVarChar(30) Signature
  CheckAcct nVarChar(15) Customer Account Code
  TransNum Int(11) Transaction Number default=0 ->OJDT
  LinesSum Num(19,6) Row Totals
  Deduction Num(19,6) Deduction Amount
  DdctPrcnt Num(19,6) Withholding Tax Deduction %
  Address nVarChar(254) Address
  CreateJdt VarChar(1) Create Journal Entry default=Y [N=No, Y=Yes]
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  VatTotal Num(19,6) Total Tax
  VatCalcult VarChar(1) Calculate Tax default=N [Y=Yes, N=No]
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SumRfndCln Num(19,6) Deduction Refund Amount
  UserSign Int(6) User Signature ->OUSR
  PrintedBy Int(6) Printed By
  Transfered VarChar(1) Transferred to next year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=57 ->ADP1
  CountryCod nVarChar(3) Country Code ->OCRY
  AddrName nVarChar(50) Address Name
  PrnConfrm VarChar(1) Confirm Printing default=N [N=No, Y=Yes]
  BnkActKey Int(11) Bank Account Internal ID ->DSC1
  CancelDate Date(8) Cancelation Date
  ManualChk VarChar(1) Manual Check default=N [N=No, Y=Yes]
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) Branch Reg. No.
  Endorse VarChar(1) Endorse default=N [N=No, Y=Yes]
  EndorsChNo Int(11) Endorsable Check No. ->OCHH
  UserSign2 Int(6) Updating User - History ->OUSR
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# OCRH - Credit Card Management
Module: Banking | 39 columns | ObjType: 72
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Instance, AbsId
  CRED_CARD: CreditCard
  CRED_TYPE: CreditType
  RECEIPT: Storno, RcptLineId, RctAbs
  CUST_CODE: CardCode
  DEP_ABS: DepNum
  IS_VALID: Storno, CreditCard, VoucherNum
  CRED_ACCT: CreditAcct
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Seq. No. in Amount
  CreditCard Int(6) Credit Card default=0 ->OCRC
  CrdCardNum nVarChar(64) Credit Card No.
  CardValid Date(8) Credit Card Validity
  VoucherNum nVarChar(27) Voucher Number
  OwnerIdNum nVarChar(15) ID Number
  OwnerPhone nVarChar(20) Telephone
  CrTypeCode Int(6) Payment Method Code ->OCRP
  NumOfPmnts Int(6) Number of Payments default=1
  PayDate Date(8) Payment Date
  FirstSum Num(19,6) First Partial Payment
  AddPmntSum Num(19,6) Each Additional Payment
  CreditSum Num(19,6) Credit Amount
  CreditCurr nVarChar(3) Credit Currency
  CreditRate Num(19,6) Credit Rate
  ConfNum nVarChar(20) Confirmation Number
  CreditType VarChar(1) Credit Transaction Type default=S [U=Telephone Transaction, S=Regular, I=Internet Transaction]
  CreditDps VarChar(1) Credit Deposit Type default=Y [Y=Manual, N=Automatic]
  Deposited VarChar(1) Paid default=N [Y=Yes, N=No]
  DeposDate Date(8) Payment Date
  RctAbs Int(11) Receipt No. ->ORCT
  DepNum Int(11) Payment Internal ID ->ODPS
  AcctCode nVarChar(15) Account for Payments ->OACT
  CreditAcct nVarChar(15) Credit Account
  CardCode nVarChar(15) BP/Account Code ->OCRD
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  Storno VarChar(1) Cancel Transaction default=N [Y=Yes, N=No]
  RcptLineId Int(11) Row Number in Receipt
  Recived Num(19,6) Received
  Converted VarChar(1) Endorsed default=N [Y=Yes, N=No]
  ConvertTo nVarChar(15) Endorsed for
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  UserSign Int(6) User Signature ->OUSR
  TransRef nVarChar(20) Trans. Reference
  CreateDate Date(8) Creation Date
  ConsolNum Int(11) Vendor Credit Code default=-1
  Project nVarChar(20) Project Code ->OPRJ
  CardName nVarChar(100) BP/Account Name

# OCRV - Credit Payments
Module: Banking | 29 columns | ObjType: 74
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Instance, PayId, AbsId
  CRED_CARD: CreditCard
  CUST_CODE: CardCode
  DEP_ABS1: DepNum
  IS_VALID: Storno, CreditCard, PayId, VoucherNum
  CRED_ACCT: CreditAcct
  DEP_ABS2: DepNum2
  DEPOSITED: Deposited
  VOUCHER_ID: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Seq. No. in Amount ->OCRH
  PayId Int(11) Payment No. default=0
  CreditCard Int(6) Credit Card default=0 ->OCRC
  CrdCardNum nVarChar(64) Credit Card No.
  CardValid Date(8) Credit Card Validity
  VoucherNum nVarChar(27) Voucher Number
  OwnerIdNum nVarChar(15) ID Number
  OwnerPhone nVarChar(20) Telephone
  PayDate Date(8) Payment Date
  PayAmount Num(19,6) Payment Amount
  CreditCurr nVarChar(3) Credit Currency
  CreditRate Num(19,6) Credit Rate
  Deposited VarChar(1) Paid default=O [C=Closed, O=Open, S=Postdated]
  DepNum2 Int(11) Postdated Deposit Key default=0 ->ODPT
  DepNum Int(11) Payment Internal ID ->ODPS
  AcctCode nVarChar(15) Account for Payments ->OACT
  VouchAcct nVarChar(15) Voucher Account ->OACT
  CreditAcct nVarChar(15) Credit Account
  CardCode nVarChar(15) BP/Account Code ->OCRD
  CrTypeCode Int(6) Payment Method Code ->OCRP
  NumOfPmnts Int(6) Number of Payments default=1
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  Storno VarChar(1) Cancel Transaction default=N [Y=Yes, N=No]
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0 ->OCRH
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  TransRef nVarChar(20) Trans. Reference
  CardName nVarChar(100) BP/Account Name

# OCTG - Payment Terms
Module: Banking | 25 columns | ObjType: 40
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupNum
  ABS_ENTRY U: PymntGroup
Fields (name type(len) description [values] ->parent table):
  GroupNum Int(6) Group Number
  PymntGroup nVarChar(100) Payment Terms Code
  PayDuMonth VarChar(1) Start From default=N [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Number of Additional Months default=0
  ExtraDays Int(6) Number of Additional Days default=0
  PaymntsNum Int(6) Number of Payments
  CredLimit Num(19,6) Max. Credit
  VolumDscnt Num(19,6) Total Discount %
  LatePyChrg Num(19,6) Interest % on Receivables
  ObligLimit Num(19,6) Commitment Limit
  ListNum Int(6) Price List ->OPLN
  Payments VarChar(1) Partial Payment default=N [Y=Yes, N=No]
  NumOfPmnts Int(6) Number of Payments default=1
  Payment1 Num(19,6) First Partial Payment
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  OpenRcpt VarChar(1) Open Incoming Payment default=N [N=No, 3=Cash, 1=Checks, 4=Credit, 2=Bank Transfer, 5=Bill of Exchange]
  DiscCode nVarChar(20) Discount Code ->OCDC
  DunningCod nVarChar(20) Dunning Code ->ORIT
  BslineDate VarChar(1) Due Date Based on default=T [P=Posting Date, S=System Date, T=Document Date, C=Closing Date]
  InstNum Int(6) No. of Installments
  TolDays Int(6) No. of Tolerance Days
  VATFirst VarChar(1) Apply Tax on 1st Installment default=N [Y=Yes, N=No, T=Tax Only]
  CrdMthd VarChar(1) Credit Method default=L [F=First Installment, L=Last Installment, E=Equally]
  CshRelev VarChar(1) Cash Relevant Transaction default=N [Y=Yes, N=No]

# ODPS - Deposit
Module: Banking | 64 columns | ObjType: 25
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DeposId
  VIS_NUM U: Series, DeposNum
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DeposId Int(11) Payment Internal ID default=0
  DeposType VarChar(1) Payment Type default=K [K=Check Deposit, C=Cash Payment, V=Credit Deposit, B=Bill of Exchange]
  DeposNum Int(11) Payment No.
  DeposDate Date(8) Payment Date
  DeposCurr nVarChar(3) Currency for Payments
  BanckAcct nVarChar(15) Deposit Account
  DeposAcct nVarChar(50) Bank Account Number
  DeposBrnch nVarChar(50) Branch for Payments
  Memo nVarChar(250) Details
  LocTotal Num(19,6) Total (LC)
  FcTotal Num(19,6) Total (FC)
  SysTotal Num(19,6) Total (SC)
  TransAbs Int(11) Journal Entry Key ->OJDT
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  DocTime Int(6) Pay-In Time
  AllocAcct nVarChar(15) Cash
  ChkType VarChar(1) Check Deposit Type default=C [C=Cash Checks, S=Postdated Checks]
  DpsBank nVarChar(30) Bank Name for Payments
  DpostorNam nVarChar(30) Name of Depositor
  Printed VarChar(1) Original/Copy default=N [Y=Yes, N=No]
  DocRate Num(19,6) Payment Rate
  CrdBankAct nVarChar(15) Voucher Account
  IsCard VarChar(1) Business Partner or Account default=A [A=G/L Account, C=BP]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  UpdateDate Date(8) Date of Update
  Splited VarChar(1) Split default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  VatAct nVarChar(15) Tax Account
  ComissAct nVarChar(15) Commissions Account
  VatTotal Num(19,6) Total Tax
  Comission Num(19,6) Commission
  ComissDate Date(8) Commission Date
  TaxDate Date(8) Document Date
  Series Int(11) Series
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ObjType nVarChar(20) Object Type ->ADP1
  FinncPriod Int(11) Posting Period ->OFPR
  VatTotlSys Num(19,6) Total Tax on Input (SC)
  ComissnSys Num(19,6) Total Commission (SC)
  UserSign Int(6) User Signature ->OUSR
  DepostNorm nVarChar(8) Deposit Norm
  PostType VarChar(1) Transaction Type default=C [C=Collection, D=Discounted]
  BankCountr nVarChar(3) Bank Country ->OCRY
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CnclDps Int(11) Cancel Deposit default=-1
  CommisVat nVarChar(8) Commission VAT Group ->OVTG
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  Project nVarChar(20) Project Code ->OPRJ
  ReconAfter VarChar(1) Reconcile Amounts After Dpst default=Y
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  ComisFC Num(19,6) Total Commission (FC)
  VatTotlFC Num(19,6) Total Tax on Input (FC)
  ComisCurr nVarChar(3) Commission Currency
  SupplCode nVarChar(254) Supplementary Code
  BPLId Int(11) Branch ->OBPL
  SysRate Num(19,6) System Currency Rate

# ODPT - Postdated Deposit
Module: Banking | 36 columns | ObjType: 76
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DeposId
Fields (name type(len) description [values] ->parent table):
  DeposId Int(11) Payment Internal ID default=0
  DeposType VarChar(1) Payment Type default=K [K=Check Deposit, V=Credit Deposit]
  DeposDate Date(8) Payment Date
  DeposCurr nVarChar(3) Currency for Payments
  BanckAcct nVarChar(15) SAP Business One Acct Code f.
  Memo nVarChar(250) Details
  LocTotal Num(19,6) Total (LC)
  FcTotal Num(19,6) Total (FC)
  SysTotal Num(19,6) Total (SC)
  TransAbs Int(11) Journal Entry Key ->OJDT
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  DocRate Num(19,6) Payment Rate
  Splited VarChar(1) Split default=N [Y=Yes, N=No]
  VatAct nVarChar(15) Tax Account
  ComissAct nVarChar(15) Commissions Account
  VatTotal Num(19,6) Total Tax
  Comission Num(19,6) Commission
  ComissDate Date(8) Commission Date
  TaxDate Date(8) Document Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  ObjType nVarChar(20) Object Type ->ADP1
  FinncPriod Int(11) Posting Period ->OFPR
  VatTotlSys Num(19,6) Total Tax on Input (SC)
  ComissnSys Num(19,6) Total Commission (SC)
  UserSign Int(6) User Signature ->OUSR
  CommisVat nVarChar(8) Commission VAT Group ->OVTG
  Project nVarChar(20) Project Code ->OPRJ
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  ComisFC Num(19,6) Total Commission (FC)
  VatTotlFC Num(19,6) Total Tax on Input (FC)
  ComisCurr nVarChar(3) Commission Currency

# ODSC - Bank Codes
Module: Banking | 20 columns | ObjType: 3
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  SECONDARY U: BankCode, CountryCod
Fields (name type(len) description [values] ->parent table):
  BankCode nVarChar(30) Bank Code
  BankName nVarChar(250) Bank Name
  DfltAcct nVarChar(50) Account for Outgoing Checks
  DfltBranch nVarChar(50) Branch for Outgoing Checks
  NextChckNo Int(11) Next Check Number
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SwiftNum nVarChar(50) BIC/SWIFT Code
  IBAN nVarChar(50) IBAN
  CountryCod nVarChar(3) Country Code ->OCRY
  PostOffice VarChar(1) Post Office default=N [Y=Yes, N=No]
  AliasName nVarChar(50) Alias Name
  AbsEntry Int(11) Absolute entry
  DfltActKey Int(11) Default Bank Account Key ->DSC1
  NextNum Int(11) Our Number in Next Boleto
  BsPstDate VarChar(1) Posting Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]
  BsValDate VarChar(1) Due Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]
  BnkOpCode Int(11) Bank Operation Code List ->OBOC
  BsDocDate VarChar(1) Document Date Definition default=C [S=Statement Date, L=Row Date, V=Due Date, C=Current Date]

# ODTY - BoE Document Type
Module: Banking | 3 columns | ObjType: 267
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  TYPE U: DocType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocType nVarChar(2) Document Type
  DocDespt nVarChar(20) Description

# OIPO - Internal Payment Order Number
Module: Banking | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Desc nVarChar(100) Description

# OIST - BoE Instruction
Module: Banking | 4 columns | ObjType: 269
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  CODE U: IsCancel, InstrCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  InstrCode nVarChar(2) Instruction
  InstrDespt nVarChar(128) Description
  IsCancel VarChar(1) Is Cancellation default=N [Y=Yes, N=No]

# OITR - Internal Reconciliation
Module: Banking | 30 columns | ObjType: 321
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ReconNum
Fields (name type(len) description [values] ->parent table):
  ReconNum Int(11) Reconciliation Number
  IsCard VarChar(1) BP or Account [C=BP, A=G/L Account]
  ReconType nVarChar(2) Reconciliation Type [0=Manual, 1=Automatic, 2=Semi-Automatic, 3=Payment, 4=Credit Memo, 5=Reversal, 6=Zero Value, 7=Cancellation, 8=BoE, 9=Deposit, 10=Bank Statement Processing, 11=Period Closing, 12=Correction Invoice, 13=Inventory/Expense Allocation, 14=WIP, 15=Deferred Tax Interim Account, 16=Down Payment Allocation, 17=Auto. Conversion Difference, 18=Interim Document]
  ReconDate Date(8) Reconciliation Date
  Total Num(19,6) Total Reconciliation Amount
  ReconCurr nVarChar(3) Reconciliation Currency ->OCRN
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CancelAbs Int(11) Canceling/-ed Reconciliation default=0 ->OITR
  IsSystem VarChar(1) System or Manual [Y=Yes, N=No]
  InitObjTyp nVarChar(20) Reconc. Initiator Object Type
  InitObjAbs Int(11) Reconc. Initiator Internal ID
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=OB Server, A=Auto Incr., D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ReconRule1 nVarChar(2) Reconciliation Rule 1 [0=Posting Date, 1=Due Date, 2=Document Date, 3=Ref. 1, 4=Ref. 2, 5=Ref. 3, 6=Project Code, 7=Control Account Code, 8=Posting Period]
  ReconRule2 nVarChar(2) Reconciliation Rule 2 [0=Posting Date, 1=Due Date, 2=Document Date, 3=Ref. 1, 4=Ref. 2, 5=Ref. 3, 6=Project Code, 7=Control Account Code, 8=Posting Period]
  ReconRule3 nVarChar(2) Reconciliation Rule 3 [0=Posting Date, 1=Due Date, 2=Document Date, 3=Ref. 1, 4=Ref. 2, 5=Ref. 3, 6=Project Code, 7=Control Account Code, 8=Posting Period]
  IsMultiBP VarChar(1) Multiple BP Reconciliation default=N [N=No, Y=Yes]
  VersionNum nVarChar(11) Version Number
  OldMatNum Int(11) Previous Reconciliation Number default=0
  ReconJEId Int(11) JE no. created by reconciliatn
  BuildDesc nVarChar(50) Build Descriptor
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VATRegNum nVarChar(32) VAT Reg. Number
  IsElectr VarChar(1) Is Electronic default=N [N=No, Y=Yes]
  CreateTS Int(11) Creation Time - Incl. Sec.
  UpdateTS Int(11) Update Full Time
  ObjType nVarChar(20) Object Type default=321

# OMTC - Bank Statement - Matching Criteria
Module: Banking | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  MATCH_TYPE U: RuleIndex, Round, MatchID
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  MatchID Int(6) Form Type Index default=1 [1=Documents, 2=Internal Reconciliation, 3=External Reconciliation]
  Round Int(6) Rounding [1=Round 1, 2=Round 2, 3=Round 3, =]
  MtcRule Int(6) Matching Rule default=0
  MtcAlias nVarChar(18) Matching Alias
  Differnce Int(11) Difference default=0
  DiffAmnt Num(19,6) Amount Difference
  RuleIndex Int(6) Rule Index

# OMTH - Reconciliation History
Module: Banking | 12 columns | ObjType: 26
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: MatchNum, IsInternal, MthAcctCod
Fields (name type(len) description [values] ->parent table):
  MthAcctCod nVarChar(15) Account Code
  IsInternal VarChar(1) Reconciliation Type default=E [I=Internal, E=External]
  MatchNum Int(11) Reconciliation No.
  Totals Num(19,6) Recon. Amount (One Side)
  IsCard VarChar(1) Select BP or Account default=A [A=G/L Account, C=BP]
  MatchType nVarChar(2) Reconciliation Type default=0 [0=Manual, 1=Ref. 1, 2=Ref. 2, 3=Ref. 3, 4=Posting Date, 5=Due Date, 6=Ref. 1 + Posting Date, 7=Ref. 2 + Posting Date, 8=Ref. 3 + Posting Date, 9=Ref. 1 + Due Date, 10=Ref. 2 + Due Date, 11=Ref. 3 + Due Date, 12=By Total]
  TransId Int(11) Reconciliation Transaction No. default=-1
  MatchDate Date(8) Reconciliation Date
  CurrType nVarChar(3) Currency Type
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  createDate Date(8) Creation Date

# OPBD - Document Type
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Code
  Descriptio nVarChar(254) Document Type Description
  Default VarChar(1) Default default=N [Y=Yes, N=No]

# OPBU - Budget ID
Module: Banking | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(100) Budget ID Code
  Default VarChar(1) Default Value default=N [Y=Yes, N=No]

# OPDF - Payment Draft
Module: Banking | 183 columns | ObjType: 140
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM: PIndicator, DocNum
  CARD: CardCode
  HANDWRITEN: Handwrtten
  CANCELED: Canceled
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Numerator
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type [C=Customer, A=Account, S=Vendor, P=P.L.A, D=TDS]
  Canceled VarChar(1) Canceled [Y=Yes, N=No]
  Handwrtten VarChar(1) Manual Numbering [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Copy, N=Original]
  DocDate Date(8) Posting Date
  DocDueDate Date(8) Value Date
  CardCode nVarChar(15) Customer/Vendor Code
  CardName nVarChar(100) Customer/Vendor Name
  Address nVarChar(254) Address
  DdctPrcnt Num(19,6) Deduction Percent
  DdctSum Num(19,6) Total Deductions
  DdctSumFC Num(19,6) Total Deductions in FC
  CashAcct nVarChar(15) Cash Account ->OACT
  CashSum Num(19,6) Cash Amount
  CashSumFC Num(19,6) Cash Amount in FC
  CreditSum Num(19,6) Credit Amount
  CredSumFC Num(19,6) Credit Amount in FC
  CheckAcct nVarChar(15) Current Account ->OACT
  CheckSum Num(19,6) Check Amount
  CheckSumFC Num(19,6) Check Amount in FC
  TrsfrAcct nVarChar(15) Transfer Account ->OACT
  TrsfrSum Num(19,6) Transfer Amount
  TrsfrSumFC Num(19,6) Transfer Amount in FC
  TrsfrDate Date(8) Transfer Date
  TrsfrRef nVarChar(27) Intended Purpose
  PayNoDoc VarChar(1) Non-Calculated Payment default=N [Y=Yes, N=No]
  NoDocSum Num(19,6) Non-Calculated Amount
  NoDocSumFC Num(19,6) Non-Calculated Amount in FC
  DocCurr nVarChar(3) Document Currency ->OCRN
  DiffCurr VarChar(1) Enter in local currency default=N [N=No, Y=Yes]
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Price
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total in FC
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
  CashSumSy Num(19,6) Cash Amount in SC
  CredSumSy Num(19,6) System Credit Amount
  CheckSumSy Num(19,6) Check Amount in SC
  TrsfrSumSy Num(19,6) Transfer Amount in SC
  NoDocSumSy Num(19,6) Non-Invoiced System Amount
  DocTotalSy Num(19,6) Document Total in SC
  ObjType nVarChar(20) Object Type [24=Incoming Payment, 46=Outgoing Payments] ->ADP1
  StornoRate Num(19,6) Cancellation Rate
  UpdateDate Date(8) Update Date
  CreateDate Date(8) Creation Date
  ApplyVAT VarChar(1) Tax Definition default=N [Y=Yes, N=No]
  TaxDate Date(8) Tax Date
  Series Int(11) Series ->NNM1
  confirmed VarChar(1) Approved default=N [Y=Yes, N=No]
  ShowJDT VarChar(1) Display Journal Entries [Y=Yes, N=No]
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
  SpltCredLn VarChar(1) Split Vendor Credit Row [Y=Yes, N=No]
  PrjCode nVarChar(20) Project ->OPRJ
  PaymentRef nVarChar(27) Payment Reference
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
  WtCode nVarChar(4) WT Code ->OWHT
  WtSum Num(19,6) WT Amount
  WtSumFrgn Num(19,6) WT Amount (FC)
  WtSumSys Num(19,6) WT Amount (SC)
  WtAccount nVarChar(15) WT Account ->OACT
  WtBaseAmnt Num(19,6) WT Taxable Amount
  Proforma VarChar(1) Proforma default=N [Y=Yes, N=No]
  BoeAbs Int(11) Boe Key ->OBOE
  BpAct nVarChar(15) BP Account ->OACT
  BcgSum Num(19,6) Bank Charge Amount
  BcgSumFC Num(19,6) Bank Charge Amount in FC
  BcgSumSy Num(19,6) Bank Charge Amount in SC
  PIndicator nVarChar(10) Period Indicator ->OPID
  PaPriority VarChar(1) Payment Priority default=6 [1=, 2=, 3=, 4=, 5=, 6=]
  PayToCode nVarChar(50) Pay to
  IsPaytoBnk VarChar(1) Is Pay to Bank default=N [N=No, Y=Yes]
  PBnkCnt nVarChar(3) Pay to Bank Country ->OCRY
  PBnkCode nVarChar(30) Pay to Bank Code
  PBnkAccnt nVarChar(50) Pay to Bank Account No.
  PBnkBranch nVarChar(50) Pay to Bank Branch
  WizDunBlck VarChar(1) Wizard Dunning Block default=N [N=No., Y=YES]
  WtBaseSum Num(19,6) Wt Base Sum
  WtBaseSumF Num(19,6) Wt Base Sum (FC)
  WtBaseSumS Num(19,6) Wt Base Sum (SC)
  UndOvDiff Num(19,6) Under/Overpayment Difference
  UndOvDiffS Num(19,6) Under/Overpayment Diff. (SC)
  BankActKey Int(11) Bank Account Internal ID ->DSC1
  VersionNum nVarChar(11) Version Number
  VatDate Date(8) Tax Date
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
  OperatCode VarChar(1) Operation Code [A=Summary Invoices Entry, B=Summary Receipts Entry, C=Invoice with Several VAT Rates, D=Correction Invoice, E=Due VAT Pending Invoice Issuance, F=Expenses Incurred by Travel Agent for Customers, G=Special Regulation for VAT Group, H=Special Regulation for Gold Investment, I=Reverse Charge Procedure, J=Unsummarized Receipts, K=Identification of Error Transactions, X=Transactions with Entrepreneurs Issuing Receipts for Agricultural Compensation, N=Service Invoicing by Travel Agencies on Behalf of Third Parties, R=Business Office Rental, S=Subsidies, T=Incoming Payments for Industrial and Intellectual Property Rights, U=Insurance Transactions, V=Purchases from Travel Agencies, W=Transactions Subject to Production, Service and Import Taxes in Ceuta and Melilla]
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

# OPEX - Payment Results Table
Module: Banking | 139 columns | ObjType: 158
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PayRunDate Date(8) Date of Payment Run
  VendorNum nVarChar(15) Vendor Code
  CustNum nVarChar(15) Customer Code
  PaymMethod nVarChar(15) Payment Means
  PaymDocNum Int(11) Payment Document No.
  FiscalYear Date(8) Fiscal Year
  Country nVarChar(3) Company Country
  CompTaxNum nVarChar(32) Company Tax Number
  PayeeName nVarChar(100) Payee Name
  PayeeZip nVarChar(20) Payee Zip Code
  PayeeCity nVarChar(100) Payee City
  PayeeStree nVarChar(100) Payee Street
  PayCountry nVarChar(3) Payee Country
  PayeeState nVarChar(3) Payee State
  PayBnkName nVarChar(250) Payee Bank Name
  PayBankZip nVarChar(20) Payee Bank Zip Code
  PayBnkCity nVarChar(100) Payee Bank City
  PayBnkStr nVarChar(100) Payee Bank Street
  PayBnkCntr nVarChar(3) Payee Bank Country
  PayBankAct nVarChar(50) Payee Bank Account
  PayBnkCode nVarChar(30) Payee Bank Code
  PayBnkCtrl nVarChar(2) Payee Bank Control Number
  PayBnkSwif nVarChar(50) Payee Bank BIC/SWIFT Code
  PayBnkIBAN nVarChar(50) Payee Bank IBAN
  PymPostDat Date(8) Payment Posting Date
  PymBnkAcct nVarChar(50) Payment Bank Account
  PymBnkCntr nVarChar(3) Payment Bank Country
  PymBnkCode nVarChar(30) Payment Bank Code
  PymBnkIBAN nVarChar(50) Payment Bank IBAN
  PymGLAcct nVarChar(15) Payment G/L Account
  Currency nVarChar(3) Main Currency
  PymDocAmnt Num(19,6) Payment Document Amount (LC)
  PymDocCurr nVarChar(3) Payment Document Currency
  PymDcAmtFC Num(19,6) Payment Document Amount (FC)
  PymCshDsct Num(19,6) Cash Discount in Payment Doc
  PyCshDscFC Num(19,6) Cash Discount in Payment Doc
  PymNumOfPa Int(11) Number of Items Paid
  PymDocRate Num(19,6) Payment Document Exchange Rate
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  PaymWizCod Int(11) Payment Wizard Code ->OPWZ
  InstrucKey nVarChar(30) Instruction Key
  CllctAutho VarChar(1) Collection Authorization
  PayBnkPost VarChar(1) Payee Bank Post Office
  PayBnkChNo Int(11) Payee Bank Next Check No.
  PayBnkHsBk VarChar(1) Payee Bank House Bank default=N [N=No, Y=Yes]
  PayBnkBlck nVarChar(100) Payee Bank Block
  PayBnkCnty nVarChar(100) Payee Bank County
  PayBnkStat nVarChar(3) Payee Bank State
  PayBnkBISR VarChar(1) Payee Bank BISR default=N [N=No, Y=Yes]
  PayBnkUsr1 nVarChar(25) Payee Bank User No. 1
  PayBnkUsr2 nVarChar(25) Payee Bank User No. 2
  PayBnkUsr3 nVarChar(25) Payee Bank User No. 3
  PayBnkUsr4 nVarChar(25) Payee Bank User No. 4
  PaymFormat nVarChar(20) Payment Format
  CompName nVarChar(100) Company Name
  CompAddres nVarChar(254) Company Address
  CompISRBil nVarChar(9) Company ISR Biller ID
  VendISRBil nVarChar(9) Vendor ISR Biller ID
  AddIdNum nVarChar(32) Additional ID No.
  CompOrgNum nVarChar(50) Company Organization No.
  PayBnkBrnc nVarChar(50) Payee Bank Branch
  PymBnkBrnc nVarChar(50) Payment Bank Branch
  UserName nVarChar(155) User Name
  UserEmail nVarChar(100) User E-Mail
  UserPortNo nVarChar(50) User Mobile Phone No.
  UserFax nVarChar(20) User Fax No.
  Department Int(6) User Department
  DebitMemo VarChar(1) Debit Memo default=N [N=No, Y=Yes]
  EuInTrnsfr VarChar(1) EU Internal Transfer default=N [N=No, Y=Yes]
  FilePath Text(16) File Path
  OrderParty nVarChar(30) Ordering Party
  PymCtrlKey nVarChar(2) Payment Bank Control Number
  PayeeTaxNo nVarChar(32) Payee Tax Number
  PymKeyCode nVarChar(6) Payment Key Code
  PayRefDtls nVarChar(20) Payee Reference Details
  FormatName nVarChar(100) Format Name
  CheckPmnt VarChar(1) Payment Done with Check default=N [N=No, Y=Yes]
  PymBnkUsr1 nVarChar(25) Payment Bank User No. 1
  PymBnkUsr2 nVarChar(25) Payment Bank User No. 2
  PymBnkUsr3 nVarChar(25) Payment Bank User No. 3
  PymBnkUsr4 nVarChar(25) Payment Bank User No. 4
  CompStreet nVarChar(100) Company Street
  CompBlock nVarChar(100) Company Block
  CompCity nVarChar(100) Company City
  CompZip nVarChar(20) Company Zip Code
  CompCounty nVarChar(100) Company County
  CompState nVarChar(3) Company State ->OCST
  PymBCACode nVarChar(3) Payment Bank Charges ->OBCA
  PaymDocTyp nVarChar(20) Payment Document Object Type
  PayOrderNo Int(11) Payment Order Number ->OIPO
  FreeText1 nVarChar(100) Free Text 1
  FreeText2 nVarChar(100) Free Text 2
  FreeText3 nVarChar(100) Free Text 3
  PymBnkSwif nVarChar(50) Payment Bank Swift Code
  PayBnkUIC nVarChar(3) Payee Bank UIC Code
  LineType VarChar(1) Line Type default=G [G=General, O=Pay on Account, T=Pay to Account]
  BoeKey Int(11) Bill of Exchange Key ->OBOE
  BoeCurrSta VarChar(1) BoE Current Status
  BoeDate Date(8) Bill of Exchange Date
  BoeDueDate Date(8) BoE Due Date
  Instruct1 nVarChar(2) BoE Instruction 1
  Instruct2 nVarChar(2) BoE Instruction 2
  BoeCancIns nVarChar(2) BoE Cancel Instruction
  BoeOccCode nVarChar(2) BoE Occurrence Code
  BoePtfID nVarChar(3) BoE Internal Portfolio ID
  BoeOurNum Int(11) Our Number in Next BoE
  BoeIntrAm Num(19,6) BoE Interest Amount
  BoeDiscD Date(8) BoE Discount Date
  BoeDisAmnt Num(19,6) BoE Discount Amount
  BoeFineD Date(8) BoE Fine Date
  BoeFineAmt Num(19,6) BoE Fine Amount
  BoeIntrstD Date(8) BoE Interest Date
  BoeIOFAmt Num(19,6) BoE IOF Amount
  BoeMovCode nVarChar(10) BoE Movement Code
  BarcodeRep nVarChar(100) Barcode Representation
  PONumber Int(11) External Payment Order Number
  POSeries Int(11) External Payment Order Series
  PaPriority VarChar(1) Payment Priority default=6 [1=, 2=, 3=, 4=, 5=, 6=]
  PaymType VarChar(1) Payment Type default=N [N=, E=Electronic, P=Mail, T=Telegraph, X=Express]
  RecipStatu nVarChar(2) Recipient Status
  BudegetId nVarChar(100) VAT Budget Classification Code
  OKATO nVarChar(11) OKATO
  PymReason nVarChar(2) Payment Reason
  PostPeriod nVarChar(10) Posting Period Code
  BaseDocTyp nVarChar(2) Base Document Type
  BaseDocDat Date(8) Base Document Date
  TaxPymType nVarChar(2) Tax Payment Type
  OKTMO nVarChar(12) OKTMO
  SeqType nVarChar(4) Sequence Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  PymDate Date(8) Payment Date
  PymBnkName nVarChar(250) Payment Bank Name
  UIPCode nVarChar(25) UIP Code
  UserId Int(6) User ID ->OUSR
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]
  EnBnkAct Text(16) Encryption of Payee Bank Acct
  EnBnkIBan Text(16) Encryption of Payee Bank IBAN
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# OPFT - Portfolio Definitions
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(50) Name
  Type VarChar(1) Type default=C [C=Cheque, B=Bill of Exchange]

# OPOI - Incoming Payment Order
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Number Int(11) Number
  Series Int(11) Series

# OPOO - Outgoing Payment Order
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Number Int(11) Number
  Series Int(11) Series

# OPPT - Payment Type
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Code
  Descriptio nVarChar(254) Payment Type Description
  Default VarChar(1) Default Value default=N [Y=Yes, N=No]

# OPRS - Tax Payer Status
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Code
  Descriptio nVarChar(254) Description
  Default VarChar(1) Default default=N [Y=Yes, N=No]

# OPTF - BoE Portfolio
Module: Banking | 5 columns | ObjType: 268
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  ID U: PtfId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PtfId nVarChar(3) Internal Portfolio ID
  PtfCode nVarChar(2) Portfolio Code
  PtfNum nVarChar(4) Portfolio Number
  PtfDespt nVarChar(20) Description

# OPWB - PWZ - Bank Account
Module: Banking | 46 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  COUNTRY U: PWZAbsEntr, Account, BankCode, Country
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  CardCode nVarChar(15) BP Code ->OCRD
  BankCode nVarChar(30) Bank Code
  Country nVarChar(3) Country ->OCRY
  Account nVarChar(50) Account No.
  Branch nVarChar(50) Branch
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  State nVarChar(3) State
  ControlKey nVarChar(2) Ctrl Internal ID
  UsrNumber1 nVarChar(25) User No. 1
  UsrNumber2 nVarChar(25) User No. 2
  UsrNumber3 nVarChar(25) User No. 3
  UsrNumber4 nVarChar(25) User No. 4
  IBAN nVarChar(50) IBAN
  LogInstanc Int(11) Log Instance default=0
  Building Text(16) Building/Floor/Room
  AliasName nVarChar(50) Alias Name
  AcctType VarChar(1) Account Type
  BankKey Int(11) Bank Internal ID ->ODSC
  BIK nVarChar(15) BIK
  AcctName nVarChar(250) Bank Account Name
  CorresAcct nVarChar(30) Correspondent Account
  Phone nVarChar(25) Phone
  Fax nVarChar(25) Fax
  ISRType Int(6) ISR Type default=2 [1=ISR, 2=BISR, 3=ISR+, 4=BISR+]
  ISRBillerI nVarChar(9) ISR Biller ID
  CustIdNum nVarChar(6) Customer ID Number default=0
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  SwiftNum nVarChar(50) BIC/SWIFT Code
  ABARoutNum nVarChar(25) ABA Routing Number
  MandateID nVarChar(35) Mandate ID
  SignDate Date(8) Date of Signature
  PWZAbsEntr Int(11) PWZ ABS Entry ->OPWZ
  BranchChk nVarChar(5) Branch Check Digit
  MandatDate Date(8) Date Of Mandate Expiration
  SeqType nVarChar(4) SEPA Seq. Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  ActType VarChar(1) Account Type [C=Checking Account, S=Savings Account]
  IsPrenot VarChar(1) Is Prenotification default=N [Y=Yes, N=No]
  EnAccount Text(16) Encryption of Account
  EnIBAN Text(16) Encryption of IBAN
  EncryptIV nVarChar(100) Encrypt IV

# OPWZ - Payment Wizard
Module: Banking | 75 columns | ObjType: 157
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: IdNumber
  NAME U: WizardName
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) ID Number
  PmntDate Date(8) Date of Payment Run
  NextDate Date(8) A/P Due Date To
  OutgoType VarChar(1) Outgoing Type default=N [Y=Yes, N=No]
  IncomType VarChar(1) Incoming Type default=N [Y=Yes, N=No]
  CheckPmntM VarChar(1) Check Payment Terms default=N [Y=Yes, N=No]
  BnkTrnsPmM VarChar(1) Bank Transfer Payment Terms default=N [Y=Yes, N=No]
  FilePath Text(16) File Path
  PostDtFrom Date(8) Posting Date From
  PostDtTo Date(8) Posting Date To
  ValDteFrom Date(8) Due Date From
  ValDateTo Date(8) Due Date To
  ApInvAmntF Num(19,6) A/P Invoice Amount From
  ApInvAmntT Num(19,6) A/P Invoice Amount To
  PchNoFrom Int(11) A/P Invoice No. From
  PchNoTo Int(11) A/P Invoice No. To
  InvNoFrom Int(11) A/R Invoice No. From
  InvNoTo Int(11) A/R Invoice No. To
  SelPriorit Int(11) Selection Priority
  Status VarChar(1) Object Status default=S [S=Saved Wizard, R=Recommended Wizard, E=Executed Wizard, H=Scheduled Wizard, L=Scheduled Executing Wizard]
  WizardName nVarChar(100) Wizard Name
  StatusDisc nVarChar(100) Status
  Canceled VarChar(1) Canceled default=N
  BoePmnMn VarChar(1) Bill of Exchange Paymt Method default=N [Y=Yes, N=No]
  SeriesOut Int(11) Outgoing Series default=0 ->NNM1
  SeriesIn Int(11) Incoming Series default=0 ->NNM1
  TotalOut Num(19,6) Total Outgoing
  TotalIn Num(19,6) Total Incoming
  ViewIntBal VarChar(1) Include Interim Acct Balance default=N [Y=Yes, N=No]
  SelMthd VarChar(1) Selection Method default=D [M=By Monthly Invoice, D=By Document Property]
  MINumFrom Int(11) Monthly Invoice No. From
  MINumTo Int(11) Monthly Invoice No. To
  MIDateFrom Date(8) Monthly Invoice Issued Date From
  MIDateTo Date(8) Monthly Invoice Issued Date To
  MIVNumFrom Int(11) A/P Monthly Invoice No. From
  MIVNumTo Int(11) A/P Monthly Invoice No. To
  MIVDateFro Date(8) A/P Monthly Invoice Date From
  MIVDateTo Date(8) A/P Monthly Invoice Date To
  APDocDtFrm Date(8) A/P Document Date From
  APDocDtTo Date(8) A/P Document Date To
  APDueDtFrm Date(8) A/P Due Date From
  NxtPmntDat Date(8) Next Payment Run Date
  MinPayAR Num(19,6) Minimum Incoming Payment
  MinPayAP Num(19,6) Minimum Outgoing Payment
  ShowAtCard VarChar(1) Display BP Ref. No. default=N [Y=Yes, N=No]
  TolerDays Int(6) Tolerance Days
  MinCashDis Num(19,6) Min. Cash Discount
  NegBalBP VarChar(1) Include Negative Balance BP default=N [Y=Yes, N=No]
  ManualJE VarChar(1) Include Manual JEs default=Y [Y=Yes, N=No]
  NegTrans VarChar(1) Include Negative Transactions default=Y [Y=Yes, N=No]
  CDTransApp VarChar(1) Apply to Cash Discount Trans. default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  CigTo Int(11) Contract Code ID To ->OCIG
  CupFrom Int(11) Unique Code of Project From ->OCUP
  CupTo Int(11) Unique Code of Project To ->OCUP
  CigFrom Int(11) Contract Code ID From ->OCIG
  BPLId Int(11) Active Branch ->OBPL
  BoeDDFrom Date(8) BoE Due Date From
  BoeDDTo Date(8) BoE Due Date To
  BoeNumFrom Int(11) BoE No. From ->OBOE
  BoeNumTo Int(11) BoE No. To ->OBOE
  BoeStatus nVarChar(32) Bill of Exchange Status
  HaExistBoe VarChar(1) Handle Existing BoE default=N [Y=Yes, N=No]
  SeriesPOO Int(11) Outgoing Payment Order Series default=0 ->NNM1
  SeriesPOI Int(11) Incoming Payment Order Series default=0 ->NNM1
  SeqType nVarChar(4) Sequence Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  PayDueDate VarChar(1) Payment Due Date Determination default=R [R=Run Date, D=Document Due Date]
  CentrPay VarChar(1) Centralized Payment default=N [Y=Yes, N=No]
  BA_AP_From Int(11) A/P Blanket Agreement From
  BA_AP_To Int(11) A/P Blanket Agreement To
  BA_AR_From Int(11) A/R Blanket Agreement From
  BA_AR_To Int(11) A/R Blanket Agreement To
  JobId Int(11) Job ID Number
  ZeroBalBP VarChar(1) Include Zero Balance BP default=Y [Y=Yes, N=No]
  ZeroBalDoc nVarChar(50) Zero Balance Document Types default=YNNNNYNNNNN

# OPYB - Payment Block
Module: Banking | 2 columns | ObjType: 159
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  PAYBLOCK U: PayBlock
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PayBlock nVarChar(50) Payment Block

# OPYD - Payment Run
Module: Banking | 8 columns | ObjType: 155
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Payment Run Code
  Name nVarChar(50) Payment Run Name
  TolerDays Int(6) Tolerance Days
  MinCashDis Num(19,6) Min. Cash Discount
  UseMinPay VarChar(1) Use Minimum Payment default=N [Y=Yes, N=No]
  MinPayAR Num(19,6) Minimum Incoming Payment
  MinPayAP Num(19,6) Minimum Outgoing Payment
  ArePayMeth VarChar(1) Payment Terms default=N [Y=Yes, N=No]

# OPYM - Payment Methods for Payment Wizard
Module: Banking | 63 columns | ObjType: 147
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PayMethCod
Fields (name type(len) description [values] ->parent table):
  PayMethCod nVarChar(15) Payment Method Code
  Descript nVarChar(100) Description
  Type VarChar(1) Type [O=Outgoing, I=Incoming]
  BankTransf VarChar(1) Payment Means [C=Check, T=Bank Transfer, B=Bill of Exchange]
  Address VarChar(1) Check Address default=N [Y=Yes, N=No]
  BankDet VarChar(1) Check Bank Details default=N [Y=Yes, N=No]
  CllctAutor VarChar(1) Check Collection Authorization default=N [Y=Yes, N=No]
  FrgnPmntBl VarChar(1) Block Foreign Payment default=N [Y=Yes, N=No]
  FrgnBnkBl VarChar(1) Block Foreign Bank default=N [Y=Yes, N=No]
  CurrRestr VarChar(1) Currency Restriction default=N [Y=Yes, N=No]
  PostOffBnk VarChar(1) Post Office Bank default=N [Y=Yes, N=No]
  MinAmount Num(19,6) Minimum Amount
  MaxAmount Num(19,6) Maximum Amount
  BnkDflt nVarChar(30) Default Bank
  UserSign Int(6) User Signature ->OUSR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  CreateDate Date(8) Creation Date
  BankCountr nVarChar(3) Bank Country ->OCRY
  DflAccount nVarChar(50) Default Bank Account
  GLAccount nVarChar(15) G/L Account ->OACT
  Branch nVarChar(50) Bank Branch
  KeyCode nVarChar(6) Key Code
  TrnsType nVarChar(2) Transaction Type
  Format nVarChar(11) File Format ->OFRM
  AgtCollect VarChar(1) Agent Collection default=N [Y=Yes, N=No]
  SendAccept VarChar(1) Send for Acceptance default=N [Y=Yes, N=No]
  GrpByDate VarChar(1) Group By Date default=N [Y=Yes, N=No]
  DepNorm nVarChar(8) Deposit Norm
  DebitMemo VarChar(1) Debit Memo default=N [N=No, Y=Yes]
  GroupPmRef VarChar(1) Group by Payment Reference No. default=N [Y=Yes, N=No]
  GroupInv VarChar(1) Group Invoices by Pay default=N [N=No, Y=Yes]
  ValDateSel VarChar(1) Due Date Selection default=P [P=Date of Payment Run, I=Due Date of Invoice, T=Payment Terms]
  PaymTerms Int(6) Payment Terms Code ->OCTG
  IntrimAcct VarChar(1) Post to G/L Interim Account default=N [N=No, Y=Yes]
  BnkActKey Int(11) Bank Account Key ->DSC1
  DocType nVarChar(2) BoE Document Type
  Accepted VarChar(1) BoE Status - Accepted
  PtfID nVarChar(3) BoE Internal Portfolio ID
  PtfCode nVarChar(2) BoE Portfolio Code
  PtfNum nVarChar(4) BoE Portfolio Number
  CurCode nVarChar(2) BoE Currency Code
  Instruct1 nVarChar(2) BoE Instruction 1
  Instruct2 nVarChar(2) BoE Instruction 2
  PaymntPlc nVarChar(128) BoE Payment Place
  BoeDll nVarChar(50) Bar Code DLL
  BankCtlKey nVarChar(2) Bank Control No.
  Active VarChar(1) Status of the Payment Method default=Y [Y=Active, N=Inactive]
  BcgPcnt Num(19,6) Bank Charge Rate (%)
  GrpByCur VarChar(1) Group Invoices by Currency default=N [N=No, Y=Yes]
  GrpByBank VarChar(1) Group Invoices by Pay-To Bank default=N [Y=Yes, N=No]
  DflIBAN nVarChar(50) Bank IBAN
  DflSwift nVarChar(50) Bank BIC/SWIFT
  BoeReport nVarChar(8) BoE Report Code
  CancInstr nVarChar(2) Cancellation Instruction
  OccurCode nVarChar(2) Occurrence Code
  MovmntCode nVarChar(10) Movement Code
  NegPymCode nVarChar(15) Negative Payment Method Code ->OPYM
  DirectDbt nVarChar(5) Direct Debit [CORE=, B2B=, COR1=]
  IssueIndic VarChar(1) Issue Indicator default=R [3=, R=]
  PrintSEPA VarChar(1) Print SEPA Prenotification default=N [Y=Yes, N=No]
  PmntType nVarChar(50) Payment Type default=01 [01=Efectivo, 02=Cheque nominativo, 03=Transferencia electrónica de fondos, 04=Tarjeta de crédito, 05=Monedero electrónico, 06=Dinero electrónico, 08=Vales de despensa, 12=Dación en pago, 13=Pago por subrogación, 14=Pago por consignación, 15=Condonación, 17=Compensación, 23=Novación, 24=Confusión, 25=Remisión de deuda, 26=Prescripción o caducidad, 27=A satisfacción del acreedor, 28=Tarjeta de débito, 29=Tarjeta de servicios, 30=Aplicación de anticipos, 99=Por definir]
  GrpByAgrNo VarChar(1) Group Blanket Agreement default=N [Y=Yes, N=No]
  SpltPmtVAT VarChar(1) Split Payments for VAT default=N [Y=Yes, N=No]

# OPYR - Payment Reason
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Code
  Descriptio nVarChar(254) Payment Reason Description
  Default VarChar(1) Default Value default=N [Y=Yes, N=No]

# ORCT - Incoming Payment
Module: Banking | 183 columns | ObjType: 24
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
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

# OROC - Retorno Operation Codes
Module: Banking | 8 columns | ObjType: 1320000028
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  OccurCode Int(11) Occurrence Code
  MovemnCode Int(6) Movement Code
  BoeStatus VarChar(1) BoE Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, L=Closed, F=Failed, V=BoE to Vendor]
  Descript nVarChar(254) Description
  Color Int(11) Color
  FileFormat nVarChar(100) File Format
  BankCode nVarChar(30) Bank Code

# ORTW - Boleto Retorno Wizard: Parameter Sets
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WDueDtFrom Date(8) Due Date From
  WDueDtTo Date(8) Due Date To
  WImpFile Text(16) Import File
  WMatching Int(11) Boleto Matching
  WBoletosAu Int(11) Boletos Automatic Count
  WBoletosMn Int(11) Boletos Manual Count
  WBoletosNI Int(11) Boletos Not Identified Count
  WRelDate Date(8) Release Date
  WCollDisc Int(11) Collection or Discounted
  WBankAcc1 nVarChar(50) Bank Acct No. 1
  WBankAcc2 nVarChar(50) Bank Acct No. 2
  WFileForm2 nVarChar(50) File Format 2

# OSVR - Saved Reconciliations
Module: Banking | 6 columns | ObjType: 230
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: acctCode
Fields (name type(len) description [values] ->parent table):
  acctCode nVarChar(15) Account Code
  endBalanc Num(19,6) Bank Statement Ending Balance
  endDate Date(8) Bank Statement Ending Date
  statemntNo Int(11) Bank Statement Number
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date

# OTPW - Tax Payment Wizard
Module: Banking | 17 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  NAME U: WizName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  WizNumber Int(11) Wizard Number
  WizName nVarChar(50) Wizard Name
  WizStatus VarChar(1) Wizard Status default=S [S=Saved, E=Executed]
  CreateDate Date(8) Wizard Creation Date
  SaveDate Date(8) Wizard Save Date
  ExecDate Date(8) Wizard Execution Date
  UserSign Int(6) User Signature
  Series Int(11) Wizard Series
  JETransId Int(11) Journal Entry Number ->OJDT
  WizDate Date(8) Wizard Date
  RG23APart2 Int(11) RG23A Part 2
  RG23CPart2 Int(11) RG23C Part 2
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String

# OUBR - Branches
Module: Banking | 4 columns | ObjType: 118
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(20) Branches Name
  Remarks nVarChar(100) Description
  UserSign Int(6) User Signature ->OUSR

# OUDP - Departments
Module: Banking | 5 columns | ObjType: 119
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(20) Departments Name
  Remarks nVarChar(100) Description
  UserSign Int(6) User Signature ->OUSR
  Father nVarChar(20) Parent Department

# OVPM - Outgoing Payments
Module: Banking | 183 columns | ObjType: 46
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: DocEntry
  NUM U: PIndicator, DocNum
  CARD: CardCode
  HANDWRITEN: Handwrtten
  CANCELED: Canceled
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  DocType VarChar(1) Document Type default=S [C=Customer, A=Account, S=Vendor, P=P.L.A, T=Tax, D=TDS]
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
  ShowAtCard VarChar(1) Display Vendor Ref. No. default=N [Y=Yes, N=No]
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
  ObjType nVarChar(20) Object Type default=46 [46=Outgoing Payments] ->ADP1
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
  PayToCode nVarChar(50) Pay To
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
  BankActKey Int(11) Bank Account No. ->DSC1
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
  OperatCode VarChar(1) Operation Code [A=Summary Invoices Entry, B=Summary Receipts Entry, C=Invoice with Several VAT Rates, D=Correction Invoice, E=Due VAT Pending Invoice Issuance, F=Expenses Incurred by Travel Agent for Customers, G=Special Regulation for VAT Group, H=Special Regulation for Gold Investment, I=Reverse Charge Procedure, J=Unsummarized Receipts, K=Identification of Error Transactions, X=Transactions with Entrepreneurs Issuing Receipts for Agricultural Compensation, N=Service Invoicing by Travel Agencies on Behalf of Third Parties, R=Business Office Rental, S=Subsidies, T=Incoming Payments for Industrial and Intellectual Property Rights, U=Insurance Transactions, V=Purchases from Travel Agencies, W=Transactions Subject to Production, Service and Import Taxes in Ceuta and Melilla]
  UndOvDiffF Num(19,6) Under/Overpayment Diff. (FC)
  MIEntry Int(11) MI Entry Include this Payment default=0
  FreeText1 nVarChar(100) Free Text 1
  FreeText2 nVarChar(100) Free Text 2
  FreeText3 nVarChar(100) Free Text 3
  ShowDocNo VarChar(1) Display Document No. default=Y [Y=Yes, N=No]
  TDSInterst Num(19,6) TDS Interest
  TDSCharges Num(19,6) TDS Other Charges
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

# PDF1 - Payment Draft - Checks
Module: Banking | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OPDF
  LineID Int(11) Row Number
  DueDate Date(8) Check Date
  CheckNum Int(11) Check Number
  BankCode nVarChar(30) Account No. default=-1
  Branch nVarChar(50) Branch Number
  AcctNum nVarChar(50) Account Number
  Details nVarChar(254) Details
  Trnsfrable VarChar(1) Negotiable default=N [Y=Yes, N=No]
  CheckSum Num(19,6) Check Amount
  Currency nVarChar(3) Check Currency ->OCRN
  Flags Int(11) Flags default=0
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  CountryCod nVarChar(3) Country Code ->OCRY
  CheckAct nVarChar(15) Checking Account ->OACT
  CheckAbs Int(11) Check ID Entry ->OCHO
  BnkActKey Int(11) Bank Account Internal ID ->DSC1
  ManualChk VarChar(1) Manual Check default=N [N=No, Y=Yes]
  FiscalID nVarChar(100) Fiscal ID
  OrigIssdBy nVarChar(254) Orginally Issued By
  Endorse VarChar(1) Endorse default=N [Y=Yes, N=No]
  EndorsChNo Int(11) Endorsable Check No. ->OCHH
  EnAcctNum Text(16) Encryption of Account Number
  EncryptIV nVarChar(100) Encrypt IV

# PDF2 - Payment Draft - Invoices
Module: Banking | 63 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InvoiceId, DocNum
  JDT: DocLine, DocTransId
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OPDF
  InvoiceId Int(11) Sequence No.
  DocEntry Int(11) Invoice Key
  SumApplied Num(19,6) Paid to Invoice
  AppliedFC Num(19,6) Paid in FC
  AppliedSys Num(19,6) Paid in SC
  InvType nVarChar(20) Invoice Category default=13 [203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 25=Deposit, 46=Payment Advice, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, -1=All Transactions, 163=A/P Correction Invoice, 165=A/R Correction Invoice, 0=]
  DocRate Num(19,6) Document Rate
  Flags Int(11) Flags default=0
  IntrsStat VarChar(1) Interest Letter Status default=U [U=Not Sent, S=Sent, C=Closed]
  DocLine Int(11) Row Key default=0
  vatApplied Num(19,6) Tax Definition
  vatAppldFC Num(19,6) Tax Paid in FC
  vatAppldSy Num(19,6) Tax Paid in SC
  selfInv VarChar(1) Autom. Invoice default=N [N=No, Y=Yes]
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  Dcount Num(19,6) Discount %
  DcntSum Num(19,6) Discount Amount
  DcntSumFC Num(19,6) Discount Amount (FC)
  DcntSumSy Num(19,6) Discount Amount (SC)
  BfDcntSum Num(19,6) Amount Before Discount
  BfDcntSumF Num(19,6) Amount Before Discount (FC)
  BfDcntSumS Num(19,6) Amount Before Discount (SC)
  BfNetDcnt Num(19,6) Net Amount Bef. Discount
  BfNetDcntF Num(19,6) Net Amount Bef. Discount (FC)
  BfNetDcntS Num(19,6) Net Amount Bef. Discount (SC)
  PaidSum Num(19,6) Amount Paid (LC)
  ExpAppld Num(19,6) Freight applied
  ExpAppldFC Num(19,6) Freight applied FC
  ExpAppldSC Num(19,6) Freight applied SC
  Rounddiff Num(19,6) Rounding Diff.
  RounddifFc Num(19,6) Rounding Diff. (FC)
  RounddifSc Num(19,6) Rounding Diff. (SC)
  InstId Int(6) Installment ID default=1
  WtAppld Num(19,6) Applied WTax
  WtAppldFC Num(19,6) Applied WTax (FC)
  WtAppldSC Num(19,6) Applied WTax (SC)
  LinkDate Date(8) Link Date
  AmtDifPst Date(8) Amount Diffs. Posting Date
  PaidDpm VarChar(1) Paid Down Payment default=N [N=No, Y=Yes]
  DpmPosted VarChar(1) Link Date
  ExpVatSum Num(19,6) VAT on Expenses Sum
  ExpVatSumF Num(19,6) VAT on Expenses Sum (FC)
  ExpVatSumS Num(19,6) VAT on Expenses Sum (SC)
  IsRateDiff VarChar(1) Is Exchange Rate default=N
  WtInvCatS Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSF Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSS Num(19,6) Withholding Tax Invoice Categ.
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  DocTransId Int(11) Trans. ID of Paid Document ->OJDT
  MIEntry Int(11) MI Entry Include this Payment default=0
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  IsSelected VarChar(1) Is Record Selected default=N [Y=Yes, N=No]
  WTOnHold Num(19,6) Withholding Tax On Hold
  WTOnhldPst Num(19,6) Withholding Tax Posted
  baseAbs Int(11) Base Document Number
  MIType nVarChar(20) MI Type Include this Payment [270=A/R Monthly Invoice, 140000014=A/P Monthly Invoice]
  DocSubType nVarChar(2) Document Subtype default=--
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]

# PDF3 - Payment Draft - Credit Vouchers
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document No. ->OPDF
  LineID Int(11) Row No.
  CreditCard Int(6) Credit Card default=-1 ->OCRC
  CreditAcct nVarChar(15) Credit Amount ->OACT
  CrCardNum nVarChar(64) Credit Card No.
  CardValid Date(8) Credit Card Valid Until
  VoucherNum nVarChar(20) Credit Voucher No.
  OwnerIdNum nVarChar(15) ID Number
  OwnerPhone nVarChar(20) Telephone
  CrTypeCode Int(6) Payment Method Code default=-1 ->OCRP
  NumOfPmnts Int(6) No. of Payments default=1
  FirstDue Date(8) 1st Payment Date
  FirstSum Num(19,6) First Partial Payment
  AddPmntSum Num(19,6) Each Additional Payment
  CreditSum Num(19,6) Credit Amount
  CreditCur nVarChar(3) Credit Voucher Currency ->OCRN
  CreditRate Num(19,6) Credit Voucher Rate
  ConfNum nVarChar(20) Confirmation No.
  CreditType VarChar(1) Credit Transaction Type default=S [U=Telephone Transaction, S=Regular, I=Internet Transaction]
  CredPmnts Int(6) No. of Credit Payments default=1
  PlCrdStat nVarChar(4) Pelecard Debit Status default=-1
  MagnetStr nVarChar(40) Magnetic Stripe Content
  SpiltCred VarChar(1) Split Credit Voucher Payment default=N [Y=Yes, N=No]
  ConsolNum Int(11) Vendor Credit Code default=-1 ->OPVL
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0

# PDF4 - Payment Draft - Account List
Module: Banking | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OPDF
  LineId Int(11) Row Number
  AcctCode nVarChar(15) Account ->OACT
  SumApplied Num(19,6) Paid
  AppliedFC Num(19,6) Paid in FC
  AppliedSys Num(19,6) Paid in SC
  Descrip nVarChar(250) Details
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  AcctName nVarChar(100) Account Name
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  GrossAmnt Num(19,6) Gross Amount
  GrssAmntFC Num(19,6) Gross Amount (FC)
  GrssAmntSC Num(19,6) Gross Amount (SC)
  AmntBase VarChar(1) Base Amount [E=Exclude Tax, I=Include Tax]
  VatAmnt Num(19,6) VAT Amount
  VatAmntFC Num(19,6) VAT Amount (FC)
  VatAmntSC Num(19,6) VAT Amount (SC)
  UserChaVat VarChar(1) User Changed VAT default=N [N=No, Y=Yes]
  TaxTypeID Int(11) Tax Type Component ID ->OSTT
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Section Int(11) Section ->OSEC
  AsseType VarChar(1) Assessee Type [C=Company, P=Others]
  LocCode Int(11) Location Code ->OLCT
  MatType Int(11) Material Type default=0
  EquVatPer Num(19,6) Equalization Tax Rate
  EquVatSum Num(19,6) Equalization VAT Amount
  EquVatSumF Num(19,6) Equalization VAT Amount (FC)
  EquVatSumS Num(19,6) Equalization VAT Amount (SC)

# PDF5 - PaymentDraft - vat adjustment
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ObjType, LineNum, InvEntry, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OPDF
  InvEntry Int(11) Invoice Key
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Tax %
  VatSum Num(19,6) Tax Amount
  BaseSum Num(19,6) Base Amount
  NoDedSum Num(19,6) Non-Deductible Amount
  BaseSumFc Num(19,6) Base Amount FC
  VatSumFc Num(19,6) Tax Amount (FC)
  NoDedSumFc Num(19,6) Non-Deductible Amount (FC)
  BaseSumSc Num(19,6) Base Amount (SC)
  NoDedSumSc Num(19,6) Non-Deductible Amount (SC)
  VatSumSc Num(19,6) Tax Amount (SC)
  CashDiscAc nVarChar(15) Cash Discount Account
  BaseObjArr Int(6) Base Object Array Number default=1
  BaseObj Int(11) Base Object default=13
  InstlmntId Int(6) Installment ID default=0
  GroupNum Int(11) Group Number default=0
  LineSeq Int(11) Row Sequence default=-1
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)

# PDF6 - Payment Drafts - Withholding Tax - Rows
Module: Banking | 77 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OPDF
  InvoiceId Int(11) Invoice Key
  WTCode nVarChar(4) WTax Code ->OWHT
  PymMean VarChar(1) Payment Means default=C [C=Cash, K=Checks, R=Credit Card, T=Bank Transfer, B=Bill of Exchange]
  DueDate Date(8) Due Date
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (SC)
  WTSumSC Num(19,6) WTax Amount (FC)
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  PymAmount Num(19,6) Payment Amount
  PymAmounF Num(19,6) Payment Amount (FC)
  PymAmounS Num(19,6) Payment Amount (SC)
  Line Int(11) Internal Number
  LogInstanc Int(11) Log Instance - History default=0
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  WTPosted Num(19,6) WT Posted
  WTPostedFC Num(19,6) WT Posted FC
  WTPostedSC Num(19,6) WT Posted SC
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  DepositNum Int(11) Deposit Number ->OVPM
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtC Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtC Num(19,6) Cess GST Base Amount (FC)
  UtgstAmt Num(19,6) UTGST Amount
  UtgstAmtSC Num(19,6) UTGST Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Amount (FC)
  CsgstAmt Num(19,6) Cess GST Amount
  CsgstAmtSC Num(19,6) Cess GST Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Amount (FC)

# PDF7 - Payment Draft - Tax Amount per Document
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OPDF
  LineSeq Int(11) Row Sequence
  InvoiceSeq Int(11) Invoice Sequence Number
  ValueDate Date(8) Due Date
  Inv4Seq Int(11) INV4 Sequence Number
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# PDF8 - Payment Draft - TDS Entries
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocNum
  INVOICE: DocLine, DocEntry, InvType
  PAYMENT: PaidLine, PaidEntry
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OPDF
  LineNum Int(11) Row Number
  InvType nVarChar(20) Invoice Category default=-1 [-1=All Transactions, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 10000079=TDS Adjustment]
  DocEntry Int(11) Invoice Internal ID
  DocLine Int(11) Invoice Row Number
  ObjectType nVarChar(20) Object Type ->ADP1
  LogInstanc Int(11) Log Instance default=0
  PaidEntry Int(11) Payment Internal ID
  PaidLine Int(11) Payment Row Number

# PEX1 - Payment Results Table - Rows
Module: Banking | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineId Int(11) Row Number
  PayRunDate Date(8) Date of Payment Run
  PaymWizCod Int(11) Payment Wizard Code
  VendorNum nVarChar(15) Vendor Code ->OCRD
  CustNum nVarChar(15) Customer Code ->OCRD
  PaymMethod nVarChar(15) Payment Means ->OPYM
  PaymDocNum Int(11) Payment Document No.
  FiscalYear Date(8) Fiscal Year
  VendRefNum nVarChar(100) Vendor Ref. No.
  ObjType nVarChar(20) Document Object Type
  DocDate Date(8) Document Posting Date
  TaxDate Date(8) Document Date
  CrdGLAcct nVarChar(15) BP Accounts Receivable/Payable ->OACT
  DocCurr nVarChar(3) Document Currency
  DocRate Num(19,6) Document Rate
  DocTotal Num(19,6) Document Total (LC)
  DocTotalFC Num(19,6) Document Total (FC)
  DocTaxAmnt Num(19,6) Tax Amount per Document Amount
  DoxTxAmtFC Num(19,6) Tax Amount per Document Amount
  DocRemarks nVarChar(254) Document Remarks
  DocPrmTerm Int(6) Document Payment Terms ->OCTG
  DocPymRef nVarChar(27) Payment Document Reference
  DocLocCurr nVarChar(3) Document Local Currency
  PymTermPer Int(11) Payment Terms Period
  DocNum Int(11) Document Number
  PymNum Int(11) Payment Number (PWZ3 - PymNum)
  PayOrderNo Int(11) Payment Order Number ->OIPO
  FreeText1 nVarChar(100) Free Text 1
  FreeText2 nVarChar(100) Free Text 2
  FreeText3 nVarChar(100) Free Text 3
  vatApplied Num(19,6) VAT Applied

# PMN5 - Payment - VAT Adjustment
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number
  InvEntry Int(11) Invoice No.
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Tax %
  VatSum Num(19,6) Tax Amount
  BaseSum Num(19,6) Base Amount
  NoDedSum Num(19,6) Nondeductible Amount
  BaseSumFc Num(19,6) Base Amount (FC)
  VatSumFc Num(19,6) Tax Amount (FC)
  NoDedSumFc Num(19,6) Nondeductible Amount (FC)
  BaseSumSc Num(19,6) Base Amount (SC)
  NoDedSumSc Num(19,6) Nondeductible Amount (SC)
  VatSumSc Num(19,6) VAT Amount (SC)
  CashDiscAc nVarChar(15) Cash Discount Account
  BaseObjArr Int(6) Base Object Array Number default=1
  BaseObj Int(11) Base Object default=13
  InstlmntId Int(6) Installment ID default=0
  GroupNum Int(11) Group Number default=0
  LineSeq Int(11) Row Sequence
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)

# PMV8 - Incoming Payment - TDS Entries
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocNum
  INVOICE: DocLine, DocEntry, InvType
  PAYMENT: PaidLine, PaidEntry
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineNum Int(11) Row Number
  InvType nVarChar(20) Invoice Category
  DocEntry Int(11) Invoice Internal ID
  DocLine Int(11) Invoice Row Number
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  PaidEntry Int(11) Payment Internal ID
  PaidLine Int(11) Payment Row Number

# PWZ1 - Payment Wizard - Rows 1
Module: Banking | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  CardCode nVarChar(15) BP Code ->OCRD
  CardName nVarChar(100) BP Name
  CardType VarChar(1) BP Type
  Checked VarChar(1) Checked
  BPCurrency nVarChar(3) BP Currency
  BPSingleP VarChar(1) BP Single Payment default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# PWZ2 - Payment Wizard - Rows 2
Module: Banking | 24 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PymCode, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  PymCode nVarChar(15) Payment Method Code ->OPYM
  BnkAccount nVarChar(15) Bank Account ->OACT
  MaxIncom Num(19,6) Max. Incoming Amount
  MaxOutgo Num(19,6) Max. Outgoing Amount
  Balance Num(19,6) G/L Balance
  ExpectBal Num(19,6) Expected G/L Balance
  Checked VarChar(1) Checked
  PymDisc nVarChar(100) Payment Description
  PymType VarChar(1) Payment Type
  IntBalance Num(19,6) G/L Interim Balance
  ExpIntBal Num(19,6) Expected G/L Interim Balance
  InterimAct nVarChar(15) Interim Account ->OACT
  BnkCountry nVarChar(3) Bank Country
  BnkCode nVarChar(30) Bank Code
  BnkAccNo nVarChar(50) Bank Account Number
  FatherLn VarChar(1) Parent Line default=N [Y=Yes, N=No]
  NegativPym nVarChar(15) Negative Payment Method Code
  NegPymBnk nVarChar(30) Negative Payment Bank Code
  NegCountry nVarChar(3) Negative Payment Bank Country
  NegPymAcct nVarChar(50) Negative Payment Bank Account
  PaymenMean VarChar(1) Payment Means
  IBAN nVarChar(50) IBAN
  SwiftNum nVarChar(50) BIC/SWIFT Code

# PWZ3 - Payment Wizard - Rows 3
Module: Banking | 160 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PymNum, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  PymNum Int(11) Payment Number ->OCRN
  CardCode nVarChar(15) Vendor Code ->OCRD
  CardName nVarChar(100) Vendor Name
  PymMeth nVarChar(15) Payment Method ->OPYM
  GLAccCode nVarChar(15) G/L Account Code ->OACT
  GLAccName nVarChar(100) G/L Account Name
  PymAmount Num(19,6) Total Payment
  PymAmntFC Num(19,6) Total Payment (FC)
  PymAmnSyst Num(19,6) Total Payment (SC)
  InvKey Int(11) Invoice Key
  DocNum Int(11) Document Number
  PostDate Date(8) Posting Date
  ValDate Date(8) Due Date
  TotalLoc Num(19,6) Total (LC)
  TotalFC Num(19,6) Total (FC)
  TotalSys Num(19,6) Total (SC)
  DueBal Num(19,6) Balance Due
  DueBalFC Num(19,6) Balance Due (FC)
  DueBalSys Num(19,6) Balance Due (SC)
  DiscPrcnt Num(19,6) Discount %
  DiscSum Num(19,6) Total Discount
  DiscSumFC Num(19,6) Total Discount (FC)
  DiscSumSy Num(19,6) Total Discount (SC)
  PayAmount Num(19,6) Payment Amount
  PayAmntFC Num(19,6) Payment Amount (FC)
  PayAmntSys Num(19,6) Payment Amount (SC)
  InvPayAmnt Num(19,6) Total Invoice for Payment
  InvPayAmFC Num(19,6) Total Invoice for Payment (FC)
  InvPayAmSy Num(19,6) Total Invoice for Payment (SC)
  CardType VarChar(1) BP Type default=C [C=Customer, S=Vendor, L=Lead]
  Country nVarChar(3) Bank Country ->OCRY
  ObjType nVarChar(20) Object Type default=13 ->ADP1
  PymBnkTrns VarChar(1) Payment Means default=C [C=Check, T=Bank Transfer, B=Bill Of Exchange]
  ActFrmtCod nVarChar(210) Account Format Code
  Checked VarChar(1) Checked
  FatherLine VarChar(1) Father Line default=N
  InvCurr nVarChar(3) Document Currency
  LineRate Num(19,6) Row Rate
  BfDcntSum Num(19,6) Amount Before Discount
  BfNetDcnt Num(19,6) Net Amount Before Discount
  vatApplied Num(19,6) VAT Applied
  IsTax VarChar(1) Is Tax default=Y
  IsFreight VarChar(1) Is Freight default=Y
  IsOrigMeth VarChar(1) Original Payment Method default=N
  FreightSum Num(19,6) Freight Sum
  IsrRef nVarChar(27) ISR Ref. No.
  RoundSum Num(19,6) Rounding Amount
  Agent nVarChar(32) Agent Code ->OAGP
  InstId Int(6) Installment ID default=1
  WtSum Num(19,6) Withholding Tax Amount
  BoeNum Int(11) Bill of Exchange No.
  NumAtCard nVarChar(100) BP Reference No.
  DeductPer Num(19,6) Deduction Percent
  DpmPosted VarChar(1) Down Payment Posted
  Status VarChar(1) Inv Status
  NumOfCheck Int(11) Number of Checks default=1
  SumFrstChk Num(19,6) Sum of First Check
  SumNxtChk Num(19,6) Sum of Next Check
  PayToCode nVarChar(50) Pay to
  PayToCntr nVarChar(3) Pay to Bank Country ->OCRY
  PayToBank nVarChar(30) Pay to Bank Code
  PayToAct nVarChar(50) Pay to Bank Account No.
  PymCurr nVarChar(3) Payment Currency
  TaxOnExpSu Num(19,6) Tax on Freight Amount
  TransId Int(11) Transaction Internal ID ->OJDT
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Line_ID Int(11) JE Row Number default=0
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  PymDate Date(8) Payment Date
  BcgSum Num(19,6) Bank Charges Amount
  BcgSumFC Num(19,6) Bank Charges Amount (FC)
  BcgSumSy Num(19,6) Bank Charges Amount (SC)
  BcgTaxSum Num(19,6) Bank Charge Tax Amount
  BcgTaxSumF Num(19,6) Bank Charge Tax Amount (FC)
  BcgTaxSumS Num(19,6) Bank Charge Tax Amount (SC)
  PrjCode nVarChar(20) Project ->OPRJ
  BcgVatGrp nVarChar(8) Bank Charge Tax Group ->OVTG
  LinePrjCod nVarChar(20) Line Project ->OPRJ
  BcgPmnt Num(19,6) Payment Amount (BCG)
  BcgPmntFc Num(19,6) Payment Amount FC (BCG)
  BcgPmntSc Num(19,6) Payment Amount SC (BCG)
  PayOrderNo Int(11) Payment Order Number ->OIPO
  LineType VarChar(1) Line Type default=G [G=General, O=Pay on Account, T=Pay to Account]
  ManualNum Int(11) Manual Entry No. default=0
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  Ref3 nVarChar(100) Reference 3
  OrdrStatus VarChar(1) Payment Order Status
  BnkCode nVarChar(30) Bank Code
  BnkAccNo nVarChar(50) Bank Account Number
  Branch nVarChar(50) Branch
  BnkCountr nVarChar(3) Manual Line Bank Country
  TBankCode nVarChar(30) Target Default Bank default=-1
  TDflAccoun nVarChar(50) Target Default Account
  TBankCount nVarChar(3) Target Bank Country ->OCRY
  TargetBran nVarChar(50) Target Bank Branch
  DscDueDate Date(8) Discount Due Date
  CIG Int(11) Contract Code Identification ->OCIG
  CUP Int(11) Unique Code of Project ->OCUP
  BoeCurrSta VarChar(1) BoE Current Status
  BoeKey Int(11) Bill of Exchange Key ->OBOE
  BoeDate Date(8) BoE Date
  BoeDueDate Date(8) Bill of Exchange Due Date
  Instruct1 nVarChar(2) BoE Instruction 1
  Instruct2 nVarChar(2) BoE Instruction 2
  BoeCancIns nVarChar(2) BoE Cancel Instruction
  BoeOccCode nVarChar(2) BoE Occurrence Code
  BoePtfID nVarChar(3) BoE Internal Portfolio ID
  BoeOurNum Int(11) Our Number in Next BoE
  BoeIntrAm Num(19,6) BoE Interest Amount
  BoeDiscD Date(8) BoE Discount Date
  BoeDisAmnt Num(19,6) BoE Discount Amount
  BoeFineD Date(8) BoE Fine Date
  BoeFineAmt Num(19,6) BoE Fine Amount
  BoeIntrstD Date(8) BoE Interest Date
  BoeIOFAmt Num(19,6) BoE IOF Amount
  BoeMovCode nVarChar(10) BoE Movement Code
  BarcodeRep nVarChar(100) Barcode Representation
  BPLId Int(11) Branch ->OBPL
  PONumber Int(11) External Payment Order Number
  POSeries Int(11) External Payment Order Series
  PaPriority VarChar(1) Payment Priority default=6 [1=, 2=, 3=, 4=, 5=, 6=]
  PaymType VarChar(1) Payment Type default=N [N=, E=Electronic, P=Mail, T=Telegraph, X=Express]
  OriPymMeth nVarChar(15) Original Payment Method Code
  PymMethTyp VarChar(1) Payment Method Type [I=Incoming, O=Outgoing]
  SinglePym VarChar(1) Single Payment default=N [N=No, Y=Yes]
  MandateID nVarChar(35) Mandate ID
  SeqType nVarChar(4) Sequence Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  BaseDocDat Date(8) Base Document Date
  OKATO nVarChar(11) OKATO
  PostPeriod nVarChar(10) Posting Period Code
  RecipStatu nVarChar(2) Recipient Status
  BudgetId nVarChar(100) VAT Budget Classification Code
  PymReason nVarChar(2) Payment Reason
  BaseDocTyp nVarChar(2) Base Document Type
  TaxPymType nVarChar(2) Tax Payment Type
  OKTMO nVarChar(12) OKTMO
  PymIsUpdat nVarChar(30) Payment method is updated
  OriPymCode nVarChar(15) Original Payment Method Code
  OriPymType VarChar(1) Original Payment Method Type
  ReasonCode Int(11) Reason Code
  OriActCode nVarChar(15) Original Account Code
  OriActName nVarChar(100) Original Account Name
  ReasonLine Int(11) Reason Line
  OriFormat nVarChar(210) Original Format Code
  WtIsPym VarChar(1) Withholding Tax is Payment Type default=N [N=No, Y=Yes]
  IBAN nVarChar(50) IBAN
  SwiftNum nVarChar(50) BIC/SWIFT Code
  UIPCode nVarChar(25) UIP Code
  AgrNo Int(11) Agreement No. ->OOAT
  ExeByServ VarChar(1) Executed by Server
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]
  VatAmount Num(19,6) VAT Amount
  EnPayToAct Text(16) Encryption of Pay to Bank Acct
  EncryptIV nVarChar(100) Encrypt IV
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# PWZ4 - Payment Wizard - Rows 4
Module: Banking | 36 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ObjType, RctId, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  PymNum Int(11) Payment Number
  CardCode nVarChar(15) Vendor's Card code ->OCRD
  CardName nVarChar(100) Vendor's Card Name
  PymMeth nVarChar(15) Payment Method ->OPYM
  GLAccCode nVarChar(15) G/L Account Code ->OACT
  PymAmount Num(19,6) Sum of payment amount
  PymAmntFC Num(19,6) Total Payment Amount (FC)
  ObjType nVarChar(20) Object Type [24=Incoming Payment, 46=Outgoing Payment]
  RctId Int(11) Document ID
  DocCurr nVarChar(3) Document Currency
  BankAccou nVarChar(50) Acct No. ->OACT
  BnkDflt nVarChar(30) Default Bank
  BankCountr nVarChar(3) Bank Country ->OCRY
  BankActKey Int(11) Bank Account Internal ID ->DSC1
  LineType VarChar(1) Line Type default=G
  ManualNum Int(11) Manual Entry No. default=0
  TBankCode nVarChar(30) Target Default Bank default=-1
  TDflAccoun nVarChar(50) Target Default Account
  TBankCount nVarChar(3) Target Bank Country ->OCRY
  TargetBran nVarChar(50) Target Bank Branch
  BcgPmnt Num(19,6) Payment Amount (BCG)
  BcgPmntFc Num(19,6) Payment Amount FC (BCG)
  RecipStatu nVarChar(2) Recipient Status
  BudgetId nVarChar(100) VAT Budget Classification Code
  OKATO nVarChar(11) OKATO
  PymReason nVarChar(2) Payment Reason
  PostPeriod nVarChar(10) Posting Period Code
  BaseDocTyp nVarChar(2) Base Document Type
  BaseDocDat Date(8) Base Docoument Date
  TaxPymType nVarChar(2) Tax Payment Type
  OKTMO nVarChar(12) OKTMO
  IBAN nVarChar(50) IBAN
  SwiftNum nVarChar(50) BIC/SWIFT Code
  UIPCode nVarChar(25) UIP Code
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# PWZ5 - Payment Wizard - Rows 5
Module: Banking | 20 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InstlmntID, Object, ErrorLine, InvID, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Entry ->OPWZ
  InvID Int(11) Inv ID
  Amount Num(19,6) Invoice Amount
  CardCode nVarChar(15) Card Code ->OCRD
  CardName nVarChar(100) Card Name
  PostDate Date(8) Posting Date
  ErrDisc nVarChar(254) Error Discription
  ErrorLine Int(11) ErrorLine
  WriteErr VarChar(1) WriteErr default=Y
  Object nVarChar(20) Object Type default=0
  InstlmntID Int(6) Installment ID default=1
  invNum Int(11) Invoice No.
  Currency nVarChar(3) Currency
  LineType VarChar(1) Line Type default=G
  DueBal Num(19,6) Balance Due
  DueBalFC Num(19,6) Balance Due (FC)
  DueBalSys Num(19,6) Balance Due (SC)
  ValDate Date(8) Due Date
  BPLId Int(11) Branch ->OBPL
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]

# PWZ6 - Payment Wizard Rows - 6
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CondNum, IdEntry
Fields (name type(len) description [values] ->parent table):
  IdEntry Int(11) ID Number ->OPWZ
  CondNum Int(11) Condition Number
  SelFldID nVarChar(100) Selection Field ID
  FromString nVarChar(200) From String Value
  FromNumber Int(11) From Number Value
  FromMoney Num(19,6) From Amount Value
  FromDate Date(8) From Date Value
  FromMemo Text(16) From Memo Value
  ToString nVarChar(200) To String Value
  ToNumber Int(11) To Number Value
  ToMoney Num(19,6) To Amount Value
  ToDate Date(8) To Date Value
  ToMemo Text(16) To Memo Value

# PYD1 - Payment Terms Allowed in Payment Run
Module: Banking | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PYMCode, PYDCode
Fields (name type(len) description [values] ->parent table):
  PYDCode nVarChar(20) Payment Run Code ->OPYD
  PYMCode nVarChar(15) Payment Method ->OPYM

# PYM1 - Currency Selection
Module: Banking | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CurrCode, PymCode
Fields (name type(len) description [values] ->parent table):
  PymCode nVarChar(15) Payment Method Code ->OPYM
  CurrCode nVarChar(3) Currency Code ->OCRN
  CurrName nVarChar(20) Currency Name
  Choose VarChar(1) Choose default=N [Y=Yes, N=No]

# RCC4 - Incoming Payment - Credit Vouchers
Module: Banking | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineId Int(11) Row Number
  AcctCode nVarChar(15) Credit Card default=-1 ->OCRC
  SumApplied Num(19,6) Credit Amount
  AppliedFC Num(19,6) Credit Card Number
  AppliedSys Num(19,6) Credit Card Validity
  Descrip nVarChar(250) Voucher Number
  VatGroup nVarChar(8) ID Number ->OVTG
  VatPrcnt Num(19,6) Telephone
  AcctName nVarChar(100) Payment Method Code default=-1
  ObjType nVarChar(20) Number of Payments default=1 ->ADP1
  LogInstanc Int(11) First Payment Date
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  GrossAmnt Num(19,6) Gross Amount
  GrssAmntFC Num(19,6) Gross Amount (FC)
  GrssAmntSC Num(19,6) Gross Amount (SC)
  AmntBase VarChar(1) Base Amount [E=Exclude Tax, I=Include Tax]
  VatAmnt Num(19,6) VAT Amount
  VatAmntFC Num(19,6) VAT Amount (FC)
  VatAmntSC Num(19,6) VAT Amount (SC)
  UserChaVat VarChar(1) User Changed VAT default=N [N=No, Y=Yes]
  TaxTypeID Int(11) Tax Type Component ID ->OSTT
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Section Int(11) Section ->OSEC
  AsseType VarChar(1) Assessee Type [C=Company, P=Others]
  LocCode Int(11) Location Code ->OLCT
  MatType Int(11) Material Type default=0
  EquVatPer Num(19,6) Equalization Tax Rate
  EquVatSum Num(19,6) Equalization VAT Amount
  EquVatSumF Num(19,6) Equalization VAT Amount (FC)
  EquVatSumS Num(19,6) Equalization VAT Amount (SC)

# RCT1 - Incoming Payment - Checks
Module: Banking | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineID Int(11) Row Number
  DueDate Date(8) Check Date
  CheckNum Int(11) Check Number
  BankCode nVarChar(30) Account No. default=-1
  Branch nVarChar(50) Branch Number
  AcctNum nVarChar(50) Account Number
  Details nVarChar(254) Details
  Trnsfrable VarChar(1) Negotiable default=N [Y=Yes, N=No]
  CheckSum Num(19,6) Check Amount
  Currency nVarChar(3) Check Currency ->OCRN
  Flags Int(11) Flags default=0
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  CountryCod nVarChar(3) Country Code ->OCRY
  CheckAct nVarChar(15) Checking Account ->OACT
  CheckAbs Int(11) Check ID Entry ->OCHH
  BnkActKey Int(11) Bank Account No. ->DSC1
  ManualChk VarChar(1) Manual Check default=N [N=No, Y=Yes]
  FiscalID nVarChar(100) Fiscal ID
  OrigIssdBy nVarChar(254) Orginally Issued By
  Endorse VarChar(1) Endorse default=N [Y=Yes, N=No]
  EndorsChNo Int(11) Endorsable Check No. ->OCHH
  EnAcctNum Text(16) Encryption of Account Number
  EncryptIV nVarChar(100) Encrypt IV

# RCT2 - Incoming Payments - Invoices
Module: Banking | 63 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InvoiceId, DocNum
  JDT: DocLine, DocTransId
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  InvoiceId Int(11) Sequence No.
  DocEntry Int(11) Invoice Key
  SumApplied Num(19,6) Paid to Invoice
  AppliedFC Num(19,6) Paid (FC)
  AppliedSys Num(19,6) Paid (SC)
  InvType nVarChar(20) Invoice Category default=13 [203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 25=Deposit, 46=Payment Advice, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, -1=All Transactions, 163=A/P Correction Invoice, 165=A/R Correction Invoice, 0=]
  DocRate Num(19,6) Document Rate
  Flags Int(11) Flags default=0
  IntrsStat VarChar(1) Interest Letter Status default=U [U=Not Sent, S=Sent, C=Closed]
  DocLine Int(11) Row Key default=0
  vatApplied Num(19,6) Tax Definition
  vatAppldFC Num(19,6) Tax Paid (FC)
  vatAppldSy Num(19,6) Tax Paid (SC)
  selfInv VarChar(1) Autom. Invoice default=N [N=No, Y=Yes]
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  Dcount Num(19,6) Discount Rate
  DcntSum Num(19,6) Discount Amount
  DcntSumFC Num(19,6) Discount Amount (FC)
  DcntSumSy Num(19,6) Discount Amount (SC)
  BfDcntSum Num(19,6) Amount Before Discount
  BfDcntSumF Num(19,6) Amount Before Discount (FC)
  BfDcntSumS Num(19,6) Amount Before Discount (SC)
  BfNetDcnt Num(19,6) Net Amount Before Discount
  BfNetDcntF Num(19,6) Net Amt Before Discount (FC)
  BfNetDcntS Num(19,6) Net Amt Before Discount (SC)
  PaidSum Num(19,6) Paid Amount (LC)
  ExpAppld Num(19,6) Freight applied
  ExpAppldFC Num(19,6) Freight applied FC
  ExpAppldSC Num(19,6) Freight applied SC
  Rounddiff Num(19,6) Rounding Diff.
  RounddifFc Num(19,6) Rounding Diff. (FC)
  RounddifSc Num(19,6) Rounding Diff. (SC)
  InstId Int(6) Installment ID default=1
  WtAppld Num(19,6) Applied WTax
  WtAppldFC Num(19,6) Applied WTax (FC)
  WtAppldSC Num(19,6) Applied WTax (SC)
  LinkDate Date(8) Link Date
  AmtDifPst Date(8) Amount Diffs. Posting Date
  PaidDpm VarChar(1) Paid Down Payment default=N [N=No, Y=Yes]
  DpmPosted VarChar(1) Link Date
  ExpVatSum Num(19,6) VAT on Freight Sum
  ExpVatSumF Num(19,6) VAT on Freight Sum (FC)
  ExpVatSumS Num(19,6) VAT on Freight Sum (SC)
  IsRateDiff VarChar(1) Is Exchange Rate default=N
  WtInvCatS Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSF Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSS Num(19,6) Withholding Tax Invoice Categ.
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  DocTransId Int(11) Trans. ID of Paid Document ->OJDT
  MIEntry Int(11) MI Entry Include this Payment default=0
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  IsSelected VarChar(1) Is Record Selected default=N [Y=Yes, N=No]
  WTOnHold Num(19,6) Withholding Tax On Hold
  WTOnhldPst Num(19,6) Withholding Tax Posted
  baseAbs Int(11) Base Document Number
  MIType nVarChar(20) MI Type Include this Payment [270=A/R Monthly Invoice, 140000014=A/P Monthly Invoice]
  DocSubType nVarChar(2) Document Subtype default=--
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]

# RCT3 - Incoming Pmt - Credit Vouchers
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document No. ->ORCT
  LineID Int(11) Row No.
  CreditCard Int(6) Credit Card default=-1 ->OCRC
  CreditAcct nVarChar(15) Credit Amount ->OACT
  CrCardNum nVarChar(64) Credit Card No.
  CardValid Date(8) Credit Card Valid Until
  VoucherNum nVarChar(20) Credit Voucher No.
  OwnerIdNum nVarChar(15) ID Number
  OwnerPhone nVarChar(20) Telephone
  CrTypeCode Int(6) Payment Method Code default=-1 ->OCRP
  NumOfPmnts Int(6) No. of Payments default=1
  FirstDue Date(8) 1st Payment Date
  FirstSum Num(19,6) 1st Partial Payment
  AddPmntSum Num(19,6) Each Additional Payment
  CreditSum Num(19,6) Credit Amount
  CreditCur nVarChar(3) Credit Currency ->OCRN
  CreditRate Num(19,6) Credit Rate
  ConfNum nVarChar(20) Confirmation No.
  CreditType VarChar(1) Credit Transaction Type default=S [U=Telephone Transaction, S=Regular, I=Internet Transaction]
  CredPmnts Int(6) No. of Credit Payments default=1
  PlCrdStat nVarChar(4) Pelecard Debit Status default=-1
  MagnetStr nVarChar(40) Magnetic Stripe Content
  SpiltCred VarChar(1) Split Credit Voucher Payment default=N [Y=Yes, N=No]
  ConsolNum Int(11) Vendor Credit Code default=-1 ->OPVL
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# RCT4 - Incoming Payment - Account List
Module: Banking | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineId Int(11) Row Number
  AcctCode nVarChar(15) Account ->OACT
  SumApplied Num(19,6) Paid
  AppliedFC Num(19,6) Paid (FC)
  AppliedSys Num(19,6) Paid (SC)
  Descrip nVarChar(250) Details
  VatGroup nVarChar(8) Tax Definition ->OVTG
  VatPrcnt Num(19,6) Tax Rate
  AcctName nVarChar(100) Account Name
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  GrossAmnt Num(19,6) Gross Amount
  GrssAmntFC Num(19,6) Gross Amount (FC)
  GrssAmntSC Num(19,6) Gross Amount (SC)
  AmntBase VarChar(1) Base Amount [E=Exclude Tax, I=Include Tax]
  VatAmnt Num(19,6) VAT Amount
  VatAmntFC Num(19,6) VAT Amount(FC)
  VatAmntSC Num(19,6) VAT Amount(SC)
  UserChaVat VarChar(1) User Changed VAT default=N [N=No, Y=Yes]
  TaxTypeID Int(11) Tax Type Component ID ->OSTT
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Section Int(11) Section ->OSEC
  AsseType VarChar(1) Assessee Type [C=Company, P=Others]
  LocCode Int(11) Location Code ->OLCT
  MatType Int(11) Material Type default=0
  EquVatPer Num(19,6) Equalization Tax Rate
  EquVatSum Num(19,6) Equalization VAT Amount
  EquVatSumF Num(19,6) Equalization VAT Amount (FC)
  EquVatSumS Num(19,6) Equalization VAT Amount (SC)

# RCT5 - Reciept vat adjustment
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  InvEntry Int(11) Invoice Key
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Tax %
  VatSum Num(19,6) Tax Amount
  BaseSum Num(19,6) Base Amount
  NoDedSum Num(19,6) Non-Deductible Amount
  BaseSumFc Num(19,6) Base Amount (FC)
  VatSumFc Num(19,6) Tax Amount (FC)
  NoDedSumFc Num(19,6) Non-Deductible Amount (FC)
  BaseSumSc Num(19,6) Base Amount (SC)
  NoDedSumSc Num(19,6) Non-Deductible Amount (SC)
  VatSumSc Num(19,6) VAT Amount (SC)
  CashDiscAc nVarChar(15) Cash Discount Account
  BaseObjArr Int(6) Base Object Array Number default=1
  BaseObj Int(11) Base Object default=13
  InstlmntId Int(6) Installment ID default=0
  GroupNum Int(11) Group Number default=0
  LineSeq Int(11) Row Sequence
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)

# RCT6 - Incoming Payments - WTax Rows
Module: Banking | 77 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  InvoiceId Int(11) Invoice Key
  WTCode nVarChar(4) WTax Code ->OWHT
  PymMean VarChar(1) Payment Means default=C [C=Cash, K=Checks, R=Credit Card, T=Bank Transfer, B=Bill of Exchange]
  DueDate Date(8) Due Date
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (SC)
  WTSumSC Num(19,6) WTax Amount (FC)
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  PymAmount Num(19,6) Payment Amount
  PymAmounF Num(19,6) Payment Amount (FC)
  PymAmounS Num(19,6) Payment Amount (SC)
  Line Int(11) Internal Number
  LogInstanc Int(11) Log Instance - History default=0
  ObjType nVarChar(20) Object Type default=24 ->ADP1
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  WTPosted Num(19,6) WT Posted
  WTPostedFC Num(19,6) WT Posted FC
  WTPostedSC Num(19,6) WT Posted SC
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  DepositNum Int(11) Deposit Number ->OVPM
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtC Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtC Num(19,6) Cess GST Base Amount (FC)
  UtgstAmt Num(19,6) UTGST Amount
  UtgstAmtSC Num(19,6) UTGST Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Amount (FC)
  CsgstAmt Num(19,6) Cess GST Amount
  CsgstAmtSC Num(19,6) Cess GST Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Amount (FC)

# RCT7 - Incoming Pmt - Tax Amount per Document
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineSeq Int(11) Row Sequence
  InvoiceSeq Int(11) Invoice Sequence Number
  ValueDate Date(8) Due Date
  Inv4Seq Int(11) INV4 Sequence Number
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# RCT8 - Incoming Payment - TDS Entries
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocNum
  INVOICE: DocLine, DocEntry, InvType
  PAYMENT: PaidLine, PaidEntry
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineNum Int(11) Row Number
  InvType nVarChar(20) Invoice Category
  DocEntry Int(11) Invoice Internal ID
  DocLine Int(11) Invoice Row Number
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  PaidEntry Int(11) Payment Internal ID
  PaidLine Int(11) Payment Row Number

# RTW1 - Boleto Retorno Wizard: Import Table
Module: Banking | 44 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  BoeMatch nVarChar(10) BoE Match
  BoeNo nVarChar(10) BoE Number
  BoeDate Date(8) BoE Date
  BoeDueDate Date(8) BoE Due Date
  CreditDate Date(8) Credit Date
  CurrBoeSt VarChar(1) Current BoE Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, L=Closed, F=Failed, V=BoE to Vendor]
  ReqBoeSt VarChar(1) Requested BoE Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, L=Closed, F=Failed, V=BoE to Vendor]
  Instruct1 nVarChar(2) BoE Instruction 1
  Instruct2 nVarChar(2) BoE Instruction 2
  CancelCode nVarChar(4) Cancellation Code
  MovmntCode Int(6) Movement Code
  OccurCode Int(6) Occurrence Code
  OccurDate Date(8) Occurrence Date
  Portfolio VarChar(1) Portfolio
  OurNum Int(11) Our Number
  ValueOfT Num(19,6) Value of Title
  NetAmnt Num(19,6) Net Amount
  PaidAmnt Num(19,6) Paid Amount
  FineAmnt Num(19,6) Fine Amount
  IntAmnt Num(19,6) Interest Amount
  Discounts Num(19,6) Discount Amount
  ServiceFee Num(19,6) Service Fee
  IOFTax Num(19,6) IOF Tax
  OtherCred Num(19,6) Other Credits
  OtherExp Num(19,6) Other Expenses
  OtherInc Num(19,6) Other Incomes
  Errors nVarChar(8) Errors
  RefNum nVarChar(254) Reference No.
  Ref2 nVarChar(254) Reference 2
  CardName nVarChar(100) BP Name
  BoEBPName nVarChar(100) BoE BP Name
  MatchCode VarChar(1) Match Code default=N [A=Automatic, M=Manual, N=Not Identified]
  Selected VarChar(1) Selected default=N
  BoeRec Int(11) BoE Record Number
  RetIndex Int(11) RET File Record Index
  Filtered VarChar(1) Filtered default=Y
  Executed VarChar(1) Executed default=N
  Failed VarChar(1) Failed default=N
  LastRun VarChar(1) Last Run default=N
  ErrorMsg nVarChar(254) Error Message
  JETransId nVarChar(10) JE Trans. ID
  CardCode nVarChar(15) BoE BP Code
  PostType VarChar(1) Transaction Type default=C [C=Collection, D=Discounted]

# RTW2 - Boleto Retorno Wizard: Import Archive
Module: Banking | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry
  SequenceNo Int(11) Sequence No.
  StampDate Date(8) Time Stamp Date
  RetFile nVarChar(254) Retorno File
  Format nVarChar(100) File Format Name
  BankCode nVarChar(30) Bank Code
  Account nVarChar(50) Acct No.
  RunType VarChar(1) Run Type default=D [D=Draft, X=Executed]
  RunRecords Int(11) Run Records
  ImCardName VarChar(1) Import Card Name default=N
  PostDate Date(8) Posting Date

# SVR1 - Saved Reconciliations - Transaction List
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: transLine, transID, acctCode
Fields (name type(len) description [values] ->parent table):
  acctCode nVarChar(15) Account Code
  transID Int(11) Transaction ID ->OJDT
  transLine Int(11) Transaction Row

# TMP8 - Incoming Payment - TDS Entries
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocNum
  INVOICE: DocLine, DocEntry, InvType
  PAYMENT: PaidLine, PaidEntry
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->ORCT
  LineNum Int(11) Row Number
  InvType nVarChar(20) Invoice Category
  DocEntry Int(11) Invoice Internal ID
  DocLine Int(11) Invoice Row Number
  ObjectType nVarChar(20) Object Type default=24 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  PaidEntry Int(11) Payment Internal ID
  PaidLine Int(11) Payment Row Number

# TPW1 - Selection Criteria
Module: Banking | 7 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  FromPeriod Date(8) From Period
  ToPeriod Date(8) To Period
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  TaxCategry Int(11) Tax Category ->ONFT
  LocCode Int(11) Location Code ->OLCT

# TPW2 - Payable Information
Module: Banking | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNumber, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  LineNumber Int(11) Line Number
  TaxCategry Int(11) Tax Category
  TaxType Int(11) Tax Type
  PyblAmnt Num(19,6) Payable Amount
  PyblAmntFC Num(19,6) Payable Amount FC
  PyblAmntSC Num(19,6) Payable Amount SC
  PLAAmnt Num(19,6) P.L.A. Amount
  PLAAmntFC Num(19,6) P.L.A. Amount (FC)
  PLAAmntSC Num(19,6) P.L.A. Amount (SC)

# TPW3 - Utilization and Payment
Module: Banking | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: MatType, CrTaxType, CrTaxCtgry, LineNum, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  LineNum Int(11) Line Number ->TPW2
  CrTaxCtgry Int(11) Credit Tax Category
  CrTaxType Int(11) Credit Tax Type
  CrUtiliz Num(19,6) Credit Utilized Amount
  CrUtilizFC Num(19,6) Credit Utilized Amount FC
  CrUtilizSC Num(19,6) Credit Utilized Amount SC
  PymMeth nVarChar(15) Payment Method
  PymAmnt Num(19,6) Payment Amount
  PymAmntFC Num(19,6) Payment Amount (FC)
  PymAmntSC Num(19,6) Payment Amount (SC)
  MatType Int(11) Material Type default=0 [0=]

# TPW4 - VAT Refund
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  RefundAcct nVarChar(15) Refund Account Code
  RefundAmnt Num(19,6) Refund Amount
  RfndAmntFC Num(19,6) Refund Amount FC
  RfndAmntSC Num(19,6) Refund Amount SC

# TPW5 - Challan Information
Module: Banking | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute Entry No ->OTPW
  ChlnDate Date(8) Challan Date
  ChlnNo nVarChar(50) Challan No
  ChlnBank nVarChar(100) Challan Bank
  ChlnMemo nVarChar(100) Challan Memo

# TPW6 - Journal Entry Information
Module: Banking | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: JeLineId, JeId, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OTPW
  JeId Int(11) JE Number ->OJDT
  JeLineId Int(11) Line Number of JE

# VPM1 - Outgoing Payments - Check Rows
Module: Banking | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  LineID Int(11) Row Number
  DueDate Date(8) Check Date
  CheckNum Int(11) Check Number
  BankCode nVarChar(30) Account No. default=-1
  Branch nVarChar(50) Branch Number
  AcctNum nVarChar(50) Account Number
  Details nVarChar(254) Details
  Trnsfrable VarChar(1) Negotiable default=N [Y=Yes, N=No]
  CheckSum Num(19,6) Check Amount
  Currency nVarChar(3) Check Currency ->OCRN
  Flags Int(11) Flags default=0
  ObjType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  CountryCod nVarChar(3) Country Code ->OCRY
  CheckAct nVarChar(15) Checking Account ->OACT
  CheckAbs Int(11) Internal Check Number ->OCHO
  BnkActKey Int(11) Bank Account No. ->DSC1
  ManualChk VarChar(1) Manual Check default=N [N=No, Y=Yes]
  FiscalID nVarChar(100) Fiscal ID
  OrigIssdBy nVarChar(254) Orginally Issued By
  Endorse VarChar(1) Endorse default=N [Y=Yes, N=No]
  EndorsChNo Int(11) Endorsable Check No. ->OCHH
  EnAcctNum Text(16) Encryption of Account Number
  EncryptIV nVarChar(100) Encrypt IV

# VPM2 - Outgoing Payments - Invoices
Module: Banking | 63 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InvoiceId, DocNum
  JDT: DocLine, DocTransId
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  InvoiceId Int(11) Sequence No.
  DocEntry Int(11) Invoice Key
  SumApplied Num(19,6) Paid to Invoice
  AppliedFC Num(19,6) Paid in FC
  AppliedSys Num(19,6) Paid in SC
  InvType nVarChar(20) Invoice Category default=18 [203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 25=Deposit, 46=Payment Advice, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, -1=All Transactions, 163=A/P Correction Invoice, 165=A/R Correction Invoice, 0=]
  DocRate Num(19,6) Document Rate
  Flags Int(11) Flags default=0
  IntrsStat VarChar(1) Interest Letter Status default=U [U=Not Sent, S=Sent, C=Closed]
  DocLine Int(11) Row Key default=0
  vatApplied Num(19,6) Tax Definition
  vatAppldFC Num(19,6) Tax Paid in FC
  vatAppldSy Num(19,6) Tax Paid in SC
  selfInv VarChar(1) Autom. Invoice default=N [N=No, Y=Yes]
  ObjType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  Dcount Num(19,6) Discount Rate
  DcntSum Num(19,6) Discount Amount
  DcntSumFC Num(19,6) Discount Amount (FC)
  DcntSumSy Num(19,6) Discount Amount (SC)
  BfDcntSum Num(19,6) Amount Before Discount
  BfDcntSumF Num(19,6) Amount Before Discount (FC)
  BfDcntSumS Num(19,6) Amount Before Discount (SC)
  BfNetDcnt Num(19,6) Net Amount Before Discount
  BfNetDcntF Num(19,6) Net Amt Before Discount (FC)
  BfNetDcntS Num(19,6) Net Amt Before Discount (SC)
  PaidSum Num(19,6) Paid Amount (LC)
  ExpAppld Num(19,6) Freight applied
  ExpAppldFC Num(19,6) Freight applied FC
  ExpAppldSC Num(19,6) Freight applied SC
  Rounddiff Num(19,6) Rounding Diff.
  RounddifFc Num(19,6) Rounding Diff. (FC)
  RounddifSc Num(19,6) Rounding Diff. (SC)
  InstId Int(6) Installment ID default=1
  WtAppld Num(19,6) Applied WTax
  WtAppldFC Num(19,6) Applied WTax (FC)
  WtAppldSC Num(19,6) Applied WTax (SC)
  LinkDate Date(8) Link Date
  AmtDifPst Date(8) Amount Diffs. Posting Date
  PaidDpm VarChar(1) Paid Down Payment default=N [N=No, Y=Yes]
  DpmPosted VarChar(1) Link Date
  ExpVatSum Num(19,6) VAT on Freight Sum
  ExpVatSumF Num(19,6) VAT on Freight Sum (FC)
  ExpVatSumS Num(19,6) VAT on Freight Sum (SC)
  IsRateDiff VarChar(1) Is Exchange Rate default=N
  WtInvCatS Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSF Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSS Num(19,6) Withholding Tax Invoice Categ.
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  DocTransId Int(11) Trans. ID of Paid Document ->OJDT
  MIEntry Int(11) MI Entry Include this Payment default=0
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  IsSelected VarChar(1) Is Record Selected default=N [Y=Yes, N=No]
  WTOnHold Num(19,6) Withholding Tax On Hold
  WTOnhldPst Num(19,6) Withholding Tax Posted
  baseAbs Int(11) Base Document Number
  MIType nVarChar(20) MI Type Include this Payment [270=A/R Monthly Invoice, 140000014=A/P Monthly Invoice]
  DocSubType nVarChar(2) Document Subtype default=--
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]

# VPM3 - Outgoing Payments - Credit Vouchers
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineID, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document No. ->OVPM
  LineID Int(11) Row No.
  CreditCard Int(6) Credit Card default=-1 ->OCRC
  CreditAcct nVarChar(15) Credit Amount ->OACT
  CrCardNum nVarChar(64) Credit Card No.
  CardValid Date(8) Credit Card Valid Until
  VoucherNum nVarChar(20) Credit Voucher No.
  OwnerIdNum nVarChar(15) ID Number
  OwnerPhone nVarChar(20) Telephone
  CrTypeCode Int(6) Payment Method Code default=-1 ->OCRP
  NumOfPmnts Int(6) No. of Payments default=1
  FirstDue Date(8) 1st Payment Date
  FirstSum Num(19,6) First Partial Payment
  AddPmntSum Num(19,6) Each Additional Payment
  CreditSum Num(19,6) Credit Amount
  CreditCur nVarChar(3) Credit Voucher Currency ->OCRN
  CreditRate Num(19,6) Credit Voucher Rate
  ConfNum nVarChar(20) Confirmation No.
  CreditType VarChar(1) Credit Transaction Type default=S [U=Telephone Transaction, S=Regular, I=Internet Transaction]
  CredPmnts Int(6) No. of Credit Payments default=1
  PlCrdStat nVarChar(4) Pelecard Debit Status default=-1
  MagnetStr nVarChar(40) Magnetic Stripe Content
  SpiltCred VarChar(1) Split Credit Voucher Payment default=N [Y=Yes, N=No]
  ConsolNum Int(11) Vendor Credit Code default=-1 ->OPVL
  ObjType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# VPM4 - Outgoing Payments - Accounts
Module: Banking | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  LineId Int(11) Row Number
  AcctCode nVarChar(15) Account ->OACT
  SumApplied Num(19,6) Paid
  AppliedFC Num(19,6) Paid in FC
  AppliedSys Num(19,6) Paid in SC
  Descrip nVarChar(250) Description
  VatGroup nVarChar(8) VAT Group ->OVTG
  VatPrcnt Num(19,6) VAT Rate
  AcctName nVarChar(100) Account Name
  ObjType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  Project nVarChar(20) Project Code ->OPRJ
  GrossAmnt Num(19,6) Gross Amount
  GrssAmntFC Num(19,6) Gross Amount (FC)
  GrssAmntSC Num(19,6) Gross Amount (SC)
  AmntBase VarChar(1) Base Amount [E=Exclude Tax, I=Include Tax]
  VatAmnt Num(19,6) VAT Amount
  VatAmntFC Num(19,6) VAT Amount (FC)
  VatAmntSC Num(19,6) VAT Amount (SC)
  UserChaVat VarChar(1) User Changed VAT default=N [N=No, Y=Yes]
  TaxTypeID Int(11) Tax Type Component ID ->OSTT
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  Section Int(11) Section ->OSEC
  AsseType VarChar(1) Assessee Type [C=Company, P=Others]
  LocCode Int(11) Location Code ->OLCT
  MatType Int(11) Material Type default=0
  EquVatPer Num(19,6) Equalization Tax Rate
  EquVatSum Num(19,6) Equalization VAT Amount
  EquVatSumF Num(19,6) Equalization VAT Amount (FC)
  EquVatSumS Num(19,6) Equalization VAT Amount (SC)

# VPM5 - Outgoing Payments - Vat Adjustment
Module: Banking | 26 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  InvEntry Int(11) Invoice Key
  LineNum Int(11) Row Number
  ObjType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  VatPrcnt Num(19,6) Tax %
  VatSum Num(19,6) Tax Amount
  BaseSum Num(19,6) Base Amount
  NoDedSum Num(19,6) Non-Deductible Amount
  BaseSumFc Num(19,6) Base Amount (FC)
  VatSumFc Num(19,6) Tax Amount (FC)
  NoDedSumFc Num(19,6) Non-Deductible Amount (FC)
  BaseSumSc Num(19,6) Base Amount (SC)
  NoDedSumSc Num(19,6) Non-Deductible Amount (SC)
  VatSumSc Num(19,6) VAT Amount (SC)
  CashDiscAc nVarChar(15) Cash Discount Account
  BaseObjArr Int(6) Base Object Array Number default=1
  BaseObj Int(11) Base Object default=18
  InstlmntId Int(6) Installment ID default=0
  GroupNum Int(11) Group Number default=0
  LineSeq Int(11) Row Sequence
  EquVatPer Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Total Equalization Tax
  EquVatSumF Num(19,6) Total Equalization Tax (FC)
  EquVatSumS Num(19,6) Total Equalization Tax (SC)

# VPM6 - Outgoing Payments - WTax Rows
Module: Banking | 77 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Line, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  InvoiceId Int(11) Invoice Key
  WTCode nVarChar(4) WTax Code ->OWHT
  PymMean VarChar(1) Payment Means default=C [C=Cash, K=Checks, R=Credit Card, T=Bank Transfer, B=Bill of Exchange]
  DueDate Date(8) Due Date
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (SC)
  WTSumSC Num(19,6) WTax Amount (FC)
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  PymAmount Num(19,6) Payment Amount
  PymAmounF Num(19,6) Payment Amount (FC)
  PymAmounS Num(19,6) Payment Amount (SC)
  Line Int(11) Internal Number
  LogInstanc Int(11) Log Instance - History default=0
  ObjType nVarChar(20) Object Type default=46 ->ADP1
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  WTPosted Num(19,6) WT Posted
  WTPostedFC Num(19,6) WT Posted FC
  WTPostedSC Num(19,6) WT Posted SC
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  DepositNum Int(11) Deposit Number ->OVPM
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtC Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtC Num(19,6) Cess GST Base Amount (FC)
  UtgstAmt Num(19,6) UTGST Amount
  UtgstAmtSC Num(19,6) UTGST Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Amount (FC)
  CsgstAmt Num(19,6) Cess GST Amount
  CsgstAmtSC Num(19,6) Cess GST Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Amount (FC)

# VPM7 - Outgoing Payments - Tax Amount per Document
Module: Banking | 13 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, DocNum
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  LineSeq Int(11) Row Sequence
  InvoiceSeq Int(11) Invoice Sequence Number
  ValueDate Date(8) Due Date
  Inv4Seq Int(11) INV4 Sequence Number
  TaxSum Num(19,6) Tax Amount
  TaxSumFrgn Num(19,6) Tax Amount (FC)
  TaxSumSys Num(19,6) Tax Amount (SC)
  BaseSum Num(19,6) Base Amount
  BaseSumFrg Num(19,6) Base Amount (FC)
  BaseSumSys Num(19,6) Base Amount (SC)
  ObjectType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0

# VPM8 - Outgoing Payment - TDS Entries
Module: Banking | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DocNum
  INVOICE: DocLine, DocEntry, InvType
  PAYMENT: PaidLine, PaidEntry
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  LineNum Int(11) Row Number
  InvType nVarChar(20) Invoice Category default=-1 [-1=All Transactions, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 10000079=TDS Adjustment]
  DocEntry Int(11) Invoice Internal ID
  DocLine Int(11) Invoice Row Number
  ObjectType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  PaidEntry Int(11) Payment Internal ID ->OVPM
  PaidLine Int(11) Payment Row Number
