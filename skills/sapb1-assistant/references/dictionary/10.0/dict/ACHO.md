<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACHO - Checks for Payment - History
Module: Banking | 59 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CheckKey, LogInstanc
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
  Details nVarChar(254) Details
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
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  SumRfndCln Num(19,6) Deduction Refund Amount
  UserSign Int(6) User Signature ->OUSR
  PrintedBy Int(6) Printed By
  Transfered VarChar(1) Transferred to Next Year default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=57 ->ADP1
  CountryCod nVarChar(3) Country/Region Code ->OCRY
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
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachment
  ECheck VarChar(1) E-Check default=N [Y=Yes, N=No]
