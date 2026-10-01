<!-- source: REFDB.chm (SAP Business One SDK 10.0 - Database Tables Reference) | version: SAP Business One 10.0 | verified: 2026-10-01 -->
# ACR1 - Business Partner Addresses - History
Module: Business Partners | 38 columns
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: CardCode, Address, AdresType, LogInstanc
Fields (name type(len) description [values] ->parent table):
  Address nVarChar(50) Address Name
  CardCode nVarChar(15) BP Code ->ACRD
  Street nVarChar(100) Street
  Block nVarChar(100) Block
  ZipCode nVarChar(20) Zip Code
  City nVarChar(100) City
  County nVarChar(100) County
  Country nVarChar(3) Country/Region ->OCRY
  State nVarChar(3) State ->OCST
  UserSign Int(6) User Signature ->OUSR
  LogInstanc Int(11) Log Instance default=0
  ObjType nVarChar(20) Object Type default=2 ->ADP1
  LicTradNum nVarChar(32) Federal Tax ID
  LineNum Int(11) Row No.
  TaxCode nVarChar(8) Tax Code ->OSTC
  Building Text(16) Building/Floor/Room
  AdresType VarChar(1) Address Type default=S [S=Ship To, B=Bill To]
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
  EncryptIV nVarChar(100) Encrypt IV
  MYFType nVarChar(2) MYF Type [S1=MYF Wholesale Sales, S2=Retail Sales, P1=MYF Wholesale Purchases, P3=Other Expense Transactions]
  VatResDate Date(8) VAT Verfication Response Date
  VatResCode Int(11) VAT Verfication Response Code ->ORVC
  VatResName nVarChar(254) VAT Verfication Response Name
  VatResAddr nVarChar(254) VAT Verfication Response Addr
