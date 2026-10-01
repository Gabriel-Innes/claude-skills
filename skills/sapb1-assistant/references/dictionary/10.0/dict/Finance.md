<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->

# AAC1 - Asset Classes - Depreciation Areas - History
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum, LogInstanc
  UNIQUE U: Code, DprAreaID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code ->OACS
  LineNum Int(11) Line Number
  DprAreaID nVarChar(15) Depreciation Area ID ->ODPA
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  AcctDtn nVarChar(15) Account Determination ->OADT
  DprTypID nVarChar(15) Depreciation Type ID ->ODTP
  UseLife Int(11) Useful Life
  LogInstanc Int(11) Log Instance default=0
  SnapshotId Int(11) Snapshot ID default=0

# AACP - Periods Category-Log
Module: Finance | 183 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number default=0
  PeriodCat nVarChar(10) Period Category
  FinancYear Date(8) Beginning of Financial Year
  Year Int(6) Financial Year
  PeriodName nVarChar(20) Period Name
  SubType VarChar(1) Sub-Period Type default=Y [Y=Year, Q=Quarters, M=Months, D=Days]
  PeriodNum Int(11) Number of Periods
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  LinkAct_1 nVarChar(15) Domestic Accounts Receivable ->OACT
  LinkAct_2 nVarChar(15) Checks Received ->OACT
  LinkAct_3 nVarChar(15) Cash on Hand ->OACT
  LinkAct_4 nVarChar(15) Account ->OACT
  LinkAct_5 nVarChar(15) Sales Tax Account ->OACT
  LinkAct_6 nVarChar(15) Customer's Deduction at Source ->OACT
  ComissAct nVarChar(15) Credit Card Deposit Fee ->OACT
  LinkAct_8 nVarChar(15) Purchase Tax ->OACT
  LinkAct_9 nVarChar(15) Foreign Accounts Receivable ->OACT
  LinkAct_10 nVarChar(15) Domestic Accounts Payable ->OACT
  LinkAct_11 nVarChar(15) Foreign Accounts Payable ->OACT
  LinkAct_12 nVarChar(15) Bank Transfer ->OACT
  LinkAct_13 nVarChar(15) Tax to Pay to ->OACT
  LinkAct_14 nVarChar(15) Tax Definition ->OACT
  LinkAct_15 nVarChar(15) Equipment and Assets ->OACT
  LinkAct_16 nVarChar(15) Withholding Tax ->OACT
  LinkAct_17 nVarChar(15) Advances on Corp. Income Tax ->OACT
  LinkAct_18 nVarChar(15) Opening Balance Account ->OACT
  DfltIncom nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Tax Exempt Revenue Account ->OACT
  DfltExpn nVarChar(15) Expense Account ->OACT
  ForgnIncm nVarChar(15) Revenue Account - Foreign ->OACT
  ECIncome nVarChar(15) Sales Revenue - EU ->OACT
  ForgnExpn nVarChar(15) Expense Account - Foreign ->OACT
  DfltRateDi nVarChar(15) Ex. Rate Diff. in All Currency ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  LinkAct_27 nVarChar(15) Automatic Reconciliation Diff. ->OACT
  DftStockOB nVarChar(15) Account for Opening Whse Bal. ->OACT
  LinkAct_19 nVarChar(15) Cash Discount ->OACT
  LinkAct_20 nVarChar(15) Cash Discount Clearing ->OACT
  LinkAct_21 nVarChar(15) Realized Exchange Diff. Loss ->OACT
  LinkAct_22 nVarChar(15) Cash Discount ->OACT
  LinkAct_23 nVarChar(15) Realized Exchange Diff. Loss ->OACT
  LinkAct_24 nVarChar(15) Rounding Account ->OACT
  LinkAct_25 nVarChar(15) Realized Exchange Diff. Gain ->OACT
  LinkAct_26 nVarChar(15) Realized Exchange Diff. Gain ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  RturnngAct nVarChar(15) Sales Returns Account ->OACT
  COGM_Act nVarChar(15) Cost of Goods Sold Account ->OACT
  AlocCstAct nVarChar(15) Allocation Account ->OACT
  VariancAct nVarChar(15) Variance Account ->OACT
  PricDifAct nVarChar(15) Price Difference Account ->OACT
  CDownPymnt nVarChar(15) Customer Down Payment Account ->OACT
  VDownPymnt nVarChar(15) Vendor Down Payment Account ->OACT
  CBoERcvble nVarChar(15) BoE Accounts Receivable ->OACT
  CBoEOnClct nVarChar(15) Bill of Exchange on Collection ->OACT
  CBoEPresnt nVarChar(15) Bill of Exchange Presentation ->OACT
  CBoEDiscnt nVarChar(15) Bill of Exchange Discounted ->OACT
  CUnpaidBoE nVarChar(15) Unpaid Bill of Exchange ->OACT
  VBoEPayble nVarChar(15) BoE Accounts Payable ->OACT
  VAsstBoEPy nVarChar(15) BoE Accounts Payable ->OACT
  COpenDebts nVarChar(15) Customer Doubtful Debts Acct ->OACT
  VOpenDebts nVarChar(15) Vendor Doubtful Debts Account ->OACT
  PurchseAct nVarChar(15) Purchase Account ->OACT
  PaReturnAc nVarChar(15) Purchase Return Account ->OACT
  PaOffsetAc nVarChar(15) Purchase Offset Account ->OACT
  LinkAct_28 nVarChar(15) Period-End Closing Account ->OACT
  ExDiffAct nVarChar(15) Exchange Rate Difference Acct ->OACT
  BalanceAct nVarChar(15) Goods Clearing Account ->OACT
  BnkChgAct nVarChar(15) Bank Charge Account ->OACT
  LinkAct_29 nVarChar(15) Other Receivable ->OACT
  LinkAct_30 nVarChar(15) Other Payable ->OACT
  IncmAcct nVarChar(15) Def. Inv. Reval. Revenue Acct ->OACT
  ExpnAcct nVarChar(15) Def. Inventory Reval. Expense ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  ExpClrAct nVarChar(15) Expense Account for Tax ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  CostRevAct nVarChar(15) COGS Revaluation Acct ->OACT
  RepomoAct nVarChar(15) REPOMO Revaluation Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  SaleVatOff nVarChar(15) Down Payment Tax Offset Acct ->OACT
  PurcVatOff nVarChar(15) Down Payment Tax Offset Acct ->OACT
  DpmSalAct nVarChar(15) Payment Advances ->OACT
  DpmPurAct nVarChar(15) Payment Advances ->OACT
  ExpVarAct nVarChar(15) Expense and Inventory Account ->OACT
  CostOffAct nVarChar(15) Cost of Sale Rev. Offset Acct ->OACT
  ECExepnses nVarChar(15) Expense Account - EU ->OACT
  StockAct nVarChar(15) Inventory Account ->OACT
  DflInPrcss nVarChar(15) Default for Stk Itm in Process ->OACT
  DfltInCstm nVarChar(15) Default for Stock Item in Cust ->OACT
  DfltProfit nVarChar(15) Inventory Offset - Incr. Acct ->OACT
  DfltLoss nVarChar(15) Inventory Offset - Decr. Acct ->OACT
  VAssets nVarChar(15) Vendor Asset Account ->OACT
  StockRvAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkRvOfAct nVarChar(15) Invent Revaluation Offset Acct ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  DfltCard nVarChar(15) Invoice and Payment BP ->OCRD
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  GlRvOffAct nVarChar(15) G/L Revaluation Offset Account ->OACT
  OverpayAP nVarChar(15) Overpayment A/P Account ->OACT
  UndrpayAP nVarChar(15) Underpayment A/P Account ->OACT
  OverpayAR nVarChar(15) Overpayment A/R Account ->OACT
  UndrpayAR nVarChar(15) Underpayment A/R Account ->OACT
  ARCMAct nVarChar(15) Sales Credit Account ->OACT
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign ->OACT
  ARCMEUAct nVarChar(15) Sales Credit Acct - EU ->OACT
  APCMAct nVarChar(15) Purchase Credit Account ->OACT
  APCMFrnAct nVarChar(15) Purchase Credit Acct - Foreign ->OACT
  APCMEUAct nVarChar(15) Purchase Credit Account - EU ->OACT
  NegStckAct nVarChar(15) Negative Inventory Adj. Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Acct ->OACT
  GLGainXdif nVarChar(15) Realized Exchange Diff. Gain ->OACT
  GLLossXdif nVarChar(15) Realized Exchange Diff. Loss ->OACT
  AmountDiff nVarChar(15) Amount Differences ->OACT
  SlfInvIncm nVarChar(15) Self Invoice Revenue Account ->OACT
  SlfInvExpn nVarChar(15) Self Invoice Expense Account ->OACT
  OnHoldAct nVarChar(15) Capital Goods On Hold Account ->OACT
  PlaAct nVarChar(15) PLA ->OACT
  ICClrAct nVarChar(15) Incoming CENVAT Clearing Acct ->OACT
  OCClrAct nVarChar(15) Outgoing CENVAT Clearing Acct ->OACT
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  SalDpmInt nVarChar(15) A/R DP Interim ->OACT
  PurDpmInt nVarChar(15) A/P DP Interim ->OACT
  ExrateOnDt nVarChar(15) Ex Rate on Def Tax Account ->OACT
  UserSign2 Int(6) Updating User ->OUSR
  EURecvAct nVarChar(15) EU Accounts Receivable ->OACT
  EUPayAct nVarChar(15) EU Accounts Payable ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  DunIntrst nVarChar(15) Dunning Interest ->OACT
  DunFee nVarChar(15) Dunning Fee ->OACT
  SnapShotId Int(11) Snapshot ID default=0
  TDSInterst nVarChar(15) TDS Interest Acct ->OACT
  TDSCharges nVarChar(15) TDS Other Charges Acct ->OACT
  SrvTaxClr nVarChar(15) Service Tax Clearing Account ->OACT
  ARConDiffG nVarChar(15) Realized Conversion Diff. Gain ->OACT
  ARConDiffL nVarChar(15) Realized Conversion Diff. Loss ->OACT
  APConDiffG nVarChar(15) Realized Conversion Diff. Gain ->OACT
  APConDiffL nVarChar(15) Realized Conversion Diff. Loss ->OACT
  GLConDiffG nVarChar(15) Realized Conversion Diff. Gain ->OACT
  GLConDiffL nVarChar(15) Realized Conversion Diff. Loss ->OACT
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account
  TDSFee nVarChar(15) TDS Fee Acct ->OACT
  ResRevenue nVarChar(15) Revenue Account ->OACT
  ResExpense nVarChar(15) Expense Account ->OACT
  ResSalesCr nVarChar(15) Sales Credit Account ->OACT
  ResPurchCr nVarChar(15) Purchase Credit Account ->OACT
  ResNotInv nVarChar(15) Res. Received Not Inv. Account ->OACT
  ResStdExp1 nVarChar(15) Std Cost Expense 1 ->OACT
  ResStdExp2 nVarChar(15) Std Cost Expense 2 ->OACT
  ResStdExp3 nVarChar(15) Std Cost Expense 3 ->OACT
  ResStdExp4 nVarChar(15) Std Cost Expense 4 ->OACT
  ResStdExp5 nVarChar(15) Std Cost Expense 5 ->OACT
  ResStdExp6 nVarChar(15) Std Cost Expense 6 ->OACT
  ResStdExp7 nVarChar(15) Std Cost Expense 7 ->OACT
  ResStdExp8 nVarChar(15) Std Cost Expense 8 ->OACT
  ResStdExp9 nVarChar(15) Std Cost Expense 9 ->OACT
  ResStdEx10 nVarChar(15) Std Cost Expense 10 ->OACT
  ResWipAct nVarChar(15) Resource WIP Account ->OACT
  ResScrapAc nVarChar(15) Scrap Account ->OACT
  WipOffPlAc nVarChar(15) WIP Offset P&L Account ->OACT
  ResOffPlAc nVarChar(15) Resource Offset P&L Account ->OACT
  ERDInARAct nVarChar(15) Exchange Rate Interim Sales Account ->OACT
  ERDInAPAct nVarChar(15) Exchange Rate Interim Purchase Account ->OACT
  CSDInARAct nVarChar(15) Cash Discount Interim Sales Account ->OACT
  CSDInAPAct nVarChar(15) Cash Discount Interim Purchase Account ->OACT
  GSTInAct nVarChar(15) GST Input Interim Account ->OACT
  GSTInterst nVarChar(15) GST Interest Account ->OACT
  GSTCharges nVarChar(15) GST Other Charges Account ->OACT
  GSTFee nVarChar(15) GST Fee Account ->OACT
  WTInARAct nVarChar(15) Interim Account for Tax ->OACT
  WTInAPAct nVarChar(15) Interim Account for Tax ->OACT
  WTExDifAct nVarChar(15) Withholding Tax Exchange Rate Diff. Account ->OACT

# AACS - Asset Classes - History
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  AssetType VarChar(1) Asset Type default=G [G=General, L=Low Value Asset]
  LimitFrom Num(19,6) Value Limit From
  LimitTo Num(19,6) Value Limit To
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  BPLId Int(11) Branch ->OBPL
  AttrGrp Int(11) Attribute Group default=-1 ->OFAA
  SnapshotId Int(11) Snapshot ID default=0

# AACT - G/L Account - History
Module: Finance | 129 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AcctCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AcctCode nVarChar(15) Account Code
  AcctName nVarChar(100) Account Name
  CurrTotal Num(19,6) Current Balance
  EndTotal Num(19,6) Opening Balance
  Finanse VarChar(1) Cash Account default=N [Y=Yes, N=No]
  Groups nVarChar(8) Main Group
  Budget VarChar(1) Budget default=N [Y=Yes, N=No]
  Frozen VarChar(1) Account on Hold [Y/N] default=N [Y=Yes, N=No]
  Free_2 VarChar(1) Free 2
  Postable VarChar(1) Account Type [Active/Title] default=Y [Y=Active Account, N=Title Account]
  Fixed VarChar(1) Primary Account
  Levels Int(6) Account Level default=2
  ExportCode nVarChar(10) Data Export Code
  GrpLine Int(11) Account Location in Group
  FatherNum nVarChar(15) Parent Account Key
  AccntntCod nVarChar(15) External Code
  CashBox VarChar(1) Primary Account [Y/N] default=N [Y=Yes, N=No]
  GroupMask Int(6) Group Mask default=1
  RateTrans VarChar(1) Conversion Differences default=Y [Y=Yes, N=No]
  TaxIncome VarChar(1) Tax Definition default=N [Y=Yes, N=No]
  ExmIncome VarChar(1) Tax Definition default=N [Y=Yes, N=No]
  ExtrMatch Int(11) External Reconciliation No.
  IntrMatch Int(11) Internal Reconciliation No.
  ActType VarChar(1) Account Type default=N [I=Sales, E=Expenditure, N=Other]
  Transfered VarChar(1) Year Transferred [Y/N] default=N [Y=Yes, N=No]
  BlncTrnsfr VarChar(1) Balances Transferred [Y/N] default=N [Y=Yes, N=No]
  OverType VarChar(1) Distribution Rule default=N [N=None, Y=Yes]
  OverCode nVarChar(8) Distribution Rule Code ->OOCR
  SysMatch Int(11) System Reconciliation No. default=-1
  PrevYear VarChar(1) Transferred from Prev. Year default=N [Y=Yes, N=No]
  ActCurr nVarChar(3) Account Currency ->OCRN
  RateDifAct nVarChar(15) Rate Differences Acct
  SysTotal Num(19,6) Balance (SC)
  FcTotal Num(19,6) Balance (Account Currency)
  Protected VarChar(1) Confidential Account default=N [Y=Yes, N=No]
  RealAcct VarChar(1) Indexed Account default=N [Y=Yes, N=No]
  Advance VarChar(1) Advance Payments default=Y [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  FrgnName nVarChar(100) Foreign Name
  Details nVarChar(254) Details - History
  ExtraSum Num(19,6) Additional Amount
  Project nVarChar(20) Project Code ->OPRJ
  RevalMatch VarChar(1) Revaluation Coordinated default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  LocMth VarChar(1) Reconciliation in LC default=Y [Y=Yes, N=No]
  MTHCounter Int(11) MTH Counter
  BNKCounter Int(11) BNK Counter
  UserSign Int(6) User Signature ->OUSR
  LocManTran VarChar(1) Control Account default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type ->ADP1
  ValidFor VarChar(1) Active default=N [Y=Yes, N=No]
  ValidFrom Date(8) Active From
  ValidTo Date(8) Active To
  ValidComm nVarChar(30) Active Remarks
  FrozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  FrozenFrom Date(8) Inactive From
  FrozenTo Date(8) Inactive To
  FrozenComm nVarChar(30) Inactive Remarks
  Counter Int(11) BP Bank Account default=0
  Segment_0 nVarChar(20) Segment 0
  Segment_1 nVarChar(20) Segment 1
  Segment_2 nVarChar(20) Segment 2
  Segment_3 nVarChar(20) Segment 3
  Segment_4 nVarChar(20) Segment 4
  Segment_5 nVarChar(20) Segment 5
  Segment_6 nVarChar(20) Segment 6
  Segment_7 nVarChar(20) Segment 7
  Segment_8 nVarChar(20) Segment 8
  Segment_9 nVarChar(20) Segment 9
  FormatCode nVarChar(210) Format Code
  CfwRlvnt VarChar(1) Cash Flow Relevant [Y/N] default=N [Y=Yes, N=No]
  ExchRate VarChar(1) Exchange Rate Differences default=Y [Y=Yes, N=No]
  RevalAcct nVarChar(15) Revaluation Account
  LastRevBal Num(19,6) Last Revaluation Balance
  LastRevDat Date(8) Last Revaluation Date
  DfltVat nVarChar(8) Default VAT Group ->OVTG
  VatChange VarChar(1) Allow Change VAT Group default=Y [Y=Yes, N=No]
  Category Int(11) Category ->OACG
  TransCode nVarChar(4) Transaction Code ->OTRC
  OverCode5 nVarChar(8) Loading Factor Code 5 ->OOCR
  OverCode2 nVarChar(8) Loading Factor Code 2 ->OOCR
  OverCode3 nVarChar(8) Loading Factor Code 3 ->OOCR
  OverCode4 nVarChar(8) Loading Factor Code 4 ->OOCR
  DfltTax nVarChar(8) Default Tax Code ->OSTC
  TaxPostAcc VarChar(1) Default Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  AcctStrLe nVarChar(2) Account Structure Level
  MeaUnit nVarChar(10) Measurement Unit
  BalDirect nVarChar(4) Direction of Balance default=0 [0=, 1=Credit, 2=Debit]
  UserSign2 Int(6) Updating User ->OUSR
  PlngLevel nVarChar(2) B1i Info for Integration
  MultiLink VarChar(1) Allow Multiple Linking default=N [N=No, Y=Yes]
  PrjRelvnt VarChar(1) Project Relevant default=N [Y=Yes, N=No]
  Dim1Relvnt VarChar(1) Dimension 1 Relevant default=N [Y=Yes, N=No]
  Dim2Relvnt VarChar(1) Dimension 2 Relevant default=N [Y=Yes, N=No]
  Dim3Relvnt VarChar(1) Dimension 3 Relevant default=N [Y=Yes, N=No]
  Dim4Relvnt VarChar(1) Dimension 4 Relevant default=N [Y=Yes, N=No]
  Dim5Relvnt VarChar(1) Dimension 5 Relevant default=N [Y=Yes, N=No]
  AccrualTyp VarChar(1) Accrual Type default=N [N=None, P=Posting Account, C=Calculation Account, I=Calculation Interim Account]
  DatevAcct nVarChar(8) DATEV Account
  DatevAutoA VarChar(1) DATEV Automatic Account default=N [Y=Yes, N=No]
  DatevFirst VarChar(1) First Data Entry default=Y [Y=Yes, N=No]
  SnapShotId Int(11) Snapshot ID default=0
  PCN874Rpt VarChar(1) PCN 874 Report Relevant default=N [Y=Yes, N=No]
  SCAdjust VarChar(1) SC Adjustment default=N [Y=Yes, N=No]
  BPLId Int(11) Assigned Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  SubLedgerN nVarChar(60) Subledger No.
  VATRegNum nVarChar(32) VAT Reg. Number
  ActId nVarChar(210) Account Identifier
  ClosingAcc nVarChar(15) G/L Account Closing
  PurpCode nVarChar(2) Account Purpose Code [01=Contas de ativo, 02=Contas de Passivo, 03=Patrim�nio L�quido, 04=Contas de Resultado, 05=Contas de Compensa��o, 09=Outras]
  RefCode nVarChar(30) Referential Account Code
  BlocManPos VarChar(1) Block Manual Posting default=N
  PriAccCode nVarChar(15) Primary Closing Account ->OACT
  CstAccOnly VarChar(1) Cost Account Only default=N [Y=YES, N=NO]
  AlloweFrom Num(19,6) Account Balance Allowed From
  AllowedTo Num(19,6) Account Balance Allowed To
  BalanceA VarChar(1) Account Balance Allowed default=N [N=NO, Y=YES]
  RmrkTmpt Int(11) Remark Text Template ->OTTR
  CemRelvnt VarChar(1) Cost Element Relevant default=N [N=No, Y=Yes]
  CemCode nVarChar(20) Cost Element Code ->OCEM
  StdActCode nVarChar(35) Standard Account Code
  TaxonCode nVarChar(15) Taxonomy Code
  InClassTyp Int(11) Income Class. Type ->OICP
  InClassCat Int(11) Income Class. Category ->OICC
  ExClassTyp Int(11) Expense Class. Type ->OECP
  ExClassCat Int(11) Expense Class. Category ->OECC

# AADT - Fixed Assets Account Determination - History
Module: Finance | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  BalanceAct nVarChar(15) Asset Balance Sheet Account ->OACT
  ClrAcqAct nVarChar(15) Acquisition Clearing Account ->OACT
  RevResvAct nVarChar(15) Revaluation Reserve ->OACT
  OrdDprAct nVarChar(15) Ordinary Depreciation ->OACT
  OrdDprAcc nVarChar(15) Accumulated Ordinary Depr. ->OACT
  UnpDprAct nVarChar(15) Unplanned Depreciation ->OACT
  UnpDprAcc nVarChar(15) Accumulated Unplanned Depr. ->OACT
  SpDprAct nVarChar(15) Special Depreciation ->OACT
  SpDprAcc nVarChar(15) Accumulated Special Depr. ->OACT
  SaRevNAct nVarChar(15) Revenue from Asset Sales (Net) ->OACT
  ReExpNAct nVarChar(15) Retirement with Expense (Net) ->OACT
  ReRevNAct nVarChar(15) Retirement with Revenue (Net) ->OACT
  ReNBVeAct nVarChar(15) NBV Retirement Expense (Gross) ->OACT
  ReNBVrAct nVarChar(15) NBV Retirement Revenue (Gross) ->OACT
  ClrDscAct nVarChar(15) Cash Discount Clearing Account ->OACT
  RevReAct nVarChar(15) Revenue Account for Retirement ->OACT
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User
  UpdateDate Date(8) Date of Update
  ClearAccRe nVarChar(15) Revenue Clearing Account ->OACT
  RevResvClr nVarChar(15) Revaluation Reserve Clearing ->OACT
  SnapshotId Int(11) Snapshot ID default=0
  RevAct nVarChar(15) Revaluation Account ->OACT
  RevLossAct nVarChar(15) Revaluation Loss ->OACT

# ACD1 - Credit Memo - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACD
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  AcctCode nVarChar(15) Account Code ->OACT
  Quantity Num(19,6) Quantity
  LineTotal Num(19,6) Line Total
  TotalFrgn Num(19,6) Line Total (FC)
  TotalSys Num(19,6) Line Total (SC)
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  NewItemCod nVarChar(50) New Item Code ->OITM
  Partial VarChar(1) Partial default=N [Y=Yes, N=No]
  APC Num(19,6) APC
  NewAstCls nVarChar(20) New Asset Class ->OACS
  ObjType nVarChar(20) Object Type
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 130=APC Write-Up, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 310=Full Transfer, 320=Partial Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# ACD2 - Credit Memo - Area Journal Transactions
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACD
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  JrnlMemo nVarChar(254) Journal Remarks
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
  TransNum Int(11) Transaction Number ->OJDT
  JrnlMemo1 nVarChar(254) Cancellation Journal Remarks
  TransNum1 Int(11) Cancellation Transaction No. ->OJDT

# ACD3 - Credit Memo - Item Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ItemLine, DprArea
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACQ
  ItemLine Int(11) Item Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Total Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSys Num(19,6) Total (SC)
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0

# ACQ1 - Capitalization - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACQ
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  AcctCode nVarChar(15) Account Code ->OACT
  Quantity Num(19,6) Quantity
  LineTotal Num(19,6) Line Total
  TotalFrgn Num(19,6) Line Total (FC)
  TotalSys Num(19,6) Line Total (SC)
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  NewItemCod nVarChar(50) New Item Code ->OITM
  Partial VarChar(1) Partial default=N [Y=Yes, N=No]
  APC Num(19,6) APC
  NewAstCls nVarChar(20) New Asset Class ->OACS
  ObjType nVarChar(20) Object Type
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 130=APC Write-Up, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 310=Full Transfer, 320=Partial Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# ACQ2 - Capitalization - Area Journal Transactions
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACQ
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  JrnlMemo nVarChar(254) Journal Remarks
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
  TransNum Int(11) Transaction Number ->OJDT
  JrnlMemo1 nVarChar(254) Cancellation Journal Remarks
  TransNum1 Int(11) Cancellation Transaction No. ->OJDT

# ACQ3 - Capitalization - Item Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ItemLine, DprArea
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACQ
  ItemLine Int(11) Item Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Total Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSys Num(19,6) Total (SC)
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0

# ACS1 - Asset Classes - Depreciation Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum
  UNIQUE U: Code, DprAreaID
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code ->OACS
  LineNum Int(11) Line Number
  DprAreaID nVarChar(15) Depreciation Area ID ->ODPA
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  AcctDtn nVarChar(15) Account Determination ->OADT
  DprTypID nVarChar(15) Depreciation Type ID ->ODTP
  UseLife Int(11) Useful Life
  LogInstanc Int(11) Log Instance default=0
  SnapshotId Int(11) Snapshot ID default=0

# ADMC - G/L Account Determination Criteria - Inventory - History
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DmcId, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DmcId Int(6) Determination ID
  DmcAlias nVarChar(100) Determination Alias
  Active VarChar(1) Determination Status default=N [Y=Yes, N=No]
  Priority Int(6) Determination Priority
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  AdvRulCol Int(6) Advanced Rules Column
  IsUDF VarChar(1) Is User Defined Field default=N [Y=Yes, N=No]

# ADPA - Fixed Asset Depreciation Areas - History
Module: Finance | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  DirectDpr VarChar(1) Direct Depreciation default=D [D=Direct Posting, I=Indirect Posting]
  RetMeth VarChar(1) Retirement Method default=G [G=Gross, N=Net]
  AreaType VarChar(1) Area Type default=O [L=Posting to G/L, O=Additional Area, D=Derived Area]
  DrvdArea nVarChar(15) Derived Area ->ODPA
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User
  UpdateDate Date(8) Date of Update
  MainArea VarChar(1) Main Booking Area default=N [Y=Yes, N=No]
  CreditCtrl VarChar(1) Tax Credit Control default=N [Y=Yes, N=No]
  TaxType Int(11) Tax Type ->OSTT
  DirRevPost VarChar(1) Direct Revenue Posting default=N [Y=Yes, N=No]
  SnapshotId Int(11) Snapshot ID default=0
  BpTaxCorr nVarChar(15) BP for Tax Correction ->OCRD
  ItmTaxCorr nVarChar(50) Item for Tax Correction ->OITM
  UsgTaxCorr Int(11) Usage for Tax Correction ->OUSG

# ADT1 - Depreciation Types - Rows - History
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Level, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code ->ODTP
  Level Int(11) Level
  Base nVarChar(3) Base default=APC [APC=Acquisition Value, NBV=Net Book Value]
  Years Int(11) Number of Years
  Percentage Num(19,6) Percentage
  LogInstanc Int(11) Log Instance default=0
  Amount Num(19,6) Amount
  SnapshotId Int(11) Snapshot ID default=0

# ADTP - Fixed Assets Depreciation Types - History
Module: Finance | 51 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  DprMeth nVarChar(2) Depreciation Method default=NO [NO=No Depreciation, SL=Straight Line, SP=Straight Line Period Control, DB=Declining Balance, ML=Multilevel, WO=Immediate Write-Off, SD=Special Depreciation, MD=Manual Depreciation, CF=Accelerated]
  DprTo Num(19,6) Minimum Depreciated Value
  Rounding VarChar(1) Round Year End Book Value default=Y [Y=Yes, N=No]
  InclSalv VarChar(1) Include Salvage Value in Depr. default=N [Y=Yes, N=No]
  SalvPerc Num(19,6) Percentage for Salvage Value
  PerAcq nVarChar(2) Period Control for Acquisition default=PR [PR=Pro Rata Temporis, HY=First Year Convention, 6M=Half Year, FY=Full Year]
  PerSubAcq nVarChar(2) Period Control Subacquisition default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, FY=Full Year]
  PerRet nVarChar(2) Period Control for Retirement default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, EL=After End of Useful Life]
  AcqPRTyp nVarChar(3) Type of PRT for Acquisition default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]
  SubPRTyp nVarChar(3) Type of PR for Subacquisition default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]
  RetPRTyp nVarChar(3) Type of PR for Retirement default=EDB [EDB=Exact Daily Base, LPP=Last Day of Prior Period, LCP=Last Day of Current Period]
  PerDpRev Num(19,6) Depreciation to Be Reversed %
  ValidFrom Date(8) Valid From default=19000101
  ValidTo Date(8) Valid To default=20991231
  sCalcMeth nVarChar(3) Calc. Method for Straight Line default=APC [APC=Acquisition Value/Total Useful Life, PRC=Percentage of Acquisition Value, NBV=Net Book Value/Remaining Life]
  sPercent Num(19,6) Percentage for Straight Line
  dBase nVarChar(3) Base for Declining Balance default=NBV [NBV=Net Book Value]
  dPercent Num(19,6) Percentage for Decl. Balance
  dFactor Num(19,6) Factor for Declining Balance default=1
  dAltDprTyp nVarChar(15) Auto. Change Depreciation Type ->ODTP
  maDecBase VarChar(1) Reduce Depreciation Base default=Y [Y=Yes, N=No]
  spMeth VarChar(1) Calc. Method for Special Depr. default=D [D=Additional, A=Alternative]
  spConcPer Int(11) Concession Period in Years
  spMaxPerc Num(19,6) Maximum Percentage
  spAdDpr nVarChar(15) Normal Depreciation ->ODTP
  spAlDpr nVarChar(15) Alternative Depreciation ->ODTP
  PoolID nVarChar(2) Depreciation Type Pool ID ->ODPP
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  DprPer VarChar(1) Depreciation Periods default=S [S=Standard, I=Individual, U=Individual Usage]
  PerFactor Num(19,6) Period Factor default=1
  spMaxAmnt Num(19,6) Maximum Amount
  spMaxFlag VarChar(1) Max. [Percentage\Amount] default=P [P=Percentage, A=Amount]
  CalcBase VarChar(1) Calculation Base default=Y [Y=Yearly, M=Monthly]
  DeprEndLFY VarChar(1) Depr. End at Last Full Year default=N [Y=Yes, N=No]
  AccuPriorP VarChar(1) Accu. Depr. of Prior Periods default=N [Y=Yes, N=No]
  DeltaCoeff Int(11) Delta Coefficient default=0
  MaxDepr Num(19,6) Maximum Depreciable Value
  FactorFFY VarChar(1) Factor Only Relevant to FFY default=N [Y=Yes, N=No]
  SnapshotId Int(11) Snapshot ID default=0
  PerTranSou nVarChar(2) Period Control Transfer Source default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, FY=Full Year]
  PerTranTar nVarChar(2) Period Control Transfer Target default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, EL=After End of Useful Life]
  TranSPRTyp nVarChar(3) Type of PR for Transfer Source default=EDB [EDB=Exact Daily Base, LPP=Last Day of Prior Period, LCP=Last Day of Current Period]
  TranTPRTyp nVarChar(3) Type of PR for Transfer Target default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]
  RoundMeth VarChar(1) Rounding Method default=N [N=Truncate to Integer, U=Round Up to Integer, D=Round Down to Integer]

# AEB1 - VAT Exemptions for Business Partners Row - History
Module: Finance | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineNum Int(11) Row Number
  ExmpDoc nVarChar(40) Exemption Doc. No.
  IssueDate Date(8) Date of Issue
  IssueTime Int(11) Time of Issue
  ExmpType Int(6) Exemption Type ->OVET
  AllItems VarChar(1) Apply to All Items default=N [N=No, Y=Yes]
  ItemCode nVarChar(50) Item No. ->OITM
  ItemDesc nVarChar(200) Item Description
  Rate Num(19,6) Rate %
  TaxCode nVarChar(8) Exemption Tax Code ->OSTC
  AuthName nVarChar(160) Name of Authorities
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  LogInstanc Int(11) Log Instance default=0
  VisOrder Int(11) Visual Order

# AEXT - Expense Types
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ExpType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ExpType nVarChar(4) Expense Type
  ExpName nVarChar(30) Expense Name
  ExpAcct nVarChar(15) G/L Account ->OACT
  PaidByComp VarChar(1) Paid By Company default=N [Y=Yes, N=No]
  VatGroup nVarChar(8) VAT Group ->OSTC
  VatGrpEU nVarChar(8) VAT Group ->OVTG
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# AFA1 - Asset Document - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, LogInstanc, ObjType
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->AFAD
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  AcctCode nVarChar(15) Account Code ->OACT
  Quantity Num(19,6) Quantity
  LineTotal Num(19,6) Line Total
  TotalFrgn Num(19,6) Line Total (FC)
  TotalSys Num(19,6) Line Total (SC)
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  NewItemCod nVarChar(50) New Item Code ->OITM
  Partial VarChar(1) Partial default=N [Y=Yes, N=No]
  APC Num(19,6) APC
  NewAstCls nVarChar(20) New Asset Class ->OACS
  ObjType nVarChar(20) Object Type
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 130=APC Write-Up, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 310=Full Transfer, 320=Partial Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# AFA2 - Asset Document - Area Journal Transactions
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum, ObjType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->AFAD
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  JrnlMemo nVarChar(254) Journal Remarks
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
  TransNum Int(11) Transaction Number ->OJDT
  JrnlMemo1 nVarChar(254) Cancellation Journal Remarks
  TransNum1 Int(11) Cancellation Transaction No. ->OJDT

# AFAD - Asset Document - History
Module: Finance | 44 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ObjType, LogInstanc
  INDEX U: DocNum, ObjType, LogInstanc, PIndicator
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PeriodCat nVarChar(10) Period Category
  FinncPriod Int(11) Posting Period ->OFPR
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=P [P=Posted, D=Draft, C=Canceled]
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  Reference nVarChar(32) Reference
  ObjType nVarChar(20) Object Type
  Currency nVarChar(3) Currency ->OCRN
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Rate
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  TransType nVarChar(20) Original Document default=-1 [13=A/R Invoice, 19=A/P Credit Memo, 18=A/P Invoice, 46=Outgoing Payment, 163=A/P Correction Invoice, 1470000049=Capitalization, 1470000060=Fixed Assets Credit Memo, -1=All Transactions, 1470000075=Manual Depreciation, 1470000090=Fixed Assets Transfer, 1470000094=Retirement]
  CreatedBy Int(11) Original
  JrnlMemo nVarChar(254) Journal Remarks
  AssetDate Date(8) Asset Value Date
  CurSource VarChar(1) Base Currency default=L [L=Local Currency, S=System Currency, F=Foreign Currency]
  DocType nVarChar(15) Document Type default=PL [PL=Ordinary Depreciation, UP=Unplanned Depreciation, SD=Special Depreciation, AP=Appreciation, TR=Asset Transfer, NC=Sales, SC=Scrapping, TC=Asset Class Transfer]
  PrjSmarz VarChar(1) Summarize by Project default=N [Y=Yes, N=No]
  DstRlSmarz VarChar(1) Summarize by Distribution Rule default=N [Y=Yes, N=No]
  ManDprType nVarChar(15) Manual Depreciation Type ->ODTP
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  DprArea nVarChar(15) Depreciation Area ->ODPA
  BPLId Int(11) Branch ->OBPL
  BaseRef nVarChar(11) Base Reference
  LVARetire VarChar(1) Low Value Asset Retirement default=N [Y=Yes, N=No]
  CancelOpt Int(6) Cancelation Option default=1
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  GdsMovType nVarChar(2) Goods Movement Type

# AFPR - Posting Period-Log
Module: Finance | 25 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) System Number
  Code nVarChar(20) Period Code
  Name nVarChar(20) Period Name
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  Free2 VarChar(1) Active for Feed default=Y [Y=Yes, N=No]
  Free3 VarChar(1) Locked default=N [N=Unlocked, S=Unlocked Except Sales, C=Closing Period, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SubNum Int(11) No. of Sub-Period
  Free VarChar(1) Free
  Free1 VarChar(1) Free1
  Addition VarChar(1) Additional Sub-Periods default=N [Y=Yes, N=No]
  AddNum Int(11) No. of Additional
  Category nVarChar(10) Category ->OACP
  Indicator nVarChar(10) Period Indicator ->OPID
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  WasStatChd VarChar(1) Status Was Checked default=N [N=No, Y=Yes]
  PeriodStat VarChar(1) Period Status default=N [N=Unlocked, S=Unlocked Except Sales, C=Closing Period, Y=Locked, A=Archived]
  UserSign2 Int(6) Updating User ->OUSR

# AGAR - G/L Account Advanced Rules - History
Module: Finance | 89 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PeriodCat nVarChar(10) Period Category
  FinancYear Date(8) Beginning of Financial Year
  Year Int(6) Financial Year
  PeriodName nVarChar(20) Period Name
  SubType VarChar(1) Sub-Period Type default=Y [Y=Year, Q=Quarters, M=Months, D=Days]
  PeriodNum Int(11) Number of Periods
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  ItemCode nVarChar(50) Item No. ->OITM
  ItmsGrpCod Int(6) Item Group ->OITB
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  BPGrpCod Int(6) BP Group ->OCRG
  LicTradNum nVarChar(32) Federal Tax ID default=!^| [!^|=All, !^|E=Empty, !^|F=Filled, Enter Tax ID=Enter Tax ID]
  ShipCountr nVarChar(3) Ship-to Country/Region ->OCRY
  ShipState nVarChar(3) Ship-To State ->OCST
  Comments nVarChar(254) Remarks
  CreateDate Date(8) Creation Date
  RuleCode nVarChar(20) Advanced Rule Code
  GLMethod VarChar(1) Get G/L Account By default=A [A=General, W=Warehouse, C=Item Group]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  DfltExpn nVarChar(15) Expense Account ->OACT
  DfltIncom nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Tax Exempt Revenue Account ->OACT
  StockAct nVarChar(15) Inventory Account ->OACT
  COGM_Act nVarChar(15) Cost of Goods Sold Account ->OACT
  AlocCstAct nVarChar(15) Allocation Account ->OACT
  VariancAct nVarChar(15) Variance Account ->OACT
  PricDifAct nVarChar(15) Price Difference Account ->OACT
  NegStckAct nVarChar(15) Negative Inventory Adj. Acct ->OACT
  DfltLoss nVarChar(15) Inventory Offset - Decr. Acct ->OACT
  DfltProfit nVarChar(15) Inventory Offset - Incr. Acct ->OACT
  RturnngAct nVarChar(15) Sales Returns Account ->OACT
  ECIncome nVarChar(15) Revenue Account - EU ->OACT
  ECExepnses nVarChar(15) Expense Account - EU ->OACT
  ForgnIncm nVarChar(15) Revenue Account - Foreign ->OACT
  ForgnExpn nVarChar(15) Expense Account - Foreign ->OACT
  PurchseAct nVarChar(15) Purchase Account ->OACT
  PaReturnAc nVarChar(15) Purchase Return Account ->OACT
  PaOffsetAc nVarChar(15) Purchase Offset Account ->OACT
  ExDiffAct nVarChar(15) Exchange Rate Differences Acct ->OACT
  BalanceAct nVarChar(15) Goods Clearing Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  StockRvAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkRvOfAct nVarChar(15) Inventory Reval. Offset Acct ->OACT
  CostRevAct nVarChar(15) COGS Revaluation Acct ->OACT
  CostOffAct nVarChar(15) COGS Revaluation Offset Acct ->OACT
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account ->OACT
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  ARCMAct nVarChar(15) Sales Credit Account ->OACT
  APCMAct nVarChar(15) Purchase Credit Account ->OACT
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign ->OACT
  APCMFrnAct nVarChar(15) Purchase Credit Acct - Foreign ->OACT
  ARCMEUAct nVarChar(15) Sales Credit Account - EU ->OACT
  APCMEUAct nVarChar(15) Purchase Credit Account - EU ->OACT
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  Active VarChar(1) Is Rule Active default=Y [Y=Yes, N=No]
  CmpPrivate VarChar(1) Company/Private/Government default=A [A=All, C=Company, I=Private, G=Government]
  VatGroup nVarChar(8) Tax Definition ->OVTG
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  Usage Int(11) Usage Code for Document ->OUSG
  FreeChrgSA nVarChar(15) Free of Charge Sales Account ->OACT
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account ->OACT
  UDF1 nVarChar(254) User Defined Field 1
  UDF2 nVarChar(254) User Defined Field 2
  UDF3 nVarChar(254) User Defined Field 3
  UDF4 nVarChar(254) User Defined Field 4
  UDF5 nVarChar(254) User Defined Field 5

# AJD1 - Journal Entry - History - Rows
Module: Finance | 145 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TransId, Line_ID, LogInstanc
  SHORT_NAME: ShortName, IntrnMatch
  ACCOUNT: Account, IntrnMatch
  TRANS_TYPE: TransType
  PROFIT_ID: ProfitCode
  CURRENCY: FCCurrency
  DUEDATE: DueDate
  REFDATE: RefDate
Fields (name type(len) description [values] ->parent table):
  TransId Int(11) Transaction Key ->OJDT
  Line_ID Int(11) Row Number default=0
  Account nVarChar(15) Account Code ->OACT
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  SYSCred Num(19,6) Credit Amount (SC)
  SYSDeb Num(19,6) Debit Amount (SC)
  FCDebit Num(19,6) Debit Amount (FC)
  FCCredit Num(19,6) Credit Amount (FC)
  FCCurrency nVarChar(3) Foreign Currency
  DueDate Date(8) Value Date
  SourceID Int(11) Source Key
  SourceLine Int(6) Source Row No.
  ShortName nVarChar(15) G/L Acc./BP Code
  IntrnMatch Int(11) Internal Reconciliation No. default=0
  ExtrMatch Int(11) External Reconciliation No. default=0
  ContraAct nVarChar(15) Counter Account
  LineMemo nVarChar(254) Row Details
  Ref3Line nVarChar(100) Reference 3
  TransType nVarChar(20) Original Journal default=-1 [15=Delivery, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 69=Landed Costs, 163=A/P Correction Invoice, 24=Incoming Payment, 25=Deposit, 46=Vendor Payment, 57=Checks for Payment, 76=Postdated Deposit, 182=BoE Transaction, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, 58=Stock Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, 68=Work Instructions, 162=Inventory Valuation, -1=All Transactions, 321=Internal Reconciliation, 140000009=Outgoing Excise Invoice, 10000079=TDS Adjustment, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 140000010=Incoming Excise Invoice, 202=Production Order]
  RefDate Date(8) Posting Date
  Ref2Date Date(8) Posting Date 3
  Ref1 nVarChar(100) Ref. 1
  Ref2 nVarChar(100) Ref. 2
  CreatedBy Int(11) Origin
  BaseRef nVarChar(11) Base Reference
  Project nVarChar(20) Project Code ->OPRJ
  TransCode nVarChar(4) Transaction Code ->OTRC
  ProfitCode nVarChar(8) Distribution Rule ->OOCR
  TaxDate Date(8) Tax Date
  SystemRate Num(19,6) Price (SC)
  MthDate Date(8) Reconciliation Date
  ToMthSum Num(19,6) Reconciliation Total
  UserSign Int(6) User Signature ->OUSR
  BatchNum Int(11) Journal Voucher No. ->OBTD
  FinncPriod Int(11) Posting Period ->OFPR
  RelTransId Int(11) Linked Transaction Key default=-1
  RelLineID Int(11) Linked Row No. default=-1
  RelType VarChar(1) Link Type default=N [N=Without Link, D=WTax Deduction - Correction]
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  BaseSum Num(19,6) Base Amount
  VatRate Num(19,6) Tax %
  Indicator nVarChar(2) Indicator Code ->OIDC
  AdjTran VarChar(1) Adjusting Trans. (Period 13) default=N [Y=Yes, N=No]
  RevSource VarChar(1) Revaluation Source default=N [F=Foreign Currency, S=System, N=No]
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  VatDate Date(8) Tax Date
  PaymentRef nVarChar(27) Payment Reference
  SYSBaseSum Num(19,6) System Base Amount
  MultMatch Int(11) Multiple BP Reconciliation No. default=0
  VatLine VarChar(1) VAT Line default=N [Y=Yes, N=No]
  VatAmount Num(19,6) VAT Amount
  SYSVatSum Num(19,6) System VAT Amount
  Closed VarChar(1) Closed default=N
  GrossValue Num(19,6) Gross Value
  CheckAbs Int(11) Check Abs
  LineType Int(11) LineType default=0
  DebCred VarChar(1) Debit Credit Line Indicator [D=Debit, C=Credit]
  SequenceNr Int(11) Assigned Sequence No. default=0
  StornoAcc nVarChar(15) Storno Account Code ->OACT
  BalDueDeb Num(19,6) Balance Due - Debit
  BalDueCred Num(19,6) Balance Due - Credit
  BalFcDeb Num(19,6) Balance Due FC - Debit
  BalFcCred Num(19,6) Balance Due FC - Credit
  BalScDeb Num(19,6) Balance Due SC - Debit
  BalScCred Num(19,6) Balance Due SC - Credit
  IsNet VarChar(1) Is Net default=Y [Y=Yes, N=No]
  DunWizBlck VarChar(1) Wizard Dunning Block default=N [N=No, Y=Yes]
  DunnLevel Int(11) Dunning Level default=0 ->ODUN
  DunDate Date(8) Last Dunning Date
  TaxType Int(6) Tax Type default=0
  TaxPostAcc VarChar(1) Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  StaCode nVarChar(8) Authority Code ->OSTA
  StaType Int(11) Authority Type ->OSTT
  TaxCode nVarChar(8) Tax Code ->OSTC
  ValidFrom Date(8) Valid From default=19000101
  GrossValFc Num(19,6) Gross Value (FC)
  LvlUpdDate Date(8) Dunning Level Update Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  MIEntry Int(11) MI Entry when include this OB default=0
  MIVEntry Int(11) A/P Monthly Invoice default=0
  ClsInTP Int(11) Tax Payment Wizard default=0
  CenVatCom Int(11) CENVAT Component default=-1
  MatType Int(11) Material Type default=-1
  PstngType Int(11) Posting Type default=0
  ValidFrom2 Date(8) Valid from2 default=19000101
  ValidFrom3 Date(8) Valid from3 default=19000101
  ValidFrom4 Date(8) Valid from4 default=19000101
  ValidFrom5 Date(8) Valid from5 default=19000101
  Location Int(11) Loc. ->OLCT
  WTaxCode nVarChar(4) Withholding Tax Code ->OWHT
  EquVatRate Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Equalization Tax Amount
  SYSEquSum Num(19,6) System Equalization Tax Amount
  TotalVat Num(19,6) Total Tax
  SYSTVat Num(19,6) System Total Tax
  WTLiable VarChar(1) WTax-Liable default=N [Y=Yes, N=No]
  WTLine VarChar(1) WTax Row default=N [Y=Yes, N=No]
  WTApplied Num(19,6) Applied WTax
  WTAppliedS Num(19,6) Applied WTax (SC)
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  LicTradNum nVarChar(32) Federal Tax ID
  InterimTyp Int(11) Interim Account Type default=0
  DprId Int(11) Down Payment Request Key
  MatchRef nVarChar(20) Reconciliation Reference
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  SLEDGERF VarChar(1) Subledger Flag
  InitRef2 nVarChar(100) Initial Reference 2
  InitRef3Ln nVarChar(27) Initial Reference 3
  ExpUUID nVarChar(50) Expense UUID
  ExpOPType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  ExTransId Int(11) Exposed Transaction ID
  DocArr Int(6) Source of Posting
  DocLine Int(11) Source Line Internal ID
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  DocEntry Int(11) Source Document Entry
  DocNum Int(11) Source Document Number
  DocType nVarChar(20) Source Document Type
  DocSubType nVarChar(2) Document Subtype
  RmrkTmpt Int(11) Remark Text Template ->OTTR
  CemCode nVarChar(20) Cost Element Code
  InClassCat Int(11) Income Classification Category
  InClassTyp Int(11) Income Classification Type
  ExClassCat Int(11) Expense Classification Category
  ExClassTyp Int(11) Expense Classification Type
  VATClassCa Int(11) VAT Classification Category
  VATClassTy Int(11) VAT Classification Type
  EVatCate Int(11) VAT Category
  EWtPercCat Int(11) Withheld Percentage Category
  EWtAmount Num(19,6) Withheld Amount
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# AJD2 - Withholding Tax - History
Module: Finance | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, LogInstanc
  SECONDERY: AbsEntry, WTCode, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->AJDT
  WTCode nVarChar(4) WTax Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  ApplAmnt Num(19,6) Applied WTax Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) WTax Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Document Reference default=-1
  BaseLine Int(11) Base Row
  BaseNum Int(11) Base Document Type default=-1 [-1=]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Row
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No. ->OBTD
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# AJDT - Journal Entry - History
Module: Finance | 113 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TransId, LogInstanc
  TRANS_TYPE: TransType, CreatedBy
  REFDATE: RefDate
  STORNO_TRA: StornoToTr
Fields (name type(len) description [values] ->parent table):
  BatchNum Int(11) Journal Voucher No. ->OBTD
  TransId Int(11) Transaction Number
  BtfStatus VarChar(1) Status default=O [O=Open, C=Closed]
  TransType nVarChar(20) Origin default=-1 [16=Returns, 203=A/R Down Payment, 15=Delivery, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt PO, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 281=A/P Tax Invoice, 69=Landed Costs, 140000009=Outgoing Excise Invoice, 140000010=Incoming Excise Invoice, 254000065=Self Invoice, 254000066=Self Credit Memo, 10000079=TDS Adjustment, 24=Incoming Payment, 25=Deposit, 46=Vendor Payment, 57=Checks for Payment, 76=Postdated Deposit, 182=BoE Transaction, -2=Opening Balance, -3=Closing Balance, 321=Internal Reconciliation, 10000046=Data Archive, 30=Journal Entry, 58=Inventory List, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, 68=Work Instructions, 162=Inventory Valuation, 202=Production Order, 1470000049=Fixed Asset Capitalization, 1470000060=Fixed Asset Capitalization Credit Memo, 1470000094=Fixed Asset Retirement, 1470000075=Fixed Asset Manual Depreciation, 1470000090=Fixed Asset Transfer, 1470000085=Fixed Asset Revaluation, -1=All Transactions, 310000001=Inventory Opening Balance, 10000071=Inventory Posting, 254000061=Input Service Distribution Invoice, 254000062=Input Service Distribution Recipient Invoice, 254000064=Input Service Distribution Recipient Credit Memo, -4=Adj. for Manual Ext. Reconciliation]
  BaseRef nVarChar(11) Origin No.
  RefDate Date(8) Posting Date
  Memo nVarChar(254) Remarks
  Ref1 nVarChar(100) Ref. 1
  Ref2 nVarChar(100) Ref. 2
  CreatedBy Int(11) Original
  LocTotal Num(19,6) Total in Local Currency
  FcTotal Num(19,6) Total in Foreign Currency
  SysTotal Num(19,6) Total in System Currency
  TransCode nVarChar(4) Transaction Code ->OTRC
  OrignCurr nVarChar(3) Revaluation Currency ->OCRN
  TransRate Num(19,6) Revaluation Rate
  BtfLine Int(11) Row No. in Voucher
  TransCurr nVarChar(3) Transaction Currency
  Project nVarChar(20) Project Code ->OPRJ
  DueDate Date(8) Due Date
  TaxDate Date(8) Document Date
  PCAddition VarChar(1) PC Addition default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updated By ->OUSR
  RefndRprt VarChar(1) Reported in 874 default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type ->ADP1
  Indicator nVarChar(2) Indicator Code ->OIDC
  AdjTran VarChar(1) Adjusting Transaction default=N [Y=Yes, N=No]
  RevSource VarChar(1) Revaluation Source default=N [F=Foreign Currency, S=System, N=No]
  StornoDate Date(8) Reversal Date
  StornoToTr Int(11) Reversed Transaction
  AutoStorno VarChar(1) Use Auto-Reverse default=N [Y=Yes, N=No]
  Corisptivi VarChar(1) Transaction Values default=N [Y=Yes, N=No]
  VatDate Date(8) VAT Date
  StampTax VarChar(1) Stamp Tax default=N [Y=Yes, N=No]
  Series Int(11) Series default=0
  Number Int(11) Number
  AutoVAT VarChar(1) Automatic Tax default=N [Y=Yes, N=No]
  DocSeries Int(11) Document Series
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  CreateTime Int(6) Generation Time
  BlockDunn VarChar(1) Block Dunning Letter default=N [N=No, Y=Yes]
  ReportEU VarChar(1) Include in EU Report default=N [Y=Yes, N=No]
  Report347 VarChar(1) Include in 347 Report default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  DocType nVarChar(60) Document Type ->OJET
  AttNum Int(11) Number of Attachments default=0
  GenRegNo VarChar(1) Generate Reg. No. or Not default=N [Y=Yes, N=No]
  RG23APart2 Int(11) RG23A Part2 No
  RG23CPart2 Int(11) RG23C Part2 No
  MatType Int(11) Material Type
  Creator nVarChar(155) Creator Name
  Approver nVarChar(155) Approver Name
  Location Int(11) Loc. ->OLCT
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  AutoWT VarChar(1) Automatic WTax default=N [Y=Yes, N=No]
  WTSum Num(19,6) WTax Amount
  WTSumSC Num(19,6) WTax Amount (SC)
  WTSumFC Num(19,6) WTax Amount (FC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedS Num(19,6) Applied WTax (SC)
  WTAppliedF Num(19,6) Applied WTax (FC)
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseVtAt Num(19,6) WTax Base VAT Amount
  BaseVtAtSC Num(19,6) WTax Base VAT Amount (SC)
  BaseVtAtFC Num(19,6) WTax Base VAT Amount (FC)
  VersionNum nVarChar(13) Version Number
  BaseTrans Int(11) Base Transaction Number
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Country/Region of Residence, 5=Certificate of Fiscal Residence, 6=Other Document]
  OperatCode VarChar(1) Operation Code [A=Summary Invoices Entry, B=Summary Receipts Entry, C=Invoice with Several VAT Rates, D=Correction Invoice, E=Due VAT Pending Invoice Issuance, F=Expenses Incurred by Travel Agent for Customers, G=Special Regulation for VAT Group, H=Special Regulation for Gold Investment, I=Reverse Charge Procedure, J=Unsummarized Receipts, K=Identification of Error Transactions, X=Transactions with Entrepreneurs Issuing Receipts for Agricultural Compensation, N=Service Invoicing by Travel Agencies on Behalf of Third Parties, R=Business Office Rental, S=Subsidies, T=Incoming Payments for Industrial and Intellectual Property Rights, U=Insurance Transactions, V=Purchases from Travel Agencies, W=Transactions Subject to Production, Service, and Import Taxes in Ceuta and Melilla]
  Ref3 nVarChar(100) Reference 3
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  SupplCode nVarChar(254) Supplementary Code
  SPSrcType Int(11) Service Posting Source Type
  SPSrcID Int(11) Service Posting Source ID
  SPSrcDLN Int(11) Service Post. Source Delivery
  DeferedTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  AgrNo Int(11) Blanket Agreement Number ->OOAT
  SeqNum Int(11) Sequence Number
  ECDPosTyp VarChar(1) ECD Posting Type default=N [N=Normal, E=Statement]
  RptPeriod nVarChar(5) Reporting Period
  RptMonth Date(8) Reporting Month
  ExTransId Int(11) Exposed Transaction ID
  PrlLinked VarChar(1) Is JE linked by MX Payroll default=N [Y=Yes, N=No]
  PTICode nVarChar(5) POI Code
  Letter VarChar(1) Letter
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  IsCoEntry VarChar(1) Cost Center Transfer form default=N [Y=Yes, N=No]
  SAPPassprt Text(16) Extended SAP Passport
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachment
  EBookable VarChar(1) E-Books Enabled default=N [N=No, Y=Yes]
  DataVers Int(11) Data Version default=1

# AMDR - Manual Distribution Rule
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode, logInstanc
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code
  OcrName nVarChar(30) Factor Description
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(6) In Which Dimension default=1 ->ODIM
  AbsEntry Int(11) Numerator
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  IsFixedAmt VarChar(1) Distribute by Fixed Amount default=N [Y=Yes, N=No]

# AMDR1 - Manual Distribution Rule - Rows
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode, PrcCode, ValidFrom, logInstanc
  PROF_ID: PrcCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code ->OMDR
  PrcCode nVarChar(8) Cost Center Code ->OPRC
  PrcAmount Num(19,6) Total in Cost Center
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Effective from default=19000101 [19000101=]
  ValidTo Date(8) Effective to
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update

# APRJ - Project Codes
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrjCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  PrjCode nVarChar(20) Project Code
  PrjName nVarChar(100) Project Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# ARTS - CPI and FC Rates for Reports - History
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RateDate, Currency, ReportType, LogInstanc
  DATE: RateDate, LogInstanc
Fields (name type(len) description [values] ->parent table):
  RateDate Date(8) Exchange Rate Date
  Currency nVarChar(3) Currency Code
  Rate Num(19,6) Currency Rate
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ReportType VarChar(1) Report Rate Type default=S [S=Standard Report Rate, I=Intrastat Exchange Rate]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(11) Updating User ->OUSR

# ARTT - CPI and FC Rates - History
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RateDate, Currency, LogInstanc
  DATE: RateDate, LogInstanc
Fields (name type(len) description [values] ->parent table):
  RateDate Date(8) Exchange Rate Date
  Currency nVarChar(3) Currency Code
  Rate Num(19,6) Currency Rate
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(11) Updating User ->OUSR

# AVEB - VAT Exemptions for Business Partners - History
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  BP_CODE U: CardCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  VersionNum nVarChar(13) Version Number
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UpdateTS Int(11) Update Full Time
  Comments nVarChar(254) Remarks

# AVT1 - Tax Definition
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, EffecDate, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Group Code
  EffecDate Date(8) Effective from
  Rate Num(19,6) Rate
  EquVatPr Num(19,6) Equalization Tax %
  MinAmount Num(19,6) Minimum Stamp Tax Amount
  FixedAmout Num(19,6) Fixed Stamp Tax Amount
  TaxType VarChar(1) Tax Type (VAT or Stamp) default=V [V=VAT, S=Stamp]
  LogInstanc Int(11) Log Instance default=0
  DatevCode Int(6) DATEV Code

# AVTG - Tax Definition
Module: Finance | 67 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
  GROUP_NAME: Name, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(50) Name
  Rate Num(19,6) Rate %
  EffecDate Date(8) Effective from
  Category VarChar(1) Category default=O [O=Output Tax, I=Input Tax]
  Account nVarChar(15) Tax Account ->OACT
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  IsEC VarChar(1) EU default=N [Y=Yes, N=No]
  Indicator VarChar(1) Triangular Deal ->OIND
  AcqstnRvrs VarChar(1) Acquisition/Reverse default=N [Y=Yes, N=No]
  NonDedct Num(19,6) Non-Deductible %
  AcqsTax nVarChar(15) Acquisition Tax Account ->OACT
  GoddsShip VarChar(1) Goods Shipment ->OGSP
  NonDedAcc nVarChar(15) Non-Deductible Acct ->OACT
  DeferrAcc nVarChar(15) Deferred Tax Account ->OACT
  EquVatPr Num(19,6) Equalization Tax %
  ReportCode nVarChar(100) Group Description
  FixdAssts VarChar(1) Fixed Assets Flag default=N [Y=Yes, N=No]
  CalcMethod VarChar(1) Calculation Method default=R [R=Rate, F=Fixed]
  TaxType VarChar(1) Tax Type (VAT or Stamp) default=V [V=VAT, S=Stamp]
  FixedAmnt Num(19,6) Fixed Amount (LC)
  ExtCode nVarChar(10) External Code
  Correction VarChar(1) Correction default=N [Y=Yes, N=No]
  VatCrctn nVarChar(8) VAT Correction ->OVTG
  RetVatCode nVarChar(8) Returning VAT Code
  RepType Int(11) Report Type ->OKRT
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  TaxCtgr nVarChar(6) Tax Type (Annual List) default=E [E=Excluded, T=Taxable, X=Exempt, N=Not Taxable, N31=N3.1 - Not Taxable - exports, N32=N3.2 - Not Taxable - intra-community sales, N33=N3.3 - Not Taxable - sales to San Marino, N34=N3.4 - Not Taxable - operations similar to export sales, N35=N3.5 - Not Taxable - due to tax exemption letter, N36=N3.6 - Not Taxable - other transactions, G=Gross Profit, R=Reverse Charge, R61=N6.1 - Reverse Charge - disposal of scrap and other recycled materials, R62=N6.2 - Accounting Reversal - sale of gold and pure silver, R63=N6.3 - Reverse Charge - subcontracting in the construction sector, R64=N6.4 - Reverse Charge - sales of buildings, R65=N6.5 - Reverse Charge - sales of cell phones, R66=N6.6 - Reverse Charge - sales of electronic products, R67=N6.7 - Reverse Charge - services of the construction and related sectors, R68=N6.8 - Reverse Charge - energy sector operations, R69=N6.9 - Reverse Charge - other cases, U=Tourism, A=Taxable - Article 162, B=Taxable - Article 173 point 5, C=Taxable - Construction, D=Taxable - Expected Confirmation, F=Taxable - Gross, I=Taxable - Import, Y=Taxable - Import from EAEU, L=Taxable - Late Export, O=Taxable - Not Confirmed, S=Taxable - Real Estate, W=Taxable - Sale of Company, H=Excluded Art. 15, J=Not Subject, J21=N2.1 - Not Subject - to VAT under articles from 7 to 7-septies of DPR 633/72, J22=N2.2 - Not Subject - other cases, K=Paid in other EU country, M=Taxable - Article 151 point 1, P=Taxable - Article 170 point 3, V=Taxable - Fixed Assets, Q=Taxable - Tax Free]
  EquAccount nVarChar(15) Equalization Tax Account ->OACT
  UserSign2 Int(6) Updating User ->OUSR
  IsIGIC VarChar(1) IGIC default=N [Y=Yes, N=No]
  ServSupply VarChar(1) Service Supply ->OSSP
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  TaxCtgrBL VarChar(1) Tax Type (Black List) default=E [E=Excluded, T=Taxable, X=Exempt, N=Not Taxable, S=Non-Subject]
  R349Code Int(11) Report 349 Code default=0 [0=, 1=E, 2=A, 3=T, 4=S, 5=I, 6=M, 7=H]
  VatRevAcc nVarChar(15) VAT in Revenue Account ->OACT
  CashDisAcc nVarChar(15) Cash Discount Account ->OACT
  DpmTaxOAcc nVarChar(15) Down Paymnt Tax Offset Account ->OACT
  VatDedAcc nVarChar(15) VAT Deductible Account ->OACT
  CstmExpAcc nVarChar(15) Customs VAT Expense Account
  CstmAlcAcc nVarChar(15) Customs VAT Allocation Account
  TaxRegion nVarChar(5) Tax Country Region default=PT [PT=Continental Portugal, PT-AC=Azores Islands, PT-MA=Madeira Islands]
  ExemReason nVarChar(3) Tax Exemption Reason [M01=Article 16th No. 6 of CIVA, M02=Article 6th Law 198/90 June 19th, M03=Cash Liabilities, M04=Exempt Article 13th of CIVA, M05=Exempt Article 14th of CIVA, M06=Exempt Article 15th of CIVA, M07=Exempt Article 9th of CIVA, M08=VAT - Self-Liquidation, M09=VAT - Non-Deductible, M10=VAT - Exempted Company, M11=VAT - Exempted (Tobacco), M12=VAT - Exempted (Travel Agencies), M13=VAT - Exempt (Second Hand Goods), M14=VAT - Exempted (Objects of Art), M15=VAT - Exempted (Collectibles and Antiques), M16=VAT - Exempted (Article 14th of RITI), M99=Not Subject to VAT]
  Agent VarChar(1) Agent default=N [Y=Yes, N=No]
  OpCode nVarChar(7) Tax Operation Code
  Export VarChar(1) Export default=N [Y=Yes, N=No]
  Section nVarChar(3) VAT Section
  SplitPaymt VarChar(1) Split Payment default=N [Y=Yes, N=No]
  SplitPayAc nVarChar(15) Split Payment Account
  TaxAgent VarChar(1) Tax Agent (Section 3) default=N [Y=Yes, N=No]
  SectionLim nVarChar(3) VAT Section (under limit)
  VatSubjCod nVarChar(10) VAT Subject Code
  VatType Int(11) Type of VAT default=-1
  VatCategor Int(11) VAT Category default=-1
  Parag44 VarChar(1) Paragraph 44 default=N [Y=Yes, N=No]
  ProrataDed VarChar(1) Pro-rata deductible default=N [Y=Yes, N=No]
  ExcFrmTaxS VarChar(1) Exclude from Tax Summary Report Total A/R or A/P Net Amounts default=N [Y=Yes, N=No]
  CstmActing VarChar(1) Customer Accounting default=N [Y=Yes, N=No]
  CstmActOut nVarChar(8) Customer Accounting Corresponding Tax Code
  StdTaxCode nVarChar(35) Standard Tax Code
  AcqRevTax nVarChar(8) Acquisition/Reverse Corresponding Tax Code
  ExReasonHU nVarChar(30) Tax Exemption Reason
  ExRemarkHU nVarChar(50) Tax Exemption Remark
  EBVatCateg Int(11) VAT Category

# AWD1 - Withholding Tax Dates
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineNum Int(11) Row Number
  DateFrom Date(8) Effective From
  Rate Num(19,6) Rate
  LogInstanc Int(11) Log Instance default=0

# AWD2 - Value Ranges
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SeqNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  EfctFrom Date(8) Effective From
  ValueFrom Num(19,6) Value From
  Rate Num(19,6) Rate
  WTCur nVarChar(3) Currency
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number

# AWH1 - Tax Definition
Module: Finance | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  WTCode nVarChar(4) WTax Code ->OWHT
  EffecDate Date(8) Effective from
  Rate Num(19,6) Rate
  LogInstanc Int(11) Log Instance default=0
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  PmntTerms Int(6) Payment Terms ->OCTG
  LineNum Int(11) Row Number
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UomEntry Int(11) UoM Entry ->OUOM
  UoMCode nVarChar(20) UoM Code
  FixedAmnt Num(19,6) Fixed Amount
  Currency nVarChar(3) Fixed Amount Currency ->OCRN
  ItrNCRate Num(19,6) TDS ITR Noncompliance Rate
  PanNCRate Num(19,6) TDS PAN Noncompliance Rate

# AWH2 - WTax Definition - Rows2
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum, SeqNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  Code nVarChar(4) Tax Code ->OWHT
  EffectDate Date(8) Date Effective
  Rate Num(19,6) Tax Rate
  MinAmount Num(19,6) Min. Amount
  MaxAmount Num(19,6) Max. Amount
  WTCUR nVarChar(3) Progressive Tax Currency ->OCRN
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number

# AWH3 - Value Range
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LineNum, SeqNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  WTCode nVarChar(4) WTax Code ->OWHT
  EfctFrom Date(8) Effective from
  ValueFrom Num(19,6) Value From
  Deduct Num(19,6) WTax to Be Deductible
  Rate Num(19,6) Rate
  WTCur nVarChar(3) Currency
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number

# AWHT - Withholding Tax
Module: Finance | 63 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  WTCode nVarChar(4) WTax Code
  WTName nVarChar(50) WTax Name
  Rate Num(19,6) Rate
  EffecDate Date(8) Effective From
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  BaseType VarChar(1) Base Type default=N [G=Gross, N=Net, V=VAT, U=UoM]
  PrctBsAmnt Num(19,6) % Base Amount
  OffclCode nVarChar(15) Official Code
  Account nVarChar(15) Account ->OACT
  MinTaxAmt Num(19,6) Minimum Taxable Amount
  IsPrgrss VarChar(1) Progressive Tax default=N [Y=Progressive Tax, N=Not Progressive Tax]
  Type VarChar(1) Withholding Type default=V [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type default=C [T=Truncated AU, C=Commercial Values]
  WTTypeId Int(11) Type ->OWTT
  WTCurrency nVarChar(3) Currency ->OCRN
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  Section Int(11) Section ->OSEC
  Threshold Num(19,6) Cumulative Threshold
  Surcharge Num(19,6) Surcharge
  Concess VarChar(1) Concessional default=N [Y=Yes, N=No]
  Assessee Int(11) Assessee ->ONOA
  ApTdsAcc nVarChar(15) A/P TDS Account ->OACT
  ApSurAcc nVarChar(15) A/P Surcharge Account ->OACT
  ApCessAcc nVarChar(15) A/P Cess Account ->OACT
  ApHscAcc nVarChar(15) A/P HSC Account ->OACT
  ArTdsAcc nVarChar(15) A/R TDS Account ->OACT
  ArSurAcc nVarChar(15) A/R Surcharge Account ->OACT
  ArCessAcc nVarChar(15) A/R Cess Account ->OACT
  ArHscAcc nVarChar(15) A/R HSC Account ->OACT
  Location Int(11) Location ->OLCT
  ReturnType VarChar(1) Return Type [A=26, B=27]
  UserSign2 Int(6) Updating User ->OUSR
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  InCSTCode Int(11) CST Code Incoming default=-1 ->OTSC
  OutCSTCode Int(11) CST Code Outgoing default=-1 ->OTSC
  CalBaseN nVarChar(2) Nature of Calculation Base ->OBSI
  PymntRsnCd nVarChar(3) Payment Reason Code ->OSWA
  DIOTRpt VarChar(1) DIOT Report default=N [Y=Yes, N=No]
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS]
  ApIgstAcc nVarChar(15) A/P IGST Account ->OACT
  ApCgstAcc nVarChar(15) A/P CGST Account ->OACT
  ApSgstAcc nVarChar(15) A/P SGST Account ->OACT
  ArIgstAcc nVarChar(15) A/R IGST Account ->OACT
  ArCgstAcc nVarChar(15) A/R CGST Account ->OACT
  ArSgstAcc nVarChar(15) A/R SGST Account ->OACT
  ApUtgstAcc nVarChar(15) A/P UTGST Account ->OACT
  ApCsgstAcc nVarChar(15) A/P Cess GST Account ->OACT
  ArUtgstAcc nVarChar(15) A/R UTGST Account ->OACT
  ArCsgstAcc nVarChar(15) A/R Cess GST Account ->OACT
  TransThres Num(19,6) Transaction Threshold default=0
  EBWTaxCate Int(11) Withholding Tax Category ->OWHC
  ArTcsInAcc nVarChar(15) A/R TCS Interim Account ->OACT
  ArSurInAcc nVarChar(15) A/R Surcharge Interim Account ->OACT
  ArCesInAcc nVarChar(15) A/R Cess Interim Account ->OACT
  ArHscInAcc nVarChar(15) A/R HSC Interim Account ->OACT
  ApTcsInAcc nVarChar(15) A/P TCS Interim Account ->OACT
  ApSurInAcc nVarChar(15) A/P Surcharge Interim Account ->OACT
  ApCesInAcc nVarChar(15) A/P Cess Interim Account ->OACT
  ApHscInAcc nVarChar(15) A/P HSC Interim Account ->OACT
  LnWTInAcc nVarChar(15) Interim Account for Tax ->OACT
  NoDedThrsh VarChar(1) Apply Tax Exemption After Threshold default=N [Y=Yes, N=No]

# AWTD - Withholding Tax Definition
Module: Finance | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WTCode nVarChar(4) WTax Code
  WTName nVarChar(50) WTax Name
  Rate Num(19,6) Rate
  EffecDate Date(8) Effective From
  Inactive VarChar(1) Inactive default=N [Y=, N=]
  OffclCode nVarChar(15) Official Code
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  BaseType VarChar(1) Base Type default=N [N=Net, V=VAT, G=Gross, H=Gross - VAT]
  WTTypeId Int(11) Type ->OWTT
  BaseMin Num(19,6) Min. Amount
  PrctBsAmnt Num(19,6) % Base Amount
  FmlId Int(11) Formula ID ->OFML
  Account nVarChar(15) Account ->OACT
  SlScProgr VarChar(1) Sliding Scale Progressive Tax default=N [Y=, N=]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CalcWHTCrM VarChar(1) Calculate Withholding Tax in Automatic Credit Memo default=Y [Y=Yes, N=No]

# AWTT - Withholding Tax Type
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTTypeId, LogInstanc
  WT_TYPE U: WTType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  WTTypeId Int(11) Internal Number
  WTType nVarChar(10) Type
  WTThresh Num(19,6) Min. WTax Amount
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# BGT1 - Budget - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BudgId, Line_ID
Fields (name type(len) description [values] ->parent table):
  BudgId Int(11) Budget Key ->OBGT
  Line_ID Int(11) Row Number default=0
  DebLTotal Num(19,6) Monthly Budget - Deb.
  CredLTotal Num(19,6) Monthly Budget - Cr.
  DebSTotal Num(19,6) Monthly Budget - SC Deb.
  CredSTotal Num(19,6) Monthly Budget - SC Cr.
  DebRLTotal Num(19,6) Monthly Bal. - Deb.
  CrdRLTotal Num(19,6) Monthly Bal. - Cr.
  DebRSTotal Num(19,6) Monthly Bal. - SC Deb.
  CrdRSTotal Num(19,6) Monthly Bal. - SC Cred.
  FtrIDRLSum Num(19,6) Fut. Monthly Incomes SC Cr.
  FtrIDRSSum Num(19,6) Fut. Monthly Incomes SC Deb.
  FtrICRLSum Num(19,6) Fut. Incomes - Cr.
  FtrICRSSum Num(19,6) Fut. Incomes - Sys. Cr.
  FtrODRLSum Num(19,6) Fut. Expen - Local Deb.
  FtrODRSSum Num(19,6) Fut.Expen - SC Deb.
  FtrOCRLSum Num(19,6) Fut.Expen - Local Cr.
  FtrOCRSSum Num(19,6) Fut.Expen - Sys. Cr.
  MonthPrcnt Num(19,6) % of annual budget amount
  LineMemo nVarChar(50) Row Details
  Instance Int(11) Instance default=1 ->OBGS
  AcctCode nVarChar(15) Account Code
  UserSign Int(6) User Signature ->OUSR

# BGT2 - Budget - Cost Accounting
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BudgId, OcrCode, DimCode
Fields (name type(len) description [values] ->parent table):
  BudgId Int(11) Budget Key ->OBGT
  OcrCode nVarChar(8) Factor Code ->OOCR
  DimCode Int(6) In Which Dimension ->ODIM
  Instance Int(11) Instance default=1 ->OBGS
  DebLTotal Num(19,6) Tot. Annu. Budgt Debit (LC)
  CredLTotal Num(19,6) Tot. Annu. Budgt Credit (LC)
  DebSTotal Num(19,6) Tot. Annu. Budgt Debit (SC)
  CredSTotal Num(19,6) Tot. Annu. Budgt Credit (SC)
  UserSign Int(6) User Signature ->OUSR

# BGT3 - Budget - Cost Accounting Rows
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BudgId, OcrCode, DimCode, Line_ID
Fields (name type(len) description [values] ->parent table):
  BudgId Int(11) Budget Key ->OBGT
  OcrCode nVarChar(8) Factor Code ->OOCR
  DimCode Int(6) In Which Dimension ->ODIM
  Instance Int(11) Instance default=1 ->OBGS
  Line_ID Int(11) Row Number
  DebLTotal Num(19,6) Monthly Budget - Deb.
  CredLTotal Num(19,6) Monthly Budget - Cr.
  DebSTotal Num(19,6) Monthly Budget - SC Deb.
  CredSTotal Num(19,6) Monthly Budget - SC Cr.
  UserSign Int(6) User Signature ->OUSR

# BOX1 - Box Definition - Rows
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, SeqNum, BosCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Group Code
  BoxMember nVarChar(30) Box Code ->OBOX
  VATMember nVarChar(8) VAT Group ->OVTG
  SeqNum Int(11) Sequence Number
  FormulSign VarChar(1) Formula Sign default=P [P=+, M=-]
  ReportType VarChar(1) Report Type default=B [B=Box Declaration, S=BAS Reporting]
  EffecDate Date(8) Effective From
  TaxType VarChar(1) Acquisition / Reverse Tax Type default=B [I=Input Tax, O=Output Tax, B=Input Tax and Output Tax]
  BosCode Int(11) Box Set Code ->OBOS

# BOX2 - Box Definition - Accounts
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, Account, BosCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Group Code
  ReportType VarChar(1) Report Type default=B [B=, S=]
  Account nVarChar(15) Account ->OACT
  SeqNum Int(11) Sequence Number
  EffecDate Date(8) Effective From
  BosCode Int(11) Box Set Code ->OBOS

# BOX3 - Box Definition - Choice
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, Value, BosCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Group Code
  ReportType VarChar(1) Report Type default=B [B=, S=]
  Value nVarChar(8) Value
  Descr nVarChar(250) Description
  EffecDate Date(8) Effective From
  BosCode Int(11) Box Set Code ->OBOS
  IsDefault VarChar(1) Is Default default=N [Y=Yes, N=No]

# BOX4 - Box Definition - Contra Accounts of Accounts
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, Account, BosCode, ContraAct
Fields (name type(len) description [values] ->parent table):
  ReportType VarChar(1) Report Type default=B [B=, S=]
  EffecDate Date(8) Effective From
  BoxCode nVarChar(30) Group Code
  Account nVarChar(15) Account
  ContraAct nVarChar(15) Offset Account
  SeqNum Int(11) Sequence Number
  BosCode Int(11) Box Set Code ->OBOS

# BTF1 - Journal Voucher - Rows
Module: Finance | 145 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BatchNum, TransId, Line_ID
  SHORT_NAME: ShortName
  ACCOUNT: Account
  BATCH_IDX: BatchNum
  CURRENCY: FCCurrency
  INTRNMATCH: ShortName, Account, IntrnMatch
Fields (name type(len) description [values] ->parent table):
  TransId Int(11) Transaction Key ->OJDT
  Line_ID Int(11) Row Number default=0
  Account nVarChar(15) Account Code ->OACT
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  SYSCred Num(19,6) System Credit Amount
  SYSDeb Num(19,6) System Debit Amount
  FCDebit Num(19,6) FC Debit Amount
  FCCredit Num(19,6) FC Credit Amount
  FCCurrency nVarChar(3) Foreign Currency
  DueDate Date(8) Due Date
  SourceID Int(11) Source Key
  SourceLine Int(6) Source Row Number
  ShortName nVarChar(15) Card/Account Code
  IntrnMatch Int(11) Internal Reconciliation No. default=0
  ExtrMatch Int(11) External Reconciliation No. default=0
  ContraAct nVarChar(15) Offset Account
  LineMemo nVarChar(254) Row Details
  Ref3Line nVarChar(100) Reference 3
  TransType nVarChar(20) Original Journal default=-1 [-1=]
  RefDate Date(8) Posting Date
  Ref2Date Date(8) Posting Date 2
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  CreatedBy Int(11) Origin
  BaseRef nVarChar(11) Base Reference
  Project nVarChar(20) Project Code ->OPRJ
  TransCode nVarChar(4) Transaction Code ->OTRC
  ProfitCode nVarChar(8) Distribution Rule ->OOCR
  TaxDate Date(8) Document Date
  SystemRate Num(19,6) System Price
  MthDate Date(8) Reconciliation Date
  ToMthSum Num(19,6) Reconciliation Total
  UserSign Int(6) User Signature ->OUSR
  BatchNum Int(11) Journal Voucher No. ->OBTD
  FinncPriod Int(11) Posting Period ->OFPR
  RelTransId Int(11) Linked Transaction Key default=-1
  RelLineID Int(11) Linked Row No. default=-1
  RelType VarChar(1) Link Type default=N [N=Without Link, D=WTax Deduction - Correction]
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  BaseSum Num(19,6) Base Amount
  VatRate Num(19,6) Tax %
  Indicator nVarChar(2) Indicator Code ->OIDC
  AdjTran VarChar(1) Adjusting Trans. (Period 13) default=N [Y=Yes, N=No]
  RevSource VarChar(1) Revaluation Source default=N [F=FC, S=System, N=No]
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  VatDate Date(8) Document Date
  PaymentRef nVarChar(27) Payment Reference
  SYSBaseSum Num(19,6) System Base Amount
  MultMatch Int(11) Multiple BP Reconciliation No. default=0
  VatLine VarChar(1) VAT Row default=N [Y=Yes, N=No]
  VatAmount Num(19,6) VAT Amount
  SYSVatSum Num(19,6) System VAT Amount
  Closed VarChar(1) Closed default=N
  GrossValue Num(19,6) Gross Value
  CheckAbs Int(11) Internal Check No.
  LineType Int(11) LineType default=0
  DebCred VarChar(1) Debit Credit Line Indicator [D=Debit, C=Credit]
  SequenceNr Int(11) Assigned Sequence No. default=0
  StornoAcc nVarChar(15) Storno Account Code ->OACT
  BalDueDeb Num(19,6) Balance Due - Debit
  BalDueCred Num(19,6) Balance Due - Credit
  BalFcDeb Num(19,6) Balance Due FC - Debit
  BalFcCred Num(19,6) Balance Due FC - Credit
  BalScDeb Num(19,6) Balance Due SC - Debit
  BalScCred Num(19,6) Balance Due SC - Credit
  IsNet VarChar(1) Is Net default=Y [Y=Yes, N=No]
  DunWizBlck VarChar(1) Wizard Dunning Block default=N [N=No, Y=Yes]
  DunnLevel Int(11) Dunning Level default=0 ->ODUN
  DunDate Date(8) Last Dunning Date
  TaxType Int(6) Tax Type default=0
  TaxPostAcc VarChar(1) Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  StaCode nVarChar(8) Authority Code ->OSTA
  StaType Int(11) Authority Type ->OSTT
  TaxCode nVarChar(8) Tax Code ->OSTC
  ValidFrom Date(8) Valid From default=19000101
  GrossValFc Num(19,6) Gross Value (FC)
  LvlUpdDate Date(8) Dunning Level Update Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  MIEntry Int(11) MI Entry when include this OB default=0
  MIVEntry Int(11) A/P Monthly Invoice default=0
  ClsInTP Int(11) Tax Payment Wizard default=0
  CenVatCom Int(11) CENVAT Component default=-1
  MatType Int(11) Material Type default=-1
  PstngType Int(11) Posting Type default=0
  ValidFrom2 Date(8) Valid from2 default=19000101
  ValidFrom3 Date(8) Valid from3 default=19000101
  ValidFrom4 Date(8) Valid from4 default=19000101
  ValidFrom5 Date(8) Valid from5 default=19000101
  Location Int(11) Loc. ->OLCT
  WTaxCode nVarChar(4) Withholding Tax Code ->OWHT
  EquVatRate Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Equalization Tax Amount
  SYSEquSum Num(19,6) System Equalization Tax Amount
  TotalVat Num(19,6) Total Tax
  SYSTVat Num(19,6) System Total Tax
  WTLiable VarChar(1) WTax-Liable default=N [Y=Yes, N=No]
  WTLine VarChar(1) WTax Row default=N [Y=Yes, N=No]
  WTApplied Num(19,6) Applied WTax
  WTAppliedS Num(19,6) Applied WTax (SC)
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  LicTradNum nVarChar(32) Federal Tax ID
  InterimTyp Int(11) Interim Account Type default=0
  DprId Int(11) Down Payment Request Key
  MatchRef nVarChar(20) Reconciliation Reference
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  SLEDGERF VarChar(1) Subledger Flag
  InitRef2 nVarChar(100) Initial Reference 2
  InitRef3Ln nVarChar(27) Initial Reference 3
  ExpUUID nVarChar(50) Expense UUID
  ExpOPType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  ExTransId Int(11) Exposed Transaction ID
  DocArr Int(6) Source of Posting
  DocLine Int(11) Source Line Internal ID
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  DocEntry Int(11) Source Document Entry
  DocNum Int(11) Source Document Number
  DocType nVarChar(20) Source Document Type
  DocSubType nVarChar(2) Document Subtype
  RmrkTmpt Int(11) Remark Text Template ->OTTR
  CemCode nVarChar(20) Cost Element Code
  InClassCat Int(11) Income Classification Category
  InClassTyp Int(11) Income Classification Type
  ExClassCat Int(11) Expense Classification Category
  ExClassTyp Int(11) Expense Classification Type
  VATClassCa Int(11) VAT Classification Category
  VATClassTy Int(11) VAT Classification Type
  EVatCate Int(11) VAT Category
  EWtPercCat Int(11) Withheld Percentage Category
  EWtAmount Num(19,6) Withheld Amount
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# BTF2 - Journal Voucher Withholding Tax - History
Module: Finance | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BatchNum, AbsEntry, LineNum
  SECONDERY: AbsEntry, WTCode, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OBTF
  WTCode nVarChar(4) WTax Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  ApplAmnt Num(19,6) Applied WTax Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Tax Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Document Reference default=-1
  BaseLine Int(11) Base Row
  BaseNum Int(11) Base Document Type [-1=]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Row
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No. ->OBTD
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# CASE - Internal Recon. Upgrade 2007A
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Intl ID for Inconsistent Amt
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Creation Time
  UserSign Int(6) User Signature ->OUSR
  Message VarChar(1) Show Message? default=N [Y=, N=, S=]

# CASE1 - Internal Recon. Upgrade 2007A
Module: Finance | 36 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Header Internal ID ->CASE
  LineId Int(11) Inconsistent Amt Number default=0
  ShortName nVarChar(15) BP Code
  Account nVarChar(15) Account Code ->OACT
  OrigAbsEnt Int(11) Original Doc. Internal ID
  OrigObjTyp Int(11) Original Doc. Type default=0 [0=All, 13=A/R Invoice, 14=A/R Credit Memo, 18=A/P Invoice, 19=A/P Credit Memo, 24=Incoming Payment, 30=Journal Entry, 46=Outgoing Payment, 163=A/P Correction Invoice, 165=A/R Correction Invoice, 203=A/R Down Payment, 204=A/P Down Payment]
  OrigDocNum Int(11) Original Document Number
  OrigInsNum Int(11) Original Installment Number
  OrigTrnsId Int(11) Original JE Trans. No. ->OJDT
  OrigTrnsLn Int(11) Original JE Row No.
  LnkRecnAbs Int(11) Linked Recon. Doc. Internal ID
  LnkRecnObj Int(11) Destination Object Type
  LnkRecnNum Int(11) Destination Document Number
  LnkRecnIns Int(11) Destination Installment Number
  LnkRecnTrn Int(11) Linked and Recon. JE Trans No. ->OJDT
  LnkRecnLn Int(11) Linked and Recon. JE Row No.
  InconsType nVarChar(2) Type of Inconsistency [1=Invoice Linked to Reconciled Payment, 2=Credit Memo Linked to Reconciled Payment, 3=Canceled Reconciliation, 4=Partial Exchange Rate Difference Recognition, 5=Payment Linked to Reconciled Transaction, 6=Journal Entry Linked to Reconciled Payment, 7=Unbalanced Reconciliation, 8=Invoice/Credit Linked to Credit/Invoice, 9=Balancing Upgrade Journal Transaction, 10=Canceled Payment or Journal Entry, 11=Cancellation of Payment/JE within Payment, 12=Unreconciled Balance Rows in Multiple BPs Reconciliation, 13=Missing Exchange Rate Difference behind Multiple BPs Reconciliation, 14=Double Application of Payments of Down Payment Request, 15=Exchange Difference Recognition of Payments of DPM Requests, 16=Reconciliation of Payments Associated with DPM Request, 17=Unbalanced Multiple BP Reconciliation, 18=Amount Differences, 19=Double application of invoice after linking of down payment, 20=Canceled payment of down payment request, 21=Credit Memo based on a Year Transfered invoice, 22=Payment of a year transfer document, 23=Processing of Payment Linked to Transactions, 24=Consolidating Business Partner, 25=Multiple Control Accounts, 26=Different Control Accounts in a Canceled Payment, 0=None]
  ReconNum Int(11) Reconciliation Number
  NewRcnNum Int(11) New Reconciliation No. ->OITR
  CredDeb VarChar(1) Credit or Debit
  Amount Num(19,6) Inconsistent Amount
  AmountFC Num(19,6) Inconsistent Amount (FC)
  AmountSC Num(19,6) Inconsistent Amount (SC)
  TransId Int(11) Balancing Trans. Internal ID ->OJDT
  TransLine Int(11) Balancing Transaction Row No.
  X Num(19,6) x
  Y Num(19,6) Y
  Z Num(19,6) Z
  LnkObjAbsE Int(11) Linked Doc. Internal ID
  LinkObjTyp Int(11) Linked Document Type
  LinkDocNum Int(11) Linked Document Number
  LinkInsNum Int(11) Linked Doc. Installment Number
  LinkTrnsId Int(11) Linked Doc. JE Trans. No. ->OJDT
  LinkTrnsLn Int(11) Linked Doc. JE Row No.
  TrnsTtlAmt Num(19,6) Balancing Trans. Total Amount
  TrnsTtlFc Num(19,6) Balancing Trans. Total Amt FC

# CCAL - Chinese Chart of Account Level Definition
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: lvlIAccLe
Fields (name type(len) description [values] ->parent table):
  lvlIAccLe Int(6) Length First Level Accounts default=4 [4=]
  accLvlSet VarChar(1) Account Level Set default=N [N=, Y=]
  balIndSet VarChar(1) Balance Dir Indicator Set default=N [N=, Y=]

# CCPD - Period-End Closing
Module: Finance | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PerAbs, Line_ID
Fields (name type(len) description [values] ->parent table):
  PerAbs Int(11) Period Code
  Line_ID Int(11) Row Number default=0
  ProfitAct nVarChar(15) Account Code ->OACT
  Ref1 nVarChar(11) Reference 1
  Ref2 nVarChar(11) Reference 2
  DueDate Date(8) Due Date
  RefDate Date(8) Posting Date
  TaxDate Date(8) Document Date
  Memo nVarChar(254) Row Details
  MarkLine VarChar(1) Select default=N [Y=Yes, N=No]
  ActKeyLine nVarChar(15) Account Code ->OACT
  LocBalLine Num(19,6) Current Balance
  FcBalLine Num(19,6) Balance (Account Currency)
  SysBalLine Num(19,6) Balance (SC)
  ToPerAbs Int(11) To Period Code
  CtrlAct nVarChar(15) Control Account ->OACT
  PL_ACCOUNT VarChar(1) P/L Account default=Y [Y=Yes, N=No]
  Ref1_l nVarChar(100) Reference 1 for line
  Ref2_l nVarChar(100) Reference 2 for line
  Ref3_l nVarChar(100) Reference 3 for line

# CDC1 - Cash Discount - Rows
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CdcCode, LineId
Fields (name type(len) description [values] ->parent table):
  CdcCode nVarChar(20) Code ->OCDC
  LineId Int(11) Row No.
  NumOfDays Int(6) Days
  Discount Num(19,6) Discount %
  Day Int(6) Day
  Month Int(6) Month

# CFH1 - Cash Flow Statement Report - History - Rows
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CFHId, LineId
Fields (name type(len) description [values] ->parent table):
  CFHId Int(11) Cash Flow History Identity ->OCFH
  LineId Int(11) Row Number
  DispItem nVarChar(100) Displayed Item Title
  Levels Int(6) Levels
  LineNum nVarChar(5) Cash Flow Line No.
  IndentChar nVarChar(6) Indent Char. default=4
  Amount Num(19,6) Amount
  Formula VarChar(1) Formula Flag default=N [N=Non-Formula, Y=Formula Node]

# DRN1 - Depreciation Run - Posting
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, AssetClass
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRN
  AcctDtn nVarChar(15) Account Determination ->OADT
  TransId Int(11) Transaction Number ->OJDT
  OrdDprAct nVarChar(15) Ordinary Depreciation Account ->OACT
  SpDprAct nVarChar(15) Special Depreciation Account ->OACT
  SpBalAct nVarChar(15) Special Balance Account ->OACT
  OrdBalAct nVarChar(15) Ordinary Balance Account ->OACT
  OrdDprAmt Num(19,6) Ordinary Depreciation Amount
  SpDprAmt Num(19,6) Special Depreciation Amount
  RevResAct nVarChar(15) Revaluation Reserve Account ->OACT
  RevResClr nVarChar(15) Revaluation Reserve Clearing ->OACT
  RevReserve Num(19,6) Revaluation Reserve Amount
  AssetClass nVarChar(20) Asset Class ->OACS
  CancelId Int(11) Cancelation Transaction No.

# DRN2 - Depreciation Run - Posting - Asset
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, AssetClass, ItemCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ODRN
  AcctDtn nVarChar(15) Account Determination ->OADT
  ItemCode nVarChar(50) Item Code ->OITM
  OrdDprAmt Num(19,6) Ordinary Depreciation Amount
  SpDprAmt Num(19,6) Special Depreciation Amount
  RevReserve Num(19,6) Revaluation Reserve Amount
  AssetClass nVarChar(20) Asset Class ->OACS

# DTP1 - Depreciation Types - Rows
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Level
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code ->ODTP
  Level Int(11) Level
  Base nVarChar(3) Base default=APC [APC=Acquisition Value, NBV=Net Book Value]
  Years Int(11) Number of Years
  Percentage Num(19,6) Percentage
  LogInstanc Int(11) Log Instance default=0
  Amount Num(19,6) Amount
  SnapshotId Int(11) Snapshot ID default=0

# FAA1 - Asset Attributes - Rows
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum
  UNIQUE U: Code, AttrID
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code ->OFAA
  LineNum Int(11) Row Number
  AttrID Int(11) Attribute ID
  AttrName nVarChar(100) Attribute Name
  FieldType VarChar(1) Field Type [A=Text, N=Numeric, D=Date, S=Amount, P=Price, Q=Quantity]
  DefaultVal nVarChar(100) Default Value
  LogInstanc Int(11) Log Instance default=0
  SnapshotId Int(11) Snapshot ID default=0

# FAC1 - Fixed Asset Parameter Change - Rows
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFAC
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  TransType nVarChar(4) Transaction Type [0=Unknown, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value, 560=Change of Period Control]
  OldDprType nVarChar(15) Old Depreciation Type ->ODTP
  NewDprType nVarChar(15) New Depreciation Type ->ODTP
  OldUsfLife Int(11) Old Useful Life
  NewUsfLife Int(11) New Useful Life
  OldDprDate Date(8) Old Depreciation Start Date
  NewDprDate Date(8) New Depreciation Start Date
  OldSalVal Num(19,6) Old Salvage Value
  NewSalVal Num(19,6) New Salvage Value
  OldTtlUnit Int(11) Old Total Units
  NewTtlUnit Int(11) New Total Units

# FAC2 - Fixed Asset Parameter Change - Period Control Change
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  PERCONTROL U: AbsEntry, DprArea, PeriodCat, VisOrder
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFAC
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  PeriodCat nVarChar(10) Period Category
  VisOrder Int(11) Visual Order
  OldDprSt VarChar(1) Old Depreciation Status default=Y [Y=Yes, N=No]
  NewDprSt VarChar(1) New Depreciation Status default=Y [Y=Yes, N=No]
  OldFactor Num(19,6) Old Factor
  NewFactor Num(19,6) New Factor

# FAM1 - Fixed Asset Data Migration - Rows
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId, LineNum
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID ->OFAM
  LineNum Int(11) Line Number
  ObjectType nVarChar(20) Object Type [1470000002=Account Determination, 1470000003=Depreciation Areas, 1470000004=Depreciation Type Pools, 1470000000=Depreciation Types, 1470000032=Asset Classes, 4=Items, 35=Item Numbering]
  ObjectCode nVarChar(20) Object Code
  ObjectName nVarChar(100) Object Name
  Status VarChar(1) Status default=Y [Y=Successful, N=Failed]
  Message nVarChar(254) Message

# FAR1 - Fixed Asset Revaluation - Rows
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OFAR
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  NBV Num(19,6) NBV
  New_NBV Num(19,6) New NBV
  Remarks nVarChar(100) Remarks
  RevalPerc Num(19,6) Revaluation Percentage %
  OrdDprDur Num(19,6) Ordinary Depr. During Period
  UnDpDur Num(19,6) Unplanned Depr. During Period
  SpDprDur Num(19,6) Special Depr. During Period
  WriteUpDur Num(19,6) Write-Up During Period

# FIX1 - Fixed Asset Transaction - Rows
Module: Finance | 34 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDARY: DprArea, PeriodCat, ItemCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFIX
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ID ->ODPA
  PeriodCat nVarChar(10) Period Category ID
  PostPeriod Int(11) Posting Subperiod
  RefDate Date(8) Posting Date
  APC Num(19,6) APC
  OrdDpr Num(19,6) Ordinary Depreciation
  UnpDpr Num(19,6) Unplanned Depreciation
  SpDprKey1 nVarChar(2) Special Depreciation Key 01 ->ODPP
  SpDpr1 Num(19,6) Special Depreciation 01
  Qty Num(19,6) Quantity
  DprType nVarChar(15) New Depreciation Type ->ODTP
  DprDate Date(8) New Depreciation Start Date
  RemLife Int(11) New Remaining Life
  SalvageVal Num(19,6) New Salvage Value
  RecvAsst nVarChar(50) Receiving Item Code ->OITM
  RetirDate Date(8) Retirement Date
  SpDprKey2 nVarChar(2) Special Depreciation Key 02 ->ODPP
  SpDpr2 Num(19,6) Special Depreciation 02
  SpDprKey3 nVarChar(2) Special Depreciation Key 03 ->ODPP
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 260=Low Value Asset Full Retirement, 270=Low Value Asset Full Scrapping, 310=Full Transfer, 320=Partial Transfer, 330=Asset Class Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 550=Revaluation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value, 560=Change of Period Control, 570=Change of Total Units]
  UsefulLife Int(11) New Useful Life
  Appr Num(19,6) Appreciation
  WriteUp Num(19,6) Write-Up
  DeltaDays Int(11) Delta Remaining Life in Days
  NewAstCls nVarChar(20) New Asset Class ->OACS
  HistOrdDpr Num(19,6) Historical Ordinary Depr.
  SpDpr3 Num(19,6) Special Depreciation 03
  TransAmnt Num(19,6) Transaction Amount
  Remark nVarChar(254) Remarks
  ReTranType nVarChar(4) Receiving Transaction Type default=0 [0=Unknown, 110=Acquisition, 115=Subacquisition]
  NewTtlUnit Int(11) New Total Unit

# FRC1 - Extend Cat. f. Financial Rep.
Module: Finance | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TemplateId, CatId, AcctCode, VisOrder
  ACCNT_CODE: AcctCode
Fields (name type(len) description [values] ->parent table):
  CatId Int(6) Numerator
  TemplateId Int(11) Template ->OFRT
  AcctCode nVarChar(15) Account Code ->OACT
  VisOrder Int(6) Display Order
  CFWId Int(11) Cash Flow Line Item ID ->OCFW
  CalcMethod nVarChar(30) Calculation Method [BOP=Beginning of Period, EOP=End of Period, CPID=Current Period In Debit, CPIC=Current Period In Credit, CPIB=Current Period In Both]
  SlpCode Int(11) Sales Unit Code ->OSLP
  PrcCode nVarChar(8) Cost Center Code ->OPRC
  CalMethod2 nVarChar(30) Calculation Method 2
  CalMethod3 nVarChar(30) Calculation Method 3
  Linked VarChar(1) Linked default=B [B=Balance, D=Debit, C=Credit]
  Sign VarChar(1) Sign default=E [E=, P=Positive, N=Negative]

# FTR1 - Transfer - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OFTR
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  AcctCode nVarChar(15) Account Code ->OACT
  Quantity Num(19,6) Quantity
  LineTotal Num(19,6) Line Total
  TotalFrgn Num(19,6) Line Total (FC)
  TotalSys Num(19,6) Line Total (SC)
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  NewItemCod nVarChar(50) New Item Code ->OITM
  Partial VarChar(1) Partial default=N [Y=Yes, N=No]
  APC Num(19,6) APC
  NewAstCls nVarChar(20) New Asset Class ->OACS
  ObjType nVarChar(20) Object Type
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 130=APC Write-Up, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 310=Full Transfer, 320=Partial Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# FTR2 - Transfer - Area Journal Transactions
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OFTR
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  JrnlMemo nVarChar(254) Journal Remarks
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
  TransNum Int(11) Transaction Number ->OJDT
  JrnlMemo1 nVarChar(254) Cancellation Journal Remarks
  TransNum1 Int(11) Cancellation Transaction No. ->OJDT

# FTR3 - Transfer - Item Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ItemLine, DprArea
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACQ
  ItemLine Int(11) Item Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Total Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSys Num(19,6) Total (SC)
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0

# GBI1 - GBI Row 1 - Electronic Account Book
Module: Finance | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  AcctBkNo nVarChar(5) Electronic Account Book No.
  AcctBkName nVarChar(30) Electronic Account Book Name
  OrgCode nVarChar(20) Organizational Code
  CompType nVarChar(8) Company Type
  Industry nVarChar(20) Industry
  SoftVender nVarChar(60) Accounting Software Provider
  Version nVarChar(20) Accounting Software Version
  FisYear nVarChar(4) Fiscal Year
  LocCurr nVarChar(3) Local Currency
  AcctStruct nVarChar(30) Account Structure

# GBI10 - GBI Row 10 - Enterprise's Cash Flow Statement
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  LineTitle nVarChar(100) Line Title
  LineNum nVarChar(5) Line Number
  Amount Num(19,6) Amount

# GBI11 - GBI Row 11 - Devalue Provision of Enterprise Assets
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History ID ->OGBI
  RowId Int(11) Row Number
  ItemName nVarChar(100) Item Name
  BOPBalance Num(19,6) Balance at Beginning of Period
  CurDebit Num(19,6) Current Period in Debit
  CurCredit Num(19,6) Current Period in Credit
  EOPBalance Num(19,6) Balance at End of Period

# GBI12 - GBI Row 12 - Shareholder's Rights and Interests Changing Report
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  ShrId Int(11) SHR Report History ID
  RowNum Int(11) Row Number in Saved Report
  ItemName nVarChar(254) Item Name
  LineNum nVarChar(6) Line number
  CurAmount Num(19,6) Amount for Current Period
  PreAmount Num(19,6) Amount for Previous Period

# GBI13 - GBI Row 13 - Enterprise's Profit Distribution Report
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History ID ->OGBI
  RowId Int(11) Row Number
  ItemName nVarChar(100) Item Name
  LineNum nVarChar(6) Line Number
  CurAmount Num(19,6) Current Period Amount
  PreAmount Num(19,6) Previous Period Amount

# GBI14 - GBI Row 14 - Small Enterprise's Cash Flow Statement
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  LineTitle nVarChar(100) Line Title
  LineNum nVarChar(5) Line Number
  PreAmount Num(19,6) Previous Year Amount
  CurAmount Num(19,6) Current Year Amount

# GBI15 - GBI Row 15 - Enterprise's VAT Payable Detail Report
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  ItemName nVarChar(100) Item Name
  LineNum nVarChar(6) Line Number
  CurMonAmnt Num(19,6) Current Month Amount
  CurYrAmnt Num(19,6) Current Year Amount

# GBI16 - GBI Row 16 - Employees
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  EmpNo nVarChar(8) Employee Number
  EmpName nVarChar(30) Employee Name

# GBI2 - GBI Row 2 - G/L Account Master Records
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  AcctCode nVarChar(15) Account Code
  AcctName nVarChar(100) Account Name
  StrucLevel Int(11) Account Structure Level
  EvalSign VarChar(1) Evaluation Sign
  AddField nVarChar(60) Possible Additional Fields
  AcctType nVarChar(20) Account Type
  MesurUnit nVarChar(10) Measurement Unit
  BlDirect nVarChar(4) Direction of Balance

# GBI3 - GBI Row 3 - Departments
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  DepNo nVarChar(8) Department Number
  DepName nVarChar(30) Department Name

# GBI4 - GBI Row 4 - Business Partners
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  BPNo nVarChar(30) BP Number
  BPName nVarChar(60) BP Name
  CatNo Int(6) Category Number
  Loc nVarChar(103) Location Area
  Tel nVarChar(50) Telephone
  Address nVarChar(100) Street/PO Box
  CreditRank nVarChar(6) Credit Rank

# GBI5 - GBI Row 5 - Projects
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  PrjCode nVarChar(20) Project Code ->OPRJ
  PrjName nVarChar(100) Project Name

# GBI6 - GBI Row 6 - G/L Account Balance
Module: Finance | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  AcctCode nVarChar(15) Account Code
  Currency nVarChar(3) Account Currency
  EvalGrp nVarChar(254) Group for Calculating
  PerBBal Num(19,6) Period Begin Balance
  PerBQty Num(19,6) Period Begin Quantity
  PerBFCBal Num(19,6) Period Begin FC Balance
  CPDAmt Num(19,6) Current Period Debit Amount
  CPDQty Num(19,6) Current Period Debit Quantity
  CPDFCAmt Num(19,6) Current Period Debit FC Amount
  CPCAmt Num(19,6) Current Period Credit Amount
  CPCQty Num(19,6) Current Period Credit Quantity
  CPCFCAmt Num(19,6) Current Period Credit FC Amnt
  PerEBal Num(19,6) Period End Balance
  PerEQty Num(19,6) Period End Quantity
  PerEFCBal Num(19,6) Period End FC Balance
  AcctPeriod nVarChar(2) Fiscal Month

# GBI7 - GBI Row 7 - Accounting Vouchers
Module: Finance | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  DocDate nVarChar(8) Document Date
  DocType nVarChar(12) Document Type
  JrnEntryNo nVarChar(20) Journal Entry Number
  LnNo Int(11) Line Number
  Remark nVarChar(50) Details of Each Line
  AcctNo nVarChar(15) G/L Account Number
  Currency nVarChar(3) Transaction Currency
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  FCDebit Num(19,6) Debit Foreign Currency Amount
  FCCredit Num(19,6) Credit Foreign Currency Amount
  Rate Num(19,6) Exchange Rate
  Quantity Num(19,6) Quantity
  UnitPrice Num(19,6) Unit Price
  EvaGrp nVarChar(254) Evaluation Group
  SettMeth nVarChar(20) Settlement Method
  BillType nVarChar(20) Bill Type
  BillNo nVarChar(30) Bill Number
  BillDate nVarChar(8) Bill Date
  AttmtNum Int(6) Number of Attachments
  Creator nVarChar(155) Creator of the Voucher
  Approver nVarChar(155) Approver of the Voucher
  Bookkeeper nVarChar(155) Bookkeeper
  Cashier nVarChar(155) Cashier
  Posted VarChar(1) Posted Sign default=1 [1=, 0=]
  Reversed VarChar(1) Reversed Sign default=0 [1=, 0=]
  DocNum nVarChar(20) Document Number

# GBI8 - GBI Row 8 - Enterprise's Balance Sheet
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  AcctName nVarChar(100) Account Name
  LineNum nVarChar(6) Line Number
  YearBAmt Num(19,6) Year Begin Amount
  PerEAmt Num(19,6) Period End Amount
  RepDate nVarChar(8) Report Date

# GBI9 - GBI Row 9 - Enterprise's Profit and Loss Statement
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: HistoryId, RowId
Fields (name type(len) description [values] ->parent table):
  HistoryId Int(11) History Key ->OGBI
  RowId Int(11) Row Number
  RepItm nVarChar(60) Report Item
  RepItmNo nVarChar(3) Report Item Number
  PeriodAmt Num(19,6) Period Amount
  YearAmt Num(19,6) Year Accumulated Amount

# ISW1 - Reported Business Partners
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizAbsEnt, CardCode
Fields (name type(len) description [values] ->parent table):
  WizAbsEnt Int(11) Wizard Run Key ->OISW
  CardCode nVarChar(15) Business Partner Code ->OCRD
  CardName nVarChar(100) Business Partner Name
  CardType VarChar(1) Business Partner Type
  NatOfTrans nVarChar(50) Nature of Transaction
  StatProc nVarChar(50) Statistical Procedure
  CustProc nVarChar(50) Customs Procedure
  TransMode nVarChar(12) Transport Mode
  Incoterms nVarChar(12) Incoterms
  PortEnEx nVarChar(50) Port of Entry or Exit
  BPVATRegNo nVarChar(32) Business Partner VAT Reg. No.
  DomFrgID VarChar(1) Domestic/Foreign Identifier
  CtryOrig nVarChar(3) Country/Region of Origin
  BPCountry nVarChar(3) Business Partner Country/Region

# ISW2 - Intrastat Reported Items
Module: Finance | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizAbsEnt, ItemCode
Fields (name type(len) description [values] ->parent table):
  WizAbsEnt Int(11) Wizard Run Key ->OISW
  ItemCode nVarChar(50) Item Code ->OITM
  CommCode nVarChar(12) Commodity Code
  SerCode nVarChar(12) Service Code
  AddMUnit nVarChar(50) Additional Measure Unit
  FactorAM Num(19,6) Factor Additional Measure
  OriRegSta nVarChar(12) Region of Origin (for Export)
  DstRegSta nVarChar(12) Destination Region (Import)
  CtryOrig nVarChar(3) Country/Region of Origin
  SerSupplM nVarChar(12) Service Supply Method default=I [I=Immediate, R=To More Resumptions]
  SerPymMeth nVarChar(12) Service Payment Method default=X [A=Accredited to Bank Account, B=Bank Transfer, X=Other]
  ItemType VarChar(1) Item Type default=I [I=Item, S=Service, N=Item not relevant to Intrastat]
  ItemName nVarChar(200) Item Name
  DestRegCry nVarChar(3) Destination Country - Region
  OrigRegCry nVarChar(3) Origin Region Country
  UseWeight VarChar(1) Use Wt in Add. Measure Calc. default=Y [Y=Yes, N=No]
  StatCode nVarChar(2) Statistical Code
  NatOfTrans nVarChar(50) Nature of Transaction
  StatProc nVarChar(50) Statistical Procedure

# ISW3 - Declaration Rows
Module: Finance | 78 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizAbsEnt, Line
Fields (name type(len) description [values] ->parent table):
  WizAbsEnt Int(11) Wizard Run Key ->OISW
  Line Int(11) Declaration Line
  ItemCode nVarChar(50) Item Code ->OITM
  RowStatus VarChar(1) Row Status default=O
  CardCode nVarChar(15) Business Partner Code ->OCRD
  ObjType Int(11) Document Type
  DocNum Int(11) Document Number
  DocLineNum Int(11) Document Line Number
  RecpType VarChar(1) Receipt Type
  DocBillDt Date(8) Document Billing Date
  Quantity Num(19,6) Quantity
  BPCtry nVarChar(3) Sender or Receiver Country/Region
  TaxCodeExt nVarChar(12) Tax Code Extension
  NetMassSgn VarChar(1) Net Mass Sign default=+ [+=Positive, -=Negative]
  NetMass Num(19,6) Net Mass
  NetMassUnt nVarChar(12) Net Mass Unit
  SupMassSgn VarChar(1) Supplementary Mass Sign default=+ [+=Positive, -=Negative]
  SupplMass Num(19,6) Supplementary Mass
  SupplUnit nVarChar(50) Supplementary Unit
  ValueSgn VarChar(1) Value Sign default=+ [+=Positive, -=Negative]
  Value Num(19,6) Value
  ValueFC Num(19,6) Value in Foreign Currency
  FCCurrency nVarChar(3) Foreign Currency
  StatValSgn VarChar(1) Statistical Value Sign [+=Positive, -=Negative]
  StatVal Num(19,6) Statistical Value
  ReturnID VarChar(1) Return Identifier
  Include VarChar(1) Include Line in Report default=Y [Y=Yes, N=No]
  IsChanged VarChar(1) Changed Line Flag default=N [Y=Yes, N=No]
  DstRegCry nVarChar(3) Destination Country - Region
  DstRegSta nVarChar(12) Destination Region State
  OriRegCry nVarChar(3) Origin Region Country
  OriRegSta nVarChar(12) Origin Region State
  BpVATregNo nVarChar(32) VAT Registration No.
  CtryOrig nVarChar(3) Country/Region of Origin
  Incoterms nVarChar(12) Incoterms
  NatOfTrans nVarChar(50) Nature of Transaction
  TransMode nVarChar(12) Transport Mode
  PortEnEx nVarChar(50) Port of Entry or Exit
  CustProc nVarChar(50) Custom Procedure
  StatProc nVarChar(50) Statistical Procedure
  DomFrgID VarChar(1) Domestic/Foreign Identifier
  ItemType VarChar(1) Item Type default=I [I=Item, S=Service, N=Item Not Relevant to Intrastat]
  CommCode nVarChar(12) Commodity Code
  SerCode nVarChar(12) Service Code
  SerSupplM VarChar(1) Service Supply Method default=I [I=Immediate, R=To More Resumptions]
  SerPymMeth VarChar(1) Service Payment Method default=A [A=Accredited to Bank Account, B=Bank Transfer, X=Other]
  CorrDate Date(8) Correction Date
  CorrSgn VarChar(1) Correction Sign default=+ [+=Positive, -=Negative]
  ReferDoc Int(11) Referenced Document
  ReferDocNo Int(11) Referenced Document No.
  ReferItem nVarChar(50) Referred Item ->OITM
  RefDocLine Int(11) Referenced Document Line
  ChgID nVarChar(16) Changed Data Record ID
  ChgUser nVarChar(50) Changed By
  ChgTimest Date(8) Time Stamp of Change
  Deleted VarChar(1) Deleted Indicator default=N [N=No, Y=Yes]
  CstSecRc nVarChar(6) Custom Section
  CorrMonth Int(6) Ref. Mo. of Summary to Correct
  CorrYear Int(6) Ref. Yr of Summary to Correct
  CorrDeclNo Int(11) No. of Declaration to Correct
  CorRowNo Int(11) Row No. Inside Sec. 3 to Correct
  DeclRowNo Int(11) Declaration File Row No.
  CorrType Int(11) Referred Type of Receipt
  CntryPay nVarChar(3) State Code for Payment
  Triangular VarChar(1) Triangular Trade default=N [N=No, Y=Yes]
  CardName nVarChar(100) Business Partner Name
  StatCode nVarChar(2) Statistical Code
  DocEntry Int(11) Document Entry
  NetValue Num(19,6) Net Value
  NetValueFC Num(19,6) Net Value in FC
  Freight Num(19,6) Freight Sum
  FreighFC Num(19,6) Freight Sum in FC
  RateFC Num(19,6) Currency Rate for FC
  Remarks nVarChar(250) Remarks
  ProtocolN Int(11) Protocol Number
  DropShip VarChar(1) Drop-Ship default=N [Y=Yes, N=No]
  WhsZipCode nVarChar(20) Warehouse Zip Code
  ValBefDsc Num(19,6) Value Before Discount

# IWZ1 - Accounts Revaluation History
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, AcctCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OIWZ
  AcctCode nVarChar(15) Account Code ->OACT
  ActName nVarChar(100) Account Name
  ActFrmBlnc Num(19,6) Account From Balance
  ExecutLine VarChar(1) Executed Row default=Y [Y=Executed Row, N=Filter Line]
  ActRevCncl VarChar(1) Account Revaluation Cancel default=N [N=No, Y=Yes]
  RevToAct nVarChar(15) Revaluate To Account
  ActDiffBal Num(19,6) Account Difference Balance
  RvCaclDate Date(8) Reval. Acct Cancellation Date
  ErrReason Int(11) Error Reason
  ActLastBal Num(19,6) Account Last Reval Balance

# IWZ2 - Inflation Warehouse Filter
Module: Finance | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, WhCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WhCode nVarChar(8) Warehouse Code ->OWHS

# IWZ3 - Items Last Revaluation Data
Module: Finance | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ItemCode, WhCode
  ABS: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OIWZ
  ItemCode nVarChar(50) Item Number ->OITM
  WhCode nVarChar(8) Warehouse Code ->OWHS
  RevalPrice Num(19,6) Revaluated Price
  BaseCurr nVarChar(3) Item Base Currency
  RevalDate Date(8) Revaluation Date
  RevalSum Num(19,6) Revaluation Sum
  BasePrice Num(19,6) Base Price
  RealAcct nVarChar(15) Revaluation Account ->OACT
  RevalOfsac nVarChar(15) Reval. Offset Account ->OACT
  RevalType VarChar(1) Revaluation Type default=S [S=Inventory Reval. Type, C=COGS Revaluation Type]
  ExeLine VarChar(1) Executed Row default=Y [Y=Yes, N=No]
  RevCancel VarChar(1) Revaluation Cancel default=N [N=No, Y=Yes]
  RvCaclDate Date(8) Reval. Acct Cancellation Date
  Quantity Num(19,6) Quantity
  BalanceBef Num(19,6) Balance Before Revaluation

# JDT1 - Journal Entry - Rows
Module: Finance | 145 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TransId, Line_ID
  SHORT_NAME: ShortName, IntrnMatch
  ACCOUNT: Account, IntrnMatch
  TRANS_TYPE: TransType
  PROFIT_ID: ProfitCode
  CURRENCY: FCCurrency
  DUEDATE: DueDate
  REFDATE: RefDate
  INTRNMATCH: ShortName, Account, IntrnMatch
  JDT1BASEL: TransType, CreatedBy, SourceLine
  JDT1CHECKA: CheckAbs, TransType
Fields (name type(len) description [values] ->parent table):
  TransId Int(11) Transaction Key ->OJDT
  Line_ID Int(11) Row Number default=0
  Account nVarChar(15) Account Code ->OACT
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  SYSCred Num(19,6) System Credit Amount
  SYSDeb Num(19,6) System Debit Amount
  FCDebit Num(19,6) Debit Amount (FC)
  FCCredit Num(19,6) Credit Amount (FC)
  FCCurrency nVarChar(3) Foreign Currency
  DueDate Date(8) Due Date
  SourceID Int(11) Source Key
  SourceLine Int(6) Source Row Number
  ShortName nVarChar(15) BP/Account Code
  IntrnMatch Int(11) Internal Reconciliation No. default=0
  ExtrMatch Int(11) External Reconciliation No. default=0
  ContraAct nVarChar(15) Offset Account
  LineMemo nVarChar(254) Row Details
  Ref3Line nVarChar(100) Reference 3
  TransType nVarChar(20) Original Journal default=-1 [15=Delivery, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 19=A/P Credit Memo, 69=Landed Costs, 163=A/P Correction Invoice, 24=Incoming Payment, 25=Deposit, 46=Vendor Payment, 57=Checks for Payment, 76=Postdated Deposit, 182=BoE Transaction, -2=Opening Balance, -3=Closing Balance, 30=Journal Entry, 58=Stock Update, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, 68=Work Instructions, 162=Inventory Valuation, -1=All Transactions, 321=Internal Reconciliation, 140000009=Outgoing Excise Invoice, 10000079=TDS Adjustment, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 140000010=Incoming Excise Invoice, 202=Production Order]
  RefDate Date(8) Posting Date
  Ref2Date Date(8) Posting Date 3
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  CreatedBy Int(11) Origin
  BaseRef nVarChar(11) Base Reference
  Project nVarChar(20) Project Code ->OPRJ
  TransCode nVarChar(4) Transaction Code ->OTRC
  ProfitCode nVarChar(8) Distribution Rule ->OOCR
  TaxDate Date(8) Document Date
  SystemRate Num(19,6) System Price
  MthDate Date(8) Reconciliation Date
  ToMthSum Num(19,6) Reconciliation Total
  UserSign Int(6) User Signature ->OUSR
  BatchNum Int(11) Journal Voucher No. ->OBTD
  FinncPriod Int(11) Posting Period ->OFPR
  RelTransId Int(11) Linked Transaction Key default=-1
  RelLineID Int(11) Linked Row No. default=-1
  RelType VarChar(1) Link Type default=N [N=Without Link, D=WTax Deduction - Correction]
  LogInstanc Int(11) Log Instance default=0
  VatGroup nVarChar(8) Tax Group ->OVTG
  BaseSum Num(19,6) Base Amount
  VatRate Num(19,6) Tax %
  Indicator nVarChar(2) Indicator Code ->OIDC
  AdjTran VarChar(1) Adjusting Trans. (Period 13) default=N [Y=Yes, N=No]
  RevSource VarChar(1) Revaluation Source default=N [F=Foreign Currency, S=System, N=No]
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  VatDate Date(8) Document Date
  PaymentRef nVarChar(27) Payment Reference No.
  SYSBaseSum Num(19,6) System Base Amount
  MultMatch Int(11) Multiple BP Reconciliation No. default=0
  VatLine VarChar(1) VAT Row default=N [Y=Yes, N=No]
  VatAmount Num(19,6) VAT Amount
  SYSVatSum Num(19,6) System VAT Amount
  Closed VarChar(1) Closed default=N
  GrossValue Num(19,6) Gross Value
  CheckAbs Int(11) Internal Check Number
  LineType Int(11) Line Type default=0
  DebCred VarChar(1) Debit Credit Line Indicator [D=Debit, C=Credit]
  SequenceNr Int(11) Assigned Sequence No. default=0
  StornoAcc nVarChar(15) Storno Account Code ->OACT
  BalDueDeb Num(19,6) Balance Due - Debit
  BalDueCred Num(19,6) Balance Due - Credit
  BalFcDeb Num(19,6) Balance Due (FC) - Debit
  BalFcCred Num(19,6) Balance Due (FC) - Credit
  BalScDeb Num(19,6) Balance Due (SC) - Debit
  BalScCred Num(19,6) Balance Due (SC) - Credit
  IsNet VarChar(1) Use Net Amount default=Y [Y=Yes, N=No]
  DunWizBlck VarChar(1) Wizard Dunning Block default=N [N=No, Y=Yes]
  DunnLevel Int(11) Dunning Level default=0 ->ODUN
  DunDate Date(8) Last Dunning Date
  TaxType Int(6) Tax Type default=0
  TaxPostAcc VarChar(1) Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  StaCode nVarChar(8) Authority Code ->OSTA
  StaType Int(11) Authority Type ->OSTT
  TaxCode nVarChar(8) Tax Code ->OSTC
  ValidFrom Date(8) Valid From default=19000101
  GrossValFc Num(19,6) Gross Value (FC)
  LvlUpdDate Date(8) Dunning Level Update Date
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  MIEntry Int(11) MI Entry when include this OB default=0 ->OMIN
  MIVEntry Int(11) A/P Monthly Invoice default=0 ->OMIV
  ClsInTP Int(11) Tax Payment Wizard default=0 ->OTPW
  CenVatCom Int(11) CENVAT Component default=-1
  MatType Int(11) Material Type default=-1
  PstngType Int(11) Posting Type default=0
  ValidFrom2 Date(8) Valid from2 default=19000101
  ValidFrom3 Date(8) Valid from3 default=19000101
  ValidFrom4 Date(8) Valid from4 default=19000101
  ValidFrom5 Date(8) Valid from5 default=19000101
  Location Int(11) Loc. ->OLCT
  WTaxCode nVarChar(4) Withholding Tax Code ->OWHT
  EquVatRate Num(19,6) Equalization Tax %
  EquVatSum Num(19,6) Equalization Tax Amount
  SYSEquSum Num(19,6) System Equalization Tax Amount
  TotalVat Num(19,6) Total Tax
  SYSTVat Num(19,6) System Total Tax
  WTLiable VarChar(1) WTax-Liable default=N [Y=Yes, N=No]
  WTLine VarChar(1) WTax Row default=N [Y=Yes, N=No]
  WTApplied Num(19,6) Applied WTax
  WTAppliedS Num(19,6) Applied WTax (SC)
  WTAppliedF Num(19,6) Applied WTax (FC)
  WTSum Num(19,6) WTax Amount
  WTSumFC Num(19,6) WTax Amount (FC)
  WTSumSC Num(19,6) WTax Amount (SC)
  PayBlock VarChar(1) Payment Block default=N [Y=Yes, N=No]
  PayBlckRef Int(11) Payment Block Abs Entry ->OPYB
  LicTradNum nVarChar(32) Federal Tax ID
  InterimTyp Int(11) Interim Account Type default=0
  DprId Int(11) Down Payment Request Key
  MatchRef nVarChar(20) Reconciliation Reference
  Ordered VarChar(1) Payment Ordered default=N [Y=Yes, N=No]
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  SLEDGERF VarChar(1) Subledger Flag
  InitRef2 nVarChar(100) Initial Reference 2
  InitRef3Ln nVarChar(27) Initial Reference 3
  ExpUUID nVarChar(50) Expense UUID
  ExpOPType VarChar(1) Expense Operation Type [P=Professional Services, R=Renting Assets, O=Others]
  ExTransId Int(11) Exposed Transaction ID
  DocArr Int(6) Source of Posting
  DocLine Int(11) Source Line Internal ID
  MYFtype nVarChar(2) MYF type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  DocEntry Int(11) Source Document Entry
  DocNum Int(11) Source Document Number
  DocType nVarChar(20) Source Document Type
  DocSubType nVarChar(2) Document Subtype
  RmrkTmpt Int(11) Remark Text Template ->OTTR
  CemCode nVarChar(20) Cost Element Code ->OCEM
  InClassCat Int(11) Income Classification Category
  InClassTyp Int(11) Income Classification Type
  ExClassCat Int(11) Expense Classification Category
  ExClassTyp Int(11) Expense Classification Type
  VATClassCa Int(11) VAT Classification Category
  VATClassTy Int(11) VAT Classification Type
  EVatCate Int(11) VAT Category
  EWtPercCat Int(11) Withheld Percentage Category
  EWtAmount Num(19,6) Withheld Amount
  EBVatExCau Int(11) VAT Exemption Cause ->OVEC

# JDT2 - Withholding Tax - History
Module: Finance | 158 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  SECONDERY U: AbsEntry, WTCode, BaseAbsEnt
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator ->OJDT
  WTCode nVarChar(4) WTax Code ->OWHT
  Rate Num(19,6) Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  ApplAmnt Num(19,6) Applied WTax Amount
  ApplAmntSC Num(19,6) Applied WTax Amount (SC)
  ApplAmntFC Num(19,6) Applied WTax Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) WTax Criteria [Y=Accrual, N=Cash]
  Account nVarChar(15) G/L Account ->OACT
  Type VarChar(1) Withholding Type [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values, N=No Rounding]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT, U=UoM]
  BaseAbsEnt Int(11) Base Document Reference default=-1
  BaseLine Int(11) Base Row
  BaseNum Int(11) Base Document Type default=-1 [-1=]
  LineNum Int(11) Row Number
  BaseRef Int(11) Base Document Reference
  Status VarChar(1) Status default=O [O=Open, C=Closed]
  TrgType Int(11) Target Document Type
  TrgAbsEntr Int(11) Target Doc. Internal No. default=-1
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  Doc1LineNo Int(11) DOC1 Line Number default=-1
  WtLineType VarChar(1) WTax Row Type default=D [D=Document Level WTax, L=Row Level WTax]
  TxblCurr nVarChar(3) Taxable Currency from Doc Row
  DtblCurr nVarChar(3) Deductible Currency
  DtblRate Num(19,6) Rate for Deductible Amount
  txblRate Num(19,6) Rate for Taxable Amount
  DtblAmount Num(19,6) Deductible Amount
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)
  TdsAppl Num(19,6) Applied TDS Amount
  TdsApplSC Num(19,6) Applied TDS Amount (SC)
  TdsApplFC Num(19,6) Applied TDS Amount (FC)
  SurAppl Num(19,6) Applied Surcharge Amount
  SurApplSC Num(19,6) Applied Surcharge Amount (SC)
  SurApplFC Num(19,6) Applied Surcharge Amount (FC)
  CessAppl Num(19,6) Applied Cess Amount
  CessApplSC Num(19,6) Applied Cess Amount (SC)
  CessApplFC Num(19,6) Applied Cess Amount (FC)
  HscAppl Num(19,6) Applied HSC Amount
  HscApplSC Num(19,6) Applied HSC Amount (SC)
  HscApplFC Num(19,6) Applied HSC Amount (FC)
  BatchNum Int(11) Journal Voucher No. ->OBTD
  InCSTCode nVarChar(2) CST Code Incoming
  OutCSTCode nVarChar(2) CST Code Outgoing
  DpmWTApl Num(19,6) DPM WT Applied Amount
  DpmWTAplSC Num(19,6) DPM WT Applied Amount (SC)
  DpmWTAplFC Num(19,6) DPM WT Applied Amount (FC)
  WTTypeId Int(11) WT Type Id ->OWTT
  LnBsAmt Num(19,6) BR Line WT Base Amount
  LnBsAmtSC Num(19,6) BR Line WT Base Amount(SC)
  LnBsAmtFC Num(19,6) BR Line WT Base Amount(FC)
  LnCmTAmt Num(19,6) BR Line Cumulated Taxable Amount
  LnCmTAmtSC Num(19,6) BR Line Cumulated Taxable Amount(SC)
  LnCmTAmtFC Num(19,6) BR Line Cumulated Taxable Amount(FC)
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=SALES TCS]
  IgstAcc nVarChar(15) IGST Account ->OACT
  CgstAcc nVarChar(15) CGST Account ->OACT
  SgstAcc nVarChar(15) SGST Account ->OACT
  IgstAmnt Num(19,6) IGST Tax Amount
  IgstAmntSC Num(19,6) IGST Tax Amount (SC)
  IgstAmntFC Num(19,6) IGST Tax Amount (FC)
  CgstAmnt Num(19,6) CGST Tax Amount
  CgstAmntSC Num(19,6) CGST Tax Amount (SC)
  CgstAmntFC Num(19,6) CGST Tax Amount (FC)
  SgstAmnt Num(19,6) SGST Tax Amount
  SgstAmntSC Num(19,6) SGST Tax Amount (SC)
  SgstAmntFC Num(19,6) SGST Tax Amount (FC)
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  IgstBAmt Num(19,6) IGST Base Amount
  IgstBAmtSC Num(19,6) IGST Base Amount (SC)
  IgstBAmtFC Num(19,6) IGST Base Amount (FC)
  CgstBAmt Num(19,6) CGST Base Amount
  CgstBAmtSC Num(19,6) CGST Base Amount (SC)
  CgstBAmtFC Num(19,6) CGST Base Amount (FC)
  SgstBAmt Num(19,6) SGST Base Amount
  SgstBAmtSC Num(19,6) SGST Base Amount (SC)
  SgstBAmtFC Num(19,6) SGST Base Amount (FC)
  IgstAppl Num(19,6) Applied IGST Amount
  IgstApplSC Num(19,6) Applied IGST Amount (SC)
  IgstApplFC Num(19,6) Applied IGST Amount (FC)
  CgstAppl Num(19,6) Applied CGST Amount
  CgstApplSC Num(19,6) Applied CGST Amount (SC)
  CgstApplFC Num(19,6) Applied CGST Amount (FC)
  SgstAppl Num(19,6) Applied SGST Amount
  SgstApplSC Num(19,6) Applied SGST Amount (SC)
  SgstApplFC Num(19,6) Applied SGST Amount (FC)
  UtgstAcc nVarChar(15) UTGST Account ->OACT
  CsgstAcc nVarChar(15) Cess GST Account ->OACT
  UtgstAmt Num(19,6) UTGST Tax Amount
  UtgstAmtSC Num(19,6) UTGST Tax Amount (SC)
  UtgstAmtFC Num(19,6) UTGST Tax Amount (FC)
  CsgstAmt Num(19,6) Cess GST Tax Amount
  CsgstAmtSC Num(19,6) Cess GST Tax Amount (SC)
  CsgstAmtFC Num(19,6) Cess GST Tax Amount (FC)
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UtgstBAmt Num(19,6) UTGST Base Amount
  UtgstBAmtS Num(19,6) UTGST Base Amount (SC)
  UtgstBAmtF Num(19,6) UTGST Base Amount (FC)
  CsgstBAmt Num(19,6) Cess GST Base Amount
  CsgstBAmtS Num(19,6) Cess GST Base Amount (SC)
  CsgstBAmtF Num(19,6) Cess GST Base Amount (FC)
  UtgstAppl Num(19,6) Applied UTGST Amount
  UtgstApplS Num(19,6) Applied UTGST Amount (SC)
  UtgstApplF Num(19,6) Applied UTGST Amount (FC)
  CsgstAppl Num(19,6) Applied Cess GST Amount
  CsgstApplS Num(19,6) Applied Cess GST Amount (SC)
  CsgstApplF Num(19,6) Applied Cess GST Amount (FC)
  EncryptIV nVarChar(100) Encrypt IV
  TcsIntAcct nVarChar(15) TCS Interim Account ->OACT
  SurIntAcct nVarChar(15) Surcharge Interim Account ->OACT
  CesIntAcct nVarChar(15) Cess Interim Account ->OACT
  HscIntAcct nVarChar(15) HSC interim Account ->OACT
  LnIntAcct nVarChar(15) Interim Account for Tax ->OACT
  FixedAmnt Num(19,6) Fixed Amount
  FixedAmtSC Num(19,6) Fixed Amount (SC)
  FixedAmtFC Num(19,6) Fixed Amount (FC)
  BaseQty Num(19,6) Base Quantity

# JST1 - TDS Adjustment - Rows
Module: Finance | 52 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, LineNum
  BASE_ENTRY: AbsId, BaseNum, BaseAbsId, BaseLine
  WT_CODE: AbsId, WTCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number ->OJST
  LineNum Int(11) Row Number default=0
  WTCode nVarChar(4) WTax Code ->OWHT
  BaseNum Int(11) Base Document Type default=-1 [-1=, 18=A/P Invoice, 204=A/P Down Payment]
  BaseAbsId Int(11) Base Document Internal ID
  BaseLine Int(11) Base Row
  LogInstanc Int(11) Log Instance default=0
  Rate Num(19,6) Rate
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  TaxbleAmnt Num(19,6) Taxable Amount
  TxblAmntSC Num(19,6) Taxable Amount (SC)
  TxblAmntFC Num(19,6) Taxable Amount (FC)
  Category VarChar(1) Category [P=Payment, I=Invoice]
  Criteria VarChar(1) Criteria [Y=Accrual, N=Cash]
  Type VarChar(1) Withholding Tax Type [V=VAT Withholding, I=Incoming Tax Withholding]
  RoundType VarChar(1) Rounding Type [T=Truncated, C=Commercial Values]
  BaseType VarChar(1) Base Type [G=Gross, N=Net, V=VAT]
  Account nVarChar(15) G/L Account ->OACT
  TdsAcc nVarChar(15) TDS Account ->OACT
  SurAcc nVarChar(15) Surcharge Account ->OACT
  CessAcc nVarChar(15) Cess Account ->OACT
  HscAcc nVarChar(15) HSC Account ->OACT
  WTAmnt Num(19,6) WTax Amount
  WTAmntSC Num(19,6) WTax Amount (SC)
  WTAmntFC Num(19,6) WTax Amount (FC)
  TdsBAmt Num(19,6) TDS Base Amount
  TdsBAmtSC Num(19,6) TDS Base Amount (SC)
  TdsBAmtFC Num(19,6) TDS Base Amount (FC)
  SurBAmt Num(19,6) Surcharge Base Amount
  SurBAmtSC Num(19,6) Surcharge Base Amount (SC)
  SurBAmtFC Num(19,6) Surcharge Base Amount (FC)
  CessBAmt Num(19,6) Cess Base Amount
  CessBAmtSC Num(19,6) Cess Base Amount (SC)
  CessBAmtFC Num(19,6) Cess Base Amount (FC)
  HscBAmt Num(19,6) HSC Base Amount
  HscBAmtSC Num(19,6) HSC Base Amount (SC)
  HscBAmtFC Num(19,6) HSC Base Amount (FC)
  TdsAmnt Num(19,6) TDS Tax Amount
  TdsAmntSC Num(19,6) TDS Tax Amount (SC)
  TdsAmntFC Num(19,6) TDS Tax Amount (FC)
  SurAmnt Num(19,6) Surcharge Tax Amount
  SurAmntSC Num(19,6) Surcharge Tax Amount (SC)
  SurAmntFC Num(19,6) Surcharge Tax Amount (FC)
  CessAmnt Num(19,6) Cess Tax Amount
  CessAmntSC Num(19,6) Cess Tax Amount (SC)
  CessAmntFC Num(19,6) Cess Tax Amount (FC)
  HscAmnt Num(19,6) HSC Tax Amount
  HscAmntSC Num(19,6) HSC Tax Amount (SC)
  HscAmntFC Num(19,6) HSC Tax Amount (FC)

# MDP1 - Manual Depreciation - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OMDP
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  AcctCode nVarChar(15) Account Code ->OACT
  Quantity Num(19,6) Quantity
  LineTotal Num(19,6) Line Total
  TotalFrgn Num(19,6) Line Total (FC)
  TotalSys Num(19,6) Line Total (SC)
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  NewItemCod nVarChar(50) New Item Code ->OITM
  Partial VarChar(1) Partial default=N [Y=Yes, N=No]
  APC Num(19,6) APC
  NewAstCls nVarChar(20) New Asset Class ->OACS
  ObjType nVarChar(20) Object Type
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 130=APC Write-Up, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 310=Full Transfer, 320=Partial Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# MDP2 - Manual Depreciation - Area Journal Transactions
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OMDP
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  JrnlMemo nVarChar(254) Journal Remarks
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
  TransNum Int(11) Transaction Number ->OJDT
  JrnlMemo1 nVarChar(254) Cancellation Journal Remarks
  TransNum1 Int(11) Cancellation Transaction No. ->OJDT

# MDP3 - Manual Depreciation - Item Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ItemLine, DprArea
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACQ
  ItemLine Int(11) Item Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Total Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSys Num(19,6) Total (SC)
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0

# MDR1 - Manual Distribution Rule - Rows
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode, PrcCode, ValidFrom
  PROF_ID: PrcCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code ->OMDR
  PrcCode nVarChar(8) Center Code ->OPRC
  PrcAmount Num(19,6) Total in Center
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=, N=]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Effective From default=19000101 [19000101=]
  ValidTo Date(8) Effective To
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update

# OACD - Credit Memo
Module: Finance | 44 columns | ObjType: 1470000060
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
  TRANS_TYPE: TransType, CreatedBy
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PeriodCat nVarChar(10) Period Category
  FinncPriod Int(11) Posting Period ->OFPR
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=P [P=Posted, D=Draft, C=Canceled]
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  Reference nVarChar(32) Reference
  ObjType nVarChar(20) Object Type
  Currency nVarChar(3) Currency ->OCRN
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Rate
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  TransType nVarChar(20) Original Document default=-1 [13=A/R Invoice, 19=A/P Credit Memo, 18=A/P Invoice, 46=Outgoing Payment, 163=A/P Correction Invoice, 1470000049=Capitalization, 1470000060=Fixed Assets Credit Memo, -1=All Transactions, 1470000075=Manual Depreciation, 1470000090=Fixed Assets Transfer, 1470000094=Retirement]
  CreatedBy Int(11) Original
  JrnlMemo nVarChar(254) Journal Remarks
  AssetDate Date(8) Asset Value Date
  CurSource VarChar(1) Base Currency default=L [L=Local Currency, S=System Currency, F=Foreign Currency]
  DocType nVarChar(15) Document Type default=PL [PL=Ordinary Depreciation, UP=Unplanned Depreciation, SD=Special Depreciation, AP=Appreciation, TR=Asset Transfer, NC=Sales, SC=Scrapping, TC=Asset Class Transfer]
  PrjSmarz VarChar(1) Summarize by Project default=N [Y=Yes, N=No]
  DstRlSmarz VarChar(1) Summarize by Distribution Rule default=N [Y=Yes, N=No]
  ManDprType nVarChar(15) Manual Depreciation Type ->ODTP
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  DprArea nVarChar(15) Depreciation Area ->ODPA
  BPLId Int(11) Branch ->OBPL
  BaseRef nVarChar(11) Base Reference
  LVARetire VarChar(1) Low Value Asset Retirement default=N [Y=Yes, N=No]
  CancelOpt Int(6) Cancelation Option default=1
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  GdsMovType nVarChar(2) Goods Movement Type

# OACG - Account Category
Module: Finance | 6 columns | ObjType: 238
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  SECOND U: Source, Name
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Name nVarChar(40) Name
  Source VarChar(1) Source default=B [B=Balance Sheet, P=Profit and Loss, C=Trial Balance, O=Other]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DateSource VarChar(1) Date Source [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Document Date, P=Partner Implementation, T=Year Transfer]
  UserSign nVarChar(6) User Signature ->OUSR

# OACK - Acknowledge Number
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  LOC_QUART U: FinYear, Quarter, Location
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  FinYear Int(11) Financial Year ->OFYM
  Quarter VarChar(1) Quarter [1=Quarter 1, 2=Quarter 2, 3=Quarter 3, 4=Quarter 4]
  AckNum nVarChar(100) Acknowledgment No.
  Location Int(11) Location ->OLCT

# OACM - Accumulation
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  ACCUM: CardCode, WTCode, PeriodCat
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  WTCode nVarChar(4) WTax Code ->OWHT
  PeriodCat nVarChar(20) Period Category
  AcmAmt Num(19,6) Accumulation Amount
  ExcdTransc VarChar(1) Exceed Transaction Threshold default=N [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update

# OACP - Periods Category
Module: Finance | 183 columns | ObjType: 220
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CATEGORY U: PeriodCat
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number default=0
  PeriodCat nVarChar(10) Period Category
  FinancYear Date(8) Beginning of Financial Year
  Year Int(6) Financial Year
  PeriodName nVarChar(20) Period Name
  SubType VarChar(1) Sub-Period Type default=Y [Y=Year, Q=Quarters, M=Months, D=Days]
  PeriodNum Int(11) Number of Periods
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  LinkAct_1 nVarChar(15) Domestic Accounts Receivable ->OACT
  LinkAct_2 nVarChar(15) Checks Received ->OACT
  LinkAct_3 nVarChar(15) Cash on Hand ->OACT
  LinkAct_4 nVarChar(15) Account ->OACT
  LinkAct_5 nVarChar(15) Sales Tax Account ->OACT
  LinkAct_6 nVarChar(15) Customer's Deduction at Source ->OACT
  ComissAct nVarChar(15) Credit Card Deposit Fee ->OACT
  LinkAct_8 nVarChar(15) Purchase Tax ->OACT
  LinkAct_9 nVarChar(15) Foreign Accounts Receivable ->OACT
  LinkAct_10 nVarChar(15) Domestic Accounts Payable ->OACT
  LinkAct_11 nVarChar(15) Foreign Accounts Payable ->OACT
  LinkAct_12 nVarChar(15) Bank Transfer ->OACT
  LinkAct_13 nVarChar(15) Tax Payable ->OACT
  LinkAct_14 nVarChar(15) Tax Definition ->OACT
  LinkAct_15 nVarChar(15) Equipment and Assets ->OACT
  LinkAct_16 nVarChar(15) Withholding Tax ->OACT
  LinkAct_17 nVarChar(15) Advances on Corp. Income Tax ->OACT
  LinkAct_18 nVarChar(15) Opening Balance Account ->OACT
  DfltIncom nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Tax Exempt Revenue Account ->OACT
  DfltExpn nVarChar(15) Expense Account ->OACT
  ForgnIncm nVarChar(15) Revenue Account - Foreign ->OACT
  ECIncome nVarChar(15) Revenue Account - EU ->OACT
  ForgnExpn nVarChar(15) Expense Account - Foreign ->OACT
  DfltRateDi nVarChar(15) Ex. Rate Diff. in All Curr. BP ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  LinkAct_27 nVarChar(15) Automatic Reconciliation Diff. ->OACT
  DftStockOB nVarChar(15) Acct. for Opening Whse Balance ->OACT
  LinkAct_19 nVarChar(15) Cash Discount ->OACT
  LinkAct_20 nVarChar(15) Cash Discount Clearing ->OACT
  LinkAct_21 nVarChar(15) Realized Exchange Diff. Loss ->OACT
  LinkAct_22 nVarChar(15) Cash Discount ->OACT
  LinkAct_23 nVarChar(15) Realized Exchange Diff. Loss ->OACT
  LinkAct_24 nVarChar(15) Rounding Account ->OACT
  LinkAct_25 nVarChar(15) Realized Exchange Diff. Gain ->OACT
  LinkAct_26 nVarChar(15) Realized Exchange Diff. Gain ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  RturnngAct nVarChar(15) Sales Returns Account ->OACT
  COGM_Act nVarChar(15) Cost of Goods Sold Account ->OACT
  AlocCstAct nVarChar(15) Allocation Account ->OACT
  VariancAct nVarChar(15) Variance Account ->OACT
  PricDifAct nVarChar(15) Price Difference Account ->OACT
  CDownPymnt nVarChar(15) Customer Down Payment Account ->OACT
  VDownPymnt nVarChar(15) Vendor Down Payments Account ->OACT
  CBoERcvble nVarChar(15) BoE Accounts Receivable ->OACT
  CBoEOnClct nVarChar(15) Bill of Exchange on Collection ->OACT
  CBoEPresnt nVarChar(15) Bill of Exchange Presentation ->OACT
  CBoEDiscnt nVarChar(15) Bill of Exchange Discounted ->OACT
  CUnpaidBoE nVarChar(15) Unpaid Bill of Exchange ->OACT
  VBoEPayble nVarChar(15) BoE Accounts Payable ->OACT
  VAsstBoEPy nVarChar(15) BoE Accounts Payable ->OACT
  COpenDebts nVarChar(15) Customer Doubtful Debts Acct ->OACT
  VOpenDebts nVarChar(15) Vendor Doubtful Debts Account ->OACT
  PurchseAct nVarChar(15) Purchase Account ->OACT
  PaReturnAc nVarChar(15) Purchase Return Account ->OACT
  PaOffsetAc nVarChar(15) Purchase Offset Account ->OACT
  LinkAct_28 nVarChar(15) Period-End Closing Account ->OACT
  ExDiffAct nVarChar(15) Exchange Rate Differences Account ->OACT
  BalanceAct nVarChar(15) Goods Clearing Account ->OACT
  BnkChgAct nVarChar(15) Bank Charges Account ->OACT
  LinkAct_29 nVarChar(15) Other Receivable ->OACT
  LinkAct_30 nVarChar(15) Other Payable ->OACT
  IncmAcct nVarChar(15) Default Inv Reval. Revenue ->OACT
  ExpnAcct nVarChar(15) Def. Inv. Reval. Revenue Acct ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  CostRevAct nVarChar(15) COGS Revaluation Acct ->OACT
  RepomoAct nVarChar(15) REPOMO Revaluation Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  SaleVatOff nVarChar(15) Down Payment Tax Offset Acct ->OACT
  PurcVatOff nVarChar(15) Down Payment Tax Offset Acct ->OACT
  DpmSalAct nVarChar(15) Payment Advances ->OACT
  DpmPurAct nVarChar(15) Payment Advances ->OACT
  ExpVarAct nVarChar(15) Expense and Inventory Account ->OACT
  CostOffAct nVarChar(15) COGS Revaluation Offset Acct ->OACT
  ECExepnses nVarChar(15) Expense Account - EU ->OACT
  StockAct nVarChar(15) Inventory Account ->OACT
  DflInPrcss nVarChar(15) Default for Stk Itm in Process ->OACT
  DfltInCstm nVarChar(15) Default for Stk Itm in Customs ->OACT
  DfltProfit nVarChar(15) Inventory Offset - Incr. Acct ->OACT
  DfltLoss nVarChar(15) Inventory Offset - Decr. Acct ->OACT
  VAssets nVarChar(15) Vendor Assets Account ->OACT
  StockRvAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkRvOfAct nVarChar(15) Inventory Reval. Offset Acct ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  DfltCard nVarChar(15) Invoice and Payment BP ->OCRD
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  GlRvOffAct nVarChar(15) G/L Revaluation Offset Account ->OACT
  OverpayAP nVarChar(15) Overpayment A/P Account ->OACT
  UndrpayAP nVarChar(15) Underpayment A/P Account ->OACT
  OverpayAR nVarChar(15) Overpayment A/R Account ->OACT
  UndrpayAR nVarChar(15) Underpayment A/R Account ->OACT
  ARCMAct nVarChar(15) Sales Credit Account ->OACT
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign ->OACT
  ARCMEUAct nVarChar(15) Sales Credit Account - EU ->OACT
  APCMAct nVarChar(15) Purchase Credit Account ->OACT
  APCMFrnAct nVarChar(15) Purchase Credit Acct - Foreign ->OACT
  APCMEUAct nVarChar(15) Purchase Credit Account - EU ->OACT
  NegStckAct nVarChar(15) Negative Inventory Adj. Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account ->OACT
  GLGainXdif nVarChar(15) Realized Exchange Diff. Gain ->OACT
  GLLossXdif nVarChar(15) Realized Exchange Diff. Loss ->OACT
  AmountDiff nVarChar(15) Amount Differences ->OACT
  SlfInvIncm nVarChar(15) Self Invoice Revenue Account ->OACT
  SlfInvExpn nVarChar(15) Self Invoice Expense Account ->OACT
  OnHoldAct nVarChar(15) Capital Goods On Hold Account ->OACT
  PlaAct nVarChar(15) PLA ->OACT
  ICClrAct nVarChar(15) Incoming CENVAT Clearing Acct ->OACT
  OCClrAct nVarChar(15) Outgoing CENVAT Clearing Acct ->OACT
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  SalDpmInt nVarChar(15) A/R DP Interim ->OACT
  PurDpmInt nVarChar(15) A/P DP Interim ->OACT
  ExrateOnDt nVarChar(15) Ex Rate on Def Tax Account ->OACT
  UserSign2 Int(6) Updating User ->OUSR
  EURecvAct nVarChar(15) EU Accounts Receivable ->OACT
  EUPayAct nVarChar(15) EU Accounts Payable ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  DunIntrst nVarChar(15) Dunning Interest ->OACT
  DunFee nVarChar(15) Dunning Fee ->OACT
  SnapShotId Int(11) Snapshot ID default=0
  TDSInterst nVarChar(15) TDS Interest Acct ->OACT
  TDSCharges nVarChar(15) TDS Other Charges Acct ->OACT
  SrvTaxClr nVarChar(15) Service Tax Clearing Account ->OACT
  ARConDiffG nVarChar(15) Realized Conversion Diff. Gain ->OACT
  ARConDiffL nVarChar(15) Realized Conversion Diff. Loss ->OACT
  APConDiffG nVarChar(15) Realized Conversion Diff. Gain ->OACT
  APConDiffL nVarChar(15) Realized Conversion Diff. Loss ->OACT
  GLConDiffG nVarChar(15) Realized Conversion Diff. Gain ->OACT
  GLConDiffL nVarChar(15) Realized Conversion Diff. Loss ->OACT
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account
  TDSFee nVarChar(15) TDS Fee Acct ->OACT
  ResRevenue nVarChar(15) Revenue Account ->OACT
  ResExpense nVarChar(15) Expense Account ->OACT
  ResSalesCr nVarChar(15) Sales Credit Account ->OACT
  ResPurchCr nVarChar(15) Purchase Credit Account ->OACT
  ResNotInv nVarChar(15) Res. Received Not Inv. Account ->OACT
  ResStdExp1 nVarChar(15) Std Cost Expense 1 ->OACT
  ResStdExp2 nVarChar(15) Std Cost Expense 2 ->OACT
  ResStdExp3 nVarChar(15) Std Cost Expense 3 ->OACT
  ResStdExp4 nVarChar(15) Std Cost Expense 4 ->OACT
  ResStdExp5 nVarChar(15) Std Cost Expense 5 ->OACT
  ResStdExp6 nVarChar(15) Std Cost Expense 6 ->OACT
  ResStdExp7 nVarChar(15) Std Cost Expense 7 ->OACT
  ResStdExp8 nVarChar(15) Std Cost Expense 8 ->OACT
  ResStdExp9 nVarChar(15) Std Cost Expense 9 ->OACT
  ResStdEx10 nVarChar(15) Std Cost Expense 10 ->OACT
  ResWipAct nVarChar(15) Resource WIP Account ->OACT
  ResScrapAc nVarChar(15) Scrap Account ->OACT
  WipOffPlAc nVarChar(15) WIP Offset P&L Account ->OACT
  ResOffPlAc nVarChar(15) Resource Offset P&L Account ->OACT
  ERDInARAct nVarChar(15) Exchange Rate Interim Sales Account ->OACT
  ERDInAPAct nVarChar(15) Exchange Rate Interim Purchase Account ->OACT
  CSDInARAct nVarChar(15) Cash Discount Interim Sales Account ->OACT
  CSDInAPAct nVarChar(15) Cash Discount Interim Purchase Account ->OACT
  GSTInAct nVarChar(15) GST Input Interim Account ->OACT
  GSTInterst nVarChar(15) GST Interest Account ->OACT
  GSTCharges nVarChar(15) GST Other Charges Account ->OACT
  GSTFee nVarChar(15) GST Fee Account ->OACT
  WTInARAct nVarChar(15) Interim Account for Tax ->OACT
  WTInAPAct nVarChar(15) Interim Account for Tax ->OACT
  WTExDifAct nVarChar(15) Withholding Tax Exchange Rate Diff. Account ->OACT

# OACQ - Capitalization
Module: Finance | 44 columns | ObjType: 1470000049
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
  TRANS_TYPE: TransType, CreatedBy
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PeriodCat nVarChar(10) Period Category
  FinncPriod Int(11) Posting Period ->OFPR
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=P [P=Posted, D=Draft, C=Canceled]
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  Reference nVarChar(32) Reference
  ObjType nVarChar(20) Object Type
  Currency nVarChar(3) Currency ->OCRN
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Rate
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  TransType nVarChar(20) Original Document default=-1 [13=A/R Invoice, 19=A/P Credit Memo, 18=A/P Invoice, 46=Outgoing Payment, 163=A/P Correction Invoice, 1470000049=Capitalization, 1470000060=Fixed Assets Credit Memo, -1=All Transactions, 1470000075=Manual Depreciation, 1470000090=Fixed Assets Transfer, 1470000094=Retirement]
  CreatedBy Int(11) Original
  JrnlMemo nVarChar(254) Journal Remarks
  AssetDate Date(8) Asset Value Date
  CurSource VarChar(1) Base Currency default=L [L=Local Currency, S=System Currency, F=Foreign Currency]
  DocType nVarChar(15) Document Type default=PL [PL=Ordinary Depreciation, UP=Unplanned Depreciation, SD=Special Depreciation, AP=Appreciation, TR=Asset Transfer, NC=Sales, SC=Scrapping, TC=Asset Class Transfer]
  PrjSmarz VarChar(1) Summarize by Project default=N [Y=Yes, N=No]
  DstRlSmarz VarChar(1) Summarize by Distribution Rule default=N [Y=Yes, N=No]
  ManDprType nVarChar(15) Manual Depreciation Type ->ODTP
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  DprArea nVarChar(15) Depreciation Area ->ODPA
  BPLId Int(11) Branch ->OBPL
  BaseRef nVarChar(11) Base Reference
  LVARetire VarChar(1) Low Value Asset Retirement default=N [Y=Yes, N=No]
  CancelOpt Int(6) Cancelation Option default=1
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  GdsMovType nVarChar(2) Goods Movement Type [SI=Opening Balance of Fixed Assets, IM=Initialization of Fixed Assets, IP=FA Use in Progress, CI=End of Fixed Assets Use, MC=Immobilization from Current Assets]

# OACR - Accrual Type
Module: Finance | 8 columns | ObjType: 540000048
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Accrual Type Code
  Name nVarChar(30) Accrual Type Name
  PostingAct nVarChar(15) Posting Account ->OACT
  CalcAcct nVarChar(15) Calculation Account ->OACT
  InterimAct nVarChar(15) Interim Account ->OACT
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OACS - Asset Classes
Module: Finance | 14 columns | ObjType: 1470000032
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  AssetType VarChar(1) Asset Type default=G [G=General, L=Low Value Asset]
  LimitFrom Num(19,6) Value Limit From
  LimitTo Num(19,6) Value Limit To
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  BPLId Int(11) Branch ->OBPL
  AttrGrp Int(11) Attribute Group default=-1 ->OFAA
  SnapshotId Int(11) Snapshot ID default=0

# OACT - G/L Accounts
Module: Finance | 129 columns | ObjType: 1
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AcctCode
  INTER_KEY: FatherNum
  CURRENCY: ActCurr
  FORMAT: FormatCode
  COUNTER: Counter
  IDENTIFIER U: ActId
Fields (name type(len) description [values] ->parent table):
  AcctCode nVarChar(15) Account Code
  AcctName nVarChar(100) Account Name
  CurrTotal Num(19,6) Current Balance
  EndTotal Num(19,6) Opening Balance
  Finanse VarChar(1) Cash Account default=N [Y=Yes, N=No]
  Groups nVarChar(8) Main Group
  Budget VarChar(1) Budget default=N [Y=Yes, N=No]
  Frozen VarChar(1) Account on Hold [Y/N] default=N [Y=Yes, N=No]
  Free_2 VarChar(1) Free 2
  Postable VarChar(1) Account [Active/Title] default=Y [Y=Active Account, N=Title Account]
  Fixed VarChar(1) Main Account
  Levels Int(6) Account Level default=2
  ExportCode nVarChar(10) Data Export Code
  GrpLine Int(11) Serial No. in Group
  FatherNum nVarChar(15) Parent Account Key
  AccntntCod nVarChar(15) External Code
  CashBox VarChar(1) Capital Account [Y/N] default=N [Y=Yes, N=No]
  GroupMask Int(6) Group Mask default=1
  RateTrans VarChar(1) For Conversion Differences default=Y [Y=Yes, N=No]
  TaxIncome VarChar(1) Tax Definition default=N [Y=Yes, N=No]
  ExmIncome VarChar(1) Tax Definition default=N [Y=Yes, N=No]
  ExtrMatch Int(11) External Reconciliation No.
  IntrMatch Int(11) Internal Reconciliation No.
  ActType VarChar(1) Account Type default=N [I=Sales, E=Expenditure, N=Other]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  BlncTrnsfr VarChar(1) Balances Transferred [Y/N] default=N [Y=Yes, N=No]
  OverType VarChar(1) Loading Type default=N [N=None, Y=Yes]
  OverCode nVarChar(8) Loading Factor Code ->OOCR
  SysMatch Int(11) System Reconciliation No. default=-1
  PrevYear VarChar(1) There are accounts from the previous year default=N [Y=Yes, N=No]
  ActCurr nVarChar(3) Account Currency ->OCRN
  RateDifAct nVarChar(15) Rate Differences Account
  SysTotal Num(19,6) Balance in System Currency
  FcTotal Num(19,6) Balance in Account Currency
  Protected VarChar(1) Confidential Account default=N [Y=Yes, N=No]
  RealAcct VarChar(1) Indexed Account default=N [Y=Yes, N=No]
  Advance VarChar(1) Advance Payments default=Y [Y=Yes, N=No]
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  FrgnName nVarChar(100) Foreign Name
  Details nVarChar(254) Details
  ExtraSum Num(19,6) Additional Amount
  Project nVarChar(20) Project Code ->OPRJ
  RevalMatch VarChar(1) Revaluation Coordinated default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  LocMth VarChar(1) LC Reconciliation default=Y [Y=Yes, N=No]
  MTHCounter Int(11) MTH Counter
  BNKCounter Int(11) BNK Counter
  UserSign Int(6) User Signature ->OUSR
  LocManTran VarChar(1) Control Account default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=1 ->ADP1
  ValidFor VarChar(1) Active default=N [Y=Yes, N=No]
  ValidFrom Date(8) Active From
  ValidTo Date(8) Active To
  ValidComm nVarChar(30) Active Remarks
  FrozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  FrozenFrom Date(8) Inactive From
  FrozenTo Date(8) Inactive To
  FrozenComm nVarChar(30) Inactive Remarks
  Counter Int(11) Counter default=0
  Segment_0 nVarChar(20) Segment 0
  Segment_1 nVarChar(20) Segment 1
  Segment_2 nVarChar(20) Segment 2
  Segment_3 nVarChar(20) Segment 3
  Segment_4 nVarChar(20) Segment 4
  Segment_5 nVarChar(20) Segment 5
  Segment_6 nVarChar(20) Segment 6
  Segment_7 nVarChar(20) Segment 7
  Segment_8 nVarChar(20) Segment 8
  Segment_9 nVarChar(20) Segment 9
  FormatCode nVarChar(210) Format Code
  CfwRlvnt VarChar(1) Cash Flow Relevant [Y/N] default=N [Y=Yes, N=No]
  ExchRate VarChar(1) Exchange Rate Differences default=Y [Y=Yes, N=No]
  RevalAcct nVarChar(15) Revaluation Account
  LastRevBal Num(19,6) Last Revaluation Balance
  LastRevDat Date(8) Last Revaluation Date
  DfltVat nVarChar(8) Default VAT Group ->OVTG
  VatChange VarChar(1) Allow Change VAT Group default=Y [Y=Yes, N=No]
  Category Int(11) Category ->OACG
  TransCode nVarChar(4) Transaction Code ->OTRC
  OverCode5 nVarChar(8) Loading Factor Code 5 ->OOCR
  OverCode2 nVarChar(8) Loading Factor Code 2 ->OOCR
  OverCode3 nVarChar(8) Loading Factor Code 3 ->OOCR
  OverCode4 nVarChar(8) Loading Factor Code 4 ->OOCR
  DfltTax nVarChar(8) Default Tax Code ->OSTC
  TaxPostAcc VarChar(1) Default Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  AcctStrLe nVarChar(2) Account Structure Level
  MeaUnit nVarChar(10) Measurement Unit
  BalDirect nVarChar(4) Direction of Balance default=0 [0=, 1=Credit, 2=Debit]
  UserSign2 Int(6) Updating User ->OUSR
  PlngLevel nVarChar(2) B1i Info for Integration
  MultiLink VarChar(1) Allow Multiple Linking default=N [N=No, Y=Yes]
  PrjRelvnt VarChar(1) Project Relevant default=N [Y=Yes, N=No]
  Dim1Relvnt VarChar(1) Dimension 1 Relevant default=N [Y=Yes, N=No]
  Dim2Relvnt VarChar(1) Dimension 2 Relevant default=N [Y=Yes, N=No]
  Dim3Relvnt VarChar(1) Dimension 3 Relevant default=N [Y=Yes, N=No]
  Dim4Relvnt VarChar(1) Dimension 4 Relevant default=N [Y=Yes, N=No]
  Dim5Relvnt VarChar(1) Dimension 5 Relevant default=N [Y=Yes, N=No]
  AccrualTyp VarChar(1) Accrual Type default=N [N=None, P=Posting Account, C=Calculation Account, I=Calculation Interim Account]
  DatevAcct nVarChar(8) DATEV Account
  DatevAutoA VarChar(1) DATEV Automatic Account default=N [Y=Yes, N=No]
  DatevFirst VarChar(1) First Data Entry default=Y [Y=Yes, N=No]
  SnapShotId Int(11) Snapshot ID default=0
  PCN874Rpt VarChar(1) PCN 874 Report Relevant default=N [Y=Yes, N=No]
  SCAdjust VarChar(1) SC Adjustment default=N [Y=Yes, N=No]
  BPLId Int(11) Assigned Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  SubLedgerN nVarChar(60) Subledger No.
  VATRegNum nVarChar(32) VAT Reg. Number
  ActId nVarChar(210) Account Identifier
  ClosingAcc nVarChar(15) G/L Account Closing
  PurpCode nVarChar(2) Account Purpose Code [01=Contas de ativo, 02=Contas de Passivo, 03=Patrim�nio L�quido, 04=Contas de Resultado, 05=Contas de Compensa��o, 09=Outras]
  RefCode nVarChar(30) Referential Account Code
  BlocManPos VarChar(1) Block Manual Posting default=N [Y=Yes, N=No]
  PriAccCode nVarChar(15) Primary Closing Account ->OACT
  CstAccOnly VarChar(1) Cost Account Only default=N [Y=YES, N=NO]
  AlloweFrom Num(19,6) Account Balance Allowed From
  AllowedTo Num(19,6) Account Balance Allowed To
  BalanceA VarChar(1) Account Balance Allowed default=N [N=NO, Y=YES]
  RmrkTmpt Int(11) Remark Text Template ->OTTR
  CemRelvnt VarChar(1) Cost Element Relevant default=N [Y=Yes, N=No]
  CemCode nVarChar(20) Cost Element Code ->OCEM
  StdActCode nVarChar(35) Standard Account Code
  TaxonCode nVarChar(15) Taxonomy Code
  InClassTyp Int(11) Income Class. Type ->OICP
  InClassCat Int(11) Income Class. Category ->OICC
  ExClassTyp Int(11) Expense Class. Type ->OECP
  ExClassCat Int(11) Expense Class. Category ->OECC

# OADG - Depreciation Groups
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  Group nVarChar(15) Depreciation Group

# OADT - Fixed Assets Account Determination
Module: Finance | 29 columns | ObjType: 1470000002
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  BalanceAct nVarChar(15) Asset Balance Sheet Account ->OACT
  ClrAcqAct nVarChar(15) Acquisition Clearing Account ->OACT
  RevResvAct nVarChar(15) Revaluation Reserve ->OACT
  OrdDprAct nVarChar(15) Ordinary Depreciation ->OACT
  OrdDprAcc nVarChar(15) Accumulated Ordinary Depr. ->OACT
  UnpDprAct nVarChar(15) Unplanned Depreciation ->OACT
  UnpDprAcc nVarChar(15) Accumulated Unplanned Depr. ->OACT
  SpDprAct nVarChar(15) Special Depreciation ->OACT
  SpDprAcc nVarChar(15) Accumulated Special Depr. ->OACT
  SaRevNAct nVarChar(15) Revenue from Asset Sales (Net) ->OACT
  ReExpNAct nVarChar(15) Retirement with Expense (Net) ->OACT
  ReRevNAct nVarChar(15) Retirement with Revenue (Net) ->OACT
  ReNBVeAct nVarChar(15) NBV Retirement Expense (Gross) ->OACT
  ReNBVrAct nVarChar(15) NBV Retirement Revenue (Gross) ->OACT
  ClrDscAct nVarChar(15) Cash Discount Clearing Account ->OACT
  RevReAct nVarChar(15) Revenue Account for Retirement ->OACT
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  ClearAccRe nVarChar(15) Revenue Clearing Account ->OACT
  RevResvClr nVarChar(15) Revaluation Reserve Clearing ->OACT
  SnapshotId Int(11) Snapshot ID default=0
  RevAct nVarChar(15) Revaluation Account ->OACT
  RevLossAct nVarChar(15) Revaluation Loss ->OACT

# OAGS - Asset Groups
Module: Finance | 2 columns | ObjType: 1470000046
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description

# OASC - Account Segmentation Categories
Module: Finance | 5 columns | ObjType: 143
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SegmentId, Code
Fields (name type(len) description [values] ->parent table):
  SegmentId Int(6) Segment ID ->OASG
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  ShortName nVarChar(10) Short Name
  UserSign Int(6) User Signature ->OUSR

# OASG - Account Segmentation
Module: Finance | 5 columns | ObjType: 142
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(6) Numerator
  Name nVarChar(100) Name
  Size Int(6) Size
  Type VarChar(1) Type default=A [A=Alphanumeric, N=Numeric]
  UserSign Int(6) User Signature ->OUSR

# OBGD - Budget Cost Assess. Mthd
Module: Finance | 17 columns | ObjType: 78
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BgdCode
  NAME U: BgdName
Fields (name type(len) description [values] ->parent table):
  BgdCode Int(11) Division Code
  BgdName nVarChar(30) Description
  BgdTotal Num(19,6) Budget Amount
  Month1 Num(19,6) January
  Month2 Num(19,6) February
  Month3 Num(19,6) March
  Month4 Num(19,6) April
  Month5 Num(19,6) May
  Month6 Num(19,6) June
  Month7 Num(19,6) July
  Month8 Num(19,6) August
  Month9 Num(19,6) September
  Month10 Num(19,6) October
  Month11 Num(19,6) November
  Month12 Num(19,6) December
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OBGS - Budget Scenario
Module: Finance | 16 columns | ObjType: 91
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  SECOND U: Name, FinancYear
  INTER_KEY: BaseId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Name nVarChar(100) Name
  BaseId Int(11) Basic Budget
  InitRate Num(19,6) Initial Ratio Percentage
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  FinancYear Date(8) Start of Fiscal Year
  IsMain VarChar(1) Main default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  RoundSys Int(6) Rounding Method default=0 [0=No Rounding, 1=Round to Full Decimal Amount, 2=Round to Full Amount, 3=Round to Full Tens Amount]
  UserSign Int(6) User Signature ->OUSR
  OcrCode nVarChar(8) Dimension 1 ->OOCR
  OcrCode2 nVarChar(8) Dimension 2 ->OOCR
  OcrCode3 nVarChar(8) Dimension 3 ->OOCR
  OcrCode4 nVarChar(8) Dimension 4 ->OOCR
  OcrCode5 nVarChar(8) Dimension 5 ->OOCR
  PrjCode nVarChar(20) Project Code ->OPRJ

# OBGT - Budget
Module: Finance | 25 columns | ObjType: 77
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  ACCNT_CODE U: AcctCode, FinancYear, Instance
  INTER_KEY: FatherCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  AcctCode nVarChar(15) Account Code
  BgdCode Int(11) Division Code ->OBGD
  FatherCode nVarChar(15) Parent Account Key
  FthrPrcnt Num(19,6) Parent Acct %
  DebLTotal Num(19,6) Total Annual Budget - Debit (LC)
  CredLTotal Num(19,6) Total Annual Budget - Credit (LC)
  DebSTotal Num(19,6) Total Annual Budget - Debit (SC)
  CredSTotal Num(19,6) Total Annual Budget - Credit (SC)
  DebRLTotal Num(19,6) Budget Balance - Debit (LC)
  CrdRLTotal Num(19,6) Budget Balance - Credit (LC)
  DebRSTotal Num(19,6) Budget Balance - Debit (SC)
  CrdRSTotal Num(19,6) Budget Balance - Credit (SC)
  FtrIDRLSum Num(19,6) Future Annual Revenues - Debit (LC)
  FtrIDRSSum Num(19,6) Future Annual Revenues - Credit (SC)
  FtrICRLSum Num(19,6) Future Revenues - Debit (LC)
  FtrICRSSum Num(19,6) Future Revenues - Debit (SC)
  FtrODRLSum Num(19,6) Future Annual Expenses - Credit (LC)
  FtrOCRLSum Num(19,6) Future Annual Expenses - Debit (LC)
  FtrODRSSum Num(19,6) Future Annual Expenses - Credit (SC)
  FtrOCRSSum Num(19,6) Future Annual Expenses - Debit (SC)
  FinancYear Date(8) Start of Fiscal Year
  Instance Int(11) Instance default=1 ->OBGS
  UserSign Int(6) User Signature ->OUSR
  SCNCounter Int(6) SCN Counter

# OBOS - Box Set Definition
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  EFFEC_DATE: EffecDate
  BZKEY U: EffecDate, ReportType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  IsUsed VarChar(1) Is Set Used default=N [Y=Yes, N=No]
  EffecDate Date(8) Effective From
  FileFmtCo Int(11) File Format Code ->OLLF
  IsDeleted VarChar(1) Is Set Deleted default=N [Y=Yes, N=No]
  ReportType VarChar(1) Report Type default=S [B=Box Declaration, S=BAS Report]

# OBOX - Box Definition
Module: Finance | 16 columns | ObjType: 216
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BoxCode, ReportType, BosCode
Fields (name type(len) description [values] ->parent table):
  BoxCode nVarChar(30) Code
  BoxName nVarChar(250) Name
  BoxType VarChar(1) Type default=V [V=VAT Group, B=Box, A=Account, M=Manual Input, T=Manual Text Input, F=Formula, S=Single Choice]
  SummayFld VarChar(1) Summary Field default=S [B=Base Amount, T=Tax Amount, Q=EQ Base Amount, E=EQ Tax Amount, N=Non-Deductible Amount, S=]
  DbtCrdt VarChar(1) Debit/Credit default=S [D=Debit Side, C=Credit Side, B=Debit Side and Credit Side, S=]
  Formula nVarChar(250) Formula Syntax
  SortOrder Int(11) Sort Order
  AbsolutVa VarChar(1) Absolute Value default=N [Y=Yes, N=No]
  ReportType VarChar(1) Report Type default=B [B=Box Declaration, S=BAS Report, X=BAS Report - Empty Effective Date Holder]
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  EffecDate Date(8) Effective From
  DecLoc VarChar(1) Declaration Location default=B [B=, C=Continent, M=Madeira, A=Azores]
  BosCode Int(11) Box Set Code ->OBOS
  Position nVarChar(250) Position in Report
  PostToAct nVarChar(15) Post-To Account ->OACT
  PostToOffA nVarChar(15) Post-To Offset Account ->OACT

# OBTD - Journal Vouchers List
Module: Finance | 10 columns | ObjType: 29
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BatchNum
  STATUS: Status
Fields (name type(len) description [values] ->parent table):
  BatchNum Int(11) Journal Voucher No.
  Status VarChar(1) Open/Closed Document default=O [O=Open, C=Closed]
  NumOfTrans Int(6) No. of Transactions
  DateID Date(8) Posting Date
  LocTotal Num(19,6) Total (LC)
  FcTotal Num(19,6) Total (FC)
  SysTotal Num(19,6) Total (SC)
  MemoID nVarChar(50) Details
  UserSign Int(6) User Signature ->OUSR
  Remarks nVarChar(50) Journal Voucher Remarks Field

# OBTF - Journal Voucher Entry
Module: Finance | 113 columns | ObjType: 28
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BatchNum, TransId
  TRANS_TYPE: TransType, CreatedBy
  JDT_NUM: TransId
  BTF_STATUS: BtfStatus
Fields (name type(len) description [values] ->parent table):
  BatchNum Int(11) Journal Voucher No. ->OBTD
  TransId Int(11) Transaction Number
  BtfStatus VarChar(1) Status default=O [O=Open, C=Closed]
  TransType nVarChar(20) Origin default=-1 [16=Returns, 203=A/R Down Payment, 15=Delivery, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt PO, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 281=A/P Tax Invoice, 69=Landed Costs, 140000009=Outgoing Excise Invoice, 140000010=Incoming Excise Invoice, 254000065=Self Invoice, 254000066=Self Credit Memo, 10000079=TDS Adjustment, 24=Incoming Payment, 25=Deposit, 46=Vendor Payment, 57=Checks for Payment, 76=Postdated Deposit, 182=BoE Transaction, -2=Opening Balance, -3=Closing Balance, 321=Internal Reconciliation, 10000046=Data Archive, 30=Journal Entry, 58=Inventory List, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, 68=Work Instructions, 162=Inventory Valuation, 202=Production Order, 1470000049=Fixed Asset Capitalization, 1470000060=Fixed Asset Capitalization Credit Memo, 1470000094=Fixed Asset Retirement, 1470000075=Fixed Asset Manual Depreciation, 1470000090=Fixed Asset Transfer, 1470000085=Fixed Asset Revaluation, -1=All Transactions, 310000001=Inventory Opening Balance, 10000071=Inventory Posting, 254000061=Input Service Distribution Invoice, 254000062=Input Service Distribution Recipient Invoice, 254000063=Input Service Distribution Credit Memo, 254000064=Input Service Distribution Recipient Credit Memo, -4=Adj. for Manual Ext. Reconciliation]
  BaseRef nVarChar(11) Origin No.
  RefDate Date(8) Posting Date
  Memo nVarChar(254) Remarks
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  CreatedBy Int(11) Origin
  LocTotal Num(19,6) Total in Local Currency
  FcTotal Num(19,6) Total in Foreign Currency
  SysTotal Num(19,6) Total in System Currency
  TransCode nVarChar(4) Transaction Code ->OTRC
  OrignCurr nVarChar(3) Original Currency ->OCRN
  TransRate Num(19,6) Transaction Rate
  BtfLine Int(11) Row in Voucher
  TransCurr nVarChar(3) Transaction Currency
  Project nVarChar(20) Project Code ->OPRJ
  DueDate Date(8) Value Date
  TaxDate Date(8) Tax Date
  PCAddition VarChar(1) PC Addition default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UpdateDate Date(8) Update Date
  CreateDate Date(8) Recording Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  RefndRprt VarChar(1) Repayment Report default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  Indicator nVarChar(2) Indicator Code ->OIDC
  AdjTran VarChar(1) Adjusting Transaction default=N [Y=Yes, N=No]
  RevSource VarChar(1) Revaluation Source default=N [F=FC, S=System, N=No]
  StornoDate Date(8) Reversal Date
  StornoToTr Int(11) Reverse Transaction
  AutoStorno VarChar(1) Use Auto-Reverse default=N [Y=Yes, N=No]
  Corisptivi VarChar(1) Transaction Values default=N [Y=Yes, N=No]
  VatDate Date(8) VAT Date
  StampTax VarChar(1) Stamp Tax default=N [Y=Yes, N=No]
  Series Int(11) Series default=0
  Number Int(11) Number
  AutoVAT VarChar(1) Automatic Tax default=N [Y=Yes, N=No]
  DocSeries Int(11) Document Series
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  CreateTime Int(6) Generation Time
  BlockDunn VarChar(1) Block Dunning Letter default=N [N=No, Y=Yes]
  ReportEU VarChar(1) Include in EU Report default=N [Y=VAT, N=No]
  Report347 VarChar(1) Include in 347 Report default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  DocType nVarChar(60) Transact. Type ->OJET
  AttNum Int(11) Number of Attachments default=0
  GenRegNo VarChar(1) Generate Reg. No. or Not default=N [Y=Yes, N=No]
  RG23APart2 Int(11) RG23A Part2 No
  RG23CPart2 Int(11) RG23C Part2 No
  MatType Int(11) Material Type
  Creator nVarChar(155) Creator Name
  Approver nVarChar(155) Approver Name
  Location Int(11) Loc. ->OLCT
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  AutoWT VarChar(1) Automatic WTax default=N [Y=Yes, N=No]
  WTSum Num(19,6) WTax Amount
  WTSumSC Num(19,6) WTax Amount (SC)
  WTSumFC Num(19,6) WTax Amount (FC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedS Num(19,6) Applied WTax (SC)
  WTAppliedF Num(19,6) Applied WTax (FC)
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseVtAt Num(19,6) WTax Base VAT Amount
  BaseVtAtSC Num(19,6) WTax Base VAT Amount (SC)
  BaseVtAtFC Num(19,6) WTax Base VAT Amount (FC)
  VersionNum nVarChar(13) Version Number
  BaseTrans Int(11) Base Transaction Number
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Country/Region of Residence, 5=Certificate of Fiscal Residence, 6=Other Document]
  OperatCode VarChar(1) Operation Code [A=Summary Invoices Entry, B=Summary Receipts Entry, C=Invoice with Several VAT Rates, D=Correction Invoice, E=Due VAT Pending Invoice Issuance, F=Expenses Incurred by Travel Agent for Customers, G=Special Regulation for VAT Group, H=Special Regulation for Gold Investment, I=Reverse Charge Procedure, J=Unsummarized Receipts, K=Identification of Error Transactions, X=Transactions with Entrepreneurs Issuing Receipts for Agricultural Compensation, N=Service Invoicing by Travel Agencies on Behalf of Third Parties, R=Business Office Rental, S=Subsidies, T=Incoming Payments for Industrial and Intellectual Property Rights, U=Insurance Transactions, V=Purchases from Travel Agencies, W=Transactions Subject to Production, Service, and Import Taxes in Ceuta and Melilla]
  Ref3 nVarChar(100) Reference 3
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  SupplCode nVarChar(254) Supplementary Code
  SPSrcType Int(11) Service Posting Source Type
  SPSrcID Int(11) Service Posting Source ID
  SPSrcDLN Int(11) Service Post. Source Delivery
  DeferedTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  AgrNo Int(11) Blanket Agreement Number ->OOAT
  SeqNum Int(11) Sequence Number
  ECDPosTyp VarChar(1) ECD Posting Type default=N [N=Normal, E=Statement]
  RptPeriod nVarChar(5) Reporting Period
  RptMonth Date(8) Reporting Month
  ExTransId Int(11) Exposed Transaction ID
  PrlLinked VarChar(1) Is JE linked by MX Payroll default=N [Y=Yes, N=No]
  PTICode nVarChar(5) POI Code
  Letter VarChar(1) Letter
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  IsCoEntry VarChar(1) Cost Center Transfer form default=N [Y=Yes, N=No]
  SAPPassprt Text(16) Extended SAP Passport
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachment
  EBookable VarChar(1) E-Books Enabled default=N [N=No, Y=Yes]
  DataVers Int(11) Data Version default=1

# OCCT - Cost Center Type
Module: Finance | 4 columns | ObjType: 540000042
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CctCode
Fields (name type(len) description [values] ->parent table):
  CctCode nVarChar(8) Cost Center Type Code
  CctName nVarChar(30) Cost Center Type Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OCDC - Cash Discount
Module: Finance | 7 columns | ObjType: 133
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Cash Discount Code
  TableDesc nVarChar(100) Cash Discount Name
  ByDate VarChar(1) By Date default=N [Y=Yes, N=No]
  Freight VarChar(1) Freight default=N [Y=Yes, N=]
  Tax VarChar(1) Tax default=N [Y=Yes, N=No]
  VatCrctn VarChar(1) VAT Correction default=N [Y=Yes, N=No]
  BaseDate VarChar(1) Base Date default=P [P=Posting Date, S=System Date, T=Document Date, C=Closing Date]

# OCFH - Cash Flow Statement History
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CFHId
Fields (name type(len) description [values] ->parent table):
  CFHId Int(11) Cash Flow History Identity
  CFHName nVarChar(100) Saved Cash Flow Name
  UserSign Int(6) User Signature ->OUSR
  UserName nVarChar(30) User Name
  CreateDate Date(8) Recording Date
  StartDate Date(8) Start Date
  EndDate Date(8) End Date

# OCFL - Cash Flow Additional Trans.
Module: Finance | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, UserId
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  DateID Date(8) Date
  Dscription nVarChar(50) Description
  Project nVarChar(20) Project Code
  Credit Num(19,6) Incoming Total
  CredCur nVarChar(3) Entrance Currency
  Debit Num(19,6) Outgoing Amount
  DebCur nVarChar(3) Issue Currency
  SecLevel Int(6) Security Level default=1 [1=Cash Account, 5=Credit, 2=Checks, 3=Customer Liabilities, 6=Bill of Exchange, 4=Payable to Vendors, 7=Customer Forecast, 8=Vendor Forecast]
  UserId Int(6) User ID
  Frequency VarChar(1) Frequency default=O [D=Daily, W=Weekly, M=Monthly, Q=Quarterly, S=Semiannually, A=Annually, O=One Time]
  Remind Int(6) Subfrequency default=-1 [-1=, 1=On Sunday, 2=On Monday, 3=On Tuesday, 4=On Wednesday, 5=On Thursday, 6=On Friday, 7=On Saturday, 101=Every 1, 102=Every 2, 103=Every 3, 104=Every 4, 105=Every 5, 106=Every 6, 107=Every 7, 108=Every 8, 109=Every 9, 110=Every 10, 115=Every 15, 130=Every 30, 145=Every 45, 160=Every 60, 1001=On 1, 1002=On 2, 1003=On 3, 1004=On 4, 1005=On 5, 1006=On 6, 1007=On 7, 1008=On 8, 1009=On 9, 1010=On 10, 1011=On 11, 1012=On 12, 1013=On 13, 1014=On 14, 1015=On 15, 1016=On 16, 1017=On 17, 1018=On 18, 1019=On 19, 1020=On 20, 1021=On 21, 1022=On 22, 1023=On 23, 1024=On 24, 1025=On 25, 1026=On 26, 1027=On 27, 1028=On 28, 1029=On 29, 1030=On 30, 1031=On 31]
  EndDate Date(8) Execution End Date
  OcrCode nVarChar(8) Distribution Rule 1 ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR

# OCFT - Cash Flow Transactions - Rows
Module: Finance | 20 columns | ObjType: 241
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CFTId
Fields (name type(len) description [values] ->parent table):
  CFTId Int(11) Cash Flow Transaction ID
  CFWId Int(11) Cash Flow Line Item ID ->OCFW
  Debit Num(19,6) Debit Amount
  Credit Num(19,6) Credit Amount
  SysCredit Num(19,6) System Credit Amount
  SysDebit Num(19,6) System Debit Amount
  FCDebit Num(19,6) FC Debit Amount
  FCCredit Num(19,6) FC Credit Amount
  FCCurrency nVarChar(3) Foreign Currency
  Account nVarChar(15) Account Code ->OACT
  BatchNum Int(11) Batch No.
  JDTId Int(11) Journal Entry ID
  JDTLineId Int(11) Journal Entry Line ID
  TransType nVarChar(20) Source Object [24=Incoming Payment, 46=Vendor Payment, 30=Journal Entry, 140=Payment Draft, 29=Journal Vouchers List, 25=Deposit, 76=Postdated Check Deposit, 182=Bill of Exchange Transaction, 42=Bank Statement, 157=Payment Wizard]
  BaseRef nVarChar(11) Base Reference
  PaymentMen nVarChar(11) Payment Means
  PaymentRef nVarChar(11) Payment Reference
  PostDate Date(8) Posting Date
  ValueDate Date(8) Value Date
  Status VarChar(1) Status

# OCFW - Cash Flow Line Item
Module: Finance | 14 columns | ObjType: 242
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CFWId
  INTER_KEY: FatherNum
  INDEX_KEY U: CFWName
Fields (name type(len) description [values] ->parent table):
  CFWId Int(11) Cash Flow Line Item ID
  CFWName nVarChar(100) Cash Flow Line Item Name
  LineNum nVarChar(5) Cash Flow Line No.
  Postable VarChar(1) Cash Flow Item [Active/Title] default=Y [Y=Active Item, N=Header Item]
  FatherNum Int(11) Parent Item Key ->OCFW
  Levels Int(6) Cash Flow Item Level default=3
  GroupMask Int(6) Group Mask default=1
  GroupLine Int(11) Serial No. in Group
  ExtrMatch Int(11) External Reconciliation No.
  IntrMatch Int(11) Internal Reconciliation No.
  RateDifCFW Int(11) Rate Differences CFW
  DataSource Int(6) Data Source
  Attr Int(6) Attribute
  Direction Int(6) Direction

# OCIG - CIG Codes
Module: Finance | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(10) Contract Code Identification

# OCUP - CUP Codes
Module: Finance | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(15) Unique Code of Project

# ODDG - Withholding Tax Deduction Groups
Module: Finance | 6 columns | ObjType: 117
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Numerator
  NAME U: DdgCode, DdgName
Fields (name type(len) description [values] ->parent table):
  Numerator Int(11) Group Key
  DdgCode nVarChar(2) Group Code ->ODGL
  DdgName nVarChar(30) Group Name
  DdctPrcnt Num(19,6) Max. Red. in %
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# ODGL - Deduction Group List
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
Fields (name type(len) description [values] ->parent table):
  GroupCode nVarChar(2) Group Code
  GroupName nVarChar(100) Group Name
  UserSign Int(6) User Signature

# ODIM - Cost Accounting Dimension
Module: Finance | 4 columns | ObjType: 251
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DimCode
  DIM_KEY: DimName
Fields (name type(len) description [values] ->parent table):
  DimCode Int(6) Dimension Code
  DimName nVarChar(15) Dimension Name
  DimActive VarChar(1) Activated? [Y/N] default=N [Y=Yes, N=No]
  DimDesc nVarChar(50) Dimension Description

# ODMC - G/L Account Determination Criteria - Inventory
Module: Finance | 10 columns | ObjType: 1470000048
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DmcId
Fields (name type(len) description [values] ->parent table):
  DmcId Int(6) Determination ID
  DmcAlias nVarChar(100) Determination Alias
  Active VarChar(1) Determination Status default=N [Y=Yes, N=No]
  Priority Int(6) Determination Priority
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  AdvRulCol Int(6) Advanced Rules Column
  IsUDF VarChar(1) Is User Defined Field default=N [Y=Yes, N=No]

# ODPA - Fixed Asset Depreciation Areas
Module: Finance | 20 columns | ObjType: 1470000003
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  DirectDpr VarChar(1) Direct Depreciation default=D [D=Direct Posting, I=Indirect Posting]
  RetMeth VarChar(1) Retirement Method default=G [G=Gross, N=Net]
  AreaType VarChar(1) Area Type default=O [L=Posting to G/L, O=Additional Area, D=Derived Area]
  DrvdArea nVarChar(15) Derived Area ->ODPA
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  MainArea VarChar(1) Main Booking Area default=N [Y=Yes, N=No]
  CreditCtrl VarChar(1) Tax Credit Control default=N [Y=Yes, N=No]
  TaxType Int(11) Tax Type ->OSTT
  DirRevPost VarChar(1) Direct Revenue Posting default=N [Y=Yes, N=No]
  SnapshotId Int(11) Snapshot ID default=0
  BpTaxCorr nVarChar(15) BP for Tax Correction ->OCRD
  ItmTaxCorr nVarChar(50) Item for Tax Correction ->OITM
  UsgTaxCorr Int(11) Usage for Tax Correction ->OUSG

# ODPP - Depreciation Type Pools
Module: Finance | 2 columns | ObjType: 1470000004
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Code
  Descr nVarChar(100) Description

# ODPV - Fixed Assets Depreciation Value
Module: Finance | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: ItemCode, DprArea, PeriodCat, SubPeriod
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ID ->ODPA
  PeriodCat nVarChar(10) Period Category
  FromDate Date(8) Period Start Date
  ToDate Date(8) Period To Date
  OrdDprPlan Num(19,6) Ordinary Depreciation Plan
  OrdDprPost Num(19,6) Ordinary Depreciation Posted
  OrdDprAct Num(19,6) Ordinary Depreciation Actual
  SpDprKey nVarChar(2) Special Depreciation Key ->ODPP
  SpDprPlan Num(19,6) Special Depreciation Plan
  SpDprPost Num(19,6) Special Depreciation Posted
  SpDprAct Num(19,6) Special Depreciation Actual
  SubPeriod Int(11) Sub-period
  OrdDprPln1 Num(19,6) Ordinary Depreciation Plan 1
  OrdDprPst1 Num(19,6) Ordinary Depreciation Posted 1
  OrdDprAct1 Num(19,6) Ordinary Depreciation Actual 1

# ODRN - Depreciation Run
Module: Finance | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  DprArea nVarChar(15) Depreciation Area ID ->ODPA
  Status VarChar(1) Status default=D [S=Depreciation Posted, N=No Depreciation Posted, C=Canceled, F=Failed, D=]
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  RefDate Date(8) Posting Date
  PeriodCat nVarChar(10) Period Category ID
  PostPeriod Int(11) Posting Subperiod
  KeyDate Date(8) Key Date
  Remarks nVarChar(32) Remarks
  NumOfJEs Int(11) No. of Journal Entries
  SumOfDpr Num(19,6) Sum of Depreciation
  SumByPro VarChar(1) Summarize by Project default=N [Y=Yes, N=No]
  SumByDistr VarChar(1) Summarize by Distribution Rule default=N [Y=Yes, N=No]
  TransType nVarChar(20) Generate Document default=-1 [-1=None, 18=A/P Invoice]
  TransAbs Int(11) Generate Doc. Abs. Entry

# ODTP - Fixed Assets Depreciation Types
Module: Finance | 51 columns | ObjType: 1470000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(15) Code
  Descr nVarChar(100) Description
  DprMeth nVarChar(2) Depreciation Method default=NO [NO=No Depreciation, SL=Straight Line, SP=Straight Line Period Control, DB=Declining Balance, ML=Multilevel, WO=Immediate Write-Off, SD=Special Depreciation, MD=Manual Depreciation, CF=Accelerated]
  DprTo Num(19,6) Minimum Depreciated Value
  Rounding VarChar(1) Round Year End Book Value default=Y [Y=Yes, N=No]
  InclSalv VarChar(1) Include Salvage Value in Depr. default=N [Y=Yes, N=No]
  SalvPerc Num(19,6) Percentage for Salvage Value
  PerAcq nVarChar(2) Period Control for Acquisition default=PR [PR=Pro Rata Temporis, HY=First Year Convention, 6M=Half Year, FY=Full Year]
  PerSubAcq nVarChar(2) Period Control Subacquisition default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, FY=Full Year]
  PerRet nVarChar(2) Period Control for Retirement default=PR [PR=Pro Rata Temporis, YR=Half Year Convention, EL=After End of Useful Life]
  AcqPRTyp nVarChar(3) Type of PRT for Acquisition default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]
  SubPRTyp nVarChar(3) Type of PR for Subacquisition default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]
  RetPRTyp nVarChar(3) Type of PR for Retirement default=EDB [EDB=Exact Daily Base, LPP=Last Day of Prior Period, LCP=Last Day of Current Period]
  PerDpRev Num(19,6) Depreciation to Be Reversed %
  ValidFrom Date(8) Valid From default=19000101
  ValidTo Date(8) Valid To default=20991231
  sCalcMeth nVarChar(3) Calc. Method for Straight Line default=APC [APC=Acquisition Value/Total Useful Life, PRC=Percentage of Acquisition Value, NBV=Net Book Value/Remaining Life]
  sPercent Num(19,6) Percentage for Straight Line
  dBase nVarChar(3) Base for Declining Balance default=NBV [NBV=Net Book Value]
  dPercent Num(19,6) Percentage for Decl. Balance
  dFactor Num(19,6) Factor for Declining Balance default=1
  dAltDprTyp nVarChar(15) Auto. Change Depreciation Type ->ODTP
  maDecBase VarChar(1) Reduce Depreciation Base default=Y [Y=Yes, N=No]
  spMeth VarChar(1) Calc. Method for Special Depr. default=D [D=Additional, A=Alternative]
  spConcPer Int(11) Concession Period in Years
  spMaxPerc Num(19,6) Maximum Percentage
  spAdDpr nVarChar(15) Normal Depreciation ->ODTP
  spAlDpr nVarChar(15) Alternative Depreciation ->ODTP
  PoolID nVarChar(2) Depreciation Type Pool ID ->ODPP
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  DprPer VarChar(1) Depreciation Periods default=S [S=Standard, I=Individual, U=Individual Usage]
  PerFactor Num(19,6) Period Factor default=1
  spMaxAmnt Num(19,6) Maximum Amount
  spMaxFlag VarChar(1) Max. [Percentage\Amount] default=P [P=Percentage, A=Amount]
  CalcBase VarChar(1) Calculation Base default=Y [Y=Yearly, M=Monthly]
  DeprEndLFY VarChar(1) Depr. End at Last Full Year default=N [Y=Yes, N=No]
  AccuPriorP VarChar(1) Accu. Depr. of Prior Periods default=N [Y=Yes, N=No]
  DeltaCoeff Int(11) Delta Coefficient default=0
  MaxDepr Num(19,6) Maximum Depreciable Value
  FactorFFY VarChar(1) Factor Only Relevant to FFY default=N [Y=Yes, N=No]
  SnapshotId Int(11) Snapshot ID default=0
  PerTranSou nVarChar(2) Period Control Transfer Source default=PR [PR=Pro Rata Temporis]
  PerTranTar nVarChar(2) Period Control Transfer Target default=PR [PR=Pro Rata Temporis]
  TranSPRTyp nVarChar(3) Type of PR for Transfer Source default=EDB [EDB=Exact Daily Base, LPP=Last Day of Prior Period, LCP=Last Day of Current Period]
  TranTPRTyp nVarChar(3) Type of PR for Transfer Target default=EDB [EDB=Exact Daily Base, FCP=First Day of Current Period, FNP=First Day of Next Period]
  RoundMeth VarChar(1) Rounding Method default=N [N=Truncate to Integer, U=Round Up to Integer, D=Round Down to Integer]

# OECC - Expense Classification Category
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Code nVarChar(50) Code
  Descriptio nVarChar(254) Description

# OECP - Expense Classification Type
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Code nVarChar(50) Code
  Descriptio nVarChar(254) Description

# OEXT - Expense Types
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ExpType
Fields (name type(len) description [values] ->parent table):
  ExpType nVarChar(4) Expense Type
  ExpName nVarChar(30) Expense Name
  ExpAcct nVarChar(15) G/L Account ->OACT
  PaidByComp VarChar(1) Paid By Company default=N [Y=Yes, N=No]
  VatGroup nVarChar(8) VAT Group ->OSTC
  VatGrpEU nVarChar(8) VAT Group ->OVTG
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OFAA - Asset Attributes
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  Name U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(100) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  SnapshotId Int(11) Snapshot ID default=0

# OFAC - Fixed Asset Parameter Change
Module: Finance | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ItemCode nVarChar(50) Item No. ->OITM
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update

# OFAM - Fixed Asset Data Migration
Module: Finance | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WizardId
Fields (name type(len) description [values] ->parent table):
  WizardId Int(11) Wizard ID
  WizardName nVarChar(100) Migration Run Name
  CreateDate Date(8) Migration Run Date
  AcctDtn VarChar(1) Migrate Account Determination default=Y [Y=Yes, N=No]
  DprArea VarChar(1) Migrate Depreciation Areas default=Y [Y=Yes, N=No]
  DprType VarChar(1) Migrate Depreciation Types default=Y [Y=Yes, N=No]
  AssetClass VarChar(1) Migrate Asset Classes default=Y [Y=Yes, N=No]
  AssetNum VarChar(1) Migrate Asset Numbering default=Y [Y=Yes, N=No]
  AssetItem VarChar(1) Migrate Asset Items default=Y [Y=Yes, N=No]
  UpdExstItm VarChar(1) Overwrite Existing Data default=N [Y=Overwrite Existing Data, N=Skip if Data Already Exists]
  Status VarChar(1) Status of Migration Run default=S [S=Successful, P=Partially Successful, F=Failed]
  Remarks nVarChar(254) Remarks
  FiscalYear nVarChar(10) Migration Data to Fiscal Year

# OFAR - Fixed Asset Revaluation
Module: Finance | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PostDate Date(8) Posting Date
  AssetDate Date(8) Asset Value Date
  Ref nVarChar(32) Reference
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(254) Journal Remarks
  DprArea nVarChar(15) Depreciation Area ->ODPA
  TransId Int(11) Transaction Number ->OJDT
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocDate Date(8) Document Date
  BPLId Int(11) Branch ->OBPL
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  RevalPerc Num(19,6) Revaluation Percentage %
  IfrsPsting VarChar(1) Ifrs posting default=N [Y=Yes, N=No]

# OFIX - Fixed Asset Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY: SrcObjType, SrcObjAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type
  SrcObjAbs Int(11) Source Object Internal ID
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancellation Date

# OFPC - Fixed Assets Fiscal Year Change
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PeriodCat nVarChar(10) Period Category
  NextPeriod nVarChar(10) Change to Period

# OFPR - Posting Period
Module: Finance | 25 columns | ObjType: 111
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) System Number
  Code nVarChar(20) Period Code
  Name nVarChar(20) Period Name
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  Free2 VarChar(1) Free default=Y [Y=Yes, N=No]
  Free3 VarChar(1) Free default=N [N=Unlocked, S=Unlocked Except Sales, C=Closing Period, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  SubNum Int(11) No. of Sub-Period
  Free VarChar(1) Free
  Free1 VarChar(1) Free1
  Addition VarChar(1) Additional Sub-Periods default=N [Y=Yes, N=No]
  AddNum Int(11) No. of Additional
  Category nVarChar(10) Category ->OACP
  Indicator nVarChar(10) Period Indicator ->OPID
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  WasStatChd VarChar(1) Status Was Checked default=N [N=No, Y=Yes]
  PeriodStat VarChar(1) Period Status default=N [N=Unlocked, S=Unlocked Except Sales, C=Closing Period, Y=Locked, A=Archived]
  UserSign2 Int(6) Updating User ->OUSR

# OFRC - Financial Report Categories
Module: Finance | 87 columns | ObjType: 96
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TemplateId, CatId
Fields (name type(len) description [values] ->parent table):
  CatId Int(6) Numerator
  TemplateId Int(11) Template ->OFRT
  Name nVarChar(254) Name
  FrgnName nVarChar(254) Foreign Name
  Levels Int(6) Account Level default=1 [1=Level 1, 2=Level 2, 3=Level 3]
  FatherNum Int(6) Parent Account Key
  Active VarChar(1) Active Account default=N [Y=Yes, N=No]
  HasSons VarChar(1) Including Children default=N [Y=Yes, N=No]
  VisOrder Int(6) Display Order
  SubSum VarChar(1) Subtotal default=N [Y=Yes, N=No]
  SubName nVarChar(100) Subtotal Name
  Furmula VarChar(1) Formula default=N [Y=Yes, N=No]
  Param_1 Int(6) Parameter 1 default=0
  Param_2 Int(6) Parameter 2 default=0
  Param_3 Int(6) Parameter 3 default=0
  Param_4 Int(6) Parameter 4 default=0
  Param_5 Int(6) Parameter 5 default=0
  Param_6 Int(6) Parameter 6 default=0
  Param_7 Int(6) Parameter 7 default=0
  Param_8 Int(6) Parameter 8 default=0
  Param_9 Int(6) Parameter 9 default=0
  Param_10 Int(6) Parameter 10 default=0
  Param_11 Int(6) Parameter 11 default=0
  Param_12 Int(6) Parameter 12 default=0
  Param_13 Int(6) Parameter 13 default=0
  Param_14 Int(6) Parameter 14 default=0
  Param_15 Int(6) Parameter 15 default=0
  Param_16 Int(6) Parameter 16 default=0
  Param_17 Int(6) Parameter 17 default=0
  Param_18 Int(6) Parameter 18 default=0
  Param_19 Int(6) Parameter 19 default=0
  Param_20 Int(6) Parameter 20 default=0
  Param_21 Int(6) Parameter 21 default=0
  Param_22 Int(6) Parameter 22 default=0
  Param_23 Int(6) Parameter 23 default=0
  Param_24 Int(6) Parameter 24 default=0
  Param_25 Int(6) Parameter 25 default=0
  OP_1 VarChar(1) Operator 1 [=Without, +=Addition, -=Subtraction]
  OP_2 VarChar(1) Operator 2 [=Without, +=Addition, -=Subtraction]
  OP_3 VarChar(1) Operator 3 [=Without, +=Addition, -=Subtraction]
  OP_4 VarChar(1) Operator 4 [=Without, +=Addition, -=Subtraction]
  OP_5 VarChar(1) Operator 5 [=Without, +=Addition, -=Subtraction]
  OP_6 VarChar(1) Operator 6 [=Without, +=Addition, -=Subtraction]
  OP_7 VarChar(1) Operator 7 [=Without, +=Addition, -=Subtraction]
  OP_8 VarChar(1) Operator 8 [=Without, +=Addition, -=Subtraction]
  OP_9 VarChar(1) Operator 9 [=Without, +=Addition, -=Subtraction]
  OP_10 VarChar(1) Operator 10 [=Without, +=Addition, -=Subtraction]
  OP_11 VarChar(1) Operator 11 [=Without, +=Addition, -=Subtraction]
  OP_12 VarChar(1) Operator 12 [=Without, +=Addition, -=Subtraction]
  OP_13 VarChar(1) Operator 13 [=Without, +=Addition, -=Subtraction]
  OP_14 VarChar(1) Operator 14 [=Without, +=Addition, -=Subtraction]
  OP_15 VarChar(1) Operator 15 [=Without, +=Addition, -=Subtraction]
  OP_16 VarChar(1) Operator 16 [=Without, +=Addition, -=Subtraction]
  OP_17 VarChar(1) Operator 17 [=Without, +=Addition, -=Subtraction]
  OP_18 VarChar(1) Operator 18 [=Without, +=Addition, -=Subtraction]
  OP_19 VarChar(1) Operator 19 [=Without, +=Addition, -=Subtraction]
  OP_20 VarChar(1) Operator 20 [=Without, +=Addition, -=Subtraction]
  OP_21 VarChar(1) Operator 21 [=Without, +=Addition, -=Subtraction]
  OP_22 VarChar(1) Operator 22 [=Without, +=Addition, -=Subtraction]
  OP_23 VarChar(1) Operator 23 [=Without, +=Addition, -=Subtraction]
  OP_24 VarChar(1) Operator 24 [=Without, +=Addition, -=Subtraction]
  ProfitLoss VarChar(1) Profit and Loss default=N [Y=Yes, N=No]
  MoveNeg VarChar(1) Move if Negative default=N [Y=Yes, N=No]
  Dummy VarChar(1) Dummy Title default=N [Y=Yes, N=No]
  HideAct VarChar(1) Hide Accounts default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ToGroup Int(6) Move to Group default=0
  ToTitle Int(6) Move to Title default=0
  LineNum nVarChar(6) Line Number
  IndentChar nVarChar(6) Indent Char.
  Reversal VarChar(1) Reversal Sign default=N [N=No, Y=Yes]
  TextTitle VarChar(1) Text Title default=N [N=No, Y=Yes]
  SumType VarChar(1) Gross/Correction/Net default=N [B=Gross, C=Correction, N=Net]
  NetIncome VarChar(1) Net Income default=N [N=No, Y=Yes]
  PLTempId Int(11) Profit & Loss Report Template
  CustName VarChar(1) Customized Account Name default=N [Y=Yes, N=No]
  ExtFromBS VarChar(1) Relevant for Bal. Sht Extract default=N [Y=Yes, N=No]
  ExtData VarChar(1) Extended Data default=N [A=Relevant for Asset History Sheet, L=Relevant for Liabilities History Sheet, N=Not Relevant]
  LegalRef nVarChar(150) Legal Reference
  PLCatId Int(6) Profit & Loss Report Category default=0
  SignAggr VarChar(1) Sign for Aggregation default=E [E=, P=Positive, N=Negative]
  Mandatory VarChar(1) Mandatory default=N [Y=Yes, N=No]
  AcctReq VarChar(1) Account Verification Required default=N [Y=Yes, N=No]
  NotPermit VarChar(1) Not Permitted for Tax default=N [Y=Yes, N=No]
  KPIFactor nVarChar(3) KPI Factor No. ->OKPF
  CatCode nVarChar(15) Category Code
  CatClass VarChar(1) Category Classification [A=Asset, L=Liabilities, E=Equity, D=Expenses, R=Revenues]

# OFRT - Financial Report Templates
Module: Finance | 15 columns | ObjType: 95
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  SECOND U: DocType, Name
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Name nVarChar(100) Name
  DocType VarChar(1) Template Type default=B [B=Balance Sheet, P=Profit and Loss, C=Trial Balance, F=Statement of Cash Flows, S=Sales Unit, T=Form 6111, A=Cost Accounting, E=Asset Devalue Provision, R=Shareholder's Rights and Interests Changing, D=Profit Distribution, V=VAT Payable Detail, L=e-Balance Sheet, O=e-Profit and Loss, H=Asset History Sheet, G=Others, I=Taxable Profit and Loss, J=Appropriation of Net Profit, K=E-Asset History Sheet]
  FRTCounter Int(6) Financial Report Template Counter
  MoveChk1 VarChar(1) Move Chk1 default=N [Y=Yes, N=No]
  MoveChk2 VarChar(1) Move Chk2 default=N [Y=Yes, N=No]
  MoveTo_1 Int(6) Move To 1 default=0
  MoveTo_2 Int(6) Move To 2 default=0
  Title_1 nVarChar(100) Title 1
  Title_2 nVarChar(100) Title 2
  ShowMiss VarChar(1) Display Missing Accounts default=N [Y=Yes, N=No]
  ToTitle_1 Int(6) Move To Title 1 default=0
  ToTitle_2 Int(6) Move To Title 2 default=0
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(11) In Which Dimension ->ODIM

# OFTR - Transfer
Module: Finance | 44 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
  TRANS_TYPE: TransType, CreatedBy
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PeriodCat nVarChar(10) Period Category
  FinncPriod Int(11) Posting Period ->OFPR
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=P [P=Posted, D=Draft, C=Canceled]
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  Reference nVarChar(32) Reference
  ObjType nVarChar(20) Object Type
  Currency nVarChar(3) Currency ->OCRN
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Rate
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  TransType nVarChar(20) Original Document default=-1 [13=A/R Invoice, 19=A/P Credit Memo, 18=A/P Invoice, 46=Outgoing Payment, 163=A/P Correction Invoice, 1470000049=Capitalization, 1470000060=Fixed Assets Credit Memo, -1=All Transactions, 1470000075=Manual Depreciation, 1470000090=Fixed Assets Transfer, 1470000094=Retirement]
  CreatedBy Int(11) Original
  JrnlMemo nVarChar(254) Journal Remarks
  AssetDate Date(8) Asset Value Date
  CurSource VarChar(1) Base Currency default=L [L=Local Currency, S=System Currency, F=Foreign Currency]
  DocType nVarChar(15) Document Type default=PL [PL=Ordinary Depreciation, UP=Unplanned Depreciation, SD=Special Depreciation, AP=Appreciation, TR=Asset Transfer, NC=Sales, SC=Scrapping, TC=Asset Class Transfer]
  PrjSmarz VarChar(1) Summarize by Project default=N [Y=Yes, N=No]
  DstRlSmarz VarChar(1) Summarize by Distribution Rule default=N [Y=Yes, N=No]
  ManDprType nVarChar(15) Manual Depreciation Type ->ODTP
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  DprArea nVarChar(15) Depreciation Area ->ODPA
  BPLId Int(11) Branch ->OBPL
  BaseRef nVarChar(11) Base Reference
  LVARetire VarChar(1) Low Value Asset Retirement default=N [Y=Yes, N=No]
  CancelOpt Int(6) Cancelation Option default=1
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  GdsMovType nVarChar(2) Goods Movement Type

# OFYM - Financial Year Master
Module: Finance | 7 columns | ObjType: 10000073
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
  ASSESSYEAR U: AssessYear
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(6) Code
  Descr nVarChar(30) Description
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  AssessYear nVarChar(6) Assessment Year
  TcsAcmBase VarChar(1) TCS Accumulation Base default=I [I=Accumulation Based on Invoice, P=Accumulation Based on Payment]

# OGAR - G/L Account Advanced Rules
Module: Finance | 89 columns | ObjType: 1470000057
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PeriodCat nVarChar(10) Period Category
  FinancYear Date(8) Beginning of Financial Year
  Year Int(6) Financial Year
  PeriodName nVarChar(20) Period Name
  SubType VarChar(1) Sub-Period Type default=Y [Y=Year, Q=Quarters, M=Months, D=Days]
  PeriodNum Int(11) Number of Periods
  F_RefDate Date(8) Posting Date From
  T_RefDate Date(8) Posting Date To
  F_DueDate Date(8) Due Date From
  T_DueDate Date(8) Due Date To
  F_TaxDate Date(8) Document Date From
  T_TaxDate Date(8) Document Date To
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  ItemCode nVarChar(50) Item No. ->OITM
  ItmsGrpCod Int(6) Item Group ->OITB
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  BPGrpCod Int(6) BP Group ->OCRG
  LicTradNum nVarChar(32) Federal Tax ID default=!^| [!^|=All, !^|E=Empty, !^|F=Filled, Enter Tax ID=Enter Tax ID]
  ShipCountr nVarChar(3) Ship-to Country/Region ->OCRY
  ShipState nVarChar(3) Ship-To State ->OCST
  Comments nVarChar(254) Remarks
  CreateDate Date(8) Creation Date
  RuleCode nVarChar(20) Advanced Rule Code
  GLMethod VarChar(1) Get G/L Account By default=A [A=General, W=Warehouse, C=Item Group]
  Transfered VarChar(1) Year Transfer [Y/N] default=N [Y=Yes, N=No]
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  DfltExpn nVarChar(15) Expense Account ->OACT
  DfltIncom nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Tax Exempt Revenue Account ->OACT
  StockAct nVarChar(15) Inventory Account ->OACT
  COGM_Act nVarChar(15) Cost of Goods Sold Account ->OACT
  AlocCstAct nVarChar(15) Allocation Account ->OACT
  VariancAct nVarChar(15) Variance Account ->OACT
  PricDifAct nVarChar(15) Price Difference Account ->OACT
  NegStckAct nVarChar(15) Negative Inventory Adj. Acct ->OACT
  DfltLoss nVarChar(15) Inventory Offset - Decr. Acct ->OACT
  DfltProfit nVarChar(15) Inventory Offset - Incr. Acct ->OACT
  RturnngAct nVarChar(15) Sales Returns Account ->OACT
  ECIncome nVarChar(15) Revenue Account - EU ->OACT
  ECExepnses nVarChar(15) Expense Account - EU ->OACT
  ForgnIncm nVarChar(15) Revenue Account - Foreign ->OACT
  ForgnExpn nVarChar(15) Expense Account - Foreign ->OACT
  PurchseAct nVarChar(15) Purchase Account ->OACT
  PaReturnAc nVarChar(15) Purchase Return Account ->OACT
  PaOffsetAc nVarChar(15) Purchase Offset Account ->OACT
  ExDiffAct nVarChar(15) Exchange Rate Differences Acct ->OACT
  BalanceAct nVarChar(15) Goods Clearing Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  StockRvAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkRvOfAct nVarChar(15) Inventory Reval. Offset Acct ->OACT
  CostRevAct nVarChar(15) COGS Revaluation Acct ->OACT
  CostOffAct nVarChar(15) COGS Revaluation Offset Acct ->OACT
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account ->OACT
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  ARCMAct nVarChar(15) Sales Credit Account ->OACT
  APCMAct nVarChar(15) Purchase Credit Account ->OACT
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign ->OACT
  APCMFrnAct nVarChar(15) Purchase Credit Acct - Foreign ->OACT
  ARCMEUAct nVarChar(15) Sales Credit Account - EU ->OACT
  APCMEUAct nVarChar(15) Purchase Credit Account - EU ->OACT
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  Active VarChar(1) Is Rule Active default=Y [Y=Yes, N=No]
  CmpPrivate VarChar(1) Company/Private/Government default=A [A=All, C=Company, I=Private, G=Government]
  VatGroup nVarChar(8) Tax Definition ->OVTG
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  Usage Int(11) Usage Code for Document ->OUSG
  FreeChrgSA nVarChar(15) Free of Charge Sales Account ->OACT
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account ->OACT
  UDF1 nVarChar(254) User Defined Field 1
  UDF2 nVarChar(254) User Defined Field 2
  UDF3 nVarChar(254) User Defined Field 3
  UDF4 nVarChar(254) User Defined Field 4
  UDF5 nVarChar(254) User Defined Field 5

# OGBI - GB Interface: Common Info
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  RepNo nVarChar(20) Report Number
  RepCompany nVarChar(60) Report Company Name
  RepPeriod nVarChar(8) Report Period
  Currency nVarChar(10) Currency Unit
  UserSign Int(6) User Signature
  CreateDate nVarChar(8) Report Creation Date
  RepType Int(11) Report Type default=0 [0=, 1=Electronic Account Book, 2=G/L Account Master Records, 3=Departments, 16=Employees, 4=Business Partners, 5=Projects, 6=G/L Account Balance, 7=Accounting Vouchers, 8=Enterprise's Balance Sheet, 9=Enterprise's Profit and Loss Statement, 10=Enterprise's Cash Flow Statement, 11=Devalue Provision of Enterprise Assets, 12=Shareholder's Rights and Interests Changing Report, 13=Enterprise's Profit Distribution Report, 14=Small Enterprise's Cash Flow Statement, 15=Enterprise's VAT Payable Detail Report]
  RepEntity nVarChar(60) Report Entity

# OHSV - Hasavsevet Journal Entry
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RecordKey
Fields (name type(len) description [values] ->parent table):
  RecordKey nVarChar(7) Record Number
  Ref1 nVarChar(5) Reference 1
  Ref2 nVarChar(5) Reference 2
  RefDate nVarChar(6) Posting Date
  DueDate nVarChar(6) Due Date
  CurrCode nVarChar(3) Currency Code
  Memo nVarChar(22) Details
  DebAcct1 nVarChar(8) Debit Account 1
  CredAcct1 nVarChar(8) Credit Account 1
  DebAmnt1 nVarChar(12) Debit
  credAmnt1 nVarChar(12) Credit
  FDebAmnt1 nVarChar(12) Debit Amount 1 in FC
  FCredAmnt1 nVarChar(12) Credit in FC
  Filler nVarChar(60) Filler
  EndField nVarChar(2) Ending Field

# OICC - Income Classification Category
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Code nVarChar(50) Code
  Descriptio nVarChar(254) Description

# OICP - Income Classification Type
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Unique Entry
  Code nVarChar(50) Code
  Descriptio nVarChar(254) Description

# OIDC - Indicator
Module: Finance | 3 columns | ObjType: 138
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(2) Indicator Code
  Name nVarChar(50) Indicator Name
  UserSign Int(6) User Signature ->OUSR

# OISW - Intrastat Wizard
Module: Finance | 73 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  DeclDescr nVarChar(200) Description
  DateFrom Date(8) Starting Date of Declaration
  DateTo Date(8) Ending Date of Declaration
  RunDate Date(8) Date of Run
  ImpExpInd VarChar(1) Import Export Indicator default=I [I=Import, E=Export]
  Status VarChar(1) Status [O=Open, C=Closed, D=Deleted, A=Archived]
  MsgType Int(11) Message Type default=0 [0=New Declaration, 9=Nil Declaration, 3=Correction Declaration]
  TtlDocVal Num(19,6) Total Document Value
  DocCount Int(11) Total Number of Documents
  CompName nVarChar(100) Company Name
  CompDeclID nVarChar(32) Company Declaration ID
  CompStreet nVarChar(100) Company Street
  CompCity nVarChar(100) Company City
  CompZip nVarChar(20) Company Zip Code
  CompCntry nVarChar(3) Company Country/Region ->OCRY
  DeclCntry nVarChar(3) Declaration Country/Region ->OCRY
  CntPersID Int(11) Contact Person ID ->OHEM
  CntPerson nVarChar(250) Contact Person
  CntEmail nVarChar(100) Contact E-Mail
  CntPhone nVarChar(50) Contact Phone
  CntFax nVarChar(50) Contact Fax
  VATRegNo nVarChar(100) VAT Reg. No. of Trader
  VATRegEx nVarChar(10) VAT Reg. No. Extension
  DeclNum nVarChar(14) Sequential Declaration Number
  DeclNoEx Int(11) No. of Declaration in Period
  HeaderId Int(11) Header ID
  DeclStat VarChar(1) Declaration Status
  DeclDept Int(6) Declaring Department
  DeclCurr nVarChar(3) Declaration Currency
  ObligLvl VarChar(1) Degree of Obligation
  TaxState nVarChar(3) Federal State of Tax Office
  CustOffc nVarChar(100) Customs Registration Office
  CustOffID nVarChar(2) Customs Registration Office ID
  DeclSerNo nVarChar(3) Declaration Sequence Number
  IntCtrlRef nVarChar(99) Interchange Control Reference
  Addr1_3p nVarChar(100) Third-Party Address Part 1
  Addr2_3p nVarChar(100) Third-Party Address Part 2
  Addr3_3p nVarChar(100) Third-Party Address Part 3
  Addr4_3p nVarChar(100) Third-Party Address Part 4
  CntPers_3p nVarChar(250) Third-Party Contact Person
  CntPhon_3p nVarChar(20) Third-Party Contact Phone
  CntFax_3p nVarChar(20) Third-Party Contact Fax
  FreeTxt1 nVarChar(70) Free Text Line 1
  FreeTxt2 nVarChar(70) Free Text Line 2
  FreeTxt3 nVarChar(70) Free Text Line 3
  FreeTxt4 nVarChar(70) Free Text Line 4
  FreeTxt5 nVarChar(70) Free Text Line 5
  ValidKey nVarChar(35) Validation Key Identification
  ISDeclOffc nVarChar(10) Intrastat Declaration Office
  ReleaseVer nVarChar(13) Release Version
  UserSign Int(6) Created by User
  PosCredVal VarChar(1) Positive Credit Memo Values default=Y [Y=Yes, N=No]
  IncPrevDoc VarChar(1) Include Previous Documents [Y=Yes, N=No]
  DeclPeriod VarChar(1) Declaration Period default=M [M=Monthly, Q=Quarterly]
  Box1 Int(6) Box 1: Periodicity default=0 [0=None of the Other Cases, 8=First Month of Quarter, 9=First and Second Months of Quarter]
  Box2 Int(6) Box 2: Company Activity default=0 [0=None of the Other Cases, 7=First Declaration, 8=Stop Activity/Change of Federal Tax ID, 9=First Declaration After Federal Tax ID Change]
  GroupData VarChar(1) Group Display Data default=Y [Y=Yes, N=No]
  CstRecSt nVarChar(6) Custom Section
  TaxCodeExt nVarChar(99) Tax Code Extension
  ExportPath Text(16) Export Path
  LLEFMAbs Int(11) EFM Template ID
  SimpProc VarChar(1) Simplified Procedure [Y=Yes, N=No]
  DspNMass VarChar(1) Require All Data [Y=Yes, N=No]
  ExlDocQt VarChar(1) Exclude Docs W/ Qty Less Than [Y=Yes, N=No]
  DocQtLm Num(19,6) Document Quantity Limit
  ExlDocAm VarChar(1) Exclude Docs W/ Amt Less Than [Y=Yes, N=No]
  DocAmLm Num(19,6) Document Amount Limit
  RunTime Int(6) Time of Run
  AddonRun VarChar(1) Upgraded Add-On Run default=N [Y=Yes, N=No]
  BaseDecl Int(11) Base Declaration ->ODCI
  GroupTrans VarChar(1) Group Transactions default=N [Y=Yes, N=No]
  IncGRandDL VarChar(1) Include Goods Receipt and Deliveries default=Y [Y=Yes, N=No]

# OIWZ - Inflation Wizard
Module: Finance | 36 columns | ObjType: 195
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WizName nVarChar(100) Wizard Name
  PostDateTo Date(8) Posting Date To
  WizType VarChar(1) Wizard Type [1=G\L Account Revaluation Wizard, 2=Inventory Revaluation Wizard, 3=COGS Revaluation Wizard]
  IndexCode nVarChar(3) Index Code
  IndexRate Num(19,6) Index Rate
  CashAcct VarChar(1) Cash Account default=N [N=No, Y=Yes]
  CashFrmBl Num(19,6) Cash from Balance
  CashCancel VarChar(1) Cash Cancel default=N [N=No, Y=Yes]
  FromItem nVarChar(50) Item Number To
  ToItem nVarChar(50) Item Number To
  ItemGroup Int(6) Item Group
  Properties nVarChar(250) Item Properties
  RvalMethod VarChar(1) Inventory Revaluation Method default=P [P=Price Source, I=Inflation Only]
  PriceSour Int(6) Price Source
  TransAbs Int(11) Journal Entry Absolute Entry
  UseDLN VarChar(1) Use Delivery Notes default=Y [Y=Yes, N=No]
  UsePCH VarChar(1) Use Invoices with Stock Trans. default=Y [Y=Yes, N=No]
  UsePCHNoSt VarChar(1) Use Invoices without Trans. default=Y [Y=Yes, N=No]
  UseImport VarChar(1) Use Import Data default=N [Y=Yes, N=No]
  CashDifBal Num(19,6) Cash Acct Difference Balance
  CashExecut VarChar(1) Cash Executed default=Y [Y=Yes, N=No]
  ActType VarChar(1) Account Type default=A [A=Post amount to adjustment account, S=Post amount to inventory account]
  VarRate Num(19,6) Price Variance Rate
  FilterExe VarChar(1) Filter Executed default=Y [Y=Yes, N=No]
  CashErrRes Int(11) Cash Account Error Reason
  CshRvToAct nVarChar(15) Cash Revaluate to Account
  MarkVar VarChar(1) Mark Items with Varient Price default=N [Y=Yes, N=No]
  ChngPrice VarChar(1) Change Price default=N [Y=Yes, N=No]
  UseSemestr VarChar(1) Revaluate by Semesters Index default=N [Y=Yes, N=No]
  CreateDate Date(8) Create Date
  CshLstRvBl Num(19,6) Cash Last Revaluation Balance
  userSign Int(6) Creating User ->OUSR
  userSign2 Int(6) Updating User ->OUSR
  CshCanclD Date(8) Cash Acct Cancellation Date
  BPLId Int(11) Active Branch ->OBPL

# OJDT - Journal Entry
Module: Finance | 113 columns | ObjType: 30
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TransId
  TRANS_TYPE: TransType, CreatedBy
  REFDATE: RefDate
  STORNO_TRA: StornoToTr
  SERIES U: Series, Number
  STORNO: StornoDate, AutoStorno
Fields (name type(len) description [values] ->parent table):
  BatchNum Int(11) Journal Voucher No. ->OBTD
  TransId Int(11) Transaction Number
  BtfStatus VarChar(1) Status default=O [O=Open, C=Closed]
  TransType nVarChar(20) Origin default=-1 [16=Returns, 203=A/R Down Payment, 15=Delivery, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 132=Correction Invoice, 20=Goods Receipt PO, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 281=A/P Tax Invoice, 69=Landed Costs, 140000009=Outgoing Excise Invoice, 140000010=Incoming Excise Invoice, 254000065=Self Invoice, 254000066=Self Credit Memo, 10000079=TDS Adjustment, 24=Incoming Payment, 25=Deposit, 46=Outgoing Payment, 57=Checks for Payment, 76=Postdated Deposit, 182=BoE Transaction, -2=Opening Balance, -3=Closing Balance, 321=Internal Reconciliation, 10000046=Data Archive, 30=Journal Entry, 58=Inventory List, 59=Goods Receipt, 60=Goods Issue, 67=Inventory Transfers, 68=Work Instructions, 162=Inventory Valuation, 202=Production Order, 1470000049=Fixed Asset Capitalization, 1470000060=Fixed Asset Capitalization Credit Memo, 1470000094=Fixed Asset Retirement, 1470000075=Fixed Asset Manual Depreciation, 1470000090=Fixed Asset Transfer, 1470000085=Fixed Asset Revaluation, 1470000071=Depreciation Run, -1=All Transactions, 310000001=Inventory Opening Balance, 10000071=Inventory Posting, 254000061=Input Service Distribution Invoice, 254000062=Input Service Distribution Recipient Invoice, 254000063=Input Service Distribution Credit Memo, 254000064=Input Service Distribution Recipient Credit Memo, -4=Adj. for Manual Ext. Reconciliation]
  BaseRef nVarChar(11) Origin No.
  RefDate Date(8) Posting Date
  Memo nVarChar(254) Remarks
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  CreatedBy Int(11) Original
  LocTotal Num(19,6) Total in Local Currency
  FcTotal Num(19,6) Total in Foreign Currency
  SysTotal Num(19,6) Total in System Currency
  TransCode nVarChar(4) Transaction Code ->OTRC
  OrignCurr nVarChar(3) Revaluation Currency ->OCRN
  TransRate Num(19,6) Revaluation Rate
  BtfLine Int(11) Row in Voucher
  TransCurr nVarChar(3) Transaction Currency
  Project nVarChar(20) Project Code ->OPRJ
  DueDate Date(8) Due Date
  TaxDate Date(8) Document Date
  PCAddition VarChar(1) PC Addition default=N [Y=Yes, N=No]
  FinncPriod Int(11) Posting Period ->OFPR
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Recording Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  RefndRprt VarChar(1) Repayment Report default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=30 ->ADP1
  Indicator nVarChar(2) Indicator Code ->OIDC
  AdjTran VarChar(1) Adjusting Transaction default=N [Y=Yes, N=No]
  RevSource VarChar(1) Revaluation Source default=N [F=FC, S=System, N=No]
  StornoDate Date(8) Reversal Date
  StornoToTr Int(11) Reverse Transaction
  AutoStorno VarChar(1) Use Auto-Reverse default=N [Y=Yes, N=No]
  Corisptivi VarChar(1) Transaction Values default=N [Y=Yes, N=No]
  VatDate Date(8) VAT Date
  StampTax VarChar(1) Stamp Tax default=N [Y=Yes, N=No]
  Series Int(11) Series default=0
  Number Int(11) Number
  AutoVAT VarChar(1) Automatic Tax default=N [Y=Yes, N=No]
  DocSeries Int(11) Document Series
  FolioPref nVarChar(4) Folio Prefix String
  FolioNum Int(11) Folio Number
  CreateTime Int(6) Generation Time
  BlockDunn VarChar(1) Block Dunning Letter default=N [N=No, Y=Yes]
  ReportEU VarChar(1) Include in EU Report default=N [Y=Yes, N=No]
  Report347 VarChar(1) Include in 347 Report default=N [Y=Yes, N=No]
  Printed VarChar(1) Printed default=N [Y=Yes, N=No]
  DocType nVarChar(60) Document Type ->OJET
  AttNum Int(11) Number of Attachments default=0
  GenRegNo VarChar(1) Generate Reg. No. or Not default=N [Y=Yes, N=No]
  RG23APart2 Int(11) RG23A Part2 No
  RG23CPart2 Int(11) RG23C Part2 No
  MatType Int(11) Material Type
  Creator nVarChar(155) Creator Name
  Approver nVarChar(155) Approver Name
  Location Int(11) Loc. ->OLCT
  SeqCode Int(6) Sequence Code
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  AutoWT VarChar(1) Automatic WTax default=N [Y=Yes, N=No]
  WTSum Num(19,6) WTax Amount
  WTSumSC Num(19,6) WTax Amount (SC)
  WTSumFC Num(19,6) WTax Amount (FC)
  WTApplied Num(19,6) Applied WTax
  WTAppliedS Num(19,6) Applied WTax (SC)
  WTAppliedF Num(19,6) Applied WTax (FC)
  BaseAmnt Num(19,6) Base Amount
  BaseAmntSC Num(19,6) Base Amount (SC)
  BaseAmntFC Num(19,6) Base Amount (FC)
  BaseVtAt Num(19,6) WTax Base VAT Amount
  BaseVtAtSC Num(19,6) WTax Base VAT Amount (SC)
  BaseVtAtFC Num(19,6) WTax Base VAT Amount (FC)
  VersionNum nVarChar(13) Version Number
  BaseTrans Int(11) Base Transaction Number
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Country/Region of Residence, 5=Certificate of Fiscal Residence, 6=Other Document]
  OperatCode VarChar(1) Operation Code [A=Summary Invoices Entry, B=Summary Receipts Entry, C=Invoice with Several VAT Rates, D=Correction Invoice, E=Due VAT Pending Invoice Issuance, F=Expenses Incurred by Travel Agent for Customers, G=Special Regulation for VAT Group, H=Special Regulation for Gold Investment, I=Reverse Charge Procedure, J=Unsummarized Receipts, K=Identification of Error Transactions, X=Transactions with Entrepreneurs Issuing Receipts for Agricultural Compensation, N=Service Invoicing by Travel Agencies on Behalf of Third Parties, R=Business Office Rental, S=Subsidies, T=Incoming Payments for Industrial and Intellectual Property Rights, U=Insurance Transactions, V=Purchases from Travel Agencies, W=Transactions Subject to Production, Service, and Import Taxes in Ceuta and Melilla, Z=Deferred Tax - Special Regime, 1=Deferred Tax - Summary Invoices Entry, 2=Deferred Tax - Invoices with Several Entries (More Than One Tax Group), 3=Deferred Tax - Correction Invoice, 4=Deferred Tax - Acquisitions Made by Travel Agencies in the Travelers Own Interest (Special Regime for Travel Agencies), 5=Deferred Tax - Simplified Invoices, 6=Deferred Tax - Correction of Errata Entries, 7=Deferred Tax - Travel Agency Services on Behalf of Third Parties, 8=Deferred Tax - Rental of Business Premises]
  Ref3 nVarChar(100) Reference 3
  SSIExmpt VarChar(1) SSI Exemption [Y=Yes, N=No]
  SignMsg Text(16) Signature Input Message
  SignDigest Text(16) Signature Digest
  CertifNum nVarChar(50) Certification Number
  KeyVersion Int(11) Private Key Version
  CUP Int(11) Unique Code of Project ->OCUP
  CIG Int(11) Contract Code Identification ->OCIG
  SupplCode nVarChar(254) Supplementary Code
  SPSrcType Int(11) Service Posting Source Type
  SPSrcID Int(11) Service Posting Source ID
  SPSrcDLN Int(11) Service Post. Source Delivery
  DeferedTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  AgrNo Int(11) Blanket Agreement Number ->OOAT
  SeqNum Int(11) Sequence Number
  ECDPosTyp VarChar(1) ECD Posting Type default=N [N=Normal, E=Statement]
  RptPeriod nVarChar(5) Reporting Period
  RptMonth Date(8) Reporting Month
  ExTransId Int(11) Exposed Transaction ID
  PrlLinked VarChar(1) Is JE linked by MX Payroll default=N [Y=Yes, N=No]
  PTICode nVarChar(5) POI Code ->OPTI
  Letter VarChar(1) Letter
  FolNumFrom Int(11) Folio Number From
  FolNumTo Int(11) Folio Number To
  RepSection nVarChar(3) Reporting Section
  ExclTaxRep VarChar(1) Exclude from Control Statement default=N [Y=Yes, N=No]
  IsCoEntry VarChar(1) Cost Center Transfer form default=N [Y=Yes, N=No]
  SAPPassprt Text(16) Extended SAP Passport
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachment
  EBookable VarChar(1) E-Books Enabled default=N [N=No, Y=Yes]
  DataVers Int(11) Data Version default=1

# OJET - JE Document Type
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: JEType
Fields (name type(len) description [values] ->parent table):
  JEType nVarChar(60) JE Document Type
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DocTypDesc nVarChar(254) Document Type Description
  ShortName nVarChar(254) Short Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OJST - TDS Adjustment
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  DocDate Date(8) Posting Date
  Comments nVarChar(254) Remarks
  JrnlMemo nVarChar(50) Journal Remarks
  TransId Int(11) Transaction Number ->OJDT
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(11) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  CreateTime Int(11) Generation Time
  DepositNum Int(11) Deposit Number ->OVPM
  CertNum nVarChar(31) Certificate Number

# OKPF - KPI Factor
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FactorId
Fields (name type(len) description [values] ->parent table):
  FactorId nVarChar(3) KPI Factor No.
  FactorName nVarChar(100) KPI Factor Name
  CatId Int(6) Numerator
  TemplateId Int(11) Template
  IsSys VarChar(1) Is System [Y=Yes, N=No]

# OKRT - Tax Report Type
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  TAX_REP_TY U: TaxRepType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Tax Report Type ID
  TaxRepType nVarChar(254) Tax Report Type Name
  Descrip nVarChar(254) Tax Report Type Description
  SumRepType Int(11) Summary VAT Report Type ->OSVT
  NameDesc nVarChar(254) Tax Report Type Name + Desc

# OMDP - Manual Depreciation
Module: Finance | 44 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
  TRANS_TYPE: TransType, CreatedBy
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PeriodCat nVarChar(10) Period Category
  FinncPriod Int(11) Posting Period ->OFPR
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=P [P=Posted, D=Draft, C=Canceled]
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  Reference nVarChar(32) Reference
  ObjType nVarChar(20) Object Type
  Currency nVarChar(3) Currency ->OCRN
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Rate
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  TransType nVarChar(20) Original Document default=-1 [13=A/R Invoice, 19=A/P Credit Memo, 18=A/P Invoice, 46=Outgoing Payment, 163=A/P Correction Invoice, 1470000049=Capitalization, 1470000060=Fixed Assets Credit Memo, -1=All Transactions, 1470000075=Manual Depreciation, 1470000090=Fixed Assets Transfer, 1470000094=Retirement]
  CreatedBy Int(11) Original
  JrnlMemo nVarChar(254) Journal Remarks
  AssetDate Date(8) Asset Value Date
  CurSource VarChar(1) Base Currency default=L [L=Local Currency, S=System Currency, F=Foreign Currency]
  DocType nVarChar(15) Document Type default=PL [PL=Ordinary Depreciation, UP=Unplanned Depreciation, SD=Special Depreciation, AP=Appreciation, TR=Asset Transfer, NC=Sales, SC=Scrapping, TC=Asset Class Transfer]
  PrjSmarz VarChar(1) Summarize by Project default=Y [Y=Yes, N=No]
  DstRlSmarz VarChar(1) Summarize by Distribution Rule default=Y [Y=Yes, N=No]
  ManDprType nVarChar(15) Manual Depreciation Type ->ODTP
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  DprArea nVarChar(15) Depreciation Area ->ODPA
  BPLId Int(11) Branch ->OBPL
  BaseRef nVarChar(11) Base Reference
  LVARetire VarChar(1) Low Value Asset Retirement default=N [Y=Yes, N=No]
  CancelOpt Int(6) Cancelation Option default=1
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  GdsMovType nVarChar(2) Goods Movement Type

# OMDR - Manual Distribution Rule
Module: Finance | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: OcrCode
Fields (name type(len) description [values] ->parent table):
  OcrCode nVarChar(8) Factor Code
  OcrName nVarChar(30) Factor Description
  OcrTotal Num(19,6) Total Factor
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DimCode Int(6) In Which Dimension default=1 ->ODIM
  AbsEntry Int(11) Numerator
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  logInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  IsFixedAmt VarChar(1) Distribute by Fixed Amount default=N [Y=Yes, N=No]

# ONFM - Nota Fiscal Model
Module: Finance | 8 columns | ObjType: 540000056
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry nVarChar(6) NF Model ID
  NfmName nVarChar(20) NF Model Name
  NfmDescrip nVarChar(100) NF Model Description
  UserSign Int(6) User Signature - Create ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  NfmCode nVarChar(10) NF Model Code
  NfmTW VarChar(1) Tax Wizard Relevant default=Y [Y=Yes, N=No]

# OPRJ - Project Codes
Module: Finance | 11 columns | ObjType: 63
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrjCode
Fields (name type(len) description [values] ->parent table):
  PrjCode nVarChar(20) Project Code
  PrjName nVarChar(100) Project Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# ORCR - Recurring Postings
Module: Finance | 25 columns | ObjType: 34
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RcurCode, Instance
  BYDATE: NextDeu
Fields (name type(len) description [values] ->parent table):
  RcurCode nVarChar(8) Recurring Postings Code
  RcurDesc nVarChar(50) Transaction Description
  Frequency VarChar(1) Frequency default=M [D=Daily, W=Weekly, M=Monthly, Q=Quarterly, S=Semi-annually, A=Annually, O=One Time, T=Template, N=Not executed yet]
  Remind Int(6) Sub-Frequency default=1
  LastPosted Date(8) Last Executed
  NextDeu Date(8) Next Execution
  EntryCount Int(6) Entries Counter default=0
  Volume Num(19,6) Transaction Amount
  VolCurr nVarChar(3) Total Currency
  FinancVol Num(19,6) Total Monetary Val. of Trans.
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  TransCode nVarChar(4) Transaction Code
  Memo nVarChar(254) Details
  LimitRtrns VarChar(1) Returns Limit default=N [Y=Yes, N=No]
  Returns Int(6) No. of Returns
  LimitDate Date(8) Date Limit
  Instance Int(6) Instance default=0
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  StampTax VarChar(1) Stamp Tax default=N [Y=Yes, N=No]
  AutoVat VarChar(1) Automatic VAT default=N [Y=Yes, N=No]
  ManageWTax VarChar(1) Manage WTax default=N [Y=Yes, N=No]
  Ref3 nVarChar(100) Reference 3
  DeferedTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]

# ORTI - Retirement
Module: Finance | 44 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  INDEX U: DocNum, PIndicator
  TRANS_TYPE: TransType, CreatedBy
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  PeriodCat nVarChar(10) Period Category
  FinncPriod Int(11) Posting Period ->OFPR
  PostDate Date(8) Posting Date
  DocDate Date(8) Document Date
  DocStatus VarChar(1) Document Status default=P [P=Posted, D=Draft, C=Canceled]
  TransId Int(11) Transaction Number ->OJDT
  Comments nVarChar(254) Remarks
  Reference nVarChar(32) Reference
  ObjType nVarChar(20) Object Type
  Currency nVarChar(3) Currency ->OCRN
  DocRate Num(19,6) Document Rate
  SysRate Num(19,6) System Rate
  PIndicator nVarChar(10) Period Indicator ->OPID
  DocTotal Num(19,6) Document Total
  DocTotalFC Num(19,6) Document Total (FC)
  DocTotalSy Num(19,6) Document Total (SC)
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  CreateDate Date(8) Create Date
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Date of Update
  TransType nVarChar(20) Original Document default=-1 [13=A/R Invoice, 19=A/P Credit Memo, 18=A/P Invoice, 46=Outgoing Payment, 163=A/P Correction Invoice, 1470000049=Capitalization, 1470000060=Fixed Assets Credit Memo, -1=All Transactions, 1470000075=Manual Depreciation, 1470000090=Fixed Assets Transfer, 1470000094=Retirement]
  CreatedBy Int(11) Original
  JrnlMemo nVarChar(254) Journal Remarks
  AssetDate Date(8) Asset Value Date
  CurSource VarChar(1) Base Currency default=L [L=Local Currency, S=System Currency, F=Foreign Currency]
  DocType nVarChar(15) Document Type default=PL [PL=Ordinary Depreciation, UP=Unplanned Depreciation, SD=Special Depreciation, AP=Appreciation, TR=Asset Transfer, NC=Sales, SC=Scrapping, TC=Asset Class Transfer]
  PrjSmarz VarChar(1) Summarize by Project default=Y [Y=Yes, N=No]
  DstRlSmarz VarChar(1) Summarize by Distribution Rule default=Y [Y=Yes, N=No]
  ManDprType nVarChar(15) Manual Depreciation Type ->ODTP
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  DprArea nVarChar(15) Depreciation Area ->ODPA
  BPLId Int(11) Branch ->OBPL
  BaseRef nVarChar(11) Base Reference
  LVARetire VarChar(1) Low Value Asset Retirement default=N [Y=Yes, N=No]
  CancelOpt Int(6) Cancelation Option default=1
  BPLName nVarChar(100) Branch Name
  VatRegNum nVarChar(32) VAT Reg. Number
  GdsMovType nVarChar(2) Goods Movement Type [BA=Retirement - End of Appropriation, AT=Sale or Transfer, PE=Extinction, Loss or Deterioration, OT=Other Fixed Outputs]

# ORTM - Rate Differences
Module: Finance | 20 columns | ObjType: 9
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, IsSysCurr
  SYS_CURR: IsSysCurr
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Reconciliation Key
  Rtmdate Date(8) Posting Date
  AcctCode nVarChar(15) G/L Account/BP Code
  IsCard VarChar(1) Card default=N [Y=Yes, N=No]
  ActCurrncy nVarChar(3) Document Valuation Currency
  ActRate Num(19,6) Document Revaluation Rate
  Balance Num(19,6) Balance
  FrnBlnc Num(19,6) FC Balance
  TransNum Int(11) Transaction Number default=0
  Valid VarChar(1) Confirmed default=N [Y=Yes, N=No]
  Delta Num(19,6) Difference in LC
  IsSysCurr VarChar(1) In System Currency default=N [Y=Yes, N=No]
  StornoDate Date(8) Reversal Date
  RevalRate Num(19,6) Revaluation Rate
  UserSign Int(6) User Signature ->OUSR
  BPLId Int(11) Branch ->OBPL
  CntBlnc Num(19,6) Converted Balance
  TransAmtSC Num(19,6) Transaction Amount Total
  BalDueSC Num(19,6) Balance Due Total
  SCAdjust VarChar(1) SC Adjustment default=N [Y=Yes, N=No]

# ORTS - CPI and FC Rates for Reports
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RateDate, Currency, ReportType
  DATE: RateDate
Fields (name type(len) description [values] ->parent table):
  RateDate Date(8) Exchange Rate Date
  Currency nVarChar(3) Currency Code
  Rate Num(19,6) Currency Rate
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  ReportType VarChar(1) Report Rate Type default=S [S=Standard Report Rate, I=Intrastat Exchange Rate]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(11) Updating User ->OUSR

# ORTT - CPI and FC Rates
Module: Finance | 8 columns | ObjType: 75
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RateDate, Currency
  DATE: RateDate
Fields (name type(len) description [values] ->parent table):
  RateDate Date(8) Exchange Rate Date
  Currency nVarChar(3) Currency Code
  Rate Num(19,6) Currency Rate
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(11) Updating User ->OUSR

# OSCM - Special Ledger - Analytical Accounting Configuration Rules: Material
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleID
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number
  RuleType Int(6) Rule Type Number default=2
  ParentID Int(6) Parent Rule ID ->OSCM
  Status VarChar(1) Rule Status
  Priority Int(6) Rule Priority default=100
  Name nVarChar(100) Rule Name
  CreateDate Date(8) Date of Rule Generation
  UpdateDate Date(8) Date of Rule Change
  UserSign Int(6) Rule Created By ->OUSR
  UserSign2 Int(6) Rule Changed By ->OUSR
  ExtCond nVarChar(200) Extended Special Data

# OSCR - Special Ledger - Analytical Accounting Configuration Rules: Revenues & Expenses
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleID
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number
  RuleType Int(6) Rule Type Number default=1
  ParentID Int(6) Parent Rule ID ->OSCR
  Status VarChar(1) Rule Status
  Priority Int(6) Rule Priority default=100
  Name nVarChar(100) Rule Name
  CreateDate Date(8) Date of Rule Generation
  UpdateDate Date(8) Date of Rule Change
  UserSign Int(6) Rule Created By ->OUSR
  UserSign2 Int(6) Rule Changed By ->OUSR
  ExtCond nVarChar(200) Extended Special Data

# OSHR - Shareholder's Rights and Interests Report History
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) Identity
  Name nVarChar(40) Report Name
  UserSign Int(6) Creater's code
  UserName nVarChar(20) Name of Creator
  CreateDate Date(8) Report Created On
  StartDate Date(8) Date Range Start
  EndDate Date(8) Date Range End
  TemplateId Int(11) Template ID

# OSLM - Special Ledger - Analytical Accounting Report: Material
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocID
Fields (name type(len) description [values] ->parent table):
  DocID Int(11) Document Identification Number
  DocDate Date(8) Date of Report Generation
  Ref1 Int(11) Journal Entry Number ->OJDT
  Ref2 Int(11) Original JE Reference ->OJDT
  Status VarChar(1) Document Status
  DateFrom Date(8) Document Start Date
  DateTo Date(8) Document End Date
  TotDebit Num(19,6) Total Debit Amount
  TotCredit Num(19,6) Total Credit Amount
  RateType VarChar(1) Type of Exchange Rate default=O [O=Original document, E=Execution date, V=Other value]
  Comment nVarChar(250) Remarks
  UserSign Int(6) User Signature ->OUSR
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  CancelUser Int(6) Document Cancelled by ->OUSR

# OSLR - Special Ledger - Analytical Accounting Report: Revenues & Expenses
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocID
Fields (name type(len) description [values] ->parent table):
  DocID Int(11) Document Identification Number
  DocDate Date(8) Date of Report Generation
  Ref1 Int(11) Journal Entry Number ->OJDT
  Ref2 Int(11) Original JE Reference ->OJDT
  Status VarChar(1) Document Status
  DateFrom Date(8) Document Start Date
  DateTo Date(8) Document End Date
  TotDebit Num(19,6) Total Debit Amount
  TotCredit Num(19,6) Total Credit Amount
  RateType VarChar(1) Type of Exchange Rate default=O [O=Original document, E=Execution date, V=Other value]
  Comment nVarChar(250) Remarks
  UserSign Int(6) User Signature ->OUSR
  Canceled VarChar(1) Canceled default=N [Y=Yes, N=No]
  CancelDate Date(8) Cancelation Date
  CancelUser Int(6) Document Cancelled by ->OUSR

# OSVT - Define Summary VAT Report Type
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) VAT Report Type ID
  Name nVarChar(254) Summary VAT Report Type
  Descript nVarChar(254) Description
  NameDesc nVarChar(254) Name & Desc

# OTAX - VAT Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: SrcObjType, SrcObjAbs, OrdinLNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type default=-1 [-1=, 13=A/R Invoice, 14=A/R Credit Memo, 165=Correction A/R Invoice, 166=Correction A/R Invoice Reversals, 18=A/P Invoice, 19=A/P Credit Memo, 163=Correction A/P Invoice, 164=Correction A/P Invoice Reversals, 46=Outgoing Payment, 24=Incoming Payment, 57=Check for Payment, 30=Journal Transaction, 67=Warehouse Transfer, 25=Deposit, 321=Internal Reconciliation, 76=Deposit Temporary, 140000010=Incoming Excise Invoice, 140000009=Outgoing Excise Invoice, 69=Import file]
  SrcObjAbs Int(11) Source Object Internal ID default=-1
  OrdinLNum Int(11) Ordial Num (BTF & Canceled) default=-1
  Cancelled VarChar(1) Canceled default=N [N=No, Y=Yes]

# OTCC - Tax Category Code
Module: Finance | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(50) Code
  Name nVarChar(254) Name

# OTRC - Journal Entry Codes
Module: Finance | 6 columns | ObjType: 45
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrnsCode
  DESCRIP: TrnsCodDsc
Fields (name type(len) description [values] ->parent table):
  TrnsCode nVarChar(4) Code
  TrnsCodDsc nVarChar(20) Description
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Pcn874Ctg VarChar(1) Trans. Category for PCN874 default=N [N=None, I=Import Log, E=Export Log, O=Other, R=A/R Invoice - Palestinian Territory, P=A/P Invoice - Palestinian Territory, M=Self-Employed - Sales, C=Self-Employed - Purchase]

# OTRT - Posting Templates
Module: Finance | 11 columns | ObjType: 55
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrtCode
Fields (name type(len) description [values] ->parent table):
  TrtCode nVarChar(8) Template Code
  Dscription nVarChar(60) Template Description
  FrgnMode VarChar(1) FC Template default=Y [Y=Yes, N=No]
  Memo nVarChar(50) Details
  TransCode nVarChar(4) Transaction Code
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  StampTax VarChar(1) Stamp Tax default=N [Y=Yes, N=No]
  AutoVat VarChar(1) Automatic VAT default=N [Y=Yes, N=No]
  ManageWTax VarChar(1) Manage WTax default=N [Y=Yes, N=No]
  DeferedTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]

# OTTR - Remark Text Templates
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Descr nVarChar(254) Template Description
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OUTX - Unreported VAT Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: SrcObjType, SrcObjAbs, OrdinLNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type default=-1 [-1=, 15=Delivery notes, 16=Revert Delivery Notes, 17=Sales Order, 20=Goods Receipt, 21=Goods Return, 22=Purchase order, 23=Sales Quotation, 112=Document Draft, 59=Goods Receipt, 60=Goods Issue, 28=Journal Batches, 140=Payment Draft, 123=Checks for Payment Drafts, 540000006=Purchase Quotation]
  SrcObjAbs Int(11) Source Object Internal ID default=-1
  OrdinLNum Int(11) Ordial Num (BTF & Canceled) default=-1
  Cancelled VarChar(1) Canceled default=N [N=No, Y=Yes]

# OUWTX - Unreported WTax Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: SrcObjType, SrcObjAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type default=-1 [-1=, 13=A/R Invoice, 14=A/R Credit Memo, 18=A/P Invoice, 19=A/P Credit Memo, 46=Outgoing Payment, 24=Incoming Payment]
  SrcObjAbs Int(11) Source Object Internal ID default=-1
  Cancelled VarChar(1) Canceled default=N [N=No, Y=Yes]
  FullCopied VarChar(1) Fully Copied default=N [N=No, Y=Yes]

# OVEB - VAT Exemptions for Business Partners
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  BP_CODE U: CardCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD
  VersionNum nVarChar(13) Version Number
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UpdateTS Int(11) Update Full Time
  Comments nVarChar(254) Remarks

# OVRW - VAT Reposting Wizard
Module: Finance | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  RunName nVarChar(100) Wizard Run Name
  RunDate Date(8) Wizard Run Date
  Status VarChar(1) Status default=E [E=Executed, S=Saved, D=Draft, C=Canceled]
  UserSign Int(11) User Signature ->OUSR
  LedgerType VarChar(1) Ledger Type default=S [S=Sales, P=Purchase]
  DebitAcc nVarChar(15) Debit Account ->OACT
  PostDate Date(8) Posting Date
  JESeries nVarChar(11) Journal Entry Series default=0
  APTISeries nVarChar(11) Invoice Series default=0
  DateType VarChar(1) Date Type default=R [R=Posting Date, D=Due Date, T=Document Date]
  DateFrom Date(8) Date From
  DateTo Date(8) Date To
  IncCorAlt VarChar(1) Include Corr. and Alter. default=N [Y=Yes, N=No]
  BPLId Int(11) This field is not used anymore ->OBPL
  RunType VarChar(1) Run Type default=M [M=Manual, C=Automatic - Export - Confirmation Expected, E=Automatic - Export - Confirmed/Not Confirmed, S=Separate Accounting]

# OVTG - Tax Definition
Module: Finance | 67 columns | ObjType: 5
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  GROUP_NAME: Name
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(50) Name
  Rate Num(19,6) Rate %
  EffecDate Date(8) Effective from
  Category VarChar(1) Category default=O [O=Output Tax, I=Input Tax]
  Account nVarChar(15) Tax Account ->OACT
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  IsEC VarChar(1) EU default=N [Y=Yes, N=No]
  Indicator VarChar(1) Triangular Deal ->OIND
  AcqstnRvrs VarChar(1) Acquisition/Reverse default=N [Y=Yes, N=No]
  NonDedct Num(19,6) Non Deduct. %
  AcqsTax nVarChar(15) Acquisition Tax Account ->OACT
  GoddsShip VarChar(1) Goods Shipment ->OGSP
  NonDedAcc nVarChar(15) Non Deduct. Acct ->OACT
  DeferrAcc nVarChar(15) Deferred Tax Account ->OACT
  EquVatPr Num(19,6) Equalization Tax %
  ReportCode nVarChar(100) Group Description
  FixdAssts VarChar(1) Fixed Assets Flag default=N [Y=Yes, N=No]
  CalcMethod VarChar(1) Calculation Method default=R [R=Rate, F=Fixed]
  TaxType VarChar(1) Tax Type (VAT or Stamp) default=V [V=VAT, S=Stamp]
  FixedAmnt Num(19,6) Fixed Amount (LC)
  ExtCode nVarChar(10) External Code
  Correction VarChar(1) Correction default=N [Y=Yes, N=No]
  VatCrctn nVarChar(8) VAT Correction ->OVTG
  RetVatCode nVarChar(8) Returning VAT Code
  RepType Int(11) Report Type ->OKRT
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  TaxCtgr nVarChar(6) Tax Type (Annual List) default=E [E=Excluded, T=Taxable, X=Exempt, N=Not Taxable, N31=N3.1 - Not Taxable - exports, N32=N3.2 - Not Taxable - intra-community sales, N33=N3.3 - Not Taxable - sales to San Marino, N34=N3.4 - Not Taxable - operations similar to export sales, N35=N3.5 - Not Taxable - due to tax exemption letter, N36=N3.6 - Not Taxable - other transactions, G=Gross Profit, R=Reverse Charge, R61=N6.1 - Reverse Charge - disposal of scrap and other recycled materials, R62=N6.2 - Accounting Reversal - sale of gold and pure silver, R63=N6.3 - Reverse Charge - subcontracting in the construction sector, R64=N6.4 - Reverse Charge - sales of buildings, R65=N6.5 - Reverse Charge - sales of cell phones, R66=N6.6 - Reverse Charge - sales of electronic products, R67=N6.7 - Reverse Charge - services of the construction and related sectors, R68=N6.8 - Reverse Charge - energy sector operations, R69=N6.9 - Reverse Charge - other cases, U=Tourism, A=Taxable - Article 162, B=Taxable - Article 173 point 5, C=Taxable - Construction, D=Taxable - Expected Confirmation, F=Taxable - Gross, I=Taxable - Import, Y=Taxable - Import from EAEU, L=Taxable - Late Export, O=Taxable - Not Confirmed, S=Taxable - Real Estate, W=Taxable - Sale of Company, H=Excluded Art. 15, J=Not Subject, J21=N2.1 - Not Subject - to VAT under articles from 7 to 7-septies of DPR 633/72, J22=N2.2 - Not Subject - other cases, K=Paid in other EU country, M=Taxable - Article 151 point 1, P=Taxable - Article 170 point 3, V=Taxable - Fixed Assets, Q=Taxable - Tax Free]
  EquAccount nVarChar(15) Equalization Tax Account ->OACT
  UserSign2 Int(6) Updating User ->OUSR
  IsIGIC VarChar(1) IGIC default=N [Y=Yes, N=No]
  ServSupply VarChar(1) Service Supply ->OSSP
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  TaxCtgrBL VarChar(1) Tax Type (Black List) default=E [E=Excluded, T=Taxable, X=Exempt, N=Not Taxable, S=Non-Subject]
  R349Code Int(11) Report 349 Code default=0 [0=, 1=E, 2=A, 3=T, 4=S, 5=I, 6=M, 7=H, 8=R, 9=D]
  VatRevAcc nVarChar(15) VAT in Revenue Account ->OACT
  CashDisAcc nVarChar(15) Cash Discount Account ->OACT
  DpmTaxOAcc nVarChar(15) Down Paymnt Tax Offset Account ->OACT
  VatDedAcc nVarChar(15) VAT Deductible Account ->OACT
  CstmExpAcc nVarChar(15) Customs VAT Expense Account
  CstmAlcAcc nVarChar(15) Customs VAT Allocation Account
  TaxRegion nVarChar(5) Tax Country Region default=PT [PT=Continental Portugal, PT-AC=Azores Islands, PT-MA=Madeira Islands]
  ExemReason nVarChar(3) Tax Exemption Reason [M01=Article 16th No. 6 of CIVA, M02=Article 6th Law 198/90 June 19th, M03=Cash Liabilities, M04=Exempt Article 13th of CIVA, M05=Exempt Article 14th of CIVA, M06=Exempt Article 15th of CIVA, M07=Exempt Article 9th of CIVA, M08=VAT - Self-Liquidation, M09=VAT - Non-Deductible, M10=VAT - Exempted Company, M11=VAT - Exempted (Tobacco), M12=VAT - Exempted (Travel Agencies), M13=VAT - Exempt (Second Hand Goods), M14=VAT - Exempted (Objects of Art), M15=VAT - Exempted (Collectibles and Antiques), M16=VAT - Exempted (Article 14th of RITI), M99=Not Subject to VAT]
  Agent VarChar(1) Agent default=N [Y=Yes, N=No]
  OpCode nVarChar(7) Tax Operation Code
  Export VarChar(1) Export default=N [Y=Yes, N=No]
  Section nVarChar(3) VAT Section
  SplitPaymt VarChar(1) Split Payment default=N [Y=Yes, N=No]
  SplitPayAc nVarChar(15) Split Payment Account ->OACT
  TaxAgent VarChar(1) Tax Agent (Section 3) default=N [Y=Yes, N=No]
  SectionLim nVarChar(3) VAT Section (under limit)
  VatSubjCod nVarChar(10) VAT Subject Code
  VatType Int(11) Type of VAT default=-1 ->OBNI
  VatCategor Int(11) VAT Category default=-1 ->OBNI
  Parag44 VarChar(1) Paragraph 44 default=N [Y=Yes, N=No]
  ProrataDed VarChar(1) Pro-rata deductible default=N [Y=Yes, N=No]
  ExcFrmTaxS VarChar(1) Exclude from Tax Summary Report Total A/R or A/P Net Amounts default=N [Y=Yes, N=No]
  CstmActing VarChar(1) Customer Accounting default=N [Y=Yes, N=No]
  CstmActOut nVarChar(8) Customer Accounting Corresponding Tax Code
  StdTaxCode nVarChar(35) Standard Tax Code
  AcqRevTax nVarChar(8) Acquisition/Reverse Corresponding Tax Code
  ExReasonHU nVarChar(30) Tax Exemption Reason
  ExRemarkHU nVarChar(50) Tax Exemption Remark
  EBVatCateg Int(11) VAT Category

# OVTR - Tax Report
Module: Finance | 88 columns | ObjType: 180
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: ReportName, FilterType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs Entry (Numerator)
  ReportName nVarChar(50) Report Name
  RptLayout VarChar(1) Report Layout default=R [R=Tax Register Book, D=Tax Declaration, B=Black List Country - Tax Declaration, L=Black List Country - Tax Declaration 2013, A=VAT Annual List, I=Annual Invoice Declaration 2011, N=Annual Invoice Declaration 2013, P=Declaration of Purchases from San Marino, E=Electronic Tax Declaration, F=Electronic Tax Declaration 2018, M=VAT Invoice Declaration 2017, G=Electronic Tax Declaration 2019, T=One-Stop Shop Declaration]
  FirstPrint Int(11) First Printed No.
  FromDate Date(8) Date From
  ToDate Date(8) Date To
  TaxDate VarChar(1) Document Date default=N [N=No, Y=Yes]
  RoundSum VarChar(1) Round Amounts default=N [N=No, Y=Yes, =.]
  Declration VarChar(1) Declaration Type default=O [O=Original, S=Substitute, C=Complementary]
  FilterType VarChar(1) Selection Criteria Type default=N [V=Tax Report, W=Withholding Tax Report, T=Report 347, E=349 Report, R=Reconciliation Report, S=Stamp Tax, U=Sales Report, N=None, B=Box Report, O=Appendix O or P Selection, A=Annual Sales Report, F=VAT Refund Report, C=Input/Output VAT Report]
  ExcludeWT VarChar(1) Exclude Withholding Tax default=N [N=No, Y=Yes]
  CustomerIn VarChar(1) Include Customers default=Y [Y=Yes, N=No]
  VendorIn VarChar(1) Include Vendors default=Y [N=No, Y=Yes]
  Period VarChar(1) Quarter, Year or Month default=Q [Q=Quarter, Y=Year, M=Month, S=.]
  Quarter Int(11) Quarter
  Year Int(11) Year
  DocType VarChar(1) A/P or A/R default=P [P=Purchasing Documents, R=Sales Documents]
  CreditMemo VarChar(1) Credit Memos default=N [N=No, Y=Yes]
  DocTypeIn VarChar(1) Include Document Type default=N [N=No, Y=Yes]
  FirstReg Int(11) First Register Number
  AccountIn VarChar(1) Include G/L Accounts default=N [N=No, Y=Yes]
  DeferTaxIn VarChar(1) Show Pmts with Deferred Tax default=Y [Y=Yes, N=No]
  ApndxOOrP VarChar(1) Appendix O or P Selection default=Y [Y=Yes, N=No]
  DispOBCB VarChar(1) Opening & Closing Balance default=Y [N=No, Y=Yes]
  FromSeries Int(11) From Tax Series Group
  ToSeries Int(11) To Tax Series Group
  canceltn VarChar(1) For EU Sales Report default=N
  HideNTrans VarChar(1) Hide Tax Codes with no Trans. default=N [N=No, Y=Yes]
  SeriesIn VarChar(1) Include Series Filter default=N [N=No, Y=Yes]
  UserCode nVarChar(25) User Code
  FromCardCo nVarChar(15) BP Code From
  ToCardCo nVarChar(15) BP Code To
  SizeOfStru Int(11) Size of Structure
  PostFrDate Date(8) Posting Date From
  PostToDate Date(8) Posting Date To
  DocFrDate Date(8) Document Date From
  DocToDate Date(8) Document Date To
  FromDoc1Nu nVarChar(11) Document 1 - From
  ToDoc1Nu nVarChar(11) Document 1 - To
  Serie1 nVarChar(11) Invoice Numbering Series default=Y [Y=Yes, N=No]
  Serie1CB VarChar(1) Inv. Numbering Series Filter default=N [Y=Yes, N=No]
  Doc1Type Int(11) Type of Document 1
  FromDoc2Nu nVarChar(11) Document 2 - From
  ToDoc2Nu nVarChar(11) Document 2 - To
  Serie2 nVarChar(11) Credit Memo Numbering Series default=Y [Y=Yes, N=No]
  Serie2CB VarChar(1) Corr. Inv. Rev. No. Series default=N [Y=Yes, N=No]
  Doc2Type Int(11) Type of Document 2
  FromDoc3Nu nVarChar(11) Document 3 - From
  ToDoc3Nu nVarChar(11) Document 3 - To
  Serie3 nVarChar(11) Corr. Inv. Numbering Series default=Y [Y=Yes, N=No]
  Serie3CB VarChar(1) Corr. Inv. Num. Series Filter default=N [Y=Yes, N=No]
  Doc3Type Int(11) Type of Document 3
  FromDoc4Nu nVarChar(11) Document 4 - From
  ToDoc4Nu nVarChar(11) Document 4 - To
  Serie4 nVarChar(11) Corr. Inv. Rev. No. Series default=Y [Y=Yes, N=No]
  Serie4CB VarChar(1) Corr. Inv. Reversal No. Series default=N [Y=Yes, N=No]
  Doc4Type Int(11) Type of Document 4
  FromDoc5Nu nVarChar(11) Document 5 - From
  ToDoc5Nu nVarChar(11) Document 5 - To
  Serie5 nVarChar(11) Down Payment Numbering Series default=Y [Y=Yes, N=No]
  Serie5CB VarChar(1) Down Payment Numbering Series default=N [Y=Yes, N=No]
  Doc5Type Int(11) Type of Document 5
  DateRBtn VarChar(1) Report Period default=I [I=Interval, D=Date]
  MarkDocsIn VarChar(1) Include Marketing Documents default=Y [N=No, Y=Yes]
  ExRate VarChar(1) Exchange Rate default=P [P=Posting, R=For Reports]
  ExRateDate VarChar(1) Exchange Rate Date default=P [P=Posting Date, D=Document Date, V=VAT Date]
  TrsPerioTp VarChar(1) Report Period Type [Y=Year, Q=Quarter, B=Bi-Monthly, M=Month, P=Period, F=Fiscal Year, G=Fiscal Quarter]
  TrsPerioNu Int(11) Report Period Number
  TrsYear Int(6) Report Year
  TrsAdjtNum Int(6) Report Adjustment Number
  DateType VarChar(1) Date Type default=P [P=Posting Date, D=Document Date, V=VAT Date, C=System Date]
  IncServDoc VarChar(1) Include Service Documents default=Y [Y=Yes, N=No]
  GrpBySCode VarChar(1) Group by Sales Code default=Y [Y=Yes, N=No]
  IncUnReDoc VarChar(1) Include Unreconciled Documents default=Y [Y=Yes, N=No]
  DoYearSum VarChar(1) Year Summary [Y=Yes, N=No]
  DefTaxOnly VarChar(1) Only Include Deferred Tax Docs default=N [Y=Yes, N=No]
  ExcElDoc VarChar(1) Exclude Electronic Documents default=N [Y=Yes, N=No]
  QtrByMnt VarChar(1) Quarter by Months default=N [Y=Yes, N=No]
  OnlyExtnTx VarChar(1) Only External Tax default=N [Y=Yes, N=No]
  IncludeWTR VarChar(1) Include Inventory Transfers default=Y [Y=Yes, N=No]
  FromMark nVarChar(40) MARK From
  ToMark nVarChar(40) MARK To
  IsueFrDate Date(8) Issue Date From
  IsueToDate Date(8) Issue Date To
  FromVatNo nVarChar(64) Issuer VAT No. From
  ToVatNo nVarChar(64) Issuer VAT No. To
  FrInvType nVarChar(50) Invoice Type From
  ToInvType nVarChar(50) Invoice Type To

# OWHC - E-Books Withholding Tax Category
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EBCateCode
Fields (name type(len) description [values] ->parent table):
  EBCateCode Int(11) Code
  EBCateDesc nVarChar(150) Description
  EBTax nVarChar(11) Tax

# OWHT - Withholding Tax
Module: Finance | 63 columns | ObjType: 178
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode
  WT_NAME: WTName
Fields (name type(len) description [values] ->parent table):
  WTCode nVarChar(4) WTax Code
  WTName nVarChar(50) WTax Name
  Rate Num(19,6) Rate
  EffecDate Date(8) Effective From
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  BaseType VarChar(1) Base Type default=N [G=Gross, N=Net, V=VAT, U=UoM]
  PrctBsAmnt Num(19,6) % Base Amount
  OffclCode nVarChar(15) Official Code
  Account nVarChar(15) Account ->OACT
  MinTaxAmt Num(19,6) Minimum Taxable Amount
  IsPrgrss VarChar(1) Progressive Tax default=N [Y=Progressive Tax, N=Not Progressive Tax]
  Type VarChar(1) Withholding Type default=V [V=VAT Withholding, I=Income Tax Withholding]
  RoundType VarChar(1) Rounding Type default=C [T=Truncated AU, C=Commercial Values, N=No Rounding]
  WTTypeId Int(11) Type ->OWTT
  WTCurrency nVarChar(3) Currency ->OCRN
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  Section Int(11) Section ->OSEC
  Threshold Num(19,6) Cumulative Threshold
  Surcharge Num(19,6) Surcharge
  Concess VarChar(1) Concessional default=N [Y=Yes, N=No]
  Assessee Int(11) Assessee ->ONOA
  ApTdsAcc nVarChar(15) A/P TDS Account ->OACT
  ApSurAcc nVarChar(15) A/P Surcharge Account ->OACT
  ApCessAcc nVarChar(15) A/P Cess Account ->OACT
  ApHscAcc nVarChar(15) A/P HSC Account ->OACT
  ArTdsAcc nVarChar(15) A/R TDS Account ->OACT
  ArSurAcc nVarChar(15) A/R Surcharge Account ->OACT
  ArCessAcc nVarChar(15) A/R Cess Account ->OACT
  ArHscAcc nVarChar(15) A/R HSC Account ->OACT
  Location Int(11) Location ->OLCT
  ReturnType VarChar(1) Return Type [A=26, B=27, C=27EQ]
  UserSign2 Int(6) Updating User ->OUSR
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  InCSTCode Int(11) CST Code Incoming default=-1 ->OTSC
  OutCSTCode Int(11) CST Code Outgoing default=-1 ->OTSC
  CalBaseN nVarChar(2) Nature of Calculation Base ->OBSI
  PymntRsnCd nVarChar(3) Payment Reason Code ->OSWA
  DIOTRpt VarChar(1) DIOT Report default=N [Y=Yes, N=No]
  TDSType VarChar(1) TDS Type [E=eTDS, D=GST TDS, C=GST TCS, S=TCS]
  ApIgstAcc nVarChar(15) A/P IGST Account ->OACT
  ApCgstAcc nVarChar(15) A/P CGST Account ->OACT
  ApSgstAcc nVarChar(15) A/P SGST Account ->OACT
  ArIgstAcc nVarChar(15) A/R IGST Account ->OACT
  ArCgstAcc nVarChar(15) A/R CGST Account ->OACT
  ArSgstAcc nVarChar(15) A/R SGST Account ->OACT
  ApUtgstAcc nVarChar(15) A/P UTGST Account ->OACT
  ApCsgstAcc nVarChar(15) A/P Cess GST Account ->OACT
  ArUtgstAcc nVarChar(15) A/R UTGST Account ->OACT
  ArCsgstAcc nVarChar(15) A/R Cess GST Account ->OACT
  TransThres Num(19,6) Transaction Threshold default=0
  EBWTaxCate Int(11) Withholding Tax Category ->OWHC
  ArTcsInAcc nVarChar(15) A/R TCS Interim Account ->OACT
  ArSurInAcc nVarChar(15) A/R Surcharge Interim Account ->OACT
  ArCesInAcc nVarChar(15) A/R Cess Interim Account ->OACT
  ArHscInAcc nVarChar(15) A/R HSC Interim Account ->OACT
  ApTcsInAcc nVarChar(15) A/P TCS Interim Account ->OACT
  ApSurInAcc nVarChar(15) A/P Surcharge Interim Account ->OACT
  ApCesInAcc nVarChar(15) A/P Cess Interim Account ->OACT
  ApHscInAcc nVarChar(15) A/P HSC Interim Account ->OACT
  LnWTInAcc nVarChar(15) Interim Account for Tax ->OACT
  NoDedThrsh VarChar(1) Apply Tax Exemption After Threshold default=N [Y=Yes, N=No]

# OWTA - Withholding Tax Accumulation
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: CardCode, PmntDate, WTTypeId, BPLId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  PmntDate Date(8) Payment Date
  WTTypeId Int(11) WT Type Id
  AccmAmnt Num(19,6) WT Accumulated Amount
  AccmAmntFC Num(19,6) WT Accumulated Amount FC
  AccmAmntSC Num(19,6) WT Accumulated Amount SC
  BPLId Int(11) Branch default=0

# OWTD - Withholding Tax Definition
Module: Finance | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  WT_CODE U: WTCode
  WT_NAME: WTName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WTCode nVarChar(4) WTax Code
  WTName nVarChar(50) WTax Code Name
  Rate Num(19,6) Rate
  EffecDate Date(8) Effective From
  Inactive VarChar(1) Inactive default=N [Y=, N=]
  OffclCode nVarChar(15) Official Code
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  BaseType VarChar(1) Base Type default=N [N=Net, V=VAT, G=Gross, H=Gross - VAT]
  WTTypeId Int(11) Type ->OWTT
  BaseMin Num(19,6) Min. Amount
  PrctBsAmnt Num(19,6) % Base Amount
  FmlId Int(11) Formula ID ->OFML
  Account nVarChar(15) Account ->OACT
  SlScProgr VarChar(1) Sliding Scale Progressive Tax default=N [Y=, N=]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CalcWHTCrM VarChar(1) Calculate Withholding Tax in Automatic Credit Memo default=Y [Y=Yes, N=No]

# OWTT - Withholding Tax Type
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTTypeId
  WT_TYPE U: WTType
Fields (name type(len) description [values] ->parent table):
  WTTypeId Int(11) Internal Number
  WTType nVarChar(10) Type
  WTThresh Num(19,6) Min. WTax Amount
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OWTX - WTax Transactions
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: SrcObjType, SrcObjAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SrcObjType nVarChar(20) Source Object Type default=-1 [-1=, 13=A/R Invoice, 14=A/R Credit Memo, 18=A/P Invoice, 19=A/P Credit Memo, 46=Outgoing Payment, 24=Incoming Payment]
  SrcObjAbs Int(11) Source Object Internal ID default=-1
  Cancelled VarChar(1) Canceled default=N [N=No, Y=Yes]
  FullCopied VarChar(1) Fully Copied default=N [N=No, Y=Yes]

# OZRD - POS Daily Summary
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DocDate Date(8) Document Date
  POSEquipNo nVarChar(20) POS Equipment No. ->OPOS
  ResetCntr Int(11) Reset Counter
  SummaryCnt Int(11) Summary Counter
  OperCntr Int(11) Operation Counter
  TotalSum Num(19,6) Total Sum
  GrossSale Num(19,6) Gross Sale Sum
  PISSum Num(19,6) PIS Sum
  COFINSSum Num(19,6) COFINS Sum

# RCI1 - Recipient List - Rows
Module: Finance | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code ->ORCI
  LineNum Int(11) Addressee Number
  ObjType nVarChar(20) Object [12=User, 171=Employee]
  ObjCode nVarChar(50) Object Code

# RCR1 - Recurring Postings - Rows
Module: Finance | 29 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RcurCode, Instance, LineId
Fields (name type(len) description [values] ->parent table):
  RcurCode nVarChar(8) Recurring Postings Code ->ORCR
  LineId Int(11) Row Number default=0
  AcctCode nVarChar(15) Account Code
  AcctDesc nVarChar(100) Account Description
  Debit Num(19,6) Debit
  Credit Num(19,6) Credit
  Currency nVarChar(3) Currency
  Instance Int(6) Instance
  VatGroup nVarChar(8) Tax Group ->OVTG
  UserSign Int(6) User Signature ->OUSR
  VatLine VarChar(1) VAT Row default=N [Y=Yes, N=No]
  CtrlAcct nVarChar(15) Control Account
  OcrCode nVarChar(8) Distr. Rule ->OOCR
  TaxType Int(6) Tax Type default=0
  TaxPostAcc VarChar(1) Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  StaCode nVarChar(8) Authority Code ->OSTA
  StaType Int(11) Authority Type ->OSTT
  TaxCode nVarChar(8) Tax Code ->OSTC
  OcrCode1 nVarChar(8) Costing Code 1 ->OOCR
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  WtLiable VarChar(1) WTax-Liable [Y=Yes, N=No]
  WTaxLine VarChar(1) WTax Row default=N [Y=Yes, N=No]
  GrossValue Num(19,6) Gross Value
  Project nVarChar(20) Project Code ->OPRJ
  BPLId Int(11) Branch ->OBPL
  CemCode nVarChar(20) Cost Element Code ->OCEM

# RTI1 - Retirement - Rows
Module: Finance | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORTI
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  AcctCode nVarChar(15) Account Code ->OACT
  Quantity Num(19,6) Quantity
  LineTotal Num(19,6) Line Total
  TotalFrgn Num(19,6) Line Total (FC)
  TotalSys Num(19,6) Line Total (SC)
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Remarks nVarChar(100) Remarks
  LogInstanc Int(11) Log Instance default=0
  NewItemCod nVarChar(50) New Item Code ->OITM
  Partial VarChar(1) Partial default=N [Y=Yes, N=No]
  APC Num(19,6) APC
  NewAstCls nVarChar(20) New Asset Class ->OACS
  ObjType nVarChar(20) Object Type
  TransType nVarChar(4) Transaction Type [0=Unknown, 110=Acquisition, 115=Subacquisition, 120=Credit Memo, 130=APC Write-Up, 210=Full Retirement, 220=Full Scrapping, 230=Partial Retirement, 240=Partial Scrapping, 310=Full Transfer, 320=Partial Transfer, 410=Manual Ordinary Depreciation, 420=Manual Unplanned Depreciation, 430=Manual Special Depreciation, 440=Appreciation, 510=Change of Depreciation Type, 520=Change of Useful Life, 530=Change of Depreciation Start Date, 540=Change of Salvage Value]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  Project nVarChar(20) Project Code ->OPRJ

# RTI2 - Retirement - Area Journal Transactions
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->ORTI
  LineNum Int(11) Row Number
  DprArea nVarChar(15) Depreciation Area ->ODPA
  JrnlMemo nVarChar(254) Journal Remarks
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0
  TransNum Int(11) Transaction Number ->OJDT
  JrnlMemo1 nVarChar(254) Cancellation Journal Remarks
  TransNum1 Int(11) Cancellation Transaction No. ->OJDT

# RTI3 - Retirement - Item Areas
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, ItemLine, DprArea
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OACQ
  ItemLine Int(11) Item Row Number
  ItemCode nVarChar(50) Item Code ->OITM
  DprArea nVarChar(15) Depreciation Area ->ODPA
  Total Num(19,6) Total
  TotalFrgn Num(19,6) Total (FC)
  TotalSys Num(19,6) Total (SC)
  ObjType nVarChar(20) Object Type
  LogInstanc Int(11) Log Instance default=0

# RTM1 - Rate Differences - Rows
Module: Finance | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, TransId, JdtLine, IsSysCurr
  SYS_CURR: IsSysCurr
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Reconciliation Key
  TransId Int(11) Journal Key ->OJDT
  JdtLine Int(11) Journal Row default=0
  IsSysCurr VarChar(1) Is System Currency default=N [Y=Yes, N=No]
  AcctCode nVarChar(15) G/L Account/BP Code
  Balance Num(19,6) Balance
  FrnBlnc Num(19,6) Balance (FC)
  Valid VarChar(1) Confirmed default=Y [Y=Yes, N=No]
  RevalRate Num(19,6) Revaluation Rate
  Delta Num(19,6) Difference in LC
  FCCurrency nVarChar(3) Foreign Currency
  JdtAcctCod nVarChar(15) Journal Account Code
  BaseRef nVarChar(11) Base Reference
  JdtType VarChar(1) Journal Entry Type default=U [P=Primary, G=Generated, W=Without Primary, U=Undefined Type]
  RefDate Date(8) Posting Date
  DueDate Date(8) Due Date
  TaxDate Date(8) Document Date
  BPLId Int(11) Branch ->OBPL
  CntBlnc Num(19,6) Converted Balance

# RTM2 - Rate Differences - SC Adjustment Rows
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, IsSysCurr, CardCode, AcctCode
  CARD_CODE: CardCode
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Reconciliation Key
  IsSysCurr VarChar(1) IS System Currency default=N [Y=Yes, N=No]
  CardCode nVarChar(15) BP Code ->OCRD
  AcctCode nVarChar(15) BP Control Account
  TransAmtSC Num(19,6) Total Transaction Amount (SC)
  BalDueSC Num(19,6) Total Balance Due (SC)

# SCM1 - Special Ledger - Analytical Accounting Configuration Rule Conditions: Material
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleID, CondNum
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCM
  CondNum Int(6) Condition Number
  Value1 nVarChar(200) Static Value
  Table1 nVarChar(20) Table Name
  Field1 nVarChar(200) Table Field Name
  Cond1 nVarChar(200) Value Selection Condition
  Group1 nVarChar(100) Group by Clause
  Relation nVarChar(50) Comparison Operator
  Value2 nVarChar(200) Static Value
  Table2 nVarChar(20) Table Name
  Field2 nVarChar(200) Table Field Name
  Cond2 nVarChar(200) Comparison Operator
  Group2 nVarChar(100) Group by Clause
  ExtCond1 nVarChar(200) Extended Special Data
  ExtCond2 nVarChar(200) Extended Special Data

# SCM2 - Special Ledger - Analytical Accounting Configuration Rule Goals: Material
Module: Finance | 22 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleID, GoalNum
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCM
  GoalNum nVarChar(6) Rule Goal Number
  TransTpVal Int(6) Transaction Type Number
  TransTpFld nVarChar(20) Transaction Type Table Field
  PrfCntVal nVarChar(8) Distribution Rule Code ->OOCR
  PrfCntFld nVarChar(20) Distribution Rule Table Field
  DebitAct nVarChar(15) Debit Account ->OACT
  CreditAct nVarChar(15) Credit Account ->OACT
  RevSides VarChar(1) Revert Debit/Credit Sides default=N [N=No, Y=Yes]
  SrcTable nVarChar(10) Main Source Table
  SrcField nVarChar(20) Main Source Table Field
  SrcFieldFC nVarChar(20) Source Field, Foreign Currency
  SrcFieldSC nVarChar(20) Source Field, System Currency
  Calc nVarChar(200) Calculation Expression
  CalcFC nVarChar(200) Expression for Foreign Calculation
  CalcSC nVarChar(200) Expression for System Calculation
  CalcCond nVarChar(200) Calculation Condition
  CalcCondFC nVarChar(200) Condition for Foreign Calculation
  CalcCondSC nVarChar(200) Condition for System Calculation
  CurrFld nVarChar(20) Table Field with Currency
  CallProc nVarChar(50) Recalculation Stored Procedure Name
  ExtCond nVarChar(200) Extended Special Data

# SCM3 - Special Ledger - Analytical Accounting Configuration Rule Additional Calculations: Material
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleID, FldNum
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCM
  FldNum Int(6) Result Field Number
  SrcTable nVarChar(20) Main Source Table
  SrcField nVarChar(20) Main Source Table Field
  CalcCase nVarChar(200) Additional Calcul. Expression
  CalcTable nVarChar(200) Main Calculation Expression
  CondCase nVarChar(200) Additional Calcul. Condition
  CondTable nVarChar(200) Main Calculation Condition
  Grouping nVarChar(100) Group by Clause
  CallProc nVarChar(50) Recalculation Stored Procedure Name
  ExtCond nVarChar(200) Extended Special Data

# SCR1 - Special Ledger - Analytical Accounting Configuration Rule Conditions: Revenues & Expenses
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleID, CondNum
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCR
  CondNum Int(6) Condition Number
  Value1 nVarChar(200) Static Value
  Table1 nVarChar(20) Table Name
  Field1 nVarChar(200) Table Field Name
  Cond1 nVarChar(200) Value Selection Condition
  Group1 nVarChar(100) Group by Clause
  Relation nVarChar(50) Comparison Operator
  Value2 nVarChar(200) Static Value
  Table2 nVarChar(20) Table Name
  Field2 nVarChar(200) Table Field Name
  Cond2 nVarChar(200) Comparison Operator
  Group2 nVarChar(100) Group by Clause
  ExtCond1 nVarChar(200) Extended Special Data
  ExtCond2 nVarChar(200) Extended Special Data

# SCR2 - Special Ledger - Analytical Accounting Configuration Rule Goals: Revenues & Expenses
Module: Finance | 22 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleID, GoalNum
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCR
  GoalNum nVarChar(6) Rule Goal Number
  TransTpVal Int(6) Transaction Type Number
  TransTpFld nVarChar(20) Transaction Type Table Field
  PrfCntVal nVarChar(8) Distribution Rule Code ->OOCR
  PrfCntFld nVarChar(20) Distribution Rule Table Field
  DebitAct nVarChar(15) Debit Account ->OACT
  CreditAct nVarChar(15) Credit Account ->OACT
  RevSides VarChar(1) Revert Debit/Credit Sides default=N [N=No, Y=Yes]
  SrcTable nVarChar(10) Main Source Table
  SrcField nVarChar(20) Main Source Table Field
  SrcFieldFC nVarChar(20) Source Field, Foreign Currency
  SrcFieldSC nVarChar(20) Source Field, System Currency
  Calc nVarChar(200) Calculation Expression
  CalcFC nVarChar(200) Expression for Foreign Calculation
  CalcSC nVarChar(200) Expression for System Calculation
  CalcCond nVarChar(200) Calculation Condition
  CalcCondFC nVarChar(200) Condition for Foreign Calculation
  CalcCondSC nVarChar(200) Condition for System Calculation
  CurrFld nVarChar(20) Table Field with Currency
  CallProc nVarChar(50) Recalculation Stored Procedure Name
  ExtCond nVarChar(200) Extended Special Data

# SCR3 - Special Ledger - Analytical Accounting Configuration Rule Additional Calculations: Revenues & Expenses
Module: Finance | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleID, FldNum
Fields (name type(len) description [values] ->parent table):
  RuleID Int(6) Rule Identification Number ->OSCR
  FldNum Int(6) Result Field Number
  SrcTable nVarChar(20) Main Source Table
  SrcField nVarChar(20) Main Source Table Field
  CalcCase nVarChar(200) Additional Calcul. Expression
  CalcTable nVarChar(200) Main Calculation Expression
  CondCase nVarChar(200) Additional Calcul. Condition
  CondTable nVarChar(200) Main Calculation Condition
  Grouping nVarChar(100) Group by Clause
  CallProc nVarChar(50) Recalculation Stored Procedure Name
  ExtCond nVarChar(200) Extended Special Data

# SHR1 - Shareholder's Rights and Interests Report History - Rows
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ShrId, RowId
Fields (name type(len) description [values] ->parent table):
  ShrId Int(11) SHR Identity ->OSHR
  RowId Int(11) Row Number
  CatId Int(6) Category Identity
  LineNum nVarChar(6) Line Number
  ItemName nVarChar(254) Item Name
  Level Int(6) Level Number
  IndentChar nVarChar(6) Number of Characters to Indent
  Formula VarChar(1) Formula?
  CurAmount Num(19,6) Current Period Amount
  PreAmount Num(19,6) Previous Period Amount

# SLM1 - Special Ledger - Analytical Accounting Report Lines: Material
Module: Finance | 34 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocID, LineID
Fields (name type(len) description [values] ->parent table):
  DocID Int(11) Document Identification Number ->OSLM
  LineID Int(11) Line Identification
  RuleID Int(6) Rule Identification Number ->OSCM
  GoalNum Int(6) Rule Goal Number
  TransType Int(6) Transaction Type Number
  PrfCntVal nVarChar(8) Distribution Rule Code ->OOCR
  PrfCntOrig nVarChar(8) Orig. Distribution Rule Code ->OOCR
  Checked VarChar(1) Selected for Processing default=Y [N=No, Y=Yes]
  Status VarChar(1) Status
  Enabled VarChar(1) Enabled for Processing default=Y [N=No, Y=Yes]
  DebitAct nVarChar(15) Debit Account ->OACT
  CreditAct nVarChar(15) Credit Account ->OACT
  RevSides VarChar(1) Revert Debit/Credit Sides default=N [N=No, Y=Yes]
  Src Num(19,6) Source Amount
  SrcFC Num(19,6) Source Amount, Foreign Currency
  SrcSC Num(19,6) Source Amount, System Currency
  SrcCalc Num(19,6) Calculated Amount
  SrcCalcFC Num(19,6) Calculated Amount - Foreign
  SrcCalcSC Num(19,6) Calculated Amount - System
  FinalSum Num(19,6) Final Amount
  FinalSumFC Num(19,6) Final Amount (FC)
  FinalSumSC Num(19,6) Final Amount (SC)
  Currency nVarChar(3) Foreign Currency ->OCRN
  MainTable nVarChar(20) Main Source Table
  PKField0 nVarChar(50) Primary Key Field
  PKField1 nVarChar(50) Primary Key Field
  PKField2 nVarChar(50) Primary Key Field
  PKField3 nVarChar(50) Primary Key Field
  PKField4 nVarChar(50) Primary Key Field
  PKField5 nVarChar(50) Primary Key Field
  PKField6 nVarChar(50) Primary Key Field
  PKField7 nVarChar(50) Primary Key Field
  PKField8 nVarChar(50) Primary Key Field
  PKField9 nVarChar(50) Primary Key Field

# SLR1 - Special Ledger - Analytical Accounting Report Lines: Revenues & Expenses
Module: Finance | 34 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocID, LineID
Fields (name type(len) description [values] ->parent table):
  DocID Int(11) Document Identification Number ->OSLR
  LineID Int(11) Line Identification
  RuleID Int(6) Rule Identification Number ->OSCR
  GoalNum Int(6) Rule Goal Number
  TransType Int(6) Transaction Type Number
  PrfCntVal nVarChar(8) Distribution Rule Code ->OOCR
  PrfCntOrig nVarChar(8) Orig. Distribution Rule Code ->OOCR
  Checked VarChar(1) Selected for Processing default=Y [N=No, Y=Yes]
  Status VarChar(1) Status
  Enabled VarChar(1) Enabled for Processing default=Y [N=No, Y=Yes]
  DebitAct nVarChar(15) Debit Account ->OACT
  CreditAct nVarChar(15) Credit Account ->OACT
  RevSides VarChar(1) Revert Debit/Credit Sides default=N [N=No, Y=Yes]
  Src Num(19,6) Source Amount
  SrcFC Num(19,6) Source Amount, Foreign Currency
  SrcSC Num(19,6) Source Amount, System Currency
  SrcCalc Num(19,6) Calculated Amount
  SrcCalcFC Num(19,6) Calculated Amount - Foreign
  SrcCalcSC Num(19,6) Calculated Amount - System
  FinalSum Num(19,6) Final Amount
  FinalSumFC Num(19,6) Final Amount (FC)
  FinalSumSC Num(19,6) Final Amount (SC)
  Currency nVarChar(3) Foreign Currency ->OCRN
  MainTable nVarChar(20) Main Source Table
  PKField0 nVarChar(50) Primary Key Field
  PKField1 nVarChar(50) Primary Key Field
  PKField2 nVarChar(50) Primary Key Field
  PKField3 nVarChar(50) Primary Key Field
  PKField4 nVarChar(50) Primary Key Field
  PKField5 nVarChar(50) Primary Key Field
  PKField6 nVarChar(50) Primary Key Field
  PKField7 nVarChar(50) Primary Key Field
  PKField8 nVarChar(50) Primary Key Field
  PKField9 nVarChar(50) Primary Key Field

# TAX1 - VAT Transactions - Rows
Module: Finance | 103 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineSeq
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OTAX
  LineSeq Int(11) Row Sequence
  SrcArrType Int(11) Source Array Type default=-1 [-1=Default, 1=Main, 12=Array1, 13=Array2, 14=Array3, 15=Array4, 16=Array5, 17=Array6, 18=Array7, 24=Array13]
  SrcLineNum Int(11) Source Row Number default=-1
  SrcGrpNum Int(11) Source Group Number default=-1 [-1=Default, 0=Group1, 1=Group2, 2=Group3]
  TaxCode nVarChar(8) Tax Code
  StaCode nVarChar(8) Tax Authority Code ->OSTA
  StaType Int(11) Tax Authority Type ->OSTT
  StaIndex Int(11) Tax Authority seq index
  IsLiable VarChar(1) Is Tax Liable default=Y [Y=Yes, N=No]
  TaxType VarChar(1) Tax Type default=Y [Y=Regular, U=Use Tax, N=No Tax, O=Tax Offset Transaction, R=Reverse Tax Offset Transaction, P=DPM Request Tax Offset Transaction, D=Deferred Tax Offset Transaction]
  IsAcq VarChar(1) Acquisition Tax Liable default=N [N=No, Y=Yes]
  Isdeferred VarChar(1) Deferred Tax [Yes/No] default=N [N=No, Y=Yes]
  ValueDate Date(8) Due Date for Payment
  VatPercent Num(19,6) VAT Percent
  NdPercent Num(19,6) Non Deductible %
  EqPercent Num(19,6) Equalization Percent
  BaseObjTyp nVarChar(20) Base Object Type default=-1 [-1=, 13=A/R Invoice, 14=A/R Credit Memo, 165=Correction A/R Invoice, 166=Correction A/R Invoice Reversals, 18=A/P Invoice, 19=A/P Credit Memo, 163=Correction A/P Invoice, 164=Correction A/P Invoice Reversals, 46=Outgoing Payment, 24=Incoming Payment, 57=Check for Payment, 30=Journal Transaction, 67=Warehouse Transfer, 25=Deposit, 321=Internal Reconciliation, 76=Deposit Temporary, 140000010=Incoming Excise Invoice, 140000009=Outgoing Excise Invoice, 69=Import file]
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
  CrditDebit VarChar(1) Credit Or Debit Transaction [C=Credit, D=Debit]
  PostingTyp VarChar(1) Sales or Purchase default=N [N=None, R=Sales, P=Purchase]
  BasePaid Num(19,6) Applied Base Sum
  BasePaidSC Num(19,6) Applied Base Sum (SC)
  BasePaidFC Num(19,6) Applied Base Sum (FC)
  VatPaid Num(19,6) Applied VAT Sum
  VatPaidSC Num(19,6) Applied VAT Sum (SC)
  VatPaidFC Num(19,6) Applied VAT Sum (FC)
  DeductPaid Num(19,6) Applied Deduct Sum
  DdctPaidSC Num(19,6) Applied Deduct Sum (SC)
  DdctPaidFC Num(19,6) Applied Deduct Sum (FC)
  EqPaid Num(19,6) Applied Equalization Sum
  EqPaidSC Num(19,6) Applied Equalization Sum (SC)
  EqPaidFC Num(19,6) Applied Equalization Sum (FC)
  TransAcct nVarChar(15) Transaction Acccount ->OACT
  LnDataNum Int(11) Row Number in Tax Data default=-1
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
  SplitPayAc nVarChar(15) Split Payment Account ->OACT
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
  CAOutCode nVarChar(8) Customer Accounting Output Tax Code
  CABasSum Num(19,6) Customer Accounting Reverse Base Sum
  CABasSumSc Num(19,6) Customer Accounting Reverse Base Sum (SC)
  CABasSumFc Num(19,6) Customer Accounting Reverse Base Sum (FC)
  CAVatSum Num(19,6) Customer Accounting Reverse VAT Sum
  CAVatSumSc Num(19,6) Customer Accounting Reverse VAT Sum (SC)
  CAVatSumFc Num(19,6) Customer Accounting Reverse VAT Sum (FC)
  CAOutAcct nVarChar(15) Customer Accounting Output Tax Account
  ExtVatPcnt Num(19,6) External VAT Percent
  ExtVatSum Num(19,6) External VAT Amount
  VatSumSrc VarChar(1) VAT Sum Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtVatSumF Num(19,6) External VAT Amount (FC)
  ExtVatSumS Num(19,6) External VAT Amount (SC)
  AcqRevTax nVarChar(8) Acquisition/Reverse Corresponding Tax Code
  VatExmPrc Num(19,6) VAT Exemption %
  VatExmBase Num(19,6) VAT Base %
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]

# TAX2 - VAT Transactions - Grouped Rows
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineSeq
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OTAX
  LineSeq Int(11) Row Sequence
  TaxCode nVarChar(8) Tax Code
  VatPercent Num(19,6) VAT Percent
  CrditDebit VarChar(1) Credit or Debit Transaction [C=Credit, D=Debit]
  BaseSum Num(19,6) Base Sum
  BaseSumSc Num(19,6) Base Sum (SC)
  BaseSumFc Num(19,6) Base Sum (FC)
  VatSum Num(19,6) VAT Sum
  VatSumSc Num(19,6) VAT Sum (SC)
  VatSumFc Num(19,6) VAT Sum (FC)
  TODedBaseS Num(19,6) Tax Only Deducted Base Sum
  TODedBaSSC Num(19,6) Tax Only Deducted Base Sum (SC)
  TODedBaSFC Num(19,6) Tax Only Deducted Base Sum (FC)
  LnDataNum Int(11) Row Number in Tax Data default=-1

# TRT1 - Posting Templates - Rows
Module: Finance | 26 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrtCode, Sequence
Fields (name type(len) description [values] ->parent table):
  TrtCode nVarChar(8) Template Code ->OTRT
  Sequence Int(11) Sequence Row No.
  AcctCode nVarChar(15) Account Code
  Line_Descr nVarChar(100) Account Description
  Debit Num(19,6) Debit
  Credit Num(19,6) Credit
  VatGroup nVarChar(8) Tax Group ->OVTG
  UserSign Int(6) User Signature ->OUSR
  VatLine VarChar(1) Vat Line default=N [Y=Yes, N=No]
  CtrlAcct nVarChar(15) Control Account
  OcrCode nVarChar(8) Distr. Rule ->OOCR
  TaxType Int(6) Tax Type default=0
  TaxPostAcc VarChar(1) Tax Posting Account default=N [N=, R=Sales Tax Account, P=Purchasing Tax Account]
  StaCode nVarChar(8) Authority Code ->OSTA
  StaType Int(11) Authority Type ->OSTT
  TaxCode nVarChar(8) Tax Code ->OSTC
  OcrCode1 nVarChar(8) Costing Code 1 ->OOCR
  OcrCode2 nVarChar(8) Costing Code 2 ->OOCR
  OcrCode3 nVarChar(8) Costing Code 3 ->OOCR
  OcrCode4 nVarChar(8) Costing Code 4 ->OOCR
  OcrCode5 nVarChar(8) Costing Code 5 ->OOCR
  WtLiable VarChar(1) WTax-Liable [Y=Yes, N=No]
  WTaxLine VarChar(1) WTax Row default=N [Y=Yes, N=No]
  GrossValue Num(19,6) Gross Value
  Project nVarChar(20) Project Code ->OPRJ
  CemCode nVarChar(20) Cost Element Code ->OCEM

# UTX1 - Unreported VAT Transactions - Rows
Module: Finance | 103 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineSeq
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
  CAOutCode nVarChar(8) Customer Accounting Output Tax Code
  CABasSum Num(19,6) Customer Accounting Reverse Base Sum
  CABasSumSc Num(19,6) Customer Accounting Reverse Base Sum (SC)
  CABasSumFc Num(19,6) Customer Accounting Reverse Base Sum (FC)
  CAVatSum Num(19,6) Customer Accounting Reverse VAT Sum
  CAVatSumSc Num(19,6) Customer Accounting Reverse VAT Sum (SC)
  CAVatSumFc Num(19,6) Customer Accounting Reverse VAT Sum (FC)
  CAOutAcct nVarChar(15) Customer Accounting Output Tax Account
  ExtVatPcnt Num(19,6) External VAT Percent
  ExtVatSum Num(19,6) External VAT Amount
  VatSumSrc VarChar(1) VAT Sum Source default=S [S=Internal System Calculation, E=External Calculation]
  ExtVatSumF Num(19,6) External VAT Amount (FC)
  ExtVatSumS Num(19,6) External VAT Amount (SC)
  AcqRevTax nVarChar(8) Acquisition/Reverse Corresponding Tax Code
  VatExmPrc Num(19,6) VAT Exemption %
  VatExmBase Num(19,6) VAT Base %
  RevCharge VarChar(1) Reverse Charge default=N [Y=Yes, N=No]

# UTX2 - Unreported VAT Transactions - Grouped Rows
Module: Finance | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineSeq
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OUTX
  LineSeq Int(11) Row Sequence
  TaxCode nVarChar(8) Tax Code
  VatPercent Num(19,6) VAT Percent
  CrditDebit VarChar(1) Credit or Debit Transaction [C=Credit, D=Debit]
  BaseSum Num(19,6) Base Sum
  BaseSumSc Num(19,6) Base Sum (SC)
  BaseSumFc Num(19,6) Base Sum (FC)
  VatSum Num(19,6) VAT Sum
  VatSumSc Num(19,6) VAT Sum (SC)
  VatSumFc Num(19,6) VAT Sum (FC)
  TODedBaseS Num(19,6) Tax Only Deducted Base Sum
  TODedBaSSC Num(19,6) Tax Only Deducted Base Sum (SC)
  TODedBaSFC Num(19,6) Tax Only Deducted Base Sum (FC)
  LnDataNum Int(11) Row Number in Tax Data default=-1

# UWTX1 - WTax Transactions - Rows
Module: Finance | 54 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineSeq
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OWTX
  LineSeq Int(11) Row Sequence
  SrcArrType Int(11) Source Array Type default=-1 [-1=Default, 1=Main, 12=Array 1, 13=Array 2, 14=Array 3]
  SrcLineNum Int(11) Source Row Number default=-1
  SrcGrpNum Int(11) Source Group Number default=-1 [-1=Default, 0=Group 1, 1=Group 2, 2=Group 3]
  BaseObjTyp nVarChar(20) Base Object Type default=-1
  BaseAbs Int(11) Base Document Internal No. default=-1
  BaseArrTyp Int(11) Base Array Type default=-1 [-1=Default, 1=Main, 12=Array 1, 13=Array 2, 14=Array 3, 15=Array 4, 16=Array 5, 17=Array 6, 18=Array 7, 24=Array 13]
  BaseLinNum Int(11) Base Row Number default=-1
  BaseGrpNum Int(11) Base Group No. default=-1 [-1=Default, 0=Group 1, 1=Group 2, 2=Group 3]
  WTaxAbsId nVarChar(8) Tax Code ID
  Account nVarChar(15) Account ->OACT
  Rate Num(19,6) Rate
  Exemption Num(19,6) Exemption Rate
  BaseType VarChar(1) Base Type default=N [N=Net, V=VAT, G=Gross, H=Gross - VAT]
  BaseNetSum Num(19,6) Base Net Sum
  BaseNetSC Num(19,6) Base Net Sum (SC)
  BaseNetFC Num(19,6) Base Net Sum (FC)
  BaseVatSum Num(19,6) Base VAT Sum
  BaseVatSC Num(19,6) Base VAT Sum (SC)
  BaseVatFC Num(19,6) Base VAT Sum (FC)
  AccBaseSum Num(19,6) Accumulated Sum
  AccBaseSC Num(19,6) Accumulated Sum (SC)
  AccBaseFC Num(19,6) Accumulated Sum (FC)
  AccWTaxSum Num(19,6) Accumulated WTax Sum
  AccWTaxSC Num(19,6) Accumulated WTax Sum (SC)
  AccWTaxFC Num(19,6) Accumulated WTax Sum (FC)
  TxblSum Num(19,6) Taxable Sum
  TxblSumSc Num(19,6) Taxable Sum (SC)
  TxblSumFc Num(19,6) Taxable Sum (FC)
  WTaxSum Num(19,6) WTax Sum
  WTaxSumSc Num(19,6) WTax Sum (SC)
  WTaxSumFc Num(19,6) WTax Sum (FC)
  ApplSum Num(19,6) Applied Sum
  ApplSumSc Num(19,6) Applied Sum (SC)
  ApplSumFc Num(19,6) Applied Sum (FC)
  CrditDebit VarChar(1) Credit or Debit Transaction [C=Credit, D=Debit]
  PostingTyp VarChar(1) Sales or Purchase default=N [N=None, R=Sales, P=Purchase]
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  WTTypeId Int(11) Type
  WhtType VarChar(1) Withholding Type default=V [V=VAT Withholding, G=Gross Income Withholding, N=Income Tax Withholding, S=Social Security Withholding, I=Industry Specific Withholding, D=District Specific Withholding]
  FmlId Int(11) Formula ID
  BaseMin Num(19,6) Min. Amount
  BaseMinSc Num(19,6) Min. Amount (SC)
  BaseMinFc Num(19,6) Min. Amount (FC)
  ResMin Num(19,6) Min.Ret./Perc. Amount
  ResMinSc Num(19,6) Min.Ret./Perc. Amount (SC)
  ResMinFc Num(19,6) Min.Ret./Perc. Amount (FC)
  AddBas Num(19,6) Add to Base Amount
  AddBasSc Num(19,6) Add to Base Amount (SC)
  AddBasFc Num(19,6) Add to Base Amount (FC)
  ABWVAT Num(19,6) Add to Base without VAT Amount
  ABWVATSc Num(19,6) Add to Base without VAT Amount (SC)
  ABWVATFc Num(19,6) Add to Base without VAT Amount (FC)

# VEB1 - VAT Exemptions for Business Partners Row
Module: Finance | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineNum Int(11) Row Number
  ExmpDoc nVarChar(40) Exemption Doc. No.
  IssueDate Date(8) Date of Issue
  IssueTime Int(11) Time of Issue
  ExmpType Int(6) Exemption Type ->OVET
  AllItems VarChar(1) Apply to All Items default=N [Y=Yes, N=No]
  ItemCode nVarChar(50) Item No. ->OITM
  ItemDesc nVarChar(200) Item Description
  Rate Num(19,6) Rate %
  TaxCode nVarChar(8) Exemption Tax Code ->OSTC
  AuthName nVarChar(160) Name of Authorities
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To
  LogInstanc Int(11) Log Instance default=0
  VisOrder Int(11) Visual Order

# VRW1 - VAT Reposting Wizard - Rows 1
Module: Finance | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, VatGroup
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  VatGroup nVarChar(8) VAT Group Code ->OVTG

# VRW2 - VAT Reposting Wizard - Rows 2
Module: Finance | 35 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, TaxInvID, VatGroup, ARINVAbs
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TaxInvID Int(11) A/P Tax Invoice ID ->OTPI
  VatGroup nVarChar(8) VAT Group Code ->OVTG
  Selected VarChar(1) Selected Line default=N [Y=Yes, N=No]
  LineStatus VarChar(1) Line Status default=R [C=Canceled, R=Regular]
  DebitAcc nVarChar(15) Debit Account ->OACT
  DocDate Date(8) Document Date
  VatAmount Num(19,6) VAT Amount
  NetAmount Num(19,6) Net Amount
  JETransID Int(11) Journal Entry Number ->OJDT
  Ref1 nVarChar(100) Reference 1
  Ref2 nVarChar(100) Reference 2
  Ref3 nVarChar(100) Reference 3
  Remarks nVarChar(254) Journal Entry Remarks
  TrnsCode nVarChar(4) Code
  BPLId Int(11) Branch ->OBPL
  ARINVAbs Int(11) First A/R Invoice Abs Entry default=0
  ARDocNumAb nVarChar(20) A/R Document No.
  ARAbsEntry Int(11) A/R Document Abs Entry default=0
  ARObjType nVarChar(20) A/R Document Object Type
  ARDocDate Date(8) A/R Document Date
  CstmrCode nVarChar(15) Customer Code
  CstmrName nVarChar(100) Customer Name
  TpiDocNum Int(11) A/P Tax Invoice No.
  TpiDocDate Date(8) A/P Tax Invoice Posting Date
  VendorCode nVarChar(15) Vendor Code
  VendorName nVarChar(100) Vendor Name
  ARDocMemo nVarChar(254) A/R Document Remarks
  TpiMemo nVarChar(254) A/P Tax Invoice Remarks
  GrsAmt Num(19,6) Gross Amount
  VatAcc nVarChar(15) VAT Account
  OpenVatAmt Num(19,6) Open VAT Amount
  OpenNetAmt Num(19,6) Open Net Amount
  OpenGrsAmt Num(19,6) Open Gross Amount
  RepstedVat Num(19,6) Reposted VAT

# VRW3 - VAT Reposting Wizard - Rows 3
Module: Finance | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CardCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) Customer/Vendor Code ->OCRD

# VTG1 - Tax Definition
Module: Finance | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, EffecDate
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Group Code
  EffecDate Date(8) Effective From
  Rate Num(19,6) Rate
  EquVatPr Num(19,6) Equalization Tax %
  MinAmount Num(19,6) Minimum Stamp Tax Amount
  FixedAmout Num(19,6) Fixed Stamp Tax Amount
  TaxType VarChar(1) Tax Type (VAT or Stamp) default=V [V=VAT, S=Stamp]
  LogInstanc Int(11) Log Instance default=0
  DatevCode Int(6) DATEV Code

# VTR1 - Tax Groups
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ObjectCode, Adtnl_Key
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Abs Entry (Numerator)
  ObjectCode nVarChar(30) Object Code
  Sum VarChar(1) Sum default=N [Y=Yes, N=No]
  DispOrder Int(11) Display Order
  ObjectType VarChar(1) Object Type
  Selected VarChar(1) Selected Object [Y=Yes, N=No]
  FromObject nVarChar(20) From Object
  ToObject nVarChar(20) To Object
  Adtnl_Key VarChar(1) Additional Key
  Amount Num(19,6) Amount

# VTR2 - Doc. Type Filter
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ObjectCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(15) Object Code [13=A/R Invoices, 14=A/R Credit Memos, 18=A/P Invoices, 19=A/P Credit Memos, 24=Incoming Payments, 30=Journal Entries, 46=Outgoing Payments, 57=Checks for Payment, 67=Inventory Transfers, 203=A/R Down Payment, 204=A/P Down Payment]
  FromDocNo Int(11) Doc. Number From
  ToDocNo Int(11) To Doc Number
  Selected VarChar(1) Is Selected Object. default=N [N=No, Y=Yes]

# VTR3 - Series Filter
Module: Finance | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, SeriesCode, ObjectCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(15) Object Code
  SeriesCode Int(11) Series Code

# WHT1 - Withholding Tax Definition
Module: Finance | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LineNum
Fields (name type(len) description [values] ->parent table):
  WTCode nVarChar(4) WTax Code ->OWHT
  EffecDate Date(8) Effective From
  Rate Num(19,6) Rate
  LogInstanc Int(11) Log Instance default=0
  TdsRate Num(19,6) TDS Rate
  SurRate Num(19,6) Surcharge Rate
  CessRate Num(19,6) Cess Rate
  HscRate Num(19,6) HSC Rate
  PmntTerms Int(6) Payment Terms ->OCTG
  LineNum Int(11) Row Number
  IgstRate Num(19,6) IGST Rate
  CgstRate Num(19,6) CGST Rate
  SgstRate Num(19,6) SGST Rate
  UtgstRate Num(19,6) UTGST Rate
  CsgstRate Num(19,6) Cess GST Rate
  UomEntry Int(11) UoM Entry ->OUOM
  UoMCode nVarChar(20) UoM Code
  FixedAmnt Num(19,6) Fixed Amount
  Currency nVarChar(3) Fixed Amount Currency ->OCRN
  ItrNCRate Num(19,6) TDS ITR Noncompliance Rate
  PanNCRate Num(19,6) TDS PAN Noncompliance Rate

# WHT2 - Withholding Tax Definition - Rows2
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum, SeqNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  Code nVarChar(4) Tax Code ->OWHT
  EffectDate Date(8) Date Effective
  Rate Num(19,6) Tax Rate
  MinAmount Num(19,6) Min. Amount
  MaxAmount Num(19,6) Max. Amount
  WTCUR nVarChar(3) Progressive Tax Currency ->OCRN
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number

# WHT3 - Value Range
Module: Finance | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WTCode, LineNum, SeqNum
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  WTCode nVarChar(4) WTax Code ->OWHT
  EfctFrom Date(8) Effective From
  ValueFrom Num(19,6) Value From
  Deduct Num(19,6) WTax to Be Deductible
  Rate Num(19,6) Rate
  WTCur nVarChar(3) Currency
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number

# WTD1 - Withholding Tax Dates
Module: Finance | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineNum Int(11) Row Number
  DateFrom Date(8) Effective From
  Rate Num(19,6) Rate
  LogInstanc Int(11) Log Instance default=0

# WTD2 - Value Ranges
Module: Finance | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum, SeqNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  EfctFrom Date(8) Effective From
  ValueFrom Num(19,6) Value From
  Rate Num(19,6) Rate
  WTCur nVarChar(3) Currency
  LogInstanc Int(11) Log Instance default=0
  LineNum Int(11) Row Number
  SeqNum Int(11) Sequence Number

# WTX1 - WTax Transactions - Rows
Module: Finance | 54 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineSeq
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID ->OWTX
  LineSeq Int(11) Row Sequence
  SrcArrType Int(11) Source Array Type default=-1 [-1=Default, 1=Main, 12=Array 1, 13=Array 2, 14=Array 3]
  SrcLineNum Int(11) Source Row Number default=-1
  SrcGrpNum Int(11) Source Group Number default=-1 [-1=Default, 0=Group 1, 1=Group 2, 2=Group 3]
  BaseObjTyp nVarChar(20) Base Object Type default=-1
  BaseAbs Int(11) Base Document Internal No. default=-1
  BaseArrTyp Int(11) Base Array Type default=-1 [-1=Default, 1=Main, 12=Array 1, 13=Array 2, 14=Array 3, 15=Array 4, 16=Array 5, 17=Array 6, 18=Array 7, 24=Array 13]
  BaseLinNum Int(11) Base Row Number default=-1
  BaseGrpNum Int(11) Base Group No. default=-1 [-1=Default, 0=Group 1, 1=Group 2, 2=Group 3]
  WTaxAbsId nVarChar(8) Tax Code ID
  Account nVarChar(15) Account ->OACT
  Rate Num(19,6) Rate
  Exemption Num(19,6) Exemption Rate
  BaseType VarChar(1) Base Type default=N [N=Net, V=VAT, G=Gross, H=Gross - VAT]
  BaseNetSum Num(19,6) Base Net Sum
  BaseNetSC Num(19,6) Base Net Sum (SC)
  BaseNetFC Num(19,6) Base Net Sum (FC)
  BaseVatSum Num(19,6) Base VAT Sum
  BaseVatSC Num(19,6) Base VAT Sum (SC)
  BaseVatFC Num(19,6) Base VAT Sum (FC)
  AccBaseSum Num(19,6) Accumulated Sum
  AccBaseSC Num(19,6) Accumulated Sum (SC)
  AccBaseFC Num(19,6) Accumulated Sum (FC)
  AccWTaxSum Num(19,6) Accumulated WTax Sum
  AccWTaxSC Num(19,6) Accumulated WTax Sum (SC)
  AccWTaxFC Num(19,6) Accumulated WTax Sum (FC)
  TxblSum Num(19,6) Taxable Sum
  TxblSumSc Num(19,6) Taxable Sum (SC)
  TxblSumFc Num(19,6) Taxable Sum (FC)
  WTaxSum Num(19,6) WTax Sum
  WTaxSumSc Num(19,6) WTax Sum (SC)
  WTaxSumFc Num(19,6) WTax Sum (FC)
  ApplSum Num(19,6) Applied Sum
  ApplSumSc Num(19,6) Applied Sum (SC)
  ApplSumFc Num(19,6) Applied Sum (FC)
  CrditDebit VarChar(1) Credit or Debit Transaction [C=Credit, D=Debit]
  PostingTyp VarChar(1) Sales or Purchase default=N [N=None, R=Sales, P=Purchase]
  Category VarChar(1) Category default=P [I=Invoice, P=Payment]
  WTTypeId Int(11) Type
  WhtType VarChar(1) Withholding Type default=V [V=VAT Withholding, G=Gross Income Withholding, N=Income Tax Withholding, S=Social Security Withholding, I=Industry Specific Withholding, D=District Specific Withholding]
  FmlId Int(11) Formula ID
  BaseMin Num(19,6) Min. Amount
  BaseMinSc Num(19,6) Min. Amount (SC)
  BaseMinFc Num(19,6) Min. Amount (FC)
  ResMin Num(19,6) Min.Ret./Perc. Amount
  ResMinSc Num(19,6) Min.Ret./Perc. Amount (SC)
  ResMinFc Num(19,6) Min.Ret./Perc. Amount (FC)
  AddBas Num(19,6) Add to Base Amount
  AddBasSc Num(19,6) Add to Base Amount (SC)
  AddBasFc Num(19,6) Add to Base Amount (FC)
  ABWVAT Num(19,6) Add to Base without VAT Amount
  ABWVATSc Num(19,6) Add to Base without VAT Amount (SC)
  ABWVATFc Num(19,6) Add to Base without VAT Amount (FC)

# ZRD1 - POS Daily Summary - Totals
Module: Finance | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
  CODE U: Code, AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Internal ID ->OZRD
  LineNum Int(11) Row Number
  Code nVarChar(8) Totalizer Code
  Number Int(11) Totalizer Number
  TotalSum Num(19,6) Total Sum
  Descriptn nVarChar(254) Description
