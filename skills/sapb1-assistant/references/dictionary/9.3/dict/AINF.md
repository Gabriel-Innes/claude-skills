<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AINF - Company Info
Module: Administration | 219 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, Version
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
  BISBnkCnt nVarChar(3) BISR Bank Country
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
