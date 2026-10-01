<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# OWHS - Warehouses
Module: Inventory and Production | 103 columns | ObjType: 64
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WhsCode
  DFT_BIN: DftBinAbs
Fields (name type(len) description [values] ->parent table):
  WhsCode nVarChar(8) Warehouse Code
  WhsName nVarChar(100) Warehouse Name
  IntrnalKey Int(11) Internal Key
  Grp_Code nVarChar(4) Group Code
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Allocation Account ->OACT
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
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
  VatGroup nVarChar(8) Tax Group ->OSTC
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County ->OCNT
  Country nVarChar(3) Country/Region ->OCRY
  State nVarChar(3) State ->OCST
  Location Int(11) Location ->OLCT
  DropShip VarChar(1) Drop-Ship default=N [N=No, Y=Yes]
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  UseTax VarChar(1) Allow Use Tax default=N [Y=Yes, N=No]
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  ExchangeAc nVarChar(15) Exchange Rate Differences Account ->OACT
  BalanceAcc nVarChar(15) Goods Clearing Account ->OACT
  PurchaseAc nVarChar(15) Purchase Account ->OACT
  PAReturnAc nVarChar(15) Purchase Return Account ->OACT
  PurchOfsAc nVarChar(15) Purchase Offset Account ->OACT
  FedTaxID nVarChar(32) Federal Tax ID
  Building Text(16) Building/Floor/Room
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  Nettable VarChar(1) Nettable default=Y [Y=Yes, N=No]
  StokRvlAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkOffsAct nVarChar(15) Inventory Revaluation Offset Account ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  CostRvlAct nVarChar(15) COGS Revaluation Account ->OACT
  CstOffsAct nVarChar(15) COGS Revaluation Offset Acct ->OACT
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  objType nVarChar(20) Object Type - History default=64
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  ARCMAct nVarChar(15) Sales Credit Account ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Account - Foreign ->OACT
  ARCMEUAct nVarChar(15) Sales Credit Account - EU ->OACT
  ARCMExpAct nVarChar(15) Tax Exempt Credit Account ->OACT
  APCMAct nVarChar(15) Purchase Credit Account ->OACT
  APCMFrnAct nVarChar(15) Purchase Credit Account - Foreign ->OACT
  APCMEUAct nVarChar(15) Purchase Credit Account - EU ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account ->OACT
  BPLid Int(11) Business Place ID ->OBPL
  OwnerCode VarChar(1) Owner Code default=1 [1=Company Item Property, 2=Third-Party Warehouse, 3=Third-Party Item in my Property]
  NegStckAct nVarChar(15) Negative Inventory Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account ->OACT
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  Excisable VarChar(1) Excisable [Yes/No] default=N [Y=Yes, N=No]
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WhShipTo nVarChar(100) Ship-to Name (WH)
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  StorKeeper Int(11) Storekeeper ->OHEM
  Shipper nVarChar(15) Shipper ->OCRD
  BinActivat VarChar(1) Bin Activated [Y/N] default=N [Y=Yes, N=No]
  BinSeptor nVarChar(5) Bin Separator default=-
  DftBinAbs Int(11) Default Bin Internal Number ->OBIN
  DftBinEnfd VarChar(1) Default Bin Enforced [Y/N] default=N [Y=Yes, N=No]
  AutoIssMtd Int(6) Auto. Issue Method default=0 [0=Single Choice, 1=Bin Location Code Order, 2=Alternative Sort Code Order, 3=Descending Quantity, 4=Ascending Quantity, 7=Ascending Quantity - Single Bin Preferred, 5=FIFO, 6=LIFO]
  ManageSnB VarChar(1) Drop-Ship Manage SnB default=N [N=No, Y=Yes]
  RecItemsBy Int(6) Receiving Bin Locations Method default=0 [0=Bin Location Code Order, 1=Alternative Sort Code Order]
  RecBinEnab VarChar(1) Enable Receiving Bin Locations default=N [Y=Yes, N=No]
  GlblLocNum nVarChar(50) Global Location Number
  RecvEmpBin VarChar(1) Restrict Receipts to Empty Bin default=Y [Y=Yes, N=No]
  Inactive VarChar(1) Inactive default=N [Y=Yes, N=No]
  RecvMaxQty VarChar(1) Recv. up to Max. Qty default=N [Y=Yes, N=No]
  AutoRecvMd Int(6) Auto. Receipt Method default=0 [0=Default Bin Location, 1=Last Bin Location That Received Item, 2=Item's Current Bin Locations, 3=Item's Current and Historical Bin Locations]
  RecvMaxWT VarChar(1) Recv. up to Max. Weight default=N [Y=Yes, N=No]
  RecvUpTo nVarChar(6) Receive up to default=0 [0=Maximum Qty, 1=Maximum Weight, 2=Max. Qty and Weight]
  FreeChrgSA nVarChar(15) Free of Charge Sales Account ->OACT
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account ->OACT
  TaxOffice nVarChar(50) Tax Office
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  External VarChar(1) External default=N [N=No, Y=Yes]
  LegalText nVarChar(250) Legal Text
