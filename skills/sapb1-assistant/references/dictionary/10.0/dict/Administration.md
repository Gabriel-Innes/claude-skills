<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->

# AAD1 - Administration Extension-Log
Module: Administration | 135 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CurrPeriod nVarChar(10) Free
  Street nVarChar(100) Street
  StreetF nVarChar(100) Street Foreign
  Block nVarChar(100) Block
  BlockF nVarChar(100) Block Foreign
  City nVarChar(100) City
  CityF nVarChar(100) City Foreign
  ZipCode nVarChar(20) Zip Code
  ZipCodeF nVarChar(20) Zip Code Foreign
  County nVarChar(100) County
  CountyF nVarChar(100) County Foreign
  State nVarChar(3) Status ->OCST
  Country nVarChar(3) Country/Region ->OCRY
  IntrntAdrs nVarChar(50) Internet Address
  Code Int(11) Code default=1
  AssType nVarChar(100) Assessee Type
  CompnyType nVarChar(100) Company Type
  NatureBiz nVarChar(100) Nature of Business
  TaxIdNum4 nVarChar(100) Federal Tax ID 4
  TaxIdNum5 nVarChar(100) Federal Tax ID 5
  TaxIdNum6 nVarChar(100) Federal Tax ID 6
  LogInstanc Int(11) Log Instance default=0
  AddrType nVarChar(100) Address Type
  AddrTypeF nVarChar(100) Address Type Foreign
  StreetNo nVarChar(100) Street No.
  StreetNoF nVarChar(100) Street No. Foreign
  Building nVarChar(100) Building/Floor/Room
  BuildingF nVarChar(100) Building/Floor/Room Foreign
  EccNo nVarChar(40) E.C.C. No.
  CERegNo nVarChar(40) C.E. Registration No.
  CERange nVarChar(60) C.E. Range
  CEDivision nVarChar(60) C.E. Division
  CeComRate nVarChar(60) C.E. Commisionerate
  MenuCode nVarChar(60) Manufacturer Code
  Jurisd nVarChar(60) Jurisdiction
  SnapShotId Int(11) Snapshot ID default=0
  STDCode Int(11) STD Code
  STDCodeF Int(11) STD Code Foreign
  CompNature Int(11) Nature of Company default=-1
  EconActT Int(11) Economic Activity Type default=-1
  CredCOrig VarChar(1) Credit Contribution Origin
  IPIPeriod VarChar(1) IPI Period
  CoopAssocT Int(11) Cooperative Association Type default=-1
  DspIBPDoc VarChar(1) Display Inactive BPs in Doc. default=Y [Y=Yes, N=No]
  DspIITMDoc VarChar(1) Display Inactive Items in Doc. default=Y [Y=Yes, N=No]
  ProfTax Int(11) Profit Taxation default=-1
  CompQualif Int(11) Company Qualification default=1
  DeclType Int(11) Declarer Type default=1
  IPITaxCon VarChar(1) IPI Tax Contributor default=N [N=No, Y=Yes]
  ISVATRegNo nVarChar(100) IS VAT Reg. No. of Trader
  ISVATRegEx nVarChar(10) IS VAT Reg. No. Extension
  ISObligLvl VarChar(1) IS Degree of Obligation
  ISTaxState nVarChar(3) IS Federal State of Tax Office ->OCST
  ISComDecID nVarChar(32) IS Company Declaration ID
  OKDPNum nVarChar(7) OKDP Number
  ISValidKey nVarChar(35) IS Validation Key Ident.
  ISDnsce nVarChar(10) IS Declaration Office
  ISDfltPath Text(16) IS Default File Path
  ISSimpProc VarChar(1) IS Simplified Procedure default=Y [Y=Yes, N=No]
  ISForceCmp VarChar(1) IS Require All Data default=Y [Y=Yes, N=No]
  ISCstRecSt nVarChar(6) IS Customs Section
  ISDfltInct Int(11) IS Default Incoterms
  ISDfCPEx Int(11) IS Default Customs Proc. Exp.
  ISDfCPIm Int(11) IS Default Customs Proc. Imp.
  ISDfNTEx Int(11) IS Dflt Nat. of Trans. for Exp
  ISDfNTIm Int(11) IS Dflt Nature of Tran. Imp.
  ISDfPortEx Int(11) IS Default Port for Export
  ISDfPortIm Int(11) IS Default Port for Import
  ISDfSPEx Int(11) IS Default Stat. Proc. Export
  ISDfSPIm Int(11) IS Default Stat. Proc. Import
  ISDfCSTEx Int(11) IS Default State for Export ->ODCI
  ISDfCSTIm Int(11) IS Default State for Import ->ODCI
  ISDfTMEx Int(11) IS Default Transport Mode Exp.
  ISDfTMIm Int(11) IS Default Transport Mode Imp.
  ISDeclDept Int(6) Declaring Department
  ISExlDocQt VarChar(1) Excl. Docs w/ Qty Less Than default=N [Y=Yes, N=No]
  ISDocQtLm Num(19,6) Document Quantity Limit
  ISExlDocAm VarChar(1) Excl. Docs w/ Amt Less Than default=N [Y=Yes, N=No]
  ISDocAmLm Num(19,6) Document Amount Limit
  ISDspNMass VarChar(1) Always Display Net Mass Value default=Y [Y=Yes, N=No]
  ImInfSup VarChar(1) IS Default Country Import
  Free2 VarChar(1) Free2
  CommerReg nVarChar(60) Commercial Register
  DateOfInc Date(8) Date of Incorporation
  SPEDProf nVarChar(2) SPED Profile
  EnvTypeNFe Int(11) Environment Type NFe default=-1
  Opt4ICMS VarChar(1) Opting for ICMS 115_03 default=N
  ISInstIntr VarChar(1) IS Install Intrastat default=N [Y=Yes, N=No]
  GlblLocNum nVarChar(50) Global Location Number
  PTLedgeGen VarChar(1) Period Type for Ledger Gen. default=M [Y=Year, Q=Quarter, M=Month, P=Period]
  BZStRegID nVarChar(6) BZSt Register ID
  BZStSendID nVarChar(11) BZSt Sender ID
  PostInVat VarChar(1) Post Input VAT in A/P Invoice default=N [Y=Yes, N=No]
  EnbEATrns VarChar(1) Enable EA for Transfer Doc. default=N [Y=Yes, N=No]
  EnbEAInv VarChar(1) Enable EA for Inv. Doc. default=N [Y=Yes, N=No]
  AuthUser nVarChar(100) Authorized User
  AuthPwd nVarChar(100) Authorization Password
  UrlGoods nVarChar(250) URL for Goods Transport
  UrlInvType nVarChar(250) URL for Invoice Type
  ElGoodsFmt Int(11) El. Doc. Format for Goods Trns ->OLLF
  ElInvFmt Int(11) El. Doc. Format for Invoice ->OLLF
  ElDigiCert Text(16) El. Digit. Cert. Path
  TaxRptFrm Date(8) Tax Wizard Reporting From
  Suframa nVarChar(100) SUFRAMA
  EnbInItIQI VarChar(1) Enable Inactive Items in IQI default=N [Y=Yes, N=No]
  EnbInItINC VarChar(1) Enable Inactive Items in INC default=Y [Y=Yes, N=No]
  ExtRevAct VarChar(1) Extend Revenue Accounts default=N [Y=Yes, N=No]
  IsStartup VarChar(1) Identify Startup Company default=N [Y=Yes, N=No]
  IsCUITMndt VarChar(1) Block adding/updating BP without valid CUIT/CUIL default=N [Y=Yes, N=No]
  LnMlBrnch VarChar(1) Allow Linking of Multiple Branches default=Y [Y=Yes, N=No]
  DfBrnchPh VarChar(1) Allow Different Branch in Phases default=Y [Y=Yes, N=No]
  AplShipPch VarChar(1) Apply Ship-to on Purchasing default=N [Y=Yes, N=No]
  AsnBrnchBP VarChar(1) Auto Assign Branches to BP default=Y [Y=Yes, N=No]
  ApyPRinAT VarChar(1) Apply PRJ in Automatic TRN default=N [Y=Yes, N=No]
  ApyDRinAT VarChar(1) Apply DR in Automatic TRN default=N [Y=Yes, N=No]
  EnMlBrkInv VarChar(1) Enable Multiple Broker Invoices for Landed Costs default=N [N=No, Y=Yes]
  PEFilePath Text(16) Payment Bank File Path1
  EnableGDPR VarChar(1) Enable Personal Data Protection Management default=N [Y=Yes, N=No]
  MTDLbltAct nVarChar(15) Outstanding Liabilities Tax Account ->OACT
  MTDClmAct nVarChar(15) Outstanding Refunds Tax Account ->OACT
  RmrksIncld VarChar(1) Document Remarks Include default=Y [Y=Base Document Number, N=BP Reference Number, E=Manual Remarks Only]
  VerfVatNo VarChar(1) Verify VAT Numbers default=N [N=No, Y=Yes]
  VerfVatMxD Int(11) Max. Days for VAT No. Verify default=1
  VerfVatAct nVarChar(100) Verify VAT No. For Doc Action default=NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  CNPJOfIT nVarChar(14) CNPJ of IT Company
  CnPerson nVarChar(60) Contact Person
  Email nVarChar(60) E-Mail
  Telephone nVarChar(50) Phone Number
  ISUseDscSV VarChar(1) Include Document Discount for Statistical Value default=Y [Y=Yes, N=No]
  UrlRegSrv nVarChar(250) URL for Series Registration Service
  ElSersReg Int(11) El. Doc. Format Series Registration
  ELSersCncl Int(11) El. Doc. Format Series Cancelation
  ELSersFin Int(11) El. Doc. Format Series Finalization
  EnbEASer VarChar(1) Enable Electronic Approval for Series default=N [Y=Yes, N=No]
  IntrFLines Int(11) Intrastat Result File Num of Lines default=-1

# AADM - Administration - Log
Module: Administration | 562 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CompnyName nVarChar(100) Company Name
  CompnyAddr nVarChar(254) Address
  Country nVarChar(3) Country/Region ->OCRY
  PrintHeadr nVarChar(100) Printing Header
  Phone1 nVarChar(50) Telephone Number 1
  Phone2 nVarChar(50) Telephone Number 2
  Fax nVarChar(50) Fax Number
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
  BankCountr nVarChar(3) Bank Country/Region
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
  UseExtRpt VarChar(1) Use Extended Reporting (OTRS) default=N [Y=Yes, N=No]
  ERpPerType VarChar(1) Period Type for Report Generation default=M [Y=Year, Q=Quarter, B=Bi-Monthly, M=Month, P=Period, F=Fiscal Year, G=Fiscal Quarter]
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
  RevisionPo VarChar(1) Split Purchase Order default=N [Y=Yes, N=No]
  Reindex VarChar(1) Rebuild Indexes default=N [Y=Yes, N=No]
  DllPath Text(16) Path to Validation DLL
  TaxIdValid VarChar(1) Tax ID Mandatory Validation default=N [Y=Yes, N=No]
  PchName nVarChar(20) Alternate Name for Purchase
  RpcName nVarChar(20) Alternate Name for A/P Credit
  PdnName nVarChar(20) Alternate Name for Goods Rcpt
  RpdName nVarChar(20) Alternate Name for Goods Rtn
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
  Phone1F nVarChar(50) Tel. No. 1 (Foreign Language)
  Phone2F nVarChar(50) Tel. No. 2 (Foreign Language)
  FaxF nVarChar(50) Fax Number (Foreign Lang.)
  ManagerF nVarChar(100) Managing Director (For. Lang.)
  TimeFormat VarChar(1) Time Template default=0 [0=24H, 1=12H]
  CigCup VarChar(1) Cig and Cup Warning default=N [Y=Yes, N=No]
  DateFormat VarChar(1) Date Template default=0 [0=DD/MM/YY, 1=DD/MM/CCYY, 2=MM/DD/YY, 3=MM/DD/CCYY, 4=CCYY/MM/DD, 5=DD/Month/YYYY, 6=YY/MM/DD]
  DateSep VarChar(1) Date Separator default=/
  FcNoBlnc VarChar(1) Foreign Currency Checking Account default=B [B=Block, D=No Message]
  ChangeRdr VarChar(1) Changed Existing Orders default=Y [Y=Yes, N=No]
  MultiCurr VarChar(1) Multi-Currency Check default=B [B=Block, D=No Message]
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
  CustIdNum nVarChar(6) Customer ID default=0
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
  ParamPath Text(16) Parameter Folder Path
  ExcelPath Text(16) Excel Folder Path
  TaxIdNum2 nVarChar(32) Federal Tax ID 2
  TaxIdNum3 nVarChar(32) Federal Tax ID 3
  DecSep VarChar(1) Decimal Separator default=.
  ThousSep VarChar(1) Thousands Separator default=,
  CurOnRight VarChar(1) Display Currency on the Right default=N [Y=Yes, N=No]
  WarnByWhs VarChar(1) Alert by Warehouse default=N [N=No, Y=Yes]
  DflBnkAcKy Int(11) Default Bank Account No. ->DSC1
  PriceSys VarChar(1) Price System default=Y [Y=Whse, N=Item]
  DftPVL Int(11) Preferred Vendor Credit default=-1
  useDdctTrc VarChar(1) WTax Deduction - Hierarchy default=N [Y=Yes, N=No]
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
  ChCtrARAct VarChar(1) Change Def. Recon. A/R Accounts default=N [Y=Yes, N=No]
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
  ExWTLiabl VarChar(1) WTax Liable Expense default=N [Y=Yes, N=No]
  free84 VarChar(1) Free84
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
  TaaSEnable VarChar(1) Enable Tax as a Service default=N [N=No, Y=Yes]
  TaaSUser nVarChar(50) TaaS User Name
  OrderBlock VarChar(1) Order Block
  RoundMthd VarChar(1) Rounding Method default=N [Y=Yes, N=No]
  AdrsFromWH VarChar(1) Use Whse Address in A/P Docs default=Y [Y=Yes, N=No]
  OrderParty nVarChar(30) Ordering Party
  CrtfcateNO nVarChar(20) Certificate No.
  ExpireDate Date(8) Expiration Date
  NINum nVarChar(20) National Insurance No.
  TaaSPass nVarChar(20) TaaS User Password
  TaaSAutURL nVarChar(250) TaaS oAuth URL
  CfwAsnMust VarChar(1) CFW Assignment Mandatory [Y/N] default=Y [N=No, Y=Yes]
  CfwInDflt Int(11) Incoming Payment Draft CF Item
  CfwOutDflt Int(11) Outgoing Payment Dflt CFW Item
  TaaSURL nVarChar(250) TaaS Service URL
  TaaSSaleAc nVarChar(15) TaaS Default Sales Account
  TaxRegime nVarChar(100) Tax Regime
  AliasName Text(16) Alias Name
  DftJPELine VarChar(1) Default Line For Local Area
  RdrConfrmd VarChar(1) Confirmed Sales Order default=Y [Y=Yes, N=No]
  PorConfrmd VarChar(1) Confirmed Purchase Order default=Y [Y=Yes, N=No]
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
  ConsumeFCT VarChar(1) Consumer Forecast default=Y [Y=Yes, N=No]
  ConsumeMtd VarChar(1) Consumption Method default=B [B=Backward-Forward, F=Forward-Backward]
  DaysBack Int(11) Days Backward default=7
  DaysFwrd Int(11) Days Forward default=7
  IsPAPrn VarChar(1) Panama Printer Connected default=N [Y=Yes, N=No]
  ShowNewTsk VarChar(1) Open Worklist on Task Arrival default=Y [N=No, Y=Yes]
  TaxCodeCst nVarChar(8) Def. Tax Code (New Customers) ->OSTC
  TaxCodeVnd nVarChar(8) Def. Tax Code (New Vendors) ->OSTC
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
  UpdateDate Date(8) Update Date
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
  NegTax VarChar(1) Allow Neg. Tax Amt in Returns default=N [Y=Yes, N=No]
  ZeroLine VarChar(1) Allow Zero Amt Row in JE default=Y [Y=Yes, N=No]
  GBOpenFile VarChar(1) Open GBI File After Export default=N [Y=Yes, N=No]
  GBIntface VarChar(1) GBI enabled default=N [Y=Yes, N=No]
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
  AttachPath Text(16) Attachment Path
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
  SplitFBSh VarChar(1) Split Fix Balance Sheet [Y/N] default=N
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
  JeUnGroup VarChar(1) Journal Entry Split Lines default=N [N=No Split, Y=In Preview Only, S=Split, T=Split Except Tax Lines, P=Split Except Tax Lines in Journal Entry Preview Only]
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
  SmtpPasswd nVarChar(254) SMTP Password
  SmtpEncode nVarChar(100) SMTP Encoding default=3 [3=English] ->OLNG
  SmtpAuthen nVarChar(100) SMTP Authentication default=N [N=No Authentication, L=Login Authentication, P=Plain Password]
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
  ExpDocLoc VarChar(1) Export To OneDrive or Locally default=0
  TenantId nVarChar(100) Tenant ID
  IntegUrl nVarChar(254) Integration Server URL default=https://b1-scp-office.cfapps.sap.hana.ondemand.com/
  EnableMTD VarChar(1) Enable Making Tax Digital default=N [N=No, Y=Yes]
  PublicComp VarChar(1) Public Company default=N [Y=Yes, N=No]
  EnableEWB VarChar(1) Enable E-Way Bills default=N [N=No, Y=Yes]
  TspEntry Int(11) Default Transporter
  TspLine Int(11) Default Transportation Line
  EwbGenType VarChar(1) Default EWB Generate Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  VolumeLic VarChar(1) Use Volume Based Licensing default=N [Y=Yes, N=No]
  Threshold Num(19,6) Threshold for Customer Accounting
  EnAuthUpt VarChar(1) Enable Authorizer Update Draft default=N [Y=Yes, N=No]
  DfSVatExG nVarChar(8) Default Tax Code for Realized Exchange Rate Diff. Gain ->OVTG
  DfSVatExL nVarChar(8) Default Tax Code for Realized Exchange Rate Diff. Loss ->OVTG
  EnUpdBpAdr VarChar(1) Enable Updating BP Address ID default=Y [Y=Yes, N=No]
  PAutoDueDt VarChar(1) Definition of Due Date To default=N [Y=Yes, N=No]
  PDuDtMonth Int(6) Month of Due Date To default=1 [1=January, 2=February, 3=March, 4=April, 5=May, 6=June, 7=July, 8=August, 9=September, 10=October, 11=November, 12=December]
  DriDownBOM VarChar(1) Open Item Master Data of an Item Directly with Link Arrow default=N [Y=Yes, N=No]
  EnExtTax VarChar(1) Enable External Tax default=N [Y=Yes, N=No]
  DfDateFct Int(11) Default Valid Date Factor default=1
  DfDateUnit VarChar(1) Default Valid Date Unit default=M [M=Months, W=Weeks, D=Days]
  EnMutiBP VarChar(1) Enable Multiple BPs default=N [Y=Yes, N=No]
  AddBPToEC VarChar(1) Add BP to Existing Equipment Card default=N
  EnAutoRsz VarChar(1) Auto Resize User Forms default=N [Y=Yes, N=No]
  QRMinSize Int(11) Minimum default=1
  QRMaxSize Int(11) Maximum default=40
  QRScale Int(11) Scale default=10
  QRExpDays Int(11) Expiration Days default=10
  QRExpir VarChar(1) Expiration Date default=N [Y=Yes, N=No]
  QRCorrLvl VarChar(1) Correction Level default=M [L=Low, M=Medium, Q=Quartile, H=High]
  TaxCatVer nVarChar(20) Version of Tax Category Code default=32.0
  EffPriDisc VarChar(1) Effective Prices Consider Both Prices Before and After Discount Groups default=N [Y=Yes, N=No]
  CpyBaseAtc VarChar(1) Copy Attachments from Base Document to Target Document default=N [Y=Yes, N=No]
  ItmDupBCD VarChar(1) Duplicate Bar Codes While Duplicating Items default=Y [Y=Yes, N=No]
  AllowUpdat VarChar(1) Allow Update Reference and UDF default=N [Y=Yes, N=No]
  BlkNegJLin VarChar(1) Block Negative Lines default=N [Y=Yes, N=No]
  EnARWTLnMX VarChar(1) Enable Sales WTax in Rows default=N [Y=Yes, N=No]
  PoARPayCat VarChar(1) Post Sales Payment Category WTax default=N [Y=Yes, N=No]
  AplyARExhR VarChar(1) Apply Sales Exchange Rate to WTax default=N [Y=Yes, N=No]
  EnAPWTLnMX VarChar(1) Enable Purchasing WTax in Rows default=N [Y=Yes, N=No]
  PoAPPayCat VarChar(1) Post Purchase Payment Category WTax default=N [Y=Yes, N=No]
  AplyAPExhR VarChar(1) Apply Purchasing Exchange Rate to WTax default=N [Y=Yes, N=No]
  DispCtInBP VarChar(1) Display Inactive Contact Persons in BP Master Data default=Y [Y=Yes, N=No]
  UseDfltPL VarChar(1) Use Default Price List default=N [Y=Yes, N=No]
  DfltCustPL Int(6) Default Price List for Customer
  DfltVendPL Int(6) Default Price List for Vendor
  EORINumber nVarChar(17) EORI Number
  SkipRutChk VarChar(1) Skip check of RUT length default=N [Y=Yes, N=No]
  EnbUQAudit VarChar(1) Enable Execution Audit Log for User-Defined Query default=Y [Y=Yes, N=No]
  CpyBomAtc VarChar(1) Copy Attachments from BOM default=N [Y=Yes, N=No]
  DnOvrwrAtc VarChar(1) Don't overwrite attachments default=N [Y=Yes, N=No]
  IsTAForMI VarChar(1) Enable Creation of Tax Adjustment for Monthly Invoice default=Y [N=No, Y=Yes]
  AutoTAAppr VarChar(1) Tax Adjustment is Approved Automatically default=Y [N=No, Y=Yes]

# AADP - Print Preferences
Module: Administration | 41 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrintId, LogInstanc
Fields (name type(len) description [values] ->parent table):
  PrintId nVarChar(4) Print Number
  ObjList Int(11) Object List default=13 [1470000049=Capitalization, 1470000071=Depreciation Run, 1470000090=Fixed Asset Transfer, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 234000031=Return Request, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 69=Landed Costs, 24=Incoming Payment, 25=Deposit, 46=Outgoing Payment, 76=Postdated Deposit, 57=Check for Payment, 30=Journal Entry, 28=Journal Voucher, 140000010=Incoming Excise Invoice, 140000009=Outgoing Excise Invoice, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 68=Work Instructions, 202=Production Order, 162=Inventory Revaluation, 156=Pick List, 1470000065=Inventory Counting, 10000071=Inventory Posting, 310000001=Inventory Opening Balances, 191=Service Call, 190=Service Contract, 176=Equipment Card, 88=Entrada, 89=Salida, 90=Traspaso, 132=Correction Invoice, 234000021=Project Management Document]
  MaxLineNum Int(6) Max. Rows per Page default=99
  TopMrgn Int(6) Top Margin Width
  BtmMrgn Int(6) Bottom Margin Width
  LftMrgn Int(6) Left Margin Width
  RgtMrgn Int(6) Right Margin Width
  PrnCompany VarChar(1) Print on Company Paper default=N [Y=Yes, N=No]
  MnhlNote VarChar(1) Text Printed by PLD default=Y [Y=Yes, N=No]
  MaxWordLin Int(6) Max. Rows for Export default=10
  V_Compress Int(6) Compress Vertically default=100 [50=50, 60=60, 70=70, 80=80, 90=90, 100=100, 110=110, 120=120, 130=130, 140=140, 150=150]
  WordPath Text(16) WORD Template Path
  BitmapPath Text(16) Picture Path
  PrintMeta VarChar(1) Print as Picture default=N [Y=Yes, N=No]
  PrintRcpt VarChar(1) Print Receipt default=N [N=No, A=Only When Adding, Y=Always]
  ShortRcpt VarChar(1) Print Payment with Invoice default=N [Y=Yes, N=No]
  ExportCode VarChar(1) Export Material/Account Code default=N [Y=Yes, N=No]
  AttachPath Text(16) Attachments Path
  DraftNote VarChar(1) Print Draft Note default=Y [Y=Yes, N=No]
  ExtPath Text(16) Extensions Path
  DmePath Text(16) DME Files Store Path
  SNType Int(6) Serial Number Type default=2 [1=Mfr Serial No., 2=Serial No., 3=Lot Number]
  GBIPath Text(16) GB Data Interface Path
  LogoFile nVarChar(200) Logo File
  LogoImage Text(16) Logo Image
  B1Server Text(16) Business One Server Address
  IsTrustSrv VarChar(1) Always Trust This Server default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User ->OUSR
  SnapShotId Int(11) Snapshot ID default=0
  DefirExpP Text(16) Export Folder
  DefirDemop Text(16) DEFIR Database Path
  PrintPDF VarChar(1) Generate PDF When Printing default=N [Y=Yes, N=No]
  PrtCancel VarChar(1) Print Watermark on Cancl. Docs default=Y [Y=Yes, N=No]
  PrtUseSys VarChar(1) Use System Print Preferences default=N [Y=Yes, N=No]
  RptList nVarChar(20) Report List default=1 [1=Aging Report, 2=Dunning Wizard]
  PreAttach Text(16) Previous Attachment Path
  ExportPDF VarChar(1) Export PDF to Dflt Attachment default=N [Y=Yes, N=No]
  AttachPDF VarChar(1) Attach Exported PDF to Doc default=N [Y=Yes, N=No]
  GSTPath Text(16) GST ANX Report Path

# ABP1 - Business Place Tax IDs
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, DstState, LogInstanc
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) BPL ID ->OBPL
  DstState nVarChar(3) Destination State ->OCST
  IENumber nVarChar(32) I.E. Number
  LogInstanc Int(11) Log Instance default=0

# ABP2 - Branch Tributary Info. Log
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, TributID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) BPL ID ->OBPL
  TributID Int(11) Tributary Info. ID
  TributType Int(11) Tributary Type default=-1 ->OBNI
  TTStartDat Date(8) Tributary Type Start Date
  TTEndDate Date(8) Tributary Type End Date
  TribRegCod Int(11) Tributary Regime Code default=-1 ->OBNI
  TRCStartD Date(8) Tributary Reg. Code Start Date
  TRCEndDate Date(8) Tributary Regime Code End Date
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=247 ->ADP1

# ACEST - CEST Codes
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, LogInstanc
  CEST_CODE U: CEST, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CEST nVarChar(32) CEST Code
  Descr Text(16) Description
  LogInstanc Int(11) Log Instance default=0

# ACFP - CFOP for Nota Fiscal
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID, LogInstanc
  CFOP_CODE U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ID Int(11) CFOP ID
  Code nVarChar(6) CFOP Code
  Descrip Text(16) Description
  App Text(16) Application
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Data Doc., P=Partner Implementation]
  UserSign nVarChar(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# ACRC - Credit Cards
Module: Administration | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CreditCard, LogInstanc
  CARD_NAME: CardName, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CreditCard Int(6) Credit Card Code
  CardName nVarChar(30) Credit Card Name
  AcctCode nVarChar(15) G/L Account ->OACT
  Phone nVarChar(50) Telephone
  CompanyId nVarChar(20) Company ID
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  IntTaxCode nVarChar(2) Internal Tax Code [1=Isracard, 2=CAL, 3=Diners, 4=American Express, 6=Leumi Card]
  UserSign2 Int(6) Updating User ->OUSR
  Country nVarChar(3) Country/Region Code ->OCRY

# ADM1 - Administration Extension
Module: Administration | 135 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  CurrPeriod nVarChar(10) Free
  Street nVarChar(100) Street
  StreetF nVarChar(100) Street Foreign
  Block nVarChar(100) Block
  BlockF nVarChar(100) Block Foreign
  City nVarChar(100) City
  CityF nVarChar(100) City Foreign
  ZipCode nVarChar(20) Zip Code
  ZipCodeF nVarChar(20) Zip Code Foreign
  County nVarChar(100) County
  CountyF nVarChar(100) County Foreign
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country/Region ->OCRY
  IntrntAdrs nVarChar(50) Internet Address
  Code Int(11) Code default=1
  AssType nVarChar(100) Assessee Type
  CompnyType nVarChar(100) Company Type
  NatureBiz nVarChar(100) Nature of Business
  TaxIdNum4 nVarChar(100) Federal Tax ID 4
  TaxIdNum5 nVarChar(100) Federal Tax ID 5
  TaxIdNum6 nVarChar(100) Federal Tax ID 6
  LogInstanc Int(11) Log Instance default=0
  AddrType nVarChar(100) Address Type
  AddrTypeF nVarChar(100) Address Type Foreign
  StreetNo nVarChar(100) Street No.
  StreetNoF nVarChar(100) Street No. Foreign
  Building nVarChar(100) Building/Floor/Room
  BuildingF nVarChar(100) Building/Floor/Room Foreign
  EccNo nVarChar(40) E.C.C. No.
  CERegNo nVarChar(40) C.E. Registration No.
  CERange nVarChar(60) C.E. Range
  CEDivision nVarChar(60) C.E. Division
  CeComRate nVarChar(60) C.E. Commisionerate
  MenuCode nVarChar(60) Manufacturer Code
  Jurisd nVarChar(60) Jurisdiction
  SnapShotId Int(11) Snapshot ID default=0
  STDCode Int(11) STD Code
  STDCodeF Int(11) STD Code Foreign
  CompNature Int(11) Nature of Company default=-1
  EconActT Int(11) Economic Activity Type default=-1
  CredCOrig VarChar(1) Credit Contribution Origin
  IPIPeriod VarChar(1) IPI Period
  CoopAssocT Int(11) Cooperative Association Type default=-1
  DspIBPDoc VarChar(1) Display Inactive Items in Doc. default=Y [Y=Yes, N=No]
  DspIITMDoc VarChar(1) Display Inactive BPs in Doc. default=Y [Y=Yes, N=No]
  ProfTax Int(11) Profit Taxation default=-1
  CompQualif Int(11) Company Qualification default=1
  DeclType Int(11) Declarer Type default=1
  IPITaxCon VarChar(1) IPI Tax Contributor default=N [N=No, Y=Yes]
  ISVATRegNo nVarChar(100) IS VAT Reg. No. of Trader
  ISVATRegEx nVarChar(10) IS VAT Reg. No. Extension
  ISObligLvl VarChar(1) IS Degree of Obligation
  ISTaxState nVarChar(3) IS Federal State of Tax Office ->OCST
  ISComDecID nVarChar(32) IS Company Declaration ID
  OKDPNum nVarChar(7) OKDP Number
  ISValidKey nVarChar(35) IS Validation Key Ident.
  ISDnsce nVarChar(10) IS Declaration Office
  ISDfltPath Text(16) IS Default File Path
  ISSimpProc VarChar(1) IS Simplified Procedure default=Y [Y=Yes, N=No]
  ISForceCmp VarChar(1) IS Require All Data default=Y [Y=Yes, N=No]
  ISCstRecSt nVarChar(6) IS Customs Section
  ISDfltInct Int(11) IS Default Incoterms
  ISDfCPEx Int(11) IS Default Customs Proc. Exp.
  ISDfCPIm Int(11) IS Default Customs Proc. Imp.
  ISDfNTEx Int(11) IS Dflt Nat. of Trans. for Exp
  ISDfNTIm Int(11) IS Dflt Nature of Tran. Imp.
  ISDfPortEx Int(11) IS Default Port for Export
  ISDfPortIm Int(11) IS Default Port for Import
  ISDfSPEx Int(11) IS Default Stat. Proc. Export
  ISDfSPIm Int(11) IS Default Stat. Proc. Import
  ISDfCSTEx Int(11) IS Default State for Export ->ODCI
  ISDfCSTIm Int(11) IS Default State for Import ->ODCI
  ISDfTMEx Int(11) IS Default Transport Mode Exp.
  ISDfTMIm Int(11) IS Default Transport Mode Imp.
  ISDeclDept Int(6) Declaring Department
  ISExlDocQt VarChar(1) Excl. Docs w/ Qty Less Than default=N [Y=Yes, N=No]
  ISDocQtLm Num(19,6) Document Quantity Limit
  ISExlDocAm VarChar(1) Excl. Docs w/ Amt Less Than default=N [Y=Yes, N=No]
  ISDocAmLm Num(19,6) Document Amount Limit
  ISDspNMass VarChar(1) Always Display Net Mass Value default=Y [Y=Yes, N=No]
  ImInfSup VarChar(1) Immediate Information Supply
  Free2 VarChar(1) Free2
  CommerReg nVarChar(60) Commercial Register
  DateOfInc Date(8) Date of Incorporation
  SPEDProf nVarChar(2) SPED Profile
  EnvTypeNFe Int(11) Environment Type NFe default=-1
  Opt4ICMS VarChar(1) Opting for ICMS 115_03 default=N
  ISInstIntr VarChar(1) IS Install Intrastat default=N [Y=Yes, N=No]
  GlblLocNum nVarChar(50) Global Location Number
  PTLedgeGen VarChar(1) Period Type for Ledger Gen. default=M [Y=Year, Q=Quarter, M=Month, P=Period]
  BZStRegID nVarChar(6) BZSt Register ID
  BZStSendID nVarChar(11) BZSt Sender ID
  PostInVat VarChar(1) Post Input VAT in A/P Invoice default=N [Y=Yes, N=No]
  EnbEATrns VarChar(1) Enable EA for Transfer Doc. default=N [Y=Yes, N=No]
  EnbEAInv VarChar(1) Enable EA for Inv. Doc. default=N [Y=Yes, N=No]
  AuthUser nVarChar(100) Authorized User
  AuthPwd nVarChar(100) Authorization Password
  UrlGoods nVarChar(250) URL for Goods Transport
  UrlInvType nVarChar(250) URL for Invoice Type
  ElGoodsFmt Int(11) El. Doc. Format for Goods Trns ->OLLF
  ElInvFmt Int(11) El. Doc. Format for Invoice ->OLLF
  ElDigiCert Text(16) El. Digit. Cert. Path
  TaxRptFrm Date(8) Tax Wizard Reporting From
  Suframa nVarChar(100) SUFRAMA
  EnbInItIQI VarChar(1) Enable Inactive Items in IQI default=N [Y=Yes, N=No]
  EnbInItINC VarChar(1) Enable Inactive Items in INC default=Y [Y=Yes, N=No]
  ExtRevAct VarChar(1) Extend Revenue Accounts default=N [Y=Yes, N=No]
  IsStartup VarChar(1) Identify Startup Company default=N [Y=Yes, N=No]
  IsCUITMndt VarChar(1) Block adding/updating BP without valid CUIT/CUIL default=N [Y=Yes, N=No]
  LnMlBrnch VarChar(1) Allow Linking of Multiple Branches default=Y [Y=Yes, N=No]
  DfBrnchPh VarChar(1) Allow Different Branch in Phases default=Y [Y=Yes, N=No]
  AplShipPch VarChar(1) Apply Ship-to on Purchasing default=N [Y=Yes, N=No]
  AsnBrnchBP VarChar(1) Auto Assign Branches to BP default=Y [Y=Yes, N=No]
  ApyPRinAT VarChar(1) Apply PRJ in Automatic TRN default=N [Y=Yes, N=No]
  ApyDRinAT VarChar(1) Apply DR in Automatic TRN default=N [Y=Yes, N=No]
  EnMlBrkInv VarChar(1) Enable Multiple Broker Invoices for Landed Costs default=N [N=No, Y=Yes]
  PEFilePath Text(16) Payment Bank File Path1
  EnableGDPR VarChar(1) Enable Personal Data Protection Management default=N [Y=Yes, N=No]
  MTDLbltAct nVarChar(15) Outstanding Liabilities Tax Account ->OACT
  MTDClmAct nVarChar(15) Outstanding Refunds Tax Account ->OACT
  RmrksIncld VarChar(1) Document Remarks Include default=Y [Y=Base Document Number, N=BP Reference Number, E=Manual Remarks Only]
  VerfVatNo VarChar(1) Verify VAT Numbers default=N [N=No, Y=Yes]
  VerfVatMxD Int(11) Max. Days for VAT No. Verify default=1
  VerfVatAct nVarChar(100) Verify VAT Num For Doc Action default=NNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  CNPJOfIT nVarChar(14) CNPJ of IT Company
  CnPerson nVarChar(60) Contact Person
  Email nVarChar(60) E-Mail
  Telephone nVarChar(50) Phone Number
  ISUseDscSV VarChar(1) Include Document Discount for Statistical Value default=Y [Y=Yes, N=No]
  UrlRegSrv nVarChar(250) URL for Series Registration Service
  ElSersReg Int(11) El. Doc. Format Series Registration
  ELSersCncl Int(11) El. Doc. Format Series Cancelation
  ELSersFin Int(11) El. Doc. Format Series Finalization
  EnbEASer VarChar(1) Enable Electronic Approval for Series default=N [Y=Yes, N=No]
  IntrFLines Int(11) Intrastat Result File Num of Lines default=-1

# ADM2 - Administration Electronic Report
Module: Administration | 68 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  TaxAuCod nVarChar(5) Tax Authority Code
  KeyEcoAct nVarChar(10) Key Economic Activity
  TaxPayType VarChar(1) Tax Payer Type default=P [P=�94, I=�96, S=�95a]
  TaxLegForm VarChar(1) Tax Payer Legal Form default=P [F=Sole Proprietorship, P=Company]
  RegName nVarChar(254) Registered Name
  RegNameExt nVarChar(11) Registered Name Extension
  SoleFName nVarChar(20) Sole Proprietor First Name
  SoleSName nVarChar(36) Sole Proprietor Surname
  SoleTitle nVarChar(10) Sole Proprietor Title
  CityTown nVarChar(48) City/Town/Village
  ZipCode nVarChar(10) Zip Code
  Telephone nVarChar(50) Telephone
  Street nVarChar(38) Street
  StreetNum nVarChar(4) Street Number
  BuildinNum Int(11) Building Number
  Email nVarChar(254) E-Mail
  State nVarChar(20) State
  RepType VarChar(1) Representative Type default=P [F=Sole Proprietorship, P=Company]
  RepCode nVarChar(2) Representative Code [1=Legal Representative, 2=Authorized Representative, 3=Common Representative, Contractual Representative, 4a=General Appointee - Sole Proprietorship or Company, 4b=Tax Advisor or Attorney, 4c=Tax Advisor]
  RepFName nVarChar(20) Representative First Name
  RepSName nVarChar(36) Representative Surname
  CompName nVarChar(36) Company Name
  BirthDate Date(8) Birth Date
  TaxACNum nVarChar(36) Tax Advisor Certificate Number
  LegEntitID nVarChar(10) Legal Entity ID
  AuthFName nVarChar(20) Authorized Person First Name
  AuthLName nVarChar(36) Authorized Person Last Name
  AuthRelat nVarChar(40) Authorized Person Relation
  AuthType VarChar(1) Type of Authorized Person
  TaxPayAttr nVarChar(2) Taxpayer Attribute
  Classifier nVarChar(11) Territorial/Adm. Classifier
  DeprMethod VarChar(1) Depreciation Method
  SubmitPlac nVarChar(3) Place of Submission
  BgtClass nVarChar(20) Budget Classification Code
  SubjOfRuF nVarChar(20) Subject of Russian Federation
  AuthFathrN nVarChar(254) Father Name
  BgtCleVAT nVarChar(20) Budget Classification Code (E-VAT)
  RepTitle nVarChar(10) Representative Title
  TaxRegime nVarChar(5) Tax Regime default=RF01 [RF01=Ordinary, RF02=Minimum taxpayers (Art. 1, section 96-117, Italian Law 244/07), RF03=New production initiatives (Art. 13, Italian Law 388/00), RF04=Agriculture and connected activities, and fishing (Arts. 34 and 34-bis, Italian Presidential Decree 633/72), RF05=Sale of salts and tobaccos (Art. 74, section 1, Italian Presidential Decree 633/72), RF06=Match sales (Art. 74, section 1, Italian Presidential Decree 633/72), RF07=Publishing (Art. 74, section 1, Italian Presidential Decree 633/72), RF08=Management of public telephone services (Art. 74, section 1, Italian Presidential Decree 633/72), RF09=Resale of public transport and parking documents (Art. 74, section 1, Italian Presidential Decree 633/72), RF10=Entertainment, gaming and other activities referred to by the tariff attached to Italian Presidential Decree 640/72 (Art. 74, section 6, Italian Presidential Decree 633/1972), RF11=Travel and tourism agencies (Art. 74-ter, Italian Presidential Decree 633/72), RF12=Farmhouse accommodation/restaurants (Art. 5, section 2, Italian Law 413/91), RF13=Door-to-door sales (Art. 25-bis, section 6, Italian Presidential Decree 600/73), RF14=Resale of used goods, artworks, antiques or collector's items (Art. 36, Italian Decree Law 41/95), RF15=Artwork, antiques or collector's items auction agencies (Art. 40-bis, Italian Decree Law 41/95), RF16=VAT paid in cash by P.A. (Art. 6, section 5, Italian Presidential Decree 633/72), RF17=VAT paid in cash by subjects with business turnover below Euro 200,000 (Art. 7, Italian Decree Law 185/2008), RF18=Other, RF19=Regime forfettario (art.1, c.54-89, L. 190/2014)]
  SoleBDate Date(8) Sole Proprietor Date of Birth
  SoleGender VarChar(1) Sole Proprietor Gender default=M [F=Female, M=Male, E=Not Specified]
  SoleCity nVarChar(40) Sole Proprietor City of Birth
  SoleDistri nVarChar(3) Sole Proprietor State of Birth
  RepFisCode nVarChar(16) Representative Fiscal Code
  RepPosCode nVarChar(2) Representative Position Code
  RepGender VarChar(1) Representative Gender default=M [F=Female, M=Male, E=Not Specified]
  RepCity nVarChar(40) Representative City of Birth
  RepDistri nVarChar(3) Representative State of Birth
  RepDate1 Date(8) Representative Start Date of Procedure
  RepDate2 Date(8) Representative End Date of Procedure
  RepPhone nVarChar(14) Representative Telephone
  RepEmail nVarChar(254) Representative E-Mail
  Country nVarChar(3) Country/Region ->OCRY
  District nVarChar(3) District ->OCST
  RegDistri nVarChar(3) Register District
  RegSCAmnt Num(19,6) Share Capital Amount
  RegSHolder nVarChar(2) Shareholder default=SU [SU=Sole Shareholder, SM=Several Shareholders]
  RegLiquida nVarChar(2) Liquidation default=LN [LS=In Liquidation, LN=Not in Liquidation]
  RepAddID nVarChar(28) Representative Additional ID
  ActCode nVarChar(15) Activity Code
  PosCode347 nVarChar(2) Position Code for Report 347 [1=1, 2=2, 3=3, 4=4, 5=5, 6=6, 7=7, 8=8, 9=9, 10=10, 11=11, 12=12, 13=13, 14=14, 15=15]
  FiscalCode nVarChar(16) Fiscal Code
  DataBoxID nVarChar(10) Data Box ID
  SmValLimit Num(19,6) Small Value Documents Limit
  RepCEOName nVarChar(254) Representative CEO Name
  RepCEOFisC nVarChar(16) Representative CEO Fiscal Code
  CmpnTypeFR nVarChar(30) Type d'entreprise

# ADP1 - Object Settings - History
Module: Administration | 67 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrintId, ObjType
  OBJECT U: ObjType
Fields (name type(len) description [values] ->parent table):
  PrintId nVarChar(4) Print No. ->OADP
  ObjType nVarChar(20) Object Type
  Copies Int(6) No. of Copies default=1
  PrintOnAdd VarChar(1) Add & Print default=N [Y=Yes, N=No]
  ExprtOnAdd VarChar(1) Add & Export default=N [Y=Yes, N=No]
  RoundSums VarChar(1) Rounding Amounts default=N [Y=Yes, N=No]
  Remark Text(16) Standard Remarks
  PrintSums VarChar(1) Print Totals default=Y [Y=Yes, N=No]
  VndrNum VarChar(1) Print Mfr Catalog No. default=N [Y=Yes, N=No]
  PrnDscnt VarChar(1) Print Discount Data default=Y [Y=Yes, N=No]
  SplitTran1 VarChar(1) Split Transaction 1 default=N [Y=Yes, N=No]
  SplitTran2 VarChar(1) Split Transaction 2 default=Y [Y=Yes, N=No]
  SplitTran3 VarChar(1) Split Transaction 3 default=Y [Y=Yes, N=No]
  ShowBothNu VarChar(1) Print Mfr Catalog No. Instead default=N [Y=Yes, N=No]
  BaseRmrk VarChar(1) Display Base Remarks default=Y [Y=Yes, N=No]
  HandCopies Int(6) No. of Copies for Manual Doc. default=1
  EngKBItem VarChar(1) Switch to English Keyboard when Entering an Item default=N [Y=Yes, N=No]
  EngKBCard VarChar(1) Switch to English Keyboard when Entering a BP default=N [Y=Yes, N=No]
  OrdrPicDef VarChar(1) Set Pick Order as Default default=N [Y=Yes, N=No]
  SpltTrBOE1 VarChar(1) Split Bill of Exchange Transaction default=N [Y=Yes, N=No]
  LineNumPPg Int(6) Row Item Number Per Page default=5
  JENumPPg Int(6) Journal Entry Number Per Page default=2
  CashPay Text(16) Remark for Cash Payments
  NonCashPay Text(16) Remark for Non-Cash Payments
  MaxUOPay Num(19,6) Max. Under/Overpayment Amount
  CkeckPaper VarChar(1) Paper for Checks default=S [B=Blank Paper, S=Overflow Check Stock, P=Overflow Blank Paper]
  AllowFuPos VarChar(1) Allow Future Posting default=N [Y=Yes, N=No]
  ErdOutMode VarChar(1) ERD Mode for Outgoing Payments default=N [Y=Yes, N=No]
  ErdIncMode VarChar(1) ERD Mode for Incoming Payments default=N [Y=Yes, N=No]
  ChkDupRef VarChar(1) Check Duplicate BP Reference Number default=N [N=Without Warning, W=Warning Only, B=Block Release]
  CpyCVRef VarChar(1) Copy BP Reference Number default=N [N=No, Y=Yes]
  BatchSerPr VarChar(1) Batch/Serial No. Print Definitions default=A [A=Document and Batch/Serial No., D=Document Only, B=Batch/Serial No. Only]
  YearTrans VarChar(1) Display Transaction in Payment default=N [N=No, Y=Yes]
  ReconJeSer Int(6) Reconciliation JE Series default=0
  ReopOrder VarChar(1) Enable Reopen Orders by Return default=N [N=No, Y=Yes]
  ForceReOrd VarChar(1) Always Reopen Orders by Return default=N [N=No, Y=Yes]
  PrintRows VarChar(1) Print Rows default=A [A=All Rows, M=All Modified Rows, T=Modified Rows Excl. Tax Amount]
  orderblock VarChar(1) Block Early Posting Date default=N [Y=Yes, N=No]
  RecomPkg VarChar(1) Recommend Packaging default=N [N=No, Y=Yes]
  Enitemcost VarChar(1) Enable Setting Item Cost default=N [Y=Yes, N=No]
  ClosePQ VarChar(1) Close Related PQ default=Y [Y=Yes, N=No]
  CpyPRPrice VarChar(1) Enable Copying PR Price default=N [Y=Yes, N=No]
  EnSetCost VarChar(1) Enable Setting Cost By Default default=N
  DftPLChk VarChar(1) Default Price List Check default=N
  DfltPLSel Int(6) Default Price List Selection default=-1
  EmailOnAdd VarChar(1) Add & E-Mail default=N [Y=Yes, N=No]
  PDFOnAdd VarChar(1) Add & Export to PDF default=N [Y=Yes, N=No]
  EmailSbj nVarChar(254) E-Mail Subject
  EmailBody Text(16) E-Mail Body
  BlockWHT08 VarChar(1) Block payment in local currency WHT 08 default=N [Y=Yes, N=No]
  BlockExprt VarChar(1) Block Export to Word default=N [N=No, Y=Yes]
  BlockPrint VarChar(1) Block print document default=N [N=No, Y=Yes]
  BlockMail VarChar(1) Block Email Document default=N [N=No, Y=Yes]
  BlockToPDF VarChar(1) Block Export to PDF default=N [N=No, Y=Yes]
  BlockFax VarChar(1) Block Sent to Fax default=N [N=No, Y=Yes]
  PoDropPrss VarChar(1) PO Drop-Ship Process default=Y [Y=Yes, N=No]
  ShowCash VarChar(1) Allow Cash Accounts Only default=N [Y=Yes, N=No]
  PRUseBPTax VarChar(1) Purchase Request use BP Tax default=N [Y=Yes, N=No]
  EnblTtlEgD VarChar(1) Apply Exchange Rate of Drawn Down Payments default=N [Y=Yes, N=No]
  EnblUpdUDF VarChar(1) Enable Updating UDF default=N [Y=Yes, N=No]
  EnblDpmTax VarChar(1) Enable Tax Calculation in Down Payment Invoices default=N [Y=Yes, N=No]
  ChkRefBP VarChar(1) Validate on Customer Level default=N [Y=Yes, N=No]
  ChkRefYear VarChar(1) Validate on Fiscal Year Level default=N [Y=Yes, N=No]
  BspDpmType VarChar(1) Down Payment Type for BSP default=E [E=, R=Down Payment Request, I=Down Payment Invoice]
  ReopenByC VarChar(1) Enable the Displaying of Base Document Items When Target Documents Are Canceled default=N [N=No, Y=Yes]
  ForceReByC VarChar(1) Always Display Base Document Items When Target Documents Are Canceled default=N [N=No, Y=Yes]
  OpenSnB VarChar(1) Open SnB form for Bin First Item when Auto Allocation default=N [N=No, Y=Yes]

# ADP2 - Report Settings - History
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrintId, RptType
  OBJECT U: RptType
Fields (name type(len) description [values] ->parent table):
  PrintId nVarChar(4) Print No. ->OADP
  RptType nVarChar(20) Report Type [1=Aging Report, 2=Dunning Wizard]
  EmailSbj nVarChar(254) E-Mail Subject
  EmailBody Text(16) E-Mail Body

# AEXD - Freight Setup
Module: Administration | 40 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ExpnsCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ExpnsCode Int(11) Internal Number
  ExpnsName nVarChar(20) Name
  RevAcct nVarChar(15) Revenue Account ->OACT
  ExpnsAcct nVarChar(15) Expense Account ->OACT
  TaxLiable VarChar(1) Tax Liable default=N [Y=Yes, N=No]
  RevFixSum Num(19,6) Fixed Amount - Revenues
  ExpFixSum Num(19,6) Fixed Amount - Expenses
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  VatGroupI nVarChar(8) Output Tax Group ->OVTG
  VatGroupO nVarChar(8) Input Tax Group ->OVTG
  DistrbMthd VarChar(1) Distribution Method default=N [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  In1099 VarChar(1) Include in 1099 default=N [Y=Yes, N=No]
  ExpOfstAct nVarChar(15) Freight Clearing Account ->OACT
  WTLiable VarChar(1) WTax Liable default=N [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method default=T [N=None, Q=Quantity, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price default=N [Y=Yes, N=No]
  SalseRpt VarChar(1) Sales Analysis Report default=N [Y=Yes, N=No]
  PchRpt VarChar(1) Purchase Analysis Report default=N [Y=Yes, N=No]
  RevExmAcct nVarChar(15) Revenues Exempted Account ->OACT
  ExpnsExAct nVarChar(15) Expense Exempted Account ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account
  ExpnsType VarChar(1) Freight Type [1=Shipping, 2=Insurance, 3=Other]
  OcrCode nVarChar(8) Distribution Rule ->OOCR
  TaxDisMthd VarChar(1) Tax Distribution Method default=N [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distribution Rule 2 ->OOCR
  OcrCode3 nVarChar(8) Distribution Rule 3 ->OOCR
  OcrCode4 nVarChar(8) Distribution Rule 4 ->OOCR
  OcrCode5 nVarChar(8) Distribution Rule 5 ->OOCR
  OcrCodeX nVarChar(100) Distribution Rule X ->OOCR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User ->OUSR
  Project nVarChar(20) Project ->OPRJ
  Intrastat VarChar(1) Intrastat Relevant default=N [Y=Yes, N=No]
  GrsFreight VarChar(1) Gross Freight default=N [Y=Yes, N=No]
  SacCode nVarChar(8) SAC Code
  FreighType VarChar(1) Freight Type default=S [S=Standard, B=Bollo]
  DataVers Int(11) Data Version default=1

# AFM1 - Tax Formula Parameter Declaration
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FmlId, DispOrder, LogInstanc
Fields (name type(len) description [values] ->parent table):
  FmlId Int(11) Formula ID ->OFML
  DispOrder Int(11) Display Order
  VarName nVarChar(64) Variable Name
  Category VarChar(1) Category default=1 [1=Input, 2=Output, 3=In Out]
  Parameter Text(16) Parameter
  DataType VarChar(1) Data Type default=S [T=Tax Amounts, S=Amounts, P=Prices, Q=Quantities, %=Percents, I=Integer, A=String, B=Boolean, M=Measures]
  LogInstanc Int(11) Log Instance default=0

# AFML - Tax Formula Master Table
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, LogInstanc
  CODE U: FmlType, Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(20) Code
  Descr nVarChar(100) Description
  SttId Int(11) Tax Type ID ->OSTT
  FmlLang Text(16) Formula Language Free Text
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  FmlType VarChar(1) Formula Type default=T [T=Tax, W=WTax]
  IsOrigFml VarChar(1) Original/Edited Formula default=Y [Y=Yes, N=No]

# AINF - Company Info
Module: Administration | 220 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  CompnyName nVarChar(100) Company Name
  Flags nVarChar(50) Flags default=NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  InfoL1 Int(11) Info L1
  InfoL2 Int(11) Info L2
  InfoA1 nVarChar(128) Info A1
  InfoA2 nVarChar(50) Info A2
  ACTStamp Int(11) ACT Stamp default=0
  ADMStamp Int(11) (( default=0
  RTTStamp Int(11) RTT Stamp default=0
  CINFStamp Int(11) CINF Stamp default=0
  LawsSet nVarChar(3) Laws Set
  EnblVatGrp VarChar(1) Tax System [O=One Tax, L=Tax per Row, C=Tax per BP]
  EnblVTGPmn VarChar(1) Use Tax Groups in Payments [Y=Yes, N=No]
  VatOOS_O nVarChar(8) Tax Definition
  VatOOS_I nVarChar(8) Tax Exempt Revenue Account
  VatStnd_O nVarChar(8) Tax Standard O
  VatStnd_I nVarChar(8) Tax Standard I
  VatExmpt_O nVarChar(8) Tax Exempt O
  VatExmpt_I nVarChar(8) Tax Exempt I
  VatHalf_O nVarChar(8) Tax Definition
  VatHalf_I nVarChar(8) Tax Definition
  VatZrRt_O nVarChar(8) Tax Zero Rate O
  VatZrRt_I nVarChar(8) Tax Zero Rate I
  MaxActGrps Int(11) Max. No. of Account Groups
  EnblDctSrc VarChar(1) Enable Deduction at Source [Y=Yes, N=No]
  EnblRCN VarChar(1) Enable Retail Chain Stores [Y=Yes, N=No]
  EnblCorINV VarChar(1) Enable Correction Invoice [Y=Yes, N=No]
  EnblCshRep VarChar(1) Enable Cash Report [Y=Yes, N=No]
  EnblIRTRep VarChar(1) Enable Interest Report [Y=Yes, N=No]
  EnblTrnRep VarChar(1) Enable Turnover Report [Y=Yes, N=No]
  EnblVPMRep VarChar(1) Enable Payments Report [Y=Yes, N=No]
  EnblACTRep VarChar(1) Enable Adv. Corp. Tax Report [Y=Yes, N=No]
  EnblFTZ VarChar(1) Enable Free Trade Zone [Y=Yes, N=No]
  EnblSlfPCH VarChar(1) Enable Self A/P Invoice [Y=Yes, N=No]
  EnblPCHUpd VarChar(1) Enable Purchase Trans. Update [Y=Yes, N=No]
  EnblRsvINV VarChar(1) Enable Reserve Invoice [Y=Yes, N=No]
  EnblRTDnld VarChar(1) Enable Rates Download [Y=Yes, N=No]
  RTTDnldAdr nVarChar(254) Rates Download Web Address
  ZPrcCode nVarChar(8) Zero Center Code
  EnblExpns VarChar(1) Enable Freight Management [Y=Yes, N=No]
  EnblRtrRep VarChar(1) Enable Returns Report [Y=Yes, N=No]
  IsEC VarChar(1) European Countries [Y=Yes, N=No]
  EnblCshDsc VarChar(1) Enable Cash Discounts [Y=Yes, N=No, V=No Tax Adjustment]
  EnblLostCD VarChar(1) Enable Lost Cash Discount [Y=Yes, N=No]
  NumActLvls Int(11) No. of Account Group Levels
  EnblRealRD VarChar(1) Enable Realized Rate Diff. [Y=Yes, N=No]
  EnblVTGNoD VarChar(1) Enable Tax on Down Payment default=Y [Y=Yes, N=No]
  EnblGLManP VarChar(1) Enable Manual Postings in Control Account [N=No, Y=Yes]
  EnblOptVIP VarChar(1) Enable Optional Tax in Payments [Y=Yes, N=No]
  EnblActCrC VarChar(1) Enable Account Currency Change [Y=Yes, N=No]
  EnblFrnAct VarChar(1) Enable Foreign Item Account [Y=Yes, N=No]
  EnblECAct VarChar(1) Enable EU Item Account [Y=Yes, N=No]
  EnblECRpt VarChar(1) Enable 349 Report [Y=Yes, N=No]
  EnblRound VarChar(1) Enable Rounding [Y=Yes, N=No]
  EnblPrVatS VarChar(1) Enable Print Tax Amount [Y=Yes, N=No]
  EnblYrTrns VarChar(1) Enable Year Transfer [Y=Year Transfer, N=No, A=Data Archive]
  EnblActTtl VarChar(1) Enable Account Title [Y=Yes, N=No]
  EnblDocWrn VarChar(1) Enable No Base Doc. Alert [Y=Yes, N=No]
  ActSegNum Int(6) No. of Segments default=0
  EnbSgmnAct VarChar(1) Enable Account Segmentation [Y=Yes, N=No]
  SizeOfSeg0 Int(6) Size of Segment 0 default=0
  SizeOfSeg1 Int(6) Size of Segment 1 default=0
  SizeOfSeg2 Int(6) Size of Segment 2 default=0
  SizeOfSeg3 Int(6) Size of Segment 3 default=0
  SizeOfSeg4 Int(6) Size of Segment 4 default=0
  SizeOfSeg5 Int(6) Size of Segment 5 default=0
  SizeOfSeg6 Int(6) Size of Segment 6 default=0
  SizeOfSeg7 Int(6) Size of Segment 7 default=0
  SizeOfSeg8 Int(6) Size of Segment 8 default=0
  SizeOfSeg9 Int(6) Size of Segment 9 default=0
  Rprt1099 VarChar(1) 1099 Report [Y=Yes, N=No]
  MultiAddss VarChar(1) Multi Address [Y=Yes, N=No]
  EnbDunning VarChar(1) Enable Dunning default=Y [Y=Yes, N=No]
  EnbQtyEDln VarChar(1) Allow Qty in Delivery Note to Exceed Base Doc. Qty [Y=Yes, N=No]
  Itw1Date Date(8) Next Alert Date
  Itw1Time Int(11) Next Alert Time
  Itw1Count Int(11) ITW1 Counter
  EnbPayRef VarChar(1) Calculate Payment Ref. No. [Y=Payment Reference No., N=No, I=ISR Reference]
  EnblDfrTax VarChar(1) Enable Deferred Tax [Y=Yes, N=No]
  EnblClsPr VarChar(1) Enable Period-End Closing [Y=Yes, N=No]
  EnblTaxEL VarChar(1) Enable Tax Exemption Letter [Y=Yes, N=No]
  EnableBOE VarChar(1) Enable Bills of Exchange default=N [Y=Yes, N=No]
  EnableWHT VarChar(1) Enable WTax default=N [Y=Yes, N=No]
  EnblEquVat VarChar(1) Enable Equalization Tax [Y=Yes, N=No]
  EnblFAsset VarChar(1) Enable Fixed Assets [Y=Yes, N=No]
  EnblDoubt VarChar(1) Enable Doubtful Debts [Y=Yes, N=No]
  RateBase VarChar(1) Base Date for Exchange Rate default=P [P=Posting Date, T=Document Date]
  BOEStatClo VarChar(1) Allow Closed Status for Bill of Exchange [Y=Yes, N=No]
  ARDocsInWT VarChar(1) Enable WTax in A/R Docs [N=No, Y=Yes]
  BISBnkCnt nVarChar(3) BISR Bank Country/Region
  BISRBnkCd nVarChar(30) BISR Bank No.
  BISRBnkAc nVarChar(50) BISR Bank Account
  BISRBranch nVarChar(50) BISR Branch
  EnblBPConn VarChar(1) Enable BP Cards Connection [Y=Yes, N=No]
  EnblVATDat VarChar(1) Enable VAT Date [Y=Yes, N=No]
  EnblStAgRp VarChar(1) Enable Stock Aging Report [Y=Yes, N=No]
  EnblCARepo VarChar(1) Enable Control Acct Reposting [Y=Yes, N=No]
  EnblMatRev VarChar(1) Enable Inventory Revaluation [Y=Yes, N=No]
  EnblMBPRec VarChar(1) Enable Multiple BPs Reconcil. [Y=Yes, N=No]
  CshDscGros VarChar(1) Cash Discount Flag For CN, HK default=N
  EnblTaxInv VarChar(1) Enable Tax Invoices [Y=Yes, N=No]
  EnblCorAct VarChar(1) Enable Correspondence of Accts [N=No, Y=Yes]
  EnblRuDIP VarChar(1) Enable RU Delivery & Invoice [N=No, Y=Yes]
  EnblCurDec VarChar(1) Enable Decimal Places [N=No, Y=Yes]
  EnblPayMtd VarChar(1) Enable Payment Method on Inv. [N=No, Y=Yes]
  EnblBaseUn VarChar(1) Enable UoM on Invoice [N=No, Y=Yes]
  EnblVATAna VarChar(1) Enable VAT Analytics Report [N=No, Y=Yes]
  EnblExREnh VarChar(1) Enable Frgn. Curr. Valuation [Y=Yes, N=No]
  VATGrpCal VarChar(1) Enable VAT Calculation by Grp [Y=Yes, N=No]
  MaxChoose Int(11) No. of Choose from List Rows default=0
  EnblInfla VarChar(1) Enable Inflation [Y=Yes, N=No]
  EnblLAWHT VarChar(1) Enable Latin America WHT [Y=Yes, N=No]
  EnblRTWHT VarChar(1) Enable Rounding Type WHT [Y=Yes, N=No]
  ChkQunty VarChar(1) Enable Check Quantity In RDR default=N [Y=Yes, N=No]
  SriMngSys VarChar(1) SRI Management System default=R [A=On Every Transaction, R=On Release Only]
  BtchMngSys VarChar(1) Batch Management System default=R [A=On Every Transaction, R=On Release Only]
  SriCreatIn VarChar(1) Auto SRI creation on receipt default=N [N=No, Y=Yes]
  EnblFolio nVarChar(2) Enable Folio Numbers [N=No, CL=Chile, MX=Mexico]
  EnblDocSbT nVarChar(2) Enable Document Subtype [N=No, CL=Chile, MX=Mexico, IN=India]
  IepsPayer VarChar(1) IEPS Payers default=N [Y=Yes, N=No]
  DaysOrdCnc Int(11) Default Days for Ord. Canc. default=30
  EnblLATaxS VarChar(1) Enable Latin America Tax Sys [Y=Yes, N=No]
  PercOfAcq Num(19,6) Percent of Total Acquisition
  MinBaseDoc Num(19,6) Minimum Base Amount per Doc
  EnblDpmJdt VarChar(1) Create JE Rows in Down Pmnt [Y=Yes, N=No]
  EnblDownP VarChar(1) Down Payment [Y=Yes, N=No]
  EnblNDdctC VarChar(1) Enable Non Deduct VAT Per Card [Y=Yes, N=No]
  DocNmMtd VarChar(1) Enable Sharing Series [Y=Yes, N=No.]
  DoFilter VarChar(1) Data Ownership Indication default=N [Y=Yes, N=No]
  EnblOnPDCh VarChar(1) Enable Opened Postdated Checks [Y=Yes, N=No]
  EnblOnWnCr VarChar(1) Open Window for Credit Voucher [Y=Yes, N=No]
  EnblDefInx VarChar(1) Enable Define Indexes [Y=Yes, N=No]
  EnblMxComm VarChar(1) Enable Max Commitment [Y=Yes, N=No]
  EnblIndxOp VarChar(1) Enable Index Option [Y=Yes, N=No]
  EnblSbtCVo VarChar(1) Enable Submit Credit Voucher [Y=Yes, N=No]
  MinAmntOAP Num(19,6) Minimum Amount for Appndix O&P
  CredSumm VarChar(1) Credit Card Summary [Y=Yes, N=No]
  PostdChk VarChar(1) Postdated Check [Y=Yes, N=No]
  PostdCred VarChar(1) Postdated Credit Voucher [Y=Yes, N=No]
  CredVend VarChar(1) Credit Vendors [Y=Yes, N=No]
  WkoStatus VarChar(1) Old Work Order Status [Y=Yes, N=No]
  DispTrByDf VarChar(1) Display Transactions by Dflt default=Y [Y=Yes, N=No]
  stampTax nVarChar(8) Default Stamp Tax ->OVTG
  MinAmntAL Num(19,6) Minimum Amount for Annual List
  BlockZeroQ VarChar(1) Block Stock Negative Quantity default=Y [Y=Yes, N=No]
  AutoCrIns VarChar(1) Auto Create Customer Eq Card default=N [Y=Yes, N=No]
  EnbRepomo VarChar(1) Enable Inflation for Cash Act [Y=Yes, N=No]
  RFCValidat VarChar(1) Enable RFC Validations [Y=Yes, N=No]
  MxDcsInPmt Int(11) Max. Number of Documents in Payment default=0
  RelStkNoPr VarChar(1) Enable Stock Release without Item Cost default=N [Y=Yes, N=No]
  CashDisc VarChar(1) Cash Discount In Document [Y=Yes, N=No]
  EnableSMS VarChar(1) Enable SMS [Y=Yes, N=No]
  EnblIndic VarChar(1) Enable Indicator [Y=Yes, N=No]
  EnbFedTax VarChar(1) Enable Federal Tax ID [Y=Yes, N=No]
  EnblCounty VarChar(1) Enable County [Y=Yes, N=No]
  Language Int(11) Language on Create Company
  ChkIntgUpd VarChar(1) Check Data Integrity On Update default=Y [Y=Yes, N=No]
  ChkIntgCre VarChar(1) Check Data Integrity On Create default=Y [Y=Yes, N=No]
  BisBnkAcKy Int(11) BISR Bank Account Key ->DSC1
  EnbZeroDec VarChar(1) Enable Print Check Show Zero Decimal default=N [Y=Yes, N=No]
  EnbDecWord VarChar(1) Show Check Decimal in Words default=Y [Y=Yes, N=No]
  ChkWrdOnly VarChar(1) Add the Word Only in Checks [Y=Yes, N=No]
  EnBnkStmnt VarChar(1) Bank Statement Processing default=N [Y=Yes, N=No]
  CalcVatGrp VarChar(1) Group Lines in VAT Calculation [Y=Yes, N=No]
  TaxSysType VarChar(1) Defines Tax Calculation System [A=Preconfigured Formula with Jurisdiction Support, B=User-Defined Formula, C=Preconfigured Formula, M=Fixed Implementation with Jurisdiction Support, S=Fixed Implementation]
  ESEnabled VarChar(1) Is Event Sender enabled? default=N [Y=Yes, N=No, C=Customize]
  RateTotal VarChar(1) Use rate for minor total calc. default=N [N=No, Y=Yes]
  CompanyHis Text(16) Create/Upgrade History
  EnblAssVal VarChar(1) Enable Assessable Value default=N [Y=Yes, N=No]
  CompanySta VarChar(1) Company Status default=U [V=Valid, I=Invalid, U=Upgrading, A=Archived, S=Inventory Valuation Utility, P=Upgrade Simulation]
  eFRTActLvs Int(11) No. of Levels in Elect. FRT
  TaxGrpType VarChar(1) Defines Tax Grouping Type default=C [C=Code, J=Jurisdiction]
  InstallNo nVarChar(30) Installation Number
  IsOldPA VarChar(1) Is Old for PA default=N [N=No, Y=Yes]
  EnbNegDoc VarChar(1) Enable Negative Total in Doc
  Algo Int(6) Encryption Algorithm
  ArcComp VarChar(1) Archived Company default=N [Y=Yes, N=No]
  UpdatedTF VarChar(1) Is Updated Tax Formula default=N [N=No, Y=Yes]
  DARDBGUID nVarChar(32) Readonly DB GUID for Archiving
  NegStoLv VarChar(1) Negative Inv.: Check Level default=I [C=Company, W=Warehouse, I=Item Setting]
  SPNEnabled VarChar(1) Enable Transact. Notification default=Y [Y=Yes, N=No]
  PrsWkCntEb VarChar(1) Personal Work Center Enabled default=N [N=No Cockpit, Y=Normal Style Cockpit, F=Fiori Style Cockpit]
  DashbdEb VarChar(1) Dashboard Enabled default=N [Y=Yes, N=No]
  BoxEffDate Date(8) Box: Effective From Date
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User ->OUSR
  SnapShotId Int(11) Snapshot ID default=0
  CreatedBy VarChar(1) Created By default=N [N=, P=Solution Packager, W=Express Configuration Wizard]
  B1SgtEb VarChar(1) B1 Suggest: Enable default=N [Y=Yes, N=No]
  IsHConEnv VarChar(1) Is in High Concurrency Env default=N [Y=Yes, N=No]
  B1BuzzEb VarChar(1) Enable Streamwork Widget default=N
  IMCEEnable VarChar(1) IMCE Enable default=N [Y=Yes, N=No]
  DKeyId nVarChar(128) Current Dynamic Key ID
  ResetDData VarChar(1) Reset Dyn. Key Data to Default default=N
  ConvDifAct VarChar(1) Enable Conversion Diff. Acct default=Y [Y=Yes, N=No]
  BasEffDate Date(8) Base Effective From Date
  oldFxAss VarChar(1) Has Used Old Fixed Assets default=N [Y=Yes, N=No]
  MaxRowsCFL Int(11) Max. Rows for Choose from List default=0 [0=Unlimited, 5000=5000, 10000=10000, 50000=50000, 100000=100000]
  ColSel Text(16) Column Selection
  EnblSPEDUF VarChar(1) Enable SPED Related UDFs default=N [Y=Yes, N=No]
  DpmAffTot VarChar(1) Down Payment Affects Total default=Y [Y=Yes, N=No]
  AliasUpd nVarChar(254) Installation Date
  TrailDays Int(6) Trial Days
  TestComp VarChar(1) Test Comp. default=N [N=No, Y=Yes]
  DashConf Text(16) Enable Side Bar
  SideEnable VarChar(1) Enable Side Bar default=N [Y=Yes, N=No]
  IsPALInit VarChar(1) Is PAL Init. or Not default=N
  PANAVer Int(11) Pervasive Version default=0
  ExpEnable VarChar(1) Enable Expense Claim default=Y
  LastSsrDat Date(8) Last SSR upload date
  LastSsrHsh nVarChar(33) Last SSR upload date hash
  B1iTimeOut Int(11) B1i Request Timeout default=30
  CpRfshEnbl VarChar(1) Enable Cockpit Auto Refresh default=N
  CpRfshIntv Int(11) Cockpit Refresh Interval default=300
  EnbMBFilt VarChar(1) Enable Filtering Mechanism by Branch default=N [Y=Yes, N=No]
  CompnyGUID nVarChar(40) Company GUID
  ShutTime Int(11) SAP Business One Shutdown Time
  Migrated VarChar(1) Migrated DB default=N [Y=Yes, N=No]

# ALR1 - Queue of messages to be sent
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineId
  STATUS: Status
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number ->OALR
  LineId Int(11) Row Number
  NameFrom nVarChar(155) From
  AddrFrom nVarChar(100) Reply Address
  NameTo nVarChar(155) To
  IsSMS VarChar(1) SMS default=N [Y=Yes, N=No, F=Fax]
  Address nVarChar(100) Address
  Status VarChar(1) Status default=U [U=Not Sent, P=In Process, S=Sent]
  ObjType nVarChar(20) Object
  ObjCode nVarChar(50) Object Code

# ALR2 - Dynamic message data row
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Location
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number ->OALR
  Location Int(11) The order of columns in message
  ColName nVarChar(30) The column name in message
  Link VarChar(1) Link Indication default=N [N=No, Y=Yes]

# ALR3 - Dynamic message data cells
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Location, Line
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number ->OALR
  Location Int(11) Number of Column in Message
  Line Int(11) Number of Column in Message
  Value nVarChar(254) The column/row value
  ObjType nVarChar(20) The linked object
  KeyStr nVarChar(254) Key string in linked object

# ALT1 - Alerts - Users
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, UserSign
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  UserSign Int(6) User Signature ->OUSR
  SendIntrnl VarChar(1) Send Internally default=N [Y=Yes, N=No]
  SendEMail VarChar(1) Send E-Mail default=N [Y=Yes, N=No]
  SendSMS VarChar(1) Send SMS default=N [Y=Yes, N=No]
  SendFax VarChar(1) Send Fax default=N [Y=Yes, N=No]

# ANCM - NCM Code
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  CODE U: NcmCode, GroupCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  NcmCode nVarChar(15) NCM Code
  Descrip nVarChar(254) Description
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  GroupCode VarChar(1) Group Code default=0
  Group Int(6) NCM Group ->ONCG

# ANN1 - Documents Numbering - Series - History
Module: Administration | 39 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Series, logInstanc
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  Series Int(11) Series default=0
  SeriesName nVarChar(8) Series Name
  InitialNum Int(11) Initial Number default=0
  NextNumber Int(11) Next Number for Use default=0
  LastNum Int(11) Last Number Allowed
  BeginStr nVarChar(20) Prefix String
  EndStr nVarChar(20) Suffix String
  Remark nVarChar(50) Remarks
  GroupCode Int(6) Group default=1 [1=Series Group 1, 2=Series Group 2, 3=Series Group 3, 4=Series Group 4, 5=Series Group 5, 6=Series Group 6, 7=Series Group 7, 8=Series Group 8, 9=Series Group 9, 10=Series Group 10, 11=Series Group 11, 12=Series Group 12, 13=Series Group 13, 14=Series Group 14, 15=Series Group 15, 16=Series Group 16, 17=Series Group 17, 18=Series Group 18, 19=Series Group 19, 20=Series Group 20, 21=Series Group 21, 22=Series Group 22, 23=Series Group 23, 24=Series Group 24, 25=Series Group 25, 26=Series Group 26, 27=Series Group 27, 28=Series Group 28, 29=Series Group 29, 30=Series Group 30]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  YearTransf VarChar(1) Year-End Closing default=N [Y=Yes, N=No]
  Indicator nVarChar(10) Period Indicator default=' ' ->OPID
  Template nVarChar(20) Template
  NumSize Int(11) Numeric Size
  FolioPref nVarChar(4) Folio Prefix String
  NextFolio Int(11) Next Folio Number
  DocSubType nVarChar(2) Document Sub-Type default=--
  DefESeries Int(6) Default Electronic Series default=0
  IsDigSerie VarChar(1) Is Digital Series default=N [Y=Yes, N=No]
  SeriesType VarChar(1) Series Type default=D [D=Document, B=Business Partner, I=Item, R=Resource, W=Withholding Certificates]
  IsManual VarChar(1) Is Manual Series default=N [Y=Yes, N=No]
  BPLId Int(11) Assigned Branch ->OBPL
  IsForCncl VarChar(1) Is Series for Cancellation default=N [Y=Yes, N=No]
  AtDocType nVarChar(2) AT Document Type [GT=GT, GA=GA, GD=GD, GR=GR, GC=GC, FT=FT, FS=FS, NC=NC, ND=ND, FR=FR]
  IsElAuth VarChar(1) Electronic Authorization Code default=N [Y=Yes, N=No]
  CoAccount VarChar(1) Cost Account Only default=N [Y=Yes, N=No]
  GenPassprt VarChar(1) Do Generate SAP Passport default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  logInstanc Int(11) Log Instance - History
  PInvType Int(11) Abs Type of Positive Value Invoice ->OEIT
  NInvType Int(11) Abs Type of Negative Value Invoice ->OEIT
  AssignedID nVarChar(70) Assigned ID
  Action VarChar(1) Action [R=Report, C=Cancel, F=Finalize]
  Status VarChar(1) Status [R=Reported, C=Canceled, F=Finalized]
  Phase VarChar(1) Phase [T=To Be Processed, I=In Process, O=OK, E=Error]

# ANN3 - Documents Numbering -Belgium Series - History
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, Series, logInstanc
  SERIES: Series, logInstanc
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  Series Int(11) Series default=0
  DocSubType nVarChar(2) VAT Code for Tax Invoice Report default=--
  logInstanc Int(11) Log Instance - History

# ANNM - Document Numbering - History
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, logInstanc
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  AutoKey Int(11) Automatic Key default=0
  DfltSeries Int(11) Default Series default=0
  UpdCounter Int(11) Update Counter default=0
  UserSign Int(6) User Signature ->OUSR
  DocSubType nVarChar(2) Document Sub-Type default=-- [--=, IE=Invoice Exempt, DN=Debit Memo, IB=Bill, EB=Exempt Bill, RI=Reserve Invoice, IR=Invoice & Receipt, DM=A/P Debit Memo, IX=Export Invoice, RP=A/P Reserve Invoice, OV=Outgoing VAT - Withholding Tax, OG=Outgoing Gross Income - Withholding Tax, ON=Outgoing Income - Withholding Tax, OS=Outgoing Social Security - Withholding Tax, OI=Outgoing Industry Specific - Withholding Tax, OD=Outgoing District Specific - Withholding Tax, IC=Incoming WTax Certificate, GA=GST Tax Invoice, GD=GST Debit Memo, RV=Refund Voucher]
  DocAlias nVarChar(20) Alternative Document Name
  PeriodTyp VarChar(1) Seq. Period Type of Supply Code
  logInstanc Int(11) Log Instance - History

# AOB1 - Sent Messages - User History
Module: Administration | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AlertCode, ObjType, ObjCode
  SEND_EM: SendEMail
  CONFIRMED2: Confirmed2
Fields (name type(len) description [values] ->parent table):
  AlertCode Int(11) Alert Code ->OALR
  ObjType nVarChar(20) Object default=12 [-1=Random, 12=User, 11=Contact Person]
  ObjCode nVarChar(50) Object Code
  ObjName nVarChar(155) Name
  SendIntrnl VarChar(1) Sent Internally default=N [Y=Yes, N=No]
  Confirmed1 VarChar(1) Confirmation 1 default=N [Y=Yes, N=No]
  ConfDate1 Date(8) Approval Time 1
  ConfTime1 Int(6) Approval Time 1
  SendEMail VarChar(1) Sent E-mail default=N [Y=Yes, N=No]
  E_Mail nVarChar(100) E-Mail
  Confirmed2 VarChar(1) Confirmation 2 default=N [Y=Yes, N=No, E=Error]
  ConfDate2 Date(8) Authorization Period 2
  ConfTime2 Int(6) Authorization Period 2
  SendSMS VarChar(1) Sent SMS default=N [Y=Yes, N=No]
  PortNum nVarChar(50) Mobile Phone Number
  Confirmed3 VarChar(1) Confirmation 3 default=N [Y=Yes, N=No, E=Error]
  ConfDate3 Date(8) Approval Time 3
  ConfTime3 Int(6) Approval Time 3
  SendFax VarChar(1) Sent Fax default=N [Y=Yes, N=No]
  Fax nVarChar(50) Fax Number
  Confirmed4 VarChar(1) Confirmation 4 default=N [Y=Yes, N=No, E=Error]
  ConfDate4 Date(8) Confirmation Date 4
  ConfTime4 Int(6) Confirmation Time 4

# APFS - Personal Fields Setup - History
Module: Administration | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  SECONDARY U: TableName, FieldName, Category, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TableName nVarChar(20) Data Subtype
  FieldName nVarChar(50) Field Name
  RefObjType nVarChar(20) Data Type
  Category VarChar(1) Category default=N [N=, R=Sales A/R, P=Purchase A/P, Q=Purchase Request, A=Inventory Transfers and Requests Sales A/R, B=Inventory Transfers and Requests Purchase A/P, C=Opportunity - Business Partner, D=Opportunity - Business Partner Channel, E=Customer Equipment Card - Business Partner, F=Customer Equipment Card - Direct Partner, L=Landed Cost - Vendor, G=Landed Cost - Broker, X=Payment Results - Business Partner, U=Payment Results - User, H=Incoming Payments, I=Outgoing Payments, J=Sales A/R, K=Purchase A/P, M=Bill of Exchange for Incoming Payments]
  OrigType VarChar(1) Default Data Classification default=U [U=User Defined, S=Sensitive Personal, P=Personal, N=Not Personal]
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  LogInstanc Int(11) Log Instance default=0
  Type VarChar(1) Data Classification default=N [N=Not Personal, S=Sensitive Personal, P=Personal]
  Descr nVarChar(254) Description
  MaxType VarChar(1) Max. Data Classification default=U [U=User Defined, S=Sensitive Personal, P=Personal]

# APJ1 - Project Plan Steps
Module: Administration | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, StepCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  StepCode Int(11) Step Code
  Father Int(11) Father Step Code
  VisOrder Int(11) Visual Order
  Level Int(11) Node Level
  StepName nVarChar(254) Step Name
  StepInfo nVarChar(254) Step Info
  StepNotes nVarChar(254) Step Notes
  StepLink nVarChar(32) Step Link to Menu ID
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  IsComplete VarChar(1) Is Complete
  LogInstanc Int(11) Log Instance
  Owner nVarChar(254) Owner ->OUSR
  Status Int(11) Status default=0
  Duration Num(19,6) Duration
  PlanTime Num(19,6) Planned Time
  AtcEntry Int(11) Attachment Entry ->OATC
  TotalPTime Num(19,6) Total Planned Time
  QueryID Int(11) Step Link Query ID ->OUQR

# APJ2 - Project Plan Steps Time Record
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, StepCode, LineNum, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  StepCode Int(11) Step Code
  LineNum Int(11) Line Number
  Date Date(8) Date
  StartTime Int(11) Start Time
  EndTime Int(11) End Time
  Remarks nVarChar(254) Remarks
  LogInstanc Int(11) Log Instance
  Owner nVarChar(254) Owner ->OHEM
  Duration Num(19,6) Duration

# APJT - Project Plan
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  TempType VarChar(1) Template Type default=N [S=System Template, N=Nonsystem Template]
  TempName nVarChar(254) Template Name
  LogInstanc Int(11) Log Instance
  UserSign Int(11) User Signature ->OUSR
  UserSign2 Int(11) Updating User ->OUSR
  CreateDate Date(8) Production Date
  UpdateDate Date(8) Date of Update
  TempDesc nVarChar(254) Template Description

# ARI1 - Add-On
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USER_CODE, AddOnID
Fields (name type(len) description [values] ->parent table):
  USER_CODE nVarChar(25) User Code ->OUSR
  AddOnID Int(11) Add-On ID
  AddOnType VarChar(1) Add-On Type [M=Manual, C=Critical, A=Automatic, D=Disabled]
  EnableFlag VarChar(1) Add-On Enable Flag default=Y [Y=Yes, N=No]

# ARST - Route Stages - History
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  SECONDARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(50) Code
  Desc nVarChar(100) Description
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Generation Time
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0

# AST1 - Sales Tax Codes - Rows
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: STCCode, Line_ID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  STCCode nVarChar(8) STC Code ->OSTC
  Line_ID Int(11) Row Number default=0
  STACode nVarChar(8) STA Code ->OSTA
  STAType Int(11) STA Type ->OSTA
  TaxOnTCode nVarChar(8) STA Tax on Tax Code ->OSTA
  TaxOnTType Int(11) STA Tax On Tax Type ->OSTA
  EfctivRate Num(19,6) Effective Rate
  FmlId Int(11) Tax Formula ID ->OFML
  CstCodeIn nVarChar(20) CST Code Incoming
  CstSuffix nVarChar(2) CST Suffix for ICMS
  LogInstanc Int(11) Log Instance default=0

# ASTC - Sales Tax Codes
Module: Administration | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(100) Name
  Rate Num(19,6) Rate
  Freight VarChar(1) Freight default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ValidForAR VarChar(1) Valid for A/R default=Y [Y=Yes, N=No]
  ValidForAP VarChar(1) Valid for A/P default=Y [Y=Yes, N=No]
  TfcId Int(11) Formula Combination ID ->OTFC
  Lock VarChar(1) Inactive default=N [Y=Yes, N=No]
  TaxIcms nVarChar(2) Taxation For ICMS
  IsItmLevel VarChar(1) Single Item Level Tax default=N [Y=Yes, N=No]
  CfopIn nVarChar(6) CFOP Incoming Code ->OCFP
  CfopOut nVarChar(6) CFOP Outgoing Code ->OCFP
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  FADebit VarChar(1) FA Debit default=N [Y=Yes, N=No]
  IsSystem VarChar(1) Is System Tax Code default=N [Y=Yes, N=No]
  VatExempt VarChar(1) Apply VAT Exemption default=N [Y=Yes, N=No]
  HashInpNm nVarChar(100) Hash Input Name
  CheckDate Date(8) Check Date

# ASTT - Sales Tax Authorities Type
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, LogInstanc
  NAME U: Name, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  Name nVarChar(40) Type Name
  UserSign Int(6) User Signature ->OUSR
  IsVat VarChar(1) VAT default=N [Y=Yes, N=No]
  NfTaxId Int(11) ID of Nota Fiscal Tax Category ->ONFT
  TpsId Int(11) ID of Tax Parameter Set ->OTPS
  PLABalance Num(19,6) PLA Current Balance
  Locked VarChar(1) Locked default=N
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CreditCtrl VarChar(1) Tax Credit Control default=N [Y=Yes, N=No]

# ASUC - Single User Setup - History
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: StpCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  StpCode Int(6) Setup Code
  StpDes nVarChar(100) Setup Description
  Action VarChar(1) Action default=B [B=Block Update, W=Warning]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

# ASVM - Systems for Value Mapping
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SysType VarChar(1) System Type default=C [C=Concur]
  SysDsc nVarChar(50) System Description

# ATC1 - Attachments - Rows
Module: Administration | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, Line
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry
  Line Int(11) Row Number
  srcPath Text(16) Source Path
  trgtPath Text(16) Target Path
  FileName nVarChar(254) File Name
  FileExt nVarChar(8) File Extension
  Date Date(8) Attachment Date
  UsrID Int(11) User ID
  Copied VarChar(1) Copied default=N [Y=Yes, N=No]
  Override VarChar(1) Override file default=N [Y=Yes, N=No]
  subPath nVarChar(254) Subpath
  FreeText nVarChar(100) Free Text
  CopyToTrgt VarChar(1) Copy to Target Document default=N [Y=Yes, N=No]
  CopyToProd VarChar(1) Copy to Production Order default=N [Y=Yes, N=No]

# ATCX - Tax Code Determination - History
Module: Administration | 42 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID
  LineNum Int(11) Row Number
  DocType Int(11) Document Type [0=Item, 1=Service, 2=Item & Service]
  BusArea Int(11) Business Area [0=Sales, 1=Purchase, 2=Sales & Purchase]
  Cond1 Int(11) Condition 1 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UDFTable1 nVarChar(20) UDF Table Name
  NumVal1 Int(11) Numeric Value
  StrVal1 nVarChar(100) String Value
  MnyVal1 Num(19,6) Monetary Value
  Cond2 Int(11) Condition 2 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UDFTable2 nVarChar(20) UDF Table Name
  NumVal2 Int(11) Numeric Value
  StrVal2 nVarChar(100) String Value
  MnyVal2 Num(19,6) Monetary Value
  Cond3 Int(11) Condition 3 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UdfTable3 nVarChar(20) UDF Table Name
  NumVal3 Int(11) Numeric Value
  StrVal3 nVarChar(100) String Value
  MnyVal3 Num(19,6) Monetary Value
  Cond4 Int(11) Condition 4 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UdfTable4 nVarChar(20) UDF Table Name
  NumVal4 Int(11) Numeric Value
  StrVal4 nVarChar(100) String Value
  MnyVal4 Num(19,6) Monetary Value
  Cond5 Int(11) Condition 5 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UdfTable5 nVarChar(20) UDF Table Name
  NumVal5 Int(11) Numeric Value
  StrVal5 nVarChar(100) String Value
  MnyVal5 Num(19,6) Monetary Value
  Descr nVarChar(250) Description
  LnTaxCode nVarChar(8) Line Tax Code
  FrLnTax nVarChar(8) Line Freight Tax
  FrHdrTax nVarChar(8) Header Freight Tax
  UDFAlias1 nVarChar(18) UDF Field Alias
  UDFAlias2 nVarChar(18) UDF Field Alias
  UDFAlias3 nVarChar(18) UDF Field Alias
  UDFAlias4 nVarChar(18) UDF Field Alias
  UDFAlias5 nVarChar(18) UDF Field Alias
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Update Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Update User ->OUSR

# ATSC - CST Code for Nota Fiscal
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID, LogInstanc
  CST_CODE U: CODE, Category, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ID Int(11) CST Internal Key
  CODE nVarChar(20) CST Code Incoming
  Situation Text(16) Description Incoming
  Locked VarChar(1) Locked default=N [Y=, N=]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Category Int(6) Tax Category default=-6 ->ONFT
  CodeOut nVarChar(20) CST Code Outgoing
  OutDesc Text(16) Description Outgoing
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# AUGR - Authorization Group - History
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupId, logInstanc
  NAME_KEY U: GroupName, logInstanc
Fields (name type(len) description [values] ->parent table):
  GroupId Int(6) Authorization Group ID
  GroupName nVarChar(155) Group Name
  GroupDec nVarChar(155) Group Description
  Allowences Text(16) Allowances
  TPLId Int(6) Template ID ->UICU
  StartDate Date(8) Start Date
  DueDate Date(8) Due Date
  GroupType VarChar(1) Group Type default=A [A=Authorization, F=Form Settings, T=Alerts, U=UI Configuration Templates, L=All]
  CockpitId Int(6) Cockpit Template ID
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User - History
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History
  updateDate Date(8) Date of Update - History
  VersionNum nVarChar(13) Version Number

# AUSR - Users - History
Module: Administration | 117 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USERID, logInstanc
Fields (name type(len) description [values] ->parent table):
  USERID Int(6) User Signature
  PASSWORD nVarChar(254) User Password default=0
  PASSWORD1 nVarChar(8) User Password
  PASSWORD2 nVarChar(8) User Password
  INTERNAL_K Int(6) Internal Number
  USER_CODE nVarChar(25) User Code
  U_NAME nVarChar(155) User Name
  GROUPS Int(6) Authorization Group default=0
  PASSWORD4 nVarChar(254) Password
  ALLOWENCES Text(16) User Confirmation
  SUPERUSER VarChar(1) Superuser default=N [Y=Yes, N=No]
  DISCOUNT Num(19,6) Max. Discount
  PASSWORD3 nVarChar(8) User Password
  Info1File nVarChar(4) Info1File
  Info1Field Int(6) Info1Field
  Info2File nVarChar(4) Info2File
  Info2Field Int(6) Info2Field
  Info3File nVarChar(4) Info3File
  Info3Field Int(6) Info3Field
  Info4File nVarChar(4) Info4File
  Info4Field Int(6) Info4Field
  dType VarChar(1) dType default=S [Y=Yes, N=No, X=, H=SHA1, S=SHA256]
  E_Mail nVarChar(100) E-Mail
  PortNum nVarChar(50) Mobile Phone Number
  OutOfOffic VarChar(1) Out of the Office default=N [Y=Yes, N=No]
  SendEMail VarChar(1) Send E-Mail default=N [Y=Yes, N=No]
  SendSMS VarChar(1) Send SMS default=N [Y=Yes, N=No]
  DfltsGroup nVarChar(8) Default ->OUDG
  CashLimit VarChar(1) Cash Amount Limit default=N [Y=Yes, N=No]
  MaxCashSum Num(19,6) Max. Cash Total
  Fax nVarChar(50) Fax Number
  SendFax VarChar(1) Send Fax default=N [Y=Yes, N=No]
  Locked VarChar(1) User Confirmation default=N [Y=Yes, N=No]
  Department Int(6) Department default=-2 ->OUDP
  Branch Int(6) Branch default=-2 ->OUBR
  UserPrefs Text(16) User Preferences
  Language Int(11) Language
  Charset Int(6) Font Language
  OpenCdt VarChar(1) Open Window for Credit Vouchers Ref. Update default=N [Y=Yes, N=No]
  CdtPrvDays Int(11) Vouchers from Last Days default=1
  DsplyRates VarChar(1) Display Rates Table on Startup default=N [Y=Yes, N=No]
  AuImpRates VarChar(1) Import Currency Exchange Rates Automatically default=N [Y=Yes, N=No]
  OpenDps VarChar(1) Open Postdated Checks Window default=N [Y=Yes, N=No]
  RcrFlag VarChar(1) Display Scheduled Recurring Postings default=N [Y=Yes, N=No]
  CheckFiles VarChar(1) Perform Data Check default=N [Y=Yes, N=No]
  OpenCredit VarChar(1) Open Window for Postdated Credit Vouchers default=N [Y=Always, N=No, D=By Date]
  CreditDay1 Int(6) Handle Postdated Credit Day 1 default=1
  CreditDay2 Int(6) Handle Postdated Credit Day 2 default=15
  WallPaper Text(16) Wallpaper
  WllPprDsp Int(6) Wallpaper Display default=1 [1=Centralized, 2=Full Screen, 3=Tile]
  AdvImagePr VarChar(1) Extended Image Processing default=N [N=Yes, O=No, Y=Full]
  ContactLog VarChar(1) Today's Activity Alert default=N [Y=Yes, N=No]
  LastWarned Date(8) Last Warned Date
  AlertPolFr Int(6) Message Check Frequency (Min.) default=5
  ScreenLock Int(6) Screen Lock Delay default=30
  ShowNewMsg VarChar(1) Display Message/Alert on Arrival default=Y [Y=Yes, N=No]
  Picture nVarChar(200) Picture
  Position nVarChar(90) Position
  Address nVarChar(254) Address
  Country nVarChar(3) Country/Region ->OCRY
  Tel1 nVarChar(50) Telephone 1
  Tel2 nVarChar(50) Telephone 2
  GENDER VarChar(1) Gender default=F [F=Female, M=Male]
  Birthday Date(8) Date of Birth
  EnbMenuFlt VarChar(1) Enable Forbidden Menu Items default=N [N=No, Y=Yes]
  objType nVarChar(20) Object Type default=12
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date
  userSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Update Date
  OneLogPwd VarChar(1) At first logon change password default=N [N=Do not change password at first login, Y=At first logon change password]
  lastLogin Date(8) Last Logon Date
  LastPwds Text(16) Last Passwords 1
  LastPwds2 nVarChar(254) Last Passwords 2 default=0
  LastPwdSet Date(8) Last Password Change
  FailedLog Int(11) Failed Login Count default=0
  PwdNeverEx VarChar(1) Password Never Expires default=N [Y=Yes, N=No]
  SalesDisc Num(19,6) Max. Sales Discount
  PurchDisc Num(19,6) Max. Purchase Discount
  LstLogoutD Date(8) Last Logoff Date
  LstLoginT Int(11) Last Logon Time
  LstLogoutT Int(11) Last Logoff Time
  LstPwdChT Int(11) Last Password Change Time
  LstPwdChB nVarChar(8) Last Password Changed By
  RclFlag VarChar(1) Display Recurring Transactions [Y=Yes, N=No]
  MobileUser VarChar(1) Mobile User default=N [Y=Yes, N=No]
  MobileIMEI nVarChar(64) Mobile IMEI
  PrsWkCntEb VarChar(1) Personal Work Center Enable default=N [Y=Yes, N=No]
  SnapShotId Int(11) Snapshot ID default=0
  STData nVarChar(40) User Password Salt
  SupportUsr VarChar(1) Support User default=N [N=No, Y=Yes]
  NoSTPwdNum Int(6) Password encrypted w/o Salt (cryptography) default=0
  DomainUser nVarChar(50) Domain user name bound in SLD
  CUSAgree VarChar(1) CUS Agreement [Y=Yes, N=No]
  EmailSig Text(16) E-Mail Signature
  TPLId Int(6) Template ID ->UICU
  DigCrtPath Text(16) Digital Certificate Path
  ShowNewTsk VarChar(1) Open Worklist on Task Arrival default=Y [N=No, Y=Yes]
  IntgrtEb VarChar(1) Enable Setting Integration default=N [Y=Yes, N=No]
  AllBrnchF VarChar(1) Allow Viewing of All (Including Unassigned To) Branches in Financial Reports default=Y [Y=Yes, N=No]
  EvtNotify VarChar(1) Allow Event Notification default=Y
  IgnDtOwn VarChar(1) Ignore Data Ownership for this user default=N [Y=Yes, N=No]
  EnterAsTab VarChar(1) Use Numeric Keypad Enter Key as Tab Key default=N [Y=Yes, N=No]
  DotAsSep VarChar(1) Use Del Key As Separator default=N [Y=Yes, N=No]
  MouseOnly VarChar(1) Document Operation by Mouse Only default=N [Y=Yes, N=No]
  Color Int(6) Company Color [0=Combined, 1=Classic, 2=Gray, 3=Violet, 4=Blue, 5=Green, 6=Yellow, 7=Orange, 8=Red, 9=Brown]
  SkinType nVarChar(254) Skin Type
  Font nVarChar(50) Font
  FontSize Int(11) Font Size
  NaturalPer VarChar(1) Natural Person default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  AutoAsnBPL VarChar(1) Auto. Assign Branches default=N [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV
  HandleEDoc VarChar(1) Can Process Electronic Documents default=Y [Y=Yes, N=No]
  ShowLicBal VarChar(1) Show License Balloon default=Y [Y=Yes, N=No]
  LicBaHDate Date(8) License Balloon Hiding Date

# AVM1 - Systems for Value Mapping Properties
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, PropID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PropID Int(11) Property ID
  PropDesc nVarChar(50) Property Description
  PropType VarChar(1) Property Type default=S [S=String, N=Numeric, D=Date]
  PropValue nVarChar(254) Property Value

# AVM2 - Systems for Value Mapping Properties
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ObjectId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectId Int(11) Object ID
  UDTName nVarChar(50) Name of user defined table

# AWEX - Workflow Engine Execution Entity
Module: Administration | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id, logInst
Fields (name type(len) description [values] ->parent table):
  Id Int(11) ID
  IsActive Int(6) Is Active
  IsConCurr Int(6) Is Concurrent
  IsScope Int(6) Is Scope
  ProcInstId nVarChar(100) Process Instance ID
  BizKey nVarChar(250) Business Key
  ParentId Int(11) Parent ID
  ProcDefId Int(11) Process Definition ID
  ActId nVarChar(250) Activity ID
  DataContex Text(16) Data Context
  B1WFInstId Int(11) Workflow Instance ID
  logInst Int(11) Log Instance
  LastUpdate nVarChar(50) Last Update Date

# AWFQ - SWFQ History Table
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SequenceID, LogInst
Fields (name type(len) description [values] ->parent table):
  SequenceID Int(11) Sequence ID
  SourceDB nVarChar(100) Source Database
  Timestamp nVarChar(20) Time Stamp
  ObjectType nVarChar(30) Object Type
  TransType VarChar(1) Transaction Type [A=Add, U=Update, C=Cancel, D=Delete]
  FieldsInKe Int(11) Number of Fields in Key
  FieldNames nVarChar(254) Key Field Names
  FieldValue nVarChar(254) Key Field Values
  UserID nVarChar(25) UserID
  TaskID nVarChar(64) Task ID
  TrigEvntID nVarChar(64) Trigger Event ID
  TrigParams Text(16) Trigger Parameters
  LogInst Int(11) Log Instance
  IsSuccess VarChar(1) Is Message Handled Successfully
  ResultMemo nVarChar(250) Memo of the Result

# AWL1 - Potential Processor of Tasks
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(6) Line ID
  Candidate nVarChar(254) Candidate
  LogIns Int(11) Log Instance
  WasRead VarChar(1) Was Read default=N [Y=Yes, N=No]
  CandExpr nVarChar(254) Candidate Expression

# AWL2 - Input data for tasks
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(11) Line ID
  ObjectType nVarChar(20) Object Type
  ObjKey nVarChar(100) Object Key
  Command VarChar(1) Command default=B [B=Based On, M=Field Mapping]
  LogIns Int(11) Log Instance
  ObjSubType nVarChar(64) Object Subtype
  ObjDetail Text(16) Object Detail

# AWL3 - Task Notes
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(11) Line ID
  Note Text(16) Note
  Creator nVarChar(25) Creator
  NoteDate Date(8) Note Date
  Access VarChar(1) Accessibility default=W [W=Workflow, T=Task]
  LogIns Int(11) Log Instance

# AWL4 - Task Output Data
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID nVarChar(64) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID nVarChar(6) Line ID
  ObjectType nVarChar(20) Object Type
  ObjKey nVarChar(100) Object Key
  LogIns Int(11) Log Instance
  OutParamID nVarChar(64) Object ID in WF Engine
  ObjSubType nVarChar(64) Object Subtype

# AWL5 - Task Field Mapping Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID nVarChar(64) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID nVarChar(6) Line ID
  InputID Int(11) Input ID
  SrcFld nVarChar(50) Source Field
  TgtFld nVarChar(50) Target Field
  LogIns Int(11) Log Instance

# AWLS - Workflow - Task Details
Module: Administration | 34 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LogIns
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID ->OWFI
  TaskID Int(11) Task ID
  WFID nVarChar(64) Workflow ID
  WFName nVarChar(100) Workflow Name
  TaskDesc nVarChar(100) Task Description
  ObjType nVarChar(20) Object Type
  Operation VarChar(1) Operation [A=Add, U=Update, D=Delete]
  ObjKey nVarChar(100) Object Key
  EnterDate Date(8) Enter Date
  EnterTime Int(6) Enter Time
  TaskType VarChar(1) Task Type
  DueDate Date(8) Due Date
  DueTime Int(6) Due Time
  UpdateDate Date(8) Update Date - History
  UpdateTime Int(6) Update Time - History
  Owner nVarChar(25) Owner
  Priority Int(6) Priority default=2 [1=High, 2=Medium, 3=Low]
  UserSign Int(6) User Signature
  Status VarChar(1) Status default=W [S=Setup, W=To Be Picked, P=Picking, G=In Progress, D=Completing, F=Completed, N=Suspended, C=Cancelling, Q=Canceled, O=Forwarding, E=Error]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History
  Deleted VarChar(1) Deleted - History
  DuraDays Int(11) Duration Days
  DuraHours Int(6) Duration Hours
  TaskName nVarChar(100) Task Name
  isPicked VarChar(1) Is Picked default=N
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  WorkListId Int(11) Worklist ID
  ObjSubType nVarChar(64) Object Subtype
  ForwardTo nVarChar(25) User to Forward
  WasRead VarChar(1) Line Read default=N
  TrigParams Text(16) Trigger Parameters
  Key nVarChar(254) Task ID in XML

# AWMG - Workflow Manager
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID, LogIns
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Workflow ID
  TemplateID Int(11) Template ID
  TmplateKey nVarChar(254) Template Key
  Name nVarChar(254) Name
  Version nVarChar(13) Version
  MAXIns Int(11) Maximum Number of Instances
  Status VarChar(1) Status default=I [I=Inactive, A=Active, E=Activation failed, M=Importing, P=Imported, F=Import failed, D=Deleted]
  XMLFile Text(16) XML File
  Desc Text(16) Description
  LogIns Int(11) Log Instance - History
  StartType VarChar(1) Start Type default=M [M=Manual Start, T=Timer Start, C=Conditional Start]

# AWTS - Workflow Engine Task Table
Module: Administration | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id, LogInst
Fields (name type(len) description [values] ->parent table):
  Id Int(11) ID
  Owner nVarChar(254) Owner
  OutputPar Text(16) Output Parameter
  EndTime nVarChar(50) End Time
  StartTime nVarChar(50) Start Time
  ProcDefId Int(11) Process Definition ID
  Name nVarChar(254) Name
  ExeId Int(11) Execution ID
  ProcInsId Int(11) Process Instance ID
  Desc nVarChar(254) Description
  InputPar Text(16) Input Parameter
  DelReason nVarChar(254) Delete Reason
  Assignee nVarChar(254) Assignee
  LogInst Int(11) Log Instance
  LastUpdate nVarChar(50) Last Update Date
  Key nVarChar(254) Task ID in XML
  B1Task Int(11) B1 Task ID

# BPL1 - Branch I.E. Numbers
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, DstState
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) BPL ID ->OBPL
  DstState nVarChar(3) Destination State ->OCST
  IENumber nVarChar(32) I.E. Number
  LogInstanc Int(11) Log Instance default=0

# BPL2 - Branch Tributary Info.
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: BPLId, TributID
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) BPL ID ->OBPL
  TributID Int(11) Tributary Info. ID
  TributType Int(11) Tributary Type default=-1 ->OBNI
  TTStartDat Date(8) Tributary Type Start Date
  TTEndDate Date(8) Tributary Type End Date
  TribRegCod Int(11) Tributary Regime Code default=-1 ->OBNI
  TRCStartD Date(8) Tributary Reg. Code Start Date
  TRCEndDate Date(8) Tributary Regime Code End Date
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=247 ->ADP1

# CDPM - Dynamic Permission
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PermId
  OBJECT: ObjectType, Name
Fields (name type(len) description [values] ->parent table):
  PermId Int(11) Permission ID
  Name nVarChar(100) Name
  ObjectType Int(11) Object Type
  ObjectKey nVarChar(200) Object ID
  Father Int(11) Parent
  PermOption Int(6) Permission Option default=0 [0=Full/Read/None, 1=Full/None, 2=Full/None/Saved Queries]
  System VarChar(1) System Flag default=N [Y=Yes, N=No]
  Hidden VarChar(1) Hidden default=N [Y=Yes, N=No]
  SortOrder Int(11) Sort Order

# CDRO - Drag & Relate - Output Fields
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId, FieldId, UserSign
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(4) Object ID
  FieldId Int(6) Field ID
  DescStr nVarChar(30) Description
  VisOrder Int(6) Visual Order default=0
  UserSign Int(6) User Form default=-1 ->OUSR

# CDRU - Drag & Relate User Settings
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserID, ObjectId, PartOf
Fields (name type(len) description [values] ->parent table):
  UserID Int(11) User ID default=-1
  ObjectId nVarChar(4) ObjectId
  PartOf VarChar(1) PartOf default=C [C=Category, R=Report, F=Table]
  Disabled VarChar(1) Disabled default=N [Y=Yes, N=No]

# CFTC - New Chart of Accounts Fields to Check
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TabName, ColName
Fields (name type(len) description [values] ->parent table):
  TabName nVarChar(100) Table Name
  ColName nVarChar(50) Column Name
  IntLevel nVarChar(2) Integrity Level

# CGEV - Event Log
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EventID
Fields (name type(len) description [values] ->parent table):
  EventID Identity(11) Event ID
  EventDate Date(8) Date of Event
  EventTime Int(11) Timestamp of Event
  UserCode nVarChar(25) Current User ID
  SourceIP nVarChar(64) Network Address of SAP Business One Client
  EventType nVarChar(32) Event Type
  EventDetls Text(16) Event Description

# CHEN - Caching Update Notification
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Component, ID
Fields (name type(len) description [values] ->parent table):
  Component VarChar(1) Component
  ID Int(11) ID
  Counter Int(11) Counter

# CHFL - Choose from List Format
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjName, FldIndex
Fields (name type(len) description [values] ->parent table):
  ObjName nVarChar(20) Object Name
  FldIndex Int(6) Field Index
  FldNum nVarChar(60) Field No.
  DispName nVarChar(30) Displayed Name
  GroupBy VarChar(1) Group By default=N [Y=Yes, N=No]
  Visible VarChar(1) Visible default=N [Y=Yes, N=No]
  DispDesc VarChar(1) Show Type default=Y [Y=Yes, N=No]
  SortOrder VarChar(1) Sort Order default=A [A=Ascending, D=Descending]
  VisIndex Int(6) Visual Index default=0

# CIF1 - Country Specific Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FldAbsEnt, Country, TransCRY
Fields (name type(len) description [values] ->parent table):
  FldAbsEnt Int(11) Field ID ->OCIF
  Country nVarChar(3) Country/Region Code ->OCRY
  TransCRY nVarChar(3) Transaction Country/Region default=XX
  IsMandImp VarChar(1) Field is mandatory for import [Y=Yes, N=No]
  IsMandExp VarChar(1) Field is mandatory for export [Y=Yes, N=No]
  IsReqAllIm VarChar(1) Field is required for import default=N [Y=Yes, N=No]
  IsReqAllEx VarChar(1) Field is required for export default=N [Y=Yes, N=No]

# CINF - Company Info
Module: Administration | 220 columns | ObjType: 124
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Version
Fields (name type(len) description [values] ->parent table):
  Version Int(11) Version
  CompnyName nVarChar(100) Company Name
  Flags nVarChar(50) Flags default=NNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
  InfoL1 Int(11) InfoL1
  InfoL2 Int(11) InfoL2
  InfoA1 nVarChar(128) InfoA1
  InfoA2 nVarChar(50) InfoA2
  ACTStamp Int(11) ACT Stamp default=0
  ADMStamp Int(11) ADM Stamp default=0
  RTTStamp Int(11) RTT Stamp default=0
  CINFStamp Int(11) CINF Stamp default=0
  LawsSet nVarChar(3) Laws Set
  EnblVatGrp VarChar(1) Tax System [O=One Tax, L=Tax per Row, C=Tax per BP]
  EnblVTGPmn VarChar(1) Use Tax Groups in Payments [Y=Yes, N=No]
  VatOOS_O nVarChar(8) Tax Definition
  VatOOS_I nVarChar(8) Tax Exempt Revenue Account
  VatStnd_O nVarChar(8) Tax Standard O
  VatStnd_I nVarChar(8) Tax Standard I
  VatExmpt_O nVarChar(8) Tax Exempt O
  VatExmpt_I nVarChar(8) Tax Exempt I
  VatHalf_O nVarChar(8) Tax Definition
  VatHalf_I nVarChar(8) Tax Definition
  VatZrRt_O nVarChar(8) Tax Zero Rate O
  VatZrRt_I nVarChar(8) Tax Zero Rate I
  MaxActGrps Int(11) Max. No. of Account Groups
  EnblDctSrc VarChar(1) Enable Deduction at Source [Y=Yes, N=No]
  EnblRCN VarChar(1) Enable Retail Chain Stores [Y=Yes, N=No]
  EnblCorINV VarChar(1) Enable Correction Invoice [Y=Yes, N=No]
  EnblCshRep VarChar(1) Enable Cash Report [Y=Yes, N=No]
  EnblIRTRep VarChar(1) Enable Interest Report [Y=Yes, N=No]
  EnblTrnRep VarChar(1) Enable Turnover Report [Y=Yes, N=No]
  EnblVPMRep VarChar(1) Enable Payments Report [Y=Yes, N=No]
  EnblACTRep VarChar(1) Enable Adv. Corp. Tax Report [Y=Yes, N=No]
  EnblFTZ VarChar(1) Enable Free Trade Zone [Y=Yes, N=No]
  EnblSlfPCH VarChar(1) Enable Self A/P Invoice [Y=Yes, N=No]
  EnblPCHUpd VarChar(1) Enable Purchase Trans. Update [Y=Yes, N=No]
  EnblRsvINV VarChar(1) Enable Reserve Invoice [Y=Yes, N=No]
  EnblRTDnld VarChar(1) Enable Rates Download [Y=Yes, N=No]
  RTTDnldAdr nVarChar(254) Rates Download Web Address
  ZPrcCode nVarChar(8) Zero Center Code
  EnblExpns VarChar(1) Enable Freight Management [Y=Yes, N=No]
  EnblRtrRep VarChar(1) Enable Returns Report [Y=Yes, N=No]
  IsEC VarChar(1) European Countries [Y=Yes, N=No]
  EnblCshDsc VarChar(1) Enable Cash Discount [Y=Yes, N=No, V=No Tax Adjustment]
  EnblLostCD VarChar(1) Enable Lost Cash Discount [Y=Yes, N=No]
  NumActLvls Int(11) No. of Account Group Levels
  EnblRealRD VarChar(1) Enable Realized Rate Diff. [Y=Yes, N=No]
  EnblVTGNoD VarChar(1) Enable Tax on Down Payment default=Y [Y=Yes, N=No]
  EnblGLManP VarChar(1) Enable Manual Postings in Control Account [N=No, Y=Yes]
  EnblOptVIP VarChar(1) Enable Optional Tax in Payments [Y=Yes, N=No]
  EnblActCrC VarChar(1) Enable Account Currency Change [Y=Yes, N=No]
  EnblFrnAct VarChar(1) Enable Foreign Item Account [Y=Yes, N=No]
  EnblECAct VarChar(1) Enable EU Item Account [Y=Yes, N=No]
  EnblECRpt VarChar(1) Enable 349 Report [Y=Yes, N=No]
  EnblRound VarChar(1) Enable Rounding [Y=Yes, N=No]
  EnblPrVatS VarChar(1) Enable Print Tax Amount [Y=Yes, N=No]
  EnblYrTrns VarChar(1) Enable Year Transfer [Y=Year Transfer, N=No, A=Data Archive]
  EnblActTtl VarChar(1) Enable Account Title [Y=Yes, N=No]
  EnblDocWrn VarChar(1) Enable No Base Doc. Alert [Y=Yes, N=No]
  ActSegNum Int(6) No. of Segments default=0
  EnbSgmnAct VarChar(1) Enable Account Segmentation [Y=Yes, N=No]
  SizeOfSeg0 Int(6) Size of Segment 0 default=0
  SizeOfSeg1 Int(6) Size of Segment 1 default=0
  SizeOfSeg2 Int(6) Size of Segment 2 default=0
  SizeOfSeg3 Int(6) Size of Segment 3 default=0
  SizeOfSeg4 Int(6) Size of Segment 4 default=0
  SizeOfSeg5 Int(6) Size of Segment 5 default=0
  SizeOfSeg6 Int(6) Size of Segment 6 default=0
  SizeOfSeg7 Int(6) Size of Segment 7 default=0
  SizeOfSeg8 Int(6) Size of Segment 8 default=0
  SizeOfSeg9 Int(6) Size of Segment 9 default=0
  Rprt1099 VarChar(1) 1099 Report [Y=Yes, N=No]
  MultiAddss VarChar(1) Multi Address [Y=Yes, N=No]
  EnbDunning VarChar(1) Enable Dunning default=Y [Y=Yes, N=No]
  EnbQtyEDln VarChar(1) Allow Qty in Delivery Note to Exceed Base Doc. Qty [Y=Yes, N=No]
  Itw1Date Date(8) Next Alert Date
  Itw1Time Int(11) Next Alert Time
  Itw1Count Int(11) ITW1 Counter
  EnbPayRef VarChar(1) Calculate Payment Ref. No. [Y=Payment Reference No., N=No, I=ISR Reference]
  EnblDfrTax VarChar(1) Enable Deferred Tax [Y=Yes, N=No]
  EnblClsPr VarChar(1) Enable Period-End Closing [Y=Yes, N=No]
  EnblTaxEL VarChar(1) Enable Tax Exemption Letter [Y=Yes, N=No]
  EnableBOE VarChar(1) Enable Bill of Exchange default=N [Y=Yes, N=No]
  EnableWHT VarChar(1) Enable WTax default=N [Y=Yes, N=No]
  EnblEquVat VarChar(1) Enable Equalization Tax [Y=Yes, N=No]
  EnblFAsset VarChar(1) Enable Fixed Assets [Y=Yes, N=No]
  EnblDoubt VarChar(1) Enable Doubtful Debts [Y=Yes, N=No]
  RateBase VarChar(1) Base Date for Exchange Rate default=P [P=Posting Date, T=Document Date]
  BOEStatClo VarChar(1) Allow Closed Status for Bill of Exchange [Y=Yes, N=No]
  ARDocsInWT VarChar(1) Enable WTax in A/R Docs [N=No, Y=Yes]
  BISBnkCnt nVarChar(3) BISR Bank Country/Region
  BISRBnkCd nVarChar(30) BISR Bank No.
  BISRBnkAc nVarChar(50) BISR Bank Account
  BISRBranch nVarChar(50) BISR Branch
  EnblBPConn VarChar(1) Enable BP Cards Connection [Y=Yes, N=No]
  EnblVATDat VarChar(1) Enable VAT Date [Y=Yes, N=No]
  EnblStAgRp VarChar(1) Enable Stock Aging Report [Y=Yes, N=No]
  EnblCARepo VarChar(1) Enable Control Account Repost [Y=Yes, N=No]
  EnblMatRev VarChar(1) Enable Inventory Revaluation [Y=Yes, N=No]
  EnblMBPRec VarChar(1) Enable Multiple BPs Reconcil. [Y=Yes, N=No]
  CshDscGros VarChar(1) Cash Discount Flag For CN, HK default=N
  EnblTaxInv VarChar(1) Enable Tax Invoices [Y=Yes, N=No]
  EnblCorAct VarChar(1) Enable Correspondence of Accts [N=No, Y=Yes]
  EnblRuDIP VarChar(1) Enable RU Delivery & Invoice default=Y [N=No, Y=Yes]
  EnblCurDec VarChar(1) Enable Decimal Places [N=No, Y=Yes]
  EnblPayMtd VarChar(1) Enable Payment Method on Inv. [N=No, Y=Yes]
  EnblBaseUn VarChar(1) Enable UoM on Invoice [N=No, Y=Yes]
  EnblVATAna VarChar(1) Enable VAT Analytics Report [N=No, Y=Yes]
  EnblExREnh VarChar(1) Enable Frgn. Curr. Valuation [Y=Yes, N=No]
  VATGrpCal VarChar(1) Enable VAT Calculation by Grp [Y=Yes, N=No]
  MaxChoose Int(11) No. of Choose from List Rows default=0
  EnblInfla VarChar(1) Enable Inflation [Y=Yes, N=No]
  EnblLAWHT VarChar(1) Enable Latin America WHT [Y=Yes, N=No]
  EnblRTWHT VarChar(1) Enable Rounding Type WHT [Y=Yes, N=No]
  ChkQunty VarChar(1) Enable Check Quantity In RDR default=N [Y=Yes, N=No]
  SriMngSys VarChar(1) SRI Management System default=R [A=On Every Transaction, R=On Release Only]
  BtchMngSys VarChar(1) Batch Management System default=R [A=On Every Transaction, R=On Release Only]
  SriCreatIn VarChar(1) Auto SRI creation on receipt default=N [N=No, Y=Yes]
  EnblFolio nVarChar(2) Enable Folio Numbers [N=No, CL=Chile, MX=Mexico]
  EnblDocSbT nVarChar(2) Enable Document Sub-type [N=No, CL=Chile, MX=Mexico, IN=India]
  IepsPayer VarChar(1) IEPS Payer default=N [Y=Yes, N=No]
  DaysOrdCnc Int(11) Default Days for Ord. Canc. default=30
  EnblLATaxS VarChar(1) Enable Latin America Tax Sys [Y=Yes, N=No]
  PercOfAcq Num(19,6) Percent of Total Acquisition
  MinBaseDoc Num(19,6) Minimum Base Amount per Doc
  EnblDpmJdt VarChar(1) Create JE rows in Down Pmnt [Y=Yes, N=No]
  EnblDownP VarChar(1) Down Payment [Y=Yes, N=No]
  EnblNDdctC VarChar(1) Enable Non Deduct VAT Per Card [Y=Yes, N=No]
  DocNmMtd VarChar(1) Enable Sharing Series [Y=YES, N=No.]
  DoFilter VarChar(1) Data Ownership Indication default=N [Y=YES, N=No]
  EnblOnPDCh VarChar(1) Enable Opened Postdated Checks [Y=Yes, N=No]
  EnblOnWnCr VarChar(1) Open Window for Credit Voucher [Y=Yes, N=No]
  EnblDefInx VarChar(1) Enable Define Indexes [Y=Yes, N=No]
  EnblMxComm VarChar(1) Enable Max Commitment [Y=Yes, N=No]
  EnblIndxOp VarChar(1) Enable Index Option [Y=Yes, N=No]
  EnblSbtCVo VarChar(1) Enable Submit Credit Voucher [Y=Yes, N=No]
  MinAmntOAP Num(19,6) Minimum Amount for Appndix O&P
  CredSumm VarChar(1) Credit Card Summary [Y=Yes, N=No]
  PostdChk VarChar(1) Postdated Check [Y=Yes, N=No]
  PostdCred VarChar(1) Postdated Credit Voucher [Y=Yes, N=No]
  CredVend VarChar(1) Credit Vendors [Y=Yes, N=No]
  WkoStatus VarChar(1) Old Work Order Status [Y=Yes, N=No]
  DispTrByDf VarChar(1) Display Transactions by Dflt default=Y [Y=Yes, N=No]
  stampTax nVarChar(8) Default Stamp Tax ->OVTG
  MinAmntAL Num(19,6) Minimum Amount for Annual List
  BlockZeroQ VarChar(1) Block Stock Negative Quantity default=Y [Y=Yes, N=No]
  AutoCrIns VarChar(1) Auto Create Customer Eq Card default=N [Y=Yes, N=No]
  EnbRepomo VarChar(1) Enable Inflation for Cash Act [Y=Yes, N=No]
  RFCValidat VarChar(1) Enable RFC Validations [Y=Yes, N=No]
  MxDcsInPmt Int(11) Max. Number of Documents in Payment default=0
  RelStkNoPr VarChar(1) Enable Stock Release without Item Cost default=N [Y=Yes, N=No]
  CashDisc VarChar(1) Cash Discount In Document [Y=Yes, N=No]
  EnableSMS VarChar(1) Enable SMS [Y=Yes, N=No]
  EnblIndic VarChar(1) Enable Indicator [Y=Yes, N=No]
  EnbFedTax VarChar(1) Enable Federal Tax ID [Y=Yes, N=No]
  EnblCounty VarChar(1) Enable County [Y=Yes, N=No]
  Language Int(11) Language on Create Company
  ChkIntgUpd VarChar(1) Check Data Integrity On Update default=Y [Y=Yes, N=No]
  ChkIntgCre VarChar(1) Check Data Integrity On Create default=Y [Y=Yes, N=No]
  BisBnkAcKy Int(11) BISR Bank Account Key ->DSC1
  EnbZeroDec VarChar(1) Enable Print Check Show Zero Decimal default=N [Y=Yes, N=No]
  EnbDecWord VarChar(1) Show Check Decimal in Words default=Y [Y=Yes, N=No]
  ChkWrdOnly VarChar(1) Add the word Only in checks [Y=Yes, N=No]
  EnBnkStmnt VarChar(1) Bank Statement Processing default=N [Y=Yes, N=No]
  CalcVatGrp VarChar(1) Group Lines in VAT Calculation [Y=Yes, N=No]
  TaxSysType VarChar(1) Defines Tax Calculation System [A=Preconfigured Formula with Jurisdiction Support, B=User-Defined Formula, C=Preconfigured Formula, M=Fixed implementation with jurisdiction support, S=Fixed implementation]
  ESEnabled VarChar(1) Is Event Sender enabled? default=N [Y=Yes, N=No, C=Customize]
  RateTotal VarChar(1) Use rate for minor total calc. default=N [N=No, Y=Yes]
  CompanyHis Text(16) Create/Upgrade History
  EnblAssVal VarChar(1) Enable Assessable Value default=N [Y=Yes, N=No]
  CompanySta VarChar(1) Company Status default=U [V=Valid, I=Invalid, U=Upgrading, A=Archived, S=Inventory Valuation Utility, P=Upgrade Simulation]
  eFRTActLvs Int(11) No. of Levels in Elect. FRT
  TaxGrpType VarChar(1) Defines Tax Grouping Type default=C [C=Code, J=Jurisdiction]
  InstallNo nVarChar(30) Installation Number
  IsOldPA VarChar(1) Is Old for PA default=N [N=No, Y=Yes]
  EnbNegDoc VarChar(1) Enable Negative Total in Doc
  Algo Int(6) Encryption Algorithm
  ArcComp VarChar(1) Archived Company default=N [Y=Yes, N=No]
  UpdatedTF VarChar(1) Is Updated Tax Formula default=N [N=No, Y=Yes]
  DARDBGUID nVarChar(32) Readonly DB GUID for Archiving
  NegStoLv VarChar(1) Negative Stock: Check Level default=I [C=Company, W=Warehouse, I=Item Setting]
  SPNEnabled VarChar(1) Enable Transact. Notification default=Y [Y=Yes, N=No]
  PrsWkCntEb VarChar(1) Personal Work Center Enabled default=N [N=No Cockpit, Y=Normal Style Cockpit, F=Fiori Style Cockpit]
  DashbdEb VarChar(1) Dashboard Enabled default=N [Y=Yes, N=No]
  BoxEffDate Date(8) Box Effective From Date
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User ->OUSR
  SnapShotId Int(11) Snapshot ID default=0
  CreatedBy VarChar(1) Created By default=N [N=, P=Solution Packager, W=Express Configuration Wizard]
  B1SgtEb VarChar(1) B1 Suggest: Enable default=Y [Y=Yes, N=No]
  IsHConEnv VarChar(1) Is in High Concurrency Env default=N [Y=Yes, N=No]
  B1BuzzEb VarChar(1) Enable Streamwork Widget default=N
  IMCEEnable VarChar(1) IMCE Enable default=N [Y=Yes, N=No]
  DKeyId nVarChar(128) Current Dynamic Key ID
  ResetDData VarChar(1) Reset Dyn. Key Data to Default default=N
  ConvDifAct VarChar(1) Enable Conversion Diff. Acct default=Y [Y=Yes, N=No]
  BasEffDate Date(8) Base Effective From Date
  oldFxAss VarChar(1) Has Used Old Fixed Assets default=N [Y=Yes, N=No]
  MaxRowsCFL Int(11) Max. Rows for Choose from List default=0 [0=Unlimited, 5000=5000, 10000=10000, 50000=50000, 100000=100000]
  ColSel Text(16) Column Selection
  EnblSPEDUF VarChar(1) Enable SPED Related UDFs default=N [Y=Yes, N=No]
  DpmAffTot VarChar(1) Down Payment Affects Total default=Y [Y=Yes, N=No]
  AliasUpd nVarChar(254) Installation Date
  TrailDays Int(6) Trial Days
  TestComp VarChar(1) Test Comp. default=N [Y=Yes, N=No]
  DashConf Text(16) Enable Side Bar
  SideEnable VarChar(1) Enable Side Bar default=N [Y=Yes, N=No]
  IsPALInit VarChar(1) Is PAL Init. or Not default=N
  PANAVer Int(11) Pervasive Version default=0
  ExpEnable VarChar(1) Enable Expense Claim default=Y [Y=Yes, N=No]
  LastSsrDat Date(8) Last SSR upload date
  LastSsrHsh nVarChar(33) Last SSR upload date hash
  B1iTimeOut Int(11) B1i Request Timeout default=30
  CpRfshEnbl VarChar(1) Enable Cockpit Auto Refresh default=N
  CpRfshIntv Int(11) Cockpit Refresh Interval default=300
  EnbMBFilt VarChar(1) Enable Filtering Mechanism by Branch default=N [Y=Yes, N=No]
  CompnyGUID nVarChar(40) Company GUID
  ShutTime Int(11) SAP Business One Shutdown Time
  Migrated VarChar(1) Migrated DB default=N [Y=Yes, N=No]

# CPL1 - Quick Copy - Instance Log
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Number ->OCPL
  LogId Int(11) Log ID
  ObjectID nVarChar(20) Object ID
  Instance nVarChar(254) Instance Key
  ErrCode nVarChar(20) Error Code
  MessageId nVarChar(20) Message ID
  MessageDes nVarChar(254) Message Description
  InstName nVarChar(254) Instance Name

# CPRF - Column Preferences
Module: Administration | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, FormID, ItemID, ColID, TPLId
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  ItemID nVarChar(50) Item Number
  ColID nVarChar(60) Column
  Width Int(11) Width
  VisInForm VarChar(1) Visible in Form default=N [Y=Yes, N=No]
  VisualIndx Int(11) Tabs Layout
  EditInForm VarChar(1) Editable in Form default=N [Y=Yes, N=No]
  VisInExpnd VarChar(1) Visible in Expanded default=N [Y=Yes, N=No]
  ExpandIndx Int(11) Expanded Index
  EditInEXP VarChar(1) Editable in Expanded default=N [Y=Yes, N=No]
  Folded VarChar(1) Folder default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ExtDisable VarChar(1) Externally Disabled default=N [N=No, Y=Yes]
  ExtInvsbl VarChar(1) Externally Invisible default=N [N=No, Y=Yes]
  TPLId Int(6) Template ID default=0 ->UICU
  TableName nVarChar(20) Table Name
  ItemUID nVarChar(32) ItemUID

# CRY1 - Country Combination Settings
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Country, TransCRY
Fields (name type(len) description [values] ->parent table):
  Country nVarChar(3) Country/Region Code ->OCRY
  TransCRY nVarChar(3) Transaction Country/Region ->OCRY
  EnableIST VarChar(1) Enable Intrastat Transactions [Y=Yes, N=No]

# CSHS - User-Defined Values
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IndexID
  DETAILS U: FormID, ItemID, ColID
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(100) Form ID
  ItemID nVarChar(52) Field
  ColID nVarChar(128) Column ID default=-1
  ActionT Int(6) Action default=0 [0=, 1=Valid Values, 2=Query]
  QueryId Int(11) Query ID ->OUQR
  IndexID Int(11) Index
  Refresh VarChar(1) Refresh default=N [Y=Yes, N=No]
  FieldID nVarChar(60) Field
  FrceRfrsh VarChar(1) Force Refresh default=N [Y=Yes, N=No]
  ByField VarChar(1) By Field default=N [Y=When Field Changes, N=When Exiting Altered Column, C=When Column Value Changes]

# CSN1 - Certificate Series - Series
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, Series
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number ->OCSN
  Series Int(6) Series
  BeginStr nVarChar(20) Prefix
  InitialNum Int(11) First No. default=1
  NextNum Int(11) Next No. default=1
  LastNum Int(11) Last No.

# CSPI - Solution Packager Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) absEntry
  Name nVarChar(50) Parameter Name
  Type nVarChar(20) Parameter Type
  Value Text(16) Parameter Value
  LstUpdDate Date(8) Last Update Date
  LstUpdTime Int(11) Last Update Time
  CheckSum nVarChar(50) Row Checksum

# CSTN - Workstation ID
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  COMPUTER U: Computer
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Computer nVarChar(30) Station ID

# CTBR - Toolbars
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, ToolbarId
Fields (name type(len) description [values] ->parent table):
  UserSign Int(6) ->OUSR
  ToolbarId Int(11)
  Docking Int(6)
  LeftID Int(6)
  TopID Int(6)
  RightID Int(6)
  BottomID Int(6)
  VisibleID VarChar(1) default=N [Y=, N=]

# CUDC - User Display Cat.
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CodeID
  FORM: NameID
Fields (name type(len) description [values] ->parent table):
  CodeID Int(11) Code
  NameID nVarChar(20) Name
  FormID Int(11) Form ID
  UserSign Int(6) User Signature ->OUSR

# CUFD - User Fields - Description
Module: Administration | 21 columns | ObjType: 152
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableID, FieldID
  ALIAS U: TableID, AliasID
Fields (name type(len) description [values] ->parent table):
  TableID nVarChar(21) Table
  FieldID Int(6) Field
  AliasID nVarChar(50) Title
  Descr nVarChar(80) Description
  TypeID VarChar(1) Type
  EditType VarChar(1) Edit Type
  SizeID Int(6) Size
  EditSize Int(6) Edit Size
  Dflt nVarChar(254) Default
  NotNull VarChar(1) Required Entry Field default=N [Y=Yes, N=No]
  IndexID VarChar(1) Create Index default=N [Y=Yes, N=No]
  RTable nVarChar(21) Linked Table ->OUTB
  RField Int(6) Linked Field
  Action VarChar(1) Action
  Sys VarChar(1) System Defined? default=N [Y=Yes, N=No]
  DfltDate Date(8) Default Date
  RelUDO nVarChar(20) Related UDO
  ValidRule nVarChar(254) Validation Rule
  RelSO nVarChar(20) Related System Object
  RThrdPTab nVarChar(100) Related to Third Party Table
  RThrdPFld nVarChar(100) Related to Third Party Field

# CULG - Company Upgrade Log
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogId
Fields (name type(len) description [values] ->parent table):
  LogId Int(11) LogId
  VersFrom Int(11) Version from
  VersTo Int(11) Version to
  TableId nVarChar(4) Table ID
  OnCreate VarChar(1) Err. on creation default=C [C=Create, Q=Query]
  ErrLevel nVarChar(30) Error Level
  InQuery nVarChar(254) -
  ErrMessage nVarChar(254) -
  UpgStart nVarChar(30) Start upgrade
  UserID Int(11) User Signature

# CUMF - Folder
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FolderId, UserSign
Fields (name type(len) description [values] ->parent table):
  FolderId Int(11) Folder Key default=0
  FolderName nVarChar(50) Folder Name
  SortNum Int(11) Sort Number
  UserSign Int(6) User Signature ->OUSR
  FatherId Int(11) Parent Key default=-1

# CUMI - My Menu Items
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserSign, Id_
  DETAIL: UserSign, Name_, Levels, FatherId, SortNum
Fields (name type(len) description [values] ->parent table):
  Id_ Int(11) Folder Key default=0
  Name_ nVarChar(100) Menu Item Name
  UserSign Int(6) User Signature ->OUSR
  FatherId Int(11) Parent Key default=-1
  SortNum Int(11) Sort Number
  Type_ VarChar(1) Menu Item Type default=- [F=Form, Q=Query, R=Report, L=Link, -=Folder]
  ObjType nVarChar(20) Object Type ->ADP1
  Key_ nVarChar(50) Internal ID
  FormMenuId Int(11) Form Menu ID
  FormNum Int(11) Form No.
  RepPath Text(16) Report Path
  Levels Int(6) Item Level default=1

# CUPC - Upgrade Control
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectId
Fields (name type(len) description [values] ->parent table):
  ObjectId nVarChar(20) Object ID
  CntBefore Int(11) Before
  CntAfter Int(11) After
  Reported VarChar(1) Reported default=O [C=Reported, O=Open]

# CUVV - User Validations
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IndexID, LineNum
Fields (name type(len) description [values] ->parent table):
  IndexID Int(11) Index ->CSHS
  Value nVarChar(254) Field Value
  LineNum Int(11) Row Number

# DADB - Data Archive DSA Balance
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Document Internal ID
  ItemCode nVarChar(50) Item Number ->OITM
  LocCode Int(11) Location Code ->OLCT
  OpenBal Num(19,6) Opening Balance

# DAR1 - Data Archive - Transaction Log
Module: Administration | 25 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ArcEntry, Line_ID
  ABS_TYPE: DocAbs, DocType
Fields (name type(len) description [values] ->parent table):
  ArcEntry Int(11) Data Archive Entry
  Line_ID Int(11) Row Number
  DocType nVarChar(20) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Internal ID
  Total Num(19,6) Total
  RefDate Date(8) Posting Date
  ClusterId Int(11) Cluster ID
  Remarks nVarChar(100) Remarks
  KeySeg1 nVarChar(15) Key Segment 1
  KeySeg2 nVarChar(15) Key Segment 2
  KeySeg3 nVarChar(15) Key Segment 3
  KeySeg4 nVarChar(15) Key Segment 4
  KeySeg5 nVarChar(15) Key Segment 5
  KeySeg6 nVarChar(15) Key Segment 6
  KeySeg7 nVarChar(20) Key Segment 7
  KeySeg8 nVarChar(15) Key Segment 8
  KeySeg9 nVarChar(15) Key Segment 9
  KeySeg10 nVarChar(15) Key Segment 10
  Series Int(11) Series
  DocSubType nVarChar(2) Document Sub-Type default=--
  PIndicator nVarChar(10) Period Indicator default=' '
  Instance Int(6) Instance default=0
  Segment Int(6) Segment default=0
  CardCode nVarChar(15) Card Code ->OCRD

# DAR2 - Data Archive - Transaction Log
Module: Administration | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ArcEntry, Line_ID
Fields (name type(len) description [values] ->parent table):
  ArcEntry Int(11) Data Archive Entry
  Line_ID Int(11) Row Number default=0
  Approve VarChar(1) Approve default=Y [Y=Yes, N=No]
  DocType Int(11) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Abs Entry
  CardCode nVarChar(15) Customer/Vendor Code
  RefDate Date(8) Posting Date
  DueDate Date(8) Due Date
  TaxDate Date(8) Document Date
  Total Num(19,6) Total
  Action VarChar(1) Action default=T [R=Remove, L=Locked, T=Temporary]
  Remarks nVarChar(50) Remarks
  KeySeg1 nVarChar(15) Key Segment 1
  KeySeg2 nVarChar(15) Key Segment 2
  KeySeg3 nVarChar(15) Key Segment 3
  KeySeg4 nVarChar(15) Key Segment 4
  KeySeg5 nVarChar(15) Key Segment 5
  KeySeg6 nVarChar(15) Key Segment 6
  ClusterId Int(11) Cluster ID

# DAR3 - Data Archive - Handwritten Documents
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ArcEntry, Line_ID
  DOC_NUM: DocType, DocSubType, DocNum, PIndicator
Fields (name type(len) description [values] ->parent table):
  ArcEntry Int(11) Data Archive Entry
  Line_ID Int(11) Row Number
  DocType nVarChar(20) Document Type
  DocAbs Int(11) Doc. No.
  DocNum Int(11) Document Number
  DocSubType nVarChar(2) Document Sub-Type default=--
  PIndicator nVarChar(10) Period Indicator default=' '

# DAR4 - Data Archive - Candidate
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ArcEntry, Line_ID
  ABS_TYPE: DocAbs, DocType
Fields (name type(len) description [values] ->parent table):
  ArcEntry Int(11) Data Archive Entry
  Series Int(11) Series
  Line_ID Int(11) Row Number
  DocType nVarChar(20) Document Type
  DocNum Int(11) Document Number
  DocAbs Int(11) Document Internal ID
  Total Num(19,6) Total
  RefDate Date(8) Posting Date
  Type VarChar(1) Type default=R [R=Recommendation, M=Marked]
  Remarks nVarChar(100) Remarks

# DATB - Data Archive Tax Balance
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  LocCode Int(11) Location Code ->OLCT
  NfTaxId Int(11) ID of Nota Fiscal Tax Category ->ONFT
  TaxComId Int(11) Tax Component ID ->OSTT
  MatType Int(11) Material Type
  ArchBal Num(19,6) Data Archived Balance
  TaxAcct nVarChar(15) Tax Account ->OACT
  IsPLA VarChar(1) PLA Field
  IsTaxCred VarChar(1) Tax Credit Field

# DBADM - Read-Only DB User
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ROUser
Fields (name type(len) description [values] ->parent table):
  ROUser nVarChar(254) Read-Only User
  ROPass nVarChar(254) Read-Only Password

# DGP1 - Customer List
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CardCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  CardCode nVarChar(15) Customer Code ->OCRD
  CardName nVarChar(100) Customer Name
  Checked VarChar(1) Checked default=Y [Y=Yes, N=No]
  CtrlAcct nVarChar(15) Control Account

# DGP2 - Expanded Selection Criteria
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CondNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  CondNum Int(11) Condition Number
  SelFldID nVarChar(100) Selection Field ID
  FromString nVarChar(200) String Value From
  FromNumber Int(11) Number Value From
  FromMoney Num(19,6) Amount Value From
  FromDate Date(8) Date Value From
  ToString nVarChar(200) String Value To
  ToNumber Int(11) Number Value To
  ToMoney Num(19,6) Amount Value To
  ToDate Date(8) Date Value To

# DGP3 - Expanded Consolidation Options
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CondNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  CondNum Int(11) Condition Number
  ConFldID nVarChar(100) Consolidation Field ID
  Checked VarChar(1) Checked default=N [Y=Yes, N=No]

# DGP4 - Business Place List
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  LineNum Int(11) Line Number
  BPLId Int(11) Business Place ID ->OBPL
  BPLName nVarChar(100) Business Place Name
  Checked VarChar(1) Checked default=Y [Y=, N=]

# DGP5 - Sort By List
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, CondNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ODGP
  CondNum Int(11) Condition Number
  SortField nVarChar(100) Sort Field default=DocNum [-1=, DocNum=Document Number, DocDate=Posting Date, DocDueDate=Due Date, NumAtCard=BP Reference No., DocTotal=Document Amount, SlpCode=Sales Employee]
  SortOrder VarChar(1) Sort Order default=A [A=Ascending, D=Descending]

# DMW1 - Query List
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PacCode, QueryCode
Fields (name type(len) description [values] ->parent table):
  PacCode Int(11) Package Code ->ODMW
  QueryCode Int(11) Query Code ->OUQR
  UserSign Int(6) User Signature ->OUSR

# EOY1 - End of Year UDOs
Module: Administration | 1 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UdoCode
Fields (name type(len) description [values] ->parent table):
  UdoCode nVarChar(20) UDO Code

# ERX1 - Excise Registering Number-Rows
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ErnId, NumTypeId
Fields (name type(len) description [values] ->parent table):
  ErnId Int(11) Excise Register Numbering ID ->OERX
  NumTypeId Int(11) Numbering Type ID
  NumTypeNam nVarChar(30) Numbering Type Name
  FirstNum Int(11) First Number
  NextNum Int(11) Next Number
  LastNum Int(11) Last Number
  ResetDate Date(8) Date of last reset

# FML1 - Tax Formula Parameter Declaration
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FmlId, DispOrder
Fields (name type(len) description [values] ->parent table):
  FmlId Int(11) Formula ID ->OFML
  DispOrder Int(11) Display Order
  VarName nVarChar(64) Variable Name
  Category VarChar(1) Category default=1 [1=Input, 2=Output, 3=In Out]
  Parameter Text(16) Parameter
  DataType VarChar(1) Data Type default=S [T=Tax Amounts, S=Amounts, P=Prices, Q=Quantities, %=Percents, I=Integer, A=String, B=Boolean, M=Measures, W=WTax]
  LogInstanc Int(11) Log Instance default=0

# FTT1 - Financial Template Import - Files
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OFTT
  LineNum Int(11) Row Number
  FileName nVarChar(254) Data Definition File Name
  ReleaDate Date(8) Release Date
  Descript nVarChar(100) Description
  Localizat nVarChar(3) Localization
  ChartAcct nVarChar(128) Chart of Accounts
  DocType VarChar(1) Template Type default=B [B=Balance Sheet, P=Profit and Loss, C=Trial Balance, F=Statement of Cash Flows, S=Sales Unit, T=Form 6111, A=Cost Accounting, E=Asset Devalue Provision, R=Shareholder's Rights and Interests Changing, D=Profit Distribution, V=VAT Payable Detail, L=e-Balance Sheet, O=e-Profit and Loss, H=Asset History Sheet, G=Others, I=Taxable Profit and Loss, J=Appropriation of Net Profit, K=E-Asset History Sheet]
  DimCode Int(11) Dimension Code ->ODIM

# GFL1 - Grid Filter Rules
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormID, GridID, UserCode, FilterID, GridColumn
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  GridID nVarChar(11) Grid ID
  UserCode Int(6) User Code
  FilterID Int(11) Filter ID
  GridColumn Int(6) Grid Column
  FilterRule Int(6) FilterRule
  Value nVarChar(254) Value
  ValueTo nVarChar(254) ValueTo

# GFL2 - Grid Filter Name
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormID, GridID, UserCode, FilterID
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  GridID nVarChar(11) Grid ID
  UserCode Int(6) User Code
  FilterID Int(11) Filter ID default=-1
  Name nVarChar(100) Name

# GPC1 - Authority Assignment
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId, BPLId, State
  CARD_CODE U: CardCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number ->OGPC
  BPLId Int(11) Branch ->OBPL
  State nVarChar(3) State ->OCST
  CardCode nVarChar(15) Vendor Code ->OCRD

# MAB1 - Menu Abbreviation
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: absEntry, MenuID
Fields (name type(len) description [values] ->parent table):
  absEntry Int(11) Internal Key
  MenuID Int(11) Menu ID
  Alias nVarChar(20) Menu Alias

# MABV - Menu Abbreviation
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: absEntry
  PKG_NAME U: pkgName
Fields (name type(len) description [values] ->parent table):
  absEntry Int(11) Internal Key
  pkgName nVarChar(200) Package Name
  fileName nVarChar(200) FileName
  imprtDate Date(8) Import Date
  pkgPath nVarChar(200) Package Path

# MAP1 - Input and Output of Mapping
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MapID, Code
Fields (name type(len) description [values] ->parent table):
  MapID Int(11) Mapping ID ->OMAP
  Code Int(11) Code
  Type nVarChar(10) Type default=NA [CRYSTAL=Crystal Report, XML=XML File, NA=Not Avalible, TXT=Text File, CSV=CSV File]
  RuleType nVarChar(10) Rule Type default=NA [XSLT=XSLT Rule, NA=Not Avalible, REGEX=Reguler expression]
  RuleRef nVarChar(50) Rule Reference ID
  RefID nVarChar(50) Reference ID
  RuleVer nVarChar(5) Rule Version
  IsFinal VarChar(1) Is Final Result default=N [Y=Yes, N=No]

# MAP2 - Mapping Input and Output Relation
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MapID, CodeIn, CodeOut
Fields (name type(len) description [values] ->parent table):
  MapID Int(11) Mapping ID ->OMAP
  CodeIn Int(11) Input Code
  CodeOut Int(11) Output Code
  Sequence Int(11) Run Sequence
  Name nVarChar(20) Parameter Name

# MDC1 - Master Data Cleanup - Log
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OMDC
  LineID Int(11) Line ID
  ObjectType nVarChar(20) Object Type
  ObjectKey nVarChar(20) Object Key
  Name nVarChar(200) Name
  LastDate Date(8) Last Transaction Date
  Action VarChar(1) Action [R=Remove, D=Deactivate]
  ObjectCode nVarChar(100) Object Code
  ActFailed VarChar(1) Action Failed default=N [Y=Yes, N=No]
  OrigAction VarChar(1) Original Action [R=Remove, D=Deactivate]
  SubObjType nVarChar(20) Subobject Type
  SubObjKey nVarChar(50) Subobject Key
  SubObjNam1 nVarChar(50) Subobject Name 1
  SubObjNam2 nVarChar(50) Subobject Name 2
  SubObjNam3 nVarChar(50) Subobject Name 3

# MDC2 - Master Data Cleanup - MD Log
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ObjectType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key ->OMDC
  ObjectType nVarChar(20) Object Type
  UserAction VarChar(1) User Action [O=Original Recommendation, D=Deactivate]
  DelContent nVarChar(100) Delete Content List

# MLS1 - Distribution Lists - Recipients
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code ->OMLS
  LineNum Int(11) Addressee Number
  ObjType nVarChar(20) Object
  ObjCode nVarChar(50) Object Code
  ObjName nVarChar(155) Name
  E_Mail nVarChar(100) E-Mail
  PortNum nVarChar(50) Mobile Phone Number
  Fax nVarChar(50) Fax Number

# MLT1 - Translations in user language
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TranEntry, LangCode
Fields (name type(len) description [values] ->parent table):
  TranEntry Int(11) Key From Header Table
  LangCode Int(11) Language Code of User Language
  Trans Text(16) Translation Content

# MPO1 - Value Mapping Data
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  LineId Int(11) Line Id
  ThirdPID Int(11) Third party internal number
  ThirdPVal nVarChar(100) Third Party Value

# MVLD - 
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: fatherId, lineNum
  GUID U: guid
Fields (name type(len) description [values] ->parent table):
  guid nVarChar(36) Guid
  fatherId nVarChar(36) Father Id
  lineNum Int(11) Line Number
  value nVarChar(254) Value
  note nVarChar(254) Note
  noteSid Int(11) Note String Id

# NFN1 - Not a Fiscal Sequence
Module: Administration | 23 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, SeqCode
  S_NAME U: ObjectCode, DocSubType, BPLId, SeqName
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONFN
  SeqCode Int(6) Seq. Code default=0
  SeqName nVarChar(8) Seq. Name
  InitialNum Int(11) Initial Number default=0
  NextNum Int(11) Next Number for Use default=0
  LastNum Int(11) Last Number Allowed
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  Remark nVarChar(50) Remarks
  GroupCode Int(6) Group default=1 [1=, 2=, 3=, 4=, 5=, 6=, 7=, 8=, 9=, 10=]
  Locked VarChar(1) Locked default=N [Y=, N=]
  YearTransf VarChar(1) Year-End Closing default=N [Y=, N=]
  Indicator nVarChar(10) Period Indicator default=' ' [' '=] ->OPID
  Template nVarChar(20) Template
  NumSize Int(11) Numeric Size
  Prefix nVarChar(8) Prefix
  Suffix nVarChar(8) Suffix
  DocSubType nVarChar(2) Document Sub-Type default=--
  Model nVarChar(6) Nota Fiscal Model default=0 ->ONFM
  Location Int(11) Location Code ->OLCT
  BPLId Int(11) Assigned Branch default=0 ->OBPL
  IsDigital VarChar(1) Digital Series default=N [Y=Yes, N=No]
  EnvTypeNFe Int(11) Environment Type NF-e default=-1 ->OBNI

# NFN2 - NFSeq User Default
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, UserSign, SeqCode
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONFN
  UserSign Int(6) User Signature ->OUSR
  SeqCode Int(6) Sequence Code
  DocSubType nVarChar(2) Document Sub-Type default=--

# NFN3 - Assigned Nota Fiscal Series
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, SeqCode
  SEQ: SeqCode
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONFN
  SeqCode Int(6) Sequence Code default=0
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=--

# NFN4 - Manual Nota Fiscal Number
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, Serial, SeriesStr, SubStr, Model, SeqCode, CardCode
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONFN
  SeqCode Int(6) Sequence Code
  SeqName nVarChar(8) Seq Name
  Serial Int(11) Serial Number
  SeriesStr nVarChar(3) Series String
  SubStr nVarChar(3) Subseries String
  DocSubType nVarChar(2) Document Sub-Type default=--
  Model nVarChar(6) Nota Fiscal Model ->ONFM
  CardCode nVarChar(15) Customer/Vendor Code default=- ->OCRD
  DocEntry Int(11) Document Abs. Entry
  DocNumber Int(11) Document Number
  IsReusable VarChar(1) Is Reusable default=N [Y=Yes, N=No]

# NNM1 - Documents Numbering - Series
Module: Administration | 39 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Series
  SER_NAME U: ObjectCode, DocSubType, SeriesName, SeriesType
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  Series Int(11) Series default=0
  SeriesName nVarChar(8) Series Name
  InitialNum Int(11) Initial Number default=0
  NextNumber Int(11) Next Number for Use default=0
  LastNum Int(11) Last Number Allowed
  BeginStr nVarChar(20) Prefix String
  EndStr nVarChar(20) Suffix String
  Remark nVarChar(50) Remarks
  GroupCode Int(6) Group default=1 [1=Series Group 1, 2=Series Group 2, 3=Series Group 3, 4=Series Group 4, 5=Series Group 5, 6=Series Group 6, 7=Series Group 7, 8=Series Group 8, 9=Series Group 9, 10=Series Group 10, 11=Series Group 11, 12=Series Group 12, 13=Series Group 13, 14=Series Group 14, 15=Series Group 15, 16=Series Group 16, 17=Series Group 17, 18=Series Group 18, 19=Series Group 19, 20=Series Group 20, 21=Series Group 21, 22=Series Group 22, 23=Series Group 23, 24=Series Group 24, 25=Series Group 25, 26=Series Group 26, 27=Series Group 27, 28=Series Group 28, 29=Series Group 29, 30=Series Group 30]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  YearTransf VarChar(1) Year-End Closing default=N [Y=Yes, N=No]
  Indicator nVarChar(10) Period Indicator default=' ' ->OPID
  Template nVarChar(20) Template
  NumSize Int(11) Numeric Size
  FolioPref nVarChar(4) Folio Prefix String
  NextFolio Int(11) Next Folio Number
  DocSubType nVarChar(2) Document Sub-Type default=--
  DefESeries Int(6) Default Electronic Series default=0
  IsDigSerie VarChar(1) Is Digital Series default=N [Y=Yes, N=No]
  SeriesType VarChar(1) Series Type default=D [D=Document, B=Business Partner, I=Item, R=Resource, W=Witholding Certificates]
  IsManual VarChar(1) Is Manual Series default=N [Y=Yes, N=No]
  BPLId Int(11) Assigned Branch ->OBPL
  IsForCncl VarChar(1) Is Series for Cancelation default=N [Y=Yes, N=No]
  AtDocType nVarChar(2) AT Document Type [GT=GT, GA=GA, GD=GD, GR=GR, GC=GC, FT=FT, FS=FS, NC=NC, ND=ND, FR=FR]
  IsElAuth VarChar(1) Elec. Authorization Code default=N [Y=Yes, N=No]
  CoAccount VarChar(1) Cost Account Only default=N [Y=Yes, N=No]
  GenPassprt VarChar(1) Do Generate SAP Passport default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  logInstanc Int(11) Log Instance - History
  PInvType Int(11) Abs Type of Positive Value Invoice ->OEIT
  NInvType Int(11) Abs Type of Negative Value Invoice ->OEIT
  AssignedID nVarChar(70) Assigned ID
  Action VarChar(1) Action [R=Report, C=Cancel, F=Finalize]
  Status VarChar(1) Status [R=Reported, C=Canceled, F=Finalized]
  Phase VarChar(1) Phase [T=To Be Processed, I=In Process, O=OK, E=Error]

# NNM2 - Series Default
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, UserSign
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  UserSign Int(6) User Signature ->OUSR
  Series Int(11) Series
  DocSubType nVarChar(2) Document Sub-Type default=--

# NNM3 - Documents Numbering -Belgium Series
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType, Series
  SERIES: Series
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  Series Int(11) Series default=0
  DocSubType nVarChar(2) VAT Code for Tax Invoice Rpt default=--
  logInstanc Int(11) Log Instance - History

# NNM4 - Electronic Series
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ESeries, InitialNum
Fields (name type(len) description [values] ->parent table):
  ESeries Int(6) Electronic Series default=0
  Series Int(11) Series
  SeriesName nVarChar(8) Series Name
  InitialNum nVarChar(20) Initial Number default=0
  NextNumber nVarChar(20) Next Number for Use default=0
  LastNum nVarChar(20) Last Number Allowed
  Prefix nVarChar(10) Prefix
  ApprovYear Int(11) Approval Year
  ApprovNum Int(11) Approval Number
  Remark nVarChar(50) Remarks

# NNM5 - Document Numbering - Removed Serial Numbers
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Series, ObjectCode, DocSubType, Number
  SERIES: Series, Number
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  Series Int(11) Series
  DocSubType nVarChar(2) Document Subtype default=--
  Number Int(11) Number

# NNM6 - Documents Numbering - Supplementary Code
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, PeriodType, StartDate, EndDate
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document ->ONNM
  PeriodType VarChar(1) Sequence Period Type [Y=Annually, M=Monthly, W=Weekly, P=Permanent]
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  Sequence Int(11) Current Sequence
  FormatStr nVarChar(254) Format String for Create Code

# OAAR - Substitute Authorizer
Module: Administration | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  AuthrID Int(11) Authorizer ID ->OUSR
  SubsttID Int(11) Substitute Authorizer ID ->OUSR
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  WtmCode Int(11) Approval Template Code ->OWTM
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  CreateDate Date(8) Date Created
  CreateTS Int(11) Creatn Time - Incl. Secs
  UserSign Int(11) User Signature ->OUSR
  UserSign2 Int(6) User Signature 2
  Applied VarChar(1) Substitute Action Performed default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Update Date

# OADF - Address Formats
Module: Administration | 5 columns | ObjType: 131
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  ADF_NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(50) Name
  Format nVarChar(100) Format
  UserSign Int(6) User Signature ->OUSR
  SuppBkLine VarChar(1) Suppress Blank Lines default=N [N=No, Y=Yes]

# OADM - Administration
Module: Administration | 562 columns | ObjType: 39
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  CompnyName nVarChar(100) Company Name
  CompnyAddr nVarChar(254) Address
  Country nVarChar(3) Country/Region ->OCRY
  PrintHeadr nVarChar(100) Printing Header
  Phone1 nVarChar(50) Telephone Number 1
  Phone2 nVarChar(50) Telephone Number 2
  Fax nVarChar(50) Fax Number
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
  BankCountr nVarChar(3) Bank Country/Region
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
  ERpPerType VarChar(1) Period Type for Report Generation default=M [Y=Year, Q=Quarter, B=Bi-Monthly, M=Month, P=Period, F=Fiscal Year, G=Fiscal Quarter]
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
  Phone1F nVarChar(50) Tel. No. 1 (Foreign Language)
  Phone2F nVarChar(50) Tel. No. 2 (Foreign Language)
  FaxF nVarChar(50) Fax Number (Foreign Lang.)
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
  free84 VarChar(1) Free84
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
  RoundMthd VarChar(1) Rounding Method default=N [Y=Yes, N=No]
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
  JeUnGroup VarChar(1) Journal Entry Split Lines default=N [N=No Split, Y=Split in Journal Entry Preview Only, S=Split, T=Split Except Tax Lines, P=Split Except Tax Lines in Journal Entry Preview Only]
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
  SmtpPasswd nVarChar(254) SMTP Password
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
  ExpDocLoc VarChar(1) Export To OneDrive or Locally default=L
  TenantId nVarChar(100) Tenant ID
  IntegUrl nVarChar(254) Integration Server URL default=https://b1-scp-office.cfapps.sap.hana.ondemand.com/
  EnableMTD VarChar(1) Enable Making Tax Digital default=N [N=No, Y=Yes]
  PublicComp VarChar(1) Public Company default=N [Y=Yes, N=No]
  EnableEWB VarChar(1) Enable E-Way Bills default=N [N=No, Y=Yes]
  TspEntry Int(11) Default Transporter
  TspLine Int(11) Default Transportation Line
  EwbGenType VarChar(1) Default EWB Generate Type default=N [N=Not Relevant, G=Generate, L=Generate - Later]
  VolumeLic VarChar(1) Use Volume Based Licensing default=N [Y=Yes, N=No]
  Threshold Num(19,6) Threshold for Customer Accounting
  EnAuthUpt VarChar(1) Enable Authorizer Update Draft default=N [Y=Yes, N=No]
  DfSVatExG nVarChar(8) Default Tax Code for Realized Exchange Rate Diff. Gain ->OVTG
  DfSVatExL nVarChar(8) Default Tax Code for Realized Exchange Rate Diff. Loss ->OVTG
  EnUpdBpAdr VarChar(1) Enable Updating BP Address ID default=Y [Y=Yes, N=No]
  PAutoDueDt VarChar(1) Definition of Due Date To default=N [Y=Yes, N=No]
  PDuDtMonth Int(6) Month of Due Date To default=1 [1=January, 2=February, 3=March, 4=April, 5=May, 6=June, 7=July, 8=August, 9=September, 10=October, 11=November, 12=December]
  DriDownBOM VarChar(1) Open Item Master Data of an Item Directly with Link Arrow default=N [Y=Yes, N=No]
  EnExtTax VarChar(1) Enable External Tax default=N [Y=Yes, N=No]
  DfDateFct Int(11) Default Valid Date Factor default=1
  DfDateUnit VarChar(1) Default Valid Date Unit default=M [M=Months, W=Weeks, D=Days]
  EnMutiBP VarChar(1) Enable Multiple BPs default=N [Y=Yes, N=No]
  AddBPToEC VarChar(1) Add BP to Existing Equipment Card default=N
  EnAutoRsz VarChar(1) Auto Resize User Forms default=N [Y=Yes, N=No]
  QRMinSize Int(11) Minimum default=1
  QRMaxSize Int(11) Maximum default=40
  QRScale Int(11) Scale default=10
  QRExpDays Int(11) Expiration Days default=10
  QRExpir VarChar(1) Expiration Date default=N [Y=Yes, N=No]
  QRCorrLvl VarChar(1) Correction Level default=M [L=Low, M=Medium, Q=Quartile, H=High]
  TaxCatVer nVarChar(20) Version of Tax Category Code default=32.0
  EffPriDisc VarChar(1) Effective Prices Consider Both Prices Before and After Discount Groups default=N [Y=Yes, N=No]
  CpyBaseAtc VarChar(1) Copy Attachments from Base Document to Target Document default=N [Y=Yes, N=No]
  ItmDupBCD VarChar(1) Duplicate Bar Codes While Duplicating Items default=Y [Y=Yes, N=No]
  AllowUpdat VarChar(1) Allow Update Reference and UDF default=N [Y=Yes, N=No]
  BlkNegJLin VarChar(1) Block Negative Lines default=N [Y=Yes, N=No]
  EnARWTLnMX VarChar(1) Enable Sales WTax in Rows default=N [Y=Yes, N=No]
  PoARPayCat VarChar(1) Post Sales Payment Category WTax default=N [Y=Yes, N=No]
  AplyARExhR VarChar(1) Apply Sales Exchange Rate to WTax default=N [Y=Yes, N=No]
  EnAPWTLnMX VarChar(1) Enable Purchasing WTax in Rows default=N [Y=Yes, N=No]
  PoAPPayCat VarChar(1) Post Purchase Payment Category WTax default=N [Y=Yes, N=No]
  AplyAPExhR VarChar(1) Apply Purchasing Exchange Rate to WTax default=N [Y=Yes, N=No]
  DispCtInBP VarChar(1) Display Inactive Contact Persons in BP Master Data default=Y [Y=Yes, N=No]
  UseDfltPL VarChar(1) Use Default Price List default=N [Y=Yes, N=No]
  DfltCustPL Int(6) Default Price List for Customer ->OPLN
  DfltVendPL Int(6) Default Price List for Vendor ->OPLN
  EORINumber nVarChar(17) EORI Number
  SkipRutChk VarChar(1) Skip check of RUT length default=N [Y=Yes, N=No]
  EnbUQAudit VarChar(1) Enable Execution Audit Log for User-Defined Query default=Y [Y=Yes, N=No]
  CpyBomAtc VarChar(1) Copy Attachments from BOM default=N [Y=Yes, N=No]
  DnOvrwrAtc VarChar(1) Don't overwrite attachments default=N [Y=Yes, N=No]
  IsTAForMI VarChar(1) Enable Creation of Tax Adjustment for Monthly Invoice default=Y [N=No, Y=Yes]
  AutoTAAppr VarChar(1) Tax Adjustment is Approved Automatically default=Y [N=No, Y=Yes]

# OADP - Print Preferences
Module: Administration | 41 columns | ObjType: 32
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PrintId
Fields (name type(len) description [values] ->parent table):
  PrintId nVarChar(4) Print Number
  ObjList Int(11) Object List default=13 [1470000049=Capitalization, 1470000071=Depreciation Run, 1470000090=Fixed Asset Transfer, 23=Sales Quotation, 17=Sales Order, 15=Delivery, 234000031=Return Request, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Return Request, 21=Goods Return, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 69=Landed Costs, 24=Incoming Payment, 25=Deposit, 46=Outgoing Payment, 76=Postdated Deposit, 57=Check for Payment, 30=Journal Entry, 28=Journal Voucher, 140000010=Incoming Excise Invoice, 140000009=Outgoing Excise Invoice, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 68=Work Instructions, 202=Production Order, 162=Inventory Revaluation, 156=Pick List, 1470000065=Inventory Counting, 10000071=Inventory Posting, 310000001=Inventory Opening Balances, 191=Service Call, 190=Service Contract, 176=Equipment Card, 88=Entrada, 89=Salida, 90=Traspaso, 132=Correction Invoice, 234000021=Project Management Document]
  MaxLineNum Int(6) Max. Rows per Page default=99
  TopMrgn Int(6) Top Margin Width
  BtmMrgn Int(6) Bottom Margin Width
  LftMrgn Int(6) Left Margin Width
  RgtMrgn Int(6) Right Margin Width
  PrnCompany VarChar(1) Print on Company Paper default=N [Y=Yes, N=No]
  MnhlNote VarChar(1) Text Printed by PLD default=Y [Y=Yes, N=No]
  MaxWordLin Int(6) Max. Rows for Export default=10
  V_Compress Int(6) Compress Vertically default=100 [50=50, 60=60, 70=70, 80=80, 90=90, 100=100, 110=110, 120=120, 130=130, 140=140, 150=150]
  WordPath Text(16) WORD Template Path
  BitmapPath Text(16) Picture Path
  PrintMeta VarChar(1) Print as Picture default=N [Y=Yes, N=No]
  PrintRcpt VarChar(1) Print Receipt default=N [N=No, A=Only When Adding, Y=Always]
  ShortRcpt VarChar(1) Print Payment with Invoice default=N [Y=Yes, N=No]
  ExportCode VarChar(1) Export Material/Account Code default=N [Y=Yes, N=No]
  AttachPath Text(16) Attachments Path
  DraftNote VarChar(1) Print Draft Note default=Y [Y=Yes, N=No]
  ExtPath Text(16) Extensions Path
  DmePath Text(16) DME Files Store Path
  SNType Int(6) Serial Number Type default=2 [1=Mfr Serial No., 2=Serial No., 3=Lot Number]
  GBIPath Text(16) GB Data Interface Path
  LogoFile nVarChar(200) Logo File
  LogoImage Text(16) Logo Image
  B1Server Text(16) Business One Server Address
  IsTrustSrv VarChar(1) Always Trust This Server default=N [Y=Yes, N=No]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User ->OUSR
  SnapShotId Int(11) Snapshot ID default=0
  DefirExpP Text(16) Export Folder
  DefirDemop Text(16) DEFIR Database Path
  PrintPDF VarChar(1) Generate PDF When Printing default=N [Y=Yes, N=No]
  PrtCancel VarChar(1) Print Watermark on Cancl. Docs default=Y [Y=Yes, N=No]
  PrtUseSys VarChar(1) Use System Print Preferences default=N [Y=Yes, N=No]
  RptList nVarChar(20) Report List default=1 [1=Aging Report, 2=Dunning Wizard]
  PreAttach Text(16) Previous Attachment Path
  ExportPDF VarChar(1) Export PDF to Dflt Attachment default=N [Y=Yes, N=No]
  AttachPDF VarChar(1) Attach Exported PDF to Doc default=N [Y=Yes, N=No]
  GSTPath Text(16) GST ANX Report Path

# OAIB - Received Alerts
Module: Administration | 8 columns | ObjType: 82
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AlertCode, UserSign
  USER: UserSign
  READ: WasRead
  DELETED: Deleted
Fields (name type(len) description [values] ->parent table):
  AlertCode Int(11) Alert Code ->OALR
  UserSign Int(6) User Signature ->OUSR
  Opened VarChar(1) Opened default=N [Y=Yes, N=No]
  RecDate Date(8) Receipt Date
  RecTime Int(6) Time Received
  WasRead VarChar(1) Read default=N [Y=Yes, N=No]
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  Failed VarChar(1) Failed default=N [Y=Yes, N=No]

# OALC - Loading Expenses
Module: Administration | 8 columns | ObjType: 48
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AlcCode
  GROUP_NAME: AlcName
Fields (name type(len) description [values] ->parent table):
  AlcCode nVarChar(2) Code
  AlcName nVarChar(30) Name
  OhType VarChar(1) Allocation By default=F [F=Cash Value Before Customs, C=Cash Value After Customs, Q=Quantity, W=Weight, V=Volume, A=Equal, L=Legal Cost]
  AcctCode nVarChar(15) Account Code ->OACT
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LaCAllcAcc nVarChar(15) Landed Costs Alloc. Account
  CostCateg VarChar(1) Cost Category [V=Customs VAT, E=Excise Cost, D=Customs Duty]

# OALR - Alerts
Module: Administration | 14 columns | ObjType: 81
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  Type VarChar(1) Type default=A [A=Alert, M=Message]
  Priority VarChar(1) Priority default=1 [0=-, 1=, 2=mHighPriority]
  TCode Int(11) Template Code ->OALT
  Subject nVarChar(254) Subject
  UserText Text(16) MEMO
  DataCols Int(11) No. of Columns
  DataParams Text(16) Data
  MsgData Text(16) Data
  UserSign Int(6) User Signature ->OUSR
  Attachment Text(16) Attached File
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AtcEntry Int(11) Attachment Entry
  AltType VarChar(1) Alert Type default=N [N=Unknown, C=Inventory Cycle]

# OALT - Alerts Management
Module: Administration | 24 columns | ObjType: 80
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  ACTIVE: Active
  NAME: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  Name nVarChar(254) Name
  Type VarChar(1) Type default=U [S=System Alert, U=User Alert]
  Priority VarChar(1) Priority default=1 [0=Low, 1=Normal, 2=High]
  Active VarChar(1) Active Alert default=N [Y=Yes, N=No]
  NumOfParam Int(11) No. of Parameters
  ParamData Text(16) Parameters
  Params Text(16) Parameters
  NumOfDocs Int(11) Documents Numbers
  DocsData Text(16) Documents
  Docs Text(16) Documents
  UserText Text(16) MEMO
  QueryId Int(11) Query
  FrqncyType VarChar(1) Frequency Type default=H [S=Minutes, H=Hours, D=Days, W=Weeks, M=Months]
  FrqncyIntr Int(11) Frequency default=1
  ExecDaY Int(6) Day of Execution default=1
  ExecTime Int(11) Execution Hour default=800
  LastDate Date(8) Execution Date
  LastTIME Int(6) Execution Time
  NextDate Date(8) Next Date
  NextTime Int(6) Next Hour
  UserSign Int(6) User Signature ->OUSR
  History VarChar(1) Save History default=N [Y=Yes, N=No]
  QCategory Int(11) Query Category ->OUQR

# OAOB - Message Sent
Module: Administration | 5 columns | ObjType: 83
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AlertCode, UserSign
  USER: UserSign
Fields (name type(len) description [values] ->parent table):
  AlertCode Int(11) Alert Code ->OALR
  SendDate Date(8) Date
  SendTime Int(6) Time
  WasSent VarChar(1) Sent default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR

# OARI - Add-On - Company Definitions
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AddOnID
Fields (name type(len) description [values] ->parent table):
  AddOnID Int(11) Add-On ID
  EGroup VarChar(1) Execution Group [A=Automatic, M=Manual, C=Critical]
  AStatus VarChar(1) Is add-on active? default=Y [Y=Yes, N=No]
  EventOrder Int(11) Add-on Event Order
  IsAdd64 VarChar(1) Add-On is 64 Bit default=N
  AddPlat VarChar(1) Add-On Installer Platform default=N [N=x86, X=x64, A=ARM]

# OATC - Attachments
Module: Administration | 1 columns | ObjType: 221
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Absolute entry

# OBDC - B1i DI Configuration
Module: Administration | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Server nVarChar(254) Server
  License nVarChar(254) License Server
  Company nVarChar(128) Company
  DBType Int(11) DB Type
  DBUser nVarChar(254) DB User
  DBPassword nVarChar(254) DB Password
  Username nVarChar(254) User Name
  UPassword nVarChar(254) User Password
  DBTrusted VarChar(1) DB Trusted
  JCOPath nVarChar(254) Java Connector Path
  Language Int(11) Language
  AddOnIF nVarChar(254) Add-On Identifier
  StateFder nVarChar(254) Bank Statement Folder
  FormatFder nVarChar(254) Bank Format Folder
  FileFolder nVarChar(254) Bank File Folder

# OBMI - Brazilian Multi-Indexer
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  IND_CODE_K U: IndexType, Code
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Unique ID
  IndexType Int(11) Indexer Type default=-1
  Code nVarChar(10) Code
  Descr nVarChar(254) Description
  RefIndCod1 nVarChar(10) First Referenced Indexer Code
  RefIndCod2 nVarChar(10) Second Referenced Indexer Code
  RefIndCod3 nVarChar(10) Third Referenced Indexer Code
  UserSign Int(6) User Signature ->OUSR

# OBOI - Count Widget
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(15) Count Widget Code
  Name nVarChar(100) Name
  QueryId Int(11) Link Query ID ->OUQR
  QCategory Int(11) Link Query Category ->OQCN
  Desc nVarChar(200) Description
  MenuId Int(11) Menu ID default=0

# OBPD - Blocked Personal Data
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  DATA_SUBJ: DatSubType, DatSubKey, DatSubKey2
  TABL_FIELD: TableName, KeyValue1, KeyValue2, KeyValue3, KeyValue4, KeyValue5, FieldName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  DatSubType nVarChar(4) Data Subject Type [OCRD=Business Partner, OCPR=Contact Person, OHEM=Employee, OUSR=User, CPN1=Campaign - BP]
  DatSubKey nVarChar(15) Data Subject Key No.1
  DatSubKey2 nVarChar(50) Data Subject Key No.2
  TableName nVarChar(20) Table Name
  KeyValue1 nVarChar(50) Key Value No.1
  KeyValue2 nVarChar(50) Key Value No.2
  KeyValue3 nVarChar(50) Key Value No.3
  KeyValue4 nVarChar(50) Key Value No.4
  KeyValue5 nVarChar(50) Key Value No.5
  FieldName nVarChar(50) Field Name
  EncryptVal Text(16) Encryption Value
  EncryptIV nVarChar(100) Encryption Initialization Vector
  CreateDate Date(8) Creation Date
  CreateTime Int(11) Creation Time

# OBRW - Browser Widget
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) Browser Widget Name
  Type Int(6) Type default=0 [0=Web Site, 1=App]
  Url nVarChar(254) Web Site or Extreme Application URL
  App nVarChar(100) Extreme Application Name
  Title nVarChar(254) Title
  ShowWebTil VarChar(1) Display Web Page Title default=N [Y=Yes, N=No]
  Size nVarChar(15) Widget Size

# OBSI - Brazil String Indexer
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  IND_CODE_K U: IndexType, Code
Fields (name type(len) description [values] ->parent table):
  IndexType Int(11) Indexer Type
  Code nVarChar(30) Code
  Descr Text(16) Beverage Table
  UserSign Int(6) User Signature ->OUSR
  ID Int(11) Unique ID
  ValidFrom Date(8) Valid From
  ValidTo Date(8) Valid To

# OCCD - Cargo Customs Declaration Numbers
Module: Administration | 9 columns | ObjType: 283
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CCDNum
Fields (name type(len) description [values] ->parent table):
  CCDNum nVarChar(40) CCD Number
  Date Date(8) Date
  CustBroker nVarChar(15) Customs Broker
  DocNum nVarChar(20) Imp./Exp. Document Number
  DocDate Date(8) Imp./Exp. Document Date
  SupNum nVarChar(20) Supply Agreement Number
  SupDate Date(8) Supply Agreement Date
  CustTerm nVarChar(15) Customs Terminal
  PayKey nVarChar(4) Payment Internal ID

# OCDP - Closing Date Procedure
Module: Administration | 6 columns | ObjType: 261
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ClsDateNum
  ABS_ENTRY U: ClsDtCode
Fields (name type(len) description [values] ->parent table):
  ClsDateNum Int(6) Closing Date Procedure Number
  ClsDtCode nVarChar(30) Closing Date Procedure Code
  BsLineDate VarChar(1) Base Row Date default=S [P=Posting Date, S=System Date]
  DueMonth VarChar(1) Start From default=N [E=Month End, H=Half Month, Y=Month Start, N=]
  ExtraMonth Int(6) Extra Month
  ExtraDay Int(6) Extra Day

# OCDT - Credit Card Payment
Module: Administration | 23 columns | ObjType: 71
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Credit Card Payment Code
  Name nVarChar(30) Credit Card Payment Name
  TERM_TYPE VarChar(1) Credit Card Payment Types default=F [D=By Dates, F=After Time Period]
  After_Days Int(6) Payment After Days
  After_Mnth Int(6) Payment After Months
  Day_From1 Int(6) From Day 1
  Day_To1 Int(6) To Day 1
  Pay_Day1 Int(6) Payment Date 1
  Pay_Month1 Int(6) No. of Months 1
  Day_From2 Int(6) From Day 2
  Day_To2 Int(6) To Day 2
  Pay_Day2 Int(6) Payment Date 2
  Pay_Month2 Int(6) No. of Months 2
  Day_From3 Int(6) From Day 3
  Day_To3 Int(6) To Day 3
  Pay_Day3 Int(6) Payment Date 3
  Pay_Month3 Int(6) No. of Months 3
  Day_From4 Int(6) From Day 4
  Day_To4 Int(6) To Day 4
  Pay_Day4 Int(6) Payment Date 4
  Pay_Month4 Int(6) No. of Months 4
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OCEST - CEST Codes
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CEST_CODE U: CEST
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CEST nVarChar(32) CEST Code
  Descr Text(16) Description
  LogInstanc Int(11) Log Instance default=0

# OCFP - CFOP for Nota Fiscal
Module: Administration | 10 columns | ObjType: 258
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  CFOP_CODE U: Code
Fields (name type(len) description [values] ->parent table):
  ID Int(11) CFOP ID
  Code nVarChar(6) CFOP Code
  Descrip Text(16) Description
  App Text(16) Application
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Data Doc., P=Partner Implementation]
  UserSign nVarChar(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OCFX - Cash Flow Forecast Object Types
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjType
Fields (name type(len) description [values] ->parent table):
  ObjType nVarChar(20) Object Type
  Level Int(11) Level
  ObjName nVarChar(100) Object Name
  Group nVarChar(2) Group

# OCHF - 312
Module: Administration | 3 columns | ObjType: 218
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjName
Fields (name type(len) description [values] ->parent table):
  ObjName nVarChar(20) Object Name
  UserSign Int(6) User Signature ->OUSR
  UpdateDate Date(8) Date of Update

# OCIF - Configuration of Intrastat Fields
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  ISTable nVarChar(4) Intrastat Wizard Table
  ISField nVarChar(10) Intrastat Wizard Field Alias
  FieldDesc nVarChar(200) Field Description
  FlLocation nVarChar(200) Field Location
  FldSource nVarChar(200) Source of the Field Value

# OCMN - Customized Menu
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GUID
  UID_KEY: MenuUID
Fields (name type(len) description [values] ->parent table):
  GUID nVarChar(32) GUID
  Name nVarChar(100) Menu Item Name
  Father nVarChar(32) Menu Parent GUID
  Type VarChar(1) Menu Type default=C [S=, A=, C=]
  SubMenu VarChar(1) Submenu Flag default=N [Y=, N=]
  MenuUID nVarChar(50) Menu UID
  ObjectType Int(11) Target Object Type
  ObjectKey nVarChar(200) Target Object ID
  PermFolder Int(11) Permission Folder ID
  SortOrder Int(11) Sort Order

# OCNA - CNAE Code
Module: Administration | 3 columns | ObjType: 278
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: CNAECode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  CNAECode nVarChar(9) Code
  Descrip Text(16) Description

# OCNT - Counties
Module: Administration | 8 columns | ObjType: 265
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  UNIQUE U: Code, Country, State
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Auto Key
  Code nVarChar(7) County Code
  Country nVarChar(3) Country/Region ->OCST
  State nVarChar(3) State ->OCST
  Name nVarChar(100) County Name
  TaxZone VarChar(1) Tax Free Zone default=N [Y=Yes, N=No]
  IbgeCode nVarChar(10) IBGE Code
  GiaCode nVarChar(10) GIA Code

# OCPC - Quick Copy Config.
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  OLDContent Text(16) Old DI Files Content
  DiExpoCont Text(16) Expose DI File Content

# OCPL - Quick Copy Log Manager
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  StartDate Date(8) Start Date
  StartTime nVarChar(6) Start Time
  EndDate Date(8) End Date
  EndTime nVarChar(6) End Time
  CopySource nVarChar(254) Copy Source
  CopyTarget nVarChar(254) Copy Target
  UserName nVarChar(20) User Name
  CopyMethod Int(6) Copy Method [2=Delete All Records Then Add New Records, 4=Update Existing Records Without Adding New Records, 8=Add New Records Without Updating Existing Records, 16=Add New Records and Update Existing Records, 0=N/A]
  FailRpn Int(6) Copy failed [1=Ignore All Errors and Copy Valid Records, 2=Obtain User Confirmation, 3=Terminate Copy Process When One or More Errors Occur, 4=Terminate Copy Process When Number of Errors Exceeds]
  MissingUDF VarChar(1) UDF missing [2=N/A, 1=Copy Records and Ignore Missing UDFs, 0=Do Not Copy Records with Missing UDFs]
  CopyType Int(6) Copy Type
  ErrorNum nVarChar(11) Error Number
  NullifyAct Int(6) Nullify Account [2=N/A, 1=Use Default Accounts in Target, 0=Use Accounts in Source]
  CopyEmtVal Int(6) Copy Empty Value [2=N/A, 1=Do Not Overwrite Target Fields and Keep Original Values, 0=Overwrite Target Fields with Empty Values]

# OCRC - Credit Cards
Module: Administration | 13 columns | ObjType: 36
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CreditCard
  CARD_NAME U: CardName
Fields (name type(len) description [values] ->parent table):
  CreditCard Int(6) Credit Card Code
  CardName nVarChar(30) Credit Card Name
  AcctCode nVarChar(15) G/L Account ->OACT
  Phone nVarChar(50) Telephone
  CompanyId nVarChar(20) Company ID
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  IntTaxCode nVarChar(2) Internal Tax Code [1=Isracard, 2=CAL, 3=Diners, 4=American Express, 6=Leumi Card]
  UserSign2 Int(6) Updating User ->OUSR
  Country nVarChar(3) Country/Region Code ->OCRY

# OCRN - Currency Codes
Module: Administration | 28 columns | ObjType: 37
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CurrCode
  CUR_NAME: CurrName
Fields (name type(len) description [values] ->parent table):
  CurrCode nVarChar(3) Currency Code
  CurrName nVarChar(20) Currency
  ChkName nVarChar(20) Name on Printed Checks
  Chk100Name nVarChar(20) Name of 100's on checks
  DocCurrCod nVarChar(3) Name on Printed Docs.
  FrgnName nVarChar(20) English
  F100Name nVarChar(20) English Hundredth Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  RoundSys Int(6) Rounding default=0 [0=No Rounding, 4=Round to Five Hundredth, 1=Round to Ten Hundredth, 2=Round to One, 3=Round to Ten]
  UserSign2 Int(6) Updating User ->OUSR
  Decimals Int(6) Decimals default=-1 [-1=Default, 0=Without Decimals, 1=1 Digit, 2=2 Digits, 3=3 Digits, 4=4 Digits, 5=5 Digits, 6=6 Digits]
  ISRCalc VarChar(1) ISR Calculation default=N [Y=Yes, N=No]
  RoundPym VarChar(1) Rounding in Pmnt default=N [Y=Yes, N=No]
  ConvUnit VarChar(1) Is a Conventional Unit default=N [Y=Yes, N=No]
  BaseCurr nVarChar(3) Base Currency for Conv. Unit ->OCRN
  Factor Num(19,6) Factor
  ChkNamePl nVarChar(20) Plural for Int.Description
  Chk100NPl nVarChar(20) Plural for Hundredth Name
  FrgnNamePl nVarChar(20) Plural for English
  F100NamePl nVarChar(20) Plural for Eng. Hundredth Name
  ISOCurrCod nVarChar(3) ISO Currency Code [AED=United Arab Emirates, Dirhams, AFN=Afghanistan, Afghanis, ALL=Albania, Leke, AMD=Armenia, Drams, ANG=Netherlands Antilles, Guilders (also called Florins), AOA=Angola, Kwanzas, ARS=Argentina, Pesos, AUD=Australia, Dollars, AWG=Aruba, Guilders (also called Florins), AZM=Azerbaijan, Manats [obsolete], AZN=Azerbaijan, New Manats, BAM=Bosnia and Herzegovina, Convertible Marks, BBD=Barbados, Dollars, BDT=Bangladesh, Taka, BGN=Bulgaria, Leva, BHD=Bahrain, Dinars, BIF=Burundi, Francs, BMD=Bermuda, Dollars, BND=Brunei, Ringgits, BOB=Bolivia, Bolivianos, BRL=Brazil, Brazilian Reals, BSD=Bahamas, Dollars, BTN=Bhutan, Ngultrum, BWP=Botswana, Pulas, BYN=Belarus, Rubles, BYR=Belarus, Rubles, BZD=Belize, Dollars, CAD=Canada, Dollars, CDF=Congo/Kinshasa, Congolese Francs, CHF=Switzerland, Francs, CLP=Chile, Pesos, CNY=China, Yuan Renminbi, COP=Colombia, Pesos, CRC=Costa Rica, Colones, CUP=Cuba, Pesos, CVE=Cape Verde, Escudos, CYP=Cyprus, Pounds, CZK=Czech Republic, Koruny, DJF=Djibouti, Francs, DKK=Denmark, Kroner, DOP=Dominican Republic, Pesos, DZD=Algeria, Algerian Dinars, EEK=Estonia, Krooni, EGP=Egypt, Pounds, ERN=Eritrea, Nakfa, ETB=Ethiopia, Birr, EUR=EU Member Countries, Euro, FJD=Fiji, Dollars, FKP=Falkland Islands (Malvinas), Pounds, GBP=United Kingdom, Pounds, GEL=Georgia, Lari, GGP=Guernsey, Pounds, GHC=Ghana, Cedis, GHS=Ghana, Cedis, GIP=Gibraltar, Pounds, GMD=Gambia, Dalasi, GNF=Guinea, Francs, GTQ=Guatemala, Quetzales, GYD=Guyana, Dollars, HKD=Hong Kong, Dollars, HNL=Honduras, Lempiras, HRK=Croatia, Kuna, HTG=Haiti, Gourdes, HUF=Hungary, Forint, IDR=Indonesia, Rupiahs, ILS=Israel, New Shekels, IMP=Isle of Man, Pounds, INR=India, Rupees, IQD=Iraq, Dinars, IRR=Iran, Rials, ISK=Iceland, Kronur, JEP=Jersey, Pounds, JMD=Jamaica, Dollars, JOD=Jordan, Dinars, JPY=Japan, Yen, KES=Kenya, Shillings, KGS=Kyrgyzstan, Soms, KHR=Cambodia, Riels, KMF=Comoros, Francs, KPW=Korea (North), Won, KRW=Korea (South), Won, KWD=Kuwait, Dinars, KYD=Cayman Islands, Dollars, KZT=Kazakhstan, Tenge, LAK=Laos, Kips, LBP=Lebanon, Pounds, LKR=Sri Lanka, Rupees, LRD=Liberia, Dollars, LSL=Lesotho, Maloti, LTL=Lithuania, Litai, LVL=Latvia, Lati, LYD=Libya, Dinars, MAD=Morocco, Dirhams, MDL=Moldova, Lei, MGA=Madagascar, Ariary, MKD=Macedonia, Denars, MMK=Myanmar (Burma), Kyats, MNT=Mongolia, Tugriks, MOP=Macau, Patacas, MRO=Mauritania, Ouguiyas, MTL=Malta, Liri, MUR=Mauritius, Rupees, MVR=Maldives (Maldive Islands), Rufiyaa, MWK=Malawi, Kwachas, MXN=Mexico, Pesos, MYR=Malaysia, Ringgits, MZM=Mozambique, Meticais [obsolete], MZN=Mozambique, Meticais [newer unit, same name], NAD=Namibia, Dollars, NGN=Nigeria, Nairas, NIO=Nicaragua, Cordobas, NOK=Norway, Krone, NPR=Nepal, Nepal Rupees, NZD=New Zealand, Dollars, OMR=Oman, Rials, PAB=Panama, Balboa, PEN=Peru, Nuevos Soles, PGK=Papua New Guinea, Kina, PHP=Philippines, Pesos, PKR=Pakistan, Rupees, PLN=Poland, Zlotych, PYG=Paraguay, Guarani, QAR=Qatar, Rials, ROL=Romania, Lei [obsolete], RON=Romania, New Lei, RSD=Serbia, Dinars, RUB=Russia, Rubles, RWF=Rwanda, Rwandan Francs, SAR=Saudi Arabia, Riyals, SBD=Solomon Islands, Dollars, SCR=Seychelles, Rupees, SDD=Sudan, Dinars [obsolete], SDG=Sudan, Pounds, SEK=Sweden, Kronor, SGD=Singapore, Dollars, SHP=Saint Helena, Pounds, SIT=Slovenia, Tolars [obsolete], SKK=Slovakia, Koruny, SLL=Sierra Leone, Leones, SOS=Somalia, Shillings, SPL=Seborga, Luigini, SRD=Suriname, Dollars, STD=Sao Tome and Principe, Dobras, SVC=El Salvador, Colones, SYP=Syria, Pounds, SZL=Swaziland, Emalangeni, THB=Thailand, Baht, TJS=Tajikistan, Somoni, TMT=Turkmenistan, Manats, TND=Tunisia, Dinars, TOP=Tonga, Pa'anga, TRY=Turkey, New Lira, TTD=Trinidad and Tobago, Dollars, TVD=Tuvalu, Tuvalu Dollars, TWD=Taiwan, New Dollars, TZS=Tanzania, Shillings, UAH=Ukraine, Hryvnia, UGX=Uganda, Shillings, USD=United States of America, Dollars, UYU=Uruguay, Pesos, UZS=Uzbekistan, Sums, VEB=Venezuela, Bolivares, VND=Viet Nam, Dong, VUV=Vanuatu, Vatu, WST=Samoa, Tala, XAF=Communaute Financiere Africaine BEAC, Francs, XAG=Silver, Ounces, XAU=Gold, Ounces, XCD=East Caribbean Dollars, XDR=International Monetary Fund (IMF) Special Drawing Rights, XOF=Communaute Financiere Africaine BCEAO, Francs, XPD=Palladium Ounces, XPF=Comptoirs Francais du Pacifique Francs, XPT=Platinum, Ounces, YER=Yemen, Rials, ZAR=South Africa, Rand, ZMK=Zambia, Kwacha, ZWD=Zimbabwe, Zimbabwe Dollars]
  MaxInDiff Num(19,6) Incoming Amt Diff. Allowed
  MaxOutDiff Num(19,6) Outgoing Amt Diff. Allowed
  MaxInPcnt Num(19,6) Incoming % Diff. Allowed
  MaxOutPcnt Num(19,6) Outgoing % Diff. Allowed
  ISOCurrNum nVarChar(3) ISO Currency Number

# OCRP - Payment Methods
Module: Administration | 11 columns | ObjType: 70
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CrTypeCode
  NAME U: CrTypeName
  CRED_CODE: CreditCard
  INSTALMENT: InstalMent
Fields (name type(len) description [values] ->parent table):
  CrTypeCode Int(6) Payment Method Code
  CrTypeName nVarChar(30) Name
  CreditCard Int(6) Assigned to Credit Card ->OCRC
  DueTerms nVarChar(8) Payment Code ->OCDT
  MinCredit Num(19,6) Minimum Credit Amount
  MinToPay Num(19,6) Minimum Payment Amount
  MaxValid Num(19,6) Max. Qty Without Approval
  InstalMent VarChar(1) Installment Payments Possible default=N [Y=Yes, N=No, C=Cr, L=Rd]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OCRY - Countries/Regions
Module: Administration | 22 columns | ObjType: 129
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(3) Code
  Name nVarChar(100) Name
  AddrFormat Int(6) Address Format ->OADF
  UserSign Int(6) User Signature ->OUSR
  IsEC VarChar(1) EU default=N [Y=Yes, N=No]
  ReportCode nVarChar(3) Code for Reports
  TaxIdDigts Int(6) No. of Digits for Tax ID
  BnkCodDgts Int(11) No. of Digits for Bank Code
  BnkBchDgts Int(11) No. of Digits for Branch
  BnkActDgts Int(11) No. of Digits for Account No.
  BnkCtKDgts Int(11) No. of Digits for Control No.
  ValDomAcct nVarChar(3) Domestic Bank Acct. Validation default=XX [XX=, BE=Belgium, ES=Spain, FR=France, IT=Italy, NL=Netherlands, PT=Portugal]
  ValIban VarChar(1) IBAN Validation default=N [Y=Yes, N=No]
  IsBlackLst VarChar(1) On Black List default=N [Y=Yes, N=No]
  UICCode nVarChar(3) UIC Country Code
  CntCodNum nVarChar(4) Country/Region Code Number
  Siscomex nVarChar(3) SISCOMEX Country/Region Code
  IsIntraS VarChar(1) Intrastat Trans. default=N [Y=Yes, N=No]
  EAEU VarChar(1) EAEU default=N [Y=Yes, N=No]
  ISO2Code nVarChar(2) ISO Alpha-2 code
  ISO3Code nVarChar(3) ISO Alpha-3 code
  ISONumeric nVarChar(3) ISO Numeric

# OCSC - Crystal Server Configuration
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) CSC Abs. Entry
  Name nVarChar(100) Server Name
  User nVarChar(30) Logon User Code
  Password nVarChar(254) Logon User Password
  URL nVarChar(200) URL
  IsDefault VarChar(1) Is Default default=N [Y=Yes, N=No]
  Port nVarChar(20) Port default=8080

# OCSN - Certificate Series
Module: Administration | 5 columns | ObjType: 10000075
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
  SECTION: Section
  LOCATION: Location
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(4) Code
  Section Int(11) Section ->OSEC
  Location Int(11) Location ->OLCT
  DfltSeries Int(6) Default Series default=0

# OCSQ - Column Sequences
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  SeqType nVarChar(8) Sequence Type
  FormID nVarChar(20) Form ID
  ColToken nVarChar(20) Column Token
  VisualIndx Int(11) Tabs Layout
  VisInForm VarChar(1) Visible in Form default=N [Y=, N=]

# OCST - States
Module: Administration | 9 columns | ObjType: 130
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Country, Code
  GST_CODE: GSTCode, Country
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(3) Code
  Country nVarChar(3) Country/Region ->OCRY
  Name nVarChar(100) Name
  UserSign Int(6) User Signature ->OUSR
  eCode Int(6) eCode
  GNRECode nVarChar(4) GNRE Code
  GSTCode nVarChar(2) GST State Code
  GSTIsUT VarChar(1) Is Union Territory default=N [Y=Yes, N=No]
  GroupCode Int(6) Group Code ->OSTG

# ODAR - Data Archiving
Module: Administration | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  PeriodDate Date(8) Period Date
  UserSign Int(6) User Signature
  CreateDate Date(8) Archive Date
  CreateTime Int(6) Archive Time
  VersionNum Int(11) Version Number
  JEPerLen VarChar(1) Journal Entry Period Length default=A [A=Period, S=Sub-period, M=Month]
  JERef1 nVarChar(100) Journal Entry Reference 1
  JERef2 nVarChar(100) Journal Entry Reference 2
  JEMemo nVarChar(254) Journal Entry Remarks
  JEByProj VarChar(1) Journal Entry By Project default=N [Y=Yes, N=No]
  JEByProf VarChar(1) Journal Entry By Dist. Rule default=N [Y=Yes, N=No]
  INPerLen VarChar(1) Inventory Period Length default=A [A=Period, S=Sub-period, M=Month]
  INPriceSrc Int(6) Inventory Price Source ->OPLN
  INRef1 nVarChar(11) Inventory Reference 1
  INRef2 nVarChar(11) Inventory Reference 2
  INMemo nVarChar(254) Inventory Remarks
  JEByCurr VarChar(1) Journal Entry by Currency default=N [Y=Yes, N=No]
  JEByDIM2 VarChar(1) Journal Entry by Dimension 2 default=N [Y=Yes, N=No]
  JEByDIM3 VarChar(1) Journal Entry by Dimension 3 default=N [Y=Yes, N=No]
  JEByDIM4 VarChar(1) Journal Entry by Dimension 4 default=N [Y=Yes, N=No]
  JEByDIM5 VarChar(1) Journal Entry by Dimension 5 default=N [Y=Yes, N=No]
  DBReduc Num(19,6) DB Reduction (MB)
  DBReducPer Num(19,6) DB Reduction (%)
  TrandReduc Int(11) Transaction Reduction
  TranReducP Num(19,6) Transaction Reduction (%)
  INZeroPrc VarChar(1) Inventory Zero Price default=N [Y=Yes, N=No]
  TranRedArP Num(19,6) Trans. Reduc. Archived (%)
  DelNonReco VarChar(1) Delete nonreconciled OBNK lns default=N [Y=Yes, N=No]
  RunName nVarChar(50) Data Archive Run Name
  RODBGUID nVarChar(32) Readonly DB GUID for Archiving
  ArchMethod VarChar(1) Archive Method default=F [F=By Financial Period, B=By Business Partner, R=By Retention Time]

# ODCI - Intrastat Configuration
Module: Administration | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CONF_ID: ConfID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Configuration Entry ID
  ConfType VarChar(1) Configuration Type [M=Additional Measurement Unit, C=Commodity Codes, P=Custom Procedures, I=Incoterms, N=Nature of Transactions, E=Ports of Entry and Exit, R=Service Codes, S=Statistical Procedures, T=Transport Modes, G=Regions]
  Code nVarChar(50) Code
  Descr nVarChar(254) Description
  PrcstVal Num(19,6) Percentage Value
  SuppUnit Int(11) Supplementary Unit ->ODCI
  Export VarChar(1) Valid for Export default=Y [Y=Yes, N=No]
  Import VarChar(1) Valid for Import default=Y [Y=Yes, N=No]
  StatCode nVarChar(2) Statistical Code
  DateFrom Date(8) Valid From
  DateTo Date(8) Valid To
  TextVal nVarChar(12) Text Value
  ConfID nVarChar(254) Configuration ID
  TriangDeal nVarChar(2) Triangular Deal Type [11=Acquisitions intra-communautaires, 21=Livraison exon�r�e, 31=Facturations dans le cadre d�op�rations triangulaires]

# ODCR - Checking Rule
Module: Administration | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RuleCode
Fields (name type(len) description [values] ->parent table):
  RuleCode nVarChar(2) Checking Rule Code
  RuleDesc nVarChar(100) Checking Rule Description
  PastRcp VarChar(1) Include Past Plan Receipts default=Y [Y=Yes, N=No]
  AutoATP VarChar(1) ATP Check Automatically default=Y [Y=Yes, N=No]
  SLDUncfm VarChar(1) Schedule for Unconfirmed Qty default=Y [Y=Yes, N=No]
  AllowUncfm VarChar(1) Allow Unconfirmed Quantity default=N [Y=Yes, N=No]
  CmltStrtg VarChar(1) Cumulation Strategy default=R [R=Required Qty on Creation; Confirmed Qty on Change, C=Confirmed Qty on Creation and Change]
  DeliStrtg VarChar(1) Delivery Strategy default=D [D=Delivery Proposal, O=One-Time Delivery, C=Complete Delivery]
  MaxPrpsls Int(11) Max. No. of Proposals default=9
  validFor VarChar(1) Active default=N
  validFrom nVarChar(8) Active From
  validTo nVarChar(8) Active To
  frozenFor VarChar(1) Inactive default=N
  frozenFrom nVarChar(8) Inactive From
  frozenTo nVarChar(8) Inactive To
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]

# ODGP - Document Generation Parameter Sets
Module: Administration | 60 columns | ObjType: 233
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SET_NAME U: SetName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SetName nVarChar(20) Set Name
  SetDesc nVarChar(100) Set Description
  CreateDate Date(8) Creation Date
  ModifyDate Date(8) Last Modified
  UserSign Int(6) User Signature ->OUSR
  Target nVarChar(20) Target Document Type default=-1 [-1=, 17=Sales Order, 15=Delivery, 16=Returns, 13=A/R Invoice]
  PostDate Date(8) Posting Date
  TaxDate Date(8) Document Date
  Series Int(11) Series
  Items VarChar(1) Items Documents Summary default=Y [Y=Yes, N=No]
  ItemSmmry VarChar(1) Items Summary Method default=N [N=No Summary, I=Summary by Items, D=Summary by Documents]
  Service VarChar(1) Service Documents Summary default=N [Y=Yes, N=No]
  ServSmmry VarChar(1) Service Summary Method default=N [N=No Summary, D=Summary by Documents]
  ExchgRate VarChar(1) Exchange Rate default=C [D=Use Base Doc. and Row Rate, B=Use Base Row Rate, C=Use Current Rate]
  CreatDraft VarChar(1) Create Drafts default=N [Y=Yes, N=No]
  BaseQUT VarChar(1) Sales Quotation Summary default=N [Y=Yes, N=No]
  BaseRDR VarChar(1) Order Summary default=N [Y=Yes, N=No]
  BaseDLN VarChar(1) Delivery Summary default=N [Y=Yes, N=No]
  BaseRDN VarChar(1) Returns Summary default=N [Y=Yes, N=No]
  BaseResINV VarChar(1) A/R Reserve Invoice Summary default=N [Y=Yes, N=No]
  ExpndSel VarChar(1) Expanded Selection Criteria default=N [Y=Yes, N=No]
  SortField nVarChar(100) Sort Field default=DocNum [DocNum=Document Number, DocDate=Posting Date, DocDueDate=Due Date, NumAtCard=BP Reference No., DocTotal=Document Amount, SlpCode=Sales Employee]
  Consolidat VarChar(1) Consolidate default=Y [Y=Yes, N=No]
  ExpandCons VarChar(1) Expanded Consolidation Options default=N [Y=Yes, N=No]
  RCNSummary VarChar(1) Reference Document default=N [Y=Yes, N=No]
  ChainCode Int(11) Retail Chain
  OredrNum1 Int(11) Order No. From
  OredrNum2 Int(11) To
  Direct VarChar(1) Direct default=N [Y=Yes, N=No]
  Indirect VarChar(1) Indirect default=N [Y=Yes, N=No]
  DoReport VarChar(1) Overview of Invoice Deliveries default=N [Y=Yes, N=No]
  FileExport VarChar(1) File Export default=N [Y=Yes, N=No]
  SavePath Text(16) File Path
  DealNum nVarChar(12) Closing No.
  UseDirect VarChar(1) Direct/Indirect default=N [Y=Yes, N=No]
  NoItmCode VarChar(1) Drop Item No. Where Cat. No. E default=N [Y=Yes, N=No]
  OnData VarChar(1) Missing Data default=N [N=Skip to Next Document, B=Skip to Next Customer, W=Ask for User Confirmation]
  OnLedger VarChar(1) Bookkeeping Alert default=N [N=Skip to Next Document, B=Skip to Next Customer, W=Ask for User Confirmation]
  OnInvnt VarChar(1) Warehouse Alert default=N [N=Skip to Next Document, B=Skip to Next Customer, W=Ask for User Confirmation]
  Summary nVarChar(250) Summary
  AltItmDocs VarChar(1) Process docsc with alt. items default=Y [Y=Yes, N=No]
  PartDelivr VarChar(1) Partial Delivery default=N [Y=Yes, N=No]
  ConsiderBP VarChar(1) Consider BP default=Y [Y=Yes, N=No]
  ConsiderTy VarChar(1) Consider Type default=Y [Y=Yes, N=No]
  EDocGenTyp VarChar(1) Electr. Doc. Generation Type default=D [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later, D=Use Defaults]
  ESeries Int(6) Electronic Series ->NNM4
  EDocNum nVarChar(20) Electronic Document Number
  ReopOriRdr VarChar(1) Reopen Origin. Order by Return default=N [Y=Yes, N=No]
  ReopManCls VarChar(1) Reop. Man. Closed/Canc. Orders default=N [Y=Yes, N=No]
  SeqCode Int(6) Target Doc. NF Sequence Code
  UseBaseSeq VarChar(1) Use Base Document NF Sequence default=N [Y=Yes, N=No]
  OnSeqCode VarChar(1) Missing NF Sequence default=N [N=Skip to Next Document, T=Use NF Sequence from Step 2]
  BPLId Int(11) Branch ->OBPL
  BlckFrOnly VarChar(1) Block Docs. with Zero Items default=N [Y=Yes, N=No]
  DocSubType nVarChar(2) Document Sub-Type default=-- [--=Bill of Supply, GA=GST Tax Invoice]
  EDocDflt VarChar(1) Apply El. Doc. Defaults default=Y [Y=Yes, N=No]
  EDocMapID Int(11) Electronic Document Format Mapping
  VatDate Date(8) VAT Allocation Date
  BsPrcMode VarChar(1) Base Document Price Mode default=Y [Y=Yes, N=No]

# ODLL - Bar Code Algorithm File
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DllEntry
  NAME U: DllName
Fields (name type(len) description [values] ->parent table):
  DllEntry Int(11) Internal Number
  DllName nVarChar(254) DLL Name
  DllDesp nVarChar(50) DLL Description

# ODMW - Data Migration
Module: Administration | 11 columns | ObjType: 136
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Package Code
  Name nVarChar(20) Package Name
  CategoryId Int(11) Category ID ->OQCN
  DestPath Text(16) Dest. Path
  Extantion nVarChar(5) Exported
  UserSign Int(6) User Signature ->OUSR
  Delim nVarChar(10) Include Title default=T [T=Tab, K=,, D=;, S=Space]
  InclTitle VarChar(1) Set to Exported default=N [Y=Yes, N=No]
  SetExp VarChar(1) New Records default=N [Y=Yes, N=No]
  NewRecs VarChar(1) Save default=N [Y=Yes, N=No]
  Summary Text(16) Summary

# ODOW - Data Ownership - Objects
Module: Administration | 11 columns | ObjType: 207
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Object, SubObject
Fields (name type(len) description [values] ->parent table):
  Object nVarChar(20) The Object Number
  SubObject Int(6) Array Offset default=0
  OwnerField Int(6) Column Number of Owner
  Active VarChar(1) Indication: Does it Work default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  UpdateUser Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AC Int(11) Cache Access Counter default=0
  OwnerCtrl Int(6) The way owner is controlled default=7

# ODOX - Data Ownership - Exceptions
Module: Administration | 10 columns | ObjType: 208
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: QueryId, Object, SubObject, OwnerShpBy
Fields (name type(len) description [values] ->parent table):
  QueryId nVarChar(20) Query ID
  Object nVarChar(20) The Object Number
  SubObject Int(6) Array Offset default=0
  UserSign Int(6) User Signature ->OUSR
  UpdateUser Int(6) Updating User ->OUSR
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AC Int(11) Cache Access Counter default=0
  OwnerShpBy VarChar(1) Defined by Ownership Method default=N [N=Not Specified, R=Ownership By Branch]

# OENC - Encryption Types
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Name
Fields (name type(len) description [values] ->parent table):
  Name nVarChar(100) Name
  CodePage Int(11) Code Page

# OEOY - End-of-Year Transfer
Module: Administration | 124 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CompName
Fields (name type(len) description [values] ->parent table):
  GenrlDefs VarChar(1) General Definitions default=Y [Y=, N=]
  ReFiles VarChar(1) Transfer Template Designer Files default=Y [Y=, N=]
  ActIndex VarChar(1) Transfer Accounts Index default=Y [Y=, N=]
  ActFromCod nVarChar(15) From Code
  ActToCode nVarChar(15) To Code
  ActGroup nVarChar(16) ActGroup default=255
  CrdIndex VarChar(1) Transfer Credit Card Index default=Y [Y=, N=]
  CrdFromCod nVarChar(15) From Code
  CrdToCode nVarChar(15) To Code
  CrdGrpCust Int(6) Customer Group
  CrdGrpVndr Int(6) Vendor Group
  CrdToknAnd VarChar(1) CrdToknAnd
  CrdUseGrps VarChar(1) CrdUseGrps
  CrdClsRang VarChar(1) CrdClsRang
  CrdGrpData nVarChar(64) Properties
  ItmIndex VarChar(1) Transfer Item Index default=Y [Y=, N=]
  ItmFromCod nVarChar(50) From Code
  ItmToCode nVarChar(50) To Code
  ItmGroup Int(6) Item Group
  ItmToknAnd VarChar(1) ItmToknAnd
  ItmUseGrps VarChar(1) ItmUseGrps
  ItmClsRang VarChar(1) ItmClsRang
  ItmGrpData nVarChar(64) Properties
  TransfDoc VarChar(1) Documents Transfer default=N [Y=, N=]
  UnDpsChk VarChar(1) Transfer Undeposited Checks default=N [Y=, N=]
  DpsChk VarChar(1) Transfer Postdated Checks default=N [Y=, N=]
  UnDpsVouch VarChar(1) Transfer Unpaid Vouchers default=N [Y=, N=]
  DpsVouch VarChar(1) Transfer Deffered Vouchers default=N [Y=, N=]
  WorkOrder VarChar(1) Open Work Instructions default=N [Y=, N=]
  RcrTrt VarChar(1) Posting Templates & Rec. Trans default=N [Y=, N=]
  Connection VarChar(1) Activities default=N [Y=, N=]
  SpcPrice VarChar(1) Special Prices default=N [Y=, N=]
  Quotations VarChar(1) Transfer Open Sales Quotations default=N
  Orders VarChar(1) Transfer Open Orders default=N [Y=, N=]
  DlvrNotes VarChar(1) Transfer Open Delivery Notes default=N [Y=, N=]
  DlvrInvocs VarChar(1) Transfer Open Invoices default=N [Y=, N=]
  P_Orders VarChar(1) Transfer Purchase Orders default=N [Y=, N=]
  P_Invoices VarChar(1) A/P Invoices default=N [Y=, N=]
  ProdTree VarChar(1) Product Tree default=N [Y=, N=]
  Subst VarChar(1) Customer/Vendor Catalog No. default=N [Y=, N=]
  Import VarChar(1) Landed Costs default=N [Y=, N=]
  Revert VarChar(1) Returns default=N [Y=, N=]
  ActBlnc VarChar(1) Transfer Account Balances default=N [Y=, N=]
  ActRef1 nVarChar(11) Ref. 1 for Opening Bal. Trans.
  ActRef2 nVarChar(11) Ref. 2 for Opening Bal. Trans.
  ActRefDate Date(8) Posting Date for OB Transactions
  ActDueDate Date(8) Due date for OB transaction
  ActMemo nVarChar(50) Journal Entry Details
  AOpnBlnAct nVarChar(15) Opening Balances Account
  AEquetyAct nVarChar(15) Retained Earnings Account
  ActExpLine VarChar(1) Transfer Split Balances default=N [Y=Unreconciled Internally, N=, E=Unreconciled Externally]
  ActBlncFrC nVarChar(15) From Code
  ActBlncToC nVarChar(15) To Code
  ActBlncGrp nVarChar(16) ActBlncGrp default=YYY
  ActZeroBln VarChar(1) Account Transactions with Zero Balance default=Y [Y=, N=]
  CrdBlnc VarChar(1) Transfer Credit Card Balances default=N [Y=, N=]
  CrdRef1 nVarChar(11) Ref. 1 for OB Transactions
  CrdRef2 nVarChar(11) Ref. 2 for OB Transactions
  CrdRefDate Date(8) Posting Date for OB Transactions
  CrdDueDate Date(8) Due date for OB transaction
  CrdMemo nVarChar(50) Journal Entry Details
  COpnBlnAct nVarChar(15) Opening Balances Account
  CrdExpLine VarChar(1) Transfer Split Balances default=N [Y=, N=]
  CrdBlncFrC nVarChar(15) From Code
  CrdBlncToC nVarChar(15) To Code
  CrdBlncGrC Int(6) Customer Group
  CrdBlnGrpV Int(6) Vendor Group
  CrdBTknAnd VarChar(1) CrdBTknAnd
  CrdBUseGrp VarChar(1) CrdBUseGrp
  CrdBClsRng VarChar(1) CrdBClsRng
  CrdBGrpDat nVarChar(64) Properties
  CrdZeroBln VarChar(1) Card Transactions with Zero Balance default=Y [Y=, N=]
  ItmBlnc VarChar(1) Transfer Item Balances default=N [Y=, N=]
  ItmRef1 nVarChar(11) Ref. 1 for Opening Bal. Trans.
  ItmRef2 nVarChar(11) Ref. 2 for Opening Bal. Trans.
  ItmRefDate Date(8) Posting Date for OB Transaction
  ItmMemo nVarChar(50) Journal Entry Details
  ItmBlncFrC nVarChar(50) From Code
  ItmBlncToC nVarChar(50) To Code
  ItmBlncGrp Int(6) Item Group
  ItmBTknAnd VarChar(1) ItmBTknAnd
  ItmBUseGrp VarChar(1) ItmBUseGrp
  ItmBClsRng VarChar(1) ItmBClsRng
  ItmBGrpDat nVarChar(64) Properties
  ItmPlnNum Int(6) Transaction Price List default=1
  ItmZeroPr VarChar(1) Transfer Items Without Price default=N [Y=, N=]
  FileReport VarChar(1) Create Report File default=Y [Y=, N=]
  CompName nVarChar(100) Company Name for Transfering
  WasGnrlDef VarChar(1) Was general data transferred default=N [Y=, N=]
  P_DlvrNots VarChar(1) Transfer PO Del. Notes default=N [Y=, N=]
  Spg VarChar(1) Transfer Discount for Groups default=N [Y=, N=]
  Pdn VarChar(1) Purchase Delivery Notes default=N [Y=, N=]
  PdnClosed VarChar(1) Closed Purchase Delivery Notes default=N [Y=, N=]
  Rpd VarChar(1) Revert Purchase Delivery Notes default=N [Y=, N=]
  ReportTemp VarChar(1) Report Templates default=N [Y=, N=]
  Confirmat VarChar(1) Confirmation default=N [Y=, N=]
  DocDraft VarChar(1) Document Drafts default=N [Y=, N=]
  ChkOutDrft VarChar(1) Checks for Payment Drafts default=N [Y=, N=]
  OptOpen VarChar(1) Open Opportunities default=N [Y=, N=]
  OptClosed VarChar(1) Closed Opportunities default=N [Y=, N=]
  SerBtchNum VarChar(1) Batch/Serial No. default=N [Y=, N=]
  CorrInvoic VarChar(1) Correction Invoice default=N [Y=, N=]
  UserGign Int(6) User Signature ->OUSR
  PaymDraf VarChar(1) Payment Draft default=N [Y=, N=]
  PaymentWiz VarChar(1) Saved Payment Wizard default=N [N=No, Y=Yes]
  AltItems VarChar(1) Alternative Items default=N [N=No, Y=Yes]
  DPIInvoice VarChar(1) A/R Down Payment Invoice default=N
  DPIRequest VarChar(1) A/R Down Payment Request default=N [Y=Yes, N=No]
  Ctr VarChar(1) Service Contracts default=N [Y=Yes, N=No]
  Ins VarChar(1) Customer Equipment Card default=N [Y=Yes, N=No]
  CorrAPInv VarChar(1) A/P Correction Invoice default=N [Y=Yes, N=No]
  CorrAPRev VarChar(1) A/P Correction Invoice Reversal default=N [Y=Yes, N=No]
  CorrARInv VarChar(1) A/R Correction Invoice default=N [Y=Yes, N=No]
  CorrARRev VarChar(1) A/R Correction Invoice Reversal default=N [Y=Yes, N=No]
  UserObj VarChar(1) User Object default=N [N=No, Y=Yes]
  AdWrkOrdr VarChar(1) Advanced Work Order default=N [Y=Yes, N=No]
  DPOInvoice VarChar(1) A/P Down Payment Invoice default=N [Y=Yes, N=No]
  DPORequest VarChar(1) A/P Down Payment Request default=N [Y=Yes, N=No]
  P_Quotatio VarChar(1) Transfer Open Pur. Quotations default=N [Y=Yes, N=No]
  WTQ VarChar(1) Inventory Transfer Requests default=N [Y=Yes, N=No]
  Oat VarChar(1) Blanket Agreement default=N [Y=Yes, N=No]
  CPN VarChar(1) Campaign default=N [Y=Yes, N=No]
  AdvRules VarChar(1) Transfer Advanced Rules default=N [Y=Yes, N=No]
  Prq VarChar(1) Purchase Request default=N

# OERN - Excise Register Numbering
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NumTypeID
Fields (name type(len) description [values] ->parent table):
  NumTypeID Int(11) ID for numbering type
  NumTypeNam nVarChar(30) Name for numbering type
  FirstNum Int(11) First number default=1
  NextNum Int(11) Next Number default=1
  LastNum Int(11) Last Number
  UserSign Int(6) User Signature ->OUSR
  ResetDate Date(8) Date of last reset

# OERT - Excise Register Numbering Type
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NumTypeId
  TYPE_NAME U: NumTypeNam
Fields (name type(len) description [values] ->parent table):
  NumTypeId Int(11) Numbering Type ID
  NumTypeNam nVarChar(30) Numbering Type Name
  FirstNum Int(11) First Number
  NextNum Int(11) Next Number
  LastNum Int(11) Last Number

# OERX - Excise Register Numbering Ext
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ErnId
  LOC_KEY U: Location
Fields (name type(len) description [values] ->parent table):
  ErnId Int(11) Excise Register Numbering ID
  Location Int(11) Loc. ->OLCT
  UserSign Int(6) User Signature ->OUSR

# OEXD - Freight Setup
Module: Administration | 40 columns | ObjType: 125
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ExpnsCode
  NAME U: ExpnsName
Fields (name type(len) description [values] ->parent table):
  ExpnsCode Int(11) Internal Number
  ExpnsName nVarChar(20) Name
  RevAcct nVarChar(15) Revenue Account ->OACT
  ExpnsAcct nVarChar(15) Expense Account ->OACT
  TaxLiable VarChar(1) Tax Liable default=N [Y=Yes, N=No]
  RevFixSum Num(19,6) Fixed Amount - Revenues
  ExpFixSum Num(19,6) Fixed Amount - Expenses
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  VatGroupI nVarChar(8) Output Tax Group ->OVTG
  VatGroupO nVarChar(8) Input Tax Group ->OVTG
  DistrbMthd VarChar(1) Distribution Method default=N [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  In1099 VarChar(1) Include in 1099 default=N [Y=Yes, N=No]
  ExpOfstAct nVarChar(15) Freight Clearing Account ->OACT
  WTLiable VarChar(1) WTax Liable default=N [Y=Yes, N=No]
  BaseMethod VarChar(1) Drawing Method default=T [N=None, Q=Quantity, T=Total, A=All]
  Stock VarChar(1) Stock default=N [Y=Yes, N=No]
  LstPchPrce VarChar(1) Last Purchase Price default=N [Y=Yes, N=No]
  SalseRpt VarChar(1) Sales Analysis Report default=N [Y=Yes, N=No]
  PchRpt VarChar(1) Purchase Analysis Report default=N [Y=Yes, N=No]
  RevExmAcct nVarChar(15) Revenues Exempted Account ->OACT
  ExpnsExAct nVarChar(15) Expense Exempted Account ->OACT
  RevRetAct nVarChar(15) Revenue Returns Account
  ExpnsType VarChar(1) Freight Type default=1 [1=Shipping, 2=Insurance, 3=Other, 4=Special]
  OcrCode nVarChar(8) Distr. Rule ->OOCR
  TaxDisMthd VarChar(1) Tax Distribution Method default=N [N=None, Q=Quantity, V=Volume, W=Weight, E=Equally, T=Row Total]
  OcrCode2 nVarChar(8) Distr. Rule2 ->OOCR
  OcrCode3 nVarChar(8) Distr. Rule3 ->OOCR
  OcrCode4 nVarChar(8) Distr. Rule4 ->OOCR
  OcrCode5 nVarChar(8) Distr. Rule5 ->OOCR
  OcrCodeX nVarChar(100) Distr. Rule ->OOCR
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  UserSign2 Int(6) Updating User ->OUSR
  Project nVarChar(20) Project ->OPRJ
  Intrastat VarChar(1) Intrastat Relevant default=N [Y=Yes, N=No]
  GrsFreight VarChar(1) Gross Freight default=N [Y=Yes, N=No]
  SacCode nVarChar(8) SAC Code
  FreighType VarChar(1) Freight Type default=S [S=Standard, B=Bollo]
  DataVers Int(11) Data Version default=1

# OFML - Tax Formula Master Table
Module: Administration | 10 columns | ObjType: 276
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: FmlType, Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(20) Code
  Descr nVarChar(100) Description
  SttId Int(11) Tax Type ID ->OSTT
  FmlLang Text(16) Formula Language Free Text
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  FmlType VarChar(1) Formula Type default=T [T=Tax, W=WTax]
  IsOrigFml VarChar(1) Original/Edited Formula default=Y [Y=Yes, N=No]

# OFRM - File Format
Module: Administration | 10 columns | ObjType: 183
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME_TYPE: Name, FrmatType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) File Format Name
  Encoding nVarChar(100) Encoding Type
  FilePath Text(16) Format Project
  IsSystem VarChar(1) System Format default=N [Y=Yes, N=No]
  FrmatType VarChar(1) Format Type default=O [I=Bank Statements, O=Payment File, L=Legal List, P=Predefined, B=Boleto File, R=Padron File]
  FileContnt Text(16) Format Project Content
  FrmatStats VarChar(1) Format Status default=U [A=Assigned, U=Unassigned]
  PaymType VarChar(1) Payment Type default=X [O=Outgoing, I=Incoming, X=]
  Hash nVarChar(128) Binary Content Hash

# OFTT - Financial Template Import
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FilePath nVarChar(254) For the Data Definition File

# OGFL - Grid Filter
Module: Administration | 5 columns | ObjType: 222
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormID, GridID, UserCode
Fields (name type(len) description [values] ->parent table):
  FormID nVarChar(20) Form ID
  GridID nVarChar(11) Grid ID
  UserCode Int(6) User Code
  DefFilter Int(11) Default Filter
  NextFltID Int(11) Next Filter ID default=1

# OGPC - Government Payment Code
Module: Administration | 6 columns | ObjType: 243000001
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(6) Code
  Descr nVarChar(100) Description
  StateTax VarChar(1) Reporting by State default=N [Y=Yes, N=No]
  Prdcity VarChar(1) Periodicity default=M [M=Monthly, Q=Quarterly, H=Semimonthly, T=Every 10 Days]
  SPEDCtgory Int(11) SPED Category [1=ICMS, 2=ICMS-ST, 3=IPI, 4=ISS, 5=PIS, 6=COFINS, 7=PIS-ST, 8=COFINS-ST]

# OGSP - Goods Shipment
Module: Administration | 3 columns | ObjType: 139
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code VarChar(1) Code
  Name nVarChar(50) Name
  UserSign Int(6) User Signature ->OUSR

# OICMS - Unencumbered ICMS Exemption Reason
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) ICMS Internal Key
  CstSuffix nVarChar(2) CST Suffix for ICMS
  MotDes Int(11) motDesICMS default=0
  Descrip Text(16) Description

# OIDX - CPI Codes
Module: Administration | 5 columns | ObjType: 38
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IdexCode
Fields (name type(len) description [values] ->parent table):
  IdexCode nVarChar(3) Code
  IndexName nVarChar(50) Name
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OIND - Triangular Deal
Module: Administration | 3 columns | ObjType: 135
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code VarChar(1) Code
  Name nVarChar(50) Name
  UserSign Int(6) User Signature ->OUSR

# OJPE - Local Era Calendar
Module: Administration | 3 columns | ObjType: 250
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code VarChar(1) Local Era Code
  EraName nVarChar(20) Local Era Name
  StartDate Date(8) Start Date

# OLLF - Legal List Format
Module: Administration | 15 columns | ObjType: 410000005
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) Electronic File Name
  Descr nVarChar(250) Electronic File Description
  MenuGuid nVarChar(32) GUID of Menu Entry
  Version nVarChar(5) Electronic File Version
  SchVersion nVarChar(5) Electronic File Schema Version
  OutPath Text(16) Output Path
  FrmId Int(11) OFRM Internal ID ->OFRM
  UpdateNum Int(11) Update Count default=0
  MenuName nVarChar(100) Menu Name
  MenuPath nVarChar(250) Menu Path
  Assigned nVarChar(10) Format Status default=N [A=Assigned, N=Not Assigned, D=Deleted]
  SboVersion nVarChar(13) Compatible Release Version
  Type nVarChar(5) Format Type default=L [AR=Electronic Document, L=Generic Electronic File, LI=Generic Electronic File for Intrastat, ARA=Electronic Authority Report, INTER=Internally Used, IM=Electronic Document - Input Message, GD=General Electronic Document, GWS=General Mapping for Web Service, GI=General Mapping for Document Import, NFeD=NF-e Invoice Document, NFeC=NF-e Cancelation Document, NFeS=NF-e Number Skipping Request, NFeWS=Web Service Mapping, CFDD=CFDi Electronic Document, CFDP=CFDi Electronic Payment & Reconciliation Document, CFDT=CFDI Electronic Transfer Document, CFDIM=CFDI Electronic Input Message Document, CFDWS=CFDi Electronic Mapping for Web Service, EETD=EET Electronic Document, EETWS=EET Electronic Mapping for Web Service, FPAD=FatturaPA Electronic Document, FPAPD="FatturaPA" Electronic Purchasing Document, FPAI=FatturaPA Electronic Document for Import, FPAWS=FatturaPA Electronic Mapping for Web Service, MTDR=Making Tax Digital Report Submission, MTDWS=Making Tax Digital Mapping for Web Service, EISD=Electronic Document, EISWS=Electronic Document Web Service, IISD1=Electronic Document for IIS INV, IISD2=Electronic Document for IIS PCH, IISD3=Electronic Document for IIS Deferred, IISD4=Electronic Document for IIS JE, IISD5=Electronic Document for IIS JE Received, IISWS=Electronic Document for IIS Web Service, ANND1=Electronic Document for IIS Annual, ANND2=Electronic Document for IIS Annual Cancel, ANNWS=Electronic Document for IIS Annual Web Service, PPLD=Electronic Document for PEPPOL Invoice, PPLWS=Electronic Document for PEPPOL Web Service, PPLCM=Electronic Document for PEPPOL Credit Note, PPLI=Electronic Document for PEPPOL Import, EBKD=Electronic Document for E-Books, EBKI=Electronic Document for E-Books Income Classification, EBKE=Electronic Document for E-Books Expense Classification, EBKR=Electronic Document for E-Books Request Documents, EBKRS=Electronic Document for E-Books Request Submitted Documents, EBKC=Electronic Document for Cancellation, EBKW=Electronic Document for E-Books Web Service, DOXD=Electronic Document for Document Information Extraction, DOXI=Electronic Document for Document Information Extraction Import, EWBD=Electronic Document for E-Way Bill, EINVD=Electronic Document for E-Billing, RTIED=Electronic Document for RTIE, RCTED=Electronic Correction Document for RTIE, RTIWS=Electronic Document for RTIE Web Service]
  SubType nVarChar(6) Format Subtype [=None, I=Intrastat, N=Normal Generic File Format]

# OLNG - User Language Table
Module: Administration | 7 columns | ObjType: 223
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  SHORT_NAME U: ShortName
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  ShortName nVarChar(3) Language Short Name
  Name nVarChar(30) Language
  SysLang Int(11) Related System Language
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OLTB - Location-based Tax Bal Table
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  index: LocCode, STAType, STACode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  LocCode Int(11) Location Code ->OLCT
  STAType Int(11) Tax Type ->OSTT
  STACode nVarChar(8) STA Code ->OSTA
  BalaType VarChar(1) Balance Type [P=, R=, C=, F=]
  Balance Num(19,6) Balance

# OLTF - Legal Text Format
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Format ID
  FormatName nVarChar(100) Legal Text Format Name

# OMAO - Mobile Add-On Setting
Module: Administration | 13 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  Name nVarChar(200) Name
  URL Text(16) Entry URL
  Type VarChar(1) Type default=M [M=Module, H=Home]
  Provider nVarChar(200) Provider
  ViewStyle VarChar(1) View Style default=P [P=Page - Universal, F=Full Screen - iPad, L=Landscape only - iPad]
  LogonMethd VarChar(1) Logon Method default=B [B=B1i Framework, S=Standard Logon, N=No Control]
  LogonPyld nVarChar(254) Logon Payload default=user={value1}&pwd={value2}
  Enable VarChar(1) Enable default=Y [Y=Yes, N=No]
  System VarChar(1) System default=N [N=No, Y=Yes]
  B1MobileAp VarChar(1) SAP Business One default=N [Y=Yes, N=No]
  B1SalesApp VarChar(1) SAP Business One Sales default=N [Y=Yes, N=No]
  B1SrvcApp VarChar(1) SAP Business One Service default=N [Y=Yes, N=No]

# OMAP - Mapping Elements
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FrmId Int(11) Format Object ID ->OFRM
  MapId Int(11) Mapping ID in Format

# OMDC - Master Data Cleanup
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  Name nVarChar(100) Master Data Cleanup Name
  CreateDate Date(8) Create Date
  UserSign Int(6) User Signature ->OUSR
  Status VarChar(1) Status [S=Saved, E=Executed]
  UpdUser nVarChar(30) Last Update User

# OMLS - Distribution List
Module: Administration | 4 columns | ObjType: 87
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(30) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OMLT - Multi-Language Translation
Module: Administration | 6 columns | ObjType: 224
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TranEntry
  Second U: TableName, FieldAlias, PK
Fields (name type(len) description [values] ->parent table):
  TranEntry Int(11) Internal Number
  TableName nVarChar(20) Table Name
  FieldAlias nVarChar(50) Field Alias
  PK nVarChar(254) Primary Key of Object
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OMPF - Message Preferences
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: MessageUid, FormUid, UserSign
Fields (name type(len) description [values] ->parent table):
  MessageUid Int(11) Message UID
  FormUid Int(11) Form UID
  UserSign Int(6) User Signature ->OUSR
  SelctedBtn Int(11) Selected Button

# OMPO - Value Mapping Object
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  B1_VALUE U: ObjectId, ObAbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectId Int(11) Object ID
  ObAbsEntry nVarChar(100) Object Internal Number

# OMPS - Map Services
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(20) Name
  QueryUrl Text(16) Query URL

# OMSG - Messaging Service Settings
Module: Administration | 4 columns | ObjType: 10000105
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USERID
Fields (name type(len) description [values] ->parent table):
  USERID Int(6) User Signature default=-1
  Signature Text(16) E-Mail signature
  UseCompSig VarChar(1) Use Company Signature default=N [Y=Yes, N=No]
  DummySig Text(16) Dummy Signature

# OMTP - Material Type
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Numerator
  MatType nVarChar(50) Material Type
  Descrip nVarChar(100) Description

# ONCG - State Groups
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Group No.
  GroupName nVarChar(20) Group Name
  UserSign Int(6) User Signature ->OUSR

# ONCM - NCM Code
Module: Administration | 8 columns | ObjType: 257
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: NcmCode, GroupCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  NcmCode nVarChar(15) NCM Code
  Descrip nVarChar(254) Description
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  GroupCode VarChar(1) Group Code default=L
  Group Int(6) NCM Group ->ONCG

# ONFN - Nota Fiscal Numbering
Module: Administration | 6 columns | ObjType: 263
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  AutoKey Int(11) Automatic Key default=0
  DfltSeq Int(6) Default Sequence default=0
  UpdCounter Int(6) Update Counter default=0
  UserSign Int(6) User Signature ->OUSR
  DocSubType nVarChar(2) Document Sub-Type default=-- [--=, GA=GST Tax Invoice, GD=GST Debit Memo, RV=Refund Voucher]

# ONFT - Nota Fiscal Tax Category (Brazil)
Module: Administration | 5 columns | ObjType: 264
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(20) Tax Category
  Locked VarChar(1) Locked default=N [N=, Y=]
  GPCId Int(11) Government Payment Code default=-1 ->OGPC
  CESTrel VarChar(1) CEST Relevant default=N [Y=, N=]

# ONNM - Document Numbering
Module: Administration | 9 columns | ObjType: 35
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ObjectCode, DocSubType
Fields (name type(len) description [values] ->parent table):
  ObjectCode nVarChar(20) Document
  AutoKey Int(11) Automatic Key default=0
  DfltSeries Int(11) Default Series default=0
  UpdCounter Int(11) Update Counter default=0
  UserSign Int(6) User Signature ->OUSR
  DocSubType nVarChar(2) Document Sub-Type default=-- [--=, IE=Invoice Exempt, DN=Debit Memo, IB=Bill, EB=Exempt Bill, RI=Reserve Invoice, IR=Invoice & Receipt, DM=A/P Debit Memo, IX=Export Invoice, RP=A/P Reserve Invoice, OV=Outgoing VAT - Withholding Tax, OG=Outgoing Gross Income - Withholding Tax, ON=Outgoing Income - Withholding Tax, OS=Outgoing Social Security - Withholding Tax, OI=Outgoing Industry Specific - Withholding Tax, OD=Outgoing District Specific - Withholding Tax, IC=Incoming WTax Certificate, GA=GST Tax Invoice, GD=GST Debit Memo, RV=Refund Voucher]
  DocAlias nVarChar(20) Alternative Document Name
  PeriodTyp VarChar(1) Seq. Period Type of Supply Code
  logInstanc Int(11) Log Instance - History

# ONOA - Nature of Assessee
Module: Administration | 4 columns | ObjType: 10000077
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(4) Code
  Descr nVarChar(100) Description
  AsseType VarChar(1) Assessee Type default=C [C=Company, P=Others]

# OOCC - BoE Occurrence Code
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: Code, IsMovement
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(10) Code
  Dscription nVarChar(128) Description
  Note nVarChar(50) Note
  ReqBoeSt VarChar(1) Requested BoE Status [G=Generated, S=Sent, D=Deposited, P=Paid, C=Canceled, F=Failed]
  IsMovement VarChar(1) Is Movement default=N [Y=Yes, N=No]

# OPCI - Process Checklist Instance
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: InstancePk
Fields (name type(len) description [values] ->parent table):
  InstancePk Int(11) Instance Primary Key
  TemplateFk Int(11) Template Foreign Key ->OPCT
  InstName nVarChar(100) Instance Name
  InstDesc nVarChar(100) Instance Description
  Creator nVarChar(100) Instance Creator
  Status VarChar(1) Instance Status default=N [N=New, P=In Process, F=Finished]
  StartDate Date(8) Start Date
  CloseDate Date(8) Close Date
  CloPrcnt Num(19,6) Closing Percentage
  Memo Text(16) Remarks
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry

# OPCT - Process Checklist Template
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  TMPLCODE U: TmplCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  TmplCode nVarChar(15) Template Primary Key
  TmplName nVarChar(100) Template Name
  XMLFile Text(16) XML File Contents

# OPFS - Personal Fields Setup
Module: Administration | 16 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: TableName, FieldName, Category
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  TableName nVarChar(20) Data Subtype
  FieldName nVarChar(50) Field Name
  RefObjType nVarChar(20) Data Type
  Category VarChar(1) Category default=N [N=, R=Sales A/R, P=Purchase A/P, Q=Purchase Request, A=Inventory Transfers and Requests Sales A/R, B=Inventory Transfers and Requests Purchase A/P, C=Opportunity - Business Partner, D=Opportunity - Business Partner Channel, E=Customer Equipment Card - Business Partner, F=Customer Equipment Card - Direct Partner, L=Landed Cost - Vendor, G=Landed Cost - Broker, X=Payment Results - Business Partner, U=Payment Results - User, H=Incoming Payments, I=Outgoing Payments, J=Sales A/R, K=Purchase A/P, M=Bill of Exchange for Incoming Payments]
  OrigType VarChar(1) Default Data Classification default=U [U=User Defined, S=Sensitive Personal, P=Personal, N=Not Personal]
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Create Time - Incl. Secs
  UpdateDate Date(8) Date of Update
  UpdateTS Int(11) Update Full Time
  LogInstanc Int(11) Log Instance default=0
  Type VarChar(1) Data Classification default=N [N=Not Personal, S=Sensitive Personal, P=Personal]
  Descr nVarChar(254) Description
  MaxType VarChar(1) Max. Data Classification default=U [U=User Defined, S=Sensitive Personal, P=Personal]

# OPID - Period Indicator
Module: Administration | 1 columns | ObjType: 184
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Indicator
Fields (name type(len) description [values] ->parent table):
  Indicator nVarChar(10) Period Indicator

# OPJT - Project Plan
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
  NAME: TempName
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  TempType VarChar(1) Template Type default=N [S=System Template, N=Nonsystem Template]
  TempName nVarChar(254) Template Name
  LogInstanc Int(11) Log Instance
  UserSign Int(11) User Signature ->OUSR
  UserSign2 Int(11) Updating User ->OUSR
  CreateDate Date(8) Production Date
  UpdateDate Date(8) Date of Update
  TempDesc nVarChar(254) Template Description

# OPOS - POS Master Data
Module: Administration | 5 columns | ObjType: 541
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: EquipNo
Fields (name type(len) description [values] ->parent table):
  EquipNo nVarChar(20) Equipment No.
  Model nVarChar(20) Model
  ManufSN nVarChar(21) Manufacturer Serial No.
  RegNo Int(6) Register No.
  NFModel nVarChar(6) Fiscal Document Model ->ONFM

# OPPA - Password Administration
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal ID default=1
  SecLevel nVarChar(20) Security Level default=Low [Low=Low, Medium=Medium, High=High, Custom=Custom]
  PwdExp Int(11) Password Expiration default=90
  PwdMinLen Int(11) Password Minimum Length default=4
  MinUppers Int(11) Password Min. Uppercase Chars. default=0
  MinLowCase Int(11) Password Min. Lowercase Chars. default=0
  MinDigits Int(11) Password Minimum Digits default=0
  MinNonAlph Int(11) Password Min. Non-alphanumeric Char. default=0
  NumPrevPwd Int(11) Pwd does not match pwd rules default=0
  NumAuthLoc Int(11) No. of Authentications Before Acct is Locked default=100
  PwdExample nVarChar(10) Password Example default=abcd

# OPQW - Purchase Quotation Generation: Parameter Sets
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SET_NAME U: SetName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SetName nVarChar(20) Set Name
  SetDesc nVarChar(100) Set Description
  CreateDate Date(8) Creation Date
  ModifyDate Date(8) Last Modified Date
  UserSign Int(6) User Signature ->OUSR
  CreatDraft VarChar(1) Create Drafts default=N [Y=Yes, N=No]
  GroupBy VarChar(1) Group By default=B [B=Business Partner, I=Item]
  ValidUntil Date(8) Valid Until Date
  BPLId Int(11) Branch ->OBPL
  ReqDate Date(8) Required Date
  BaseOn VarChar(1) Base On Type

# OPRF - Preferences
Module: Administration | 17 columns | ObjType: 41
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormNumber, UserSign
Fields (name type(len) description [values] ->parent table):
  FormNumber Int(11) User Form No.
  ExPref1 nVarChar(254) Ex preferences 1
  ExPref2 nVarChar(254) Ex preferences 2
  ExPref3 nVarChar(254) Ex preferences 3
  ExPref4 nVarChar(254) Ex preferences 4
  ExPref5 nVarChar(254) Ex preferences 5
  ExPref6 nVarChar(254) Ex preferences 6
  ExPref7 nVarChar(254) Ex preferences 7
  ExPref8 nVarChar(254) Ex preferences 8
  ExPref9 nVarChar(254) Ex preferences 9
  ExPref10 nVarChar(254) Ex preferences 10
  ExPref11 nVarChar(254) Ex preferences 11
  ExPref12 nVarChar(254) Ex preferences 12
  ExPref13 nVarChar(254) Ex preferences 13
  ExPref14 nVarChar(254) Ex preferences 14
  ExPref15 nVarChar(254) Ex preferences 15
  UserSign Int(6) User Signature ->OUSR

# OPRO - Property Object
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE_NAME U: MapID, Code, Name
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Property ID
  MapID Int(11) Mapping ID ->OMAP
  Code Int(11) Input/Output Code
  Type nVarChar(6) Property Type default=Strin [Strin=String, XML=XML, String=]
  Name nVarChar(50) Property Name
  IsBlob VarChar(1) Is BLOB Type [Y=, N=]
  TValue nVarChar(250) Text Value
  BValue Text(16) BLOB Value
  Encoding nVarChar(20) Encoding [base64=]

# OPSG - Product Source Code Groups
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Group No.
  GroupName nVarChar(20) Group Name
  UserSign Int(6) User Signature ->OUSR

# OPVL - Lender - Pelecard
Module: Administration | 5 columns | ObjType: 115
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  CONSOL_NUM U: ConsolNum
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Number
  Name nVarChar(50) Name
  ConsolNum nVarChar(2) Vendor Code
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OQFD - Query Fields
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IntrnalKey
  ALIAS U: QryCode, CategoryID
Fields (name type(len) description [values] ->parent table):
  IntrnalKey Int(11) Internal Key
  QryCode nVarChar(254) Query Code
  CategoryID Int(11) Category ID
  BaseCode nVarChar(254) Base Code

# OQRC - QR Code
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: SrcObjType, SrcObjAbs, FieldName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  FileContnt Text(16) QR Code Image Content
  SrcObjType Int(11) Source Object Type
  SrcObjAbs nVarChar(20) Source Object Internal ID
  FieldName nVarChar(50) Field Name
  ExpAfter Int(6) Expire after defined days
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time - Incl. Secs
  UpdateDate Date(8) Update Date
  UpdateTS Int(11) Update Time - Incl. Secs

# ORIT - Dunning Interest Rate
Module: Administration | 5 columns | ObjType: 149
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Interest Code
  Name nVarChar(50) Interest Name
  IncPartPay VarChar(1) Include Partially Paid Inv. default=Y [Y=Yes, N=No]
  DayInMonth Int(11) Number of Days in Month
  OrigRate VarChar(1) Use Original Exchange Rate default=Y [Y=Yes, N=No]

# ORLD - Reference Links Definition
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  OBJ_FIELD U: ObjectCode, DocSubType
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectCode nVarChar(20) Document
  DocSubType nVarChar(2) Document Subtype default=-- [--=, IE=Invoice Exempt, DN=Debit Memo, IB=Bill, EB=Exempt Bill, DM=A/P Debit Memo, IX=Export Invoice, GA=GST Tax Invoice, GD=GST Debit Memo]
  Status VarChar(1) Status default=O [O=Original, C=Customized]

# ORLS - Reference Links Sources
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Name nVarChar(100) Name

# ORMK - Remark 1
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  Code U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code VarChar(1) Code
  Particular Text(16) Particulars

# ORST - Route Stages
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  SECONDARY U: Code
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  Code nVarChar(50) Code
  Desc nVarChar(100) Description
  UserSign Int(6) User Signature
  UserSign2 Int(6) Updating User
  CreateDate Date(8) Creation Date
  CreateTime Int(6) Generation Time
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0

# OSEC - Sections
Module: Administration | 4 columns | ObjType: 10000074
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
  ECODE U: eCode
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(15) Code
  Descr nVarChar(30) Description
  eCode nVarChar(3) eCode

# OSHP - Shipping Types
Module: Administration | 6 columns | ObjType: 49
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrnspCode
  NAME U: TrnspName
Fields (name type(len) description [values] ->parent table):
  TrnspCode Int(6) Code
  TrnspName nVarChar(40) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  WebSite nVarChar(50) Web Site
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# OSRL - Serial Numbers
Module: Administration | 5 columns | ObjType: 47
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ItemCode, SerialNum
  INV_NUM: DocNum, ItemCode
  CARD_KEY: CardCode
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  SerialNum nVarChar(17) Serial Number
  CardCode nVarChar(15) Customer Code ->OCRD
  DocNum Int(11) Invoice Number
  UserSign Int(6) User Signature ->OUSR

# OSSP - Service Supply
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code VarChar(1) Code
  Name nVarChar(50) Name
  UserSign Int(6) User Signature ->OUSR

# OSTA - Sales Tax Authorities
Module: Administration | 36 columns | ObjType: 126
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, Type
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(100) Name
  Rate Num(19,6) Rate
  SalesTax nVarChar(15) Sales Tax Account ->OACT
  UseTax nVarChar(15) Use Tax Account ->OACT
  Type Int(11) Type ->OSTT
  UserSign Int(6) User Signature ->OUSR
  PurchTax nVarChar(15) Purchasing Tax Account ->OACT
  deferrAcct nVarChar(15) Deferred Tax Account ->OACT
  NonDdctPrc Num(19,6) Non Deductible %
  NonDdctAct nVarChar(15) Non Deductible Account ->OACT
  TaxInPrice VarChar(1) Included in Price default=N [Y=Yes, N=No]
  Exempt VarChar(1) Exempt default=N [Y=Yes, N=No]
  APExpAct nVarChar(15) Purchasing Tax Expense Account ->OACT
  ARExpAct nVarChar(15) Sales Tax Expense Account ->OACT
  CredBala Num(19,6) Credit Balance: Raw Material
  CredFG Num(19,6) Credit for Finished Goods
  CredCG Num(19,6) Credit for Capital Goods
  InGrossRev VarChar(1) Included in Gross Revenue default=N [Y=Yes, N=No]
  EfctDate Date(8) Effective From
  SvcTaxCr Num(19,6) Credit for Service Tax
  MinAmount Num(19,6) Min. Taxable Amount
  MaxAmount Num(19,6) Max. Taxable Amount
  FlatAmount Num(19,6) Flat Tax Amount
  TextCode Int(6) Text Code
  UnencumTax VarChar(1) Unencumbered Tax default=N [Y=Yes, N=No]
  TaxOnRI VarChar(1) Tax On Reserve Invoice default=N [Y=Yes, N=No]
  DIOTRptTyp VarChar(1) DIOT Report Type [A=15% or 16% VAT, B=15% or 16% VAT on Import, C=Exempt on Import, D=0% VAT, E=Exempt, F=VAT on Returns, Discounts, and Rebates, G=Stimulus for Northern Border Region]
  IsSystem VarChar(1) Is System Tax Jurisdiction default=N [Y=Yes, N=No]
  RvsCrgPrc Num(19,6) Reverse Charge %
  InFirstIns VarChar(1) Included in First Installment default=N [Y=Yes, N=No]
  SaleTaxRCM nVarChar(15) Sales Tax RCM Account ->OACT
  SaleRCMClr nVarChar(15) Sales Tax RCM Clearing Account ->OACT
  VatExempt VarChar(1) Apply VAT Exemption default=N [Y=Yes, N=No]
  VatExmPrc Num(19,6) VAT Exemption %
  VatExmBase Num(19,6) Base VAT %

# OSTC - Sales Tax Codes
Module: Administration | 21 columns | ObjType: 128
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(100) Name
  Rate Num(19,6) Rate
  Freight VarChar(1) Freight default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  ValidForAR VarChar(1) Valid for A/R default=Y [Y=Yes, N=No]
  ValidForAP VarChar(1) Valid for A/P default=Y [Y=Yes, N=No]
  TfcId Int(11) Formula Combination ID ->OTFC
  Lock VarChar(1) Inactive default=N [Y=Yes, N=No]
  TaxIcms nVarChar(2) Taxation For ICMS
  IsItmLevel VarChar(1) Single Item Level Tax default=N [Y=Yes, N=No]
  CfopIn nVarChar(6) CFOP Incoming Code ->OCFP
  CfopOut nVarChar(6) CFOP Outgoing Code ->OCFP
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  FADebit VarChar(1) FA Debit default=N [Y=Yes, N=No]
  IsSystem VarChar(1) Is System Tax Code default=N [Y=Yes, N=No]
  VatExempt VarChar(1) Apply VAT Exemption default=N [Y=Yes, N=No]
  HashInpNm nVarChar(100) Hash Input Name
  CheckDate Date(8) Check Date

# OSTG - State Groups
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Group No.
  GroupName nVarChar(20) Group Name
  UserSign Int(6) User Signature ->OUSR

# OSTT - Sales Tax Authorities Type
Module: Administration | 12 columns | ObjType: 127
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  Name nVarChar(40) Type Name
  UserSign Int(6) User Signature ->OUSR
  IsVat VarChar(1) VAT default=N [Y=Yes, N=No]
  NfTaxId Int(11) ID of Nota Fiscal Tax Category ->ONFT
  TpsId Int(11) ID of Tax Parameter Set ->OTPS
  PLABalance Num(19,6) PLA Current Balance
  Locked VarChar(1) Locked default=N
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  CreditCtrl VarChar(1) Tax Credit Control default=N [Y=Yes, N=No]

# OSUC - Single User Setup
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: StpCode
Fields (name type(len) description [values] ->parent table):
  StpCode Int(6) Setup Code
  StpDes nVarChar(100) Setup Description
  Action VarChar(1) Action default=B [B=Block Update, W=Warning]
  LogInstanc Int(11) Log Instance default=0
  UpdateDate Date(8) Date of Update
  CreateDate Date(8) Creation Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR

# OSUL - Support User Login Record
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Main ID
  RealName nVarChar(100) Real Name
  LogReason nVarChar(100) Login Reason [A=Transaction Issue Analysis, B=Setup Issue Analysis, C=Data Issue Analysis, D=Add-on Issue Analysis, E=Customer Usage Assistance, F=System Maintenance, G=Consulting, H=Other, I=Add-on Access, J=Root Cause Analysis, K=Consulting / Support]
  LogDetail Text(16) Login Detail Information
  Mac nVarChar(100) MAC Address
  Machine nVarChar(100) Machine Name
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  EndDate Date(8) End Date
  EndTime Int(11) End Time
  ChkHash Text(16) Checked Hash Value

# OSUS - Support Usage Statistics
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Identity(11) Internal Number
  SessionID Int(11) Session ID
  Type Int(11) Type
  ID nVarChar(254) ID
  Param nVarChar(254) Param.
  TimeStamp Date(8) Time Stamp

# OSVM - Systems for Value Mapping
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SysType VarChar(1) System Type default=C [C=Concur]
  SysDsc nVarChar(50) System Description

# OTCD - Tax Code Determination
Module: Administration | 4 columns | ObjType: 266
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD_TYPE U: TcdType
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  TcdType nVarChar(2) Determination Type default=MI [MI=Material Item, SI=Service Item, SD=Service Document, WT=Withholding Tax]
  DftArCode nVarChar(8) Default Sales Tax Code
  DftApCode nVarChar(8) Default Purchase Tax Code

# OTCX - Tax Code Determination
Module: Administration | 42 columns | ObjType: 540000005
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Document ID
  LineNum Int(11) Row Number
  DocType Int(11) Document Type [0=Item, 1=Service, 2=Item & Service]
  BusArea Int(11) Business Area [0=Sales, 1=Purchase, 2=Sales & Purchase]
  Cond1 Int(11) Condition 1 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UDFTable1 nVarChar(20) UDF Table Name
  NumVal1 Int(11) Numeric Value
  StrVal1 nVarChar(100) String Value
  MnyVal1 Num(19,6) Monetary Value
  Cond2 Int(11) Condition 2 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UDFTable2 nVarChar(20) UDF Table Name
  NumVal2 Int(11) Numeric Value
  StrVal2 nVarChar(100) String Value
  MnyVal2 Num(19,6) Monetary Value
  Cond3 Int(11) Condition 3 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UdfTable3 nVarChar(20) UDF Table Name
  NumVal3 Int(11) Numeric Value
  StrVal3 nVarChar(100) String Value
  MnyVal3 Num(19,6) Monetary Value
  Cond4 Int(11) Condition 4 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UdfTable4 nVarChar(20) UDF Table Name
  NumVal4 Int(11) Numeric Value
  StrVal4 nVarChar(100) String Value
  MnyVal4 Num(19,6) Monetary Value
  Cond5 Int(11) Condition 5 [0=, 1=Federal Tax ID, 2=Ship-To Address, 3=Ship-To Street / PO Box, 4=Ship-To City, 5=Ship-To ZIP Code, 6=Ship-To County, 7=Ship-To State, 8=Ship-to Country/Region, 9=Item, 10=Item Group, 11=Business Partner, 12=Customer Group, 13=Vendor Group, 14=Warehouse, 15=G/L Account, 16=Customer Equalization tax, 17=Tax Status, 18=Freight, 19=UDF, 20=Branch, 21=Type of Business]
  UdfTable5 nVarChar(20) UDF Table Name
  NumVal5 Int(11) Numeric Value
  StrVal5 nVarChar(100) String Value
  MnyVal5 Num(19,6) Monetary Value
  Descr nVarChar(250) Description
  LnTaxCode nVarChar(8) Line Tax Code
  FrLnTax nVarChar(8) Line Freight Tax
  FrHdrTax nVarChar(8) Header Freight Tax
  UDFAlias1 nVarChar(18) UDF Field Alias
  UDFAlias2 nVarChar(18) UDF Field Alias
  UDFAlias3 nVarChar(18) UDF Field Alias
  UDFAlias4 nVarChar(18) UDF Field Alias
  UDFAlias5 nVarChar(18) UDF Field Alias
  LogInstanc Int(11) Log Instance
  UpdateDate Date(8) Update Date
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Update User ->OUSR

# OTFC - Tax Type Combination
Module: Administration | 3 columns | ObjType: 275
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(20) Code
  Descr nVarChar(100) Description

# OTIZ - Company Time Zone
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) Index
  ChangeDate nVarChar(50) Date of Change
  TimeZone Int(11) Index of Time Zone
  ActiveDst VarChar(1) Indicator: DST Active or Not default=U [Y=, N=, U=]
  offset Int(11) Offset

# OTNC - Transaction Category
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TRANS U: TransCat
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  TransCat nVarChar(100) Transaction Category
  Locked VarChar(1) Locked default=N

# OTNN - 1099 Forms
Module: Administration | 4 columns | ObjType: 145
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormCode
  NAME U: Form1099
Fields (name type(len) description [values] ->parent table):
  FormCode Int(11) Form Code
  Form1099 nVarChar(100) 1099 Form
  UserSign Int(6) User Signature ->OUSR
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]

# OTOB - 1099 Opening Balance
Module: Administration | 6 columns | ObjType: 148
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: VendCode, Form1099, Box1099
Fields (name type(len) description [values] ->parent table):
  VendCode nVarChar(15) Vendor Code ->OCRD
  Form1099 Int(11) 1099 Form ->OTNN
  Box1099 nVarChar(20) 1099 Box
  PostDate Date(8) Posting Date
  AmountLC Num(19,6) Amount (LC)
  Submitted VarChar(1) Submitted default=N [Y=Yes, N=New]

# OTPA - Tax Parameter Attributes
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(8) Attribute Code
  Descr nVarChar(30) Description
  DataType VarChar(1) Data Type default=S [S=Amounts, P=Prices, Q=Quantities, %=Percents, I=Integer, A=String, M=Measures]
  FieldId Int(11) Field ID in CUFD ->CUFD
  Locked VarChar(1) Locked default=N [Y=Yes, N=Changeable]

# OTPL - Import Template
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TplNum
  CODE U: TplCode, TplType
Fields (name type(len) description [values] ->parent table):
  TplNum Int(11) Template Number
  TplName nVarChar(100) Template Name
  TplType nVarChar(5) Template Type [T=Target BPs, B=BP, I=Items, F=Fixed Asset]
  TplCode nVarChar(20) Template Code

# OTPR - Tax Return Values
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(7) Return Value Code
  Descr nVarChar(30) Description
  Display VarChar(1) Display default=Y [Y=Yes, N=No]
  FieldID Int(11) Field ID in CUFD ->CUFD
  Locked VarChar(1) Locked default=N [Y=Yes, N=Changeable]
  DataType VarChar(1) Data Type default=S [T=Tax Amounts, S=Amounts, P=Prices, Q=Quantities, %=Percents, I=Integer, A=String, M=Measures]

# OTPS - Tax Parameter
Module: Administration | 3 columns | ObjType: 271
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  CODE U: Code
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Code nVarChar(5) Code
  Descr nVarChar(100) Description

# OTRN - Multilingual Service Table
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CATCODE U: Category, PriCode, SecCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Doc. Entry
  Category nVarChar(6) Category [CRRpt=CR Report, Menu=Menu Item, EFM=EFM Item]
  PriCode nVarChar(128) Primary Code
  SecCode nVarChar(128) Secondary Code
  SourceLang Int(11) Source Language
  CreateDate Date(8) Create Date
  UpdateDate Date(8) Update Date

# OTRSS - Tax Replacement State Subscription
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: State
Fields (name type(len) description [values] ->parent table):
  State nVarChar(3) State ->OCST
  IEST nVarChar(14) IEST

# OTSC - CST Code for Nota Fiscal
Module: Administration | 12 columns | ObjType: 259
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
  CST_CODE U: CODE, Category
Fields (name type(len) description [values] ->parent table):
  ID Int(11) CST Internal Key
  CODE nVarChar(20) CST Code Incoming
  Situation Text(16) Description Incoming
  Locked VarChar(1) Locked default=N [Y=, N=]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Category Int(6) Tax Category default=-6 ->ONFT
  CodeOut nVarChar(20) CST Code Outgoing
  OutDesc Text(16) Description Outgoing
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OUDG - User Defaults
Module: Administration | 50 columns | ObjType: 93
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  Name nVarChar(20) Name
  Warehouse nVarChar(8) Warehouse ->OWHS
  SalePerson Int(11) Sales Employee default=-1 ->OSLP
  ICTCard nVarChar(15) BP for Invoice + Payment ->OCRD
  CashAcct nVarChar(15) Cash Account
  CheckAcct nVarChar(15) Current Account
  CreditCard Int(6) Credit Card ->OCRC
  PrintRcpt VarChar(1) Print Receipt default=N [N=No, A=Only When Adding, Y=Always]
  ShortRcpt VarChar(1) Print Payment & Invoice in Succession default=N [Y=Yes, N=No]
  Color Int(6) Windows Color [0=Combined, 1=Classic, 2=Gray, 3=Violet, 4=Blue, 5=Green, 6=Yellow, 7=Orange, 8=Red, 9=Brown]
  Address nVarChar(254) Address
  Country nVarChar(3) Country/Region ->OCRY
  PrintHeadr nVarChar(100) Printing Header
  Phone1 nVarChar(50) Telephone Number 1
  Phone2 nVarChar(50) Telephone Number 2
  Fax nVarChar(50) Fax Number
  E_Mail nVarChar(100) E-Mail
  FrgnAddr nVarChar(254) Address in Foreign Language
  FrnPrntHdr nVarChar(100) Printing Header in Foreign Lan
  FrgnPhone1 nVarChar(50) Telephone Number 1 (Foreign Lang.)
  FrgnPhone2 nVarChar(50) Telephone Number 2 (Foreign Lang.)
  FrgnFax nVarChar(50) Fax Number (Foreign Lang.)
  DflTaxCode nVarChar(8) Default Tax Code ->OSTC
  FreeZoneNo nVarChar(32) Additional ID Number
  UserSign Int(6) User Signature ->OUSR
  free1 VarChar(1) Free1
  UseTax VarChar(1) Use Tax [Y=Yes, N=No]
  AdrsFromWh VarChar(1) Use Warehouse Address in A/P Documents default=N [Y=Yes, N=No]
  Language Int(11) Language ->OLNG
  Font nVarChar(50) Font
  FontSize Int(11) Font Size
  BPLId Int(11) Default Branch ->OBPL
  AssetInDoc VarChar(1) Allow Creation of Asset in Doc. default=N [Y=Yes, N=No]
  AttachPath Text(16) Attachments Path
  DflPTICode nVarChar(5) Default POI Code ->OPTI
  Free4 VarChar(1) unused
  Free2 VarChar(1) unused
  Free3 VarChar(1) unused
  DflPosCR Int(11) Default POS/Cash Register ->OPCM
  TimeFormat VarChar(1) Time Template [0=24H, 1=12H]
  DateFormat VarChar(1) Date Template [0=DD/MM/YY, 1=DD/MM/YYYY, 2=MM/DD/YY, 3=MM/DD/YYYY, 4=CCYY/MM/DD, 5=DD/Month/YYYY, 6=YY/MM/DD]
  DateSep VarChar(1) Date Separator
  DecSep VarChar(1) Decimal Separator
  ThousSep VarChar(1) Thousands Separator
  WallPaper Text(16) Wallpaper
  WllPprDsp nVarChar(6) Wallpaper Display [1=Centralized, 2=Full Screen, 3=Tile]
  SkinType nVarChar(254) Skin Type
  CharMonth Int(11) Number of Characters in Month
  HandleEDoc VarChar(1) Can Take Control of eDoc Processing in Electronic Document Monitor default=Y [Y=Yes, N=No]

# OUDO - User-Defined Object
Module: Administration | 29 columns | ObjType: 206
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  TABLE U: TableName
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  Name nVarChar(100) Name
  TableName nVarChar(19) Table Name ->OUTB
  LogTable nVarChar(20) Log Table Name
  TYPE VarChar(1) Object Type default=1 [1=Master Data, 3=Document]
  MngSeries VarChar(1) Manage Series default=N [Y=Yes, N=No]
  CanDelete VarChar(1) Delete default=Y [Y=Yes, N=No]
  CanClose VarChar(1) Close default=N [Y=Yes, N=No]
  CanCancel VarChar(1) Cancel default=N [Y=Yes, N=No]
  ExtName nVarChar(254) Extension Name
  CanFind VarChar(1) Find default=N [Y=Yes, N=No]
  CanYrTrnsf VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  CanDefForm VarChar(1) Create Default Form default=N [Y=Yes, N=No]
  CanLog VarChar(1) Log default=N [Y=Yes, N=No]
  OvrWrtDll VarChar(1) Overwrite DLL File default=Y [Y=Yes, N=No]
  UIDFormat VarChar(1) Unique Form ID Format default=Y [Y=Yes, N=No]
  CanArchive VarChar(1) Archive default=N
  MenuItem VarChar(1) Specify Menu Item default=N [Y=Yes, N=No]
  MenuCapt nVarChar(254) Menu Caption
  FatherMenu Int(11) Parent Menu ID
  Position Int(6) Menu Position
  CanNewForm VarChar(1) Create Enhanced Form default=Y
  IsRebuild VarChar(1) If Needed, Rebuild New Form default=Y
  NewFormSrf Text(16) Enhanced Form: SRF File
  MenuUid nVarChar(32) Menu UID
  LstUpdDate Date(8) Last Update Date
  LstUpdTime Int(11) Last Update Time
  CanApprove VarChar(1) Approve default=N [Y=Yes, N=No]
  TemplateID Int(11) Workflow Template ID ->OWMG

# OUGR - Authorization Group
Module: Administration | 15 columns | ObjType: 231000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupId
  NAME_KEY U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupId Int(6) Authorization Group ID
  GroupName nVarChar(155) Group Name
  GroupDec nVarChar(155) Group Description
  Allowences Text(16) Allowances
  TPLId Int(6) Template ID ->UICU
  StartDate Date(8) Start Date
  DueDate Date(8) Due Date
  GroupType VarChar(1) Group Type default=A [A=Authorization, F=Form Settings, T=Alerts, U=UI Configuration Templates, L=All]
  CockpitId Int(6) Cockpit Template ID
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User - History ->OUSR
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  VersionNum nVarChar(13) Version Number

# OUKD - User Key Description
Module: Administration | 5 columns | ObjType: 193
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, KeyId
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(20) Table Name
  KeyId Int(6) Key Index
  KeyName nVarChar(10) Key Name
  UniqueKey VarChar(1) Unique Key default=N [Y=Yes, N=No]
  Action VarChar(1) Action default=N [A=Add, U=Update, D=Delete, N=None]

# OULA - EULA
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SerialNum
Fields (name type(len) description [values] ->parent table):
  SerialNum Int(11) Serial Number
  Signed VarChar(1) Signed default=N [Y=Yes, N=No]
  Checked VarChar(1) Checked default=N [Y=Yes, N=No]
  EULAType VarChar(1) EULA Type default=P [E=Evaluation, P=Productive]
  Licensor nVarChar(100) Licensor
  Licensee nVarChar(100) Licensee
  InstallNo nVarChar(30) Installation Number
  Signer nVarChar(155) Signer
  UFunction nVarChar(100) Signer Function
  Username nVarChar(155) B1 User Name
  SignDate Date(8) Signing Date
  DocVer nVarChar(50) EULA Document Version
  EULADoc Text(16) EULA Document
  EULAFormat nVarChar(50) EULA Format default=TXT [PDF=PDF, TXT=TXT]
  Checksum nVarChar(150) EULA Record Checksum

# OUPT - User Autorization Tree
Module: Administration | 9 columns | ObjType: 214
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId nVarChar(20) Authorization ID
  Name nVarChar(64) Name
  Options Int(6) Options default=0 [0=Full/Read/None, 1=Full/None]
  FathId nVarChar(20) Parent ID ->OUPT
  VisOrder Int(6) Display Order
  Levels Int(6) Levels default=1
  IsItem VarChar(1) IS Item default=N [Y=Yes, N=No]
  Action Int(6) Action
  UserSign Int(6) User Signature ->OUSR

# OUSG - Usage of Nota Fiscal
Module: Administration | 17 columns | ObjType: 260
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Int(11) Usage ID
  Usage nVarChar(20) Usage
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Auto Incr., D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign nVarChar(6) User Signature ->OUSR
  PostTax Int(6) Post Tax in Price to Stock default=1 [1=Yes, 0=No]
  TaxOnly VarChar(1) Tax Only default=N [Y=Yes, N=No]
  CFOPIIS nVarChar(6) CFOP Incoming In-State ->OCFP
  CFOPIOS nVarChar(6) CFOP Incoming Out-State ->OCFP
  CFOPII nVarChar(6) CFOP Incoming Import ->OCFP
  CFOPOIS nVarChar(6) CFOP Outgoing In-State ->OCFP
  CFOPOOS nVarChar(6) CFOP Outgoing Out-State ->OCFP
  CFOPOE nVarChar(6) CFOP Outgoing Export ->OCFP
  Descr nVarChar(100) Usage Description
  FreeChrgBP VarChar(1) Free of Charge (BP) default=N [Y=Yes, N=No]
  ThirdParty VarChar(1) Third Party default=N [Y=Yes, N=No]
  Adjustment VarChar(1) Adjustment default=N [Y=Yes, N=No]

# OUSR - Users
Module: Administration | 117 columns | ObjType: 12
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USERID
  PASSWORD: PASSWORD
  USER_CODE U: USER_CODE
  INTERNAL U: INTERNAL_K
Fields (name type(len) description [values] ->parent table):
  USERID Int(6) User Signature
  PASSWORD nVarChar(254) User Password default=0
  PASSWORD1 nVarChar(8) User Password
  PASSWORD2 nVarChar(8) User Password
  INTERNAL_K Int(6) Internal Number
  USER_CODE nVarChar(25) User Code
  U_NAME nVarChar(155) User Name
  GROUPS Int(6) User Group default=0 [0=Regular, 99=Deleted]
  PASSWORD4 nVarChar(254) Password
  ALLOWENCES Text(16) User Confirmation
  SUPERUSER VarChar(1) Superuser default=N [Y=Yes, N=No]
  DISCOUNT Num(19,6) Max. Discount
  PASSWORD3 nVarChar(8) User Password
  Info1File nVarChar(4) Info1File
  Info1Field Int(6) Info1Field
  Info2File nVarChar(4) Info2File
  Info2Field Int(6) Info2Field
  Info3File nVarChar(4) Info3File
  Info3Field Int(6) Info3Field
  Info4File nVarChar(4) Info4File
  Info4Field Int(6) Info4Field
  dType VarChar(1) dType default=S [Y=Yes, N=No, X=, H=SHA1, S=SHA256]
  E_Mail nVarChar(100) E-Mail
  PortNum nVarChar(50) Mobile Phone Number
  OutOfOffic VarChar(1) Out of Office default=N [Y=Yes, N=No]
  SendEMail VarChar(1) Send E-Mail default=N [Y=Yes, N=No]
  SendSMS VarChar(1) Send SMS default=N [Y=Yes, N=No]
  DfltsGroup nVarChar(8) Defaults ->OUDG
  CashLimit VarChar(1) Cash Amount Limit default=N [Y=Yes, N=No]
  MaxCashSum Num(19,6) Max. Cash Total
  Fax nVarChar(50) Fax Number
  SendFax VarChar(1) Send Fax default=N [Y=Yes, N=No]
  Locked VarChar(1) User Locked default=N [Y=Yes, N=No]
  Department Int(6) Department default=-2 ->OUDP
  Branch Int(6) Branch default=-2 ->OUBR
  UserPrefs Text(16) User Preferences
  Language Int(11) Language
  Charset Int(6) Font Language
  OpenCdt VarChar(1) Open Window for Credit Reference default=N [Y=Yes, N=No]
  CdtPrvDays Int(11) Vouchers from Last Days default=1
  DsplyRates VarChar(1) Display Rate Table on start up default=N [Y=Yes, N=No]
  AuImpRates VarChar(1) Import Currency Rates Automatically default=N [Y=Yes, N=No]
  OpenDps VarChar(1) Open Postdated Checks Window default=N [Y=Yes, N=No]
  RcrFlag VarChar(1) Display Transactions Scheduled for Today default=N [Y=Yes, N=No]
  CheckFiles VarChar(1) File Check default=N [Y=Yes, N=No]
  OpenCredit VarChar(1) Open Postdated Credit Vouchers Window [Y=Always, N=No, D=By Date]
  CreditDay1 Int(6) Credit Handling Day 1 default=1
  CreditDay2 Int(6) Credit Handling Day 2 default=15
  WallPaper Text(16) Wallpaper
  WllPprDsp Int(6) Wallpaper Display [1=Centralized, 2=Full Screen, 3=Tile]
  AdvImagePr VarChar(1) Extended Image Processing [N=Partial, O=Without, Y=Full]
  ContactLog VarChar(1) Today's Activity Alert default=N [Y=Yes, N=No]
  LastWarned Date(8) Last Warned Date
  AlertPolFr Int(6) Message Check Frequency default=5
  ScreenLock Int(6) Screen Lock Delay default=30
  ShowNewMsg VarChar(1) Open Message on Arrival default=Y [Y=Yes, N=No]
  Picture nVarChar(200) Picture
  Position nVarChar(90) Position
  Address nVarChar(254) Address
  Country nVarChar(3) Country/Region ->OCRY
  Tel1 nVarChar(50) Telephone 1
  Tel2 nVarChar(50) Telephone 2
  GENDER VarChar(1) Gender default=F [F=Female, M=Male]
  Birthday Date(8) Birthday
  EnbMenuFlt VarChar(1) Enable Forbidden Menu Items default=N [N=No, Y=Yes]
  objType nVarChar(20) Object Type - History default=12
  logInstanc Int(11) Log Instance - History
  userSign Int(6) Creating User - History ->OUSR
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  OneLogPwd VarChar(1) At first logon change password default=Y [N=Password should not be changed at first login, Y=Password should be changed at first login]
  lastLogin Date(8) Last Logon Date
  LastPwds Text(16) Last Passwords 1
  LastPwds2 nVarChar(254) Last Passwords 2 default=0
  LastPwdSet Date(8) Last Password Change
  FailedLog Int(11) Failed Login Count default=0
  PwdNeverEx VarChar(1) Password Never Expires default=N [Y=Yes, N=No]
  SalesDisc Num(19,6) Max. Sales Discount
  PurchDisc Num(19,6) Max. Purchase Discount
  LstLogoutD Date(8) Last Logoff Date
  LstLoginT Int(11) Last Logon Time
  LstLogoutT Int(11) Last Logoff Time
  LstPwdChT Int(11) Last Password Change Time
  LstPwdChB nVarChar(8) Last Password Changed By
  RclFlag VarChar(1) Display Recurring Transactions default=N [Y=Yes, N=No]
  MobileUser VarChar(1) Mobile User default=N [Y=Yes, N=No]
  MobileIMEI nVarChar(64) Mobile IMEI
  PrsWkCntEb VarChar(1) Personal Work Center Enable default=N [Y=Yes, N=No]
  SnapShotId Int(11) Snapshot ID default=0
  STData nVarChar(40) User Password Salt
  SupportUsr VarChar(1) Support User default=N [N=No, Y=Yes]
  NoSTPwdNum Int(6) Password encrypted w/o Salt (cryptography) default=0
  DomainUser nVarChar(50) Domain user name bound in SLD
  CUSAgree VarChar(1) CUS Agreement [Y=Yes, N=No]
  EmailSig Text(16) E-Mail Signature
  TPLId Int(6) Template ID ->UICU
  DigCrtPath Text(16) Digital Certificate Path
  ShowNewTsk VarChar(1) Open Worklist on Task Arrival default=Y [Y=Yes, N=No]
  IntgrtEb VarChar(1) Enable Setting Integration default=N [Y=Yes, N=No]
  AllBrnchF VarChar(1) Allow Viewing of All (Including Unassigned To) Branches in Financial Reports default=Y [Y=Yes, N=No]
  EvtNotify VarChar(1) Allow Event Notification default=Y
  IgnDtOwn VarChar(1) Ignore Data Ownership for this user default=N [Y=Yes, N=No]
  EnterAsTab VarChar(1) Use Numeric Keypad Enter Key as Tab Key default=N [Y=Yes, N=No]
  DotAsSep VarChar(1) Use Del Key As Separator default=N [Y=Yes, N=No]
  MouseOnly VarChar(1) Document Operation by Mouse Only default=N [Y=Yes, N=No]
  Color Int(6) Company Color [0=Combined, 1=Classic, 2=Gray, 3=Violet, 4=Blue, 5=Green, 6=Yellow, 7=Orange, 8=Red, 9=Brown]
  SkinType nVarChar(254) Skin Type
  Font nVarChar(50) Font
  FontSize Int(11) Font Size
  NaturalPer VarChar(1) Natural Person default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  AutoAsnBPL VarChar(1) Auto. Assign Branches default=N [Y=Yes, N=No]
  EncryptIV nVarChar(100) Encrypt IV
  HandleEDoc VarChar(1) Can Process Electronic Documents default=Y [Y=Yes, N=No]
  ShowLicBal VarChar(1) Show License Balloon default=Y [Y=Yes, N=No]
  LicBaHDate Date(8) License Balloon Hiding Date

# OUTB - User Tables
Module: Administration | 9 columns | ObjType: 153
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(20) Table Name
  Descr nVarChar(30) Description
  TblNum Int(11) Table number
  ObjectType nVarChar(20) Object Type default=0 [0=No Object, 1=Master Data, 2=Master Data Rows, 3=Document, 4=Document Rows, 5=No Object with Auto. Increment]
  UsedInObj nVarChar(20) Used in Object
  LogTable nVarChar(20) Log Table
  Archivable VarChar(1) Archivable default=N [Y=Yes, N=No]
  ArchivDate nVarChar(18) Archive Date
  DisplyMenu VarChar(1) Display Menu default=Y [Y=Yes, N=No]

# OVET - VAT Exemption Types
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: typeID
Fields (name type(len) description [values] ->parent table):
  typeID Int(6) Type ID
  TypeCode nVarChar(2) Type Code
  TypeName nVarChar(100) Type Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]

# OVMC - Value Mapping Communication Object
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  SYS_ID Int(11) Third Party System ID
  ObjectId Int(11) Object ID
  Type nVarChar(2) Type default=MD [MD=Master Data, TR=Transaction]
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  EndDate Date(8) End Date
  EndTime Int(11) End Time
  Message Text(16) Message
  Status VarChar(1) Communication Status default=P [P=Pending, E=Error, N=New, S=Successful, R=Rejected]

# OVNM - VAT Report Numbering
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: NumId
Fields (name type(len) description [values] ->parent table):
  NumId Int(11) Numbering ID
  NumName nVarChar(10) Numbering Name
  First nVarChar(9) First Number
  Next nVarChar(9) Next Number
  Last nVarChar(9) Last Number
  YrDepend VarChar(1) Year-Dependent default=N [Y=Year-Dependent, N=Year-Indepedent]
  DefaultNum VarChar(1) Default Numbering default=N [Y=Default Numbering, N=No Default Numbering]

# OWEX - Workflow Engine Execution Entity
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  IsActive Int(6) Is Active
  IsConCurr Int(6) Is Concurrent
  IsScope Int(6) Is Scope
  ProcInstId nVarChar(100) Process Instance ID
  ParentId Int(11) Parent ID
  ProcDefId Int(11) Process Definition ID
  ActId nVarChar(250) Activity ID
  DataContex Text(16) Data Context
  B1WFInstId Int(11) Workflow Instance ID
  LastUpdate nVarChar(50) Last Update Date and Time

# OWFER - Workflow Error Message
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Identity(11) Internal Number
  MsgID nVarChar(64) Message ID
  MsgDetails Text(16) Message Details
  CreateDate Date(8) Create Date - History
  UserSign Int(6) Updating User - History ->OUSR
  CreateTime Int(11) Create Time
  MsgTaskID nVarChar(6) Message Task ID
  MsgErrSrc nVarChar(20) Message Source
  Remark Text(16) Remarks
  MsgType VarChar(1) Message Type [I=Information, E=Error, W=Warning]
  MsgInstID Int(11) Message Instance ID
  TemplateID Int(11) Template ID

# OWFI - Workflow - Instances
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WFInstID
Fields (name type(len) description [values] ->parent table):
  WFInstID Identity(11) WF Instance ID
  ExecID Int(11) WF Instance on Engine
  TemplateID Int(11) WF Template ID
  Creator nVarChar(25) Creator
  Status nVarChar(8) Status [S=Setup, F=Completed, G=In Progress, C=Cancelling, Q=Canceled, E=Error]
  StartDate Date(8) Start Date
  StartTime Int(6) Start Time
  EndTime Int(6) End Time
  EndDate Date(8) End Date
  IsAutoStar Int(6) Is auto start instance

# OWIN - Workflow Engine Information
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) ID
  WFInstId Int(11) Workflow Instance ID
  TaskId Int(11) Task ID
  ProcDefId nVarChar(250) Process Definition ID
  FlowElemId nVarChar(250) Flow Element ID
  InfoType nVarChar(2) Information Type [E=Error, W=Warning, I=Information, O=Other]
  InfoCode nVarChar(10) Predefined Information Code
  Desc Text(16) Description
  CreateDate Date(8) Create Date
  CreateTime Int(11) Create Time
  IsRead VarChar(1) Info. read by SAP Business One? [N=No, Y=Yes]

# OWJB - Workflow Job Entity
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Int(11) ID
  HandlerTyp nVarChar(50) Handler Type
  ExecId Int(11) Execution ID
  Rev Int(11) Revision
  DueDate Date(8) Due Date
  ProcInstId Int(11) Process Instance ID
  Type nVarChar(250) Type
  HandlerCfg nVarChar(250) Handler Configuration

# OWLS - Workflow - Task Details
Module: Administration | 34 columns | ObjType: 1620000000
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID ->OWFI
  TaskID Identity(11) Task ID
  WFID nVarChar(64) Workflow ID
  WFName nVarChar(100) Workflow Name
  TaskDesc nVarChar(100) Task Description
  ObjType nVarChar(20) Object Type
  Operation VarChar(1) Operation [A=Add, U=Update, D=Delete]
  ObjKey nVarChar(100) Object Key
  EnterDate Date(8) Enter Date
  EnterTime Int(6) Enter Time
  TaskType VarChar(1) Task Type
  DueDate Date(8) Due Date
  DueTime Int(6) Due Time
  UpdateDate Date(8) Update Date - History
  UpdateTime Int(6) Update Time - History
  Owner nVarChar(25) Owner
  Priority Int(6) Priority default=2 [1=High, 2=Medium, 3=Low]
  UserSign Int(6) User Signature
  Status VarChar(1) Status default=W [S=Setup, W=To Be Picked, P=Picking, G=In Progress, D=Completing, F=Completed, N=Suspended, C=Cancelling, Q=Canceled, O=Forwarding, E=Error]
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History
  Deleted VarChar(1) Deleted - History
  DuraDays Int(11) Duration Days
  DuraHours Int(6) Duration Hours
  TaskName nVarChar(100) Task Name
  isPicked VarChar(1) Is Picked default=N
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  WorkListId Int(11) Worklist ID
  ObjSubType nVarChar(64) Object Subtype
  ForwardTo nVarChar(25) User to Forward
  WasRead VarChar(1) Line Read default=N
  TrigParams Text(16) Trigger Parameters
  Key nVarChar(254) Task ID in XML

# OWMG - Workflow Manager
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ID
Fields (name type(len) description [values] ->parent table):
  ID Identity(11) Workflow ID
  TemplateID Int(11) Template ID
  TmplateKey nVarChar(254) Template Key
  Name nVarChar(254) Name
  Version nVarChar(13) Version
  MAXIns Int(11) Maximum Number of Instances
  Status VarChar(1) Status default=I [I=Inactive, A=Active, E=Activation failed, M=Importing, P=Imported, F=Import failed, D=Deleted]
  XMLFile Text(16) XML File
  Desc Text(16) Description
  LogIns Int(11) Log Instance - History
  StartType VarChar(1) Start Type default=M [M=Manual Start, T=Timer Start, C=Conditional Start]

# OWST - Confirmation Level
Module: Administration | 6 columns | ObjType: 120
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WstCode
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  WstCode Int(11) Stage ->OWST
  Name nVarChar(20) Name
  Remarks nVarChar(100) Description
  MaxReqr Int(6) No. of Authorizers default=1
  UserSign Int(6) User Signature ->OUSR
  MaxRejReqr Int(6) No. of Rejects default=1

# OWTI - Workflow Timer Definition
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  Name nVarChar(50) Name
  TemplateId Int(11) Workflow Template ID
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  RepeatCnt Int(11) Repeat Event Count
  Duration nVarChar(200) Duration
  LastUpdate nVarChar(50) Last Update Date and Time
  UnScheStDt Date(8) Start Date of Next Schedule
  UnScheStTi Int(11) Start Time of Next Schedule
  UnScheReCt Int(11) Unschedule Repeat Count
  IsComplete VarChar(1) Is This Timer Completed default=N [Y=Yes, N=No]
  JobHanType nVarChar(50) Job Handler Type
  JobHanConf Text(16) Job Handler Configuration
  IsActive VarChar(1) Is This an Active Timer

# OWTJ - Workflow Timer Job
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  IsASync VarChar(1) Is Asychronized [Y=Yes, N=No]
  Status nVarChar(10) Status
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  TimerEtyId Int(11) Timer Entity ID
  JobHanConf Text(16) Job Handler Configuration
  JobHanType nVarChar(50) Job Handler Type
  LastUpdate nVarChar(50) Last Update Date and Time

# OWTM - Approval Templates
Module: Administration | 8 columns | ObjType: 121
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WtmCode
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  Name nVarChar(20) Name
  Remarks nVarChar(100) Description
  Conds VarChar(1) Conditions default=N [Y=Yes, N=No]
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature ->OUSR
  PmptChg VarChar(1) Prompt Change default=Y [Y=Yes, N=No]
  AppOnUpd VarChar(1) Apply on Update default=Y [Y=Yes, N=No]

# OWTS - Workflow Engine Task Table
Module: Administration | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Id
Fields (name type(len) description [values] ->parent table):
  Id Identity(11) ID
  Owner nVarChar(254) Owner
  OutputPar Text(16) Output Param.
  EndTime nVarChar(50) End Time
  StartTime nVarChar(50) Start Time
  ProcDefId Int(11) Process Definition ID
  Name nVarChar(254) Name
  ExeId Int(11) Execution ID
  ProcInsId Int(11) Process Instance ID
  Desc nVarChar(254) Description
  InputPar Text(16) Input Parameter
  DelReason nVarChar(254) Delete Reason
  Assignee nVarChar(254) Assignee
  LogInst Int(11) Log Instance
  LastUpdate nVarChar(50) Last Update Date and Time
  Key nVarChar(254) Task ID in XML
  B1Task Int(11) B1 Task ID

# PCI1 - Process Checklist Element Extended Data
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: InstancePk, LineNum
Fields (name type(len) description [values] ->parent table):
  InstancePk Int(11) Instance Primary Key ->OPCI
  LineNum Int(11) Line Number
  BPMNElId nVarChar(254) BPMN Model Element ID
  BPMNElDes nVarChar(254) BPMN Model Element Description
  ParamType nVarChar(254) Parameter Type
  ParamKey nVarChar(254) Parameter Key
  ParamVal nVarChar(254) Parameter Value

# PJT1 - Project Plan Steps
Module: Administration | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, StepCode
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  StepCode Int(11) Step Code
  Father Int(11) Father Step Code
  VisOrder Int(11) Visual Order
  Level Int(11) Node Level
  StepName nVarChar(254) Step Name
  StepInfo nVarChar(254) Step Info
  StepNotes nVarChar(254) Step Notes
  StepLink nVarChar(32) Step Link to Menu ID
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  IsComplete VarChar(1) Is Complete
  LogInstanc Int(11) Log Instance
  Owner nVarChar(254) Owner ->OUSR
  Status Int(11) Status default=0
  Duration Num(19,6) Duration
  PlanTime Num(19,6) Planned Time
  AtcEntry Int(11) Attachment Entry ->OATC
  TotalPTime Num(19,6) Total Planned Time
  QueryID Int(11) Step Link Query ID ->OUQR

# PJT2 - Project Plan Steps Time Record
Module: Administration | 10 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry, StepCode, LineNum
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Internal Number
  StepCode Int(11) Step Code
  LineNum Int(11) Line Number
  Date Date(8) Date
  StartTime Int(11) Start Time
  EndTime Int(11) End Time
  Remarks nVarChar(254) Remarks
  LogInstanc Int(11) Log Instance
  Owner nVarChar(254) Owner ->OHEM
  Duration Num(19,6) Duration

# PQW1 - Purchase Quotation Generation: Line Items
Module: Administration | 24 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineNum
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OPQW
  LineNum Int(11) Row Number
  ItemCode nVarChar(50) Item No. ->OITM
  Dscription nVarChar(200) Item/Service Description
  PQTReqDate Date(8) Pur Quotation: Required Date
  PQTReqQty Num(19,6) Pur Quotation: Required Qty
  BuyUnitMsr nVarChar(100) Purchasing UoM
  FreeTxt nVarChar(100) Free Text
  PQTGrpNum Int(11) Pur. Quotation Group Number
  PQTGrpSer Int(11) Pur. Quotation Group Series
  PQTGrpHW VarChar(1) Pur. Quotation Group Manual default=N [Y=Yes, N=No]
  ValidUntil Date(8) Valid Until Date
  WhsCode nVarChar(8) Warehouse Code ->OWHS
  PQTSeries Int(11) Purchase Quotation Series ->NNM1
  PRAbsEntry Int(11) Purchase Request Number ->OPRQ
  ReqName nVarChar(155) Requester Name
  PRLineNum Int(11) Purchase Request Row Number
  PRLineStat VarChar(1) Purchase Request Row Status
  DistriRule nVarChar(8) Distribution Rule
  Project nVarChar(20) Project Code
  VendMfrNum nVarChar(17) Vendor Mfr Catalog No.
  ShipType Int(6) Shipping Type
  ItmPerUnit Num(19,6) No. of Items per Purchase Unit
  PriceMode VarChar(1) Price Mode default=N [N=Net, G=Gross]

# QFD1 - Query Fields Definition
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IntrnalKey, LineNum
Fields (name type(len) description [values] ->parent table):
  IntrnalKey Int(11) Internal Key
  LineNum Int(11) Row Number
  FieldName nVarChar(80) Field Name
  FieldDesc nVarChar(100) Field Description
  OrigTable nVarChar(100) Original Table
  OrigField nVarChar(50) Original Field
  EditType VarChar(1) Edit Type [-=None, T=Tax, R=Rate, P=Price, S=Sum, N=Unit, Q=Quantity, %=Percent, M=Measure]
  StatType VarChar(1) Statistical Type default=D [D=Dimension, M=Measure]
  AggrType VarChar(1) Aggregation Type default=N [N=None, S=Sum, A=Average, C=Count, M=Minimum, X=Maximum]
  LinkTable nVarChar(100) Linked Table
  DeciPlace Int(6) Decimal Places default=2 [0=No Decimals, 1=One Decimal, 2=Two Decimals, 3=Three Decimals, 4=Four Decimals, 5=Five Decimals, 6=No Rounding, 7=Amounts, 8=Prices, 9=Rates, 10=Quantities, 11=Units, 12=Percent]
  DbType VarChar(1) Database Type

# RIT1 - Interest Rates
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, LineNum
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Object Code ->ORIT
  LineNum Int(11) Row Number
  Days Int(6) Number of Tolerance Days
  IntrstPrct Num(19,6) Interest %
  FixedSum Num(19,6) Fixed Interest Amount
  FixSumCurr nVarChar(3) Fixed Amount Currency

# RLD1 - Reference Links Definition
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, TargetType, TargetFld
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ORLD
  TargetType VarChar(1) Target Type default=H [H=Header, B=BP Row, L=Row]
  TargetFld nVarChar(50) Target Field
  SourceFld nVarChar(50) Source Field
  OrderNum Int(11) Order Number
  SourceType VarChar(1) Source Type default=E [B=Base Document Reference, C=Column, D=Default, E=Not Defined, I=Installment Number, S=Reference Link Sources, T=Remarks Template]

# RLS1 - Reference Links Sources Definition
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineID
  OBJARRFLD U: SrcObjType, SrcArr, SrcFld
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->ORLS
  LineID Int(11) Line Id
  SrcObjType nVarChar(20) Source Object Type
  SrcArr Int(6) Source of Posting
  SrcFld nVarChar(21) Source Field

# RSAT - RecordSet Audit Table
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: QueryID
Fields (name type(len) description [values] ->parent table):
  QueryID Identity(11) Query ID
  QueryDate Int(11) Date of Query
  QueryTime Int(11) Timestamp of Query
  QueryDetls Text(16) Query Details

# SDEX - Dynamic Extensions
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormId, ItemId, ColumnId
Fields (name type(len) description [values] ->parent table):
  FormId Int(11) Form ID
  ItemId Int(11) Item ID default=0
  ColumnId Int(11) Column ID default=0
  BefAppl Text(16) Application Before
  AftAppl Text(16) Application After
  BefScript VarChar(1) Is Script Before default=Y [Y=Yes, N=No]
  AftScript VarChar(1) Is Script After default=Y [Y=Yes, N=No]
  UserSign Int(6) User Signature default=-1 ->OUSR

# SDIS - Dynamic Interface (Strings)
Module: Administration | 8 columns | ObjType: 229
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormId, ItemId, ColumnId, Language
Fields (name type(len) description [values] ->parent table):
  FormId nVarChar(40) Form ID
  ItemId nVarChar(40) Item ID
  ColumnId nVarChar(20) Column ID
  Language Int(11) Language Code default=0
  ItemString nVarChar(254) Item String
  IsBold VarChar(1) Is Bold default=N [Y=Yes, N=No]
  IsItalic VarChar(1) Is Italics default=N [Y=Yes, N=No]
  UserSign Int(6) User Signature default=-1 ->OUSR

# SHS1 - Fields that can automatically refresh user-defined values
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: IndexID, FieldID
Fields (name type(len) description [values] ->parent table):
  IndexID Int(11) Index ->CSHS
  FieldID nVarChar(60) Field

# SMSG - 
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Internal Key default=1 [1=Unique key]
  Signature Text(16) E-Mail signature

# SPRG - Application Start
Module: Administration | 8 columns | ObjType: 86
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LineNum, UserCode
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Row Number
  UserCode nVarChar(25) User Code default=-1
  Name nVarChar(128) Application Name
  FileName nVarChar(254) File Name
  Path Text(16) Application Route
  Params Text(16) Application Parameters
  OPRTION nVarChar(50) Operation Method default=open [open=Open, edit=Edit, explore=Find Folder, find=Find File, print=Print, properties=Properties]
  WIN_STYLE nVarChar(2) Windows Type default=1 [0=Hide, 1=Standard, 3=Enlarge, 5=Operate as Previous, 6=Reduce, 9=Restore]

# STA1 - Valid Period
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: StaCode, SttType, EfctDate
Fields (name type(len) description [values] ->parent table):
  StaCode nVarChar(8) Tax Parameter Code ->OSTA
  SttType Int(11) Tax Type ->OSTT
  EfctDate Date(8) Effective From
  Rate Num(19,6) Rate
  TaaSUpdate Date(8) Last Update By TaaS

# STC1 - Sales Tax Codes - Rows
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: STCCode, Line_ID
  STACode: STACode, STAType
Fields (name type(len) description [values] ->parent table):
  STCCode nVarChar(8) STC Code ->OSTC
  Line_ID Int(11) Row Number default=0
  STACode nVarChar(8) STA Code ->OSTA
  STAType Int(11) STA Type ->OSTA
  TaxOnTCode nVarChar(8) STA Tax on Tax Code ->OSTA
  TaxOnTType Int(11) STA Tax On Tax Type ->OSTA
  EfctivRate Num(19,6) Effective Rate
  FmlId Int(11) Tax Formula ID ->OFML
  CstCodeIn nVarChar(20) CST Code Incoming
  CstSuffix nVarChar(2) CST Suffix for ICMS
  LogInstanc Int(11) Log Instance default=0

# SVM1 - Systems for Value Mapping Properties
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, PropID
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  PropID Int(11) Property ID
  PropDesc nVarChar(50) Property Description
  PropType VarChar(1) Property Type default=S [S=String, N=Numeric, D=Date, P=Password]
  PropValue nVarChar(254) Property Value

# SVM2 - Systems for Value Mapping Properties
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, ObjectId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  ObjectId Int(11) Object ID
  UDTName nVarChar(50) Name of user defined table

# TCD1 - Key Fields for Determination
Module: Administration | 20 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD1_UNI U: TcdId, Priority
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  TcdId Int(11) Tax Determination Code ->OTCD
  KeyFld_1 Int(11) Key Fields 1 default=0
  KeyFld_2 Int(11) Key Fields 2 default=0
  KeyFld_3 Int(11) Key Fields 3 default=0
  Priority Int(11) Priority default=0
  Descr nVarChar(100) Description
  KeyFld_4 Int(11) Key Fields 4 default=0
  UDFTable_1 nVarChar(20) UDF Table Name 1
  UDFAlias_1 nVarChar(18) UDF Field Alias 1
  UDFTable_2 nVarChar(20) UDF Table Name 2
  UDFAlias_2 nVarChar(18) UDF Field Alias 2
  UDFTable_3 nVarChar(20) UDF Table Name 3
  UDFAlias_3 nVarChar(18) UDF Field Alias 3
  UDFTable_4 nVarChar(20) UDF Table Name 4
  UDFAlias_4 nVarChar(18) UDF Field Alias 4
  KeyFld_5 Int(11) Key Fields 5 default=0
  UDFTable_5 nVarChar(20) UDF Table Name 5
  UDFAlias_5 nVarChar(18) UDF Field Alias 5
  LegalText nVarChar(250) Legal Text

# TCD2 - Key Field Values
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD2_UNI U: Tcd1Id, DispOrder
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Tcd1Id Int(11) Tax Determination ID ->TCD1
  DispOrder Int(11) Display Order
  KeyFld_1_V nVarChar(50) Key Fields 1 Value
  KeyFld_2_V nVarChar(50) Key Fields 2 Value
  KeyFld_3_V nVarChar(50) Key Fields 3 Value
  KeyFld_4_V nVarChar(50) Key Fields 4 Value
  KeyFld_5_V nVarChar(50) Key Fields 5 Value

# TCD3 - Tax Code Determination
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
  TCD3_UNI U: Tcd2Id, EfctFrom
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Tcd2Id Int(11) Determination Key Field ID ->TCD2
  EfctFrom Date(8) Effective From
  EfctTo Date(8) Effective To
  TaxCode nVarChar(8) Tax Code

# TCD4 - Withholding Tax Code Determination
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Internal Number
  Tcd2Id Int(11) Determination Key Field ID
  WTCode nVarChar(8) WTax Code
  Type VarChar(1) WTax Code Type default=L [R=AR Default WT Code, P=AP Default WT Code, L=Line Item WT Code]

# TCD5 - Tax Code by Usage
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsId
Fields (name type(len) description [values] ->parent table):
  AbsId Int(11) Numerator
  Tcd3Id Int(11) Valid Period ID
  UsageCode Int(11) Usage
  TaxCode nVarChar(8) Tax Code
  Type VarChar(1) Tax Code Type default=L [R=A/R Default Tax Code, P=A/P Default Tax Code, L=Line Item Tax Code]
  ExpTaxCode nVarChar(8) Freight Tax Code
  PurTaxCode nVarChar(8) Purchase Tax Code

# TDR1 - Can Be Archive
Module: Administration | 12 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line_ID
Fields (name type(len) description [values] ->parent table):
  Line_ID Int(11) Row Number
  KeySeg1 nVarChar(15) Key Segment 1
  KeySeg2 nVarChar(15) Key Segment 2
  KeySeg3 nVarChar(15) Key Segment 3
  KeySeg4 nVarChar(15) Key Segment 4
  KeySeg5 nVarChar(15) Key Segment 5
  KeySeg6 nVarChar(15) Key Segment 6
  KeySeg7 nVarChar(15) Key Segment 7
  KeySeg8 nVarChar(15) Key Segment 8
  KeySeg9 nVarChar(15) Key Segment 9
  KeySeg10 nVarChar(15) Key Segment 10
  DocAbs Int(11) Document Internal ID

# TFC1 - Tax Type Combination - Rows
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TfcId, DispOrder
  TAXTYPE: TypeId
Fields (name type(len) description [values] ->parent table):
  TfcId Int(11) TFC ID ->OTFC
  DispOrder Int(11) Display Order
  TypeId Int(11) Tax Type ID ->OSTT
  FmlId Int(11) Formula ID ->OFML

# TNN1 - 1099 Boxes
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: FormCode, Box1099
Fields (name type(len) description [values] ->parent table):
  FormCode Int(11) Form Code ->OTNN
  Box1099 nVarChar(20) 1099 Box
  BoxDescr nVarChar(100) Box Description
  UserSign Int(6) User Signature ->OUSR
  Locked VarChar(1) Locked default=N [N=Changeable, Y=Locked]
  Min1099Amt Num(19,6) Minimum 1099 Amount

# TPL1 - Template - Records
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TplNum, LineNum
Fields (name type(len) description [values] ->parent table):
  TplNum Int(11) Template Code ->OTPL
  LineNum Int(11) Line No.
  FieldPos Int(11) Field Pos.
  SrcArrType Int(11) Source Array Type default=1 [-1=None, 1=Main, 12=Array 1, 13=Array 2, 14=Array 3, 15=Array 4, 16=Array 5, 17=Array 6, 18=Array 7, 19=Array 8, 20=Array 9, 21=Array 10, 22=Array 11]
  SrcObjType Int(11) Source Object Type default=-1

# TPS1 - Tax Parameter Attributes
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TpsId, TpaId
  ORDER U: TpsId, DispOrder
Fields (name type(len) description [values] ->parent table):
  TpsId Int(11) Tax Parameter Set ->OTPS
  DispOrder Int(11) Display Order
  TpaId Int(11) ID of Attributes Mapping ->OTPA
  Mandatory VarChar(1) Mandatory to Input default=N [Y=Yes, N=No]

# TPS2 - Tax Parameter - Return Values
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TpsId, TprId
  ORDER U: TpsId, DispOrder
Fields (name type(len) description [values] ->parent table):
  TpsId Int(11) Tax Parameter Set ->OTPS
  DispOrder Int(11) Display Order
  TprId Int(11) ID of Return Values Mapping ->OTPR

# TRN1 - Subtable of OTRN
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrnAbsEntr, LineNum
  UniqueIdx U: TrnAbsEntr, ItemType, ItemCode, LineNum
Fields (name type(len) description [values] ->parent table):
  TrnAbsEntr Int(11) OTRN Abs Entry
  LineNum Int(11) Line Number of Table
  ItemCode nVarChar(254) Item Code
  ItemType nVarChar(8) Item Type
  SlimType nVarChar(8) Slim Type
  MaxLength Int(11) Max. Length
  SourceText Text(16) Source Text
  Memo Text(16) Memo

# TRN2 - Subtable of OTRN
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TrnAbsEntr, LineNum, SubLineNum
  UniqueIdx U: TrnAbsEntr, LineNum, LangCode
Fields (name type(len) description [values] ->parent table):
  TrnAbsEntr Int(11) OTRN Abs Entry
  LineNum Int(11) Line Number of TRN1
  SubLineNum Int(11) Subline Number
  LangCode Int(11) Language Code
  Text Text(16) Translated Text

# UDG1 - User Defaults - Documents
Module: Administration | 15 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, ObjType
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  ObjType nVarChar(20) Object Type
  Copies Int(6) No. of Copies default=1
  PrintOnAdd VarChar(1) Add & Print default=N [Y=Yes, N=No]
  ExprtOnAdd VarChar(1) Add & Export default=N [Y=Yes, N=No]
  RoundSums VarChar(1) Totals Rounding default=N [Y=Yes, N=No]
  Remark Text(16) Permanent Remark
  PrintSums VarChar(1) Print Totals default=Y [Y=Yes, N=No]
  VndrNum VarChar(1) Print Mfr Catalog No. default=N [Y=Yes, N=No]
  PrnDscnt VarChar(1) Print Discount Data default=Y [Y=Yes, N=No]
  HandCopies Int(6) No. of Copies for Manual Doc. default=1
  EngKBItem VarChar(1) English Keyboard Entering Item No. default=N [Y=Yes, N=No]
  EngKBCard VarChar(1) English Keyboard Entering BP Code default=N [Y=Yes, N=No]
  EmailOnAdd VarChar(1) Add & E-Mail default=N [Y=Yes, N=No]
  PDFOnAdd VarChar(1) Add & Export to PDF default=N [Y=Yes, N=No]

# UDG2 - User Defaults - Credit Cards
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, CreditCard
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  CreditCard Int(6) Credit Card Code ->OCRC
  AcctCode nVarChar(15) Credit Amount Code ->OACT

# UDG3 - User Defaults - POS/Cash Register
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, PosCashReg
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) Code
  PosCashReg Int(11) POS/Cash Register ->OPCM

# UDG4 - User Defaults - Default POI for Folio Numbering Documents
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, FNDAbs
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(8) POI Code
  FNDAbs Int(11) Folio Numbering Document Abs Entry ->OFND
  ObjectCode nVarChar(20) Document
  DocSubtype nVarChar(2) Subdocument default=-- [--=, DM=A/P Debit Memo, DN=A/R Debit Memo, IB=A/R Bill]
  DflPTICode nVarChar(5) Default POI Code ->OPTI
  DflPtiFCE nVarChar(5) Default POI Code for FCE

# UDO1 - User-Defined Objects - Child
Module: Administration | 5 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, SonNum
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  SonNum Int(11) Child No.
  TableName nVarChar(19) Table Name ->OUTB
  LogName nVarChar(20) Log Table Name
  SonName nVarChar(100) Child Name default=' '

# UDO2 - User-Defined Objects - Find Columns
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, ColumnNum
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  ColumnNum Int(11) Column Number
  ColAlias nVarChar(52) Column Alias
  ColumnDesc nVarChar(80) Column Description

# UDO3 - User-Defined Objects - Found Columns
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, SonNum, ColumnNum
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  ColumnNum Int(11) Form Column Number
  SonNum Int(11) Child No. default=0
  ColAlias nVarChar(52) Form Column Alias
  ColDesc nVarChar(80) Form Column Description
  ColEdit VarChar(1) Form Column Actived or Not default=N

# UDO4 - User-Defined Objects - Child Table Columns
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code, SonNum, ColumnNum
Fields (name type(len) description [values] ->parent table):
  Code nVarChar(20) Code
  ColumnNum Int(11) Form Column Number
  SonNum Int(11) Child No.
  ColAlias nVarChar(52) Form Column Alias
  ColDesc nVarChar(80) Form Column Description
  ColIsUsed VarChar(1) Form Column Used or Not default=N
  ColEdit VarChar(1) Form Column Actived or Not default=N

# UFD1 - User Fields - Values Definitions
Module: Administration | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableID, FieldID, IndexID
Fields (name type(len) description [values] ->parent table):
  TableID nVarChar(21) Table
  FieldID Int(6) Field
  IndexID Int(6) Index
  FldValue nVarChar(254) Value
  Descr nVarChar(254) Description
  FldDate Date(8) Date Value

# UGR1 - Group Authorization
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: GroupLink, PermId
Fields (name type(len) description [values] ->parent table):
  GroupLink Int(6) Group Link ->OUGR
  PermId nVarChar(20) Authorization ID ->OUPT
  Permission VarChar(1) Authorization default=N [V=Various, F=Full, R=Read Only, N=None, U=Undefined Type]

# UKD1 - User Sub-Keys Description
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TableName, KeyId, SubKeyId
  ALIAS: TableName, ColAlias
Fields (name type(len) description [values] ->parent table):
  TableName nVarChar(20) Table Name
  KeyId Int(6) Key Index
  SubKeyId Int(6) Sub-Key Index
  ColAlias nVarChar(18) Column Alias

# UPT1 - User Authorization Tree - Extended Permission
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: PermId, FormId
  FORM_ID: FormId
Fields (name type(len) description [values] ->parent table):
  PermId nVarChar(20) Authorization ID ->OUPT
  FormId nVarChar(20) Form ID
  VisOrder Int(6) Display Order

# USR1 - Short Cut
Module: Administration | 43 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USERLINK
Fields (name type(len) description [values] ->parent table):
  STATUS VarChar(1) Status
  USERLINK Int(6) User Link ->OUSR
  MODIF01 nVarChar(2) Modifiers
  MODIF02 nVarChar(2) Modifiers
  MODIF03 nVarChar(2) Modifiers
  MODIF04 nVarChar(2) Modifiers
  MODIF05 nVarChar(2) Modifiers
  MODIF06 nVarChar(2) Modifiers
  MODIF07 nVarChar(2) Modifiers
  MODIF08 nVarChar(2) Modifiers
  MODIF09 nVarChar(2) Modifiers
  MODIF10 nVarChar(2) Modifiers
  MODIF11 nVarChar(2) Modifiers
  MODIF12 nVarChar(2) Modifiers
  MODIF13 nVarChar(2) Modifiers
  ATOMID01 Int(11) Autom. ID
  ATOMID02 Int(11) Autom. ID
  ATOMID03 Int(11) Autom. ID
  ATOMID04 Int(11) Autom. ID
  ATOMID05 Int(11) Autom. ID
  ATOMID06 Int(11) Autom. ID
  ATOMID07 Int(11) Autom. ID
  ATOMID08 Int(11) Autom. ID
  ATOMID09 Int(11) Autom. ID
  ATOMID10 Int(11) Autom. ID
  ATOMID11 Int(11) Autom. ID
  ATOMID12 Int(11) Autom. ID
  ATOMID13 Int(11) Autom. ID
  STRID01 Int(11) String ID
  STRID02 Int(11) String ID
  STRID03 Int(11) String ID
  STRID04 Int(11) String ID
  STRID05 Int(11) String ID
  STRID06 Int(11) String ID
  STRID07 Int(11) String ID
  STRID08 Int(11) String ID
  STRID09 Int(11) String ID
  STRID10 Int(11) String ID
  STRID11 Int(11) String ID
  STRID12 Int(11) String ID
  STRID13 Int(11) String ID
  RESERVED nVarChar(16) RESERVED
  FILLER nVarChar(16) Filler

# USR2 - Run External Application
Module: Administration | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USER_CODE
Fields (name type(len) description [values] ->parent table):
  USER_CODE nVarChar(25) Alert Code
  PATH1 Text(16) Path 1
  PATH2 Text(16) Path 2
  PATH3 Text(16) Path 3
  PATH4 Text(16) Path 4
  PATH5 Text(16) Path 5
  PATH6 Text(16) Path 6
  PATH7 Text(16) Path 7
  PATH8 Text(16) Path 8
  PATH9 Text(16) Path 9
  PATH10 Text(16) Path 10

# USR3 - User Authorization
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserLink, PermId
Fields (name type(len) description [values] ->parent table):
  UserLink Int(6) User Link ->OUSR
  PermId nVarChar(20) Authorization ID ->OUPT
  Permission VarChar(1) Authorization default=N [V=Various, F=Full, R=Read Only, N=None, U=Undefined Type]

# USR5 - User Access Log
Module: Administration | 18 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: UserCode, Action, Date, Time, SessionID
Fields (name type(len) description [values] ->parent table):
  UserCode nVarChar(25) User Code ->OUSR
  Action VarChar(1) Performed Action [I=Logon Succeeded, F=Logon Failed, O=Logoff, C=Created, S=Superuser Selected, D=Superuser Deselected, L=Locked, U=Unlocked, P=Password Changed, N=Screen Unlock Failed, T=Temporary User Change, R=Removed]
  ActionBy nVarChar(25) User Who Performed the Action
  ClientIP nVarChar(200) IP Address of Client Computer
  Date Date(8) Date
  Time Int(11) Time default=0
  ClientName nVarChar(200) Hostname of Client Computer
  ProcessID Int(11) Process ID of B1 Application default=-1
  SessionID Int(11) Connection Session ID default=-1
  ReasonID Int(11) Reason ID [1=Planned: Initial System Configuration, 2=Planned: System Configuration Change, 3=Planned: System Maintenance, 4=Planned: Knowledge Transfer to End-User, 11=Unplanned: Root Cause Analysis, 12=Unplanned: Knowledge Transfer to End-User, 13=Unplanned: System Maintenance, 14=Unplanned: System Configuration Change, 51=System Maintenance, 52=Root Cause Analysis, 53=Consulting / Support, 54=Other]
  ReasonDesc nVarChar(250) Reason Description
  WinSessnID Int(11) Client Windows Session ID default=-1
  WinUsrName nVarChar(100) User Name of Windows User
  ProcName nVarChar(80) Process Name of Logged-On App.
  AliveDurtn Int(11) Time Logged-On User Keep Alive default=0
  LogoutTime Int(11) User Logout Time
  Source nVarChar(100) Login Terminal
  UserID Int(6) User ID

# VIEWS - SQL Company Views
Module: Administration | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ViewName
Fields (name type(len) description [values] ->parent table):
  ViewName nVarChar(100) View Name
  ViewString Text(16) View String
  ViewType VarChar(1) View Type default=S [S=Static, D=Dynamic]

# WLS1 - Potential Processor of Tasks
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(6) Line ID
  Candidate nVarChar(254) Candidate
  LogIns Int(11) Log Instance
  WasRead VarChar(1) Was Read default=N [Y=Yes, N=No]
  CandExpr nVarChar(254) Candidate Expression

# WLS2 - Input data for tasks
Module: Administration | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(11) Line ID
  ObjectType nVarChar(20) Object Type
  ObjKey nVarChar(100) Object Key
  Command VarChar(1) Command default=B [B=Based On, M=Field Mapping]
  LogIns Int(11) Log Instance
  ObjSubType nVarChar(64) Object Subtype
  ObjDetail Text(16) Object Detail

# WLS3 - Notes of Tasks
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID
Fields (name type(len) description [values] ->parent table):
  WFInstID Int(11) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID Int(11) Line ID
  Note Text(16) Note
  Creator nVarChar(25) Creator
  NoteDate Date(8) Note Date
  Access VarChar(1) Accessibility default=W [W=Workflow, T=Task]
  LogIns Int(11) Log Instance

# WLS4 - Task Output Data
Module: Administration | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID
Fields (name type(len) description [values] ->parent table):
  WFInstID nVarChar(64) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID nVarChar(6) Line ID
  ObjectType nVarChar(20) Object Type
  ObjKey nVarChar(100) Object Key
  LogIns Int(11) Log Instance
  OutParamID nVarChar(64) Object ID in WF Engine
  ObjSubType nVarChar(64) Object Subtype

# WLS5 - Task Field Mapping Information
Module: Administration | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TaskID, LineID
Fields (name type(len) description [values] ->parent table):
  WFInstID nVarChar(64) Workflow Instance ID
  TaskID Int(11) Task ID ->OWLS
  LineID nVarChar(6) Line ID
  InputID Int(11) Input ID
  SrcFld nVarChar(50) Source Field
  TgtFld nVarChar(50) Target Field
  LogIns Int(11) Log Instance

# WST1 - Confirmation Level - Rows
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WstCode, UserID
Fields (name type(len) description [values] ->parent table):
  WstCode Int(11) Code ->OWST
  UserID Int(11) User Code default=-1 ->OUSR

# WTM1 - Approval Templates - Producers
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WtmCode, UserID
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  UserID Int(11) User Code default=-1 ->OUSR

# WTM2 - Confirmation Templates - Stages
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WtmCode, WstCode
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  WstCode Int(11) Stage ->OWST
  SortId Int(6) Sort Code default=1
  Remarks nVarChar(100) Description

# WTM3 - Approval Templates - Documents
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WtmCode, TransType
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  TransType nVarChar(20) Original Document [23=Sales Quotation, 17=Sales Order, 15=Delivery, 234000031=Returns Request, 16=Returns, 203=A/R Down Payment, 13=A/R Invoice, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 14=A/R Credit Memo, 132=Correction Invoice, 1470000113=Purchase Request, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 234000032=Goods Returns Request, 21=Goods Returns, 204=A/P Down Payment, 18=A/P Invoice, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 19=A/P Credit Memo, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 1470000065=Inventory Counting, 310000001=Inventory Opening Balance, 10000071=Inventory Posting, 46=Outgoing Payment, 1250000026=Sales Blanket Agreements, 1250000027=Purchase Blanket Agreements]

# WTM4 - Approval Templates - Terms
Module: Administration | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WtmCode, CondId
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  CondId Int(11) Condition No. default=0 [1=Deviation from Credit Limit, 2=Deviation from Commitment, 3=Gross Profit %, 4=Discount %, 5=Deviation from Budget, 7=Quantity, 8=Item Code, 9=Total, 6=Total Document, 10=Counted Quantity, 11=Variance, 12=Variance %, 0=Undefined Type]
  opCode Int(6) Ratio default=0 [1=Greater Than, 2=Greater or Equal, 3=Less Than, 4=Less or Equal, 5=Equal, 6=Does not Equal, 7=In Range, 8=Not in Range, 0=Undefined Type]
  opValue nVarChar(90) Value

# WTM5 - Approval Templates - Queries
Module: Administration | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: WtmCode, QueryId
Fields (name type(len) description [values] ->parent table):
  WtmCode Int(11) Code ->OWTM
  QueryId Int(11) User Query Id ->OUQR
