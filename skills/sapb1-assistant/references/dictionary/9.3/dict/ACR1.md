<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# ACR1 - Business Partner Addresses - History
Module: Business Partners | 32 columns
Indexes (name: columns; first = primary key; U = unique):
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
