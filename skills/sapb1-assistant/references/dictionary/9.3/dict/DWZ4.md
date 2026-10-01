<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# DWZ4 - Dunning Wizard Array 4-Paging Grid
Module: Marketing Documents | 51 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RowId, WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->ODWZ
  CheckLine VarChar(1) Checked Row default=Y
  ExeChkLine VarChar(1) Executed Checked Row default=Y
  RowId Int(11) Row Num
  CardCode nVarChar(15) BP Card Code ->OCRD
  LetterNum Int(11) Letter Number
  DunnLevel Int(11) Dunning Level
  CardName nVarChar(100) BP Name
  DocCur nVarChar(3) Doc. Currency
  DocType Int(11) Source Table [13=A/R Invoice, 203=Down Payment Incoming, 165=Correction A/R Invoice, 14=A/R Credit Memo, 24=Incoming Payment, 30=Journal Transactions, -2=Open Balance, -3=Close Balance]
  DocNum Int(11) Doc. No.
  InstlmntID Int(6) Installment ID
  DueDate Date(8) Due Date
  LastLvlDte Date(8) Last Update Date
  LastDunDte Date(8) Last Dunning Date
  NewLvlDate Date(8) New Level Update Date
  DocAmntLC nVarChar(100) DOC. AMOUNT (LC)
  DocAmntFC nVarChar(100) DOC. AMOUNT (FC)
  OpenAmtLC nVarChar(100) Open Amount (LC)
  OpenAmtFC nVarChar(100) Open Amount (FC)
  IntrstDays Int(11) Interest Days
  IntrstPC Num(19,6) Interest Percent
  IntAmntLC nVarChar(100) Interest Amount (LC)
  IntAmntFC nVarChar(100) Interest Amount (FC)
  InclAmntLC nVarChar(100) Total Incl. Amount (LC)
  InclAmntFC nVarChar(100) Total Incl. Amount (FC)
  FeeLC nVarChar(100) Fee (LC)
  FeeFC nVarChar(100) Fee (FC)
  AllTotalLC nVarChar(100) Overall Total (LC)
  AllTotalFC nVarChar(100) Overall Total (FC)
  AutoPost VarChar(1) Automatic Posting default=N [N=No, B=Interest and Fee, I=Interest Only, F=Fee Only]
  LineProp Int(11) Line Property
  YearDays Int(11) Year Days
  YearlyRate Num(19,6) Yearly Rate
  LetterFrmt nVarChar(8) Letter Formant
  MinBlan Num(19,6) Min. Balance
  GrpMethod VarChar(1) Group Method
  DocEntry Int(11) DocEntry
  DocRate nVarChar(100) Exchange Rate on Document
  FeeCurr nVarChar(3) Fee Currency
  OrigFee Num(19,6) Original Fee on Dunning Term
  MinBalCurr nVarChar(3) Minimum Balance Currency
  LvlUpdated nVarChar(3) Level Updated
  DunAddr nVarChar(254) Dunning Address
  DocText nVarChar(254) Doc. Text
  ParentId Int(11) Parent Id
  BpCode2 nVarChar(15) BP Code 2
  BpType VarChar(1) BP Type
  CardName2 nVarChar(100) Card Name 2
  Comment nVarChar(254) Comment
  BPLId Int(11) Branch ID
