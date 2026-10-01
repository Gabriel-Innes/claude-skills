<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AITW - Items - Warehouse - History
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: logInstanc, WhsCode, ItemCode
  ITEM: ItemCode
  WHS: WhsCode
  COUNTED: WasCounted
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Defined
  OnOrder Num(19,6) Ordered
  Consig Num(19,6) Consignment Goods WH
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  MinStock Num(19,6) Min. Stock
  MaxStock Num(19,6) Max. Stock
  MinOrder Num(19,6) Min. Order
  AvgPrice Num(19,6) Average Price
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  BalInvntAc nVarChar(15) Inventory Acc. ->OACT
  SaleCostAc nVarChar(15) Cost Acc. ->OACT
  TransferAc nVarChar(15) Transfers Acc. ->OACT
  RevenuesAc nVarChar(15) Revenues Acct ->OACT
  VarianceAc nVarChar(15) Variance Acc. ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns ->OACT
  ExpensesAc nVarChar(15) Expenses Acct. ->OACT
  EURevenuAc nVarChar(15) Sales Revenue - EU ->OACT
  EUExpensAc nVarChar(15) EU Expenses Acc. ->OACT
  FrRevenuAc nVarChar(15) Sales Revenue - Foreign ->OACT
  FrExpensAc nVarChar(15) Foreign Expenses Acc. ->OACT
  ExmptIncom nVarChar(15) Exempt Revenues Account ->OACT
  PriceDifAc nVarChar(15) Price Differences Acc.
  ExchangeAc nVarChar(15) Exchange Rate Differences Acc.
  BalanceAcc nVarChar(15) Goods Clearing Acc.
  PurchaseAc nVarChar(15) Purchase Acc.
  PAReturnAc nVarChar(15) PA Return Acc.
  PurchOfsAc nVarChar(15) Purchase Offset Acc.
  ShpdGdsAct nVarChar(15) Shipped Goods Account
  VatRevAct nVarChar(15) VAT in Revenue Account
  StockValue Num(19,6) Stock Value
  DecresGlAc nVarChar(15) Decrease GL Acc.
  IncresGlAc nVarChar(15) Increase GL Acc.
  StokRvlAct nVarChar(15) Stock Inflation Adjust Account
  StkOffsAct nVarChar(15) Stock Inflation Offset Account
  WipAcct nVarChar(15) WIP Material Account
  WipVarAcct nVarChar(15) WIP Material Variance Account
  CostRvlAct nVarChar(15) Cost Inflation Account
  CstOffsAct nVarChar(15) Cost Inflation Offset Account
  ExpClrAct nVarChar(15) Expenses Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offsetting Account ->OACT
  Object nVarChar(20) Object Type - History default=31
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Update Date - History
  ARCMAct nVarChar(15) Sales Credit Acct
  ARCMFrnAct nVarChar(15) Sales Credit Foreign Acct
  ARCMEUAct nVarChar(15) Sales Credit EU Acct
  ARCMExpAct nVarChar(15) Exempted Credits
  APCMAct nVarChar(15) Purchase Credit Acct
  APCMFrnAct nVarChar(15) Foreign Purchase Credit Acct
  APCMEUAct nVarChar(15) EU Purchase Credit Acct
  RevRetAct nVarChar(15) Revenue Returns Account
  NegStckAct nVarChar(15) Negative Stock Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Acct
  PurBalAct nVarChar(15) Purchase Balance Account
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  Freezed VarChar(1) Item Frozen in Warehouse default=N [Y=Yes, N=No]
  FreezeDoc Int(11) INC Document Frozen By ->OINC
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account
