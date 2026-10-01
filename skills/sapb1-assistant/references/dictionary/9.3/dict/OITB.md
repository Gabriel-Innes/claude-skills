<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OITB - Item Groups
Module: Inventory and Production | 82 columns | ObjType: 52
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ItmsGrpCod
  GROUP_NAME U: ItmsGrpNam
Fields (name type(len) description [values] ->parent table):
  ItmsGrpCod Int(6) Number
  ItmsGrpNam nVarChar(20) Group Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  BalInvntAc nVarChar(15) Inventory Account ->OACT
  SaleCostAc nVarChar(15) Cost of Goods Sold Account ->OACT
  TransferAc nVarChar(15) Allocation Account ->OACT
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
  CycleCode Int(6) Cycle Code ->OCYC
  Alert VarChar(1) Alert default=N [N=No, Y=Yes]
  PriceDifAc nVarChar(15) Price Difference Account ->OACT
  ExchangeAc nVarChar(15) Exchange Rate Differences Account ->OACT
  BalanceAcc nVarChar(15) Goods Clearing Account ->OACT
  PurchaseAc nVarChar(15) Purchase Account ->OACT
  PAReturnAc nVarChar(15) Purchase Return Account ->OACT
  PurchOfsAc nVarChar(15) Purchase Offset Account ->OACT
  ShpdGdsAct nVarChar(15) Shipped Goods Account ->OACT
  VatRevAct nVarChar(15) VAT in Revenue Account ->OACT
  DecresGlAc nVarChar(15) G/L Decrease Account ->OACT
  IncresGlAc nVarChar(15) G/L Increase Account ->OACT
  InvntSys VarChar(1) Inventory System [A=Moving Average, S=Standard, F=FIFO]
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  StokRvlAct nVarChar(15) Inventory Revaluation Account ->OACT
  StkOffsAct nVarChar(15) Inventory Revaluation Offset Account ->OACT
  WipAcct nVarChar(15) WIP Inventory Account ->OACT
  WipVarAcct nVarChar(15) WIP Inventory Variance Account ->OACT
  CostRvlAct nVarChar(15) COGS Revaluation Account ->OACT
  CstOffsAct nVarChar(15) COGS Revaluation Offset Acct ->OACT
  ExpClrAct nVarChar(15) Expense Clearing Account ->OACT
  ExpOfstAct nVarChar(15) Expense Offset Account ->OACT
  Object nVarChar(20) Object Type - History default=52
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
  ItemClass VarChar(1) Service or Material default=2 [1=Service, 2=Material]
  OSvcCode Int(11) Outgoing Service Code default=-1 ->OSCD
  ISvcCode Int(11) Incoming Service Code default=-1 ->OSCD
  ServiceGrp Int(11) Service Group default=-1 ->OSGP
  NCMCode Int(11) NCM Code default=-1 ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  NegStckAct nVarChar(15) Negative Inventory Adjustment Acct ->OACT
  StkInTnAct nVarChar(15) Stock In Transit Account ->OACT
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
  FreeChrgSA nVarChar(15) Free of Charge Sales Account ->OACT
  FreeChrgPU nVarChar(15) Free of Charge Purchase Account ->OACT
  RawMtrl VarChar(1) Raw Material default=N [N=No, Y=Yes]
