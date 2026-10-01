<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OCHD - Checks for Payment Drafts
Module: Banking | 56 columns | ObjType: 123
Indexes (name: columns; first = primary key; U = unique):
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
