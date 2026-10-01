<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# SCL6 - Service Call Scheduling
Module: Service | 51 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: Line, SrcvCallID
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
  Country nVarChar(3) Country ->OCRY
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
  AddrTypeBS VarChar(1) Address Type [S=Ship To, B=Bill to]
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
