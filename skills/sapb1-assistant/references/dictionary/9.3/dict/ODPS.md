<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ODPS - Deposit
Module: Banking | 64 columns | ObjType: 25
Indexes (name: columns; first = primary key; U = unique):
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
