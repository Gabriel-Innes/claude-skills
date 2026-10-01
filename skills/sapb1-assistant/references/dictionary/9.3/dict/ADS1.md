<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ADS1 - House Bank Accounts
Module: Banking | 79 columns
Indexes (name: columns; first = primary key; U = unique):
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
