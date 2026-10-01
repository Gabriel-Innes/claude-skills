<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ASCL - History
Module: Service | 104 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: logInstanc, callID
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
  itemName nVarChar(100) Item Description
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
  PIndicator nVarChar(10) Period Indicator ->OPID
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
  AddrType VarChar(1) Address Type default=S [S=Ship To, B=Bill to]
  Street nVarChar(100) Street
  City nVarChar(100) City
  Room nVarChar(50) Room
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country ->OCRY
  DisplInCal VarChar(1) Display in Calendar default=N [Y=Yes, N=No]
  SupplCode nVarChar(254) Supplementary Code
  Attachment Text(16) Attachment
  AtcEntry Int(11) Attachment Entry
  NumAtCard nVarChar(100) Business Partner Ref. No.
  ProSubType Int(6) Problem Subtype ->OPST
  BPType VarChar(1) BP Type default=R [R=Sales, P=Purchasing]
  Telephone nVarChar(50) Phone Number
  BPPhone1 nVarChar(20) BP Phone Number1
  BPPhone2 nVarChar(20) BP Phone Number1
  BPCellular nVarChar(50) BP Mobile Phone Number
  BPFax nVarChar(20) BP Fax Number
  BPShipCode nVarChar(50) BP Ship-to Code
  BPShipAddr nVarChar(254) BP Ship-to Address
  BPBillCode nVarChar(50) BP Bill-to Code
  BPBillAddr nVarChar(254) BP Bill-to Address
  BPTerrit Int(11) BP Territory
  BPE_Mail nVarChar(100) BP E-Mail
  BPProjCode nVarChar(20) BP Project Code
  BPContact nVarChar(245) BP Contact Person
  OwnerCode Int(11) Service Call Owner ->OHEM
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased]
