<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ADP1 - Object Settings - History
Module: Administration | 67 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrintId, ObjType
  OBJECT U: ObjType
Fields (name type(len) description [values] ->parent table):
  PrintId nVarChar(4) Print No. ->OADP
  ObjType nVarChar(20) Object Type
  Copies Int(6) No. of Copies default=1
  PrintOnAdd VarChar(1) Add & Print default=N [Y=Yes, N=No]
  ExprtOnAdd VarChar(1) Add & Export default=N [Y=Yes, N=No]
  RoundSums VarChar(1) Rounding Amounts default=N [Y=Yes, N=No]
  Remark Text(16) Standard Remarks
  PrintSums VarChar(1) Print Totals default=Y [Y=Yes, N=No]
  VndrNum VarChar(1) Print Mfr Catalog No. default=N [Y=Yes, N=No]
  PrnDscnt VarChar(1) Print Discount Data default=Y [Y=Yes, N=No]
  SplitTran1 VarChar(1) Split Transaction 1 default=N [Y=Yes, N=No]
  SplitTran2 VarChar(1) Split Transaction 2 default=Y [Y=Yes, N=No]
  SplitTran3 VarChar(1) Split Transaction 3 default=Y [Y=Yes, N=No]
  ShowBothNu VarChar(1) Print Mfr Catalog No. Instead default=N [Y=Yes, N=No]
  BaseRmrk VarChar(1) Display Base Remarks default=Y [Y=Yes, N=No]
  HandCopies Int(6) No. of Copies for Manual Doc. default=1
  EngKBItem VarChar(1) Switch to English Keyboard when Entering an Item default=N [Y=Yes, N=No]
  EngKBCard VarChar(1) Switch to English Keyboard when Entering a BP default=N [Y=Yes, N=No]
  OrdrPicDef VarChar(1) Set Pick Order as Default default=N [Y=Yes, N=No]
  SpltTrBOE1 VarChar(1) Split Bill of Exchange Transaction default=N [Y=Yes, N=No]
  LineNumPPg Int(6) Row Item Number Per Page default=5
  JENumPPg Int(6) Journal Entry Number Per Page default=2
  CashPay Text(16) Remark for Cash Payments
  NonCashPay Text(16) Remark for Non-Cash Payments
  MaxUOPay Num(19,6) Max. Under/Overpayment Amount
  CkeckPaper VarChar(1) Paper for Checks default=S [B=Blank Paper, S=Overflow Check Stock, P=Overflow Blank Paper]
  AllowFuPos VarChar(1) Allow Future Posting default=N [Y=Yes, N=No]
  ErdOutMode VarChar(1) ERD Mode for Outgoing Payments default=N [Y=Yes, N=No]
  ErdIncMode VarChar(1) ERD Mode for Incoming Payments default=N [Y=Yes, N=No]
  ChkDupRef VarChar(1) Check Duplicate BP Reference Number default=N [N=Without Warning, W=Warning Only, B=Block Release]
  CpyCVRef VarChar(1) Copy BP Reference Number default=N [N=No, Y=Yes]
  BatchSerPr VarChar(1) Batch/Serial No. Print Definitions default=A [A=Document and Batch/Serial No., D=Document Only, B=Batch/Serial No. Only]
  YearTrans VarChar(1) Display Transaction in Payment default=N [N=No, Y=Yes]
  ReconJeSer Int(6) Reconciliation JE Series default=0
  ReopOrder VarChar(1) Enable Reopen Orders by Return default=N [N=No, Y=Yes]
  ForceReOrd VarChar(1) Always Reopen Orders by Return default=N [N=No, Y=Yes]
  PrintRows VarChar(1) Print Rows default=A [A=All Rows, M=All Modified Rows, T=Modified Rows Excl. Tax Amount]
  orderblock VarChar(1) Block Early Posting Date default=N [Y=Yes, N=No]
  RecomPkg VarChar(1) Recommend Packaging default=N [N=No, Y=Yes]
  Enitemcost VarChar(1) Enable Setting Item Cost default=N [Y=Yes, N=No]
  ClosePQ VarChar(1) Close Related PQ default=Y [Y=Yes, N=No]
  CpyPRPrice VarChar(1) Enable Copying PR Price default=N [Y=Yes, N=No]
  EnSetCost VarChar(1) Enable Setting Cost By Default default=N
  DftPLChk VarChar(1) Default Price List Check default=N
  DfltPLSel Int(6) Default Price List Selection default=-1
  EmailOnAdd VarChar(1) Add & E-Mail default=N [Y=Yes, N=No]
  PDFOnAdd VarChar(1) Add & Export to PDF default=N [Y=Yes, N=No]
  EmailSbj nVarChar(254) E-Mail Subject
  EmailBody Text(16) E-Mail Body
  BlockWHT08 VarChar(1) Block payment in local currency WHT 08 default=N [Y=Yes, N=No]
  BlockExprt VarChar(1) Block Export to Word default=N [N=No, Y=Yes]
  BlockPrint VarChar(1) Block print document default=N [N=No, Y=Yes]
  BlockMail VarChar(1) Block Email Document default=N [N=No, Y=Yes]
  BlockToPDF VarChar(1) Block Export to PDF default=N [N=No, Y=Yes]
  BlockFax VarChar(1) Block Sent to Fax default=N [N=No, Y=Yes]
  PoDropPrss VarChar(1) PO Drop-Ship Process default=Y [Y=Yes, N=No]
  ShowCash VarChar(1) Allow Cash Accounts Only default=N [Y=Yes, N=No]
  PRUseBPTax VarChar(1) Purchase Request use BP Tax default=N [Y=Yes, N=No]
  EnblTtlEgD VarChar(1) Apply Exchange Rate of Drawn Down Payments default=N [Y=Yes, N=No]
  EnblUpdUDF VarChar(1) Enable Updating UDF default=N [Y=Yes, N=No]
  EnblDpmTax VarChar(1) Enable Tax Calculation in Down Payment Invoices default=N [Y=Yes, N=No]
  ChkRefBP VarChar(1) Validate on Customer Level default=N [Y=Yes, N=No]
  ChkRefYear VarChar(1) Validate on Fiscal Year Level default=N [Y=Yes, N=No]
  BspDpmType VarChar(1) Down Payment Type for BSP default=E [E=, R=Down Payment Request, I=Down Payment Invoice]
  ReopenByC VarChar(1) Enable the Displaying of Base Document Items When Target Documents Are Canceled default=N [N=No, Y=Yes]
  ForceReByC VarChar(1) Always Display Base Document Items When Target Documents Are Canceled default=N [N=No, Y=Yes]
  OpenSnB VarChar(1) Open SnB form for Bin First Item when Auto Allocation default=N [N=No, Y=Yes]
