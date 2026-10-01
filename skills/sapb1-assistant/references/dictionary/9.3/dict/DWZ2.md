<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DWZ2 - Dunning Wizard Array 2-Invoice Filter
Module: Marketing Documents | 43 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocType, InstlmntID, DocAbs, LetterNum, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  CardCode nVarChar(15) BP Card Code ->OCRD
  LetterNum Int(11) Letter Number
  TotalFee Num(19,6) Total Fee
  FeeCurr nVarChar(3) Total Fee Currency ->OCRN
  TtlopnIntr Num(19,6) Sum of Open Sum+Interest
  EDunLevel nVarChar(3) Edited Dunning Level
  OpnIntrCrr nVarChar(3) Total Open + Interest Currency
  DocAbs Int(11) Document Internal Number
  DocNum Int(11) Doc. No.
  InstlmntID Int(6) Installment ID
  IntrstPC Num(19,6) Interest Percent
  IntrstAmnt Num(19,6) Interest Amount
  IntrstCurr nVarChar(3) Interest Currency ->OCRN
  ChckLine VarChar(1) Checked Row default=N [Y=Yes, N=No]
  IntrstDays Int(11) Interest Days
  DocType Int(11) Source Table [13=A/R Invoice, 203=Down Payment Incoming, 165=Correction A/R Invoice, 14=A/R Credit Memo, 24=Incoming Payment, 30=Journal Transactions, -2=Open Balance, -3=Close Balance, 46=Outgoing Payments]
  DueDate Date(8) Due Date
  LetterLvl nVarChar(3) Letter Level default=0
  OpenSum Num(19,6) Open Sum
  OpenCurr nVarChar(3) Open Sum Currency
  sumIntrClc Num(19,6) Sum for Interest Calculation
  folioNum nVarChar(14) Folio Number
  LvlUpdated VarChar(1) Level Updated Flag default=N [Y=Yes, N=No]
  TotalFeeFC Num(19,6) Total Fee in Document Currency
  TotalFeeLC Num(19,6) Total Fee in Local Currency
  TotalFeeSC Num(19,6) Total Fee in System Currency
  TtlopnInFC Num(19,6) Sum of Open Sum+Interest FC
  TtlopnInSC Num(19,6) Sum of Open Sum+Interest SC
  IntrAmtFC Num(19,6) Interest Amount (FC)
  IntrAmtSC Num(19,6) Interest Amount (SC)
  OpenSumFC Num(19,6) Open Sum (FC)
  OpenSumSC Num(19,6) Open Sum (SC)
  ExeChkLine VarChar(1) Executed Checked Row default=N [Y=Yes, N=No]
  AutoPost VarChar(1) Automatic Posting default=N [N=No, B=Interest and Fee, I=Interest Only, F=Fee Only]
  DocRate Num(19,6) Document Rate
  UnpaidBoEV Num(19,6) Unpaid BoE Value
  BoENumber Int(11) BoE Number
  BoEStatus VarChar(1) BoE Status
  BoEDate Date(8) BoE Date
  BoEKey Int(11) BoE Key
  BPType VarChar(1) Business Partner Type default=C [C=Customer, S=Vendor]
  BPLId Int(11) Assigned Branch ->OBPL
