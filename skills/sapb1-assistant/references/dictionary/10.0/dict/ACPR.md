<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACPR - Contact Persons - History
Module: Business Partners | 54 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CntctCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  CntctCode Int(11) Internal Number
  CardCode nVarChar(15) BP Code ->OCRD
  Name nVarChar(50) Contact Person Name
  Position nVarChar(90) Position
  Address nVarChar(254) Address
  Tel1 nVarChar(50) Telephone 1
  Tel2 nVarChar(50) Telephone 2
  Cellolar nVarChar(50) Mobile Phone Number
  Fax nVarChar(50) Fax Number
  E_MailL nVarChar(100) E-Mail
  Pager nVarChar(30) Pager
  Notes1 nVarChar(100) Remark 1
  Notes2 nVarChar(100) Remark 2
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
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
  ResidCntry nVarChar(100) Country/Region of Residence
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
  EncryptIV nVarChar(100) Encrypt IV
  CnnectAddr nVarChar(50) Connected Address
  CnAddrType VarChar(1) Connected Address Type [S=Ship To, B=Bill To]
  Frgncntry nVarChar(3) Stato Estero
