<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UTX1 - Unreported VAT Transactions - Rows
Module: Finance | 86 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineSeq, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OUTX
  LineSeq Int(11) Row Sequence
  SrcArrType Int(11) Source Array Type default=-1 [-1=Default, 1=Main, 12=Array1, 13=Array2, 14=Array3, 15=Array4, 16=Array5, 17=Array6, 18=Array7, 24=Array13]
  SrcLineNum Int(11) Source Row Number default=-1
  SrcGrpNum Int(11) Source Group Number default=-1 [-1=Default, 0=Group1, 1=Group2, 2=Group3]
  TaxCode nVarChar(8) Tax Code
  StaCode nVarChar(8) Tax Authority Code ->OSTA
  StaType Int(11) Tax Authority Type ->OSTT
  StaIndex Int(11) Tax Authority Seq Index
  IsLiable VarChar(1) Is Tax Liable default=Y [Y=Yes, N=No]
  TaxType VarChar(1) Tax Type default=Y [Y=Regular, U=Use Tax, N=No Tax, O=Tax Offset Transaction, R=Reverse Tax Offset Transaction, P=DPM Request Tax Offset Transaction, D=Deferred Tax Offset Transaction]
  IsAcq VarChar(1) Is Acquisition Tax default=N [N=No, Y=Yes]
  Isdeferred VarChar(1) Deferred Tax [Yes/No] default=N [N=No, Y=Yes]
  ValueDate Date(8) Due Date for Payment
  VatPercent Num(19,6) VAT Percent
  NdPercent Num(19,6) Non Deductible %
  EqPercent Num(19,6) Equalization Percent
  BaseObjTyp nVarChar(20) Base Object Type default=-1 [-1=, 15=Delivery notes, 16=Revert Delivery Notes, 17=Sales Order, 20=Goods Receipt, 21=Goods Return, 22=Purchase order, 23=Sales Quotation, 112=Document Draft, 59=Goods Receipt, 60=Goods Issue, 28=Journal Batches, 140=Payment Draft, 123=Checks for Payment Drafts, 540000006=Purchase Quotation]
  BaseAbs Int(11) Base Document Internal No. default=-1
  BaseArrTyp Int(11) Base Array Type default=-1 [-1=Default, 1=Main, 12=Array1, 13=Array2, 14=Array3, 15=Array4, 16=Array5, 17=Array6, 18=Array7, 24=Array13]
  BaseLinNum Int(11) Base Row Number default=-1
  BaseGrpNum Int(11) Base Group No. default=-1 [-1=Default, 0=Group1, 1=Group2, 2=Group3]
  BaseSum Num(19,6) Base Sum
  BaseSumSc Num(19,6) Base Sum (SC)
  BaseSumFc Num(19,6) Base Sum (FC)
  VatSum Num(19,6) VAT Sum
  VatSumSc Num(19,6) VAT Sum (SC)
  VatSumFc Num(19,6) VAT Sum (FC)
  DeductSum Num(19,6) Deduct VAT Sum
  DedctSumSC Num(19,6) Deduct VAT Sum (SC)
  DedctSumFC Num(19,6) Deduct VAT Sum (FC)
  EqSum Num(19,6) Equalization Sum
  EqSumSC Num(19,6) Equalization Sum (SC)
  EqSumFC Num(19,6) Equalization Sum (FC)
  TaxAcct nVarChar(15) Tax Account ->OACT
  DefAcct nVarChar(15) Deferred Tax Account ->OACT
  NdAcct nVarChar(15) Non Deduct. Account ->OACT
  AcqAcct nVarChar(15) Acquisition Tax Account ->OACT
  ExpAcct nVarChar(15) Expense Account ->OACT
  CrditDebit VarChar(1) Credit Or Debit Transaction [C=Credit, D=DEBIT]
  PostingTyp VarChar(1) Sales or Purchasing default=N [N=None, R=Sales, P=Purchase]
  BasePaid Num(19,6) Applied Base Sum
  BasePaidSC Num(19,6) Applied Base Sum SC
  BasePaidFC Num(19,6) Applied Base Sum FC
  VatPaid Num(19,6) Applied VAT Sum
  VatPaidSC Num(19,6) Applied VAT Sum SC
  VatPaidFC Num(19,6) Applied VAT Sum FC
  DeductPaid Num(19,6) Applied Deduct Sum
  DdctPaidSC Num(19,6) Applied Deduct Sum SC
  DdctPaidFC Num(19,6) Applied Deduct Sum FC
  EqPaid Num(19,6) Applied Equalization Sum
  EqPaidSC Num(19,6) Applied Equalization Sum SC
  EqPaidFC Num(19,6) Applied Equalization Sum FC
  TransAcct nVarChar(15) Transaction Acccount ->OACT
  LnDataNum Int(11) Line Number in Tax Data default=-1
  InPrice VarChar(1) Included in Price default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt default=N [Y=Yes, N=No]
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  PostStatus VarChar(1) Posting Status default=Y [Y=Yes, N=No]
  IsItmLevel VarChar(1) Is Item Level Tax default=N [N=No, Y=Yes]
  MinTAmt Num(19,6) Min. Taxable Amount
  MinTAmtSC Num(19,6) Min. Taxable Amount (SC)
  MinTAmtFC Num(19,6) Min. Taxable Amount (FC)
  MaxTAmt Num(19,6) Max. Taxable Amount
  MaxTAmtSC Num(19,6) Max. Taxable Amount (SC)
  MaxTAmtFC Num(19,6) Max. Taxable Amount (FC)
  FlatTAmt Num(19,6) Flat Tax Amount
  FlatTAmtSC Num(19,6) Flat Tax Amount (SC)
  FlatTAmtFC Num(19,6) Flat Tax Amount (FC)
  EqTaxAcct nVarChar(15) Equalization Tax Account ->OACT
  Reposted VarChar(1) Reposted in Transfer Wizard default=N [Y=Yes, N=No]
  Unencumbrd VarChar(1) Unencumbered default=N [Y=Yes, N=No]
  IsSplitPay VarChar(1) Split Payment default=N [Y=Yes, N=No]
  SplitPayAc nVarChar(15) Split Payment Account
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  RvsChrgPrc Num(19,6) Reverse Charge %
  RvsChrgSum Num(19,6) Reverse Charge Sum
  RvsChrgSC Num(19,6) Reverse Charge Sum (SC)
  RvsChrgFC Num(19,6) Reverse Charge Sum (FC)
  GstPayAct nVarChar(15) GST Payable Account ->OACT
  RvsPaid Num(19,6) Applied Reverse Charge Sum
  RvsPaidSC Num(19,6) Applied Reverse Charge (SC)
  RvsPaidFC Num(19,6) Applied Reverse Charge (FC)
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  GstRecvAct nVarChar(15) GST Receivable Account ->OACT
  IsCstmAct VarChar(1) Apply Customer Accounting Tax Rule default=N [N=No, Y=Yes]
