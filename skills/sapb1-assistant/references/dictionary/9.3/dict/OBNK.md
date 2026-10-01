<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OBNK - External Bank Statement Received
Module: Banking | 73 columns | ObjType: 42
Indexes (name: columns; first = primary key; U = unique):
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
