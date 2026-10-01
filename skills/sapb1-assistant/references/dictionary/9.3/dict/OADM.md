<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OADM - Administration
Module: Administration | 522 columns | ObjType: 39
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  CompnyName nVarChar(100) Company Name
  CompnyAddr nVarChar(254) Address
  Country nVarChar(3) Country ->OCRY
  PrintHeadr nVarChar(100) Printing Header
  Phone1 nVarChar(20) Telephone Number 1
  Phone2 nVarChar(20) Telephone Number 2
  Fax nVarChar(20) Fax Number
  E_Mail nVarChar(100) E-Mail
  Manager nVarChar(100) Managing Director
  CompType VarChar(1) Chart of Accounts Template default=U
  MainCurncy nVarChar(3) Local Currency
  SysCurrncy nVarChar(3) System Currency
  DispPosDeb VarChar(1) Open Balance with Minus Sign default=N [Y=Yes, N=No]
  DefLengthU Int(6) Standard Unit of Length default=2
  DefWeightU Int(6) Default Weight UoM default=2
  DfltVendPM nVarChar(15) Default Payt Method for Vendor ->OPYM
  DirectRate VarChar(1) Direct/Indirect Rate default=Y [Y=Yes, N=No]
  MinAmnt347 Num(19,6) Minimum Amount for 347 Report
  AutoITW VarChar(1) Set Items - Warehouses default=N [Y=Yes, N=No]
  BankCountr nVarChar(3) Bank Country
  TaxIdNum nVarChar(32) Federal Tax ID
  RevOffice nVarChar(100) Tax Office
  FreeZoneNo nVarChar(32) Additional ID Number
  DdctFileNo nVarChar(50) Deduction File No.
  VatCharge VarChar(1) Tax Collection default=Y [Y=Yes, N=No]
  PayOutVat VarChar(1) Tax Definition default=N [Y=Yes, N=No]
  VatPrcnt Num(19,6) Tax Rate
  DpsitPrcnt Num(19,6) Advances on Corp. Income Tax %
  IncomeTax Num(19,6) Withholding Tax %
  VendorDdct VarChar(1) Withholding Tax default=N [Y=Yes, N=No]
  CustmrDdct VarChar(1) Customer's Deduction at Source default=N [Y=Yes, N=No]
  DdctPercnt Num(19,6) Withholding Tax Deduction %
  DdctExpire Date(8) Withholding Tax Ded. in % - Ex
  DdctOffice nVarChar(100) Withholding Tax Deduction - Of
  EURepSqntl Int(11) Sequential Number of EU Sales default=0
  BoxRptSeq Int(11) Box Report Sequential Number default=0
  WTLiable VarChar(1) WTax Liable default=Y
  DfltCustPM nVarChar(15) Default Payt Method for Cust. ->OPYM
  AllowFuPos VarChar(1) Allow Future Posting Date default=N [Y=Yes, N=No]
  UseProdWip VarChar(1) Use Product WIP Account default=Y [Y=Yes, N=No]
  CurrPeriod nVarChar(10) Current Period
  XmlPath Text(16) XML File Path
  DflBnkKey Int(11) Default Bank Key ->ODSC
  BSInstled VarChar(1) Bank Statement Installed default=N [Y=Yes, N=No]
  UseShpdGd VarChar(1) Use Shipped Goods Account default=N [Y=Yes, N=No]
  UseExtRpt VarChar(1) Use Extended Reporting default=N [Y=Yes, N=No]
  ERpPerType VarChar(1) Period Type for Report Generation default=M [Y=Year, Q=Quarter, M=Month, P=Period]
  DfSVatExmp nVarChar(8) Sales Tax Group for Exempt
  DfPVatExmp nVarChar(8) Purchases Tax Group for Exempt
  Manager1 nVarChar(100) General Manager
  Manager1F nVarChar(100) General Manager (For. Lang.)
  CCMask VarChar(1) Mask Credit Card Number default=Y [Y=Yes, N=No]
  ObligLimit VarChar(1) Commitment Restriction default=N [Y=Yes, N=No]
  CreditLimt VarChar(1) Credit Restriction default=N [Y=Yes, N=No]
  SalesLimit VarChar(1) Restrict Sales default=N [Y=Yes, N=No]
  DlnLimit VarChar(1) Restrict Deliv. Notes (PO) default=N [Y=Yes, N=No]
  OrderLimit VarChar(1) Restrict Orders default=N [Y=Yes, N=No]
  AddDlnBlnc VarChar(1) Consider Del. Notes in Sales Restriction default=N [Y=Yes, N=No]
  CreditDpst VarChar(1) Credit Deposit Type default=N [Y=Manually, N=Automatically]
  MultiLang VarChar(1) Multi-Language Support Enabled default=N [Y=Yes, N=No]
  DbVers Int(11) Database Version
  ApplVers Int(11) Application Version
  DflWebSite Text(16) Default for Web Site
  DflFTPSite Text(16) Default for FTP Site
  UseTax VarChar(1) Use Tax default=N [Y=Yes, N=No]
  RevisionPo VarChar(1) Split PO default=N [Y=Yes, N=No]
  Reindex VarChar(1) Rebuild Indexes default=N [Y=Yes, N=No]
  DllPath Text(16) Path to Validation DLL
  TaxIdValid VarChar(1) Tax ID Mandatory Validation default=N [Y=Yes, N=No]
  PchName nVarChar(20) Alternate Name for Purchase
  RpcName nVarChar(20) Alternate Name for A/P Credit
  PdnName nVarChar(20) Alternate Name for Goods Rcpt
  RpdName nVarChar(20) Alternate Name for Gds Return
  PorName nVarChar(20) Alternate Name for Purchase
  LevelWarn VarChar(1) Alert Type for Whse Inventory default=W [W=Warning Only, B=Block, N=No Message]
  CrdCommUse VarChar(1) Set Commission by Customer default=N [Y=Yes, N=No]
  ItmCommUse VarChar(1) Set Commission by Item default=N [Y=Yes, N=No]
  SlpCommUse VarChar(1) Set Commission by Sales Empl. default=N [Y=Yes, N=No]
  DfCustTerm Int(6) Default Payment Term for Cust. default=-1
  DfVendTerm Int(6) Default Payment Term for Vend. default=-1
  SaleProfit VarChar(1) Calc. Gross Profit per Trans. default=Y [Y=Yes, N=No]
  CostPrcLst Int(6) Price List for Reval. Price default=-1
  GrossBySal VarChar(1) Gross Profit After Sale default=N [Y=Yes, N=No]
  TreePricOn VarChar(1) Display Price for Parent Only default=N [Y=Yes, N=No]
  AddVat VarChar(1) Calc. Tax in Sales Quotation default=Y [Y=Yes, N=No]
  BaseFld VarChar(1) Base Field default=Y [Y=Yes, N=No]
  ClosedQuot VarChar(1) Allow Closed Sales Quotations default=N [Y=Yes, N=No]
  UseCode VarChar(1) User Conversion Code default=N [Y=Yes, N=No]
  Code1 nVarChar(8) CODE1
  Code2 nVarChar(8) CODE2
  Code3 nVarChar(8) CODE3
  Code4 nVarChar(8) CODE4
  Color Int(6) Company Color default=1 [0=Combined, 1=Classic, 2=Gray, 3=Violet, 4=Blue, 5=Green, 6=Yellow, 7=Orange, 8=Red, 9=Brown]
  SumDec Int(6) Totals Accuracy default=2
  QtyDec Int(6) Accuracy of Quantities default=3
  PriceDec Int(6) Price Accuracy default=2
  RateDec Int(6) Rate Accuracy default=4
  PercentDec Int(6) Percentage Rate Accuracy default=4
  MeasureDec Int(6) Measuring Accuracy for Units default=3
  DdAutoRun VarChar(1) DD Auto Run default=N [Y=Yes, N=No]
  DdNextDue Date(8) DD Next Due Date
  DdHour Int(6) DD Hour
  CmpnyAddrF nVarChar(254) Address in Foreign Language
  DflTaxCode nVarChar(8) Default Tax Code ->OSTC
  PrintHdrF nVarChar(100) Letter Header in Foreign Lang.
  Phone1F nVarChar(20) Tel. No. 1 (Foreign Language)
  Phone2F nVarChar(20) Tel. No. 2 (Foreign Language)
  FaxF nVarChar(20) Fax Number (Foreign Lang.)
  ManagerF nVarChar(100) Managing Director (For. Lang.)
  TimeFormat VarChar(1) Time Template default=0 [0=24H, 1=12H]
  CigCup VarChar(1) Cig and Cup Warning default=N [Y=Yes, N=No]
  DateFormat VarChar(1) Date Template default=0 [0=DD/MM/YY, 1=DD/MM/CCYY, 2=MM/DD/YY, 3=MM/DD/CCYY, 4=CCYY/MM/DD, 5=DD/Month/YYYY, 6=YY/MM/DD]
  DateSep VarChar(1) Date Separator default=/
  FcNoBlnc VarChar(1) FC Checking Account default=B [B=Block, D=No Message]
  ChangeRdr VarChar(1) Changed Existing Orders default=Y [Y=Yes, N=No]
  MultiCurr VarChar(1) All Currencies Check default=B [B=Block, D=No Message]
  PickParDlv VarChar(1) Partial Deliv. Pick and Pack default=N [Y=Yes, N=No]
  MaxTaxIncr Num(19,6) Maximum Increase of Tax Amount
  ISRType Int(6) ISR Type default=2 [1=ISR, 2=BISR, 3=ISR+, 4=BISR+]
  MaxTaxDecr Num(19,6) Maximum Decrease of Tax Amount
  RoundRmrk VarChar(1) Display Rounding Remark default=Y [Y=Yes, N=No]
  ISRBillerI nVarChar(9) ISR Biller ID
  UpdStamp Int(11) Update Stamp
  SysCNoEdit VarChar(1) Block System Currency Editing default=Y [Y=Yes, N=No]
  RefDNoEdit VarChar(1) Block Updating of Posting Date default=Y [Y=Yes, N=No]
  DfltWhs nVarChar(8) Default Warehouse
  TaxDNoEdit VarChar(1) Free default=Y [Y=Yes, N=No]
  DfSVatItem nVarChar(8) Tax Definition
  DfSVatServ nVarChar(8) Tax Definition
  DfPVatItem nVarChar(8) Tax Group for Purchase Item
  DfPVatServ nVarChar(8) Tax Group for Service Purchase
  DoBudget VarChar(1) Calculate Budget default=N [Y=Yes, N=No]
  CustIdNum nVarChar(6) Customer ID Number default=0
  BgtBlock VarChar(1) Block Budget default=N [B=Only Annual Alert, N=Monthly Alert Only, W=Block]
  BgtWarning VarChar(1) Budget Alert default=A [A=Annual Alert, M=Monthly Alert]
  BdgtPORDoc VarChar(1) Block Purchase Orders default=Y [Y=Yes, N=No]
  BdgtAcctng VarChar(1) Block Bookkeeping default=N [Y=Yes, N=No]
  BdgtDflt Int(11) Default Budget Cost Assmt Mthd default=1
  ContInvnt VarChar(1) Perpetual Inventory Management default=N [Y=Yes, N=No]
  InvntSystm VarChar(1) Perpetual Inventory System default=A [A=Moving Average, S=Standard, F=FIFO]
  ApplicIFRS VarChar(1) Application of IFRS default=N [N=No, Y=Yes]
  StartYear Int(6) Starting in Fiscal Year
  According Int(6) Report According To default=1 [1=, 2=, 3=]
  MltpBrnchs VarChar(1) Enable Multiple Branches default=N [Y=Yes, N=No]
  EnblSrvTax VarChar(1) Enable Service Tax default=N [Y=Yes, N=No]
  DftRCN Int(11) Default for Retail Chains default=-6
  RoundVat VarChar(1) Round Tax Amounts default=N [Y=Yes, N=No]
  BdgtPDNDoc VarChar(1) Block Deliv. Notes for Purch. default=Y [Y=Yes, N=No]
  IRSFileNo nVarChar(9) File Number in Income Tax
  DeferrTax VarChar(1) Deferred Tax default=N [Y=Yes, N=No]
  DflIntrst Num(19,6) Min. Default Interest Amount
  DfltSlp Int(6) Sales Employee default=-1
  DflCrCard Int(6) Default Credit Card
  DflBnkCode nVarChar(30) Default Bank No.
  DflBnkAcct nVarChar(50) Default Bank Account
  DflBranch nVarChar(50) Default Branch
  UsePaSys VarChar(1) Use PA System default=N [Y=Yes, N=No]
  Serv_Usr nVarChar(20) Service Code
  Serv_Pass nVarChar(20) Service Password
  ParamPath Text(16) Param. Folder Path
  ExcelPath Text(16) Excel Folder Path
  TaxIdNum2 nVarChar(32) Federal Tax ID 2
  TaxIdNum3 nVarChar(32) Federal Tax ID 3
  DecSep VarChar(1) Decimal Separator default=.
  ThousSep VarChar(1) Thousandths Separator default=,
  CurOnRight VarChar(1) Display Currency on the Right default=N [Y=Yes, N=No]
  WarnByWhs VarChar(1) Alert by Warehouse default=N [N=No, Y=Yes]
  DflBnkAcKy Int(11) Default Bank Account Number ->DSC1
  PriceSys VarChar(1) Price System default=Y [Y=Whse, N=Item]
  DftPVL Int(11) Preferred Vendor Credit default=-1
  useDdctTrc VarChar(1) WTax Deduction Hierarchy default=N [Y=Yes, N=No]
  useDocWrf VarChar(1) Doc. Confirmation default=N [Y=Yes, N=No]
  BtchStatus VarChar(1) Default for Batch Status default=0 [0=Released, 1=Not Accessible, 2=Locked]
  OrderBatch VarChar(1) Manage Orders in Batches default=Y [Y=Yes, N=No]
  GLMethod VarChar(1) Set G/L Account By default=W [W=Warehouse, C=Item Group, L=Item Level]
  SetSriUniq VarChar(1) Set Unique Serial No. default=N [Y=Yes, N=No]
  SriUniqFld VarChar(1) Unique Serial No. default=3 [0=None, 2=Mfr Serial No., 3=Serial Number, 4=Lot Number]
  MaxHistory Int(11) Max. History default=99
  TaxRateDet VarChar(1) Tax Rate Determination default=P [P=Posting Date, D=Document Date]
  RefreshQty VarChar(1) Refresh in Whse Qty in DI default=N [Y=Yes, N=No]
  StockNoBas VarChar(1) Stock No. Base
  MaxCntRows Int(11) Allowed Max Rows in Counting default=10000
  CentPmtInc VarChar(1) Enable Incom. Centralized Payt default=N [N=No, Y=Yes]
  CentPmtOut VarChar(1) Enable Outg. Centralized Payt default=N [N=No, Y=Yes]
  ChCtrAPAct VarChar(1) Change Def. Recon. A/P Accts default=N [Y=Yes, N=No]
  ChCtrARAct VarChar(1) Change Def. Recon. A/R Accts default=N [Y=Yes, N=No]
  PACUsrName nVarChar(100) PAC User Name
  PACPasswrd nVarChar(100) PAC Password
  CaredType nVarChar(2) BP Type Code [01=01, 04=04, 15=15, 71=71, 73=73, 75=75]
  PBSNumber nVarChar(8) PBS Number
  PBSGroupNo nVarChar(5) PBS Group Number
  OrgNumber nVarChar(100) Organization Number
  ActSep VarChar(1) Account Segments Separator default=-
  DspBokpWin VarChar(1) Display Bookkeeping Window default=N [Y=Yes, N=No]
  SHandleWT VarChar(1) Withholding Tax default=N [Y=Yes, N=No]
  SDfltWT nVarChar(4) Default Withholding Tax Code ->OWHT
  IncresGlAc nVarChar(15) G/L Increase Account [Y=Yes, N=No] ->OACT
  PHandleWT VarChar(1) Withholding Tax
  PDfltWT nVarChar(4) Default Withholding Tax Code ->OWHT
  ExWTLiabl VarChar(1) WTax-Liable Expense default=N [Y=Yes, N=No]
  EDocSeqNum Int(11) Electronic Document Sequence Number default=1
  AllowPostZ VarChar(1) Allow Inb. Pstng W/o a Price default=N [Y=Yes, N=No]
  PostDiffR Num(19,6) Display in Red Greater Than % default=5 [5=Variance Percentage Default Value]
  EnableRO VarChar(1) Enable Release Only Snb in Pst default=N [Y=Yes, N=No]
  UalLastDel Date(8) Last Delete Date on Table OUAL
  UalKeepDay Int(11) Days for keeping data on OUAL default=30
  NegAmount VarChar(1) Use Negative Amounts default=Y [Y=Yes, N=No]
  EnbDocOpt VarChar(1) Enable Document Optimization default=Y [Y=Yes, N=No]
  HldCode nVarChar(20) Holiday Name ->OHLD
  AlphaDoc VarChar(1) Use Alphanum. ID for Document default=N [N=No, Y=Yes]
  EDocURL2 nVarChar(254) El. Doc. Service URL 2
  EnPriceMod VarChar(1) Enable Separate Price Mode default=N [N=No, Y=Yes]
  TaaSEnable VarChar(1) Enable Tax as a Service default=N [N=Do Not Use, Y=Sales and Purchase, S=Sales Only]
  TaaSUser nVarChar(50) TaaS User Name
  OrderBlock VarChar(1) Order Block
  RoundMthd VarChar(1) Rounding Method default=N [Y=Yes, N=No, =]
  AdrsFromWH VarChar(1) Use Whse Address in A/P Docs. default=Y [Y=Yes, N=No]
  OrderParty nVarChar(30) Ordering Party
  CrtfcateNO nVarChar(20) Certificate No.
  ExpireDate Date(8) Expiration Date
  NINum nVarChar(20) National Insurance No.
  TaaSPass nVarChar(20) TaaS User Password
  TaaSAutURL nVarChar(250) TaaS oAuth URL
  CfwAsnMust VarChar(1) CFW Assignment Mandatory [Y/N] default=Y [N=No, Y=Yes]
  CfwInDflt Int(11) Incoming Payment Dflt CFW Item
  CfwOutDflt Int(11) Outgoing Payment Dflt CFW Item
  TaaSURL nVarChar(250) TaaS Service URL
  TaaSSaleAc nVarChar(15) TaaS Default Sales Account
  TaxRegime nVarChar(100) Tax Regime
  AliasName Text(16) Alias Name
  DftJPELine VarChar(1) Default Line For Local Area
  RdrConfrmd VarChar(1) Sales Order Confirmed default=Y [Y=Yes, N=No]
  PorConfrmd VarChar(1) Purchase Order Confirmed default=Y [Y=Yes, N=No]
  TaaSPurcAc nVarChar(15) TaaS Default Purchase Account
  AdvImagePr VarChar(1) Extended Image Processing default=N [N=Partial, O=Without, Y=Full]
  ChfAcc Int(11) Chief Accountant ->OHEM
  TaxMethod VarChar(1) Taxation Method [0=On Shipment, 1=On Payment]
  CEO Int(11) CEO ->OHEM
  WllPprDsp Int(6) Wallpaper Display default=1 [1=Centralized, 2=Full Screen, 3=Tile]
  WallPaper Text(16) Wallpaper
  RndToTDec VarChar(1) Round VAT to Tenths default=N [Y=Yes, N=No]
  SDfltITWT nVarChar(4) Default Income Tax WTax Code ->OWHT
  PDfltITWT nVarChar(4) Default Income Tax WTax Code ->OWHT
  CheckFiles VarChar(1) File Check default=N [Y=Yes, N=No]
  DsplyRates VarChar(1) Display Rate Table on start up default=N [Y=Yes, N=No]
  DfActCurr VarChar(1) Default Account Currency default=Y [Y=All Currencies, N=Local Currency]
  defTaxVend VarChar(1) Deferred Tax for Vendors default=N [Y=Yes, N=No]
  RcrFlag VarChar(1) Display Transactions Scheduled for Today default=N [Y=Yes, N=No]
  RclFlag VarChar(1) Display Recurring Transactions default=N [Y=Yes, N=No]
  ContactLog VarChar(1) Today's Activity Alert default=N [Y=Yes, N=No]
  ShowNewMsg VarChar(1) Open Message on Arrival default=Y [Y=Yes, N=No]
  OpenCdt VarChar(1) Open Window for Credit Reference default=N [Y=Yes, N=No]
  AutoVat VarChar(1) Automatic VAT Row Creation In default=N [Y=Yes, N=No]
  ConsumeFCT VarChar(1) Consumption Forecast default=Y [Y=Yes, N=No]
  ConsumeMtd VarChar(1) Consumption Method default=B [B=Backward-Forward, F=Forward-Backward]
  DaysBack Int(11) Days Backward default=7
  DaysFwrd Int(11) Days Forward default=7
  IsPAPrn VarChar(1) Panama Printer Connected default=N [Y=Yes, N=No]
  ShowNewTsk VarChar(1) Open Worklist on Task Arrival default=Y [N=No, Y=Yes]
  TaxCodeCst nVarChar(8) Default Tax Code (New Custs.) ->OSTC
  TaxCodeVnd nVarChar(8) Default Tax Code (New Vendors) ->OSTC
  State nVarChar(3) Status ->OCST
  CharMonth Int(11) Number of Characters in Month
  free83 VarChar(1) Free83
  ScreenLock Int(6) Screen Lock Delay default=30
  OpenCredit VarChar(1) Open Postdated Credit Vouchers Window default=N [Y=Always, N=No, D=By Date]
  OpenDps VarChar(1) Open Postdated Checks Window default=N [Y=Yes, N=No]
  AltBOEPost VarChar(1) Active Alternative BOE Post default=N [Y=Yes, N=No]
  LDiscTotal VarChar(1) Calc. Row Disc. from Tot. Pr. default=Y [Y=Yes, N=No]
  Code Int(11) Code default=1
  DfltDunTrm nVarChar(25) Default Dunning Terms ->ODUT
  Profession nVarChar(50) Profession
  AlertPolFr Int(6) Message Check Frequency default=5
  DfltCDP Int(6) Default Closing Date Procedure default=-1
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign Int(6) User Signature ->OUSR
  DflBCACode nVarChar(3) Default Bank Charges Alloc. ->OBCA
  IgrAllCash VarChar(1) Ignore All Cash Flow Relevant default=Y [Y=Yes, N=No]
  TaxPayerRf nVarChar(32) Unique Taxpayer Ref. (UTR)
  EmployerRf nVarChar(32) Employer's Reference
  PStatAutCh VarChar(1) Period Status Automatic Change default=Y [Y=Yes, N=No]
  PStatDelay Int(6) Period Status Change Delay default=1
  RepBusType nVarChar(2) Reporting Business Type default=2 [Y=Yes, N=No, 1=Industrial, 2=Commercial, 3=Service Provider, 4=Contractor, 9=Other, 99=Report includes more than one business]
  RepBusOthr nVarChar(32) Reporting Business Type Desc.
  BrachNum nVarChar(4) Branch Number
  BuisnesDsc nVarChar(50) Business Description [Y=Yes, N=No]
  ReptMethod nVarChar(2) Reporting Method default=2 [1=Cash, 2=Cumulative, 3=US Dollar Regulation]
  AcctMethod nVarChar(2) Accounting Method default=2 [1=Unilateral, 2=Double]
  Bookpitype nVarChar(2) Bookkeeping Type default=2 [1=Manual, 2=Computerized, 3=Mixed]
  ActSoftNam nVarChar(100) Accounting Software Name
  OpnClsRmrk VarChar(1) Copy Opening/Closing Remarks default=Y [Y=Yes, N=No]
  TaxRndRule VarChar(1) Default Tax Rounding Rule [R=Round Off, C=Round Up, F=Round Down]
  NegTax VarChar(1) Allow Negative Tax Amt in Rpt default=N [Y=Yes, N=No]
  ZeroLine VarChar(1) Allow Zero Row in JE default=Y [Y=Yes, N=No]
  GBOpenFile VarChar(1) Open GBI File After Export default=N [Y=Yes, N=No]
  GBIntface VarChar(1) GB Data Interface Enable default=N [Y=Yes, N=No]
  DfltCDPV Int(6) Default A/P Closing Date Proc. default=-1
  OnHldPert Num(19,6) Capital Goods On Hold Percent.
  WTRndRule VarChar(1) Default WTax Rounding Rule [R=Round Off, C=Round Up, F=Round Down]
  GPPrcntSrv Num(19,6) Default GP % in Service Doc.
  DspFrznBP VarChar(1) Display Inactive BPs in Rpt default=Y [Y=Yes, N=No]
  DspFrznITM VarChar(1) Display Inactive Items in Rpt default=Y [Y=Yes, N=No]
  WTAccumAmt Num(19,6) Accum. Amount for WTax on AP
  NewDPRCus VarChar(1) Hide Dpm Invoice default=Y [Y=Yes, N=No]
  ServNature VarChar(1) Service Nature [P=Service Provider, D=Service Distributor]
  PickLimit VarChar(1) Restrict Pick List default=N [Y=Yes, N=No]
  WTAccAmtAR Num(19,6) Accum. Amount for WTax on AR
  UseProdPL VarChar(1) Use Production P&L Accounts default=N [N=Use Balance Sheet Only, Y=Use Balance Sheet and Profit and Loss Account]
  QueryDec Int(6) Calculated Query Accuracy
  ExRtDefTax VarChar(1) Exchange Rate on Deferred Tax default=N [Y=Yes, N=No]
  BoletoPath Text(16) Boleto Path
  UserSign2 Int(6) Updating User ->OUSR
  MMLastImpD Date(8) Last Import File Date
  CpyExhRate VarChar(1) Copy Exchange Rate in Copy To default=N [Y=Yes, N=No]
  MapService Int(11) Map Service default=-1 ->OMPS
  ODWFreq Int(11) Open Doc. Refresh Frequency default=30
  GTSOutPath Text(16) GTS Outbound Path
  UseMltDims VarChar(1) Use Multidimensions default=Y [Y=Yes, N=No]
  MDStyle VarChar(1) Multidimensions Display Style default=U [U=Unified, S=Separate]
  GTSInPath Text(16) GTS Inbound Path
  GTSSep nVarChar(10) GTS Separator
  GTSDftChk Int(11) GTS Default Checker ->OHEM
  GTSDftPye Int(11) GTS Default Payee ->OHEM
  GTSMaxAmt Num(19,6) GTS Max. Amount
  RspOverAmt VarChar(1) Response to Exceeding Amount default=B [B=Block, S=Split]
  DRBlock1 VarChar(1) Distribution Rule: Block 1 default=N [N=Without Warning, B=Block Posting]
  DRBlock2 VarChar(1) Distribution Rule: Block 2 default=N [N=Without Warning, B=Block Posting]
  DRBlock3 VarChar(1) Distribution Rule: Block 3 default=N [N=Without Warning, B=Block Posting]
  DRBlock4 VarChar(1) Distribution Rule: Block 4 default=N [N=Without Warning, B=Block Posting]
  DRBlock5 VarChar(1) Distribution Rule: Block 5 default=N [N=Without Warning, B=Block Posting]
  PrjBlock VarChar(1) Project Block default=N [N=Without Warning, B=Block Posting]
  SimReport VarChar(1) Simulation Report default=N [Y=Yes, N=No]
  SnapShotId Int(11) Snapshot ID default=0
  BackOrder VarChar(1) Pick and Pack Back Order default=N [Y=Yes, N=No]
  HQLocation VarChar(1) Headquarters Location default=B [B=, C=Continent, M=Madeira, A=Azores]
  DigCrtPath Text(16) Digital Certificate Path
  DflWTS Int(6) Default E-Tax Web Site default=-1
  EnbApprDI VarChar(1) Enable DI Approval Process default=N [Y=Yes, N=No]
  ChBPSerie VarChar(1) Verify Non-manual BP Series default=N [Y=Yes, N=No]
  ChItmSerie VarChar(1) Verify Non-manual ITM Series default=N [Y=Yes, N=No]
  ETRTaxOffi Int(11) ETR Tax Office default=0 ->OTOF
  ETRTaxPers VarChar(1) ETR Tax Person Type [T=VAT Payer, R=Another Person Registered for Tax, S=Person required to submit a tax declaration/return according to section 78, paragraphs 3, 4, and 9, D=Taxable person according to section 3, subsection 5, when applying a tax deduction, I=Tax agent when importing goods according to section 69]
  EDocExpFrm Int(11) Electronic Doc. Export Format
  PCN874RTyp VarChar(1) PCN874 Report Type default=1 [1=Registered Business, 6=Finan. Institution/Non-Profit Org.]
  BTWDecProv nVarChar(3) BTW Declaration Provider default=BPL [BPL=BPL, INT=INT]
  BTWDcPrvID nVarChar(100) BTW Declaration Provider ID
  BTWName nVarChar(100) BTW Name
  BTWStreet nVarChar(100) BTW Street
  BTWCity nVarChar(100) BTW City
  BTWZip nVarChar(30) BTW ZIP Code
  BTWPhone nVarChar(100) BTW Phone Number
  BTWOB Int(11) BTW OB ID default=1
  BTWICP Int(11) BTW ICL ID default=1
  BTWOBFmt Int(11) BTW OB Mapping Format
  BTWICPFmt Int(11) BTW ICP Mapping Format
  ETRPhoneNo nVarChar(20) ETR Telephone Number
  EDTestMode VarChar(1) Electronic Document Test Mode default=N [Y=Yes, N=No]
  EDocGenTyp VarChar(1) El. Doc. Default Gen. Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  EDocRptFmt Int(11) El. Document Report Format
  EDocPass nVarChar(100) El. Doc. Service Password
  EDProcess VarChar(1) Electronic Document Process default=I [C=CFD, I=CFDI]
  PAC nVarChar(20) PAC default=XML ->OPAC
  NotifAlert VarChar(1) Notification by Alert default=Y [Y=Yes, N=No]
  NotifEmail VarChar(1) Notification by E-Mail default=N [Y=Yes, N=No]
  EDocUDQCat Int(11) Electronic Document UDQ Category
  EOutputPth Text(16) Ouput Directory for Electronic Documents
  EDelDocFrm Int(11) Electronic Delivery Doc. Export Format
  EDocPmnFmt Int(11) El. Doc. Payment Format
  EDocURL1 nVarChar(254) El. Doc. Service URL 1
  ETRFaxNo nVarChar(20) ETR Fax Number
  ETRMgrPhn nVarChar(20) ETR Manager's Phone Number
  EDFormat Int(11) Electronic Document Format ->OLLF
  AIDFormat Int(11) Annual Invoice Decl. Format ->OLLF
  CrtLineRFQ VarChar(1) Create Online Quotation default=N [Y=Yes, N=No]
  DflJET nVarChar(60) Default JE Type ->OJET
  OnlyPaidIn VarChar(1) Display Only Paid Reserve Inv. default=N [N=No, Y=Yes]
  PDDEnabled VarChar(1) Payments Due Date Enabled default=N
  MaxDays4DD Int(11) Max. Allowed Range for Due Dte default=0
  AutoAddUoM VarChar(1) Auto. Add UoMs to Items default=Y [Y=Enabled, N=Disabled]
  AutoAddPkg VarChar(1) Auto. Add Pkgs to Items default=Y [Y=Enabled, N=Disabled]
  BinActivat VarChar(1) Has Whse Bin Activated [Y/N] default=N [Y=Yes, N=No]
  IssuePriBy Int(6) Issue Primarily By SnB or Bin default=0 [0=Issue Primarily By Serial/Batch Numbers, 1=Issue Primarily By Bin Location]
  InstFixAst VarChar(1) Enable Fixed Assets default=N [Y=Yes, N=No]
  DeprecCalc VarChar(1) Depreciation Calculation default=M [M=Month, D=Day]
  FixAstMod VarChar(1) Fixed Asset Mode default=P [P=Production, T=Transfer]
  SopPath Text(16) Solution Packager Exe. Path
  NewAcctDe VarChar(1) New G/L Account Determination default=N [Y=Yes, N=No]
  ClnZeroPln VarChar(1) Clean Zero Price Row in ITM1 default=N [N=No, Y=Yes]
  CmdDisBoth VarChar(1) Display Both Related Docs. default=Y [Y=Yes, N=No]
  CnclMaxDay Int(11) Max. No. of Days For Cancel
  AttachPath Text(16) Attachments Path
  ConfigPath Text(16) Configuration Path
  WrkshtPath Text(16) Worksheet Path
  ICDifExPe1 Num(19,6) Single Count Variance (%) default=5 [5=Single Counting Type - Default Variance Percentage]
  ICDifExPe2 Num(19,6) Multiple Count Max. Variance (%) default=5 [5=Multiple Counting Type - Default Max Variance Percentage]
  ClsZoDiffR VarChar(1) Close Rows Cont. Zero Diff. default=Y [Y=Yes, N=No]
  ClsNoConfi VarChar(1) Close Without Confirmation default=N [Y=Enabled, N=Disabled]
  DTWPath Text(16) DTW Exe. Path
  DfltByEml VarChar(1) Default by E-Mail default=E [E=E-Mail, O=Outlook E-Mail]
  CreditDay1 Int(6) Credit Handling Day 1 default=1
  INVOBPrice VarChar(1) Inventory OB Price Zero default=N [N=No, Y=Yes]
  SplitFBSh VarChar(1) Split Asset Balance Sheet Acct default=N
  NotifyRqr VarChar(1) Notify Requester default=N
  DeactivFA VarChar(1) Deactivate Asset When End Life default=N [N=No, Y=Yes]
  CshDctFA VarChar(1) CM for Payment Cash Discount default=N [N=No, Y=Yes]
  SendAlert VarChar(1) Send Internal Message default=N
  BdgtPRQDOC VarChar(1) Block Purchase Request default=N [Y=Yes, N=No]
  IsReuseNum VarChar(1) Enable Document Number Reuse default=N [N=No, Y=Yes]
  IsReuseNFN VarChar(1) Enable Nota Fiscal No. Reuse default=N [N=No, Y=Yes]
  SIPLReport VarChar(1) Show Inactive PL in Reports default=N [Y=Yes, N=No]
  SIPLDoc VarChar(1) Show Inactive PL in Docs default=N [Y=Yes, N=No]
  SIPLSeting VarChar(1) Show Inactive PL in Settings default=N [Y=Yes, N=No]
  PriceProcM VarChar(1) On Change UoM Conversion Rules default=U [R=Remove UoM Prices, U=Update UoM Prices Accordingly, L=Keep Corresponding UoM Prices Unchanged, K=Keep All UoM Prices Unchanged]
  ChkQtyINV VarChar(1) Enable Check Quantity in INV default=N [Y=Yes, N=No]
  EnbAdvATP VarChar(1) Enable Advanced ATP default=N [Y=Yes, N=No]
  EnblCase VarChar(1) Enable Case Sensitivity default=N [N=No, Y=Yes]
  EnbSupplC VarChar(1) Enable Supplementary Code default=Y [Y=Yes, N=No]
  MBAOnPer VarChar(1) Allow Multiple BAs for Period default=N [N=No, Y=Yes]
  MBAOnAP VarChar(1) Block Multiple BAs for AP Doc. default=N [N=No, Y=Yes]
  MBAOnAR VarChar(1) Block Multiple BAs for AR Doc. default=N [N=No, Y=Yes]
  ApyBsActSP VarChar(1) Apply Active Special Prices default=N [Y=Yes, N=No]
  ApyBsActPV VarChar(1) Apply Active Period and Volume default=N [Y=Yes, N=No]
  ApyBsActPL VarChar(1) Apply Active Price Lists default=N [Y=Yes, N=No]
  IsUpdNstdB VarChar(1) Update Non-Std Based Prices default=N [Y=Yes, N=No]
  SnBDfltSB VarChar(1) SnB Default Eval. System SB default=N [Y=Yes, N=No]
  OneBOneRec VarChar(1) One Batch One Receipt default=N [Y=Yes, N=No]
  ReptCurrcy nVarChar(2) R6111 Report Currency default=1 [1=Amounts in NIS, 2=Amounts in USD]
  ICDifExPe3 Num(19,6) Multiple Count Vldt. Variance (%) default=5 [5=Multiple Counting Type - Default Individual Counter Variance Percentage]
  INCSingToV VarChar(1) Copy Single Counter to Validt. default=Y [Y=Yes, N=No]
  POrCByINC VarChar(1) Posting or Create Date by INC default=N [Y=Based on Posting Date, N=Based on Creation Date]
  EnbNegPym VarChar(1) Enable Negative Payment default=N [Y=Yes, N=No]
  SirenNo nVarChar(9) Siren Number
  SEPACredID nVarChar(35) SEPA Creditor ID
  InstitCode nVarChar(2) Institution Code [10=Secretaria da Receita Federal do Brasil, 20=Banco Central do Brasil (COSIF)]
  ECDFormat Int(11) ECD File Format ->OLLF
  ApyDRinPEC VarChar(1) Apply DR in Period End Closing default=N [Y=Yes, N=No]
  ApyPRinPEC VarChar(1) Apply PJ in Period End Closing default=N [Y=Yes, N=No]
  TaxPyerSta nVarChar(2) TAX_PAYER_STATUS
  MaxINVRptR Int(11) Allowed Rows in INC Trans Rpt default=85000
  DftResWhs nVarChar(8) Default Resource Warehouse
  AutoResWhs VarChar(1) Auto Add All Warehouses to New Resources default=Y [Y=Yes, N=No]
  InActRpt VarChar(1) Inactive Reports default=Y [Y=Yes, N=No]
  InActMkt VarChar(1) Inactive Marketing Documents default=Y [Y=Yes, N=No]
  InActPln VarChar(1) Inactive Price Lists default=Y [Y=Yes, N=No]
  StartFrom VarChar(1) Start From default=1 [1=Today, 2=Month Start, 3=Month End]
  Months Int(6) Months default=1
  Days Int(6) Days default=0
  JEInFATran VarChar(1) Always Create JE in Transfer default=N [Y=Yes, N=No]
  TPLId Int(6) UI Template ID ->UICU
  TxtSrch VarChar(1) Text Search default=N [Y=Yes, N=No]
  ApyIBtoACT VarChar(1) Apply IBAN Vldt. to Bank Acct default=N [Y=Yes, N=No]
  JeUnGroup VarChar(1) Journal Entry Split Lines default=N [N=No Split, Y=Split in Journal Entry Preview Only, S=Split]
  IgnoreAdde VarChar(1) Print Document Without Addenda default=N [Y=Yes, N=No]
  EnterAsTab VarChar(1) Use Numeric Keypad ENTER Key as TAB Key default=N [Y=Yes, N=No]
  MouseOnly VarChar(1) Document Operation by Mouse Only default=N [Y=Yes, N=No]
  PrjMngmnt VarChar(1) Enable Project Management default=N [Y=, N=No]
  ElectrDocs VarChar(1) Enable Electronic Documents default=N [Y=Yes, N=No]
  DotAsSep VarChar(1) Use Dot Key As Separator default=N [Y=Yes, N=No]
  DoMngMth nVarChar(11) Data Ownership Management Method default=D [D=Document Only, B=Business Partner Only, A=Business Partner and Document, R=Branch]
  AlwBPNOwn VarChar(1) Allow BP Without an Owner default=N [Y=Yes, N=No]
  EmptyPKL VarChar(1) Create an Empty Pick List default=N [Y=Yes, N=No]
  ExcNInvItm VarChar(1) Exclude Non-Inventory Items default=N [Y=Yes, N=No]
  PayRefCalc Int(6) Payment Reference Calculation default=1 [1=Payment Reference, 2=Global Structured Creditor Reference]
  MultiSched VarChar(1) Multiple scheduling on Service Call default=N [Y=Yes, N=No]
  CloseWipV VarChar(1) Close to Parent Item WIP Variance Account default=N [Y=Yes, N=No]
  onHldLimt Num(19,6) Capital Goods on Hold Limit
  EnbApUpDoc VarChar(1) Enable Updating Doc Added/Updated via Approval Process default=N [Y=Yes, N=No]
  EnbApUpDft VarChar(1) Enable Updating Draft in Status Pending/Approved default=N [Y=Yes, N=No]
  EnPacking VarChar(1) Display Packing Drawer default=N [Y=Yes, N=No]
  BlockZeroQ VarChar(1) Block Stock Negative Quantity default=Y [Y=Yes, N=No]
  NegStoLv VarChar(1) Negative Stock: Check Level default=I [C=Company, W=Warehouse, I=Item Setting]
  EnUpdBAPln VarChar(1) Enable Update BA Plan default=N [Y=Yes, N=No]
  BAOpPOR VarChar(1) BA Option for Purchase Orders default=N [N=Without Warning, W=Warning, B=Block Posting]
  BAOpPDN VarChar(1) BA Option for GRPOs default=N [N=Without Warning, W=Warning, B=Block Posting]
  BAOpAcctng VarChar(1) BA Option for Accounting default=N [N=Without Warning, W=Warning, B=Block Posting]
  AssgnOBAAP VarChar(1) Assign only valid BA for AP default=N [N=No, Y=Yes]
  AssngOBAAR VarChar(1) Assign only valid BA for AR default=N [N=No, Y=Yes]
  ApyToNewBP VarChar(1) Apply Change Only to New BP default=N [Y=Yes, N=No]
  PrrConfrmd VarChar(1) Goods Return Request Confirmed default=Y [Y=Yes, N=No]
  RrrConfrmd VarChar(1) Return Request Confirmed default=Y [Y=Yes, N=No]
  DflSeries Int(11) Default Series ->NNM1
  EnblLC VarChar(1) Enable Live Collaboration default=N [N=No, Y=Yes]
  DflAcct nVarChar(210) Default Account ->OACT
  SmtpServer nVarChar(100) SMTP Server
  SmtpPort nVarChar(10) SMTP Port
  SmtpName nVarChar(100) SMTP User Name
  SmtpPasswd nVarChar(100) SMTP Password
  SmtpEncode nVarChar(100) SMTP Encoding default=3 [3=English] ->OLNG
  SmtpAuthen nVarChar(100) SMTP Authentication default=N [N=No Authentication, L=Login Authentication, I=Integrated Windows Authentication]
  TlsEncryp VarChar(1) TLS Encryption default=N
  HtmlDirect VarChar(1) HTML Direction Right to Left default=N
  IncSubject VarChar(1) Include Subject in Msg Body default=N
  TenLevel VarChar(1) Tenant Level Configuration default=N
  CreditDay2 Int(6) Credit Handling Day 2 default=15
  CdtPrvDays Int(11) Vouchers from Last Days default=1
  AuImpRates VarChar(1) Import Currency Rates Automatically default=N [Y=Yes, N=No]
  ValidateBa VarChar(1) Validate Account Balance default=N [N=Without Warning, W=Warning Only, B=Block Posting]
  ManRemark VarChar(1) Mandatory Remark default=N [N=No, Y=Yes]
  ManRmkType VarChar(1) Mandatory Remark Type default=H [H=Header Only, R=Rows Only, B=Rows and Header]
  ManRmkAlt VarChar(1) Mandatory Remark Alert Type default=B [W=Warning Only, B=Block Posting]
  TermsPath Text(16) Terms and Conditions Path
  EDocWSFrm Int(11) El. Doc. WS Format
  DspBUoM VarChar(1) Display Batch Quantities By default=0 [0=Document Row UoM, 1=Inventory UoM]
  EDocSName nVarChar(200) El. Doc. Sender Name
  EDocSEMail nVarChar(200) El. Doc. Sender E-Mail
  CpyRulToTx VarChar(1) Copy Distribution Rules to Tax Related Rows default=N [Y=Yes, N=No]
  BpNoLock VarChar(1) Business Partner Without Lock default=N [N=No, Y=Yes]
  SearchUrl nVarChar(254) Search Engine URL default=http://www.google.com/search?q={SapName} {FormName} {MessageString} site:sap.com
  EnableMTD VarChar(1) Enable Making Tax Digital default=N [N=No, Y=Yes]
  ClientID nVarChar(100) Making Tax Digital Client ID
  ClntSecret nVarChar(100) Making Tax Digital Client Secret
  AuthURL nVarChar(254) Making Tax Digital Authorized URL
  TokenURL nVarChar(254) Making Tax Digital Token URL
  RedrctURL nVarChar(254) Making Tax Digital Redirect URL
  Threshold Num(19,6) Threshold for Customer Accounting
  PublicComp VarChar(1) Public Company default=N [Y=Yes, N=No]
  EnableEWB VarChar(1) E-Way Bill Auto-Generation default=N [N=No, Y=Yes]
  TspEntry Int(11) Default Transporter ->OTSP
  TspLine Int(11) Default Transportation Line
  EwbGenType VarChar(1) Default E-Way Bill Generation Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  VolumeLic VarChar(1) Use Volume Based Licensing default=N [Y=Yes, N=No]
