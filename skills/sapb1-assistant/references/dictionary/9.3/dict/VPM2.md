<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# VPM2 - Outgoing Payments - Invoices
Module: Banking | 63 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: InvoiceId, DocNum
  JDT: DocLine, DocTransId
Fields (name type(len) description [values] ->parent table):
  DocNum Int(11) Document Number ->OVPM
  InvoiceId Int(11) Sequence No.
  DocEntry Int(11) Invoice Key
  SumApplied Num(19,6) Paid to Invoice
  AppliedFC Num(19,6) Paid in FC
  AppliedSys Num(19,6) Paid in SC
  InvType nVarChar(20) Invoice Category default=18 [203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 25=Deposit, 46=Payment Advice, 57=Checks for Payment, 76=Postdated Deposit, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, -1=All Transactions, 163=A/P Correction Invoice, 165=A/R Correction Invoice, 0=]
  DocRate Num(19,6) Document Rate
  Flags Int(11) Flags default=0
  IntrsStat VarChar(1) Interest Letter Status default=U [U=Not Sent, S=Sent, C=Closed]
  DocLine Int(11) Row Key default=0
  vatApplied Num(19,6) Tax Definition
  vatAppldFC Num(19,6) Tax Paid in FC
  vatAppldSy Num(19,6) Tax Paid in SC
  selfInv VarChar(1) Autom. Invoice default=N [N=No, Y=Yes]
  ObjType nVarChar(20) Object Type default=46 ->ADP1
  LogInstanc Int(11) Log Instance default=0
  Dcount Num(19,6) Discount Rate
  DcntSum Num(19,6) Discount Amount
  DcntSumFC Num(19,6) Discount Amount (FC)
  DcntSumSy Num(19,6) Discount Amount (SC)
  BfDcntSum Num(19,6) Amount Before Discount
  BfDcntSumF Num(19,6) Amount Before Discount (FC)
  BfDcntSumS Num(19,6) Amount Before Discount (SC)
  BfNetDcnt Num(19,6) Net Amount Before Discount
  BfNetDcntF Num(19,6) Net Amt Before Discount (FC)
  BfNetDcntS Num(19,6) Net Amt Before Discount (SC)
  PaidSum Num(19,6) Paid Amount (LC)
  ExpAppld Num(19,6) Freight applied
  ExpAppldFC Num(19,6) Freight applied FC
  ExpAppldSC Num(19,6) Freight applied SC
  Rounddiff Num(19,6) Rounding Diff.
  RounddifFc Num(19,6) Rounding Diff. (FC)
  RounddifSc Num(19,6) Rounding Diff. (SC)
  InstId Int(6) Installment ID default=1
  WtAppld Num(19,6) Applied WTax
  WtAppldFC Num(19,6) Applied WTax (FC)
  WtAppldSC Num(19,6) Applied WTax (SC)
  LinkDate Date(8) Link Date
  AmtDifPst Date(8) Amount Diffs. Posting Date
  PaidDpm VarChar(1) Paid Down Payment default=N [N=No, Y=Yes]
  DpmPosted VarChar(1) Link Date
  ExpVatSum Num(19,6) VAT on Freight Sum
  ExpVatSumF Num(19,6) VAT on Freight Sum (FC)
  ExpVatSumS Num(19,6) VAT on Freight Sum (SC)
  IsRateDiff VarChar(1) Is Exchange Rate default=N
  WtInvCatS Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSF Num(19,6) Withholding Tax Invoice Categ.
  WtInvCatSS Num(19,6) Withholding Tax Invoice Categ.
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  DocTransId Int(11) Trans. ID of Paid Document ->OJDT
  MIEntry Int(11) MI Entry Include this Payment default=0
  OcrCode2 nVarChar(8) Distribution Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule5 ->OOCR
  IsSelected VarChar(1) Is Record Selected default=N [Y=Yes, N=No]
  WTOnHold Num(19,6) Withholding Tax On Hold
  WTOnhldPst Num(19,6) Withholding Tax Posted
  baseAbs Int(11) Base Document Number
  MIType nVarChar(20) MI Type Include this Payment [270=A/R Monthly Invoice, 140000014=A/P Monthly Invoice]
  DocSubType nVarChar(2) Document Subtype default=--
  SpltPmtVAT VarChar(1) Split Payment default=N [Y=Yes, N=No]
