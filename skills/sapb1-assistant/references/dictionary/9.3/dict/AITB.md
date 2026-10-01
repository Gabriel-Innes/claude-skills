<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AITB - Item Groups - History
Module: Inventory and Production | 82 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: logInstanc, ItmsGrpCod
  GROUP_NAME U: logInstanc, ItmsGrpNam
Fields (name type(len) description [values] ->parent table):
  ItmsGrpCod Int(6) Number
  ItmsGrpNam nVarChar(20) Group Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost Of Goods Sold ->OACT
  TransferAc nVarChar(15) Allocation Acct ->OACT
  RevenuesAc nVarChar(15) Revenue Account ->OACT
  VarianceAc nVarChar(15) Variance Acct ->OACT
  DecreasAc nVarChar(15) Inventory Offset - Decrease ->OACT
  IncreasAc nVarChar(15) Inventory Offset - Increase ->OACT
  ReturnAc nVarChar(15) Sales Returns ->OACT
  ExpensesAc nVarChar(15) Expense Account ->OACT
  EURevenuAc nVarChar(15) Sales Revenue - EU ->OACT
  EUExpensAc nVarChar(15) EU Expense Acct ->OACT
  FrRevenuAc nVarChar(15) Sales Revenue - Foreign ->OACT
  FrExpensAc nVarChar(15) Foreign Expense Acct ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  CycleCode Int(6) Cycle Code ->OCYC
  Alert VarChar(1) Alert default=N [N=No, Y=Yes]
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  ExchangeAc nVarChar(15) Exchange Rate Differences Account ->OACT
  BalanceAcc nVarChar(15) Goods Clearing Acct ->OACT
  PurchaseAc nVarChar(15) Purchase Acct ->OACT
  PAReturnAc nVarChar(15) PA Return Acct ->OACT
  PurchOfsAc nVarChar(15) Purchase Offset Acct ->OACT
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Acct ->OACT
  IncresGlAc nVarChar(15) G/L Increase Acct ->OACT
  InvntSys VarChar(1) Inventory System [A=Moving Average, S=Standard, F=FIFO]
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  StokRvlAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkOffsAct nVarChar(15) Inventory Revaluation Offset Account ->OACT
  WipAcct nVarChar(15) WIP Material Account ->OACT
  WipVarAcct nVarChar(15) WIP Material Variance Account ->OACT
  CostRvlAct nVarChar(15) Cost of Sale Revaluation Acct ->OACT
  CstOffsAct nVarChar(15) Cost of Sales Reval. Offs. Acct ->OACT
  ExpClrAct nVarChar(15) Expenses Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  Object nVarChar(20) Object Type - History default=52
  logInstanc Int(11) Log Instance - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Update Date - History
  ARCMAct nVarChar(15) Sales Credit Acct ->OACT
  ARCMFrnAct nVarChar(15) Sales Credit Foreign Acct ->OACT
  ARCMEUAct nVarChar(15) Sales Credit EU Acct ->OACT
  ARCMExpAct nVarChar(15) Exempted Credits ->OACT
  APCMAct nVarChar(15) Purchase Credit Acct ->OACT
  APCMFrnAct nVarChar(15) Foreign Purchase Credit Acct ->OACT
  APCMEUAct nVarChar(15) EU Purchase Credit Acct ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account ->OACT
  ItemClass VarChar(1) Service or Material default=2 [1=Service, 2=Material]
  OSvcCode Int(11) Outgoing Service Code default=-1 ->OSCD
  ISvcCode Int(11) Incoming Service Code default=-1 ->OSCD
  ServiceGrp Int(11) Service Group default=-1 ->OSGP
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  NegStckAct nVarChar(15) Negative Inventory Adjustment ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Acct ->OACT
  PurBalAct nVarChar(15) Purchase Balance Account ->OACT
  WhICenAct nVarChar(15) Incoming CENVAT Account (WH) ->OACT
  WhOCenAct nVarChar(15) Outgoing CENVAT Account (WH) ->OACT
  WipOffset nVarChar(15) WIP Offset P&L Account ->OACT
  StockOffst nVarChar(15) Inventory Offset P&L Account ->OACT
  UgpEntry Int(11) Default UoM Group Entry ->OUGP
  IUoMEntry Int(11) Default Inventory UoM ->OUOM
  ToleranDay Int(11) Tolerance Days
  RuleCode nVarChar(2) Checking Rule Code ->ODCR
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]
  FreeChrgSA nVarChar(15) Free of Charge Sales Account
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account
  RawMtrl VarChar(1) Raw Material default=N [N=No, Y=Yes]
