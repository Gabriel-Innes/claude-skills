<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->

# ACT1 - Service Contract - Items
Module: Service | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContractID, Line, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No. ->OCTR
  Line Int(11) Row
  ManufSN nVarChar(36) Mfr. Serial No.
  InternalSN nVarChar(36) Serial Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  ItemGroup Int(6) Item Group ->OITB
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  ItmGrpName nVarChar(20) Item Group Name
  InsID Int(11) Customer Equipment Card ID ->OINS
  TermDate Date(8) Termination Date
  LogInstanc Int(11) Log Instance - History
  EncryptIV nVarChar(100) Encrypt IV

# ACT2 - Service Contract - Recurring Transactions
Module: Service | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContractID, RcpEntry, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No. ->OCTR
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance - History
  EncryptIV nVarChar(100) Encrypt IV

# ACTR - Service Contracts
Module: Service | 70 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContractID, LogInstanc
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No.
  CstmrCode nVarChar(15) Business Partner Code ->OCRD
  CstmrName nVarChar(100) Business Partner Name
  CntctCode Int(11) Contact Person Code ->OCPR
  Owner Int(6) Owner ->OUSR
  Status VarChar(1) Contract Status default=D [A=Approved, F=On Hold, D=Draft, T=Terminated]
  CntrcTmplt nVarChar(20) Contract Template ->OCTT
  CntrcType VarChar(1) Contract Type default=S [C=Business Partner, G=Item Group, S=Serial Number]
  Renewal VarChar(1) Renewal default=N [Y=Yes, N=No]
  RemindVal Int(6) Reminder Time
  RemindUnit VarChar(1) Remind Unit default=D [D=Days, W=Weeks, M=Months]
  Duration Int(6) Duration of Coverage
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  ResponsVal Int(6) Resolution Time
  ResponsUnt VarChar(1) Resolution Unit default=D [D=Days, H=Hours]
  Descriptio nVarChar(254) Description
  SrcDocType VarChar(1) Source Document Type default=I [Q=Sales Quotation, O=Sales Order, D=Delivery, I=A/R Invoice]
  DocNum Int(11) Source Document
  MonEnabled VarChar(1) Monday Enabled default=Y [Y=Yes, N=No]
  TueEnabled VarChar(1) Tuesday Enabled default=Y [Y=Yes, N=No]
  WedEnabled VarChar(1) Wednesday Enabled default=Y [Y=Yes, N=No]
  ThuEnabled VarChar(1) Thursday Enabled default=Y [Y=Yes, N=No]
  FriEnabled VarChar(1) Friday Enabled default=Y [Y=Yes, N=No]
  SatEnabled VarChar(1) Saturday Enabled default=Y [Y=Yes, N=No]
  SunEnabled VarChar(1) Sunday Enabled default=Y [Y=Yes, N=No]
  MonStart Int(6) Monday Start default=800
  MonEnd Int(6) Monday End default=1700
  TueStart Int(6) Tuesday Start default=800
  TueEnd Int(6) Tuesday End default=1700
  WedStart Int(6) Wednesday Start default=800
  WedEnd Int(6) Wednesday End default=1700
  ThuStart Int(6) Thursday Start default=800
  ThuEnd Int(6) Thursday End default=1700
  FriStart Int(6) Friday Start default=800
  FriEnd Int(6) Friday End default=1700
  SatStart Int(6) Saturday Start default=0
  SatEnd Int(6) Saturday End default=2359
  SunStrart Int(6) Sunday Start default=0
  SunEnd Int(6) Sunday End default=2359
  InclParts VarChar(1) Include Parts default=N [N=No, Y=Yes]
  InclWork VarChar(1) Include Labor default=N [N=No, Y=Yes]
  InclTravel VarChar(1) Include Travel default=N [N=No, Y=Yes]
  Attachment Text(16) Attachments
  CreateDate Date(8) Creation Date
  Remarks1 Text(16) Template Remarks
  Remarks2 Text(16) Remarks
  RemindFlg VarChar(1) Reminder Sent default=N [Y=Yes, N=No]
  CTR1Count Int(11) CTR1 Counter default=0
  DocEntry Int(11) Linked Document No.
  RemTmDays Int(11) Remind Time in Days
  ResTmHours Int(11) Response Time in Hours
  InclHldays VarChar(1) Include Holidays default=N [N=No, Y=Yes]
  SrvcType VarChar(1) Service Type default=R [R=Regular, W=Warranty]
  TermDate Date(8) Termination Date
  ResponseV Int(6) Response Time
  ResponseU VarChar(1) Response Unit default=H [D=Days, H=Hours]
  AtcEntry Int(11) Attachment Entry ->OATC
  Transfered VarChar(1) Year Transfer default=N
  Instance Int(6) Instance default=0
  BPType VarChar(1) BP Type default=R [R=Sales, P=Purchasing]
  OwnerCode Int(11) Service Contract Owner ->OHEM
  UserSign Int(6) User Signature ->OUSR
  ObjType nVarChar(20) Object Type - History default=190
  LogInstanc Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV
  Printed VarChar(1) Printed default=N

# AINS - Customer Equipment Card - History
Module: Service | 56 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: insID, logInstanc
Fields (name type(len) description [values] ->parent table):
  insID Int(11) Equipment Card Number
  customer nVarChar(15) Business Partner Code ->OCRD
  custmrName nVarChar(100) Business Partner Name
  contactCod Int(11) Contact Person Code ->OCPR
  directCsmr nVarChar(15) Direct Customer
  drctCsmNam nVarChar(100) Direct Customer Name
  manufSN nVarChar(36) Mfr. Serial No.
  internalSN nVarChar(36) Serial Number
  warranty VarChar(1) Warranty Flag default=N [Y=Yes, N=No]
  wrrntyStrt Date(8) Warranty Start Date
  wrrntyEnd Date(8) Warranty End Date
  responsVal Int(6) Time Required for Response
  responsUnt VarChar(1) Unit for the previous field default=D [H=Hour(s), D=Day(s)]
  itemCode nVarChar(50) Foreign Key To Item ->OITM
  itemName nVarChar(200) Item Description
  itemGroup Int(6) Item Group ->OITB
  manufDate Date(8) Manufacture Date
  delivery Int(11) Delivery Key ->ODLN
  deliveryNo Int(11) Delivery Number
  invoice Int(11) Invoice Key ->OINV
  invoiceNum Int(11) Invoice Number
  dlvryDate Date(8) Delivery Date
  cntctPhone nVarChar(20) Contact Phone
  street nVarChar(100) Street
  block nVarChar(100) Block
  zip nVarChar(20) Zip Code
  city nVarChar(100) City
  county nVarChar(100) County
  country nVarChar(3) Country/Region ->OCRY
  state nVarChar(3) State ->OCST
  instLction nVarChar(254) Installation Location
  contract Int(11) Contract ->OCTR
  cntrctStrt Date(8) Contract Start Date
  cntrctEnd Date(8) Contract End Date
  attachment Text(16) Attachments
  objType nVarChar(20) Object Type default=176
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date
  userSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Update Date
  Building Text(16) Building/Floor/Room
  status VarChar(1) Status default=A [A=Active, R=Returned, T=Terminated, L=Loaned, I=In Repair Lab]
  replcIns Int(11) The CEC this replaced ->OINS
  repByIns Int(11) The CEC this is replaced by ->OINS
  technician Int(11) Default Technician ->OHEM
  territory Int(11) Default Territory ->OTER
  AtcEntry Int(11) Attachment Entry ->OATC
  Transfered VarChar(1) Year Transfer default=N
  AddrType nVarChar(100) Address Type
  Instance Int(6) Instance default=0
  StreetNo nVarChar(100) Street No.
  BPType VarChar(1) BP Type default=R [R=Sales, P=Purchasing, B=Sales & Purchasing]
  OwnerCode Int(11) Equipment Card Owner ->OHEM
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV

# ANS1 - Customer Equipment Card - Multiple Business Partners - History
Module: Service | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: InsID, BpCode, LogInstanc
Fields (name type(len) description [values] ->parent table):
  InsID Int(11) Equipment Card No. ->OINS
  BpCode nVarChar(15) BP Code ->OCRD
  LogInstanc Int(11) Log Instance default=0

# ASC1 - Service Call Solutions - History
Module: Service | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: srvcCallID, line, logInstanc
Fields (name type(len) description [values] ->parent table):
  srvcCallID Int(11) Service Call No. - History ->OSCL
  line Int(6) Row Number - History default=-1
  solutionID Int(11) Solution ID - History ->OSLT
  objType nVarChar(20) Object Type - History default=191
  logInstanc Int(11) Log Instance - History
  userSign Int(6) Creating User - History ->OUSR
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  VisOredr Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV

# ASC2 - Service Call Inventory Expenses - History
Module: Service | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line, LogInstanc
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. - History ->OSCL
  Line Int(6) Row - History default=-1
  ItemCode nVarChar(50) Item No. - History ->OITM
  ItemName nVarChar(200) Item Description - History
  TransToTec Num(19,6) Transfer to Technician - History
  Delivered Num(19,6) Delivered - History
  RetFromTec Num(19,6) Returned from Technician - History
  Returned Num(19,6) Returned - History
  Bill VarChar(1) Bill - History default=Y [Y=Yes, N=No]
  QtyToBill Num(19,6) Quantity to Bill - History
  QtyToInv Num(19,6) Invoiced Qty - History
  ObjectType nVarChar(20) Object Type - History default=191
  LogInstanc Int(11) Log Instance - History
  UserSign Int(6) User Signature - History ->OUSR
  CreateDate Date(8) Creation Date - History
  UserSign2 Int(6) User Signature 2 - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  VisOrder Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV

# ASC3 - Service Call Travel/Labor Expenses - History
Module: Service | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line, LogInstanc
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  ItemCode nVarChar(50) Item Number ->OITM
  ItemName nVarChar(200) Item Description
  HourFrom Int(6) Delivered
  HourTo Int(6) Returned
  Quantity Num(19,6) Quantity
  Bill VarChar(1) Bill default=Y [Y=Yes, N=No]
  QtyToBill Num(19,6) Quantity to Bill
  QtyToInv Num(19,6) Invoiced Qty
  SaleUnits nVarChar(5) Sale Units
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  VisOrder Int(11) Visual Order
  Deliverd Num(19,6) Delivered
  Returned Num(19,6) Returned
  EncryptIV nVarChar(100) Encrypt IV

# ASC4 - Service Call Travel/Labor Expenses - History
Module: Service | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line, PartType, DocAbs, Object, LogInstanc
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  PartType VarChar(1) Part Type default=I [I=Inventory, N=Travel/Labor]
  DocAbs Int(11) Document Internal Number
  Object nVarChar(20) Document Type default=13 [13=A/R Invoice, 15=Delivery, 16=Returns, 67=Inventory Transaction, 14=A/R Credit Memo, 165=A/R Correction Invoice, 0=, 17=Sales Order, 23=Sales Quotation, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 18=A/P Invoice, 19=A/P Credit Memo, 21=Goods Return, 234000032=Goods Return Request, 234000031=Return Request]
  DocPstDate Date(8) Document Posting Date
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  DocNumber Int(11) Document No.
  Transfered VarChar(1) Transfered default=Y [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  StckTrnDir VarChar(1) Inventory Transaction Direction [T=Transfer to Technician, N=Transfer from Technician]
  Instance Int(6) Instance default=0

# ASC5 - Service Call Activities - History
Module: Service | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrvcCallId, Line, LogInstanc
Fields (name type(len) description [values] ->parent table):
  SrvcCallId Int(11) Service Call No. ->OSCL
  Line Int(6) Row No. default=-1
  ClgID Int(11) Activity Code ->OCLG
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  VisOrder Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV

# ASC6 - Service Call Scheduling - History
Module: Service | 52 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line, LogInstanc
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row
  Technician Int(11) Technician ->OHEM
  HandledBy Int(6) Handled by User ->OUSR
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  EndDate Date(8) End Date
  EndTime Int(11) End Time
  Duration Num(19,6) Service Call Duration
  Location Int(6) Location default=-1 ->OCLO
  AddressId nVarChar(50) Address Code
  Address nVarChar(254) Address
  Reminder VarChar(1) Reminder default=N [Y=Yes, N=No]
  RemQty Num(19,6) Reminder Quantity
  DisplInCal VarChar(1) Display in Calendar default=N [Y=Yes, N=No]
  Unsched VarChar(1) Unscheduled Call default=Y [Y=Yes, N=No]
  DurType VarChar(1) Duration UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  RemType VarChar(1) Reminder UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  LogInstanc Int(11) Log Instance default=0
  RemDate Date(8) Reminder Date
  RemSent VarChar(1) Reminder Sent default=N [Y=Yes, N=No]
  RemTime Int(6) Reminder Time
  Street nVarChar(100) Street
  City nVarChar(100) City
  Room nVarChar(50) Room
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country/Region ->OCRY
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  ZipCode nVarChar(20) Zip Code
  Block nVarChar(100) Block
  County nVarChar(100) County
  TaxOffice nVarChar(50) Tax Office
  GlblLocNum nVarChar(50) Global Location Number
  ActualDur Num(19,6) Actual Duration
  ActDurType VarChar(1) Actual Duration UoM default=M [M=Minutes, H=Hours, D=Days]
  Close VarChar(1) Close default=N [Y=Yes, N=No]
  Remark nVarChar(254) Remarks
  AddrTypeBS VarChar(1) Address Type [S=Ship To, B=Bill To]
  SignName nVarChar(100) Signature Name
  SaleOrders nVarChar(100) Sales Orders
  ChkInDate Date(8) Check in Date
  ChkInTime Int(11) Check in Time
  ChkInLoc nVarChar(254) Check in Location
  ChkLontitu nVarChar(14) Check in Longitude
  ChkLatitu nVarChar(13) Check in Latitude
  ChkOutDate Date(8) Check out Date
  ChkOutTime Int(11) Check out Time
  SignData Text(16) Signature Data
  EncryptIV nVarChar(100) Encrypt IV

# ASCL - History
Module: Service | 107 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: callID, logInstanc
Fields (name type(len) description [values] ->parent table):
  callID Int(11) Call ID
  subject nVarChar(254) Subject
  customer nVarChar(15) Business Partner Code ->OCRD
  custmrName nVarChar(100) Business Partner Name
  contctCode Int(11) Contact Person ->OCPR
  manufSN nVarChar(36) Mfr Serial No.
  internalSN nVarChar(36) Serial Number
  contractID Int(11) Contract No.
  cntrctDate Date(8) Contract End Date
  resolDate Date(8) Resolution Date
  resolTime Int(6) Resolution Time
  free_1 VarChar(1) Warranty default=N [Y=Yes, N=No]
  free_2 Date(8) Warranty End Date
  origin Int(6) Origin ->OSCO
  itemCode nVarChar(50) Item Number ->OITM
  itemName nVarChar(200) Item Description
  itemGroup Int(6) Item Group
  status Int(6) Status default=-3 ->OSCS
  priority VarChar(1) Priority default=L [L=Low, M=Medium, H=High]
  callType Int(6) Call Type ->OSCT
  problemTyp Int(6) Problem Type ->OSCP
  assignee Int(6) Handled By ->OUSR
  descrption Text(16) Description
  objType nVarChar(20) Object Type default=191
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date
  createTime Int(6) Creation Time
  closeDate Date(8) Closing Date
  closeTime Int(6) Closing Time
  userSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  SCL1Count Int(11) InternalSCL1Count default=0
  SCL2Count Int(11) InternalSCL2Count default=0
  isEntitled VarChar(1) Entitled for Service default=N [N=Not Entitled, C=Valid contract exists]
  insID Int(11) Install Card No. ->OINS
  technician Int(11) Technician ->OHEM
  resolution Text(16) Resolution
  Scl1NxtLn Int(11) SCL1 Next Line
  Scl2NxtLn Int(11) SCL2 Next Line
  Scl3NxtLn Int(11) SCL3 Next Line
  Scl4NxtLn Int(11) SCL4 Next Line
  Scl5NxtLn Int(11) SCL5 Next Line
  isQueue VarChar(1) Belongs to a Queue default=N [N=No, Y=Yes]
  Queue nVarChar(20) Queue ->OQUE
  resolOnDat Date(8) Resolution on Date
  resolOnTim Int(6) Resolution on Time
  respByDate Date(8) Response by Date
  respByTime Int(6) Response by Time
  respOnDate Date(8) Response on Date
  respOnTime Int(6) Response on Time
  respAssign Int(6) Assigned for Response ->OUSR
  AssignDate Date(8) Assigned Date
  AssignTime Int(6) Assigned Time
  UpdateTime Int(6) Updated Time
  responder Int(6) Responder ->OUSR
  Transfered VarChar(1) Year Transfer default=N
  Instance Int(6) Instance default=0
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator default=' ' ->OPID
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  EndDate Date(8) End Date
  EndTime Int(11) End Time
  Duration Num(19,6) Service Call Duration
  DurType VarChar(1) Duration UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  Reminder VarChar(1) Reminder default=N [Y=Yes, N=No]
  RemQty Num(19,6) Reminder Quantity
  RemType VarChar(1) Reminder UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  RemDate Date(8) Reminder Date
  RemSent VarChar(1) Reminder Sent default=N [Y=Yes, N=No]
  RemTime Int(6) Reminder Time
  Location Int(6) Location default=-1 ->OCLO
  AddrName nVarChar(50) Address Name
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill To]
  Street nVarChar(100) Street
  City nVarChar(100) City
  Room nVarChar(50) Room
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country/Region ->OCRY
  DisplInCal VarChar(1) Display in Calendar default=N [Y=Yes, N=No]
  SupplCode nVarChar(254) Supplementary Code
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  NumAtCard nVarChar(100) Business Partner Ref. No.
  ProSubType Int(6) Problem Subtype ->OPST
  BPType VarChar(1) Business Partner Type default=R [R=Sales, P=Purchasing]
  Telephone nVarChar(50) Phone Number
  BPPhone1 nVarChar(50) BP Phone Number1
  BPPhone2 nVarChar(50) BP Phone Number1
  BPCellular nVarChar(50) BP Mobile Phone Number
  BPFax nVarChar(50) BP Fax Number
  BPShipCode nVarChar(50) BP Ship-to Code
  BPShipAddr nVarChar(254) BP Ship-to Address
  BPBillCode nVarChar(50) BP Bill-to Code
  BPBillAddr nVarChar(254) BP Bill-to Address
  BPTerrit Int(11) Business Partner Territory
  BPE_Mail nVarChar(100) Business Partner E-Mail
  BPProjCode nVarChar(20) Business Partner Project Code ->OPRJ
  BPContact nVarChar(245) BP Contact Person
  OwnerCode Int(11) Service Call Owner ->OHEM
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV
  Printed VarChar(1) Printed default=N
  DataVers Int(11) Data Version default=1

# ASGP - Service Group for Brazil
Module: Service | 6 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LogInstanc
  CODE U: ServiceGrp, LogInstanc
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Service Group ID
  ServiceGrp nVarChar(3) Service Group
  Descrip nVarChar(70) Description
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# CTR1 - Service Contract - Items
Module: Service | 14 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContractID, Line
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No. ->OCTR
  Line Int(11) Row
  ManufSN nVarChar(36) Mfr Serial No.
  InternalSN nVarChar(36) Serial Number
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  ItemGroup Int(6) Item Group ->OITB
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  ItmGrpName nVarChar(20) Item Group Name
  InsID Int(11) Customer Equipment Card ID ->OINS
  TermDate Date(8) Termination Date
  LogInstanc Int(11) Log Instance - History
  EncryptIV nVarChar(100) Encrypt IV

# CTR2 - Service Contract - Recurring Transactions
Module: Service | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContractID, RcpEntry
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No. ->OCTR
  RcpEntry Int(11) Recurring Template Entry ->ORCP
  LogInstanc Int(11) Log Instance - History
  EncryptIV nVarChar(100) Encrypt IV

# INS1 - Customer Equipment Card - Multiple Business Partners
Module: Service | 3 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: InsID, BpCode
Fields (name type(len) description [values] ->parent table):
  InsID Int(11) Equipment Card No. ->OINS
  BpCode nVarChar(15) BP Code ->OCRD
  LogInstanc Int(11) Log Instance default=0

# OAGP - Agent Name
Module: Service | 6 columns | ObjType: 177
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AgentCode
  AGENT_NAME U: AgentName
Fields (name type(len) description [values] ->parent table):
  AgentCode nVarChar(32) Agents
  AgentName nVarChar(50) Agent Name
  Memo nVarChar(50) Description
  Locked VarChar(1) Locked
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR

# OCTR - Service Contracts
Module: Service | 70 columns | ObjType: 190
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: ContractID
Fields (name type(len) description [values] ->parent table):
  ContractID Int(11) Contract No.
  CstmrCode nVarChar(15) Business Partner Code ->OCRD
  CstmrName nVarChar(100) Business Partner Name
  CntctCode Int(11) Contact Person Code ->OCPR
  Owner Int(6) Owner ->OUSR
  Status VarChar(1) Contract Status default=D [A=Approved, F=On Hold, D=Draft, T=Terminated]
  CntrcTmplt nVarChar(20) Contract Template ->OCTT
  CntrcType VarChar(1) Contract Type default=S [C=Business Partner, G=Item Group, S=Serial Number]
  Renewal VarChar(1) Renewal default=N [Y=Yes, N=No]
  RemindVal Int(6) Reminder Time
  RemindUnit VarChar(1) Remind Unit default=D [D=Day(s), W=Week(s), M=Month(s)]
  Duration Int(6) Duration of Coverage
  StartDate Date(8) Start Date
  EndDate Date(8) End Date
  ResponsVal Int(6) Resolution Time
  ResponsUnt VarChar(1) Resolution Unit default=D [D=Day(s), H=Hour(s)]
  Descriptio nVarChar(254) Description
  SrcDocType VarChar(1) Source Document Type default=I [Q=Sales Quotation, O=Sales Order, D=Delivery, I=A/R Invoice]
  DocNum Int(11) Source Document
  MonEnabled VarChar(1) Monday Enabled default=Y [Y=Yes, N=No]
  TueEnabled VarChar(1) Tuesday Enabled default=Y [Y=Yes, N=No]
  WedEnabled VarChar(1) Wednesday Enabled default=Y [Y=Yes, N=No]
  ThuEnabled VarChar(1) Thursday Enabled default=Y [Y=Yes, N=No]
  FriEnabled VarChar(1) Friday Enabled default=Y [Y=Yes, N=No]
  SatEnabled VarChar(1) Saturday Enabled default=Y [Y=Yes, N=No]
  SunEnabled VarChar(1) Sunday Enabled default=Y [Y=Yes, N=No]
  MonStart Int(6) Monday Start default=800
  MonEnd Int(6) Monday End default=1700
  TueStart Int(6) Tuesday Start default=800
  TueEnd Int(6) Tuesday End default=1700
  WedStart Int(6) Wednesday Start default=800
  WedEnd Int(6) Wednesday End default=1700
  ThuStart Int(6) Thursday Start default=800
  ThuEnd Int(6) Thursday End default=1700
  FriStart Int(6) Friday Start default=800
  FriEnd Int(6) Friday End default=1700
  SatStart Int(6) Saturday Start default=0
  SatEnd Int(6) Saturday End default=2359
  SunStrart Int(6) Sunday Start default=0
  SunEnd Int(6) Sunday End default=2359
  InclParts VarChar(1) Include Parts default=N [N=No, Y=Yes]
  InclWork VarChar(1) Include Labor default=N [N=No, Y=Yes]
  InclTravel VarChar(1) Include Travel default=N [N=No, Y=Yes]
  Attachment Text(16) Attachments
  CreateDate Date(8) Creation Date
  Remarks1 Text(16) Template Remarks
  Remarks2 Text(16) Remarks
  RemindFlg VarChar(1) Reminder Sent default=N [Y=Yes, N=No]
  CTR1Count Int(11) CTR1 Counter default=0
  DocEntry Int(11) Linked Document No.
  RemTmDays Int(11) Remind Time in Days
  ResTmHours Int(11) Response Time in Hours
  InclHldays VarChar(1) Include Holidays default=N [N=No, Y=Yes]
  SrvcType VarChar(1) Service Type default=R [R=Regular, W=Warranty]
  TermDate Date(8) Termination Date
  ResponseV Int(6) Response Time
  ResponseU VarChar(1) Response Unit default=H [D=Day(s), H=Hour(s)]
  AtcEntry Int(11) Attachment Entry ->OATC
  Transfered VarChar(1) Year Transfer default=N
  Instance Int(6) Instance default=0
  BPType VarChar(1) BP Type default=R [R=Sales, P=Purchasing]
  OwnerCode Int(11) Service Contract Owner ->OHEM
  UserSign Int(6) User Signature ->OUSR
  ObjType nVarChar(20) Object Type - History default=190
  LogInstanc Int(11) Log Instance - History
  UserSign2 Int(6) Updating User - History ->OUSR
  UpdateDate Date(8) Date of Update - History
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV
  Printed VarChar(1) Printed default=N

# OCTT - Contract Template
Module: Service | 42 columns | ObjType: 170
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TmpltName
Fields (name type(len) description [values] ->parent table):
  TmpltName nVarChar(20) Template Name
  Deleted VarChar(1) Deleted default=N [Y=Yes, N=No]
  Renewal VarChar(1) Renewal default=N [Y=Yes, N=No]
  RemindVal Int(6) Remind Before Renewal
  RemindUnit VarChar(1) Remind Unit default=D [D=Day(s), W=Week(s), M=Month(s)]
  Duration Int(6) Duration of Coverage
  ResponsVal Int(6) Resolution Value
  ResponsUnt VarChar(1) Resolution Unit default=D [D=Day(s), H=Hour(s)]
  Descriptio nVarChar(254) Description
  PriceList Int(6) Price List No.
  CntrctType VarChar(1) Contract Type default=S [C=Customer, G=Item Group, S=Serial Number]
  MonEnabled VarChar(1) Monday Enabled default=Y [Y=Yes, N=No]
  TueEnabled VarChar(1) Tuesday Enabled default=Y [Y=Yes, N=No]
  WedEnabled VarChar(1) Wednesday Enabled default=Y [Y=Yes, N=No]
  ThuEnabled VarChar(1) Thursday Enabled default=Y [Y=Yes, N=No]
  FriEnabled VarChar(1) Friday Enabled default=Y [Y=Yes, N=No]
  SatEnabled VarChar(1) Saturday Enabled default=Y [Y=Yes, N=No]
  SunEnabled VarChar(1) Sunday Enabled default=Y [Y=Yes, N=No]
  MonStart Int(6) Monday Start default=800
  MonEnd Int(6) Monday End default=1700
  TueStart Int(6) Tuesday Start default=800
  TueEnd Int(6) Tuesday End default=1700
  WedStart Int(6) Wednesday Start default=800
  WedEnd Int(6) Wednesday End default=1700
  ThuStart Int(6) Thursday Start default=800
  ThuEnd Int(6) Thursday End default=1700
  FriStart Int(6) Friday Start default=800
  FriEnd Int(6) Friday End default=1700
  SatStart Int(6) Saturday Start default=0
  SatEnd Int(6) Saturday End default=2359
  SunStrart Int(6) Sunday Start default=0
  SunEnd Int(6) Sunday End default=2359
  InclParts VarChar(1) Include Parts default=N [N=No, Y=Yes]
  InclWork VarChar(1) Include Labor default=N [N=No, Y=Yes]
  InclTravel VarChar(1) Include Travel default=N [N=No, Y=Yes]
  Attachment Text(16) Attachments
  CreateDate Date(8) Creation Date
  Remark Text(16) Remarks
  InclHldays VarChar(1) Include Holidays default=N [N=No, Y=Yes]
  ResponseV Int(6) Response Value
  ResponseU VarChar(1) Response Unit default=H [H=Hour(s), D=Day(s)]
  AtcEntry Int(11) Attachment Entry

# OINS - Customer Equipment Card
Module: Service | 56 columns | ObjType: 176
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: insID
  C_ITM_SN_S: customer, itemCode, internalSN, status
  ITM_MNFSN: itemCode, manufSN
  ITM_INTSN: itemCode, internalSN
Fields (name type(len) description [values] ->parent table):
  insID Int(11) Equipment Card No.
  customer nVarChar(15) Business Partner Code ->OCRD
  custmrName nVarChar(100) Business Partner Name
  contactCod Int(11) Contact Person Code ->OCPR
  directCsmr nVarChar(15) Direct Customer
  drctCsmNam nVarChar(100) Direct Customer Name
  manufSN nVarChar(36) Mfr Serial No.
  internalSN nVarChar(36) Serial Number
  warranty VarChar(1) Warranty default=N [Y=Yes, N=No]
  wrrntyStrt Date(8) Warranty Start Date
  wrrntyEnd Date(8) Warranty End Date
  responsVal Int(6) Time Required for Response
  responsUnt VarChar(1) Time Unit default=D [H=Hour(s), D=Day(s)]
  itemCode nVarChar(50) Item No. ->OITM
  itemName nVarChar(200) Item Description
  itemGroup Int(6) Item Group ->OITB
  manufDate Date(8) Manufacture Date
  delivery Int(11) Delivery Key ->ODLN
  deliveryNo Int(11) Delivery Number
  invoice Int(11) Invoice Key ->OINV
  invoiceNum Int(11) Invoice Number
  dlvryDate Date(8) Delivery Date
  cntctPhone nVarChar(20) Contact Phone
  street nVarChar(100) Street
  block nVarChar(100) Block
  zip nVarChar(20) Zip Code
  city nVarChar(100) City
  county nVarChar(100) County
  country nVarChar(3) Country/Region ->OCRY
  state nVarChar(3) State ->OCST
  instLction nVarChar(254) Installation Location
  contract Int(11) Contract ->OCTR
  cntrctStrt Date(8) Contract Start Date
  cntrctEnd Date(8) Contract End Date
  attachment Text(16) Attachments
  objType nVarChar(20) Object Type default=176
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date
  userSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  Building Text(16) Building/Floor/Room
  status VarChar(1) Status default=A [A=Active, R=Returned, T=Terminated, L=Loaned, I=In Repair Lab]
  replcIns Int(11) The CEC this replaced ->OINS
  repByIns Int(11) The CEC this is replaced by ->OINS
  technician Int(11) Default Technician ->OHEM
  territory Int(11) Default Territory ->OTER
  AtcEntry Int(11) Attachment Entry ->OATC
  Transfered VarChar(1) Year Transfer default=N
  AddrType nVarChar(100) Address Type
  Instance Int(6) Instance default=0
  StreetNo nVarChar(100) Street No.
  BPType VarChar(1) BP Type default=R [R=Sales, P=Purchasing, B=Sales & Purchasing]
  OwnerCode Int(11) Equipment Card Owner ->OHEM
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV

# OISR - Service Calls
Module: Service | 10 columns | ObjType: 105
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: RequestNum
Fields (name type(len) description [values] ->parent table):
  RequestNum Int(11) Request No.
  Open_Date Date(8) Start Date
  Open_Time Int(11) Start Time
  Task_Id Int(11) Request No. in SAP Business One
  Contact nVarChar(30) Contact Person
  Phone nVarChar(20) Telephone
  TaskType Int(6) Request Type default=0 [0=Explanation, 1=Error, 2=Complaints]
  Dscription nVarChar(254) Call Description
  Answer Text(16) Troubleshooting
  Status VarChar(1) Call Status default=O [O=Open, C=Closed]

# OQUE - Queue
Module: Service | 5 columns | ObjType: 194
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: queueID
Fields (name type(len) description [values] ->parent table):
  queueID nVarChar(20) Queue ID
  descript nVarChar(200) Description
  manager Int(11) Queue Manager default=0 ->OUSR
  email nVarChar(200) Queue E-Mail
  inactive VarChar(1) Inactive default=N [Y=Yes, N=No]

# ORCI - Recipient List
Module: Service | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Code
  NAME: Name
Fields (name type(len) description [values] ->parent table):
  Code Int(11) Code
  Name nVarChar(30) Name
  Active VarChar(1) Active default=Y [Y=Yes, N=No]
  IsMultiple VarChar(1) Is Mulitple default=N [Y=Yes, N=No]
  DataSource VarChar(1) Data Source default=N [N=Unknown, I=Interface, U=Update, M=Import, O=DI API, S=Service Layer, W=Web Client, A=Doc. Generation Wizard, D=Restore Wizard, P=Partner Implementation, T=Year Transfer]
  UserSign Int(6) User Signature ->OUSR
  UserSign2 nVarChar(6) Updating User ->OUSR

# OREQ - External System Call Request
Module: Service | 9 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Request ID
  Category Int(11) Request Category
  Status VarChar(1) Request Status default=N [N=New, P=In Process, S=Completed, C=Comfirmed, F=Failed]
  CreateDate Date(8) Request Creation Date
  CreateTime Int(11) Request Creation Time
  LstUpdDate Date(8) Latest Update Date
  LstUpdTime Int(11) Latest Update Time
  UserSign nVarChar(8) Latest Update User Code
  Port Int(11) Port

# OSCD - Service Code Table
Module: Service | 5 columns | ObjType: 254
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: County, ServiceCD
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) ID
  County Int(11) County Code ->OCNT
  ServiceCD nVarChar(15) Service Code
  Descrip nVarChar(70) Description
  Incomimg VarChar(1) Is Incomimg(Y/N) default=Y [Y=Incoming, N=Outgoing]

# OSCL - Service Calls
Module: Service | 107 columns | ObjType: 191
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: callID
  NUM U: DocNum, Instance, PIndicator
  SERIES: Series
  REMDATE: RemDate
  REMTIME: RemTime
Fields (name type(len) description [values] ->parent table):
  callID Int(11) Call ID
  subject nVarChar(254) Subject
  customer nVarChar(15) Business Partner Code ->OCRD
  custmrName nVarChar(100) Business Partner Name
  contctCode Int(11) Contact Person ->OCPR
  manufSN nVarChar(36) Mfr Serial No.
  internalSN nVarChar(36) Serial Number
  contractID Int(11) Contract No. ->OCTR
  cntrctDate Date(8) Contract End Date
  resolDate Date(8) Resolution Date
  resolTime Int(6) Resolution Time
  free_1 VarChar(1) Warranty default=N [Y=Yes, N=No]
  free_2 Date(8) Warranty End Date
  origin Int(6) Origin ->OSCO
  itemCode nVarChar(50) Item No. ->OITM
  itemName nVarChar(200) Item Description
  itemGroup Int(6) Item Group ->OITB
  status Int(6) Status default=-3 ->OSCS
  priority VarChar(1) Priority default=L [L=Low, M=Medium, H=High]
  callType Int(6) Call Type ->OSCT
  problemTyp Int(6) Problem Type ->OSCP
  assignee Int(6) Handled By ->OUSR
  descrption Text(16) Description
  objType nVarChar(20) Object Type default=191
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date
  createTime Int(6) Creation Time
  closeDate Date(8) Closing Date
  closeTime Int(6) Closing Time
  userSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  SCL1Count Int(11) InternalSCL1Count default=0
  SCL2Count Int(11) InternalSCL2Count default=0
  isEntitled VarChar(1) Entitle for Service default=N [N=Not Entitled, C=Valid contract exists]
  insID Int(11) Install Card No. ->OINS
  technician Int(11) Technician ->OHEM
  resolution Text(16) Resolution
  Scl1NxtLn Int(11) SCL1 Next Line
  Scl2NxtLn Int(11) SCL2 Next Line
  Scl3NxtLn Int(11) SCL3 Next Line
  Scl4NxtLn Int(11) SCL4 Next Line
  Scl5NxtLn Int(11) SCL5 Next Line
  isQueue VarChar(1) Belongs to a Queue default=N [N=No, Y=Yes]
  Queue nVarChar(20) Queue ->OQUE
  resolOnDat Date(8) Resolution on Date
  resolOnTim Int(6) Resolution on Time
  respByDate Date(8) Response by Date
  respByTime Int(6) Response by Time
  respOnDate Date(8) Response on Date
  respOnTime Int(6) Response on Time
  respAssign Int(6) Assigned for Response ->OUSR
  AssignDate Date(8) Assigned Date
  AssignTime Int(6) Assigned Time
  UpdateTime Int(6) Updated Time
  responder Int(6) Responder ->OUSR
  Transfered VarChar(1) Year Transfer default=N
  Instance Int(6) Instance default=0
  DocNum Int(11) Document Number
  Series Int(11) Series ->NNM1
  Handwrtten VarChar(1) Manual Numbering default=N [Y=Yes, N=No]
  PIndicator nVarChar(10) Period Indicator default=' ' ->OPID
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  EndDate Date(8) End Date
  EndTime Int(11) End Time
  Duration Num(19,6) Service Call Duration
  DurType VarChar(1) Duration UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  Reminder VarChar(1) Reminder default=N [Y=Yes, N=No]
  RemQty Num(19,6) Reminder Quantity
  RemType VarChar(1) Reminder UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  RemDate Date(8) Reminder Date
  RemSent VarChar(1) Reminder Sent default=N [Y=Yes, N=No]
  RemTime Int(6) Reminder Time
  Location Int(6) Location default=-1 ->OCLO
  AddrName nVarChar(50) Address Name
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill To]
  Street nVarChar(100) Street
  City nVarChar(100) City
  Room nVarChar(50) Room
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country/Region ->OCRY
  DisplInCal VarChar(1) Display in Calendar default=N [Y=Yes, N=No]
  SupplCode nVarChar(254) Supplementary Code
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  NumAtCard nVarChar(100) Business Partner Ref. No.
  ProSubType Int(6) Problem Subtype ->OPST
  BPType VarChar(1) Business Partner Type default=R [R=Sales, P=Purchasing]
  Telephone nVarChar(50) Phone Number
  BPPhone1 nVarChar(50) BP Phone Number1
  BPPhone2 nVarChar(50) BP Phone Number1
  BPCellular nVarChar(50) BP Mobile Phone Number
  BPFax nVarChar(50) BP Fax Number
  BPShipCode nVarChar(50) BP Ship-to Code
  BPShipAddr nVarChar(254) BP Ship-to Address
  BPBillCode nVarChar(50) BP Bill-to Code
  BPBillAddr nVarChar(254) BP Bill-to Address
  BPTerrit Int(11) Business Partner Territory
  BPE_Mail nVarChar(100) Business Partner E-Mail
  BPProjCode nVarChar(20) Business Partner Project Code ->OPRJ
  BPContact nVarChar(245) BP Contact Person
  OwnerCode Int(11) Service Call Owner ->OHEM
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
  EncryptIV nVarChar(100) Encrypt IV
  Printed VarChar(1) Printed default=N
  DataVers Int(11) Data Version default=1

# OSCO - Service Call Origins
Module: Service | 5 columns | ObjType: 192
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: originID
Fields (name type(len) description [values] ->parent table):
  originID Int(6) Origin ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Locked VarChar(1) Locked
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# OSCP - Service Call Problem Types
Module: Service | 4 columns | ObjType: 169
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: prblmTypID
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  prblmTypID Int(6) Problem Type ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# OSCS - Service Call Statuses
Module: Service | 5 columns | ObjType: 167
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: statusID
  NAME: Name
Fields (name type(len) description [values] ->parent table):
  statusID Int(6) Status ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Locked VarChar(1) Locked
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# OSCT - Service Call Types
Module: Service | 4 columns | ObjType: 168
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: callTypeID
  NAME U: Name
Fields (name type(len) description [values] ->parent table):
  callTypeID Int(6) Call Type ID
  Name nVarChar(20) Name
  Descriptio Text(16) Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# OSGP - Service Group for Brazil
Module: Service | 6 columns | ObjType: 255
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry
  CODE U: ServiceGrp
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Service Group ID
  ServiceGrp nVarChar(3) Service Group
  Descrip nVarChar(70) Description
  LogInstanc Int(11) Log Instance default=0
  UserSign2 Int(6) Updating User ->OUSR
  UpdateDate Date(8) Update Date

# OSLT - Service Call Solutions
Module: Service | 17 columns | ObjType: 189
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SltCode
Fields (name type(len) description [values] ->parent table):
  SltCode Int(11) Solution Code
  ItemCode nVarChar(50) Item No. ->OITM
  StatusNum Int(11) Status ->OSST
  Owner Int(11) Owner ->OUSR
  CreatedBy Int(11) Created By ->OUSR
  DateCreate Date(8) Creation Date
  UpdateBy Int(11) Last Update by ->OUSR
  DateUpdate Date(8) Last Update Date
  Subject nVarChar(254) Subject
  Symptom nVarChar(254) Symptom
  Cause nVarChar(254) Cause
  Descriptio Text(16) Description
  Attachment Text(16) Attachments
  AtcEntry Int(11) Attachment Entry
  Transfered VarChar(1) Year Transfer default=N
  Instance Int(6) Instance default=0
  DataVers Int(11) Data Version default=1

# OSST - Service Call Solution Statuses
Module: Service | 4 columns | ObjType: 188
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Number
  NAME: Name
Fields (name type(len) description [values] ->parent table):
  Number Int(11) Number
  Name nVarChar(20) Name
  Descriptio nVarChar(254) Description
  Active VarChar(1) Active default=Y [Y=Yes, N=No]

# QUE1 - Queue Members
Module: Service | 2 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: queueID, member
Fields (name type(len) description [values] ->parent table):
  queueID nVarChar(20) Queue ID ->OQUE
  member Int(11) Member Name ->OUSR

# QUE2 - Queue Elements
Module: Service | 7 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: queueID, elementNum
  OBJ_ELEM U: queueID, objType, elementId
Fields (name type(len) description [values] ->parent table):
  queueID nVarChar(20) Queue ID ->OQUE
  objType nVarChar(20) Object Type
  elementId Int(11) Element ID
  elementNum Int(11) Element Number
  priority Int(11) Priority
  createDate Date(8) Creation Date
  createTime Int(6) Creation Time

# REQ1 - External System Call Request - Message List
Module: Service | 8 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Request ID ->OREQ
  LineId Int(11) Message Line ID
  MsgType VarChar(1) Message Type default=I [I=Information, W=Warning, E=Error]
  ErrCode nVarChar(3) Error Code
  MsgBody Text(16) Message Body
  Status VarChar(1) Message Status default=U [U=Unread, R=Read]
  MsgDate Date(8) Message Log Date
  MsgTime Int(11) Message Log Time

# REQ2 - External System Call Request - Argument List
Module: Service | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId, ArgName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Request ID ->OREQ
  LineId Int(11) Message Line ID default=1
  ArgName nVarChar(20) Argument Name
  ArgValue nVarChar(254) Argument Value

# REQ3 - External System Call Request - Message Argument List
Module: Service | 4 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: AbsEntry, LineId, ArgName
Fields (name type(len) description [values] ->parent table):
  AbsEntry Int(11) Request ID ->OREQ
  LineId Int(11) Message Line ID ->REQ1
  ArgName nVarChar(20) Argument Name
  ArgValue nVarChar(254) Argument Value

# SCL1 - Service Call Solutions - Rows
Module: Service | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: srvcCallID, line
Fields (name type(len) description [values] ->parent table):
  srvcCallID Int(11) Service Call No. ->OSCL
  line Int(6) Row No. default=-1
  solutionID Int(11) Solution ID ->OSLT
  objType nVarChar(20) Object Type default=191
  logInstanc Int(11) Log Instance
  userSign Int(6) Creating User ->OUSR
  createDate Date(8) Creation Date
  userSign2 Int(6) Updating User ->OUSR
  updateDate Date(8) Date of Update
  VisOredr Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV

# SCL2 - Service Call Inventory Expenses
Module: Service | 19 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  TransToTec Num(19,6) Transfer to Technican
  Delivered Num(19,6) Delivered
  RetFromTec Num(19,6) Returned from Technician
  Returned Num(19,6) Returned
  Bill VarChar(1) Bill default=Y [Y=Yes, N=No]
  QtyToBill Num(19,6) Quantity to Bill
  QtyToInv Num(19,6) Invoiced Qty
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  VisOrder Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV

# SCL3 - Service Call Travel/Labor Expenses
Module: Service | 21 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  ItemCode nVarChar(50) Item No. ->OITM
  ItemName nVarChar(200) Item Description
  HourFrom Int(6) Delivered
  HourTo Int(6) Returned
  Quantity Num(19,6) Quantity
  Bill VarChar(1) Bill default=Y [Y=Yes, N=No]
  QtyToBill Num(19,6) Quantity to Bill
  QtyToInv Num(19,6) Invoiced Qty
  SaleUnits nVarChar(5) Sale Units
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  VisOrder Int(11) Visual Order
  Deliverd Num(19,6) Delivered
  Returned Num(19,6) Returned
  EncryptIV nVarChar(100) Encrypt IV

# SCL4 - Expense Documents
Module: Service | 17 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line, PartType, DocAbs, Object
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  PartType VarChar(1) Part Type default=I [I=Inventory, N=Travel/Labor]
  DocAbs Int(11) Document Internal Number
  Object nVarChar(20) Document Type default=13 [13=A/R Invoice, 15=Delivery, 16=Returns, 67=Inventory Transfer, 14=A/R Credit Memo, 165=A/R Correction Invoice, 0=, 17=Sales Order, 23=Sales Quotation, 540000006=Purchase Quotation, 22=Purchase Order, 20=Goods Receipt PO, 18=A/P Invoice, 19=A/P Credit Memo, 21=Goods Return, 234000032=Goods Return Request, 234000031=Return Request]
  DocPstDate Date(8) Document Posting Date
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  DocNumber Int(11) Document No.
  Transfered VarChar(1) Transfered default=Y [Y=Yes, N=No]
  VisOrder Int(11) Visual Order
  StckTrnDir VarChar(1) Inventory Transaction Direction [T=Transfer to Technician, N=Transfer from Technician]
  Instance Int(6) Instance default=0

# SCL5 - Service Call Activities
Module: Service | 11 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrvcCallId, Line
Fields (name type(len) description [values] ->parent table):
  SrvcCallId Int(11) Service Call No. ->OSCL
  Line Int(6) Row default=-1
  ClgID Int(11) Activity Code ->OCLG
  ObjectType nVarChar(20) Object Type default=191
  LogInstanc Int(11) Log Instance
  UserSign Int(6) User Signature ->OUSR
  CreateDate Date(8) Creation Date
  UserSign2 Int(6) User Signature 2 ->OUSR
  UpdateDate Date(8) Date of Update
  VisOrder Int(11) Visual Order
  EncryptIV nVarChar(100) Encrypt IV

# SCL6 - Service Call Scheduling
Module: Service | 52 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: SrcvCallID, Line
Fields (name type(len) description [values] ->parent table):
  SrcvCallID Int(11) Service Call No. ->OSCL
  Line Int(6) Row
  Technician Int(11) Technician ->OHEM
  HandledBy Int(6) Handled by User ->OUSR
  StartDate Date(8) Start Date
  StartTime Int(11) Start Time
  EndDate Date(8) End Date
  EndTime Int(11) End Time
  Duration Num(19,6) Service Call Duration
  Location Int(6) Location default=-1 ->OCLO
  AddressId nVarChar(50) Address Code
  Address nVarChar(254) Address
  Reminder VarChar(1) Reminder default=N [Y=Yes, N=No]
  RemQty Num(19,6) Reminder Quantity
  DisplInCal VarChar(1) Display in Calendar default=N [Y=Yes, N=No]
  Unsched VarChar(1) Unscheduled Call default=Y [Y=Yes, N=No]
  DurType VarChar(1) Duration UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  RemType VarChar(1) Reminder UoM default=M [S=Seconds, M=Minutes, H=Hours, D=Days]
  LogInstanc Int(11) Log Instance default=0
  RemDate Date(8) Reminder Date
  RemSent VarChar(1) Reminder Sent default=N [Y=Yes, N=No]
  RemTime Int(6) Reminder Time
  Street nVarChar(100) Street
  City nVarChar(100) City
  Room nVarChar(50) Room
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country/Region ->OCRY
  Address2 nVarChar(50) Address Name 2
  Address3 nVarChar(50) Address Name 3
  AddrType nVarChar(100) Address Type
  StreetNo nVarChar(100) Street No.
  ZipCode nVarChar(20) Zip Code
  Block nVarChar(100) Block
  County nVarChar(100) County
  TaxOffice nVarChar(50) Tax Office
  GlblLocNum nVarChar(50) Global Location Number
  ActualDur Num(19,6) Actual Duration
  ActDurType VarChar(1) Actual Duration UoM default=M [M=Minutes, H=Hours, D=Days]
  Close VarChar(1) Close default=N [Y=Yes, N=No]
  Remark nVarChar(254) Remarks
  AddrTypeBS VarChar(1) Address Type [S=Ship To, B=Bill To]
  SignName nVarChar(100) Signature Name
  SaleOrders nVarChar(100) Sales Orders
  ChkInDate Date(8) Check in Date
  ChkInTime Int(11) Check in Time
  ChkInLoc nVarChar(254) Check in Location
  ChkLontitu nVarChar(14) Check in Longitude
  ChkLatitu nVarChar(13) Check in Latitude
  ChkOutDate Date(8) Check out Date
  ChkOutTime Int(11) Check out Time
  SignData Text(16) Signature Data
  EncryptIV nVarChar(100) Encrypt IV

# SCL7 - Service Call BP Address
Module: Service | 67 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: DocEntry
Fields (name type(len) description [values] ->parent table):
  DocEntry Int(11) Document Internal ID ->OSCL
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
  State nVarChar(3) State Code
  County nVarChar(7) County Code
  Incoterms nVarChar(3) Incoterms
  Vehicle nVarChar(10) Vehicle ID
  VidState nVarChar(3) Vehicle ID (State)
  NfRef nVarChar(254) NF Reference
  Carrier nVarChar(15) Carrier Code ->OCRD
  QoP Int(11) Quantity of Packs
  PackDesc nVarChar(10) Pack Description
  Brand nVarChar(20) Brand
  NoSU Int(11) Number of Shipping Unit
  NetWeight Num(19,6) Net Weight
  GrsWeight Num(19,6) Gross Weight
  LogInstanc Int(11) Log Instance default=0
  ObjectType nVarChar(20) Object Type default=191 ->ADP1
  TaxId10 nVarChar(100) Tax ID 10
  TransCat nVarChar(100) Transaction Category
  FormNo nVarChar(100) Form No.
  TaxId11 nVarChar(100) Tax ID 11
  StreetS nVarChar(100) Street
  BlockS nVarChar(100) Block
  BuildingS Text(16) Building/Floor/Room
  CityS nVarChar(100) City
  ZipCodeS nVarChar(20) Zip Code
  CountyS nVarChar(100) County
  StateS nVarChar(3) State ->OCST
  CountryS nVarChar(3) Country/Region ->OCRY
  AddrTypeS nVarChar(100) Address Type
  StreetNoS nVarChar(100) Street No.
  StreetB nVarChar(100) Street
  BlockB nVarChar(100) Block
  BuildingB Text(16) Building/Floor/Room
  CityB nVarChar(100) City
  ZipCodeB nVarChar(20) Zip Code
  CountyB nVarChar(100) County
  StateB nVarChar(3) State ->OCST
  CountryB nVarChar(3) Country/Region ->OCRY
  AddrTypeB nVarChar(100) Address Type
  StreetNoB nVarChar(100) Street No.
  ImpORExp VarChar(1) Import or Export [N=, Y=]
  Vat VarChar(1) VAT default=N [N=No VAT Support, Y=VAT Support]
  AltCrdNamB nVarChar(100) Alternative BP Name
  AltTaxIdB nVarChar(32) Alternative Tax ID
  Address2S nVarChar(50) Address Name 2
  Address3S nVarChar(50) Address Name 3
  Address2B nVarChar(50) Address Name 2
  Address3B nVarChar(50) Address Name 3
  MainUsage Int(11) Main Usage Code of Document ->OUSG
  GlbLocNumS nVarChar(50) Global Location Number
  GlbLocNumB nVarChar(50) Global Location Number
  CollectDT nVarChar(20) Date and Time of Collection
  TransprtDT Date(8) Transport Starting Date
  TransprtRS nVarChar(100) Transport Reason
  TaxId12 nVarChar(50) Tax ID 12
  TaxId13 nVarChar(100) Deductee Ref. No. in India
  EncryptIV nVarChar(100) Encrypt IV
