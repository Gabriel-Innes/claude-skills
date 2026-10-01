<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCRH - Credit Card Management
Module: Banking | 39 columns | ObjType: 72
Indexes (name: columns; first = primary key; U = unique):
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
