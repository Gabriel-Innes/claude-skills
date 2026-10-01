<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# TGG1 - Target Group Details
Module: Business Partners | 32 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: TargetCode, LineNum
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
  Telephone nVarChar(50) Telephone
  Cellolar nVarChar(50) Mobile Phone
  Fax nVarChar(50) Fax
  Address nVarChar(100) Address
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  City nVarChar(100) City
  ZipCode nVarChar(20) Zip Code
  County nVarChar(100) County
  State nVarChar(3) State ->OCST
  Country nVarChar(3) Country/Region ->OCRY
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
