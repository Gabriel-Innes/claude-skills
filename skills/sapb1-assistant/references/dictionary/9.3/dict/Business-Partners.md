<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->

# ABPL - Business Place
Module: Business Partners | 55 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, BPLId
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) Branch ID
  BPLName nVarChar(100) Branch Name
  BPLFrName nVarChar(100) Branch Name (Foreign)
  VATRegNum nVarChar(12) VAT Reg. Number
  RepName nVarChar(15) Rep. Name
  Industry nVarChar(20) Industry
  Business nVarChar(20) Business
  Address nVarChar(254) Address
  AddressFr nVarChar(254) Address (Foreign)
  MainBPL VarChar(1) Main BPL default=N [Y=Main Business Place, N=Not Main Business Place]
  TxOffcNo nVarChar(3) Tax Office No.
  Disabled VarChar(1) Disabled default=N [Y=Disabled, N=Enabled]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  DflCust nVarChar(15) Default Customer ID ->OCRD
  DflVendor nVarChar(15) Default Vendor ID ->OCRD
  DflWhs nVarChar(8) Default Warehouse ID ->OWHS
  DflTaxCode nVarChar(8) Default Tax Code ->OCNA
  RevOffice nVarChar(100) Tax Office
  TaxIdNum nVarChar(32) Federal Tax ID
  TaxIdNum2 nVarChar(32) Federal Tax ID 2
  TaxIdNum3 nVarChar(32) Federal Tax ID 3
  AddtnlId nVarChar(32) Additional ID Number
  CompNature Int(11) Nature of Company default=-1 ->OBNI
  EconActT Int(11) Economic Activity Type default=-1 ->OBNI
  CredCOrig nVarChar(2) Credit Contribution Origin ->OBSI
  IPIPeriod nVarChar(2) IPI Period ->OBSI
  CoopAssocT Int(11) Cooperative Association Type default=-1 ->OBNI
  PrefState nVarChar(3) Default State
  ProfTax Int(11) Profit Taxation default=-1 ->OBNI
  CompQualif Int(11) Company Qualification default=-1 ->OBNI
  DeclType Int(11) Declarer Type default=-1 ->OBNI
  AddrType nVarChar(100) Address Type
  Street nVarChar(100) Street
  StreetNo nVarChar(100) Street No.
  Building nVarChar(100) Building/Floor/Room
  ZipCode nVarChar(20) Zip Code
  Block nVarChar(100) Block
  City nVarChar(100) City
  State nVarChar(3) State
  County nVarChar(100) County ->OCNT
  Country nVarChar(3) Country ->OCST
  PmtClrAct nVarChar(15) Payment Clearing Account ->OACT
  CommerReg nVarChar(60) Commercial Register
  DateOfInc Date(8) Date of Incorporation
  SPEDProf nVarChar(2) SPED Profile ->OBSI
  EnvTypeNFe Int(11) Environment Type NFe default=-1 ->OBNI
  Opt4ICMS VarChar(1) Opting for ICMS 115_03 default=N
  AliasName Text(16) Alias Name
  GlblLocNum nVarChar(50) Global Location Number
  TaxRptFrm Date(8) Tax Wizard Reporting From
  Suframa nVarChar(100) SUFRAMA
  DfltResWhs nVarChar(8) Default Resource Warehouse ID ->OWHS
  SnapshotId Int(11) Snapshot ID default=0

# ACL1 - Activity Check-ins
Module: Business Partners | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, ClgCode
Fields (name type(len) description [values] ->parent table):
  ClgCode Int(11) Activity Number ->OCLG
  LineNum Int(11) Line Number
  Date Date(8) Date
  Location nVarChar(254) Location
  Latitude nVarChar(13) Latitude
  Longitude nVarChar(14) Longitude
  Time Int(11) Time
  OwnerUser Int(6) Owner User ->OUSR
  OwnerEmp Int(11) Owner Employee ->OHEM
  LogInstanc Int(11) Log Instance default=0

# ACLG - Activities - History
Module: Business Partners | 93 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ClgCode
  CRD_CODE: CardCode
  OPPORT: OprLine, OprId
Fields (name type(len) description [values] ->parent table):
  ClgCode Int(11) Activity Number
  CardCode nVarChar(15) BP Code ->OCRD
  Notes Text(16) Remarks
  CntctDate Date(8) System Date
  CntctTime Int(11) Time
  Recontact Date(8) Activity Date
  Closed VarChar(1) Closed Activity default=N [Y=Yes, N=No]
  CloseDate Date(8) Closing Date
  ContactPer nVarChar(90) Contact Person Name
  Tel nVarChar(50) Telephone
  Fax nVarChar(20) Fax
  CntctSbjct Int(6) Activity Subject default=-1 ->OCLS
  Transfered VarChar(1) Transferred to Next Year default=N [Y=Yes, N=No]
  DocType nVarChar(20) Linked Document default=-1 [13=A/R Invoice, 14=A/R Credit Memo, 15=Delivery, 16=Return, 17=Sales Order, 18=A/P Invoice, 19=A/P Credit Memo, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase order, 23=Sales Quotation, 24=Incoming Payment, 25=Deposit, 30=Journal Entry, 46=Outgoing Payment, 57=Checks for Payment, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 68=Work Order, 69=Landed Costs, 132=Correction Invoice, 162=Material Revaluation, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment, 140000009=Outgoing Excise Invoice, 140000010=Incoming Excise Invoice, -1=, 0=, 4=Items, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 1320000012=Campaign, 540000006=Purchase Quotation, 1250000025=Blanket Agreements, 1470000113=Purchase Request, 112=Document Drafts, 140=Payment Drafts, 123=Checks for Payment Drafts]
  DocNum nVarChar(50) Linked Document Number
  DocEntry nVarChar(50) Linked Document Entry
  Attachment Text(16) Attachment
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AttendUser Int(6) Dealt by ->OUSR
  CntctCode Int(11) Contact Person ->OCPR
  UserSign Int(6) User Signature
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  Action VarChar(1) Activity default=C [C=Phone Call, M=Meeting, T=Task, E=Note, P=Campaign, N=Other]
  Details nVarChar(100) Details
  CntctType Int(6) Activity Type default=-1 ->OCLT
  Location Int(6) Location default=-1 ->OCLO
  BeginTime Int(11) Start Time
  Duration Num(19,6) Activity Duration
  DurType VarChar(1) Duration UoM default=M [M=Minutes, H=Hours, D=Days]
  ENDTime Int(11) End Time
  Priority VarChar(1) Priority default=1 [0=Low, 1=Normal, 2=High]
  Reminder VarChar(1) Reminder default=N [Y=Yes, N=No]
  RemQty Num(19,6) Reminder Quantity
  RemType VarChar(1) Reminder Units default=M [M=Minutes, H=Hours, D=Days]
  OprId Int(11) Opportunity - Key
  OprLine Int(6) Row No. - Opportunity
  RemDate Date(8) Reminder Date
  RemTime Int(6) Reminder Time
  RemSented VarChar(1) Reminder Was Sent default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  endDate Date(8) End/Due Date
  status Int(11) Status ->OCLA
  personal VarChar(1) Personal Flag default=N [Y=Yes, N=No]
  inactive VarChar(1) Inactive Flag default=N [Y=Yes, N=No]
  tentative VarChar(1) Tentative Flag default=N [Y=Yes, N=No]
  street nVarChar(100) Street
  city nVarChar(100) City
  country nVarChar(3) Country ->OCRY
  state nVarChar(3) State ->OCST
  room nVarChar(50) Room
  parentType nVarChar(20) Parent Object Type
  parentId Int(11) Parent Object ID
  prevActvty Int(11) Previous Activity
  AtcEntry Int(11) Attachment Entry
  RecurPat VarChar(1) Recurrence Pattern default=N [N=None, D=Daily, W=Weekly, M=Monthly, A=Annually]
  EndType VarChar(1) Recurrence End Type default=N [N=No End Date, C=By Counter, D=By Date]
  SeStartDat Date(8) Series Start Date
  SeEndDat Date(8) Series End Date
  MaxOccur Int(11) Max. Occurrences
  Interval Int(11) Interval default=1
  Sunday VarChar(1) Sunday default=N [N=No, Y=Yes]
  Monday VarChar(1) Monday default=N [N=No, Y=Yes]
  Tuesday VarChar(1) Tuesday default=N [N=No, Y=Yes]
  Wednesday VarChar(1) Wednesday default=N [N=No, Y=Yes]
  Thursday VarChar(1) Thursday default=N [N=No, Y=Yes]
  Friday VarChar(1) Friday default=N [N=No, Y=Yes]
  Saturday VarChar(1) Saturday default=N [N=No, Y=Yes]
  SubOption VarChar(1) Suboption default=1 [1=Option 1, 2=Option 2]
  DayInMonth Int(11) Repeat Day in Month
  Month Int(11) Repeat Month
  DayOfWeek Int(11) Repeat Day of Week
  Week Int(11) Repeat Week in Month [1=First, 2=Second, 3=Third, 4=Fourth, 5=Last]
  SeriesNum Int(11) Series Number
  OrigDate Date(8) Original Date
  IsRemoved VarChar(1) Removed Flag default=N [N=No, Y=Yes]
  LastRemind Date(8) Last Reminder Date
  AssignedBy Int(6) Assigned By ->OUSR
  AddrName nVarChar(50) Address Name
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill To]
  AttendEmpl Int(11) Dealt by Employee ->OHEM
  NextDate Date(8) Date of Next Occurrence
  NextTime Int(6) Time of Next Occurrence
  OwnerCode Int(11) Activities Owner ->OHEM
  AttendReci Int(11) Attend Recipient ->ORCI
  ActType Int(11) Activity Type ->PMC5
  LaborItem nVarChar(50) Labor Item No.
  ResCode nVarChar(50) Resource Code from ORSC ->ORSC
  FIPROJECT nVarChar(20) Financial Project ->OPRJ
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  CreateDate Date(8) Creation Date

# ACP1 - Campaign - BPs
Module: Business Partners | 45 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CpnLineNum, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  BpCode nVarChar(15) BP Code ->OCRD
  BpName nVarChar(100) BP Name
  GroupName nVarChar(20) BP Group Name
  Industry nVarChar(15) BP Industry Name
  Status VarChar(1) BP Status [A=Active, I=Inactive]
  CntCode nVarChar(50) Contact Code
  CntTitle nVarChar(10) Contact Title
  CntPstn nVarChar(90) Contact Position
  CntEmail nVarChar(100) Contact E-Mail
  CntTel nVarChar(20) Contact Telephone
  CntMobile nVarChar(50) Contact Mobile
  CntFax nVarChar(20) Contact Fax
  CntAddr nVarChar(100) Contact Address
  Response VarChar(1) Response from Company default=N [Y=Yes, N=No]
  OpprId Int(11) Related Opportunity ->OOPR
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  City nVarChar(100) City
  ZipCode nVarChar(100) Zip Code
  County nVarChar(100) County
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country ->OCRY
  Building Text(16) Building/Floor/Room
  CActivity VarChar(1) Create Activity [Y/N] default=Y
  DocType nVarChar(20) Document Type default=-1 [E=, P=Opportunities, Q=Sales Quotations, O=Sales Orders, D=Deliveries, I=A/R Invoices, -97=Purchase Opportunities, 540000006=Purchase Quotations, 22=Purchase Orders, 20=Goods Receipt POs, 18=A/P Invoices]
  ShowBPDoc VarChar(1) Show BP Documents [Y/N] default=N
  DocNumber Int(11) Related Document
  DocEntry Int(11) Document Entry
  AssignTo VarChar(1) Assign to User or Employee default=U [U=User, E=Employee]
  AssignName Int(11) User or Employee Name
  FirstName nVarChar(50) First Name
  MiddleName nVarChar(50) Middle Name
  LastName nVarChar(50) Last Name
  LicTradNum nVarChar(32) Federal Tax ID
  AddrType nVarChar(100) Address Type
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  StreetNo nVarChar(100) Street No.
  AddressID nVarChar(50) Address ID
  RspType nVarChar(20) Response Type ->ORPT
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]

# ACP2 - Campaign - Items
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CpnLineNum, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  ItemType VarChar(1) Item Type [I=Items, L=Labor, T=Travel]
  ItemGrp nVarChar(20) Item Group
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# ACP3 - Campaign - Partners
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CpnLineNum, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  ParterId Int(11) Partners ->OPRT
  OrlCode Int(11) Relationship Code ->OORL
  RelatCard nVarChar(15) Related BP ->OCRD
  Memo nVarChar(50) Details
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# ACPN - Campaign
Module: Business Partners | 27 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogIns, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No.
  Name nVarChar(100) Campaign Name
  Type VarChar(1) Campaign Type default=E [E=E-Mail, M=Mail, F=Fax, P=Phone Call, T=Meeting, S=SMS, W=Web, O=Other]
  TargetGrp nVarChar(20) Target Group ->OTGG
  Owner Int(11) Campaign Owner ->OHEM
  Status VarChar(1) Campaign Status default=O [O=Open, F=Finished, C=Canceled]
  StartDate Date(8) Campaign Start Date
  FinishDate Date(8) Campaign Finish Date
  Remarks Text(16) Campaign Remarks
  WizardGen VarChar(1) Generated by Wizard default=N [Y=Yes, N=No]
  Template Text(16) Campaign Template
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachments
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Create Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, P=Partner Implementation, T=Year of Transfer]
  Transfered VarChar(1) Year Transfer default=N
  Instance Int(6) Instance default=0
  Url Text(16) Web Link
  TmplPath nVarChar(254) Template Path
  TargetType VarChar(1) Target Group Type default=C [C=Customer, S=Vendor]
  ExeOption VarChar(1) Execute Option default=O [L=Generate External List, O=Send E-Mail Using Microsoft Office Outlook, B=Send E-Mail Using SAP Business One Mail, F=Send Fax, U=Generate URL]
  Executed VarChar(1) Executed [Y=Yes, N=No]
  VersionNum nVarChar(11) Version Number

# ACPR - Contact Persons - History
Module: Business Partners | 50 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, CntctCode
Fields (name type(len) description [values] ->parent table):
  CntctCode Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  Name nVarChar(50) Contact Person Name
  Position nVarChar(90) Position
  Address nVarChar(100) Address
  Tel1 nVarChar(20) Telephone 1
  Tel2 nVarChar(20) Telephone 2
  Cellolar nVarChar(50) Mobile Phone Number
  Fax nVarChar(20) Fax Number
  E_MailL nVarChar(100) E-Mail
  Pager nVarChar(30) Pager
  Notes1 nVarChar(100) Remark 1
  Notes2 nVarChar(100) Remark 2
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Password nVarChar(8) Password
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type ->ADP1
  BirthPlace nVarChar(100) Place of Birth
  BirthDate Date(8) Date of Birth
  Gender VarChar(1) Gender default=E [M=Male, F=Female, E=, *=Masked]
  Profession nVarChar(50) Profession
  updateDate Date(8) Date of Update
  updateTime Int(11) Update Time
  Title nVarChar(10) Title
  BirthCity nVarChar(100) City of Birth
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  FirstName nVarChar(50) First Name
  MiddleName nVarChar(50) Middle Name
  LastName nVarChar(50) Last Name
  BirthState nVarChar(3) State of Birth ->OCST
  ResidCity nVarChar(100) City of Residence
  ResidCntry nVarChar(100) Country of Residence
  ResidState nVarChar(3) State of Residence ->OCST
  NFeRcpn VarChar(1) NF-e Recipient default=N [Y=Yes, N=No]
  EmlGrpCode nVarChar(20) E-Mail Group Code ->OEGP
  BlockComm VarChar(1) Block Sending Marketing default=N [N=No, Y=Yes]
  FiscalCode nVarChar(16) Fiscal Code for Resident
  CtyPrvsYr nVarChar(100) City for Previous Year
  SttPrvsYr nVarChar(3) State for Previous Year ->OCST
  CtyCdPrvsY nVarChar(4) City Code for Previous Year
  CtyCurYr nVarChar(100) City for Current Year
  SttCurYr nVarChar(3) State for Current Year ->OCST
  CtyCdCurYr nVarChar(4) City Code for Current Year
  NotResdSch VarChar(1) Not resident Schumacker [Y=Yes, N=No]
  CtyFsnCode nVarChar(100) Fusione comuni
  NaturalPer VarChar(1) Natural Person default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time Incl. Sec.

# ACR1 - Business Partner Addresses - History
Module: Business Partners | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AdresType, Address, CardCode
Fields (name type(len) description [values] ->parent table):
  Address nVarChar(50) Address Name
  CardCode nVarChar(15) BP Code ->ACRD
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  Country nVarChar(3) Country ->OCRY
  State nVarChar(3) State
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=2 ->ADP1
  LicTradNum nVarChar(32) Federal Tax ID
  LineNum Int(11) Row No.
  TaxCode nVarChar(8) Tax Code ->OSTC
  Building Text(16) Building/Floor/Room
  AdresType VarChar(1) Address Type default=S [S=Ship To, B=Bill to]
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  AltCrdName nVarChar(100) Alternative BP Name
  AltTaxId nVarChar(32) Alternative Tax ID
  TaxOffice nVarChar(50) Tax Office
  GlblLocNum nVarChar(50) Global Location Number
  Ntnlty nVarChar(100) Nationality
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  TaaSEnbl VarChar(1) TaaS Service Enabled on Address default=Y [Y=Yes, N=No]
  GSTRegnNo nVarChar(15) GSTIN
  GSTType Int(11) GST Type ->OGTY
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time Incl. Sec.

# ACR11 - BP Tributary Info.
Module: Business Partners | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TributID, Address, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(25) BP Code ->OCRD
  Address nVarChar(50) Address
  TributID Int(11) Tributary Info. ID
  TributType Int(11) Tributary Type default=-1 ->OBNI
  TTStartDat Date(8) Tributary Type Start Date
  TTEndDate Date(8) Tributary Type End Date
  TribRegCod Int(11) Tributary Regime Code default=-1 ->OBNI
  TRCStartD Date(8) Tributary Reg. Code Start Date
  TRCEndDate Date(8) Tributary Regime Code End Date
  LogInstanc Int(11) Log Instance default=0

# ACR12 - BP eDoc Settings
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ProtCode, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  ProtCode Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI] ->OECM
  GenType VarChar(1) Generation Type default=N [N=Not Relevant, G=Generate, L=Generate Later]
  MapID Int(11) Electronic Document Format Mapping
  LogInstanc Int(11) Log Instance default=0

# ACR2 - Bussiness Partners - Payment Methods-History
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineNum, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  LineNum Int(11) Row Number
  PymCode nVarChar(15) Payment Method Code ->OPYM
  LogInstanc Int(11) Log Instance default=0
  ObjType Int(6) Object Type default=2 ->ADP1

# ACR3 - Business Partner Control Accounts - History
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstane, AcctType, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  AcctType VarChar(1) Account Type default=M [M=Domestic, F=Foreign, D=Down Payment, A=Assets Account, R=Bill of Exchange Accounts Receivable, P=Bill of Exchange Accounts Payable, C=Bill of Exchange on Collection, S=Bill of Exchange Presentation, Y=Assets Bill of Exchange Acct Payable, I=Bill of Exchange Discounted, U=Unpaid Bill of Exchange, O=Open Debts]
  AcctCode nVarChar(15) Account Code ->OACT
  LogInstane Int(11) Log Instance default=0
  ObjType Int(6) Object Type default=2 ->ADP1

# ACR4 - Allowed WTax Codes for BP - History
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, WTCode, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  WTCode nVarChar(4) WTax Code
  LogInstanc Int(11) Log Instance default=0

# ACR5 - BP Payment Dates
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, PmntDate, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  PmntDate nVarChar(2) Payment Date
  LogInstanc Int(11) Log Instance default=0

# ACR7 - Fiscal IDs for BP Master Data
Module: Business Partners | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AddrType, Address, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(25) BP Code ->OCRD
  Address nVarChar(50) Address
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  CNAEId Int(11) Brazilian CNAE Code ->OCNA
  TaxId10 nVarChar(100) Tax ID 10
  TaxId11 nVarChar(100) Tax ID 11
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill to]
  ECCNo nVarChar(40) E.C.C. No.
  CERegNo nVarChar(40) C.E. Registration No.
  CERange nVarChar(60) C.E. Range
  CEDivis nVarChar(60) C.E. Division
  CEComRate nVarChar(60) C.E. Commisionerate
  LogInstanc Int(11) Log Instance default=0
  SefazDate Date(8) Date of Update from SEFAZ
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India

# ACRB - Business Partner Bank Accounts - History
Module: Business Partners | 46 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsEntry
  ACCOUNT U: LogInstanc, CardCode, Account, BankCode, Country
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  CardCode nVarChar(15) BP Code ->OCRD
  BankCode nVarChar(30) Bank Code
  Country nVarChar(3) Country ->OCRY
  Account nVarChar(50) Account No.
  Branch nVarChar(50) Branch
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  State nVarChar(3) State
  ControlKey nVarChar(2) Control Key
  UsrNumber1 nVarChar(25) User No. 1
  UsrNumber2 nVarChar(25) User No. 2
  UsrNumber3 nVarChar(25) User No. 3
  UsrNumber4 nVarChar(25) User No. 4
  IBAN nVarChar(50) IBAN
  LogInstanc Int(11) Log Instance default=0
  Building Text(16) Building/Floor/Room
  AliasName nVarChar(50) Alias Name
  AcctType VarChar(1) Account Type
  BankKey Int(11) Bank Internal ID ->ODSC
  BIK nVarChar(15) BIK
  AcctName nVarChar(250) Bank Account Name
  CorresAcct nVarChar(30) Correspondent Account
  Phone nVarChar(25) Phone
  Fax nVarChar(25) Fax
  ISRType Int(6) ISR Type
  ISRBillerI nVarChar(9) ISR Biller ID
  CustIdNum nVarChar(6) Customer ID Number default=0
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  SwiftNum nVarChar(50) BIC/SWIFT Code
  ABARoutNum nVarChar(25) ABA Routing Number
  MandateID nVarChar(35) Mandate ID
  SignDate Date(8) Date of Signature
  PWZAbsEntr Int(11) PWZ ABS Entry ->OPWZ
  BranchChk nVarChar(5) Branch Check Digit
  MandatDate Date(8) Date Of Mandate Expiration
  SeqType nVarChar(4) SEPA Seq. Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  ActType VarChar(1) Account Type [C=Checking Account, S=Savings Account]
  IsPrenot VarChar(1) Is Prenotification default=N [Y=Yes, N=No]
  EnAccount Text(16) Encryption of Account
  EnIBAN Text(16) Encryption of IBAN
  EncryptIV nVarChar(100) Encrypt IV

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

# AOA1 - Blanket Agreement - Rows
Module: Business Partners | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AgrLineNum, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->AOAT
  AgrLineNum Int(11) Agreement Row Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  ItemGroup Int(6) Item Group ->OITB
  PlanQty Num(19,6) Planned Quantity
  UnitPrice Num(19,6) Unit Price
  Currency nVarChar(3) Price Currency
  CumQty Num(19,6) Cumulative Quantity
  CumAmntFC Num(19,6) Cumulative Amount in FC
  CumAmntLC Num(19,6) Cumulative Amount in LC
  FreeTxt nVarChar(100) Free Text
  InvntryUom nVarChar(100) Inventory UoM
  LogInstanc Int(11) Log Instance default=0
  VisOrder Int(11) Visual Order
  RetPortion Num(19,6) Goods Return Probability
  WrrtyEnd Date(8) Date When Goods Expire
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  PlanAmtLC Num(19,6) Planned Amount (LC)
  PlanAmtFC Num(19,6) Planned Amount (FC)
  Discount Num(19,6) Line Discount
  UomEntry Int(11) UoM Entry ->OUOM
  UomCode nVarChar(20) UoM Code
  NumPerMsr Num(19,6) UoM Value default=0
  UndlvQty Num(19,6) Undeliverd Quantity
  UndlvAmntL Num(19,6) Undeliverd Amount LC
  UndlvAmntF Num(19,6) Undeliverd Amount FC
  TrnspCode Int(6) Shipping Type ->OSHP
  Project nVarChar(20) Project Code ->OPRJ
  TaxCode nVarChar(8) Tax Code
  TAXRate Num(19,6) TAX Rate
  PlVatAmtLC Num(19,6) Planned VAT Amount (LC)
  PlVatAmtFC Num(19,6) Planned VAT Amount (FC)
  CumVtAmtLC Num(19,6) Cumulative VAT Amount (LC)
  CumVtAmtFC Num(19,6) Cumulative VAT Amount (FC)

# AOA2 - Blanket Agreement - Details
Module: Business Partners | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AgrEfctNum, AgrLnNum, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->AOAT
  AgrLnNum Int(11) Agreement Item Row Number
  AgrEfctNum Int(11) Agreement Effective Row No.
  DatePeriod VarChar(1) Frequency default=M [D=Daily, W=Weekly, M=Monthly, Q=Quarterly, S=Semi-Annually, A=Annually, O=One Time]
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  CallUp nVarChar(100) Release Information
  WhsCode nVarChar(8) Warehouse Code default=-1 ->OWHS
  Quantity Num(19,6) Item Quantity
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  LogInstanc Int(11) Log Instance default=0
  AmountLC Num(19,6) Planned Amount (LC)
  AmountFC Num(19,6) Planned Amount (FC)

# AOA3 - Item Details: Activity
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, ActivityID, AgrEfctNum, AgrLnNum, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->AOAT
  AgrLnNum Int(11) Agreement Item Row Number
  AgrEfctNum Int(11) Agreement Effective: Row No.
  ActivityID Int(11) Activity ID ->OCLG
  LogInstanc Int(11) Log Instance default=0

# AOA4 - Blanket Agreement - Recurring Transactions
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, RcpEntry, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance default=0

# AOAT - Blanket Agreement
Module: Business Partners | 53 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, AbsID
Fields (name type(len) description [values] ->parent table):
  AbsID Int(11) Agreement No.
  BpCode nVarChar(15) BP Code ->OCRD
  BpName nVarChar(100) BP Name
  CntctCode Int(11) Contact Person ->OCPR
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  TermDate Date(8) Termination Date
  Descript nVarChar(254) Description
  Type VarChar(1) Agreement Type default=G [G=General, S=Specific]
  Status VarChar(1) Agreement Status default=D [A=Approved, F=On Hold, D=Draft, T=Terminated, C=Canceled, X=To Be Terminated, P=To Be On Hold]
  Owner Int(11) Owner ->OHEM
  Renewal VarChar(1) Renewal default=N [Y=Yes, N=No]
  UseDiscnt VarChar(1) Use BP Special Price default=Y [Y=Yes, N=No]
  RemindVal Int(6) Reminder
  RemindUnit VarChar(1) Reminder Unit default=D [D=Day(s), W=Week(s), M=Month(s)]
  Remarks Text(16) Remarks
  AtchEntry Int(11) Attachment Entry ->OATC
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdtDate Date(8) Update Date
  CreateDate Date(8) Create Date
  Cancelled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year of Transfer]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  RemindFlg VarChar(1) Reminder Sent default=N [Y=Yes, N=No]
  Fulfilled VarChar(1) Fulfilled default=N [Y=Fulfilled, N=Not Fulfilled]
  Attachment Text(16) Attachments
  SettleProb Num(19,6) Settlement Probability %
  UpdtTime Int(11) Update Time
  Method VarChar(1) Agreement Method default=I [I=Items Method, M=Monetary Method]
  GroupNum Int(6) Payment Terms Code ->OCTG
  ListNum Int(6) Price List No. ->OPLN
  SignDate Date(8) Signing Date
  AmendedTo Int(11) Amendment To
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  ObjType nVarChar(20) Object Type default=1250000025 ->ADP1
  Handwrtten VarChar(1) Manual Numbering default=N
  PIndicator nVarChar(10) Period Indicator ->OPID
  BpType VarChar(1) BP Type default=C [C=Customer, S=Vendor]
  Instance Int(6) Instance default=0
  PayMethod nVarChar(15) Payment Method ->OPYM
  NumAtCard nVarChar(100) Customer/Vendor Ref. No.
  BPCurr nVarChar(3) BP Currency ->OCRN
  FixedRate Num(19,6) Exchange Rate
  TrnspCode Int(6) Shipping Type ->OSHP
  Project nVarChar(20) Project Code ->OPRJ
  PriceMode VarChar(1) Price Mode default=N [N=Net, G=Gross]
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  FromStat VarChar(1) From Status default=D [F=On Hold, D=Draft]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  SAPPassprt Text(16) Extended SAP Passport

# AWD3 - WTax Codes Details for BP
Module: Business Partners | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineId, AbsEntry
  BP U: LogInstanc, DetailType, DateFrom, KeyPart2, KeyPart1, WTCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  KeyPart1 nVarChar(15) BP key part 1
  KeyPart2 nVarChar(15) BP key part 2
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  Rate Num(19,6) Currency Rate
  DetailType nVarChar(2) Type of Detailed Information [A=Allowed, S=Special Rate, E=Exemption]
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, P=Partner Implementation]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0

# AWD4 - WTax Codes Details for Item
Module: Business Partners | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineId, AbsEntry
  ITEM U: LogInstanc, DateFrom, ItemCode, WTCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  ItemCode nVarChar(50) Item No. ->OITM
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, P=Partner Implementation]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0

# AWD5 - WTax Codes Details for Freight
Module: Business Partners | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, LineId, AbsEntry
  EXPNSCODE U: LogInstanc, DateFrom, ExpnsCode, WTCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  ExpnsCode Int(11) Freight Code ->OEXD
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, P=Partner Implementation]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0

# CLG1 - Activity CheckIns
Module: Business Partners | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, ClgCode
Fields (name type(len) description [values] ->parent table):
  ClgCode Int(11) Activity Number ->OCLG
  LineNum Int(11) Line Number
  Date Date(8) Date
  Location nVarChar(254) Location
  Latitude nVarChar(13) Latitude
  Longitude nVarChar(14) Longitude
  Time Int(11) Time
  OwnerUser Int(6) Owner User ->OUSR
  OwnerEmp Int(11) Owner Employee ->OHEM
  LogInstanc Int(11) Log Instance default=0

# CPN1 - Campaign - BPs
Module: Business Partners | 45 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CpnLineNum, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  BpCode nVarChar(15) BP Code ->OCRD
  BpName nVarChar(100) BP Name
  GroupName nVarChar(20) BP Group Name
  Industry nVarChar(15) BP Industry Name
  Status VarChar(1) BP Status [A=Active, I=Inactive]
  CntCode nVarChar(50) Contact Code
  CntTitle nVarChar(10) Contact Title
  CntPstn nVarChar(90) Contact Position
  CntEmail nVarChar(100) Contact E-Mail
  CntTel nVarChar(20) Contact Telephone
  CntMobile nVarChar(50) Contact Mobile
  CntFax nVarChar(20) Contact Fax
  CntAddr nVarChar(100) Contact Address
  Response VarChar(1) Response from Company default=N [Y=Yes, N=No]
  OpprId Int(11) Related Opportunity ->OOPR
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  City nVarChar(100) City
  ZipCode nVarChar(100) Zip Code
  County nVarChar(100) County
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country ->OCRY
  Building Text(16) Building/Floor/Room
  CActivity VarChar(1) Create Activity [Y/N] default=Y
  DocType nVarChar(20) Document Type default=-1 [-1=, 97=Sales Opportunities, 23=Sales Quotations, 17=Sales Orders, 15=Deliveries, 13=A/R Invoices, -97=Purchase Opportunities, 540000006=Purchase Quotations, 22=Purchase Orders, 20=Goods Receipt POs, 18=A/P Invoices]
  ShowBPDoc VarChar(1) Show BP Documents [Y/N] default=N
  DocNumber Int(11) Related Document
  DocEntry Int(11) Document Entry
  AssignTo VarChar(1) Assign to User or Employee default=U [U=User, E=Employee]
  AssignName Int(11) User or Employee Name
  FirstName nVarChar(50) First Name
  MiddleName nVarChar(50) Middle Name
  LastName nVarChar(50) Last Name
  LicTradNum nVarChar(32) Federal Tax ID
  AddrType nVarChar(100) Address Type
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  StreetNo nVarChar(100) Street No.
  AddressID nVarChar(50) Address ID
  RspType nVarChar(20) Response Type ->ORPT
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]

# CPN2 - Campaign - Items
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CpnLineNum, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  ItemType VarChar(1) Item Type [I=Items, L=Labor, T=Travel]
  ItemGrp nVarChar(20) Item Group
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# CPN3 - Campaign - Partners
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CpnLineNum, CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No. ->OCPN
  CpnLineNum Int(11) Campaign Line Number
  ParterId Int(11) Partners ->OPRT
  OrlCode Int(11) Relationship Code ->OORL
  RelatCard nVarChar(15) Related BP ->OCRD
  Memo nVarChar(50) Details
  LogIns Int(11) Log Instance - History
  VisOrder Int(11) Visual Order

# CRD1 - Business Partners - Addresses
Module: Business Partners | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AdresType, Address, CardCode
Fields (name type(len) description [values] ->parent table):
  Address nVarChar(50) Address Name
  CardCode nVarChar(15) BP Code ->OCRD
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  Country nVarChar(3) Country ->OCRY
  State nVarChar(3) State
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=2 ->ADP1
  LicTradNum nVarChar(32) Federal Tax ID
  LineNum Int(11) Row Number
  TaxCode nVarChar(8) Tax Code ->OSTC
  Building Text(16) Building/Floor/Room
  AdresType VarChar(1) Address Type default=S [S=Ship To, B=Bill to]
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  AltCrdName nVarChar(100) Alternative BP Name
  AltTaxId nVarChar(32) Alternative Tax ID
  TaxOffice nVarChar(50) Tax Office
  GlblLocNum nVarChar(50) Global Location Number
  Ntnlty nVarChar(100) Nationality
  DIOTNat nVarChar(3) DIOT Nationality ->OCRY
  TaaSEnbl VarChar(1) TaaS Service Enabled on Address default=Y [Y=Yes, N=No]
  GSTRegnNo nVarChar(15) GSTIN
  GSTType Int(11) GST Type ->OGTY
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time Incl. Sec.

# CRD11 - BP Tributary Info.
Module: Business Partners | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TributID, Address, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(25) BP Code ->OCRD
  Address nVarChar(50) Address
  TributID Int(11) Tributary Info. ID
  TributType Int(11) Tributary Type default=-1 ->OBNI
  TTStartDat Date(8) Tributary Type Start Date
  TTEndDate Date(8) Tributary Type End Date
  TribRegCod Int(11) Tributary Regime Code default=-1 ->OBNI
  TRCStartD Date(8) Tributary Reg. Code Start Date
  TRCEndDate Date(8) Tributary Regime Code End Date
  LogInstanc Int(11) Log Instance default=0

# CRD12 - BP eDoc Settings
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ProtCode, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  ProtCode Int(11) Communication Type or Protocol [0=Invalid, 1=GEN, 2=EET, 3=CFDI] ->OECM
  GenType VarChar(1) Generation Type default=N [N=Not Relevant, G=Generate, L=Generate Later]
  MapID Int(11) Electronic Document Format Mapping
  LogInstanc Int(11) Log Instance default=0

# CRD2 - Bussiness Partners - Payment Methods
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, CardCode
  CRD_PYM: PymCode, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  LineNum Int(11) Row Number
  PymCode nVarChar(15) Payment Method Code ->OPYM
  LogInstanc Int(11) Log Instance default=0
  ObjType Int(6) Object Type default=2 ->ADP1

# CRD3 - BP Control Account
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AcctType, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  AcctType VarChar(1) Account Type default=M [M=Domestic, F=Foreign, D=Down Payment, A=Assets Account, R=Bill of Exchange Accounts Receivable, P=Bill of Exchange Accounts Payable, C=Bill of Exchange on Collection, S=Bill of Exchange Presentation, Y=Assets Bill of Exchange Acct Payable, I=Bill of Exchange Discounted, U=Unpaid Bill of Exchange, O=Open Debts, H=Cash Discount Interim, E=Exchange Rate Interim]
  AcctCode nVarChar(15) Account Code ->OACT
  LogInstane Int(11) Log Instance default=0
  ObjType Int(6) Object Type default=2 ->ADP1

# CRD4 - Allowed WTax Codes for BP
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: WTCode, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  WTCode nVarChar(4) WTax Code
  LogInstanc Int(11) Log Instance default=0

# CRD5 - BP Payment Dates
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PmntDate, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  PmntDate nVarChar(2) Payment Date
  LogInstanc Int(11) Log Instance default=0

# CRD6 - BP's Payer Name
Module: Business Partners | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardPyName, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  CardPyName nVarChar(48) Payer Name in Bank Statement

# CRD7 - Fiscal IDs for BP Master Data
Module: Business Partners | 25 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AddrType, Address, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(25) BP Code ->OCRD
  Address nVarChar(50) Address
  TaxId0 nVarChar(100) Tax ID 0
  TaxId1 nVarChar(100) Tax ID 1
  TaxId2 nVarChar(100) Tax ID 2
  TaxId3 nVarChar(100) Tax ID 3
  TaxId4 nVarChar(100) Tax ID 4
  TaxId5 nVarChar(100) Tax ID 5
  TaxId6 nVarChar(100) Tax ID 6
  TaxId7 nVarChar(100) Tax ID 7
  TaxId8 nVarChar(100) Tax ID 8
  TaxId9 nVarChar(100) Tax ID 9
  CNAEId Int(11) Brazil CNAE Code ->OCNA
  TaxId10 nVarChar(100) Tax ID 10
  TaxId11 nVarChar(100) Tax ID 11
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill to]
  ECCNo nVarChar(40) E.C.C. No.
  CERegNo nVarChar(40) C.E. Registration No.
  CERange nVarChar(60) C.E. Range
  CEDivis nVarChar(60) C.E. Division
  CEComRate nVarChar(60) C.E. Commisionerate
  LogInstanc Int(11) Log Instance default=0
  SefazDate Date(8) Date of Update from SEFAZ
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India

# CRD8 - BP Branch Assignment
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BPLId, CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code ->OCRD
  BPLId Int(11) Assigned Branch ->OBPL
  DisabledBP VarChar(1) Disabled for BP default=N [Y=Yes, N=No]

# CRD9 - OCRD Extension
Module: Business Partners | 11 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(25) BP Code ->OCRD
  ISTransMod Int(11) Intrastat Transport Mode ->ODCI
  ISIncoterm Int(11) Intrastat Incoterms ->ODCI
  ISState Int(11) Intrastat State ->ODCI
  ISNatTrans Int(11) Intrastat Nature of Trans. ->ODCI
  ISStatProc Int(11) Intrastat Statistical Proc. ->ODCI
  ISCustProc Int(11) Intrastat Customs Proc. ->ODCI
  ISCRYOrig nVarChar(3) Intrastat Country Origin ->OCRY
  ISPort Int(11) Intrastat Port of Entry/Exit ->ODCI
  ISDomFrgld VarChar(1) Intrastat Domestic/Foreign ID
  ISRelevant VarChar(1) Intrastat Relevant default=N [Y=Yes, N=No]

# DDT1 - Withholding Tax Deduction Hierarchy - Rows
Module: Business Partners | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, DdtKey
Fields (name type(len) description [values] ->parent table):
  DdtKey Int(11) Hierarchy Key ->ODDT
  LineNum Int(11) Row Number
  DdctPrcnt Num(19,6) Deduction %
  MaxSum Num(19,6) Maximum Total
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Data Doc., P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OAT1 - Blanket Agreement - Rows
Module: Business Partners | 35 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AgrLineNum, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLineNum Int(11) Agreement Row Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(100) Item Description
  ItemGroup Int(6) Item Group ->OITB
  PlanQty Num(19,6) Planned Quantity
  UnitPrice Num(19,6) Unit Price
  Currency nVarChar(3) Price Currency
  CumQty Num(19,6) Cumulative Quantity
  CumAmntFC Num(19,6) Cumulative Amount in FC
  CumAmntLC Num(19,6) Cumulative Amount in LC
  FreeTxt nVarChar(100) Free Text
  InvntryUom nVarChar(100) Inventory UoM
  LogInstanc Int(11) Log Instance default=0
  VisOrder Int(11) Visual Order
  RetPortion Num(19,6) Goods Return Probability
  WrrtyEnd Date(8) Date When Goods Expire
  LineStatus VarChar(1) Row Status default=O [O=Open, C=Closed]
  PlanAmtLC Num(19,6) Planned Amount (LC)
  PlanAmtFC Num(19,6) Planned Amount (FC)
  Discount Num(19,6) Line Discount
  UomEntry Int(11) UoM Entry ->OUOM
  UomCode nVarChar(20) UoM Code
  NumPerMsr Num(19,6) UoM Value default=0
  UndlvQty Num(19,6) Undeliverd Quantity
  UndlvAmntL Num(19,6) Undeliverd Amount LC
  UndlvAmntF Num(19,6) Undeliverd Amount FC
  TrnspCode Int(6) Shipping Type ->OSHP
  Project nVarChar(20) Project Code ->OPRJ
  TaxCode nVarChar(8) Tax Code
  TAXRate Num(19,6) TAX Rate
  PlVatAmtLC Num(19,6) Planned VAT Amount (LC)
  PlVatAmtFC Num(19,6) Planned VAT Amount (FC)
  CumVtAmtLC Num(19,6) Cumulative VAT Amount (LC)
  CumVtAmtFC Num(19,6) Cumulative VAT Amount (FC)

# OAT2 - Blanket Agreement - Details
Module: Business Partners | 14 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AgrEfctNum, AgrLnNum, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Item Row Number
  AgrEfctNum Int(11) Agreement Effective Row No.
  DatePeriod VarChar(1) Frequency default=M [D=Daily, W=Weekly, M=Monthly, Q=Quarterly, S=Semi-Annually, A=Annually, O=One Time]
  FromDate Date(8) From Date
  ToDate Date(8) To Date
  CallUp nVarChar(100) Release Information
  WhsCode nVarChar(8) Warehouse Code default=-1 ->OWHS
  Quantity Num(19,6) Item Quantity
  ConsumeFCT VarChar(1) Consumer Sales Forecast [Y=Yes, N=No]
  FreeTxt nVarChar(100) Free Text
  LogInstanc Int(11) Log Instance default=0
  AmountLC Num(19,6) Planned Amount (LC)
  AmountFC Num(19,6) Planned Amount (FC)

# OAT3 - Item Details: Activity
Module: Business Partners | 5 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ActivityID, AgrEfctNum, AgrLnNum, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  AgrLnNum Int(11) Agreement Line Number
  AgrEfctNum Int(11) Line Number
  ActivityID Int(11) Activity ID ->OCLG
  LogInstanc Int(11) Log Instance default=0

# OAT4 - Blanket Agreement - Recurring Transactions
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RcpEntry, AgrNo
Fields (name type(len) description [values] ->parent table):
  AgrNo Int(11) Agreement No. ->OOAT
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance default=0

# OBPL - Business Place
Module: Business Partners | 55 columns | ObjType: 247
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BPLId
  NAME U: BPLName
Fields (name type(len) description [values] ->parent table):
  BPLId Int(11) Branch ID
  BPLName nVarChar(100) Branch Name
  BPLFrName nVarChar(100) Branch Name (Foreign)
  VATRegNum nVarChar(12) VAT Reg. Number
  RepName nVarChar(15) Rep. Name
  Industry nVarChar(20) Industry
  Business nVarChar(20) Business
  Address nVarChar(254) Address
  AddressFr nVarChar(254) Address (Foreign)
  MainBPL VarChar(1) Main BPL default=N [Y=Main Business Place, N=Not Main Business Place]
  TxOffcNo nVarChar(3) Tax Office No.
  Disabled VarChar(1) Disabled default=N [Y=Disabled, N=Enabled]
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  DflCust nVarChar(15) Default Customer ID ->OCRD
  DflVendor nVarChar(15) Default Vendor ID ->OCRD
  DflWhs nVarChar(8) Default Warehouse ID ->OWHS
  DflTaxCode nVarChar(8) Default Tax Code ->OCNA
  RevOffice nVarChar(100) Tax Office
  TaxIdNum nVarChar(32) Branch Reg. No.
  TaxIdNum2 nVarChar(32) Federal Tax ID 2
  TaxIdNum3 nVarChar(32) Federal Tax ID 3
  AddtnlId nVarChar(32) Additional ID Number
  CompNature Int(11) Nature of Company default=-1 ->OBNI
  EconActT Int(11) Economic Activity Type default=-1 ->OBNI
  CredCOrig nVarChar(2) Credit Contribution Origin ->OBSI
  IPIPeriod nVarChar(2) IPI Period ->OBSI
  CoopAssocT Int(11) Cooperative Association Type default=-1 ->OBNI
  PrefState nVarChar(3) Default State
  ProfTax Int(11) Profit Taxation default=-1 ->OBNI
  CompQualif Int(11) Company Qualification default=-1 ->OBNI
  DeclType Int(11) Declarer Type default=-1 ->OBNI
  AddrType nVarChar(100) Address Type
  Street nVarChar(100) Street
  StreetNo nVarChar(100) Street No.
  Building nVarChar(100) Building/Floor/Room
  ZipCode nVarChar(20) Zip Code
  Block nVarChar(100) Block
  City nVarChar(100) City
  State nVarChar(3) State
  County nVarChar(100) County ->OCNT
  Country nVarChar(3) Country ->OCRY
  PmtClrAct nVarChar(15) Payment Clearing Account ->OACT
  CommerReg nVarChar(60) Commercial Register
  DateOfInc Date(8) Date of Incorporation
  SPEDProf nVarChar(2) SPED Profile ->OBSI
  EnvTypeNFe Int(11) Environment Type NFe default=-1 ->OBNI
  Opt4ICMS VarChar(1) Opting for ICMS 115_03 default=N
  AliasName Text(16) Alias Name
  GlblLocNum nVarChar(50) Global Location Number
  TaxRptFrm Date(8) Tax Wizard Reporting From
  Suframa nVarChar(100) SUFRAMA
  DfltResWhs nVarChar(8) Default Resource Warehouse ID ->OWHS
  SnapshotId Int(11) Snapshot ID default=0

# OBPP - BP Priorities
Module: Business Partners | 2 columns | ObjType: 150
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PrioCode
Fields (name type(len) description [values] ->parent table):
  PrioCode Int(11) Priority
  PrioDesc nVarChar(10) Priority Description

# OCLA - Activity Status
Module: Business Partners | 4 columns | ObjType: 217
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: statusID
Fields (name type(len) description [values] ->parent table):
  statusID Int(11) Status ID
  name nVarChar(30) Status Name
  descriptio nVarChar(254) Status Description
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]

# OCLG - Activities
Module: Business Partners | 93 columns | ObjType: 33
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ClgCode
  CRD_CODE: CardCode
  OPPORT: OprLine, OprId
Fields (name type(len) description [values] ->parent table):
  ClgCode Int(11) Activity Number
  CardCode nVarChar(15) BP Code ->OCRD
  Notes Text(16) Remarks
  CntctDate Date(8) System Date
  CntctTime Int(11) Time
  Recontact Date(8) Activity Date
  Closed VarChar(1) Closed Activity default=N [Y=Yes, N=No]
  CloseDate Date(8) Closing Date
  ContactPer nVarChar(90) Contact Person Name
  Tel nVarChar(50) Telephone
  Fax nVarChar(20) Fax
  CntctSbjct Int(6) Activity Subject default=-1 ->OCLS
  Transfered VarChar(1) Transfered to Next Year default=N [Y=Yes, N=No]
  DocType nVarChar(20) Linked Document default=-1 [13=A/R Invoice, 14=A/R Credit Memo, 15=Delivery, 16=Return, 17=Sales Order, 18=A/P Invoice, 19=A/P Credit Memo, 20=Goods Receipt PO, 21=Goods Return, 22=Purchase order, 23=Sales Quotation, 24=Incoming Payment, 25=Deposit, 30=Journal Entry, 46=Outgoing Payment, 57=Checks for Payment, 59=Goods Receipt, 60=Goods Issue, 1250000001=Inventory Transfer Request, 67=Inventory Transfer, 68=Work Order, 69=Landed Costs, 132=Correction Invoice, 162=Material Revaluation, 202=Production Order, 203=A/R Down Payment, 204=A/P Down Payment, 140000009=Outgoing Excise Invoice, 140000010=Incoming Excise Invoice, -1=, 0=, 4=Items, 163=A/P Correction Invoice, 164=A/P Correction Invoice Reversal, 165=A/R Correction Invoice, 166=A/R Correction Invoice Reversal, 1320000012=Campaign, 540000006=Purchase Quotation, 1250000025=Blanket Agreements, 1470000113=Purchase Request, 112=Document Drafts, 140=Payment Drafts, 123=Checks for Payment Drafts, 254000065=Self Invoice, 254000066=Self Credit Memo]
  DocNum nVarChar(50) Linked Document Number
  DocEntry nVarChar(50) Linked Document Entry
  Attachment Text(16) Attachment
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  AttendUser Int(6) Dealt by ->OUSR
  CntctCode Int(11) Contact Person ->OCPR
  UserSign Int(6) User Signature
  SlpCode Int(11) Sales Employee default=-1 ->OSLP
  Action VarChar(1) Activity default=C [C=Phone Call, M=Meeting, T=Task, E=Note, P=Campaign, N=Other]
  Details nVarChar(100) Details
  CntctType Int(6) Activity Type default=-1 ->OCLT
  Location Int(6) Location default=-1 ->OCLO
  BeginTime Int(11) Start Time
  Duration Num(19,6) Activity Duration
  DurType VarChar(1) Duration UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  ENDTime Int(11) End Time
  Priority VarChar(1) Priority default=1 [0=Low, 1=Normal, 2=High]
  Reminder VarChar(1) Reminder default=N [Y=Yes, N=No]
  RemQty Num(19,6) Reminder Quantity
  RemType VarChar(1) Reminder Units default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  OprId Int(11) Opportunity - Key
  OprLine Int(6) Row No. - Opportunity
  RemDate Date(8) Reminder Date
  RemTime Int(6) Reminder Time
  RemSented VarChar(1) Reminder Was Sent default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  endDate Date(8) End/Due Date
  status Int(11) Status ->OCLA
  personal VarChar(1) Personal Flag default=N [Y=Yes, N=No]
  inactive VarChar(1) Inactive Flag default=N [Y=Yes, N=No]
  tentative VarChar(1) Tentative Flag default=N [Y=Yes, N=No]
  street nVarChar(100) Street
  city nVarChar(100) City
  country nVarChar(3) Country ->OCRY
  state nVarChar(3) State ->OCST
  room nVarChar(50) Room
  parentType nVarChar(20) Parent Object Type
  parentId Int(11) Parent Object ID
  prevActvty Int(11) Previous Activity
  AtcEntry Int(11) Attachment Entry
  RecurPat VarChar(1) Recurrence Pattern default=N [N=None, D=Daily, W=Weekly, M=Monthly, A=Annually]
  EndType VarChar(1) Recurrence End Type default=N [N=No End Date, C=By Counter, D=By Date]
  SeStartDat Date(8) Series Start Date
  SeEndDat Date(8) Series End Date
  MaxOccur Int(11) Max Occurrences
  Interval Int(11) Interval default=1
  Sunday VarChar(1) Sunday default=N [N=No, Y=Yes]
  Monday VarChar(1) Monday default=N [N=No, Y=Yes]
  Tuesday VarChar(1) Tuesday default=N [N=No, Y=Yes]
  Wednesday VarChar(1) Wednesday default=N [N=No, Y=Yes]
  Thursday VarChar(1) Thursday default=N [N=No, Y=Yes]
  Friday VarChar(1) Friday default=N [N=No, Y=Yes]
  Saturday VarChar(1) Saturday default=N [N=No, Y=Yes]
  SubOption VarChar(1) Suboption default=1 [1=Option 1, 2=Option 2]
  DayInMonth Int(11) Repeat Day in Month
  Month Int(11) Repeat Month
  DayOfWeek Int(11) Repeat Day of Week
  Week Int(11) Repeat Week in Month [1=first, 2=second, 3=third, 4=fourth, 5=last]
  SeriesNum Int(11) Series Number
  OrigDate Date(8) Original Date
  IsRemoved VarChar(1) Removed Flag default=N [N=No, Y=Yes]
  LastRemind Date(8) Last Reminder Date
  AssignedBy Int(6) Assigned By ->OUSR
  AddrName nVarChar(50) Address Name
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill to]
  AttendEmpl Int(11) Dealt by Employee ->OHEM
  NextDate Date(8) Date of Next Occurrence
  NextTime Int(6) Time of Next Occurrence
  OwnerCode Int(11) Activities Owner ->OHEM
  AttendReci Int(11) Attend Recipient ->ORCI
  ActType Int(11) Activity Type ->PMC5
  LaborItem nVarChar(50) Labor Item No.
  ResCode nVarChar(50) Resource Code from ORSC ->ORSC
  FIPROJECT nVarChar(20) Financial Project ->OPRJ
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  CreateDate Date(8) Creation Date

# OCLO - Meetings Location
Module: Business Partners | 5 columns | ObjType: 104
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(50) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]

# OCLS - Activity Subjects
Module: Business Partners | 6 columns | ObjType: 84
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  type U: Name, Type
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(20) Name
  Type Int(6) Related Type default=-1 ->OCLT
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# OCLT - Activity Types
Module: Business Partners | 5 columns | ObjType: 103
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Code
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(6) Code
  Name nVarChar(20) Name
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, p=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# OCOG - Commission Groups
Module: Business Partners | 7 columns | ObjType: 65
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Commission Group Code
  GroupName nVarChar(30) Commission Group Name
  Commission Num(19,6) Commission Percentage
  PrvComsnPr Num(19,6) Prev. Commission in %
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OCPN - Campaign
Module: Business Partners | 27 columns | ObjType: 1320000012
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CpnNo
Fields (name type(len) description [values] ->parent table):
  CpnNo Int(11) Campaign No.
  Name nVarChar(100) Campaign Name
  Type VarChar(1) Campaign Type default=E [E=E-Mail, M=Mail, F=Fax, P=Phone Call, T=Meeting, S=SMS, W=Web, O=Other]
  TargetGrp nVarChar(20) Target Group ->OTGG
  Owner Int(11) Campaign Owner ->OHEM
  Status VarChar(1) Campaign Status default=O [O=Open, F=Finished, C=Canceled]
  StartDate Date(8) Campaign Start Date
  FinishDate Date(8) Campaign Finish Date
  Remarks Text(16) Campaign Remarks
  WizardGen VarChar(1) Generated by Wizard default=N [Y=Yes, N=No]
  Template Text(16) Campaign Template
  AtcEntry Int(11) Attachment Entry ->OATC
  Attachment Text(16) Attachments
  LogIns Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Create Date
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, P=Partner Implementation, T=Year of Transfer]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  Instance Int(6) Instance default=0
  Url Text(16) Web Link
  TmplPath nVarChar(254) Template Path
  TargetType VarChar(1) Target Group Type default=C [C=Customer, S=Vendor]
  ExeOption VarChar(1) Execute Option default=O [L=Generate External List, O=Send E-Mail Using Microsoft Office Outlook, B=Send E-Mail Using SAP Business One Mail, F=Send Fax, U=Generate URL]
  Executed VarChar(1) Executed [Y=Yes, N=No]
  VersionNum nVarChar(11) Version Number

# OCPR - Contact Persons
Module: Business Partners | 50 columns | ObjType: 11
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CntctCode
  CARD U: Name, CardCode
Fields (name type(len) description [values] ->parent table):
  CntctCode Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  Name nVarChar(50) Contact Person Name
  Position nVarChar(90) Position
  Address nVarChar(100) Address
  Tel1 nVarChar(20) Telephone 1
  Tel2 nVarChar(20) Telephone 2
  Cellolar nVarChar(50) Mobile Phone
  Fax nVarChar(20) Fax
  E_MailL nVarChar(100) E-Mail
  Pager nVarChar(30) Pager
  Notes1 nVarChar(100) Remark 1
  Notes2 nVarChar(100) Remark 2
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  Password nVarChar(8) Password
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=11 ->ADP1
  BirthPlace nVarChar(100) Place of Birth
  BirthDate Date(8) Date of Birth
  Gender VarChar(1) Gender default=E [M=Male, F=Female, E=, *=Masked]
  Profession nVarChar(50) Profession
  updateDate Date(8) Date of Update
  updateTime Int(11) Update Time
  Title nVarChar(10) Title
  BirthCity nVarChar(100) City of Birth
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  FirstName nVarChar(50) First Name
  MiddleName nVarChar(50) Middle Name
  LastName nVarChar(50) Last Name
  BirthState nVarChar(3) State of Birth ->OCST
  ResidCity nVarChar(100) City of Residence
  ResidCntry nVarChar(100) Country of Residence
  ResidState nVarChar(3) State of Residence ->OCST
  NFeRcpn VarChar(1) NF-e Recipient default=N [Y=Yes, N=No]
  EmlGrpCode nVarChar(20) E-Mail Group Code ->OEGP
  BlockComm VarChar(1) Block Sending Marketing default=N [N=No, Y=Yes]
  FiscalCode nVarChar(16) Fiscal Code for Resident
  CtyPrvsYr nVarChar(100) City for Previous Year
  SttPrvsYr nVarChar(3) State for Previous Year ->OCST
  CtyCdPrvsY nVarChar(4) City Code for Previous Year
  CtyCurYr nVarChar(100) City for Current Year
  SttCurYr nVarChar(3) State for Current Year ->OCST
  CtyCdCurYr nVarChar(4) City Code for Current Year
  NotResdSch VarChar(1) Not resident Schumacker [Y=Yes, N=No]
  CtyFsnCode nVarChar(100) Fusione comuni
  NaturalPer VarChar(1) Natural Person default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time Incl. Sec.

# OCQG - Card Properties
Module: Business Partners | 4 columns | ObjType: 44
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupCode
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Property Group Code
  GroupName nVarChar(50) Property Name
  UserSign Int(6) User Signature ->OUSR
  Filler nVarChar(10) Filler

# OCRB - BP - Bank Account
Module: Business Partners | 46 columns | ObjType: 187
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode, Account, BankCode, Country
  ABSENTRY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Key
  CardCode nVarChar(15) BP Code ->OCRD
  BankCode nVarChar(30) Bank Code
  Country nVarChar(3) Country ->OCRY
  Account nVarChar(50) Account No.
  Branch nVarChar(50) Branch
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  State nVarChar(3) State
  ControlKey nVarChar(2) Ctrl Int. ID
  UsrNumber1 nVarChar(25) User No. 1
  UsrNumber2 nVarChar(25) User No. 2
  UsrNumber3 nVarChar(25) User No. 3
  UsrNumber4 nVarChar(25) User No. 4
  IBAN nVarChar(50) IBAN
  LogInstanc Int(11) Log Instance default=0
  Building Text(16) Building/Floor/Room
  AliasName nVarChar(50) Alias Name
  AcctType VarChar(1) Account Type
  BankKey Int(11) Bank Internal ID ->ODSC
  BIK nVarChar(15) BIK
  AcctName nVarChar(250) Bank Account Name
  CorresAcct nVarChar(30) Correspondent Account
  Phone nVarChar(25) Phone
  Fax nVarChar(25) Fax
  ISRType Int(6) ISR Type default=2 [1=ISR, 2=BISR, 3=ISR+, 4=BISR+]
  ISRBillerI nVarChar(9) ISR Biller ID
  CustIdNum nVarChar(6) Customer ID Number default=0
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  SwiftNum nVarChar(50) BIC/SWIFT Code
  ABARoutNum nVarChar(25) ABA Routing Number
  MandateID nVarChar(35) Mandate ID
  SignDate Date(8) Date of Signature
  PWZAbsEntr Int(11) PWZ ABS Entry ->OPWZ
  BranchChk nVarChar(5) Branch Check Digit
  MandatDate Date(8) Date Of Mandate Expiration
  SeqType nVarChar(4) SEPA Seq. Type [OOFF=OOFF, FRST=FRST, RCUR=RCUR, FNAL=FNAL]
  ActType VarChar(1) Account Type [C=Checking Account, S=Savings Account]
  IsPrenot VarChar(1) Is Prenotification default=N [Y=Yes, N=No]
  EnAccount Text(16) Encryption of Account
  EnIBAN Text(16) Encryption of IBAN
  EncryptIV nVarChar(100) Encrypt IV

# OCRD - Business Partner
Module: Business Partners | 367 columns | ObjType: 2
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode
  CARD_NAME: CardName
  CARD_TYPE: CardType
  FATHER: FatherCard
  TERMS: GroupNum
  CURRENCY: Currency
  COM_GROUP: CommGrCode
  PRICE_LIST: ListNum
  PAY_ACCT: DebPayAcct
  ABS_ENTRY U: DocEntry
  OWNER_CODE: OwnerCode
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
  DebtLine Num(19,6) Payable Limit
  Discount Num(19,6) Discount %
  VatStatus VarChar(1) Tax Definition default=Y [Y=Liable, N=Exempted, E=EU]
  LicTradNum nVarChar(32) Federal Tax ID
  DdctStatus VarChar(1) Liable for Ded. at Source default=N [Y=Yes, N=No]
  DdctPrcnt Num(19,6) Withholding Tax Deduction %
  ValidUntil Date(8) Expiration Date for -% of Deduction
  Chrctrstcs Int(11) Properties
  ExMatchNum Int(11) Last Ext. Reconciliation No.
  InMatchNum Int(11) Last Int. Reconciliation No.
  ListNum Int(6) Price List No. ->OPLN
  DNoteBalFC Num(19,6) Open DN Balance in BP Curr.
  OrderBalFC Num(19,6) Open Orders Bal. in BP Curr.
  DNoteBalSy Num(19,6) Open Deliveries/GRPO Balance in SC
  OrderBalSy Num(19,6) Open Orders Balance in SC
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  BalTrnsfrd VarChar(1) Balances transferred default=N [Y=Yes, N=No]
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
  Cellular nVarChar(50) Mobile Phone
  AvrageLate Int(6) Average Payment Delay in Days
  City nVarChar(100) Bill-to City
  County nVarChar(100) Bill-to County
  Country nVarChar(3) Bill-to Country ->OCRY
  MailCity nVarChar(100) Ship-to City
  MailCounty nVarChar(100) Ship-to County
  MailCountr nVarChar(3) Ship-to Country ->OCRY
  E_Mail nVarChar(100) E-Mail
  Picture nVarChar(200) Picture
  DflAccount nVarChar(50) Default Account
  DflBranch nVarChar(50) Default Branch
  BankCode nVarChar(30) Default Bank default=-1
  AddID nVarChar(64) ID No. 2
  Pager nVarChar(30) Pager
  FatherCard nVarChar(15) BP Summary ->OCRD
  CardFName nVarChar(100) Foreign Name
  FatherType VarChar(1) Parent Summary Type default=P [P=Payments Summary, D=Delivery Consolidation]
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
  DscntObjct Int(6) Object for Discounts default=-1 [-1=, 52=Groups, 8=Properties, 43=Companies, 4=Items]
  DscntRel VarChar(1) Discounts Ratio default=L [L=Lowest Discount, H=Highest Discount, A=Average Disc., S=Discount Totals, M=Discount Multiples]
  SPGCounter Int(6) SPG Counter default=0
  SPPCounter Int(11) SPP Counter default=0
  DdctFileNo nVarChar(9) Tax Deduction File Number
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
  LocMth VarChar(1) LC Reconciliation default=Y [Y=Yes, N=No]
  validFor VarChar(1) Active default=N [Y=Yes, N=No]
  validFrom Date(8) Active From
  validTo Date(8) Active To
  frozenFor VarChar(1) Inactive default=N [Y=Yes, N=No]
  frozenFrom Date(8) Inactive From
  frozenTo Date(8) Inactive To
  sEmployed VarChar(1) Self-Employed default=N [Y=Yes, N=No]
  MTHCounter Int(11) MTH Counter
  BNKCounter Int(11) BNK Counter
  DdgKey Int(11) Withholding Tax Deduction Grp default=-1 ->ODDG
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
  DebPayAcct nVarChar(15) Accounts Receivable/Payable ->OACT
  ShipToDef nVarChar(50) Ship-to-Default
  Block nVarChar(100) Bill-to Block
  MailBlock nVarChar(100) Ship-to Block
  Password nVarChar(32) Password
  ECVatGroup nVarChar(8) Tax Group ->OVTG
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  IBAN nVarChar(50) IBAN
  DocEntry Int(11) Internal Number
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
  VatIdUnCmp nVarChar(32) Unified Federal Tax ID
  AgentCode nVarChar(32) Agent Code ->OAGP
  TolrncDays Int(6) Tolerance Days
  SelfInvoic VarChar(1) Self Invoice
  DeferrTax VarChar(1) Deferred Tax [Y=Yes, N=No]
  LetterNum nVarChar(20) Tax Exemption Letter No.
  MaxAmount Num(19,6) Max. Exemption Amount
  FromDate Date(8) Exemption Validity Date From
  ToDate Date(8) Exemption Validity Date To
  WTLiable VarChar(1) Subject to Withholding Tax [Y=Yes, N=No]
  CrtfcateNO nVarChar(20) Certificate No.
  ExpireDate Date(8) Expiration Date
  NINum nVarChar(20) Registration No.
  AccCritria VarChar(1) Accrual default=N [Y=Yes, N=No]
  WTCode nVarChar(4) WTax Code ->OWHT
  Equ VarChar(1) Equalization Tax default=N [Y=Yes, N=No]
  HldCode nVarChar(20) Holidays Name ->OHLD
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
  BoEPrsnt nVarChar(15) Customer Bill of Exchang Pres ->OACT
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
  CDPNum Int(6) Closing Date Procedure Number ->OCDP
  DflBankKey Int(11) Default Bank Key ->ODSC
  BCACode nVarChar(3) Bank Charges Allocation Codes ->OBCA
  UseShpdGd VarChar(1) Use Shipped Goods Account default=Y [Y=Yes, N=No]
  RegNum nVarChar(32) Company Reg. No. (CRN)
  VerifNum nVarChar(32) WTax Verification No.
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
  ResidenNum VarChar(1) Residence Number default=1 [1=Spanish Fiscal ID, 2=VAT Registration Number, 3=Passport, 4=Fiscal ID Issued by the Country of Residence, 5=Certificate of Fiscal Residence, 6=Other Document, 7=Not Registered]
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
  free312 VarChar(1) Free312
  free313 VarChar(1) Free313
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
  ExcptnlEvt VarChar(1) Exceptional Event [1=Vittime di richieste estorsive, 2=Soggetti colpiti dagli eventi sismici in data 24 agosto 2016, 3=Soggetti nel comune di Lampedusa e Linosa, emergenza umanitaria, 4=Soggetti colpiti dagli eventi sismici in ottobre 2016, 5=Soggetti colpiti da eventi sismici in gennaio 2017, 8=Altri eventi eccezionali]
  ExpnPrfFnd Num(19,6) Professional Funds Expenses
  EdrsFromBP VarChar(1) Endorsable Checks from This BP default=Y [Y=Yes, N=No]
  EdrsToBP VarChar(1) This BP Accepts Endorsed Checks default=N [Y=Yes, N=No]
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
  PriceMode VarChar(1) Price Mode [N=Net, G=Gross]
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
  TspEntry Int(11) Default Transporter ->OTSP
  TspLine Int(11) Default Transportation Line

# OCRG - Card Groups
Module: Business Partners | 9 columns | ObjType: 10
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: GroupCode
  GROUP_TYPE: GroupType
  GROUP_NAME U: GroupName
Fields (name type(len) description [values] ->parent table):
  GroupCode Int(6) Group No.
  GroupName nVarChar(20) Group Name
  GroupType VarChar(1) Group Type default=C [C=Customer Group, S=Vendor Group]
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  PriceList Int(6) Price List ->OPLN
  DiscRel VarChar(1) Effective Discount Groups default=L [L=Lowest Discount, H=Highest Discount, A=Average, S=Total, M=Discount Multiples]
  EffecPrice VarChar(1) Effective Price default=D [D=Default Priority, L=Lowest Price, H=Highest Price]

# OCRW - BP for IIS Annual
Module: Business Partners | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsEntry
  BP_YEAR U: Year, CardCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number
  CardCode nVarChar(15) BP Code
  Year Int(6) Report Year
  SentMeth VarChar(1) Method of Sending [D=Doc. Date, T=Tax Date]
  SentValue Num(19,6) Sent Value
  LastAMeth VarChar(1) Last Accepted Method [D=Doc. Date, T=Tax Date]
  LastAValue Num(19,6) Last Accepted Value
  ReportID nVarChar(50) Report ID

# ODDT - Withholding Tax Deduction Hierarchy
Module: Business Partners | 12 columns | ObjType: 116
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Numerator
  CARD U: TrcCode, WHShaamGrp, CardCode
Fields (name type(len) description [values] ->parent table):
  Numerator Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  TrcCode nVarChar(10) Hierarchy Code
  TrcName nVarChar(30) Hierarchy Name
  DateFrom Date(8) Valid From
  DateTo Date(8) Valid Until
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  LastUpdate Date(8) Last Update Date
  WHShaamGrp VarChar(1) Withholding Shaam Group default=1 [1=Services and Asset, 2=Agricultural Products, 3=Insurance Commissions, 4=Withholding Tax Instructions, 5=Interest, Exchange Rate Differences]
  DdctPrcnt Num(19,6) Deduction %
  MaxSum Num(19,6) Maximum Total

# ODUN - Dunning Letters
Module: Business Partners | 8 columns | ObjType: 151
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum
Fields (name type(len) description [values] ->parent table):
  LineNum Int(11) Row Number
  LetrFormat nVarChar(8) Letter Format
  EffctAftr nVarChar(3) Effective After (Days)
  LetterFee Num(19,6) Fee Per Letter
  FeeCurr nVarChar(3) Fee Currency
  MinBalance Num(19,6) Minimum Balance
  MinBlnCurr nVarChar(3) Minimum Balance Currency
  CalcIntert VarChar(1) Interest default=N [Y=Yes, N=No]

# OEGP - E-Mail Group
Module: Business Partners | 6 columns | ObjType: 234000004
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: EmlGrpCode
Fields (name type(len) description [values] ->parent table):
  EmlGrpCode nVarChar(20) E-Mail Group Code
  EmlGrpName nVarChar(100) E-Mail Group Name
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(11) User Signature ->OUSR
  LogInstanc Int(11) Log Instance

# OOAT - Blanket Agreement
Module: Business Partners | 53 columns | ObjType: 1250000025
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: AbsID
  NUM U: Instance, BpType, PIndicator, Number
Fields (name type(len) description [values] ->parent table):
  AbsID Int(11) Agreement No.
  BpCode nVarChar(15) BP Code ->OCRD
  BpName nVarChar(100) BP Name
  CntctCode Int(11) Contact Person ->OCPR
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  TermDate Date(8) Termination Date
  Descript nVarChar(254) Description
  Type VarChar(1) Agreement Type default=G [G=General, S=Specific]
  Status VarChar(1) Agreement Status default=D [A=Approved, B=To Be Approved, F=On Hold, D=Draft, T=Terminated, C=Canceled, X=To Be Terminated, P=To Be On Hold]
  Owner Int(11) Owner ->OHEM
  Renewal VarChar(1) Renewal default=N [Y=Yes, N=No]
  UseDiscnt VarChar(1) Use BP Special Price default=Y [Y=Yes, N=No]
  RemindVal Int(6) Reminder
  RemindUnit VarChar(1) Reminder Unit default=D [D=Day(s), W=Week(s), M=Month(s)]
  Remarks Text(16) Remarks
  AtchEntry Int(11) Attachment Entry ->OATC
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdtDate Date(8) Update Date
  CreateDate Date(8) Create Date
  Cancelled VarChar(1) Canceled default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Upgrade, M=Import, O=DI API, A=Auto Summary, D=Restore Wizard, P=Partner Implementation, T=Year of Transfer]
  Transfered VarChar(1) Year Transfer default=N [Y=Yes, N=No]
  RemindFlg VarChar(1) Reminder Sent default=N [Y=Yes, N=No]
  Fulfilled VarChar(1) Fulfilled default=N [Y=Fulfilled, N=Not Fulfilled]
  Attachment Text(16) Attachments
  SettleProb Num(19,6) Settlement Probability %
  UpdtTime Int(11) Update Time
  Method VarChar(1) Agreement Method default=I [I=Items Method, M=Monetary Method]
  GroupNum Int(6) Payment Terms Code ->OCTG
  ListNum Int(6) Price List No. ->OPLN
  SignDate Date(8) Signing Date
  AmendedTo Int(11) Amendment To
  Series Int(11) Series ->NNM1
  Number Int(11) Number
  ObjType nVarChar(20) Object Type default=1250000025 ->ADP1
  Handwrtten VarChar(1) Manual Numbering default=N
  PIndicator nVarChar(10) Period Indicator ->OPID
  BpType VarChar(1) BP Type default=C [C=Customer, S=Vendor]
  Instance Int(6) Instance default=0
  PayMethod nVarChar(15) Payment Method ->OPYM
  NumAtCard nVarChar(100) Customer/Vendor Ref. No.
  BPCurr nVarChar(3) BP Currency ->OCRN
  FixedRate Num(19,6) Exchange Rate
  TrnspCode Int(6) Shipping Type ->OSHP
  Project nVarChar(20) Project Code ->OPRJ
  PriceMode VarChar(1) Price Mode default=N [N=Net, G=Gross]
  WddStatus VarChar(1) Authorization Status default=- [-=Without, W=Pending, Y=Approved, N=Rejected, P=Generated, A=Generated by Authorizer, C=Canceled]
  FromStat VarChar(1) From Status default=D [F=On Hold, D=Draft]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  SAPPassprt Text(16) Extended SAP Passport

# OPRT - Partners
Module: Business Partners | 8 columns | ObjType: 108
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: PrtId
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  PrtId Int(11) Sequence No.
  Name nVarChar(15) Name
  RelatnType nVarChar(20) Relationship Type
  RelatCard nVarChar(15) Related BP ->OCRD
  Memo nVarChar(50) Details
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  DefaultORL Int(11) Default Relationship ->OORL

# ORPT - Response Type
Module: Business Partners | 3 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: RspType
Fields (name type(len) description [values] ->parent table):
  Dscrptn nVarChar(100) Response Description
  RspType nVarChar(20) Response Type
  IsActived VarChar(1) Active default=Y [Y=Yes, N=No]

# OSCN - Customer/Vendor Cat. No.
Module: Business Partners | 8 columns | ObjType: 73
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Substitute, CardCode, ItemCode
  CARD_SCN: Substitute, CardCode
  CARD: ItemCode, CardCode
  ITEM: CardCode, ItemCode
  SUBSTITUTE: Substitute
Fields (name type(len) description [values] ->parent table):
  ItemCode nVarChar(50) Item No. ->OITM
  CardCode nVarChar(15) BP Code ->OCRD
  Substitute nVarChar(50) BP Catalog Number
  Transfered VarChar(1) Postponed to Next Year default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  ShowSCN VarChar(1) Display BP Catalog Number default=N [Y=Yes, N=No]

# OSLP - Sales Employee
Module: Business Partners | 15 columns | ObjType: 53
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: SlpCode
  SLP_NAME U: SlpName
  COM_GROUP: GroupCode
Fields (name type(len) description [values] ->parent table):
  SlpCode Int(11) Sales Employee Code
  SlpName nVarChar(155) Sales Employee Name
  Memo nVarChar(50) Remarks
  Commission Num(19,6) % Commission for Sales Employee
  GroupCode Int(6) Commission Group default=0 ->OCOG
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  EmpID Int(11) Employee ID ->OHEM
  Active VarChar(1) Active default=Y [Y=Active, N=Inactive]
  Telephone nVarChar(20) Telephone
  Mobil nVarChar(50) Mobile
  Fax nVarChar(20) Fax
  Email nVarChar(100) E-Mail
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]

# OTBP - Target Group Business Partner
Module: Business Partners | 16 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: CardCode
Fields (name type(len) description [values] ->parent table):
  CardCode nVarChar(15) BP Code
  CardName nVarChar(100) BP Name
  CntctPrsn nVarChar(90) Contact Person
  Title nVarChar(10) Title
  Position nVarChar(90) Position
  E_Mail nVarChar(100) E-Mail
  Telephone nVarChar(20) Telephone
  Cellolar nVarChar(50) Mobile Phone
  Fax nVarChar(20) Fax
  Address nVarChar(100) Address
  Street nVarChar(100) Street/PO Box
  Block nVarChar(100) Block
  City nVarChar(100) City
  ZipCode nVarChar(20) Zip Code
  County nVarChar(100) County
  Building nVarChar(100) Building/Floor/Room

# OTER - Territories
Module: Business Partners | 5 columns | ObjType: 200
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: territryID
  LOCATION U: lindex, parent
  DESCRIPT: descript
Fields (name type(len) description [values] ->parent table):
  territryID Int(11) Territory ID
  descript nVarChar(200) Description
  parent Int(11) Superordinate Object default=-1 ->OTER
  lindex Int(11) Location Index
  inactive VarChar(1) Inactive default=N [Y=Yes, N=No]

# OTGG - Target Group
Module: Business Partners | 3 columns | ObjType: 1320000002
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TargetCode
Fields (name type(len) description [values] ->parent table):
  TargetCode nVarChar(20) Target Group Code
  TargetName nVarChar(100) Target Group Name
  TargetType VarChar(1) Target Group Type default=C [C=Customer, S=Vendor]

# OVTP - Vendor Type
Module: Business Partners | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: ABSEntry
  TYPE: VendorType
Fields (name type(len) description [values] ->parent table):
  ABSEntry Int(11) Primary Key
  VendorType nVarChar(32) Vendor Type
  Descript nVarChar(120) Description
  Locked VarChar(1) Locked default=N

# TGG1 - Target Group Details
Module: Business Partners | 32 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineNum, TargetCode
Fields (name type(len) description [values] ->parent table):
  TargetCode nVarChar(20) Target Group Code ->OTGG
  CardCode nVarChar(15) BP Code
  CardName nVarChar(100) BP Name
  GroupCode nVarChar(20) Group Code
  Industry Text(16) Industry
  validFor VarChar(1) Active [A=Active, I=Inactive]
  CntctPrsn nVarChar(50) Contact Person ->OCPR
  Title nVarChar(10) Title
  Position nVarChar(90) Position
  E_Mail nVarChar(100) E-Mail
  Telephone nVarChar(20) Telephone
  Cellolar nVarChar(50) Mobile Phone
  Fax nVarChar(20) Fax
  Address nVarChar(100) Address
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  City nVarChar(100) City
  ZipCode nVarChar(20) Zip Code
  County nVarChar(100) County
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country ->OCRY
  Building Text(16) Building/Floor/Room
  LineNum Int(11) Line Number
  FirstName nVarChar(50) First Name
  MiddleName nVarChar(50) Middle Name
  LastName nVarChar(50) Last Name
  LicTradNum nVarChar(32) Federal Tax ID
  AddrType nVarChar(100) Address Type
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  StreetNo nVarChar(100) Street No.
  AddressID nVarChar(50) Address ID

# USR6 - User Branch Assignment
Module: Business Partners | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BPLId, UserCode
Fields (name type(len) description [values] ->parent table):
  UserCode nVarChar(25) User Code ->OUSR
  BPLId Int(11) Assigned Branch ->OBPL
  DigCrtPath Text(16) Digital Certificate Path
  AcsDsbldBP VarChar(1) Access Disabled BP default=N [Y=Yes, N=No]

# WTD3 - WTax Codes Details for BP
Module: Business Partners | 12 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
  BP U: DetailType, DateFrom, KeyPart2, KeyPart1, WTCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  KeyPart1 nVarChar(15) BP Key Part 1
  KeyPart2 nVarChar(15) BP Key Part 2
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  Rate Num(19,6) Currency Rate
  DetailType nVarChar(2) Type of Detailed Information [A=Allowed, S=Special Rate, E=Exemption]
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, P=Partner Implementation, U=UI Reproweb Autocomplete]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0

# WTD4 - WTax Codes Details for Item
Module: Business Partners | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
  ITEM U: DateFrom, ItemCode, WTCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  ItemCode nVarChar(50) Item No. ->OITM
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, P=Partner Implementation]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0

# WTD5 - WTax Codes Details for Freight
Module: Business Partners | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LineId, AbsEntry
  EXPNSCODE U: DateFrom, ExpnsCode, WTCode
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Internal Number ->OWTD
  LineId Int(11) Row Number
  WTCode nVarChar(4) WTax Code
  ExpnsCode Int(11) Freight Code ->OEXD
  DateFrom Date(8) Effective Date From
  DateTo Date(8) Effective Date To
  DataSource VarChar(1) Data Source default=N [N=Unknown, M=Import, O=DI API, P=Partner Implementation]
  UpdateDate Date(8) Date of Update
  LogInstanc Int(11) Log Instance default=0
