<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OACT - G/L Accounts
Module: Finance | 123 columns | ObjType: 1
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
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
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
  PurpCode nVarChar(2) Account Purpose Code [01=Contas de ativo, 02=Contas de Passivo, 03=Patrimônio Líquido, 04=Contas de Resultado, 05=Contas de Compensação, 09=Outras]
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
