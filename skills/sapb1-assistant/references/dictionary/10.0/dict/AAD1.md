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
