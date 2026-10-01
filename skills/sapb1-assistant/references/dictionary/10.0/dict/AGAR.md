<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
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
