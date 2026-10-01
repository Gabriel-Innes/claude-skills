<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OPWZ - Payment Wizard
Module: Banking | 75 columns | ObjType: 157
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IdNumber
  NAME U: WizardName
Fields (name type(len) description [values] ->parent table):
  IdNumber Int(11) ID Number
  PmntDate Date(8) Date of Payment Run
  NextDate Date(8) A/P Due Date To
  OutgoType VarChar(1) Outgoing Type default=N [Y=Yes, N=No]
  IncomType VarChar(1) Incoming Type default=N [Y=Yes, N=No]
  CheckPmntM VarChar(1) Check Payment Terms default=N [Y=Yes, N=No]
  BnkTrnsPmM VarChar(1) Bank Transfer Payment Terms default=N [Y=Yes, N=No]
  FilePath Text(16) File Path
  PostDtFrom Date(8) Posting Date From
  PostDtTo Date(8) Posting Date To
  ValDteFrom Date(8) Due Date From
  ValDateTo Date(8) Due Date To
  ApInvAmntF Num(19,6) A/P Invoice Amount From
  ApInvAmntT Num(19,6) A/P Invoice Amount To
  PchNoFrom Int(11) A/P Invoice No. From
  PchNoTo Int(11) A/P Invoice No. To
  InvNoFrom Int(11) A/R Invoice No. From
  InvNoTo Int(11) A/R Invoice No. To
  SelPriorit Int(11) Selection Priority
  Status VarChar(1) Object Status default=S [S=Saved Wizard, R=Recommended Wizard, E=Executed Wizard, H=Scheduled Wizard, L=Scheduled Executing Wizard]
  WizardName nVarChar(100) Wizard Name
  StatusDisc nVarChar(100) Status
  Canceled VarChar(1) Canceled default=N
  BoePmnMn VarChar(1) Bill of Exchange Paymt Method default=N [Y=Yes, N=No]
  SeriesOut Int(11) Outgoing Series default=0 ->NNM1
  SeriesIn Int(11) Incoming Series default=0 ->NNM1
  TotalOut Num(19,6) Total Outgoing
  TotalIn Num(19,6) Total Incoming
  ViewIntBal VarChar(1) Include Interim Acct Balance default=N [Y=Yes, N=No]
  SelMthd VarChar(1) Selection Method default=D [M=By Monthly Invoice, D=By Document Property]
  MINumFrom Int(11) Monthly Invoice No. From
  MINumTo Int(11) Monthly Invoice No. To
  MIDateFrom Date(8) Monthly Invoice Issued Date From
  MIDateTo Date(8) Monthly Invoice Issued Date To
  MIVNumFrom Int(11) A/P Monthly Invoice No. From
  MIVNumTo Int(11) A/P Monthly Invoice No. To
  MIVDateFro Date(8) A/P Monthly Invoice Date From
  MIVDateTo Date(8) A/P Monthly Invoice Date To
  APDocDtFrm Date(8) A/P Document Date From
  APDocDtTo Date(8) A/P Document Date To
  APDueDtFrm Date(8) A/P Due Date From
  NxtPmntDat Date(8) Next Payment Run Date
  MinPayAR Num(19,6) Minimum Incoming Payment
  MinPayAP Num(19,6) Minimum Outgoing Payment
  ShowAtCard VarChar(1) Display BP Ref. No. default=N [Y=Yes, N=No]
  TolerDays Int(6) Tolerance Days
  MinCashDis Num(19,6) Min. Cash Discount
  NegBalBP VarChar(1) Include Negative Balance BP default=N [Y=Yes, N=No]
  ManualJE VarChar(1) Include Manual JEs default=Y [Y=Yes, N=No]
  NegTrans VarChar(1) Include Negative Transactions default=Y [Y=Yes, N=No]
  CDTransApp VarChar(1) Apply to Cash Discount Trans. default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  CigTo Int(11) Contract Code ID To ->OCIG
  CupFrom Int(11) Unique Code of Project From ->OCUP
  CupTo Int(11) Unique Code of Project To ->OCUP
  CigFrom Int(11) Contract Code ID From ->OCIG
  BPLId Int(11) Active Branch ->OBPL
  BoeDDFrom Date(8) BoE Due Date From
  BoeDDTo Date(8) BoE Due Date To
  BoeNumFrom Int(11) BoE No. From ->OBOE
  BoeNumTo Int(11) BoE No. To ->OBOE
  BoeStatus nVarChar(32) Bill of Exchange Status
  HaExistBoe VarChar(1) Handle Existing BoE default=N [Y=Yes, N=No]
  SeriesPOO Int(11) Outgoing Payment Order Series default=0 ->NNM1
  SeriesPOI Int(11) Incoming Payment Order Series default=0 ->NNM1
  SeqType nVarChar(4) Sequence Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  PayDueDate VarChar(1) Payment Due Date Determination default=R [R=Run Date, D=Document Due Date]
  CentrPay VarChar(1) Centralized Payment default=N [Y=Yes, N=No]
  BA_AP_From Int(11) A/P Blanket Agreement From
  BA_AP_To Int(11) A/P Blanket Agreement To
  BA_AR_From Int(11) A/R Blanket Agreement From
  BA_AR_To Int(11) A/R Blanket Agreement To
  JobId Int(11) Job ID Number
  ZeroBalBP VarChar(1) Include Zero Balance BP default=Y [Y=Yes, N=No]
  ZeroBalDoc nVarChar(50) Zero Balance Document Types default=YNNNNYNNNNN
