<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
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
