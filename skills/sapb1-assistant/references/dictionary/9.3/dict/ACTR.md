<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACTR - Service Contracts
Module: Service | 68 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: LogInstanc, ContractID
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
