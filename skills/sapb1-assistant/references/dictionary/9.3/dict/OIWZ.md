<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OIWZ - Inflation Wizard
Module: Finance | 35 columns | ObjType: 195
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  WizName nVarChar(100) Wizard Name
  PostDateTo Date(8) Posting Date To
  WizType VarChar(1) Wizard Type [1=GL Account Revaluation Wizard, 2=Inventory Revaluation Wizard, 3=COGS Revaluation Wizard]
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
