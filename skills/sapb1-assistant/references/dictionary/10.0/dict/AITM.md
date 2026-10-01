<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# AITM - Items - History
Module: Inventory and Production | 332 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, LogInstanc
  ITEM_NAME: ItemName
  TREE_TYPE: TreeType
  COM_GROUP: CommisGrp
  SALE: SellItem
  PURCHASE: PrchseItem
  INVENTORY: InvntItem
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item Number
  ItemName nVarChar(200) Item Description
  FrgnName nVarChar(200) Foreign Name
  ItmsGrpCod Int(6) Item Group default=100 ->OITB
  CstGrpCode Int(6) Customs Group default=-1 ->OARG
  VatGourpSa nVarChar(8) Tax Definition ->OVTG
  CodeBars nVarChar(254) Bar Code
  VATLiable VarChar(1) Tax Liable default=Y [Y=Yes, N=No]
  PrchseItem VarChar(1) Purchasing Item default=Y [Y=Yes, N=No]
  SellItem VarChar(1) Sales Item default=Y [Y=Yes, N=No]
  InvntItem VarChar(1) Inventory Item default=Y [Y=Yes, N=No]
  OnHand Num(19,6) In Stock
  IsCommited Num(19,6) Qty Ordered by Customers
  OnOrder Num(19,6) Qty Ordered from Vendors
  IncomeAcct nVarChar(15) Revenue Account ->OACT
  ExmptIncom nVarChar(15) Exempt Revenue Account ->OACT
  MaxLevel Num(19,6) Free1
  DfltWH nVarChar(8) Default Whse
  CardCode nVarChar(15) Preferred Vendor ->OCRD
  SuppCatNum nVarChar(50) Mfr Catalog No.
  BuyUnitMsr nVarChar(100) Purchasing UoM default=Unit
  NumInBuy Num(19,6) Items per Purchasing Unit
  ReorderQty Num(19,6) Required (Purchasing UoM)
  MinLevel Num(19,6) Minimum Inventory Level
  LstEvlPric Num(19,6) Last Evaluated Price
  LstEvlDate Date(8) Date of Last Revaluation Price
  CustomPer Num(19,6) Customs Rate
  Canceled VarChar(1) Canceled Item [Yes/No] default=N [Y=Yes, N=No]
  MnufctTime Int(11) Production Date
  WholSlsTax VarChar(1) Tax Rate for Wholesaler
  RetilrTax VarChar(1) Sales Tax %
  SpcialDisc Num(19,6) Special Discount %
  DscountCod Int(6) Discount Code
  TrackSales VarChar(1) Follow-Up [Yes/No] default=N [Y=Yes, N=No]
  SalUnitMsr nVarChar(100) Sales UoM default=Unit
  NumInSale Num(19,6) No. of Items per Sales Unit
  Consig Num(19,6) Consignment Goods Whse
  QueryGroup Int(11) Properties default=0
  Counted Num(19,6) Counted Qty
  OpenBlnc Num(19,6) Opening Stock
  EvalSystem VarChar(1) Valuation Method [A=Moving Average, S=Standard, F=FIFO, B=Serial/Batch]
  UserSign Int(6) User Signature ->OUSR
  FREE VarChar(1) Free Item [Y/N] default=N [Y=Yes, N=No]
  PicturName nVarChar(200) Picture
  Transfered VarChar(1) Year Transferred [Y/N] default=N [Y=Yes, N=No]
  BlncTrnsfr VarChar(1) Balances Transferred [Y/N] default=N [Y=Yes, N=No]
  UserText Text(16) Item Remarks
  SerialNum nVarChar(17) Serial Number
  CommisPcnt Num(19,6) Commission % for Item
  CommisSum Num(19,6) Total Commission for Item
  CommisGrp Int(6) Commission Group default=0 ->OCOG
  TreeType VarChar(1) Bill of Materials Type default=N [N=Not a BOM, A=Assembly, S=Sales, P=Production, T=Template]
  TreeQty Num(19,6) No. of Units
  LastPurPrc Num(19,6) Last Purchase Price
  LastPurCur nVarChar(3) Last Purchase Currency
  LastPurDat Date(8) Last Purchase Date
  ExitCur nVarChar(3) Release Currency
  ExitPrice Num(19,6) Release Price
  ExitWH nVarChar(8) Release Warehouse
  AssetItem VarChar(1) Fixed Asset Indicator default=N [Y=Yes, N=No]
  WasCounted VarChar(1) Counted default=N [Y=Yes, N=No]
  ManSerNum VarChar(1) Serial No. Management default=N [Y=Yes, N=No]
  SHeight1 Num(19,6) Height 1 - Sales Unit
  SHght1Unit Int(6) Height 1 - UoM for Sales
  SHeight2 Num(19,6) Height 2 - Sales Unit
  SHght2Unit Int(6) Height 2 - UoM for Sales
  SWidth1 Num(19,6) Width 1 - Sales Unit
  SWdth1Unit Int(6) Width 1 - UoM for Sales
  SWidth2 Num(19,6) Width 2 - Sales Unit
  SWdth2Unit Int(6) Width 2 - UoM for Sales
  SLength1 Num(19,6) Length 1 - Sales Unit
  SLen1Unit Int(6) Length 1 - UoM for Sales
  Slength2 Num(19,6) Length 2 - Sales Unit
  SLen2Unit Int(6) Length 2 - UoM for Sales
  SVolume Num(19,6) Volume - Sales Unit
  SVolUnit Int(6) Volume - UoM for Sales
  SWeight1 Num(19,6) Weight 1 - Sales Unit
  SWght1Unit Int(6) Weight 1 - UoM for Sales
  SWeight2 Num(19,6) Weight 2 - Sales Unit
  SWght2Unit Int(6) Weight 2 - UoM for Sales
  BHeight1 Num(19,6) Height 1 - Purchasing Unit
  BHght1Unit Int(6) Height 1 - UoM for Purchasing
  BHeight2 Num(19,6) Height 2 - Purchasing Unit
  BHght2Unit Int(6) Height 2 - UoM for Purchasing
  BWidth1 Num(19,6) Width 1 - Purchasing Unit
  BWdth1Unit Int(6) Width 1 - UoM for Purchasing
  BWidth2 Num(19,6) Width 2 - Purchasing Unit
  BWdth2Unit Int(6) Width 2 - UoM for Purchasing
  BLength1 Num(19,6) Length 1 - Purchase Unit
  BLen1Unit Int(6) Length 1 - UoM for Purchasing
  Blength2 Num(19,6) Length 2 - Purchasing Unit
  BLen2Unit Int(6) Length 2 - UoM for Purchasing
  BVolume Num(19,6) Volume - Purchasing Unit
  BVolUnit Int(6) Volume - UoM for Purchasing
  BWeight1 Num(19,6) Weight 1 - Purchasing Unit
  BWght1Unit Int(6) Weight 1 - UoM for Purchasing
  BWeight2 Num(19,6) Weight 2 - Purchasing Unit
  BWght2Unit Int(6) Weight 2 - UoM for Purchasing
  FixCurrCms nVarChar(3) Currency of Fixed Commission
  FirmCode Int(6) Manufacturer default=-1 ->OMRC
  LstSalDate Date(8) Last Sale Date
  QryGroup1 VarChar(1) Property 1 default=N [Y=Yes, N=No]
  QryGroup2 VarChar(1) Property 2 default=N [Y=Yes, N=No]
  QryGroup3 VarChar(1) Property 3 default=N [Y=Yes, N=No]
  QryGroup4 VarChar(1) Property 4 default=N [Y=Yes, N=No]
  QryGroup5 VarChar(1) Property 5 default=N [Y=Yes, N=No]
  QryGroup6 VarChar(1) Property 6 default=N [Y=Yes, N=No]
  QryGroup7 VarChar(1) Property 7 default=N [Y=Yes, N=No]
  QryGroup8 VarChar(1) Property 8 default=N [Y=Yes, N=No]
  QryGroup9 VarChar(1) Property 9 default=N [Y=Yes, N=No]
  QryGroup10 VarChar(1) Property 10 default=N [Y=Yes, N=No]
  QryGroup11 VarChar(1) Property 11 default=N [Y=Yes, N=No]
  QryGroup12 VarChar(1) Property 12 default=N [Y=Yes, N=No]
  QryGroup13 VarChar(1) Property 13 default=N [Y=Yes, N=No]
  QryGroup14 VarChar(1) Property 14 default=N [Y=Yes, N=No]
  QryGroup15 VarChar(1) Property 15 default=N [Y=Yes, N=No]
  QryGroup16 VarChar(1) Property 16 default=N [Y=Yes, N=No]
  QryGroup17 VarChar(1) Property 17 default=N [Y=Yes, N=No]
  QryGroup18 VarChar(1) Property 18 default=N [Y=Yes, N=No]
  QryGroup19 VarChar(1) Property 19 default=N [Y=Yes, N=No]
  QryGroup20 VarChar(1) Property 20 default=N [Y=Yes, N=No]
  QryGroup21 VarChar(1) Property 21 default=N [Y=Yes, N=No]
  QryGroup22 VarChar(1) Property 22 default=N [Y=Yes, N=No]
  QryGroup23 VarChar(1) Property 23 default=N [Y=Yes, N=No]
  QryGroup24 VarChar(1) Property 24 default=N [Y=Yes, N=No]
  QryGroup25 VarChar(1) Property 25 default=N [Y=Yes, N=No]
  QryGroup26 VarChar(1) Property 26 default=N [Y=Yes, N=No]
  QryGroup27 VarChar(1) Property 27 default=N [Y=Yes, N=No]
  QryGroup28 VarChar(1) Property 28 default=N [Y=Yes, N=No]
  QryGroup29 VarChar(1) Property 29 default=N [Y=Yes, N=No]
  QryGroup30 VarChar(1) Property 30 default=N [Y=Yes, N=No]
  QryGroup31 VarChar(1) Property 31 default=N [Y=Yes, N=No]
  QryGroup32 VarChar(1) Property 32 default=N [Y=Yes, N=No]
  QryGroup33 VarChar(1) Property 33 default=N [Y=Yes, N=No]
  QryGroup34 VarChar(1) Property 34 default=N [Y=Yes, N=No]
  QryGroup35 VarChar(1) Property 35 default=N [Y=Yes, N=No]
  QryGroup36 VarChar(1) Property 36 default=N [Y=Yes, N=No]
  QryGroup37 VarChar(1) Property 37 default=N [Y=Yes, N=No]
  QryGroup38 VarChar(1) Property 38 default=N [Y=Yes, N=No]
  QryGroup39 VarChar(1) Property 39 default=N [Y=Yes, N=No]
  QryGroup40 VarChar(1) Property 40 default=N [Y=Yes, N=No]
  QryGroup41 VarChar(1) Property 41 default=N [Y=Yes, N=No]
  QryGroup42 VarChar(1) Property 42 default=N [Y=Yes, N=No]
  QryGroup43 VarChar(1) Property 43 default=N [Y=Yes, N=No]
  QryGroup44 VarChar(1) Property 44 default=N [Y=Yes, N=No]
  QryGroup45 VarChar(1) Property 45 default=N [Y=Yes, N=No]
  QryGroup46 VarChar(1) Property 46 default=N [Y=Yes, N=No]
  QryGroup47 VarChar(1) Property 47 default=N [Y=Yes, N=No]
  QryGroup48 VarChar(1) Property 48 default=N [Y=Yes, N=No]
  QryGroup49 VarChar(1) Property 49 default=N [Y=Yes, N=No]
  QryGroup50 VarChar(1) Property 50 default=N [Y=Yes, N=No]
  QryGroup51 VarChar(1) Property 51 default=N [Y=Yes, N=No]
  QryGroup52 VarChar(1) Property 52 default=N [Y=Yes, N=No]
  QryGroup53 VarChar(1) Property 53 default=N [Y=Yes, N=No]
  QryGroup54 VarChar(1) Property 54 default=N [Y=Yes, N=No]
  QryGroup55 VarChar(1) Property 55 default=N [Y=Yes, N=No]
  QryGroup56 VarChar(1) Property 56 default=N [Y=Yes, N=No]
  QryGroup57 VarChar(1) Property 57 default=N [Y=Yes, N=No]
  QryGroup58 VarChar(1) Property 58 default=N [Y=Yes, N=No]
  QryGroup59 VarChar(1) Property 59 default=N [Y=Yes, N=No]
  QryGroup60 VarChar(1) Property 60 default=N [Y=Yes, N=No]
  QryGroup61 VarChar(1) Property 61 default=N [Y=Yes, N=No]
  QryGroup62 VarChar(1) Property 62 default=N [Y=Yes, N=No]
  QryGroup63 VarChar(1) Property 63 default=N [Y=Yes, N=No]
  QryGroup64 VarChar(1) Property 64 default=N [Y=Yes, N=No]
  CreateDate Date(8) Production Date
  UpdateDate Date(8) Date of Update
  ExportCode nVarChar(20) Data Export Code
  SalFactor1 Num(19,6) Sales Factor 1
  SalFactor2 Num(19,6) Sales Factor 2
  SalFactor3 Num(19,6) Sales Factor 3
  SalFactor4 Num(19,6) Sales Factor 4
  PurFactor1 Num(19,6) Purchasing Factor 1
  PurFactor2 Num(19,6) Purchasing Factor 2
  PurFactor3 Num(19,6) Purchasing Factor 3
  PurFactor4 Num(19,6) Purchasing Factor 4
  SalFormula nVarChar(40) Sales Formula
  PurFormula nVarChar(40) Purchasing Formula
  VatGroupPu nVarChar(8) Purchasing Tax Definition ->OVTG
  AvgPrice Num(19,6) Item Cost
  PurPackMsr nVarChar(30) Packaging UoM (Purchasing) default=Box
  PurPackUn Num(19,6) Quantity per Package (Purchasing)
  SalPackMsr nVarChar(30) Packaging UoM (Sales) default=Box
  SalPackUn Num(19,6) Quantity per Package (Sales)
  SCNCounter Int(6) SCN Counter
  ManBtchNum VarChar(1) Manage Batch No. [Yes/No] default=N [Y=Yes, N=No]
  ManOutOnly VarChar(1) Manage SN on Release Only default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer, G=Fixed Assets Migration]
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  BlockOut VarChar(1) Force Selection of Serial No. or Batch No. default=Y [Y=Yes, N=No]
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type ->ADP1
  SWW nVarChar(16) Additional Identifier
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  DocEntry Int(11) Numerator
  ExpensAcct nVarChar(15) Expense Account ->OACT
  FrgnInAcct nVarChar(15) Revenue Account - Foreign ->OACT
  ShipType Int(6) Shipping Type ->OSHP
  GLMethod VarChar(1) Set G/L Accounts By default=W [W=Warehouse, C=Item Group, L=Item Level]
  ECInAcct nVarChar(15) Revenue Account - EU
  FrgnExpAcc nVarChar(15) Expense Account - Foreign
  ECExpAcc nVarChar(15) Expense Account - EU
  TaxType VarChar(1) Tax Type default=Y [Y=Regular Tax, U=Use Tax, N=No Tax]
  ByWh VarChar(1) Manage Inventory by Warehouse
  WTLiable VarChar(1) Withholding Tax Liable default=Y [Y=Yes, N=No]
  ItemType VarChar(1) Item Type default=I [I=Items, L=Labor, T=Travel, F=Fixed Assets]
  WarrntTmpl nVarChar(20) Warranty Template ->OCTT
  BaseUnit nVarChar(20) Base Unit Name
  CountryOrg nVarChar(3) Country/Region of Origin
  StockValue Num(19,6) Inventory Value
  Phantom VarChar(1) Phantom Item default=N [Y=Yes, N=No]
  IssueMthd VarChar(1) Issue Method default=B [B=Backflush, M=Manual]
  FREE1 VarChar(1) Yield in %
  PricingPrc Num(19,6) Pricing Percentage
  MngMethod VarChar(1) Management Method default=R [A=On Every Transaction, R=On Release Only]
  ReorderPnt Num(19,6) Reorder Point
  InvntryUom nVarChar(100) Inventory UoM
  PlaningSys VarChar(1) Planning Method default=N [M=MRP, N=None]
  PrcrmntMtd VarChar(1) Procurement Method default=B [B=Buy, M=Make]
  OrdrIntrvl Int(6) Order Interval ->OCYC
  OrdrMulti Num(19,6) Order Multiple
  MinOrdrQty Num(19,6) Minimum Order Quantity
  LeadTime Int(11) Lead Time
  IndirctTax VarChar(1) Indirect Tax default=N [Y=Yes, N=No]
  TaxCodeAR nVarChar(8) Sales Tax Code ->OSTC
  TaxCodeAP nVarChar(8) Purchasing Tax Code ->OSTC
  OSvcCode Int(11) Outgoing Service Code ->OSCD
  ISvcCode Int(11) Incoming Service Code ->OSCD
  ServiceGrp Int(11) Service Group ->OSGP
  NCMCode Int(11) NCM Code ->ONCM
  MatType nVarChar(3) Material Type default=1 ->OMTP
  MatGrp Int(11) Material Group default=-1 ->OMGP
  ProductSrc nVarChar(2) Product Source default=0 ->OPSC
  ServiceCtg Int(11) Service Category default=-1 [-1=] ->OSCG
  ItemClass VarChar(1) Service or Material default=2 [2=Material, 1=Service]
  Excisable VarChar(1) Excisable [Yes/No] default=N [Y=Yes, N=No]
  ChapterID Int(11) Chapter ID default=-1 ->OCHP
  NotifyASN nVarChar(40) Notification Availed SN.
  ProAssNum nVarChar(20) Provisional Assessment No.
  AssblValue Num(19,6) Assessable Value
  DNFEntry Int(11) DNF Code Entry default=-1 ->ODNF
  UserSign2 Int(6) Updating User ->OUSR
  Spec nVarChar(30) Item Specification
  TaxCtg nVarChar(4) Tax Category
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  FuelCode Int(11) Fuel default=-1 ->OBFI
  BeverTblC nVarChar(2) Beverage Table ->OBSI
  BeverGrpC nVarChar(2) Beverage Group ->OBSI
  BeverTM Int(11) Beverage Brand default=-1 ->OBNI
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  ToleranDay Int(11) Tolerance Days
  UgpEntry Int(11) UoM Group ->OUGP
  PUoMEntry Int(11) Default Purchasing UoM ->OUOM
  SUoMEntry Int(11) Default Sales UoM ->OUOM
  IUoMEntry Int(11) Inventory UoM ->OUOM
  IssuePriBy Int(6) Issue Primarily By SnB or Bin [0=Issue Primarily by Serial/Batch Number, 1=Issue Primarily by Bin Location]
  AssetClass nVarChar(20) Asset Class ->OACS
  AssetGroup nVarChar(15) Asset Group ->OAGS
  InventryNo nVarChar(12) Inventory Number of Asset
  Technician Int(11) Technician of Fixed Asset ->OHEM
  Employee Int(11) Employee of Fixed Asset ->OHEM
  Location Int(11) Location ->OLCT
  StatAsset VarChar(1) Owned by Company default=N [Y=Yes, N=No]
  Cession VarChar(1) Cession default=N [Y=Yes, N=No]
  DeacAftUL VarChar(1) Deactivate After Useful Life default=N [Y=Yes, N=No]
  AsstStatus VarChar(1) Asset Status default=N [N=New, A=Active, I=Inactive]
  CapDate Date(8) Capitalization Date
  AcqDate Date(8) Acquisition Date
  RetDate Date(8) Retirement Date
  GLPickMeth VarChar(1) G/L Account Pick Method default=A [A=General, W=Warehouse, C=Item Group]
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  MgrByQty VarChar(1) Manage Asset by Quantity default=N [Y=Yes, N=No]
  AssetRmk1 nVarChar(100) Asset Remark 1
  AssetRmk2 nVarChar(100) Asset Remark 2
  AssetAmnt1 Num(19,6) Asset Amount 1
  AssetAmnt2 Num(19,6) Asset Amount 2
  DeprGroup nVarChar(15) Depreciation Group ->OADG
  AssetSerNo nVarChar(32) Asset Serial Number
  CntUnitMsr nVarChar(100) Inventory Counting UoM Name
  NumInCnt Num(19,6) No. of Items per Counting Unit
  INUoMEntry Int(11) Inventory Counting UoM Entry ->OUOM
  OneBOneRec VarChar(1) One Batch One Receipt default=N [Y=Yes, N=No]
  RuleCode nVarChar(2) Checking Rule Code ->ODCR
  ScsCode nVarChar(10) Scs Code
  SpProdType nVarChar(2) Special Product Type [MT=Cellular Phones, IO=Integrated Circuits]
  IWeight1 Num(19,6) Weight 1 - Inventory
  IWght1Unit Int(6) Weight 1 - Inventory Unit
  IWeight2 Num(19,6) Weight 2 - Inventory
  IWght2Unit Int(6) Weight 2 - Inventory Unit
  CompoWH VarChar(1) Component Warehouse default=B [B=From Bill of Materials Line, P=From Parent Item Document Line]
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  VirtAstItm VarChar(1) Virtual Asset Item default=N [N=No, Y=Yes]
  SouVirAsst nVarChar(50) Source Virtual Asset Item ->OITM
  InCostRoll VarChar(1) Include in Prod. Cost Rollup default=Y [Y=Yes, N=No]
  PrdStdCst Num(19,6) Production Std Cost
  EnAstSeri VarChar(1) Enforce Asset Serial Numbers default=N [Y=Yes, N=No]
  LinkRsc nVarChar(50) Linked Resource ->ORSC
  OnHldPert Num(19,6) Capital Goods On Hold Percent
  onHldLimt Num(19,6) Capital Goods on Hold Limit
  PriceUnit Int(11) Pricing Unit ->OUOM
  GSTRelevnt VarChar(1) GST Relevant default=N [Y=Yes, N=No]
  SACEntry Int(11) SAC Entry default=-1 ->OSAC
  GstTaxCtg VarChar(1) GST Tax Category default=R [R=Regular, N=Nil Rated, E=Exempt]
  AssVal4WTR Num(19,6) Assessable Value for WTR
  ExcImpQUoM Int(11) Default Excise Imported Quantity UoM [112=Liters, m3, 168=Tonne, metric ton (1000 kg), 251=Horsepower (1 hp = 0.75 kW), 831=Liters of anhydrous (pure) alcohol]
  ExcFixAmnt Num(19,6) Default Excise Fixed Amount
  ExcRate Num(19,6) Default Excise Rate
  SOIExc VarChar(1) SOI Excisable default=4 [1=Excisable, 2=Exemption of excises, 3=Excises are paid to another authority, 4=Not Excisable]
  TNVED nVarChar(10) TNVED Code
  Imported VarChar(1) Imported Item default=N [Y=Yes, N=No]
  AutoBatch VarChar(1) Automatic Batch Creation default=N [Y=Yes, N=No]
  CstmActing VarChar(1) Customer Accounting default=N [N=No, Y=Yes]
  StdItemId Int(11) Standard Item Identification ->OUNCL
  CommClass Int(11) Commodity Classification ->OUNCL
  TaxCatCode nVarChar(50) Tax Category Code for GTS ->OTCC
  DataVers Int(11) Data Version default=1
  NVECode nVarChar(6) NVE Code
  CESTCode Int(11) CEST Code default=-1 ->OCEST
  CtrSealQty Num(19,6) Control Seal Qty
  LegalText nVarChar(250) Legal Text
  QRCodeSrc Text(16) QR Code Source
  Traceable VarChar(1) Traceable default=N [Y=Yes, N=No]
