<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACP1 - Campaign - BPs
Module: Business Partners | 45 columns
Indexes (name: columns; first = primary key; U = unique):
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
