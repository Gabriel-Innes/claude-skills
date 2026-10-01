<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
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
