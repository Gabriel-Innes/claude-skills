<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ADM2 - Administration Electronic Report
Module: Administration | 67 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  TaxAuCod nVarChar(5) Tax Authority Code
  KeyEcoAct nVarChar(10) Key Economic Activity
  TaxPayType VarChar(1) Tax Payer Type default=P [P=§94, I=§96, S=§95a]
  TaxLegForm VarChar(1) Tax Payer Legal Form default=P [F=Sole Proprietorship, P=Company]
  RegName nVarChar(254) Registered Name
  RegNameExt nVarChar(11) Registered Name Extension
  SoleFName nVarChar(20) Sole Proprietor First Name
  SoleSName nVarChar(36) Sole Proprietor Surname
  SoleTitle nVarChar(10) Sole Proprietor Title
  CityTown nVarChar(48) City/Town/Village
  ZipCode nVarChar(10) Zip Code
  Telephone nVarChar(14) Telephone
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
  TaxPayAttr VarChar(1) Taxpayer Attribute
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
  Country nVarChar(3) Country ->OCRY
  District nVarChar(3) District ->OCST
  RegDistri nVarChar(3) Register District
  RegSCAmnt Num(19,6) Share Capital Amount
  RegSHolder nVarChar(2) Shareholder default=SU [SU=Sole Shareholder, SM=Several Shareholders]
  RegLiquida nVarChar(2) Liquidation default=LN [LS=In Liquidation, LN=Not in Liquidation]
  RepAddID nVarChar(28) Representative Additional ID
  ActCode nVarChar(6) Activity Code
  PosCode347 nVarChar(2) Position Code for Report 347 [1=1, 2=2, 3=3, 4=4, 5=5, 6=6, 7=7, 8=8, 9=9, 10=10, 11=11, 12=12, 13=13, 14=14, 15=15]
  FiscalCode nVarChar(16) Fiscal Code
  DataBoxID nVarChar(10) Data Box ID
  SmValLimit Num(19,6) Small Value Documents Limit
  RepCEOName nVarChar(254) Representative CEO Name
  RepCEOFisC nVarChar(16) Representative CEO Fiscal Code
