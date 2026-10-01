<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OACP - Periods Category
Module: Finance | 180 columns | ObjType: 220
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
