<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# UITW - Items - Warehouse
Module: Inventory and Production | 73 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WhsCode, ItemCode
  WHS: WhsCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->UITM
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Defined
  OnOrder Num(19,6) Ordered
  Consig Num(19,6) Consignment Goods Whse
  Counted Num(19,6) Counted Quantity
  WasCounted VarChar(1) Counted Yes/No default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  MinStock Num(19,6) Minimum Inventory
  MaxStock Num(19,6) Maximum Inventory
  MinOrder Num(19,6) Min. Order
  AvgPrice Num(19,6) Average Price
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Transfer Acct ->OACT
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Account ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease Account ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase Account ->OACT
  ReturnAc nVarChar(15) Sales Returns Account ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Revenue Account - EU ->OACT
  EUExpensAc nVarChar(15) Expense Account - EU ->OACT
  FrRevenuAc nVarChar(15) Revenue Account - Foreign ->OACT
  FrExpensAc nVarChar(15) Expense Account - Foreign ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  PriceDifAc nVarChar(15) Price Differences Account
  ExchangeAc nVarChar(15) Exchange Rate Differences Account
  BalanceAcc nVarChar(15) Goods Clearing Account
  PurchaseAc nVarChar(15) Purchase Account
  PAReturnAc nVarChar(15) Purchase Return Account
  PurchOfsAc nVarChar(15) Purchase Offset Account
  ShpdGdsAct nVarChar(15) Shipped Goods Account
  VatRevAct nVarChar(15) VAT in Revenue Account
  StockValue Num(19,6) Inventory Value
  DecresGlAc nVarChar(15) G/L Decrease Account
  IncresGlAc nVarChar(15) G/L Increase Account
  StokRvlAct nVarChar(15) Stock Inflation Adjust Account
  StkOffsAct nVarChar(15) Stock Inflation Offset Account
  WipAcct nVarChar(15) WIP Inventory Account
  WipVarAcct nVarChar(15) WIP Inventory Variance Account
  CostRvlAct nVarChar(15) Cost Inflation Account
  CstOffsAct nVarChar(15) Cost Inflation Offset Account
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  Object nVarChar(20) Object Type - History default=31
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  ARCMAct nVarChar(15) Sales Credit Account
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign
  ARCMEUAct nVarChar(15) Sales Credit Account - EU
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account
  APCMAct nVarChar(15) Purchase Credit Account
  APCMFrnAct nVarChar(15) Purchase Credit Account - Foreign
  APCMEUAct nVarChar(15) Purchase Credit Account - EU
  RevRetAct nVarChar(15) Revenue Returns Account
  NegStckAct nVarChar(15) Neg. Inventory Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account
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
