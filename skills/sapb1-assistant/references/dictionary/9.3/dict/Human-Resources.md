<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->

# AHE1 - Absence Information
Module: Human Resources | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee ID ->OHEM
  line Int(6) Absence Information Row
  fromDate Date(8) Absence from
  toDate Date(8) Absence to
  reason nVarChar(20) Reason
  approvedBy nVarChar(20) Approved By
  cnfrmrNum Int(11) Confirmer Number ->OHEM
  LogInstanc Int(11) Log Instance default=0
  type Int(11) Absence Type

# AHE2 - Education
Module: Human Resources | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Education: Information Row
  fromDate Date(8) Education from
  toDate Date(8) Education to
  type Int(11) Education Type ->OHED
  institute nVarChar(100) Institute
  major nVarChar(50) Major
  diploma nVarChar(50) Diploma
  LogInstanc Int(11) Log Instance default=0

# AHE3 - Employee Reviews
Module: Human Resources | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Employee Review Row
  date Date(8) Employee Review Date
  reviewDesc nVarChar(100) Review Description
  manager Int(11) Manager ->OHEM
  grade nVarChar(50) Grade
  remarks Text(16) Reviews
  LogInstanc Int(11) Log Instance default=0

# AHE4 - Previous Employment
Module: Human Resources | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Previous Employment Row
  fromDate Date(8) Employment from
  toDate Date(8) Employment to
  employer nVarChar(50) Employer
  position nVarChar(50) Position
  remarks Text(16) Previous Employment
  LogInstanc Int(11) Log Instance default=0

# AHE6 - Employee Roles
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Employee Role Row
  roleID Int(11) Role ID ->OHTY
  LogInstanc Int(11) Log Instance default=0

# AHE7 - Savings Payments
Module: Human Resources | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Row
  ConName nVarChar(50) Contract Name
  PmntNotes nVarChar(50) Payment Details
  AN Num(19,6) Employee
  AG Num(19,6) Employer
  BankName nVarChar(50) Bank Name
  BankCode nVarChar(20) Bank Code
  BankAcct nVarChar(20) Bank Account
  LogInstanc Int(11) Log Instance default=0
  ANCurrency nVarChar(3) Employee Currency
  AGCurrency nVarChar(3) Employer Currency
  Sequence VarChar(1) Frequency default=M [B=, M=Monthly, Q=Quarterly, S=Semi-annually, Y=Yearly]
  EnBnkAcct Text(16) Encryption of Bank Account
  EncryptIV nVarChar(100) Encrypt IV

# AHEM - Employees - History
Module: Human Resources | 135 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: LogInstanc, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No.
  lastName nVarChar(50) Last Name
  firstName nVarChar(50) First Name
  middleName nVarChar(50) Middle Name
  sex VarChar(1) Gender default=M [F=Female, M=Male, E=Not Specified]
  jobTitle nVarChar(20) Job Title
  type Int(11) Employee Type ->OHTY
  dept Int(6) Department ->OUDP
  branch Int(6) Branch ->OUBR
  workStreet nVarChar(100) Work Street
  workBlock nVarChar(100) Work Block
  workZip nVarChar(20) Work Zip Code
  workCity nVarChar(100) Work City
  workCounty nVarChar(100) Work County
  workCountr nVarChar(3) Work Country ->OCRY
  workState nVarChar(3) Work State
  manager Int(11) Manager ->OHEM
  userId Int(11) User ID ->OUSR
  salesPrson Int(11) Sales Employee ->OSLP
  officeTel nVarChar(20) Office Phone
  officeExt nVarChar(20) Office Ext.
  mobile nVarChar(20) Mobile Phone
  pager nVarChar(20) Pager
  homeTel nVarChar(20) Home Phone
  fax nVarChar(20) Fax
  email nVarChar(100) E-Mail
  startDate Date(8) Start Date
  status Int(11) Status ->OHST
  salary Num(19,6) Salary
  salaryUnit VarChar(1) Salary Unit default=M [H=Hour, D=Day, W=Week, M=Month, Y=Year, S=Semimonthly, B=Biweekly]
  emplCost Num(19,6) Employee Costs
  empCostUnt VarChar(1) Employee Cost Unit default=M [H=Hour, D=Day, W=Week, M=Month, Y=Year]
  termDate Date(8) Termination Date
  termReason Int(11) Termination Reason ->OHTR
  bankCode nVarChar(30) Bank Code ->ODSC
  bankBranch nVarChar(100) Bank Branch
  bankBranNo nVarChar(30) Bank Branch No.
  bankAcount nVarChar(100) Bank Account
  homeStreet nVarChar(100) Home Street
  homeBlock nVarChar(100) Home Block
  homeZip nVarChar(20) Home Zip Code
  homeCity nVarChar(100) Home City
  homeCounty nVarChar(100) Home County
  homeCountr nVarChar(3) Home Country ->OCRY
  homeState nVarChar(3) Home State
  birthDate Date(8) Date of Birth
  brthCountr nVarChar(3) Country of Birth ->OCRY
  martStatus VarChar(1) Marital Status default=S [S=Single, M=Married, D=Divorced, W=Widowed, N=Not Specified]
  nChildren Int(6) No. of Children
  govID nVarChar(64) ID Issued by Authorities
  citizenshp nVarChar(3) Citizenship ->OCRY
  passportNo nVarChar(64) Passport No.
  passportEx Date(8) Passport Expiration Date
  picture nVarChar(200) Picture
  remark Text(16) Remarks
  attachment Text(16) Attachments
  salaryCurr nVarChar(3) Salary Currency
  empCostCur nVarChar(3) Employee Costs Currency
  WorkBuild Text(16) Work Building/Floor/Room
  HomeBuild Text(16) Home Building/Floor/Room
  position Int(11) Position ->OHPS
  AtcEntry Int(11) Attachment Entry
  AddrTypeW nVarChar(100) Work Address Type
  AddrTypeH nVarChar(100) Home Address Type
  StreetNoW nVarChar(100) Work Street No.
  StreetNoH nVarChar(100) Home Street No.
  DispMidNam VarChar(1) Display Middle Name default=N [N=No, Y=Yes]
  NamePos VarChar(1) Name Positioning Set default=1 [1=Last Name, First Name, 2=First Name, Last Name]
  DispComma VarChar(1) Display Comma default=N [N=No, Y=Yes]
  CostCenter nVarChar(8) Cost Center ->OPRC
  CompanyNum nVarChar(20) Company Number
  VacPreYear Int(11) Vacation: Previous Year
  VacCurYear Int(11) Vacation: Current Year
  MunKey nVarChar(20) Municipality Key
  TaxClass nVarChar(2) Tax Class default=0 [0=, 1=Tax Class I, 2=Tax Class II, 3=Tax Class III, 4=Tax Class IV, 5=Tax Class V, 6=Tax Class VI]
  InTaxLiabi nVarChar(2) Income Tax Liability default=0 [0=, 1=On Tax Card, 2=Flat-Rate Tax, 3=Cross-Border Employee, 4=Not Liable]
  EmTaxCCode nVarChar(9) Religion default=0 [0=, --=No Church Tax Liability, AK=(AK) Old Catholic, EV=(EV) Protestant, FA=(FA) Non-Denomination Alzey, FB=(FB) Non-Denominational Regional Congregation Baden, FG=(FG) Non-Denominational Regional Congregation Palatinate, FM=(FM) Non-Denominational Congregation Mainz, FR=(FR) French-Reformed, FS=(FS) Non-Denominational Congregation Offenbach/Mainz, IB=(IB) Israelite Religious Community Baden, IL=(IL) Israelite Rural, IS=(IS) Israelite, IW=(IW) Israelite Religious Community Wuerttemberg, JD=(JD) Jewish Religion Tax, JH=(JH) Jewish Religion Tax, JS=(JS) Jewish Religion Tax, LT=(LT) Lutheran, RF=(RF) Reformed, RK=(RK) Roman Catholic]
  RelPartner nVarChar(9) Religion of Partner default=0 [0=, --=No Church Tax Liability, AK=(AK) Old Catholic, EV=(EV) Protestant, FA=(FA) Non-Denomination Alzey, FB=(FB) Non-Denominational Regional Congregation Baden, FG=(FG) Non-Denominational Regional Congregation Palatinate, FM=(FM) Non-Denominational Congregation Mainz, FR=(FR) French-Reformed, FS=(FS) Non-Denominational Congregation Offenbach/Mainz, IB=(IB) Israelite Religious Community Baden, IL=(IL) Israelite Rural, IS=(IS) Israelite, IW=(IW) Israelite Religious Community Wuerttemberg, JD=(JD) Jewish Religion Tax, JH=(JH) Jewish Religion Tax, JS=(JS) Jewish Religion Tax, LT=(LT) Lutheran, RF=(RF) Reformed, RK=(RK) Roman Catholic]
  ExemptAmnt Num(19,6) Exemption Amount
  ExemptUnit nVarChar(20) Exemption Amount Period default=0 [0=, 1=Yearly, 2=Monthly, 3=Weekly, 4=Daily]
  AddiAmnt Num(19,6) Additional Amount
  AddiUnit nVarChar(20) Additional Amount Period default=0 [0=, 1=Yearly, 2=Monthly, 3=Weekly, 4=Daily]
  TaxOName nVarChar(50) Tax Office Name
  TaxONum nVarChar(20) Tax Office Number
  HeaInsName nVarChar(50) Health Insurance Company Name
  HeaInsCode nVarChar(50) Health Insurance Code
  HeaInsType nVarChar(20) Type of Health Insurance [=, AOK=(AOK), IKK=(IKK), EKK=(EKK), BKK=(BKK), BKS=(BKS), LKK=(LKK)]
  SInsurNum nVarChar(20) Social Insurance Number
  StatusOfP nVarChar(2) Professional Status default=-1 [-1=, 0=Trainee, 1=Worker, 2=Skilled Worker, 3=Supervisor/Foreman, 4=Office Worker, 5=Youth Help/Sheltered Workshop, 6=On Career Advancement Training, 7=Homeworker, 8=Part Time, 9=Part Time > 18 Hrs]
  StatusOfE nVarChar(2) Educational Status default=0 [0=, 1=W/o Professional Qualification, 2=W. Professional Qualification, 3=High School w/o Prof. Qualif., 4=High School w. Prof. Qualific., 5=Vocational Qualification, 6=University, 7=Not Possible to Specify]
  BCodeDateV nVarChar(20) Bank Code for DATEV
  DevBAOwner VarChar(1) Deviating Bank Account Owner default=N [Y=Yes, N=No]
  FNameSP nVarChar(50) First Name of Spouse
  SurnameSP nVarChar(50) Last Name of Spouse
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  PersGroup nVarChar(5) Person Group default=-1 [-1=, 101=Subject to Social Insurance, 102=Apprentice, 104=Home Worker, 105=Trainee, 106=Student, 108=Early Retirement, 109=Part-Time Employee, 110=Short-Term Employee, 112=Family Member: Agriculture, 113=Addnl Income: Agriculture, 114=Addnl Income: Seasonal Agriculture, 116=Receiving Compensation Pay, 118=Irregularly Employed, 119=Pensioner, 997=Not Specified]
  JTCode nVarChar(5) Job Title Code
  ExtEmpNo nVarChar(20) Ext. Employee No.
  BirthPlace nVarChar(100) Place of Birth
  PymMeth nVarChar(2) Payment Method default=05 [-1=, 05=Bank Transfer]
  ExemptCurr nVarChar(3) Exemption Amount Currency
  AddiCurr nVarChar(3) Additional Amount Currency
  STDCode Int(11) STD Code
  FatherName nVarChar(150) Father's Name
  CPF nVarChar(100) Personal Fiscal ID
  CRC nVarChar(20) CRC Number
  ContResp VarChar(1) Accountant Responsible default=N [Y=Yes, N=No]
  RepLegal VarChar(1) Legal Representative default=N [Y=Yes, N=No]
  DirfDeclar VarChar(1) DIRF Responsible default=N [Y=Yes, N=No]
  UF_CRC nVarChar(3) CRC State
  IDType nVarChar(30) ID Type ->OIDT
  Active VarChar(1) Employee Status default=Y [Y=Active, N=Inactive]
  BPLId Int(11) Branch ->OBPL
  ManualNUM nVarChar(60) Manual EMP No.
  PassIssue Date(8) Passport Issue Date
  PassIssuer nVarChar(254) Passport Issuer
  QualCode nVarChar(3) Qualification Code default=000 [000=n/a, 203=Diretor, 204=Conselheiro de Administração, 205=Administrador, 206=Administrador do Grupo, 207=Administrador de Sociedade Filiada, 220=Administrador Judicial - Pessoa Fisica, 222=Administrador Judicial - Pessoa Juridica - profissional responsável, 223=Administrador Judicial / Gestor, 226=Gestor Judicial, 309=Procurador, 312=Inventariante, 313=Liquidante, 315=Interventor, 801=Empresário, 900=Contador, 999=Outros]
  PRWebAccss VarChar(1) Enable Access to PR from Web default=N [Y=Yes, N=No]
  PrePRWeb VarChar(1) Previous Stats of PR Web Access default=N [Y=Yes, N=No]
  BPLink nVarChar(15) BP Link ->OCRD
  NaturalPer VarChar(1) Natural Person default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  EnRligion Text(16) Encryption of Religion
  EnRligionP Text(16) Encryption of Religion Partner
  EncryptIV nVarChar(100) Encrypt IV
  EnGovID Text(16) Encryption of Government ID
  EnPassport Text(16) Encryption of Passport No.
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time Incl. Sec.
  UpdateTS Int(11) Update Full Time
  EnInsurNum Text(16) Encryption of Social Insurance No.
  EnBnkAcct Text(16) Encryption of Bank Account

# HEM1 - Absence Information
Module: Human Resources | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee ID ->OHEM
  line Int(6) Absence Information Row
  fromDate Date(8) Absence from
  toDate Date(8) Absence to
  reason nVarChar(20) Reason
  approvedBy nVarChar(20) Approved By
  cnfrmrNum Int(11) Confirmer Number ->OHEM
  LogInstanc Int(11) Log Instance default=0
  type Int(11) Absence Type

# HEM10 - Employee Branch Assignment
Module: Human Resources | 2 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: BPLId, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No.
  BPLId Int(11) Assigned Branch ->OBPL

# HEM2 - Education
Module: Human Resources | 9 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Education Information Row
  fromDate Date(8) Education from
  toDate Date(8) Education to
  type Int(11) Education Type ->OHED
  institute nVarChar(100) Institute
  major nVarChar(50) Major
  diploma nVarChar(50) Diploma
  LogInstanc Int(11) Log Instance default=0

# HEM3 - Employee Reviews
Module: Human Resources | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Employee Review Row
  date Date(8) Employee Review Date
  reviewDesc nVarChar(100) Review Description
  manager Int(11) Manager ->OHEM
  grade nVarChar(50) Grade
  remarks Text(16) Reviews
  LogInstanc Int(11) Log Instance default=0

# HEM4 - Previous Employment
Module: Human Resources | 8 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Previous Employment Row
  fromDate Date(8) Employment from
  toDate Date(8) Employment to
  employer nVarChar(50) Employer
  position nVarChar(50) Position
  remarks Text(16) Previous Employment
  LogInstanc Int(11) Log Instance default=0

# HEM5 - Employee Data Ownership Authorization
Module: Human Resources | 10 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: Object, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  Object nVarChar(20) The Object Number
  Peer VarChar(1) Peer Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type]
  Manager VarChar(1) Manager Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  Subord VarChar(1) Subordinate Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  Dept VarChar(1) Department Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  Branch VarChar(1) Branch Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  Team VarChar(1) Team Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type, =]
  AC Int(11) Cache Access Counter default=0
  Cmpny VarChar(1) Company Authorization default=N [F=Full, R=Read Only, N=None, U=Undefined Type]

# HEM6 - Employee Roles
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Employee Role Row
  roleID Int(11) Role ID ->OHTY
  LogInstanc Int(11) Log Instance default=0

# HEM7 - Savings Payments
Module: Human Resources | 15 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: line, empID
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No. ->OHEM
  line Int(6) Row
  ConName nVarChar(50) Contract Name
  PmntNotes nVarChar(50) Payment Details
  AN Num(19,6) Employee
  AG Num(19,6) Employer
  BankName nVarChar(50) Bank Name
  BankCode nVarChar(20) Bank Code
  BankAcct nVarChar(20) Bank Account
  LogInstanc Int(11) Log Instance default=0
  ANCurrency nVarChar(3) Employee Currency
  AGCurrency nVarChar(3) Employer Currency
  Sequence VarChar(1) Frequency default=M [B=, M=Monthly, Q=Quarterly, S=Semi-annually, Y=Yearly]
  EnBnkAcct Text(16) Encryption of Bank Account
  EncryptIV nVarChar(100) Encrypt IV

# HET1 - Employee Transfer Details
Module: Human Resources | 6 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: empID, TransferID
Fields (name type(len) description [values] ->parent table):
  TransferID Int(11) Foreign Key to OHET ->OHET
  empID Int(11) Foreign Key to OHEM ->OHEM
  Transfered Date(8) Timestamp: Status "Sent"
  Status VarChar(1) Processing Status default=N [N=New, S=Sent, A=Accepted, E=Error]
  Comment Text(16) Any comments
  TransTime Int(6) Time When Status Is "Sent"

# HLD1 - Holiday Dates
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: EndDate, StrDate, HldCode
Fields (name type(len) description [values] ->parent table):
  HldCode nVarChar(20) Holiday Code ->OHLD
  StrDate Date(8) Start Date
  EndDate Date(8) End Date
  Rmrks nVarChar(50) Remarks

# HTM1 - Team Members
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: empID, teamID
Fields (name type(len) description [values] ->parent table):
  teamID Int(11) Team ID ->OHTM
  line Int(6) Row
  empID Int(11) Employee ID ->OHEM
  role VarChar(1) Role in Team default=M [L=Leader, M=Member]

# OHED - Education Types
Module: Human Resources | 4 columns | ObjType: 175
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: edType
  NAME_KEY U: name
Fields (name type(len) description [values] ->parent table):
  edType Int(11) Education Type
  name nVarChar(20) Name
  descriptio Text(16) Description
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]

# OHEM - Employees
Module: Human Resources | 135 columns | ObjType: 171
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: empID
  OUSR: userId
  OSLP: salesPrson
  NAME: lastName, middleName, firstName
Fields (name type(len) description [values] ->parent table):
  empID Int(11) Employee No.
  lastName nVarChar(50) Last Name
  firstName nVarChar(50) First Name
  middleName nVarChar(50) Middle Name
  sex VarChar(1) Gender default=M [F=Female, M=Male, E=Not Specified]
  jobTitle nVarChar(20) Job Title
  type Int(11) Employee Type ->OHTY
  dept Int(6) Department ->OUDP
  branch Int(6) Branch ->OUBR
  workStreet nVarChar(100) Work Street
  workBlock nVarChar(100) Work Block
  workZip nVarChar(20) Work Zip Code
  workCity nVarChar(100) Work City
  workCounty nVarChar(100) Work County
  workCountr nVarChar(3) Work Country ->OCRY
  workState nVarChar(3) Work State
  manager Int(11) Manager ->OHEM
  userId Int(11) User ID ->OUSR
  salesPrson Int(11) Sales Employee ->OSLP
  officeTel nVarChar(20) Office Phone
  officeExt nVarChar(20) Office Ext.
  mobile nVarChar(20) Mobile Phone
  pager nVarChar(20) Pager
  homeTel nVarChar(20) Home Phone
  fax nVarChar(20) Fax
  email nVarChar(100) E-Mail
  startDate Date(8) Start Date
  status Int(11) Status ->OHST
  salary Num(19,6) Salary
  salaryUnit VarChar(1) Salary Unit default=M [H=Hour, D=Day, W=Week, M=Month, Y=Year, S=Semimonthly, B=Biweekly]
  emplCost Num(19,6) Employee Costs
  empCostUnt VarChar(1) Employee Cost Unit default=M [H=Hour, D=Day, W=Week, M=Month, Y=Year]
  termDate Date(8) Termination Date
  termReason Int(11) Termination Reason ->OHTR
  bankCode nVarChar(30) Bank Code ->ODSC
  bankBranch nVarChar(100) Bank Branch
  bankBranNo nVarChar(30) Bank Branch No.
  bankAcount nVarChar(100) Bank Account
  homeStreet nVarChar(100) Home Street
  homeBlock nVarChar(100) Home Block
  homeZip nVarChar(20) Home Zip Code
  homeCity nVarChar(100) Home City
  homeCounty nVarChar(100) Home County
  homeCountr nVarChar(3) Home Country ->OCRY
  homeState nVarChar(3) Home State
  birthDate Date(8) Date of Birth
  brthCountr nVarChar(3) Country of Birth ->OCRY
  martStatus VarChar(1) Marital Status default=S [S=Single, M=Married, D=Divorced, W=Widowed, N=Not Specified]
  nChildren Int(6) No. of Children
  govID nVarChar(64) ID Issued by Authorities
  citizenshp nVarChar(3) Citizenship ->OCRY
  passportNo nVarChar(64) Passport No.
  passportEx Date(8) Passport Expiration Date
  picture nVarChar(200) Picture
  remark Text(16) Remarks
  attachment Text(16) Attachments
  salaryCurr nVarChar(3) Salary Currency
  empCostCur nVarChar(3) Employee Costs Currency
  WorkBuild Text(16) Work Building/Floor/Room
  HomeBuild Text(16) Home Building/Floor/Room
  position Int(11) Position ->OHPS
  AtcEntry Int(11) Attachment Entry
  AddrTypeW nVarChar(100) Work Address Type
  AddrTypeH nVarChar(100) Home Address Type
  StreetNoW nVarChar(100) Work Street No.
  StreetNoH nVarChar(100) Home Street No.
  DispMidNam VarChar(1) Display Middle Name default=N [N=No, Y=Yes]
  NamePos VarChar(1) Name Positioning Set default=1 [1=Last Name, First Name, 2=First Name, Last Name]
  DispComma VarChar(1) Display Comma default=N [N=No, Y=Yes]
  CostCenter nVarChar(8) Cost Center ->OPRC
  CompanyNum nVarChar(20) Company Number
  VacPreYear Int(11) Vacation: Previous Year
  VacCurYear Int(11) Vacation: Current Year
  MunKey nVarChar(20) Municipality Key
  TaxClass nVarChar(2) Tax Class default=0 [0=, 1=Tax Class I, 2=Tax Class II, 3=Tax Class III, 4=Tax Class IV, 5=Tax Class V, 6=Tax Class VI]
  InTaxLiabi nVarChar(2) Income Tax Liability default=0 [0=, 1=On Tax Card, 2=Flat-Rate Tax, 3=Cross-Border Employee, 4=Not Liable]
  EmTaxCCode nVarChar(9) Confession default=0 [0=, --=No Church Tax Liability, AK=(AK) Old Catholic, EV=(EV) Protestant, FA=(FA) Non-Denomination Alzey, FB=(FB) Non-Denominational Regional Congregation Baden, FG=(FG) Non-Denominational Regional Congregation Palatinate, FM=(FM) Non-Denominational Congregation Mainz, FR=(FR) French-Reformed, FS=(FS) Non-Denominational Congregation Offenbach/Mainz, IB=(IB) Israelite Religious Community Baden, IL=(IL) Israelite Rural, IS=(IS) Israelite, IW=(IW) Israelite Religious Community Wuerttemberg, JD=(JD) Jewish Religion Tax, JH=(JH) Jewish Religion Tax, JS=(JS) Jewish Religion Tax, LT=(LT) Lutheran, RF=(RF) Reformed, RK=(RK) Roman Catholic]
  RelPartner nVarChar(9) Confession of Partner default=0 [0=, --=No Church Tax Liability, AK=(AK) Old Catholic, EV=(EV) Protestant, FA=(FA) Non-Denomination Alzey, FB=(FB) Non-Denominational Regional Congregation Baden, FG=(FG) Non-Denominational Regional Congregation Palatinate, FM=(FM) Non-Denominational Congregation Mainz, FR=(FR) French-Reformed, FS=(FS) Non-Denominational Congregation Offenbach/Mainz, IB=(IB) Israelite Religious Community Baden, IL=(IL) Israelite Rural, IS=(IS) Israelite, IW=(IW) Israelite Religious Community Wuerttemberg, JD=(JD) Jewish Religion Tax, JH=(JH) Jewish Religion Tax, JS=(JS) Jewish Religion Tax, LT=(LT) Lutheran, RF=(RF) Reformed, RK=(RK) Roman Catholic]
  ExemptAmnt Num(19,6) Exemption Amount
  ExemptUnit nVarChar(20) Exemption Amount Period default=0 [0=, 1=Yearly, 2=Monthly, 3=Weekly, 4=Daily]
  AddiAmnt Num(19,6) Additional Amount
  AddiUnit nVarChar(20) Additional Amount Period default=0 [0=, 1=Yearly, 2=Monthly, 3=Weekly, 4=Daily]
  TaxOName nVarChar(50) Tax Office Name
  TaxONum nVarChar(20) Tax Office Number
  HeaInsName nVarChar(50) Health Insurance Company Name
  HeaInsCode nVarChar(50) Health Insurance Code
  HeaInsType nVarChar(20) Type of Health Insurance [=, AOK=(AOK), IKK=(IKK), EKK=(EKK), BKK=(BKK), BKS=(BKS), LKK=(LKK)]
  SInsurNum nVarChar(20) Social Insurance Number
  StatusOfP nVarChar(2) Professional Status default=-1 [-1=, 0=Trainee, 1=Worker, 2=Skilled Worker, 3=Supervisor/Foreman, 4=Office Worker, 5=Youth Help/Sheltered Workshop, 6=On Career Advancement Training, 7=Homeworker, 8=Part Time, 9=Part Time > 18 Hrs]
  StatusOfE nVarChar(2) Educational Status default=0 [0=, 1=W/o Professional Qualification, 2=W. Professional Qualification, 3=High School w/o Prof. Qualif., 4=High School w. Prof. Qualific., 5=Vocational Qualification, 6=University, 7=Not Possible to Specify]
  BCodeDateV nVarChar(20) Bank Code for DATEV
  DevBAOwner VarChar(1) Deviating Bank Account Owner default=N [Y=Yes, N=No]
  FNameSP nVarChar(50) First Name of Spouse
  SurnameSP nVarChar(50) Last Name of Spouse
  LogInstanc Int(11) Log Instance default=0
  UserSign Int(6) User Signature ->OUSR
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date
  PersGroup nVarChar(5) Person Group default=-1 [-1=, 101=Subject to Social Insurance, 102=Apprentice, 104=Home Worker, 105=Trainee, 106=Student, 108=Early Retirement, 109=Part-Time Employee, 110=Short-Term Employee, 112=Family Member: Agriculture, 113=Addnl Income: Agriculture, 114=Addnl Income: Seasonal Agriculture, 116=Receiving Compensation Pay, 118=Irregularly Employed, 119=Pensioner, 997=Not Specified]
  JTCode nVarChar(5) Job Title Code
  ExtEmpNo nVarChar(20) Ext. Employee No.
  BirthPlace nVarChar(100) Place of Birth
  PymMeth nVarChar(2) Payment Method default=05 [-1=, 05=Bank Transfer]
  ExemptCurr nVarChar(3) Exemption Amount Currency
  AddiCurr nVarChar(3) Additional Amount Currency
  STDCode Int(11) STD Code
  FatherName nVarChar(150) Father's Name
  CPF nVarChar(100) Personal Fiscal ID
  CRC nVarChar(20) CRC Number
  ContResp VarChar(1) Accountant Responsible default=N [Y=Yes, N=No]
  RepLegal VarChar(1) Legal Representative default=N [Y=Yes, N=No]
  DirfDeclar VarChar(1) DIRF Responsible default=N [Y=Yes, N=No]
  UF_CRC nVarChar(3) CRC State
  IDType nVarChar(30) ID Type ->OIDT
  Active VarChar(1) Employee Status default=Y [Y=Active, N=Inactive]
  BPLId Int(11) Branch ->OBPL
  ManualNUM nVarChar(60) Manual EMP No.
  PassIssue Date(8) Passport Issue Date
  PassIssuer nVarChar(254) Passport Issuer
  QualCode nVarChar(3) Qualification Code default=000 [000=n/a, 203=Diretor, 204=Conselheiro de Administração, 205=Administrador, 206=Administrador do Grupo, 207=Administrador de Sociedade Filiada, 220=Administrador Judicial - Pessoa Fisica, 222=Administrador Judicial - Pessoa Juridica - profissional responsável, 223=Administrador Judicial / Gestor, 226=Gestor Judicial, 309=Procurador, 312=Inventariante, 313=Liquidante, 315=Interventor, 801=Empresário, 900=Contador, 999=Outros]
  PRWebAccss VarChar(1) Enable Access to PR from Web default=N [Y=Yes, N=No]
  PrePRWeb VarChar(1) Previous Stats of PR Web Access default=N [Y=Yes, N=No]
  BPLink nVarChar(15) BP Link ->OCRD
  NaturalPer VarChar(1) Natural Person default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  EnRligion Text(16) Encryption of Religion
  EnRligionP Text(16) Encryption of Religion Partner
  EncryptIV nVarChar(100) Encrypt IV
  EnGovID Text(16) Encryption of Government ID
  EnPassport Text(16) Encryption of Passport No.
  CreateDate Date(8) Creation Date
  CreateTS Int(11) Creation Time Incl. Sec.
  UpdateTS Int(11) Update Full Time
  EnInsurNum Text(16) Encryption of Social Insurance No.
  EnBnkAcct Text(16) Encryption of Bank Account

# OHET - Object: HR Employee Transfer
Module: Human Resources | 7 columns | ObjType: 480000001
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: TransferID
Fields (name type(len) description [values] ->parent table):
  TransferID Int(11) Unique ID for Transfer
  TransStart Date(8) Transfer Start Date
  TransEnd Date(8) Timestamp if Status is "Sent"
  Status VarChar(1) Processing Status default=N [N=New, P=Processing, S=Sent, R=Received, A=Accepted, E=Error]
  Comment Text(16) Any comments
  StartTime Int(6) Transfer Start Time
  EndTime Int(6) Time When Status Is "Sent"

# OHLD - Holiday Table
Module: Human Resources | 6 columns | ObjType: 186
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: HldCode
Fields (name type(len) description [values] ->parent table):
  HldCode nVarChar(20) Holidays Name
  WndFrm VarChar(1) Weekend From default=6 [1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday]
  WndTo VarChar(1) To default=1 [1=Sunday, 2=Monday, 3=Tuesday, 4=Wednesday, 5=Thursday, 6=Friday, 7=Saturday]
  isCurYear VarChar(1) Current Year default=Y [Y=Yes, N=No]
  ignrWnd VarChar(1) Ignore Weekend default=N
  WeekNoRule VarChar(1) Rule to Calculate Week Number default=J [J=First week starts on January 1, D=First week starts in first 4-day week, F=First week starts in first full week]

# OHPS - Employee Position
Module: Human Resources | 4 columns | ObjType: 210
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: posID
  NAME U: name
Fields (name type(len) description [values] ->parent table):
  posID Int(11) Item ID
  name nVarChar(20) Position Name
  descriptio Text(16) Description
  LocFields VarChar(1) Activate Localization Fields default=N [Y=, N=]

# OHST - Employee Status
Module: Human Resources | 3 columns | ObjType: 173
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: statusID
  NAME_KEY U: name
Fields (name type(len) description [values] ->parent table):
  statusID Int(11) Status ID
  name nVarChar(20) Name
  descriptio Text(16) Description

# OHTM - Employee Teams
Module: Human Resources | 3 columns | ObjType: 211
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: teamID
  NAME_KEY U: name
Fields (name type(len) description [values] ->parent table):
  teamID Int(11) Team ID
  name nVarChar(20) Team Name
  descriptio Text(16) Description

# OHTR - Termination Reason
Module: Human Resources | 3 columns | ObjType: 174
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: reasonID
  NAME_KEY U: name
Fields (name type(len) description [values] ->parent table):
  reasonID Int(11) Reason ID
  name nVarChar(20) Name
  descriptio Text(16) Description

# OHTY - Employee Types
Module: Human Resources | 4 columns | ObjType: 172
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: typeID
  NAME_KEY: name
Fields (name type(len) description [values] ->parent table):
  typeID Int(11) Employee Type ID
  name nVarChar(20) Name
  descriptio Text(16) Description
  locked VarChar(1) Locked default=N [Y=Yes, N=No]

# OIDT - Employee ID Type
Module: Human Resources | 4 columns
Indexes (name: columns; first = primary key; U = unique) - WARNING: multi-column key order here is reversed vs SAP's 10.0 reference (read as a set; see references/dictionary/INDEX.md):
  PRIMARY U: IDType
Fields (name type(len) description [values] ->parent table):
  IDType nVarChar(30) ID Type
  Locked VarChar(1) Locked default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
