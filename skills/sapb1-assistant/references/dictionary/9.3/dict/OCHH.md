<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCHH - Check Register
Module: Banking | 37 columns | ObjType: 27
Indexes (name: columns; first = primary key; U = unique):
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
