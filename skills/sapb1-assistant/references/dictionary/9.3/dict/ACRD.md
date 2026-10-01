<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACRD - Business Partners - History
Module: Business Partners | 367 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, CardCode
  ABS_ENTRY U: LogInstanc, DocEntry
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  CardName nVarChar(100) BP Name
  CardType VarChar(1) BP Type default=C [C=Customer, S=Vendor, L=Lead]
  GroupCode Int(6) Group Code ->OCRG
  CmpPrivate VarChar(1) Business Partner Type default=C [C=Company, I=Private, G=Government, E=Employee]
  Address nVarChar(100) Bill-to Street
  ZipCode nVarChar(20) Bill-to Zip Code
  MailAddres nVarChar(100) Ship-to Street
  MailZipCod nVarChar(20) Ship-to Zip Code
  Phone1 nVarChar(20) Telephone 1
  Phone2 nVarChar(20) Telephone 2
  Fax nVarChar(20) Fax Number
  CntctPrsn nVarChar(90) Contact Person
  Notes nVarChar(100) Remarks
  Balance Num(19,6) Account Balance
  ChecksBal Num(19,6) Open Checks Balance
  DNotesBal Num(19,6) Open Deliveries/GRPO Balance
  OrdersBal Num(19,6) Open Orders Balance
  GroupNum Int(6) Payment Terms Code default=-1 ->OCTG
  CreditLine Num(19,6) Credit Limit
  DebtLine Num(19,6) Commitment Limit
  Discount Num(19,6) Discount %
  VatStatus VarChar(1) Tax Definition default=Y [Y=Liable, N=Exempted, E=EU]
  LicTradNum nVarChar(32) Federal Tax ID
  DdctStatus VarChar(1) Liable for Ded. at Source default=N [Y=Yes, N=No]
  DdctPrcnt Num(19,6) % Withholding Tax Deduction
  ValidUntil Date(8) Expiration Date for -% of Deduction
  Chrctrstcs Int(11) Properties
  ExMatchNum Int(11) Last Ext. Reconciliation No.
  InMatchNum Int(11) Last Int. Reconciliation No.
  ListNum Int(6) Price List No. ->OPLN
  DNoteBalFC Num(19,6) Open DN Balance (BP Currency)
  OrderBalFC Num(19,6) Open Orders Balance (BP Crcy)
  DNoteBalSy Num(19,6) Open Deliveries/GRPO Balance in SC
  OrderBalSy Num(19,6) Open Orders Balance in SC
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  BalTrnsfrd VarChar(1) Balances Transferred default=N [Y=Yes, N=No]
  IntrstRate Num(19,6) Interest % on Liabilities
  Commission Num(19,6) Commission % for Customer
  CommGrCode Int(6) Commission Group default=0 ->OCOG
  Free_Text Text(16) Free Text
  SlpCode Int(11) Sales Employee Code default=-1 ->OSLP
  PrevYearAc VarChar(1) Previous Year Balance default=N [Y=Yes, N=No]
  Currency nVarChar(3) BP Currency ->OCRN
  RateDifAct nVarChar(15) Rate Differences Account ->OACT
  BalanceSys Num(19,6) Account Balance in SC
  BalanceFC Num(19,6) BP Balance in FC
  Protected VarChar(1) Protected BP default=N [Y=Yes, N=No]
  Cellular nVarChar(50) Mobile Phone Number
  AvrageLate Int(6) Average Payment Delay in Days
  City nVarChar(100) Bill-to City
  County nVarChar(100) Bill-to County
  Country nVarChar(3) Bill-to Country
  MailCity nVarChar(100) Ship-to City
  MailCounty nVarChar(100) Ship-to County
  MailCountr nVarChar(3) Ship-to Country
  E_Mail nVarChar(100) E-Mail
  Picture nVarChar(200) Picture
  DflAccount nVarChar(50) Default Account
  DflBranch nVarChar(50) Default Branch
  BankCode nVarChar(30) Default Bank default=-1
  AddID nVarChar(64) ID No. 2
  Pager nVarChar(30) Pager No.
  FatherCard nVarChar(15) Consolidating BP ->OCRD
  CardFName nVarChar(100) Foreign Name
  FatherType VarChar(1) Parent Summary Type default=P [P=Payment Consolidation, D=Delivery Consolidation]
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
  DdctOffice nVarChar(10) Deduction Approval Office
  CreateDate Date(8) Creation Date
  UpdateDate Date(8) Date of Update
  ExportCode nVarChar(8) Data Export Code
  DscntObjct Int(6) Subject for Discount default=-1 [-1=, 52=Groups, 8=Properties, 43=Companies, 4=Items]
  DscntRel VarChar(1) Discounts Ratio default=L [L=Lowest Discount, H=Highest Discount, A=Average Disc., S=Discount Totals, M=Discount Multiples]
  SPGCounter Int(6) SPG Counter
  SPPCounter Int(11) SPP Counter
  DdctFileNo nVarChar(9) Tax Deduction File No.
  SCNCounter Int(6) SCN Counter
  MinIntrst Num(19,6) Min. Interest Letter Amount
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  OprCount Int(11) Open Opportunities
  ExemptNo nVarChar(50) Exempt No.
  Priority Int(11) Priority default=-1 ->OBPP
  CreditCard Int(6) Credit Cards default=-1 ->OCRC
  CrCardNum nVarChar(64) Credit Card No.
  CardValid Date(8) Credit Card Validity
  UserSign Int(6) User Signature ->OUSR
  LocMth VarChar(1) Reconciliation (LC) default=Y [Y=Yes, N=No]
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  sEmployed VarChar(1) Self-Employed default=N [Y=Yes, N=No]
  MTHCounter Int(11) Match History Counter
  BNKCounter Int(11) BNK Counter
  DdgKey Int(11) WTax Deduction - Group default=-1 ->ODDG
  DdtKey Int(11) Current Deduction Hierarchy default=-1
  ValidComm nVarChar(30) Active Remarks
  FrozenComm nVarChar(30) Inactive Remarks
  chainStore VarChar(1) Belongs to Retail Store default=N [Y=Yes, N=No]
  DiscInRet VarChar(1) Allow Doc Discount in Returns default=N [Y=Yes, N=No]
  State1 nVarChar(3) Bill-to State ->OCST
  State2 nVarChar(3) Ship-to State ->OCST
  VatGroup nVarChar(8) Tax Code ->OSTC
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=2 ->ADP1
  Indicator nVarChar(2) Indicator ->OIDC
  ShipType Int(6) Shipping Type ->OSHP
  DebPayAcct nVarChar(15) Control Account ->OACT
  ShipToDef nVarChar(50) Ship to - Default
  Block nVarChar(100) Block
  MailBlock nVarChar(100) Delivery Block
  Password nVarChar(32) Password
  ECVatGroup nVarChar(8) Tax Group ->OVTG
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  IBAN nVarChar(50) IBAN
  DocEntry Int(11) Numerator
  FormCode Int(11) 1099 Form Code ->OTNN
  Box1099 nVarChar(20) 1099 Box
  PymCode nVarChar(15) Payment Method Code default=-1 ->OPYM
  BackOrder VarChar(1) Backorder default=Y [Y=Yes, N=No]
  PartDelivr VarChar(1) Partial Delivery default=Y [Y=Yes, N=No]
  DunnLevel Int(11) Dunning Level ->ODUN
  DunnDate Date(8) Dunning Date
  BlockDunn VarChar(1) Block Dunning default=N [Y=Yes, N=No]
  BankCountr nVarChar(3) Bank Country ->OCRY
  CollecAuth VarChar(1) Collection Authorization default=N [N=No, Y=Yes]
  DME nVarChar(5) DME Identification
  InstrucKey nVarChar(30) Instruction Key
  SinglePaym VarChar(1) Single Payment default=N [N=No, Y=Yes]
  ISRBillId nVarChar(9) ISR Biller ID
  PaymBlock VarChar(1) Payment Block default=N [N=No, Y=Yes]
  RefDetails nVarChar(20) Reference Details
  HouseBank nVarChar(30) House Bank default=-1
  OwnerIdNum nVarChar(15) ID Number
  PyBlckDesc Int(11) Payment Block Description default=-1 ->OPYB
  HousBnkCry nVarChar(3) House Bank Country
  HousBnkAct nVarChar(50) House Bank Account
  HousBnkBrn nVarChar(50) House Bank Branch
  ProjectCod nVarChar(20) Project Code ->OPRJ
  SysMatchNo Int(11) Last Sys. Reconciliation No. default=-1
  VatIdUnCmp nVarChar(32) VAT ID for Unified Company
  AgentCode nVarChar(32) Agent Code ->OAGP
  TolrncDays Int(6) Tolerance Days
  SelfInvoic VarChar(1) Self Invoice
  DeferrTax VarChar(1) Deferred Tax [Y=Yes, N=No]
  LetterNum nVarChar(20) Tax Exemption Letter No.
  MaxAmount Num(19,6) Max. Exemption Amount
  FromDate Date(8) Exemption Validity Date From
  ToDate Date(8) Exemption Validity Date To
  WTLiable VarChar(1) Subject to Withholding Tax [Y=Yes, N=No]
  CrtfcateNO nVarChar(20) Certificate Number
  ExpireDate Date(8) Expiration Date
  NINum nVarChar(20) Registration No.
  AccCritria VarChar(1) Accrued Criteria default=N [Y=Yes, N=No]
  WTCode nVarChar(4) Withholding Tax Code ->OWHT
  Equ VarChar(1) Equalization Tax default=N [Y=Yes, N=No]
  HldCode nVarChar(20) Holiday Set Name ->OHLD
  ConnBP nVarChar(15) Linked Business Partner ->OCRD
  MltMthNum Int(11) Last Multi. Reconciliation No.
  TypWTReprt VarChar(1) BP Type for WTax Report default=C [C=Company, P=Person]
  VATRegNum nVarChar(32) VAT Reg. Number
  RepName nVarChar(15) Representative Name
  Industry Text(16) Industry
  Business Text(16) Business
  WTTaxCat Text(16) Withholding Tax Cat.
  IsDomestic VarChar(1) Is Domestic default=Y [Y=Domestic, N=Foreign]
  IsResident VarChar(1) Is Resident default=Y [Y=Resident, N=Non-Resident]
  AutoCalBCG VarChar(1) Auto Calculated Bank Charges default=N [N=No, Y=Yes]
  OtrCtlAcct nVarChar(15) Other Receivable/Payable ->OACT
  AliasName Text(16) Alias Name
  Building Text(16) Bill-to Building/Floor/Room
  MailBuildi Text(16) Ship to Building/Floor/Room
  BoEPrsnt nVarChar(15) Customer BoE Presentation ->OACT
  BoEDiscnt nVarChar(15) Customer BoE Discounted ->OACT
  BoEOnClct nVarChar(15) Bill of Exchange on Collection ->OACT
  UnpaidBoE nVarChar(15) Unpaid Bill of Exchange ->OACT
  ITWTCode nVarChar(4) Income Tax WTax Code ->OWHT
  DunTerm nVarChar(25) Dunning Term ->ODUT
  ChannlBP nVarChar(15) Channel BP ->OCRD
  DfTcnician Int(11) Default Technician ->OHEM
  Territory Int(11) Territory ->OTER
  BillToDef nVarChar(50) Bill-to Default
  DpmClear nVarChar(15) Payment Advances ->OACT
  IntrntSite nVarChar(100) Web Site
  LangCode Int(11) Language Code ->OLNG
  HousActKey Int(11) House Bank Account Key ->DSC1
  Profession nVarChar(50) Profession
  CDPNum Int(6) Closing Date Procedure No. ->OCDP
  DflBankKey Int(11) Default Bank ID ->ODSC
  BCACode nVarChar(3) Bank Charges Allocation Codes ->OBCA
  UseShpdGd VarChar(1) Use Shipped Goods Account default=Y [Y=Yes, N=No]
  RegNum nVarChar(32) Company Reg. No. (CRN)
  VerifNum nVarChar(32) Verification No.
  BankCtlKey nVarChar(2) Default Bank Internal ID
  HousCtlKey nVarChar(2) House Bank Control Number
  AddrType nVarChar(100) Bill-to Address Type
  InsurOp347 VarChar(1) 347 Insurance Operation default=N [N=No, Y=Yes]
  MailAddrTy nVarChar(100) Ship-to Address Type
  StreetNo nVarChar(100) Bill-to Street No.
  MailStrNo nVarChar(100) Ship-to Street No.
  TaxRndRule VarChar(1) Tax Rounding Rule default=D [D=Company Default, R=Round Off, C=Round Up, F=Round Down]
  VendTID Int(11) Vender Type ID ->OVTP
  ThreshOver VarChar(1) Threshold Overlook default=N [Y=Yes, N=No]
  SurOver VarChar(1) Surcharge Overlook default=N [Y=Yes, N=No]
  VendorOcup nVarChar(15) Vendor Occupation
  OpCode347 VarChar(1) 347 Operation Code [A=Goods or Services Acquisitions, D=Public Entities Acquisitions, G=Travel Agent Purchases, B=Sales or Services Revenues, E=Public Subsidies, F=Travel Agent Sales]
  DpmIntAct nVarChar(15) DPM Interim Account ->OACT
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Country of Residence, 5=Certificate of Fiscal Residence, 6=Other Document]
  UserSign2 Int(6) Updating User ->OUSR
  PlngGroup nVarChar(10) Planning Group
  VatIDNum nVarChar(32) VAT ID Number
  Affiliate VarChar(1) Affiliate default=N [Y=Yes, N=No]
  MivzExpSts VarChar(1) Mivzak Export Status default=B [B=Not Exported, U=Exported, D=Deleted]
  HierchDdct VarChar(1) Hierarchical Deduction default=Y [Y=Yes, N=No]
  CertWHT VarChar(1) Withholding Tax Certified default=N [Y=Yes, N=No]
  CertBKeep VarChar(1) Bookkeeping Certified default=N [Y=Yes, N=No]
  WHShaamGrp VarChar(1) Withholding Shaam Group default=1 [1=Services and Asset, 2=Agricultural Products, 3=Insurance Commissions, 4=Withholding Tax Instructions, 5=Interest Exchange Rate Differences]
  IndustryC Int(11) Industry ->OOND
  DatevAcct nVarChar(9) DATEV Account
  DatevFirst VarChar(1) First Data Entry default=Y [Y=Yes, N=No]
  GTSRegNum nVarChar(20) GTS Registration Number
  GTSBankAct nVarChar(80) GTS Bank Account
  GTSBilAddr nVarChar(80) GTS Billing Address
  HsBnkSwift nVarChar(50) House Bank BIC/SWIFT Code
  HsBnkIBAN nVarChar(50) House Bank IBAN
  DflSwift nVarChar(50) Default Bank BIC/SWIFT Code
  AutoPost VarChar(1) Automatic Posting default=N [N=No, B=Interest and Fee, I=Interest Only, F=Fee Only]
  IntrAcc nVarChar(15) Interest Account
  FeeAcc nVarChar(15) Fee Account
  CpnNo Int(11) Campaign No. ->OCPN
  NTSWebSite Int(6) E-Tax Web Site ->OTWS
  DflIBAN nVarChar(50) Default Bank IBAN
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  EDocExpFrm Int(11) Electronic Doc. Export Format
  TaxIdIdent VarChar(1) Tax ID Category default=3 [1=Self-Employed, 2=Company, 3=Registered Business, 5=International Company]
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  DiscRel VarChar(1) Disc. Relations default=L [L=Lowest Discount, H=Highest Discount, A=Average, S=Total, M=Discount Multiples]
  NoDiscount VarChar(1) No Discounts default=N [Y=Yes, N=No]
  SCAdjust VarChar(1) SC Adjustment default=N [Y=Yes, N=No]
  DflAgrmnt Int(11) Default Blanket Agreement No. ->OOAT
  GlblLocNum nVarChar(50) Global Location Number
  SenderID nVarChar(50) EDI Message Sender ID
  RcpntID nVarChar(50) EDI Message Recipient ID
  MainUsage Int(11) Main Usage
  SefazCheck VarChar(1) Check BP Status on SEFAZ default=N [Y=Yes, N=No]
  free312 VarChar(1) Reply from SEFAZ
  free313 VarChar(1) Date of Update from SEFAZ
  DateFrom Date(8) Relationship Initial Date
  DateTill Date(8) Relationship Final Date
  RelCode nVarChar(2) Relationship Code [01=Matriz no exterior, 02=Filial, inclusive agência ou dependência, no exterior, 03=Coligada, inclusive equiparada, 04=Controladora, 05=Controlada (exceto subsidiária integral), 06=Subsidiária integral, 07=Controlada em conjunto, 08=Entidade de Propósito Específico (conforme definição da CVM), 09=Participante do conglomerado, conforme norma específica do órgão regulador, exceto as que se enquadrem nos tipos precedentes, 10=Vinculadas (Art. 23 da Lei 9.430/96), exceto as que se enquadrem nos tipos precedentes, 11=Localizada em país com tributação favorecida (Art. 24 da Lei 9.430/96), exceto as que se enquadrem nos tipos precedentes]
  OKATO nVarChar(11) OKATO
  OKTMO nVarChar(12) OKTMO
  KBKCode nVarChar(20) KBK Budget Classification Code
  TypeOfOp VarChar(1) Type of Operation [P=Professional Services, R=Renting Assets, O=Others]
  OwnerCode Int(11) BP Owner ->OHEM
  MandateID nVarChar(35) Mandate ID
  SignDate Date(8) Date of Signature
  Remark1 Int(11) Remark 1 ->ORMK
  ConCerti nVarChar(20) Concessional Certificate
  TpCusPres Int(11) Type of End-User Presence default=9 ->OBNI
  RoleTypCod nVarChar(2) Role Type Code
  BlockComm VarChar(1) Block Sending Marketing default=N [N=No, Y=Yes]
  EmplymntCt nVarChar(2) Employment Category [A=Retired, B=Retired belonging to "casellario", C=University Teacher, D=High School Teacher, E=Primary or Kindergarten Teacher, F=Graduates and Troops, G=Military Subofficer, H=Military Officer, K=Judge, L=Employees Abroad, M=Member of Cooperatives, N=Freelance Earning Amounts as Employee, P=Scholarships Beneficiary, Q=Minister, R=Doctor, S=Freelance Earning Amounts from State, Regions, Cities, T=Compensation to Elective Officers, T1=Compensation to Parliament Member, T2=Annuity Check to Parliament Member, T3=Annuity Check to Parliament Member Having Terminated Mandate During the Year, T4=Constitutional Court, U=Workers Earning Annuity and Income, V=Earning Supplementary Annuity, W=Earning Annuity Check, Y=Workers Engaged in Community Services, Z=Heir/Successor, Z1=Heir/Successor - Not Resident, Z2=Former Spouse, Z3=Artisan Cooperative Members]
  ExcptnlEvt VarChar(1) Exceptional Event [1=Vittime di richieste estorsive, 2=Soggetti colpiti dagli eventi sismici in data 24 agosto 2016, 3=Soggetti nel comune di Lampedusa e Linosa, emergenza umanitaria, 4=Soggetti colpiti dagli eventi sismici in ottobre 2016, 6=Altri eventi eccezionali]
  ExpnPrfFnd Num(19,6) Professional Funds Expenses
  EdrsFromBP VarChar(1) Endorsable Checks from This BP default=Y [N=No, Y=Yes]
  EdrsToBP VarChar(1) This BP Accepts Endorsed Checks default=N [N=No, Y=Yes]
  CreateTS Int(11) Creatn Time - Incl. Secs
  UpdateTS Int(11) Update Full Time
  EDocGenTyp VarChar(1) Electr. Doc. Generation Type [N=Not Relevant, G=Generate, L=Generate - Later, S=Send, R=Send - Later]
  eStreet nVarChar(38) Street
  eStreetNum nVarChar(4) Street Number
  eBuildnNum Int(11) Building Number
  eZipCode nVarChar(10) Zip Code
  eCityTown nVarChar(48) City/Town/Village
  eCountry nVarChar(3) Country ->OCRY
  eDistrict nVarChar(3) District
  RepFName nVarChar(20) Representative First Name
  RepSName nVarChar(36) Representative Surname
  RepCmpName nVarChar(36) Company Name
  RepFisCode nVarChar(16) Representative Fiscal Code
  RepAddID nVarChar(28) Representative Additional ID
  PECAddr nVarChar(254) PEC Address
  IPACodePA nVarChar(32) Receiver Code for Public Administration
  PriceMode VarChar(1) Price Mode [G=Gross, N=Net]
  EffecPrice VarChar(1) Effective Price default=D [D=Default Priority, L=Lowest Price, H=Highest Price]
  TxExMxVdTp VarChar(1) Exemption Max validate type default=I [I=Individual Documents, A=Accumulated Document Amount]
  MerchantID nVarChar(15) Merchant ID
  UseBilAddr VarChar(1) Determine GST by Using Bill to default=N [Y=Yes, N=No]
  NaturalPer VarChar(1) Natural Person default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  EnAddID Text(16) Encryption of ID No. 2
  EncryptIV nVarChar(100) Encrypt IV
  EnDflAccnt Text(16) Encryption of Default Account
  EnDflIBAN Text(16) Encryption of Default IBAN
  EnERD4In VarChar(1) Enable ERD for Incoming Payments default=Y [Y=Yes, N=No]
  EnERD4Out VarChar(1) Enable ERD for Outgoing Payments default=Y [Y=Yes, N=No]
  DflCustomr VarChar(1) Default Customer default=N [N=Not a default customer, D=Default customer, P=Partially erased, C=Default customer who has been partially erased]
  TspEntry Int(11) Default Transporter
  TspLine Int(11) Default Transportation Line
