<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# AHEM - Employees - History
Module: Human Resources | 135 columns
Indexes (name: columns; first = primary key; U = unique):
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
